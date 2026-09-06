/**
 * Site content, distilled from the research in /research.
 *
 * RULES FOR THIS FILE
 *   - Every factual claim carries a `src` (a URL) or is marked `unverified`.
 *   - Numbers come from the scraped archive, not from memory.
 *   - Where the team's own history and the primary record disagree, both are
 *     shown. See `history` entries with a `note`.
 *
 * Archive: 1,321 race records, 2007-2026, from row2k, NEIRA, MPSRA/HereNow and
 * USRowing time-team results. 394 first-place finishes. 186 named athletes.
 */

export const SOURCES = {
  crls: 'https://crlsrowing.org/about/history-of-the-program/',
  neira: 'http://neira.qra.org/',
  row2k: 'https://www.row2k.com/results/index.cfm?league=NEIRA',
  mpsra: 'http://mpsra.org/',
  cambridgeDay: 'https://www.cambridgeday.com/2026/05/28/crew-teams-shine-championships/',
  crimson1922: 'https://www.thecrimson.com/article/1922/5/22/schoolboy-crews-race-on-charles-pthe/',
  crimson1926: 'https://www.thecrimson.com/article/1926/6/2/rindge-technical-victor-as-public-school/',
  crimson1929: 'https://www.thecrimson.com/article/1929/3/23/schoolboys-to-compete-in-annual-regatta/',
  pocock: 'https://www.pocock.com/shells/hypercarbon-comp-k4',
  instagram: 'https://www.instagram.com/crlscrew/',
};

/* ------------------------------------------------------------------ *
 * The spine of the story
 * ------------------------------------------------------------------ */
export const CHAPTERS = [
  { id: 'river', num: '01', title: 'The Charles', kicker: 'Where it happens' },
  { id: 'then', num: '02', title: 'One Heat', kicker: '1889 – 1929' },
  { id: 'gap', num: '03', title: 'Sixty Years', kicker: '1929 – 1989' },
  { id: 'return', num: '04', title: 'Borrowed Colors', kicker: '1989 – 2000' },
  { id: 'fleet', num: '05', title: 'The Fleet', kicker: 'What they row' },
  { id: 'record', num: '06', title: 'The Record', kicker: '1,321 races' },
  { id: 'now', num: '07', title: 'Best Season', kicker: '2026' },
  { id: 'free', num: '08', title: 'No Fee', kicker: 'Why it matters' },
];

/* ------------------------------------------------------------------ *
 * History — the long arc
 * ------------------------------------------------------------------ */
