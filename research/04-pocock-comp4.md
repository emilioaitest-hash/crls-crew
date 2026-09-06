# Pocock Hypercarbon Comp K4+ — Technical Reference for 3D Modeling

**Subject:** Pocock Racing Shells "Hypercarbon Comp K4+" coxed four (4+) sweep racing shell
**Purpose:** Dimensionally accurate reference for a photorealistic 3D model
**Compiled:** 2026-09-05

---

## 0. READ THIS FIRST — Two Critical Corrections to the Brief

The task brief contained two assumptions that the research contradicts. Both materially change the model:

**1. The product is called the "Hypercarbon Comp K4+", not the "Comp 4+".**
Pocock names its fours **K4**, not "4". The Competition tier is *"Hypercarbon Comp"*, and only two hulls exist in it: the **Comp V8** (eight) and the **Comp K4+** (coxed four).[1][5] There is no separate "Comp 4+" product page. Pocock's four/quad family is: Hypercarbon Comp K4+, Hypercarbon K4+, Hypercarbon K4-/x, and Core K4+/-/x.[5]

**2. The Comp K4+ is a BOW-LOADER (bow-coxed), not stern-coxed.**
Confirmed visually from Pocock's own overhead product photography (see §3.1). The coxswain lies semi-supine in a compartment immediately aft of the bow ball. This is the single biggest shape decision in the model — a stern-coxed four looks completely different. Details and evidence in §3.

**3. Length:** the brief's "~13.4 m / 44 ft" refers to *overall* length. Pocock publishes **waterline** length, which for the Comp K4+ is 12.50–12.93 m (41'–42'5").[1] LOA is longer. See §1.2 and §2.1.

---

## 1. THE COMPANY AND THE PRODUCT

### 1.1 Pocock Racing Shells — History

Founded Seattle, Washington, **1911**, by George Pocock; the oldest rowing shell manufacturer in the world.[6][7] George's father was head boat builder for Eton College at Windsor; George raced singles on the Thames, won £50, and used the money to buy passage with his brother Dick on a cattle boat to Canada, arriving in Vancouver BC on his 20th birthday in 1911 with $20.[6]

Timeline relevant to the brand's visual identity:

| Era | Event |
|---|---|
| 1912 | Hiram Conibear, UW crew coach, brings the brothers to Seattle. Shop in the "Tokyo Tea Room" until 1916.[6] |
| 1916–1922 | Pococks build floatplane pontoons for William E. Boeing; George becomes Boeing assembly foreman.[6] |
| 1923 | Unknown University of Washington crew wins the national championship in a Pocock boat; demand explodes.[6][7] |
| 1923–1976 | George builds shells for nearly every racing college in the US. Western red cedar becomes the signature material — "impervious to rot and light in weight."[12] |
| 1936 | The UW crew wins gold at the Berlin Olympics in the Pocock-built *Husky Clipper* — the "Boys in the Boat" story. |
| 1952–1964 | Every US crew in all seven boat classes at four consecutive Olympics races in Pocock shells.[12] |
| 1956 | Stan Pocock experiments with fiberglass while his father is at the Melbourne Olympics; replaces wooden ribs with a fiberglass sandwich skin.[6] |
| 1961 | Stan builds the first fiberglass rowing boat ever (a wherry).[6] |
| 1966 | Last year every shell and oar at the IRA regatta is Pocock-built.[12] |
| 1981 | Stan develops the first all-carbon-fiber **monocoque** racing shells — the shoulderless boat, his "crowning achievement."[6] |
| 1985–2018 | Bill Tytus leads the company; designs the Hypercarbon K4 and V8.[6] |
| 1998 | "Hypercarbon" proprietary laminate schedule introduced.[7] |
| 2013 | **Hypercarbon Comp** released (V8 first), enabled by the G6 wing rigger's weight savings.[1] |
| 2016 | xVIII released — first Pocock hull designed from pure conic sections.[5][6] |
| 2017 | **G7 wing rigger debuts; Comp K4+ released** with the proven K4+ hull, new layup, updated decks and coxswain station.[1] |
| Today | Everett, Washington shop. ~6 weeks build time per boat in normal production.[4][7] |

> **Modeling note — historical accuracy trap:** The cedar, varnished-wood Pocock of *The Boys in the Boat* (1936) is a **completely different-looking object** from a modern Comp K4+. If the website's aesthetic references the 1936 story, do not let that bleed into the geometry. The modern boat is a glossy white painted composite monocoque with black exposed-carbon decks and black wing riggers.

### 1.2 The Competition ("Comp") Series

The Hypercarbon Comp is the top of Pocock's *layup* hierarchy for existing hull shapes. Pocock's own product-line summary:[5]

| Tier | Description |
|---|---|
| **xVIII** | Newest hull design and layup (Spring 2016). Conic-section hull. Most serious programs. |
| **Hypercarbon Comp** | "The development of our 7th Generation wing rigger has allowed for even MORE carbon to be strategically placed into the Hypercarbon Comp layup. V8 and K4+ available now."[5] |
| **Hypercarbon** | Elite racing shell. All-carbon construction with foam core. |
| **Core** | Durable carbon/fiberglass with foam or syntactic resin core. Club/novice workhorse. |
| **Legacy** | Race-capable teaching and training boat. |

The Comp K4+ marketing copy in full: *"The Hypercarbon Comp K4+ follows in the footsteps of the Comp V8. The PROVEN K4+ hull shape gets our 7th generation rigger, a layup with improved stiffness-to-weight, and updated decks/coxswain station."*[1]

**Key insight for the modeler:** the Comp K4+ shares its **hull mold** with the Hypercarbon K4+ ("the PROVEN K4+ hull shape").[1] What differs is the laminate, the G7 rigger, the deck treatment, and the coxswain station. This means Hypercarbon K4+ photography is valid hull reference; only rigger and deck details differ.

### 1.3 Options and Customization (verified)[1]

- **Riggers:** G7 wing rigger — "our most updated and easily adjustable **stern mounted carbon wing**." Padded rigger bags available.
- **Footboards:** Fully adjustable, unbreakable carbon fiber, with Rowing Shoes or Racing Sandals.
- **Seats:** "Super light, super durable **single carriage carbon** with sealed bearing wheels."
- **Customization:** **Vinyl striping in 10 colors and 4 styles.** (This is the *only* color customization — the hull itself is always white. See §6.1.)
- Footgear also accommodates Nike Omadas, the Shimano SRD system, and BatLogic.[4]

---

## 2. DIMENSIONS TABLE

### 2.1 VERIFIED SPECS — Pocock published, Hypercarbon Comp K4+[1]

| Hull size | Crew weight (lb) | Crew weight (kg) | Waterline length | WL length (m) | Avg. fully rigged wt (lb) | (kg) |
|---|---|---|---|---|---|---|
| **Small** | 125–165 | 57–75 | 41' 0" | **12.50** | 106 | 48.1 |
| **Medium** | 160–195 | 73–88 | 41' 6" | **12.65** | 110 | 49.9 |
| **Large** | 190–230 | 86–104 | 42' 5" | **12.93** | 112 | 50.8 |

> *Source note:* one cached search snippet for this URL returned a six-row table identical to the Hypercarbon K4+ page. The live page extraction returns the three-row table above. I use the three-row table as authoritative for the Comp; the six-row table belongs to the standard Hypercarbon K4+.[1][2]

**Waterline beam** is not published on the Comp or Hypercarbon K4+ pages. It *is* published for the Core K4+, which is a different layup but the same class of hull, and is the best available proxy:[3]

| Hull size | Core K4+ waterline beam | (cm) | Core K4+ waterline length | (m) |
|---|---|---|---|---|
| Small | 16.37 in | **41.6** | 41.75 ft | 12.73 |
| Medium | 17.40 in | **44.2** | 42.125 ft | 12.84 |
| Large | 17.57 in | **44.6** | 43.00 ft | 13.11 |

