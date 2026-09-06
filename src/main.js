/**
 * CRLS Rowing — site behaviour.
 *
 * Three jobs:
 *   1. Render the boat: a slow hero pass, and an inspectable model in the fleet
 *      section. Both share the geometry in src/boat/.
 *   2. Build the data-driven sections from src/data/team.js so no number on the
 *      page is hand-typed.
 *   3. Scroll: reveal-on-enter, a chapter readout, and a progress bar.
 *
 * Motion is deliberately restrained. The hero rotates about a quarter of a turn
 * over the whole scroll; nothing loops, nothing bounces, and everything stops
 * entirely under prefers-reduced-motion.
 */

import * as THREE from 'three';
import Lenis from 'lenis';
import {
  SPEC, buildHull, buildDeck, buildCockpitWell, buildCoxWell,
} from './boat/pocock.js';
import {
  buildRiggers, buildSlidesAndSeats, buildFittings, buildFoils, buildOars, buildCoxFittings,
} from './boat/hardware.js';
import {
  HISTORY, SEASONS, MILESTONES_2026, FLEET, RIVALS, ARCHIVE,
} from './data/team.js';

const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ================================================================== *
 * Shared boat scene factory
 * ================================================================== */

function studioEnv(renderer) {
  const c = document.createElement('canvas');
  c.width = 32; c.height = 256;
  const g = c.getContext('2d');
  const grad = g.createLinearGradient(0, 0, 0, 256);
  grad.addColorStop(0.00, '#eef4fb');
  grad.addColorStop(0.38, '#cdd9e6');
  grad.addColorStop(0.50, '#ffffff');   // horizon band: the hull's long highlight
  grad.addColorStop(0.58, '#aab6c2');
  grad.addColorStop(1.00, '#6f7a85');
  g.fillStyle = grad; g.fillRect(0, 0, 32, 256);
  const tex = new THREE.CanvasTexture(c);
  tex.mapping = THREE.EquirectangularReflectionMapping;
  tex.colorSpace = THREE.SRGBColorSpace;
  const pmrem = new THREE.PMREMGenerator(renderer);
  const env = pmrem.fromEquirectangular(tex).texture;
  pmrem.dispose(); tex.dispose();
  return env;
}

let sharedGeo = null;
function boatGeometry() {
  if (!sharedGeo) {
    sharedGeo = {
      hull: buildHull({ stations: 300, ring: 30 }),
      deck: buildDeck({ stations: 300, across: 10 }),
      cockpit: buildCockpitWell(),
      cox: buildCoxWell(),
      riggers: buildRiggers(),
      seats: buildSlidesAndSeats(),
      fittings: buildFittings(),
      foils: buildFoils(),
      oars: buildOars(),
      coxfit: buildCoxFittings(),
    };
  }
  return sharedGeo;
}

function makeBoat(renderer) {
  const env = studioEnv(renderer);
  const M = {
    hull: new THREE.MeshPhysicalMaterial({
      color: 0xffffff, roughness: 0.12, metalness: 0,
      clearcoat: 1, clearcoatRoughness: 0.06,
      side: THREE.DoubleSide, envMapIntensity: 1.35,
    }),
    carbon: new THREE.MeshPhysicalMaterial({
      // Real exposed carbon under clearcoat is a dark grey with a visible
      // sheen, not a black void. At 0x101318 the decks swallowed all light and
      // the cockpit read as a hole in the boat.
      color: 0x24282e, roughness: 0.34, metalness: 0.45,
      clearcoat: 0.9, clearcoatRoughness: 0.16,
      side: THREE.DoubleSide, envMapIntensity: 1.45,
    }),
    metal: new THREE.MeshStandardMaterial({
      color: 0xb4b9bf, roughness: 0.28, metalness: 0.92, envMapIntensity: 1.2,
    }),
    black: new THREE.MeshPhysicalMaterial({
      color: 0x14171b, roughness: 0.34, metalness: 0.3,
      clearcoat: 0.6, clearcoatRoughness: 0.25, envMapIntensity: 1,
    }),
    white: new THREE.MeshStandardMaterial({
      color: 0xffffff, roughness: 0.22, envMapIntensity: 1.2,
    }),
    blade: new THREE.MeshPhysicalMaterial({
      color: 0x0c0e11, roughness: 0.3, metalness: 0.15,
      clearcoat: 0.9, clearcoatRoughness: 0.12,
      side: THREE.DoubleSide, envMapIntensity: 1.15,
    }),
  };

  const g = boatGeometry();
  const group = new THREE.Group();
  group.add(new THREE.Mesh(g.hull, M.hull));
  group.add(new THREE.Mesh(g.deck, M.carbon));
  group.add(new THREE.Mesh(g.cockpit, M.carbon));
  group.add(new THREE.Mesh(g.cox, M.carbon));
  group.add(new THREE.Mesh(g.riggers, M.black));
  group.add(new THREE.Mesh(g.seats, M.metal));
  group.add(new THREE.Mesh(g.fittings, M.white));
  group.add(new THREE.Mesh(g.foils, M.carbon));
  group.add(new THREE.Mesh(g.oars, M.blade));
  group.add(new THREE.Mesh(g.coxfit, M.black));
  group.position.x = -SPEC.loa / 2;

  const pivot = new THREE.Group();
  pivot.add(group);
  return { pivot, env };
}

