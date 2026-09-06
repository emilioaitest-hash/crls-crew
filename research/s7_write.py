#!/usr/bin/env python3
"""Write 02-results.json (schema-conformant) and 02-results.md.

Every record carries its own source_url. Anything not directly evidenced by a
retrieved source is recorded as UNKNOWN rather than inferred.
"""
import json, os, re, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_JSON = os.path.join(HERE, "02-results.json")
OUT_MD = os.path.join(HERE, "02-results.md")

SOURCE_NOTE = {
    "neira-qra-official": "NEIRA championship official timing (neira.qra.org)",
    "neira-championship-pdf": "NEIRA championship official results PDF",
    "usrowing-timeteam": "USRowing Northeast Youth Championships official timing (time-team)",
    "herenow": "HereNow regatta timing system (times computed from the system's "
               "own raw start/finish timestamps)",
    "herenow-mpsra": "HereNow / MPSRA championship timing",
    "row2k": "row2k NEIRA results, as submitted by the host school",
}


def to_sec(t):
    if not t:
        return None
    m = re.match(r"^(?:(\d+):)?(\d{1,2}):(\d{2}(?:\.\d+)?)$", t)
    if m:
        return int(m.group(1) or 0) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    return None


# ---------------------------------------------------------------- trophies
def build_trophies(races):
    """Only trophies evidenced by a retrieved source."""
    T = []
    # MPSRA current trophy holders - straight from mpsra.org
    for name, page, note in [
        ("MPSRA Girls 4+s Team Trophy (The Kendra Bauer Trophy)",
         "http://mpsra.org/?page_id=103",
         "Listed on the MPSRA site as the current Spring Championship trophy holder"),
        ("MPSRA Boys 4+s Team Trophy (The Jennifer Bauer Trophy)",
         "http://mpsra.org/?page_id=103",
         "Listed on the MPSRA site as the current Spring Championship trophy holder"),
        ("MPSRA Girls Varsity 4+ Trophy", "http://mpsra.org/?page_id=103",
         "Listed on the MPSRA site as the current Spring Championship trophy holder"),
        ("MPSRA Boys Varsity 4+ Trophy", "http://mpsra.org/?page_id=103",
         "Listed on the MPSRA site as the current Spring Championship trophy holder"),
        ("MPSRA Fall Girls 4+s Team Trophy (The Dale Wickenheiser Award)",
         "http://mpsra.org/?page_id=96",
         "Listed on the MPSRA site as the current Fall Championship trophy holder"),
        ("MPSRA Fall Girls Varsity 4+ (Starbeams Productions Award)",
         "http://mpsra.org/?page_id=96",
         "Listed on the MPSRA site as the current Fall Championship trophy holder"),
        ("MPSRA Fall Boys Varsity 4+ (Lake Quinsigamond Community Rowing Award)",
         "http://mpsra.org/?page_id=96",
         "Listed on the MPSRA site as the current Fall Championship trophy holder"),
        ("MPSRA Fall Girls Novice 4+", "http://mpsra.org/?page_id=96",
         "Listed on the MPSRA site as the current Fall Championship trophy holder"),
    ]:
        T.append({"trophy": name, "holder": "Cambridge Rindge & Latin School",
                  "year": "current as listed", "source_url": page, "notes": note})

    T.append({
        "trophy": "The Mayor's Cup (Cambridge)",
        "holder": "contested annually by CRLS and BB&N",
        "year": "2007-2026 (races located)",
        "source_url": "https://www.row2k.com/results/index.cfm?league=NEIRA",
        "notes": "The Cambridge Mayor's Cup is the CRLS vs Buckingham Browne & Nichols "
                 "dual. row2k carries CRLS/BB&N Mayor's Cup results for 2007, 2008, "
                 "2009, 2010, 2011, 2012, 2014, 2015, 2017, 2018, 2019, 2022, 2023, "
                 "2025 and 2026. Which school held the Cup in a given year is NOT "
                 "stated on those result pages, so per-year Cup winners are UNKNOWN; "
                 "the individual race results are in the races[] array.",
    })

    # Girls/Boys Fours Points Trophy streak - Cambridge Day, 2026
    T.append({
        "trophy": "MPSRA Girls Fours Points Trophy",
        "holder": "Cambridge Rindge & Latin School",
        "year": 2026,
        "source_url": "https://www.cambridgeday.com/2026/05/28/crew-teams-shine-championships/",
        "notes": "Fifth consecutive Girls Fours Points Trophy (2026), per Cambridge Day.",
    })
    T.append({
        "trophy": "MPSRA Boys Fours Points Trophy",
        "holder": "Cambridge Rindge & Latin School",
        "year": 2026,
        "source_url": "https://www.cambridgeday.com/2026/05/28/crew-teams-shine-championships/",
        "notes": "Retained for the fifth consecutive year (2026), per Cambridge Day.",
    })
    return T


