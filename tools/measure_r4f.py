"""R4 pass F: no-JS rendering. Disable script execution BEFORE navigating."""
import cdp, json, time

cdp.launch(1600, 900)
ws = cdp.connect()
ws.call("Emulation.setDeviceMetricsOverride", width=1600, height=900,
        deviceScaleFactor=1, mobile=False)
ws.call("Page.enable"); ws.call("Runtime.enable")
ws.call("Emulation.setScriptExecutionDisabled", value=True)
ws.call("Page.navigate", url='http://localhost:4188/crls-crew/')
time.sleep(4)

# Runtime.evaluate still works for the inspector even with page scripts disabled
JS = r"""
(()=>{
 const out={};const R=e=>e.getBoundingClientRect();
 const t=e=>e?e.textContent.replace(/\s+/g,' ').trim():null;
 out.title=document.title;
 out.htmlClass=document.documentElement.className;
 out.heroLines=[...document.querySelectorAll('.hero h1, .hero-line, .mask span, h1')]
   .slice(0,6).map(e=>({cls:e.className,txt:t(e).slice(0,70),
     w:+R(e).width.toFixed(0),h:+R(e).height.toFixed(0),
     op:getComputedStyle(e).opacity,vis:getComputedStyle(e).visibility}));
 out.heroStats=[...document.querySelectorAll('.hero-stat')].map(e=>({
   txt:t(e).slice(0,60),num:t(e.querySelector('.hero-stat-n, .stat-n, b, strong, .num')),
   op:getComputedStyle(e).opacity}));
 // any element still showing a literal 0 counter
 out.counters=[...document.querySelectorAll('[data-count], .count, .hero-stat')]
   .map(e=>({tag:e.tagName,cls:e.className,dc:e.getAttribute('data-count'),txt:t(e).slice(0,50)}));
 out.timelineRows=document.querySelectorAll('.tl-item').length;
 out.chartBars=document.querySelectorAll('.bar').length;
 out.results=document.querySelectorAll('.result').length;
 out.schools=document.querySelectorAll('.school').length;
 out.facts=document.querySelectorAll('.facts dt').length;
 out.fleet=document.querySelectorAll('.boat').length;
 // is anything left invisible because reveal never ran?
 let hidden=0,total=0;
 for(const el of document.querySelectorAll('[data-reveal]')){
   total++; const cs=getComputedStyle(el);
   if(+cs.opacity<0.05) hidden++;}
 out.reveal={total,hidden};
 out.bodyTextLen=document.body.textContent.replace(/\s+/g,' ').trim().length;
 out.docW=document.documentElement.scrollWidth; out.innerW=innerWidth;
 return out;})()
"""
print(json.dumps(cdp.ev(ws, JS), indent=1))
cdp.shot(ws, "/Users/AISandbox/crls-crew/renders/r4-nojs.png")