function makeRenderer(canvas) {
  const r = new THREE.WebGLRenderer({
    canvas, antialias: true, alpha: true, powerPreference: 'high-performance',
  });
  r.setPixelRatio(Math.min(1.75, devicePixelRatio));
  r.outputColorSpace = THREE.SRGBColorSpace;
  r.toneMapping = THREE.ACESFilmicToneMapping;
  r.toneMappingExposure = 1.0;
  return r;
}

/* ================================================================== *
 * Hero scene
 * ================================================================== */
function initHero() {
  const canvas = document.getElementById('boat-canvas');
  if (!canvas) return null;

  let renderer;
  try { renderer = makeRenderer(canvas); }
  catch (e) { console.warn('WebGL unavailable', e); canvas.style.display = 'none'; return null; }

  const scene = new THREE.Scene();
  const { pivot, env } = makeBoat(renderer);
  scene.environment = env;
  scene.add(pivot);

  // Hero lighting is deliberately harder than the fleet view's: a strong key
  // from the upper right, a cool rim raking the far side of the hull, and a
  // warm low kicker standing in for the 5:30pm light on the river. Against a
  // near-black page the hull has to be carved out by light or it disappears.
  const key = new THREE.DirectionalLight(0xffffff, 2.6);
  key.position.set(6, 8, 4);
  const rim = new THREE.DirectionalLight(0x9dc4ff, 2.2);
  rim.position.set(-7, 2.5, -6);
  // A weak neutral kicker. An earlier warm one (0xe8a06a) tinted the whole
  // white hull orange — on a near-white clearcoat almost any coloured light
  // reads as paint, not light.
  const kick = new THREE.DirectionalLight(0xdce8f5, 0.55);
  kick.position.set(-2, -1.2, 6);
  scene.add(key, rim, kick);

  const cam = new THREE.PerspectiveCamera(38, 1, 0.1, 200);

  function layout() {
    const w = canvas.clientWidth || innerWidth;
    const h = canvas.clientHeight || innerHeight;
    renderer.setSize(w, h, false);
    cam.aspect = w / h;
    // Frame the boat in the right half of the screen, clear of the headline.
    // On narrow screens it centres and pulls back instead.
    const narrow = w < 900;
    const dist = narrow ? 15.5 : 11.5;
    cam.position.set(dist * 0.40, dist * 0.26, dist * 0.88);
    cam.lookAt(narrow ? 0 : -1.9, -0.10, 0);
    cam.updateProjectionMatrix();
  }
  layout();
  addEventListener('resize', layout);
  // The window may never resize while the element does — the fleet stage has a
  // different aspect ratio on mobile and is below the fold at load, so a
  // resize listener alone left the canvas with a stale desktop buffer.
  if (typeof ResizeObserver === 'function') {
    new ResizeObserver(() => layout()).observe(canvas);
  }
  requestAnimationFrame(() => layout());

  let progress = 0;
  const state = {
    set p(v) { progress = v; },
    render() {
      // A quarter turn across the whole page, plus a slow settle.
      pivot.rotation.y = -0.55 + progress * 1.6;
      pivot.rotation.z = 0.045 - progress * 0.06;
      pivot.position.y = 0.15 - progress * 0.35;
      renderer.render(scene, cam);
    },
  };
  state.render();
  return state;
}

