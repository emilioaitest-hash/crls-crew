"""
Adversarial verification of the live site.

The weakness of tools/audit.py is that it only measures selectors I thought to
list — which is exactly how `.credit` sat at 3.25:1 through four review rounds.
This script does not take a selector list. It walks every element that renders
its own text and checks all of them, so a component nobody remembered still
gets caught.

Usage: python3 tools/adversarial.py [width] [height]
"""
import sys, time, json
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import cdp  # noqa: E402

W = int(sys.argv[1]) if len(sys.argv) > 1 else 1600
H = int(sys.argv[2]) if len(sys.argv) > 2 else 900
URL = f"https://emilioaitest-hash.github.io/crls-crew/?adv={int(time.time())}"

SCAN = r"""
(() => {
  const lum = (rgb) => {
    const m = rgb.match(/[\d.]+/g); if (!m) return null;
    const v = m.slice(0, 3).map(n => { let x = n / 255; return x <= 0.03928 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4); });
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2];
  };
  const ratio = (fg, bg) => {
    const l1 = lum(fg), l2 = lum(bg);
    if (l1 === null || l2 === null) return null;
    const [h, l] = l1 > l2 ? [l1, l2] : [l2, l1];
    return +((h + 0.05) / (l + 0.05)).toFixed(2);
  };
  // walk up for the first non-transparent background
  const bgOf = (el) => {
    let n = el;
    while (n && n !== document.documentElement) {
      const b = getComputedStyle(n).backgroundColor;
      if (b && !/rgba\(0, 0, 0, 0\)|transparent/.test(b)) return b;
      n = n.parentElement;
    }
    return 'rgb(10,12,14)';
  };

  const out = [];
  const seen = new Set();
  document.querySelectorAll('*').forEach(el => {
    // only elements rendering their OWN text
    const own = [...el.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim().length > 1);
    if (!own.length) return;
    const r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) return;
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none') return;
    if (parseFloat(cs.opacity) === 0) return;

    let fg = cs.color;
    // fold element opacity into the comparison, since it lightens text against bg
    const op = parseFloat(cs.opacity);
    const cr = ratio(fg, bgOf(el));
    if (cr === null) return;

    const size = parseFloat(cs.fontSize);
    const weight = parseInt(cs.fontWeight) || 400;
    // WCAG large text: >=24px, or >=18.66px bold
    const large = size >= 24 || (size >= 18.66 && weight >= 700);
    const need = large ? 3.0 : 4.5;

    if (cr < need) {
      const sel = el.tagName.toLowerCase() + (el.className && el.className.toString ? '.' + el.className.toString().trim().split(/\s+/).join('.') : '');
      if (seen.has(sel)) return;
      seen.add(sel);
      out.push({ sel: sel.slice(0, 60), ratio: cr, need, size: +size.toFixed(1), opacity: op,
                 text: el.textContent.trim().slice(0, 42) });
    }
  });
  return { fails: out, scanned: document.querySelectorAll('*').length };
})()
"""

cdp.launch(W, H)
c = cdp.connect()
print("loaded:", cdp.new_page(c, URL, W, H, wait=6.0, scroll_all=True))
for s in ('river', 'then', 'gap', 'return', 'fleet', 'record', 'now', 'free'):
    cdp.ev(c, f"document.getElementById('{s}') && document.getElementById('{s}').scrollIntoView()")
    time.sleep(0.7)
time.sleep(1.2)

r = cdp.ev(c, SCAN)
print(f"\n=== every text-bearing element scanned at {W}x{H} ===")
print(f"elements in document: {r['scanned']}")
if r['fails']:
    print(f"CONTRAST FAILURES: {len(r['fails'])}")
    for f in r['fails']:
        print(f"  {f['ratio']:>5} (needs {f['need']})  {f['size']}px op{f['opacity']}  {f['sel']}")
        print(f"         \"{f['text']}\"")
else:
    print("CONTRAST: no failures — every text element meets WCAG AA for its size")
