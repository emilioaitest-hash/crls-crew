/**
 * Pocock Hypercarbon Comp K4+  —  "Wylde"
 * Cambridge Rindge & Latin School
 *
 * Parametric hull lofted from station geometry. Metres throughout.
 * Bow at x=0, stern at x=LOA. Rowers face the stern; the boat travels bow-first.
 *
 * WHAT THE RESEARCH FORCED (research/04-pocock-comp4.md):
 *   - This is a BOW-LOADER. The coxswain lies semi-supine in a compartment just
 *     aft of the bow ball. The stern is a clean closed deck tapering to a point.
 *     There is no stern cockpit. This is the single biggest shape decision.
 *   - Monocoque: one continuous stressed skin, no internal ribs or shoulders,
 *     with a full-length structural pan forming the cockpit floor.
 *   - Exit angle is LARGER than entry angle (~4.5 deg vs ~3.8 deg): the bow is
 *     finer than the stern. Most people model shells symmetric. They aren't.
 *   - Topsides flare above the waterline through the cox compartment so the deck
 *     is wide while the submerged section stays needle-fine.
 *
 * The section-area distribution is checked against US Patent 5,474,008
 * (Vespoli), the only published racing-shell area curve, in tools/validate-hull.js.
 */

import * as THREE from 'three';

export const SPEC = {
  /* --- principal dimensions ---
   * Pocock publishes WATERLINE figures, not overall ones (research §2.1):
   *   Comp K4+ medium: WL length 12.65 m
   *   Core K4+ medium: WL beam   43.1 cm  (Comp WL beam is not published;
   *                                        the Core shares the hull class)
   * LOA and max beam at the saxboard are therefore larger than the waterline
   * figures: the hull flares above the water and the fine ends lift clear. */
  loa: 13.60,          // length overall (inferred: WL 12.65 / ~0.93)
  beamMax: 0.550,      // max beam at the saxboard (deck level)
  beamWL: 0.431,       // max beam AT THE WATERLINE — published, Core K4+ medium
  beamPeak: 0.398,     // station of max beam (solved from the patent area curve)
  depthMid: 0.310,     // sheer-to-keel amidships
  depthEnd: 0.100,
  rocker: 0.052,       // keel rise at the ends; lifts the fine ends clear
  sheerRise: 0.052,

  /* Topside flare: the hull widens above the waterline everywhere, not only at
   * the bow. This is what reconciles a 43 cm waterline beam with a 55 cm
   * saxboard beam, and it is why a shell looks wider than it floats. */
  flareWL: 0.62,       // height fraction where flare begins (0=keel, 1=sheer)

  /* --- entry / exit half-angles, radians (patent-derived) --- */
  entryAngle: 3.8 * Math.PI / 180,
  exitAngle: 4.5 * Math.PI / 180,

  /* --- section fullness: superellipse exponent bow -> mid -> stern --- */
  nBow: 1.30,          // fine V
  nMid: 2.05,          // semicircle
  nStern: 1.70,        // shallow U

  /* --- bow flare (creates the coxswain's volume above the waterline) --- */
  flareStart: 0.24,    // flare fades out by this station
  flareMax: 0.088,     // extra half-width at the sheer, at the bow
  flareHeight: 0.55,   // only applies above this fraction of section depth

  /* --- coxswain compartment (bow-loaded) --- */
  coxOpenStart: 0.070, // 0.95 m
  coxOpenEnd: 0.136,   // 1.85 m  -> 0.90 m long (World Rowing min 0.70 m)
  coxHalfMax: 0.150,

  /* --- main cockpit: one continuous opening for all four rowers --- */
  cockpitStart: 0.320, // 4.35 m
  cockpitEnd: 0.769,   // 10.45 m
  cockpitHalfMax: 0.192,
  gunwaleWidth: 0.030,

  /* --- crew: seat 1 at bow, seat 4 (stroke) nearest the stern --- */
  seatStations: [0.4155, 0.5052, 0.5949, 0.6846], // 1.22 m apart
  coxStation: 0.103,

  /* --- rigging ---
   * oarlockHeight is measured from the SEAT TOP, which is how riggers are
   * actually set up ("height above the seat", Pocock's historical standard
   * 6.25 in = 15.9 cm; modern sweep 16-19 cm). It is NOT measured from the
   * gunwale — treating it as a gunwale offset put the pins 35 cm above the
   * seat, roughly double reality, which the placement validator caught. */
  spread: 0.850,       // centreline to pin
  oarlockHeight: 0.170,   // ABOVE THE SEAT TOP
  slideLength: 0.810,  // Pocock catalogue: 32 in tracks
  trackGauge: 0.285,
  stretcherAngle: 40 * Math.PI / 180,

  /* --- sweep oar --- */
  oarLength: 3.74,
  bladeLength: 0.552,
  bladeWidth: 0.248,

  /* Rigger side per seat, bow -> stern. Strictly alternating; stroke on port.
     true = oarlock to starboard (-z), false = to port (+z). */
  rigStarboard: [true, false, true, false],

  bowBallDia: 0.040,
};

