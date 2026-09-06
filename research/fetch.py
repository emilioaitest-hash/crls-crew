#!/usr/bin/env python3
"""Cached fetcher for row2k / other rowing result pages. Stdlib only."""
import os, re, sys, time, hashlib, subprocess, json

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
os.makedirs(CACHE, exist_ok=True)

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def cache_path(url):
    h = hashlib.sha1(url.encode()).hexdigest()[:20]
    return os.path.join(CACHE, h + ".html")

def fetch(url, force=False, sleep=0.25):
    p = cache_path(url)
    if os.path.exists(p) and not force and os.path.getsize(p) > 200:
        return open(p, encoding="utf-8", errors="replace").read()
    for attempt in range(3):
        try:
            out = subprocess.run(
                ["curl", "-sL", "--compressed", "--max-time", "45",
                 "-A", UA, url],
                capture_output=True, timeout=60)
            txt = out.stdout.decode("utf-8", errors="replace")
            if len(txt) > 200:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(txt)
                time.sleep(sleep)
                return txt
        except Exception as e:
            pass
        time.sleep(1.5 * (attempt + 1))
    return ""

# ---------- HTML helpers ----------
TAG = re.compile(r"<[^>]+>")
def strip_tags(s):
    s = re.sub(r"(?is)<script.*?</script>", " ", s)
    s = re.sub(r"(?is)<style.*?</style>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</(tr|p|div|h\d|table)>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", "\t", s)
    s = TAG.sub("", s)
    s = (s.replace("&nbsp;", " ").replace("&amp;", "&").replace("&#39;", "'")
          .replace("&quot;", '"').replace("&rsquo;", "'").replace("&lsquo;", "'")
          .replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&ndash;", "-")
          .replace("&mdash;", "-").replace("&lt;", "<").replace("&gt;", ">")
          .replace("&#8217;", "'").replace("&eacute;","e"))
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s

CRLS_PATTERNS = [
    r"\bCRLS\b", r"Cambridge\s+Rindge", r"Cambridge\s+R\s*&\s*L",
    r"Cambridge\s+R&L", r"Rindge\s*&?\s*and?\s*Latin", r"\bC\.?R\.?L\.?S\.?\b",
]
CRLS_RE = re.compile("|".join(CRLS_PATTERNS), re.I)

def has_crls(text):
    return bool(CRLS_RE.search(text))

if __name__ == "__main__":
    print(fetch(sys.argv[1])[:2000])
