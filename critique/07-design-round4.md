# CRLS Rowing — Design Critique, Round 4

**Judged against:** Awwwards Site of the Day (the real bar)
**Reviewed at:** 2560×1440, 1600×900, 390×844 — live build served from `dist/` via `vite preview`, measured over CDP
**Commit under review:** `e6f1d9d` "Round 3 fixes: delete the duplicate, write the column, stop decorating"
**Source read:** `index.html`, `src/styles.css`, `src/main.js`, `src/data/team.js`
**Prior reviews:** `01-design.md` 6.2 REJECTED · `05-design-round2.md` 7.4 HM · `06-design-round3.md` 7.6 HM

Measured with `tools/cdp.py` driving headless Chrome against `http://localhost:4188/crls-crew/` (`location.href` confirmed every pass). Glyph density is the union area of text client rects — the same method that exposed round 3's "94% fill" as a 245px underline. Webfont resolution confirmed (`document.fonts.status === 'loaded'`) before every type metric.

---

## VERDICT

**Overall: 7.9 / 10 — HONORABLE MENTION.** Still not Site of the Day. But the reason changed, and that matters more than the +0.3.

Round 3 closed by saying the gap was **content, not craft** — roughly 30 sentences nobody had written. **Those sentences got written.** The apparatus column now carries 37 key/value pairs averaging 201 characters per row, with Harvard Crimson citations carrying real publication dates, race distances, finishing margins and heat orders. `['Conditions','Rain']` and `['Stretch','Powerhouse']` as the *entire* content of a row are gone. That was the hard part, and it is done.

And the column still measures emptier than it did in round 3.

**Aside glyph density: 14.8% (R3) → 10.2% (R4).** Not because the writing failed — because `.facts` is capped at `max-width: 32rem` (512px) inside a track that this round widened to **992px**. The content doubled; the track doubled faster; the box holding the content did not move. Half the apparatus column is empty by CSS declaration, with 554px of `border-top` still drawing across nothing on every row.

**The claimed "47.4%" is the round-3 error repeated in a new place.** Measured horizontal ink extent across the track is **44.1%** — within noise of the claim. Measured ink *area* is 10.2%. The number being reported is still how far right the text reaches, not how much text there is. Third round in a row that a fill claim has been made against a horizontal measure and failed against an area measure.

Seven of thirteen items landed cleanly, including two that had been open since round 2. The duplication is genuinely gone. The stair-step is genuinely gone. The stagger genuinely animates. Four unprompted content additions — the boat rename, the fleet roster, the road-to-final progressions, the honest medal claim — are the best evidence of authorship in the project's history.

Against that: the site shipped a horizontal scrollbar on mobile, caused by the apparatus rewrite itself, and reintroduced a 3.25:1 contrast failure in brand-new markup after spending two rounds eliminating exactly that value.

---

## SCORES

| # | Category | R1 | R2 | R3 | **R4** | Δ (R3→R4) |
|---|---|---|---|---|---|---|
| 1 | Typography | 7.0 | 8.0 | 8.0 | **8.2** | +0.2 |
| 2 | Layout | 4.0 | 6.0 | 6.5 | **6.8** | +0.3 |
| 3 | Colour & Light | 8.0 | 8.0 | 8.0 | **8.2** | +0.2 |
| 4 | Motion | 5.5 | 6.5 | 6.5 | **7.0** | +0.5 |
| 5 | Narrative | 7.0 | 8.5 | 8.0 | **8.5** | +0.5 |
| 6 | AI-Slop Resistance | 8.5 | 9.0 | 8.5 | **9.0** | +0.5 |
| | **Overall** | **6.2** | **7.4** | **7.6** | **7.9** | **+0.3** |

Both categories that went down in round 3 recovered fully. Nothing went down this round.

---

## DID THE ROUND-3 FIXES LAND?