/* ------------------------------------------------------------------ *
 * Curves
 * ------------------------------------------------------------------ */

const clamp01 = (v) => Math.min(1, Math.max(0, v));
export const smooth = (e0, e1, x) => {
  const t = clamp01((x - e0) / (e1 - e0));
  return t * t * (3 - 2 * t);
};

// Half-beam shape. Separate fore and aft curves so the entry can be finer than
// the exit, which is what the patent data says a real shell does.
//
// These are not guesses. tools/solve-beam.js inverts the section-area curve of
// US Patent 5,474,008 — area(t) = halfBeam(t) x submergedDepth(t) x fullness(t)
// — to recover the half-beam distribution the patent implies, then least-squares
// fits this two-sided form to it. Max beam lands forward of midships, which is
// characteristic of a racing shell: the volume is carried early and the run aft
// is long and fine.
const K_FWD = 2.00;
const K_AFT = 2.54;

/**
 * Normalized beam distribution along the length: 0 at the ends, 1 at beamPeak.
 * Both the waterline beam and the saxboard beam are scaled from this, so the
 * plan-view shape of the hull is defined in exactly one place.
 *
 * Two regimes, blended:
 *   - through the body, a two-sided power curve fitted to the patent's
 *     section-area distribution (tools/solve-beam.js)
 *   - at each end, a straight-line wedge of a prescribed half-angle
 *
 * The wedge matters because a racing shell's entry is genuinely a straight fine
 * taper, and because angle is a *slope* condition: a power curve of exponent >1
 * has zero slope at the tip (infinitely sharp), and exponent <1 has infinite
 * slope (blunt). Only a linear term gives a real, finite entry angle. The blend
 * is smooth so no crease appears in the surface.
 */
const BOW_WEDGE_LEN = 0.10;    // fraction of LOA over which the wedge rules
const STERN_WEDGE_LEN = 0.09;

export function beamShape(t) {
  const tp = SPEC.beamPeak;
  if (t <= 0 || t >= 1) return 0;

  let base;
  if (t < tp) {
    const s = t / tp;
    base = 1 - Math.pow(1 - s, K_FWD);
  } else {
    const s = (1 - t) / (1 - tp);
    base = 1 - Math.pow(1 - s, K_AFT);
  }

  // Straight wedges. Slope is set so the half-angle at the sheer matches the
  // target: tan(angle) = d(halfBeam)/dx, and halfBeam = (beamMax/2)*shape.
  const perMetre = (ang) => Math.tan(ang) / (SPEC.beamMax / 2);   // d(shape)/dx
  if (t < BOW_WEDGE_LEN) {
    const wedge = perMetre(SPEC.entryAngle) * (t * SPEC.loa);
    const w = smooth(0, BOW_WEDGE_LEN, t);        // 0 at tip -> 1 at zone end
    base = wedge * (1 - w) + base * w;
  }
  const d = 1 - t;
  if (d < STERN_WEDGE_LEN) {
    const wedge = perMetre(SPEC.exitAngle) * (d * SPEC.loa);
    const w = smooth(0, STERN_WEDGE_LEN, d);
    base = wedge * (1 - w) + base * w;
  }
  return Math.max(0, base);
}