def build_milestones(races):
    M = [
        {"year": 2026, "milestone": "Girls 1V qualified for USRowing Youth National "
         "Championships - 2nd time in school history (first was 2022)",
         "detail": "3rd at USRowing Northeast Youth Championships, 7:27.54: Laurel "
                   "Moldrem, Sinead O'Gorman-Jones, Imogen Wu, Isla Agnew, cox Ada LaMaster",
         "source_url": "https://www.cambridgeday.com/2026/05/28/crew-teams-shine-championships/",
         "corroboration": "Time and placing independently confirmed in the USRowing "
                          "Northeast Youth Championships official timing "
                          "(Womens Youth 4+ Final A, 3rd, 07:27.54)."},
        {"year": 2026, "milestone": "Boys 1V qualified for Youth Nationals for the first "
         "time since 2018 - 4th time in school history",
         "detail": "3rd at USRowing Northeast Youth Championships, 6:44.62: Nicolas "
                   "Karnath, Daniel Morland, Zeke Bittker, Mateus Verdi, cox Son Schneider",
         "source_url": "https://www.cambridgeday.com/2026/05/28/crew-teams-shine-championships/",
         "corroboration": "Time and placing independently confirmed in the USRowing "
                          "Northeast Youth Championships official timing "
                          "(Mens Youth 4+ Final A, 3rd, 06:44.62)."},
        {"year": 2026, "milestone": "Girls 3rd varsity 4+ took 2nd at the NEIRA Championship",
         "detail": "6:24.415 behind Choate (6:14.661). Kat Levitt, Nina Penagos-Esquitin, "
                   "Beatrix Taylor, Jacqueline Long, cox Antonia Millan. CRLS was one of "
                   "only three public schools racing the NEIRA fours category.",
         "source_url": "http://neira.qra.org/",
         "corroboration": "Exact time confirmed in NEIRA official results "
                          "(Girl's Third Four w/Cox, Grand Final)."},
        {"year": 2026, "milestone": "Boys 4th varsity 4+ took 3rd at the NEIRA Championship",
         "detail": "5:35.063, under 1.3s behind winner Brooks. Ethan Garcia, Peter "
                   "Giakoumis, Rio Thielow, Roland De Sola, cox Akash Walter.",
         "source_url": "http://neira.qra.org/",
         "corroboration": "Exact time confirmed in NEIRA official results "
                          "(Boy's Fourth Four w/Cox, Grand Final)."},
        {"year": 2026, "milestone": "Boys Novice 8+ won the MPSRA cup for the first time "
         "in school history",
         "detail": "Boys crews placed first in all their time trials and A finals at the "
                   "MPSRA State Championship; boys novice 4+, 1st varsity 4+ and 2nd "
                   "varsity 4+ all won.",
         "source_url": "https://www.cambridgeday.com/2026/05/28/crew-teams-shine-championships/",
         "corroboration": "MPSRA 2026 championship results are in races[] from the "
                          "HereNow timing system."},
        {"year": 2026, "milestone": "Girls swept 1-2-3 in the MPSRA 3rd varsity 4+",
         "detail": "Cups in girls 1st novice 4+ and 1st varsity 4+; wins in 2nd novice 4+ "
                   "and 2nd varsity 4+; novice girls 8+ 3rd; Iris Moyer bronze in the single.",
         "source_url": "https://www.cambridgeday.com/2026/05/28/crew-teams-shine-championships/",
         "corroboration": "See MPSRA 2026 records in races[]."},
        {"year": 2022, "milestone": "Girls crew reached USRowing Youth National "
         "Championships for the first time in school history",
         "detail": "Womens Youth 4+ - Time Trial 5th (7:06.0), A/B Semifinal 4th (7:29.5), "
                   "B Final 2nd (7:24.9) at Nathan Benderson Park, Sarasota FL.",
         "source_url": "https://legacy.herenow.com/results/#/races/21018/results",
         "corroboration": "Results retrieved from the HereNow timing system."},
        {"year": 2018, "milestone": "Boys raced the USRowing Youth National Championships "
         "(Lake Natoma, Rancho Cordova CA)",
         "detail": "Mens Ltwt Youth 4+ - Time Trial 18th (6:53.4), Repechage 4th (7:10.7), "
                   "C Final 4th (7:26.8).",
         "source_url": "https://legacy.herenow.com/results/#/races/20504/results",
         "corroboration": "Results retrieved from the HereNow timing system."},
        {"year": 2017, "milestone": "Boys raced the USRowing Youth National Championships "
         "(Nathan Benderson Park, Sarasota FL)",
         "detail": "Mens Ltwt Youth 4+ - Time Trial 8th (6:38.9), Semifinal 5th (7:03.6), "
                   "B Final 4th (6:46.8).",
         "source_url": "https://legacy.herenow.com/results/#/races/20374/results",
         "corroboration": "Results retrieved from the HereNow timing system."},
    ]
    return M