/* ================================================================== *
 * Fleet scene — inspectable, with named views
 * ================================================================== */
function initFleet() {
  const canvas = document.getElementById('fleet-canvas');
  if (!canvas) return;

  let renderer;
  try { renderer = makeRenderer(canvas); }
  catch (e) { canvas.style.display = 'none'; return; }

  const scene = new THREE.Scene();
  const { pivot, env } = makeBoat(renderer);
  scene.environment = env;
  scene.add(pivot);
  // Brighter than the hero: this is an inspection stage, so the hull should be
  // fully legible rather than dramatically lit.
  const key = new THREE.DirectionalLight(0xffffff, 2.3); key.position.set(5, 8, 5);
  const rim = new THREE.DirectionalLight(0xbcd4ff, 1.9); rim.position.set(-6, 3, -5);
  const fill = new THREE.DirectionalLight(0xe8eef7, 0.8); fill.position.set(0, -2, 6);
  const hemi = new THREE.HemisphereLight(0xdbe7f4, 0x2b3038, 1.2);
  scene.add(key, rim, fill, hemi);

  const cam = new THREE.PerspectiveCamera(34, 1, 0.05, 200);
  let viewName = 'quarter';
  let drag = 0, targetDrag = 0;

  // Distance needed to fit `span` metres across the frame at the current FOV
  // and aspect. Framing the boat by its own length keeps every view correctly
  // composed at any stage size, instead of guessing camera positions.
  function fitDistance(span, fovDeg, aspect, vertical) {
    const fov = THREE.MathUtils.degToRad(fovDeg);
    const half = span / 2;
    if (vertical) return half / Math.tan(fov / 2);
    const hFov = 2 * Math.atan(Math.tan(fov / 2) * aspect);
    return half / Math.tan(hFov / 2);
  }

  function layout() {
    const w = canvas.clientWidth, h = canvas.clientHeight;
    if (!w || !h) return;
    renderer.setSize(w, h, false);
    const aspect = w / h;
    cam.aspect = aspect;

    const L = SPEC.loa;
    const narrow = w < 700;
    const pad = narrow ? 1.28 : 1.14;   // headroom around the boat

    if (viewName === 'side') {
      cam.fov = 34;
      const d = fitDistance(L * pad, cam.fov, aspect, false);
      cam.position.set(0, 0.05, d);
      cam.lookAt(0, 0.02, 0);
    } else if (viewName === 'plan') {
      cam.fov = 34;
      const d = fitDistance(L * pad, cam.fov, aspect, false);
      cam.position.set(0, d, 0.01);
      cam.lookAt(0, 0, 0);
    } else if (viewName === 'quarter') {
      cam.fov = 34;
      // A 24:1 object seen on a diagonal will always fight a letterbox frame.
      // Swing the camera much closer to broadside (a shallow three-quarter)
      // and drop it near the waterline: the boat then lies almost along the
      // frame's long axis, which is the only way it fits whole while still
      // reading as three-dimensional. Both oars are inside `rigged`.
      const rigged = L * 1.16;
      const d = fitDistance(rigged * (narrow ? 1.20 : 1.02), cam.fov, aspect, false);
      cam.position.set(d * 0.20, d * 0.155, d * 0.90);
      cam.lookAt(0, -0.01, 0);
    } else if (viewName === 'bow') {
      cam.fov = 30;
      cam.position.set(-L * 0.44, 0.55, 1.05);
      cam.lookAt(-L * 0.24, -0.02, 0);
    } else {
      cam.fov = 38;
      cam.position.set(1.7, 0.86, 1.7);
      cam.lookAt(0.30, -0.06, 0);
    }
    cam.updateProjectionMatrix();
  }

  let raf = null, visible = false;
  function frame() {
    drag += (targetDrag - drag) * 0.08;
    pivot.rotation.y = drag;
    renderer.render(scene, cam);
    raf = visible ? requestAnimationFrame(frame) : null;
  }

  // Visibility is measured, not observed: under smooth scroll an
  // IntersectionObserver may never fire, which previously left this canvas
  // unrendered and holding a stale buffer.
  const checkVisible = () => {
    const r = canvas.getBoundingClientRect();
    const nowVisible = r.bottom > -150 && r.top < innerHeight + 150;
    if (nowVisible && !raf) { layout(); frame(); }
    visible = nowVisible;
  };
  addEventListener('scroll', checkVisible, { passive: true });
  setInterval(checkVisible, 250);
  checkVisible();

  if (typeof IntersectionObserver === 'function') {
    new IntersectionObserver(() => checkVisible(), { rootMargin: '150px' }).observe(canvas);
  }

  addEventListener('resize', layout);
  // The window may never resize while the element does — the fleet stage has a
  // different aspect ratio on mobile and is below the fold at load, so a
  // resize listener alone left the canvas with a stale desktop buffer.
  if (typeof ResizeObserver === 'function') {
    new ResizeObserver(() => layout()).observe(canvas);
  }
  requestAnimationFrame(() => layout());

  // drag to spin
  let down = false, lastX = 0;
  const onDown = (e) => { down = true; lastX = (e.touches ? e.touches[0] : e).clientX; };
  const onMove = (e) => {
    if (!down) return;
    const x = (e.touches ? e.touches[0] : e).clientX;
    targetDrag += (x - lastX) * 0.006;
    lastX = x;
    if (e.cancelable) e.preventDefault();
  };
  const onUp = () => { down = false; };
  canvas.addEventListener('pointerdown', onDown);
  addEventListener('pointermove', onMove, { passive: false });
  addEventListener('pointerup', onUp);
  canvas.style.cursor = 'grab';

  document.querySelectorAll('.view-tab').forEach((btn) => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.view-tab').forEach((b) => b.setAttribute('aria-pressed', 'false'));
      btn.setAttribute('aria-pressed', 'true');
      viewName = btn.dataset.view || 'quarter';
      targetDrag = 0;
      drag = 0;
      pivot.rotation.y = 0;
      layout();
    });
  });
}

