"""Round 4 verification. Same method as round 3: glyph AREA, not box width."""
import cdp, json, sys

W = int(sys.argv[1]) if len(sys.argv) > 1 else 2560
H = int(sys.argv[2]) if len(sys.argv) > 2 else 1440

cdp.launch(W, H)
ws = cdp.connect()
href = cdp.new_page(ws, 'http://localhost:4188/crls-crew/', W, H)
print("### VIEWPORT", W, "x", H, " href:", href)

JS = r"""
(()=>{
 const out={}; const R=e=>e.getBoundingClientRect();

 // ---- glyph AREA: union of text client rects. This is the round-3 method
 //      that exposed the 245px leader rule as fake fill.
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

 // ---------- P0.1 duplicate ----------
 out.dup={
  rows:[...document.querySelectorAll('.tl-item')].map(it=>({
    year:it.querySelector('.tl-year')?.textContent.trim(),
    title:it.querySelector('.tl-title')?.textContent.trim().slice(0,60),
    sect:it.closest('section')?.id})),
  count:document.querySelectorAll('.tl-item').length,
  has2000Row:[...document.querySelectorAll('.tl-year')].some(e=>e.textContent.trim()==='2000'),
  revivalBand:!!document.querySelector('.hinge--minor'),
  quoteCount:document.querySelectorAll('.quote').length,
 };

 // ---------- P0.2 apparatus density (THE claim) ----------
 out.density=[...document.querySelectorAll('.tl-item')].map(it=>{
   const a=it.querySelector('.tl-aside'), b=it.children[1];
   if(!a) return {year:it.querySelector('.tl-year')?.textContent.trim(),noAside:true};
   const ar=R(a), br=R(b);
   return {year:it.querySelector('.tl-year').textContent.trim(),
     asidePct:+((glyphArea(a)/(ar.width*ar.height))*100).toFixed(1),
     bodyPct:+((glyphArea(b)/(br.width*br.height))*100).toFixed(1),
     asideW:+ar.width.toFixed(0), asideH:+ar.height.toFixed(0),
     bodyH:+br.height.toFixed(0),
     factPairs:a.querySelectorAll('dt').length,
     asideChars:a.textContent.replace(/\s+/g,' ').trim().length};
 });
 const d=out.density.filter(x=>!x.noAside);
 out.densityMean={aside:+(d.reduce((s,x)=>s+x.asidePct,0)/d.length).toFixed(1),
                  body:+(d.reduce((s,x)=>s+x.bodyPct,0)/d.length).toFixed(1),
                  asideCharsMean:+(d.reduce((s,x)=>s+x.asideChars,0)/d.length).toFixed(0),
                  asideCharsMin:Math.min(...d.map(x=>x.asideChars)),
                  asideCharsMax:Math.max(...d.map(x=>x.asideChars))};

 // ---------- vertical fill of aside track ----------
 out.vfill=[...document.querySelectorAll('.tl-item')].map(it=>{
   const a=it.querySelector('.tl-aside'); if(!a)return null;
   const kids=[...a.children]; const ar=R(a);
   const lb=kids.length?Math.max(...kids.map(k=>R(k).bottom)):ar.top;
   return {year:it.querySelector('.tl-year').textContent.trim(),
     trackH:+ar.height.toFixed(0), usedH:+(lb-ar.top).toFixed(0),
     pct:+(((lb-ar.top)/ar.height)*100).toFixed(1)};}).filter(Boolean);

 // ---------- P0.2b leader rule ----------
 const dd0=document.querySelector('.facts dd'), f0=document.querySelector('.facts');
 out.factsCss=f0?{cols:getComputedStyle(f0).gridTemplateColumns,
   maxw:getComputedStyle(f0).maxWidth,
   ddAlign:getComputedStyle(dd0).textAlign,
   ddBorderBottom:getComputedStyle(dd0).borderBottomWidth+' '+getComputedStyle(dd0).borderBottomStyle,
   dtAlign:getComputedStyle(document.querySelector('.facts dt')).textAlign}:null;
 // dead run: box width minus widest text rect, per dd
 out.leader=[...document.querySelectorAll('.facts dd')].map(dd=>{
   const r=R(dd); const g=document.createRange(); g.selectNodeContents(dd);
   const rects=[...g.getClientRects()];
   const tw=rects.length?Math.max(...rects.map(x=>x.width)):0;
   return +(r.width-tw).toFixed(0);});
 out.leaderStats=out.leader.length?{n:out.leader.length,
   mean:+(out.leader.reduce((a,b)=>a+b,0)/out.leader.length).toFixed(0),
   min:Math.min(...out.leader),max:Math.max(...out.leader)}:null;
 out.ddSample=[...document.querySelectorAll('.facts dd')].slice(0,10)
   .map(d=>({txt:d.textContent.trim().slice(0,52),
             boxW:+R(d).width.toFixed(0),
             lines:(()=>{const g=document.createRange();g.selectNodeContents(d);
                     return [...g.getClientRects()].length;})()}));

 // ---------- contrast ----------
 function lum(c){const m=c.match(/[\d.]+/g).map(Number);
  const f=v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4);};
  return 0.2126*f(m[0])+0.7152*f(m[1])+0.0722*f(m[2]);}
 function bgOf(el){let e=el;while(e){const c=getComputedStyle(e).backgroundColor;
  if(c&&c!=='rgba(0, 0, 0, 0)'&&!/, *0\)$/.test(c))return c;e=e.parentElement;}
  return 'rgb(10,12,14)';}
 function ratio(el){const a=lum(getComputedStyle(el).color),b=lum(bgOf(el));
  return +(((Math.max(a,b)+0.05)/(Math.min(a,b)+0.05))).toFixed(2);}
 out.contrast={};
 for(const sel of ['.src','.bar-year','.lane','.lane.pub','.school','.facts dt','.facts dd',
    '.note','.silence-count','.p-l','.p-n','.bar-none','.boat-state','.heat-label']){
  const els=[...document.querySelectorAll(sel)];
  if(!els.length){out.contrast[sel]=null;continue;}
  const rs=els.map(ratio);
  out.contrast[sel]={n:els.length,min:Math.min(...rs),max:Math.max(...rs),
    color:getComputedStyle(els[0]).color,fs:getComputedStyle(els[0]).fontSize,
    failAA:rs.filter(r=>r<4.5).length};}

 // ---------- right-edge alignment ----------
 const probes=[['.timeline','timeline'],['#river .split','river split'],
  ['#chart','chart'],['.boat-stage','boat stage'],['.foot-inner','footer'],
  ['#field','field'],['.progression','progression'],['.heat','heat'],
  ['.narrow--flush','flush block'],['.thesis','thesis'],['.results','results']];
 out.edges=probes.map(([s,n])=>{const e=document.querySelector(s);
  if(!e)return{name:n,missing:true};const r=R(e);
  return{name:n,left:+r.left.toFixed(0),right:+r.right.toFixed(0),w:+r.width.toFixed(0)};});
 out.timelineMaxW=(()=>{const t=document.querySelector('.timeline');
  return t?getComputedStyle(t).maxWidth:null;})();
 out.tlCols=(()=>{const t=document.querySelector('.tl-item');
  return t?getComputedStyle(t).gridTemplateColumns:null;})();

 // ---------- measure / CPL ----------
 function chars(el){const t=el.textContent.replace(/\s+/g,' ').trim();
  const cs=getComputedStyle(el);const c=document.createElement('canvas').getContext('2d');
  c.font=`${cs.fontStyle} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
  const avg=c.measureText(t.slice(0,400)).width/Math.min(400,t.length);
  return {w:+R(el).width.toFixed(0),fs:cs.fontSize,ch:+(R(el).width/avg).toFixed(1)};}
 out.measures={};
 const lead=document.querySelector('.split .lead'); if(lead)out.measures.lead=chars(lead);
 const tb=document.querySelector('.tl-body p'); if(tb)out.measures.tlBody=chars(tb);
 const nf=document.querySelector('.narrow--flush');
 if(nf){const p=nf.querySelector('p'); if(p)out.measures.flushP=chars(p);
   out.measures.flushBox={w:+R(nf).width.toFixed(0),css:getComputedStyle(nf).width};}
 out.inlineMarginInline=document.querySelectorAll('[style*="margin-inline"]').length;

 // ---------- motion ----------
 const sc=[...document.querySelectorAll('.school')];
 out.motion={
  schoolN:sc.length,
  schoolDur:sc.length?getComputedStyle(sc[0]).transitionDuration:null,
  schoolDelays:sc.slice(0,8).map(e=>getComputedStyle(e).transitionDelay),
  schoolOpacity:sc.slice(0,8).map(e=>getComputedStyle(e).opacity),
  fieldIn:document.querySelector('#field')?.classList.contains('in'),
  revealN:document.querySelectorAll('[data-reveal]').length,
  buckets:(()=>{const b={};for(const el of document.querySelectorAll('[data-reveal]')){
    const cs=getComputedStyle(el);const k=cs.transitionDuration+' | '+cs.transitionDelay.split(',')[0];
    b[k]=(b[k]||0)+1;}return b;})(),
 };

 // ---------- 2020 annotation clearance ----------
 const bn=document.querySelector('.bar-none');
 if(bn){const br=R(bn);const col=bn.closest('.bar-col');
  const by=col?col.querySelector('.bar-year'):null;
  out.bar2020={noneBottom:+br.bottom.toFixed(0),noneTop:+br.top.toFixed(0),
    noneW:+br.width.toFixed(0),noneH:+br.height.toFixed(0),
    yearTop:by?+R(by).top.toFixed(0):null,
    clearance:by?+(R(by).top-br.bottom).toFixed(0):null,
    css:getComputedStyle(bn).bottom};}

 // ---------- progression ----------
 const pr=document.querySelector('.progression');
 if(pr){out.progression={cols:getComputedStyle(pr).gridTemplateColumns,
   nums:[...pr.querySelectorAll('.p-n')].map(e=>({t:e.textContent.trim(),
     fs:getComputedStyle(e).fontSize})),
   cellW:[...pr.children].map(c=>+R(c).width.toFixed(0))};}

 // ---------- fleet roster ----------
 const fl=document.querySelector('#fleet');
 out.fleet=fl?{boats:[...fl.querySelectorAll('.boat')].map(b=>({
    name:b.querySelector('.boat-id b')?.textContent.trim(),
    sub:b.querySelector('.boat-id em')?.textContent.trim(),
    state:b.querySelector('.boat-state')?.textContent.trim(),
    hull:b.querySelector('.boat-swatch')?.getAttribute('data-hull')}))}:null;
 out.seldon=document.body.textContent.includes('Seldon');
 out.wylde=(document.body.textContent.match(/Wylde/g)||[]).length;

 // ---------- road to final ----------
 out.roads=[...document.querySelectorAll('.result')].map(r=>({
   t:r.querySelector('h3,.res-title')?.textContent.trim().slice(0,40),
   hasRoad:!!r.querySelector('.road,.progress,.rounds'),
   txt:r.textContent.replace(/\s+/g,' ').trim().slice(0,180)}));

 // ---------- overflow ----------
 out.docW=document.documentElement.scrollWidth;
 out.innerW=innerWidth;
 out.scrollH=document.body.scrollHeight;
 out.overflowers=(()=>{const bad=[];
   for(const el of document.querySelectorAll('*')){const r=R(el);
     if(r.width>0&&r.right>innerWidth+1)bad.push({t:el.tagName+'.'+(el.className&&el.className.baseVal===undefined?String(el.className).split(' ')[0]:''),
       right:+r.right.toFixed(0),w:+r.width.toFixed(0)});}
   return bad.slice(0,12);})();
 const wraps=[...document.querySelectorAll('.wrap')];
 out.wrap=wraps.length?{w:+R(wraps[2]||wraps[0]).width.toFixed(0),
   pct:+((R(wraps[2]||wraps[0]).width/innerWidth)*100).toFixed(1)}:null;
 return out;})()
"""

res = cdp.ev(ws, JS)
print(json.dumps(res, indent=1))
cdp.shot(ws, f"/Users/AISandbox/crls-crew/renders/r4-{W}-top.png")
