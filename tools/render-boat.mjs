/**
 * Offscreen render harness for the boat. Renders orthographic-ish views to PNG
 * so the geometry can be inspected without a browser, and so critique passes
 * have something concrete to look at.
 *
 * Run:  node tools/render-boat.mjs
 */
import * as THREE from 'three';
import { createCanvas } from 'canvas';
import fs from 'fs';
import path from 'path';
import {
  SPEC, buildHull, buildDeck, buildCockpitWell, buildCoxWell,
} from '../src/boat/pocock.js';
import {
  buildRiggers, buildSlidesAndSeats, buildFittings, buildOars, buildCoxFittings,
} from '../src/boat/hardware.js';

const OUT = path.resolve('renders');
fs.mkdirSync(OUT, { recursive: true });

const W = 1600, H = 900;

// ---- headless GL via gl package, falling back to a wireframe rasteriser ----
let gl = null;
try {
  const mod = await import('gl');
  gl = mod.default(W, H, { preserveDrawingBuffer: true });
} catch (e) {
  console.log('headless-gl unavailable:', e.message);
}

if (!gl) {
  console.log('\nNo GPU context. Emitting a vector line-drawing instead so the');
  console.log('geometry can still be checked (silhouette, stations, hardware).\n');
  await lineDrawing();
  process.exit(0);
}

const renderer = new THREE.WebGLRenderer({ context: gl, antialias: true });
renderer.setSize(W, H);
renderer.setPixelRatio(1);
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.05;

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x0d1014);

const matHull = new THREE.MeshStandardMaterial({
  color: 0xf2f2ee, roughness: 0.22, metalness: 0.0,
  side: THREE.DoubleSide,
});
const matCarbon = new THREE.MeshStandardMaterial({
  color: 0x14161a, roughness: 0.34, metalness: 0.35, side: THREE.DoubleSide,
});
const matMetal = new THREE.MeshStandardMaterial({
  color: 0x9aa0a6, roughness: 0.35, metalness: 0.85,
});
const matBlack = new THREE.MeshStandardMaterial({ color: 0x101216, roughness: 0.5 });
const matBall = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.3 });

const boat = new THREE.Group();
boat.add(new THREE.Mesh(buildHull(), matHull));
boat.add(new THREE.Mesh(buildDeck(), matCarbon));
boat.add(new THREE.Mesh(buildCockpitWell(), matCarbon));
boat.add(new THREE.Mesh(buildCoxWell(), matCarbon));
boat.add(new THREE.Mesh(buildRiggers(), matBlack));
boat.add(new THREE.Mesh(buildSlidesAndSeats(), matMetal));
boat.add(new THREE.Mesh(buildFittings(), matBall));
boat.add(new THREE.Mesh(buildOars(), matBlack));
boat.add(new THREE.Mesh(buildCoxFittings(), matBlack));
boat.position.x = -SPEC.loa / 2;
scene.add(boat);

scene.add(new THREE.HemisphereLight(0x9fb6cd, 0x1a1a1a, 1.2));
const key = new THREE.DirectionalLight(0xffffff, 2.2);
key.position.set(4, 8, 6); scene.add(key);
const rim = new THREE.DirectionalLight(0x88aaff, 1.1);
rim.position.set(-6, 3, -5); scene.add(rim);

const views = [
  { name: 'side', pos: [0, 0.6, 11], look: [0, 0, 0] },
  { name: 'three-quarter', pos: [6.5, 3.4, 7.5], look: [0, -0.1, 0] },
  { name: 'plan', pos: [0, 11, 0.001], look: [0, 0, 0] },
  { name: 'bow', pos: [-8.5, 1.2, 2.6], look: [-2, 0, 0] },
  { name: 'stern', pos: [8.5, 1.4, 2.6], look: [2, 0, 0] },
  { name: 'cockpit', pos: [1.2, 1.5, 2.0], look: [0.4, 0, 0] },
];

for (const v of views) {
  const cam = new THREE.PerspectiveCamera(32, W / H, 0.1, 100);
  cam.position.set(...v.pos);
  cam.lookAt(...v.look);
  const rt = new THREE.WebGLRenderTarget(W, H, { samples: 4 });
  renderer.setRenderTarget(rt);
  renderer.render(scene, cam);
  const buf = new Uint8Array(W * H * 4);
  renderer.readRenderTargetPixels(rt, 0, 0, W, H, buf);
  const canvas = createCanvas(W, H);
  const ctx = canvas.getContext('2d');
  const img = ctx.createImageData(W, H);
  // flip vertically
  for (let y = 0; y < H; y++) {
    const src = (H - 1 - y) * W * 4;
    img.data.set(buf.subarray(src, src + W * 4), y * W * 4);
  }
  ctx.putImageData(img, 0, 0);
  const p = path.join(OUT, `boat-${v.name}.png`);
  fs.writeFileSync(p, canvas.toBuffer('image/png'));
  console.log('wrote', p);
}

/* ------------------------------------------------------------------ *
 * Fallback: SVG line drawing of the hull, straight from the curves.
 * ------------------------------------------------------------------ */
