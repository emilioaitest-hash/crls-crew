# CRLS Rowing — Design Critique, Round 3

**Judged against:** Awwwards Site of the Day (the real bar)
**Reviewed at:** 2560×1440, 1600×900, 390×844 — live build served from `dist/` via `vite preview`, measured over CDP
**Source read:** `index.html`, `src/styles.css`, `src/main.js`, `src/data/team.js`
**Prior reviews:** `01-design.md` — 6.2 / 10, REJECTED · `05-design-round2.md` — 7.4 / 10, Honorable Mention

Every number below was measured on the running build at `http://localhost:4188/crls-crew/` (`location.href` confirmed on each pass — no stale tabs).

---

## VERDICT

**Overall: 7.6 / 10 — HONORABLE MENTION.** Still not Site of the Day.

Round 2 said the difference between 7.4 and Site of the Day was *writing*, not CSS. Round 3's answer was to write 24 key/value pairs and then spend the rest of the budget on CSS anyway. The score moves +0.2.

Three of the ten items landed cleanly. The footer regression is genuinely fixed — footer and section wrap now agree to the pixel at all three viewports. The measure is unified. The revival got its band.

But the headline claim does not survive measurement. **The claim is "fill went 9–49% → ~94%." The 94% figure is measuring a dotted leader rule, not text.** `.facts dd` carries `border-bottom` and `text-align: right`, so every `dd` box spans the full 393px column regardless of how short the value is. "Charles" is 59px of text in a 364px box — 305px of that "fill" is an underline. Measured by actual glyph area, the apparatus column is **14.8% ink against 47.9% in the prose column beside it**, and the mean leader run is **245px of empty rule per row**. The dead column was not filled. It was underlined.

And the fix list introduced three new defects, one of them the most embarrassing kind: **the 2000 timeline row and the new revival band now tell the same story twice, 288px apart, using the same headline words and the same four numbers.**

---

## SCORES

| # | Category | R1 | R2 | **R3** | Δ (R2→R3) |
|---|---|---|---|---|---|
| 1 | Typography | 7.0 | 8.0 | **8.0** | — |
| 2 | Layout | 4.0 | 6.0 | **6.5** | +0.5 |
| 3 | Colour & Light | 8.0 | 8.0 | **8.0** | — |
| 4 | Motion | 5.5 | 6.5 | **6.5** | — |
| 5 | Narrative | 7.0 | 8.5 | **8.0** | **−0.5** |
| 6 | AI-Slop Resistance | 8.5 | 9.0 | **8.5** | **−0.5** |
| | **Overall** | **6.2** | **7.4** | **7.6** | **+0.2** |

Two categories went **down**. That has not happened in either prior round.

---

## DID THE ROUND-2 FIXES LAND?

