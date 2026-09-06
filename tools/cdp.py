"""Minimal CDP client over a stdlib websocket. No deps."""
import json, os, socket, struct, base64, hashlib, subprocess, time, urllib.request

PORT = int(os.environ.get("CDP_PORT", "9333"))
PROFILE = "/tmp/crls-cdp-profile"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def launch(width=2560, height=1440):
    subprocess.run(["pkill", "-f", "crls-cdp-profile"], capture_output=True)
    time.sleep(0.6)
    os.makedirs(PROFILE, exist_ok=True)
    subprocess.Popen([
        CHROME, "--headless=new", f"--remote-debugging-port={PORT}",
        f"--user-data-dir={PROFILE}", "--no-first-run", "--no-default-browser-check",
        "--disable-extensions", "--hide-scrollbars", "--force-device-scale-factor=1",
        "--enable-unsafe-swiftshader", "--use-gl=angle", "--use-angle=swiftshader",
        f"--window-size={width},{height}", "about:blank",
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(80):
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json/version", timeout=1).read()
            return True
        except Exception:
            time.sleep(0.35)
    raise RuntimeError("chrome did not come up")


class WS:
    def __init__(self, url):
        _, rest = url.split("://", 1)
        hostport, path = rest.split("/", 1)
        host, port = hostport.split(":")
        self.s = socket.create_connection((host, int(port)), timeout=45)
        key = base64.b64encode(os.urandom(16)).decode()
        req = (f"GET /{path} HTTP/1.1\r\nHost: {hostport}\r\nUpgrade: websocket\r\n"
               f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\n"
               f"Sec-WebSocket-Version: 13\r\n\r\n")
        self.s.sendall(req.encode())
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += self.s.recv(4096)
        self.buf = buf.split(b"\r\n\r\n", 1)[1]
        self.mid = 0

    def _recv(self, n):
        while len(self.buf) < n:
            chunk = self.s.recv(65536)
            if not chunk:
                raise RuntimeError("socket closed")
            self.buf += chunk
        out, self.buf = self.buf[:n], self.buf[n:]
        return out

    def send(self, payload: bytes):
        hdr = bytearray([0x81])
        n = len(payload)
        mask = os.urandom(4)
        if n < 126:
            hdr.append(0x80 | n)
        elif n < 65536:
            hdr.append(0x80 | 126); hdr += struct.pack(">H", n)
        else:
            hdr.append(0x80 | 127); hdr += struct.pack(">Q", n)
        hdr += mask
        hdr += bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
        self.s.sendall(bytes(hdr))

    def recv(self):
        while True:
            b0, b1 = self._recv(2)
            op = b0 & 0x0F
            ln = b1 & 0x7F
            if ln == 126:
                ln = struct.unpack(">H", self._recv(2))[0]
            elif ln == 127:
                ln = struct.unpack(">Q", self._recv(8))[0]
            data = self._recv(ln)
            if op == 1:
                return data.decode("utf-8", "replace")
            if op == 8:
                raise RuntimeError("ws closed")

    def call(self, method, **params):
        self.mid += 1
        mid = self.mid
        self.send(json.dumps({"id": mid, "method": method, "params": params}).encode())
        while True:
            msg = json.loads(self.recv())
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})


def connect():
    tabs = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json").read())
    page = [t for t in tabs if t["type"] == "page"][0]
    return WS(page["webSocketDebuggerUrl"])


def new_page(ws, url, width, height, wait=3.0, scroll_all=True):
    ws.call("Emulation.setDeviceMetricsOverride", width=width, height=height,
            deviceScaleFactor=1, mobile=False)
    ws.call("Page.enable")
    ws.call("Runtime.enable")
    ws.call("Page.navigate", url=url)
    time.sleep(wait)
    if scroll_all:
        # walk the whole page so scroll-driven reveals fire, then return to top
        ev(ws, """(async()=>{const H=document.body.scrollHeight;
          for(let y=0;y<H;y+=400){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,16));}
          window.scrollTo(0,0);await new Promise(r=>setTimeout(r,400));return H;})()""", awaitp=True)
        time.sleep(1.0)
    return ev(ws, "location.href")


def ev(ws, expr, awaitp=False):
    r = ws.call("Runtime.evaluate", expression=expr, returnByValue=True,
                awaitPromise=awaitp, userGesture=True)
    if "exceptionDetails" in r:
        return {"__error": str(r["exceptionDetails"].get("exception", {}).get("description"))[:400]}
    return r.get("result", {}).get("value")


def shot(ws, path, full=False):
    kw = {"format": "png", "captureBeyondViewport": bool(full)}
    r = ws.call("Page.captureScreenshot", **kw)
    with open(path, "wb") as f:
        f.write(base64.b64decode(r["data"]))
    return path