export const HISTORY = [
  {
    year: '1640s',
    title: 'A Latin school in Cambridge',
    body: `Cambridge sets up a public grammar school under Master Elijah Corlett. The
    program's own history dates it to 1643 and calls it the second public high school in
    what became the United States; other records put the town's school at 1648. Either
    way, the institution these rowers belong to is older than the country by more than a
    century.`,
    note: 'The program says 1643. Wikipedia and the school\'s motto page say 1648. Shown as disputed rather than resolved.',
    aside: [
      ['Corlett&rsquo;s school', 'The &ldquo;lattin schoole&rdquo;'],
      ['Cambridge was', 'The fifth town in the colony to found one'],
      ['After', 'Boston, Charlestown, Dorchester, Salem'],
      ['Founding date', '1643 per the program; 1648 per the town record'],
    ],
    src: SOURCES.crls,
  },
  {
    year: '1889',
    title: 'Cambridge Latin takes to the water',
    body: `The Cambridge Latin High crew begins racing. It is a small program, rowing
    fours against Rindge Technical School and Browne & Nichols — schools that sat within
    a mile of each other on either side of the river.`,
    note: 'The 1889 start date comes from the program\'s own history. No independent source was found for that specific year, though the era itself is well documented.',
    aside: [
      ['Course', 'The Charles, downstream'],
      ['By 1899 the league held', 'Twelve schools in and around Boston'],
      ['Public', 'Cambridge, English, Waltham, Brookline, Boston Latin'],
      ['Private', 'Nobles, B&amp;N, Volkmann&rsquo;s, Stone&rsquo;s, Chauncy Hall'],
      ['Run by', 'The Interscholastic Rowing Association, under the B.A.A.'],
    ],
    src: SOURCES.crls,
  },
  {
    year: '1903',
    title: 'The fastest schoolboy crew on the river',
    body: `Cambridge Latin wins its heat of the Interscholastic Rowing Association
    championship in 5 minutes 33 seconds over a mile of downstream Charles, taking nine
    seconds off the interscholastic record. Three heats went off that afternoon, four
    crews in each. The other two were won by Boston Latin and Waltham High \u2014 all three
    public schools.`,
    aside: [
      ['Time', '5:33'],
      ['Course', 'Hereford Street to the coal yard by Cottage Farm Bridge'],
      ['That bridge today', 'The BU Bridge'],
      ['Other heat winners', 'Boston Latin, Waltham &mdash; also public schools'],
      ['Recorded in', 'The Harvard Crimson, 28 May 1903'],
    ],
    src: 'https://www.thecrimson.com/article/1903/5/28/school-rowing-record-lowered-pthe-preliminary/',
  },
  {
    year: '1922',
    title: 'Three schools, one afternoon, in the rain',
    body: `The Harvard Crimson records Cambridge Latin, Rindge Technical and Browne &
    Nichols racing on the Charles on the same rainy afternoon. Rindge Tech loses the
    Harvard Challenge Cup by two feet.`,
    aside: [
      ['Distance', 'Half a mile'],
      ['Withdrew', 'Noble and Greenough, Huntington'],
      ['Second fours order', 'B&amp;N, Cambridge Latin, Tabor, Rindge'],
      ['First fours order', 'B&amp;N, Rindge, Nobles, Cambridge Latin, Tabor'],
      ['Recorded in', 'The Harvard Crimson, 19 May 1922'],
    ],
    src: SOURCES.crimson1922,
  },
  {
    year: '1926',
    title: 'The public schools get their own regatta',
    body: `Rindge Technical wins the first regatta held by the new Schoolboy Rowing
    Association, then races the private-school crews the following day.`,
    aside: [
      ['Replaced', 'The schoolboy races at the Harvard Invitation Regatta'],
      ['Undercard', 'Belmont Hill beat Nobles by four feet'],
      ['Medals from', 'The Harvard Athletic Association'],
      ['Crimson headline', '&ldquo;Public school eights race&rdquo;'],
      ['Recorded in', 'The Harvard Crimson, 2 June 1926'],
    ],
    src: SOURCES.crimson1926,
  },
  {
    year: '1929',
    title: 'The eights were separated. The fours were not.',
    body: `In the last documented Schoolboy Regatta of the era, the eights were split into
    separate public-school and private-school heats. The fours — the boat Cambridge rowed —
    raced everyone together, in one heat. A public-school four lining up against the prep
    schools on equal terms is not a modern idea. It is the oldest thing about this program.`,
    pull: true,
    src: SOURCES.crimson1929,
  },
  {
    year: '1929',
    title: 'And then it stopped',
    body: `The program's history holds that the stock market crash ended the crew. The
    timing is tight: the regatta was scheduled for June 1st, and the market broke that
    October. Whatever ended it, the boats went away and did not come back for sixty years.`,
    note: 'Causation is the program\'s account, not a documented fact. The 1929 season preceded the crash.',
    aside: [
      ['Regatta scheduled', '1 June 1929'],
      ['Market broke', 'That October &mdash; four months later'],
      ['Cause', 'The program&rsquo;s own account; unverified'],
      ['Next CRLS crew', '1989'],
    ],
    src: SOURCES.crls,
  },
  {
    year: '1978',
    title: 'Two schools become one',
    body: `Cambridge High & Latin merges with the Rindge Technical School. The two crews
    that used to race each other are now the same school. Most sources date the merger to
    1977.`,
    note: 'The rowing history page says 1978; Wikipedia, History Cambridge and the Crimson all say 1977.',
    aside: [
      ['A four-way merger', 'Latin, Rindge Tech, Pilot, Fundamental'],
      ['Date disputed', 'Program says 1978; three sources say 1977'],
      ['Rowing at the time', 'None, and none for another eleven years'],
    ],
    src: SOURCES.crls,
  },
  {
    year: '1989',
    title: 'Rowing under someone else\'s name',
    body: `The program resurfaces as the Cambridge Rindge & Latin Crew Club, training with
    Community Rowing in Boston. For eleven years the crews race in another organization's
    name and another organization's colors. Teachers Linda Lipkin, Phyllis Bretholtz and
    Tobe Korsgren drive the kids to practice.`,
    aside: [
      ['Years since the last race', '60'],
      ['Status', 'A club, not yet a school team'],
      ['Often fielded', 'Complete eights'],
      ['Lasted under that name', 'Eleven years'],
    ],
    src: SOURCES.crls,
  },
  {
    year: '1999',
    title: 'A bay of their own',
    body: `Athletic Director Bill Bates and the coaches get a CRLS boat bay written into
    the remodeled Cambridge Boat Club. For the first time the program has somewhere to
    keep boats.`,
    aside: [
      ['The clubhouse holds', 'Seven boat bays; one is theirs'],
      ['Also gained', 'ADA entrance, showers, a library'],
      ['Stretch', 'The Powerhouse'],
      ['Years without a boathouse', '110'],
    ],
    src: SOURCES.crls,
  },
  {
    year: '2000',
    title: 'Twelve students and no equipment',
    body: `Spring 2000 is the first official season under CRLS's own name and colors. It
    starts in January as a part-time, non-racing program with twelve students who mostly
    cannot row. By March it is a six-day-a-week varsity program with fifty kids, five
    boats, five races and two coaches.`,
    pull: true,
    aside: [
      ['January', 'Part-time, non-racing'],
      ['By March', 'Six days a week, varsity'],
      ['First races', 'Five, that spring'],
    ],
    src: SOURCES.crls,
  },
];