| # | Fix | Status | Measurement |
|---|---|---|---|
| P0.1 | Write the apparatus column | **PARTIAL — claim does not survive** | `aside` present on 9/9 rows, 24 `dt`/`dd` pairs ✓. But glyph-area density is **14.8% aside vs 47.9% body**; mean leader dead-run **245px** (min 78, max 336). Vertical fill is **45.4% (2000)**, **52.6% (1989)**, 74.6% (1999). The "93.8%" is `dd` box width, not ink. |
| P0.1b | `.timeline` capped at 78rem | **LANDED, but causes a new defect** | `max-width: 1248px` ✓, rule ends at x=1664. **But every other block on the page ends at x=2144** — see New Regression #2. |
| P0.2 | Footer regression | **LANDED** | `display:contents` gone; `.foot-inner` is `display:grid`. 2560px: foot-inner **left 416 / right 2144**, section wrap **left 416 / right 2144** — exact. 1600px: both **64 / 1536**. 390px: both **20 / 370**. |
| P0.3 | `.src` contrast | **LANDED** | 23 elements, **5.66–6.22:1**, 0 fail AA (was 3.25:1). |
| P0.3 | `.bar-year` contrast | **LANDED** | 20 elements, **6.22–14.89:1**, 0 fail AA. |
| P0.3 | `.school` contrast | **LANDED** | 21 elements, **5.15–14.89:1**, 0 fail AA. |
| P0.3 | `.facts dt` contrast | **LANDED** | 24 elements at **6.22:1**. |
| P0.3 | **`.lane` contrast** | **MISSED** | `styles.css:508` **still `color: var(--grey-2)`**. 8 of 14 lanes measure **2.96:1** — fails AA. This was named explicitly in round 2's P0.3 alongside the three that were fixed. |
| P0.3 | `.silence-count` | **PARTIAL** | `#3f4a55`, measured **2.17:1** (claim said ~2.2, round 2 asked for ~2.6). Better than 1.25:1, still below the 2.5–3:1 target. |
| P1.5 | `.narrow--flush` class | **PARTIAL** | Inline `margin-inline` count is **0** ✓, class exists ✓. But at 44rem the closing prose now runs **704px / 79 characters** — the widest measure on the site, in the section that was *just* narrowed elsewhere for being too wide. Traded one defect for its opposite. |
| P2.6 | `.split` 44rem → 36rem | **LANDED** | `max-width: 576px`; `.lead` measures **48 CPL**, `.tl-body` **61 CPL**. Both inside 45–68ch. |
| P2.7 | `.boat-stage` 32:9 | **LANDED** | `aspect-ratio: 32/9`, measured **1728×486 = 3.56**. |
| P2.8 | Motion — school stagger | **MISSED (no-op)** | `.school` delays are correctly `0 / 28 / 56 / 84ms…` — but `.school` **`transition-duration` is `0s`** and `.school` is not a reveal target (`schoolIsReveal: false`); only the `#field` parent reveals. A delay on a zero-duration transition animates nothing. Chips still arrive as one block. |
| P2.8 | Motion — 0.95s curve | **LANDED** | `.hinge-line`, `.hinge-line--minor`, `.thesis .amount`, `.quote` = **0.95s cubic-bezier(.16,1,.3,1)**. 4 elements. |
| P2.9 | 2020 on the bar | **PARTIAL** | `.bar-none` renders on the 2020 column ✓, legend entry removed ✓, 6.22:1 ✓. But it is **10px rotated vertical type in a 16px-wide box**, and the label's bottom sits at y=14063 with `.bar-year` starting at y=14064 — **0px of separation**, so "No season" collides visually with "2020". |
| P2.10 | Stage the revival | **PARTIAL — creates a duplication** | `.hinge--minor` band exists at `--ink-2`, 12/50/5/5 in `--dawn` ✓, replaced the 394px quote section ✓ (`.quote` count now 1). **But the 2000 timeline row was never removed**, so the same headline and the same four numbers appear twice, 288px apart. |

**Score: 7 landed, 6 partial, 2 missed, plus 3 new regressions.**

Round 2 was 5 landed / 6 partial / 0 missed / 1 regression. The miss-and-regression count went **up**.

---

## 1. TYPOGRAPHY — 8.0 (unchanged)

Real gains, cancelled by a real loss.

**Gained.** The contrast sweep is the most disciplined work in this round. `.src` (23 elements), `.bar-year` (20), `.school` (21) and `.facts dt` (24) all moved from 3.25:1 to 5.15–6.22:1. That is 88 elements of previously-failing text now passing AA, and it was the correct fix applied consistently. `.split` at 36rem finally unifies the measure: 48 CPL for `.lead`, 61 CPL for `.tl-body`, 33 CPL for `.note` — the three-measure problem round 1 opened with is closed.

**Lost.** `.narrow--flush` at 44rem sets the site's **closing argument** — the paragraph that carries "$0 to row" — at **79 characters**, the widest measure on the page. The same round that narrowed `.split` from 78ch to 48ch widened this block to 79ch. Two fixes in one commit pulling in opposite directions is not a unified type system; it is two people editing a stylesheet.

`.facts` is typographically weak in a way the numbers hide. Right-aligned `dd` with a `border-bottom` produces a **restaurant-menu leader** — `Charles` sits 305px away from its own label with a rule between them. At 12px mono, across 24 pairs, the eye has to traverse a third of a metre of empty underline to connect key to value. A left-aligned two-column list at `minmax(auto, max-content)` would read better and measure honestly.

---

## 2. LAYOUT — 6.5 (was 6.0)

Half a point. The footer fix is worth it; the apparatus non-fix and a new misalignment cap it.

**What landed.** The footer is correct at every viewport tested — 416/2144, 64/1536, 20/370, matching the section wrap exactly. Round 2's regression is gone and gone properly, with a real class rather than another inline override. Inline `margin-inline` overrides are now **0** across the document, closing an item that had been open since round 1.

**Why it is still a 6.5.** The apparatus column is the same failure round 2 named, wearing a rule instead of admitting it is empty:

| Measure | R2 | R3 |
|---|---|---|
| Aside glyph density | (not measured) | **14.8%** |
| Body glyph density | — | **47.9%** |
| Mean leader dead-run per `dd` | — | **245px** |
| Vertical fill, 2000 row | — | **45.4%** |
| Vertical fill, 1989 row | — | **52.6%** |

