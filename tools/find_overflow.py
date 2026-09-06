"""Find which element actually overflows the viewport at a given width."""
import sys, json, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import cdp  # noqa: E402

URL = sys.argv[1] if len(sys.argv) > 1 else "https://emilioaitest-hash.github.io/crls-crew/"
W, H = 390, 844

cdp.launch(W, H)
c = cdp.connect()
print("loaded:", cdp.new_page(c, URL, W, H, wait=6.0, scroll_all=True))

EXPR = r"""
(() => {
  const vw = document.documentElement.clientWidth;
  const bad = [];
  document.querySelectorAll('*').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) return;
    const right = r.right + window.scrollX;
    if (right > vw + 1) {
      bad.push({
        tag: el.tagName.toLowerCase(),
        cls: (el.className && el.className.toString ? el.className.toString() : '').slice(0, 48),
        id: el.id || '',
        w: Math.round(r.width),
        right: Math.round(right),
        over: Math.round(right - vw),
      });
    }
  });
  // widest offenders first, and drop children whose parent is already listed
  bad.sort((a, b) => b.over - a.over);
  return { vw, docW: document.documentElement.scrollWidth, count: bad.length, worst: bad.slice(0, 18) };
})()
"""
print(json.dumps(cdp.ev(c, EXPR), indent=1))
