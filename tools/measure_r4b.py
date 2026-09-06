"""R4 focused: is the apparatus column FILLED, or just written-and-capped?
Measures glyph area against three denominators so the number can't hide:
  (a) the .facts box itself   (b) the .tl-aside track   (c) the whole row
"""
import cdp, json, sys

W = int(sys.argv[1]) if len(sys.argv) > 1 else 2560
H = int(sys.argv[2]) if len(sys.argv) > 2 else 1440
cdp.launch(W, H)
ws = cdp.connect()
print("href:", cdp.new_page(ws, 'http://localhost:4188/crls-crew/', W, H))

JS = r"""
(()=>{
 const out={}; const R=e=>e.getBoundingClientRect();
 function glyphArea(root){let a=0;
  const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let n;
  while((n=w.nextNode())){if(!n.nodeValue.trim())continue;
   const g=document.createRange();g.selectNodeContents(n);
   for(const r of g.getClientRects())a+=r.width*r.height;}
  return a;}
 function inkRight(root){let m=-1e9;
  const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let n;
  while((n=w.nextNode())){if(!n.nodeValue.trim())continue;
   const g=document.createRange();g.selectNodeContents(n);
   for(const r of g.getClientRects())if(r.width>0)m=Math.max(m,r.right);}
  return m;}

 out.rows=[...document.querySelectorAll('.tl-item')].map(it=>{
   const a=it.querySelector('.tl-aside');
   const f=a?a.querySelector('.facts'):null;
   const b=it.children[1];
   const ar=R(a), br=R(b), rr=R(it);
   const ga=glyphArea(a);
   const ink=inkRight(a);
   return {
     year:it.querySelector('.tl-year').textContent.trim(),
     factsW: f?+R(f).width.toFixed(0):null,
     factsH: f?+R(f).height.toFixed(0):null,
     factsPct: f?+((glyphArea(f)/(R(f).width*R(f).height))*100).toFixed(1):null,
     trackW:+ar.width.toFixed(0), trackPct:+((ga/(ar.width*ar.height))*100).toFixed(1),
     bodyPct:+((glyphArea(b)/(br.width*br.height))*100).toFixed(1),
     // horizontal: rightmost glyph in the aside vs the track's right edge
     inkRightOffset:+(ar.right-ink).toFixed(0),
     inkUsedW:+(ink-ar.left).toFixed(0),
     hFillPct:+(((ink-ar.left)/ar.width)*100).toFixed(1),
     // the rule spans the whole row; where does ANY ink in the row stop?
     rowRight:+rr.right.toFixed(0), rowInkRight:+inkRight(it).toFixed(0),
     ruleOverhang:+(rr.right-inkRight(it)).toFixed(0),
     chars:a.textContent.replace(/\s+/g,' ').trim().length,
     pairs:a.querySelectorAll('dt').length,
   };});
 const r=out.rows;
 out.mean={factsPct:+(r.reduce((s,x)=>s+x.factsPct,0)/r.length).toFixed(1),
   trackPct:+(r.reduce((s,x)=>s+x.trackPct,0)/r.length).toFixed(1),
   bodyPct:+(r.reduce((s,x)=>s+x.bodyPct,0)/r.length).toFixed(1),
   hFillPct:+(r.reduce((s,x)=>s+x.hFillPct,0)/r.length).toFixed(1),
   ruleOverhang:+(r.reduce((s,x)=>s+x.ruleOverhang,0)/r.length).toFixed(0),
   chars:+(r.reduce((s,x)=>s+x.chars,0)/r.length).toFixed(0)};

 // every dd: text width vs box width (leader dead-run)
 out.dd=[...document.querySelectorAll('.facts dd')].map(d=>{
   const rr=R(d); const g=document.createRange(); g.selectNodeContents(d);
   const rects=[...g.getClientRects()];
   const widest=rects.length?Math.max(...rects.map(x=>x.width)):0;
   return {txt:d.textContent.trim().slice(0,60),boxW:+rr.width.toFixed(0),
     textW:+widest.toFixed(0),dead:+(rr.width-widest).toFixed(0),lines:rects.length};});
 out.ddStats={n:out.dd.length,
   meanDead:+(out.dd.reduce((s,x)=>s+x.dead,0)/out.dd.length).toFixed(0),
   maxDead:Math.max(...out.dd.map(x=>x.dead)),
   minDead:Math.min(...out.dd.map(x=>x.dead)),
   multiline:out.dd.filter(x=>x.lines>1).length,
   meanChars:+(out.dd.reduce((s,x)=>s+x.txt.length,0)/out.dd.length).toFixed(0)};
 const f=document.querySelector('.facts');
 out.factsBox={w:+R(f).width.toFixed(0),maxw:getComputedStyle(f).maxWidth,
   cols:getComputedStyle(f).gridTemplateColumns,
   trackW:+R(document.querySelector('.tl-aside')).width.toFixed(0)};
 return out;})()
"""
print(json.dumps(cdp.ev(ws, JS), indent=1))
