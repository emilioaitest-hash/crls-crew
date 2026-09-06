/**
 * Fits the half-beam curve exponents and rocker so the hull's normalized
 * section-area distribution matches US Patent 5,474,008 (Vespoli), the only
 * published racing-shell area curve. Brute-force search over the shape
 * parameters, scored by RMS against the patent.
 *
 * Run:  node tools/fit-hull.js
 */
import { SPEC, sheerZ, sectionDepth } from '../src/boat/pocock.js';

const vespoli = [0, 0.085, 0.235, 0.570, 0.825, 0.963, 1.000, 0.964, 0.830, 0.582, 0.258, 0.101, 0];
const vSta = [0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.0];

const clamp01 = (v) => Math.min(1, Math.max(0, v));
const smooth = (e0, e1, x) => { const t = clamp01((x - e0) / (e1 - e0)); return t * t * (3 - 2 * t); };

function makeHalfBeam(kFwd, kAft, peak) {
  const B = SPEC.beamMax / 2;
  return (t) => {
    if (t <= 0 || t >= 1) return 0;
    if (t < peak) { const s = t / peak; return B * (1 - Math.pow(1 - s, kFwd)); }
    const s = (1 - t) / (1 - peak);
    return B * (1 - Math.pow(1 - s, kAft));
  };
}

function makeKeel(rocker, pow) {
  return (t) => { const d = (t - 0.52) / 0.52; return rocker * Math.pow(Math.min(1, Math.abs(d)), pow); };
}

function sectionN(t, nBow, nMid, nStern) {
  if (t < 0.5) return nBow + (nMid - nBow) * smooth(0.015, 0.5, t);
  return nMid + (nStern - nMid) * smooth(0.5, 0.99, t);
}

function areaBelow(t, zw, hb, kz, nB, nM, nS, M = 260) {
  const B = hb(t);
  const zs = kz(t) + sectionDepth(t) + SPEC.sheerRise * Math.pow(clamp01(Math.abs(t - 0.52) / 0.52), 2.6);
  const D = zs - kz(t);
  const n = sectionN(t, nB, nM, nS);
  const e = 2 / n;
  let area = 0, prevY = 0, prevZ = zs - D;
  for (let j = 1; j <= M; j++) {
    const th = (j / M) * Math.PI * 0.5;
    const y = B * Math.pow(Math.sin(th), e);
    const z = zs - D * Math.pow(Math.cos(th), e);
    const zm = (prevZ + z) / 2;
    if (zm < zw) area += 2 * ((prevY + y) / 2) * Math.abs(z - prevZ);
    prevY = y; prevZ = z;
  }
  return area;
}

function score(kFwd, kAft, peak, rocker, rpow, nB, nM, nS) {
  const hb = makeHalfBeam(kFwd, kAft, peak);
  const kz = makeKeel(rocker, rpow);

  // find waterline for the target displacement
  const target = 0.406;
  const vol = (zw) => {
    let v = 0; const N = 300;
    for (let i = 0; i < N; i++) v += areaBelow((i + 0.5) / N, zw, hb, kz, nB, nM, nS, 160) * (SPEC.loa / N);
    return v;
  };
  let lo = 0, hi = 0.32;
  for (let k = 0; k < 34; k++) { const m = (lo + hi) / 2; if (vol(m) < target) lo = m; else hi = m; }
  const wl = (lo + hi) / 2;

  // waterline extent
  let a = 0, b = 1;
  for (let i = 0; i <= 1500; i++) { const t = i / 1500; if (kz(t) < wl && hb(t) > 0.004) { a = t; break; } }
  for (let i = 1500; i >= 0; i--) { const t = i / 1500; if (kz(t) < wl && hb(t) > 0.004) { b = t; break; } }
  const lwl = (b - a) * SPEC.loa;

  let aMax = 0;
  const ours = vSta.map((v) => {
    const t = a + (b - a) * v;
    const ar = areaBelow(t, wl, hb, kz, nB, nM, nS, 220);
    if (ar > aMax) aMax = ar;
    return ar;
  });
  if (aMax <= 0) return { rms: 99 };
  const oursN = ours.map((x) => x / aMax);
  let ss = 0, mx = 0;
  for (let i = 0; i < vSta.length; i++) {
    const d = oursN[i] - vespoli[i];
    ss += d * d; mx = Math.max(mx, Math.abs(d));
  }
  const rms = Math.sqrt(ss / vSta.length);

  const draft = wl - kz(peak);
  const fb = (kz(peak) + sectionDepth(peak)) - wl;
  return { rms, mx, wl, lwl, draft, fb, oursN, aMax };
}

console.log('searching (coarse pass)...\n');
let best = null;
const consider = (kFwd, kAft, peak, rocker, nB, nM) => {
  const r = score(kFwd, kAft, peak, rocker, 1.9, nB, nM, 1.70);
  if (r.rms < 90 && r.lwl > 12.2 && r.lwl < 13.15 &&
      r.draft > 0.14 && r.draft < 0.21 && r.fb > 0.10 && r.fb < 0.19) {
    if (!best || r.rms < best.r.rms) best = { kFwd, kAft, peak, rocker, nB, nM, r };
  }
};

// Coarse: vary the two shape exponents that dominate the area curve.
for (const kFwd of [1.05, 1.2, 1.35, 1.5, 1.65]) {
  for (const kAft of [1.35, 1.55, 1.75, 1.95, 2.15]) {
    for (const peak of [0.48, 0.51, 0.54]) {
      consider(kFwd, kAft, peak, 0.042, 1.30, 2.05);
    }
  }
}
if (!best) { console.log('coarse pass found nothing'); process.exit(1); }
console.log(`coarse best: kFwd=${best.kFwd} kAft=${best.kAft} peak=${best.peak} rms=${best.r.rms.toFixed(4)}`);

// Refine around the coarse optimum, now including rocker and section fullness.
const c = { ...best };
for (const kFwd of [c.kFwd - 0.10, c.kFwd - 0.05, c.kFwd, c.kFwd + 0.05, c.kFwd + 0.10]) {
  for (const kAft of [c.kAft - 0.10, c.kAft - 0.05, c.kAft, c.kAft + 0.05, c.kAft + 0.10]) {
    for (const peak of [c.peak - 0.02, c.peak, c.peak + 0.02]) {
      for (const rocker of [0.034, 0.042, 0.050]) {
        for (const nM of [1.95, 2.05, 2.15]) {
          consider(kFwd, kAft, peak, rocker, 1.30, nM);
        }
      }
    }
  }
}

if (!best) { console.log('no candidate satisfied the constraints'); process.exit(1); }

console.log('BEST FIT');
console.log(`  K_FWD    ${best.kFwd}`);
console.log(`  K_AFT    ${best.kAft}`);
console.log(`  beamPeak ${best.peak}`);
console.log(`  rocker   ${best.rocker}`);
console.log(`  nBow     ${best.nB}`);
console.log(`  nMid     ${best.nM}`);
console.log(`\n  RMS ${best.r.rms.toFixed(4)}   max ${best.r.mx.toFixed(4)}`);
console.log(`  LWL ${best.r.lwl.toFixed(3)} m   draft ${best.r.draft.toFixed(4)}   freeboard ${best.r.fb.toFixed(4)}`);
console.log('\n   sta   patent    ours     diff');
for (let i = 0; i < vSta.length; i++) {
  const d = best.r.oursN[i] - vespoli[i];
  console.log(`  ${vSta[i].toFixed(2)}   ${vespoli[i].toFixed(3)}   ${best.r.oursN[i].toFixed(3)}  ${(d >= 0 ? '+' : '') + d.toFixed(3)}`);
}
