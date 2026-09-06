"""R5 visual: screenshot the 1889 apparatus row at each width so the measured
density can be checked against what a human actually sees.
"""
import sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import cdp  # noqa: E402

W = int(sys.argv[1]); H = int(sys.argv[2]); tag = sys.argv[3]
URL = "https://emilioaitest-hash.github.io/crls-crew/" + f"?r5shot={int(time.time())}"
cdp.launch(W, H)
c = cdp.connect()
print("href:", cdp.new_page(c, URL, W, H, wait=6.0, scroll_all=True))
cdp.ev(c, """(()=>{const r=[...document.querySelectorAll('.tl-item')][1];
  r.scrollIntoView({block:'center'});return 1;})()""")
time.sleep(2.0)
print("confirm:", cdp.ev(c, "location.href"))
box = cdp.ev(c, """(()=>{const r=[...document.querySelectorAll('.tl-item')][1];
  const b=r.getBoundingClientRect();
  return {x:Math.round(b.left),y:Math.round(b.top),w:Math.round(b.width),h:Math.round(b.height)};})()""")
print("row box:", box)
cdp.shot(c, f"/tmp/r5_row_{tag}.png")
cdp.ev(c, "window.scrollTo(0,0)"); time.sleep(1.0)
cdp.shot(c, f"/tmp/r5_hero_{tag}.png")
print("saved", tag)
