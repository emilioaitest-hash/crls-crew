"""R4 pass E: locate the 390px horizontal overflow exactly, and check .facts on mobile."""
import cdp, json

cdp.launch(390, 844)
ws = cdp.connect()
print("href:", cdp.new_page(ws, 'http://localhost:4188/crls-crew/', 390, 844))

JS = r"""
(()=>{
 const out={};const R=e=>e.getBoundingClientRect();
 out.docW=document.documentElement.scrollWidth;
 out.bodyW=document.body.scrollWidth;
 out.innerW=innerWidth;
 // any element whose own scrollWidth exceeds its clientWidth (internal overflow)
 out.selfOverflow=[];
 for(const el of document.querySelectorAll('*')){
   if(el.scrollWidth>el.clientWidth+1 && el.clientWidth>0){
     out.selfOverflow.push({sel:el.tagName.toLowerCase()+(el.className&&typeof el.className==='string'?'.'+el.className.trim().split(/\s+/).join('.'):''),
       scrollW:el.scrollWidth,clientW:el.clientWidth,
       over:el.scrollWidth-el.clientWidth});}}
 out.selfOverflow=out.selfOverflow.slice(0,15);
 // absolute document coords, independent of current scroll
 const sx=window.scrollX;
 out.pastViewport=[];
 for(const el of document.querySelectorAll('*')){
   const r=R(el);
   if(r.width>0&&r.height>0&&(r.right+sx)>out.innerW+1){
     out.pastViewport.push({sel:el.tagName.toLowerCase()+(el.className&&typeof el.className==='string'?'.'+el.className.trim().split(/\s+/).slice(0,3).join('.'):''),
       right:+(r.right+sx).toFixed(0),w:+r.width.toFixed(0),
       txt:(el.textContent||'').replace(/\s+/g,' ').trim().slice(0,40)});}}
 out.pastViewport=out.pastViewport.slice(0,20);
 // .facts geometry on mobile
 const f=document.querySelector('.facts');
 out.facts={w:+R(f).width.toFixed(0),cols:getComputedStyle(f).gridTemplateColumns};
 out.ddLines=[...document.querySelectorAll('.facts dd')].slice(0,12).map(d=>{
   const g=document.createRange();g.selectNodeContents(d);
   return {t:d.textContent.trim().slice(0,44),boxW:+R(d).width.toFixed(0),
     lines:[...g.getClientRects()].length,h:+R(d).height.toFixed(0)};});
 out.dtW=[...document.querySelectorAll('.facts dt')].slice(0,8)
   .map(d=>({t:d.textContent.trim(),w:+R(d).width.toFixed(0)}));
 return out;})()
"""
print(json.dumps(cdp.ev(ws, JS), indent=1))
cdp.shot(ws, "/Users/AISandbox/crls-crew/renders/r4-390-top.png")