| # | Fix | Status | Measurement |
|---|---|---|---|
| P0.1 | Delete the 2000 duplicate | **LANDED** | `isStaged` applied to both halves. **9 rows**, no 2000 row (`has2000Row: false`). Phrase scan: "twelve students" ×1, "no equipment" ×1, "fifty kids" ×0. 5-gram block-overlap scan across all `.tl-item`/`.hinge`/`.thesis`/`.quote`: **0 duplicate pairs**. `.quote` count 1. The revival band is the only telling. *(Claim said 8 rows; there are 9 — the 1929 hinge is filtered, the 1929 "And then it stopped" row is not. Harmless, but the claim was miscounted.)* |
| P0.2 | **Write the apparatus column** | **PARTIAL — content landed, display did not** | Writing is real: **37 dt/dd pairs**, mean **201 chars** per aside (min 71, max 294), Crimson citations with dates ("28 May 1903", "19 May 1922", "2 June 1926"), distances, margins, finishing orders. But **glyph density 10.2%** (R3: 14.8%), body column **38.5%**. `.facts` is `max-width: 32rem` = **512px inside a 992px track**. Claimed 47.4% ≈ measured **hFill 44.1%** — horizontal extent, not ink. |
| P0.2b | Kill the leader rule | **LANDED** | `.facts dd`: `text-align: start`, `border-bottom: 0px none`. Grid `minmax(0,max-content) minmax(0,1fr)` = 109px/379px, both left. No rule is drawn, so the 245px dead-run is genuinely gone. |
| P0.3 | `.lane` contrast | **LANDED — exceeds claim** | `var(--grey)`. 14 lanes, **4.69–5.66:1**, 0 fail AA. The 8 "Private" labels measure **5.66:1** (claim said 5.15). Was 2.96:1. |
| R3-r1 | 480px stair-step | **LANDED** | `.timeline` `max-width: none`, aside track `minmax(0,1fr)`. **2560px:** timeline / split / chart / boat-stage / footer / field / progression / heat / thesis / results **all 416→2144**. **1600px:** all **64→1536**. **390px:** all **20→370**. Exact at every viewport. |
| R3-r3 | `.narrow--flush` 44rem→36rem | **PARTIAL — goal not met** | Box is 576px (was 704px) ✓. But measured on trimmed rendered lines it runs **77 CPL** and is **still the widest prose measure on the site** (`.tl-body` 75, `.split .lead` 62). The claimed "~62 CPL" is `.split .lead`'s number, not this block's. Smaller type in the same box width — 18px in 576px — produces more characters, not fewer. |
| P2.8 | `.school` stagger actually animates | **LANDED — verified in flight** | `transitionDuration` **0.5s** (was 0s) ✓, delays cascade 0/28/56/84/112/140/168/196ms ✓, `html:not(.js-reveal)` fallback present ✓. Caught mid-transition on a genuine scroll reveal: opacity **0.74 / 0.62 / 0.47 / 0.28 / 0.04 / 0 / 0 …** across chips in one frame, max spread **0.74**, settling to all-1. It visibly staggers. |
| P2.6 | `.bar-none` clearance | **LANDED** | `bottom: 67.2px` (4.2rem). Clearance to `.bar-year` = **26px** at 2560, 1600 *and* 390. Was 0px. |
| P2.8b | `.silence-count` → #47535f | **LANDED** | `rgb(71,83,95)` = #47535F, **2.49:1**. R3 asked ~2.6; 2.49 is inside the 2.5–3:1 intent within rounding. Was 2.17:1. |
| P2.9 | `.progression` is a progression | **LANDED** | `1.15fr 1.6fr 1fr 1fr` → cells **417 / 580 / 363 / 363**. "50" numeral at **96px** against 72px. Real hierarchy; no longer four equal cards. |
| P2.10 | Mobile `.heat-row` stacks, docW == innerW | **MISSED as submitted** | `.heat-row` does stack ✓, but at 390px **docW 446 vs innerW 390 — 56px of horizontal overflow.** Cause is new: `.facts` two-column grid inside a 242px track forces `dd` boxes to 63px and 36px, wrapping values to 5 lines and overflowing 21–48px. The heat diagram was fixed; the apparatus rewrite broke it somewhere else. *(See Regressions — a concurrent commit landed a fix mid-review.)* |
| NEW | Boat renamed, fleet roster | **LANDED** | "Seldon" appears **0** times. "Wylde" ×3. `#fleet` lists **Wylde** (white hull · Hypercarbon Comp K4+ · Modelled), **Og Res** (black · Not yet modelled), **Usain** (white · Not yet modelled). |
| NEW | Road to final | **LANDED** | Two `.road` lists: Girls 1V **7:11.11 3rd → 7:41.01 2nd → 7:27.54 3rd**; Boys 1V **6:28.31 2nd → 7:00.06 2nd → 6:44.62 3rd**. Time trial / semifinal / final A with times and places. |
| NEW | Medal claim stated honestly | **LANDED** | `index.html:386–392` gives the team's "third and fourth" claim *and* what the record shows: "across every NEIRA championship from 2011 to 2026, these are the only two top-three finishes CRLS has, and both came on the same Saturday." The figcaption repeats the distinction. This is the correct handling. |
| NEW | No-JS hero | **LANDED (hero only)** | Script execution disabled before navigation: `<h1>` "At home on the Charles" renders at **opacity 1, 1372×619**. All four stats carry real values in markup — **1,321 / 394 / 186 / $0** with `data-count` attributes. Previously blank and "0". Below the fold with JS off: **0 timeline rows, 0 bars, 0 results, 0 chips, 0 facts, 0 boats**, body text 5,389 chars total. The hero claim lands; the site remains entirely JS-dependent below it. |

