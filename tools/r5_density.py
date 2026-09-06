"""R5 independent density check.

audit.py measures ink with `range.selectNodeContents(CONTAINER)` then sums
getClientRects(). On a container that range yields BLOCK boxes, not glyph
boxes, so it measures the box, not the text. R4's measure_r4b.py walked TEXT
NODES. This runs BOTH on the same DOM in the same pass so the delta is
attributable to method, not to build/viewport drift.
"""
import sys, json, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import cdp  # noqa: E402

URL = sys.argv[1] if len(sys.argv) > 1 else "https://emilioaitest-hash.github.io/crls-crew/"
W = int(sys.argv[2]) if len(sys.argv) > 2 else 2560
H = int(sys.argv[3]) if len(sys.argv) > 3 else 1440
URL += ("&" if "?" in URL else "?") + f"r5={int(time.time())}"

cdp.launch(W, H)
c = cdp.connect()
href = cdp.new_page(c, URL, W, H, wait=6.0, scroll_all=True)
print("href:", href)
cdp.ev(c, "document.getElementById('then') && document.getElementById('then').scrollIntoView()")
time.sleep(2.0)
print("href confirm:", cdp.ev(c, "location.href"))
print("fonts:", cdp.ev(c, "document.fonts.status"))

EXPR = r"""
(() => {
  const R = e => e.getBoundingClientRect();

  // --- METHOD A: audit.py's. Range over the CONTAINER.
  const containerArea = (el) => {
    const r = document.createRange(); r.selectNodeContents(el);
    return [...r.getClientRects()].reduce((a,c)=>a+c.width*c.height,0);
  };
  const containerRight = (el) => {
    const r = document.createRange(); r.selectNodeContents(el);
    const x = [...r.getClientRects()];
    return x.length ? Math.max(...x.map(c=>c.right)) : null;
  };
  const containerRectCount = (el) => {
    const r = document.createRange(); r.selectNodeContents(el);
    return [...r.getClientRects()].length;
  };

  // --- METHOD B: R4's. Walk TEXT NODES only; each range is one text run.
  const glyphArea = (root) => {
    let a=0; const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT); let n;
    while((n=w.nextNode())){ if(!n.nodeValue.trim()) continue;
      const g=document.createRange(); g.selectNodeContents(n);
      for(const r of g.getClientRects()) a+=r.width*r.height; }
    return a; };
  const glyphRight = (root) => {
    let m=-1e9; const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT); let n;
    while((n=w.nextNode())){ if(!n.nodeValue.trim()) continue;
      const g=document.createRange(); g.selectNodeContents(n);
      for(const r of g.getClientRects()) if(r.width>0) m=Math.max(m,r.right); }
    return m>-1e9 ? m : null; };
  const glyphRectCount = (root) => {
    let k=0; const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT); let n;
    while((n=w.nextNode())){ if(!n.nodeValue.trim()) continue;
      const g=document.createRange(); g.selectNodeContents(n);
      k+=[...g.getClientRects()].length; }
    return k; };

  const rows=[]; 
  for (const row of document.querySelectorAll('.tl-item')) {
    const a = row.querySelector('.tl-aside'); if(!a) continue;
    const b = row.querySelector('.tl-body');
    const f = a.querySelector('.facts');
    const ab = R(a), rr = R(row);
    const area = ab.width*ab.height; if(!area) continue;
    const cRight = containerRight(a), gRight = glyphRight(a);
    rows.push({
      year:(row.querySelector('.tl-year')||{textContent:'?'}).textContent.trim(),
      trackW:Math.round(ab.width), trackH:Math.round(ab.height),
      A_areaPct:+(containerArea(a)/area*100).toFixed(1),
      B_areaPct:+(glyphArea(a)/area*100).toFixed(1),
      A_rects:containerRectCount(a), B_rects:glyphRectCount(a),
      A_hFill:cRight?+((cRight-ab.left)/ab.width*100).toFixed(1):null,
      B_hFill:gRight?+((gRight-ab.left)/ab.width*100).toFixed(1):null,
      A_overhang:cRight?Math.round(rr.right-cRight):null,
      B_overhang:gRight?Math.round(rr.right-gRight):null,
      bodyB:b?+(glyphArea(b)/(R(b).width*R(b).height)*100).toFixed(1):null,
      factsW:f?Math.round(R(f).width):null,
      factsMaxW:f?getComputedStyle(f).maxWidth:null,
      chars:a.textContent.replace(/\s+/g,' ').trim().length,
      pairs:a.querySelectorAll('dt').length,
    });
  }
  const mean=(k)=>{const v=rows.map(r=>r[k]).filter(x=>x!==null&&x!==undefined);
    return v.length?+(v.reduce((a,b)=>a+b,0)/v.length).toFixed(1):null;};
  return {rows, mean:{
    A_areaPct:mean('A_areaPct'), B_areaPct:mean('B_areaPct'),
    A_hFill:mean('A_hFill'), B_hFill:mean('B_hFill'),
    A_overhang:mean('A_overhang'), B_overhang:mean('B_overhang'),
    bodyB:mean('bodyB'), chars:mean('chars'), pairs:mean('pairs'),
  }};
})()
"""
r = cdp.ev(c, EXPR)
print(f"\n=== APPARATUS DENSITY at {W}px — two methods, same DOM ===")
print(f"{'year':7s} {'trkW':>5s} {'A_area':>7s} {'B_area':>7s} {'A_rct':>5s} {'B_rct':>5s} {'A_hF':>6s} {'B_hF':>6s} {'A_ovh':>6s} {'B_ovh':>6s} {'body':>6s} {'chars':>5s}")
for x in r['rows']:
    print(f"{x['year']:7s} {x['trackW']:5d} {x['A_areaPct']:7.1f} {x['B_areaPct']:7.1f} "
          f"{x['A_rects']:5d} {x['B_rects']:5d} {x['A_hFill']:6.1f} {x['B_hFill']:6.1f} "
          f"{x['A_overhang']:6d} {x['B_overhang']:6d} {x['bodyB']:6.1f} {x['chars']:5d}")
m = r['mean']
print(f"\nMETHOD A (audit.py, container range):  area {m['A_areaPct']}%  hFill {m['A_hFill']}%  overhang {m['A_overhang']}px")
print(f"METHOD B (R4, text-node walk):        area {m['B_areaPct']}%  hFill {m['B_hFill']}%  overhang {m['B_overhang']}px")
print(f"body column (method B):               {m['bodyB']}%")
print(f"mean chars/aside {m['chars']}   mean pairs/aside {m['pairs']}")
print(f"facts box width {r['rows'][0]['factsW']}px   max-width {r['rows'][0]['factsMaxW']}")
