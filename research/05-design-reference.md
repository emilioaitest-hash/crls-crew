# 05 — Design Reference Dossier
### Visual and interaction language for an award-caliber rowing site
Compiled 2026-09-05. Sources are linked inline. Where a claim comes from observed page behavior rather than a published case study, it is marked **[observed]**. Where it needs checking before you rely on it, it is marked **[verify]**.

Client brief context: CRLS Crew (Cambridge Rindge & Latin), high school rowing on the Charles. Existing prototypes in this repo: `Vox Style.html` (Archivo + Source Serif 4, `--accent:#fff100`, hairline grid, numbered section heads, SVG boat diagrams) and `Style Board.html`. This dossier is written to critique and extend those, not to replace them.

---

## Part 1 — Vox visual language

### 1.1 What Vox actually uses

Vox.com's type stack, verified against Fonts In Use (2014 launch documentation) and a 2026 token extraction of the live homepage:

| Role | Face | Foundry | Live spec |
|---|---|---|---|
| Display / headline / UI | **Balto** | Mark Simonson Studio | 22–70px, weight 700, tracking −0.7px at display sizes |
| Body / paragraph | **Harriet** | Okay Type | 14–20px, weight 400, tracking −0.14 to −0.2px |
| Eyebrow / kicker / timestamp | **Roboto Mono** | Google (Christian Robertson) | 11–12px, UPPERCASE, weights 400/500/700, tracking **1.1px** |
| Legacy tertiary | Alright Sans | Okay Type | Present in 2014 launch, largely retired |

Sources: <https://fontsinuse.com/uses/6828/vox-website>, <https://www.shadcn.io/design/vox>, <https://wtfont.app/site/vox.com>

All three are commercial licenses. Do not attempt to license Balto and Harriet for a high school team site. The **transferable move is the three-register structure**, not the faces: one grotesque doing all the shouting, one serif doing all the reading, one mono doing all the labelling. Section 5 gives free equivalents.

### 1.2 Color

Vox is a single-voltage system. There is essentially one chromatic hue on the entire page.

```
--vox-yellow:      #fff200;   /* masthead band, CTA fill, feature tile, list bullets */
--vox-ink:         #131313;   /* all headlines and body */
--vox-ink-absolute:#000000;   /* wordmark only */
--vox-ink-soft:    #4a4a4a;
--vox-ink-muted:   #636363;
--vox-hairline:    #e9e9e9;   /* the entire elevation system */
--vox-link-blue:   #6aaae4;   /* appears once, on the vox.com dot */
--vox-canvas:      #ffffff;
```

The extraction counts **14 yellow paint events on the whole homepage**. The yellow is never a text color, never a border, never a hover state, never faded below 100% saturation. It reads closer to hazard tape than to a brand accent.

Your prototype uses `#fff100`. Vox's actual value is `#fff200`. Trivial difference, but if you are going to cite Vox, cite it correctly, and more importantly **be aware you are one hue away from being a Vox clone**. See 1.6.

### 1.3 Geometry and elevation

- Radius scale is `0px` / `1px` / `2px` / `100px` (pill) / `50%` (orb). Story cards, the masthead band, feature tiles all render at **0**. The "Join now" CTA is **1px**. The newsletter input is **2px**.
- There are **no drop shadows**. Every shadow token in the extraction is either a 1px inset underline on an active nav tab or a 1px focus ring. Elevation is carried by a `1px #e9e9e9` hairline, a yellow fill, or a mono uppercase kicker.
- A `12px` rounded button, `shadow-lg`, or any `backdrop-filter: blur()` breaks the register instantly. This is the single most useful Vox lesson for an anti-slop site: **flat canvas, hairline separation, typographic hierarchy**.

### 1.4 Layout DNA

The 2017 homepage redesign (design director Yesenia Perez-Cruz) explicitly moved Vox **toward a newspaper layout and away from a photo-driven one**, chasing "credible, smart, functional density." The yellow bracket around "Top Stories" is called out in their own writeup as the detail holding the hero together.

Sources: <https://product.voxmedia.com/2017/4/6/15182844/behind-vox-homepage-refresh>, <https://www.poynter.org/tech-tools/2017/why-vox-redesigned-its-homepage-with-newspapers-in-mind/>

Transferable principles:
1. **Density is a credibility signal.** A page that fits more real information per screen reads as more serious than one with 160px of padding around a single sentence.
2. **A bracket, rule, or band beats a card.** Vox groups by drawing a line around things, not by floating them on a surface.
3. **Numbered, labelled sections.** The card-stack explainer format Vox pioneered numbers its steps. Your prototype already does this with `.snum`. Keep it.

### 1.5 Platform history (so you cite it correctly)

- **Chorus** — Vox Media's proprietary CMS, opened to external publishers in 2018.
- **Unison** — the design system that migrated 350+ sites across 8 brands (Vox, The Verge, Curbed, Eater, Polygon, Recode, Racked, SB Nation) onto one codebase with per-brand "scenarios." Vox's scenario was the text-forward newspaper one; The Verge's was bold and asymmetric.
- **Duet** — the design system built for The Verge's relaunch. Public docs at <https://www.duetds.com/typography/>. Duet is *The Verge's* language, not Vox.com's. Do not conflate them.
- Vox Media **dropped Chorus in 2023** and replatformed onto decoupled WordPress (Axios scoop; XWP case study).
- The **corporate** Vox Media identity (2019, Triboro Studios) is purple with a custom display face called **Onward**. This is the parent company, not vox.com. Do not pull purple from here. Purple is also the single loudest AI-slop tell in Part 4.

Sources: <https://www.sanettesloan.com/designportfolio/unison-mtdch>, <https://www.axios.com/2023/07/18/vox-media-chorus>, <https://design.voxmedia.com/2019/11/6/20950220/the-new-vox-media-logo-and-corporate-identity>

### 1.6 The honest warning

Vox yellow on white with a black grotesque is one of the most recognizable editorial signatures on the web. An Awwwards jury will read a direct lift as derivative, and Creativity (20%) is scored on "originality of concept and execution." **Take the grammar, change the voltage.**

Concrete moves that keep the Vox logic while breaking the Vox look:
- Swap the single accent to something owned by the subject. Charles River at 6am is grey-blue and amber. CRLS colors. A blade-livery color. Anything that is *specifically about this team* beats a borrowed yellow.
- Keep the 14-paint-event discipline. Whatever the accent is, use it fewer than 15 times on a page and never as body text.
- Keep the hairline-as-elevation rule verbatim. It is the least copied and most valuable part.
- Replace the newspaper grid with a grid that means something for rowing: a lane grid (6 lanes, 2000m), a stroke-cycle grid (4 phases), a seat grid (8 + cox). Your prototype's 4-column `.cycle` already does this. Push it further.

---

## Part 2 — Awwwards: what actually wins

### 2.1 The published rubric

Official: <https://www.awwwards.com/about-evaluation>

| Criterion | Weight |
|---|---|
| Design | **40%** |
| Usability (UX/UI) | **30%** |
| Creativity | **20%** |
| Content | **10%** |

Mechanics, corroborated across the official page and jury-member writeups:
- Minimum **18 jurors** score each approved submission.
- The **3 scores furthest from the average are dropped** to kill outliers.
- Voting runs **5 days**; a site with a strong jury score plus ≥10 validated PRO votes can be called early.
- **6.5+ earns an Honorable Mention.** Site of the Day goes to the day's highest score, in practice mid-to-high 8s.
- SOTD winners are passed to a **separate developer jury** scored against the Development Guidelines; above 7 earns a **Developer Award** covering engineering, accessibility, and code quality.
- A **Mobile Excellence** track scores against Google's mobile criteria with a **70/100 qualifying threshold**.

