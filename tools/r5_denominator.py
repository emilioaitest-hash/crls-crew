"""R5: prove WHAT audit.py is actually measuring, and decompose the denominator.

Two questions:
 1. Are audit.py's extra rects block boxes? Dump them with their sizes.
 2. Is `ink area / track area` fair? The .tl-aside may be stretched by the grid
    to the body column's height, in which case the aside can never reach body
    density no matter how much is written. Measure aside CONTENT height vs
    TRACK height, and re-report density against content height.
"""
import sys, json, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import cdp  # noqa: E402

URL = "https://emilioaitest-hash.github.io/crls-crew/"
W, H = 2560, 1440
URL += f"?r5b={int(time.time())}"
cdp.launch(W, H)
c = cdp.connect()
print("href:", cdp.new_page(c, URL, W, H, wait=6.0, scroll_all=True))
cdp.ev(c, "document.getElementById('then').scrollIntoView()")
time.sleep(2.0)
print("href confirm:", cdp.ev(c, "location.href"))

EXPR = r"""
(() => {
  const R = e=>e.getBoundingClientRect();
  const aside = document.querySelectorAll('.tl-item .tl-aside')[1]; // 1889 row
  const ab = R(aside);

  // dump every rect audit.py's container-range returns
  const cr = document.createRange(); cr.selectNodeContents(aside);
  const A = [...cr.getClientRects()].map(c=>({w:Math.round(c.width),h:Math.round(c.height),
      x:Math.round(c.left-ab.left),y:Math.round(c.top-ab.top)}));

  // dump every rect the text-node walk returns
  const B=[]; const wk=document.createTreeWalker(aside,NodeFilter.SHOW_TEXT); let n;
  while((n=wk.nextNode())){ if(!n.nodeValue.trim()) continue;
    const g=document.createRange(); g.selectNodeContents(n);
    for(const r of g.getClientRects()) B.push({w:Math.round(r.width),h:Math.round(r.height),
      x:Math.round(r.left-ab.left),y:Math.round(r.top-ab.top),t:n.nodeValue.trim().slice(0,28)}); }

  // denominator decomposition across all rows
  const rows=[];
  const glyphArea=(root)=>{let a=0;const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let m;
    while((m=w.nextNode())){if(!m.nodeValue.trim())continue;const g=document.createRange();
      g.selectNodeContents(m);for(const r of g.getClientRects())a+=r.width*r.height;}return a;};
  for (const row of document.querySelectorAll('.tl-item')) {
    const a=row.querySelector('.tl-aside'); if(!a) continue;
    const b=row.querySelector('.tl-body');
    const ar=R(a), br=R(b);
    // content height = union vertical extent of the aside's own children
    const kids=[...a.children].map(k=>R(k));
    const top=Math.min(...kids.map(k=>k.top)), bot=Math.max(...kids.map(k=>k.bottom));
    const contentH=bot-top;
    const ga=glyphArea(a);
    rows.push({year:row.querySelector('.tl-year').textContent.trim(),
      trackW:Math.round(ar.width), trackH:Math.round(ar.height),
      contentH:Math.round(contentH), bodyH:Math.round(br.height),
      stretch:+(ar.height/contentH).toFixed(2),
      pctTrack:+(ga/(ar.width*ar.height)*100).toFixed(1),
      pctContent:+(ga/(ar.width*contentH)*100).toFixed(1),
      bodyPctTrack:+(glyphArea(b)/(br.width*br.height)*100).toFixed(1),
      alignSelf:getComputedStyle(a).alignSelf});
  }
  const mean=k=>+(rows.reduce((s,x)=>s+x[k],0)/rows.length).toFixed(1);
  return {A, B, nA:A.length, nB:B.length, asideW:Math.round(ab.width), asideH:Math.round(ab.height),
    rows, meanPctTrack:mean('pctTrack'), meanPctContent:mean('pctContent'),
    meanBodyPctTrack:mean('bodyPctTrack'), meanStretch:mean('stretch'),
    lineHeight:getComputedStyle(document.querySelector('.facts')).lineHeight,
    fontSize:getComputedStyle(document.querySelector('.facts')).fontSize};
})()
"""
r = cdp.ev(c, EXPR)
print(f"\n--- 1889 aside is {r['asideW']}x{r['asideH']} ---")
print(f"METHOD A returned {r['nA']} rects (audit.py):")
for x in r['A']:
    tag = "  <-- FULL-WIDTH BLOCK BOX" if x['w'] >= r['asideW'] - 2 else ""
    print(f"   {x['w']:5d} x {x['h']:4d}  at ({x['x']:4d},{x['y']:4d}){tag}")
print(f"\nMETHOD B returned {r['nB']} rects (text nodes):")
for x in r['B']:
    print(f"   {x['w']:5d} x {x['h']:4d}  at ({x['x']:4d},{x['y']:4d})  '{x['t']}'")

print(f"\n--- denominator: is the track stretched? ---")
print(f"{'year':7s} {'trkH':>5s} {'contH':>6s} {'bodyH':>6s} {'strch':>6s} {'%track':>7s} {'%cont':>7s} {'body%':>6s}")
for x in r['rows']:
    print(f"{x['year']:7s} {x['trackH']:5d} {x['contentH']:6d} {x['bodyH']:6d} {x['stretch']:6.2f} "
          f"{x['pctTrack']:7.1f} {x['pctContent']:7.1f} {x['bodyPctTrack']:6.1f}")
print(f"\nmean % of TRACK   : {r['meanPctTrack']}%   (this is R4's method: 10.2%)")
print(f"mean % of CONTENT : {r['meanPctContent']}%   (denominator = aside's own content height)")
print(f"mean body % track : {r['meanBodyPctTrack']}%")
print(f"mean stretch      : {r['meanStretch']}x   align-self: {r['rows'][0]['alignSelf']}")
print(f".facts font-size {r['fontSize']}  line-height {r['lineHeight']}")
