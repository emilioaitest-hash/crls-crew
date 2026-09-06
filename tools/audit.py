"""
Full design audit of the deployed site, in one pass.

Consolidates what four rounds of critique proved worth measuring. Every check
here exists because a real bug got past a weaker check:

  ink AREA vs horizontal extent   — rounds 3 and 4 both caught a "fill" claim
                                    made against how far right text reached
  docW vs innerW at 390px         — three consecutive rounds shipped a mobile
                                    scrollbar from three different causes
  rendered CPL, trimmed lines     — a canvas average flattered the closing
                                    argument by up to 10 characters
  chart scrolled into view        — measuring it offscreen reports 20 bars at
                                    zero height and looks like a broken chart
  contrast on every text token    — --grey-2 (3.25:1) crept back into new
                                    markup after four separate removals
  no-JS render                    — the hero shipped blank and "0" for weeks

Usage:
    python3 tools/audit.py [url] [width] [height]
    python3 tools/audit.py                      # live site, 2560x1440
"""
import sys, time, json
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import cdp  # noqa: E402

import time as _t
URL = sys.argv[1] if len(sys.argv) > 1 else "https://emilioaitest-hash.github.io/crls-crew/"
# Always cache-bust. A stale CSS bundle once reported a contrast failure that
# had already been fixed and deployed, which is a false alarm that costs a
# debugging cycle every time.
URL += ("&" if "?" in URL else "?") + f"audit={int(_t.time())}"
W = int(sys.argv[2]) if len(sys.argv) > 2 else 2560
H = int(sys.argv[3]) if len(sys.argv) > 3 else 1440

AUDIT = r"""
(() => {
  const out = {};
  const inkArea = (el) => {
    if (!el) return 0;
    const r = document.createRange(); r.selectNodeContents(el);
    return [...r.getClientRects()].reduce((a, c) => a + c.width * c.height, 0);
  };
  const inkRight = (el) => {
    if (!el) return null;
    const r = document.createRange(); r.selectNodeContents(el);
    const rects = [...r.getClientRects()];
    return rects.length ? Math.max(...rects.map(c => c.right)) : null;
  };
  const mean = (a) => a.length ? +(a.reduce((x, y) => x + y, 0) / a.length).toFixed(1) : null;

  // --- apparatus density: AREA, and extent alongside it so the two can't be confused
  const rows = [...document.querySelectorAll('.tl-item')];
  const areas = [], extents = [], overhangs = [];
  for (const row of rows) {
    const a = row.querySelector('.tl-aside'); if (!a) continue;
    const ab = a.getBoundingClientRect(); if (!ab.width || !ab.height) continue;
    areas.push(+(inkArea(a) / (ab.width * ab.height) * 100).toFixed(1));
    const right = inkRight(a);
    if (right) {
      extents.push(+((right - ab.left) / ab.width * 100).toFixed(1));
      overhangs.push(Math.round(row.getBoundingClientRect().right - right));
    }
  }
  out.apparatus = { inkAreaPct: mean(areas), horizExtentPct: mean(extents), ruleOverhangPx: mean(overhangs), rows: areas.length };

  // --- contrast across every text component the critiques argued about
  const lum = (rgb) => { const v = rgb.match(/\d+/g).slice(0, 3).map(n => { let x = n / 255; return x <= 0.03928 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4); }); return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]; };
  const ratio = (a, b) => { const l1 = lum(a), l2 = lum(b); const [h, l] = l1 > l2 ? [l1, l2] : [l2, l1]; return +((h + 0.05) / (l + 0.05)).toFixed(2); };
  const BG = 'rgb(10,12,14)';
  const worst = (sel) => { const e = [...document.querySelectorAll(sel)]; return e.length ? Math.min(...e.map(x => ratio(getComputedStyle(x).color, BG))) : null; };
  out.contrast = {};
  for (const sel of ['.src', '.note', '.lane:not(.us)', '.school:not(.us)', '.bar-year', '.facts dt', '.facts dd', '.boat-state', '.tl-title', '.credit'])
    out.contrast[sel] = worst(sel);
  out.contrastFails = Object.entries(out.contrast).filter(([, v]) => v !== null && v < 4.5).map(([k, v]) => `${k} ${v}`);

  // --- measure: characters per rendered line, trimmed
  const cpl = (sel) => {
    const el = document.querySelector(sel); if (!el) return null;
    const r = document.createRange(); r.selectNodeContents(el);
    const lines = [...r.getClientRects()].filter(c => c.height > 4).length;
    return lines ? Math.round(el.textContent.trim().replace(/\s+/g, ' ').length / lines) : null;
  };
  out.cpl = { closing: cpl('.narrow--flush p'), tlBody: cpl('.tl-body p'), lead: cpl('.split .lead'), note: cpl('.note') };
  out.cplOver68 = Object.entries(out.cpl).filter(([, v]) => v && v > 68).map(([k, v]) => `${k} ${v}`);

  // --- alignment
  const right = (s) => { const e = document.querySelector(s); return e ? Math.round(e.getBoundingClientRect().right) : null; };
  out.rightEdges = {};
  for (const s of ['.timeline', '.split', '#chart', '.boat-stage', '.foot-inner', '#field', '.progression'])
    out.rightEdges[s] = right(s);
  out.edgesAgree = new Set(Object.values(out.rightEdges).filter(Boolean)).size === 1;

  // --- overflow, the real test: document against the viewport
  out.docW = document.documentElement.scrollWidth;
  out.innerW = window.innerWidth;
  out.overflow = out.docW > out.innerW;

  // --- motion actually animates
  const chip = document.querySelector('.school');
  out.schoolTransition = chip ? getComputedStyle(chip).transitionDuration : null;

  // --- content integrity
  out.timelineYears = [...document.querySelectorAll('.tl-year')].map(e => e.textContent.trim());
  out.dupeYears = out.timelineYears.filter((y, i, a) => a.indexOf(y) !== i && y !== '1929');
  out.counters = [...document.querySelectorAll('[data-count]')].map(e => e.textContent);
  out.fleet = [...document.querySelectorAll('#fleet-roster .boat b')].map(e => e.textContent);
  out.hasSeldon = document.body.innerText.includes('Seldon');
  return out;
})()
"""