Source for mechanics: <https://www.hontran.dev/blog/awwwards-judging-criteria>, <https://www.utsubo.com/blog/award-winning-website-design-guide>

**The number that should govern your build: Design + Usability = 70%.** WebGL is inside the 20%. A site that stutters on a mid-tier Android loses more Usability than the effect earns in Creativity.

### 2.2 Twelve-plus recent Site of the Day winners

Pulled live from <https://www.awwwards.com/websites/sites_of_the_day/> on 2026-09-05, then each site opened and inspected. Font names, canvas presence, and library detection are **[observed]** from the live DOM.

**1. Gionatan Nese '26** — <https://www.gionatannese.com/> (Awwwards: `/sites/gionatan-nese-26`)
Designer portfolio, Milan. Next.js with Turbopack, 25 chunks, **one full-viewport WebGL canvas (2400×1366)**, custom cursor element present. Type is **LayGrotesk + Teodor** (a grotesque/serif pair, both commercial). Why it wins: a portfolio that is itself the portfolio piece, with the WebGL used as a single continuous surface rather than a set of tricks. **No `prefers-reduced-motion` rules found in stylesheets [observed] — this is the exact gap that costs Developer Award points.**

**2. ILLOCA** — <https://illoca.com/> (`/sites/illoca`)
AI design engine for architects, by Unseen Studio (the Green Chameleon rebrand, 35+ SOTDs). Fonts: **F37 Analog, Graphik Web, and a bespoke "Architect Pro" family with Symbols / Alt / Rule / Rule Marker cuts** — a purpose-drawn technical-drawing typeface with its own symbol and rule-line sets. `h1` at **92.5px / weight 500**. WebGL canvas present. **1 reduced-motion media query found [observed].** Why it wins: the custom type system *is* the concept. The Architect Pro "Rule Marker" cut means their annotation lines are typographic, not SVG. Directly stealable for a rowing diagram: draw your callout leaders as font glyphs.

**3. Trevor Noah** — <https://www.trevornoah.com/> (`/sites/trevor-noah`, OFF+BRAND)
Talent site uniting standup, podcast, books, tour. Webflow front end with a custom `app.js` served off Vercel, plus a WebGL canvas. **`h1` renders at 317px** on a `#1d2440` navy ground with `#f9fcf4` off-white text, in **Die Grotesk D**, with **Die Grotesk B and C** carrying other registers. Why it wins: three optical cuts of one family across three roles, and typographic scale used as the primary event. The 317px headline does the work a hero video usually does.

**4. Paul Kalkbrenner** — <https://www.paulkalkbrenner.net/> (`/sites/paul-kalkbrenner`, HOLOGRAPHIK)
Musician site. Relevant to CRLS because it solves the same structural problem: an entity with a schedule (tour dates / regatta results), a body of work (tracks / seasons), and a personal narrative, all in one scroll.

**5. Squarespace Foundations** — <https://brand.squarespace.com/typography> (`/sites/squarespace-foundations`, Resn)
An **interactive brand guideline**. The deep link lands on the typography page. Why it matters here: it is the reference for how to make type specimens interactive without them becoming a gimmick. If CRLS wants a "how the boat works" section, this is the model for turning a spec sheet into an experience.

**6. ERA Residence** — <https://www.era-residence.com/> (`/sites/era-residence`, The First The Last)
Mediterranean property. Included as the reference for **material-led art direction**: stone, water, and light as the palette source rather than a color picker. The rowing analogue is carbon fiber, varnished wood, river water, and morning fog.

**7. Aardvark Book Club** — <https://aardvarkbookclub.com/> (`/sites/aardvark-book-club`, FUTURE THREE®)
The most technically instructive stack on this list, and fully readable **[observed]**:
```
Webflow  +  Barba.js 2.10.3  +  @barba/prefetch 2.2.0
GSAP 3.15  +  ScrollTrigger  +  SplitText  +  CustomEase
Lenis (detected)
Fonts: Champ (display, h1 100px / 700 / −1px tracking), Degular (body), Hello Organichand (script accent)
Two canvases: one 2400×1750 2D, one 300×150 WebGL
```
This is the canonical award-site recipe: **Barba for page transitions, GSAP + ScrollTrigger for choreography, SplitText for text reveals, CustomEase for a signature easing curve, Lenis for scroll weight.** If you build one thing from this dossier, build this stack.

**8. Decathlon Yestalgia** — <https://decathlonyestalgia.com/> (`/sites/decathlon-yestalgia`, index)
90s-archive sportswear capsule. **The closest brief on this list to CRLS.** It is a sports brand doing period-specific, playful art direction from archive material. A high school crew program has exactly this asset: decades of team photos, old blade liveries, yearbook results. Study how they make archive material feel designed rather than scanned.

**9. AI in Design Report 2026** — <https://stateofaidesign.com/> (`/sites/ai-in-design-report-2026`, ++hellohello)
"A research report transformed into an editorial digital experience, where data, analysis, and motion speak in a single visual language." **This is the direct structural precedent for a Vox-style explainer winning SOTD.** Built on **Framer** with only 4 scripts and **no canvas at all [observed]**. Type: **Beausite Classic** (Medium/Regular/Bold), **Fragment Mono** and **Geist Mono** for data. `h1` at **120px / weight 500 / −7.2px letter-spacing** (that is −0.06em, an aggressive optical correction). Proof that you can take SOTD with zero WebGL if the editorial system is strong enough.

