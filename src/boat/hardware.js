/**
 * Rigging and hardware for the Pocock Hypercarbon Comp K4+.
 *
 * All geometry derives from SPEC so the assembly stays coherent when a
 * dimension moves. What makes a shell read as real is this hardware: the wing
 * riggers zigzagging port/starboard down the boat, the tracks, the shoes raked
 * back at 40 degrees, the hatchet blades. Get those wrong and no amount of
 * shading rescues it.
 *
 * Key facts this file encodes (research/04-pocock-comp4.md):
 *   - G7 carbon WING rigger, bolted across the TOP of the gunwales, not
 *     side-mounted tubes. One wing spar per station plus one bowbrace.
 *   - Riggers alternate sides strictly: S, P, S, P from bow to stern.
 *   - Tracks are 32 in / 81 cm (Pocock catalogue), not the 70 cm often quoted.
 *   - Integrated fin-and-rudder with no gap between them.
 */

import * as THREE from 'three';
import {
  SPEC, sheerZ, keelZ, halfBeam, tube, V, seatTopZ, pinZ, smooth,
} from './pocock.js';

/* ------------------------------------------------------------------ *
 * Geometry merge (avoids depending on BufferGeometryUtils)
 * ------------------------------------------------------------------ */
export function mergeGeos(geos) {
  const valid = geos.filter((g) => g && g.attributes.position);
  const out = new THREE.BufferGeometry();
  let vCount = 0, iCount = 0;
  for (const g of valid) {
    if (!g.attributes.normal) g.computeVertexNormals();
    if (!g.index) {
      const n = g.attributes.position.count;
      g.setIndex(Array.from({ length: n }, (_, i) => i));
    }
    vCount += g.attributes.position.count;
    iCount += g.index.count;
  }
  const pos = new Float32Array(vCount * 3);
  const nrm = new Float32Array(vCount * 3);
  const idx = new Uint32Array(iCount);
  let vo = 0, io = 0;
  for (const g of valid) {
    pos.set(g.attributes.position.array, vo * 3);
    nrm.set(g.attributes.normal.array, vo * 3);
    const gi = g.index.array;
    for (let i = 0; i < gi.length; i++) idx[io + i] = gi[i] + vo;
    io += gi.length;
    vo += g.attributes.position.count;
  }
  out.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  out.setAttribute('normal', new THREE.BufferAttribute(nrm, 3));
  out.setIndex(new THREE.BufferAttribute(idx, 1));
  return out;
}

const box = (w, h, d, x, y, z, rz = 0, ry = 0) => {
  const g = new THREE.BoxGeometry(w, h, d);
  if (rz) g.rotateZ(rz);
  if (ry) g.rotateY(ry);
  g.translate(x, y, z);
  return g;
};

/** Sign of the rigger side for seat i: +1 = port (+z), -1 = starboard (-z). */
export function rigSide(i) {
  return SPEC.rigStarboard[i] ? -1 : 1;
}

/* ------------------------------------------------------------------ *
 * G7 carbon wing riggers
 * ------------------------------------------------------------------ *
 * Each station carries ONE wing: an airfoil spar bolted across both gunwales,
 * swept aft and rising outboard to the pin on whichever side that seat rows.
 * Plus a bowbrace running forward to the gunwale. Far fewer members than a
 * tubular rigger, which is the main visual difference.
 */
