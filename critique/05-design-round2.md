# CRLS Rowing — Design Critique, Round 2

**Judged against:** Awwwards Site of the Day (the real bar)
**Reviewed at:** 2560px, 1600px, 390px — live build served from `dist/` via `vite preview`
**Source read:** `index.html`, `src/styles.css`, `src/main.js`
**Prior review:** `01-design.md` — 6.2 / 10, REJECTED

---

## VERDICT

**Overall: 7.4 / 10 — HONORABLE MENTION.** Not Site of the Day.

Round 1 said the site would jump roughly two points if the grid were fixed. It jumped 1.2. That gap is the story of this round.

The two narrative fixes are genuinely excellent. The 1929 hinge is now the best thing on the site — a full-bleed `--ink-2` band, 104px display type, the orange/grey heat diagram staged beneath it at full width. It does exactly what round 1 asked and it works. The sixty-year silence is 165vh of near-empty ink with a rule that fills as you fall through it. Those are real compositional ideas, and no template generator produces either of them.

The layout fix is where the honesty has to come in. The third track was added to `.tl-item` — the CSS is correct and the mechanism is right. But **the content to fill it was never written.** Five of the nine timeline rows put a 64px `Source ↗` link into a 736px track. The dead right column was not eliminated; it was renamed. And the site picked up a new regression on the way — the footer now ignores the page gutter entirely and runs flush to both viewport edges.

This is a much better site than the one reviewed in round 1. It is not yet a winning one.

---

## SCORES

| # | Category | R1 | R2 | Δ |
|---|---|---|---|---|
| 1 | Typography | 7.0 | **8.0** | +1.0 |
| 2 | Layout | 4.0 | **6.0** | +2.0 |
| 3 | Colour & Light | 8.0 | **8.0** | — |
| 4 | Motion | 5.5 | **6.5** | +1.0 |
| 5 | Narrative | 7.0 | **8.5** | +1.5 |
| 6 | AI-Slop Resistance | 8.5 | **9.0** | +0.5 |
| | **Overall** | **6.2** | **7.4** | **+1.2** |

---

## DID THE ROUND-1 FIXES LAND?

| # | Fix | Status | Evidence |
|---|---|---|---|
| P0.1 | `.tl-item` third track | **PARTIAL** | Grid is `6rem / 544px / 992px` at 2560px ✓. But apparatus ink fills 49% of the track on 4 rows and **9% on 5 rows**. Mean dead space per row: **766px** — vs ~690px in round 1. |
| P0.2 | `.wrap` 84rem → 108rem | **LANDED** | 1728px at 2560px viewport = **67.5%** of screen, up from 52%. Exactly as specified. |
| P0.3 | 1929 pulled into a `.hinge` band | **LANDED — best fix on the site** | Full-bleed `--ink-2`, `.hinge-line` at **104px**, heat diagram full width beneath, filtered out of the timeline in `main.js:346`. |
| P1.4 | `.note` legibility | **LANDED** | 13px, `--grey` #8b9299 = **6.22:1**, `max-width: 46ch` → 419px measured. Passes AA. |
| P1.5 | `#gap` at 165vh + fill + counter | **PARTIAL** | 2376px at a 1440px viewport = **165vh exactly** ✓, rule fills 0→100% ✓, counter climbs 1929→1989 ✓. But the counter is `--ink-3` #1e242b on #0a0c0e = **1.25:1 — invisible.** |
| P1.6 | `.h2--climax` + line breaks | **LANDED** | Climax headings 104px vs 60px baseline ✓. `The field<br>they race in` and `The<br>first time around` both corrected in markup ✓. |
| P2.7 | Reveal 0.9s → 0.55s + stagger | **PARTIAL** | Duration is `0.55s, 0.55s` ✓. Stagger reaches **15 of 50** reveal elements (`.tl-item`, `.result`). The other 35 still share one identical gesture. |
| P2.8 | Chart 2020 + year labels | **PARTIAL** | 2020 labelled — but only in the legend, not on the bar. `.bar-year` went 10px → **11px**, still `--grey-2` at **3.25:1**. Fails AA. Early seasons still render 38–47px against 375px maxima. |
| P2.11 | `$0` promoted | **LANDED** | `.hero-stat.is-thesis` in `--dawn` ✓, mid-page `.thesis` callout after the chart at 112px ✓. |
| — | Fleet stage 24:9 | **PARTIAL** | Full-width 1728×648 stage ✓, camera framed by FOV/aspect from hull LOA ✓. But the hull fills ~25% of stage height, and in `fl-quarter3.png` the stern runs to the exact frame edge. |
| P2.9 | Inline `margin-inline:0` overrides | **PARTIAL** | One converted to `auto` (`:249`). **`index.html:375` still carries `style="margin-inline:0"`** — that block measures 544px = **21.3% of a 2560px viewport**. |
| P2.10 | Mobile header clip | **LANDED** | `@media (max-width: 40rem)` hides `#chapter-label`, bar drops to 3.5rem. No horizontal overflow at 390px. |