**10. Miu Miu — A House That We Shaped** — <https://immersivebags.miumiu.com/> (`/sites/miu-miu-a-house-that-we-shaped`, Merci Michel)
Explorable 3D house with interactive objects. The reference for **spatial navigation as menu**: the environment replaces the nav bar. If CRLS wants a 3D boathouse fleet viewer (your prototype's stated ambition), this is the model to study for how to make an explorable space still be usable.

**11. /zeroz Brand Site** — <https://otsuka-air.jp/> (`/sites/zeroz-brand-site`, SHIFTBRAIN)
"Chapters unfold through 3DCG." Japanese studio craft. The reference for **chaptered 3D narrative** where the 3D advances the story rather than decorating it.

**12. The Watch (FS 60P)** — <https://thewatch.60fps.fr/> (`/sites/the-watch`, 60fps)
"A real-time WebGL piece that interacts with the content around it." **Two scripts total** — one bundle plus a Cloudflare beacon — driving a 2400×1366 WebGL canvas. `h1` at **291.7px in Nekst**. The tightest engineering on the list: an entire real-time product visualization in a single Vite bundle. This is the reference for **WebGL that reacts to DOM content** rather than living in an isolated hero.

**13. Mosby's Files** — <https://www.mosbyfiles.com/about> (`/sites/mosbys-files`, Tubik)
Research archive of early American architects. Self-described: *"a CSS-only skeuomorphic folder system."* Nuxt, **two scripts, no canvas, no GSAP, no Lenis [observed]**. Dark ground `#191919`, text `#fdfaf7`, **Signifier** serif body with **Founders Grotesk** headings. Why it matters most for CRLS: **an archive site took SOTD on CSS craft and art direction alone.** No WebGL. A crew program's results archive, boat log, and alumni records could take exactly this route.

**14. The State of the Gallery** — <https://mesh3d.gallery/the-state-of-the-gallery> (`/sites/the-state-of-the-gallery`)
"An overview of the gallery in numbers and picks." A data-forward editorial piece about who is making the strongest Three.js work. Useful both as a stats-page reference and as a curated index of current WebGL practice.

**15. 20 Years Inspired By People** — <https://inspiring.nk.studio/es> (`/sites/20-years-inspired-by-people`, /nk.studio)
"An archive of stories, people and moments." Anniversary retrospective. The structural model for a program history section, which a school crew team with a long record should have.

**Also worth studying (Site of the Month tier):** Immersive Garden's *GQ × Audemars Piguet — The Extraordinary Lab* (SOTM Mar 2026) and *Cartier Watches & Wonders 2026* (SOTD + Developer Award, May 2026). Their published approach is GSAP for transitions, Lenis for scroll, custom shaders for volumetric light, DOM reserved for text and UI, iterated live in the browser with hot shader reloading. <https://www.awwwards.com/immersivegarden/>

### 2.3 Recurring craft techniques across the winners

Ranked by how often they showed up:

1. **Lenis smooth scroll** with GSAP's ticker driving it in one rAF loop. Ubiquitous.
2. **GSAP ScrollTrigger** with `pin` + `scrub` for chaptered sections.
3. **SplitText character/word/line reveals**, usually a `clip-path` or `yPercent` stagger, never a plain fade.
4. **A named custom easing curve** (`CustomEase`) reused across the whole site so motion has a signature.
5. **Barba.js page transitions** with prefetch, so navigation never white-flashes.
6. **Oversized display type** as the hero event. Observed `h1` sizes: 317px, 291px, 120px, 100px, 92px. Negative tracking at display size is near-universal (−0.06em on stateofaidesign).
7. **Three or more optical cuts of one family** rather than three different families (Die Grotesk B/C/D; Architect Pro Alt/Rule/Symbols).
8. **A mono for data.** Fragment Mono, Geist Mono, Roboto Mono. Universal for labels, timestamps, and numbers.
9. **Custom cursor**, present on roughly half. Note this is a *risk* — see the accessibility section.
10. **Just-in-time WebGL**: canvas mounted via IntersectionObserver, disposed when off-screen.
11. **Dark ground or stark white**, rarely anything between. `#191919`, `#1d2440`, `#ffffff`.
12. **Two-script builds.** The Watch and Mosby's Files each ship two scripts. Bundle discipline is visible to the developer jury.

### 2.4 What jurors penalize

From the jury-member writeups, consistent across sources:
- Derivative concepts. Riding the trend of the moment hits Creativity directly.
- Effects without a concept. Reads as *lack of control* under Design, the 40% criterion.
- Jank. A hero below 60fps costs more Usability than it earns in Creativity.
- Desktop-only thinking. Caps you on 30% of the score.
- Placeholder content. Lorem ipsum and stock-grade imagery bleed the Content 10% *and* undercut Design.
- **No accessibility floor**: missing focus states, no reduced-motion path, low contrast, or a custom cursor that hides the real one. Described as "small things a juror reads as carelessness."

---

## Part 3 — Scrollytelling and narrative structure

### 3.1 The five primitives

Everything published since the form matured is a recombination of these:

| Primitive | Mechanism | Best for |
|---|---|---|
| **Pinned background** | `position: sticky` graphic, text steps scroll past it | Diagram annotation, map zoom |
| **Scrubbed sequence** | canvas image sequence or `<video>` `currentTime` driven by scroll progress | Physical motion, assembly |
| **Chaptered video** | discrete video segments per chapter | Documentary |
| **Stepper-driven chart** | Scrollama step events swap chart state | Data narrative |
| **Pinned product** | object pinned, camera/state changes with scroll | Product, equipment |

For a rowing site, the **scrubbed sequence** is the obvious high-value one: the stroke cycle is a literal, cyclical, physical motion that scroll position maps onto perfectly. Catch → Drive → Finish → Recovery is a scrub, not four cards. Your prototype currently renders it as four static SVG frames. **Turning `.cycle` into a scroll-scrubbed body-position sequence is the single highest-leverage upgrade in the file.**

### 3.2 The implementation the newsrooms actually use

**Scrollama** (Russell Samora, The Pudding) — <https://github.com/russellsamora/scrollama>, current 3.2.0.
Uses `IntersectionObserver` instead of scroll events, which is why it does not jank. Three features: **step triggers** (fires when an element crosses a threshold), **step progress** (0–100% completion of a step), and container enter/exit (deprecated since 2.0.0 in favor of CSS).

The key Pudding insight, from <https://pudding.cool/process/scrollytelling-sticky/>: **offload the sticky graphic entirely to `position: sticky` in CSS.** The old pattern needed JS to manage stuck state and dimensions. Now you need none of it. Scrollama handles step events only; CSS handles pinning.

```css
.scrolly { display: grid; grid-template-columns: 1fr; }
.scrolly__graphic {
  position: sticky;
  top: 0;
  height: 100vh;
  display: grid;
  place-items: center;
}
.scrolly__step { min-height: 100vh; }     /* one screen of scroll per beat */
.scrolly__step:last-child { margin-bottom: 50vh; }  /* let the last beat land */
```

**ai2html** (Archie Tse, NYT, open-sourced March 2015) converts Adobe Illustrator artwork into responsive HTML + CSS + images. It is why NYT graphics have real text in them at every breakpoint instead of a flat PNG. If any part of the CRLS site involves hand-drawn diagrams that need to be responsive and selectable, this is the pipeline.
<https://mobilevis.github.io/assets/mobilevis2018_paper_20.pdf>

### 3.3 Narrative structures that work

**Linear vs. elastic.** The academic framing (Mörth et al., ScrollyVis, arXiv:2207.03616) distinguishes **linear** scrollytelling from **elastic**, where the reader can dive deeper at chosen points. Elastic is harder and usually better.

**The Pudding's branching model.** Their IVF interactive runs **two simultaneous narrative tracks (Parent and Child)** that the reader chooses between, with optional "deep dive" sections tucked away like side quests. The first decision the reader faces is *structural, not topical*. That is a strong pattern: make the reader commit to a point of view before they commit to a subject.

For CRLS this maps cleanly. The first choice could be **"Row" or "Watch"** — the athlete's experience versus the spectator's. Same regatta, two tracks, different information hierarchy in each.

**Pacing rules that hold up:**
- One idea per beat. If a step needs two sentences of setup, it is two steps.
- Roughly `100vh` of scroll per beat. Below `70vh` the reader has no time to read before the graphic moves; above `150vh` it feels stalled.
- **Reveal, do not restate.** The graphic should show something the text has not already said. The Pudding's signature move is a sentence saying "in 2014, the most repetitive song used the same phrase over 200 times" landing at the exact moment one data point lights up.
- Chapter transitions need a **hard break**: full-bleed color change, a full-viewport typographic card, or a scale reset. Continuous scroll with no punctuation reads as one undifferentiated 12,000px page.
- Give the reader a **position anchor**. A persistent scale indicator, chapter number, or progress element. For rowing this is free: a **2000m distance marker** that counts down as the reader scrolls is both a progress bar and a thematic device.
- **Land the last beat.** Add `50vh` of margin after the final step so it does not exit while the reader is still reading it.

### 3.4 Scroll position as a storytelling device, specific to rowing

Cheap and specific ideas that use scroll as meaning rather than as transport:
- **Scroll = distance.** The page is 2000m long. The header reads `0m → 2000m`. Section boundaries are the 500m splits. Stroke rate and split time are readouts pinned to the scroll.
- **Scroll = the stroke.** One section pins the rower and scrubs catch→finish, so scrolling *is* pulling.
- **Scroll = the season.** September (learn to row, cold, dark) to May (championship). Palette temperature shifts with scroll progress.
- **Scroll = the boat filling.** The eight assembles seat by seat as you descend, 8 through bow.

---

## Part 4 — Anti-AI-slop (priority section)

### 4.1 The root cause, stated once

From Wikipedia's *Signs of AI writing* (WikiProject AI Cleanup), which is the primary source most of the tooling below is derived from:

> LLMs use statistical algorithms to guess what should come next based on a large corpus. It thus tends to **regress to the mean**; the result tends toward the most statistically likely result that applies to the widest variety of cases.

Their illustration is worth keeping: the highly specific *"inventor of the first train-coupling device"* becomes *"a revolutionary titan of industry."* The subject becomes **simultaneously less specific and more exaggerated.** That is the whole disease, in text and in pixels. Diffusion models and LLMs both output the centroid of their training distribution.

The design corollary, from `funboy322/avoid-ai-design`: *"Large language models are trained toward the average, so their UI output clusters around a handful of safe defaults."*

**So the antidote is always the same: specificity.** Not "better." Not "more premium." Specific. A real name, a real time, a real photograph, a real constraint.

### 4.2 The sources

| Repo / page | What it is | License | Notes |
|---|---|---|---|
| [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | The canonical field guide, with real diffed examples | CC BY-SA 4.0 | Primary source. Shortcuts: `WP:AISIGNS`, `WP:AITELLS` |
| [blader/humanizer](https://github.com/blader/humanizer) | Agent skill, **35 numbered patterns** with before/after, derived from the Wikipedia page | MIT | 43.4k stars |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Design language + **deterministic 27-rule visual detector**, no LLM at runtime | Apache 2.0 | 65.8k stars. `npx impeccable detect <path|url>` |
| [funboy322/avoid-ai-design](https://github.com/funboy322/avoid-ai-design) | Audits AI-generated frontend, catalogs tells by category with HTML and React fixes | MIT | Has `detect` mode that scores without editing |
| [waddle36/anti-ai-slop](https://github.com/waddle36/anti-ai-slop) | Unified field guide synthesizing impeccable + humanizer | MIT / Apache 2.0 | Names **6 absolute bans** |
| [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | Prose, preserves voice; detect mode names each pattern and quotes the line | MIT | |
| [jalaalrd/anti-ai-slop-writing](https://github.com/jalaalrd/anti-ai-slop-writing) | **Generation-time** constraints: 50+ banned words, 35+ phrases, 16 openers | MIT | Based on CMU 2025, Wikipedia, Buffer's 52M-post analysis |
| [mshumer/unslop](https://github.com/mshumer/unslop) | Empirically profiles a model's own defaults, then writes an avoidance profile. **Visual mode screenshots HTML output to catch CSS/layout/color clichés** | MIT | |
| [tropes.fyi/directory](https://tropes.fyi/directory) | AI writing pattern directory | | Linked from the Wikipedia page |

Also: the Wikipedia page carries an **August 2026 maintenance banner** stating parts of it are outdated for the most recent models. Treat the list as a moving target, not scripture.

### 4.3 Visual tells — the checkable list

Compiled from `impeccable`, `avoid-ai-design`, and `anti-ai-slop`. Each is a **detectable signal**, not a matter of taste.

**The six absolute bans** (`waddle36/anti-ai-slop`, from impeccable):
1. **Side-stripe / colored left border on cards** (`border-left: 4px solid <accent>`)
2. **Gradient text** (`background-clip: text` on a headline)
3. **Glassmorphism by reflex** (`backdrop-filter: blur()` with no real elevation system behind it)
4. **The hero-metric template** (three oversized numbers with vague labels: "10x faster", "99.9% uptime", "500+ customers")
5. **Identical card grids** (three or four cards, same size, same shape, same weight)
6. **Modal as first thought** (reaching for a dialog before considering inline or a page)

**Color**
- Purple / indigo / violet gradient, usually `#6366f1 → #8b5cf6 → #a855f7` or any `from-purple-500 to-indigo-600`
- Untouched shadcn `zinc` / `slate` ramps
- Default Tailwind `blue-600` buttons
- Timid, evenly-spread palettes where six colors all have the same weight and none dominates
- Any `oklch()` value copy-pasted from a generator without adjustment

**Typography**
- **Inter** as the default for everything. (Also: Roboto, Poppins, Montserrat, system stack.)
- No display face at all — one family at three weights doing every job
- **Space Grotesk treated as the "safe interesting" pick**, which makes it a non-choice
- No pairing, no optical sizes, no mono for data

**Layout**
- Centered hero → subhead → two buttons → three feature cards → CTA. The template.
- Zero asymmetry anywhere on the page
- Three-tier pricing with a "most popular" ring
- Four-column footer
- Uniform `gap-4` / `p-6` spacing with no spatial hierarchy

**Components**
- `rounded-2xl shadow-lg` on everything
- Icon in a rounded square above every heading
- Default shadcn Card/Button with no styling applied

**Icons and glyphs**
- The worn `lucide` set: `Sparkles` next to anything AI, `ArrowRight`, `Zap`
- Emoji used as feature bullets or in headings
- **Arrow glyphs stapled to CTAs**: "Get started →". Catalogued as tell **CP3**, described as "the typographic cousin of the em-dash."
- Generic abstract SVG blobs

**Imagery**
- Gradient placeholder rectangles where a photo should be
- DiceBear avatars
- Generic stock-photo energy

**Motion**
- None at all, or the identical `fade-in-up` on every single element with the same duration and delay

### 4.4 Text tells — the checkable list

From the Wikipedia page and `blader/humanizer`'s 35 patterns.

**Content-level**
- **Inflated significance.** Watch for: *stands/serves as, is a testament/reminder, a crucial/pivotal/vital/key role, underscores its importance, reflects broader, symbolizing its enduring, setting the stage for, marks a shift, key turning point, evolving landscape, indelible mark, deeply rooted*
- **Superficial `-ing` analysis** bolted to sentence ends: *highlighting…, underscoring…, reflecting…, contributing to…, fostering…, enhancing…, showcasing…*
- **Promotional drift**: *boasts a, vibrant, rich, profound, nestled, in the heart of, groundbreaking, renowned, diverse array, natural beauty*
- **Vague attribution**: *Experts argue, Observers have cited, Industry reports, Some critics argue, several publications* — with one or zero actual sources
- **The challenges-and-future-prospects coda**: "Despite these challenges, X continues to thrive."
- **Name-dropping coverage to prove importance**, and *"maintains an active social media presence"*

**Sentence-level**
- **AI vocabulary by era** (the page tracks this over time):
  - *2023–mid-2024:* Additionally, boasts, bolstered, crucial, delve, emphasizing, enduring, garner, intricate, interplay, key, landscape, meticulous, pivotal, underscore, tapestry, testament, valuable, vibrant
  - *Mid-2024–mid-2025:* align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant
  - *Mid-2025 on:* emphasizing, enhance, highlighting, showcasing
- **Copula avoidance.** *serves as / stands as / functions as / represents / boasts / features / offers* replacing plain *is* and *has*. One study found a >10% drop in *is*/*are* in academic writing in 2023.
- **Negative parallelism**: "Not just X, but Y." "It's not X. It's Y."
- **Rule of three by default**: "innovation, inspiration, and insights"
- **Uniform sentence length.** `anti-ai-slop-writing` calls this "the single most measurable detection signal." Human writing has burstiness.
- **False agency**: "the data tells us", "the market rewards". Name the human.
- **False ranges**: "from the Big Bang to dark matter"

**Formatting**
- Em-dash overuse (multiple repos ban it categorically rather than limiting it)
- Excessive boldface, especially **bold mini-headings** at the start of list items
- Title Case In Headings
- Emoji as structural formatting
- Curly quotes and apostrophes where the surrounding source uses straight
- Skipped heading levels; thematic breaks between every section
- Markdown leaking into non-markdown contexts

**Fabrication**
- Invented statistics, fabricated quotes, fake anecdotes. This is the actual problem; the style tells are just symptoms. The Wikipedia guide is explicit: *"do not merely treat these signs as the problems to be fixed; that could just make detection harder."*

### 4.5 What makes design read as human

Extracted from the same sources plus the winner analysis in Part 2:

- **Commit to one direction.** `avoid-ai-design`'s workflow requires naming a single aesthetic direction with **three to five defining moves** before writing any code. AI output hedges across several directions at once. Pick brutalist editorial, or warm archival, or technical-drawing, and then be ruthless.
- **Asymmetry.** One dominant element and one subordinate one, not two equal columns. Not everything centered.
- **A dominant color plus a sharp accent**, not a spread of six equal-weight colors and not a gradient.
- **Deliberate constraint.** Mosby's Files took SOTD with two scripts, no canvas, and two typefaces. Constraint is legible as intention.
- **Real photography.** Team photos. Blades. Cold hands. Fog on the Charles. A single genuine 6am photograph beats any generated hero image, and jurors score Content on exactly this.
- **Idiosyncratic type.** ILLOCA drew a bespoke family with a *rule-marker cut*. You cannot buy that. But you can pick a face that nobody uses, and use its weird features on purpose.
- **Editorial density.** More real information per screen. Vox's whole credibility argument.
- **Imperfection with intent.** A hand-drawn diagram, a scanned team photo with the fold visible, a result sheet in its original typeface.
- **Specificity of content.** This is the biggest one. "The engine room" is specific. "Excellence in athletics" is slop. Your prototype already gets this right: *"a bad stroke seat makes seven other people slow"* is a real sentence that only someone who has rowed would write. Protect that voice everywhere.

### 4.6 Automated gates you can actually run

```bash
# Visual slop, deterministic, 27 rules, no LLM, no API key
npx impeccable detect src/
npx impeccable detect index.html
npx impeccable detect https://your-staging-url.com

# Prose slop as a CI gate (sloplint, from the soundshuman/humanize toolchain)
sloplint scan content/ --fail-above 50
```

Wire `npx impeccable detect` into CI on the `src/` directory. It is deterministic, so it will not flap.

---

## Part 5 — Typography

Constraints: free or open-source, self-hostable, **not Inter / Poppins / Montserrat / Roboto**. Rowing times need **tabular figures** (`font-feature-settings: "tnum" 1;` or `font-variant-numeric: tabular-nums;`) so that 5:38.2 and 6:11.9 align in a results table.

### 5.1 Display / high-impact condensed or grotesque

**Big Shoulders** — *primary recommendation*
- Get: <https://fonts.google.com/specimen/Big+Shoulders> · source <https://github.com/xotypeco/big_shoulders>
- License: **SIL OFL 1.1**
- Designer: Patric King, XOType, for the Chicago Design System
- Why: a **condensed American Gothic variable superfamily** with Display, Text, **Inline**, and **Stencil** cuts. Explicitly rooted in railway transport, public political action, and dance. It is tall, narrow, athletic, and carries civic-institutional weight without being a generic sports condensed. The Stencil and Inline cuts give you a second and third register for free, which is the "three optical cuts of one family" move that Trevor Noah and ILLOCA both use.
- Rowing fit: a boat is 60ft long and 25in wide. Condensed type is the typographic form of that proportion.
- Numerals: **[verify]** run the fonttools check in 5.6.

**Archivo / Archivo Narrow / Archivo Expanded** — *the safe strong choice, and what your prototype already uses*
- Get: <https://fonts.google.com/specimen/Archivo> · <https://www.omnibus-type.com/fonts/archivo/>
- License: **SIL OFL 1.1**. Designer Héctor Gatti, Omnibus-Type, Buenos Aires
- Why: grotesque sans built for print and screen simultaneously, "reminiscent of late nineteenth century American typefaces," 200+ languages, **variable with both weight (100–900) and width axes**. Your prototype uses it at weight 900 with −0.035em tracking, which is correct.
- Note: Archivo is legitimately good but it is also *becoming* a common editorial default. If you keep it, differentiate by exploiting the **width axis** hard (Archivo Expanded for section numbers, Narrow for dense data) rather than only the weight axis.

**Anybody** — *the risky, distinctive pick*
- Get: <https://fonts.google.com/specimen/Anybody> · <https://etceteratype.co/anybody>
- License: **SIL OFL 1.1**. Tyler Finck, Etcetera Type Company
- Why: Eurostile lineage with a heavy dose of 90s, **width axis 50–150** (UltraCondensed to ExtraExpanded), weight 100–900, high x-height, low cap height. The extreme widths are exaggerated by design. 10° italic.
- Rowing fit: this is the closest free face to a 1990s regatta program / boathouse signage aesthetic. Pairs naturally with a Decathlon-Yestalgia-style archive treatment.

**Bricolage Grotesque** — *if you want character over impact*
- Get: <https://fonts.google.com/specimen/Bricolage+Grotesque> · <https://ateliertriay.github.io/bricolage/>
- License: **SIL OFL 1.1**. Mathieu Triay
- Why: **three axes — weight, width, and optical size.** Self-described as "French attitude and British mannerisms." Genuinely idiosyncratic rather than neutral, which is exactly what section 4.5 asks for. The optical-size axis means your 100px headline and your 14px caption get different letterforms automatically.

**Also worth auditioning:** Velvetyne's catalog (<https://velvetyne.fr>) — **Anthony**, **Basteleur**, **Terminal Grotesque**, all OFL, all genuinely strange. Collletttivo's **Apfel Grotezk** (<https://www.collletttivo.it/typefaces/apfel-grotezk>, OFL, round and airy neo-grotesque). Fontshare (<https://www.fontshare.com>) has **Khand**, **Clash Display**, **Bespoke Stencil** — free for commercial use under the **ITF Free Font License**, which is *not* OFL; read it before shipping **[verify]**.

### 5.2 Workhorse text face with real character

**Newsreader** — *primary recommendation*
- Get: <https://fonts.google.com/specimen/Newsreader> · <https://productiontype.com/family/newsreader>
- License: **SIL OFL 1.1**. Production Type
- Why: designed by a serious commercial foundry *specifically for continuous on-screen reading in content-rich environments*. **Two axes: optical size 6–72 and weight 200–800.** The optical-size axis is the thing premium editorial families charge for. Caption, Text, and Display cuts from one file.
- This is your Harriet substitute, and it is a better argument than Source Serif 4 (which your prototype currently uses and which is fine but less distinctive).

**Fraunces** — *if the site should feel warmer and more hand-made*
- Get: <https://fonts.google.com/specimen/Fraunces> · <https://fraunces.undercase.xyz/>
- License: **SIL OFL 1.1**. Undercase Type (Phaedra Charles, Flavia Zimbardi)
- Why: an "Old Style" family with **`SOFT` and `WONK` axes** in addition to weight and optical size. The `WONK` axis literally dials in eccentric letterforms. Nothing reads less machine-generated than a typeface with a wonk axis.
- Caution: high personality. Use for pull quotes and section openers, not for 800 words of body copy.

**Instrument Serif / Instrument Sans** — worth auditioning as a pairing, both OFL, both on Google Fonts **[verify current availability]**.

### 5.3 Monospace for data, splits, and race times

**Martian Mono** — *primary recommendation*
- Get: <https://fonts.google.com/specimen/Martian+Mono> · <https://github.com/evilmartians/mono>
- License: **SIL OFL 1.1**. Evil Martians
- Why: monospaced cut of Martian Grotesk. **Two axes: width (Condensed → SemiExpanded) and weight (Thin → ExtraBold)** — rare for a mono. 28 static styles. Described by its makers as brutal and eye-catching, with metrics equilibrium.
- Rowing fit: **monospace guarantees tabular figures by definition.** Every digit is the same width, so a results table aligns without any OpenType feature at all. Use Condensed for dense split tables, SemiExpanded for a hero time.

**Alternatives:** **IBM Plex Mono** (OFL, the neutral choice, more legible at small sizes), **Fragment Mono** and **Geist Mono** (both OFL, both observed on the SOTD-winning stateofaidesign.com), **Sligoil** from Velvetyne (OFL, much more characterful).

### 5.4 The recommended stack for CRLS

```css
/* Display: condensed civic-athletic. Exploit the width axis. */
--font-display: 'Big Shoulders Display', 'Archivo Expanded', 'Arial Narrow', sans-serif;

/* Text: optical-size-aware editorial serif. */
--font-text: 'Newsreader', Georgia, serif;

/* Data: splits, race times, seat numbers, dates, labels. */
--font-data: 'Martian Mono', ui-monospace, 'SFMono-Regular', monospace;
```

Three families, three jobs, mirroring the Balto / Harriet / Roboto Mono structure without borrowing its look. The mono carries the uppercase kicker role at ~11–12px with ~0.09em tracking, which is the Vox move worth stealing verbatim.

### 5.5 Tabular figures, non-negotiable for race results

```css
.result-time,
.split,
table td,
.stat-number {
  font-variant-numeric: tabular-nums lining-nums;
  font-feature-settings: "tnum" 1, "lnum" 1;
  font-variant-ligatures: none;   /* stop 5:38 forming odd ligatures in display faces */
}

/* Slashed zero if the face has it — prevents 0/O confusion in bow numbers */
.bow-number { font-feature-settings: "tnum" 1, "zero" 1; }
```

Also set `font-variant-numeric: tabular-nums` on any element whose number *changes* (a scroll-driven distance counter, an animated stat) or the layout will visibly jitter as digits swap width. This is a real bug jurors notice.

### 5.6 Verify tabular figures before committing

Do not trust a specimen page. Check the actual font binary:

```bash
python3 -m venv .venv && . .venv/bin/activate && pip install fonttools

# List every OpenType feature in the file. Look for 'tnum', 'lnum', 'zero'.
python3 - <<'PY'
from fontTools.ttLib import TTFont
import sys, glob
for path in glob.glob("public/fonts/*.[wot][ot][fft]*"):
    f = TTFont(path)
    feats = set()
    for tag in ("GSUB","GPOS"):
        if tag in f:
            for fr in f[tag].table.FeatureList.FeatureRecord:
                feats.add(fr.FeatureTag)
    print(f"{path:50s} tnum={'tnum' in feats} lnum={'lnum' in feats} zero={'zero' in feats}")
    print("   all:", " ".join(sorted(feats)))
PY
```

If `tnum` is absent, either pick a different face for numbers or use the mono for all figures. Do not ship a results table with proportional digits.

### 5.7 Self-hosting

Self-host. 28% of sites now self-host fonts exclusively. It removes a third-party request, kills the CORS/privacy question, and lets you subset.

```bash
pip install "fonttools[woff]" brotli
# Subset to Latin + the punctuation and figures you actually use
pyftsubset BigShouldersDisplay.ttf \
  --unicodes="U+0000-00FF,U+2000-206F,U+2070-209F,U+2190-21FF,U+2212" \
  --layout-features="kern,liga,tnum,lnum,zero,ss01" \
  --flavor=woff2 --output-file=big-shoulders.subset.woff2
```

```css
@font-face {
  font-family: 'Big Shoulders Display';
  src: url('/fonts/big-shoulders.subset.woff2') format('woff2-variations');
  font-weight: 100 900;
  font-display: swap;          /* or 'optional' if CLS matters more than FOUT */
  font-style: normal;
}
```

Preload only the one face used above the fold:
```html
<link rel="preload" href="/fonts/big-shoulders.subset.woff2" as="font" type="font/woff2" crossorigin>
```

---

## Part 6 — Technical craft

### 6.1 Smooth scroll: Lenis

Repo: <https://github.com/darkroomengineering/lenis>. Note the packages `@studio-freight/react-lenis` and `@studio-freight/hamo` were **retired** when Studio Freight became Darkroom Engineering. Use `lenis` and `lenis/react`.

The single most important detail: **Lenis and GSAP must share one rAF loop**, or pins jump, triggers fire at the wrong scroll positions, and scrubbing desyncs.

```js
import Lenis from 'lenis'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
gsap.registerPlugin(ScrollTrigger)

const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),  // expo-out
  smoothWheel: true,
  syncTouch: false,      // leave native inertia on touch; syncTouch feels wrong on iOS
})

// 1. ScrollTrigger reads position from Lenis
lenis.on('scroll', ScrollTrigger.update)

// 2. GSAP's ticker drives Lenis — one loop for the whole page
gsap.ticker.add((time) => lenis.raf(time * 1000))
gsap.ticker.lagSmoothing(0)

// 3. Expose stop/start for modals, menus, lightboxes
export const stopScroll  = () => lenis.stop()
export const startScroll = () => lenis.start()
```

**Mandatory reduced-motion escape hatch:**
```js
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  lenis.destroy()
  document.documentElement.style.scrollBehavior = 'auto'
}
```
Skipping this is one of the specific things the developer jury penalizes.

### 6.2 Scroll-driven animation: GSAP vs native CSS

**Native CSS scroll-driven animations** (`animation-timeline: scroll()` / `view()`), support as of 2026 per caniuse:

| Browser | Status |
|---|---|
| Chrome / Edge | ✅ 115+ |
| Opera | ✅ 101+ |
| Safari (desktop + iOS) | ✅ **26.0+** |
| Firefox | ❌ still behind `layout.css.scroll-driven-animations.enabled` as of 155+ |

Sources: <https://caniuse.com/wf-scroll-driven-animations>, <https://developer.chrome.com/blog/css-ui-ecommerce-sda>

**The decision:**
- **Use native CSS** for simple, self-contained reveals: fade-in-on-enter, progress bars, sticky-header shrink, image parallax within its own container. It runs on the **compositor thread** at 60fps with zero JS and zero bundle cost. `animation-timeline` is ignored by non-supporting browsers, so the fallback is just "the element sits in its final state" if you set `animation-fill-mode: both`.
- **Use GSAP ScrollTrigger** for anything with `pin`, `scrub`, or cross-element choreography. There is no native equivalent for pinning a section while a timeline scrubs.
- Guard native usage with `@supports (animation-timeline: scroll())`.

```css
@supports (animation-timeline: view()) {
  .reveal {
    animation: reveal linear both;
    animation-timeline: view();
    animation-range: entry 15% cover 40%;
  }
}
@keyframes reveal {
  from { opacity: 0; clip-path: inset(45% 20% 45% 20%); }
  to   { opacity: 1; clip-path: inset(0% 0% 0% 0%); }
}
```

**ScrollTrigger rules that matter:**
```js
gsap.timeline({
  scrollTrigger: {
    trigger: '.stroke-cycle',
    start: 'top top',
    end: '+=2000',
    pin: true,
    scrub: 1,           // 1s catch-up. Never combine scrub with toggleActions.
    invalidateOnRefresh: true,
  }
})
```
- Animate **transform and opacity only** (`x`, `y`, `scale`, `rotation`, `autoAlpha`). These stay on the compositor. Never animate `width`, `height`, `top`, `left`, `margin`, or `padding` — they trigger layout.
- Use `scrub` for scroll-linked progress **or** `toggleActions` for discrete play/reverse. Not both on the same trigger.
- For high-frequency updates like a cursor follower, use `gsap.quickTo()`, not `gsap.to()` per frame.
- `will-change: transform` on pinned elements only, and remove it after. Leaving it on everything costs memory.
- Use `gsap.context()` / `createScope` per component and `revert()` on cleanup so triggers do not leak across route changes.

### 6.3 Three.js hero setup

The non-negotiable renderer configuration. Getting either of the first two lines wrong is why most amateur WebGL looks flat and washed out:

```js
import * as THREE from 'three'
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js'
import { RGBELoader } from 'three/addons/loaders/RGBELoader.js'

const renderer = new THREE.WebGLRenderer({
  antialias: true,
  alpha: false,
  powerPreference: 'high-performance',
})

// --- The two lines that decide whether it looks pro ---
renderer.toneMapping        = THREE.ACESFilmicToneMapping
renderer.outputColorSpace   = THREE.SRGBColorSpace
renderer.toneMappingExposure = 1.0

// Cap DPR. 2 is plenty; 3 on a modern phone quadruples fragment cost for no visible gain.
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
renderer.setSize(container.clientWidth, container.clientHeight)
```

**Environment lighting.** `metalness > 0` with no environment map renders as a black blob. Always provide one:

```js
const pmrem = new THREE.PMREMGenerator(renderer)
pmrem.compileEquirectangularShader()

// Option A — free, zero network cost, good enough for most marketing heroes
scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture

// Option B — a real HDRI when you need specific reflections (river, sky, boathouse)
new RGBELoader().load('/hdri/charles-river-1k.hdr', (hdr) => {
  hdr.mapping = THREE.EquirectangularReflectionMapping
  scene.environment = pmrem.fromEquirectangular(hdr).texture
  hdr.dispose()
  pmrem.dispose()
})
```
Use a **1k or 2k HDRI**, never 4k, for web. A 4k HDR is 20–40MB.

**Shadows.** Real-time shadow maps are the most common performance sink. For a single hero object:
- **Preferred:** bake a soft contact shadow into a texture on a plane, or use `three/addons/objects/Sky.js` + a `ContactShadows`-style setup. Zero per-frame cost.
- **If you need dynamic:** one `DirectionalLight` with `castShadow`, `shadow.mapSize` at `1024` (not 2048), `shadow.camera` frustum tightened to the object's bounding box, `PCFSoftShadowMap`. One shadow-casting light, never three.

**Performance budget for a marketing hero:**

| Metric | Target |
|---|---|
| Draw calls | **< 100**, ideally < 30 |
| Triangles | **< 250k** for a hero object |
| Texture memory | **< 40MB** total |
| DPR | capped at **2** |
| Frame time | **< 16.6ms** on desktop, **< 33ms** on a mid-tier Android |
| WebGL bundle | keep three + addons under **~180KB gzipped** by importing from `three/addons/` selectively, never `import * from 'three/examples'` |
| Model format | **glTF + Draco or Meshopt**, KTX2/Basis for textures |

**Mount just-in-time.** Every winner that ships WebGL does this. Never create a context on page load:

```js
const io = new IntersectionObserver(([entry]) => {
  if (entry.isIntersecting) mountGL()
  else disposeGL()                    // renderer.dispose(), geometry.dispose(), texture.dispose()
}, { rootMargin: '200px' })
io.observe(canvasSection)
```

**Test on a real mid-tier Android** before declaring done, not on DevTools throttling.

### 6.4 The loading sequence

What award sites actually do, and where the amateur version goes wrong:

- **The loader must be shorter than the content it hides.** A 6-second loader on a 1.2-second page is theater and jurors read it as such. If the assets genuinely need 3 seconds, the loader earns 3 seconds.
- **Make the progress real.** Drive it from `THREE.DefaultLoadingManager.onProgress` or a font/image `Promise.all`, not a fake `setInterval`. Fake progress that hits 100% then waits is immediately obvious.
- **The loader should be the first frame of the design, not a spinner.** A counter in the mono face, the wordmark assembling, a single rule extending. It establishes the type system before the page arrives.
- **Hand off with a transition, not a cut.** The loader element should animate into the hero (a clip-path wipe, a scale-and-fade of the counter into the H1 position). This is where GSAP `CustomEase` earns its place: define one signature curve and use it here and on every page transition.
- **Render meaningful HTML underneath.** The loader is an overlay on a real page, so the site still works with JS disabled and LCP is not blocked on the animation.
- **Skip it entirely for returning visitors** (`sessionStorage` flag) and **skip it entirely under `prefers-reduced-motion`**.

### 6.5 Accessibility the Awwwards developer jury actually checks

These are named explicitly in jury guidance as things read as carelessness.

**Reduced motion.** Do not use a blanket kill switch that removes all feedback. WCAG 2.1 SC 2.3.3. Replace motion with a crossfade:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
And in JS: destroy Lenis, skip the loader, set ScrollTrigger animations to their end state rather than scrubbing them.

Your prototype has `@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}` — correct instinct, but `transition: none` removes state feedback entirely. Prefer the near-zero-duration form above so hover and focus states still register.

**Focus.** WCAG 2.2 SC 2.4.7. Never `outline: none` without a replacement.
```css
:where(a, button, input, select, textarea, [tabindex]):focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
/* forced-colors fallback so the ring survives Windows High Contrast */
@media (forced-colors: active) {
  :where(a, button, [tabindex]):focus-visible { outline: 2px solid CanvasText; }
}
```
`:focus-visible` fires for keyboard navigation and not for mouse clicks, which removes the old aesthetic objection entirely. Contrast the ring at **3:1 minimum** against its background.

**Custom cursors.** Roughly half the winners use one. The specific penalty named by jurors is *"a custom cursor that hides the real one."* If you build one:
- Never set `cursor: none` globally without a visible replacement that tracks reliably.
- Disable it entirely on touch (`@media (hover: none)`) and under reduced motion.
- Keep the native cursor on form fields and text.

**Keyboard.**
- Every interactive element reachable by Tab in visual order.
- A visible skip link to main content.
- Scroll-jacked sections must still respond to `PageDown`, `Space`, `Home`, `End`, and arrow keys. Lenis handles this; verify it after you add pins.
- Interactive SVG elements (your `.seatg` seat hotspots) need `tabindex="0"`, `role="button"`, an `aria-label`, and a `keydown` handler for Enter and Space. **Your prototype currently binds `mouseenter` and `click` only, so the seat diagram is entirely unusable by keyboard.** That is a direct, findable Usability deduction.

**Contrast.** 4.5:1 for body text, 3:1 for large text and UI components. Check your `--muted:#6b6d75` on `--wash:#f4f4f2` **[verify]** and any text placed on the accent color.

**Motion safety.** No parallax exceeding roughly 20% of viewport height on background elements. No autoplaying video with motion above the fold without a pause control.

---

## Part 7 — Scoring rubric

Score the site out of 100. Mapped to Awwwards' published weights so the total is directly comparable. Anything scoring below 70 will not clear Honorable Mention; SOTD territory starts around 85.

### A. Design — 40 points

| # | Criterion | Pts |
|---|---|---|
| A1 | **One named art direction.** The direction can be stated in one sentence with 3–5 defining moves. Static frames still look authored with all motion removed. | 6 |
| A2 | **Typographic system.** ≥3 distinct registers (display / text / data). A consistent modular scale. Negative tracking applied at display sizes. Optical sizing used if the family has it. | 6 |
| A3 | **Type is the primary event somewhere.** At least one headline above 100px at desktop, set with intent. | 3 |
| A4 | **Color discipline.** One dominant ground, one accent. Accent appears fewer than ~15 times per page and never as body text. No gradient used as a substitute for a decision. | 5 |
| A5 | **Grid with tension.** Asymmetry present. Not everything centered. The grid means something about the subject (lanes, seats, splits), not just 12 columns. | 5 |
| A6 | **Elevation system is real.** Hairlines, bands, or genuine layering. Not `shadow-lg` on every card. | 3 |
| A7 | **Spatial hierarchy.** Spacing scale has ≥5 meaningfully different steps in use. Not uniform `gap-4` everywhere. | 3 |
| A8 | **Consistency across all breakpoints.** The type scale, grid, and hierarchy hold at 375px, 768px, 1440px, and 2560px. | 5 |
| A9 | **Detail craft.** Optical alignment corrected by hand. Hanging punctuation or optical margin where it matters. No orphans in headlines. | 4 |

### B. Usability — 30 points

| # | Criterion | Pts |
|---|---|---|
| B1 | **60fps sustained** during the heaviest scroll section on desktop; **≥30fps on a real mid-tier Android**. Measured, not assumed. | 6 |
| B2 | **Mobile is a first-class version**, not a shrunk desktop. Clears Google's mobile criteria at ≥70/100. | 6 |
| B3 | **`prefers-reduced-motion` fully honored.** Lenis destroyed, loader skipped, scrubs set to end state, crossfade instead of a total kill. | 4 |
| B4 | **Visible `:focus-visible` on every interactive element**, ≥3:1 contrast, with a `forced-colors` fallback. | 3 |
| B5 | **Full keyboard operability**, including interactive SVG and scroll-jacked sections. Skip link present. | 3 |
| B6 | **Contrast passes** 4.5:1 body / 3:1 large and UI, including text on the accent color. | 3 |
| B7 | **Navigation is legible.** A first-time visitor knows where they are and what else exists within 5 seconds. | 3 |
| B8 | **Load discipline.** LCP < 2.5s on 4G. Loader duration ≤ actual asset load. Progress is real. Bundle justified. | 2 |

### C. Creativity — 20 points

| # | Criterion | Pts |
|---|---|---|
| C1 | **The concept is specific to this subject** and could not be lifted onto a different client by swapping the logo. | 7 |
| C2 | **Motion is choreographed, not decorated.** A named signature easing curve reused throughout. Transitions carry meaning. | 5 |
| C3 | **At least one technique executed at a level that is genuinely hard**, whether a shader, a scrubbed sequence, a custom type treatment, or a CSS-only system. | 4 |
| C4 | **Not derivative.** Does not read as "current Awwwards trend" or as a recognizable clone of a known site (including Vox). | 4 |

### D. Content — 10 points

| # | Criterion | Pts |
|---|---|---|
| D1 | **Zero placeholder content.** No lorem ipsum, no `2,000m` sample stats standing in for real ones, no stock imagery. | 3 |
| D2 | **Real photography or original illustration.** Genuine team images, not generated or licensed generics. | 3 |
| D3 | **Copy has a specific voice.** Written by someone who knows the sport. Passes the anti-slop text check in section E. | 2 |
| D4 | **Content and design pull in the same direction.** The words, images, and motion are one argument, not a shell around text. | 2 |

### E. Anti-slop gate — pass/fail, applied before scoring

**Any single failure caps the total at 70 regardless of section scores.** These are absolutes.

**Visual**
- [ ] No purple/indigo/violet gradient anywhere
- [ ] No `background-clip: text` gradient headline
- [ ] No `backdrop-filter: blur()` without a real elevation system behind it
- [ ] No colored left border on cards (`border-left: 4px solid`)
- [ ] No centered hero → subhead → two buttons → three equal cards → CTA sequence
- [ ] No three-or-four identical cards in a row at equal weight
- [ ] No icon-in-a-rounded-square above headings
- [ ] No `rounded-2xl shadow-lg` applied uniformly
- [ ] Inter, Poppins, Montserrat, Roboto, and the bare system stack are all absent
- [ ] No oversized meaningless statistics ("100% commitment", "10x the effort")
- [ ] No emoji in headings or as feature bullets
- [ ] No arrow glyph welded to a CTA label ("Row with us →")
- [ ] No abstract SVG blobs, no gradient placeholder rectangles, no DiceBear avatars
- [ ] No `Sparkles` / `ArrowRight` / `Zap` lucide icons used as decoration
- [ ] Motion is not the identical `fade-in-up` on every element
- [ ] `npx impeccable detect src/` returns zero P0 findings

**Text**
- [ ] No AI-vocabulary cluster: delve, tapestry, testament, pivotal, vibrant, landscape, showcasing, underscore, fostering, robust, meticulous, seamless, elevate
- [ ] No "not just X, but Y" or "It's not X. It's Y."
- [ ] No default rule-of-three lists
- [ ] No superficial `-ing` clauses stapled to sentence ends ("…, highlighting the team's dedication")
- [ ] No vague attribution ("coaches say", "experts agree") without a named source
- [ ] No "Despite these challenges…" coda
- [ ] No copula avoidance: uses *is* and *has*, not *serves as* and *boasts*
- [ ] Sentence lengths vary. No three consecutive sentences of similar length.
- [ ] No em-dash clusters
- [ ] No bold mini-headings opening list items
- [ ] Sentence case in headings, not Title Case
- [ ] Every number, name, time, and date is real and verifiable. No invented statistics.

### F. Quick verdict bands

| Score | Reading |
|---|---|
| 90–100 | Site of the Day contender. Submit. |
| 80–89 | Strong Honorable Mention, one or two fixes from SOTD. |
| 70–79 | Honorable Mention range. Find the Usability leaks first, they are cheapest. |
| 55–69 | Good-looking but not award-grade. Usually a missing concept (C1) or a missing accessibility floor (B3–B6). |
| < 55 | Reads as templated. Run section E and fix every failure before scoring again. |

---

## Appendix — immediate actions on the existing prototype

Reading `Vox Style.html` against this dossier:

**Keep**
- The numbered section heads (`.snum`), the hairline `1px` grid on `.fleet` / `.cycle` / `.strip`, the 3px masthead rule, and the zero-radius geometry. That is the Vox grammar done right.
- The voice. *"a bad stroke seat makes seven other people slow"* and *"nowhere to hide"* are exactly the specificity section 4.5 asks for.
- `font-variant-numeric` is not yet set anywhere. Add it to `.st .n`, `.readout .rnum`, and any results table.

**Fix**
1. `.seatg` seat hotspots bind `mouseenter` and `click` only. Add `tabindex="0"`, `role="button"`, `aria-label`, and Enter/Space handling. Currently keyboard-inaccessible. **B5 failure.**
2. `--accent:#fff100` is Vox's yellow off by one digit. Either match `#fff200` and accept the clone reading, or replace it with a color owned by the team. Recommend the latter. **C4 risk.**
3. `@media(prefers-reduced-motion:reduce){*{transition:none}}` kills state feedback. Use the near-zero-duration form in 6.5.
4. `.strip` numbers are placeholder ("Placeholder figures"). **D1 failure until real CRLS results are in.**
5. `.cta:hover{transform:translate(-2px,-2px);box-shadow:4px 4px 0 var(--ink)}` is the one hard-shadow moment in an otherwise shadowless system. Either commit to hard offset shadows as a system or remove this one.
6. `.cycle` is four static frames. Convert to a scroll-scrubbed sequence per 3.1. Highest-leverage single change in the file.

**Add**
- Big Shoulders Display or Archivo Expanded for the display register, self-hosted and subset, replacing the Google Fonts CDN link.
- Martian Mono for `.kicker`, `.bmeta`, `.fcap`, and all figures.
- A 2000m scroll-distance anchor as the progress device.
- Real photography. It is worth more than any WebGL you could add.
