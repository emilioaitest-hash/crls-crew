"""
Apparatus column density, measured the way round 4 demanded: ink AREA (union of
text client rects) over the track's box area — NOT how far right the text
reaches. Round 3 and round 4 both caught a fill claim made against horizontal
extent, so this reports both and labels which is which.
"""
import sys, json, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import cdp  # noqa: E402

URL = sys.argv[1] if len(sys.argv) > 1 else "https://emilioaitest-hash.github.io/crls-crew/"
W = int(sys.argv[2]) if len(sys.argv) > 2 else 2560
H = int(sys.argv[3]) if len(sys.argv) > 3 else 1440

cdp.launch(W, H)
c = cdp.connect()
print("loaded:", cdp.new_page(c, URL, W, H, wait=6.0, scroll_all=True))
cdp.ev(c, "document.getElementById('then') && document.getElementById('then').scrollIntoView()")
time.sleep(2.0)

EXPR = r"""
(() => {
  // Union area of every text rect inside an element, so overlapping lines are
  // not double-counted.
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

  const rows = [...document.querySelectorAll('.tl-item')];
  const out = [];
  for (const row of rows) {
    const aside = row.querySelector('.tl-aside');
    const body = row.querySelector('.tl-body');
    const year = (row.querySelector('.tl-year') || {}).textContent || '?';
    if (!aside) continue;
    const ab = aside.getBoundingClientRect();
    const rowBox = row.getBoundingClientRect();
    const area = ab.width * ab.height;
    const right = inkRight(aside);
    out.push({
      year: year.trim(),
      trackW: Math.round(ab.width),
      areaPct: area ? +(inkArea(aside) / area * 100).toFixed(1) : null,
      hFillPct: right ? +((right - ab.left) / ab.width * 100).toFixed(1) : null,
      ruleOverhang: right ? Math.round(rowBox.right - right) : null,
      bodyAreaPct: body ? +(inkArea(body) / (body.getBoundingClientRect().width * body.getBoundingClientRect().height) * 100).toFixed(1) : null,
    });
  }
  const mean = (k) => {
    const v = out.map(o => o[k]).filter(x => x !== null);
    return v.length ? +(v.reduce((a, b) => a + b, 0) / v.length).toFixed(1) : null;
  };
  return {
    rows: out,
    meanAreaPct: mean('areaPct'),
    meanHFillPct: mean('hFillPct'),
    meanOverhang: mean('ruleOverhang'),
    meanBodyAreaPct: mean('bodyAreaPct'),
  };
})()
"""
res = cdp.ev(c, EXPR)
print(f"\n=== apparatus density at {W}px ===")
for r in res['rows']:
    print(f"  {r['year']:6s} track {r['trackW']:4d}px   area {r['areaPct']:5.1f}%   hFill {r['hFillPct']:5.1f}%   overhang {r['ruleOverhang']:4d}px")
print(f"\n  MEAN ink AREA      : {res['meanAreaPct']}%   (R3: 14.8%  R4: 10.2%)")
print(f"  MEAN horiz extent  : {res['meanHFillPct']}%   <- the misleading number")
print(f"  MEAN rule overhang : {res['meanOverhang']}px  (R4: 554px, target <200)")
print(f"  body column area   : {res['meanBodyAreaPct']}%")