**Score: 5 landed, 6 partial, 0 missed, plus 1 new regression.**

---

## 1. TYPOGRAPHY — 8.0 (was 7.0)

The single best-executed fix set. `.note` is genuinely readable now: 13px, 6.22:1, capped at 46ch. Scale contrast finally exists — 104px climax headings against a 60px baseline is a real hierarchy, and the hinge line at 104px gives the story a typographic peak that round 1 correctly said was missing. Both orphaned line breaks are fixed in markup rather than left to `text-wrap`.

**Still broken:**

- **`.src` fails AA, 23 times, and P0.1 made it more prominent.** `--grey-2` #5b646d at 12px = **3.25:1**. Round 1 fixed `.note` and left `.src` alone — but the third-column fix *promoted* these links into the apparatus track, where on five of nine rows the `Source ↗` link is the **only** thing in the column. The most-exposed text in the new layout is text that fails contrast. That is an own-goal.
- **Same failure on `.bar-year` (11px, 3.25:1), `.lane` labels, and 18 of 21 `.school` chips.** The palette has a systemic problem: `--grey-2` is used as a body-adjacent colour and it is not one.
- **`.lead` measure still inconsistent.** `.split`'s second child spans `2 / -1` with `max-width: 44rem`, so `.lead` runs **704px at 24px ≈ 78 characters** while `.tl-body` beside it holds 544px. Round 1 flagged this at 685px/76ch. Unchanged.

---

## 2. LAYOUT — 6.0 (was 4.0)

Two points of real movement, and the reason it is not more.

**What worked.** `.wrap` at 108rem puts content at 67.5% of a 2560px screen, up from 52%. Section rhythm now genuinely varies — 1440 / 576 / 1939 / 1036 / 2376 / 1624 / 394 / 1784 / 1420 / 1511 / 1031 — against round 1's flat repetition. The hinge and the silence are full-width compositional events. The site no longer has one idea about putting things on a screen.

**Why it is still a 6.** The third track is structurally present and editorially empty:

| Row content | Aside track | Ink in track | Fill | Dead |
|---|---|---|---|---|
| Source + note (4 rows) | 736px | 360px | 49% | 573px |
| Source only (5 rows) | 736px | 64px | **9%** | **920px** |

Mean dead space per timeline row is **766px** — numerically *worse* than round 1's ~690px, because `.wrap` grew while the content did not. The full-width `border-top` still draws a rule across emptiness on the majority of rows. The diagnosis in round 1 was right; the fix treated it as a CSS problem when it was an editorial one.

`.split` has the same shape: `#river` measures 308px of dead space right of the last glyph.

**New regression — the footer.** `index.html:393` carries `<div class="wrap" style="display:contents">`. That annihilates the wrapper, and `.foot` has no inline padding of its own. Measured at 1600px:

```
footer title left edge:  0px      (every other section: 64px)
footer links right edge: 1600px   (every other section: 1536px)
misalignment:            64px on both sides
```

The last thing a juror sees is the one element on the page that ignores the grid the whole site is built on. At 2560px it runs the full 2560px while content above it stops at 2144px.

**Also outstanding:** `index.html:375` still overrides `margin-inline:0` — 21.3% of viewport width, exactly the defect round 1 named. The boat stage is 1728×648 with the hull occupying roughly a quarter of the height, and the stern touches the right frame edge in the three-quarter view.

---

## 3. COLOUR & LIGHT — 8.0 (unchanged)

Gains and losses cancel.

**Gained:** the `.hinge` band at `--ink-2` is the first genuine tonal event in the scroll — round 1's complaint that 4,400px passed with no change of ground is now answered. The silence rule uses a `--dawn` → `--dawn-lit` gradient, the first time the accent has been used as *light* rather than as a label.