/* ================================================================== *
 * Content
 * ================================================================== */
function fillTimelines() {
  const early = document.getElementById('timeline-early');
  const ret = document.getElementById('timeline-return');
  if (!early || !ret) return;

  const item = (h, i) => `
    <article class="tl-item${h.pull ? ' pull' : ''}" data-reveal style="--i:${i}">
      <div class="tl-year">${h.year}</div>
      <div>
        <h3 class="tl-title">${h.title}</h3>
        <div class="tl-body">
          <p>${h.body.replace(/\s+/g, ' ').trim()}</p>
        </div>
      </div>
      <div class="tl-aside">
        ${h.aside ? `<dl class="facts">${h.aside
          .map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join('')}</dl>` : ''}
        ${h.src ? `<a class="src" href="${h.src}" target="_blank" rel="noopener">Source</a>` : ''}
        ${h.note ? `<p class="note">${h.note}</p>` : ''}
      </div>
    </article>`;

  const cut = HISTORY.findIndex((h) => h.year === '1978');
  // The 1929 "one heat" entry is staged as its own full-bleed section, so it is
  // filtered out here rather than repeated as an ordinary timeline row.
  const isHinge = (h) => h.pull && h.year === '1929';
  early.innerHTML = HISTORY.slice(0, cut).filter((h) => !isHinge(h)).map(item).join('');
  ret.innerHTML = HISTORY.slice(cut).map(item).join('');
}

