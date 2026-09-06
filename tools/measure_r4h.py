"""R4 pass H: definitive CPL with TRIMMED rendered lines, measured both before
and after webfonts resolve — to test whether round 3's CPL numbers were taken
against fallback metrics."""
import cdp, json, time

cdp.launch(2560, 1440)
ws = cdp.connect()
ws.call("Emulation.setDeviceMetricsOverride", width=2560, height=1440,
        deviceScaleFactor=1, mobile=False)
ws.call("Page.enable"); ws.call("Runtime.enable")
ws.call("Page.navigate", url='http://localhost:4188/crls-crew/')
time.sleep(4)

MEASURE = r"""
(()=>{
 function trimmedLines(el){
  const walk=document.createTreeWalker(el,NodeFilter.SHOW_TEXT);
  let n; const chars=[];
  while((n=walk.nextNode())){
    const t=n.nodeValue;
    for(let i=0;i<t.length;i++){
      const rg=document.createRange(); rg.setStart(n,i); rg.setEnd(n,i+1);
      const r=rg.getBoundingClientRect();
      if(r.width<=0)continue;              // skip collapsed whitespace
      chars.push({c:t[i],top:Math.round(r.top),left:r.left,right:r.right});
    }}
  if(!chars.length)return null;
  const byTop={};
  for(const c of chars){(byTop[c.top]=byTop[c.top]||[]).push(c);}
  return Object.keys(byTop).map(top=>{
    const cs=byTop[top].sort((a,b)=>a.left-b.left);
    const txt=cs.map(x=>x.c).join('').replace(/^\s+|\s+$/g,'');
    return {n:txt.length,txt,
      px:+(Math.max(...cs.map(x=>x.right))-Math.min(...cs.map(x=>x.left))).toFixed(0)};
  }).sort((a,b)=>b.n-a.n);
 }
 function rep(sel){
  const el=document.querySelector(sel); if(!el)return null;
  const ls=trimmedLines(el); if(!ls||!ls.length)return null;
  const cs=getComputedStyle(el);
  return {sel,boxW:+el.getBoundingClientRect().width.toFixed(0),fs:cs.fontSize,
    fam:cs.fontFamily.split(',')[0].replace(/["']/g,''),
    maxCPL:ls[0].n,widestPx:ls[0].px,sample:ls[0].txt.slice(0,72)};
 }
 return {fontStatus:document.fonts.status,
   lead:rep('.split .lead'), tlBody:rep('.tl-body p'),
   flush:rep('.narrow--flush p'), note:rep('.note')};
})()
"""

print("=== IMMEDIATELY AFTER LOAD ===")
print(json.dumps(cdp.ev(ws, MEASURE), indent=1))
cdp.ev(ws, "document.fonts.ready.then(()=>1)", awaitp=True)
time.sleep(1.0)
print("\n=== AFTER document.fonts.ready ===")
print(json.dumps(cdp.ev(ws, MEASURE), indent=1))
