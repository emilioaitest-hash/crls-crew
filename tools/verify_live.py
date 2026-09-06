"""
Independent verification of the live deployed site, using the headless CDP
client the round-3 critic wrote. This does NOT touch the user's Chrome and does
not need the remote-debugging prompt, because it launches its own instance on a
throwaway profile.

Usage:  python3 tools/verify_live.py [width] [height]
"""
import sys, json, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import cdp  # noqa: E402

URL = "https://emilioaitest-hash.github.io/crls-crew/"

W = int(sys.argv[1]) if len(sys.argv) > 1 else 1600
H = int(sys.argv[2]) if len(sys.argv) > 2 else 900

cdp.launch(W, H)
c = cdp.connect()
href = cdp.new_page(c, URL, W, H, wait=6.0, scroll_all=True)
print("loaded:", href)

CHECKS = r"""
(() => {
  const out = {};
  out.href = location.href;

  // --- content correctness ---
  out.years = [...document.querySelectorAll('.tl-year')].map(e => e.textContent);
  out.dupe2000 = out.years.filter(y => y === '2000').length;
  out.has1903 = document.body.innerText.includes('5:33');
  out.boatName = (document.querySelector('.boat-name') || {}).textContent || null;
  out.seldon = document.body.innerText.includes('Seldon');
  out.fleet = [...document.querySelectorAll('#fleet-roster .boat b')].map(e => e.textContent);
  out.roadRows = document.querySelectorAll('.road li').length;
  out.counters = [...document.querySelectorAll('[data-count]')].map(e => e.textContent);

  // --- glyph-area density: the measurement that mattered in R3 ---
  const inkOf = (el) => {
    if (!el) return 0;
    const r = document.createRange(); r.selectNodeContents(el);
    return [...r.getClientRects()].reduce((a, c) => a + c.width * c.height, 0);
  };
  const rows = [...document.querySelectorAll('.tl-item')];
  const dens = (sel) => rows.map(r => {
    const e = r.querySelector(sel); if (!e) return null;
    const b = e.getBoundingClientRect();
    return b.width * b.height ? inkOf(e) / (b.width * b.height) : null;
  }).filter(v => v !== null);
  const mean = a => a.length ? +(a.reduce((x, y) => x + y, 0) / a.length * 100).toFixed(1) : null;
  out.asideDensity = mean(dens('.tl-aside'));
  out.bodyDensity = mean(dens('.tl-body'));

  // --- leader rule gone? ---
  const dd = document.querySelector('.facts dd');
  out.ddBorder = dd ? getComputedStyle(dd).borderBottomWidth : null;
  out.ddAlign = dd ? getComputedStyle(dd).textAlign : null;

  // --- right-edge alignment ---
  const right = (s) => { const e = document.querySelector(s); return e ? Math.round(e.getBoundingClientRect().right) : null; };
  out.rightEdges = {
    timeline: right('.timeline'), split: right('.split'), chart: right('#chart'),
    stage: right('.boat-stage'), foot: right('.foot-inner'),
  };
  out.edgesAgree = new Set(Object.values(out.rightEdges).filter(Boolean)).size === 1;

  // --- contrast ---
  const lum = (rgb) => { const v = rgb.match(/\d+/g).slice(0, 3).map(n => { let x = n / 255; return x <= 0.03928 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4); }); return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]; };
  const ratio = (a, b) => { const l1 = lum(a), l2 = lum(b); const [h, l] = l1 > l2 ? [l1, l2] : [l2, l1]; return +((h + 0.05) / (l + 0.05)).toFixed(2); };
  const bg = 'rgb(10,12,14)';
  const worst = (sel) => { const els = [...document.querySelectorAll(sel)]; return els.length ? Math.min(...els.map(e => ratio(getComputedStyle(e).color, bg))) : null; };
  out.contrast = {
    lane: worst('.lane:not(.us)'), src: worst('.src'), barYear: worst('.bar-year'),
    school: worst('.school:not(.us)'), factsDt: worst('.facts dt'), note: worst('.note'),
  };
  out.contrastFails = Object.entries(out.contrast).filter(([, v]) => v !== null && v < 4.5).map(([k]) => k);

  // --- motion actually animates ---
  const chip = document.querySelector('.school');
  out.schoolTransition = chip ? getComputedStyle(chip).transitionDuration : null;

  // --- chart ---
  const bars = [...document.querySelectorAll('.bar')].map(b => Math.round(b.getBoundingClientRect().height));
  out.barsZero = bars.filter(h => h === 0).length;
  out.barsMax = bars.length ? Math.max(...bars) : 0;

  // --- overflow ---
  out.docW = document.documentElement.scrollWidth;
  out.innerW = window.innerWidth;
  out.overflow = out.docW > out.innerW;

  return out;
})()
"""

res = cdp.ev(c, CHECKS)
print(f"=== {W}x{H} ===")
print(json.dumps(res, indent=1))