/** Half-beam at the sheer (saxboard), metres — the widest point of a section. */
export function halfBeam(t) {
  return (SPEC.beamMax / 2) * beamShape(t);
}

/** Half-beam at the waterline, metres. */
export function halfBeamWL(t) {
  return (SPEC.beamWL / 2) * beamShape(t);
}

/** Vertical distance from sheer down to keel at station t. */
export function sectionDepth(t) {
  const body = Math.pow(Math.sin(Math.PI * Math.pow(clamp01(t), 0.94)), 0.52);
  return SPEC.depthEnd + (SPEC.depthMid - SPEC.depthEnd) * body;
}

/** Keel line. Lowest amidships, lifting toward both ends. */
export function keelZ(t) {
  const d = (t - 0.52) / 0.52;
  return SPEC.rocker * Math.pow(Math.abs(Math.min(1, Math.abs(d))), 1.9);
}

/** Sheer (gunwale) height. */
export function sheerZ(t) {
  const d = Math.abs(t - 0.52) / 0.52;
  return keelZ(t) + sectionDepth(t) + SPEC.sheerRise * Math.pow(clamp01(d), 2.6);
}

/** Superellipse exponent, morphing bow -> mid -> stern. */
function sectionN(t) {
  if (t < 0.5) return THREE.MathUtils.lerp(SPEC.nBow, SPEC.nMid, smooth(0.015, 0.5, t));
  return THREE.MathUtils.lerp(SPEC.nMid, SPEC.nStern, smooth(0.5, 0.99, t));
}

/**
 * Extra half-width from bow flare, at height fraction s of the section.
 * Zero below flareHeight, growing toward the sheer, and only near the bow.
 * This is what gives the coxswain somewhere to lie without fattening the
 * underwater body.
 */
function flareAt(t, s) {
  if (t >= SPEC.flareStart) return 0;
  const along = 1 - smooth(0.03, SPEC.flareStart, t);   // 1 at bow -> 0
  const up = smooth(SPEC.flareHeight, 1.0, s);          // 0 low -> 1 at sheer
  return SPEC.flareMax * along * up;
}

/**
 * Point on a hull section.
 *
 * The section is built in two parts, which is what a real racing shell is:
 *   below flareWL  — a narrow, near-semicircular underwater body whose maximum
 *                    width is beamWL (43 cm), the part that actually displaces
 *   above flareWL  — topsides flaring out to the saxboard beam (55 cm), plus
 *                    extra flare at the bow to house the coxswain
 *
 * Modelling this as one curve from keel to sheer — which is the obvious thing
 * to do — makes the underwater body 28% too wide, and the hull then floats end
 * to end instead of lifting its fine ends clear. That was a real bug here.
 *
 * @param t station 0..1  @param s 0 at keel -> 1 at sheer
 * @returns [halfWidth, height]
 */
export function sectionPoint(t, s) {
  const shapeF = beamShape(t);            // 0..1 along the length
  const zs = sheerZ(t);
  const D = zs - keelZ(t);
  const n = sectionN(t);
  const su = clamp01(s);
  const th = su * Math.PI * 0.5;
  const e = 2 / n;

  // underwater body: superellipse limited to the waterline beam
  const halfWL = (SPEC.beamWL / 2) * shapeF;
  let y = halfWL * Math.pow(Math.sin(th), e);

  // topside flare above flareWL, opening out to the saxboard beam
  if (su > SPEC.flareWL) {
    const up = smooth(SPEC.flareWL, 1.0, su);
    const halfDeck = (SPEC.beamMax / 2) * shapeF;
    y += (halfDeck - halfWL) * Math.pow(up, 1.35);
  }

  // extra bow flare for the coxswain compartment
  y += flareAt(t, su);

  const z = zs - D * Math.pow(Math.cos(th), e);
  return [y, z];
}

/* ------------------------------------------------------------------ *
 * Reference heights used by both the hull and the hardware.
 * Declared here (before the mesh builders) so they are initialised by the
 * time any module-level geometry construction reads them.
 * ------------------------------------------------------------------ */

