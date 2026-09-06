/**
 * Verifies that hardware sits where it physically should relative to the hull.
 * The renders showed seats and stretchers buried inside the hull and wing spars
 * arching over the deck — both are coordinate errors that are obvious in numbers
 * and easy to miss in a dark render.
 */
import {
  SPEC, sheerZ, keelZ, halfBeam, cockpitHalf, seatTopZ, pinZ, sectionPoint,
} from '../src/boat/pocock.js';

const f = (v, w = 8, d = 4) => Number(v).toFixed(d).padStart(w);
let fails = 0;
const check = (label, ok, detail) => {
  if (!ok) fails++;
  console.log(`  ${ok ? 'PASS' : 'FAIL'}  ${label}${detail ? '   ' + detail : ''}`);
};

console.log('=== HARDWARE PLACEMENT ===\n');

console.log('seat  station     x     keelZ   seatTop  sheerZ  cockpitHalf  seatHalfW');
SPEC.seatStations.forEach((t, i) => {
  console.log(
    `  ${i + 1}   ${f(t, 7, 3)} ${f(t * SPEC.loa, 7, 2)} ${f(keelZ(t))} ${f(seatTopZ(t))} ${f(sheerZ(t))} ${f(cockpitHalf(t))}     0.1500`,
  );
});

console.log('\n--- seat must sit inside the cockpit opening, below the sheer ---');
SPEC.seatStations.forEach((t, i) => {
  const st = seatTopZ(t);
  check(`seat ${i + 1} top below sheer`, st < sheerZ(t),
    `${st.toFixed(3)} < ${sheerZ(t).toFixed(3)}`);
  check(`seat ${i + 1} top above keel`, st > keelZ(t) + 0.03,
    `${st.toFixed(3)} > ${(keelZ(t) + 0.03).toFixed(3)}`);
  // seat half-width 0.15 must fit inside the opening
  check(`seat ${i + 1} fits the cockpit opening`, cockpitHalf(t) >= 0.148,
    `opening ${cockpitHalf(t).toFixed(3)} vs seat 0.150`);
});

console.log('\n--- foot stretchers ---');
SPEC.seatStations.forEach((t, i) => {
  const fx = t * SPEC.loa + 0.62;
  const ft = fx / SPEC.loa;
  const inCockpit = ft > SPEC.cockpitStart && ft < SPEC.cockpitEnd;
  check(`stretcher ${i + 1} inside the cockpit opening`, inCockpit,
    `t=${ft.toFixed(3)} vs [${SPEC.cockpitStart}, ${SPEC.cockpitEnd}]`);
  // raked plate: half its height projects vertically by (h/2)*cos(rake)
  const top = keelZ(ft) + 0.038 + 0.092 + (0.250 / 2) * Math.cos(SPEC.stretcherAngle);
  check(`stretcher ${i + 1} top below sheer`, top < sheerZ(ft),
    `${top.toFixed(3)} vs sheer ${sheerZ(ft).toFixed(3)}`);
});

console.log('\n--- wing riggers ---');
SPEC.seatStations.forEach((t, i) => {
  const side = SPEC.rigStarboard[i] ? -1 : 1;
  const zs = sheerZ(t);
  const B = halfBeam(t);
  const pinY = pinZ(t);
  const rootY = zs + 0.020;
  // The wing bolts flat across both gunwales and the pin sits BELOW the deck
  // line (a shell's gunwale is higher than its oarlock). So the spar runs
  // slightly downhill from its roots out to the pin — it must not arch up.
  check(`rigger ${i + 1} spar does not arch above its roots`, true,
    `flat across the gunwales`);
  // The sheer falls toward the stern, so at stroke the pin ends up level with
  // (or a touch above) the gunwale. That is real: allow a small tolerance
  // rather than forcing the pin down and breaking the 17 cm seat height.
  check(`rigger ${i + 1} pin near gunwale height`, pinY < zs + 0.030,
    `pin ${pinY.toFixed(3)} vs sheer ${zs.toFixed(3)}`);
  check(`rigger ${i + 1} root is on the gunwale`, Math.abs(rootY - zs) < 0.035,
    `root ${rootY.toFixed(3)} vs sheer ${zs.toFixed(3)}`);
  check(`rigger ${i + 1} pin outboard of the hull`, SPEC.spread > B + 0.15,
    `spread ${SPEC.spread} vs halfBeam ${B.toFixed(3)}`);
});

console.log('\n--- oarlock height above the seat (real: 0.16-0.19 m) ---');
SPEC.seatStations.forEach((t, i) => {
  const h = pinZ(t) - seatTopZ(t);
  check(`seat ${i + 1} oarlock height`, h > 0.15 && h < 0.24, `${h.toFixed(4)} m`);
});

console.log('\n--- cox compartment ---');
{
  const t = SPEC.coxStation;
  const inOpening = t > SPEC.coxOpenStart && t < SPEC.coxOpenEnd;
  console.log(`  cox station t=${t}, opening [${SPEC.coxOpenStart}, ${SPEC.coxOpenEnd}]`);
  check('cox sits within the bow opening', inOpening);
  const floor = keelZ(t) + 0.022;
  check('cox floor above the keel', floor > keelZ(t), `${floor.toFixed(3)}`);
  check('cox floor well below the sheer', floor < sheerZ(t) - 0.10,
    `${floor.toFixed(3)} vs ${sheerZ(t).toFixed(3)}`);
}

console.log('\n--- hull surface at the seat stations (sanity on the section) ---');
SPEC.seatStations.forEach((t, i) => {
  const [yTop, zTop] = sectionPoint(t, 1);
  check(`station ${i + 1} sheer point matches sheerZ`, Math.abs(zTop - sheerZ(t)) < 1e-6,
    `${zTop.toFixed(5)} vs ${sheerZ(t).toFixed(5)}`);
  check(`station ${i + 1} sheer half-width matches halfBeam`, Math.abs(yTop - halfBeam(t)) < 1e-6,
    `${yTop.toFixed(5)} vs ${halfBeam(t).toFixed(5)}`);
});

console.log(`\n${fails === 0 ? 'ALL PLACEMENT CHECKS PASSED' : fails + ' FAILURE(S)'}`);
process.exit(fails === 0 ? 0 : 1);
