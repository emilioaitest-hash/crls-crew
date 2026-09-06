"""R5 comprehensive independent measurement. Live site, cache-busted.

Everything here is measured against TEXT NODES or trimmed rendered lines.
Nothing trusts a container-level Range, which is how audit.py gets 74.2%.
"""
import sys, json, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import cdp  # noqa: E402

BASE = "https://emilioaitest-hash.github.io/crls-crew/"
W = int(sys.argv[1]) if len(sys.argv) > 1 else 2560
H = int(sys.argv[2]) if len(sys.argv) > 2 else 1440
URL = BASE + f"?r5full={int(time.time())}"

cdp.launch(W, H)
c = cdp.connect()
print("href:", cdp.new_page(c, URL, W, H, wait=6.0, scroll_all=True))
for sec in ('then', 'record', 'fleet', 'field'):
    cdp.ev(c, f"document.getElementById('{sec}') && document.getElementById('{sec}').scrollIntoView()")
    time.sleep(1.0)
cdp.ev(c, "document.getElementById('then') && document.getElementById('then').scrollIntoView()")
time.sleep(1.8)
print("href confirm:", cdp.ev(c, "location.href"), "| fonts:", cdp.ev(c, "document.fonts.status"))

EXPR = r"""
(() => {
  const out={}, R=e=>e.getBoundingClientRect();

  /* ---------- contrast: EVERY text-bearing element, real backgrounds ---------- */
  const lum=rgb=>{const v=rgb.match(/[\d.]+/g).slice(0,3).map(n=>{let x=n/255;
    return x<=0.03928?x/12.92:Math.pow((x+0.055)/1.055,2.4);});
    return 0.2126*v[0]+0.7152*v[1]+0.0722*v[2];};
  const ratio=(a,b)=>{const l1=lum(a),l2=lum(b);const[h,l]=l1>l2?[l1,l2]:[l2,l1];
    return +((h+0.05)/(l+0.05)).toFixed(2);};
  const effBg=el=>{let n=el;while(n&&n!==document.documentElement){
    const bg=getComputedStyle(n).backgroundColor;
    if(bg&&bg!=='rgba(0, 0, 0, 0)'&&!/,\s*0\)$/.test(bg))return bg;n=n.parentElement;}
    return 'rgb(10, 12, 14)';};
  const px=s=>parseFloat(s)||0;

  const texts=[];
  for(const el of document.querySelectorAll('body *')){
    // direct text content only
    let own=''; for(const n of el.childNodes) if(n.nodeType===3) own+=n.nodeValue;
    if(!own.trim()) continue;
    const cs=getComputedStyle(el);
    if(cs.visibility==='hidden'||cs.display==='none') continue;
    const r=R(el); if(!r.width||!r.height) continue;
    if(px(cs.opacity)<0.05) continue;
    const cr=ratio(cs.color,effBg(el));
    const fs=px(cs.fontSize), fw=parseInt(cs.fontWeight)||400;
    const large = fs>=24 || (fs>=18.66 && fw>=700);
    texts.push({sel:el.tagName.toLowerCase()+'.'+(el.className&&el.className.baseVal===undefined?String(el.className).trim().split(/\s+/).join('.'):''),
      color:cs.color, bg:effBg(el), ratio:cr, fs:+fs.toFixed(1), fw, large,
      txt:own.trim().replace(/\s+/g,' ').slice(0,42), op:+cs.opacity});
  }
  out.textCount=texts.length;
  // exclude the deliberately-ghosted silence numeral from the AA gate but report it
  out.silenceCount=texts.filter(t=>/silence-count/.test(t.sel)).map(t=>({r:t.ratio,c:t.color,txt:t.txt}));
  const gate=texts.filter(t=>!/silence-count/.test(t.sel));
  out.aaFails=gate.filter(t=>t.ratio < (t.large?3:4.5))
    .map(t=>({sel:t.sel,ratio:t.ratio,color:t.color,fs:t.fs,large:t.large,txt:t.txt}));
  out.aaFailCount=out.aaFails.length;
  // anything resolving to the retired --grey-2 #5b646d = rgb(91,100,109)
  out.grey2Text=texts.filter(t=>t.color==='rgb(91, 100, 109)')
    .map(t=>({sel:t.sel,ratio:t.ratio,txt:t.txt}));
  out.minRatio=Math.min(...gate.map(t=>t.ratio));
  out.worst=gate.slice().sort((a,b)=>a.ratio-b.ratio).slice(0,8)
    .map(t=>({sel:t.sel,r:t.ratio,fs:t.fs,txt:t.txt}));
  // named components
  out.byComp={};
  for(const s of ['.src','.note','.lane','.school','.bar-year','.facts dt','.facts dd',
                  '.boat-state','.credit','.plate figcaption','.silence-marks','.tl-title','.view-tab']){
    const e=[...document.querySelectorAll(s)].filter(x=>x.textContent.trim());
    if(!e.length){out.byComp[s]=null;continue;}
    const rs=e.map(x=>ratio(getComputedStyle(x).color,effBg(x)));
    out.byComp[s]={n:e.length,min:Math.min(...rs),max:Math.max(...rs)};
  }

  /* ---------- CPL from trimmed rendered lines ---------- */
  const cplOf=el=>{
    const r=document.createRange(); r.selectNodeContents(el);
    const rects=[...r.getClientRects()].filter(c=>c.height>4&&c.width>2);
    const chars=el.textContent.trim().replace(/\s+/g,' ').length;
    return rects.length?{cpl:Math.round(chars/rects.length),lines:rects.length,chars,
      boxW:Math.round(R(el).width),fs:getComputedStyle(el).fontSize}:null;};
  out.cpl={};
  for(const s of ['.narrow--flush p','.tl-body p','.split .lead','.note','.hinge-body p','.thesis p']){
    const els=[...document.querySelectorAll(s)].filter(e=>e.textContent.trim().length>60);
    if(!els.length){out.cpl[s]=null;continue;}
    const m=els.map(cplOf).filter(Boolean);
    out.cpl[s]={n:m.length,mean:+(m.reduce((a,b)=>a+b.cpl,0)/m.length).toFixed(0),
      max:Math.max(...m.map(x=>x.cpl)),min:Math.min(...m.map(x=>x.cpl)),
      boxW:m[0].boxW,fs:m[0].fs};
  }

  /* ---------- .facts dd dead space: box width vs actual text width ---------- */
  const dds=[...document.querySelectorAll('.facts dd')];
  out.dd=dds.map(d=>{const rr=R(d);const g=document.createRange();g.selectNodeContents(d);
    const rects=[...g.getClientRects()].filter(x=>x.width>1);
    const widest=rects.length?Math.max(...rects.map(x=>x.width)):0;
    return {boxW:Math.round(rr.width),textW:Math.round(widest),dead:Math.round(rr.width-widest),
      lines:rects.length,txt:d.textContent.trim().slice(0,50)};});
  out.ddStats={n:out.dd.length,meanBoxW:Math.round(out.dd.reduce((s,x)=>s+x.boxW,0)/out.dd.length),
    meanTextW:Math.round(out.dd.reduce((s,x)=>s+x.textW,0)/out.dd.length),
    meanDead:Math.round(out.dd.reduce((s,x)=>s+x.dead,0)/out.dd.length),
    meanFillPct:+(out.dd.reduce((s,x)=>s+x.textW/x.boxW,0)/out.dd.length*100).toFixed(1)};
  out.factsGrid=(()=>{const f=document.querySelector('.facts');const cs=getComputedStyle(f);
    return {w:Math.round(R(f).width),maxW:cs.maxWidth,cols:cs.gridTemplateColumns,gap:cs.columnGap};})();

  /* ---------- restatement: tokenise each dd against prose in its OWN row ---------- */
  const STOP=new Set(('the a an and or of in on at to for by with from as is was were be been it its this that '+
    'their his her they them he she we our us you your i not no but if then than so all any each which who whom '+
    'what when where how why can could would should may might must have has had do does did are am s t re ve ll d'
    ).split(' '));
  const tok=s=>s.toLowerCase().replace(/[’']/g,'').replace(/[^a-z0-9\s]/g,' ')
    .split(/\s+/).filter(w=>w&&w.length>2&&!STOP.has(w));
  out.pairs=[];
  for(const row of document.querySelectorAll('.tl-item')){
    const body=row.querySelector('.tl-body'); if(!body) continue;
    const prose=new Set(tok(body.textContent));
    const year=(row.querySelector('.tl-year')||{textContent:'?'}).textContent.trim();
    const dts=[...row.querySelectorAll('.facts dt')], dv=[...row.querySelectorAll('.facts dd')];
    for(let i=0;i<dv.length;i++){
      const t=tok(dv[i].textContent);
      if(!t.length) continue;
      const hit=t.filter(w=>prose.has(w)).length;
      out.pairs.push({year,dt:(dts[i]||{textContent:''}).textContent.trim(),
        dd:dv[i].textContent.trim().slice(0,70),
        tokens:t.length,contained:+(hit/t.length).toFixed(2)});
    }
  }
  out.pairStats={total:out.pairs.length,
    restating:out.pairs.filter(p=>p.contained>=0.5).length,
    restatePct:+(out.pairs.filter(p=>p.contained>=0.5).length/out.pairs.length*100).toFixed(1)};

  /* ---------- --river actually used? ---------- */
  const rv=getComputedStyle(document.documentElement).getPropertyValue('--river').trim();
  const rvl=getComputedStyle(document.documentElement).getPropertyValue('--river-lit').trim();
  out.river={declared:rv,lit:rvl,users:[]};
  for(const el of document.querySelectorAll('body *')){
    const cs=getComputedStyle(el);
    for(const prop of ['color','backgroundColor','borderTopColor','boxShadow','textShadow','backgroundImage','fill','stroke']){
      const v=cs[prop]||'';
      if(/45,\s*74,\s*92/.test(v)||/74,\s*122,\s*148/.test(v)){
        out.river.users.push({sel:el.tagName.toLowerCase()+'.'+String(el.className).trim().split(/\s+/).join('.'),
          prop, val:String(v).slice(0,70)});}
    }
  }
  out.river.litUsed=out.river.users.some(u=>/74,\s*122,\s*148/.test(u.val));
  out.river.nUsers=out.river.users.length;

  /* ---------- structure / content ---------- */
  out.docW=document.documentElement.scrollWidth; out.innerW=window.innerWidth;
  out.overflow=out.docW>out.innerW;
  out.years=[...document.querySelectorAll('.tl-year')].map(e=>e.textContent.trim());
  out.has1903=out.years.includes('1903');
  const bt=document.body.innerText;
  out.p1903={ '5:33': (bt.match(/5:33/g)||[]).length, 'nine seconds':(bt.match(/nine seconds/gi)||[]).length,
    'interscholastic':(bt.match(/interscholastic/gi)||[]).length };
  out.hingeText=[...document.querySelectorAll('.hinge')].map(h=>h.textContent.replace(/\s+/g,' ').trim().slice(0,600));
  out.rightEdges={}; for(const s of ['.timeline','.split','#chart','.boat-stage','.foot-inner','#field','.progression','.thesis','.results'])
    {const e=document.querySelector(s); out.rightEdges[s]=e?Math.round(R(e).right):null;}
  out.edgeSet=[...new Set(Object.values(out.rightEdges).filter(Boolean))];
  // reveals
  const rev=[...document.querySelectorAll('[data-reveal],.reveal,.tl-item,.school,.result,.bar-col')];
  const sig={};
  for(const e of rev){const cs=getComputedStyle(e);
    const k=cs.transitionDuration+'|'+cs.transitionDelay; sig[k]=(sig[k]||0)+1;}
  out.revealSigs=Object.entries(sig).sort((a,b)=>b[1]-a[1]).slice(0,8);
  out.revealTotal=rev.length;
  return out;
})()
"""
r = cdp.ev(c, EXPR)
if isinstance(r, dict) and '__error' in r:
    print(r); sys.exit(1)