**Lost:** `.silence-count` is `--ink-3` #1e242b on #0a0c0e — **1.25:1**. A 128px number that climbs 1929 → 1989 is the emotional payload of the entire silence section and it is functionally invisible. Setting it near-black was clearly a deliberate "ghost numeral" choice; at 1.25:1 it reads as a rendering fault, not restraint. Around 2.5–3:1 it would read as intended.

`--river` and `--river-lit` remain declared and essentially unused outside the WebGL rim light. The site still defines itself a cold blue mid-tone and never lights anything with it.

---

## 4. MOTION — 6.5 (was 5.5)

0.55s is the right duration and the fast-scroll half-opacity problem is gone. `--i` stagger on `.tl-item` and `.result` at 55ms is correct and reads well. Chart bars cascade at 38ms. The hero's quarter-turn tied to scroll progress is a genuinely good, restrained idea. `prefers-reduced-motion` is handled thoroughly — every counter, bar and reveal has an explicit reduced path, and the scroll layer has a failure fallback that shows everything rather than stranding the page.

**Why not higher:** 35 of 50 reveal elements still share one undifferentiated fade. The stagger reached the two list-like components and stopped. Motion still announces that a scroll tick fired rather than arguing for what arrived. The hinge — the site's climax — gets the same 0.55s fade as a footnote.

---

## 5. NARRATIVE — 8.5 (was 7.0)

The biggest gain, and it is deserved.

The 1929 hinge is now staged as the argument it always was: date line in `--dawn`, "The eights were separated. / *The fours were not.*" at 104px with the negation in accent, and the heat diagram directly beneath at full width showing four public lanes, four private lanes, then the mixed six-lane final with `Cambridge` filled solid orange. The information design carries the thesis without a caption. This is the piece of the site a juror would screenshot.

The silence works structurally — 165vh of near-nothing between two dated marks is the correct answer to "sixty years of nothing," and falling through it takes real time. The counter would complete it if you could see it.

`$0` now appears three times at three scales: hero stat in accent, 112px mid-page thesis after the chart, and the `#free` argument. The reader carries the thesis instead of meeting it at 12,700px.

**Remaining sag:** `#return` is still six undifferentiated timeline rows with no staged moment of its own — the 1989 revival ("Twelve students, no equipment. By March: fifty kids, five boats") is a better story than its presentation. It gets a pull-quote in a separate 394px section rather than a composition.

---

## 6. AI-SLOP RESISTANCE — 9.0 (was 8.5)

Nothing regressed and two things improved. The hinge band and the 165vh silence are structurally specific to *this* story — they cannot be lifted to another subject, which is the strongest available evidence of authorship. Every tell from round 1 still reads **No**. The stylesheet comments now document reasoning rather than decoration (why the kicker light was desaturated, why reveal is driven from the scroll tick rather than IntersectionObserver under Lenis, why the mask uses line-height 1). That is a real designer's file.

The round-1 "composition mismatched to content" partial is now **mostly resolved** — a 20-year chart and a 24:1 hull finally get full-width stages.

---

## THE SINGLE MOST DAMAGING WEAKNESS

> **The apparatus column is architecture without content. Five of nine timeline rows place a 64px `Source ↗` link — which itself fails AA at 3.25:1 — into a 736px track, leaving a mean 766px of dead space beneath a full-width rule.**

Round 1's most damaging weakness was a CSS mismatch. Round 2's is an editorial one, and it is harder: the grid now *has* the right shape, and the page has nothing to put in it. The site widened the container and added a track, then filled that track with the one text style on the page that a juror cannot read.

This is what separates 7.4 from 8.5. Everything else on the list below is an afternoon's work; this one requires writing.

---

## PRIORITIZED FIX LIST

### P0 — blocking Site of the Day

**1. `#then` / `#return` — write the apparatus column, or collapse it.**
`main.js:328–341`, the `item()` template. Five of nine rows emit only `<a class="src">Source</a>` into a 736px track. Two options, and you must pick one:
- **Fill it (preferred).** Add an `aside` field to each `HISTORY` entry in `src/data/team.js` and render it in `.tl-aside`: the rival school's name, the boat class raced, the finishing margin, the newspaper the result came from. You already scraped this. Four to six rows of `.spec-table`-style key/value mono at 13px would fill the track at ~60% and turn the rule into a real edge.
- **Collapse it.** If there is genuinely nothing to say, change `main.js` to add a `.tl-item--bare` class on rows without a note, and in `styles.css:421` give that modifier `grid-template-columns: 6rem minmax(0, 34rem)` with `border-top-width: 0 0 0 auto` so the rule stops where the content stops.
Do not ship the current state, where the rule spans 1728px and the content spans 808px.