### 2.2 Comparison — Hypercarbon K4+ (same hull, standard layup)[2]

| Hull size | Crew weight (lb) | Waterline length | Rigged wt (lb) |
|---|---|---|---|
| Small (lwt.) | 115–145 | 40' 10" | 106 |
| Small | 140–165 | 41' 0" | 106 |
| Medium (lwt.) | 150–170 | 41' 3" | 110 |
| Medium | 160–180 | 41' 6" | 110 |
| Large | 175–200 | 42' 5" | 112 |
| XL | 190–225 | 42' 8" | 112 |

### 2.3 VERIFIED — Regulatory (World Rowing / FISA)[19]

| Parameter | Value |
|---|---|
| **4+ minimum weight** | **51 kg** (51.7 kg w/ wireless system, 52.2 kg w/ wired) |
| Minimum boat length, all classes | 7.20 m |
| **Bow ball** | Solid ball, **min. Ø 4 cm**, bright white, covering the point of the bow |
| **Coxswain seat opening** | **≥ 70 cm long**, and as wide as the boat for **≥ 50 cm**. Inner surface smooth; no structure may restrict inner width |
| Rudders | Only one rudder allowed |
| Fins | Any number, but must be fixed and vertical on the hull |
| Sweep oar blade thickness | ≥ 5 mm, measured 3 mm from the outer edge |
| Production plaque | Permanently affixed inside the boat, up to 50 cm², listing builder name/address, logo, year, design crew weight, and weight at construction |
| Weight includes | Riggers, stretchers, shoes, slides, seats, hull extensions, speakers + wiring, attached seat pads |
| Weight excludes | Oars, bow number |

> **Weight paradox worth understanding:** the Comp K4+ Small at 106 lb = **48.1 kg** is *below* the 51 kg FISA minimum. This is intentional and confirmed by Pocock's own FAQ: *"The boats are at weight with the Aluminum Wing, and underweight with Carbon."*[4] Crews racing internationally tape ballast to the hull to make weight. For the model this means nothing visually except that a race-day boat may carry small lead weights taped inside the hull.

### 2.4 TYPICAL VALUES — inferred, for a coxed four (label as inference)

| Parameter | Value | Basis |
|---|---|---|
| **Length overall (LOA)** | **13.4–13.8 m** (44–45 ft) | INFERRED. WL length 12.50–12.93 m[1] ÷ 0.92–0.94 typical WL:LOA ratio for a fine-ended shell. Cross-checks against the widely cited "4+ ≈ 44 ft / 13.4 m"[20] and NSW Rowing's 13.7 m.[19-adj] Use **13.6 m** for a medium hull. |
| **Maximum beam (at saxboard/gunwale)** | **50–57 cm** | INFERRED from WL beam 41.6–44.6 cm[3] plus typical flare. Published figures for 4+ class run 55–60 cm. Use **~55 cm** at the widest station. |
| **Maximum draft (loaded)** | **17–20 cm** | INFERRED. Scaled from the Vespoli 8+ patent: 0.563–0.629 ft = 17.2–19.2 cm for an eight.[16] A four sits similarly deep — displacement per unit length is comparable. |
| **Freeboard amidships (loaded)** | **12–18 cm** | INFERRED. A 1990s rec.sport.rowing post on the then-new Pocock bow-loaded four notes *"Gunwales are a bit lower than in other fours (1 in)"*[26] — Pocock runs low freeboard. |
| **Freeboard at bow deck peak** | **28–35 cm** | INFERRED. Must clear the coxswain's head/shoulders. |
| **Hull skin thickness** | **1.5–3 mm** total sandwich | INFERRED from monocoque foam-core carbon construction.[4] |
| **Length:beam ratio** | **~25:1** | Derived: 13.6 m / 0.55 m. Racing shells run up to 30:1.[16] |
| **Displacement, medium crew** | **~430–470 kg** | Derived: 4 × 82 kg rowers + 55 kg cox + 50 kg boat + ~14 kg oars. |

---

## 3. HULL GEOMETRY

### 3.1 Coxswain Configuration — BOW-LOADER (VERIFIED)

**The Pocock Comp K4+ is bow-coxed.** Verified by direct visual inspection of Pocock's own overhead plan-view product photography at high zoom:

- `HypercarbonK4_CarbonWingRiggers_LARGE.jpg` — 8192 × 1280 px overhead plan view
- `hypercarbon-comp-k4plus-zoom.jpg` — 8192 × 1280 px overhead plan view

In both images, at one end of the hull there is a **white bow ball** on a fine needle point, and **immediately inboard of it** an enclosed compartment with a rounded coaming opening — the coxswain's station — followed by the four rower stations. The opposite end tapers to a fine point with no compartment. The coxswain compartment is *forward of* all four rowers.

This is corroborated by:
- The FHC Crew glossary: *"Bowloader: Refers to a type of boat (usually a four) where the coxswain rides lying down beneath the bow decking. **Most racing fours are bowloaders.**"*[28]
- Vespoli sells a dedicated *"Push-Pull Steering Cable — Bow Coxed Fours"* part, confirming this is the standard four configuration across US builders.[27]
- A rec.sport.rowing thread specifically recommending *"POCOCK'S NEW BOW-LOADED FOUR ... Carbon-fiber wing rigger design, bow-loaded, light, responsive and tight."*[26]
- Pocock's parts list includes a **"Bowcox tiller"** as a distinct steering part.[15]

**Both configurations, for completeness:**

| | Bow-coxed (bowloader) — *what the Comp K4+ is* | Stern-coxed |
|---|---|---|
| Cox posture | Semi-supine, reclined, head just above the bow deck[13] | Seated upright, facing the crew |
| Position | Forward of bow seat, aft of the bow ball | Aft of stroke seat, at the stern |
| CoG | Lower — the cox's mass sits near/below the waterline; boat is easier to set[13] | Higher |
| Sight line | Eyes nearly level with the deck; excellent course view, cannot see the crew | Sees the whole crew, blocked forward view |
| Steering | Push-pull rod or cable to the stern rudder[27] | Rudder lines / toggles at each hand |
| Visual signature | Smooth continuous bow deck with a single oval opening near the bow; **no** stern seat well | Open stern well with a visible seat and backrest |

> **Modeling consequence:** the stern of a Comp K4+ is a *clean, closed, tapering deck* running from stroke seat to a fine point. Do not model a stern cockpit. The only stern features are the deck seam, the fin, and the rudder.

### 3.2 Overall Form

The hull is a **displacement monocoque** — a single continuous stressed skin from bow to stern with no internal ribs or shoulders.[4] Pocock is explicit: *"With true monocoque construction, there are no fragile, highly loaded shoulders and ribs. Since there are no joints to break down, the shell will not lose stiffness over time. Every Pocock hull is a monocoque hull."*[4]

Pocock's stiffness testing confirms a **full-length pan** running the length of the cockpit — a design Pocock developed and Resolute and Vespoli's M2 subsequently adopted — as the primary structural stiffening element.[8] This is a visible feature: the cockpit floor is a continuous molded trough, not a series of bulkheaded wells.

Overall profile in side view:

```
        BOW (cox end)                                                       STERN
         |                                                                     |
    ()===\__                                                                   |
   bow    \  ___cox opening___                                              ___/
   ball    \/                 \____  ____  ____  ____  ____  ____  ____  ___/
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            <-- deck: high at cox, falls to a long low gunwale run -->
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~ WATERLINE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             \______________________________________________________/  |
                    keel line: very shallow rocker                    fin+rudder
```

### 3.3 Cross-Sections (Body Plan)

Modern racing shells use a **semi-circular to shallow-U section**. Two independent characterizations:

- Wikipedia/Racing shell: *"The boat's long length and **semicircular cross-section** reduce drag to a minimum."*[32]
- Atkinsopht's hydrodynamic model, used for shell resistance calculation, explicitly assumes *"a **semi-circular hull cross section centered in the saxboard plane**"* when deriving wetted beam, draft and wetted surface area.[17]
- Row HQ describes the underwater form as a **"wineglass cross-section"**, knife-thin at bow ball and stern.[20]
- Naval-architecture commentary on shells: *"Most modern shells utilize a 'U-shape' or slightly flattened semi-circle to provide enough 'reserve stability' for the rowers to apply maximum power without the boat rolling excessively."*

**Section progression bow → stern (INFERRED, consistent with the above and with the plan-view photography):**

```
 St.0 bow      St.1          St.2-3         St.5 midship      St.7-8         St.10 stern
  (point)    fine V         deepening U      semi-circle      U flattening    (point)

    |            /\             \  /            \    /          \      /          |
    |           /  \             \/              \__/            \____/           |
    ▲          ▼               ▼                ▼                ▼               ▲
  knife      sharp V        rounded V       semicircular      shallow U       knife
   edge      deadrise        bilge          max beam+draft    flattened        edge
```

- **Stations 0–1 (bow / cox compartment):** Very fine, near-knife entry. Section is a deep narrow V. Above the waterline the topsides flare outward and upward substantially to create the volume the coxswain lies inside, so the *deck* is wide here while the *underwater* section is still very fine. This flare is the most distinctive shape feature of a bowloader.
- **Stations 2–4:** V softens into a rounded-bilge U. Beam and draft build steadily.
- **Station 5 (midship, ~stroke/3-seat area):** Maximum beam and maximum draft. Section is essentially a **semi-circle** with the flat of the saxboard plane closing the top. This is where the modeler should place max beam ~55 cm and max draft ~18 cm.
- **Stations 6–8:** Section flattens slightly and beam reduces. The bilge radius grows — a shallow U.
- **Stations 9–10 (stern):** Rapid taper to a fine point, but the *exit is fuller than the entry* (see §3.4 for angles).

### 3.4 Published Offsets — the only real numbers available

No Pocock offsets table is public. However, **US Patent 5,474,008** (Vespoli USA, inventors Michael Vespoli, Bruce Nelson, Carl Scragg, 1994) publishes a complete sectional-area curve for a competitive eight in both lightweight and super-heavyweight form.[16] This is the closest thing to a published racing-shell lines table that exists, and the *shape of the curve* is directly transferable to a four — only the scale differs.

**Sectional areas below the waterline (ft²), super-heavyweight eight:**[16]

| Station | Area (ft²) | Normalized (A/Amax) |
|---|---|---|
| 0 (bow) | 0.000 | 0.000 |
| 0.5 | 0.078 | 0.085 |
| 1 | 0.215 | 0.235 |
| 2 | 0.520 | 0.570 |
| 3 | 0.753 | 0.825 |
| 4 | 0.879 | 0.963 |
| **5 (max)** | **0.913** | **1.000** |
| 6 | 0.880 | 0.964 |
| 7 | 0.758 | 0.830 |
| 8 | 0.531 | 0.582 |
| 9 | 0.236 | 0.258 |
| 9.5 | 0.092 | 0.101 |
| 10 (stern) | 0.000 | 0.000 |

Station spacing = 1/10 of waterline length. **The normalized column is the useful one** — apply it to a four by scaling to the four's own max section area.

Other verified parameters from the same patent:[16]

| Parameter | Lightweight 8+ | Super-heavyweight 8+ |
|---|---|---|
| Waterline length | ≥ 51.5 ft | 57.1–59.6 ft |
| **Entry angle (half-angle at bow)** | **3.4°–3.8°** | **3.6°–4.0°** |
| **Exit angle (half-angle at stern)** | **3.9°–4.9°** | **4.05°–4.95°** |
| Max draft | 0.563–0.578 ft (17.2–17.6 cm) | 0.614–0.629 ft (18.7–19.2 cm) |
| Max waterline beam | 1.74–1.77 ft (53.0–53.9 cm) | 1.89–1.92 ft (57.6–58.5 cm) |
| Wetted surface area | 92.7–93.2 ft² | — |
| Metacentric height | 0.235–0.288 ft | ≥ 0.251 ft |

> **Two things to take from this table.** First, **the exit angle is always larger than the entry angle** — roughly 4° in, 4.5° out. The bow is finer than the stern. Model the bow as the sharper, more needle-like end. Second, the sectional-area curve is very nearly symmetric fore-and-aft but peaks slightly forward of station 5 and carries more volume aft of station 6 than forward of station 4.

### 3.5 Rocker (Keel Line)

**INFERRED.** No published Pocock rocker figure exists. For a racing shell of this class:

- Total rocker is **very shallow — on the order of 3–6 cm** over the full length.
- The keel line is essentially **straight and flat for the middle ~60%** of the hull (roughly stations 2–8), which is what makes a shell fast and also what makes it directionally unstable enough to need a fin.
- Rocker rises smoothly in the last ~15% at each end, sweeping up to meet the stem and stern points.
- The bow rises to the bow ball; the stern rises to the stern point. Both rises are gentle curves, not knuckles.

### 3.6 Sheer Line

**Described from Pocock plan-view and profile photography (verified visually), with dimensions inferred:**

- From the bow ball, the deck rises steeply over ~1.0–1.5 m to a **peak over the coxswain compartment**. This is the highest point of the whole boat.
- Aft of the cox compartment, the sheer **drops to its lowest point** and then runs almost dead flat for the entire cockpit — the full length of all four rower stations. This long, low, straight gunwale run is the dominant visual line of the boat.
- Approaching the stern, the sheer rises very slightly and the deck closes over, tapering to the stern point.
- The gunwale (saxboard) is a narrow flat ledge — the rigger mounting surface. Pocock mounts its wings **to the top of the gunwales**, so this surface must be modeled flat and wide enough to take a bolted saddle.[14]

### 3.7 Bow and Stern Termination

**Bow:** an extremely fine, needle-like point. The last ~60 cm of the bow is essentially a thin blade of composite. The stem is near-vertical with slight rake. It terminates in the mandatory **white bow ball, Ø ≥ 4 cm**[19] — visually a small white sphere on the very tip, clearly visible in Pocock's plan-view photography. Just aft of the bow ball on the deck is the **bow number holder**, a small clip/bracket (Pocock lists a "Bowclip" as a stock part[15]) that takes a vertical rectangular bow number card during racing.

**Stern:** tapers to a fine point, marginally fuller than the bow per the exit-angle data (§3.4). The stern deck is closed and continuous. Underneath, near the stern, sit the **fin and rudder** (§4.8).

### 3.8 Waterline — Empty vs Crewed

**INFERRED but visually critical:**

- **Empty (on slings or racked):** the hull barely touches the water. Draft perhaps 4–6 cm. The boat floats absurdly high — a 50 kg hull displacing 50 kg of water spread over 13.6 m. Nearly the entire hull is visible; the waterline sits near the turn of the bilge.
- **Crewed (4 rowers + cox, ~450 kg total):** draft ~17–20 cm. Freeboard amidships drops to ~12–18 cm. **This is the state to model for an on-water render.** The waterline runs from the bow point, sweeps down and aft, runs nearly parallel to the gunwale through the cockpit, and sweeps back up to the stern point.
- The difference between the two is roughly **13–15 cm of draft** — enough that a render made at empty-boat waterline will look obviously wrong to a rower.
- At speed the boat also **squats slightly by the stern** and generates a small bow wave and a visible transom-less wake trailing from the stern point.

---

## 4. DECK, COCKPIT, RIGGING AND HARDWARE

### 4.1 Deck Layout

Running bow → stern:

1. **Bow ball** (white, Ø ≥ 4 cm) on the point.[19]
2. **Bow deck** — short, rising, with the bow number clip.[15]
3. **Coxswain compartment** — an oval/elongated opening in the deck, minimum 70 cm long and full-width for at least 50 cm.[19] Coaming lip around the opening. Padded headrest at the forward end. This is where the cox lies, head forward, looking over the bow deck.
4. **Bulkhead / deck closure** aft of the cox station.
5. **Main cockpit** — one long continuous opening containing all four rower stations. Pocock's full-length structural **pan** forms the floor.[8]
6. **Stern deck** — closed, tapering to the stern point.

**Exposed carbon:** The Comp's headline cosmetic feature is an **"exposed carbon fiber cockpit"** (stated for the Comp V8, and the Comp K4+ gets "updated decks/coxswain station" in the same idiom).[1] In the product photography the decks and cockpit interior are visibly **black woven carbon twill under clear coat**, against a white painted hull.

### 4.2 Riggers — G7 Carbon Wing (VERIFIED)

**Type: wing rigger, not tubular pin rigger.** Pocock has used wing riggers for decades; the "STANDARD OUTRIGGERS" (tubular aluminum/stainless side-mount) in the parts catalogue are legacy items for old boats.[15]

**Comp K4+ specifically:** *"Debuting in 2017, the **G7 wing rigger** is our most updated and easily adjustable **stern mounted carbon wing**."*[1]

Verified characteristics:

- **Material:** carbon fiber. (The standard Hypercarbon K4+ offers a choice of carbon or aircraft-grade T-6 aluminum wing at the same price; the Comp is specified with the carbon G7.[1][2][4])
- **Mounting: bolted across the top of the gunwales.** Pocock: *"by attaching to the top of the gunwales, [it] lessens the chance of contact with the water. Mounting riggers to the top of gunwales also distributes rowing loads more efficiently and requires less supporting structure than side-bolted riggers."*[14] Pocock's stiffness testing found its wing, *"bolted across the gunwales, is a structural stiffening element and exhibits by far the least flex of all boats"* tested.[8]
- **Geometry:** an aerodynamic, aerospace-inspired **airfoil section** spanning the boat, cranked/swept outboard and upward to carry the pin. *"Pocock's aerospace inspired design reduces air drag."*[14] Visually, in Pocock's overhead photography, each wing appears as a swept-back V or boomerang shape spanning the hull, with the oarlock at the outboard tip.
- **"Stern mounted"** means the wing spar sits on the stern side of the pin. (Contrast: the xVIII medium uses an "industry-first bow mounted carbon fiber sweep wing", where the pin cup mounts on the end and spreads force evenly across the rigger.[5][29])
- **Bowbrace:** each wing assembly includes a **bowbrace** — a diagonal stay running forward from the rigger to the gunwale, resisting the fore-aft twisting couple. The G7 Complete assembly contains: *"G7 Wing Rigger, 1/2" Pin (w/ hardware), Sill Pin (w/ hardware), 1/4" Clip On Spacers, C2 Oarlock, Bowbrace (Complete)."*[18] The bowbrace is itself made of a long tube, a short tube, locknuts (L/R) and a threaded adjuster.[23] Pocock's standard bowbrace tube fits *"K4+/K45+/K5+ all seats"*.[23]
- **Number of stays:** one wing spar (spanning gunwale to gunwale) plus **one bowbrace per side**. This is far fewer members than a traditional 3-stay tubular rigger — a key visual difference.
- **Sizing:** wings *"come in 3 separate heights"*, stamped **#2, #2.5, #3** on the bottom of the wing mount.[23]
- **Adjustment:** G5/G6 carbon wings use a *"fully adjustable, eccentric pin"* — turning the pin moves the pitch in and out, and *"the pitch leans away from the arrow that is marked on the pin nut."*[4] G7 uses a **slotted sill insert** with its own pin assembly; some G6 wings were retrofitted with the slotted sill to accept it.[23]
- **Care:** carbon wings are more fragile and more expensive to replace than aluminum; Pocock strongly recommends spare port and starboard wings on hand plus rigger bags.[4]

### 4.3 Rigger Spread (sweep four)

| Source | Value |
|---|---|
| **Pocock historical standard (wooden boats, pre-1965)** | **32 in = 81.3 cm**, identical for Pocock pairs and fours[12] — VERIFIED but historical |
| Modern sweep standard | **84–86 cm** pin-to-centerline[21] |
| Common working range across all sweep classes (2-, 4-, 4+, 8+), school to elite | **83–87 cm** |
| World Rowing rigging worked example | Spread = **84 cm**[11] |
| Australian practice | 86–88 cm |

**Recommendation for the model: 85 cm** from centerline to pin, per side. Label as TYPICAL — Pocock does not publish a modern spread figure, and it is a coach-adjustable setting anyway.

### 4.4 Oarlocks / Swivels (VERIFIED)

- The G7 assembly ships with a **Concept2 oarlock**.[18][23]
- Shape: a **U-shaped molded plastic block** (usually black) that the oar shaft sits inside, rotating around the pin. A hinged **gate** closes across the open top and screws down to keep the oar captive.[21]
- **Pin:** ½" diameter stainless steel, vertical, polished where the swivel rides.[18][23] (A 7/16" pin assembly also exists for some wings.[23])
- **Pitch bushings:** the G7 assembly includes **4/4 pitch bushings** — i.e. 4° at the catch face and 4° at the release face.[18][23] Pitch is set by swapping these plastic inserts rather than bending the pin.
- **Spacers:** ¼" clip-on spacers stack under the oarlock to set height.[18][23]
- **Oarlock height above the seat:** 16–18 cm typical for sweep[21]; Pocock's historical fixed standard was **6¼ in = 15.875 cm**.[12] Broader published range 16–19 cm for sweep.[11] **Use ~17 cm.** (TYPICAL)
- **Pitch:** ~4° is normal, set with the plastic inserts. Stern pitch 4–6°; lateral pitch held at 0–1°.[11][21] Overall pitch as the blade enters typically lands at 6–7° at the pin.

### 4.5 Seats and Tracks (VERIFIED)

- **Seat:** "Super light, super durable **single carriage carbon** with sealed bearing wheels."[1] Pocock also offers a **Croker seat top** option.[2] Contoured saddle shape with two raised buttock pockets and a central relief channel. A **seat horn** and **seat bungee cord** are stock parts.[15][23]
- **Wheels:** ball-bearing wheels on axles; four wheels on a single carriage.[1][15]
- **Tracks/slides:** Pocock's catalogue lists **"Tracks, 32" aluminum"** — **81.3 cm**.[15] Modern slides generally run 28–32 in (71–81 cm).[20] **Use 81 cm** for a Pocock. Track stops with rivets at each end; track wedges set the slide angle.[15][23]
- The tracks are bolted to the top of the **seat deck** / structural pan, one pair per rower station, running fore-and-aft parallel to the centerline.

> The brief suggested ~70 cm tracks. Pocock's own parts catalogue says 32 in / 81.3 cm.[15] Use 81 cm.

### 4.6 Foot Stretchers (VERIFIED + TYPICAL)

- **Comp K4+:** "Fully adjustable, **unbreakable carbon fiber footboards** with Rowing Shoes or Racing Sandals."[1]
- Construction: a pair of shoes bolted to a **shoe plate**, mounted on a **footboard**, which is adjustable fore-and-aft on a **notched channel track** with **T-bolts and wing nuts** and a **center pin handle**.[15]
- **Angle: 38–42° from horizontal** (TYPICAL). *"The general range is 38–42 degrees, with a shallower angle allowing the rower to have better compression and a steeper angle allowing you to drive with more..."*[22] Other sources give 39–42°. **Use 40°.**
- **Heel restraint:** a **heel cup** with **heel bracket**, plus **heel ties** — mandatory safety gear. World Rowing requires foot stretchers *"of a type which allows the rowers to get clear of the boat with no delay in an emergency."*[19] Model visible heel tie cords.
- Footgear options: Pocock Rowing Shoe (men's 8–15) or Rowing Sandal (Small = men's 7–10, Large = 11+); also accommodates Nike Omadas, Shimano SRD, BatLogic.[4]
- Pocock recommends carrying a **complete spare foot stretcher** to regattas.[4]