json.dump(r, open(f"/tmp/r5_{W}.json", "w"), indent=1)

print(f"\n############ R5 FULL SWEEP {W}x{H} ############")
print(f"\n-- CONTRAST: {r['textCount']} text-bearing elements swept, real bg resolution")
print(f"   AA failures: {r['aaFailCount']}")
for f in r['aaFails'][:12]: print(f"     {f['ratio']:5.2f}:1  {f['sel'][:42]:42s} fs{f['fs']} '{f['txt'][:32]}'")
print(f"   elements resolving to retired --grey-2 (#5b646d): {len(r['grey2Text'])}")
for g in r['grey2Text'][:8]: print(f"     {g['ratio']}:1 {g['sel'][:50]} '{g['txt'][:30]}'")
print(f"   min ratio (excl. silence-count): {r['minRatio']}:1")
print("   worst 8:")
for w_ in r['worst']: print(f"     {w_['r']:5.2f}:1  {w_['sel'][:44]:44s} '{w_['txt'][:30]}'")
print(f"   silence-count (intentional ghost): {r['silenceCount']}")
print("   by component:")
for k, v in r['byComp'].items():
    print(f"     {k:22s} {('n='+str(v['n'])+'  '+str(v['min'])+'–'+str(v['max'])+':1') if v else 'absent'}")

