import cdp, json

cdp.launch(2560, 1440)
ws = cdp.connect()
print("href:", cdp.new_page(ws, 'http://localhost:4188/crls-crew/', 2560, 1440))

JS = r"""
(() => {
 const out={};
 const R=e=>e.getBoundingClientRect();
 // TEXT-ONLY rightmost glyph (ignore borders/backgrounds) inside each aside
 function textRight(root){let m=-1e9;const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let n;
   while((n=w.nextNode())){if(!n.nodeValue.trim())continue;const g=document.createRange();g.selectNodeContents(n);
   for(const r of g.getClientRects())if(r.width>0)m=Math.max(m,r.right);}return m;}
 out.asideTextFill=[...document.querySelectorAll('.tl-item')].map(it=>{
   const a=it.querySelector('.tl-aside');const ar=R(a);const t=textRight(a);
   const facts=a.querySelector('.facts');
   const fr=facts?R(facts):null;
   return {year:it.querySelector('.tl-year').textContent.trim(),
     asideW:+ar.width.toFixed(0),
     textInkW:+(t-ar.left).toFixed(0),
     textFillPct:+(((t-ar.left)/ar.width)*100).toFixed(1),
     deadAfterText:+(ar.right-t).toFixed(0),
     factsW:fr?+fr.width.toFixed(0):null,
     // vertical: does aside content reach the row height?
     asideContentH:+[...a.children].reduce((s,c)=>s+R(c).height,0).toFixed(0),
     rowH:+R(it).height.toFixed(0)};
 });
 // .lane precise
 function lum(c){const m=c.match(/[\d.]+/g).map(Number);const f=v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)};
   return .2126*f(m[0])+.7152*f(m[1])+.0722*f(m[2]);}
 function bgOf(el){let e=el;while(e){const c=getComputedStyle(e).backgroundColor;
   if(c&&c!=='rgba(0, 0, 0, 0)'&&!/, *0\)$/.test(c))return c;e=e.parentElement;}return 'rgb(10,12,14)';}
 function ct(el){const a=lum(getComputedStyle(el).color),b=lum(bgOf(el));
   return +(((Math.max(a,b)+.05)/(Math.min(a,b)+.05)).toFixed(2));}
 out.lanes=[...document.querySelectorAll('.lane')].map(e=>({
   cls:e.className,txt:e.textContent.trim().slice(0,16),
   color:getComputedStyle(e).color,bg:bgOf(e),ratio:ct(e),fs:getComputedStyle(e).fontSize}));
 // all small text audit
 out.audit=[];
 for(const el of document.querySelectorAll('*')){
   const cs=getComputedStyle(el);const fs=parseFloat(cs.fontSize);
   if(fs>15)continue;
   const hasText=[...el.childNodes].some(n=>n.nodeType===3&&n.nodeValue.trim());
   if(!hasText)continue;const r=R(el);if(r.width<1||r.height<1)continue;
   const c=ct(el);if(c<4.5)out.audit.push({sel:el.className||el.tagName,fs:cs.fontSize,ratio:c,txt:el.textContent.trim().slice(0,28)});
 }
 // silence count
 const sc=document.querySelector('.silence-count');
 out.silence=sc?{color:getComputedStyle(sc).color,ratio:ct(sc),fs:getComputedStyle(sc).fontSize,txt:sc.textContent.trim()}:null;
 // hero + wide-screen fill
 out.hero=(()=>{const h=document.querySelector('#top .wrap')||document.querySelector('#top');
   return {w:+R(h).width.toFixed(0),pct:+((R(h).width/innerWidth)*100).toFixed(1)}})();
 // split dead space
 out.splits=[...document.querySelectorAll('.split')].map(s=>{
   const r=R(s);const t=textRight(s);
   return {parent:s.closest('section')?.id,w:+r.width.toFixed(0),
     dead:+(r.right-t).toFixed(0),fill:+(((t-r.left)/r.width)*100).toFixed(1)};});
 return out;})()
"""
r = cdp.ev(ws, JS)
print(json.dumps(r, indent=1))