function fillChart() {
  const el = document.getElementById('chart');
  if (!el) return;
  const max = Math.max(...SEASONS.map((s) => s.races));
  // Mark the seasons the narrative turns on: the first year on record, the
  // jump in 2015, the lost 2020 season, and the best year.
  const keyYears = new Set([2007, 2015, 2020, 2026]);
  el.innerHTML = SEASONS.map((s) => {
    const h = s.races ? Math.max(2, (s.races / max) * 100) : 1.5;
    const w = s.races ? (s.wins / s.races) * 100 : 0;
    const label = s.races
      ? `${s.year}: ${s.races} races, ${s.wins} won`
      : `${s.year}: no season`;
    return `
      <div class="bar-col${s.races ? '' : ' dim'}"${keyYears.has(s.year) ? ' data-key="1"' : ''} title="${label}">
        ${s.races ? '' : '<div class="bar-none">No season</div>'}
        <div class="bar-track">
          <div class="bar" style="height:${h}%">
            <div class="won" style="--w:${w}%"></div>
          </div>
        </div>
        <div class="bar-year">${s.year}</div>
      </div>`;
  }).join('');
}

function fillResults() {
  const el = document.getElementById('results');
  if (!el) return;
  const ord = (n) => (n === 1 ? 'st' : n === 2 ? 'nd' : n === 3 ? 'rd' : 'th');
  el.innerHTML = MILESTONES_2026.map((m, i) => `
    <article class="result" data-reveal style="--i:${i}">
      <div class="result-head">
        ${m.place ? `<div class="result-place">${m.place}<sup>${ord(m.place)}</sup></div>` : '<div></div>'}
        ${m.time ? `<div class="result-time">${m.time}</div>` : ''}
      </div>
      <h3>${m.title}</h3>
      <p>${m.detail}</p>
      ${m.road ? `<ol class="road">${m.road.map(([round, time, place]) => `
        <li><span class="r-round">${round}</span><span class="r-time">${time}</span><span class="r-place">${place}${ord(place)}</span></li>`).join('')}</ol>` : ''}
      ${m.crew ? `<div class="crew">${m.crew.map((c) => `<b>${c}</b>`).join(' · ')}${m.cox ? ` · cox <b>${m.cox}</b>` : ''}</div>` : ''}
      ${m.src ? `<a class="src" href="${m.src}" target="_blank" rel="noopener">Source</a>` : ''}
    </article>`).join('');
}

function fillFleet() {
  const boat = FLEET[0];
  const t = document.getElementById('spec-table');
  const n = document.getElementById('boat-notes');
  if (n) n.textContent = boat.notes.replace(/\s+/g, ' ').trim();
  if (t) {
    t.innerHTML += boat.specs
      .map(([k, v]) => `<tr><th scope="row">${k}</th><td>${v}</td></tr>`)
      .join('');
  }

  // The rest of the fleet. Only three shells are named anywhere in the
  // program's public record, all in one race-day lineup, so the roster shows
  // exactly what that source says and marks the rest as not yet modelled.
  const r = document.getElementById('fleet-roster');
  if (r) {
    r.innerHTML = FLEET.map((b) => `
      <li class="boat${b.status === 'built' ? ' is-built' : ''}">
        <span class="boat-swatch" data-hull="${(b.hull || '').toLowerCase()}" aria-hidden="true"></span>
        <span class="boat-id">
          <b>${b.name}</b>
          <em>${b.hull} hull${b.model ? ` &middot; ${b.model}` : ''}</em>
        </span>
        <span class="boat-state">${b.status === 'built' ? 'Modelled' : 'Not yet modelled'}</span>
      </li>`).join('');
  }
}

function fillField() {
  const el = document.getElementById('field');
  if (!el) return;
  el.innerHTML = RIVALS.map((r, i) => {
    const cls = r.us ? 'school us' : r.kind === 'public' ? 'school public' : 'school';
    return `<span class="${cls}" style="--i:${i}">${r.name}</span>`;
  }).join('');
}

/* ================================================================== *
 * Scroll
 * ================================================================== */