export function buildRiggers() {
  const geos = [];
  const L = SPEC.loa;

  SPEC.seatStations.forEach((t, i) => {
    const side = rigSide(i);
    const x = t * L;
    const zs = sheerZ(t);
    const B = halfBeam(t);

    // Pin: outboard at `spread`, at the correct height ABOVE THE SEAT, aft a touch.
    const pin = V(x + 0.055, pinZ(t), side * SPEC.spread);

    // Wing spar: from the far gunwale, across the boat, out to the pin.
    const rootFar = V(x + 0.030, zs + 0.020, -side * (B - 0.010));
    const rootNear = V(x + 0.030, zs + 0.020, side * (B - 0.010));

    // Build the spar as a swept airfoil: a lofted ribbon rather than a tube.
    geos.push(wingSpar(rootFar, rootNear, pin, side));

    // Gunwale saddles where the wing bolts down (top-mounted, both sides)
    for (const r of [rootFar, rootNear]) {
      geos.push(box(0.115, 0.022, 0.052, r.x, r.y - 0.008, r.z));
      // bolt heads
      for (const dx of [-0.035, 0.035]) {
        const b = new THREE.CylinderGeometry(0.005, 0.005, 0.012, 8);
        b.translate(r.x + dx, r.y + 0.008, r.z);
        geos.push(b);
      }
    }

    // Bowbrace: diagonal stay running forward from the wing to the gunwale.
    const braceFoot = V(x - 0.46, zs + 0.010, side * (B - 0.014));
    const braceTop = pin.clone().lerp(rootNear, 0.30).add(V(0, -0.012, 0));
    geos.push(tube(braceFoot, braceTop, 0.0085, 10));
    geos.push(box(0.055, 0.014, 0.026, braceFoot.x, braceFoot.y, braceFoot.z));

    /* --- oarlock assembly --- */
    const pinBot = pin.clone().add(V(0, -0.030, 0));
    const pinTop = pin.clone().add(V(0, 0.068, 0));
    geos.push(tube(pinBot, pinTop, 0.0064, 10));   // 1/2 in stainless pin

    // Concept2 swivel: a U-block the oar sits in, opening outboard.
    const swY = pin.y + 0.026;
    const u = new THREE.TorusGeometry(0.031, 0.0092, 8, 20, Math.PI * 1.30);
    u.rotateX(Math.PI / 2);
    u.rotateY(side > 0 ? -0.42 : Math.PI + 0.42);
    u.translate(pin.x, swY, pin.z);
    geos.push(u);

    // gate bar across the top
    geos.push(box(0.011, 0.052, 0.011, pin.x, swY + 0.032, pin.z + side * 0.028));

    // pitch/height spacers stacked under the swivel
    for (let s = 0; s < 3; s++) {
      const sp = new THREE.CylinderGeometry(0.014, 0.014, 0.0055, 12);
      sp.translate(pin.x, pin.y - 0.006 - s * 0.006, pin.z);
      geos.push(sp);
    }
  });

  return mergeGeos(geos);
}

/**
 * A swept wing spar as a lofted ribbon with an airfoil-ish section.
 * Runs far gunwale -> near gunwale -> out and up to the pin.
 */
function wingSpar(rootFar, rootNear, pin, side) {
  const pts = [];
  const N = 26;
  // quadratic through the three control points, then out to the pin
  for (let i = 0; i <= N; i++) {
    const u = i / N;
    let p;
    if (u < 0.45) {
      const s = u / 0.45;
      p = rootFar.clone().lerp(rootNear, s);
      // Flat across the gunwales. A real wing bolts down to both saxboards; an
      // arch over the cockpit would foul the rowers and looked like a handle.
    } else {
      const s = (u - 0.45) / 0.55;
      const mid = rootNear.clone().lerp(pin, 0.5).add(V(-0.02, 0.03, 0));
      const a = rootNear.clone().lerp(mid, s);
      const b = mid.clone().lerp(pin, s);
      p = a.lerp(b, s);
    }
    pts.push(p);
  }

  const pos = [], idx = [];
  const CH = 8;                                   // chord samples
  for (let i = 0; i <= N; i++) {
    const p = pts[i];
    const nxt = pts[Math.min(N, i + 1)];
    const prv = pts[Math.max(0, i - 1)];
    const tan = new THREE.Vector3().subVectors(nxt, prv).normalize();
    const up = new THREE.Vector3(0, 1, 0);
    const chordDir = new THREE.Vector3().crossVectors(tan, up).normalize();
    const u = i / N;
    // chord tapers outboard; thickness follows a simple airfoil profile
    const chord = THREE.MathUtils.lerp(0.085, 0.052, u);
    const thick = THREE.MathUtils.lerp(0.020, 0.013, u);
    for (let c = 0; c <= CH; c++) {
      const cu = c / CH;                          // 0 leading -> 1 trailing
      const off = (cu - 0.5) * chord;
      const th = thick * Math.sin(Math.PI * Math.pow(cu, 0.75)) * 0.5;
      const base = p.clone().addScaledVector(chordDir, off);
      pos.push(base.x, base.y + th, base.z);
      pos.push(base.x, base.y - th, base.z);
    }
  }
  const perRow = (CH + 1) * 2;
  for (let i = 0; i < N; i++) {
    for (let c = 0; c < CH; c++) {
      const a = i * perRow + c * 2;
      const b = a + perRow;
      idx.push(a, b, a + 2, a + 2, b, b + 2);         // top
      idx.push(a + 1, a + 3, b + 1, a + 3, b + 3, b + 1); // bottom
    }
  }
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  g.setIndex(idx);
  g.computeVertexNormals();
  return g;
}

