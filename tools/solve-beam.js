/**
 * Solve the half-beam curve directly from the patent's section-area curve
 * instead of guessing exponents.
 *
 * area(t) ~= halfBeam(t) * submergedDepth(t) * fullness(t)
 *
 * We know the target area distribution (US Patent 5,474,008) and we can compute
 * submerged depth and fullness from the current geometry. So the required
 * half-beam at each station falls straight out, and we fit a smooth analytic
 * curve through it.
 */
import { SPEC, sectionDepth, keelZ } from '../src/boat/pocock.js';

const vespoli = [0, 0.085, 0.235, 0.570, 0.825, 0.963, 1.000, 0.964, 0.830, 0.582, 0.258, 0.101, 0];
const vSta = [0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.0];

const clamp01 = (v) => Math.min(1, Math.max(0, v));
const smooth = (e0, e1, x) => { const t = clamp01((x - e0) / (e1 - e0)); return t * t * (3 - 2 * t); };

const nBow = SPEC.nBow, nMid = SPEC.nMid, nStern = SPEC.nStern;
const sectionN = (t) => (t < 0.5
  ? nBow + (nMid - nBow) * smooth(0.015, 0.5, t)
  : nMid + (nStern - nMid) * smooth(0.5, 0.99, t));

/** Fraction of the bounding box (2*halfBeam x submergedDepth) that a
 *  superellipse section actually fills, below the waterline. */
function fullness(t, wl) {
  const zs = keelZ(t) + sectionDepth(t) + SPEC.sheerRise * Math.pow(clamp01(Math.abs(t - 0.52) / 0.52), 2.6);
  const D = zs - keelZ(t);
  const e = 2 / sectionN(t);
  const M = 400;
  let area = 0, py = 0, pz = zs - D;
  for (let j = 1; j <= M; j++) {
    const th = (j / M) * Math.PI * 0.5;
    const y = Math.pow(Math.sin(th), e);           // normalized half-width
    const z = zs - D * Math.pow(Math.cos(th), e);
    if ((pz + z) / 2 < wl) area += 2 * ((py + y) / 2) * Math.abs(z - pz);
    py = y; pz = z;
  }
  const sub = Math.max(1e-6, wl - keelZ(t));
  return area / (2 * sub);   // area if halfBeam were 1
}

// Target: displacement 0.406 m^3 over the LOA.
// Work in normalized area, then scale to hit displacement.
const N = 400;
const wlGuess = 0.170;

// required normalized area at every station, interpolated from the patent
function patentAt(u) {
  if (u <= 0) return 0;
  if (u >= 1) return 0;
  for (let i = 1; i < vSta.length; i++) {
    if (u <= vSta[i]) {
      const f = (u - vSta[i - 1]) / (vSta[i] - vSta[i - 1]);
      return vespoli[i - 1] + f * (vespoli[i] - vespoli[i - 1]);
    }
  }
  return 0;
}

// Required half-beam shape (unnormalized): hb ~ targetArea / (subDepth * fullness)
const samples = [];
for (let i = 0; i <= N; i++) {
  const t = i / N;
  const sub = Math.max(1e-6, wlGuess - keelZ(t));
  const fl = fullness(t, wlGuess);
  const need = patentAt(t) / (sub * fl);
  samples.push({ t, need });
}
const peak = Math.max(...samples.map((s) => s.need));
samples.forEach((s) => { s.norm = s.need / peak; });

console.log('Required half-beam shape (normalized), derived from the patent:\n');
console.log('    t    required');
for (const u of [0, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.52, 0.6, 0.7, 0.8, 0.9, 0.95, 1]) {
  const s = samples[Math.round(u * N)];
  console.log(`  ${u.toFixed(2)}    ${s.norm.toFixed(4)}`);
}

// Fit  norm(t) = 1 - (1 - s)^k  on each side of the peak, least squares over k.
let tPeak = samples.reduce((best, s) => (s.norm > best.norm ? s : best), samples[0]).t;
console.log(`\npeak of required curve at t = ${tPeak.toFixed(3)}`);

function fitSide(from, to, forward) {
  let bestK = 1, bestE = Infinity;
  for (let k = 0.4; k <= 3.5; k += 0.005) {
    let e = 0, n = 0;
    for (const s of samples) {
      if (s.t < from || s.t > to) continue;
      const u = forward ? (s.t - from) / (to - from) : (to - s.t) / (to - from);
      const model = 1 - Math.pow(1 - clamp01(u), k);
      e += (model - s.norm) ** 2; n++;
    }
    e = Math.sqrt(e / Math.max(1, n));
    if (e < bestE) { bestE = e; bestK = k; }
  }
  return { k: bestK, rms: bestE };
}

const fwd = fitSide(0, tPeak, true);
const aft = fitSide(tPeak, 1, false);
console.log(`\nK_FWD = ${fwd.k.toFixed(3)}   (fit rms ${fwd.rms.toFixed(4)})`);
console.log(`K_AFT = ${aft.k.toFixed(3)}   (fit rms ${aft.rms.toFixed(4)})`);
console.log(`beamPeak = ${tPeak.toFixed(3)}`);

console.log('\nfitted vs required:');
console.log('    t   required   fitted');
for (const u of [0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]) {
  const s = samples[Math.round(u * N)];
  const model = u < tPeak
    ? 1 - Math.pow(1 - clamp01(u / tPeak), fwd.k)
    : 1 - Math.pow(1 - clamp01((1 - u) / (1 - tPeak)), aft.k);
  console.log(`  ${u.toFixed(2)}    ${s.norm.toFixed(4)}   ${model.toFixed(4)}`);
}