The prose column carries **3.2× the ink density** of the apparatus column beside it. On the 2000 row the aside uses 129px of a 285px track and stops; the rule keeps going. Round 2 asked for "the rival school's name, the boat class raced, the finishing margin, the newspaper the result came from" — concrete research already scraped. What shipped is `['Conditions', 'Rain']` and `['Stretch', 'Powerhouse']`: two-word restatements of the prose next to them, padded to width by a border.

**New misalignment (see regressions).** Capping `.timeline` at 78rem fixed the rule-overhang problem locally and broke the page's vertical alignment globally: the timeline now ends at **x=1664** while `.split`, `.progression`, `#chart`, `.boat-stage`, `.heat`, `#field` and the footer all end at **x=2144**. A **480px stair-step** in the right margin, twice, in the two longest sections.

`.split` dead space is unchanged from round 2 — `#river` 439px, `#then` 443px, `#record` 437px, `#now` 471px, `#free` 510px. Content width at 2560px holds at **67.5%**.

---

## 3. COLOUR & LIGHT — 8.0 (unchanged)

`.silence-count` moved 1.25:1 → **2.17:1**. That is real progress from "invisible" to "faint," and the transition on `color` is a nice touch. But round 2 asked for ~2.6:1 and the delivered value undershoots its own stated target (~2.2 claimed, 2.17 measured). At 128px it now reads as a very dark numeral rather than a rendering fault — improvement, not resolution.

Against that, **`.lane` was left at `--grey-2`, 2.96:1, on the heat diagram** — the single best piece of information design on the site, the one a juror screenshots. Eight of the fourteen lanes in it are the "Private" labels, and they are the comparison the whole argument rests on. Fixing the contrast of the chart axis and the school chips while leaving the hinge diagram's own labels failing is precisely backwards.

`--river` / `--river-lit` remain declared and unused outside the WebGL rim light. Third round running.

---

## 4. MOTION — 6.5 (unchanged)

The 0.95s curve landed on exactly the right four elements — `.hinge-line`, `.hinge-line--minor`, `.thesis .amount`, `.quote`. That is the "reserve the long duration for the moments the story turns on" note, executed correctly.

The stagger did not land at all. `.school` carries `transition-delay: calc(var(--i) * 28ms)` and the `--i` values are correctly emitted (0, 28, 56, 84, 112, 140ms…), but **`.school` has `transition-duration: 0s`** and no `data-reveal`, so nothing transitions. The chips still appear as one block when `#field` reveals. This is a CSS-only fix with no observable effect — structurally the same error round 2 caught on the apparatus column, in a different file.

**21 of 53 reveal elements still share `0.55s` at `0s` delay.** Round 2 measured 35 of 50 undifferentiated; the improvement is real but modest, and it came from the `.result`/`.tl-item`/`.bar-col` staggers that already existed.

---

## 5. NARRATIVE — 8.0 (was 8.5) ← **down**

The first regression in narrative across three rounds, and it is self-inflicted.

The revival band itself is good. `2000 · THE PROGRAM RESTARTS` in `--dawn`, "Twelve students, / *no equipment*" with the negation in accent, four numbers as a bordered progression, a closing lead about two boats at nationals. It is a legitimate second staged moment and it does what round 2 asked at the right smaller scale.

**But the 2000 timeline row it was supposed to replace is still there, 288px above it.**

| | Timeline row (y=10463) | Revival band (y=10751) |
|---|---|---|
| Heading | "Twelve students and no equipment" | "Twelve students, no equipment" |
| Numbers | "twelve students… fifty kids, five boats, five races" | 12 · 50 · 5 · 5 |
| Aside | `Started with 12 students / By March 50 rowers / Boats 5` | — |

The same sentence, the same four figures, three times within 300 vertical pixels — twice in the row (prose and aside) and again in the band. `main.js:354` filters the 1929 hinge out of the timeline (`isHinge = h.pull && h.year === '1929'`) precisely so it is not duplicated; the identical filter was not extended to the 2000 entry when the second band was built. The pattern for the fix exists in the same function, six lines up.

A juror does not diagnose this as a missed filter. They read it as a site that repeats itself — which undercuts the one quality this project has been trading on since round 1: that a person did the research and made the decisions.

The 1929 hinge remains the best thing on the site and is untouched. The 165vh silence still works.

---

## 6. AI-SLOP RESISTANCE — 8.5 (was 9.0) ← **down**

Half a point off, for two specific tells that were not firing in round 2.