**2. `index.html:393` — delete `style="display:contents"` from the footer wrap.**
This is a regression, not a round-1 leftover. It removes the footer from the page grid entirely: footer content sits at x=0 while every section above it starts at x=64 (1600px) or x=416 (2560px). Replace with `<div class="wrap">` and move `display: grid; grid-template-columns: 1fr auto` from `.foot` onto that wrap so the two-column footer layout survives.

**3. `.src` — fix contrast on 23 elements.**
`styles.css:203`: `color: var(--grey-2)` → `var(--grey)`. That takes 3.25:1 → 6.22:1, matching the `.note` fix already shipped. This is one line and it is now the most-exposed text in the new timeline layout. Apply the same substitution to `.bar-year` (`:543`), `.lane` (`:491`), and `.school` (`:731`).

### P1 — high

**4. `.silence-count` — make the counter visible.**
`styles.css:867`: `color: var(--ink-3)` (#1e242b, **1.25:1**) → `#3a444e` (~2.6:1) or `--grey-2` (3.25:1). A 128px numeral climbing 1929→1989 is the payload of a 2,376px section; at present the section reads as an accidental blank. Consider also raising it from `clamp(3rem, 9vw, 8rem)` to fill more of the empty right half, and adding `--dawn` to the final `1989` state so arriving somewhere is marked.

**5. `index.html:375` — remove the last `margin-inline:0` override.**
Round 1's item #9, still outstanding. That block measures 544px = 21.3% of a 2560px viewport. Replace the inline style with a real `.narrow--flush` modifier class in the stylesheet, and widen it to `44rem` so the closing argument is not the narrowest column on the page.

### P2 — polish

**6. `.split` — unify the measure.**
`styles.css:128`: `.split > :nth-child(2):last-child { max-width: 44rem }` lets `.lead` run 704px ≈ 78 characters while `.tl-body` beside it holds 544px. Drop to `36rem` so every prose column on the site sits between 60–68 characters.

**7. `.boat-stage` — close the vertical gap.**
The stage is 1728×648 and the hull occupies roughly a quarter of that height; the three-quarter view also runs the stern to the exact right frame edge. In `main.js:261`, raise the quarter-view pad from `1.02` to ~`1.10` to clear the crop, and reduce `.boat-stage` to `aspect-ratio: 32/9` at `min-width: 60rem` so the frame matches the object rather than boxing it in empty ground.

**8. Motion — extend the stagger past two components.**
35 of 50 reveal elements still fade identically. Add `--i` staggering to `.school` chips in `#free` (they are a list and should arrive as one) and give `.hinge-line` and `.thesis .amount` a slower, separate 0.9s curve. Reserve the long duration for the three moments the story turns on.

**9. `#record` chart — annotate 2020 on the bar, not in the legend.**
The "2020 — no season" note lives in `.chart-key` where nobody connects it to the 6px sliver. Put a rotated `NO SEASON` label directly on the 2020 column. The 2007–2014 seasons still render 38–47px against a 375px maximum — a secondary win-*rate* line over the raw-count bars would make eight of twenty seasons legible instead of decorative.

**10. `#return` — stage the 1989 revival.**
The one remaining flat stretch. "Twelve students, no equipment. By March: fifty kids, five boats, five races" is currently a pull-quote in an unnamed 394px section. Give it the `.hinge` treatment at smaller scale — a banded full-bleed with the four numbers (12 → 50 → 5 → 5) set as a progression in `--dawn`. The site now has one great staged moment; it needs a second so the first does not read as a one-off.

---

## CLOSING

Round 1 asked for two things above all: fix the grid, and stage the two moments the story is actually about. **The staging was done, and done well.** The 1929 hinge is award-quality and the sixty-year silence is a real compositional idea. Narrative and typography both moved a full point or more, and the site is now measurably harder to mistake for a template.

The grid was half-fixed. `.wrap` widened correctly, section rhythm arrived, and the third track exists — but it exists empty, the rule still points at nothing on five rows out of nine, and the footer picked up a regression that breaks the page's own alignment on the final screen.

**7.4 / 10 — Honorable Mention.** Fix the footer and the `.src` contrast in an afternoon; that alone is worth ~0.3. Then write the apparatus column, which is the real work and the difference between this and a Site of the Day.
