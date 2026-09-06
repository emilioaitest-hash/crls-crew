# CRLS Rowing — At Home on the Charles

A documentary website for the Cambridge Rindge & Latin School crew program: a
no-fee public high school rowing team in Cambridge, Massachusetts that races
New England's prep schools on the Charles River.

## What this is built from

Nothing on the page is invented. Every number comes from a scraped archive and
every claim carries a source link.

**The race archive** — 1,321 results, 2007–2026, pulled from row2k, the NEIRA
championship PDFs, MPSRA/HereNow timing data and USRowing regionals. 394 first
places. 186 coxswains named. The season chart is drawn straight from it.

**The history** — the program's own account, cross-checked against The Harvard
Crimson's archive. Where the team's history and the primary record disagree
(the 1643 vs 1648 founding, the 1977 vs 1978 merger, whether the 1929 crash
actually ended the program), the page shows both rather than picking one.

**The 1929 heat structure** — the argument of the site. The Crimson's preview of
that year's Schoolboy Regatta records the eights split into separate public and
private heats, while the fours raced everyone together in one heat. The fours
are the boat Cambridge rowed.

## The boat

`src/boat/` builds a Pocock Hypercarbon Comp K4+ as parametric geometry rather
than a downloaded mesh. It is a bow-loader with G7 carbon wing riggers, which
the research corrected — the first version had a stern cockpit and tubular
riggers, and both were wrong.

The hull is validated numerically before it is ever rendered:

```
node tools/validate-hull.js       # form, displacement, area curve
node tools/validate-hardware.js   # rigging and cockpit placement
```

| Check | Result | Real boat |
|---|---|---|
| Entry / exit half-angle | 3.80° / 4.50° | 3.6–4.0 / 4.05–4.95 |
| Draft, loaded | 171 mm | 172–192 (8+) |
| Freeboard | 137 mm | 120–180 |
| Waterline length | 12.90 m | 12.50–12.93 published |
| Prismatic coefficient | 0.648 | 0.60–0.68 |
| Section-area curve vs US Patent 5,474,008 | RMS 0.035 | — |

`tools/solve-beam.js` derives the half-beam distribution by inverting the
patent's section-area curve, rather than guessing exponents.

## Running it

```
npm install
npm run dev       # http://localhost:5173
npm run build
```

## Photography

`src/data/photos.js` records provenance for every image. One archive photo was
removed because it showed rowers in MIT kit rather than CRLS. The strongest
frame in the set is row2k's and is flagged `NEEDS_CLEARANCE` — it is credited on
the page but needs permission before publication.

The team's public archive is mostly race-announcement graphics with type burned
in; only a handful are usable photographs. Commissioned photography is the
single biggest improvement available to this site.

## Structure

```
index.html            the page
src/styles.css        design system
src/main.js           scroll, reveals, both 3D scenes
src/boat/pocock.js    hull geometry
src/boat/hardware.js  riggers, seats, oars, fittings
src/data/team.js      all content, with sources
tools/                validators and the beam solver
research/             the raw scrape and reference documents
```