print(f"\n-- CPL (trimmed rendered lines)")
for k, v in r['cpl'].items():
    if v: print(f"   {k:20s} n={v['n']:2d}  mean {v['mean']:3d}  range {v['min']}–{v['max']}  box {v['boxW']}px  {v['fs']}")

print(f"\n-- .facts dd dead space   grid: {r['factsGrid']}")
s = r['ddStats']
print(f"   n={s['n']}  mean box {s['meanBoxW']}px  mean text {s['meanTextW']}px  mean DEAD {s['meanDead']}px  fill {s['meanFillPct']}%")

print(f"\n-- RESTATEMENT: {r['pairStats']}")
print("   restating pairs (>=50% contained in own row's prose):")
for p in [x for x in r['pairs'] if x['contained'] >= 0.5]:
    print(f"     {p['year']:6s} {p['contained']:.2f}  {p['dt'][:20]:20s} | {p['dd'][:52]}")

print(f"\n-- --river: declared {r['river']['declared']} / lit {r['river']['lit']}")
print(f"   users: {r['river']['nUsers']}   --river-lit used: {r['river']['litUsed']}")
for u in r['river']['users'][:8]: print(f"     {u['sel'][:40]:40s} {u['prop']:16s} {u['val'][:48]}")

print(f"\n-- STRUCTURE")
print(f"   docW {r['docW']} vs innerW {r['innerW']}  overflow={r['overflow']}")
print(f"   years {r['years']}   1903 present: {r['has1903']}   1903 phrases {r['p1903']}")
print(f"   right edges {r['edgeSet']}  ({r['rightEdges']})")
print(f"   reveal signatures (n={r['revealTotal']}): {r['revealSigs']}")
print(f"\n-- HINGE TEXT")
for h in r['hingeText']: print(f"   {h[:560]}\n")