### 4.7 Rigger Alternation Pattern (sweep four)

Seats number **1 at the bow to 4 at the stern**. **Stroke is seat 4, nearest the stern**; bow is seat 1.[grokipedia/coxed four]

Standard rig for a coxed four — riggers alternate sides:

```
   BOW (cox lies here) ──────────────────────────────────────► STERN
        ┌───────┐
   (o)══╡  COX  ╞══[1]═══════[2]═══════[3]═══════[4]═══════▷  fin/rudder
        └───────┘   S         P         S         P
                    │         │         │         │
   STARBOARD side ──┘         │         │         │
   PORT side ─────────────────┘─────────┼─────────┘
                                        │
   Seat 1 (bow)    : STARBOARD rigger  (rower's oar to port... see note)
   Seat 2          : PORT rigger
   Seat 3          : STARBOARD rigger
   Seat 4 (stroke) : PORT rigger        ← stroke side
```

- Rowers are split evenly: **bow side (starboard) = seats 1 and 3; stroke side (port) = seats 2 and 4.**
- **Bow pair** = seats 1 and 2. **Stern pair** = seats 3 and 4.
- The convention "stroke side = port" holds when the stroke's oar is on port. This is the common US/UK default, and the pattern *alternates strictly* regardless. A "bow-rigged" or "Italian-rigged" boat swaps the pattern — but for a default render, use the alternating pattern above with stroke on port.
- **Critical modeling point:** because riggers alternate, the wings are *not* mirrored pairs at each station. Each station has **one** wing spanning the boat, with the oarlock on alternating sides. Viewed from above, the oarlocks zigzag: S, P, S, P from bow to stern.

### 4.8 Steering, Fin and Rudder (VERIFIED)

- **Fin (skeg):** a fixed vertical foil on the keel near the stern. Pocock: *"Our specially engineered **integrated fin and rudder system** minimizes unnecessary drag. The fin is molded to the **optimal foil shape**... Our system effectively **closes the area between the back of the fin and the front of the rudder** for uninterrupted flow. Bottom line, foil-shaped fins are faster than flat sheet metal fins."*[14] So model the fin and rudder as a **continuous foil assembly with no gap**, not a flat plate.
- Pocock stocks a **"Fin, plastic (8+, 4+)"** as a distinct part from the smaller 1x/2x fin.[15]
- **The fin is engineered to break away.** Pocock: *"Never use silicone or other adhesives on the fin box. The fin is engineered to break away."*[4] It seats in a **fin box** recessed in the hull.
- **Rudder:** one only, per World Rowing.[19] Parts: **rudder blade (plastic)** + **rudder shaft**.[15] Mounted at the stern, immediately aft of the fin.
- **Steering linkage — bowloader specific:** because the cox lies in the bow, the linkage runs the *entire length of the boat*. Pocock stocks a **"Bowcox tiller"** plus **cable** and **housing** sold by the foot.[15] Vespoli sells a **"Push-Pull Steering Cable — Bow Coxed Fours."**[27] So the mechanism is a **sheathed push-pull cable** (Bowden-type), not the open rudder lines/toggles of a stern-coxed boat.
  - In a stern-coxed boat you would see **tiller ropes with tiller balls** running along the gunwales to the cox's hands.[15] **Do not model these on the Comp K4+.**
  - On the bowloader, the cable is largely **concealed** — RowSource notes *"In the stern you're used to steering cables that run along the port and starboard gunwales. **In a bowloader you may not see the steering wires.**"* The cox operates a small **tiller handle/rod** inside the bow compartment.
- Other stern-area details: **Yoke** and **steering pulley** are stock parts.[15]

### 4.9 Other Deck and Structural Details

| Item | Detail | Source |
|---|---|---|
| **Gunwale / saxboard** | Narrow flat ledge along the cockpit edge; the rigger bolting surface. Carbon is used *"in gunwale and keel to simulate a beam."* | [4][14] |
| **Ribs / internal structure** | **None visible.** Monocoque — no shoulders, no ribs. The cockpit interior is a smooth continuous molded **full-length pan**. | [4][8] |
| **Shoulder / deck seam** | Because the boat is shoulderless, there is no traditional shoulder joint. The deck-to-hull transition is a **molded seam at the gunwale line**, visible as a fine parting line. | [4][6] |
| **Splash guards** | Low, molded, at the forward end of the cockpit and around the cox opening. | INFERRED |
| **Gunwale guard** | Pocock provides a gunwale guard option with all new boats (protects gunwales from trailer straps). | [4] |
| **Bow number holder** | "Bowclip" — small bracket on the bow deck. | [15] |
| **Cox box holder** | Stock part; mounted in the cox compartment. Cox box + wiring adds ~4 lb. | [8][15] |
| **Inspection ports** | Round screw-in ports in the decks for access to sealed compartments. | [15] |
| **Drain bung** | Small threaded plug, typically low near the stern. | [15] |
| **Decking tape** | Sold in 1" × 150' and ½" × 150' rolls — used along seams. | [15] |
| **Production plaque** | Required inside the boat, ≤ 50 cm². | [19] |
| **Washboard plate** | Plastic, under the rigger mounts. | [15] |

---

## 5. OARS

Sweep oars are **not part of the boat's minimum weight** and are bought separately.[19] Concept2 is the dominant US supplier; Croker and Dreissigacker (Dreissigacker *is* Concept2 — the founding brothers) are the other names, plus Croker (Australia).

### 5.1 Length (VERIFIED — Concept2)[9][24]

| Range | Comp / Smoothie2 / Big Blade | Fat2 |
|---|---|---|
| Short | 367–372 cm | 362–367 cm |
| **Medium** | **370–375 cm** | 365–370 cm |
| Long | 373–378 cm | 368–373 cm |

Oars are adjustable; ~4 turns of the end screw moves 1 cm.[24] **Use 372 cm** for a default four. Measured from the end of the grip to the end of the blade, continuing through the blade centerline on a hatchet.[24]

### 5.2 Blade Shapes (VERIFIED — Concept2)[10][25]

| Blade | Length | Width at tip | Width at broadest | Thickness | Notes |
|---|---|---|---|---|---|
| **Fat2** | **55 cm** | **19 cm** | **26.5 cm** | 5 mm | Asymmetric hatchet, Vortex Edge standard, widest current design. Rigged 4–8 cm shorter than Smoothie2. |
| Smoothie2 (VE / PE) | 54 cm | — | 25 cm | 5 mm | Asymmetric hatchet. The workhorse. |
| Big Blade | 52 or 55 cm | 25 cm | 25 cm | 5 mm | Asymmetric, central ridge on face. The original 1991 hatchet. |
| **Macon** | 58 cm | Med 16.5 / Lg 18 cm | Med 20 / Lg 21 cm | 5 mm | **Symmetrical "tulip"**, central spine. The *old* pre-1991 shape. Recreational/classic use. |

**Hatchet vs Macon — the shape difference that matters:**
- **Macon** is *symmetrical* about the shaft axis — a rounded "tulip" or spoon, longer (58 cm) and narrower (20–21 cm), with a central spine on the face. This is the classic shape and is **wrong for a modern racing four**.
- **Hatchet/cleaver** (Fat2, Smoothie2, Big Blade) is **asymmetric**: the blade extends much further on one side of the shaft axis than the other, giving a cleaver or meat-axe outline. Shorter (52–55 cm) and much wider (25–26.5 cm). The tip is squared off, not rounded. **This is what to model.**
- The brief's "roughly 25 cm wide by 55 cm long" is accurate — it matches Big Blade 55 (25 × 55) and is close to Fat2 (26.5 × 55).
- **Vortex Edge:** a raised ridge along the blade tip edge, standard on Comp, Fat2, and Smoothie2 VE.[10] A small but visible surface detail.