**Score: 9 landed, 3 partial, 1 missed, plus 2 new regressions.**

R3 was 7 landed / 6 partial / 2 missed / 3 regressions. Every count improved.

---

## 1. TYPOGRAPHY — 8.2 (was 8.0)

The leader rule is gone and that is a genuine typographic correction, not a cosmetic one. `.facts dd` left-aligned with no `border-bottom` turns a restaurant menu back into a definition list; "Fours" now sits 1.5rem from "Boat class" instead of 291px away behind an underline. Contrast is now clean across the whole apparatus: `.src` 5.66–6.22:1 (24 elements), `.facts dt` 6.22:1 (37), `.facts dd` 14.89:1 (37), `.note` 5.66–6.22:1, `.bar-year` 6.22–14.89:1, `.school` 5.15–14.89:1, `.lane` 4.69–5.66:1. **Zero AA failures across 150+ measured text elements** in the components three rounds have been arguing about.

**Still wrong.** The measure is *still* not unified, and the claim that it is does not survive a trimmed-line count:

| Block | Box | Size | **CPL** |
|---|---|---|---|
| `.narrow--flush p` (closing argument) | 576px | 18px | **77** |
| `.tl-body p` | 544px | 18px | **75** |
| `.split .lead` | 576px | 24px | **62** |
| `.note` | 419px | 13px | **40** |

The closing argument came down from 704px to 576px and is **still the widest measure on the site**. Round 3 asked for it to stop being the widest; it is. Narrowing the box while leaving 18px type in it moved 87→77 characters, not to 62 — the 62 belongs to `.lead`, which is 24px in the same width. Two of the top three prose measures sit above the 68ch ceiling this project set for itself in round 2.

**New failure in new code.** `.boat-state` renders "Not yet modelled" twice at `--grey-2` = **3.25:1**. That is the exact value rounds 2 and 3 spent four separate fixes eliminating from `.src`, `.bar-year`, `.lane` and `.school` — reintroduced in markup written this round. The palette lesson did not travel to the new component.

---

## 2. LAYOUT — 6.8 (was 6.5)

The alignment regression is comprehensively fixed and the apparatus column is comprehensively not.

**What landed.** Dropping `.timeline { max-width: 78rem }` and restoring the aside track to `minmax(0, 1fr)` put every block on the page back on one edge. At 2560px, ten major blocks all run **416 → 2144**. At 1600px, all **64 → 1536**. At 390px, all **20 → 370**. The 480px jog in the right margin entering and leaving `#then` and `#return` is gone. Inline `margin-inline` overrides remain at **0**. Content width holds at **67.5%** of a 2560px viewport (92% at 1600px).

**Why it is still a 6.8.** The apparatus column is emptier than it was last round, and the mechanism is a single declaration:

| Measure | R2 | R3 | **R4** |
|---|---|---|---|
| Aside glyph density | — | 14.8% | **10.2%** |
| Body glyph density | — | 47.9% | **38.5%** |
| Aside chars per row (mean) | ~2 words | ~2 words | **201** |
| `.facts` box width | — | — | **512px** |
| Aside track width | 736px | ~512px | **992px** |
| Mean rule overhang per row | 766px | — | **554px** |

