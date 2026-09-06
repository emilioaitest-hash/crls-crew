import cdp, json, sys

W = int(sys.argv[1]) if len(sys.argv) > 1 else 2560
H = int(sys.argv[2]) if len(sys.argv) > 2 else 1440

cdp.launch(W, H)
ws = cdp.connect()
href = cdp.new_page(ws, 'http://localhost:4188/crls-crew/', W, H)
print("### VIEWPORT", W, "x", H, "  href:", href)

JS = r"""
(() => {
  const out = {};
  const R = e => e.getBoundingClientRect();
  const sx = window.scrollX;

  // --- helper: rightmost painted ink inside an element (text + non-empty boxes)
  function inkRight(root){
    let max = -1e9;
    const walk = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = walk.nextNode())) {
      if (!n.nodeValue.trim()) continue;
      const rg = document.createRange(); rg.selectNodeContents(n);
      for (const r of rg.getClientRects()) if (r.width > 0) max = Math.max(max, r.right);
    }
    for (const el of root.querySelectorAll('*')) {
      const cs = getComputedStyle(el), r = R(el);
      if (r.width < 1 || r.height < 1) continue;
      const painted = (cs.backgroundColor !== 'rgba(0, 0, 0, 0)') ||
        ['Top','Right','Bottom','Left'].some(s =>
          cs['border'+s+'Width'] !== '0px' && cs['border'+s+'Style'] !== 'none');
      if (painted) max = Math.max(max, r.right);
    }
    return max;
  }
  function inkLeft(root){
    let min = 1e9;
    const walk = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = walk.nextNode())) {
      if (!n.nodeValue.trim()) continue;
      const rg = document.createRange(); rg.selectNodeContents(n);
      for (const r of rg.getClientRects()) if (r.width > 0) min = Math.min(min, r.left);
    }
    return min;
  }

  // ---------- P0.1 apparatus column ----------
  out.timeline = {};
  const tls = [...document.querySelectorAll('.timeline')].map(t => {
    const cs = getComputedStyle(t);
    return { id: t.parentElement && t.parentElement.id, w: +R(t).width.toFixed(1),
             maxw: cs.maxWidth };
  });
  out.timeline.wrappers = tls;

  out.timeline.rows = [...document.querySelectorAll('.tl-item')].map(it => {
    const cs = getComputedStyle(it);
    const aside = it.querySelector('.tl-aside');
    const ar = aside ? R(aside) : null;
    const ink = aside ? inkRight(aside) : null;
    const facts = aside ? aside.querySelector('.facts') : null;
    return {
      year: it.querySelector('.tl-year')?.textContent.trim(),
      cols: cs.gridTemplateColumns,
      rowW: +R(it).width.toFixed(1),
      borderTopW: +R(it).width.toFixed(1),
      asideW: ar ? +ar.width.toFixed(1) : null,
      asideInkW: (ar && ink > -1e8) ? +(ink - ar.left).toFixed(1) : 0,
      fill: (ar && ink > -1e8) ? +(((ink - ar.left) / ar.width) * 100).toFixed(1) : 0,
      dead: (ar && ink > -1e8) ? +(ar.right - ink).toFixed(1) : (ar ? ar.width : 0),
      hasFacts: !!facts,
      factRows: facts ? facts.querySelectorAll('dt').length : 0,
      asideH: ar ? +ar.height.toFixed(0) : null,
      bodyH: +R(it.children[1]).height.toFixed(0),
    };
  });

  // rule vs content: rightmost ink anywhere in the row vs the border-top span
  out.timeline.ruleOverhang = [...document.querySelectorAll('.tl-item')].map(it => {
    const r = R(it); const ink = inkRight(it);
    return { year: it.querySelector('.tl-year')?.textContent.trim(),
             ruleRight: +r.right.toFixed(1), inkRight: +ink.toFixed(1),
             overhang: +(r.right - ink).toFixed(1) };
  });

  // ---------- P0.2 footer alignment ----------
  const foot = document.querySelector('.foot');
  const fi = document.querySelector('.foot-inner');
  const probe = document.querySelector('#record .wrap') || document.querySelector('.section .wrap');
  out.footer = {
    footInnerExists: !!fi,
    footInnerDisplay: fi ? getComputedStyle(fi).display : null,
    footInnerCols: fi ? getComputedStyle(fi).gridTemplateColumns : null,
    footInnerLeft: fi ? +R(fi).left.toFixed(1) : null,
    footInnerRight: fi ? +R(fi).right.toFixed(1) : null,
    footInnerW: fi ? +R(fi).width.toFixed(1) : null,
    sectionWrapLeft: probe ? +R(probe).left.toFixed(1) : null,
    sectionWrapRight: probe ? +R(probe).right.toFixed(1) : null,
    sectionWrapW: probe ? +R(probe).width.toFixed(1) : null,
    footTextLeft: fi ? +inkLeft(fi).toFixed(1) : null,
  };

  // ---------- P0.3 contrast ----------
  function lum(c){
    const m = c.match(/[\d.]+/g).map(Number);
    const f = v => { v/=255; return v<=0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055,2.4); };
    return 0.2126*f(m[0]) + 0.7152*f(m[1]) + 0.0722*f(m[2]);
  }
  function bgOf(el){
    let e = el;
    while (e) {
      const c = getComputedStyle(e).backgroundColor;
      if (c && c !== 'rgba(0, 0, 0, 0)' && !/, *0\)$/.test(c)) return c;
      e = e.parentElement;
    }
    return 'rgb(10,12,14)';
  }
  function ratio(el){
    const fg = getComputedStyle(el).color, bg = bgOf(el);
    const a = lum(fg), b = lum(bg);
    return +(((Math.max(a,b)+0.05)/(Math.min(a,b)+0.05))).toFixed(2);
  }
  out.contrast = {};
  for (const sel of ['.src','.bar-year','.lane','.school','.facts dt','.facts dd',
                     '.note','.silence-count','.p-l','.p-n','.bar-none','.chart-key span']) {
    const els = [...document.querySelectorAll(sel)];
    if (!els.length) { out.contrast[sel] = null; continue; }
    const rs = els.map(ratio);
    out.contrast[sel] = { n: els.length, min: Math.min(...rs), max: Math.max(...rs),
      color: getComputedStyle(els[0]).color,
      fontSize: getComputedStyle(els[0]).fontSize,
      failAA: rs.filter(r => r < 4.5).length };
  }

  // ---------- P1.5 narrow--flush ----------
  const nf = document.querySelector('.narrow--flush');
  out.flush = nf ? { w: +R(nf).width.toFixed(1), pct: +((R(nf).width/innerWidth)*100).toFixed(1),
                     left: +R(nf).left.toFixed(1), maxw: getComputedStyle(nf).maxWidth,
                     cssW: getComputedStyle(nf).width } : null;
  out.inlineMarginInline = [...document.querySelectorAll('[style*="margin-inline"]')].length;

  // ---------- P2.6 measure unification ----------
  function chars(el){
    // measure characters per line from the widest line box of the first <p>
    const t = el.textContent.replace(/\s+/g,' ').trim();
    const r = R(el);
    const cs = getComputedStyle(el);
    // approximate: use canvas to measure avg char width
    const c = document.createElement('canvas').getContext('2d');
    c.font = `${cs.fontStyle} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
    const avg = c.measureText(t.slice(0,400)).width / Math.min(400, t.length);
    return { w: +r.width.toFixed(0), fs: cs.fontSize, ch: +(r.width/avg).toFixed(1) };
  }
  out.measures = {};
  const lead = document.querySelector('.split .lead');
  if (lead) out.measures.lead = chars(lead);
  const tb = document.querySelector('.tl-body p');
  if (tb) out.measures.tlBody = chars(tb);
  const sp2 = document.querySelector('.split > :nth-child(2):last-child');
  if (sp2) out.measures.splitSecond = { w: +R(sp2).width.toFixed(0),
     maxw: getComputedStyle(sp2).maxWidth };
  if (nf) { const p = nf.querySelector('p'); if (p) out.measures.flushP = chars(p); }

  // ---------- P2.7 boat stage ----------
  const bs = document.querySelector('.boat-stage');
  out.boat = bs ? { w:+R(bs).width.toFixed(0), h:+R(bs).height.toFixed(0),
                    ar: +(R(bs).width/R(bs).height).toFixed(2),
                    css: getComputedStyle(bs).aspectRatio } : null;

  // ---------- P2.8 motion ----------
  const dur = {};
  for (const el of document.querySelectorAll('[data-reveal], .school')) {
    const cs = getComputedStyle(el);
    const k = cs.transitionDuration + ' | ' + cs.transitionDelay.split(',')[0];
    dur[k] = (dur[k]||0)+1;
  }
  out.motion = { buckets: dur,
    revealCount: document.querySelectorAll('[data-reveal]').length,
    schoolDelays: [...document.querySelectorAll('.school')].slice(0,6)
      .map(e=>getComputedStyle(e).transitionDelay),
    hingeLine: (()=>{const e=document.querySelector('.hinge-line');
      return e?{d:getComputedStyle(e).transitionDuration,f:getComputedStyle(e).transitionTimingFunction}:null})(),
    amount: (()=>{const e=document.querySelector('.thesis .amount');
      return e?{d:getComputedStyle(e).transitionDuration}:null})(),
  };

  // ---------- P2.9 2020 annotation ----------
  const bn = document.querySelector('.bar-none');
  out.chart2020 = bn ? { text: bn.textContent.trim(), w:+R(bn).width.toFixed(0),
      h:+R(bn).height.toFixed(0), fs:getComputedStyle(bn).fontSize,
      color:getComputedStyle(bn).color,
      visible: R(bn).width>0 && R(bn).height>0,
      parentYear: bn.closest('.bar-col')?.getAttribute('title') } : null;
  out.chartKeyText = [...document.querySelectorAll('.chart-key span')].map(e=>e.textContent.trim());
  out.barHeights = [...document.querySelectorAll('.bar')].map(b=>+R(b).height.toFixed(0));

  // ---------- P2.10 revival section ----------
  const hm = document.querySelector('.hinge--minor');
  out.revival = hm ? { h:+R(hm).height.toFixed(0), w:+R(hm).width.toFixed(0),
      bg:getComputedStyle(hm).backgroundColor,
      lineFs:getComputedStyle(document.querySelector('.hinge-line--minor')).fontSize,
      nums:[...document.querySelectorAll('.p-n')].map(e=>e.textContent.trim()),
      numFs:getComputedStyle(document.querySelector('.p-n')).fontSize,
      progW:+R(document.querySelector('.progression')).width.toFixed(0),
      progCols:getComputedStyle(document.querySelector('.progression')).gridTemplateColumns } : null;

  // ---------- section rhythm ----------
  out.sections = [...document.querySelectorAll('section, footer')].map(s=>({
    id: s.id || s.className.split(' ').slice(0,2).join('.'),
    h: +R(s).height.toFixed(0), w:+R(s).width.toFixed(0) }));

  // ---------- content width ----------
  const wraps = [...document.querySelectorAll('.wrap')];
  out.wrap = { n: wraps.length, w: wraps.length? +R(wraps[2]||wraps[0]).width.toFixed(0):null,
    pct: wraps.length ? +((R(wraps[2]||wraps[0]).width/innerWidth)*100).toFixed(1):null };
  out.docW = document.documentElement.scrollWidth;
  out.innerW = innerWidth;
  out.scrollH = document.body.scrollHeight;
  return out;
})()
"""

res = cdp.ev(ws, JS)
print(json.dumps(res, indent=1)[:20000])
cdp.shot(ws, f"/Users/AISandbox/crls-crew/renders/r3-{W}-top.png")
