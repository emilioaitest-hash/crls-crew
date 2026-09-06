import cdp, json
cdp.launch(2560, 1440)
ws = cdp.connect()
print("href:", cdp.new_page(ws, 'http://localhost:4188/crls-crew/', 2560, 1440))
JS = r"""
(()=>{
 const out={};const R=e=>e.getBoundingClientRect();
 // --- 2020 label clipping
 const bn=document.querySelector('.bar-none');
 const col=bn.closest('.bar-col');
 const track=col.querySelector('.bar-track');
 // full text width if unclipped
 const probe=document.createElement('span');
 const cs=getComputedStyle(bn);
 probe.style.cssText=`position:absolute;visibility:hidden;white-space:nowrap;
   font-family:${cs.fontFamily};font-size:${cs.fontSize};letter-spacing:${cs.letterSpacing};
   text-transform:${cs.textTransform}`;
 probe.textContent=bn.textContent;document.body.appendChild(probe);
 const natural=probe.getBoundingClientRect().width;probe.remove();
 const br=R(bn),cr=R(col),tr=R(track);
 out.label2020={text:bn.textContent,naturalTextLen:+natural.toFixed(0),
   renderedH:+br.height.toFixed(0),renderedW:+br.width.toFixed(0),
   labelTop:+br.top.toFixed(0),labelBottom:+br.bottom.toFixed(0),
   colTop:+cr.top.toFixed(0),colBottom:+cr.bottom.toFixed(0),
   trackTop:+tr.top.toFixed(0),trackBottom:+tr.bottom.toFixed(0),
   clippedTop:+(tr.top-br.top).toFixed(0),
   overflowsTrack: br.top < tr.top,
   colOverflow:getComputedStyle(col).overflow,
   trackOverflow:getComputedStyle(track).overflow,
   chartOverflow:getComputedStyle(document.querySelector('#chart')).overflow};
 // does the year label collide?
 const yr=col.querySelector('.bar-year');
 const yrr=R(yr);
 out.label2020.yearTop=+yrr.top.toFixed(0);
 out.label2020.gapToYear=+(yrr.top-br.bottom).toFixed(0);
 out.label2020.overlapsYear = br.bottom > yrr.top;

 // --- school chip transition actually animates?
 const s=document.querySelector('.school');
 const scs=getComputedStyle(s);
 out.school={transition:scs.transition,duration:scs.transitionDuration,
   delay:scs.transitionDelay,property:scs.transitionProperty,
   opacity:scs.opacity,transform:scs.transform};
 // compare to a reveal element that does animate
 const t=document.querySelector('.tl-item');
 const tcs=getComputedStyle(t);
 out.tlItem={duration:tcs.transitionDuration,delay:tcs.transitionDelay,
   property:tcs.transitionProperty};
 // is .school even a reveal target?
 out.schoolIsReveal=!!document.querySelector('.school[data-reveal]');
 out.fieldIsReveal=!!document.querySelector('#field[data-reveal]');
 out.schoolParentReveal=document.querySelector('.school').closest('[data-reveal]')?.className;
 return out;})()
"""
print(json.dumps(cdp.ev(ws, JS), indent=1))
