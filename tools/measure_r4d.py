"""R4 pass D: observe the school-chip reveal as it genuinely fires on scroll.
No class manipulation - just scroll #field into view and sample opacity."""
import cdp, json, time

cdp.launch(2560, 1440)
ws = cdp.connect()
# navigate WITHOUT the full-page scroll walk, so #field has not revealed yet
ws.call("Emulation.setDeviceMetricsOverride", width=2560, height=1440,
        deviceScaleFactor=1, mobile=False)
ws.call("Page.enable"); ws.call("Runtime.enable")
ws.call("Page.navigate", url='http://localhost:4188/crls-crew/')
time.sleep(4)
print("href:", cdp.ev(ws, "location.href"))
print("fields in? ", cdp.ev(ws, "document.querySelector('#field')?.classList.contains('in')"))
print("chip opacity pre-scroll:", cdp.ev(ws,
    "[...document.querySelectorAll('.school')].slice(0,6).map(e=>getComputedStyle(e).opacity)"))

# scroll #field into view and sample the transition in flight
JS = r"""
(async()=>{
 const f=document.querySelector('#field');
 const chips=[...document.querySelectorAll('.school')];
 const samp=()=>chips.slice(0,10).map(c=>+(+getComputedStyle(c).opacity).toFixed(2));
 const pre=samp();
 f.scrollIntoView({block:'center'});
 const frames=[];
 for(let i=0;i<10;i++){ await new Promise(r=>setTimeout(r,60)); frames.push(samp()); }
 await new Promise(r=>setTimeout(r,1200));
 const settled=samp();
 // spread at each frame = evidence of a visible stagger
 const spreads=frames.map(f=>+(Math.max(...f)-Math.min(...f)).toFixed(2));
 return {inClass:f.classList.contains('in'),pre,frames,settled,
   maxSpread:Math.max(...spreads),spreads,
   dur:getComputedStyle(chips[0]).transitionDuration,
   delays:chips.slice(0,10).map(c=>getComputedStyle(c).transitionDelay)};
})()
"""
print(json.dumps(cdp.ev(ws, JS, awaitp=True), indent=1))
