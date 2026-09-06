/**
 * Rigging, seats, oars and hardware for the Pocock Comp 4+.
 *
 * Everything is generated from SPEC so the whole assembly stays consistent when
 * a dimension changes. A racing shell reads as real mostly because of this
 * hardware: the rigger triangulation, the alternating port/starboard pattern,
 * the tracks, the shoes raked back, the hatchet blades. Get those wrong and no
 * amount of shading saves it.
 */

import * as THREE from 'three';
import { SPEC, sheerZ, keelZ, halfBeam, tube, V, seatTopZ } from './pocock.js';

const merge = (geos) => {
  // Minimal geometry merge — avoids pulling in BufferGeometryUtils.
  const out = new THREE.BufferGeometry();
  let vCount = 0, iCount = 0;
  for (const g of geos) {
    vCount += g.attributes.position.count;
    iCount += g.index ? g.index.count : 0;
  }
  const pos = new Float32Array(vCount * 3);
  const nrm = new Float32Array(vCount * 3);
  const idx = new Uint32Array(iCount);
  let vo = 0, io = 0;
  for (const g of geos) {
    if (!g.attributes.normal) g.computeVertexNormals();
    pos.set(g.attributes.position.array, vo * 3);
    nrm.set(g.attributes.normal.array, vo * 3);
    if (g.index) {
      const gi = g.index.array;
      for (let i = 0; i < gi.length; i++) idx[io + i] = gi[i] + vo;
      io += gi.length;
    }
    vo += g.attributes.position.count;
  }
  out.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  out.setAttribute('normal', new THREE.BufferAttribute(nrm, 3));
  out.setIndex(new THREE.BufferAttribute(idx, 1));
  return out;
};

const box = (w, h, d, x, y, z, rot) => {
  const g = new THREE.BoxGeometry(w, h, d);
  if (rot) g.rotateZ(rot);
  g.translate(x, y, z);
  return g;
};

/* ------------------------------------------------------------------ *
 * Riggers — tubular aluminium, the classic Pocock arrangement.
 * Three struts triangulating out to the pin: two from the gunwale at
 * different stations, one lower brace. This is what makes it look real.
 * ------------------------------------------------------------------ */
