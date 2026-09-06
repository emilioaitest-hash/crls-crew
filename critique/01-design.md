# CRLS Rowing — Design Critique

**Judged against:** Awwwards Site of the Day (the real bar, not the "nice portfolio piece" bar)
**Reviewed at:** 1240px, 1600px, 2560px, and 390px
**Source read:** `index.html`, `src/styles.css`, `src/data/team.js`

---

## VERDICT

**Overall: 6.2 / 10 — REJECTED for Site of the Day.**
Honorable Mention is reachable, but only after fix #1. Not before.

This is not slop. Somebody with taste chose this stack and held a line: no purple, no Inter, no glass, no icon-tile grid. The hero is genuinely good and the content is real archival research, not filler. That puts it in the top decile of what gets submitted.

But SOTD is not awarded for restraint. It is awarded for *composition*, and this site has essentially one composition that it repeats eleven times. The hero writes a cheque — full-bleed, 240px display type, 94% of the viewport — that every section below it refuses to cash. From `#river` to `#free` the site becomes a 544px-wide text column parked on the left of a 1600px screen with a hairline rule stretching past it into nothing. A juror scrolling this on a 27" display sees a beautiful masthead followed by 12,000 pixels of dead right-hand margin.

---

## SCORES

| # | Category | Score |
|---|---|---|
| 1 | Typography | 7.0 |
| 2 | Layout | 4.0 |
| 3 | Colour & Light | 8.0 |
| 4 | Motion | 5.5 |
| 5 | Narrative | 7.0 |
| 6 | AI-Slop Resistance | 8.5 |

---

## 1. TYPOGRAPHY — 7.0

**Working.** Big Shoulders at `clamp(4.5rem, 15vw, 16rem)` with `line-height: 0.86` and `letter-spacing: -4.8px` is a real typographic decision — the hero's three stacked lines lock into a solid rectangle of ink. Newsreader at 18px/29.16px (1.62) is a correct body setting. Three faces with three genuinely separate jobs — display / prose / data — is a professional stack, and the Martian Mono numerals with `font-variant-numeric: tabular-nums` on `.tl-year` are the right call.

**Broken:**