### 5.3 Shaft, Sleeve, Collar, Handle

- **Shaft:** carbon fiber, tapered — thicker near the collar, thinner toward the blade. Available in "Ultralight" and "Skinny" profiles; Ultralight comes in Soft/Medium/Stiff flex.[Concept2 order guide]
- **Sleeve:** a plastic wrap on the shaft where it sits in the oarlock, protecting the shaft and providing the bearing surface. Concept2 Macon, Concept2 Smoothie and Croker sleeves are the common types.[21]
- **Collar / button:** an adjustable plastic stop clamped on the shaft, bearing against the inboard face of the oarlock, setting the inboard length laterally.[21] Position: **spread + 29–31 cm** = inboard, measured from the end of the handle.[24] At 85 cm spread → **inboard ≈ 114–116 cm** (matches Concept2's stated 113–117 cm sweep inboard range).
- **Handle/grip:** sweep oars have a **single long cylindrical grip** for two hands (unlike sculls' two short grips). Composite adjustable handles, or fixed wood in Small 39 mm / Medium 42 mm / Large 45 mm diameter.[Concept2 order guide]
- **Standard color:** white blades unless custom-ordered; custom colors are single solid colors only, and any stripes/designs must be applied by the crew.[10]

### 5.4 Rigging Relationships (for posing oars correctly)

- **Sweep arc:** ~90° total (catch to finish); elite average is **92°**.[11][slideshare]
- **Catch angle:** 45–62° before perpendicular; elite average **55°**.[11]
- **Finish angle:** 30–35° past perpendicular.[11]
- Worked example from World Rowing: SL = 90°+, Catch = −58°, Finish = 33°, Spread = 84 cm.[11]
- **Gearing ratio** example (men's coxless pair): oar 376 cm, inboard 117 cm, span 85 cm → ratio 2.74.[slideshare]

---

## 6. APPEARANCE AND FINISH

### 6.1 Color — Pocock Boats Are White. Always. (VERIFIED)

This is one of the most useful verified facts in this document. Pocock's FAQ, in full:[4]

> *"The hull is finished in the mold and is the first step of the build process. This creates the smoothest surface possible and minimizes the amount of weight that goes into paint... **Pocock shells use a proprietary white paint and clear coat over carbon fiber. We had to pick one color to go with, so we went with white.** When you are offered color customization by a boat builder, it means the boats are painted in the last step of the process. When this is the case, hulls are not just painted, but also faired out and smoothed down with Bondo. We would much rather spend time taking care of our molds and provide our customers with **white boats that have more carbon, less paint, and ZERO Bondo.**"*

So:
- **Hull: gloss white**, painted *in the mold*, with clear coat over carbon.
- **The only customization is vinyl striping — 10 colors, 4 styles.**[1] These are applied decals, typically a pin stripe or wider band running along the hull side near the gunwale, in the team's color.
- **Decks and cockpit: exposed black carbon weave under clear coat** — the Comp's signature look.[1] Expect a visible 2×2 twill pattern.
- Because the finish is molded rather than sprayed-and-faired, the surface is **exceptionally smooth and optically flat** — Pocock: *"We tenaciously buff and polish our molds and control the mold's release system to ensure that the finished hull is perfectly smooth."*[14]

### 6.2 Logo and Wordmark Placement

From Pocock's own product photography (verified visually):
- A **Pocock logo mark** appears on the **bow deck**, forward, and again near the **stern deck**. In the overhead views these read as small dark graphics on the white/black deck.
- Pocock stocks **"Decal, large"** and **"Decal, small"** as separate parts.[15]
- Team/school identification (large block letters, e.g. a university initial) is applied as **vinyl on the hull side** near the bow, forward of the first rigger — visible in the K4+ detail photography as a large dark letterform on the white hull.
- The **production plaque** is inside the boat, not a visible exterior feature.[19]

### 6.3 Material and Layup (VERIFIED)

Pocock's stated materials:[4]
- **Carbon** — stiffness component. *"Used in gunwale and keel to simulate a beam, and throughout the hull for rigidity at minimal weight."*
- **Kevlar™** — high impact resistance; a layer used throughout certain boats to prevent breakage.
- **Fiberglass** — used where solid reinforcement fabric is needed.
- **Closed cell foam core** — *"The tiny enclosed cells prevent water absorption and provide a greater bonding surface with the skin."*

By tier:[5]
- **Hypercarbon / Hypercarbon Comp:** all-carbon layup with a **foam core**.
- **Core:** carbon/fiberglass with foam or **syntactic resin core**.

**Hypercarbon laminate system:** developed with the University of Washington Department of Chemical Engineering — a new high-performance epoxy **wet laminating** system developed specifically for Pocock to improve stiffness and strength.[14] Pocock's own comparative testing showed the Hypercarbon laminate is *"almost twice as stiff longitudinally, 22% stiffer in torsion and has 38% less rigger deflection"* than the previous laminate, while being a few pounds lighter.[8]

Build sequence (outside-in) — relevant because it explains the finish:[14]
1. Molds meticulously waxed
2. Proprietary **white paint applied into the mold** — this becomes the outer skin
3. Carbon and composite fibers, hand-cut in the shop, laid in
4. Cured — creating a strong paint-to-fiber bond that *"will not crack, peel or dimple"*
5. Boat comes out of the mold clean, needing no patching or painting

### 6.4 Light Behavior on a Wet Composite Hull

For shader/lighting setup (INFERRED from material properties, but well-grounded):

- **Dry gloss white gelcoat/paint + clear coat:** a **two-layer specular response** — a broad diffuse white base with a tight, bright clear-coat specular highlight on top. Roughness on the clear coat is very low (0.05–0.12). The hull acts almost like automotive paint.
- **Wet:** a water film **lowers roughness further** (toward 0.02–0.05) and **raises specular intensity**, producing long mirror-like streaks of sky and shoreline reflection down the topsides. Water sheets off rather than beading — the surface is waxed (Pocock recommends 3M Scotchgard Marine Liquid Wax twice yearly[4]).
- **Exposed carbon decks:** strongly **anisotropic**. The twill weave produces directional highlights that shift as the view angle changes, plus a visible weave normal-map at close range. Base color near-black with a slight brown-purple sheen in the resin. Clear coat on top adds a second, sharper specular layer.
- **Waterline:** expect a **wet/dry transition line** on the topsides — the hull is darker, glossier and more reflective below the spray line, with visible droplets and a slight sheen gradient above it.
- **Underwater:** below the waterline the white hull reads as pale green-blue through the water, with caustics playing across it and strong refractive distortion at the waterline itself.
- **Riggers:** carbon wings are **satin-to-gloss black**, less reflective than the deck. Aluminum wings (on the standard Hypercarbon) are **brushed/anodized silver** with visible weld beads at the joints — clearly visible in Pocock's detail photography.
- **Metal hardware:** pins and bolts are **polished stainless** — sharp, bright, small specular hits.

---

## 7. REFERENCE IMAGERY

### 7.1 Pocock Official — Hypercarbon Comp K4+ (the exact subject)

All URLs verified present in the page source of `https://www.pocock.com/shells/hypercarbon-comp-k4/`.

| View | Direct image URL |
|---|---|
| **Overhead plan, full boat, 8192×1280** ★ | `https://www.pocock.com/wp-content/uploads/2016/03/hypercarbon-comp-k4plus-zoom.jpg` |
| Detail 1 (full res) | `https://www.pocock.com/wp-content/uploads/2017/03/Compk4plus-1.jpg` |
| Detail 1 (1200×800) | `https://www.pocock.com/wp-content/uploads/2017/03/Compk4plus-1-1200x800.jpg` |
| Detail 2 (full res) | `https://www.pocock.com/wp-content/uploads/2017/03/Compk4plus-2.jpg` |
| Detail 2 (1200×800) | `https://www.pocock.com/wp-content/uploads/2017/03/Compk4plus-2-1200x800.jpg` |
| Detail 4 (full res) | `https://www.pocock.com/wp-content/uploads/2017/03/Compk4plus-4.jpg` |
| Detail 4 (1200×800) | `https://www.pocock.com/wp-content/uploads/2017/03/Compk4plus-4-1200x800.jpg` |
| Vertical composite (500×3320) | `https://www.pocock.com/wp-content/uploads/2017/03/comp-k4plus-vertical.jpg` |
| Shared K4+ detail | `https://www.pocock.com/wp-content/uploads/2017/03/k4plus-3.jpg` |

★ = **the single most valuable reference.** This is a full-length, dead-overhead plan view at 8192 px wide. It is effectively a photographic plan drawing: measure the hull outline, rigger positions, cockpit opening, and cox compartment directly off it.

### 7.2 Pocock Official — Hypercarbon K4+ (same hull mold, different rigger/deck)

From `https://www.pocock.com/shells/hypercarbon-k4/`:

| View | Direct image URL |
|---|---|
| **Overhead plan, carbon wings, 8192×1280** ★ | `https://www.pocock.com/wp-content/uploads/2016/01/HypercarbonK4_CarbonWingRiggers_LARGE.jpg` |
| **Overhead plan, aluminum wings (500×3320)** ★ | `https://www.pocock.com/wp-content/uploads/2016/01/HypercarbonK4_AluminumWingRiggers-e1454098294382.jpg` |
| Overhead plan, carbon wings (500×3200) | `https://www.pocock.com/wp-content/uploads/2016/01/HypercarbonK4_CarbonWingRiggers-e1454098297850.jpg` |
| Page header, boat on water (2000×500) | `https://www.pocock.com/wp-content/uploads/2016/01/kfourplusheader.jpg` |
| Hero (2000×500) | `https://www.pocock.com/wp-content/uploads/2016/01/k4plus.jpg` |
| Detail 1 | `https://www.pocock.com/wp-content/uploads/2016/01/k4plus-1.jpg` |
| Detail 3 | `https://www.pocock.com/wp-content/uploads/2016/01/k4plus-3.jpg` |
| **Detail 4 — footboard/stretcher close-up** ★ | `https://www.pocock.com/wp-content/uploads/2016/01/k4plus-4.jpg` |
| Detail 5 | `https://www.pocock.com/wp-content/uploads/2016/01/k4plus-5.jpg` |

**The aluminum vs carbon wing pair is exceptionally useful** — the same boat photographed from the same overhead angle with both rigger options, letting you compare wing geometry directly.

`k4plus-4.jpg` is a high-resolution close-up showing the aluminum foot-stretcher structure with weld beads, the white rowing shoes with straps, the black carbon cockpit weave, the white hull with a team letterform decal, the black seat track, and a black deck clip. This is the best single texture/material reference.

### 7.3 Pocock Company Pages

| Page | URL |
|---|---|
| Comp K4+ product page | `https://www.pocock.com/shells/hypercarbon-comp-k4/` |
| Hypercarbon K4+ product page | `https://www.pocock.com/shells/hypercarbon-k4/` |
| Core K4+ (has waterline beam) | `https://www.pocock.com/shells/core-k4/` |
| All shells / product line | `https://www.pocock.com/shells/` |
| FAQ (materials, color, rigging) | `https://www.pocock.com/about/faq/` |
| History | `https://www.pocock.com/about/history/` |
| Stiffness testing data | `https://www.pocock.com/prototyping-engineering/stiffness-testing/` |
| Science of Speed (wings, fin, finish) | `https://pocockparts.com/pages/the-science-of-speed` |
| Parts store — K4 riggers | `https://pocockparts.com/collections/k4` |
| G7 Carbon Sweep Wing (complete) | `https://pocockparts.com/products/g7-carbon-wing-complete-oarlock-sill-pin-bowbrace` |
| Historical parts catalogue (dimensions!) | `http://www.pocockclassic.org/pocock/parts.html` |
| History photos | `https://www.pocock.com/wp-content/uploads/2015/06/history1.jpg` … `history7.jpg` |

### 7.4 Angles Still Needed — Where to Find Them

Pocock's own photography is overwhelmingly **overhead plan view**. It does not publish clean side-profile, bow-on, or stern-on studio shots. For those:

| Angle | Where to look |
|---|---|
| Side profile, bow-on, stern-on, three-quarter, on-water action | **row2k photo galleries** — `https://www.row2k.com/gallery/` . Filter by "Fours". Large archive of racing photography, searchable by year and regatta. e.g. `https://www.row2k.com/gallery/index.cfm?year=2024` |
| Coxed four racing, all angles | row2k Lake Wheeler Invitational fours gallery: `https://www.row2k.com/gallery/gallery.cfm?action=gallery&category=Lake+Wheeler+Invitational&dir=2026Spring%2FWheeler%2F0424WheelerPM4s` |
| Men's Four Olympic champions feature (high-quality action) | `https://www.row2k.com/features/6462/1231-mens-four-olympic-champions/` |
| Cockpit / rigger detail | Pocock parts store product photography: `https://pocockparts.com/collections/k4` |
| Refurbishment shots (hull stripped, interior) | `https://flr.rowerchoice.dev.stradiggy.com/shell-refurbishment/` |
| Pocock social media (frequent new-boat photography) | Instagram `@pocockracing`, Facebook `PocockRacing` |

### 7.5 Existing 3D Models, CAD and Line Drawings

| Resource | URL | Notes |
|---|---|---|
| **Coxless Four Rowing Boat — Sketchfab** | `https://sketchfab.com/3d-models/coxless-four-rowing-boat-f111d0136b3c494ba4d2d4502d31e705` | By adrianovalentini. A 4− (no cox) but the closest published model to the subject. 4K diffuse/metallic/roughness textures. Also on CGTrader and TurboSquid. **Best available 3D starting reference.** |
| **1:10 sculling racing shell — MakerWorld** | `https://makerworld.com/en/models/874684-1-10-sculling-racing-shell-rowing-boat` | Free print model. *"It is modeled after a real racing shell, riggers and oars. **The measurements are to scale.**"* Useful for proportion checking. |
| **US Patent 5,474,008 — Eight man rowing shell** ★ | `https://patents.google.com/patent/US5474008A/en` | **The single best geometry document available.** Vespoli/Nelson/Scragg. Full sectional-area tables, entry/exit angles, max beam/draft, metacentric height, and 7 pages of drawings including body plans (FIGS. 5a/5b/6a/6b), lines plan (FIG. 2), plan view (FIG. 1), and cross-section (FIG. 3). |
| Patent drawing sheets (direct) | `https://patentimages.storage.googleapis.com/71/f2/5f/8692ff0fe97d3c/US5474008-drawings-page-2.png` (also pages 3–8, same URL pattern with different hashes — see the patent page) | The body-plan sheets are the actual sectional drawings. |
| Atkinsopht — Shell Hydrodynamics | `http://atkinsopht.com/row/shellhyd.htm` | Computational shell model. Documents the semi-circular section assumption, block and prismatic coefficients, wetted surface derivation. Notes that builders would not release Cb/Cp data. |
| Veloce Racing Scull plans (buildable) | `https://duckworks.com/veloce-racing-scull-plans` | Actual buildable plans for a single. Wrong boat class, but real shell lines. |
| Reddit thread seeking shell/oarlock models | `https://reddit.com/r/Rowing/comments/1ifbljm/looking_for_shell_oarlock_and_other_3d_models_for` | Confirms the scarcity — no good public CAD of racing shells exists. |

> **No Pocock CAD, offsets table, or lines drawing is publicly available.** I searched Pocock's site, the parts store, GrabCAD, Sketchfab, and patent databases. Pocock treats hull lines as trade secret — Atkinsopht records that *"A request for information from many boat makers has produced no result whatever."*[17] The Vespoli patent is the workaround: it is the only published, dimensioned racing-shell geometry in the public record.

---

## 8. MODELING CHECKLIST — Quick Reference

```
HULL
  [ ] LOA                    13.6 m          (INFERRED from 12.65 m WL, medium hull)
  [ ] Waterline length       12.65 m         (VERIFIED, medium)
  [ ] Max beam (gunwale)     ~55 cm          (INFERRED)
  [ ] Waterline beam         44.2 cm         (VERIFIED, Core K4+ medium proxy)
  [ ] Max draft, loaded      ~18 cm          (INFERRED from patent)
  [ ] Freeboard amidships    12-18 cm        (INFERRED)
  [ ] Entry half-angle       ~3.8 deg        (VERIFIED, patent)
  [ ] Exit half-angle        ~4.5 deg        (VERIFIED, patent — LARGER than entry)
  [ ] Rocker, total          3-6 cm          (INFERRED)
  [ ] Section shape          semicircular / shallow-U, wineglass underwater
  [ ] Max section at         station 5 (midship), slightly forward
  [ ] Construction look      monocoque, NO ribs, NO shoulders, full-length pan

COXSWAIN  -- BOW LOADER
  [ ] Cox compartment aft of bow ball, forward of seat 1
  [ ] Opening >= 70 cm long, full-width for >= 50 cm
  [ ] Padded headrest at forward end
  [ ] Deck peaks over the cox station -- highest point of the boat
  [ ] NO stern cockpit. Stern deck is closed and tapers to a point.

RIGGING
  [ ] G7 carbon wing rigger, stern-mounted, bolted ACROSS TOP of gunwales
  [ ] 4 wings, oarlocks alternating S-P-S-P bow to stern
  [ ] 1 bowbrace stay per side per station
  [ ] Spread                 85 cm centerline-to-pin   (TYPICAL)
  [ ] Oarlock height         ~17 cm above seat          (TYPICAL)
  [ ] Pin                    1/2 in stainless, vertical
  [ ] Pitch                  4 deg (4/4 bushings)       (VERIFIED)
  [ ] Oarlock                Concept2, black, hinged gate
  [ ] Tracks                 81.3 cm (32 in) aluminum   (VERIFIED)
  [ ] Seat                   single-carriage carbon, sealed bearing wheels
  [ ] Footboard              carbon, 40 deg rake, heel cups + heel ties

OARS (x4)
  [ ] Length                 372 cm                     (VERIFIED range)
  [ ] Blade                  HATCHET, asymmetric — 25 x 55 cm  (NOT Macon)
  [ ] Blade thickness        5 mm min                   (VERIFIED, rule)
  [ ] Inboard                ~115 cm  (spread + 30 cm)
  [ ] Shaft                  carbon, tapered
  [ ] Collar + plastic sleeve at the oarlock
  [ ] Single long grip (sweep, two hands)

STERN
  [ ] Foil-shaped fin in a break-away fin box
  [ ] Rudder immediately aft, NO GAP to the fin (integrated system)
  [ ] Push-pull sheathed cable to bow — steering wires mostly CONCEALED
  [ ] NO tiller ropes / toggles along the gunwales

BOW
  [ ] White bow ball, dia >= 4 cm                        (VERIFIED, rule)
  [ ] Bow number clip on the deck

FINISH
  [ ] Hull            GLOSS WHITE, molded-in paint + clear coat
  [ ] Decks/cockpit   EXPOSED BLACK CARBON TWILL under clear coat
  [ ] Stripe          vinyl, team color, along the hull side
  [ ] Riggers         satin/gloss black carbon
  [ ] Logo            Pocock mark on bow deck and stern deck
  [ ] Hardware        polished stainless
```

---

## 9. CONFIDENCE SUMMARY

| Section | Confidence | Note |
|---|---|---|
| Company history, product line | **High** | Pocock's own site |
| Comp K4+ published specs (crew wt, WL length, rigged wt) | **High** | Pocock product page, verified by extraction |
| Waterline beam | **Medium** | From Core K4+ page; same hull class, different layup. Not published for the Comp. |
| Bow-coxed configuration | **High** | Visually confirmed in two independent Pocock plan-view photographs, corroborated by four textual sources |
| Rigger type (G7 carbon wing, stern-mounted, gunwale-top) | **High** | Named explicitly on the product page and in the parts store |
| Materials and layup | **High** | Pocock FAQ and Science of Speed |
| Color and finish | **High** | Pocock FAQ states it unambiguously |
| Regulatory dimensions (bow ball, cox opening, weight) | **High** | World Rowing equipment compliance page |
| Oar dimensions | **High** | Concept2 published specs |
| Sectional-area curve, entry/exit angles | **Medium-High** | Real published data, but for an eight (Vespoli patent), not a Pocock four. Shape transfers; absolute scale does not. |
| LOA, max beam, draft, freeboard, rocker | **Low-Medium — INFERRED** | Derived from waterline data + class norms. Not published by Pocock. |
| Sheer line description | **Medium** | Read from photography, not measured |
| Rigger spread, oarlock height, stretcher angle | **Medium — TYPICAL** | Coach-adjustable settings; class norms given, Pocock historical values noted |

**The riskiest numbers in this document are LOA, max beam, freeboard and rocker.** If dimensional accuracy against photographs is the acceptance criterion, derive these by photogrammetry from `hypercarbon-comp-k4plus-zoom.jpg` (8192 px overhead plan) scaled against the one hard known: the 12.65 m waterline length. That single image plus that one scale reference will beat every inferred figure in §2.4.

---

## Sources

[1] https://www.pocock.com/shells/hypercarbon-comp-k4
[2] https://www.pocock.com/shells/hypercarbon-k4
[3] https://www.pocock.com/shells/core-k4
[4] https://www.pocock.com/about/faq
[5] https://www.pocock.com/shells
[6] https://www.pocock.com/about/history
[7] https://en.wikipedia.org/wiki/Pocock_Racing_Shells
[8] https://www.pocock.com/prototyping-engineering/stiffness-testing
[9] https://www.concept2.com/oars/sweeps/length-and-rigging
[10] https://www.concept2.com/oars/sweeps/blades
[11] https://worldrowing.com/wp-content/uploads/2020/10/Practical-Boat-Rigging-Gianni-Postilione-Conny-Draper.pdf
[12] https://uclamensrowing.com/shells-riggers
[13] https://en.wikipedia.org/wiki/Bowloader
[14] https://pocockparts.com/pages/the-science-of-speed
[15] http://www.pocockclassic.org/pocock/parts.html
[16] https://patents.google.com/patent/US5474008A/en
[17] http://atkinsopht.com/row/shellhyd.htm
[18] https://pocockparts.com/products/g7-carbon-wing-complete-oarlock-sill-pin-bowbrace
[19] https://worldrowing.com/technical/equipment-technology/equipment-compliance
[20] https://rowhq.app/us/glossary/rowing-shell
[21] https://rowhq.app/ca/glossary/rigger
[22] https://readyallrow.org/tag/foot-stretchers
[23] https://pocockparts.com/collections/k4
[24] https://www.concept2.com/support/oars/oar-length
[25] https://www.concept2.nl/en/oars/oar-options/blades/fat2
[26] https://groups.google.com/g/rec.sport.rowing/c/WlcxfydKxDI
[27] https://store.vespoli.com/Steering-Parts-Coxed-Boats-8-4-c29605456
[28] https://www.fhccrew.org/the-boat
[29] https://pocockparts.com/pages/eights
[30] https://sketchfab.com/3d-models/coxless-four-rowing-boat-f111d0136b3c494ba4d2d4502d31e705
[31] https://makerworld.com/en/models/874684-1-10-sculling-racing-shell-rowing-boat
[32] https://en.wikipedia.org/wiki/Racing_shell
[33] https://www.row2k.com/gallery