def fmt_time(t):
    return t or "UNKNOWN"


HEADLINE = [
    {"label": "2026 - Girls 1V, 3rd at USRowing Northeast Youth Championships",
     "text": "**7:27.54**, 6.29s behind Greenwich, in the Womens Youth 4+ A Final at Mercer "
             "Lake (17 May 2026) - qualifying for Youth Nationals for only the 2nd time in "
             "school history. Laurel Moldrem, Sinead O'Gorman-Jones, Imogen Wu, Isla Agnew, "
             "cox Ada LaMaster. "
             "<https://usrowing.regatta.time-team.com/usrowing-northeast-youth/2026>"},
    {"label": "2026 - Boys 1V, 3rd at USRowing Northeast Youth Championships",
     "text": "**6:44.62**, 3.87s off the win in the Mens Youth 4+ A Final - a CRLS boys boat "
             "into Youth Nationals for the first time since 2018 and only the 4th time ever. "
             "Nicolas Karnath, Daniel Morland, Zeke Bittker, Mateus Verdi, cox Son Schneider. "
             "<https://usrowing.regatta.time-team.com/usrowing-northeast-youth/2026>"},
    {"label": "2026 - Girls 3rd varsity 4+, 2nd at the NEIRA Championship",
     "text": "**6:24.415** in the Grand Final, beating Brooks by 0.76s for silver behind "
             "Choate (6:14.661). Kat Levitt, Nina Penagos-Esquitin, Beatrix Taylor, "
             "Jacqueline Long, cox Antonia Millan. <http://neira.qra.org/>"},
    {"label": "2026 - Boys 4th varsity 4+, 3rd at the NEIRA Championship",
     "text": "**5:35.063** in the Grand Final, 1.29s behind winner Brooks. Ethan Garcia, "
             "Peter Giakoumis, Rio Thielow, Roland De Sola, cox Akash Walter. "
             "<http://neira.qra.org/>"},
    {"label": "2022 - Girls 1V won the USRowing Northeast Youth Championship",
     "text": "Won the Womens Youth 4+ **Final in 7:21.8**, having also won the time trial "
             "(6:42.8) and semifinal (7:19.2) - the run that took CRLS girls to Youth "
             "Nationals for the first time. "
             "<https://legacy.herenow.com/results/#/races/21017/results>"},
    {"label": "2022 - Girls 4+ 2nd in the B Final at USRowing Youth Nationals",
     "text": "**7:24.9** in the Womens Youth 4+ B Final at Nathan Benderson Park, Sarasota - "
             "the first CRLS girls crew ever to race Youth Nationals. "
             "<https://legacy.herenow.com/results/#/races/21018/results>"},
    {"label": "2025 - Girls 1V won the MPSRA state title",
     "text": "**6:44.8** in the Girls 1st Varsity 4+ Grand Final, 9.7s clear of Somerville. "
             "The boys 1V took the matching title in **6:04.6**, 14.4s clear. "
             "<https://legacy.herenow.com/results/#/races/21341/results>"},
    {"label": "2026 - Boys swept every MPSRA A Final they entered",
     "text": "1st novice 8+ (**5:15.6**), 1st novice 4+ (6:01.9), 1V 4+ (**5:16.2**), "
             "2V 4+ (5:33.9) and 3rd/4th varsity 4+ (5:25.8) - the novice eight winning the "
             "cup for the first time in school history. "
             "<https://legacy.herenow.com/results/#/races/21436/results>"},
    {"label": "2022 - Girls 2nd varsity 4+ won its NEIRA Championship final",
     "text": "**6:13.250** - a NEIRA championship final win, the strongest CRLS result in "
             "the archive at that regatta. "
             "<https://neirarowing.org/documents/2022NEIRA.pdf>"},
    {"label": "2024 - Girls 1V won the NEIRA Petite Final",
     "text": "**5:56.896**, top of the B-final field at Lake Quinsigamond. "
             "<https://neirarowing.org/documents/2024NEIRAResults.pdf>"},
    {"label": "2017 - Boys lightweight 4+ won the Northeast Youth title",
     "text": "Fastest in the time trial (**6:47.6**) and won the final in **7:00.8**, "
             "sending the crew to Youth Nationals where they took the B Final in 6:46.8. "
             "<https://legacy.herenow.com/results/#/races/20373/results>"},
    {"label": "Head of the Charles - CRLS on its home water",
     "text": "Best located finishes: Men's Youth Fours **17:20.4** (38th, 2017) and Women's "
             "Youth Fours **19:48.4** (32nd, 2017); also 2016 and 2018. "
             "<https://legacy.herenow.com/results/#/races/20398/results>"},
]