/* ------------------------------------------------------------------ *
 * Season-by-season, computed from the scraped archive
 * ------------------------------------------------------------------ */
export const SEASONS = [
  { year: 2007, races: 13, wins: 0, podium: 11 },
  { year: 2008, races: 16, wins: 0, podium: 16 },
  { year: 2009, races: 24, wins: 4, podium: 24 },
  { year: 2010, races: 35, wins: 12, podium: 35 },
  { year: 2011, races: 37, wins: 11, podium: 28 },
  { year: 2012, races: 41, wins: 19, podium: 39 },
  { year: 2013, races: 27, wins: 6, podium: 22 },
  { year: 2014, races: 28, wins: 5, podium: 17 },
  { year: 2015, races: 110, wins: 55, podium: 79 },
  { year: 2016, races: 96, wins: 27, podium: 66 },
  { year: 2017, races: 111, wins: 28, podium: 58 },
  { year: 2018, races: 96, wins: 18, podium: 50 },
  { year: 2019, races: 102, wins: 23, podium: 56 },
  { year: 2020, races: 0, wins: 0, podium: 0, note: 'No season' },
  { year: 2021, races: 47, wins: 7, podium: 24 },
  { year: 2022, races: 110, wins: 34, podium: 67 },
  { year: 2023, races: 95, wins: 18, podium: 68 },
  { year: 2024, races: 127, wins: 39, podium: 85 },
  { year: 2025, races: 119, wins: 47, podium: 83 },
  { year: 2026, races: 87, wins: 41, podium: 82 },
];

