import cdp, json
cdp.launch(390, 844)
ws = cdp.connect()
print("href:", cdp.new_page(ws, 'http://localhost:4188/crls-crew/', 390, 844))
JS = r"""
(()=>{
 const vw=document.documentElement.clientWidth;
 const bad=[];
 for(const el of document.querySelectorAll('*')){
   const r=el.getBoundingClientRect();
   if(r.width<1||r.height<1)continue;
   if(r.right>vw+1||r.left<-1){
     bad.push({tag:el.tagName,cls:(el.className&&el.className.baseVal!==undefined?el.className.baseVal:el.className||'').toString().slice(0,44),
       left:+r.left.toFixed(0),right:+r.right.toFixed(0),w:+r.width.toFixed(0),
       txt:(el.textContent||'').trim().replace(/\s+/g,' ').slice(0,36),
       ovf:getComputedStyle(el).overflowX,
       pos:getComputedStyle(el).position});
   }
 }
 // keep the outermost offenders only
 const out=bad.filter(b=>b.right>vw+2);
 return {vw,docW:document.documentElement.scrollWidth,count:out.length,
   worst:out.sort((a,b)=>b.right-a.right).slice(0,25)};})()
"""
print(json.dumps(cdp.ev(ws, JS), indent=1))
cdp.shot(ws, "/Users/AISandbox/crls-crew/renders/r3-390-top.png")
