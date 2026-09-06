"""R4 pass G: unambiguous CPL. Reconstruct each rendered LINE's actual text by
grouping characters by their rendered y, then count characters directly."""
import cdp, json

cdp.launch(2560, 1440)
ws = cdp.connect()
print("href:", cdp.new_page(ws, 'http://localhost:4188/crls-crew/', 2560, 1440))
print("fonts:", cdp.ev(ws, "document.fonts.ready.then(()=>document.fonts.status)", awaitp=True))

JS = r"""
(()=>{
 // group characters into rendered lines by their top coordinate
 function lines(el){
  const out=[];
  const walk=document.createTreeWalker(el,NodeFilter.SHOW_TEXT);
  let n; const chars=[];
  while((n=walk.nextNode())){
    const t=n.nodeValue;
    for(let i=0;i<t.length;i++){
      const rg=document.createRange(); rg.setStart(n,i); rg.setEnd(n,i+1);
      const r=rg.getBoundingClientRect();
      if(r.width===0&&r.height===0)continue;
      chars.push({c:t[i],top:Math.round(r.top),left:r.left,right:r.right});
    }}
  if(!chars.length)return null;
  const byTop={};
  for(const c of chars){(byTop[c.top]=byTop[c.top]||[]).push(c);}
  for(const top of Object.keys(byTop)){
    const cs=byTop[top].sort((a,b)=>a.left-b.left);
    out.push({top:+top,text:cs.map(x=>x.c).join(''),
      n:cs.length,
      px:+(Math.max(...cs.map(x=>x.right))-Math.min(...cs.map(x=>x.left))).toFixed(0)});}
  out.sort((a,b)=>a.top-b.top);
  return out;
 }
 function report(sel,label){
  const el=document.querySelector(sel); if(!el)return null;
  const ls=lines(el); if(!ls)return null;
  const widest=ls.reduce((a,b)=>b.n>a.n?b:a);
  const cs=getComputedStyle(el);
  return {label,sel,boxW:+el.getBoundingClientRect().width.toFixed(0),
    fs:cs.fontSize,fam:cs.fontFamily.split(',')[0].replace(/["']/g,''),
    maxCPL:widest.n,widestLinePx:widest.px,
    widestLineText:widest.text,
    perLine:ls.map(l=>l.n)};
 }
 const out=[];
 out.push(report('.split .lead','split lead'));
 out.push(report('.tl-body p','tl-body p'));
 out.push(report('.narrow--flush p','narrow--flush p (closing argument)'));
 out.push(report('.note','note'));
 // every prose block, ranked
 const all=[...document.querySelectorAll('.lead, .tl-body p, .narrow p, .narrow--flush p, .hinge-sub')]
   .map(e=>{const ls=lines(e); if(!ls)return null;
     const w=ls.reduce((a,b)=>b.n>a.n?b:a);
     return {cls:(e.className||e.parentElement.className||'').slice(0,28),
       boxW:+e.getBoundingClientRect().width.toFixed(0),
       fs:getComputedStyle(e).fontSize,maxCPL:w.n};})
   .filter(Boolean).sort((a,b)=>b.maxCPL-a.maxCPL);
 return {blocks:out.filter(Boolean),widest:all.slice(0,8)};
})()
"""
print(json.dumps(cdp.ev(ws, JS), indent=1))