export const ARCHIVE = {
  totalRaces: 1321,
  wins: 394,
  // Every name in the scraped archive is a coxswain: row2k, NEIRA and MPSRA
  // result tables record the entry and its cox, not the full crew. Calling
  // these "athletes" would overstate what the data contains.
  coxswains: 186,
  firstYear: 2007,
  lastYear: 2026,
  championshipRaces: 571,
  championshipWins: 173,
};

/* ------------------------------------------------------------------ *
 * 2026 — the season the team called its best
 * ------------------------------------------------------------------ */
export const MILESTONES_2026 = [
  {
    title: 'Girls 1V to Youth Nationals',
    detail: 'Third at the USRowing Northeast Regionals in 7:27.54 — the second time in school history a girls crew has gone to Nationals. The first was 2022.',
    crew: ['Laurel Moldrem', 'Sinead O\'Gorman-Jones', 'Imogen Wu', 'Isla Agnew'],
    cox: 'Ada LaMaster',
    time: '7:27.54',
    place: 3,
    // Road to the final, from the regatta's own timing data.
    road: [
      ['Time trial', '7:11.11', 3],
      ['Semifinal', '7:41.01', 2],
      ['Final A', '7:27.54', 3],
    ],
    src: SOURCES.cambridgeDay,
  },
  {
    title: 'Boys 1V to Youth Nationals',
    detail: 'Third at Regionals in 6:44.62 — the first CRLS boys crew at Nationals since 2018, and only the fourth in school history.',
    crew: ['Nicolas Karnath', 'Daniel Morland', 'Zeke Bittker', 'Mateus Verdi'],
    cox: 'Son Schneider',
    time: '6:44.62',
    place: 3,
    road: [
      ['Time trial', '6:28.31', 2],
      ['Semifinal', '7:00.06', 2],
      ['Final A', '6:44.62', 3],
    ],
    src: SOURCES.cambridgeDay,
  },
  {
    title: 'Girls 3V — second at NEIRA',
    detail: 'Silver at the New England championship in 6:24.415, behind Choate. CRLS was one of three public schools in the fours event.',
    crew: ['Kat Levitt', 'Nina Penagos-Esquitin', 'Beatrix Taylor', 'Jacqueline Long'],
    cox: 'Antonia Millan',
    time: '6:24.415',
    place: 2,
    src: SOURCES.neira,
  },
  {
    title: 'Boys 4V — third at NEIRA',
    detail: 'Bronze in 5:35.063, less than 1.3 seconds behind Brooks.',
    crew: ['Ethan Garcia', 'Peter Giakoumis', 'Rio Thielow', 'Roland De Sola'],
    cox: 'Akash Walter',
    time: '5:35.063',
    place: 3,
    src: SOURCES.neira,
  },
  {
    title: 'Fifth straight Girls Fours Points Trophy',
    detail: 'At the Massachusetts state championship: cups in the girls 1st novice 4+ and 1st varsity 4+, wins in the 2nd novice and 2nd varsity, and a 1-2-3 sweep of the 3rd varsity.',
    src: SOURCES.mpsra,
  },
  {
    title: 'Boys novice 8+ — a first',
    detail: 'The boys novice eight won the MPSRA cup for the first time in school history.',
    src: SOURCES.mpsra,
  },
];

/** The team's own words, from their Instagram. */
export const VOICE = [
  {
    text: 'Our third and fourth NEIRA medals in CRLS history. Our most successful season ever.',
    when: 'May 2026',
    src: SOURCES.instagram,
  },
  {
    text: 'CRLS is one of a handful of public schools that competes in this prestigious event.',
    when: 'May 2026',
    src: SOURCES.instagram,
  },
  {
    text: 'To the 17 seniors on our team — this is your moment. Come watch us fly.',
    when: 'May 2026',
    src: SOURCES.instagram,
  },
];

/* ------------------------------------------------------------------ *
 * The fleet
 * ------------------------------------------------------------------ */