/** Seat top height at a station. */
export function seatTopZ(t) {
  return keelZ(t) + 0.130;
}

/**
 * Height of the oarlock pin. Measured from the SEAT TOP, which is how rigging
 * is actually specified — not from the gunwale.
 */
export function pinZ(t) {
  return seatTopZ(t) + SPEC.oarlockHeight;
}

/* ------------------------------------------------------------------ *
 * Deck openings
 * ------------------------------------------------------------------ */

function openingHalf(t, a, b, wMax, endPow) {
  if (t <= a || t >= b) return 0;
  const u = (t - a) / (b - a);
  const shape = Math.pow(Math.sin(Math.PI * u), endPow);
  const limit = Math.max(0, halfBeam(t) + flareAt(t, 1) - SPEC.gunwaleWidth);
  return Math.min(wMax * shape, limit);
}

/** Coxswain compartment opening (bow). */
export function coxHalf(t) {
  return openingHalf(t, SPEC.coxOpenStart, SPEC.coxOpenEnd, SPEC.coxHalfMax, 0.55);
}

/** Main cockpit opening (all four rowers). */
export function cockpitHalf(t) {
  return openingHalf(t, SPEC.cockpitStart, SPEC.cockpitEnd, SPEC.cockpitHalfMax, 0.34);
}

/** Combined opening at t — the deck is closed wherever this is 0. */
export function deckOpenHalf(t) {
  return Math.max(coxHalf(t), cockpitHalf(t));
}

/* ------------------------------------------------------------------ *
 * Mesh building
 * ------------------------------------------------------------------ */

const pushTri = (idx, a, b, c) => { idx.push(a, b, c); };

function finish(pos, uv, idx) {
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2));
  g.setIndex(idx);
  g.computeVertexNormals();
  return g;
}

/** Outer hull skin, keel to sheer, both sides. */
export function buildHull({ stations = 420, ring = 40 } = {}) {
  const pos = [], uv = [], idx = [];
  const L = SPEC.loa;
  const cols = ring * 2 + 1;

  for (let i = 0; i <= stations; i++) {
    // cosine spacing puts more stations at the fine ends where curvature is high
    const t = 0.5 - 0.5 * Math.cos(Math.PI * (i / stations));
    for (let j = 0; j < cols; j++) {
      const k = j - ring;
      const s = Math.abs(k) / ring;
      const sgn = k === 0 ? 0 : Math.sign(k);
      const [y, z] = sectionPoint(t, s);
      pos.push(t * L, z, y * sgn);
      uv.push(t, (k / ring) * 0.5 + 0.5);
    }
  }
  for (let i = 0; i < stations; i++) {
    for (let j = 0; j < cols - 1; j++) {
      const a = i * cols + j, b = a + 1, c = a + cols, d = c + 1;
      pushTri(idx, a, c, b); pushTri(idx, b, c, d);
    }
  }
  return finish(pos, uv, idx);
}

/** Deck: sheer inboard to the opening edge (or centreline where closed). */
export function buildDeck({ stations = 420, across = 12 } = {}) {
  const pos = [], uv = [], idx = [];
  const L = SPEC.loa;
  const cols = across + 1;

  for (const side of [1, -1]) {
    const base = pos.length / 3;
    for (let i = 0; i <= stations; i++) {
      const t = 0.5 - 0.5 * Math.cos(Math.PI * (i / stations));
      const B = halfBeam(t) + flareAt(t, 1);
      const open = deckOpenHalf(t);
      const zs = sheerZ(t);
      for (let j = 0; j <= across; j++) {
        const f = j / across;
        const y = THREE.MathUtils.lerp(B, open, f);
        // deck crown: peaks at the centreline where the deck is closed
        const rel = B > 1e-6 ? 1 - y / B : 0;
        const crown = 0.016 * Math.pow(clamp01(rel), 1.5) * (open > 0 ? 0.35 : 1);
        const lip = open > 0 ? 0.005 * smooth(0.6, 1, f) : 0;
        pos.push(t * L, zs + crown - lip, y * side);
        uv.push(t, f);
      }
    }
    for (let i = 0; i < stations; i++) {
      for (let j = 0; j < across; j++) {
        const a = base + i * cols + j, b = a + 1, c = a + cols, d = c + 1;
        if (side === 1) { pushTri(idx, a, c, b); pushTri(idx, b, c, d); }
        else { pushTri(idx, a, b, c); pushTri(idx, b, d, c); }
      }
    }
  }
  return finish(pos, uv, idx);
}