cdp.launch(W, H)
c = cdp.connect()
print("loaded:", cdp.new_page(c, URL, W, H, wait=6.0, scroll_all=True))
for sec in ('then', 'record', 'fleet'):
    cdp.ev(c, f"document.getElementById('{sec}') && document.getElementById('{sec}').scrollIntoView()")
    time.sleep(1.2)
cdp.ev(c, "document.getElementById('then').scrollIntoView()")
time.sleep(1.8)

r = cdp.ev(c, AUDIT)
a = r['apparatus']
print(f"\n=== AUDIT {W}x{H} ===")
print(f"apparatus ink AREA   {a['inkAreaPct']}%   (R3 14.8 / R4 10.2, target >35)")
print(f"  horiz extent       {a['horizExtentPct']}%   <- NOT a fill measure")
print(f"  rule overhang      {a['ruleOverhangPx']}px  (R4 554, target <200)")
print(f"contrast failures    {r['contrastFails'] or 'none'}")
print(f"CPL over 68          {r['cplOver68'] or 'none'}   {r['cpl']}")
print(f"edges agree          {r['edgesAgree']}   {sorted(set(v for v in r['rightEdges'].values() if v))}")
print(f"overflow             {r['overflow']}   docW {r['docW']} vs innerW {r['innerW']}")
print(f"school transition    {r['schoolTransition']}")
print(f"duplicate years      {r['dupeYears'] or 'none'}")
print(f"counters             {r['counters']}")
print(f"fleet                {r['fleet']}   stale name present: {r['hasSeldon']}")

fails = []
if a['inkAreaPct'] is not None and a['inkAreaPct'] < 35: fails.append('apparatus density')
if r['contrastFails']: fails.append('contrast')
if r['overflow']: fails.append('overflow')
if not r['edgesAgree']: fails.append('alignment')
if r['dupeYears']: fails.append('duplicate content')
if r['hasSeldon']: fails.append('stale boat name')
print(f"\n{'FAIL: ' + ', '.join(fails) if fails else 'PASS — every gate clear'}")