export function buildRiggers() {
  const geos = [];
  const L = SPEC.loa;
  const r1 = 0.0115;  // main tube radius
  const r2 = 0.0085;  // brace radius

  SPEC.seatStations.forEach((t, i) => {
    const port = SPEC.rigPortSide[i];
    const side = port ? 1 : -1;
    const x = t * L;
    const zs = sheerZ(t);
    const B = halfBeam(t);

    // Pin position: outboard at `spread`, slightly aft of the seat, raised.
    const pin = V(x + 0.045, zs + SPEC.oarlockHeight, side * SPEC.spread);

    // Three mounting feet on the gunwale
    const fwd = V(x - 0.30, zs + 0.006, side * (B - 0.012));
    const aft = V(x + 0.34, zs + 0.006, side * (B - 0.012));
    const low = V(x + 0.02, zs - 0.075, side * (B - 0.020));

    geos.push(tube(fwd, pin, r1, 10));
    geos.push(tube(aft, pin, r1, 10));
    geos.push(tube(low, pin, r2, 8));
    // cross brace between the two upper arms for stiffness
    const midF = fwd.clone().lerp(pin, 0.55);
    const midA = aft.clone().lerp(pin, 0.55);
    geos.push(tube(midF, midA, 0.006, 8));

    // Mounting plates at the gunwale
    for (const f of [fwd, aft]) {
      geos.push(box(0.075, 0.016, 0.030, f.x, f.y, f.z));
    }

    /* --- oarlock / swivel --- */
    // vertical pin
    const pinTop = pin.clone().add(V(0, 0.062, 0));
    const pinBot = pin.clone().add(V(0, -0.028, 0));
    geos.push(tube(pinBot, pinTop, 0.0075, 10));

    // the swivel body: a U that closes around the oar sleeve
    const swivelY = pin.y + 0.020;
    const sw = new THREE.TorusGeometry(0.030, 0.0075, 8, 18, Math.PI * 1.35);
    sw.rotateX(Math.PI / 2);
    sw.rotateY(side > 0 ? -0.35 : Math.PI + 0.35);
    sw.translate(pin.x, swivelY, pin.z);
    geos.push(sw);

    // the gate bar across the top
    geos.push(box(0.010, 0.048, 0.010, pin.x, swivelY + 0.030, pin.z + side * 0.026));
  });

  return merge(geos);
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
    const zt = keelZ(t) + 0.075;      // track height off the keel
    const len = SPEC.slideLength;

    // Two tracks, running fore-aft
    for (const s of [1, -1]) {
      const g = new THREE.BoxGeometry(len, 0.012, 0.020);
      g.translate(x - 0.06, zt, s * half);
      geos.push(g);
      // track feet
      for (const dx of [-len / 2 + 0.05, 0, len / 2 - 0.05]) {
        geos.push(box(0.030, 0.028, 0.016, x - 0.06 + dx, zt - 0.020, s * half));
      }
    }

    // Seat: shaped pad sitting on four wheels, parked at roughly half slide
    const sx = x - 0.02;
    const sy = seatTopZ(t);
    const seat = new THREE.BoxGeometry(0.290, 0.022, 0.245);
    seat.translate(sx, sy, 0);
    geos.push(seat);
    // contoured underside blocks
    geos.push(box(0.230, 0.030, 0.180, sx, sy - 0.024, 0));
    // wheels
    for (const dx of [-0.10, 0.10]) {
      for (const s of [1, -1]) {
        const w = new THREE.CylinderGeometry(0.017, 0.017, 0.014, 10);
        w.rotateX(Math.PI / 2);
        w.translate(sx + dx, zt + 0.017, s * half);
        geos.push(w);
      }
    }

    /* --- foot stretcher --- */
    // Plate raked back ~40 degrees, positioned toward the stern of the seat.
    const fx = x + 0.62;
    const fzBase = keelZ(t) + 0.055;
    const rake = THREE.MathUtils.degToRad(41);

    const plate = new THREE.BoxGeometry(0.026, 0.300, 0.300);
    plate.rotateZ(rake);
    plate.translate(fx, fzBase + 0.115, 0);
    geos.push(plate);

    // Two shoes, heels down, splayed slightly
    for (const s of [1, -1]) {
      const shoe = new THREE.BoxGeometry(0.075, 0.230, 0.098);
      shoe.rotateZ(rake);
      shoe.rotateY(s * 0.06);
      shoe.translate(fx - 0.028, fzBase + 0.120, s * 0.082);
      geos.push(shoe);
      // heel cup
      const heel = new THREE.BoxGeometry(0.055, 0.055, 0.092);
      heel.translate(fx + 0.055, fzBase + 0.030, s * 0.082);
      geos.push(heel);
    }

    // stretcher mounting rails
    for (const s of [1, -1]) {
      geos.push(box(0.320, 0.014, 0.016, fx - 0.06, fzBase + 0.005, s * 0.115));
    }
  });

  return merge(geos);
}

/* ------------------------------------------------------------------ *
 * Structural detail: ribs, knees, and the shoulder where deck meets hull
 * ------------------------------------------------------------------ */
export function buildStructure() {
  const geos = [];
  const L = SPEC.loa;
  // Ribs visible inside the cockpit
  for (let i = 0; i < 14; i++) {
    const t = SPEC.cockpitStart + (SPEC.cockpitEnd - SPEC.cockpitStart) * (i / 13);
    const x = t * L;
    const z = keelZ(t) + 0.045;
    const w = 0.30;
    geos.push(box(0.014, 0.050, w, x, z, 0));
  }
  return merge(geos);
}

/* ------------------------------------------------------------------ *
 * Bow ball, rudder, skeg, bow number holder
 * ------------------------------------------------------------------ */