/**
 * Inner surfaces of an opening: the coaming wall dropping to the pan floor.
 * Used for both the cox compartment and the main cockpit.
 */
function buildWell(a, b, halfFn, { stations = 260, depthRing = 9, floorLift = 0.028 } = {}) {
  const pos = [], uv = [], idx = [];
  const L = SPEC.loa;
  const cols = depthRing + 1;

  for (const side of [1, -1]) {
    const base = pos.length / 3;
    for (let i = 0; i <= stations; i++) {
      const t = a + (b - a) * (i / stations);
      const w = halfFn(t);
      const zs = sheerZ(t);
      const floor = keelZ(t) + floorLift;
      for (let j = 0; j <= depthRing; j++) {
        const f = j / depthRing;
        const y = w * (1 - 0.52 * Math.pow(f, 1.6));
        const z = THREE.MathUtils.lerp(zs, floor, Math.pow(f, 0.88));
        pos.push(t * L, z, y * side);
        uv.push(t, f);
      }
    }
    for (let i = 0; i < stations; i++) {
      for (let j = 0; j < depthRing; j++) {
        const p = base + i * cols + j, q = p + 1, r = p + cols, s2 = r + 1;
        if (side === 1) { pushTri(idx, p, q, r); pushTri(idx, q, s2, r); }
        else { pushTri(idx, p, r, q); pushTri(idx, q, r, s2); }
      }
    }
  }

  // floor pan
  const fb = pos.length / 3;
  for (let i = 0; i <= stations; i++) {
    const t = a + (b - a) * (i / stations);
    const w = halfFn(t) * 0.48;
    const z = keelZ(t) + floorLift;
    pos.push(t * L, z, w); uv.push(t, 0);
    pos.push(t * L, z, -w); uv.push(t, 1);
  }
  for (let i = 0; i < stations; i++) {
    const p = fb + i * 2;
    pushTri(idx, p, p + 1, p + 2);
    pushTri(idx, p + 1, p + 3, p + 2);
  }
  return finish(pos, uv, idx);
}

export function buildCockpitWell() {
  return buildWell(SPEC.cockpitStart, SPEC.cockpitEnd, cockpitHalf, { stations: 300 });
}

export function buildCoxWell() {
  return buildWell(SPEC.coxOpenStart, SPEC.coxOpenEnd, coxHalf,
    { stations: 120, depthRing: 8, floorLift: 0.022 });
}

/* ------------------------------------------------------------------ *
 * Helpers shared with hardware.js
 * ------------------------------------------------------------------ */

export function tube(a, b, r, seg = 12) {
  const dir = new THREE.Vector3().subVectors(b, a);
  const len = dir.length();
  const g = new THREE.CylinderGeometry(r, r, len, seg, 1, false);
  g.translate(0, len / 2, 0);
  g.applyQuaternion(new THREE.Quaternion().setFromUnitVectors(
    new THREE.Vector3(0, 1, 0), dir.clone().normalize()));
  g.translate(a.x, a.y, a.z);
  return g;
}

export const V = (x, y, z) => new THREE.Vector3(x, y, z);

/** Section area below a given waterline height — used by the validator. */
export function sectionAreaBelow(t, zw, M = 500) {
  let area = 0;
  let prev = sectionPoint(t, 0);
  for (let j = 1; j <= M; j++) {
    const cur = sectionPoint(t, j / M);
    const zMid = (prev[1] + cur[1]) / 2;
    if (zMid < zw) area += 2 * ((prev[0] + cur[0]) / 2) * Math.abs(cur[1] - prev[1]);
    prev = cur;
  }
  return area;
}