Read that table in order. The writing went from two words to 201 characters — a real editorial win. The track went from ~512px to 992px. And `.facts` stayed pinned at `max-width: 32rem`. **The content that was finally written is confined to the left half of the space that was finally made for it.** Per-row density runs 4.2% (1989) to 14.0% (1889); not one row reaches round 3's fix-list target of 35%.

The `border-top` still spans the full 1728px row while ink stops at x≈1590 — **554px of rule across nothing, every row.** Better than round 2's 766px, worse than it should be given the content now exists.

**Mobile shipped broken.** At 390px the reviewed commit measures **docW 446 vs innerW 390**. The `.heat-row` fix worked; `.facts` replaced it as the overflow source. A two-column definition list inside a 242px track gives `dd` boxes of 63px and 36px — "Three heats, four crews each" wraps to **5 lines in a 36px box**. This is the apparatus rewrite breaking the viewport it was supposed to have been tested in.

---

## 3. COLOUR & LIGHT — 8.2 (was 8.0)

`.lane` is fixed, and it was the one that mattered. Round 3 called leaving it "precisely backwards" — fixing the chart axis and the school chips while the hinge diagram's own labels failed. All 14 lanes now measure 4.69–5.66:1, the eight "Private" labels at **5.66:1**, better than the 5.15 claimed. The site's best piece of information design is now legible in the part that carries its argument.

`.silence-count` at #47535f measures **2.49:1** — a 128px numeral that finally reads as a deliberately quiet mark rather than a rendering fault. Round 2 asked for this; it took two rounds but it is right.

**Against that:** `.boat-state` at 3.25:1, as above. And `--river` / `--river-lit` are declared and unused outside the WebGL rim light for the **fourth consecutive round**. The site has defined itself a cold blue mid-tone across four reviews and has never once lit anything with it. At some point that stops being an oversight and becomes a dead variable that should either be used or deleted.

---

## 4. MOTION — 7.0 (was 6.5)

The stagger finally animates, and I verified it the way round 3 demanded — not by reading CSS but by catching it in flight. Scrolling `#field` into view on a fresh load and sampling every 60ms gives a single frame reading **0.74 / 0.62 / 0.47 / 0.28 / 0.04 / 0 / 0 / 0** across the first eight chips, max spread 0.74, monotonic, settling to all-1. Chips arrive as a cascade. Round 3's `transition-duration: 0s` no-op is properly resolved, and the `html:not(.js-reveal)` fallback means it degrades to simply present.

The 0.95s curve still sits on the right three elements (`.hinge-line`, `.thesis .amount`, `.quote`).

**Why not higher.** **22 of 55 reveal elements still share `0.55s` at `0s` delay** — against 21 of 53 in round 3. That is statistically unchanged for the third round running. The stagger has now reached `.tl-item`, `.result`, `.bar-col` and `.school`; everything else still fades identically. Motion still mostly announces that a scroll tick fired.

---

## 5. NARRATIVE — 8.5 (was 8.0, recovering round 3's loss)

The duplication is gone and I checked it three ways: no 2000 timeline row, phrase counts of 1 for "twelve students" and "no equipment", and a 5-gram overlap scan across every timeline row, hinge, thesis and quote returning **zero duplicate block pairs**. The revival band is the only telling of that story. Round 3's self-inflicted regression is fully reversed.

More interesting is what arrived unprompted, because all four items are the same *kind* of decision:

- **The boat was renamed** from "Seldon Wylde" to "Wylde" because the longer name appeared in no primary source. The correction came from the coach's race-day lineup — which also surfaced two more shells, now listed in `#fleet` with hull colour and an honest "Modelled / Not yet modelled" state rather than pretending the 3D model covers the fleet.
- **The medal claim is no longer laundered.** The site states what the team says *and* what the scraped record independently shows, and lets the reader see the gap.
- **Road-to-final progressions** give the two Nationals boats an actual shape — 6:28.31 2nd, 7:00.06 2nd, 6:44.62 3rd — instead of a single result number.

That cluster is a project checking itself against its own sources and publishing the discrepancy. It is the strongest authorship signal in four rounds.

