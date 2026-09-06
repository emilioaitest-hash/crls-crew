import cdp, json, sys
W = int(sys.argv[1]); H = int(sys.argv[2])
cdp.launch(W, H)
ws = cdp.connect()
print("href:", cdp.new_page(ws, 'http://localhost:4188/crls-crew/', W, H), "vp", W)

JS = r"""
(()=>{
 // TRUE characters-per-line: group character rects by their top coordinate
 function cpl(el){
   const tn=[...el.childNodes].find(n=>n.nodeType===3&&n.nodeValue.trim())||
     (()=>{const w=document.createTreeWalker(el,NodeFilter.SHOW_TEXT);let n;
       while((n=w.nextNode()))if(n.nodeValue.trim())return n;return null;})();
   if(!tn)return null;
   const s=tn.nodeValue;const lines={};
   for(let i=0;i<s.length;i++){
     if(!s[i].trim())continue;
     const r=document.createRange();r.setStart(tn,i);r.setEnd(tn,i+1);
     const b=r.getBoundingClientRect();if(!b.width)continue;
     const k=Math.round(b.top);lines[k]=(lines[k]||0)+1;
   }
   const v=Object.values(lines);
   if(!v.length)return null;
   // ignore the last (ragged) line
   const full=v.length>1?v.slice(0,-1):v;
   return {lines:v.length,maxCPL:Math.max(...v),
     avgFullCPL:+(full.reduce((a,b)=>a+b,0)/full.length).toFixed(1),
     w:+el.getBoundingClientRect().width.toFixed(0),
     fs:getComputedStyle(el).fontSize};
 }
 const out={};
 const probe=[['#river .lead','river lead'],['.tl-body p','timeline body'],
   ['.narrow--flush p','flush closing prose'],['.hinge--minor .lead','revival lead'],
   ['.note','note footnote'],['#free .lead','free lead'],['#now .lead','now lead']];
 out.cpl={};
 for(const [s,n] of probe){const e=document.querySelector(s);out.cpl[n]=e?cpl(e):null;}
 // every .narrow--flush paragraph
 out.flushAll=[...document.querySelectorAll('.narrow--flush p')].map(p=>cpl(p));
 // headings scale
 out.h2=[...document.querySelectorAll('h2')].map(h=>({
   t:h.textContent.trim().replace(/\s+/g,' ').slice(0,34),
   fs:getComputedStyle(h).fontSize,cls:h.className,
   w:+h.getBoundingClientRect().width.toFixed(0)}));
 return out;})()
"""
print(json.dumps(cdp.ev(ws, JS), indent=1))
