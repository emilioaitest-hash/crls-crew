import cdp, json
cdp.launch(2560, 1440)
ws = cdp.connect()
print("href:", cdp.new_page(ws, 'http://localhost:4188/crls-crew/', 2560, 1440))
JS = r"""
(()=>{
 const out={};const R=e=>e.getBoundingClientRect();
 // duplication check: last timeline row vs revival band
 const rows=[...document.querySelectorAll('#return .tl-item')];
 const last=rows[rows.length-1];
 const rev=document.querySelector('.hinge--minor');
 out.dup={
   lastRowYear:last.querySelector('.tl-year').textContent.trim(),
   lastRowTitle:last.querySelector('.tl-title').textContent.trim(),
   lastRowBody:last.querySelector('.tl-body').textContent.replace(/\s+/g,' ').trim(),
   lastRowIsPull:last.classList.contains('pull'),
   lastRowBottom:+R(last).bottom.toFixed(0),
   revivalTop:+R(rev).top.toFixed(0),
   pxApart:+(R(rev).top-R(last).bottom).toFixed(0),
   revivalHead:rev.querySelector('.hinge-line').textContent.replace(/\s+/g,' ').trim(),
   revivalYear:rev.querySelector('.hinge-year').textContent.trim(),
   revivalNums:[...rev.querySelectorAll('.p-n')].map(e=>e.textContent.trim()),
   revivalLabels:[...rev.querySelectorAll('.p-l')].map(e=>e.textContent.trim()),
 };
 // do the numbers 12/50/5/5 also appear in the row body?
 const b=out.dup.lastRowBody.toLowerCase();
 out.dup.bodyMentions={twelve:b.includes('twelve'),fifty:b.includes('fifty'),
   five_boats:b.includes('five boats'),five_races:b.includes('five races')};
 // section-level right edges: is the timeline now short?
 const blocks=[['#then .timeline','then timeline'],['#then .split','then split'],
   ['#return .timeline','return timeline'],['#return .wrap','return wrap'],
   ['.progression','revival progression'],['#chart','chart']];
 out.edges=blocks.map(([s,n])=>{const e=document.querySelector(s);
   if(!e)return{n,missing:1};const r=R(e);return{n,right:+r.right.toFixed(0),w:+r.width.toFixed(0)};});
 // reduced motion
 out.hasReducedBlock = [...document.styleSheets].some(ss=>{try{
   return [...ss.cssRules].some(r=>r.conditionText&&/prefers-reduced-motion/.test(r.conditionText));
 }catch(e){return false}});
 return out;})()
"""
print(json.dumps(cdp.ev(ws, JS), indent=1))
box = cdp.ev(ws, "(()=>{const r=document.querySelector('#return .tl-item:last-child').getBoundingClientRect();window.scrollTo(0,window.scrollY+r.top-120);return 1})()")
import time; time.sleep(1.0)
cdp.shot(ws, "/Users/AISandbox/crls-crew/renders/r3-dup.png")
print("shot dup")
