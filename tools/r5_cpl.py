"""R5 CPL, R4's exact method: reconstruct rendered lines char-by-char, trim, and
report the WIDEST line (maxCPL) — the number R4 scored .narrow--flush at 77 on.
Reporting mean instead of max is how a wide block can look compliant.
"""
import sys, json, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import cdp  # noqa: E402

W = int(sys.argv[1]) if len(sys.argv) > 1 else 2560
H = int(sys.argv[2]) if len(sys.argv) > 2 else 1440
URL = "https://emilioaitest-hash.github.io/crls-crew/" + f"?r5cpl={int(time.time())}"
cdp.launch(W, H)
c = cdp.connect()
print("href:", cdp.new_page(c, URL, W, H, wait=6.0, scroll_all=True))
cdp.ev(c, "document.fonts.ready.then(()=>1)", awaitp=True)
time.sleep(1.0)
print("href confirm:", cdp.ev(c, "location.href"), "fonts:", cdp.ev(c, "document.fonts.status"))

JS = r"""
(()=>{
 function trimmedLines(el){
  const walk=document.createTreeWalker(el,NodeFilter.SHOW_TEXT);
  let n; const chars=[];
  while((n=walk.nextNode())){
    const t=n.nodeValue;
    for(let i=0;i<t.length;i++){
      const rg=document.createRange(); rg.setStart(n,i); rg.setEnd(n,i+1);
      const r=rg.getBoundingClientRect();
      if(r.width<=0)continue;
      chars.push({c:t[i],top:Math.round(r.top),left:r.left,right:r.right});
    }}
  if(!chars.length)return null;
  const byTop={};
  for(const c of chars){(byTop[c.top]=byTop[c.top]||[]).push(c);}
  return Object.keys(byTop).map(top=>{
    const cs=byTop[top].sort((a,b)=>a.left-b.left);
    const txt=cs.map(x=>x.c).join('').replace(/^\s+|\s+$/g,'');
    return {n:txt.length,txt,px:+(Math.max(...cs.map(x=>x.right))-Math.min(...cs.map(x=>x.left))).toFixed(0)};
  }).sort((a,b)=>b.n-a.n);
 }
 // every prose block on the page, ranked by widest rendered line
 const sels='.split .lead, .tl-body p, .narrow p, .narrow--flush p, .hinge-body p, .hinge-sub, .thesis p, .note';
 const all=[...document.querySelectorAll(sels)].filter(e=>e.textContent.trim().length>60).map(e=>{
   const ls=trimmedLines(e); if(!ls||!ls.length)return null;
   const cs=getComputedStyle(e);
   return {cls:(e.className||e.parentElement.className||'').toString().slice(0,26),
     boxW:Math.round(e.getBoundingClientRect().width), fs:cs.fontSize,
     maxCPL:ls[0].n, meanCPL:Math.round(ls.reduce((a,b)=>a+b.n,0)/ls.length),
     lines:ls.length, sample:ls[0].txt.slice(0,64)};
 }).filter(Boolean).sort((a,b)=>b.maxCPL-a.maxCPL);
 const byClass={};
 for(const b of all){ const k=b.cls||'(none)'; (byClass[k]=byClass[k]||[]).push(b.maxCPL); }
 return {ranked:all.slice(0,14), over68:all.filter(b=>b.maxCPL>68).length, total:all.length,
   byClass:Object.entries(byClass).map(([k,v])=>({cls:k,n:v.length,max:Math.max(...v),
     mean:Math.round(v.reduce((a,b)=>a+b,0)/v.length)})).sort((a,b)=>b.max-a.max)};
})()
"""
r = cdp.ev(c, JS)
print(f"\n=== CPL at {W}px — widest rendered line per block (R4's method) ===")
print(f"{'class':28s} {'box':>6s} {'fs':>6s} {'maxCPL':>7s} {'mean':>5s} {'lines':>6s}")
for b in r['ranked']:
    flag = "  << over 68" if b['maxCPL'] > 68 else ""
    print(f"{b['cls']:28s} {b['boxW']:6d} {b['fs']:>6s} {b['maxCPL']:7d} {b['meanCPL']:5d} {b['lines']:6d}{flag}")
print(f"\nblocks over 68 CPL: {r['over68']} / {r['total']}")
print("\nby class (max of widest lines):")
for x in r['byClass']:
    print(f"  {x['cls']:28s} n={x['n']:2d}  max {x['max']:3d}  mean {x['mean']:3d}")