/**
 * The fleet, as the team itself names it.
 *
 * Source: the coach's race-day lineup in "CRLS Crew - 5/23/2025 - NEIRA/MPSRA
 * Update #3", which assigns boats to crews as
 *   "Boat: | Wylde (white) | Og Res (black) | Usain (white)".
 *
 * That post is the only place in the program's entire public record where
 * individual shells are named — the site has no fleet page and no christening
 * posts. Builder and model are known for Wylde only; the others are listed with
 * what the source actually says and nothing more.
 */
export const FLEET = [
  {
    id: 'wylde',
    name: 'Wylde',
    builder: 'Pocock',
    model: 'Hypercarbon Comp K4+',
    type: 'Coxed four',
    hull: 'White',
    status: 'built',
    specs: [
      ['Length overall', '13.6 m'],
      ['Beam at saxboard', '55 cm'],
      ['Beam at waterline', '43.1 cm'],
      ['Waterline length', '12.65 m'],
      ['Racing minimum', '51 kg'],
      ['Coxswain', 'Bow-loaded'],
      ['Rigger', 'G7 carbon wing'],
      ['Spread', '85 cm'],
      ['Slide', '81 cm'],
    ],
    lineup: 'Girls 1st novice four, 23 May 2025',
    notes: `A bow-loader: the coxswain lies flat under the foredeck with their head just
    above the deck line, which drops the boat's centre of gravity and makes it easier to
    set. The stern is a closed deck running clean to a point. The wing rigger bolts across
    the top of both gunwales rather than to the sides — Pocock's argument is that it
    spreads the load better and keeps the hardware out of the water.`,
    src: SOURCES.pocock,
  },,
  {
    id: 'og-res',
    name: 'Og Res',
    hull: 'Black',
    type: 'Coxed four',
    status: 'named-only',
    lineup: 'Girls 2nd novice four, 23 May 2025',
    src: SOURCES.crls,
  },
  {
    id: 'usain',
    name: 'Usain',
    hull: 'White',
    type: 'Coxed four',
    status: 'named-only',
    lineup: 'Girls 3rd novice four, 23 May 2025',
    src: SOURCES.crls,
  }
];

/* ------------------------------------------------------------------ *
 * Program facts
 * ------------------------------------------------------------------ */
export const PROGRAM = {
  athletes: 90,
  fee: 0,
  home: 'Cambridge Boat Club',
  water: 'The Charles River',
  leagues: ['NEIRA', 'MPSRA'],
  seasons: 'Club sport in the fall, varsity in the spring',
  mascot: 'Falcons',
  motto: 'At Home on the Charles',
  src: 'https://crlsrowing.org/about/',
};

/** Schools CRLS races in NEIRA. Nearly all are private. */
export const RIVALS = [
  { name: 'Choate', kind: 'private' },
  { name: 'Nobles', kind: 'private' },
  { name: 'Belmont Hill', kind: 'private' },
  { name: 'Brooks', kind: 'private' },
  { name: 'Groton', kind: 'private' },
  { name: "St. Mark's", kind: 'private' },
  { name: 'Winsor', kind: 'private' },
  { name: 'BB&N', kind: 'private' },
  { name: 'Middlesex', kind: 'private' },
  { name: 'Deerfield', kind: 'private' },
  { name: 'Exeter', kind: 'private' },
  { name: 'Andover', kind: 'private' },
  { name: 'Taft', kind: 'private' },
  { name: 'Hotchkiss', kind: 'private' },
  { name: 'Berkshire', kind: 'private' },
  { name: 'NMH', kind: 'private' },
  { name: 'Pomfret', kind: 'private' },
  { name: 'Dexter Southfield', kind: 'private' },
  { name: 'CRLS', kind: 'public', us: true },
  { name: 'Boston Latin', kind: 'public' },
  { name: 'Brookline', kind: 'public' },
];
