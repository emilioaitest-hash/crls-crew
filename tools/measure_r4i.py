"""R4 pass I: duplication scan, road-to-final, new-code contrast, motion buckets."""
import cdp, json

cdp.launch(2560, 1440)
ws = cdp.connect()
print("href:", cdp.new_page(ws, 'http://localhost:4188/crls-crew/', 2560, 1440))

JS = r"""
(()=>{
 const out={};const R=e=>e.getBoundingClientRect();
 const norm=s=>s.replace(/\s+/g,' ').trim().toLowerCase();

 // ---- duplication: does the 2000 revival story appear more than once?
 const body=norm(document.body.textContent);
 out.phrase={};
 for(const p of ['twelve students','no equipment','fifty kids','five boats','50 rowers',
                 'twelve students, no equipment']){
   out.phrase[p]=(body.match(new RegExp(p.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'),'g'))||[]).length;}
 // block-level: any two blocks sharing a long shingle
 const blocks=[...document.querySelectorAll('.tl-item, .hinge, .hinge--minor, .thesis, .quote, section > .wrap > p')]
   .map(e=>({cls:(e.className||'').slice(0,26),t:norm(e.textContent)}))
   .filter(b=>b.t.length>60);
 const dups=[];
 for(let i=0;i<blocks.length;i++)for(let j=i+1;j<blocks.length;j++){
   const a=blocks[i].t.split(' '),b=blocks[j].t.split(' ');
   const sh=new Set(); for(let k=0;k+5<=a.length;k++)sh.add(a.slice(k,k+5).join(' '));
   let hit=0; for(let k=0;k+5<=b.length;k++) if(sh.has(b.slice(k,k+5).join(' ')))hit++;
   if(hit>2)dups.push({a:blocks[i].cls,b:blocks[j].cls,shared5grams:hit});}
 out.blockDuplicates=dups;

 // ---- road to final
 out.roads=[...document.querySelectorAll('.road, .rounds, .progress')].map(r=>({
   cls:r.className,items:[...r.querySelectorAll('li')].map(li=>li.textContent.replace(/\s+/g,' ').trim())}));

 // ---- contrast of code added THIS round
 function lum(c){const m=c.match(/[\d.]+/g).map(Number);
  const f=v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4);};
  return 0.2126*f(m[0])+0.7152*f(m[1])+0.0722*f(m[2]);}
 function bgOf(el){let e=el;while(e){const c=getComputedStyle(e).backgroundColor;
  if(c&&c!=='rgba(0, 0, 0, 0)'&&!/, *0\)$/.test(c))return c;e=e.parentElement;}return 'rgb(10,12,14)';}
 function ratio(el){const a=lum(getComputedStyle(el).color),b=lum(bgOf(el));
  return +(((Math.max(a,b)+0.05)/(Math.min(a,b)+0.05))).toFixed(2);}
 out.newCode={};
 for(const sel of ['.boat-state','.boat-id em','.boat-id b','.road li','.road b','.road span']){
  const els=[...document.querySelectorAll(sel)];
  if(!els.length){out.newCode[sel]='NONE';continue;}
  out.newCode[sel]=els.map(e=>({t:e.textContent.trim().slice(0,26),r:ratio(e),
    c:getComputedStyle(e).color,fs:getComputedStyle(e).fontSize}));}

 // ---- motion buckets
 const b={};
 for(const el of document.querySelectorAll('[data-reveal]')){
  const cs=getComputedStyle(el);const k=cs.transitionDuration+' | '+cs.transitionDelay.split(',')[0];
  b[k]=(b[k]||0)+1;}
 out.motion={total:document.querySelectorAll('[data-reveal]').length,buckets:b,
   undifferentiated:b['0.55s, 0.55s | 0s']||0};
 return out;})()
"""
print(json.dumps(cdp.ev(ws, JS), indent=1))
