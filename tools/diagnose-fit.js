/** Diagnose which constraint is rejecting candidates in the hull fit. */
import { SPEC, sectionDepth } from '../src/boat/pocock.js';

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
const makeKeel = (rocker, pow) => (t) => {
  const d = (t - 0.52) / 0.52; return rocker * Math.pow(Math.min(1, Math.abs(d)), pow);
};
function sectionN(t, nB, nM, nS) {
  if (t < 0.5) return nB + (nM - nB) * smooth(0.015, 0.5, t);
  return nM + (nS - nM) * smooth(0.5, 0.99, t);
}
function areaBelow(t, zw, hb, kz, nB, nM, nS, M = 260) {
  const B = hb(t);
  const zs = kz(t) + sectionDepth(t) + SPEC.sheerRise * Math.pow(clamp01(Math.abs(t - 0.52) / 0.52), 2.6);
  const D = zs - kz(t);
  const e = 2 / sectionN(t, nB, nM, nS);
  let area = 0, py = 0, pz = zs - D;
  for (let j = 1; j <= M; j++) {
    const th = (j / M) * Math.PI * 0.5;
    const y = B * Math.pow(Math.sin(th), e);
    const z = zs - D * Math.pow(Math.cos(th), e);
    if ((pz + z) / 2 < zw) area += 2 * ((py + y) / 2) * Math.abs(z - pz);
    py = y; pz = z;
  }
  return area;
}

function evaluate(kFwd, kAft, peak, rocker, nB, nM, nS) {
  const hb = makeHalfBeam(kFwd, kAft, peak);
  const kz = makeKeel(rocker, 1.9);
  const target = 0.406;
  const vol = (zw) => {
    let v = 0; const N = 260;
    for (let i = 0; i < N; i++) v += areaBelow((i + 0.5) / N, zw, hb, kz, nB, nM, nS, 150) * (SPEC.loa / N);
    return v;
  };
  let lo = 0, hi = 0.32;
  for (let k = 0; k < 32; k++) { const m = (lo + hi) / 2; if (vol(m) < target) lo = m; else hi = m; }
  const wl = (lo + hi) / 2;
  let a = 0, b = 1;
  for (let i = 0; i <= 1200; i++) { const t = i / 1200; if (kz(t) < wl && hb(t) > 0.004) { a = t; break; } }
  for (let i = 1200; i >= 0; i--) { const t = i / 1200; if (kz(t) < wl && hb(t) > 0.004) { b = t; break; } }
  const lwl = (b - a) * SPEC.loa;
  const draft = wl - kz(peak);
  const fb = (kz(peak) + sectionDepth(peak)) - wl;
  return { wl, lwl, draft, fb, a, b };
}

console.log('Which constraint is binding?\n');
console.log(' kFwd kAft peak rocker |    wl    LWL   draft  freeb | verdict');
for (const kFwd of [1.05, 1.35, 1.65]) {
  for (const kAft of [1.35, 1.75, 2.15]) {
    for (const rocker of [0.042, 0.070, 0.100]) {
      const r = evaluate(kFwd, kAft, 0.51, rocker, 1.30, 2.05, 1.70);
      const okL = r.lwl > 12.2 && r.lwl < 13.15;
      const okD = r.draft > 0.14 && r.draft < 0.21;
      const okF = r.fb > 0.10 && r.fb < 0.19;
      const why = [okL ? '' : 'LWL', okD ? '' : 'draft', okF ? '' : 'freeboard'].filter(Boolean).join(',');
      console.log(
        `${kFwd.toFixed(2)} ${kAft.toFixed(2)} ${(0.51).toFixed(2)} ${rocker.toFixed(3)}  |`,
        `${r.wl.toFixed(3)} ${r.lwl.toFixed(2)} ${r.draft.toFixed(3)} ${r.fb.toFixed(3)} |`,
        why ? 'reject: ' + why : 'OK',
      );
    }
  }
}

console.log('\nNote: LWL is length *at the waterline*. With very fine ends and shallow');
console.log('rocker the hull is immersed almost end to end, so LWL -> LOA. Pocock');
console.log('publishes WL 12.50-12.93 m against an LOA around 13.6 m, i.e. the ends');
console.log('lift clear. That requires MORE rocker than 42 mm, or a shorter LOA.');