/* ------------------------------------------------------------------ *
 * Slides, seats, foot stretchers
 * ------------------------------------------------------------------ */
export function buildSlidesAndSeats() {
  const geos = [];
  const L = SPEC.loa;
  const half = SPEC.trackGauge / 2;

  SPEC.seatStations.forEach((t) => {
    const x = t * L;
    const zt = keelZ(t) + 0.072;
    const len = SPEC.slideLength;

    // tracks
    for (const s of [1, -1]) {
      geos.push(box(len, 0.013, 0.021, x - 0.05, zt, s * half));
      for (const dx of [-len / 2 + 0.06, 0, len / 2 - 0.06]) {
        geos.push(box(0.032, 0.026, 0.017, x - 0.05 + dx, zt - 0.019, s * half));
      }
      // end stops
      for (const dx of [-len / 2 + 0.012, len / 2 - 0.012]) {
        geos.push(box(0.010, 0.020, 0.026, x - 0.05 + dx, zt + 0.016, s * half));
      }
    }

    // seat, parked around a third up the slide
    const sx = x - 0.03;
    const sy = seatTopZ(t);
    geos.push(contouredSeat(sx, sy));

    // wheels
    for (const dx of [-0.105, 0.105]) {
      for (const s of [1, -1]) {
        const w = new THREE.CylinderGeometry(0.018, 0.018, 0.015, 12);
        w.rotateX(Math.PI / 2);
        w.translate(sx + dx, zt + 0.018, s * half);
        geos.push(w);
      }
    }

    /* foot stretcher: shoes on a raked footboard */
    const fx = x + 0.62;
    const fz = keelZ(t) + 0.038;
    const rake = SPEC.stretcherAngle;

    // Footboard: sized so its top edge stays below the sheer once raked.
    geos.push(box(0.022, 0.250, 0.290, fx, fz + 0.092, 0, rake));

    for (const s of [1, -1]) {
      // shoe
      geos.push(box(0.072, 0.200, 0.096, fx - 0.026, fz + 0.098, s * 0.078, rake, s * 0.05));
      // heel cup
      geos.push(box(0.054, 0.048, 0.090, fx + 0.046, fz + 0.022, s * 0.078));
      // heel tie
      const tie = new THREE.CylinderGeometry(0.0022, 0.0022, 0.075, 6);
      tie.rotateZ(Math.PI / 2.6);
      tie.translate(fx + 0.026, fz + 0.044, s * 0.078);
      geos.push(tie);
    }

    // adjustment rails
    for (const s of [1, -1]) {
      geos.push(box(0.320, 0.012, 0.016, fx - 0.06, fz + 0.003, s * 0.112));
    }
  });

  return mergeGeos(geos);
}

/** Contoured saddle: two buttock pockets with a relief channel between. */
function contouredSeat(x, y) {
  const shape = new THREE.Shape();
  const w = 0.150, d = 0.128;
  shape.moveTo(-d, 0);
  shape.quadraticCurveTo(-d, -w * 0.85, -d * 0.35, -w);
  shape.lineTo(d * 0.45, -w * 0.92);
  shape.quadraticCurveTo(d, -w * 0.6, d, 0);
  shape.quadraticCurveTo(d, w * 0.6, d * 0.45, w * 0.92);
  shape.lineTo(-d * 0.35, w);
  shape.quadraticCurveTo(-d, w * 0.85, -d, 0);
  const g = new THREE.ExtrudeGeometry(shape, {
    depth: 0.020, bevelEnabled: true, bevelThickness: 0.006,
    bevelSize: 0.007, bevelSegments: 3, curveSegments: 14,
  });
  g.rotateX(-Math.PI / 2);
  g.rotateY(Math.PI / 2);
  g.translate(x, y, 0);
  return g;
}