function initScroll(hero) {
  const prog = document.getElementById('prog');
  const label = document.getElementById('chapter-label');
  const chapters = [...document.querySelectorAll('[data-chapter]')];

  // Reveal is driven from the scroll tick rather than IntersectionObserver.
  //
  // Lenis animates a transform on the scroll container, so elements do not
  // change position relative to the IO root and observers never fire — the
  // page would scroll with every section still at opacity 0. Measuring
  // ourselves on each tick is both correct under smooth scroll and cheap,
  // because nodes drop out of the set as soon as they are revealed.
  let pending = [...document.querySelectorAll('[data-reveal]')];
  const revealVisible = () => {
    if (!pending.length) return;
    const limit = innerHeight * 0.92;
    const still = [];
    for (const n of pending) {
      const r = n.getBoundingClientRect();
      // Reveal once the top edge has come up past the trigger line. Anything
      // already above the viewport counts as revealed too — jumping down the
      // page must not leave a trail of permanently hidden sections behind.
      if (r.top < limit) n.classList.add('in');
      else still.push(n);
    }
    pending = still;
  };
  const watch = () => {
    const known = new Set(pending);
    document.querySelectorAll('[data-reveal]:not(.in)').forEach((n) => {
      if (!known.has(n)) pending.push(n);
    });
    revealVisible();
  };
  revealVisible();

  // chart bars animate as a group, staggered
  const chart = document.getElementById('chart');
  let chartStarted = false;
  const maybeChart = () => {
    if (!chart) return;
    const cols = [...chart.children];
    if (!cols.length) return;
    const r = chart.getBoundingClientRect();
    if (r.top > innerHeight * 0.85) return;
    if (!chartStarted) {
      chartStarted = true;
      cols.forEach((c, i) => {
        setTimeout(() => c.classList.add('in'), reduced ? 0 : i * 38);
      });
      // Backstop: if the staggered timers are starved (throttled tab), make
      // sure every column still ends up revealed rather than invisible.
      setTimeout(() => cols.forEach((c) => c.classList.add('in')), 1600);
      return;
    }
    // Keep sweeping until they are all in; costs one class check per tick.
    if (cols.some((c) => !c.classList.contains('in'))) {
      cols.forEach((c) => c.classList.add('in'));
    }
  };

  // counters
  let counters = [...document.querySelectorAll('[data-count]')];
  const maybeCount = () => {
    if (!counters.length) return;
    const still = [];
    for (const el of counters) {
      const r = el.getBoundingClientRect();
      // Fire as soon as any part of the number is inside the viewport. An
      // earlier 0.9 * innerHeight trigger line missed the hero stats by 8px on
      // a 1000px viewport, so the site loaded showing "0 races on record".
      if (r.top >= innerHeight || r.bottom <= 0) { still.push(el); continue; }
      const target = +el.dataset.count;
      if (reduced) { el.textContent = target.toLocaleString(); continue; }
      // The markup ships the real number so a no-JS reader sees it. Reset to
      // zero here, at the moment the count actually starts.
      el.textContent = '0';
      const t0 = performance.now(), dur = 1400;
      // Guarded by a timeout so a throttled tab still lands on the real number
      // instead of freezing part-way through the count.
      const settle = setTimeout(() => { el.textContent = target.toLocaleString(); }, dur + 400);
      const tick = (t) => {
        const k = Math.min(1, (t - t0) / dur);
        const eased = 1 - Math.pow(1 - k, 3);
        el.textContent = Math.round(target * eased).toLocaleString();
        if (k < 1) requestAnimationFrame(tick);
        else clearTimeout(settle);
      };
      requestAnimationFrame(tick);
    }
    counters = still;
  };

  // The sixty-year gap: a rule that fills and a year count that climbs from
  // 1929 to 1989 as the section passes. The empty scroll IS the content here,
  // so it needs something to measure itself against.
  const silenceRule = document.getElementById('silence-rule');
  const silenceCount = document.getElementById('silence-count');
  const silenceYears = document.getElementById('silence-years');
  const gapSection = document.getElementById('gap');
  function updateSilence() {
    if (!gapSection || !silenceRule) return;
    const r = gapSection.getBoundingClientRect();
    const span = r.height - innerHeight;
    const p = span > 0 ? Math.min(1, Math.max(0, -r.top / span)) : 0;
    silenceRule.firstElementChild.style.setProperty('--fill', (p * 100).toFixed(1) + '%');
    const yr = Math.round(1929 + p * 60);
    if (silenceCount) silenceCount.textContent = yr;
    if (silenceYears) silenceYears.textContent = (yr - 1929) + ' years';
  }

  function onScroll(y) {
    revealVisible();
    maybeChart();
    maybeCount();
    updateSilence();
    const max = document.body.scrollHeight - innerHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, y / max)) : 0;
    if (prog) prog.style.setProperty('--p', (p * 100).toFixed(2) + '%');
    if (hero) { hero.p = p; hero.render(); }

    // chapter readout
    let current = chapters[0];
    for (const c of chapters) {
      if (c.getBoundingClientRect().top <= innerHeight * 0.45) current = c;
    }
    if (current && label && label.textContent !== current.dataset.chapter) {
      label.textContent = current.dataset.chapter;
    }
  }

  // Signal to CSS that JS is driving the reveals. Until this lands, every
  // [data-reveal] element is plain visible, so a failed bundle or a throttled
  // tab shows the whole page rather than a blank one.
  if (!reduced) document.documentElement.classList.add('js-reveal');

  // Native scroll is always wired up. Lenis is an enhancement on top; if its
  // rAF loop is throttled (background tab, reduced power mode) the page still
  // tracks scroll, still reveals, and still updates the chapter readout.
  addEventListener('scroll', () => onScroll(window.scrollY), { passive: true });

  if (!reduced) {
    try {
      const lenis = new Lenis({ duration: 1.1, smoothWheel: true });
      lenis.on('scroll', ({ scroll }) => onScroll(scroll));
      const raf = (t) => { lenis.raf(t); requestAnimationFrame(raf); };
      requestAnimationFrame(raf);
    } catch (e) {
      console.warn('smooth scroll unavailable, using native', e);
    }
  }
  onScroll(window.scrollY);

  // Lenis swallows the browser's own scroll events while it is animating, and
  // programmatic scrollTo never emits one at all. A cheap polled fallback keeps
  // the reveal/chapter/progress state correct no matter how the page was moved
  // — including by keyboard, anchor jump, or devtools. It costs one comparison
  // per tick and stops doing any work once everything has been revealed.
  let lastY = -1;
  setInterval(() => {
    const y = window.scrollY;
    if (y !== lastY) { lastY = y; onScroll(y); }
  }, 120);

  // hero lines: staged from a class so the resting state is plain CSS and the
  // animation cannot leave the type stuck half-revealed.
  //
  // Note: this deliberately does NOT sit inside requestAnimationFrame. A
  // backgrounded or throttled tab never runs rAF, which would leave the
  // headline permanently translated off its own mask — the page would render
  // as an empty screen. A timeout always fires.
  const lines = document.querySelectorAll('.hero-title .l > span');
  const showLines = () => lines.forEach((s) => s.classList.add('shown'));
  if (reduced) {
    showLines();
    // With motion reduced there is no reveal choreography at all: show every
    // section, fill every counter, and draw the chart immediately. Leaving this
    // to the scroll tick stranded the page at one visible section.
    pending.forEach((n) => n.classList.add('in'));
    pending = [];
    document.querySelectorAll('[data-count]').forEach((el) => {
      el.textContent = (+el.dataset.count).toLocaleString();
    });
    counters = [];
    if (chart) {
      chartDone = true;
      [...chart.children].forEach((c) => c.classList.add('in'));
    }
  } else {
    lines.forEach((s, i) => { s.style.transitionDelay = `${0.10 + i * 0.09}s`; });
    setTimeout(showLines, 60);
  }

  // re-watch anything injected after first paint
  setTimeout(watch, 60);
}

/* ================================================================== *
 * Boot
 * ================================================================== */
try {
  fillTimelines();
  fillChart();
  fillResults();
  fillFleet();
  fillField();
} catch (e) {
  console.error('content build failed', e);
}

let hero = null;
try { hero = initHero(); } catch (e) { console.error('hero failed', e); }
try { initFleet(); } catch (e) { console.error('fleet failed', e); }
try { initScroll(hero); } catch (e) {
  console.error('scroll failed', e);
  // Never leave the page mid-animation: if the scroll layer dies, show
  // everything rather than stranding the reveal state.
  document.querySelectorAll('[data-reveal]').forEach((n) => n.classList.add('in'));
  document.querySelectorAll('.hero-title .l > span').forEach((n) => n.classList.add('shown'));
  document.querySelectorAll('.bar-col').forEach((n) => n.classList.add('in'));
}

document.documentElement.dataset.ready = 'true';
