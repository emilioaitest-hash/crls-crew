import cdp, json
cdp.launch(2560, 1440)
ws = cdp.connect()
print("href:", cdp.new_page(ws, 'http://localhost:4188/crls-crew/', 2560, 1440))
JS = r"""
(()=>{
 const out={};const R=e=>e.getBoundingClientRect();
 out.quoteCount=document.querySelectorAll('.quote').length;
 // aside leader dead space stats
 const dds=[...document.querySelectorAll('.facts dd')];
 const leaders=dds.map(d=>{const r=R(d);const g=document.createRange();g.selectNodeContents(d);
   const rs=[...g.getClientRects()];return r.width-(rs.length?rs[0].width:0);});
 out.leader={n:leaders.length,mean:+(leaders.reduce((a,b)=>a+b,0)/leaders.length).toFixed(0),
   min:+Math.min(...leaders).toFixed(0),max:+Math.max(...leaders).toFixed(0)};
 // glyph density summary
 function ga(root){let a=0;const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let n;
  while((n=w.nextNode())){if(!n.nodeValue.trim())continue;const g=document.createRange();
  g.selectNodeContents(n);for(const r of g.getClientRects())a+=r.width*r.height;}return a;}
 const rows=[...document.querySelectorAll('.tl-item')];
 const dens=rows.map(it=>{const a=it.querySelector('.tl-aside'),b=it.children[1];
   const ar=R(a),br=R(b);
   return [ (ga(a)/(ar.width*ar.height))*100, (ga(b)/(br.width*br.height))*100 ];});
 out.density={asideMean:+(dens.reduce((s,d)=>s+d[0],0)/dens.length).toFixed(1),
   bodyMean:+(dens.reduce((s,d)=>s+d[1],0)/dens.length).toFixed(1)};
 // boat stage at mobile? report desktop min-height
 const bs=document.querySelector('.boat-stage');
 out.boat={ar:getComputedStyle(bs).aspectRatio,minH:getComputedStyle(bs).minHeight,
   w:+R(bs).width.toFixed(0),h:+R(bs).height.toFixed(0)};
 // hull fill inside stage
 const cv=document.querySelector('#fleet-canvas');
 out.canvas=cv?{w:+R(cv).width.toFixed(0),h:+R(cv).height.toFixed(0)}:null;
 // 0.95s elements
 out.slow=[...document.querySelectorAll('*')].filter(e=>getComputedStyle(e).transitionDuration.startsWith('0.95'))
   .map(e=>e.className.toString().slice(0,40));
 // count reveal elements sharing identical gesture
 const m={};
 for(const e of document.querySelectorAll('[data-reveal]')){
   const cs=getComputedStyle(e);m[cs.transitionDuration+'/'+cs.transitionDelay]=(m[cs.transitionDuration+'/'+cs.transitionDelay]||0)+1;}
 out.revealBuckets=m;
 out.revealTotal=document.querySelectorAll('[data-reveal]').length;
 // how many reveal elements have zero delay (undifferentiated)
 out.zeroDelay=[...document.querySelectorAll('[data-reveal]')]
   .filter(e=>getComputedStyle(e).transitionDelay.startsWith('0s')).length;
 return out;})()
"""
print(json.dumps(cdp.ev(ws, JS), indent=1))