/* ------------------------------------------------------------------ *
 * Fittings: bow ball, integrated fin + rudder, bow number clip
 * ------------------------------------------------------------------ */
export function buildFittings() {
  const geos = [];
  const L = SPEC.loa;

  // Bow ball — white, 4 cm, on the point
  const ball = new THREE.SphereGeometry(SPEC.bowBallDia / 2, 20, 16);
  ball.translate(-0.010, sheerZ(0) - 0.058, 0);
  geos.push(ball);

  // Integrated fin + rudder: continuous foil, no gap (Pocock design point)
  const finT = 0.845;
  const finX = finT * L;
  const finZ = keelZ(finT);
  const foil = new THREE.Shape();
  foil.moveTo(0, 0);
  foil.lineTo(0.215, 0);
  foil.lineTo(0.245, -0.118);
  foil.quadraticCurveTo(0.150, -0.140, 0.040, -0.128);
  foil.closePath();
  const fin = new THREE.ExtrudeGeometry(foil, {
    depth: 0.0065, bevelEnabled: true, bevelThickness: 0.0018,
    bevelSize: 0.0022, bevelSegments: 2, curveSegments: 10,
  });
  fin.rotateY(Math.PI / 2);
  fin.translate(finX, finZ - 0.004, 0.0033);
  geos.push(fin);

  // Rudder blade immediately aft, closing the gap
  const rud = new THREE.Shape();
  rud.moveTo(0, 0);
  rud.lineTo(0.098, 0);
  rud.quadraticCurveTo(0.112, -0.055, 0.086, -0.104);
  rud.lineTo(0.014, -0.096);
  rud.closePath();
  const rg = new THREE.ExtrudeGeometry(rud, {
    depth: 0.0055, bevelEnabled: true, bevelThickness: 0.0015,
    bevelSize: 0.0018, bevelSegments: 2, curveSegments: 8,
  });
  rg.rotateY(Math.PI / 2);
  rg.translate(finX + 0.246, finZ - 0.006, 0.0028);
  geos.push(rg);

  // Bow number clip on the foredeck
  geos.push(box(0.012, 0.070, 0.008, 0.040 * L, sheerZ(0.040) + 0.045, 0));

  return mergeGeos(geos);
}

/* ------------------------------------------------------------------ *
 * Sweep oars — hatchet blades, correct handedness per seat
 * ------------------------------------------------------------------ */
export function buildOars({ angleDeg = 32, squared = true } = {}) {
  const geos = [];
  const L = SPEC.loa;
  const ang = THREE.MathUtils.degToRad(angleDeg);

  SPEC.seatStations.forEach((t, i) => {
    const side = rigSide(i);
    const x = t * L + 0.055;
    const pinY = pinZ(t);
    const pinSide = side * SPEC.spread;

    // outboard direction, swept toward the bow (rowers pull toward the stern)
    const dir = new THREE.Vector3(-Math.sin(ang), 0, side * Math.cos(ang)).normalize();
    const inboardLen = 0.88;
    const pin = V(x, pinY, pinSide);
    const inboard = pin.clone().addScaledVector(dir, -inboardLen);
    const tip = pin.clone().addScaledVector(dir, SPEC.oarLength - inboardLen - SPEC.bladeLength);

    // shaft, tapering outboard
    const mid = inboard.clone().lerp(tip, 0.5);
    geos.push(tube(inboard, mid, 0.0230, 12));
    geos.push(tube(mid, tip, 0.0186, 12));

    // handle
    const hEnd = inboard.clone().addScaledVector(dir, -0.31);
    geos.push(tube(inboard, hEnd, 0.0188, 12));
    // handle end cap
    const cap = new THREE.SphereGeometry(0.0192, 10, 8);
    cap.translate(hEnd.x, hEnd.y, hEnd.z);
    geos.push(cap);

    // collar + button at the pin
    const collar = new THREE.CylinderGeometry(0.0295, 0.0295, 0.055, 14);
    const q = new THREE.Quaternion().setFromUnitVectors(V(0, 1, 0), dir);
    collar.applyQuaternion(q);
    collar.translate(pin.x, pin.y, pin.z);
    geos.push(collar);
    const button = new THREE.CylinderGeometry(0.0345, 0.0345, 0.013, 14);
    button.applyQuaternion(q);
    const bp = pin.clone().addScaledVector(dir, -0.030);
    button.translate(bp.x, bp.y, bp.z);
    geos.push(button);

    geos.push(hatchetBlade(tip, dir, side, squared));
  });

  return mergeGeos(geos);
}