- **`.note` footnotes are unreadable.** `--t-micro: 0.6875rem` = **11px**, set in a monospace, at `--grey-2` (#5b646d) on #0a0c0e. That is a **2.9:1 contrast ratio — fails WCAG AA outright** — at a size below the 12px legibility floor, and in `#gap` it runs to a measured **124 characters per line**. These footnotes are where the site's credibility lives ("The program says 1643. Wikipedia says…"). They are currently the least readable text on the page. Self-defeating.
- **Every H2 is the same size and the same width.** Six `<h2>`s, all `clamp(2rem, 4.2vw, 3.75rem)` → 60px, all rendering at **exactly 595px wide**. There is no typographic climax anywhere after the hero. "The best season they have had" — the emotional peak of the story — is set identically to "A mile and a quarter of moving water."
- **Two bad line breaks, both orphaning a stranded fragment:**
  - "The first time / **around**"
  - "The field they / **race in**" ← splits the verb phrase. Worst break on the page.
- **Lead measure inconsistent.** `.lead` paragraphs run 685px @ 24px in `#river` and `#gap` (≈57ch, fine) but the 18px follow-on prose in those same sections also sits at 685px = **76 characters**. Two different measures in one column, neither matching the 544px used elsewhere.

---

## 2. LAYOUT — 4.0 ← the failing grade

This is where the site loses the award, and it is one bug repeated everywhere.

**The mechanism, exactly:**

```css
.wrap    { width: min(100% - var(--gutter)*2, 84rem); }  /* 1344px cap */
.tl-item { grid-template-columns: 7rem 1fr; }            /* 1fr ≈ 1232px */
.tl-body { max-width: var(--measure); }                  /* 544px */
.tl-item { border-top: 1px solid var(--rule-soft); }     /* spans all 1344px */
```

The `1fr` track is ~1232px. The text inside it is capped at 544px. **~690px of every timeline row is empty — but the rule above it draws the full 1344px.** The eye is handed a horizontal line pointing at nothing. This is not "generous whitespace," it is an unclosed container, and it repeats down all 2,657px of `#then`, all of `#return`, and again in `#gap`.

**Measured content width:**

| Viewport | Hero | Every section below |
|---|---|---|
| 1600px | 92% | 84% |
| **2560px** | **94%** | **52%** |

At 2560px the body of the site collapses to **just over half the screen** while the hero still owns 94% of it. The site is actively worse the better your monitor is — the exact opposite of what a jury with a 5K display wants to see.

**Other layout failures:**

- **Zero section rhythm.** Section heights: 507 / **2657** / 703 / 572 / 1732 / 360 / 1169 / 836 / 1373 / 879. Every one of them is the same left-aligned `.split` with a sticky heading. `#then` alone is 2,657px of identical timeline rows with no compositional break — no full-bleed, no image, no change of axis.
- **A genuinely boring centered strip exists.** `index.html:154`, `:187`, `:347` — `<div class="narrow" style="margin-inline:0">`. Three inline-style overrides fighting the stylesheet's own `margin-inline: auto`, which is the signature of a layout nobody trusted. At 2560px the unnamed section at `index.html:152` measures **20% of viewport width**.
- **`.split`'s comment admits the problem it doesn't solve.** Line 113–115: *"This stops long sections reading as a single ragged strip down the left edge of a very wide screen."* It doesn't. The heading column goes sticky, the prose column stays 544px, and the ragged left strip is exactly what ships.

---

## 3. COLOUR & LIGHT — 8.0

The strongest axis. `#0a0c0e` / `#f4f1ea` / `#c9683a` is a disciplined, unfashionable, correct palette — bone rather than pure white is the right instinct for an archival subject, and the near-black has a blue cast (`--ink-3: #1e242b`) that reads as cold river water rather than generic dark mode.

**The accent is genuinely earned.** 59 elements carry `--dawn`, and it is used *semantically* rather than decoratively: timeline years, chapter numerals (01–07), `WON` bars in the chart, the `Public` and `Cambridge` lanes in the 1929 heat diagram, and podium places. In the heat diagram, orange = public school and grey = private school — the accent is carrying the entire argument of the site in a single hue. That is exactly what a single accent is for. Credit where due.

**Deductions:** across `#then` and `#return` — nearly 4,400px of continuous scroll — there is no tonal event at all. Bone on ink, bone on ink. `--river: #2d4a5c` and `--river-lit: #4a7a94` are declared in `:root` and barely used. The site defined itself a cold blue mid-tone and then never lit anything with it.

---

## 4. MOTION — 5.5

**Good:** `prefers-reduced-motion` is handled (confirmed in the stylesheet). The masked hero line reveal is clean. The 3D boat renders at 685×428 without jank.

**The problem is that it is one gesture, globally applied.** Measured transition durations across the DOM:

- `0.9s` on 21 elements
- `0.9s, 0.9s` on 50 elements

**71 elements share one 0.9s reveal.** That is a scroll-triggered `.in` class bolted onto everything — `.hero-stat`, `.tl-item`, `.quote`, `.boat-name`, `.spec-table`, `.result` all fade identically. Nothing is choreographed; nothing arrives *because* of what it is. At SOTD level, motion has to argue. Here it only announces that an IntersectionObserver fired.

Also: 0.9s is too slow for a reveal that fires 71 times. Scrolling fast means permanently reading half-opacity text.

---

## 5. NARRATIVE — 7.0

The arc is the best thing about this project and the reason it's worth fixing rather than scrapping. River → 1889–1929 when public and private raced in **one heat** → sixty years of nothing → 1989 revival under a borrowed name → the fleet → twenty seasons of data → best season ever → **$0 to row**. That is a real thesis with a real antagonist, and the 1929 heat diagram — public lanes in orange, private in grey, all in one race — is the single best piece of information design on the site.

**Where it sags:**

- **`#then` is 2,657px long and structurally flat.** Six timeline entries at the same weight. The 1929 moment — *"The eights were separated. The fours were not."* — is the hinge of the entire argument and it is styled as `.tl-item.pull`, barely distinguishable from the five rows around it.
- **The sixty-year gap is the most cinematic beat in the story and gets the smallest section.** `#gap` is **572px** — shorter than everything around it. Sixty years of silence should be the longest, emptiest scroll on the site. Instead it's the shortest.
- **`$0 TO ROW` is buried.** It appears as the fourth hero stat, at the same size as "186 named athletes," and the `#free` section that argues it lands after the reader has already scrolled 12,700px. The thesis arrives too late and too quietly.

---

## 6. AI-SLOP TELLS — 8.5 (few fire)

Credit first: `styles.css:9` literally says *"Deliberately NOT here: purple/indigo gradients, glassmorphism, Inter."* The discipline held.

| Tell | Fires? | Note |
|---|---|---|
| Purple/indigo gradient | **No** | Palette is ink/bone/burnt-orange throughout |
| Generic tech hue | **No** | `#c9683a` is a considered, unfashionable choice |
| Icon + heading + sentence tile grid | **No** | No feature tiles anywhere |
| Coloured left border on cards | **Borderline** | `.note` uses `border-left: 1px solid var(--rule)` — but it's a neutral hairline on a footnote, a legitimate editorial convention. Not slop. |
| Unearned glassmorphism | **Borderline** | `backdrop-filter: blur(6px)` on the sticky header (`:232`). Functional legibility scrim over scrolling content, not decoration. Passes. |
| Oversized meaningless stats | **No** | 1,321 races / 394 won / 186 athletes / $0 are all real, sourced numbers |
| Rounded-square icon above heading | **No** | Absent |
| Everything centered | **No** — inverted | The failure is the opposite: everything is left-locked with a dead right column |
| Inter / system-ui default | **No** | Three self-hosted `woff2` faces with `font-display: swap` |
| Composition mismatched to content | **Partially** | The palette and type match the subject well; the *grid* does not — a 1,321-race dataset and a 20-year chart are being served by a single narrow prose column |

**Verdict on slop: this site is not AI slop.** Its problems are the problems of a real designer who built one good template and then never varied it.

---

## THE SINGLE MOST DAMAGING WEAKNESS

> **`.wrap` caps at 84rem while `.tl-body` caps at 34rem inside a `1fr` track — so ~690px of every content row is empty, and `border-top` draws a full-width rule across that emptiness.**

One CSS mismatch, repeated in `.tl-item`, `.split`, and `.narrow`, produces the dead right column that defines the entire experience below the fold. It is why the site scores 52% content width at 2560px, why there is no section rhythm, and why the hero feels like it belongs to a different, better project. **Fix this and the site jumps roughly two points.** Nothing else on this list matters as much.

---

## PRIORITIZED FIX LIST

### P0 — blocking

**1. `#then` / `#return` / `.tl-item` — kill the dead right column.**
Change `styles.css:399` from `grid-template-columns: 7rem 1fr` to `grid-template-columns: 7rem minmax(0, 34rem) minmax(0, 1fr)` and move the `.note` footnote and the `Source ↗` link out of `.tl-body` into that new third column. The prose keeps its 544px measure, the empty 690px becomes the apparatus column, and the full-width `border-top` finally has content beneath its full span. This single change fixes the site's defining flaw.

**2. `.wrap` — stop shrinking on large displays.**
`styles.css:109`: change `min(100% - var(--gutter)*2, 84rem)` to `min(100% - var(--gutter)*2, 108rem)`. Content goes from 52% → ~68% of a 2560px viewport. Pair with fix #1 so the extra width lands in the apparatus column, not in the measure.

**3. `#then` — break the 2,657px monotony with one full-bleed moment.**
Pull the 1929 entry (`.tl-item.pull`, *"The eights were separated. The fours were not."*) out of the timeline entirely. Give it a full-bleed 100vw band at `--ink-2`, set the line at `--t-h1` (6.5rem) instead of the current 37.6px `.tl-title`, and place the orange/grey heat diagram directly beneath it at full width. This is the hinge of the argument — stage it as one.

### P1 — high

**4. `.note` — make the footnotes readable.**
`styles.css:206`: raise `--t-micro` from `0.6875rem` (11px) to `0.8125rem` (13px), change `color: var(--grey-2)` (#5b646d, **2.9:1 — fails AA**) to `var(--grey)` (#8b9299, ~5.4:1 — passes), and add `max-width: 42ch` to stop the 124-character lines in `#gap`.

**5. `#gap` — make sixty years of silence feel like sixty years.**
`#gap` is currently 572px, the shortest section on the site. Raise it to a minimum of `180vh` of near-empty `--ink`, with only "Then nothing, / for sixty years" and a thin `--dawn` rule that lengthens as you scroll from 1929 to 1989. The one place on this site where enormous empty space is *the content*, and it's the one place it isn't used.

**6. `h2` — introduce scale contrast and fix the two bad breaks.**
All six H2s render at 60px / 595px wide. Give the two climax headings — "The best season they have had" (`#now`) and the `#free` thesis heading — `--t-h1` (`clamp(2.75rem, 7vw, 6.5rem)`). Then insert `<br>` manually: "The field they race in" must break as "The field / they race in", never "The field they / race in". Same for "The first time / around" → "The / first time around".

### P2 — polish

**7. Reveal motion — stop treating 71 elements identically.**
Drop the global `.in` transition from `0.9s` to `0.55s`, and add `transition-delay: calc(var(--i) * 60ms)` on `.tl-item`, `.result`, and `.bar-col` children so rows cascade instead of flashing in as a block. Reserve the slow 0.9s exclusively for the hero and the new 1929 full-bleed band.

**8. `#record` chart — the first eight seasons are illegible and 2020 is unexplained.**
The 2007–2014 bars render 4–8px tall and the 2020 column is a near-invisible sliver with no annotation — a reader cannot tell whether that's a bad season or COVID. Add a `√` or log scale toggle, or normalise bar height to win *rate* rather than raw count, and label 2020 explicitly ("no season — COVID"). Also raise `.bar-year` from `font-size: 10px` (`:512`); rotated 10px mono is at the edge of legibility.

**9. `index.html:154, :187, :347` — remove the three inline `style="margin-inline:0"` overrides.**
These fight `.narrow`'s own `margin-inline: auto`. Replace with a real modifier class (`.narrow--flush`) so the layout system is honest about what it's doing. At 2560px one of these sections measures 20% of viewport width.

**10. Mobile 390px — the header right-hand label is clipped.**
The chapter indicator renders as "THE (" and "ON" — cut off at the viewport edge rather than wrapping or truncating cleanly. Either drop the right-hand chapter label below 40rem or give it `text-overflow: ellipsis` with a defined width. Also reconsider the `7rem` year column on `.tl-item` at mobile (`:399`): a 4-character year is consuming ~33% of a 390px screen and squeezing the body measure.

**11. `#free` / hero — promote the thesis.**
`$0 TO ROW` is the argument of the entire site and currently sits as the fourth of four equal hero stats, with its supporting section arriving 12,700px later. Set it apart in the hero at display scale in `--dawn`, and add a mid-page callback around `#record` so the reader carries "no fee" through the results rather than meeting it only at the end.

---

## CLOSING

The research is real, the palette is disciplined, the hero is award-quality, and the 1929 one-heat diagram is a genuinely smart piece of information design. This project has a thesis, which is more than most SOTD winners can say.

What it does not have is a second idea about how to put things on a screen. Eleven sections, one template, 690px of dead air in every one of them. Fix the grid and stage the two moments the story is actually about — the 1929 heat and the sixty-year silence — and this becomes a credible Site of the Day submission. As it stands: **rejected.**