| Tell | R2 | R3 | Note |
|---|---|---|---|
| Purple/indigo, glass, Inter, icon tiles | No | **No** | Palette discipline holds absolutely |
| Oversized meaningless stats | No | **Borderline** | `12 / 50 / 5 / 5` in a **four-up bordered grid of equal cells** is the single most generic component shape on the web. The numbers are real and sourced; the container is a stat-card row. `.progression` uses `repeat(4, 1fr)` — 430.75px × 4 — which renders "5 boats" and "5 races" at identical visual weight to "50 rowers," flattening the progression it is named for. A real progression would scale or step. |
| Content repeated rather than composed | No | **Yes** | The 2000 duplication above. Saying the same thing twice at two scales, 288px apart, is what a generator does when it cannot tell that two blocks describe one event. |
| Padding to fill a container | No | **Yes** | 245px mean leader rules turning a 2-word value into a full-width row is decoration standing in for content — the exact substitution round 2 flagged and this round formalised in CSS. |

Everything else still reads No, and the stylesheet comments remain a genuine designer's file — the new ones explain *why* `--grey-2` fails and *why* 32:9 matches the object. That is still not slop. But three rounds in, the tells are moving in the wrong direction for the first time.

---

## THE SINGLE MOST DAMAGING WEAKNESS

> **The apparatus column still has nothing to say, and this round taught it to hide that with a 245px underline. 14.8% glyph density against 47.9% in the column beside it — the dead space round 1 diagnosed and round 2 renamed is now decorated.**

This is the third consecutive round in which this exact column is the top item. Round 1: the track doesn't exist. Round 2: the track exists and is empty. Round 3: the track is empty and has a rule drawn across the emptiness so it measures as full.

The reason it keeps failing is that it keeps being treated as a layout problem. It is not. There are **1,321 scraped races** in this project and the apparatus column for 1889 says `['River', 'Charles']`. The research to fill it exists — round 2 named it precisely: rival school, boat class, finishing margin, source publication. Until somebody writes four real facts per row, no `grid-template-columns` value will fix this, and the site will keep scoring 6.5 on layout.

---

## NEW REGRESSIONS

Round 2 found a footer regression introduced by a round-1 fix. Round 3 finds **three**, all in code touched this round.

**1. Content duplication at the revival — introduced by P2.10.** *(narrative, severe)*
The 2000 `HISTORY` entry renders as a timeline row **and** as the new `.hinge--minor` band, 288px apart, with the same headline and the same 12/50/5/5. `main.js:354` filters the 1929 duplicate; the 2000 duplicate was not added to that filter.

**2. 480px right-edge stair-step — introduced by P0.1's `.timeline { max-width: 78rem }`.** *(layout, moderate)*
`.timeline` ends at x=1664; `.split`, `#chart`, `.progression`, `.boat-stage`, `.heat`, `#field` and `.foot-inner` all end at x=2144. Fixing the rule-overhang inside the timeline broke the timeline's agreement with every other block on the page. Visible as a hard 480px jog in the right margin entering and leaving both `#then` and `#return`.

**3. Closing measure widened to 79 CPL — introduced by P1.5's `.narrow--flush { width: 44rem }`.** *(typography, minor)*
The same commit that narrowed `.split` to 36rem/48 CPL set the site's closing argument to 44rem/79 CPL. Round 2 explicitly asked for 44rem, so this is a fix that was specified wrong and implemented faithfully — but it ships as the widest measure on the site.

**Also still open from round 2, not a new regression but not fixed either:** `.lane` at 2.96:1 was named in round 2's P0.3 in the same sentence as `.src`, `.bar-year` and `.school`. Three of the four were fixed. Mobile still overflows — `docW 602` in a `390` viewport, from `.heat-row`'s `grid-template-columns: 9rem 1fr` with eight flex lanes; this is pre-existing (`.heat` is untouched since the first commit), not new, but it means the **390px experience has a horizontal scrollbar and 212px of the heat diagram off-screen**, and no round has caught it until now.

---

## PRIORITIZED FIX LIST

### P0 — blocking Site of the Day

**1. Delete the duplicate 2000 timeline row.** *(30 seconds, and it is embarrassing until it is done)*
`main.js:354`: `const isHinge = (h) => h.pull && (h.year === '1929' || h.year === '2000');`
The filter already exists for 1929. Extend it. Verify `#return .tl-item:last-child` becomes the 1999 row.