/**
 * Asymmetric cleaver ("hatchet") blade.
 *
 * Built in the blade's own 2D frame and then oriented, which is much easier to
 * reason about than rotating an extrusion three times:
 *   local +x  = outboard, along the shaft
 *   local +y  = across the blade (tip-ward edge positive)
 *   local +z  = the face normal
 *
 * A real hatchet is NOT symmetric about the shaft: it carries more area on the
 * tip side, has a squared-off outboard end, and the face is dished. The earlier
 * version extruded a flat outline and read as a dark rectangle.
 */
function hatchetBlade(root, dir, side, squared) {
  const bl = SPEC.bladeLength, bw = SPEC.bladeWidth;

  const shape = new THREE.Shape();
  // neck at the shaft
  shape.moveTo(0, -0.026);
  // lower (bow-side) edge sweeping out
  shape.bezierCurveTo(bl * 0.18, -bw * 0.30, bl * 0.34, -bw * 0.44, bl * 0.60, -bw * 0.46);
  shape.lineTo(bl * 0.93, -bw * 0.42);
  // squared outboard end with rounded corners
  shape.quadraticCurveTo(bl, -bw * 0.40, bl, -bw * 0.30);
  shape.lineTo(bl, bw * 0.34);
  shape.quadraticCurveTo(bl, bw * 0.46, bl * 0.92, bw * 0.48);
  // upper edge, carrying more area (the "hatchet" side)
  shape.lineTo(bl * 0.54, bw * 0.50);
  shape.bezierCurveTo(bl * 0.30, bw * 0.50, bl * 0.14, bw * 0.34, 0, 0.026);
  shape.closePath();

  const g = new THREE.ExtrudeGeometry(shape, {
    depth: 0.0075,
    bevelEnabled: true,
    bevelThickness: 0.0030,
    bevelSize: 0.0042,
    bevelSegments: 3,
    curveSegments: 26,
  });
  g.center();
  // recentre so the neck sits at the origin rather than the bounding-box middle
  g.computeBoundingBox();
  const bb = g.boundingBox;
  g.translate(-bb.min.x, 0, 0);

  // Dish the face: a real blade is spooned, deepest near the middle.
  const p = g.attributes.position;
  for (let i = 0; i < p.count; i++) {
    const bx = p.getX(i), by = p.getY(i);
    const u = THREE.MathUtils.clamp(bx / bl, 0, 1);
    const v = THREE.MathUtils.clamp(Math.abs(by) / (bw * 0.5), 0, 1);
    const dish = 0.020 * Math.sin(Math.PI * Math.pow(u, 0.85)) * (1 - v * v * 0.6);
    p.setZ(i, p.getZ(i) - dish);
  }
  g.computeVertexNormals();

  // Orient: local +x along the oar, face square to the water when `squared`.
  if (squared) g.rotateX(Math.PI / 2);
  // blades on opposite sides mirror
  if (side < 0) g.rotateX(Math.PI);
  g.applyQuaternion(new THREE.Quaternion().setFromUnitVectors(V(1, 0, 0), dir));
  g.translate(root.x, root.y, root.z);
  return g;
}

/* ------------------------------------------------------------------ *
 * Coxswain fittings in the bow compartment
 * ------------------------------------------------------------------ */
export function buildCoxFittings() {
  const geos = [];
  const L = SPEC.loa;
  const t = SPEC.coxStation;
  const x = t * L;
  const z = keelZ(t);

  // headrest pad at the forward end
  geos.push(box(0.090, 0.030, 0.170, x - 0.30, z + 0.075, 0));
  // back pad
  geos.push(box(0.420, 0.026, 0.190, x + 0.10, z + 0.052, 0));
  // steering toggle on a short post
  const post = new THREE.CylinderGeometry(0.006, 0.006, 0.070, 8);
  post.translate(x + 0.16, z + 0.090, 0.085);
  geos.push(post);
  geos.push(box(0.055, 0.014, 0.020, x + 0.16, z + 0.128, 0.085));

  return mergeGeos(geos);
}
