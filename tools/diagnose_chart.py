"""Why are the chart bars zero-height at this viewport?"""
import sys, json
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import cdp  # noqa: E402

URL = "https://emilioaitest-hash.github.io/crls-crew/"
W = int(sys.argv[1]) if len(sys.argv) > 1 else 2560
H = int(sys.argv[2]) if len(sys.argv) > 2 else 1440

cdp.launch(W, H)
c = cdp.connect()
print("loaded:", cdp.new_page(c, URL, W, H, wait=6.0, scroll_all=True))

# scroll the chart into view explicitly and let it settle
cdp.ev(c, "document.getElementById('record').scrollIntoView()")
import time; time.sleep(2.5)

print(json.dumps(cdp.ev(c, r"""
(() => {
  const col = document.querySelector('.bar-col');
  const trk = document.querySelector('.bar-track');
  const bar = document.querySelector('.bar');
  const cs = (e) => e ? getComputedStyle(e) : null;
  const box = (e) => { if (!e) return null; const r = e.getBoundingClientRect();
    return {w: Math.round(r.width), h: Math.round(r.height), top: Math.round(r.top)}; };
  return {
    chartH: box(document.querySelector('.chart')),
    colH: box(col), trackH: box(trk), barH: box(bar),
    colClasses: col ? col.className : null,
    colOverflow: cs(col) ? cs(col).overflow : null,
    trackFlex: cs(trk) ? cs(trk).flex : null,
    trackMinH: cs(trk) ? cs(trk).minHeight : null,
    barHeightCSS: cs(bar) ? cs(bar).height : null,
    barStyleAttr: bar ? bar.getAttribute('style') : null,
    barTransform: cs(bar) ? cs(bar).transform : null,
    inCount: document.querySelectorAll('.bar-col.in').length,
  };
})()
""" ), indent=1))