**Remaining sag.** The apparatus content, now that it exists, is **54% restatement**. Tokenising each `dd` against the prose in its own row: 21 of 39 pairs are ≥50% contained in the paragraph beside them. "Boat class / Fours" sits next to "rowing fours". "Rivals / Rindge Technical, Browne & Nichols" sits next to "against Rindge Technical School and Browne & Nichols". The genuinely additive 46% — Crimson publication dates, "Half a mile", "The Pilot and Fundamental programs", "None, for 49 years", the 1922 finishing order — is exactly what round 2 asked for and proves the research supports the rest.

---

## 6. AI-SLOP RESISTANCE — 9.0 (was 8.5, recovering round 3's loss)

| Tell | R2 | R3 | **R4** | Note |
|---|---|---|---|---|
| Purple/indigo, glass, Inter, icon tiles | No | No | **No** | Palette discipline holds four rounds running |
| Oversized meaningless stats | No | Borderline | **No** | `.progression` now 417/580/363/363 with "50" at 96px against 72px. A progression that progresses. |
| Content repeated rather than composed | No | **Yes** | **No** | 0 duplicate blocks by 5-gram scan |
| Padding to fill a container | No | **Yes** | **No** | Leader rule deleted; no border, no right-align |
| Claims outrunning sources | No | No | **No** — improved | Medal claim, boat name and fleet state all now say what is known vs. what is asserted |

Both tells that fired in round 3 are cleared, and the round's content work actively strengthens the category. A generator does not rename an object because the long form appeared in no primary source, and it does not publish the delta between what a team claims and what the record shows.

The drag is `.facts` capped at half its track — not slop exactly, but the kind of unexamined leftover that reads as nobody having looked at the finished page on a wide screen.

---

## THE SINGLE MOST DAMAGING WEAKNESS

> **The apparatus column, fourth round running — but for the first time the content is not the problem. 37 sourced pairs averaging 201 characters are compressed into 512px of a 992px track by `.facts { max-width: 32rem }`, measuring 10.2% ink where the prose beside it measures 38.5%, under 554px of rule that still points at nothing.**

Round 1: the track doesn't exist. Round 2: the track exists and is empty. Round 3: the track is empty and has a rule drawn across the emptiness so it measures as full. **Round 4: the track has real content and a `max-width` that keeps half of it empty anyway.**

This is now a one-line problem. The 30 sentences round 3 said had to be written have been written — they are sitting in `src/data/team.js` with Harvard Crimson datelines. They are being displayed in half the space allotted to them. Every prior round could honestly say the fix required research; this one cannot.

---

## NEW REGRESSIONS

**1. 390px horizontal overflow, caused by the apparatus rewrite.** *(layout, moderate)*
`docW 446 vs innerW 390` — 56px. `.facts`' two-column grid inside a 242px `.tl-aside` produces `dd` boxes of 63px and 36px; `dl.facts` self-overflows 21–48px on multiple rows, propagating up through `.tl-item` → `.timeline` → `.wrap` → `main` → `body`. Round 3 fixed the heat diagram's 602px overflow and the same round introduced a new one in the component it was rewriting.

*Noted in fairness:* a concurrent commit (`8409b7d`, "Fix the 390px horizontal overflow properly") landed **during this review**, adding `min-width: 0` to grid/flex children and stacking `.facts` to one column below 40rem. Rebuilt and remeasured: **docW 390 == innerW 390**, residual self-overflow 3px on `.bar-year`. The fix is correct and works. It is not in the commit under review, so the item is scored as MISSED, but it should not be re-fixed.

**2. `.boat-state` at 3.25:1 — fails AA, in new markup.** *(typography/colour, minor but telling)*
"Not yet modelled" ×2 at `--grey-2`. Rounds 2 and 3 removed this exact value from `.src`, `.bar-year`, `.lane` and `.school` across 88 elements. The fleet roster shipped with it back. One line.

**3. `.facts` capped at 32rem inside a 992px track.** *(layout — the headline item, counted above, not double-counted in scoring)*

**Still open from earlier rounds:** `--river` / `--river-lit` unused, fourth round. 22 of 55 reveals undifferentiated. Site is 100% JS-dependent below the hero — with scripts off, the timeline, chart, results, chips, fleet and the entire apparatus column render as nothing.

---

## PRIORITIZED FIX LIST

### P0 — blocking Site of the Day

