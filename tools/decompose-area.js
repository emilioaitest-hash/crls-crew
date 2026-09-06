/**
 * Decompose the section-area error: is the deficit coming from beam, depth, or
 * section fullness? Area at a station is roughly (halfBeam * depth * shapeFactor),
 * so comparing each factor's own normalized curve against the patent's area
 * curve tells us which one is actually wrong.
 */
import { SPEC, halfBeam, sectionDepth, keelZ, sheerZ, sectionPoint, sectionAreaBelow } from '../src/boat/pocock.js';

const vespoli = [0, 0.085, 0.235, 0.570, 0.825, 0.963, 1.000, 0.964, 0.830, 0.582, 0.258, 0.101, 0];
const vSta = [0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.0];

// waterline for 406 kg
function volumeBelow(zw, N = 700) {
  let v = 0;
  for (let i = 0; i < N; i++) v += sectionAreaBelow((i + 0.5) / N, zw, 260) * (SPEC.loa / N);
  return v;
}
let lo = 0, hi = 0.31;
for (let k = 0; k < 50; k++) { const m = (lo + hi) / 2; if (volumeBelow(m, 400) < 0.406) lo = m; else hi = m; }
const wl = (lo + hi) / 2;
console.log('waterline', wl.toFixed(4), '\n');

// Effective LWL by area threshold
let aPeak = 0;
for (let i = 0; i <= 500; i++) aPeak = Math.max(aPeak, sectionAreaBelow(i / 500, wl, 200));
const th = aPeak * 0.015;
let a = 0, b = 1;
for (let i = 0; i <= 2000; i++) { const t = i / 2000; if (sectionAreaBelow(t, wl, 200) > th) { a = t; break; } }
for (let i = 2000; i >= 0; i--) { const t = i / 2000; if (sectionAreaBelow(t, wl, 200) > th) { b = t; break; } }
console.log('LWL span t=', a.toFixed(3), '->', b.toFixed(3), ' =', ((b - a) * SPEC.loa).toFixed(2), 'm\n');

console.log(' sta      area   beamN   depthN   submDepth   patient  areaN   err');
let maxBeam = 0, maxSub = 0, maxArea = 0;
const rows = vSta.map((v) => {
  const t = a + (b - a) * v;
  const ar = sectionAreaBelow(t, wl, 400);
  const hb = halfBeam(t);
  const sub = Math.max(0, wl - keelZ(t));      // submerged depth at this station
  maxBeam = Math.max(maxBeam, hb);
  maxSub = Math.max(maxSub, sub);
  maxArea = Math.max(maxArea, ar);
  return { v, t, ar, hb, sub };
});
rows.forEach((r, i) => {
  console.log(
    r.v.toFixed(2).padStart(5),
    r.ar.toFixed(5).padStart(9),
    (r.hb / maxBeam).toFixed(3).padStart(7),
    (r.sub / maxSub).toFixed(3).padStart(8),
    r.sub.toFixed(4).padStart(11),
    vespoli[i].toFixed(3).padStart(9),
    (r.ar / maxArea).toFixed(3).padStart(7),
    ((r.ar / maxArea) - vespoli[i]).toFixed(3).padStart(7),
  );
});

console.log('\nDIAGNOSIS');
console.log('If beamN tracks the patent curve but submDepth collapses toward the ends,');
console.log('the problem is the KEEL LINE (rocker) lifting the ends out of the water,');
console.log('not the beam distribution. Area = beam x submerged depth x fullness.');
console.log('\nkeelZ at stations:');
[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1].forEach((v) => {
  const t = a + (b - a) * v;
  console.log(`  v=${v.toFixed(2)}  t=${t.toFixed(3)}  keelZ=${keelZ(t).toFixed(4)}  submerged=${(wl - keelZ(t)).toFixed(4)}`);
});
