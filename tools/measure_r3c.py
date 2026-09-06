import cdp, json

cdp.launch(2560, 1440)
ws = cdp.connect()
print("href:", cdp.new_page(ws, 'http://localhost:4188/crls-crew/', 2560, 1440))

JS = r"""
(()=>{
 const out={};const R=e=>e.getBoundingClientRect();
 // RIGHT-EDGE ALIGNMENT across major blocks
 const probes=[['#river .split','river split'],['.timeline','timeline'],
   ['#then .wrap','then wrap'],['#return .wrap','return wrap'],
   ['.boat-stage','boat stage'],['#chart','chart'],['.progression','progression'],
   ['.foot-inner','footer'],['#field','field'],['.thesis','thesis'],
   ['.hinge .wrap','hinge wrap'],['.narrow--flush','flush block'],
   ['.heat','heat diagram'],['.results','results']];
 out.edges=probes.map(([s,n])=>{const e=document.querySelector(s);
   if(!e)return {name:n,missing:true};const r=R(e);
   return {name:n,left:+r.left.toFixed(0),right:+r.right.toFixed(0),w:+r.width.toFixed(0)};});

 // GLYPH-AREA density: total union area of text rects / container area
 function glyphArea(root){let a=0;const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let n;
  while((n=w.nextNode())){if(!n.nodeValue.trim())continue;const g=document.createRange();
  g.selectNodeContents(n);for(const r of g.getClientRects())a+=r.width*r.height;}return a;}
 out.density=[...document.querySelectorAll('.tl-item')].map(it=>{
   const a=it.querySelector('.tl-aside'),b=it.children[1];
   const ar=R(a),br=R(b);
   return {year:it.querySelector('.tl-year').textContent.trim(),
     asideGlyphPct:+((glyphArea(a)/(ar.width*ar.height))*100).toFixed(1),
     bodyGlyphPct:+((glyphArea(b)/(br.width*br.height))*100).toFixed(1),
     asideH:+ar.height.toFixed(0),bodyH:+br.height.toFixed(0),
     asideArea:+(ar.width*ar.height).toFixed(0)};});

 // vertical dead space in the aside track
 out.asideVertical=[...document.querySelectorAll('.tl-item')].map(it=>{
   const a=it.querySelector('.tl-aside');
   const kids=[...a.children];const ar=R(a);
   const lastBottom=kids.length?Math.max(...kids.map(k=>R(k).bottom)):ar.top;
   return {year:it.querySelector('.tl-year').textContent.trim(),
     trackH:+ar.height.toFixed(0),usedH:+(lastBottom-ar.top).toFixed(0),
     deadH:+(ar.bottom-lastBottom).toFixed(0),
     pct:+(((lastBottom-ar.top)/ar.height)*100).toFixed(1)};});

 // facts geometry
 const f=document.querySelector('.facts');
 out.facts={w:+R(f).width.toFixed(0),maxw:getComputedStyle(f).maxWidth,
   cols:getComputedStyle(f).gridTemplateColumns,
   ddAlign:getComputedStyle(document.querySelector('.facts dd')).textAlign,
   ddBorder:getComputedStyle(document.querySelector('.facts dd')).borderBottom};
 // dd text ink vs dd box
 out.ddInk=[...document.querySelectorAll('.facts dd')].slice(0,6).map(d=>{
   const r=R(d);const g=document.createRange();g.selectNodeContents(d);
   const rects=[...g.getClientRects()];const tw=rects.length?rects[0].width:0;
   return {txt:d.textContent.trim().slice(0,24),boxW:+r.width.toFixed(0),
     textW:+tw.toFixed(0),leaderW:+(r.width-tw).toFixed(0)};});
 return out;})()
"""
print(json.dumps(cdp.ev(ws, JS), indent=1))