export function buildFittings() {
  const geos = [];
  const L = SPEC.loa;

  // Bow ball — mandatory safety fitting, 4 cm
  const ball = new THREE.SphereGeometry(SPEC.bowBallDia / 2, 18, 14);
  ball.translate(-0.012, sheerZ(0) - 0.052, 0);
  geos.push(ball);

  // Skeg / fin under the hull aft
  const fin = new THREE.BoxGeometry(0.170, 0.105, 0.006);
  fin.translate(0.855 * L, keelZ(0.855) - 0.052, 0);
  geos.push(fin);

  // Rudder behind the fin
  const rud = new THREE.BoxGeometry(0.085, 0.090, 0.005);
  rud.translate(0.905 * L, keelZ(0.905) - 0.046, 0);
  geos.push(rud);

  return merge(geos);
}

/* ------------------------------------------------------------------ *
 * Sweep oars — hatchet blades, correct handedness per seat.
 * Built lying in the water at the catch-ish angle so the boat reads as rigged.
 * ------------------------------------------------------------------ */
export function buildOars({ angleDeg = 34, feather = false } = {}) {
  const geos = [];
  const L = SPEC.loa;
  const ang = THREE.MathUtils.degToRad(angleDeg);

  SPEC.seatStations.forEach((t, i) => {
    const port = SPEC.rigPortSide[i];
    const side = port ? 1 : -1;
    const x = t * L + 0.045;
    const zs = sheerZ(t);
    const pinY = zs + SPEC.oarlockHeight;
    const pinZ = side * SPEC.spread;

    // Direction from pin outboard, swept aft by `ang`
    const dir = new THREE.Vector3(-Math.sin(ang), 0, side * Math.cos(ang)).normalize();
    const inboard = new THREE.Vector3(x, pinY, pinZ).addScaledVector(dir, -0.86);
    const outEnd = new THREE.Vector3(x, pinY, pinZ)
      .addScaledVector(dir, SPEC.oarLength - 0.86 - SPEC.bladeLength);

    // Shaft, slightly tapered — two segments reads better than one
    const mid = inboard.clone().lerp(outEnd, 0.55);
    geos.push(tube(inboard, mid, 0.0225, 10));
    geos.push(tube(mid, outEnd, 0.0185, 10));

    // Handle
    const hEnd = inboard.clone().addScaledVector(dir, -0.30);
    geos.push(tube(inboard, hEnd, 0.0185, 10));

    // Collar / button at the pin
    const btn = new THREE.CylinderGeometry(0.032, 0.032, 0.030, 12);
    const q = new THREE.Quaternion().setFromUnitVectors(V(0, 1, 0), dir);
    btn.applyQuaternion(q);
    btn.translate(x, pinY, pinZ);
    geos.push(btn);

    /* --- hatchet blade --- */
    // Asymmetric cleaver: wider at the tip-side, scooped.
    const bl = SPEC.bladeLength, bw = SPEC.bladeWidth;
    const shape = new THREE.Shape();
    shape.moveTo(0, -0.030);
    shape.quadraticCurveTo(bl * 0.28, -bw * 0.52, bl * 0.72, -bw * 0.50);
    shape.lineTo(bl, -bw * 0.34);
    shape.quadraticCurveTo(bl * 1.02, 0, bl, bw * 0.30);
    shape.lineTo(bl * 0.70, bw * 0.44);
    shape.quadraticCurveTo(bl * 0.26, bw * 0.42, 0, 0.030);
    shape.closePath();

    const blade = new THREE.ExtrudeGeometry(shape, {
      depth: 0.010, bevelEnabled: true, bevelThickness: 0.004,
      bevelSize: 0.004, bevelSegments: 2, curveSegments: 16,
    });
    // orient: lay flat, then rotate to sit on the shaft axis
    blade.rotateY(Math.PI / 2);
    const bq = new THREE.Quaternion().setFromUnitVectors(V(1, 0, 0), dir);
    blade.applyQuaternion(bq);
    if (!feather) {
      // squared blade: rotate about the shaft so the face is vertical
      const rq = new THREE.Quaternion().setFromAxisAngle(dir, side * Math.PI * 0.5);
      blade.applyQuaternion(rq);
    }
    blade.translate(outEnd.x, outEnd.y, outEnd.z);
    geos.push(blade);
  });

  return merge(geos);
}
