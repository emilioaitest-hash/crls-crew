"""R4 pass C: fonts-ready CPL, contrast, stagger-in-flight, no-JS, mobile."""
import cdp, json, sys

W = int(sys.argv[1]) if len(sys.argv) > 1 else 2560
H = int(sys.argv[2]) if len(sys.argv) > 2 else 1440
cdp.launch(W, H)
ws = cdp.connect()
print("href:", cdp.new_page(ws, 'http://localhost:4188/crls-crew/', W, H))

# make sure webfonts are actually resolved before any text metric is taken
print("fontsReady:", cdp.ev(ws, "document.fonts.ready.then(()=>document.fonts.status)", awaitp=True))
print("loadedFaces:", cdp.ev(ws, "[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight).join(' | ')"))

JS = r"""
(()=>{
 const out={}; const R=e=>e.getBoundingClientRect();

 // ---- TRUE characters-per-line: count chars in the widest rendered line box
 //      via Range over the text node, rather than a canvas average.
 function trueCPL(el){
  const node=[...el.childNodes].find(n=>n.nodeType===3&&n.nodeValue.trim())||el.firstChild;
  const txt=el.textContent.replace(/\s+/g,' ').trim();
  const g=document.createRange(); g.selectNodeContents(el);
  const rects=[...g.getClientRects()].filter(r=>r.width>1);
  if(!rects.length) return null;
  // widest line, then binary-count how many characters fit that width
  const widest=Math.max(...rects.map(r=>r.width));
  // walk characters accumulating width using a measuring range
  let best=0;
  if(node&&node.nodeType===3){
    const t=node.nodeValue;
    let lineStart=0, count=0, prevTop=null, cur=0;
    for(let i=0;i<t.length;i++){
      const rg=document.createRange(); rg.setStart(node,i); rg.setEnd(node,i+1);
      const r=rg.getBoundingClientRect();
      if(r.width===0&&r.height===0) continue;
      if(prevTop===null) prevTop=r.top;
      if(Math.abs(r.top-prevTop)>2){ best=Math.max(best,cur); cur=0; prevTop=r.top; }
      cur++;
    }
    best=Math.max(best,cur);
  }
  const cs=getComputedStyle(el);
  return {w:+R(el).width.toFixed(0),fs:cs.fontSize,fam:cs.fontFamily.split(',')[0],
          cpl:best,lines:rects.length,widestLine:+widest.toFixed(0)};
 }
 out.cpl={};
 const lead=document.querySelector('.split .lead'); if(lead)out.cpl.lead=trueCPL(lead);
 const tb=document.querySelector('.tl-body p'); if(tb)out.cpl.tlBody=trueCPL(tb);
 const nf=document.querySelector('.narrow--flush');
 if(nf){const p=nf.querySelector('p'); if(p)out.cpl.flushP=trueCPL(p);
   out.cpl.flushBoxW=+R(nf).width.toFixed(0);}
 const note=document.querySelector('.note'); if(note)out.cpl.note=trueCPL(note);
 // widest prose measure anywhere
 out.cpl.allProse=[...document.querySelectorAll('.lead, .tl-body p, .narrow p, .narrow--flush p')]
   .map(e=>{const c=trueCPL(e);return c?{cpl:c.cpl,w:c.w,cls:e.className||e.parentElement.className}:null})
   .filter(Boolean).sort((a,b)=>b.cpl-a.cpl).slice(0,6);

 // ---- contrast, full
 function lum(c){const m=c.match(/[\d.]+/g).map(Number);
  const f=v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4);};
  return 0.2126*f(m[0])+0.7152*f(m[1])+0.0722*f(m[2]);}
 function bgOf(el){let e=el;while(e){const c=getComputedStyle(e).backgroundColor;
  if(c&&c!=='rgba(0, 0, 0, 0)'&&!/, *0\)$/.test(c))return c;e=e.parentElement;}
  return 'rgb(10,12,14)';}
 function ratio(el){const a=lum(getComputedStyle(el).color),b=lum(bgOf(el));
  return +(((Math.max(a,b)+0.05)/(Math.min(a,b)+0.05))).toFixed(2);}
 out.contrast={};
 for(const sel of ['.src','.bar-year','.lane','.school','.facts dt','.facts dd','.note',
   '.silence-count','.p-l','.p-n','.bar-none','.boat-state','.heat-label','.chart-key span']){
  const els=[...document.querySelectorAll(sel)];
  if(!els.length){out.contrast[sel]='NONE';continue;}
  const rs=els.map(ratio);
  out.contrast[sel]={n:els.length,min:Math.min(...rs),max:Math.max(...rs),
   color:getComputedStyle(els[0]).color,fs:getComputedStyle(els[0]).fontSize,
   failAA:rs.filter(r=>r<4.5).length};}
 // the 8 "Private" lanes specifically
 out.privateLanes=[...document.querySelectorAll('.lane')]
   .filter(l=>/private/i.test(l.textContent))
   .map(l=>({t:l.textContent.trim(),r:ratio(l),c:getComputedStyle(l).color}));

 return out;})()
"""
print(json.dumps(cdp.ev(ws, JS), indent=1))

# ---- school chip stagger, caught mid-flight
STAG = r"""
(async()=>{
 const f=document.querySelector('#field');
 const chips=[...document.querySelectorAll('.school')];
 f.classList.remove('in');
 chips.forEach(c=>{c.style.transition='none';c.style.opacity='';c.style.transform='';});
 void f.offsetWidth;
 chips.forEach(c=>{c.style.transition='';});
 void f.offsetWidth;
 const before=chips.slice(0,8).map(c=>+getComputedStyle(c).opacity.slice(0,4));
 f.classList.add('in');
 await new Promise(r=>setTimeout(r,120));
 const mid=chips.slice(0,8).map(c=>+getComputedStyle(c).opacity.slice(0,4));
 await new Promise(r=>setTimeout(r,900));
 const after=chips.slice(0,8).map(c=>+getComputedStyle(c).opacity.slice(0,4));
 return {before,mid,after,
   spread:+(Math.max(...mid)-Math.min(...mid)).toFixed(3),
   monotonic: mid.every((v,i,a)=>i===0||v<=a[i-1]+0.02)};
})()
"""
print("STAGGER:", json.dumps(cdp.ev(ws, STAG, awaitp=True), indent=1))