async function lineDrawing() {
  const { halfBeam, sheerZ, keelZ, sectionPoint, cockpitHalf, coxHalf } =
    await import('../src/boat/pocock.js');

  const pad = 40, sw = 1400;
  const sx = (t) => pad + t * sw;
  const scaleY = 900;

  let svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${sw + pad * 2}" height="760" viewBox="0 0 ${sw + pad * 2} 760">
  <rect width="100%" height="100%" fill="#0d1014"/>
  <g fill="none" stroke-width="1.6">`;

  // --- profile (side view) ---
  const yOff1 = 170;
  const py = (z) => yOff1 - z * scaleY * 0.42;
  let sheer = '', keel = '';
  for (let i = 0; i <= 400; i++) {
    const t = i / 400;
    sheer += `${i ? 'L' : 'M'}${sx(t).toFixed(1)},${py(sheerZ(t)).toFixed(1)}`;
    keel += `${i ? 'L' : 'M'}${sx(t).toFixed(1)},${py(keelZ(t)).toFixed(1)}`;
  }
  svg += `<path d="${sheer}" stroke="#e8e6e1"/><path d="${keel}" stroke="#7f8c99"/>`;
  // waterline
  svg += `<line x1="${pad}" y1="${py(0.1747).toFixed(1)}" x2="${pad + sw}" y2="${py(0.1747).toFixed(1)}" stroke="#3d5a80" stroke-dasharray="6 5"/>`;
  svg += `<text x="${pad}" y="${yOff1 - 120}" fill="#8a929c" font-family="monospace" font-size="13">PROFILE  —  LOA ${SPEC.loa} m</text>`;

  // --- plan view ---
  const yOff2 = 400;
  let top = '', bot = '', ctop = '', cbot = '';
  for (let i = 0; i <= 400; i++) {
    const t = i / 400;
    const b = halfBeam(t) * scaleY * 0.42;
    top += `${i ? 'L' : 'M'}${sx(t).toFixed(1)},${(yOff2 - b).toFixed(1)}`;
    bot += `${i ? 'L' : 'M'}${sx(t).toFixed(1)},${(yOff2 + b).toFixed(1)}`;
  }
  svg += `<path d="${top}" stroke="#e8e6e1"/><path d="${bot}" stroke="#e8e6e1"/>`;
  // openings
  for (const [fn, col] of [[coxHalf, '#c8553d'], [cockpitHalf, '#4a7c8c']]) {
    let a = '', b2 = '';
    let started = false;
    for (let i = 0; i <= 400; i++) {
      const t = i / 400;
      const w = fn(t) * scaleY * 0.42;
      if (w > 0.5) {
        a += `${started ? 'L' : 'M'}${sx(t).toFixed(1)},${(yOff2 - w).toFixed(1)}`;
        b2 += `${started ? 'L' : 'M'}${sx(t).toFixed(1)},${(yOff2 + w).toFixed(1)}`;
        started = true;
      }
    }
    svg += `<path d="${a}" stroke="${col}"/><path d="${b2}" stroke="${col}"/>`;
  }
  // seats + riggers
  SPEC.seatStations.forEach((t, i) => {
    const side = SPEC.rigStarboard[i] ? 1 : -1;
    const x = sx(t), yb = yOff2 + side * SPEC.spread * scaleY * 0.42;
    svg += `<line x1="${x}" y1="${yOff2}" x2="${x}" y2="${yb.toFixed(1)}" stroke="#d4a373" stroke-width="2.4"/>`;
    svg += `<circle cx="${x}" cy="${yb.toFixed(1)}" r="4" fill="#d4a373"/>`;
    svg += `<text x="${x - 4}" y="${yOff2 + 4}" fill="#8a929c" font-family="monospace" font-size="11">${i + 1}</text>`;
  });
  svg += `<text x="${pad}" y="${yOff2 - 130}" fill="#8a929c" font-family="monospace" font-size="13">PLAN  —  beam ${SPEC.beamMax} m, spread ${SPEC.spread} m, riggers alternate S/P</text>`;

  // --- body plan (sections) ---
  const yOff3 = 660;
  const cx = pad + sw / 2;
  for (const t of [0.05, 0.1, 0.2, 0.3, 0.398, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]) {
    let d = '';
    const fwd = t <= 0.398;
    for (let j = 0; j <= 60; j++) {
      const [y, z] = sectionPoint(t, j / 60);
      const px = cx + (fwd ? 1 : -1) * y * scaleY * 0.62;
      const pz = yOff3 - (z - keelZ(t)) * scaleY * 0.62;
      d += `${j ? 'L' : 'M'}${px.toFixed(1)},${pz.toFixed(1)}`;
    }
    svg += `<path d="${d}" stroke="${fwd ? '#e8e6e1' : '#7f8c99'}" stroke-width="1.2"/>`;
  }
  svg += `<line x1="${cx}" y1="${yOff3 - 120}" x2="${cx}" y2="${yOff3 + 6}" stroke="#3a4048"/>`;
  svg += `<text x="${pad}" y="${yOff3 - 110}" fill="#8a929c" font-family="monospace" font-size="13">BODY PLAN  —  forward sections right, aft left</text>`;

  svg += `</g></svg>`;
  const p = path.join(OUT, 'boat-lines.svg');
  fs.writeFileSync(p, svg);
  console.log('wrote', p);
}