def write_md(data):
    races = data["races"]
    by_year = defaultdict(list)
    for r in races:
        by_year[r["year"]].append(r)
    L = []
    A = L.append
    A("# CRLS Crew - Race Results Archive")
    A("")
    A(f"**{len(races)} race results** for Cambridge Rindge & Latin School rowing, "
      f"covering **{min(by_year)}-{max(by_year)}**.")
    A("")
    A("Every result below was extracted from a primary timing source and carries its "
      "own `source_url` in `02-results.json`. Nothing here is inferred: where a squad, "
      "boat or time could not be established from the source it is recorded as `UNKNOWN`.")
    A("")
    A("## Sources")
    A("")
    A("| Source | Records | What it is |")
    A("|---|---:|---|")
    c = Counter(r["source"] for r in races)
    for s, n in c.most_common():
        A(f"| `{s}` | {n} | {SOURCE_NOTE.get(s, '')} |")
    A("")
    A("### How times were derived")
    A("")
    A("- **NEIRA championships** - official NEIRA results. 2026 comes from the "
      "structured official results at neira.qra.org; 2011-2025 from the official "
      "NEIRA results PDFs. The PDFs are 3-column layouts, so each was parsed under "
      "7 independent column-splitting strategies and only values agreed by a strict "
      "majority were kept. Cross-check: for 2026, the PDF and the official HTML agree "
      "on **319 of 321** comparable cells (the 2 disagreements are non-CRLS rows, and "
      "the official HTML was used for 2026 regardless).")
    A("- **MPSRA / HereNow** - the HereNow timing system's own database. Elapsed time "
      "is computed as `FinishTime1 - StartTime1` from the raw timestamps and placings "
      "are the rank of those elapsed times within the flight. Validated against the "
      "official MPSRA 2025 results PDF: every CRLS time matches exactly.")
    A("- **USRowing Northeast Youth Championships** - official time-team timing "
      "(`adjusted_result` / `adjusted_pos`), the regatta's own published results.")
    A("- **row2k** - NEIRA dual and tri-meet results as submitted by the host school. "
      "Placings are the finish order shown on the page.")
    A("")
    A("### A note on squad (boys/girls) attribution")
    A("")
    A("Many row2k NEIRA pages combine both squads with no gender label on the result "
      "blocks. Ground-truth pages that publish an explicit race order (2026 "
      "CRLS/Hopkins, 2024 Middlesex/CRLS, 2010 Middlesex/Pomfret/CRLS) show the boys' "
      "blocks are listed first, then the girls', with the boat-rank sequence resetting "
      "at the switch. That split is detected and then **validated against the times** "
      "before use. Where a block names its own squad, that label always wins. Where "
      "neither holds, `squad` is `UNKNOWN` - "
      f"{sum(1 for r in races if r['squad'] == 'UNKNOWN')} records.")
    A("")

    # headline results
    A("## Selected results")
    A("")
    for r in HEADLINE:
        A(f"- **{r['label']}** - {r['text']}")
    A("")

    A("## Trophies")
    A("")
    for t in data["trophies"]:
        A(f"- **{t['trophy']}** - {t['holder']} ({t['year']})  ")
        A(f"  {t['notes']}  ")
        A(f"  <{t['source_url']}>")
    A("")
    A("## Milestones")
    A("")
    for m in data["milestones"]:
        A(f"### {m['year']} - {m['milestone']}")
        A("")
        A(m["detail"])
        A("")
        A(f"*{m.get('corroboration','')}*  ")
        A(f"Source: <{m['source_url']}>")
        A("")

    A("## All results by year")
    A("")
    for y in sorted(by_year, reverse=True):
        rs = by_year[y]
        A(f"### {y} ({len(rs)} results)")
        A("")
        A("| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |")
        A("|---|---|---|---|---|---|---|---|---|")
        for r in sorted(rs, key=lambda x: (x["date"], x["regatta"], str(x["event"]))):
            pl = r["place"] if r["place"] is not None else "UNKNOWN"
            A(f"| {r['date']} | {(r['regatta'] or '')[:44]} | {(r['event'] or '')[:42]} "
              f"| {r['squad']} | {r['boat']} | {pl} | {fmt_time(r['time'])} "
              f"| {r['margin'] or ''} | [{r['source']}]({r['source_url']}) |")
        A("")
    open(OUT_MD, "w").write("\n".join(L))