**1. Let the apparatus column occupy the track it was given.**
`styles.css:959`: `.facts { max-width: 32rem }` → `max-width: none` (the track is already `minmax(0, 1fr)` and capped by `.wrap`). Widen `grid-template-columns` to `minmax(0, max-content) minmax(0, 1fr)` across the full 992px. Target **≥25% glyph density** (currently 10.2%) and rule overhang **<200px** (currently 554px). Re-verify with `tools/measure_r4b.py` — check ink *area*, not horizontal extent. This is the single highest-value change on the site and it is one declaration.

**2. `.boat-state` — `var(--grey-2)` → `var(--grey)`.**
3.25:1 → 6.22:1 on two elements. The same substitution already applied four times elsewhere.

### P1 — high

**3. Keep the 390px overflow fix and add a regression check.**
`8409b7d` resolves it (docW 390 == innerW 390 verified). Add `docW === innerW` at 390/768/1024 to whatever gets run before the next round — this is the third consecutive round with a mobile overflow bug from a different cause.

**4. Stop the closing argument being the widest measure.**
`.narrow--flush p` runs **77 CPL**, `.tl-body p` **75 CPL**, both above the 68ch ceiling. Either drop `.narrow--flush` to ~30rem, or raise its type to 20px so 576px yields ~65 characters. Verify by counting characters in trimmed rendered lines, not with a canvas average — the two methods disagree by up to 10 CPL and the canvas one flattered this block last round.

### P2 — polish

**5. Rewrite the 21 restating pairs.**
54% of `dd` values are ≥50% contained in the prose beside them. The additive 46% shows the research supports better. Replace "Boat class / Fours" and "Rivals / Rindge Technical, Browne & Nichols" — both verbatim from the adjacent sentence — with facts the paragraph does not already carry: crew names, lane draws, margins, the other finishers.

**6. Give the remaining 22 reveals a reason to move.** Unchanged for three rounds at 22/55.

**7. Use `--river` / `--river-lit`, or delete them.** Fourth round declared and unused.

**8. Consider server-rendering the timeline.** With JS off the site is a hero and 5,389 characters. The apparatus column — the thing four rounds of critique have been about — does not exist without JavaScript.

---

## IS THE REMAINING GAP CRAFT OR CONTENT?

**Craft. For the first time in four rounds, it is craft.**

Rounds 2 and 3 both concluded the gap was writing — that no `grid-template-columns` value would fix a column with nothing to say. That was correct then and it has been answered. The archival detail exists: 37 pairs, Crimson datelines, distances, margins, finishing orders, plus a boat rename and a medal claim that were checked against primary sources and published honestly.

What is left is:

- one `max-width` keeping that content in half its track *(fix #1)*
- one colour value *(fix #2)*
- one type size *(fix #4)*
- a mobile overflow already fixed in a commit that landed during this review *(fix #3)*

That is an afternoon, and it is worth roughly a full point — the apparatus column alone is holding Layout at 6.8 and has been the top-line item in all four reviews.

The honest residual content gap is smaller and specific: **21 pairs that restate their own paragraph.** Not 30 sentences of new research — a rewrite of half a column using material already scraped.

**Is it Site of the Day? No — not at 7.9, not with 10.2% density in the column the site's credibility rests on, and not shipping a horizontal scrollbar at 390px.** But this is the first round where I can say precisely what the remaining distance is, it is measured in CSS declarations rather than research hours, and nothing on the list requires a new idea.

---

## CLOSING

Nine of thirteen items landed. The duplication is gone and verified three ways. The stair-step is gone at every viewport, exactly. The stagger animates and I watched it do so frame by frame. The 2020 label has its 26px. `.lane` is finally fixed. The progression progresses. The hero survives with JavaScript off. And four content decisions arrived unbidden that no generator makes — renaming the boat because the source didn't support the name, and printing the gap between what the team claims and what the record proves.

Round 3 ended: "write the column, and the next round is a different conversation." The column got written. It is being displayed at 10.2% ink in a 992px track because a `max-width: 32rem` from an older, narrower layout was never revisited — and the fill claim was measured horizontally again, which is the third round running that a percentage has been reported against extent instead of area.

**7.9 / 10 — Honorable Mention.** Remove one `max-width`, change one colour, and remeasure by area. That is the distance now.