**2. Write the apparatus column for real — or collapse it. Third and final time.**
Not `['Conditions', 'Rain']`. Per round 2's spec, from research already in `research/`: **rival school, boat class, finishing margin, source publication, race distance**. Target ≥35% glyph density (currently 14.8%) and ≥75% vertical fill on every row (currently 45% on two).
Then **remove `border-bottom` from `.facts dd` and left-align it** — `grid-template-columns: max-content max-content` with a `1.5rem` gap. That kills the 245px leader. If the honest answer is that only four rows have four real facts, then collapse the track on the other five with `.tl-item--bare { grid-template-columns: 6rem minmax(0, 34rem) }` and let the rule stop where the content stops.

**3. Fix `.lane` contrast — the one that was missed.**
`styles.css:508`: `color: var(--grey-2)` → `var(--grey)`. 2.96:1 → 6.22:1, on the eight "Private" labels in the site's best diagram. One line, and it was already on round 2's list.

### P1 — high

**4. Resolve the 480px right-edge stair-step.**
Either drop `.timeline { max-width: 78rem }` and widen the aside track to `minmax(0, 1fr)` once it has real content (preferred — fix #2 makes this free), or apply the same 78rem cap to `.split` so the two long sections agree with each other. Do not ship a page where the timeline and the chart end 480px apart.

**5. Make the school-chip stagger actually animate.**
`.school` has a 28ms delay on a `0s` transition. Give `.school` `transition: opacity .55s var(--ease), transform .55s var(--ease)` and either a `data-reveal` per chip or an `.in` cascade from the `#field` parent. Verify by measuring `transitionDuration !== '0s'`, not by reading the CSS.

**6. Separate "No season" from the 2020 axis label.**
`.bar-none` bottom = 14063, `.bar-year` top = 14064. Raise `bottom` from `2.6rem` to ~`4rem`, or move the annotation above the bar. Currently two pieces of rotated 10px mono touch.

### P2 — polish

**7. `.narrow--flush` 44rem → 36rem.** 79 CPL → ~62, matching the `.split` fix shipped in the same commit.

**8. `.silence-count` to ~2.6:1.** `#3f4a55` measures 2.17:1, short of both round 2's target and this round's own claim. `#47535f` gets there.

**9. Make `.progression` a progression, not four equal cards.** `repeat(4, 1fr)` renders 12, 50, 5 and 5 at identical weight. Scale the cells (`2fr 3fr 1fr 1fr`) or scale the numerals so 50 dominates. As four equal bordered boxes it is the most template-shaped component on the site.

**10. Fix the 390px horizontal overflow.** `docW 602` vs `innerW 390`. Below 40rem, give `.heat-row` `grid-template-columns: 1fr` with the label above, and let `.lanes` wrap. Pre-existing, but it is a broken mobile experience on the site's signature diagram and no round has fixed it.

---

## IS THE REMAINING GAP CRAFT OR CONTENT?

**Content — and specifically writing, not photography.**

The craft gap is now small and cheap. Items 1, 3, 5, 6, 7 and 8 above are collectively about **two hours** of work: one filter condition, four colour values, one transition declaration, one offset. Item 4 is an afternoon. None of it requires a new idea.

What separates this site from Site of the Day is the same thing it was in round 2, stated more plainly: **the apparatus column needs roughly 30 sentences of real archival detail that nobody has written yet.** The project scraped 1,321 races and produced a `dd` that says "Rain." The research directory has the material; the data file has two-word placeholders. That is a writing task, and this round demonstrated that it cannot be solved by styling — the attempt to style it produced a 245px leader rule that made the numbers look better and the page look worse.

Photography is *not* the gap. The existing images are used well and credited properly.

The second content gap is smaller but real: `#return` and `#free` still have no staged moment of their own now that the revival band duplicates rather than replaces. Once the duplicate row is deleted, the band becomes the genuine second moment round 2 asked for, and narrative goes back to 8.5 on its own.

---

## CLOSING

The footer is fixed properly. 88 elements of failing text now pass AA. The measure is unified, the inline overrides are finally gone, the boat stage matches its object, and the site has a second banded moment. Those are real, and they are why the score moved up rather than down.

But this round claimed a 94% fill that measures 14.8% in ink, shipped a stagger that animates nothing, left one of the four named contrast fixes undone, broke the page's right edge in two places, and printed the same paragraph twice within one screen. Round 2 caught a fix that was CSS-only with no content written. **Round 3 contains two more of exactly that, plus a duplication that a single `||` in an existing filter would have prevented.**

The gap to Site of the Day has not been craft since round 2, and it is not craft now. It is roughly 30 sentences that have to be written by someone who has read the archive. Everything else on this page is an afternoon.

**7.6 / 10 — Honorable Mention.** Delete the duplicate row today. Then write the column, and the next round is a different conversation.