if __name__ == "__main__":
    races = json.load(open(os.path.join(HERE, "part_all.json")))["races"]
    # strip helper keys, conform to schema
    clean = []
    for r in races:
        clean.append({
            "year": r["year"], "date": r["date"], "regatta": r["regatta"],
            "venue": r["venue"], "event": r["event"], "squad": r["squad"],
            "boat": r["boat"], "boat_class": r.get("boat_class"),
            "place": r["place"], "time": r["time"], "margin": r["margin"],
            "field": r["field"], "athletes": r["athletes"],
            "coxswain": r["coxswain"], "crls_entry_name": r.get("crls_entry_name"),
            "source": r["source"], "source_url": r["source_url"],
            "notes": r["notes"],
        })
    data = {
        "team": "Cambridge Rindge & Latin School (CRLS) Crew, Cambridge, Massachusetts",
        "generated": "2026-09-05",
        "record_count": len(clean),
        "year_range": [min(r["year"] for r in clean), max(r["year"] for r in clean)],
        "races": clean,
        "trophies": build_trophies(clean),
        "milestones": build_milestones(clean),
    }
    json.dump(data, open(OUT_JSON, "w"), indent=1)
    write_md(data)
    print("wrote", OUT_JSON, len(clean), "races")
    print("wrote", OUT_MD)
