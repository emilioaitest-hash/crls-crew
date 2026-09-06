# CRLS Crew - Race Results Archive

**1321 race results** for Cambridge Rindge & Latin School rowing, covering **2007-2026**.

Every result below was extracted from a primary timing source and carries its own `source_url` in `02-results.json`. Nothing here is inferred: where a squad, boat or time could not be established from the source it is recorded as `UNKNOWN`.

## Sources

| Source | Records | What it is |
|---|---:|---|
| `herenow` | 722 | HereNow regatta timing system (times computed from the system's own raw start/finish timestamps) |
| `row2k` | 502 | row2k NEIRA results, as submitted by the host school |
| `neira-championship-pdf` | 71 | NEIRA championship official results PDF |
| `neira-qra-official` | 16 | NEIRA championship official timing (neira.qra.org) |
| `usrowing-timeteam` | 10 | USRowing Northeast Youth Championships official timing (time-team) |

### How times were derived

- **NEIRA championships** - official NEIRA results. 2026 comes from the structured official results at neira.qra.org; 2011-2025 from the official NEIRA results PDFs. The PDFs are 3-column layouts, so each was parsed under 7 independent column-splitting strategies and only values agreed by a strict majority were kept. Cross-check: for 2026, the PDF and the official HTML agree on **319 of 321** comparable cells (the 2 disagreements are non-CRLS rows, and the official HTML was used for 2026 regardless).
- **MPSRA / HereNow** - the HereNow timing system's own database. Elapsed time is computed as `FinishTime1 - StartTime1` from the raw timestamps and placings are the rank of those elapsed times within the flight. Validated against the official MPSRA 2025 results PDF: every CRLS time matches exactly.
- **USRowing Northeast Youth Championships** - official time-team timing (`adjusted_result` / `adjusted_pos`), the regatta's own published results.
- **row2k** - NEIRA dual and tri-meet results as submitted by the host school. Placings are the finish order shown on the page.

### A note on squad (boys/girls) attribution

Many row2k NEIRA pages combine both squads with no gender label on the result blocks. Ground-truth pages that publish an explicit race order (2026 CRLS/Hopkins, 2024 Middlesex/CRLS, 2010 Middlesex/Pomfret/CRLS) show the boys' blocks are listed first, then the girls', with the boat-rank sequence resetting at the switch. That split is detected and then **validated against the times** before use. Where a block names its own squad, that label always wins. Where neither holds, `squad` is `UNKNOWN` - 71 records.

## Selected results

- **2026 - Girls 1V, 3rd at USRowing Northeast Youth Championships** - **7:27.54**, 6.29s behind Greenwich, in the Womens Youth 4+ A Final at Mercer Lake (17 May 2026) - qualifying for Youth Nationals for only the 2nd time in school history. Laurel Moldrem, Sinead O'Gorman-Jones, Imogen Wu, Isla Agnew, cox Ada LaMaster. <https://usrowing.regatta.time-team.com/usrowing-northeast-youth/2026>
- **2026 - Boys 1V, 3rd at USRowing Northeast Youth Championships** - **6:44.62**, 3.87s off the win in the Mens Youth 4+ A Final - a CRLS boys boat into Youth Nationals for the first time since 2018 and only the 4th time ever. Nicolas Karnath, Daniel Morland, Zeke Bittker, Mateus Verdi, cox Son Schneider. <https://usrowing.regatta.time-team.com/usrowing-northeast-youth/2026>
- **2026 - Girls 3rd varsity 4+, 2nd at the NEIRA Championship** - **6:24.415** in the Grand Final, beating Brooks by 0.76s for silver behind Choate (6:14.661). Kat Levitt, Nina Penagos-Esquitin, Beatrix Taylor, Jacqueline Long, cox Antonia Millan. <http://neira.qra.org/>
- **2026 - Boys 4th varsity 4+, 3rd at the NEIRA Championship** - **5:35.063** in the Grand Final, 1.29s behind winner Brooks. Ethan Garcia, Peter Giakoumis, Rio Thielow, Roland De Sola, cox Akash Walter. <http://neira.qra.org/>
- **2022 - Girls 1V won the USRowing Northeast Youth Championship** - Won the Womens Youth 4+ **Final in 7:21.8**, having also won the time trial (6:42.8) and semifinal (7:19.2) - the run that took CRLS girls to Youth Nationals for the first time. <https://legacy.herenow.com/results/#/races/21017/results>
- **2022 - Girls 4+ 2nd in the B Final at USRowing Youth Nationals** - **7:24.9** in the Womens Youth 4+ B Final at Nathan Benderson Park, Sarasota - the first CRLS girls crew ever to race Youth Nationals. <https://legacy.herenow.com/results/#/races/21018/results>
- **2025 - Girls 1V won the MPSRA state title** - **6:44.8** in the Girls 1st Varsity 4+ Grand Final, 9.7s clear of Somerville. The boys 1V took the matching title in **6:04.6**, 14.4s clear. <https://legacy.herenow.com/results/#/races/21341/results>
- **2026 - Boys swept every MPSRA A Final they entered** - 1st novice 8+ (**5:15.6**), 1st novice 4+ (6:01.9), 1V 4+ (**5:16.2**), 2V 4+ (5:33.9) and 3rd/4th varsity 4+ (5:25.8) - the novice eight winning the cup for the first time in school history. <https://legacy.herenow.com/results/#/races/21436/results>
- **2022 - Girls 2nd varsity 4+ won its NEIRA Championship final** - **6:13.250** - a NEIRA championship final win, the strongest CRLS result in the archive at that regatta. <https://neirarowing.org/documents/2022NEIRA.pdf>
- **2024 - Girls 1V won the NEIRA Petite Final** - **5:56.896**, top of the B-final field at Lake Quinsigamond. <https://neirarowing.org/documents/2024NEIRAResults.pdf>
- **2017 - Boys lightweight 4+ won the Northeast Youth title** - Fastest in the time trial (**6:47.6**) and won the final in **7:00.8**, sending the crew to Youth Nationals where they took the B Final in 6:46.8. <https://legacy.herenow.com/results/#/races/20373/results>
- **Head of the Charles - CRLS on its home water** - Best located finishes: Men's Youth Fours **17:20.4** (38th, 2017) and Women's Youth Fours **19:48.4** (32nd, 2017); also 2016 and 2018. <https://legacy.herenow.com/results/#/races/20398/results>

## Trophies

- **MPSRA Girls 4+s Team Trophy (The Kendra Bauer Trophy)** - Cambridge Rindge & Latin School (current as listed)  
  Listed on the MPSRA site as the current Spring Championship trophy holder  
  <http://mpsra.org/?page_id=103>
- **MPSRA Boys 4+s Team Trophy (The Jennifer Bauer Trophy)** - Cambridge Rindge & Latin School (current as listed)  
  Listed on the MPSRA site as the current Spring Championship trophy holder  
  <http://mpsra.org/?page_id=103>
- **MPSRA Girls Varsity 4+ Trophy** - Cambridge Rindge & Latin School (current as listed)  
  Listed on the MPSRA site as the current Spring Championship trophy holder  
  <http://mpsra.org/?page_id=103>
- **MPSRA Boys Varsity 4+ Trophy** - Cambridge Rindge & Latin School (current as listed)  
  Listed on the MPSRA site as the current Spring Championship trophy holder  
  <http://mpsra.org/?page_id=103>
- **MPSRA Fall Girls 4+s Team Trophy (The Dale Wickenheiser Award)** - Cambridge Rindge & Latin School (current as listed)  
  Listed on the MPSRA site as the current Fall Championship trophy holder  
  <http://mpsra.org/?page_id=96>
- **MPSRA Fall Girls Varsity 4+ (Starbeams Productions Award)** - Cambridge Rindge & Latin School (current as listed)  
  Listed on the MPSRA site as the current Fall Championship trophy holder  
  <http://mpsra.org/?page_id=96>
- **MPSRA Fall Boys Varsity 4+ (Lake Quinsigamond Community Rowing Award)** - Cambridge Rindge & Latin School (current as listed)  
  Listed on the MPSRA site as the current Fall Championship trophy holder  
  <http://mpsra.org/?page_id=96>
- **MPSRA Fall Girls Novice 4+** - Cambridge Rindge & Latin School (current as listed)  
  Listed on the MPSRA site as the current Fall Championship trophy holder  
  <http://mpsra.org/?page_id=96>
- **The Mayor's Cup (Cambridge)** - contested annually by CRLS and BB&N (2007-2026 (races located))  
  The Cambridge Mayor's Cup is the CRLS vs Buckingham Browne & Nichols dual. row2k carries CRLS/BB&N Mayor's Cup results for 2007, 2008, 2009, 2010, 2011, 2012, 2014, 2015, 2017, 2018, 2019, 2022, 2023, 2025 and 2026. Which school held the Cup in a given year is NOT stated on those result pages, so per-year Cup winners are UNKNOWN; the individual race results are in the races[] array.  
  <https://www.row2k.com/results/index.cfm?league=NEIRA>
- **MPSRA Girls Fours Points Trophy** - Cambridge Rindge & Latin School (2026)  
  Fifth consecutive Girls Fours Points Trophy (2026), per Cambridge Day.  
  <https://www.cambridgeday.com/2026/05/28/crew-teams-shine-championships/>
- **MPSRA Boys Fours Points Trophy** - Cambridge Rindge & Latin School (2026)  
  Retained for the fifth consecutive year (2026), per Cambridge Day.  
  <https://www.cambridgeday.com/2026/05/28/crew-teams-shine-championships/>

## Milestones

### 2026 - Girls 1V qualified for USRowing Youth National Championships - 2nd time in school history (first was 2022)

3rd at USRowing Northeast Youth Championships, 7:27.54: Laurel Moldrem, Sinead O'Gorman-Jones, Imogen Wu, Isla Agnew, cox Ada LaMaster

*Time and placing independently confirmed in the USRowing Northeast Youth Championships official timing (Womens Youth 4+ Final A, 3rd, 07:27.54).*  
Source: <https://www.cambridgeday.com/2026/05/28/crew-teams-shine-championships/>

### 2026 - Boys 1V qualified for Youth Nationals for the first time since 2018 - 4th time in school history

3rd at USRowing Northeast Youth Championships, 6:44.62: Nicolas Karnath, Daniel Morland, Zeke Bittker, Mateus Verdi, cox Son Schneider

*Time and placing independently confirmed in the USRowing Northeast Youth Championships official timing (Mens Youth 4+ Final A, 3rd, 06:44.62).*  
Source: <https://www.cambridgeday.com/2026/05/28/crew-teams-shine-championships/>

### 2026 - Girls 3rd varsity 4+ took 2nd at the NEIRA Championship

6:24.415 behind Choate (6:14.661). Kat Levitt, Nina Penagos-Esquitin, Beatrix Taylor, Jacqueline Long, cox Antonia Millan. CRLS was one of only three public schools racing the NEIRA fours category.

*Exact time confirmed in NEIRA official results (Girl's Third Four w/Cox, Grand Final).*  
Source: <http://neira.qra.org/>

### 2026 - Boys 4th varsity 4+ took 3rd at the NEIRA Championship

5:35.063, under 1.3s behind winner Brooks. Ethan Garcia, Peter Giakoumis, Rio Thielow, Roland De Sola, cox Akash Walter.

*Exact time confirmed in NEIRA official results (Boy's Fourth Four w/Cox, Grand Final).*  
Source: <http://neira.qra.org/>

### 2026 - Boys Novice 8+ won the MPSRA cup for the first time in school history

Boys crews placed first in all their time trials and A finals at the MPSRA State Championship; boys novice 4+, 1st varsity 4+ and 2nd varsity 4+ all won.

*MPSRA 2026 championship results are in races[] from the HereNow timing system.*  
Source: <https://www.cambridgeday.com/2026/05/28/crew-teams-shine-championships/>

### 2026 - Girls swept 1-2-3 in the MPSRA 3rd varsity 4+

Cups in girls 1st novice 4+ and 1st varsity 4+; wins in 2nd novice 4+ and 2nd varsity 4+; novice girls 8+ 3rd; Iris Moyer bronze in the single.

*See MPSRA 2026 records in races[].*  
Source: <https://www.cambridgeday.com/2026/05/28/crew-teams-shine-championships/>

### 2022 - Girls crew reached USRowing Youth National Championships for the first time in school history

Womens Youth 4+ - Time Trial 5th (7:06.0), A/B Semifinal 4th (7:29.5), B Final 2nd (7:24.9) at Nathan Benderson Park, Sarasota FL.

*Results retrieved from the HereNow timing system.*  
Source: <https://legacy.herenow.com/results/#/races/21018/results>

### 2018 - Boys raced the USRowing Youth National Championships (Lake Natoma, Rancho Cordova CA)

Mens Ltwt Youth 4+ - Time Trial 18th (6:53.4), Repechage 4th (7:10.7), C Final 4th (7:26.8).

*Results retrieved from the HereNow timing system.*  
Source: <https://legacy.herenow.com/results/#/races/20504/results>

### 2017 - Boys raced the USRowing Youth National Championships (Nathan Benderson Park, Sarasota FL)

Mens Ltwt Youth 4+ - Time Trial 8th (6:38.9), Semifinal 5th (7:03.6), B Final 4th (6:46.8).

*Results retrieved from the HereNow timing system.*  
Source: <https://legacy.herenow.com/results/#/races/20374/results>

## All results by year

### 2026 (87 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2026-04-11 | BB&N vs CRLS (Mayor's Cup) | First Boat | boys | 1V | 1 | 4:25.4 | 13.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1A9140D19180C189B6A831FB6F435C23) |
| 2026-04-11 | BB&N vs CRLS (Mayor's Cup) | Fourth Boat | boys | 4V | 1 | 4:50.0 | 3.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1A9140D19180C189B6A831FB6F435C23) |
| 2026-04-11 | BB&N vs CRLS (Mayor's Cup) | Fourth Boat | girls | 4V | 2 | 5:29.2 | 7.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1A9140D19180C189B6A831FB6F435C23) |
| 2026-04-11 | BB&N vs CRLS (Mayor's Cup) | Other | girls | UNKNOWN | 1 | 4:50.1 | 16.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1A9140D19180C189B6A831FB6F435C23) |
| 2026-04-11 | BB&N vs CRLS (Mayor's Cup) | Other | girls | UNKNOWN | 1 | 5:06.1 | 6.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1A9140D19180C189B6A831FB6F435C23) |
| 2026-04-11 | BB&N vs CRLS (Mayor's Cup) | Second Boat | boys | 2V | 1 | 4:31.8 | 8.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1A9140D19180C189B6A831FB6F435C23) |
| 2026-04-11 | BB&N vs CRLS (Mayor's Cup) | Third Boat | boys | 3V | 1 | 4:44.2 | 8.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1A9140D19180C189B6A831FB6F435C23) |
| 2026-04-11 | BB&N vs CRLS (Mayor's Cup) | Third Boat | girls | 3V | 1 | 5:08.2 | 27.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1A9140D19180C189B6A831FB6F435C23) |
| 2026-04-22 | Mayor’s Cup: CRLS vs BB&N | First Boat | UNKNOWN | 1V | 1 | 4:48 | 22.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=A9D13B797BEDC786C15FE46340A92068) |
| 2026-04-25 | Brooks vs. CRLS, Middlesex and NMH - correct | Fifth Boat | boys | 5V | 1 | 6:22.6 | 8.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=B5B633DFB75BB9FA84BC8CC58D8CEED8) |
| 2026-04-25 | Brooks vs. CRLS, Middlesex and NMH - correct | Fifth Boat | girls | 5V | 1 | 7:22.0 | 2.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=B5B633DFB75BB9FA84BC8CC58D8CEED8) |
| 2026-04-25 | Brooks vs. CRLS, Middlesex and NMH - correct | First Boat | boys | 1V | 2 | 5:27.4 | 3.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=B5B633DFB75BB9FA84BC8CC58D8CEED8) |
| 2026-04-25 | Brooks vs. CRLS, Middlesex and NMH - correct | Fourth Boat | boys | 4V | 1 | 6:01.8 | 7.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=B5B633DFB75BB9FA84BC8CC58D8CEED8) |
| 2026-04-25 | Brooks vs. CRLS, Middlesex and NMH - correct | Fourth Boat | girls | 4V | 3 | 7:13.3 | 15.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=B5B633DFB75BB9FA84BC8CC58D8CEED8) |
| 2026-04-25 | Brooks vs. CRLS, Middlesex and NMH - correct | Other | girls | UNKNOWN | 2 | 6:06.3 | 8.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=B5B633DFB75BB9FA84BC8CC58D8CEED8) |
| 2026-04-25 | Brooks vs. CRLS, Middlesex and NMH - correct | Other | girls | UNKNOWN | 2 | 6:31.0 | 11.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=B5B633DFB75BB9FA84BC8CC58D8CEED8) |
| 2026-04-25 | Brooks vs. CRLS, Middlesex and NMH - correct | Second Boat | boys | 2V | 3 | 5:52.3 | 15.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=B5B633DFB75BB9FA84BC8CC58D8CEED8) |
| 2026-04-25 | Brooks vs. CRLS, Middlesex and NMH - correct | Third Boat | boys | 3V | 2 | 6:01.2 | 10.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=B5B633DFB75BB9FA84BC8CC58D8CEED8) |
| 2026-04-25 | Brooks vs. CRLS, Middlesex and NMH - correct | Third Boat | girls | 3V | 3 | 7:01.9 | 8.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=B5B633DFB75BB9FA84BC8CC58D8CEED8) |
| 2026-05-02 | Cambridge Rindge abd Latin School at Groton | Fifth Boat | boys | 5V | 2 | 4:18.3 | 6.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73B77871E3536483D98EF9378161BD6F) |
| 2026-05-02 | Cambridge Rindge abd Latin School at Groton | Fifth Boat | girls | 5V | 1 | 4:58.2 | 8.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73B77871E3536483D98EF9378161BD6F) |
| 2026-05-02 | Cambridge Rindge abd Latin School at Groton | First Boat | boys | 1V | 1 | 3:56.3 | 6.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73B77871E3536483D98EF9378161BD6F) |
| 2026-05-02 | Cambridge Rindge abd Latin School at Groton | Fourth Boat | boys | 4V | 1 | 4:08.6 | 10.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73B77871E3536483D98EF9378161BD6F) |
| 2026-05-02 | Cambridge Rindge abd Latin School at Groton | Fourth Boat | girls | 4V | 1 | 4:52.8 | 10.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73B77871E3536483D98EF9378161BD6F) |
| 2026-05-02 | Cambridge Rindge abd Latin School at Groton | Other | girls | UNKNOWN | 1 | 4:25.3 | 4.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73B77871E3536483D98EF9378161BD6F) |
| 2026-05-02 | Cambridge Rindge abd Latin School at Groton | Other | girls | UNKNOWN | 2 | 4:45.2 | 1.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73B77871E3536483D98EF9378161BD6F) |
| 2026-05-02 | Cambridge Rindge abd Latin School at Groton | Second Boat | boys | 2V | 2 | 4:12.8 | 7.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73B77871E3536483D98EF9378161BD6F) |
| 2026-05-02 | Cambridge Rindge abd Latin School at Groton | Third Boat | boys | 3V | 2 | 4:12.5 | 7.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73B77871E3536483D98EF9378161BD6F) |
| 2026-05-02 | Cambridge Rindge abd Latin School at Groton | Third Boat | girls | 3V | 1 | 4:45.3 | 19.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73B77871E3536483D98EF9378161BD6F) |
| 2026-05-06 | Winsor School vs. Nobles vs. CRLS | Fifth Boat | girls | 5V | 2 | 6:35.4 | 5.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CAF6A3546F2E621A5341EAEBA6CFA90B) |
| 2026-05-06 | Winsor School vs. Nobles vs. CRLS | First Boat | girls | 1V | 2 | 5:25.4 | 5.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CAF6A3546F2E621A5341EAEBA6CFA90B) |
| 2026-05-06 | Winsor School vs. Nobles vs. CRLS | Fourth Boat | girls | 4V | 2 | 6:29.8 | 13.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CAF6A3546F2E621A5341EAEBA6CFA90B) |
| 2026-05-06 | Winsor School vs. Nobles vs. CRLS | Second Boat | girls | 2V | 3 | 5:44.5 | 8.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CAF6A3546F2E621A5341EAEBA6CFA90B) |
| 2026-05-06 | Winsor School vs. Nobles vs. CRLS | Sixth Boat | girls | 6V | 1 | 6:14.1 | 11.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CAF6A3546F2E621A5341EAEBA6CFA90B) |
| 2026-05-06 | Winsor School vs. Nobles vs. CRLS | Sixth Boat | girls | 6V | 5 | 6:34.7 | 20.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CAF6A3546F2E621A5341EAEBA6CFA90B) |
| 2026-05-06 | Winsor School vs. Nobles vs. CRLS | Third Boat | girls | 3V | 2 | 5:56.6 | 7.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CAF6A3546F2E621A5341EAEBA6CFA90B) |
| 2026-05-09 | CRLS vs Hopkins, Dexter Southfield | Fifth Boat | girls | 5V | 1 | 5:36.6 | 47.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=49E35C8A20A0736D6FDA5531D8829D8F) |
| 2026-05-09 | CRLS vs Hopkins, Dexter Southfield | First Boat | boys | 1V | 1 | 4:25.0 | 21.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=49E35C8A20A0736D6FDA5531D8829D8F) |
| 2026-05-09 | CRLS vs Hopkins, Dexter Southfield | Fourth Boat | boys | 4V | 1 | 4:48.85 | 43.94s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=49E35C8A20A0736D6FDA5531D8829D8F) |
| 2026-05-09 | CRLS vs Hopkins, Dexter Southfield | Fourth Boat | girls | 4V | 1 | 5:31.0 | 9.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=49E35C8A20A0736D6FDA5531D8829D8F) |
| 2026-05-09 | CRLS vs Hopkins, Dexter Southfield | Other | girls | UNKNOWN | 1 | 4:59.7 | 17.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=49E35C8A20A0736D6FDA5531D8829D8F) |
| 2026-05-09 | CRLS vs Hopkins, Dexter Southfield | Other | girls | UNKNOWN | 1 | 5:11.3 | 24.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=49E35C8A20A0736D6FDA5531D8829D8F) |
| 2026-05-09 | CRLS vs Hopkins, Dexter Southfield | Second Boat | boys | 2V | 1 | 4:37.21 | 13.18s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=49E35C8A20A0736D6FDA5531D8829D8F) |
| 2026-05-09 | CRLS vs Hopkins, Dexter Southfield | Third Boat | boys | 3V | 1 | 4:40.86 | 16.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=49E35C8A20A0736D6FDA5531D8829D8F) |
| 2026-05-09 | CRLS vs Hopkins, Dexter Southfield | Third Boat | girls | 3V | 1 | 5:09.0 | 23.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=49E35C8A20A0736D6FDA5531D8829D8F) |
| 2026-05-16 | USRowing Northeast Youth Championships | Mens Youth 4+ - Semifinal 2 | boys | 1V | 2 | 07:00.06 | 2.04s | [usrowing-timeteam](https://usrowing.regatta.time-team.com/usrowing-northeast-youth/2026/races/b56c2657-44c4-408a-a59a-3b5722e55fcc) |
| 2026-05-16 | USRowing Northeast Youth Championships | Mens Youth 4+ - Time Trial | boys | 1V | 2 | 06:28.31 | 6.10s | [usrowing-timeteam](https://usrowing.regatta.time-team.com/usrowing-northeast-youth/2026/races/ea0c6e74-007f-4804-a22a-dd637c897a32) |
| 2026-05-16 | USRowing Northeast Youth Championships | Womens Youth 4+ - Semifinal 2 | girls | 1V | 2 | 07:41.01 | 7.61s | [usrowing-timeteam](https://usrowing.regatta.time-team.com/usrowing-northeast-youth/2026/races/1d482c21-6b9c-4ffb-90af-ac36495f1166) |
| 2026-05-16 | USRowing Northeast Youth Championships | Womens Youth 4+ - Time Trial | girls | 1V | 3 | 07:11.11 | 7.14s | [usrowing-timeteam](https://usrowing.regatta.time-team.com/usrowing-northeast-youth/2026/races/2f520fad-83ae-4a51-9719-eb85ab723ac6) |
| 2026-05-17 | USRowing Northeast Youth Championships | Mens Youth 4+ - Final A | boys | 1V | 3 | 06:44.62 | 3.87s | [usrowing-timeteam](https://usrowing.regatta.time-team.com/usrowing-northeast-youth/2026/races/f3d676b7-220d-4b19-a1ff-c87bccc26252) |
| 2026-05-17 | USRowing Northeast Youth Championships | Womens Youth 4+ - Final A | girls | 1V | 3 | 07:27.54 | 6.29s | [usrowing-timeteam](https://usrowing.regatta.time-team.com/usrowing-northeast-youth/2026/races/74d908e7-230a-48bd-b32f-48296444d27a) |
| 2026-05-23 | NEIRA Championship 2026 | Boy's First Four w/Cox - Heat 1 | boys | 1V | 3 | 5:09.735 | 4.99s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Boy's First Four w/Cox - Petite Final | boys | 1V | 2 | 5:16.771 | 4.41s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Boy's Fourth Four w/Cox - Grand Final | boys | 4V | 3 | 5:35.063 | 1.28s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Boy's Fourth Four w/Cox - Heat 2 | boys | 4V | 2 | 5:17.092 | 7.43s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Boy's Second Four w/Cox - Heat 3 | boys | 2V | 3 | 5:19.258 | 5.17s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Boy's Second Four w/Cox - Petite Final | boys | 2V | 2 | 5:41.782 | 3.18s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Boy's Third Four w/Cox - Grand Final | boys | 3V | 4 | 5:39.428 | 15.55s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Boy's Third Four w/Cox - Heat 2 | boys | 3V | 3 | 5:18.370 | 14.69s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Girl's First Four w/Cox - Grand Final | girls | 1V | 4 | 5:51.827 | 12.30s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Girl's First Four w/Cox - Heat 3 | girls | 1V | 2 | 5:51.361 | 2.58s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Girl's Fourth Four w/Cox - Grand Final | girls | 4V | 6 | 6:41.309 | 19.07s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Girl's Fourth Four w/Cox - Heat 1 | girls | 4V | 3 | 6:05.338 | 10.28s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Girl's Second Four w/Cox - Heat 1 | girls | 2V | 3 | 5:57.651 | 12.44s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Girl's Second Four w/Cox - Petite Final | girls | 2V | 2 | 6:17.886 | 1.44s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Girl's Third Four w/Cox - Grand Final | girls | 3V | 2 | 6:24.415 | 9.75s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-23 | NEIRA Championship 2026 | Girl's Third Four w/Cox - Heat 2 | girls | 3V | 2 | 5:58.385 | 4.14s | [neira-qra-official](http://neira.qra.org/) |
| 2026-05-24 | MPSRA Spring Championship | Boys 1st Novice 4+ Final A | boys | 1st Novice | 1 | 6:01.9 | 27.40s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Boys 1st Novice 4+ Time Trial | boys | 1st Novice | 1 | 5:45.9 | 18.00s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Boys 1st Novice 8+ Final A | boys | 1st Novice | 1 | 5:15.6 | 9.90s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Boys 1st Novice 8+ Time Trial | boys | 1st Novice | 1 | 5:22.7 | 7.90s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Boys 1st Varsity 4+ Final A | boys | 1V | 1 | 5:16.2 | 4.20s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Boys 1st Varsity 4+ Time Trial | boys | 1V | 1 | 5:18.5 | 7.50s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Boys 2nd Varsity 4+ Final A | boys | 2V | 1 | 5:33.9 | 7.90s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Boys 2nd Varsity 4+ Time Trial | boys | 2V | 1 | 5:35.6 | 5.70s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Boys 3rd / 4th Varsity 4+ Final A | boys | 4V | 1 | 5:25.8 | 8.20s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Boys 3rd / 4th Varsity 4+ Final A | boys | 4V | 2 | 5:34.0 | 8.20s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Girls 1st Novice 4+ Final A | girls | 1st Novice | 1 | 6:44.3 | 26.00s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Girls 1st Novice 8+ Final A | girls | 1st Novice | 3 | 6:13.9 | 5.10s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Girls 1st Novice 8+ Time Trial | girls | 1st Novice | 2 | 5:59.7 | 9.90s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Girls 1st Varsity 4+ Final A | girls | 1V | 1 | 6:05.3 | 31.30s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Girls 1x Final A | girls | UNKNOWN | 3 | 8:15.3 | 39.80s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Girls 2nd Novice 4+ Final A | girls | 2nd Novice | 1 | 6:51.8 | 87.00s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Final A | girls | 2V | 1 | 6:32.9 | 13.90s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Girls 3rd Varsity 4+ Final A | girls | 3V | 1 | 6:52.2 | 3.20s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Girls 3rd Varsity 4+ Final A | girls | 3V | 2 | 6:55.4 | 3.20s | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |
| 2026-05-24 | MPSRA Spring Championship | Girls 3rd Varsity 4+ Final A | girls | 3V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21436/results) |

### 2025 (119 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2025-04-16 | Cambridge Mayor's Cup: BB&N vs. CRLS | Fifth Boat | girls | 5V | 2 | 5:17 | 1.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=181E3474D2FC1C1BDC3CD092B1E1976C) |
| 2025-04-16 | Cambridge Mayor's Cup: BB&N vs. CRLS | First Boat | girls | 1V | 2 | 4:49 | 1.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=181E3474D2FC1C1BDC3CD092B1E1976C) |
| 2025-04-16 | Cambridge Mayor's Cup: BB&N vs. CRLS | Fourth Boat | girls | 4V | 1 | 5:10 | 9.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=181E3474D2FC1C1BDC3CD092B1E1976C) |
| 2025-04-16 | Cambridge Mayor's Cup: BB&N vs. CRLS | Second Boat | girls | 2V | 1 | 5:02 | 14.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=181E3474D2FC1C1BDC3CD092B1E1976C) |
| 2025-04-16 | Cambridge Mayor's Cup: BB&N vs. CRLS | Third Boat | girls | 3V | 1 | 5:02 | 20.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=181E3474D2FC1C1BDC3CD092B1E1976C) |
| 2025-04-23 | BB&N, CRLS and Thayer (Mayor's Cup) | First Boat | boys | 1V | 1 | 4:22.23 | 1.83s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=70A75824096A2554B9F78A0E50641458) |
| 2025-04-23 | BB&N, CRLS and Thayer (Mayor's Cup) | Fourth Boat | boys | 4V | 1 | 4:46.60 | 5.21s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=70A75824096A2554B9F78A0E50641458) |
| 2025-04-23 | BB&N, CRLS and Thayer (Mayor's Cup) | Second Boat | boys | 2V | 1 | 4:29.28 | 1.42s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=70A75824096A2554B9F78A0E50641458) |
| 2025-04-23 | BB&N, CRLS and Thayer (Mayor's Cup) | Third Boat | boys | 3V | 2 | 4:37.45 | 0.63s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=70A75824096A2554B9F78A0E50641458) |
| 2025-04-26 | Brooks vs. CRLS, Hopkins, Middlesex and NMH | Fifth Boat | girls | 5V | 1 | 7:06 | 27.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=168B5F55B689601CCC0CC8B65FAE5BAC) |
| 2025-04-26 | Brooks vs. CRLS, Hopkins, Middlesex and NMH | First Boat | boys | 1V | 5 | 5:31 | 17.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=168B5F55B689601CCC0CC8B65FAE5BAC) |
| 2025-04-26 | Brooks vs. CRLS, Hopkins, Middlesex and NMH | Fourth Boat | boys | 4V | 2 | 5:54 | 7.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=168B5F55B689601CCC0CC8B65FAE5BAC) |
| 2025-04-26 | Brooks vs. CRLS, Hopkins, Middlesex and NMH | Fourth Boat | girls | 4V | 1 | 6:38.1 | 0.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=168B5F55B689601CCC0CC8B65FAE5BAC) |
| 2025-04-26 | Brooks vs. CRLS, Hopkins, Middlesex and NMH | Other | girls | UNKNOWN | 5 | 6:16.8 | 24.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=168B5F55B689601CCC0CC8B65FAE5BAC) |
| 2025-04-26 | Brooks vs. CRLS, Hopkins, Middlesex and NMH | Other | girls | UNKNOWN | 3 | 6:19.0 | 8.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=168B5F55B689601CCC0CC8B65FAE5BAC) |
| 2025-04-26 | Brooks vs. CRLS, Hopkins, Middlesex and NMH | Second Boat | boys | 2V | 2 | 5:40 | 7.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=168B5F55B689601CCC0CC8B65FAE5BAC) |
| 2025-04-26 | Brooks vs. CRLS, Hopkins, Middlesex and NMH | Third Boat | boys | 3V | 2 | 5:48 | 7.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=168B5F55B689601CCC0CC8B65FAE5BAC) |
| 2025-04-26 | Brooks vs. CRLS, Hopkins, Middlesex and NMH | Third Boat | girls | 3V | 1 | 6:18.5 | 4.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=168B5F55B689601CCC0CC8B65FAE5BAC) |
| 2025-04-30 | The Winsor School, Choate, Cambridge Rindge  | Fifth Boat | girls | 5V | 1 | 5:11.36 | 10.84s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=97F7AB1A3583B5AD0B685E7720855CFF) |
| 2025-04-30 | The Winsor School, Choate, Cambridge Rindge  | First Boat | girls | 1V | 2 | 4:48.9 | 5.64s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=97F7AB1A3583B5AD0B685E7720855CFF) |
| 2025-04-30 | The Winsor School, Choate, Cambridge Rindge  | Fourth Boat | girls | 4V | 3 | 5:15.6 | 14.44s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=97F7AB1A3583B5AD0B685E7720855CFF) |
| 2025-04-30 | The Winsor School, Choate, Cambridge Rindge  | Second Boat | girls | 2V | 3 | 5:00.3 | 6.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=97F7AB1A3583B5AD0B685E7720855CFF) |
| 2025-04-30 | The Winsor School, Choate, Cambridge Rindge  | Sixth Boat | girls | 6V | 1 | 5:14.09 | 3.39s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=97F7AB1A3583B5AD0B685E7720855CFF) |
| 2025-04-30 | The Winsor School, Choate, Cambridge Rindge  | Third Boat | girls | 3V | 1 | 04:59.80 | 3.47s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=97F7AB1A3583B5AD0B685E7720855CFF) |
| 2025-05-03 | CRLS at Groton | Fifth Boat | boys | 5V | 2 | 4:23.9 | 9.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FF45AC48CF863069B998EA93AF28A674) |
| 2025-05-03 | CRLS at Groton | Fifth Boat | girls | 5V | 1 | 4:54.0 | 22.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FF45AC48CF863069B998EA93AF28A674) |
| 2025-05-03 | CRLS at Groton | First Boat | boys | 1V | 2 | 3:56.6 | 7.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FF45AC48CF863069B998EA93AF28A674) |
| 2025-05-03 | CRLS at Groton | Fourth Boat | boys | 4V | 2 | 4:20.8 | 8.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FF45AC48CF863069B998EA93AF28A674) |
| 2025-05-03 | CRLS at Groton | Fourth Boat | girls | 4V | 1 | 4:40.3 | 5.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FF45AC48CF863069B998EA93AF28A674) |
| 2025-05-03 | CRLS at Groton | Other | girls | UNKNOWN | 2 | 4:22.7 | 9.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FF45AC48CF863069B998EA93AF28A674) |
| 2025-05-03 | CRLS at Groton | Other | girls | UNKNOWN | 1 | 4:29.7 | 4.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FF45AC48CF863069B998EA93AF28A674) |
| 2025-05-03 | CRLS at Groton | Second Boat | boys | 2V | 2 | 4:09.8 | 14.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FF45AC48CF863069B998EA93AF28A674) |
| 2025-05-03 | CRLS at Groton | Third Boat | boys | 3V | 2 | 4:05 | 11.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FF45AC48CF863069B998EA93AF28A674) |
| 2025-05-03 | CRLS at Groton | Third Boat | girls | 3V | 1 | 4:36.9 | 11.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FF45AC48CF863069B998EA93AF28A674) |
| 2025-05-10 | Amber Zapatka Memorial Regatta | Mens Jr 2x Time Trial | boys | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21340/results) |
| 2025-05-10 | Amber Zapatka Memorial Regatta | Mens Jr Novice 8+ Time Trial | boys | Novice | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21340/results) |
| 2025-05-10 | Amber Zapatka Memorial Regatta | Mens Jr Varsity 4+ Time Trial | boys | 1V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21340/results) |
| 2025-05-10 | Amber Zapatka Memorial Regatta | Womens Jr 2nd Varsity 4+ Time Trial | girls | 2V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21340/results) |
| 2025-05-10 | Amber Zapatka Memorial Regatta | Womens Jr 3rd Varsity 4+ Final A | girls | 3V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21340/results) |
| 2025-05-10 | Amber Zapatka Memorial Regatta | Womens Jr Novice 4+ Time Trial | girls | Novice | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21340/results) |
| 2025-05-10 | Amber Zapatka Memorial Regatta | Womens Jr Varsity 4+ Time Trial | girls | 1V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21340/results) |
| 2025-05-10 | Amber Zapatka Memorial Regatta | Womens U17 4+ Final A | girls | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21340/results) |
| 2025-05-24 | NEIRA Championship 2025 | boys 1V 4+ - Heat 1 | boys | 1V | 4 | 5:15.421 | 12.95s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-24 | NEIRA Championship 2025 | boys 1V 4+ - Petite Final | boys | 1V | 3 | 5:00.847 | 3.56s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-24 | NEIRA Championship 2025 | boys 2V 4+ - Heat 1 | boys | 2V | 3 | 5:22.925 | 9.08s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-24 | NEIRA Championship 2025 | boys 2V 4+ - Petite Final | boys | 2V | 4 | 5:20.341 | 8.14s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-24 | NEIRA Championship 2025 | boys 3V 4+ - Grand Final | boys | 3V | 5 | 5:13.102 | 17.86s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-24 | NEIRA Championship 2025 | boys 3V 4+ - Heat 2 | boys | 3V | 3 | 5:32.917 | 7.72s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-24 | NEIRA Championship 2025 | boys 4V 4+ - Grand Final | boys | 4V | 5 | 5:28.507 | 18.26s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-24 | NEIRA Championship 2025 | boys 4V 4+ - Heat 1 | boys | 4V | 3 | 5:49.574 | 25.37s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-24 | NEIRA Championship 2025 | girls 1V 4+ - Heat 2 | girls | 1V | 6 | 5:49.860 | 18.94s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-24 | NEIRA Championship 2025 | girls 2V 4+ - Heat 1 | girls | 2V | 4 | 6:06.090 | 14.90s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-24 | NEIRA Championship 2025 | girls 2V 4+ - Petite Final | girls | 2V | 6 | 5:58.471 | 18.33s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-24 | NEIRA Championship 2025 | girls 3V 4+ - Heat 2 | girls | 3V | 3 | 6:07.590 | 2.51s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-24 | NEIRA Championship 2025 | girls 3V 8+ - Grand Final | girls | 3V | 5 | 5:58.575 | 43.55s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-24 | NEIRA Championship 2025 | girls 4V 4+ - Grand Final | girls | 4V | 5 | 5:58.575 | 9.69s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-24 | NEIRA Championship 2025 | girls 4V 4+ - Heat 2 | girls | 4V | 3 | 6:19.963 | 13.38s | [neira-championship-pdf](https://neirarowing.org/documents/2025NEIRAResults.pdf) |
| 2025-05-25 | MPSRA Spring Championship | Boys 1st Novice 4+ Grand Final | boys | 1st Novice | 2 | 5:38.1 | 8.70s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Boys 1st Novice 4+ Time Trial | boys | 1st Novice | 2 | 9:02.4 | 13.90s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Boys 1st Varsity 4+ Grand Final | boys | 1V | 1 | 6:04.6 | 14.40s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Boys 1st Varsity 4+ Time Trial | boys | 1V | 1 | 7:34.4 | 22.00s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Boys 2- / Girls 2- / Mix Inc 2x Final | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Boys 2nd Varsity 4+ Final | boys | 2V | 1 | 5:56.6 | 12.40s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Boys 3rd Varsity 4+ Final | boys | 3V | 1 | 6:12.2 | 48.60s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Boys 4th Varsity 4+ Final | boys | 4V | 1 | 6:03.9 | 30.60s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Girls 1st Novice 4+ Final | girls | 1st Novice | 2 | 7:52.1 | 7.80s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Girls 1st Varsity 4+ Grand Final | girls | 1V | 1 | 6:44.8 | 9.70s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Girls 1st Varsity 4+ Time Trial | girls | 1V | 1 | 8:38.8 | 14.00s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Girls 2nd Novice 4+ Final | girls | 2nd Novice | 1 | 6:38.1 | 13.10s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Girls 2nd Novice 4+ Final | girls | 2nd Novice | 4 | 8:10.7 | 92.60s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Final | girls | 2V | 1 | 6:41.7 | 22.90s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Girls 3rd Varsity 4+ Final | girls | 3V | 1 | 6:45.7 | 50.90s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Girls 4th Varsity 4+ Final | girls | 4V | 1 | 6:52.4 | 0.20s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Girls 4th Varsity 4+ Final | girls | 4V | 2 | 6:52.6 | 0.20s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-05-25 | MPSRA Spring Championship | Girls 4th Varsity 4+ Final | girls | 4V | 3 | 7:33.9 | 41.50s | [herenow](https://legacy.herenow.com/results/#/races/21341/results) |
| 2025-10-05 | Textile River Regatta | Mens Jr 4+ A | boys | UNKNOWN | 1 | 14:55.9 | 0.50s | [herenow](https://legacy.herenow.com/results/#/races/21375/results) |
| 2025-10-05 | Textile River Regatta | Mens Jr 4+ B | boys | UNKNOWN | 1 | 14:58.8 | 47.80s | [herenow](https://legacy.herenow.com/results/#/races/21375/results) |
| 2025-10-05 | Textile River Regatta | Mens Jr 4+ B | boys | UNKNOWN | 6 | 16:15.7 | 76.90s | [herenow](https://legacy.herenow.com/results/#/races/21375/results) |
| 2025-10-05 | Textile River Regatta | Mens Jr 4+ B | boys | UNKNOWN | 7 | 16:18.3 | 79.50s | [herenow](https://legacy.herenow.com/results/#/races/21375/results) |
| 2025-10-05 | Textile River Regatta | Mens Jr 8+ B | boys | UNKNOWN | 15 | 16:26.4 | 134.60s | [herenow](https://legacy.herenow.com/results/#/races/21375/results) |
| 2025-10-05 | Textile River Regatta | Womens Jr 4+ A | girls | UNKNOWN | 1 | 16:20.9 | 8.10s | [herenow](https://legacy.herenow.com/results/#/races/21375/results) |
| 2025-10-05 | Textile River Regatta | Womens Jr 4+ B | girls | UNKNOWN | 1 | 17:08.8 | 2.70s | [herenow](https://legacy.herenow.com/results/#/races/21375/results) |
| 2025-10-05 | Textile River Regatta | Womens Jr 4+ B | girls | UNKNOWN | 6 | 18:03.2 | 54.40s | [herenow](https://legacy.herenow.com/results/#/races/21375/results) |
| 2025-10-05 | Textile River Regatta | Womens Jr 4+ B | girls | UNKNOWN | 11 | 18:38.0 | 89.20s | [herenow](https://legacy.herenow.com/results/#/races/21375/results) |
| 2025-10-05 | Textile River Regatta | Womens Jr 8+ B | girls | UNKNOWN | 4 | 16:41.3 | 53.90s | [herenow](https://legacy.herenow.com/results/#/races/21375/results) |
| 2025-10-11 | Head of the Kevin 3 | All combined events | girls | UNKNOWN | 42 | 19:03.3 | 264.90s | [herenow](https://legacy.herenow.com/results/#/races/21365/results) |
| 2025-10-11 | Head of the Kevin 3 | All combined events | girls | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21365/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Mens 2nd Varsity 4+ | boys | 2V | 1 | 16:22.2 | 3.90s | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Mens 3rd/4th Varsity 4+ | boys | 4V | 1 | 16:52.6 | 17.00s | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Mens 3rd/4th Varsity 4+ | boys | 4V | 3 | 17:13.6 | 21.00s | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Mens Novice 8+ | boys | Novice | 2 | 16:20.9 | 0.00s | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Mens Novice 8+ | boys | Novice | 16 | 19:32.4 | 191.50s | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Mens Varsity 4+ | boys | 1V | 5 | 15:56.3 | 56.30s | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Womens 1st Varsity 4+ | girls | 1V | 1 | 17:46.0 | 25.40s | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Womens 1st Varsity 8+ | girls | 1V | 7 | 17:51.7 | 47.30s | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Womens 2nd Varsity 4+ | girls | 2V | 1 | 18:54.1 | 46.80s | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Womens 3rd/4th Varsity 4+ | girls | 4V | 1 | 20:04.9 | 35.80s | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Womens 3rd/4th Varsity 4+ | girls | 4V | 3 | 21:03.5 | 58.60s | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Womens 3rd/4th Varsity 4+ | girls | 4V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Womens Novice 4+ | girls | Novice | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Womens Novice 8+ | girls | Novice | 6 | 19:32.4 | 70.30s | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-12 | Northeast Fall Championship Regatta | Womens Novice 8+ | girls | Novice | 10 | 20:45.0 | 142.90s | [herenow](https://legacy.herenow.com/results/#/races/21376/results) |
| 2025-10-26 | MPSRA Fall Championship | Boys 1st Novice 8+ | boys | 1st Novice | 2 | 15:24.8 | 19.40s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Boys 1st Varsity 4+ | boys | 1V | 1 | 15:23.0 | 12.40s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Boys 2nd Novice 8+ | boys | 2nd Novice | 1 | 17:31.0 | 68.80s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Boys 2nd Varsity 4+ | boys | 2V | 1 | 15:47.4 | 67.70s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Boys 3rd Varsity 4+ | boys | 3V | 1 | 16:17.7 | 50.30s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Boys 4th Varsity 4+ | boys | 4V | 1 | 17:16.4 | 2.10s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Girls 1st Novice 4+ | girls | 1st Novice | 1 | 19:16.0 | 71.10s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Girls 1st Novice 8+ | girls | 1st Novice | 3 | 17:49.4 | 30.90s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Girls 1st Varsity 4+ | girls | 1V | 1 | 17:10.0 | 50.80s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Girls 1x | girls | UNKNOWN | 1 | 19:32.1 | 101.10s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Girls 2nd Novice 8+ | girls | 2nd Novice | 2 | 19:21.1 | 6.30s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Girls 2nd Varsity 4+ | girls | 2V | 1 | 17:41.1 | 6.70s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Girls 2nd Varsity 4+ | girls | 2V | 2 | 17:47.8 | 6.70s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Girls 3rd Varsity 4+ | girls | 3V | 1 | 18:30.6 | 23.60s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Girls 3rd Varsity 4+ | girls | 3V | 2 | 18:54.2 | 23.60s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Girls 4th Varsity 4+ | girls | 4V | 1 | 18:28.3 |  | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |
| 2025-10-26 | MPSRA Fall Championship | Girls 4x+ | girls | UNKNOWN | 3 | 18:41.9 | 101.30s | [herenow](https://legacy.herenow.com/results/#/races/21378/results) |

### 2024 (127 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2024-04-13 | BB&N CRLS | Fifth Boat | boys | 5V | 1 | 5:07.96 | 8.74s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F2BDD2379584CF678DC6C30959529211) |
| 2024-04-13 | BB&N CRLS | Fifth Boat | girls | 5V | 2 | 6:09.7 | 30.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F2BDD2379584CF678DC6C30959529211) |
| 2024-04-13 | BB&N CRLS | First Boat | boys | 1V | 1 | 4:28.07 | 0.87s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F2BDD2379584CF678DC6C30959529211) |
| 2024-04-13 | BB&N CRLS | Fourth Boat | boys | 4V | 1 | 4:57.24 | 4.36s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F2BDD2379584CF678DC6C30959529211) |
| 2024-04-13 | BB&N CRLS | Fourth Boat | girls | 4V | 1 | 5:38.8 |  | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F2BDD2379584CF678DC6C30959529211) |
| 2024-04-13 | BB&N CRLS | Other | girls | UNKNOWN | 2 | 5:01.4 | 9.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F2BDD2379584CF678DC6C30959529211) |
| 2024-04-13 | BB&N CRLS | Other | girls | UNKNOWN | 1 | 5:10.8 | 15.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F2BDD2379584CF678DC6C30959529211) |
| 2024-04-13 | BB&N CRLS | Second Boat | boys | 2V | 2 | 4:36.21 | 3.04s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F2BDD2379584CF678DC6C30959529211) |
| 2024-04-13 | BB&N CRLS | Third Boat | boys | 3V | 2 | 4:55.05 | 12.26s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F2BDD2379584CF678DC6C30959529211) |
| 2024-04-13 | BB&N CRLS | Third Boat | girls | 3V | 1 | 5:13.1 |  | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F2BDD2379584CF678DC6C30959529211) |
| 2024-04-17 | CRLS vs Thayer Academy, BU Academy | First Boat | boys | 1V | 1 | 4:32.09 | 40.85s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5AC13C0A039EE6AFC8E97E47C247F44E) |
| 2024-04-24 | Belmont Hill, Middlesex, CRLS | Fourth Boat | boys | 4V | 2 | 4:57.0 | 18.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=95B6D80715F8274903E678063EA5058A) |
| 2024-04-24 | Belmont Hill, Middlesex, CRLS | Fourth Boat | boys | 4V | 3 | 5:34.4 | 55.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=95B6D80715F8274903E678063EA5058A) |
| 2024-04-24 | Belmont Hill, Middlesex, CRLS | Second Boat | boys | 2V | 2 | 4:46.2 | 20.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=95B6D80715F8274903E678063EA5058A) |
| 2024-04-24 | Belmont Hill, Middlesex, CRLS | Third Boat | boys | 3V | 2 | 4:56.7 | 4.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=95B6D80715F8274903E678063EA5058A) |
| 2024-04-27 | Brooks vs NMH, Middlesex and CRLS | Fifth Boat | boys | 5V | 2 | 6:54.8 | 15.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DA7A1EFD458CB4B765258C3FD9635963) |
| 2024-04-27 | Brooks vs NMH, Middlesex and CRLS | Fifth Boat | girls | 5V | 2 | 8:23.0 | 23.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DA7A1EFD458CB4B765258C3FD9635963) |
| 2024-04-27 | Brooks vs NMH, Middlesex and CRLS | First Boat | boys | 1V | 2 | 5:41.3 | 3.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DA7A1EFD458CB4B765258C3FD9635963) |
| 2024-04-27 | Brooks vs NMH, Middlesex and CRLS | Fourth Boat | boys | 4V | 2 | 5:38.5 | 9.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DA7A1EFD458CB4B765258C3FD9635963) |
| 2024-04-27 | Brooks vs NMH, Middlesex and CRLS | Fourth Boat | girls | 4V | 4 | 6:54.0 | 31.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DA7A1EFD458CB4B765258C3FD9635963) |
| 2024-04-27 | Brooks vs NMH, Middlesex and CRLS | Other | girls | UNKNOWN | 2 | 6:35.3 | 12.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DA7A1EFD458CB4B765258C3FD9635963) |
| 2024-04-27 | Brooks vs NMH, Middlesex and CRLS | Other | girls | UNKNOWN | 4 | 6:22.0 | 13.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DA7A1EFD458CB4B765258C3FD9635963) |
| 2024-04-27 | Brooks vs NMH, Middlesex and CRLS | Second Boat | boys | 2V | 3 | 5:44.4 | 17.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DA7A1EFD458CB4B765258C3FD9635963) |
| 2024-04-27 | Brooks vs NMH, Middlesex and CRLS | Third Boat | boys | 3V | 3 | 5:52.6 | 15.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DA7A1EFD458CB4B765258C3FD9635963) |
| 2024-04-27 | Brooks vs NMH, Middlesex and CRLS | Third Boat | girls | 3V | 1 | 6:12.5 | 0.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DA7A1EFD458CB4B765258C3FD9635963) |
| 2024-05-01 | NCDS, Winsor, CRLS | Fifth Boat | UNKNOWN | 5V | 2 | 5:13 | 3.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C55D042DC8DE58BCD614F6CCB55D1228) |
| 2024-05-01 | NCDS, Winsor, CRLS | First Boat | UNKNOWN | 1V | 1 | 4:46 | 4.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C55D042DC8DE58BCD614F6CCB55D1228) |
| 2024-05-01 | NCDS, Winsor, CRLS | Fourth Boat | UNKNOWN | 4V | 2 | 5:48 | 37.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C55D042DC8DE58BCD614F6CCB55D1228) |
| 2024-05-01 | NCDS, Winsor, CRLS | Second Boat | UNKNOWN | 2V | 1 | 5:01 | 6.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C55D042DC8DE58BCD614F6CCB55D1228) |
| 2024-05-01 | NCDS, Winsor, CRLS | Third Boat | UNKNOWN | 3V | 2 | 5:15 | 9.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C55D042DC8DE58BCD614F6CCB55D1228) |
| 2024-05-04 | Cambridge Rindge and Latin HS at Groton | First Boat | boys | 1V | 2 | 4:07.2 | 9.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CF11D4E6381F0019C765544CCA920DEE) |
| 2024-05-04 | Cambridge Rindge and Latin HS at Groton | Fourth Boat | boys | 4V | 2 | 4:30.8 | 10.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CF11D4E6381F0019C765544CCA920DEE) |
| 2024-05-04 | Cambridge Rindge and Latin HS at Groton | Fourth Boat | girls | 4V | 2 | 5:10.2 | 19.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CF11D4E6381F0019C765544CCA920DEE) |
| 2024-05-04 | Cambridge Rindge and Latin HS at Groton | Other | girls | UNKNOWN | 1 | 4:19.5 | 4.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CF11D4E6381F0019C765544CCA920DEE) |
| 2024-05-04 | Cambridge Rindge and Latin HS at Groton | Other | girls | UNKNOWN | 2 | 4:30.6 | 10.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CF11D4E6381F0019C765544CCA920DEE) |
| 2024-05-04 | Cambridge Rindge and Latin HS at Groton | Second Boat | boys | 2V | 2 | 4:20.4 | 12.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CF11D4E6381F0019C765544CCA920DEE) |
| 2024-05-04 | Cambridge Rindge and Latin HS at Groton | Third Boat | boys | 3V | 2 | 4:17.9 | 8.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CF11D4E6381F0019C765544CCA920DEE) |
| 2024-05-04 | Cambridge Rindge and Latin HS at Groton | Third Boat | girls | 3V | 2 | 4:40.6 | 3.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CF11D4E6381F0019C765544CCA920DEE) |
| 2024-05-11 | Middlesex vs. Cambridge Rindge and Latin Sch | First Boat | boys | 1V | 2 | 5:12.3 | 9.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=61A86E8629F7DAFB0E0306631556FC20) |
| 2024-05-11 | Middlesex vs. Cambridge Rindge and Latin Sch | Fourth Boat | boys | 4V | 1 | 5:44.6 | 17.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=61A86E8629F7DAFB0E0306631556FC20) |
| 2024-05-11 | Middlesex vs. Cambridge Rindge and Latin Sch | Fourth Boat | girls | 4V | 2 | 6:50.4 | 34.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=61A86E8629F7DAFB0E0306631556FC20) |
| 2024-05-11 | Middlesex vs. Cambridge Rindge and Latin Sch | Other | girls | UNKNOWN | 2 | 5:43.1 | 7.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=61A86E8629F7DAFB0E0306631556FC20) |
| 2024-05-11 | Middlesex vs. Cambridge Rindge and Latin Sch | Other | girls | UNKNOWN | 1 | 5:57.6 | 6.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=61A86E8629F7DAFB0E0306631556FC20) |
| 2024-05-11 | Middlesex vs. Cambridge Rindge and Latin Sch | Second Boat | boys | 2V | 1 | 5:35.4 | 12.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=61A86E8629F7DAFB0E0306631556FC20) |
| 2024-05-11 | Middlesex vs. Cambridge Rindge and Latin Sch | Third Boat | boys | 3V | 1 | 5:34.9 | 12.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=61A86E8629F7DAFB0E0306631556FC20) |
| 2024-05-11 | Middlesex vs. Cambridge Rindge and Latin Sch | Third Boat | girls | 3V | 2 | 6:05.1 | 0.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=61A86E8629F7DAFB0E0306631556FC20) |
| 2024-05-18 | USRowing Northeast Youth Championships | Mens Youth 4+ - Time Trial | boys | 1V | 7 | 06:59.67 | 21.32s | [usrowing-timeteam](https://usrowing.regatta.time-team.com/usrowing-northeast-youth/2024/races/a6a6aa0d-ea8c-4cb9-b638-b0c51f3aa574) |
| 2024-05-18 | USRowing Northeast Youth Championships | Womens Youth 4+ - Time Trial | girls | 1V | 4 | 07:34.03 | 13.72s | [usrowing-timeteam](https://usrowing.regatta.time-team.com/usrowing-northeast-youth/2024/races/d5446ed6-ad76-4e87-883b-8f31b6b1ad68) |
| 2024-05-19 | USRowing Northeast Youth Championships | Mens Youth 4+ - Semifinal 2 | boys | 1V | 4 | 07:11.39 | 12.37s | [usrowing-timeteam](https://usrowing.regatta.time-team.com/usrowing-northeast-youth/2024/races/b38b680d-d325-497f-87a5-be5760a15f5d) |
| 2024-05-19 | USRowing Northeast Youth Championships | Womens Youth 4+ - Semifinal 1 | girls | 1V | 5 | 08:06.71 | 22.41s | [usrowing-timeteam](https://usrowing.regatta.time-team.com/usrowing-northeast-youth/2024/races/00c9110f-e575-42a9-bae6-185b1eb6063e) |
| 2024-05-25 | NEIRA Championship 2024 | boys 1V 4+ - Heat 1 | boys | 1V | 6 | 5:16.777 | 11.04s | [neira-championship-pdf](https://neirarowing.org/documents/2024NEIRAResults.pdf) |
| 2024-05-25 | NEIRA Championship 2024 | boys 2V 4+ - Heat 1 | boys | 2V | 4 | 5:24.722 | 15.37s | [neira-championship-pdf](https://neirarowing.org/documents/2024NEIRAResults.pdf) |
| 2024-05-25 | NEIRA Championship 2024 | boys 2V 4+ - Heat 3 | boys | 2V | 6 | 5:27.551 | 7.88s | [neira-championship-pdf](https://neirarowing.org/documents/2024NEIRAResults.pdf) |
| 2024-05-25 | NEIRA Championship 2024 | boys 2V 4+ - Petite Final | boys | 2V | 4 | 5:40.053 | 9.92s | [neira-championship-pdf](https://neirarowing.org/documents/2024NEIRAResults.pdf) |
| 2024-05-25 | NEIRA Championship 2024 | boys 3V 4+ - Grand Final | boys | 3V | 6 | 5:27.551 | 17.57s | [neira-championship-pdf](https://neirarowing.org/documents/2024NEIRAResults.pdf) |
| 2024-05-25 | NEIRA Championship 2024 | boys 3V 4+ - Heat 2 | boys | 3V | 4 | 5:24.722 | 5.72s | [neira-championship-pdf](https://neirarowing.org/documents/2024NEIRAResults.pdf) |
| 2024-05-25 | NEIRA Championship 2024 | boys 4V 4+ - Grand Final | boys | 4V | 6 | 5:58.885 | 41.43s | [neira-championship-pdf](https://neirarowing.org/documents/2024NEIRAResults.pdf) |
| 2024-05-25 | NEIRA Championship 2024 | boys 4V 4+ - Heat 2 | boys | 4V | 3 | 5:36.259 | 23.22s | [neira-championship-pdf](https://neirarowing.org/documents/2024NEIRAResults.pdf) |
| 2024-05-25 | NEIRA Championship 2024 | girls 1V 4+ - Heat 1 | girls | 1V | 3 | 5:46.052 |  | [neira-championship-pdf](https://neirarowing.org/documents/2024NEIRAResults.pdf) |
| 2024-05-25 | NEIRA Championship 2024 | girls 1V 4+ - Petite Final | girls | 1V | 1 | 5:56.896 | 1.88s | [neira-championship-pdf](https://neirarowing.org/documents/2024NEIRAResults.pdf) |
| 2024-05-25 | NEIRA Championship 2024 | girls 2V 4+ - Heat 1 | girls | 2V | 3 | 5:58.471 | 9.17s | [neira-championship-pdf](https://neirarowing.org/documents/2024NEIRAResults.pdf) |
| 2024-05-25 | NEIRA Championship 2024 | girls 2V 4+ - Petite Final | girls | 2V | 4 | 6:13.611 | 4.13s | [neira-championship-pdf](https://neirarowing.org/documents/2024NEIRAResults.pdf) |
| 2024-05-25 | NEIRA Championship 2024 | girls 3V 4+ - Heat 1 | girls | 3V | 5 | 6:01.829 | 15.44s | [neira-championship-pdf](https://neirarowing.org/documents/2024NEIRAResults.pdf) |
| 2024-05-25 | NEIRA Championship 2024 | girls 4V 4+ - Heat 1 | girls | 4V | 6 | 6:36.994 | 37.04s | [neira-championship-pdf](https://neirarowing.org/documents/2024NEIRAResults.pdf) |
| 2024-05-26 | MPSRA Spring Championship | Boys 1st Novice 4+ Grand Final | boys | 1st Novice | 1 | 5:33.4 | 0.70s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Boys 1st Novice 4+ Time Trial | boys | 1st Novice | 4 | 5:31.1 | 5.70s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Boys 1st Varsity 4+ Grand Final | boys | 1V | 1 | 5:05.9 | 8.60s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Boys 1st Varsity 4+ Time Trial | boys | 1V | 1 | 4:48.8 | 6.50s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Boys 2nd Varsity 4+ Grand Final | boys | 2V | 1 | 5:27.9 | 6.50s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Boys 3rd Varsity 4+ Grand Final | boys | 3V | 1 | 5:20.8 | 10.50s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Boys 4th Varsity 4+ Grand Final | boys | 4V | 1 | 5:27.5 | 3.20s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Boys 4th Varsity 4+ Grand Final | boys | 4V | 2 | 5:30.7 | 3.20s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Girls 1st Novice 4+ Grand Final | girls | 1st Novice | 2 | 6:12.4 | 7.30s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Girls 1st Novice 4+ Time Trial | girls | 1st Novice | 1 | 6:01.1 | 0.40s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Girls 1st Novice 8+ Petite Final | girls | 1st Novice | 1 | 6:00.3 | 14.70s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Girls 1st Novice 8+ Time Trial | girls | 1st Novice | 7 | 5:45.3 | 22.90s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Girls 1st Varsity 4+ Grand Final | girls | 1V | 2 | 5:43.7 | 5.40s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Girls 1st Varsity 4+ Time Trial | girls | 1V | 2 | 5:20.9 | 4.20s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Girls 2nd Novice 4+ Grand Final | girls | 2nd Novice | 1 | 6:31.0 | 9.70s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Grand Final | girls | 2V | 2 | 5:49.4 | 9.70s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Time Trial | girls | 2V | 2 | 5:36.0 | 14.60s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Girls 2x Flight 1 | girls | UNKNOWN | 4 | 6:51.1 | 63.70s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Girls 3rd Varsity 4+ Grand Final | girls | 3V | 2 | 5:53.5 | 0.60s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-05-26 | MPSRA Spring Championship | Girls 4th Varsity 4+ Grand Final | girls | 4V | 2 | 6:39.0 | 37.00s | [herenow](https://legacy.herenow.com/results/#/races/21232/results) |
| 2024-09-21 | CRI Fall Classic | Mens Jr 2x | boys | UNKNOWN | 7 | 21:20.2 | 164.80s | [herenow](https://legacy.herenow.com/results/#/races/21276/results) |
| 2024-09-21 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | 1 | 18:41.9 | 5.20s | [herenow](https://legacy.herenow.com/results/#/races/21276/results) |
| 2024-09-21 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | 4 | 19:28.1 | 46.20s | [herenow](https://legacy.herenow.com/results/#/races/21276/results) |
| 2024-09-21 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | 7 | 19:46.3 | 64.40s | [herenow](https://legacy.herenow.com/results/#/races/21276/results) |
| 2024-09-21 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | 8 | 19:50.5 | 68.60s | [herenow](https://legacy.herenow.com/results/#/races/21276/results) |
| 2024-09-21 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | 10 | 19:56.2 | 74.30s | [herenow](https://legacy.herenow.com/results/#/races/21276/results) |
| 2024-09-21 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 7 | 20:42.2 | 54.50s | [herenow](https://legacy.herenow.com/results/#/races/21276/results) |
| 2024-09-21 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 14 | 21:36.4 | 108.70s | [herenow](https://legacy.herenow.com/results/#/races/21276/results) |
| 2024-09-21 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 20 | 22:12.3 | 144.60s | [herenow](https://legacy.herenow.com/results/#/races/21276/results) |
| 2024-09-21 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 24 | 24:14.8 | 267.10s | [herenow](https://legacy.herenow.com/results/#/races/21276/results) |
| 2024-09-21 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 25 | 24:20.7 | 273.00s | [herenow](https://legacy.herenow.com/results/#/races/21276/results) |
| 2024-10-06 | Textile River Regatta | Mens Jr 4+ "A" | boys | UNKNOWN | 4 | 16:54.1 | 34.20s | [herenow](https://legacy.herenow.com/results/#/races/21275/results) |
| 2024-10-06 | Textile River Regatta | Mens Jr 4+ "B" | boys | UNKNOWN | 1 | 16:55.5 | 21.40s | [herenow](https://legacy.herenow.com/results/#/races/21275/results) |
| 2024-10-06 | Textile River Regatta | Mens Jr 4+ "B" | boys | UNKNOWN | 3 | 17:33.6 | 38.10s | [herenow](https://legacy.herenow.com/results/#/races/21275/results) |
| 2024-10-06 | Textile River Regatta | Mens Jr 4+ "B" | boys | UNKNOWN | 9 | 17:53.1 | 57.60s | [herenow](https://legacy.herenow.com/results/#/races/21275/results) |
| 2024-10-06 | Textile River Regatta | Mens Jr 4+ "B" | boys | UNKNOWN | 10 | 18:04.8 | 69.30s | [herenow](https://legacy.herenow.com/results/#/races/21275/results) |
| 2024-10-06 | Textile River Regatta | Mens Jr Novice 8+ | boys | Novice | 1 | 16:28.0 | 14.20s | [herenow](https://legacy.herenow.com/results/#/races/21275/results) |
| 2024-10-06 | Textile River Regatta | Mens Jr Novice 8+ | boys | Novice | 14 | 18:46.3 | 138.30s | [herenow](https://legacy.herenow.com/results/#/races/21275/results) |
| 2024-10-06 | Textile River Regatta | Womens Jr 4+ "A" | girls | UNKNOWN | 6 | 18:41.1 | 51.70s | [herenow](https://legacy.herenow.com/results/#/races/21275/results) |
| 2024-10-06 | Textile River Regatta | Womens Jr 4+ "B" | girls | UNKNOWN | 1 | 18:53.8 | 3.80s | [herenow](https://legacy.herenow.com/results/#/races/21275/results) |
| 2024-10-06 | Textile River Regatta | Womens Jr 4+ "B" | girls | UNKNOWN | 12 | 20:49.4 | 115.60s | [herenow](https://legacy.herenow.com/results/#/races/21275/results) |
| 2024-10-06 | Textile River Regatta | Womens Jr 4+ "B" | girls | UNKNOWN | 13 | 21:17.9 | 144.10s | [herenow](https://legacy.herenow.com/results/#/races/21275/results) |
| 2024-10-06 | Textile River Regatta | Womens Jr 4+ "B" | girls | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21275/results) |
| 2024-10-06 | Textile River Regatta | Womens Jr Novice 8+ | girls | Novice | 9 | 20:13.1 | 91.50s | [herenow](https://legacy.herenow.com/results/#/races/21275/results) |
| 2024-10-06 | Textile River Regatta | Womens Jr Novice 8+ | girls | Novice | 10 | 20:18.6 | 97.00s | [herenow](https://legacy.herenow.com/results/#/races/21275/results) |
| 2024-10-13 | Head of the Quinobequin | Mens U15 1x | boys | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21265/results) |
| 2024-10-13 | Head of the Quinobequin | Mens U17 1x | boys | UNKNOWN | 20 | 13:33.0 | 67.10s | [herenow](https://legacy.herenow.com/results/#/races/21265/results) |
| 2024-10-13 | Head of the Quinobequin | Mens U19 1x | boys | UNKNOWN | 28 | 13:37.1 | 114.30s | [herenow](https://legacy.herenow.com/results/#/races/21265/results) |
| 2024-10-27 | MPSRA Fall Championship | Boys 1st Novice 8+ | boys | 1st Novice | 1 | 15:03.5 | 37.60s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |
| 2024-10-27 | MPSRA Fall Championship | Boys 1st Varsity 4+ | boys | 1V | 1 | 15:46.4 | 11.40s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |
| 2024-10-27 | MPSRA Fall Championship | Boys 2nd Novice 8+ | boys | 2nd Novice | 1 | 17:01.6 | 61.00s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |
| 2024-10-27 | MPSRA Fall Championship | Boys 2nd Varsity 4+ | boys | 2V | 1 | 15:48.0 | 78.20s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |
| 2024-10-27 | MPSRA Fall Championship | Boys 3rd Varsity 4+ | boys | 3V | 1 | 16:53.0 | 8.00s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |
| 2024-10-27 | MPSRA Fall Championship | Boys 4th Varsity 4+ | boys | 4V | 1 | 16:41.2 | 33.50s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |
| 2024-10-27 | MPSRA Fall Championship | Boys 4th Varsity 4+ | boys | 4V | 2 | 17:14.7 | 33.50s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |
| 2024-10-27 | MPSRA Fall Championship | Girls 1st Novice 4+ | girls | 1st Novice | 2 | 19:13.5 | 16.40s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |
| 2024-10-27 | MPSRA Fall Championship | Girls 1st Novice 8+ | girls | 1st Novice | 3 | 18:37.1 | 56.80s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |
| 2024-10-27 | MPSRA Fall Championship | Girls 1st Varsity 4+ | girls | 1V | 1 | 17:22.7 | 32.10s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |
| 2024-10-27 | MPSRA Fall Championship | Girls 2nd Novice 4+ | girls | 2nd Novice | 2 | 19:19.8 | 2.30s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |
| 2024-10-27 | MPSRA Fall Championship | Girls 2nd Varsity 4+ | girls | 2V | 1 | 17:29.4 | 74.50s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |
| 2024-10-27 | MPSRA Fall Championship | Girls 3rd Varsity 4+ | girls | 3V | 1 | 18:10.9 | 94.30s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |
| 2024-10-27 | MPSRA Fall Championship | Girls 4th Varsity 4+ | girls | 4V | 1 | 19:15.5 | 10.90s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |
| 2024-10-27 | MPSRA Fall Championship | Girls 4th Varsity 4+ | girls | 4V | 2 | 19:26.4 | 10.90s | [herenow](https://legacy.herenow.com/results/#/races/21280/results) |

### 2023 (95 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2023-04-08 | Cambridge Mayor's Cup: CRLS vs. BB&N | First Boat | boys | 1V | 2 | 4:26.8 | 4.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F97C64017C4CB0D51F42090A16048CB5) |
| 2023-04-08 | Cambridge Mayor's Cup: CRLS vs. BB&N | Fourth Boat | boys | 4V | 2 | 5:09.0 | 23.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F97C64017C4CB0D51F42090A16048CB5) |
| 2023-04-08 | Cambridge Mayor's Cup: CRLS vs. BB&N | Fourth Boat | girls | 4V | 2 | 5:31.1 | 6.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F97C64017C4CB0D51F42090A16048CB5) |
| 2023-04-08 | Cambridge Mayor's Cup: CRLS vs. BB&N | Other | girls | UNKNOWN | 1 | 4:39.8 | 5.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F97C64017C4CB0D51F42090A16048CB5) |
| 2023-04-08 | Cambridge Mayor's Cup: CRLS vs. BB&N | Other | girls | UNKNOWN | 2 | 5:22.0 | 29.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F97C64017C4CB0D51F42090A16048CB5) |
| 2023-04-08 | Cambridge Mayor's Cup: CRLS vs. BB&N | Second Boat | boys | 2V | 2 | 4:35.0 | 8.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F97C64017C4CB0D51F42090A16048CB5) |
| 2023-04-08 | Cambridge Mayor's Cup: CRLS vs. BB&N | Third Boat | boys | 3V | 1 | 4:40.8 | 2.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F97C64017C4CB0D51F42090A16048CB5) |
| 2023-04-08 | Cambridge Mayor's Cup: CRLS vs. BB&N | Third Boat | girls | 3V | 1 | 5:12.1 | 14.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F97C64017C4CB0D51F42090A16048CB5) |
| 2023-04-29 | Northfield Mount Hermon, Brooks School, Camb | Fifth Boat | girls | 5V | 3 | 8:08 | 82.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6B0B61A81F7CAE8C8A32C8CDB18E91ED) |
| 2023-04-29 | Northfield Mount Hermon, Brooks School, Camb | First Boat | boys | 1V | 3 | 5:37.1 | 40.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6B0B61A81F7CAE8C8A32C8CDB18E91ED) |
| 2023-04-29 | Northfield Mount Hermon, Brooks School, Camb | Fourth Boat | boys | 4V | 3 | 6:37.8 | 52.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6B0B61A81F7CAE8C8A32C8CDB18E91ED) |
| 2023-04-29 | Northfield Mount Hermon, Brooks School, Camb | Fourth Boat | girls | 4V | 3 | 7:12 | 41.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6B0B61A81F7CAE8C8A32C8CDB18E91ED) |
| 2023-04-29 | Northfield Mount Hermon, Brooks School, Camb | Other | girls | UNKNOWN | 3 | 5:55 | 5.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6B0B61A81F7CAE8C8A32C8CDB18E91ED) |
| 2023-04-29 | Northfield Mount Hermon, Brooks School, Camb | Other | girls | UNKNOWN | 3 | 6:30 | 30.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6B0B61A81F7CAE8C8A32C8CDB18E91ED) |
| 2023-04-29 | Northfield Mount Hermon, Brooks School, Camb | Third Boat | boys | 3V | 3 | 5:57.4 | 27.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6B0B61A81F7CAE8C8A32C8CDB18E91ED) |
| 2023-04-29 | Northfield Mount Hermon, Brooks School, Camb | Third Boat | girls | 3V | 3 | 6:44 | 27.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6B0B61A81F7CAE8C8A32C8CDB18E91ED) |
| 2023-05-11 | Cambridge Rindge & Latin School vs. Winsor | Fifth Boat | girls | 5V | 2 | 4:49.5 | 8.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C3AD5F84C851A4FEB8A1DD57712CF3C0) |
| 2023-05-11 | Cambridge Rindge & Latin School vs. Winsor | First Boat | girls | 1V | 2 | 4:35.0 | 5.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C3AD5F84C851A4FEB8A1DD57712CF3C0) |
| 2023-05-11 | Cambridge Rindge & Latin School vs. Winsor | Fourth Boat | girls | 4V | 2 | 5:32.0 | 37.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C3AD5F84C851A4FEB8A1DD57712CF3C0) |
| 2023-05-11 | Cambridge Rindge & Latin School vs. Winsor | Second Boat | girls | 2V | 2 | 5:12.2 | 23.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C3AD5F84C851A4FEB8A1DD57712CF3C0) |
| 2023-05-11 | Cambridge Rindge & Latin School vs. Winsor | Third Boat | girls | 3V | 2 | 5:06.5 | 15.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C3AD5F84C851A4FEB8A1DD57712CF3C0) |
| 2023-05-13 | NEIRA Cambridge Rindge and Latin vs Thayer B | First Boat | boys | 1V | 1 | 4:11.88 | 36.62s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F3E40CF56EBACA5850DF8BE2AC2814D4) |
| 2023-05-13 | NEIRA Cambridge Rindge and Latin vs Thayer B | Other | girls | 5V | 1 | 4:59 | 13.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F3E40CF56EBACA5850DF8BE2AC2814D4) |
| 2023-05-13 | NEIRA Cambridge Rindge and Latin vs Thayer B | Second Boat | boys | 2V | 1 | 4:28 | 14.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F3E40CF56EBACA5850DF8BE2AC2814D4) |
| 2023-05-13 | NEIRA Cambridge Rindge and Latin vs Thayer B | Second Boat | boys | 5V | 3 | 4:46 | 18.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F3E40CF56EBACA5850DF8BE2AC2814D4) |
| 2023-05-13 | NEIRA Cambridge Rindge and Latin vs Thayer B | Third Boat | boys | 3V | 2 | 4:56.23 | 15.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F3E40CF56EBACA5850DF8BE2AC2814D4) |
| 2023-05-20 | Belmont Hill vs. NMH, CRLS | First Boat | boys | 1V | 3 | 4:32.6 | 19.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=A0C7FFCB8A3511C37F63CEAAF96C4DBE) |
| 2023-05-20 | Belmont Hill vs. NMH, CRLS | Fourth Boat | boys | 3V | 2 | 5:13.1 | 35.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=A0C7FFCB8A3511C37F63CEAAF96C4DBE) |
| 2023-05-20 | Belmont Hill vs. NMH, CRLS | Second Boat | boys | 2V | 3 | 4:55.1 | 26.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=A0C7FFCB8A3511C37F63CEAAF96C4DBE) |
| 2023-05-20 | Northeast Youth Championship | Womens Novice 4+ Heat 3 | girls | Novice | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21133/results) |
| 2023-05-20 | Northeast Youth Championship | Womens U17 4+ Final | girls | UNKNOWN | 6 | 8:12.7 | 53.60s | [herenow](https://legacy.herenow.com/results/#/races/21133/results) |
| 2023-05-20 | Northeast Youth Championship | Womens U17 4+ Semifinal 2 | girls | UNKNOWN | 3 | 8:15.5 | 34.30s | [herenow](https://legacy.herenow.com/results/#/races/21133/results) |
| 2023-05-20 | Northeast Youth Championship | Womens U17 4+ Time Trial | girls | UNKNOWN | 7 | 8:29.0 | 51.20s | [herenow](https://legacy.herenow.com/results/#/races/21133/results) |
| 2023-05-20 | Northeast Youth Championship | Womens Youth 2nd 4+ Heat 1 | girls | 2V | 3 | 8:08.4 | 68.00s | [herenow](https://legacy.herenow.com/results/#/races/21133/results) |
| 2023-05-20 | Northeast Youth Championship | Womens Youth 2nd 4+ Heat 3 | girls | 2V | 4 | 9:02.8 | 43.60s | [herenow](https://legacy.herenow.com/results/#/races/21133/results) |
| 2023-05-20 | Northeast Youth Championship | Womens Youth 4+ Semifinal 2 | girls | 1V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21133/results) |
| 2023-05-20 | Northeast Youth Championship | Womens Youth 4+ Time Trial | girls | 1V | 7 | 7:53.1 | 26.90s | [herenow](https://legacy.herenow.com/results/#/races/21133/results) |
| 2023-05-27 | NEIRA Championship 2023 | girls 1V 4+ - Heat 2 | girls | 1V | 4 | 5:46.289 | 13.11s | [neira-championship-pdf](https://neirarowing.org/documents/2023NEIRAResults.pdf) |
| 2023-05-27 | NEIRA Championship 2023 | girls 1V 4+ - Petite Final | girls | 1V | 5 | 5:58.659 | 11.66s | [neira-championship-pdf](https://neirarowing.org/documents/2023NEIRAResults.pdf) |
| 2023-05-27 | NEIRA Championship 2023 | girls 3V 4+ - Heat 2 | girls | 3V | 6 | 6:28.398 | 36.82s | [neira-championship-pdf](https://neirarowing.org/documents/2023NEIRAResults.pdf) |
| 2023-05-28 | MPSRA Spring Championship | Boys 1st Novice 4+ Final A | boys | 1st Novice | 2 | 5:29.7 | 16.10s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Boys 1st Varsity 4+ Final A | boys | 1V | 2 | 5:07.6 | 8.90s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Boys 1st Varsity 4+ Time Trial | boys | 1V | 2 | 4:59.4 | 11.80s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Boys 2nd Novice 4+ Final A | boys | 2nd Novice | 2 | 5:48.9 | 13.00s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Boys 2nd Varsity 4+ Final A | boys | 2V | 1 | 5:08.9 | 3.90s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Boys 3rd Varsity 4+ Final A | boys | 3V | 3 | 5:38.5 | 30.00s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Boys Novice 2x Final A | boys | Novice | 6 | 6:10.5 | 38.60s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Girls 1st Novice 4+ Final A | girls | 1st Novice | 1 | 5:39.2 | 25.90s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Girls 1st Novice 4+ Time Trial | girls | 1st Novice | 1 | 5:42.0 | 31.20s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Girls 1st Novice 8+ Final B | girls | 1st Novice | 2 | 5:59.4 | 13.50s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Girls 1st Novice 8+ Time Trial | girls | 1st Novice | 7 | 6:03.1 | 45.50s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Girls 1st Varsity 4+ Final A | girls | 1V | 1 | 5:27.8 | 15.00s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Girls 1st Varsity 4+ Time Trial | girls | 1V | 1 | 5:29.5 | 20.70s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Final A | girls | 2V | 1 | 5:44.3 | 7.40s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Girls 2x Flight 2 | girls | UNKNOWN | 3 | 6:37.7 | 46.70s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Girls 3rd Varsity 4+ Final A | girls | 3V | 1 | 6:01.7 | 24.70s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-05-28 | MPSRA Spring Championship | Girls 3rd Varsity 4+ Final A | girls | 3V | 2 | 6:26.4 | 24.70s | [herenow](https://legacy.herenow.com/results/#/races/21141/results) |
| 2023-10-01 | Textile River Regatta | Mens Jr 4+ "A" | boys | UNKNOWN | 2 | 15:53.2 | 3.10s | [herenow](https://legacy.herenow.com/results/#/races/21165/results) |
| 2023-10-01 | Textile River Regatta | Mens Jr 4+ "B" | boys | UNKNOWN | 17 | 19:08.5 | 187.10s | [herenow](https://legacy.herenow.com/results/#/races/21165/results) |
| 2023-10-01 | Textile River Regatta | Mens Jr 8+ "A" | boys | UNKNOWN | 15 | 15:53.9 | 92.80s | [herenow](https://legacy.herenow.com/results/#/races/21165/results) |
| 2023-10-01 | Textile River Regatta | Mens Jr Ltwt 4+ | boys | UNKNOWN | 2 | 16:45.0 | 1.70s | [herenow](https://legacy.herenow.com/results/#/races/21165/results) |
| 2023-10-01 | Textile River Regatta | Mens Jr Ltwt 4+ | boys | UNKNOWN | 7 | 19:11.1 | 147.80s | [herenow](https://legacy.herenow.com/results/#/races/21165/results) |
| 2023-10-01 | Textile River Regatta | Womens Jr 4+ "A" | girls | UNKNOWN | 4 | 17:10.1 | 9.80s | [herenow](https://legacy.herenow.com/results/#/races/21165/results) |
| 2023-10-01 | Textile River Regatta | Womens Jr 4+ "B" | girls | UNKNOWN | 3 | 17:53.5 | 32.00s | [herenow](https://legacy.herenow.com/results/#/races/21165/results) |
| 2023-10-01 | Textile River Regatta | Womens Jr 4+ "B" | girls | UNKNOWN | 7 | 18:19.6 | 58.10s | [herenow](https://legacy.herenow.com/results/#/races/21165/results) |
| 2023-10-01 | Textile River Regatta | Womens Jr 4x+ | girls | UNKNOWN | 3 | 18:19.0 | 85.30s | [herenow](https://legacy.herenow.com/results/#/races/21165/results) |
| 2023-10-01 | Textile River Regatta | Womens Jr 8+ "A" | girls | UNKNOWN | 12 | 18:18.9 | 130.40s | [herenow](https://legacy.herenow.com/results/#/races/21165/results) |
| 2023-10-08 | New England Jr/HS/Masters Championship | Mens Jr/HS 1st Novice 8+ | boys | 1st Novice | 7 | 16:34.3 | 93.20s | [herenow](https://legacy.herenow.com/results/#/races/21161/results) |
| 2023-10-08 | New England Jr/HS/Masters Championship | Mens Jr/HS 1st Varsity 4+ | boys | 1V | 5 | 15:26.8 | 61.40s | [herenow](https://legacy.herenow.com/results/#/races/21161/results) |
| 2023-10-08 | New England Jr/HS/Masters Championship | Mens Jr/HS 1st Varsity 8+ | boys | 1V | 15 | 14:50.0 | 70.00s | [herenow](https://legacy.herenow.com/results/#/races/21161/results) |
| 2023-10-08 | New England Jr/HS/Masters Championship | Mens Jr/HS 2nd Varsity 4+ | boys | 2V | 8 | 17:36.1 | 115.50s | [herenow](https://legacy.herenow.com/results/#/races/21161/results) |
| 2023-10-08 | New England Jr/HS/Masters Championship | Mens Jr/HS 3rd/4th Varsity 4+ | boys | 4V | 2 | 18:31.0 | 41.50s | [herenow](https://legacy.herenow.com/results/#/races/21161/results) |
| 2023-10-08 | New England Jr/HS/Masters Championship | Womens Jr/HS 1st Novice 8+ | girls | 1st Novice | 13 | 20:47.0 | 252.10s | [herenow](https://legacy.herenow.com/results/#/races/21161/results) |
| 2023-10-08 | New England Jr/HS/Masters Championship | Womens Jr/HS 1st Varsity 4+ | girls | 1V | 2 | 16:47.1 | 1.60s | [herenow](https://legacy.herenow.com/results/#/races/21161/results) |
| 2023-10-08 | New England Jr/HS/Masters Championship | Womens Jr/HS 2nd Varsity 4+ | girls | 2V | 2 | 17:29.4 | 26.80s | [herenow](https://legacy.herenow.com/results/#/races/21161/results) |
| 2023-10-08 | New England Jr/HS/Masters Championship | Womens Jr/HS 3rd/4th Varsity 4+ | girls | 4V | 2 | 18:34.2 | 8.50s | [herenow](https://legacy.herenow.com/results/#/races/21161/results) |
| 2023-10-08 | New England Jr/HS/Masters Championship | Womens Jr/HS 4x+ (HOCR) | girls | UNKNOWN | 7 | 17:30.0 | 71.70s | [herenow](https://legacy.herenow.com/results/#/races/21161/results) |
| 2023-10-08 | New England Jr/HS/Masters Championship | Womens Jr/HS 4x+ (HOCR) | girls | UNKNOWN | 8 | 19:01.2 | 162.90s | [herenow](https://legacy.herenow.com/results/#/races/21161/results) |
| 2023-10-29 | MPSRA Fall Championship | Boys 1st Novice 4+ | boys | 1st Novice | 2 | 16:49.2 | 25.80s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Boys 1st Novice 8+ | boys | 1st Novice | 2 | 16:13.7 | 14.40s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Boys 1st Varsity 4+ | boys | 1V | 1 | 16:17.3 | 5.10s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Boys 1st Varsity 8+ | boys | 1V | 6 | 15:53.5 | 97.40s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Boys 2nd Novice 4+ | boys | 2nd Novice | 2 | 19:44.5 | 88.80s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Boys 2nd Varsity 4+ | boys | 2V | 2 | 16:41.5 | 27.70s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Boys 3rd Varsity 4+ | boys | 3V | 2 | 17:51.0 | 27.70s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Boys 4th Varsity 4+ | boys | 4V | 1 | 17:44.2 | 18.00s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Girls 1st Novice 4+ | girls | 1st Novice | 3 | 19:44.6 | 83.80s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Girls 1st Novice 8+ | girls | 1st Novice | 6 | 19:22.8 | 155.70s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Girls 1st Varsity 4+ | girls | 1V | 1 | 17:10.7 | 55.40s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Girls 1st Varsity 8+ | girls | 1V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Girls 2nd Novice 4+ | girls | 2nd Novice | 3 | 23:27.5 | 230.90s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Girls 2nd Varsity 4+ | girls | 2V | 1 | 21:27.1 | 25.50s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Girls 3rd Varsity 4+ | girls | 3V | 2 | 20:17.6 | 68.10s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Girls 4th Varsity 4+ | girls | 4V | 1 | 18:23.0 |  | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |
| 2023-10-29 | MPSRA Fall Championship | Girls 4x | girls | UNKNOWN | 2 | 18:51.1 | 126.30s | [herenow](https://legacy.herenow.com/results/#/races/21187/results) |

### 2022 (110 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2022-04-09 | BB&N and CRLS | First Boat | girls | 1V | 1 | 4:49.7 | 15.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=ECDDEE684E95653E3CEA80483918B760) |
| 2022-04-09 | BB&N and CRLS | Fourth Boat | girls | 4V | 2 | 6:00.4 | 10.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=ECDDEE684E95653E3CEA80483918B760) |
| 2022-04-09 | BB&N and CRLS | Second Boat | girls | 2V | 1 | 5:13.1 | 9.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=ECDDEE684E95653E3CEA80483918B760) |
| 2022-04-09 | BB&N and CRLS | Third Boat | girls | 3V | 1 | 5:46.7 | 4.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=ECDDEE684E95653E3CEA80483918B760) |
| 2022-04-09 | The Mayor's Cup: BB&N vs CRLS | First Boat | boys | 1V | 2 | 4:45.5 | 5.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F4DB651BE2D4C9B2A83E07E1F473870F) |
| 2022-04-09 | The Mayor's Cup: BB&N vs CRLS | Second Boat | boys | 2V | 1 | 5:04.3 | 5.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F4DB651BE2D4C9B2A83E07E1F473870F) |
| 2022-04-09 | The Mayor's Cup: BB&N vs CRLS | Third Boat | boys | 3V | 1 | 5:04.2 | 2.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=F4DB651BE2D4C9B2A83E07E1F473870F) |
| 2022-04-13 | CRLS @ NCDS | First Boat | girls | 1V | 1 | 4:29 | 28.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5AD11BA575254EB4FDBDAC67D084DA89) |
| 2022-04-13 | CRLS @ NCDS | Fourth Boat | girls | 4V | 2 | 5:27 | 18.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5AD11BA575254EB4FDBDAC67D084DA89) |
| 2022-04-13 | CRLS @ NCDS | Second Boat | girls | 2V | 1 | 4:32 | 16.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5AD11BA575254EB4FDBDAC67D084DA89) |
| 2022-04-13 | CRLS @ NCDS | Third Boat | girls | 3V | 1 | 4:54 | 13.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5AD11BA575254EB4FDBDAC67D084DA89) |
| 2022-05-01 | Derryfield vs. CRLS, UVRF | First Boat | boys | 1V | 2 | 5:12.9 | 8.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB9C5AB2591B00002BCDA5E1E09E7CF5) |
| 2022-05-01 | Derryfield vs. CRLS, UVRF | Fourth Boat | boys | 4V | 1 | 4:53.6 | 36.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB9C5AB2591B00002BCDA5E1E09E7CF5) |
| 2022-05-01 | Derryfield vs. CRLS, UVRF | Fourth Boat | boys | 4V | 3 | 5:37.1 | 43.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB9C5AB2591B00002BCDA5E1E09E7CF5) |
| 2022-05-01 | Derryfield vs. CRLS, UVRF | Fourth Boat | girls | 4V | 1 | 6:13.6 | 16.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB9C5AB2591B00002BCDA5E1E09E7CF5) |
| 2022-05-01 | Derryfield vs. CRLS, UVRF | Fourth Boat | girls | 4V | 3 | 6:55.1 | 41.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB9C5AB2591B00002BCDA5E1E09E7CF5) |
| 2022-05-01 | Derryfield vs. CRLS, UVRF | Other | girls | UNKNOWN | 1 | 5:18.4 | 14.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB9C5AB2591B00002BCDA5E1E09E7CF5) |
| 2022-05-01 | Derryfield vs. CRLS, UVRF | Second Boat | boys | 2V | 2 | 5:18.3 | 2.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB9C5AB2591B00002BCDA5E1E09E7CF5) |
| 2022-05-01 | Derryfield vs. CRLS, UVRF | Third Boat | boys | 3V | 1 | 5:28.1 | 6.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB9C5AB2591B00002BCDA5E1E09E7CF5) |
| 2022-05-01 | Derryfield vs. CRLS, UVRF | Third Boat | girls | 3V | 1 | 5:52.9 | 14.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB9C5AB2591B00002BCDA5E1E09E7CF5) |
| 2022-05-12 | Cambridge Rindge and Latin v Winsor | First Boat | girls | 1V | 2 | 4:56.96 | 4.91s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=40CD5E5E7FC52F043A3214833B44325D) |
| 2022-05-12 | Cambridge Rindge and Latin v Winsor | Fourth Boat | girls | 4V | 2 | 6:40.07 | 73.42s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=40CD5E5E7FC52F043A3214833B44325D) |
| 2022-05-12 | Cambridge Rindge and Latin v Winsor | Second Boat | girls | 2V | 2 | 5:15.10 | 6.99s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=40CD5E5E7FC52F043A3214833B44325D) |
| 2022-05-12 | Cambridge Rindge and Latin v Winsor | Third Boat | girls | 3V | 2 | 6:03.71 | 35.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=40CD5E5E7FC52F043A3214833B44325D) |
| 2022-05-15 | Belmont Hill vs CRLS | First Boat | boys | 1V | 2 | 4:29.5 | 16.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C0D32EC751DC897A975EB4F33D426102) |
| 2022-05-15 | Belmont Hill vs CRLS | Second Boat | boys | 2V | 2 | 4:54.9 | 26.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C0D32EC751DC897A975EB4F33D426102) |
| 2022-05-15 | Belmont Hill vs CRLS | Third Boat | boys | 3V | 1 | 4:59.7 | 6.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C0D32EC751DC897A975EB4F33D426102) |
| 2022-05-15 | Belmont Hill vs CRLS | Third Boat | boys | 3V | 3 | 5:58.4 | 58.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C0D32EC751DC897A975EB4F33D426102) |
| 2022-05-21 | Northeast Youth Championship | Mens Novice 4+ Heat 3 | boys | Novice | 5 | 8:21.9 | 56.50s | [herenow](https://legacy.herenow.com/results/#/races/21017/results) |
| 2022-05-21 | Northeast Youth Championship | Mens U17 4+ Time Trial | boys | UNKNOWN | 8 | 6:39.3 | 31.40s | [herenow](https://legacy.herenow.com/results/#/races/21017/results) |
| 2022-05-21 | Northeast Youth Championship | Mens Youth 2nd 4+ Heat 1 | boys | 2V | 5 | 7:53.4 | 63.90s | [herenow](https://legacy.herenow.com/results/#/races/21017/results) |
| 2022-05-21 | Northeast Youth Championship | Mens Youth 4+ Time Trial | boys | 1V | 19 | 6:57.4 | 51.70s | [herenow](https://legacy.herenow.com/results/#/races/21017/results) |
| 2022-05-21 | Northeast Youth Championship | Womens Novice 4+ Heat 2 | girls | Novice | 5 | 9:29.6 | 110.30s | [herenow](https://legacy.herenow.com/results/#/races/21017/results) |
| 2022-05-21 | Northeast Youth Championship | Womens Novice 8+ Heat 1 | girls | Novice | 5 | 8:47.4 | 100.40s | [herenow](https://legacy.herenow.com/results/#/races/21017/results) |
| 2022-05-21 | Northeast Youth Championship | Womens U17 4+ Final | girls | UNKNOWN | 6 | 8:14.0 | 42.00s | [herenow](https://legacy.herenow.com/results/#/races/21017/results) |
| 2022-05-21 | Northeast Youth Championship | Womens U17 4+ Time Trial | girls | UNKNOWN | 4 | 7:09.8 | 25.50s | [herenow](https://legacy.herenow.com/results/#/races/21017/results) |
| 2022-05-21 | Northeast Youth Championship | Womens Youth 2nd 4+ Final | girls | 2V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21017/results) |
| 2022-05-21 | Northeast Youth Championship | Womens Youth 2nd 4+ Heat 1 | girls | 2V | 2 | 7:40.4 | 14.00s | [herenow](https://legacy.herenow.com/results/#/races/21017/results) |
| 2022-05-21 | Northeast Youth Championship | Womens Youth 2nd 4+ Heat 1 | girls | 2V | 4 | 8:48.8 | 82.40s | [herenow](https://legacy.herenow.com/results/#/races/21017/results) |
| 2022-05-21 | Northeast Youth Championship | Womens Youth 4+ Final | girls | 1V | 1 | 7:21.8 | 2.50s | [herenow](https://legacy.herenow.com/results/#/races/21017/results) |
| 2022-05-21 | Northeast Youth Championship | Womens Youth 4+ Semi-Final 1 | girls | 1V | 1 | 7:19.2 | 5.00s | [herenow](https://legacy.herenow.com/results/#/races/21017/results) |
| 2022-05-21 | Northeast Youth Championship | Womens Youth 4+ Time Trial | girls | 1V | 1 | 6:42.8 | 0.50s | [herenow](https://legacy.herenow.com/results/#/races/21017/results) |
| 2022-05-28 | NEIRA Championship 2022 | girls 1V 4+ - Grand Final | girls | 1V | 4 | 5:46.872 | 8.56s | [neira-championship-pdf](https://neirarowing.org/documents/2022NEIRA.pdf) |
| 2022-05-28 | NEIRA Championship 2022 | girls 2V 4+ - Final 3 | girls | 2V | 1 | 6:13.250 | 2.91s | [neira-championship-pdf](https://neirarowing.org/documents/2022NEIRA.pdf) |
| 2022-05-29 | MPSRA Spring Championship | Boys 1st Novice 4+ Final A | boys | 1st Novice | 2 | 5:31.6 | 7.70s | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Boys 1st Varsity 4+ Final A | boys | 1V | 3 | 5:19.5 | 17.00s | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Boys 1st Varsity 4+ Time Trial | boys | 1V | 3 | 5:25.2 | 12.30s | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Boys 1x Flight 1 | boys | UNKNOWN | 2 | 6:16.3 | 34.70s | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Boys 2nd Novice 4+ Final A | boys | 2nd Novice | 1 | 5:48.6 | 26.30s | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Boys 2nd Varsity 4+ Final A | boys | 2V | 2 | 5:27.5 | 4.80s | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Boys 3rd Varsity 4+ Final A | boys | 3V | 2 | 6:31.5 | 47.60s | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Girls 1st Novice 4+ Final A | girls | 1st Novice | 3 | 6:24.2 | 17.70s | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Girls 1st Novice 4+ Time Trial | girls | 1st Novice | 4 | 6:15.0 | 19.60s | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Girls 1st Novice 8+ Final B | girls | 1st Novice | 2 | 6:14.1 | 20.10s | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Girls 1st Novice 8+ Time Trial | girls | 1st Novice | 8 | 6:21.3 | 44.50s | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Girls 1st Varsity 4+ Final A | girls | 1V | 1 | 5:14.8 | 39.60s | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Final A | girls | 2V | 1 | 5:36.5 | 25.20s | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Girls 2x Flight 2 | girls | UNKNOWN | 2 | 6:51.5 | 30.30s | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Girls 3rd Varsity 4+ Final A | girls | 3V | 1 | 6:02.0 |  | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-05-29 | MPSRA Spring Championship | Girls 4th Varsity 4+ Final A | girls | 4V | 1 | 6:05.2 |  | [herenow](https://legacy.herenow.com/results/#/races/21031/results) |
| 2022-06-09 | Youth National Championship | Womens Youth 4+ A/B Semi Final 1 | girls | 1V | 4 | 7:29.5 | 8.40s | [herenow](https://legacy.herenow.com/results/#/races/21018/results) |
| 2022-06-09 | Youth National Championship | Womens Youth 4+ Final B | girls | 1V | 2 | 7:24.9 | 1.00s | [herenow](https://legacy.herenow.com/results/#/races/21018/results) |
| 2022-06-09 | Youth National Championship | Womens Youth 4+ Time Trial | girls | 1V | 5 | 7:06.0 | 4.60s | [herenow](https://legacy.herenow.com/results/#/races/21018/results) |
| 2022-09-17 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21042/results) |
| 2022-09-17 | CRI Fall Classic | Mens Jr 8+ | boys | UNKNOWN | 8 | 18:03.0 | 84.50s | [herenow](https://legacy.herenow.com/results/#/races/21042/results) |
| 2022-09-17 | CRI Fall Classic | Mens Jr 8+ | boys | UNKNOWN | 21 | 19:49.9 | 191.40s | [herenow](https://legacy.herenow.com/results/#/races/21042/results) |
| 2022-09-17 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 4 | 20:39.2 | 58.00s | [herenow](https://legacy.herenow.com/results/#/races/21042/results) |
| 2022-09-17 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 15 | 22:30.0 | 168.80s | [herenow](https://legacy.herenow.com/results/#/races/21042/results) |
| 2022-09-17 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 22 | 24:16.2 | 275.00s | [herenow](https://legacy.herenow.com/results/#/races/21042/results) |
| 2022-09-17 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 25 | 24:40.0 | 298.80s | [herenow](https://legacy.herenow.com/results/#/races/21042/results) |
| 2022-09-17 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21042/results) |
| 2022-10-02 | Garbage | Mens Jr Ltwt 4+ | boys | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21053/results) |
| 2022-10-02 | Garbage | Womens Jr 4+ "B" | girls | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21053/results) |
| 2022-10-02 | Textile River Regatta | Mens Jr 8+ "A" | boys | UNKNOWN | 12 | 18:24.3 | 111.00s | [herenow](https://legacy.herenow.com/results/#/races/21069/results) |
| 2022-10-02 | Textile River Regatta | Mens Jr Ltwt 4+  (CANCELLED) | boys | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21069/results) |
| 2022-10-02 | Textile River Regatta | Womens Jr 4+ "A" | girls | UNKNOWN | 2 | 19:59.3 | 10.20s | [herenow](https://legacy.herenow.com/results/#/races/21069/results) |
| 2022-10-02 | Textile River Regatta | Womens Jr 4+ "B" | girls | UNKNOWN | 10 | 22:15.0 | 183.50s | [herenow](https://legacy.herenow.com/results/#/races/21069/results) |
| 2022-10-02 | Textile River Regatta | Womens Jr 4+ "B" | girls | UNKNOWN | 13 | 22:23.8 | 192.30s | [herenow](https://legacy.herenow.com/results/#/races/21069/results) |
| 2022-10-02 | Textile River Regatta | Womens Jr 8+ "B" | girls | UNKNOWN | 9 | 21:33.6 | 105.20s | [herenow](https://legacy.herenow.com/results/#/races/21069/results) |
| 2022-10-08 | New England Jr/HS/Masters Championship | Mens Jr/HS 1st Novice 8+ | boys | 1st Novice | 20 | 19:58.7 | 248.30s | [herenow](https://legacy.herenow.com/results/#/races/21057/results) |
| 2022-10-08 | New England Jr/HS/Masters Championship | Mens Jr/HS 1st Varsity 4+ | boys | 1V | 7 | 15:51.2 | 73.50s | [herenow](https://legacy.herenow.com/results/#/races/21057/results) |
| 2022-10-08 | New England Jr/HS/Masters Championship | Mens Jr/HS 2nd Varsity 4+ | boys | 2V | 2 | 15:57.9 | 66.30s | [herenow](https://legacy.herenow.com/results/#/races/21057/results) |
| 2022-10-08 | New England Jr/HS/Masters Championship | Mens Jr/HS 3rd/4th Varsity 4+ | boys | 4V | 3 | 16:22.9 | 81.70s | [herenow](https://legacy.herenow.com/results/#/races/21057/results) |
| 2022-10-08 | New England Jr/HS/Masters Championship | Mens Jr/HS 3rd/4th Varsity 4+ | boys | 4V | 6 | 17:38.7 | 157.50s | [herenow](https://legacy.herenow.com/results/#/races/21057/results) |
| 2022-10-08 | New England Jr/HS/Masters Championship | Womens Jr/HS 1st Novice 4+ | girls | 1st Novice | 5 | 20:31.4 | 79.50s | [herenow](https://legacy.herenow.com/results/#/races/21057/results) |
| 2022-10-08 | New England Jr/HS/Masters Championship | Womens Jr/HS 1st Novice 8+ | girls | 1st Novice | 12 | 19:18.5 | 129.90s | [herenow](https://legacy.herenow.com/results/#/races/21057/results) |
| 2022-10-08 | New England Jr/HS/Masters Championship | Womens Jr/HS 1st Varsity 4+ | girls | 1V | 1 | 16:35.2 | 16.60s | [herenow](https://legacy.herenow.com/results/#/races/21057/results) |
| 2022-10-08 | New England Jr/HS/Masters Championship | Womens Jr/HS 2nd Novice 8+ | girls | 2nd Novice | 6 | 20:49.6 | 154.80s | [herenow](https://legacy.herenow.com/results/#/races/21057/results) |
| 2022-10-08 | New England Jr/HS/Masters Championship | Womens Jr/HS 2nd Varsity 4+ | girls | 2V | 2 | 18:37.1 | 21.60s | [herenow](https://legacy.herenow.com/results/#/races/21057/results) |
| 2022-10-08 | New England Jr/HS/Masters Championship | Womens Jr/HS 3rd/4th Varsity 4+ | girls | 4V | 1 | 19:50.2 | 88.80s | [herenow](https://legacy.herenow.com/results/#/races/21057/results) |
| 2022-10-08 | New England Jr/HS/Masters Championship | Womens Jr/HS 3rd/4th Varsity 4+ | girls | 4V | 2 | 21:19.0 | 88.80s | [herenow](https://legacy.herenow.com/results/#/races/21057/results) |
| 2022-10-15 | Head of the Kevin 3 | Men's Champ Single | boys | UNKNOWN | 28 | 18:17.8 | 212.30s | [herenow](https://legacy.herenow.com/results/#/races/21048/results) |
| 2022-10-15 | Head of the Kevin 3 | Men's Champ Single | boys | UNKNOWN | 31 | 18:21.7 | 216.20s | [herenow](https://legacy.herenow.com/results/#/races/21048/results) |
| 2022-10-15 | Head of the Kevin 3 | Men's Champ Single | boys | UNKNOWN | 51 | 19:26.0 | 280.50s | [herenow](https://legacy.herenow.com/results/#/races/21048/results) |
| 2022-10-15 | Head of the Kevin 3 | Men's Champ Single | boys | UNKNOWN | 117 | 24:04.3 | 558.80s | [herenow](https://legacy.herenow.com/results/#/races/21048/results) |
| 2022-10-30 | MPSRA Fall Championship | Boys 1st Novice 4+ | boys | 1st Novice | 3 | 19:39.8 | 75.70s | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |
| 2022-10-30 | MPSRA Fall Championship | Boys 1st Varsity 4+ | boys | 1V | 1 | 16:49.1 | 12.30s | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |
| 2022-10-30 | MPSRA Fall Championship | Boys 2nd Novice 4+ | boys | 2nd Novice | 1 | 21:40.9 | 136.20s | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |
| 2022-10-30 | MPSRA Fall Championship | Boys 2nd Varsity 4+ | boys | 2V | 1 | 17:30.0 | 21.30s | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |
| 2022-10-30 | MPSRA Fall Championship | Boys 2x | boys | UNKNOWN | 3 | 19:57.3 | 207.90s | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |
| 2022-10-30 | MPSRA Fall Championship | Boys 3rd Varsity 4+ | boys | 3V | 1 | 18:44.3 | 62.80s | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |
| 2022-10-30 | MPSRA Fall Championship | Girls 1st Novice 4+ | girls | 1st Novice | 1 | 20:25.3 | 42.90s | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |
| 2022-10-30 | MPSRA Fall Championship | Girls 1st Novice 8+ | girls | 1st Novice | 6 | 20:05.8 | 162.80s | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |
| 2022-10-30 | MPSRA Fall Championship | Girls 1st Varsity 4+ | girls | 1V | 1 | 17:44.8 | 101.50s | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |
| 2022-10-30 | MPSRA Fall Championship | Girls 1st Varsity 8+ | girls | 1V | 6 | 18:27.2 | 101.30s | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |
| 2022-10-30 | MPSRA Fall Championship | Girls 2nd Novice 8+ | girls | 2nd Novice | 1 | 19:29.4 | 11.60s | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |
| 2022-10-30 | MPSRA Fall Championship | Girls 2nd Varsity 4+ | girls | 2V | 1 | 22:17.8 |  | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |
| 2022-10-30 | MPSRA Fall Championship | Girls 2x | girls | UNKNOWN | 3 | 21:06.5 | 147.70s | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |
| 2022-10-30 | MPSRA Fall Championship | Girls 3rd Varsity 4+ | girls | 3V | 1 | 20:12.6 |  | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |
| 2022-10-30 | MPSRA Fall Championship | Girls 4th Varsity 4+ | girls | 4V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/21055/results) |

### 2021 (47 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2021-05-23 | Cambridge RLS vs. Duxbury | First Boat | boys | 1V | 2 | 4:40.4 | 16.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB6D9B45FEF29A1A98FA245AD50FE3BA) |
| 2021-05-23 | Cambridge RLS vs. Duxbury | Fourth Boat | girls | 4V | 2 | 5:43.6 | 36.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB6D9B45FEF29A1A98FA245AD50FE3BA) |
| 2021-05-23 | Cambridge RLS vs. Duxbury | Other | girls | UNKNOWN | 2 | 4:56.1 | 4.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB6D9B45FEF29A1A98FA245AD50FE3BA) |
| 2021-05-23 | Cambridge RLS vs. Duxbury | Other | girls | UNKNOWN | 2 | 5:15.1 | 6.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB6D9B45FEF29A1A98FA245AD50FE3BA) |
| 2021-05-23 | Cambridge RLS vs. Duxbury | Second Boat | boys | 2V | 2 | 4:54.2 | 16.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB6D9B45FEF29A1A98FA245AD50FE3BA) |
| 2021-05-23 | Cambridge RLS vs. Duxbury | Third Boat | boys | 3V | 3 | 5:05.4 | 35.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB6D9B45FEF29A1A98FA245AD50FE3BA) |
| 2021-05-23 | Cambridge RLS vs. Duxbury | Third Boat | girls | 3V | 2 | 5:37.0 | 18.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=BB6D9B45FEF29A1A98FA245AD50FE3BA) |
| 2021-09-18 | CRI Fall Classic | Mens Jr 2x | boys | UNKNOWN | 5 | 21:54.2 | 139.50s | [herenow](https://legacy.herenow.com/results/#/races/20918/results) |
| 2021-09-18 | CRI Fall Classic | Mens Jr 4x | boys | UNKNOWN | 2 | 21:34.7 | 127.90s | [herenow](https://legacy.herenow.com/results/#/races/20918/results) |
| 2021-09-18 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 6 | 20:48.0 | 72.10s | [herenow](https://legacy.herenow.com/results/#/races/20918/results) |
| 2021-09-18 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 11 | 22:54.4 | 198.50s | [herenow](https://legacy.herenow.com/results/#/races/20918/results) |
| 2021-09-18 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 18 | 23:50.2 | 254.30s | [herenow](https://legacy.herenow.com/results/#/races/20918/results) |
| 2021-09-18 | CRI Fall Classic | Womens Jr Varsity 4x+ | girls | 1V | 6 | 26:40.3 | 364.40s | [herenow](https://legacy.herenow.com/results/#/races/20918/results) |
| 2021-10-03 | Textile River Regatta | Mens Jr 2x | boys | UNKNOWN | 9 | 19:37.6 | 182.20s | [herenow](https://legacy.herenow.com/results/#/races/20934/results) |
| 2021-10-03 | Textile River Regatta | Mens Jr 4+ "A" | boys | UNKNOWN | 3 | 16:40.4 | 52.00s | [herenow](https://legacy.herenow.com/results/#/races/20934/results) |
| 2021-10-03 | Textile River Regatta | Mens Jr 8+ "A" | boys | UNKNOWN | 11 | 16:26.6 | 89.60s | [herenow](https://legacy.herenow.com/results/#/races/20934/results) |
| 2021-10-03 | Textile River Regatta | Mens Jr Ltwt 4+ | boys | UNKNOWN | 2 | 18:30.1 | 13.80s | [herenow](https://legacy.herenow.com/results/#/races/20934/results) |
| 2021-10-03 | Textile River Regatta | Womens Jr 4+ "A" | girls | UNKNOWN | 2 | 17:29.6 | 24.80s | [herenow](https://legacy.herenow.com/results/#/races/20934/results) |
| 2021-10-03 | Textile River Regatta | Womens Jr 4+ "B" | girls | UNKNOWN | 1 | 17:59.9 | 33.50s | [herenow](https://legacy.herenow.com/results/#/races/20934/results) |
| 2021-10-03 | Textile River Regatta | Womens Jr 4x | girls | UNKNOWN | 9 | 20:41.8 | 177.40s | [herenow](https://legacy.herenow.com/results/#/races/20934/results) |
| 2021-10-03 | Textile River Regatta | Womens Jr 8+ "A" | girls | UNKNOWN | 13 | 19:39.8 | 173.30s | [herenow](https://legacy.herenow.com/results/#/races/20934/results) |
| 2021-10-03 | Textile River Regatta | Womens Jr Ltwt 2x | girls | UNKNOWN | 3 | 22:56.0 | 283.00s | [herenow](https://legacy.herenow.com/results/#/races/20934/results) |
| 2021-10-03 | Textile River Regatta | Womens Jr Ltwt 4+ | girls | UNKNOWN | 2 | 19:29.8 | 23.90s | [herenow](https://legacy.herenow.com/results/#/races/20934/results) |
| 2021-10-09 | New England Jr/HS Championship | Mens Jr/HS 1st Varsity 4+ | boys | 1V | 8 | 16:28.5 | 69.90s | [herenow](https://legacy.herenow.com/results/#/races/20938/results) |
| 2021-10-09 | New England Jr/HS Championship | Mens Jr/HS 1st Varsity 8+ | boys | 1V | 1 | 15:26.7 | 22.70s | [herenow](https://legacy.herenow.com/results/#/races/20938/results) |
| 2021-10-09 | New England Jr/HS Championship | Mens Jr/HS 2nd Varsity 4+ | boys | 2V | 5 | 17:35.2 | 59.70s | [herenow](https://legacy.herenow.com/results/#/races/20938/results) |
| 2021-10-09 | New England Jr/HS Championship | Womens Jr/HS 1st Novice 4+ | girls | 1st Novice | 2 | 19:41.6 | 11.00s | [herenow](https://legacy.herenow.com/results/#/races/20938/results) |
| 2021-10-09 | New England Jr/HS Championship | Womens Jr/HS 1st Varsity 4+ | girls | 1V | 2 | 17:11.1 | 19.10s | [herenow](https://legacy.herenow.com/results/#/races/20938/results) |
| 2021-10-09 | New England Jr/HS Championship | Womens Jr/HS 2nd Varsity 4+ | girls | 2V | 1 | 17:58.9 | 27.50s | [herenow](https://legacy.herenow.com/results/#/races/20938/results) |
| 2021-10-09 | New England Jr/HS Championship | Womens Jr/HS 3rd/4th Varsity 4+ | girls | 4V | 1 | 20:01.5 | 71.50s | [herenow](https://legacy.herenow.com/results/#/races/20938/results) |
| 2021-10-09 | New England Jr/HS Championship | Womens Jr/HS 3rd/4th Varsity 4+ | girls | 4V | 3 | 22:48.9 | 167.40s | [herenow](https://legacy.herenow.com/results/#/races/20938/results) |
| 2021-10-16 | Head of the Kevin 3 | Men's Champ Single | boys | UNKNOWN | 18 | 17:53.9 | 191.40s | [herenow](https://legacy.herenow.com/results/#/races/20931/results) |
| 2021-10-16 | Head of the Kevin 3 | Men's Champ Single | boys | UNKNOWN | 46 | 18:59.0 | 256.50s | [herenow](https://legacy.herenow.com/results/#/races/20931/results) |
| 2021-10-17 | Head of the Quinobequin | Mens U17 1x | boys | UNKNOWN | 26 | 15:48.9 | 109.50s | [herenow](https://legacy.herenow.com/results/#/races/20947/results) |
| 2021-10-17 | Head of the Quinobequin | Mens U19 1x | boys | UNKNOWN | 35 | 16:12.7 | 188.20s | [herenow](https://legacy.herenow.com/results/#/races/20947/results) |
| 2021-10-17 | Head of the Quinobequin | Mens U19 1x | boys | UNKNOWN | 39 | 17:09.0 | 244.50s | [herenow](https://legacy.herenow.com/results/#/races/20947/results) |
| 2021-10-31 | MPSRA Fall Championship | Boys 1st Novice 4+ | boys | 1st Novice | 3 | 18:30.2 | 92.90s | [herenow](https://legacy.herenow.com/results/#/races/20942/results) |
| 2021-10-31 | MPSRA Fall Championship | Boys 1st Novice 8+ | boys | 1st Novice | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20942/results) |
| 2021-10-31 | MPSRA Fall Championship | Boys 2nd Novice 8+ | boys | 2nd Novice | 5 | 19:31.9 | 321.30s | [herenow](https://legacy.herenow.com/results/#/races/20942/results) |
| 2021-10-31 | MPSRA Fall Championship | Girls 1st Novice 4+ | girls | 1st Novice | 4 | 28:40.9 | 647.70s | [herenow](https://legacy.herenow.com/results/#/races/20942/results) |
| 2021-10-31 | MPSRA Fall Championship | Girls 1st Novice 4+ | girls | 1st Novice | 5 | 28:42.9 | 649.70s | [herenow](https://legacy.herenow.com/results/#/races/20942/results) |
| 2021-10-31 | MPSRA Fall Championship | Girls 1st Novice 8+ | girls | 1st Novice | 6 | 21:11.3 | 265.30s | [herenow](https://legacy.herenow.com/results/#/races/20942/results) |
| 2021-10-31 | MPSRA Fall Championship | Girls 1st Varsity 4+ | girls | 1V | 1 | 13:10.1 | 127.30s | [herenow](https://legacy.herenow.com/results/#/races/20942/results) |
| 2021-10-31 | MPSRA Fall Championship | Girls 1st Varsity 8+ | girls | 1V | 8 | 15:50.7 | 232.60s | [herenow](https://legacy.herenow.com/results/#/races/20942/results) |
| 2021-10-31 | MPSRA Fall Championship | Girls 2nd Varsity 4+ | girls | 2V | 1 | 13:36.2 |  | [herenow](https://legacy.herenow.com/results/#/races/20942/results) |
| 2021-10-31 | MPSRA Fall Championship | Girls 3rd Varsity 4+ | girls | 3V | 1 | 15:00.6 |  | [herenow](https://legacy.herenow.com/results/#/races/20942/results) |
| 2021-10-31 | MPSRA Fall Championship | Girls 4x | girls | UNKNOWN | 4 | 21:37.1 | 248.10s | [herenow](https://legacy.herenow.com/results/#/races/20942/results) |

### 2019 (102 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2019-04-06 | Mayor's Cup: BB&N vs. CRLS | First Boat | boys | 1V | 2 | 4:28.67 | 2.03s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=87111F9FB1630E1B9D6783EA26C0E3DD) |
| 2019-04-06 | Mayor's Cup: BB&N vs. CRLS | First Boat | girls | 1V | 1 | 4:58.4 | 0.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CB8DA6D886642993CC1A6FF710FA8EFC) |
| 2019-04-06 | Mayor's Cup: BB&N vs. CRLS | Fourth Boat | boys | 4V | 3 | 5:04.42 | 16.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=87111F9FB1630E1B9D6783EA26C0E3DD) |
| 2019-04-06 | Mayor's Cup: BB&N vs. CRLS | Fourth Boat | girls | 4V | 1 | 5:35.1 | 9.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CB8DA6D886642993CC1A6FF710FA8EFC) |
| 2019-04-06 | Mayor's Cup: BB&N vs. CRLS | Second Boat | boys | 2V | 2 | 4:46.9 | 2.74s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=87111F9FB1630E1B9D6783EA26C0E3DD) |
| 2019-04-06 | Mayor's Cup: BB&N vs. CRLS | Second Boat | girls | 2V | 1 | 5:06.8 | 8.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CB8DA6D886642993CC1A6FF710FA8EFC) |
| 2019-04-06 | Mayor's Cup: BB&N vs. CRLS | Third Boat | girls | 3V | 2 | 5:58.0 | 30.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=CB8DA6D886642993CC1A6FF710FA8EFC) |
| 2019-04-13 | Belmont Hill, CRLS, Dexter | First Boat | boys | 1V | 3 | 4:43.1 | 24.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=D5868B93E171FF9A8AEAAEC8983B6712) |
| 2019-04-13 | Belmont Hill, CRLS, Dexter | Second Boat | boys | 2V | 2 | 4:38.2 | 18.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=D5868B93E171FF9A8AEAAEC8983B6712) |
| 2019-04-13 | Belmont Hill, CRLS, Dexter | Third Boat | boys | 3V | 2 | 5:05.6 | 31.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=D5868B93E171FF9A8AEAAEC8983B6712) |
| 2019-04-13 | CRLS vs. Dexter Southfield | First Boat | girls | 1V | 1 | 5:09.7 | 13.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9A0AC2DA4115A9FA896661C30B9E832B) |
| 2019-04-13 | CRLS vs. Dexter Southfield | Second Boat | girls | 2V | 1 | 5:12.8 | 40.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9A0AC2DA4115A9FA896661C30B9E832B) |
| 2019-04-13 | CRLS vs. Dexter Southfield | Third Boat | girls | 3V | 2 | 6:12.3 | 11.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9A0AC2DA4115A9FA896661C30B9E832B) |
| 2019-04-28 | Hopkins vs CRLS, Derryfield | Fifth Boat | boys | Novice | 1 | 5:16.8 | 10.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73BAAD5D11B6B8F42C9DB3795CAA80BB) |
| 2019-04-28 | Hopkins vs CRLS, Derryfield | First Boat | boys | 1V | 2 | 4:57.8 | 8.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73BAAD5D11B6B8F42C9DB3795CAA80BB) |
| 2019-04-28 | Hopkins vs CRLS, Derryfield | Other | girls | UNKNOWN | 1 | 5:27.4 | 18.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73BAAD5D11B6B8F42C9DB3795CAA80BB) |
| 2019-04-28 | Hopkins vs CRLS, Derryfield | Other | girls | UNKNOWN | 1 | 5:36 | 28.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73BAAD5D11B6B8F42C9DB3795CAA80BB) |
| 2019-04-28 | Hopkins vs CRLS, Derryfield | Other | girls | UNKNOWN | 2 | 6:04.6 | 28.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73BAAD5D11B6B8F42C9DB3795CAA80BB) |
| 2019-04-28 | Hopkins vs CRLS, Derryfield | Second Boat | boys | 2V | 3 | 5:13.5 | 9.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73BAAD5D11B6B8F42C9DB3795CAA80BB) |
| 2019-04-28 | Hopkins vs CRLS, Derryfield | Third Boat | girls | Novice | 1 | 5:55.9 | 10.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=73BAAD5D11B6B8F42C9DB3795CAA80BB) |
| 2019-05-11 | CRLS vs. Duxbury, Northfield Mt. Hermon | Fifth Boat | boys | Novice | 1 | 4:53.43 | 4.84s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DD851F5EAB761D11D14BCDF9759AFAB1) |
| 2019-05-11 | CRLS vs. Duxbury, Northfield Mt. Hermon | First Boat | boys | 1V | 2 | 4:12.19 | 2.24s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DD851F5EAB761D11D14BCDF9759AFAB1) |
| 2019-05-11 | CRLS vs. Duxbury, Northfield Mt. Hermon | Fourth Boat | girls | Novice | 2 | 4:57.7 | 6.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DD851F5EAB761D11D14BCDF9759AFAB1) |
| 2019-05-11 | CRLS vs. Duxbury, Northfield Mt. Hermon | Other | girls | UNKNOWN | 2 | 4:38.7 | 5.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DD851F5EAB761D11D14BCDF9759AFAB1) |
| 2019-05-11 | CRLS vs. Duxbury, Northfield Mt. Hermon | Other | girls | UNKNOWN | 1 | 4:47.9 | 15.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DD851F5EAB761D11D14BCDF9759AFAB1) |
| 2019-05-11 | CRLS vs. Duxbury, Northfield Mt. Hermon | Second Boat | boys | 2V | 2 | 4:33.42 | 8.88s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DD851F5EAB761D11D14BCDF9759AFAB1) |
| 2019-05-18 | Northeast Youth Championship | Mens Youth 2- Final | boys | 1V | 6 | 7:16.8 | 24.40s | [herenow](https://legacy.herenow.com/results/#/races/20595/results) |
| 2019-05-18 | Northeast Youth Championship | Mens Youth 2- Time Trial | boys | 1V | 5 | 6:36.4 | 11.70s | [herenow](https://legacy.herenow.com/results/#/races/20595/results) |
| 2019-05-18 | Northeast Youth Championship | Womens Youth 2nd 4+ Final | girls | 2V | 4 | 7:27.6 | 17.50s | [herenow](https://legacy.herenow.com/results/#/races/20595/results) |
| 2019-05-18 | Northeast Youth Championship | Womens Youth 2nd 4+ Heat 2 | girls | 2V | 2 | 7:20.4 | 3.30s | [herenow](https://legacy.herenow.com/results/#/races/20595/results) |
| 2019-05-18 | Northeast Youth Championship | Womens Youth 4+ Semi 1 | girls | 1V | 4 | 7:21.9 | 25.40s | [herenow](https://legacy.herenow.com/results/#/races/20595/results) |
| 2019-05-18 | Northeast Youth Championship | Womens Youth 4+ Time Trial | girls | 1V | 8 | 6:43.7 | 19.80s | [herenow](https://legacy.herenow.com/results/#/races/20595/results) |
| 2019-05-25 | NEIRA Championship 2019 | boys 2V 4+ - Heat 2 | boys | 2V | 6 | 5:36.970 | 37.01s | [neira-championship-pdf](https://www.row2k.com/results/files/20190525NEIRA.pdf) |
| 2019-05-25 | NEIRA Championship 2019 | boys 3V 4+ - Grand Final | boys | 3V | 6 | 5:36.970 | 12.93s | [neira-championship-pdf](https://www.row2k.com/results/files/20190525NEIRA.pdf) |
| 2019-05-25 | NEIRA Championship 2019 | girls 1V 4+ - Heat 3 | girls | 1V | 4 | 5:53.089 | 4.68s | [neira-championship-pdf](https://www.row2k.com/results/files/20190525NEIRA.pdf) |
| 2019-05-25 | NEIRA Championship 2019 | girls 1V 4+ - Petite Final | girls | 1V | 3 | 6:24.809 | 0.54s | [neira-championship-pdf](https://www.row2k.com/results/files/20190525NEIRA.pdf) |
| 2019-05-25 | NEIRA Championship 2019 | girls 2V 4+ - Heat 1 | girls | 2V | 4 | 5:47.899 | 6.04s | [neira-championship-pdf](https://www.row2k.com/results/files/20190525NEIRA.pdf) |
| 2019-05-25 | NEIRA Championship 2019 | girls 2V 4+ - Petite Final | girls | 2V | 3 | 6:40.178 | 12.67s | [neira-championship-pdf](https://www.row2k.com/results/files/20190525NEIRA.pdf) |
| 2019-05-25 | NEIRA Championship 2019 | girls 4V 4+ - Heat 2 | girls | 4V | 6 | 6:13.576 | 12.58s | [neira-championship-pdf](https://www.row2k.com/results/files/20190525NEIRA.pdf) |
| 2019-05-26 | MPSRA Spring Championship | Boys 1st Novice 4+ Final A | boys | 1st Novice | 1 | 5:04.5 | 4.80s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Boys 1st Novice 4+ Time Trial | boys | 1st Novice | 1 | 5:02.7 | 7.90s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Boys 1st Novice 8+ Final B | boys | 1st Novice | 2 | 5:04.2 | 3.30s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Boys 1st Novice 8+ Time Trial | boys | 1st Novice | 7 | 5:13.0 | 28.50s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Boys 1st Varsity 4+ Final A CANCELLED | boys | 1V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Boys 1st Varsity 4+ Time Trial | boys | 1V | 5 | 4:59.7 | 7.00s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Boys 1x Flight 1 | boys | UNKNOWN | 4 | 5:55.8 | 37.30s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Boys 2x Flight 1 | boys | UNKNOWN | 3 | 5:19.1 | 28.80s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Boys 2x Flight 2 | boys | UNKNOWN | 2 | 6:09.1 | 32.60s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Girls 1st Novice 4+ Final A | girls | 1st Novice | 1 | 5:35.3 | 17.60s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Girls 1st Novice 4+ Time Trial | girls | 1st Novice | 1 | 5:33.1 | 22.10s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Girls 1st Novice 8+ Final B | girls | 1st Novice | 2 | 5:58.0 | 21.70s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Girls 1st Novice 8+ Time Trial | girls | 1st Novice | 8 | 6:09.0 | 58.70s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Girls 1st Varsity 4+ Final A CANCELLED | girls | 1V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Girls 1st Varsity 4+ Time Trial | girls | 1V | 1 | 5:12.1 | 4.60s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Final A | girls | 2V | 1 | 5:18.0 | 12.20s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Time Trial | girls | 2V | 1 | 5:22.5 | 11.00s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Girls 3rd Varsity 4+ Final A | girls | 3V | 2 | 5:42.5 | 7.40s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-05-26 | MPSRA Spring Championship | Girls 4th Varsity 4+ Final A | girls | 4V | 1 | 6:09.0 | 33.80s | [herenow](https://legacy.herenow.com/results/#/races/20678/results) |
| 2019-09-21 | CRI Fall Classic | Mens Jr 2x | boys | UNKNOWN | 3 | 20:43.4 | 52.40s | [herenow](https://legacy.herenow.com/results/#/races/20717/results) |
| 2019-09-21 | CRI Fall Classic | Mens Jr 2x | boys | UNKNOWN | 5 | 22:56.1 | 185.10s | [herenow](https://legacy.herenow.com/results/#/races/20717/results) |
| 2019-09-21 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | 15 | 21:26.2 | 168.60s | [herenow](https://legacy.herenow.com/results/#/races/20717/results) |
| 2019-09-21 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | 16 | 21:28.1 | 170.50s | [herenow](https://legacy.herenow.com/results/#/races/20717/results) |
| 2019-09-21 | CRI Fall Classic | Womens Jr 2x | girls | UNKNOWN | 2 | 23:14.3 | 1.30s | [herenow](https://legacy.herenow.com/results/#/races/20717/results) |
| 2019-09-21 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 9 | 21:22.5 | 99.10s | [herenow](https://legacy.herenow.com/results/#/races/20717/results) |
| 2019-09-21 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 22 | 22:53.9 | 190.50s | [herenow](https://legacy.herenow.com/results/#/races/20717/results) |
| 2019-09-21 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20717/results) |
| 2019-10-06 | Textile River Regatta | Mens Jr 1x | boys | UNKNOWN | 10 | 22:17.5 | 223.00s | [herenow](https://legacy.herenow.com/results/#/races/20687/results) |
| 2019-10-06 | Textile River Regatta | Mens Jr 4+ | boys | UNKNOWN | 14 | 17:52.2 | 69.30s | [herenow](https://legacy.herenow.com/results/#/races/20687/results) |
| 2019-10-06 | Textile River Regatta | Mens Jr 4+ | boys | UNKNOWN | 24 | 18:56.8 | 133.90s | [herenow](https://legacy.herenow.com/results/#/races/20687/results) |
| 2019-10-06 | Textile River Regatta | Mens Jr 4+ | boys | UNKNOWN | 30 | 19:30.4 | 167.50s | [herenow](https://legacy.herenow.com/results/#/races/20687/results) |
| 2019-10-06 | Textile River Regatta | Mens Jr Novice 8+ | boys | Novice | 10 | 19:16.9 | 133.30s | [herenow](https://legacy.herenow.com/results/#/races/20687/results) |
| 2019-10-06 | Textile River Regatta | Womens Jr 4+ | girls | UNKNOWN | 1 | 18:31.4 | 6.60s | [herenow](https://legacy.herenow.com/results/#/races/20687/results) |
| 2019-10-06 | Textile River Regatta | Womens Jr 4+ | girls | UNKNOWN | 5 | 19:05.0 | 33.60s | [herenow](https://legacy.herenow.com/results/#/races/20687/results) |
| 2019-10-06 | Textile River Regatta | Womens Jr 4+ | girls | UNKNOWN | 26 | 21:24.4 | 173.00s | [herenow](https://legacy.herenow.com/results/#/races/20687/results) |
| 2019-10-06 | Textile River Regatta | Womens Jr 8+ "A" | girls | UNKNOWN | 16 | 19:23.5 | 139.00s | [herenow](https://legacy.herenow.com/results/#/races/20687/results) |
| 2019-10-06 | Textile River Regatta | Womens Jr Novice 8+ | girls | Novice | 13 | 20:35.4 | 174.40s | [herenow](https://legacy.herenow.com/results/#/races/20687/results) |
| 2019-10-13 | Head of the Quinobequin | Mens U19 1x | boys | UNKNOWN | 23 | 15:16.3 | 144.20s | [herenow](https://legacy.herenow.com/results/#/races/20703/results) |
| 2019-10-13 | New England Jr/HS Championship | Mens 1st Varsity 4+ | boys | 1V | 8 | 16:23.0 | 90.10s | [herenow](https://legacy.herenow.com/results/#/races/20704/results) |
| 2019-10-13 | New England Jr/HS Championship | Mens 2nd Varsity 4+ | boys | 2V | 5 | 17:04.7 | 47.20s | [herenow](https://legacy.herenow.com/results/#/races/20704/results) |
| 2019-10-13 | New England Jr/HS Championship | Mens 3rd/4th Varsity 4+ | boys | 4V | 1 | 17:20.8 | 7.00s | [herenow](https://legacy.herenow.com/results/#/races/20704/results) |
| 2019-10-13 | New England Jr/HS Championship | Mens Jr/HS 1st Novice 8+ | boys | 1st Novice | 11 | 14:09.3 | 111.30s | [herenow](https://legacy.herenow.com/results/#/races/20704/results) |
| 2019-10-13 | New England Jr/HS Championship | Womens 1st Varsity 4+ | girls | 1V | 3 | 16:55.4 | 19.40s | [herenow](https://legacy.herenow.com/results/#/races/20704/results) |
| 2019-10-13 | New England Jr/HS Championship | Womens 1st Varsity 8+ | girls | 1V | 6 | 16:04.3 | 132.10s | [herenow](https://legacy.herenow.com/results/#/races/20704/results) |
| 2019-10-13 | New England Jr/HS Championship | Womens Jr/HS 1st Novice 4+ | girls | 1st Novice | UNKNOWN | 16:27.0 |  | [herenow](https://legacy.herenow.com/results/#/races/20704/results) |
| 2019-10-13 | New England Jr/HS Championship | Womens Jr/HS 1st Novice 8+ | girls | 1st Novice | 13 | 15:35.9 | 152.80s | [herenow](https://legacy.herenow.com/results/#/races/20704/results) |
| 2019-10-13 | New England Jr/HS Championship | Womens Jr/HS 2nd Novice 8+ | girls | 2nd Novice | 5 | 16:31.5 | 126.10s | [herenow](https://legacy.herenow.com/results/#/races/20704/results) |
| 2019-10-27 | MPSRA Fall Championship | Boys 1st Novice 8+ | boys | 1st Novice | 9 | 17:43.5 | 126.80s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Boys 1st Varsity 4+ | boys | 1V | 4 | 18:03.5 | 97.40s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Boys 1x | boys | UNKNOWN | 7 | 20:08.9 | 149.90s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Boys 2- | boys | UNKNOWN | 1 | 17:43.6 | 23.30s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Boys 2nd Varsity 4+ | boys | 2V | 2 | 17:28.9 | 48.70s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Boys 2x | boys | UNKNOWN | 6 | 18:53.3 | 157.80s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Boys 2x | boys | UNKNOWN | 8 | 20:19.9 | 244.40s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Boys 3rd Varsity 4+ | boys | 3V | 2 | 19:30.8 | 105.50s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Boys 4th Varsity 4+ | boys | 4V | UNKNOWN | 19:11.0 |  | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Girls 1st Novice 4+ | girls | 1st Novice | 2 | 19:31.9 | 15.90s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Girls 1st Novice 8+ | girls | 1st Novice | 7 | 19:29.4 | 55.60s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Girls 1st Varsity 4+ | girls | 1V | 2 | 17:50.6 | 5.00s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Girls 2nd Novice 8+ | girls | 2nd Novice | 2 | 21:13.5 | 6.60s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Girls 2nd Varsity 4+ | girls | 2V | 1 | 18:30.5 | 51.90s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Girls 3rd Varsity 4+ | girls | 3V | 2 | 19:56.3 | 30.90s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |
| 2019-10-27 | MPSRA Fall Championship | Girls 4th Varsity 4+ | girls | 4V | 2 | 22:01.8 | 90.70s | [herenow](https://legacy.herenow.com/results/#/races/20689/results) |

### 2018 (96 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2018-04-07 | Milton (Cambridge Mayor's Cup) | First Boat | boys | 1V | 2 | 4:24.58 | 2.27s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C80B53596B21925E2BDC210948E3CBAC) |
| 2018-04-07 | Milton (Cambridge Mayor's Cup) | Other | girls | UNKNOWN | 2 | 5:14.57 | 8.19s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C80B53596B21925E2BDC210948E3CBAC) |
| 2018-04-07 | Milton (Cambridge Mayor's Cup) | Other | girls | UNKNOWN | 1 | 5:01.11 | 12.88s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C80B53596B21925E2BDC210948E3CBAC) |
| 2018-04-07 | Milton (Cambridge Mayor's Cup) | Second Boat | boys | 2V | 1 | 4:38.23 | 2.34s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C80B53596B21925E2BDC210948E3CBAC) |
| 2018-04-07 | Milton (Cambridge Mayor's Cup) | Third Boat | boys | 3V | 2 | 4:54.35 | 12.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C80B53596B21925E2BDC210948E3CBAC) |
| 2018-04-14 | Cambridge Rindge and Latin vs. Dexter Southf | First Boat | girls | 1V | 2 | 5:13.51 | 5.98s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=EF4D2982E21A089ED170F8C6704B6CE3) |
| 2018-04-14 | Cambridge Rindge and Latin vs. Dexter Southf | Second Boat | girls | 2V | 1 | 5:20.42 | 6.23s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=EF4D2982E21A089ED170F8C6704B6CE3) |
| 2018-04-25 | Belmont Hill vs Middlesex, CRLS | First Boat | boys | 1V | 2 | 4:26.1 | 19.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=E96D75B62AC0DCD49DE898BB020B5AAA) |
| 2018-04-25 | Belmont Hill vs Middlesex, CRLS | Second Boat | boys | 2V | 2 | 4:28.8 | 9.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=E96D75B62AC0DCD49DE898BB020B5AAA) |
| 2018-04-25 | Belmont Hill vs Middlesex, CRLS | Third Boat | boys | 3V | 2 | 4:46.4 | 22.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=E96D75B62AC0DCD49DE898BB020B5AAA) |
| 2018-04-29 | Hopkins vs CRLS, Derryfield, King | First Boat | UNKNOWN | 1V | 1 | 5:34 | 4.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DCD4EC62817F7854CB4633906A7A6D64) |
| 2018-04-29 | Hopkins vs CRLS, Derryfield, King | Other | UNKNOWN | UNKNOWN | 1 | 5:23 | 1.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DCD4EC62817F7854CB4633906A7A6D64) |
| 2018-04-29 | Hopkins vs CRLS, Derryfield, King | Other | UNKNOWN | UNKNOWN | 1 | 5:44 | 2.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DCD4EC62817F7854CB4633906A7A6D64) |
| 2018-04-29 | Hopkins vs CRLS, Derryfield, King | Second Boat | UNKNOWN | 2V | 1 | 5:36 | 12.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DCD4EC62817F7854CB4633906A7A6D64) |
| 2018-04-29 | Hopkins vs CRLS, Derryfield, King | Third Boat | UNKNOWN | 3V | 1 | 5:36 | 9.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DCD4EC62817F7854CB4633906A7A6D64) |
| 2018-04-29 | Hopkins vs CRLS, Derryfield, King | Third Boat | UNKNOWN | 3V | 3 | 6:32 | 37.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=DCD4EC62817F7854CB4633906A7A6D64) |
| 2018-05-19 | CRLS vs Duxbury | First Boat | boys | 1V | 2 | 4:27.9 | 2.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3E4BF286382FDA124416E9609F6CF2C8) |
| 2018-05-19 | CRLS vs Duxbury | Fourth Boat | boys | Novice | 2 | 4:42 | 8.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3E4BF286382FDA124416E9609F6CF2C8) |
| 2018-05-19 | CRLS vs Duxbury | Other | girls | 2V | 3 | 5:09.5 | 9.31s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3E4BF286382FDA124416E9609F6CF2C8) |
| 2018-05-19 | CRLS vs Duxbury | Other | girls | UNKNOWN | 1 | 4:56.75 | 2.87s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3E4BF286382FDA124416E9609F6CF2C8) |
| 2018-05-19 | CRLS vs Duxbury | Second Boat | boys | 2V | 2 | 4:41.8 | 7.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3E4BF286382FDA124416E9609F6CF2C8) |
| 2018-05-19 | CRLS vs Duxbury | Third Boat | boys | 3V | 3 | 5:02 | 18.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3E4BF286382FDA124416E9609F6CF2C8) |
| 2018-05-19 | CRLS vs Duxbury | Third Boat | girls | Novice | 2 | 5:29.0 | 37.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3E4BF286382FDA124416E9609F6CF2C8) |
| 2018-05-19 | Northeast Youth Championship | Mens Youth Ltwt 4+ Final A | boys | 1V | 3 | 7:39.4 | 21.80s | [herenow](https://legacy.herenow.com/results/#/races/20502/results) |
| 2018-05-19 | Northeast Youth Championship | Mens Youth Ltwt 4+ Time Trial 1 | boys | 1V | 1 | 6:57.3 | 1.30s | [herenow](https://legacy.herenow.com/results/#/races/20502/results) |
| 2018-05-26 | NEIRA Championship 2018 | boys 1V 4+ - Heat 3 | boys | 1V | 5 | 5:12.909 | 15.22s | [neira-championship-pdf](https://neirarowing.org/documents/2018NEIRAResults.pdf) |
| 2018-05-26 | NEIRA Championship 2018 | boys 2V 4+ - Heat 1 | boys | 2V | 4 | 5:33.502 | 17.18s | [neira-championship-pdf](https://neirarowing.org/documents/2018NEIRAResults.pdf) |
| 2018-05-26 | NEIRA Championship 2018 | girls 1V 4+ - Heat 3 | girls | 1V | 5 | 5:50.413 | 14.08s | [neira-championship-pdf](https://neirarowing.org/documents/2018NEIRAResults.pdf) |
| 2018-05-26 | NEIRA Championship 2018 | girls 2V 4+ - Heat 1 | girls | 2V | 5 | 6:15.183 | 22.91s | [neira-championship-pdf](https://neirarowing.org/documents/2018NEIRAResults.pdf) |
| 2018-05-27 | MPSRA Spring Championship | Boys 1st Novice 8+ B Final | boys | 1st Novice | 1 | 4:07.3 | 6.90s | [herenow](https://legacy.herenow.com/results/#/races/20503/results) |
| 2018-05-27 | MPSRA Spring Championship | Boys 1st Novice 8+ Time Trial | boys | 1st Novice | 9 | 6:19.0 | 51.10s | [herenow](https://legacy.herenow.com/results/#/races/20503/results) |
| 2018-05-27 | MPSRA Spring Championship | Boys 1st Varsity 4+ A Final | boys | 1V | 5 | 3:51.9 | 8.90s | [herenow](https://legacy.herenow.com/results/#/races/20503/results) |
| 2018-05-27 | MPSRA Spring Championship | Boys 1st Varsity 4+ Time Trial | boys | 1V | 3 | 5:38.9 | 9.60s | [herenow](https://legacy.herenow.com/results/#/races/20503/results) |
| 2018-05-27 | MPSRA Spring Championship | Boys 2nd Varsity 4+ A Final | boys | 2V | 1 | 3:51.1 | 5.40s | [herenow](https://legacy.herenow.com/results/#/races/20503/results) |
| 2018-05-27 | MPSRA Spring Championship | Boys 2nd Varsity 4+ Time Trial | boys | 2V | 1 | 5:35.3 | 0.80s | [herenow](https://legacy.herenow.com/results/#/races/20503/results) |
| 2018-05-27 | MPSRA Spring Championship | Boys 3rd Varsity 4+ A Final | boys | 3V | 3 | 4:02.2 | 4.80s | [herenow](https://legacy.herenow.com/results/#/races/20503/results) |
| 2018-05-27 | MPSRA Spring Championship | Boys 4th Varsity 4+ A Final | boys | 4V | 4 | 4:42.3 | 35.70s | [herenow](https://legacy.herenow.com/results/#/races/20503/results) |
| 2018-05-27 | MPSRA Spring Championship | Girls 1st Varsity 4+ A Final | girls | 1V | 2 | 4:10.2 | 1.70s | [herenow](https://legacy.herenow.com/results/#/races/20503/results) |
| 2018-05-27 | MPSRA Spring Championship | Girls 1st Varsity 4+ Time Trial | girls | 1V | 1 | 6:09.4 | 0.90s | [herenow](https://legacy.herenow.com/results/#/races/20503/results) |
| 2018-05-27 | MPSRA Spring Championship | Girls 2nd Varsity 4+ A Final | girls | 2V | 2 | 4:26.9 | 5.20s | [herenow](https://legacy.herenow.com/results/#/races/20503/results) |
| 2018-05-27 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Time Trial | girls | 2V | 1 | 6:36.4 | 5.40s | [herenow](https://legacy.herenow.com/results/#/races/20503/results) |
| 2018-05-27 | MPSRA Spring Championship | Girls Novice 4+ A Final | girls | Novice | 4 | 5:09.3 | 24.30s | [herenow](https://legacy.herenow.com/results/#/races/20503/results) |
| 2018-06-08 | Youth National Championship | Mens Ltwt Youth 4+ Final C | boys | 1V | 4 | 7:26.8 | 4.90s | [herenow](https://legacy.herenow.com/results/#/races/20504/results) |
| 2018-06-08 | Youth National Championship | Mens Ltwt Youth 4+ Repechage 2 | boys | 1V | 4 | 7:10.7 | 7.70s | [herenow](https://legacy.herenow.com/results/#/races/20504/results) |
| 2018-06-08 | Youth National Championship | Mens Ltwt Youth 4+ Time Trial 1 | boys | 1V | 18 | 6:53.4 | 24.50s | [herenow](https://legacy.herenow.com/results/#/races/20504/results) |
| 2018-09-15 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | 8 | 22:03.3 | 141.10s | [herenow](https://legacy.herenow.com/results/#/races/20556/results) |
| 2018-09-15 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | UNKNOWN | 20:37.0 |  | [herenow](https://legacy.herenow.com/results/#/races/20556/results) |
| 2018-09-15 | CRI Fall Classic | Mens Jr 8+ | boys | UNKNOWN | 10 | 20:48.8 | 229.90s | [herenow](https://legacy.herenow.com/results/#/races/20556/results) |
| 2018-09-15 | CRI Fall Classic | Womens Jr 1x | girls | UNKNOWN | 2 | 26:20.7 | 135.90s | [herenow](https://legacy.herenow.com/results/#/races/20556/results) |
| 2018-09-15 | CRI Fall Classic | Womens Jr 2x | girls | UNKNOWN | 8 | 26:40.2 | 269.70s | [herenow](https://legacy.herenow.com/results/#/races/20556/results) |
| 2018-09-15 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 12 | 23:54.0 | 164.80s | [herenow](https://legacy.herenow.com/results/#/races/20556/results) |
| 2018-09-15 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 16 | 25:22.3 | 253.10s | [herenow](https://legacy.herenow.com/results/#/races/20556/results) |
| 2018-09-15 | CRI Fall Classic | Womens Jr 4x | girls | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20556/results) |
| 2018-09-30 | Textile River Regatta | Mens Jr 4+ | boys | UNKNOWN | 2 | 15:42.0 | 19.20s | [herenow](https://legacy.herenow.com/results/#/races/20547/results) |
| 2018-09-30 | Textile River Regatta | Mens Jr 4+ | boys | UNKNOWN | 23 | 16:56.6 | 93.80s | [herenow](https://legacy.herenow.com/results/#/races/20547/results) |
| 2018-09-30 | Textile River Regatta | Mens Jr 4+ | boys | UNKNOWN | 32 | 17:26.3 | 123.50s | [herenow](https://legacy.herenow.com/results/#/races/20547/results) |
| 2018-09-30 | Textile River Regatta | Mens Jr 4+ | boys | UNKNOWN | 42 | 18:17.9 | 175.10s | [herenow](https://legacy.herenow.com/results/#/races/20547/results) |
| 2018-09-30 | Textile River Regatta | Mens Jr Novice 2x | boys | Novice | 3 | 19:04.2 | 33.10s | [herenow](https://legacy.herenow.com/results/#/races/20547/results) |
| 2018-09-30 | Textile River Regatta | Womens Jr 4+ | girls | UNKNOWN | 4 | 17:09.5 | 29.20s | [herenow](https://legacy.herenow.com/results/#/races/20547/results) |
| 2018-09-30 | Textile River Regatta | Womens Jr 4+ | girls | UNKNOWN | 38 | 20:03.6 | 203.30s | [herenow](https://legacy.herenow.com/results/#/races/20547/results) |
| 2018-09-30 | Textile River Regatta | Womens Jr 4x | girls | UNKNOWN | 5 | 17:31.2 | 74.80s | [herenow](https://legacy.herenow.com/results/#/races/20547/results) |
| 2018-10-07 | New England Jr/HS Championship | Mens 1st Varsity 4+ | boys | 1V | 3 | 15:16.5 | 37.40s | [herenow](https://legacy.herenow.com/results/#/races/20526/results) |
| 2018-10-07 | New England Jr/HS Championship | Mens 2nd Varsity 4+ | boys | 2V | 5 | 16:18.2 | 65.60s | [herenow](https://legacy.herenow.com/results/#/races/20526/results) |
| 2018-10-07 | New England Jr/HS Championship | Mens 3rd/4th Varsity 4+ | boys | 4V | 2 | 17:27.0 | 39.40s | [herenow](https://legacy.herenow.com/results/#/races/20526/results) |
| 2018-10-07 | New England Jr/HS Championship | Mens 3rd/4th Varsity 4+ | boys | 4V | 4 | 17:46.7 | 59.10s | [herenow](https://legacy.herenow.com/results/#/races/20526/results) |
| 2018-10-07 | New England Jr/HS Championship | Mens Jr/HS 1st Novice 8+ | boys | 1st Novice | 8 | 12:39.3 | 77.50s | [herenow](https://legacy.herenow.com/results/#/races/20526/results) |
| 2018-10-07 | New England Jr/HS Championship | Womens 1st Varsity 4+ | girls | 1V | 4 | 17:04.4 | 28.00s | [herenow](https://legacy.herenow.com/results/#/races/20526/results) |
| 2018-10-07 | New England Jr/HS Championship | Womens 2nd Varsity 4+ | girls | 2V | 10 | 21:25.3 | 190.20s | [herenow](https://legacy.herenow.com/results/#/races/20526/results) |
| 2018-10-07 | New England Jr/HS Championship | Womens Jr/HS 1st Novice 8+ | girls | 1st Novice | 15 | 14:48.7 | 152.90s | [herenow](https://legacy.herenow.com/results/#/races/20526/results) |
| 2018-10-07 | New England Jr/HS Championship | Womens Jr/HS 2nd Novice 8+ | girls | 2nd Novice | 3 | 14:36.8 | 121.60s | [herenow](https://legacy.herenow.com/results/#/races/20526/results) |
| 2018-10-07 | New England Jr/HS Championship | Womens Jr/HS Varsity & Novice 2x | girls | Novice | 4 | 13:43.1 | 45.80s | [herenow](https://legacy.herenow.com/results/#/races/20526/results) |
| 2018-10-07 | New England Jr/HS Championship | Womens Jr/HS Varsity & Novice 2x | girls | Novice | 6 | 13:56.8 | 59.50s | [herenow](https://legacy.herenow.com/results/#/races/20526/results) |
| 2018-10-14 | Head of the Quinobequin | Mens U17 1x | boys | UNKNOWN | 22 | 16:56.8 | 200.00s | [herenow](https://legacy.herenow.com/results/#/races/20555/results) |
| 2018-10-14 | Head of the Quinobequin | Mens U17 1x | boys | UNKNOWN | 23 | 17:02.7 | 205.90s | [herenow](https://legacy.herenow.com/results/#/races/20555/results) |
| 2018-10-14 | Head of the Quinobequin | Mens U19 1x | boys | UNKNOWN | 28 | 16:48.4 | 210.30s | [herenow](https://legacy.herenow.com/results/#/races/20555/results) |
| 2018-10-14 | Head of the Quinobequin | Mens U19 1x | boys | UNKNOWN | 30 | 18:55.5 | 337.40s | [herenow](https://legacy.herenow.com/results/#/races/20555/results) |
| 2018-10-14 | Head of the Quinobequin | Womens U17 1x | girls | UNKNOWN | 5 | 16:26.2 | 83.60s | [herenow](https://legacy.herenow.com/results/#/races/20555/results) |
| 2018-10-14 | Head of the Quinobequin | Womens U17 1x | girls | UNKNOWN | 18 | 17:11.1 | 128.50s | [herenow](https://legacy.herenow.com/results/#/races/20555/results) |
| 2018-10-14 | Head of the Quinobequin | Womens U17 1x | girls | UNKNOWN | 21 | 17:46.8 | 164.20s | [herenow](https://legacy.herenow.com/results/#/races/20555/results) |
| 2018-10-14 | Head of the Quinobequin | Womens U19 1x | girls | UNKNOWN | 18 | 16:56.0 | 157.10s | [herenow](https://legacy.herenow.com/results/#/races/20555/results) |
| 2018-10-14 | Head of the Quinobequin | Womens U19 1x | girls | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20555/results) |
| 2018-10-20 | Head Of The Charles | Men's Youth Fours | boys | 1V | 42 | 19:15.2 | 101.70s | [herenow](https://legacy.herenow.com/results/#/races/20514/results) |
| 2018-10-20 | Head Of The Charles | Women's Youth Fours | girls | 1V | 24 | 20:18.7 | 100.90s | [herenow](https://legacy.herenow.com/results/#/races/20514/results) |
| 2018-10-20 | Head Of The Charles | Womens Youth Coxed Quad | girls | 1V | 24 | 21:16.9 | 131.40s | [herenow](https://legacy.herenow.com/results/#/races/20514/results) |
| 2018-10-28 | MPSRA Fall Championship | Boys 1st Novice 4+ | boys | 1st Novice | 3 | 14:08.4 | 40.70s | [herenow](https://legacy.herenow.com/results/#/races/20561/results) |
| 2018-10-28 | MPSRA Fall Championship | Boys 1st Novice 8+ | boys | 1st Novice | 8 | 14:57.9 | 172.70s | [herenow](https://legacy.herenow.com/results/#/races/20561/results) |
| 2018-10-28 | MPSRA Fall Championship | Boys 1st Varsity 4+ | boys | 1V | 1 | 12:13.1 | 2.30s | [herenow](https://legacy.herenow.com/results/#/races/20561/results) |
| 2018-10-28 | MPSRA Fall Championship | Boys 2nd Varsity 4+ | boys | 2V | 2 | 12:52.0 | 1.90s | [herenow](https://legacy.herenow.com/results/#/races/20561/results) |
| 2018-10-28 | MPSRA Fall Championship | Boys 3rd Varsity 4+ | boys | 3V | 3 | 13:43.6 | 38.80s | [herenow](https://legacy.herenow.com/results/#/races/20561/results) |
| 2018-10-28 | MPSRA Fall Championship | Boys 4th Varsity 4+ | boys | 4V | 3 | 13:42.7 | 20.50s | [herenow](https://legacy.herenow.com/results/#/races/20561/results) |
| 2018-10-28 | MPSRA Fall Championship | Girls 1st Novice 4+ | girls | 1st Novice | 1 | 14:34.5 | 26.20s | [herenow](https://legacy.herenow.com/results/#/races/20561/results) |
| 2018-10-28 | MPSRA Fall Championship | Girls 1st Novice 8+ | girls | 1st Novice | 8 | 15:57.1 | 164.90s | [herenow](https://legacy.herenow.com/results/#/races/20561/results) |
| 2018-10-28 | MPSRA Fall Championship | Girls 1st Varsity 4+ | girls | 1V | 2 | 13:30.4 | 1.50s | [herenow](https://legacy.herenow.com/results/#/races/20561/results) |
| 2018-10-28 | MPSRA Fall Championship | Girls 2nd Varsity 4+ | girls | 2V | 1 | 13:39.8 | 18.50s | [herenow](https://legacy.herenow.com/results/#/races/20561/results) |
| 2018-10-28 | MPSRA Fall Championship | Girls 3rd Varsity 4+ | girls | 3V | 3 | 16:04.5 | 79.70s | [herenow](https://legacy.herenow.com/results/#/races/20561/results) |
| 2018-10-28 | MPSRA Fall Championship | Girls 4th Varsity 4+ | girls | 4V | 2 | 15:59.5 | 68.80s | [herenow](https://legacy.herenow.com/results/#/races/20561/results) |

### 2017 (111 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 12 - Junior Women LWT & HWT, Open HS | girls | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 12 - Junior Women LWT & HWT, Open HS | girls | UNKNOWN | 5 | 8:22.3 | 60.60s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 12 - Junior Women LWT & HWT, Open HS | girls | UNKNOWN | 10 | 8:35.5 | 73.80s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 12 - Junior Women LWT & HWT, Open HS | girls | UNKNOWN | 16 | 8:45.6 | 83.90s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 12 - Junior Women LWT & HWT, Open HS | girls | UNKNOWN | 4 | 8:28.2 | 31.70s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 12 - Junior Women LWT & HWT, Open HS | girls | UNKNOWN | 20 | 9:36.2 | 99.70s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 13 - Junior Women LWT, Open HS | girls | UNKNOWN | 5 | 7:59.3 | 4.10s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 13 - Junior Women LWT, Open HS | girls | UNKNOWN | 12 | 8:18.0 | 22.80s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 14 - Junior Men HWT & LWT, Open HS | boys | UNKNOWN | 11 | 7:32.2 | 58.50s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 14 - Junior Men HWT & LWT, Open HS | boys | UNKNOWN | 2 | 7:24.9 | 1.30s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 14 - Junior Men HWT & LWT, Open HS | boys | UNKNOWN | 9 | 7:38.7 | 15.10s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 15 - Junior LWT Men, Open HS | boys | UNKNOWN | 20 | 7:11.9 | 31.70s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 15 - Junior LWT Men, Open HS | boys | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 15 - Junior LWT Men, Open HS | boys | UNKNOWN | 1 | 6:59.4 | 0.30s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 15 - Junior LWT Men, Open HS | boys | UNKNOWN | 2 | 6:59.7 | 0.30s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 15 - Junior LWT Men, Open HS | boys | UNKNOWN | 4 | 7:04.2 | 4.80s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 15 - Junior LWT Men, Open HS | boys | UNKNOWN | 14 | 7:25.1 | 23.40s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 15 - Junior LWT Men, Open HS | boys | UNKNOWN | 19 | 7:33.0 | 31.30s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 16 - Junior LWT Men, Open HS | boys | UNKNOWN | 13 | 6:51.1 | 14.10s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 16 - Junior LWT Men, Open HS | boys | UNKNOWN | 22 | 7:01.1 | 23.20s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 17 - Junior HWT Women, Open HS | girls | UNKNOWN | 9 | 8:15.5 | 19.70s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 18 - Junior HWT Women, Open HS | girls | UNKNOWN | 11 | 7:34.1 | 12.20s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 19 -Junior HWT Men, Open HS | boys | UNKNOWN | 18 | 8:03.6 | 68.60s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-02-12 | C.R.A.S.H.-B. Sprints | Wave 20 --Junior HWT Men, Open HS | boys | UNKNOWN | 5 | 6:43.4 | 9.10s | [herenow](https://legacy.herenow.com/results/#/races/20330/results) |
| 2017-04-08 | NEIRA Boys Fours: BB&N vs. CRLS; Milton (May | First Boat | boys | 1V | 1 | 4:01.8 | 10.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6FB3384D5CC3492A87B0C133BEA1AF5E) |
| 2017-04-08 | NEIRA Boys Fours: BB&N vs. CRLS; Milton (May | Second Boat | boys | 2V | 1 | 4:13.1 | 6.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6FB3384D5CC3492A87B0C133BEA1AF5E) |
| 2017-04-08 | NEIRA Girls Fours: BB&N Girls varsity vs. CR | First Boat | girls | 1V | 2 | 4:30.4 | 1.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C18F3ACD54A0883B096601A84805DE80) |
| 2017-04-08 | NEIRA Girls Fours: BB&N Girls varsity vs. CR | Second Boat | girls | 2V | 1 | 4:49.8 | 8.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=C18F3ACD54A0883B096601A84805DE80) |
| 2017-04-15 | CRLS | First Boat | boys | 1V | 3 | 4:43.0 | 5.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1E3EC8A3BCA6687FB52638A930052F59) |
| 2017-04-15 | CRLS | Second Boat | boys | 2V | 2 | 4:51.9 | 4.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1E3EC8A3BCA6687FB52638A930052F59) |
| 2017-04-15 | CRLS | Third Boat | boys | 3V | 1 | 4:50.1 | 5.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1E3EC8A3BCA6687FB52638A930052F59) |
| 2017-04-15 | NEIRA Girls Fours: Cambridge Rindge and Lati | First Boat | girls | 1V | 1 | 5:35.38 | 0.83s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=E7137A2845C5A8F4CD2D472096AFDD86) |
| 2017-04-15 | NEIRA Girls Fours: Cambridge Rindge and Lati | Second Boat | girls | 2V | 1 | 5:40.43 | 5.22s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=E7137A2845C5A8F4CD2D472096AFDD86) |
| 2017-04-26 | Dexter / Southfield | First Boat | boys | 1V | 3 | 4:04.03 | 9.65s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=74EFDE21F578DE6367CC71210618311F) |
| 2017-04-26 | Dexter / Southfield | Fourth Boat | boys | 4V | 2 | 4:27 | 8.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=74EFDE21F578DE6367CC71210618311F) |
| 2017-04-26 | Dexter / Southfield | Other | girls | UNKNOWN | 1 | 4:23.86 | 1.06s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=74EFDE21F578DE6367CC71210618311F) |
| 2017-04-26 | Dexter / Southfield | Other | girls | UNKNOWN | 2 | 4:35 | 13.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=74EFDE21F578DE6367CC71210618311F) |
| 2017-04-26 | Dexter / Southfield | Second Boat | boys | 2V | 2 | 4:07.78 | 1.68s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=74EFDE21F578DE6367CC71210618311F) |
| 2017-04-26 | Dexter / Southfield | Third Boat | boys | 3V | 1 | 4:11.71 | 9.49s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=74EFDE21F578DE6367CC71210618311F) |
| 2017-04-26 | Dexter / Southfield | Third Boat | girls | 3V | 3 | 4:56.5 | 18.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=74EFDE21F578DE6367CC71210618311F) |
| 2017-04-29 | NEIRA Boys & Girls Fours: Hopkins vs. CRLS | First Boat | boys | 1V | 2 | 4:40.43 | 1.05s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FC237E6784E661C0E07D4785C23EA7A9) |
| 2017-04-29 | NEIRA Boys & Girls Fours: Hopkins vs. CRLS | Fourth Boat | boys | 4V | 2 | 5:18.19 | 12.13s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FC237E6784E661C0E07D4785C23EA7A9) |
| 2017-04-29 | NEIRA Boys & Girls Fours: Hopkins vs. CRLS | Other | girls | UNKNOWN | 1 | 5:10.97 |  | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FC237E6784E661C0E07D4785C23EA7A9) |
| 2017-04-29 | NEIRA Boys & Girls Fours: Hopkins vs. CRLS | Second Boat | boys | 2V | 1 | 4:34.79 | 9.42s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FC237E6784E661C0E07D4785C23EA7A9) |
| 2017-04-29 | NEIRA Boys & Girls Fours: Hopkins vs. CRLS | Third Boat | boys | 3V | 1 | 4:46.29 | 10.83s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FC237E6784E661C0E07D4785C23EA7A9) |
| 2017-04-29 | NEIRA Boys & Girls Fours: Hopkins vs. CRLS | Third Boat | girls | 3V | 1 | 5:39.60 | 46.44s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=FC237E6784E661C0E07D4785C23EA7A9) |
| 2017-05-20 | Northeast Youths | Mens Youth 2nd 4+ Final | boys | 2V | 3 | 7:25.6 | 14.50s | [herenow](https://legacy.herenow.com/results/#/races/20373/results) |
| 2017-05-20 | Northeast Youths | Mens Youth 2nd 4+ Time Trial | boys | 2V | 3 | 6:48.8 | 16.90s | [herenow](https://legacy.herenow.com/results/#/races/20373/results) |
| 2017-05-20 | Northeast Youths | Mens Youth 2nd 4+ Time Trial | boys | 2V | 16 | 8:14.0 | 102.10s | [herenow](https://legacy.herenow.com/results/#/races/20373/results) |
| 2017-05-20 | Northeast Youths | Mens Youth 4+ Final | boys | 1V | 5 | 6:54.5 | 19.40s | [herenow](https://legacy.herenow.com/results/#/races/20373/results) |
| 2017-05-20 | Northeast Youths | Mens Youth 4+ Semifinal 1 | boys | 1V | 3 | 6:49.0 | 16.70s | [herenow](https://legacy.herenow.com/results/#/races/20373/results) |
| 2017-05-20 | Northeast Youths | Mens Youth 4+ Time Trial | boys | 1V | 5 | 6:36.5 | 14.50s | [herenow](https://legacy.herenow.com/results/#/races/20373/results) |
| 2017-05-20 | Northeast Youths | Mens Youth Ltwt 4+ Final | boys | 1V | 1 | 7:00.8 | 1.60s | [herenow](https://legacy.herenow.com/results/#/races/20373/results) |
| 2017-05-20 | Northeast Youths | Mens Youth Ltwt 4+ Time Trial | boys | 1V | 1 | 6:47.6 | 0.80s | [herenow](https://legacy.herenow.com/results/#/races/20373/results) |
| 2017-05-20 | Northeast Youths | Womens Youth 2nd 4+ Final | girls | 2V | 7 | 8:26.3 | 26.20s | [herenow](https://legacy.herenow.com/results/#/races/20373/results) |
| 2017-05-20 | Northeast Youths | Womens Youth 2nd 4+ Time Trial | girls | 2V | 4 | 7:39.9 | 18.90s | [herenow](https://legacy.herenow.com/results/#/races/20373/results) |
| 2017-05-20 | Northeast Youths | Womens Youth 4+ Semifinal 2 | girls | 1V | 4 | 7:35.0 | 14.30s | [herenow](https://legacy.herenow.com/results/#/races/20373/results) |
| 2017-05-20 | Northeast Youths | Womens Youth 4+ Time Trial | girls | 1V | 6 | 7:18.4 | 12.80s | [herenow](https://legacy.herenow.com/results/#/races/20373/results) |
| 2017-05-20 | Northeast Youths | Womens Youth Novice 4+ Final | girls | Novice | 4 | 8:39.2 | 20.40s | [herenow](https://legacy.herenow.com/results/#/races/20373/results) |
| 2017-05-20 | Northeast Youths | Womens Youth Novice 4+ Time Trial | girls | Novice | 6 | 8:08.9 | 32.90s | [herenow](https://legacy.herenow.com/results/#/races/20373/results) |
| 2017-05-27 | NEIRA Championship 2017 | boys 1V 4+ - Heat 1 | boys | 1V | 3 | 4:56.270 | 8.22s | [neira-championship-pdf](http://neira.qra.org/PDF/2017NEIRA.pdf) |
| 2017-05-27 | NEIRA Championship 2017 | boys 1V 4+ - Petite Final | boys | 1V | 3 | 5:09.770 | 3.69s | [neira-championship-pdf](http://neira.qra.org/PDF/2017NEIRA.pdf) |
| 2017-05-27 | NEIRA Championship 2017 | boys 2V 4+ - Heat 2 | boys | 2V | 3 | 5:03.710 | 3.64s | [neira-championship-pdf](http://neira.qra.org/PDF/2017NEIRA.pdf) |
| 2017-05-27 | NEIRA Championship 2017 | boys 3V 4+ - Heat 2 | boys | 3V | 2 | 5:03.670 | 0.27s | [neira-championship-pdf](http://neira.qra.org/PDF/2017NEIRA.pdf) |
| 2017-05-27 | NEIRA Championship 2017 | girls 1V 4+ - Heat 3 | girls | 1V | 5 | 5:42.800 | 7.91s | [neira-championship-pdf](http://neira.qra.org/PDF/2017NEIRA.pdf) |
| 2017-05-28 | MPSRA Spring Championship | Boys 1st Varsity 4+ Grand Final | boys | 1V | 1 | 4:56.3 | 4.70s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-05-28 | MPSRA Spring Championship | Boys 1st Varsity 4+ Heat 1 | boys | 1V | 1 | 5:36.0 | 5.40s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-05-28 | MPSRA Spring Championship | Boys 2- | boys | UNKNOWN | 2 | 5:47.8 | 1.40s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-05-28 | MPSRA Spring Championship | Boys 2nd Varsity 4+ Final | boys | 2V | 1 | 5:11.1 | 15.70s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-05-28 | MPSRA Spring Championship | Boys 2nd Varsity 4+ Heat 1 | boys | 2V | 1 | 5:16.7 | 16.70s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-05-28 | MPSRA Spring Championship | Boys 3rd Varsity 4+ Final | boys | 3V | 1 | 5:07.0 | 22.80s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-05-28 | MPSRA Spring Championship | Boys 4th Varsity 4+ Final | boys | 4V | 2 | 5:55.4 | 27.50s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-05-28 | MPSRA Spring Championship | Boys Novice 4+ Final | boys | Novice | 3 | 5:02.5 | 20.10s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-05-28 | MPSRA Spring Championship | Girls 1st Varsity 4+ Grand Final | girls | 1V | 2 | 5:23.8 | 4.00s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-05-28 | MPSRA Spring Championship | Girls 1st Varsity 4+ Heat 1 | girls | 1V | 1 | 6:11.1 | 20.00s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-05-28 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Final | girls | 2V | 1 | 5:57.7 | 6.30s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-05-28 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Heat 1 | girls | 2V | 1 | 5:53.4 | 16.00s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-05-28 | MPSRA Spring Championship | Girls 3rd Varsity 4+ Final | girls | 3V | 2 | 5:30.1 | 0.30s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-05-28 | MPSRA Spring Championship | Girls Novice 4+ Final | girls | Novice | 3 | 6:15.4 | 9.30s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-05-28 | MPSRA Spring Championship | Girls Novice 4+ Heat 1 | girls | Novice | 1 | 6:54.2 | 2.60s | [herenow](https://legacy.herenow.com/results/#/races/20384/results) |
| 2017-06-09 | Youth Nationals | Mens Ltwt Youth 4+ Final B | boys | 1V | 4 | 6:46.8 | 4.70s | [herenow](https://legacy.herenow.com/results/#/races/20374/results) |
| 2017-06-09 | Youth Nationals | Mens Ltwt Youth 4+ Semifinal 1 | boys | 1V | 5 | 7:03.6 | 15.10s | [herenow](https://legacy.herenow.com/results/#/races/20374/results) |
| 2017-06-09 | Youth Nationals | Mens Ltwt Youth 4+ Time Trial | boys | 1V | 8 | 6:38.9 | 13.10s | [herenow](https://legacy.herenow.com/results/#/races/20374/results) |
| 2017-09-16 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | 2 | 19:27.5 | 1.90s | [herenow](https://legacy.herenow.com/results/#/races/20433/results) |
| 2017-09-16 | CRI Fall Classic | Mens Jr 8+ | boys | UNKNOWN | 12 | 19:22.8 | 131.30s | [herenow](https://legacy.herenow.com/results/#/races/20433/results) |
| 2017-09-16 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 2 | 21:49.8 | 43.20s | [herenow](https://legacy.herenow.com/results/#/races/20433/results) |
| 2017-09-16 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | 4 | 22:13.6 | 67.00s | [herenow](https://legacy.herenow.com/results/#/races/20433/results) |
| 2017-09-16 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20433/results) |
| 2017-10-01 | Textile River Regatta | Mens Jr 4+ | boys | UNKNOWN | 3 | 21:59.1 | 20.00s | [herenow](https://legacy.herenow.com/results/#/races/20437/results) |
| 2017-10-01 | Textile River Regatta | Mens Jr 4+ | boys | UNKNOWN | 6 | 22:19.5 | 40.40s | [herenow](https://legacy.herenow.com/results/#/races/20437/results) |
| 2017-10-01 | Textile River Regatta | Mens Jr 8+ A | boys | UNKNOWN | 19 | 22:04.3 | 157.10s | [herenow](https://legacy.herenow.com/results/#/races/20437/results) |
| 2017-10-01 | Textile River Regatta | Womens Jr 2x | girls | UNKNOWN | 4 | 27:01.5 | 149.50s | [herenow](https://legacy.herenow.com/results/#/races/20437/results) |
| 2017-10-01 | Textile River Regatta | Womens Jr 4+ | girls | UNKNOWN | 5 | 24:39.9 | 71.10s | [herenow](https://legacy.herenow.com/results/#/races/20437/results) |
| 2017-10-01 | Textile River Regatta | Womens Jr 4x | girls | UNKNOWN | 4 | 26:03.2 | 126.30s | [herenow](https://legacy.herenow.com/results/#/races/20437/results) |
| 2017-10-15 | HOCR Test | Men's Youth Fours | boys | 1V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20318/results) |
| 2017-10-15 | HOCR Test | Women's Youth Fours | girls | 1V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20318/results) |
| 2017-10-15 | Head of the Quinobequin | Mens U19 1x | boys | UNKNOWN | 22 | 14:49.7 | 102.40s | [herenow](https://legacy.herenow.com/results/#/races/20435/results) |
| 2017-10-21 | Head Of The Charles | Men's Youth Fours | boys | 1V | 38 | 17:20.4 | 67.50s | [herenow](https://legacy.herenow.com/results/#/races/20398/results) |
| 2017-10-21 | Head Of The Charles | Men's Youth Fours | boys | 1V | 52 | 17:38.4 | 85.50s | [herenow](https://legacy.herenow.com/results/#/races/20398/results) |
| 2017-10-21 | Head Of The Charles | Women's Youth Fours | girls | 1V | 32 | 19:48.4 | 93.20s | [herenow](https://legacy.herenow.com/results/#/races/20398/results) |
| 2017-10-29 | MPSRA Fall Championship | Boys 1st Novice 8+ | boys | 1st Novice | 9 | 17:12.5 | 133.40s | [herenow](https://legacy.herenow.com/results/#/races/20425/results) |
| 2017-10-29 | MPSRA Fall Championship | Boys 1st Varsity 4+ | boys | 1V | 1 | 15:32.1 | 3.60s | [herenow](https://legacy.herenow.com/results/#/races/20425/results) |
| 2017-10-29 | MPSRA Fall Championship | Boys 1st Varsity 8+ | boys | 1V | 7 | 15:10.1 | 79.80s | [herenow](https://legacy.herenow.com/results/#/races/20425/results) |
| 2017-10-29 | MPSRA Fall Championship | Boys 2nd Varsity 4+ | boys | 2V | 1 | 15:57.4 | 11.90s | [herenow](https://legacy.herenow.com/results/#/races/20425/results) |
| 2017-10-29 | MPSRA Fall Championship | Boys Novice 4+ | boys | Novice | 3 | 17:35.3 | 65.00s | [herenow](https://legacy.herenow.com/results/#/races/20425/results) |
| 2017-10-29 | MPSRA Fall Championship | Girls 1st Novice 8+ | girls | 1st Novice | 7 | 19:43.7 | 219.40s | [herenow](https://legacy.herenow.com/results/#/races/20425/results) |
| 2017-10-29 | MPSRA Fall Championship | Girls 1st Varsity 4+ | girls | 1V | 1 | 17:27.6 | 3.00s | [herenow](https://legacy.herenow.com/results/#/races/20425/results) |
| 2017-10-29 | MPSRA Fall Championship | Girls 2nd Varsity 4+ | girls | 2V | 1 | 17:44.9 | 27.30s | [herenow](https://legacy.herenow.com/results/#/races/20425/results) |
| 2017-10-29 | MPSRA Fall Championship | Girls 2x | girls | UNKNOWN | 3 | 17:42.6 | 18.40s | [herenow](https://legacy.herenow.com/results/#/races/20425/results) |
| 2017-10-29 | MPSRA Fall Championship | Girls 2x | girls | UNKNOWN | 7 | 19:32.2 | 128.00s | [herenow](https://legacy.herenow.com/results/#/races/20425/results) |
| 2017-10-29 | MPSRA Fall Championship | Girls Novice 4+ | girls | Novice | 4 | 18:49.4 | 63.30s | [herenow](https://legacy.herenow.com/results/#/races/20425/results) |

### 2016 (96 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2016-04-16 | Girl's Fours: Winsor School vs. Choate, Camb | 2nd Four | girls | 2V | 3 | 4:52.1 | 10.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=0FB87F11432916227253F28DF563F70A) |
| 2016-04-16 | Girl's Fours: Winsor School vs. Choate, Camb | Varsity Four | girls | 1V | 2 | 4:38.9 | 5.03s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=0FB87F11432916227253F28DF563F70A) |
| 2016-04-27 | Belmont Hill  vs. CRLS, Middlesex, BC High | 2V4 | UNKNOWN | UNKNOWN | 3 | 4:57.8 | 29.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=715F8F3775B95354D047387DFC99D8BC) |
| 2016-04-27 | Belmont Hill  vs. CRLS, Middlesex, BC High | 3V4 | UNKNOWN | UNKNOWN | 2 | 4:42.2 | 6.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=715F8F3775B95354D047387DFC99D8BC) |
| 2016-04-27 | Belmont Hill  vs. CRLS, Middlesex, BC High | Varsity Four | UNKNOWN | 1V | 2 | 4:30.7 | 15.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=715F8F3775B95354D047387DFC99D8BC) |
| 2016-05-04 | St. Mark's School (Girls' Fours) vs. Newton  | Second Varsity Four | girls | 2V | 3 | 5:47.92 | 4.09s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=02EF2E9292ABF5545FAD43FE24E8D057) |
| 2016-05-04 | St. Mark's School (Girls' Fours) vs. Newton  | Third Varsity Four | girls | 3V | 3 | 6:01.2 | 10.95s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=02EF2E9292ABF5545FAD43FE24E8D057) |
| 2016-05-04 | St. Mark's School (Girls' Fours) vs. Newton  | Varsity Four | girls | 1V | 3 | 5:37.46 | 11.97s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=02EF2E9292ABF5545FAD43FE24E8D057) |
| 2016-05-08 | Fours: CRLS vs. DBMS, Medford, CRI | 1st Varsity Four | UNKNOWN | 1V | 2 | 8:10.70 | 19.18s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=EBC4BC890AFF71C9FA7CF279CFD041FA) |
| 2016-05-08 | Fours: CRLS vs. DBMS, Medford, CRI | 2nd Varsity Four | UNKNOWN | 2V | 1 | 8:34.66 | 54.78s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=EBC4BC890AFF71C9FA7CF279CFD041FA) |
| 2016-05-08 | Fours: CRLS vs. DBMS, Medford, CRI | 3rd Varsity Four | UNKNOWN | 2V | 2 | 8:52.34 | 31.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=EBC4BC890AFF71C9FA7CF279CFD041FA) |
| 2016-05-08 | Fours: CRLS vs. DBMS, Medford, CRI | 4th Varsity Four | UNKNOWN | 4V | 1 | 8:58.82 | 9.15s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=EBC4BC890AFF71C9FA7CF279CFD041FA) |
| 2016-05-09 | Fours: CRLS vs. DBMS, CRI, CBC | 1st Varsity Four | UNKNOWN | 1V | 4 | 9:08.95 | 27.41s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1806CE2EF84BCAD0CA37C4F35A889058) |
| 2016-05-09 | Fours: CRLS vs. DBMS, CRI, CBC | 2nd Varsity Four | UNKNOWN | 2V | 2 | 9:37.43 | 7.01s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1806CE2EF84BCAD0CA37C4F35A889058) |
| 2016-05-09 | Fours: CRLS vs. DBMS, CRI, CBC | 2nd Varsity Four | UNKNOWN | 3V | 4 | 10:07.35 | 36.93s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1806CE2EF84BCAD0CA37C4F35A889058) |
| 2016-05-09 | Fours: CRLS vs. DBMS, CRI, CBC | Fourth Varsity Four | UNKNOWN | 4V | 3 | 10:12.60 | 46.05s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1806CE2EF84BCAD0CA37C4F35A889058) |
| 2016-05-14 | Lowell Invitational | Mens Jr 2nd Novice 4+ Final | boys | 2nd Novice | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-14 | Lowell Invitational | Mens Jr 2nd Varsity 4+ Final | boys | 2V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-14 | Lowell Invitational | Mens Jr 2nd Varsity 4+ Heat 1 | boys | 2V | 2 | 7:01.7 | 12.40s | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-14 | Lowell Invitational | Mens Jr 2nd Varsity 4+ Heat 1 | boys | 2V | 4 | 7:14.0 | 24.70s | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-14 | Lowell Invitational | Mens Jr 2nd Varsity 4+ Heat 2 | boys | 2V | 1 | 6:31.5 | 1.50s | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-14 | Lowell Invitational | Mens Jr Novice 4+ Final | boys | Novice | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-14 | Lowell Invitational | Mens Jr Novice 4+ Heat 2 | boys | Novice | 1 | 7:21.1 | 25.90s | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-14 | Lowell Invitational | Mens Jr Varsity 4+ Heat 4 | boys | 1V | 2 | 6:46.0 | 15.00s | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-14 | Lowell Invitational | Womens Jr 2nd Varsity 4+ Final | girls | 2V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-14 | Lowell Invitational | Womens Jr 2nd Varsity 4+ Heat 1 | girls | 2V | 2 | 3:36.0 | 8.60s | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-14 | Lowell Invitational | Womens Jr 2nd Varsity 4+ Heat 3 | girls | 2V | 1 | 7:34.5 | 20.00s | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-14 | Lowell Invitational | Womens Jr 2nd Varsity 4+ Heat 4 | girls | 2V | 3 | 7:44.6 | 11.80s | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-14 | Lowell Invitational | Womens Jr Novice 4+ Heat 3 | girls | Novice | 4 | 8:30.7 | 41.30s | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-14 | Lowell Invitational | Womens Jr Varsity 4+ Final | girls | 1V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-14 | Lowell Invitational | Womens Jr Varsity 4+ Heat 3 | girls | 1V | 1 | 7:27.6 | 13.70s | [herenow](https://legacy.herenow.com/results/#/races/20226/results) |
| 2016-05-21 | Northeast Youth Championship | Mens Youth 2nd 4+ Final A | boys | 2V | 2 | 7:11.9 | 1.50s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Mens Youth 2nd 4+ Final A | boys | 2V | 6 | 7:26.0 | 15.60s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Mens Youth 2nd 4+ Heat 1 | boys | 2V | 2 | 8:01.9 | 3.50s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Mens Youth 2nd 4+ Heat 2 | boys | 2V | 3 | 7:54.3 | 7.30s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Mens Youth 2nd 4+ Semi 1 | boys | 2V | 3 | 7:16.5 | 4.60s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Mens Youth 2nd 4+ Semi 2 | boys | 2V | 3 | 7:26.1 | 12.80s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Mens Youth 4+ Heat 2 | boys | 1V | 3 | 7:48.7 | 18.10s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Mens Youth 4+ Heat 4 | boys | 1V | 2 | 7:42.3 | 8.00s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Mens Youth 4+ Semi 1 | boys | 1V | 4 | 6:58.2 | 16.50s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Mens Youth 4+ Semi 1 | boys | 1V | 6 | 7:06.4 | 24.70s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Mens Youth Novice 4+ Final A | boys | Novice | 2 | 7:20.2 | 1.10s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Mens Youth Novice 4+ Heat 2 | boys | Novice | 1 | 7:55.3 | 6.70s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Womens Youth 2nd 4+ Final A | girls | 2V | 5 | 8:04.8 | 13.60s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Womens Youth 2nd 4+ Heat 3 | girls | 2V | 1 | 8:39.4 | 21.70s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Womens Youth 2nd 4+ Semi 2 | girls | 2V | 2 | 8:06.6 | 4.20s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Womens Youth 4+ Final A | girls | 1V | 5 | 7:35.5 | 22.10s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Womens Youth 4+ Heat 3 | girls | 1V | 3 | 8:50.5 | 31.40s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Womens Youth 4+ Heat 4 | girls | 1V | 1 | 8:37.9 | 9.20s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Womens Youth 4+ Semi 2 | girls | 1V | 3 | 7:44.5 | 14.40s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Womens Youth 4+ Semi 2 | girls | 1V | 5 | 7:53.8 | 23.70s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Womens Youth Ltwt 4+ Heat 2 | girls | 1V | 5 | 9:31.6 | 65.50s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-21 | Northeast Youth Championship | Womens Youth Novice 8+ Heat 3 | girls | Novice | 6 | 9:36.2 | 88.00s | [herenow](https://legacy.herenow.com/results/#/races/20229/results) |
| 2016-05-28 | NEIRA Championship 2016 | girls 1V 4+ - Petite Final | girls | 1V | 2 | 5:51.084 | 5.92s | [neira-championship-pdf](http://www.neirarowing.org/documents/2016NEIRAResults.pdf) |
| 2016-05-28 | NEIRA Championship 2016 | girls 3V 4+ - Heat 2 | girls | 3V | 3 | 6:04.430 | 4.97s | [neira-championship-pdf](http://www.neirarowing.org/documents/2016NEIRAResults.pdf) |
| 2016-05-29 | MPSRA Spring Championship | Boys 1st Varsity 4+ Grand Final | boys | 1V | 1 | 5:29.4 | 4.50s | [herenow](https://legacy.herenow.com/results/#/races/20232/results) |
| 2016-05-29 | MPSRA Spring Championship | Boys 1st Varsity 4+ Heat 3 | boys | 1V | 1 | 5:43.5 | 10.80s | [herenow](https://legacy.herenow.com/results/#/races/20232/results) |
| 2016-05-29 | MPSRA Spring Championship | Boys 2nd Varsity 4+ Final | boys | 2V | 1 | 5:43.0 | 1.50s | [herenow](https://legacy.herenow.com/results/#/races/20232/results) |
| 2016-05-29 | MPSRA Spring Championship | Boys 2nd Varsity 4+ Heat 2 | boys | 2V | 1 | 5:48.2 | 15.90s | [herenow](https://legacy.herenow.com/results/#/races/20232/results) |
| 2016-05-29 | MPSRA Spring Championship | Boys 3rd Varsity 4+ Final | boys | 3V | 1 | 5:47.7 | 8.70s | [herenow](https://legacy.herenow.com/results/#/races/20232/results) |
| 2016-05-29 | MPSRA Spring Championship | Boys 4th Varsity 4+ Final | boys | 4V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20232/results) |
| 2016-05-29 | MPSRA Spring Championship | Boys Novice 4+ Final | boys | Novice | 1 | 6:02.4 | 16.90s | [herenow](https://legacy.herenow.com/results/#/races/20232/results) |
| 2016-05-29 | MPSRA Spring Championship | Boys Novice 4+ Heat 1 | boys | Novice | 1 | 5:52.1 | 25.90s | [herenow](https://legacy.herenow.com/results/#/races/20232/results) |
| 2016-05-29 | MPSRA Spring Championship | Girls 1st Varsity 4+ Grand Final | girls | 1V | 2 | 6:06.9 | 1.70s | [herenow](https://legacy.herenow.com/results/#/races/20232/results) |
| 2016-05-29 | MPSRA Spring Championship | Girls 1st Varsity 4+ Heat 2 | girls | 1V | 1 | 6:05.9 | 19.30s | [herenow](https://legacy.herenow.com/results/#/races/20232/results) |
| 2016-05-29 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Final | girls | 2V | 1 | 6:13.1 | 6.00s | [herenow](https://legacy.herenow.com/results/#/races/20232/results) |
| 2016-05-29 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Heat 2 | girls | 2V | 1 | 6:19.5 | 31.60s | [herenow](https://legacy.herenow.com/results/#/races/20232/results) |
| 2016-05-29 | MPSRA Spring Championship | Girls 3rd/4th Varsity 4+ Final | girls | 4V | 1 | 6:27.1 | 20.10s | [herenow](https://legacy.herenow.com/results/#/races/20232/results) |
| 2016-05-29 | MPSRA Spring Championship | Girls Novice 4+ Final | girls | Novice | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20232/results) |
| 2016-07-10 | Cromwell Cup | Mens Open 2- Heat 3 | boys | UNKNOWN | 4 | 4:01.9 | 38.60s | [herenow](https://legacy.herenow.com/results/#/races/20240/results) |
| 2016-09-17 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | 3 | 19:39.1 | 39.40s | [herenow](https://legacy.herenow.com/results/#/races/20302/results) |
| 2016-09-17 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | 6 | 20:37.8 | 98.10s | [herenow](https://legacy.herenow.com/results/#/races/20302/results) |
| 2016-09-17 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20302/results) |
| 2016-10-09 | New England Jr/HS Championship | Mens 1st Varsity 4+ | boys | 1V | 1 | 16:25.6 | 4.20s | [herenow](https://legacy.herenow.com/results/#/races/20315/results) |
| 2016-10-09 | New England Jr/HS Championship | Mens 2nd Varsity 4+ | boys | 2V | 1 | 16:48.0 | 3.00s | [herenow](https://legacy.herenow.com/results/#/races/20315/results) |
| 2016-10-09 | New England Jr/HS Championship | Mens 3rd/4th Varsity 4+ | boys | 4V | 1 | 17:16.2 | 66.30s | [herenow](https://legacy.herenow.com/results/#/races/20315/results) |
| 2016-10-09 | New England Jr/HS Championship | Mens 3rd/4th Varsity 4+ | boys | 4V | 2 | 18:22.5 | 66.30s | [herenow](https://legacy.herenow.com/results/#/races/20315/results) |
| 2016-10-09 | New England Jr/HS Championship | Womens 1st Varsity 4+ | girls | 1V | 3 | 18:25.6 | 25.40s | [herenow](https://legacy.herenow.com/results/#/races/20315/results) |
| 2016-10-09 | New England Jr/HS Championship | Womens 2nd Varsity 4+ | girls | 2V | 10 | 21:45.5 | 168.40s | [herenow](https://legacy.herenow.com/results/#/races/20315/results) |
| 2016-10-15 | Head of the Kevin III | HOK Speed Order | UNKNOWN | UNKNOWN | 54 | 19:58.1 | 284.30s | [herenow](https://legacy.herenow.com/results/#/races/20306/results) |
| 2016-10-22 | Head of the Charles | Men's Youth Fours | boys | 1V | 20 | 18:53.5 | 48.90s | [herenow](https://legacy.herenow.com/results/#/races/20272/results) |
| 2016-10-22 | Head of the Charles | Men's Youth Fours | boys | 1V | 38 | 19:18.2 | 73.60s | [herenow](https://legacy.herenow.com/results/#/races/20272/results) |
| 2016-10-22 | Head of the Charles | Women's Youth Fours | girls | 1V | 22 | 20:53.5 | 77.80s | [herenow](https://legacy.herenow.com/results/#/races/20272/results) |
| 2016-10-30 | MPSRA Fall Championship | Boys 1st Novice 8+ | boys | 1st Novice | 10 | 19:15.0 | 232.20s | [herenow](https://legacy.herenow.com/results/#/races/20311/results) |
| 2016-10-30 | MPSRA Fall Championship | Boys 1st Varsity 4+ | boys | 1V | 1 | 15:10.2 | 41.70s | [herenow](https://legacy.herenow.com/results/#/races/20311/results) |
| 2016-10-30 | MPSRA Fall Championship | Boys 2nd Varsity 4+ | boys | 2V | 1 | 15:41.1 | 85.90s | [herenow](https://legacy.herenow.com/results/#/races/20311/results) |
| 2016-10-30 | MPSRA Fall Championship | Boys 2nd/3rd Novice 8+ | boys | 2nd Novice | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20311/results) |
| 2016-10-30 | MPSRA Fall Championship | Boys 3rd/4th Varsity 4+ | boys | 4V | 1 | 15:42.4 | 58.80s | [herenow](https://legacy.herenow.com/results/#/races/20311/results) |
| 2016-10-30 | MPSRA Fall Championship | Boys 3rd/4th Varsity 4+ | boys | 4V | 2 | 16:41.2 | 58.80s | [herenow](https://legacy.herenow.com/results/#/races/20311/results) |
| 2016-10-30 | MPSRA Fall Championship | Boys Novice 4+ | boys | Novice | 2 | 17:52.7 | 13.20s | [herenow](https://legacy.herenow.com/results/#/races/20311/results) |
| 2016-10-30 | MPSRA Fall Championship | Girls 1st Novice 8+ | girls | 1st Novice | 7 | 19:05.5 | 114.50s | [herenow](https://legacy.herenow.com/results/#/races/20311/results) |
| 2016-10-30 | MPSRA Fall Championship | Girls 1st Varsity 4+ | girls | 1V | 3 | 17:24.1 | 10.10s | [herenow](https://legacy.herenow.com/results/#/races/20311/results) |
| 2016-10-30 | MPSRA Fall Championship | Girls 2nd Varsity 4+ | girls | 2V | 1 | 17:47.2 | 63.90s | [herenow](https://legacy.herenow.com/results/#/races/20311/results) |
| 2016-10-30 | MPSRA Fall Championship | Girls 2nd/3rd Novice 8+ | girls | 2nd Novice | 3 | 22:42.1 | 258.90s | [herenow](https://legacy.herenow.com/results/#/races/20311/results) |
| 2016-10-30 | MPSRA Fall Championship | Girls 3rd/4th Varsity 4+ | girls | 4V | 3 | 20:19.5 | 102.20s | [herenow](https://legacy.herenow.com/results/#/races/20311/results) |
| 2016-10-30 | MPSRA Fall Championship | Girls Novice 4+ | girls | Novice | 3 | 21:16.6 | 113.60s | [herenow](https://legacy.herenow.com/results/#/races/20311/results) |

### 2015 (110 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2015-04-10 | Mayor's Cup (Boys and Girls Fours): CRLS  vs | Boys 1V Four | boys | 1V | 1 | 4:20.2 | 18.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5212802) |
| 2015-04-10 | Mayor's Cup (Boys and Girls Fours): CRLS  vs | Girls 1V Four | girls | 1V | 2 | 4:49.7 | 10.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5212802) |
| 2015-04-12 | Fours: Bancroft Crew vs. CRLS, Hopkins, Worc | 1G4 | girls | 1V | 1 | 5:48.0 | 20.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7924365) |
| 2015-04-12 | Fours: Bancroft Crew vs. CRLS, Hopkins, Worc | 2B4 | boys | 2V | 1 | 5:36.5 | 10.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7924365) |
| 2015-04-12 | Fours: Bancroft Crew vs. CRLS, Hopkins, Worc | 2G4 | girls | 2V | 1 | 6:06.3 | 2.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7924365) |
| 2015-04-12 | Fours: Bancroft Crew vs. CRLS, Hopkins, Worc | 2G4 | girls | 2V | 3 | 6:21.1 | 14.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7924365) |
| 2015-04-12 | Fours: Bancroft Crew vs. CRLS, Hopkins, Worc | 3B4 | boys | 3V | 1 | 5:34.3 | 32.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7924365) |
| 2015-04-12 | Fours: Bancroft Crew vs. CRLS, Hopkins, Worc | 3B4 | boys | 3V | 2 | 6:06.3 | 32.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7924365) |
| 2015-04-12 | Fours: Bancroft Crew vs. CRLS, Hopkins, Worc | Varsity Four | UNKNOWN | 1V | 1 | 5:04.1 | 11.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7924365) |
| 2015-04-16 | Boys and Girls FOURS: CRLS  vs. Milton | Boys 2V Four | boys | 2V | 1 | 5:08.73 | 18.25s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5038425) |
| 2015-04-16 | Boys and Girls FOURS: CRLS  vs. Milton | Boys 3V Four | boys | 3V | 1 | 4:30.16 | 3.78s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5038425) |
| 2015-04-16 | Boys and Girls FOURS: CRLS  vs. Milton | Boys 4V Four | boys | 4V | 1 | 5:10.19 | 12.62s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5038425) |
| 2015-04-16 | Boys and Girls FOURS: CRLS  vs. Milton | Girls 2V Four | girls | 2V | 1 | 5:57.79 |  | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5038425) |
| 2015-04-16 | Boys and Girls FOURS: CRLS  vs. Milton | Girls 3V Four | girls | 3V | 1 | 5:19 | 10.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5038425) |
| 2015-04-16 | Boys and Girls FOURS: CRLS  vs. Milton | Girls 4V Four | girls | 4V | 1 | 5:21.27 | 43.61s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5038425) |
| 2015-04-16 | Boys and Girls FOURS: CRLS  vs. Milton | Varsity 8 | girls | 1V | 2 | 5:11.22 | 1.08s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5038425) |
| 2015-04-16 | Boys and Girls FOURS: CRLS  vs. Milton | Varsity Four | boys | 1V | 1 | 4:44.95 | 15.15s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5038425) |
| 2015-04-18 | Lincoln School vs. Boys and Girls 4s CRLS, M | Boys 1V/2V | boys | 1V | 1 | 4:53.6 | 8.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2183463) |
| 2015-04-18 | Lincoln School vs. Boys and Girls 4s CRLS, M | Boys 1V/2V | boys | 2V | 2 | 5:01.9 | 8.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2183463) |
| 2015-04-18 | Lincoln School vs. Boys and Girls 4s CRLS, M | Boys 3V/4V | boys | 3V | 1 | 5:07.8 | 17.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2183463) |
| 2015-04-18 | Lincoln School vs. Boys and Girls 4s CRLS, M | Boys 3V/4V | boys | 4V | 2 | 5:24.9 | 17.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2183463) |
| 2015-04-18 | Lincoln School vs. Boys and Girls 4s CRLS, M | Girls 1V | girls | 1V | 1 | 5:37.5 | 2.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2183463) |
| 2015-04-18 | Lincoln School vs. Boys and Girls 4s CRLS, M | Girls 2V | girls | 2V | 1 | 5:54.8 | 9.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2183463) |
| 2015-04-18 | Lincoln School vs. Boys and Girls 4s CRLS, M | Girls 3V | girls | 3V | 1 | 5:52.7 | 19.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2183463) |
| 2015-04-18 | Lincoln School vs. Boys and Girls 4s CRLS, M | Girls 4V | girls | 4V | 1 | 5:48.6 | 36.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2183463) |
| 2015-05-06 | CRLS vs. BLS 1v and 3v (FOURS) | Girls 1V Four | girls | 1V | 1 | 4:41.7 | 8.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2848581) |
| 2015-05-06 | CRLS vs. BLS 1v and 3v (FOURS) | Girls 3V Four | girls | 3V | 1 | 4:50.22 | 25.09s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2848581) |
| 2015-05-07 | CRLS vs. BLS 2v and 4v (Fours) | Girls 2V Four | girls | 2V | 1 | 3:23.29 | 17.79s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3635747) |
| 2015-05-07 | CRLS vs. BLS 2v and 4v (Fours) | Girls 4v Four | girls | 4V | 1 | 3:53.81 | 18.89s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3635747) |
| 2015-05-09 | The Davison Cup | 2V | boys | 2V | 1 | 6:10.5 | 26.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1969264) |
| 2015-05-09 | The Davison Cup | 3V | boys | 3V | 1 | 5:47.6 | 40.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1969264) |
| 2015-05-09 | The Davison Cup | 4V | boys | 4V | 1 | 6:10.3 | 38.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1969264) |
| 2015-05-09 | The Davison Cup | Novice | girls | Novice | 1 | 6:59.5 | 19.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1969264) |
| 2015-05-09 | The Davison Cup | Varsity Four | boys | 1V | 1 | 6:14.4 | 0.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1969264) |
| 2015-05-09 | The Davison Cup- Boys Fours | 2V | boys | 2V | 1 | 5:13.7 | 7.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7697717) |
| 2015-05-09 | The Davison Cup- Boys Fours | 2V | boys | 2V | 2 | 5:21.0 | 7.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7697717) |
| 2015-05-09 | The Davison Cup- Boys Fours | Novice | boys | Novice | 4 | 6:52.4 | 28.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7697717) |
| 2015-05-09 | The Davison Cup- Boys Fours | Varsity Four | boys | 1V | 1 | 5:15.3 | 5.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7697717) |
| 2015-05-13 | Cambridge Rindge and Latin School  vs. Newto | 3V 4+ | UNKNOWN | 3V | 1 | 5:54.27 | 15.44s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3576885) |
| 2015-05-13 | Cambridge Rindge and Latin School  vs. Newto | 4V 4+ | UNKNOWN | 4V | 1 | 5:55 | 16.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3576885) |
| 2015-05-16 | Northeast Youth Championships | Mens Youth 2nd 4+ Final | boys | 2V | 4 | 7:27.4 | 6.00s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Mens Youth 2nd 4+ Heat 2 | boys | 2V | 1 | 7:07.8 | 8.70s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Mens Youth 2nd 4+ Heat 3 | boys | 2V | 1 | 7:17.5 | 11.50s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Mens Youth 2nd 4+ Semifinal 2 | boys | 2V | 3 | 7:13.6 | 2.50s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Mens Youth 2nd 4+ Semifinal 2 | boys | 2V | 5 | 7:34.9 | 23.80s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Mens Youth 4+ Heat 3 | boys | 1V | 5 | 7:08.1 | 22.60s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Mens Youth 4+ Heat 4 | boys | 1V | 1 | 6:59.5 | 2.10s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Mens Youth 4+ Semifinal 2 | boys | 1V | 4 | 6:47.6 | 6.50s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Womens Youth 2nd 4+ Final | girls | 2V | 6 | 8:51.0 | 60.50s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Womens Youth 2nd 4+ Heat 3 | girls | 2V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Womens Youth 2nd 4+ Semifinal 1 | girls | 2V | 3 | 8:14.4 | 16.40s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Womens Youth 4+ Heat 1 | girls | 1V | 2 | 7:57.2 | 15.20s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Womens Youth 4+ Heat 2 | girls | 1V | 2 | 7:59.5 | 28.40s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Womens Youth 4+ Semifinal 1 | girls | 1V | 5 | 7:44.7 | 20.30s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Womens Youth 4+ Semifinal 2 | girls | 1V | 5 | 7:46.8 | 37.20s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-16 | Northeast Youth Championships | Womens Youth Ltwt 4+ Heat 2 | girls | 1V | 4 | 8:05.8 | 23.60s | [herenow](https://legacy.herenow.com/results/#/races/20143/results) |
| 2015-05-24 | MPSRA Spring Championship | Boy's 4th Varsity 4+ Final | boys | 4V | 1 | 5:15.9 | 8.30s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-24 | MPSRA Spring Championship | Boys 1st Novice 8+ Heat 2 | boys | 1st Novice | 5 | 6:08.5 | 70.10s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-24 | MPSRA Spring Championship | Boys 1st Varsity 4+ Grand Final | boys | 1V | 3 | 5:09.7 | 0.20s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-24 | MPSRA Spring Championship | Boys 1st Varsity 4+ Heat 3 | boys | 1V | 1 | 4:57.3 | 8.80s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-24 | MPSRA Spring Championship | Boys 2nd Varsity 4+ Final | boys | 2V | 1 | 5:14.8 | 0.50s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-24 | MPSRA Spring Championship | Boys 2nd Varsity 4+ Heat 3 | boys | 2V | 1 | 5:05.8 | 31.30s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-24 | MPSRA Spring Championship | Boys 3rd Varsity 4+ Final | boys | 3V | 1 | 5:29.2 | 2.80s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-24 | MPSRA Spring Championship | Boys 3rd Varsity 4+ Heat 2 | boys | 3V | 1 | 5:17.4 | 11.00s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-24 | MPSRA Spring Championship | Girls 1st Novice 8+ Heat 2 | girls | 1st Novice | 5 | 5:48.1 | 24.60s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-24 | MPSRA Spring Championship | Girls 1st Varsity 4+ Heat 3 | girls | 1V | 4 | 6:07.6 | 31.00s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-24 | MPSRA Spring Championship | Girls 1st Varsity 4+ Petite Final | girls | 1V | 1 | 5:54.5 | 12.00s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-24 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Final | girls | 2V | 2 | 5:49.1 | 4.70s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-24 | MPSRA Spring Championship | Girls 2nd Varsity 4+ Heat 1 | girls | 2V | 2 | 5:34.9 | 0.80s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-24 | MPSRA Spring Championship | Girls 3rd Varsity 4+ Final | girls | 3V | 1 | 5:40.8 | 7.30s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-24 | MPSRA Spring Championship | Girls 4th Varsity 4+ Final | girls | 4V | 1 | 6:10.3 | 16.70s | [herenow](https://legacy.herenow.com/results/#/races/20189/results) |
| 2015-05-30 | NEIRA Championship 2015 | boys 1V 4+ - Heat 1 | boys | 1V | 5 | 5:21.381 | 17.74s | [neira-championship-pdf](http://www.neirarowing.org/documents/2015NEIRAResults.pdf) |
| 2015-05-30 | NEIRA Championship 2015 | boys 2V 4+ - Heat 2 | boys | 2V | 4 | 5:18.632 | 15.19s | [neira-championship-pdf](http://www.neirarowing.org/documents/2015NEIRAResults.pdf) |
| 2015-05-30 | NEIRA Championship 2015 | girls 1V 4+ - Heat 2 | girls | 1V | 5 | 6:06.184 | 33.35s | [neira-championship-pdf](http://www.neirarowing.org/documents/2015NEIRAResults.pdf) |
| 2015-05-30 | NEIRA Championship 2015 | girls 2V 4+ - Heat 1 | girls | 2V | 4 | 5:56.720 | 11.84s | [neira-championship-pdf](http://www.neirarowing.org/documents/2015NEIRAResults.pdf) |
| 2015-05-30 | NEIRA Championship 2015 | girls 3V 4+ - Grand Final | girls | 3V | 5 | 5:59.753 | 13.24s | [neira-championship-pdf](http://www.neirarowing.org/documents/2015NEIRAResults.pdf) |
| 2015-05-30 | NEIRA Championship 2015 | girls 3V 4+ - Heat 2 | girls | 3V | 3 | 5:57.189 | 9.82s | [neira-championship-pdf](http://www.neirarowing.org/documents/2015NEIRAResults.pdf) |
| 2015-05-30 | NEIRA Championship 2015 | girls 4V 4+ - Grand Final | girls | 4V | 5 | 6:11.104 | 13.55s | [neira-championship-pdf](http://www.neirarowing.org/documents/2015NEIRAResults.pdf) |
| 2015-05-30 | NEIRA Championship 2015 | girls 4V 4+ - Heat 1 | girls | 4V | 1 | 6:03.297 | 0.12s | [neira-championship-pdf](http://www.neirarowing.org/documents/2015NEIRAResults.pdf) |
| 2015-09-19 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | 2 | 20:16.0 | 49.60s | [herenow](https://legacy.herenow.com/results/#/races/20161/results) |
| 2015-09-19 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | 6 | 21:33.7 | 127.30s | [herenow](https://legacy.herenow.com/results/#/races/20161/results) |
| 2015-09-19 | CRI Fall Classic | Mens Jr 4+ | boys | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20161/results) |
| 2015-09-19 | CRI Fall Classic | Womens Jr 4+ | girls | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20161/results) |
| 2015-10-11 | New England Jr/HS Championship | Mens 1st Varsity 4+ | boys | 1V | 6 | 15:16.7 | 38.40s | [herenow](https://legacy.herenow.com/results/#/races/20196/results) |
| 2015-10-11 | New England Jr/HS Championship | Mens 2nd Varsity 4+ | boys | 2V | 1 | 15:23.2 | 40.40s | [herenow](https://legacy.herenow.com/results/#/races/20196/results) |
| 2015-10-11 | New England Jr/HS Championship | Mens 3rd/4th Varsity 4+ | boys | 4V | 1 | 16:01.3 | 7.60s | [herenow](https://legacy.herenow.com/results/#/races/20196/results) |
| 2015-10-11 | New England Jr/HS Championship | Mens 3rd/4th Varsity 4+ | boys | 4V | 2 | 16:08.9 | 7.60s | [herenow](https://legacy.herenow.com/results/#/races/20196/results) |
| 2015-10-11 | New England Jr/HS Championship | Mens Jr/HS 1st Novice 4+ | boys | 1st Novice | 13 | 19:14.6 | 422.30s | [herenow](https://legacy.herenow.com/results/#/races/20196/results) |
| 2015-10-11 | New England Jr/HS Championship | Mens Jr/HS 1st Novice 8+ | boys | 1st Novice | 19 | 15:08.9 | 229.50s | [herenow](https://legacy.herenow.com/results/#/races/20196/results) |
| 2015-10-11 | New England Jr/HS Championship | Womens 1st Varsity 4+ | girls | 1V | 5 | 16:54.4 | 35.30s | [herenow](https://legacy.herenow.com/results/#/races/20196/results) |
| 2015-10-11 | New England Jr/HS Championship | Womens 2nd Varsity 4+ | girls | 2V | 1 | 17:20.4 | 2.10s | [herenow](https://legacy.herenow.com/results/#/races/20196/results) |
| 2015-10-11 | New England Jr/HS Championship | Womens 3rd/4th Varsity 4+ | girls | 4V | 1 | 17:53.3 | 1.40s | [herenow](https://legacy.herenow.com/results/#/races/20196/results) |
| 2015-10-11 | New England Jr/HS Championship | Womens Jr/HS 1st Novice 4+ | girls | 1st Novice | 3 | 14:31.0 | 36.50s | [herenow](https://legacy.herenow.com/results/#/races/20196/results) |
| 2015-10-11 | New England Jr/HS Championship | Womens Jr/HS 1st Novice 8+ | girls | 1st Novice | 15 | 15:26.8 | 194.50s | [herenow](https://legacy.herenow.com/results/#/races/20196/results) |
| 2015-10-25 | MPSRA Fall Championship | Boys 1st Novice 8+ | boys | 1st Novice | 6 | 15:54.3 | 133.10s | [herenow](https://legacy.herenow.com/results/#/races/20208/results) |
| 2015-10-25 | MPSRA Fall Championship | Boys 1st Varsity 4+ | boys | 1V | 1 | 13:52.5 | 13.00s | [herenow](https://legacy.herenow.com/results/#/races/20208/results) |
| 2015-10-25 | MPSRA Fall Championship | Boys 2nd Varsity 4+ | boys | 2V | 1 | 14:21.2 | 36.30s | [herenow](https://legacy.herenow.com/results/#/races/20208/results) |
| 2015-10-25 | MPSRA Fall Championship | Boys 3rd/4th Varsity 4+ | boys | 4V | 1 | 14:05.6 | 66.10s | [herenow](https://legacy.herenow.com/results/#/races/20208/results) |
| 2015-10-25 | MPSRA Fall Championship | Boys 3rd/4th Varsity 4+ | boys | 4V | 2 | 15:11.7 | 66.10s | [herenow](https://legacy.herenow.com/results/#/races/20208/results) |
| 2015-10-25 | MPSRA Fall Championship | Boys Novice 4+ | boys | Novice | 4 | 17:15.7 | 105.50s | [herenow](https://legacy.herenow.com/results/#/races/20208/results) |
| 2015-10-25 | MPSRA Fall Championship | Girls 1st Novice 8+ | girls | 1st Novice | 7 | 19:39.6 | 280.70s | [herenow](https://legacy.herenow.com/results/#/races/20208/results) |
| 2015-10-25 | MPSRA Fall Championship | Girls 1st Varsity 4+ | girls | 1V | 3 | 15:18.4 | 11.60s | [herenow](https://legacy.herenow.com/results/#/races/20208/results) |
| 2015-10-25 | MPSRA Fall Championship | Girls 2nd Varsity 4+ | girls | 2V | 1 | 15:48.7 | 9.60s | [herenow](https://legacy.herenow.com/results/#/races/20208/results) |
| 2015-10-25 | MPSRA Fall Championship | Girls 3rd/4th Varsity 4+ | girls | 4V | 1 | 16:25.8 | 5.10s | [herenow](https://legacy.herenow.com/results/#/races/20208/results) |
| 2015-10-25 | MPSRA Fall Championship | Girls 3rd/4th Varsity 4+ | girls | 4V | 4 | 17:31.4 | 65.60s | [herenow](https://legacy.herenow.com/results/#/races/20208/results) |
| 2015-10-25 | MPSRA Fall Championship | Girls Novice 4+ | girls | Novice | 1 | 17:41.4 | 33.40s | [herenow](https://legacy.herenow.com/results/#/races/20208/results) |
| 2015-10-31 | South Shore Invitational Novice Challenge | Mens Junior Novice 4+ | boys | Novice | 3 | 14:01.3 | 13.20s | [herenow](https://legacy.herenow.com/results/#/races/20213/results) |
| 2015-10-31 | South Shore Invitational Novice Challenge | Mens Junior Novice 8+ | boys | Novice | 3 | 16:25.6 | 132.70s | [herenow](https://legacy.herenow.com/results/#/races/20213/results) |
| 2015-10-31 | South Shore Invitational Novice Challenge | Womens Junior Novice 4+ | girls | Novice | 2 | 16:21.9 | 73.40s | [herenow](https://legacy.herenow.com/results/#/races/20213/results) |
| 2015-10-31 | South Shore Invitational Novice Challenge | Womens Junior Novice 8+ | girls | Novice | 3 | 11:47.3 | 84.10s | [herenow](https://legacy.herenow.com/results/#/races/20213/results) |

### 2014 (28 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2014-04-05 | Boys Fours, Mayor's Cup Regatta: Buckingham, | 2V Four | boys | 2V | 1 | 4:17 | 7.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8350810) |
| 2014-04-05 | Boys Fours, Mayor's Cup Regatta: Buckingham, | Varsity Four | boys | 1V | 1 | 4:04 | 8.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8350810) |
| 2014-04-05 | Varsity Girls Fours, Mayors Cup: Buckingham, | Girls 1V Fours | girls | 1V | 2 | 4:48.8 | 8.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8145544) |
| 2014-04-05 | Varsity Girls Fours, Mayors Cup: Buckingham, | Girls 2V fours | girls | 2V | 2 | 4:57.1 | 15.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8145544) |
| 2014-04-13 | FOURS: Bancroft School vs. Canterbury, CRLS, | 1G4 | girls | 1V | 2 | 6:12.69 | 10.56s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5646423) |
| 2014-04-13 | FOURS: Bancroft School vs. Canterbury, CRLS, | 2B4 | boys | 2V | 1 | 5:38.56 | 2.43s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5646423) |
| 2014-04-13 | FOURS: Bancroft School vs. Canterbury, CRLS, | 2G4 | girls | 2V | 1 | 6:28.86 | 0.24s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5646423) |
| 2014-04-13 | FOURS: Bancroft School vs. Canterbury, CRLS, | 3B4 | boys | 3V | 3 | 7:34.54 | 29.68s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5646423) |
| 2014-04-13 | FOURS: Bancroft School vs. Canterbury, CRLS, | 3B4 | boys | 3V | 4 | 7:56.79 | 51.93s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5646423) |
| 2014-04-13 | FOURS: Bancroft School vs. Canterbury, CRLS, | Varsity Four | UNKNOWN | 1V | 2 | 5:21.67 | 7.23s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5646423) |
| 2014-04-23 | Belmont Hill vs. Middlesex, CRLS  Boys Fours | 2V4 | boys | UNKNOWN | 3 | 4:26.8 | 27.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6284452) |
| 2014-04-23 | Belmont Hill vs. Middlesex, CRLS  Boys Fours | 3V4 | boys | UNKNOWN | 3 | 4:50.2 | 46.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6284452) |
| 2014-04-23 | Belmont Hill vs. Middlesex, CRLS  Boys Fours | Varsity Four | boys | 1V | 3 | 4:13.7 | 20.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6284452) |
| 2014-05-17 | Northeast Youth Championship | Mens Youth 2- Heat 1 | boys | 1V | 5 | 7:41.0 | 50.10s | [herenow](https://legacy.herenow.com/results/#/races/10086/results) |
| 2014-05-17 | Northeast Youth Championship | Mens Youth 4+ Heat 1<br>No Time Taken | boys | 1V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/10086/results) |
| 2014-05-17 | Northeast Youth Championship | Mens Youth Ltwt 4+ Final | boys | 1V | 4 | 6:34.3 | 10.70s | [herenow](https://legacy.herenow.com/results/#/races/10086/results) |
| 2014-05-17 | Northeast Youth Championship | Mens Youth Ltwt 4+ Heat 2 | boys | 1V | 3 | 6:38.9 | 9.50s | [herenow](https://legacy.herenow.com/results/#/races/10086/results) |
| 2014-05-17 | Northeast Youth Championship | Womens Youth 2x Heat 3 | girls | 1V | 2 | 7:51.6 | 5.10s | [herenow](https://legacy.herenow.com/results/#/races/10086/results) |
| 2014-05-17 | Northeast Youth Championship | Womens Youth 2x Semi 1 | girls | 1V | 4 | 7:46.7 | 23.30s | [herenow](https://legacy.herenow.com/results/#/races/10086/results) |
| 2014-05-17 | Northeast Youth Championship | Womens Youth 4+ Heat 2 | girls | 1V | 4 | 7:26.6 | 21.30s | [herenow](https://legacy.herenow.com/results/#/races/10086/results) |
| 2014-05-17 | Northeast Youth Championship | Womens Youth 4+ Semi 1 | girls | 1V | 6 | 7:29.6 | 28.60s | [herenow](https://legacy.herenow.com/results/#/races/10086/results) |
| 2014-05-17 | Northeast Youth Championship | Womens Youth Ltwt 2x Heat 2 | girls | 1V | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/10086/results) |
| 2014-09-14 | CRI Rumble on the River | Mens Jr 4+ | boys | UNKNOWN | 2 | 20:40.2 | 35.50s | [herenow](https://legacy.herenow.com/results/#/races/20111/results) |
| 2014-09-14 | CRI Rumble on the River | Mens Jr 4+ | boys | UNKNOWN | 4 | 23:36.6 | 211.90s | [herenow](https://legacy.herenow.com/results/#/races/20111/results) |
| 2014-09-14 | CRI Rumble on the River | Mens Jr 4+ | boys | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/20111/results) |
| 2014-09-14 | CRI Rumble on the River | Womens Jr 4+ | girls | UNKNOWN | 1 | 22:54.0 | 135.40s | [herenow](https://legacy.herenow.com/results/#/races/20111/results) |
| 2014-09-14 | CRI Rumble on the River | Womens Jr 4+ | girls | UNKNOWN | 2 | 25:09.4 | 135.40s | [herenow](https://legacy.herenow.com/results/#/races/20111/results) |
| 2014-09-14 | CRI Rumble on the River | Womens Jr 8+ | girls | UNKNOWN | 7 | 24:43.8 | 286.20s | [herenow](https://legacy.herenow.com/results/#/races/20111/results) |

### 2013 (27 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2013-04-14 | Fours: Bancroft School vs. CRLS, Canterbury, | 1G4 | girls | 1V | 1 | 05:05.0 | 19.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9448885) |
| 2013-04-14 | Fours: Bancroft School vs. CRLS, Canterbury, | 2B4 | boys | 2V | 3 | 05:45.2 | 11.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9448885) |
| 2013-04-14 | Fours: Bancroft School vs. CRLS, Canterbury, | 2G4 | girls | 2V | 1 | 06:09.8 | 28.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9448885) |
| 2013-04-14 | Fours: Bancroft School vs. CRLS, Canterbury, | 3B4 | boys | 3V | 2 | 06:28.1 | 12.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9448885) |
| 2013-04-14 | Fours: Bancroft School vs. CRLS, Canterbury, | 3G4 | girls | 3V | 2 | 06:23.6 | 1.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9448885) |
| 2013-04-14 | Fours: Bancroft School vs. CRLS, Canterbury, | Varsity Four | UNKNOWN | 1V | 2 | 04:58.4 | 6.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9448885) |
| 2013-05-01 | Girls' Fours: Newton Country Day School vs.  | 2nd Four | girls | 2V | 2 | 5:21.9 | 5.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4239886) |
| 2013-05-01 | Girls' Fours: Newton Country Day School vs.  | 3rd Four | girls | 3V | 2 | 5:41.08 | 13.28s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4239886) |
| 2013-05-01 | Girls' Fours: Newton Country Day School vs.  | 4th Four | girls | 4V | 2 | 6:00.94 | 23.01s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4239886) |
| 2013-05-01 | Girls' Fours: Newton Country Day School vs.  | Varsity Four | girls | 1V | 2 | 5:18.0 | 16.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4239886) |
| 2013-05-12 | The Davison Cup | 2nd Girls 4 | girls | UNKNOWN | 1 | 6:44.54 | 13.49s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6248266) |
| 2013-05-12 | The Davison Cup | 3rd Girls 4 | girls | UNKNOWN | 1 | 6:34.01 | 45.42s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6248266) |
| 2013-05-12 | The Davison Cup | Novice Girls 4 | girls | Novice | 1 | 6:47.18 | 18.89s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6248266) |
| 2013-05-12 | The Davison Cup | Varsity Four | UNKNOWN | 1V | 1 | 6:20.03 | 18.54s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6248266) |
| 2013-05-12 | The Davison Cup- Boys Fours | Boys 2nd 4 | boys | 2V | 2 | 6:23.65 | 3.42s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3437410) |
| 2013-05-12 | The Davison Cup- Boys Fours | Boys 3rd 4 | boys | 3V | 3 | 7:14.32 | 24.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3437410) |
| 2013-05-12 | The Davison Cup- Boys Fours | Boys Novice 4 | boys | Novice | 2 | 6:07.39 | 9.69s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3437410) |
| 2013-05-12 | The Davison Cup- Boys Fours | Varsity Four | boys | 1V | 2 | 5:49.72 | 7.57s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3437410) |
| 2013-05-18 | Girl's 4s: Winsor School vs. Lincoln/CRLS | 2nd Four | girls | 2V | 2 | 4:46.5 | 12.34s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5254639) |
| 2013-05-18 | Girl's 4s: Winsor School vs. Lincoln/CRLS | 3rd Four | girls | 3V | 2 | 4:53 | 11.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5254639) |
| 2013-05-18 | Girl's 4s: Winsor School vs. Lincoln/CRLS | 4th Four | girls | 4V | 2 | 5:17 | 24.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5254639) |
| 2013-05-18 | Girl's 4s: Winsor School vs. Lincoln/CRLS | Varsity Four | girls | 1V | 2 | 4:36.7 | 5.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5254639) |
| 2013-05-18 | NEIRA Championship 2013 | boys 1V 4+ - Heat 2 | boys | 1V | 6 | 5:17.561 | 20.91s | [neira-championship-pdf](http://www.neirarowing.org/documents/2013NEIRA_Results.pdf) |
| 2013-05-18 | NEIRA Championship 2013 | girls 1V 4+ - Heat 1 | girls | 1V | 4 | 5:44.020 | 14.95s | [neira-championship-pdf](http://www.neirarowing.org/documents/2013NEIRA_Results.pdf) |
| 2013-05-18 | NEIRA Championship 2013 | girls 2V 4+ - Heat 3 | girls | 2V | 4 | 5:54.618 | 16.08s | [neira-championship-pdf](http://www.neirarowing.org/documents/2013NEIRA_Results.pdf) |
| 2013-05-18 | NEIRA Championship 2013 | girls 2V 8+ - Grand Final | girls | 2V | 6 | 5:49.690 | 39.63s | [neira-championship-pdf](http://www.neirarowing.org/documents/2013NEIRA_Results.pdf) |
| 2013-05-18 | NEIRA Championship 2013 | girls 3V 4+ - Heat 1 | girls | 3V | 6 | 6:02.904 | 18.70s | [neira-championship-pdf](http://www.neirarowing.org/documents/2013NEIRA_Results.pdf) |

### 2012 (41 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2012-04-07 | Mayor's Cup - Varsity Girls Fours: Buckingha | 2V Girls | girls | 2V | 2 | 5:08 | 15.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=211027) |
| 2012-04-07 | Mayor's Cup - Varsity Girls Fours: Buckingha | 3v Girls | girls | 3V | 2 | 5:05 | 15.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=211027) |
| 2012-04-07 | Mayor's Cup - Varsity Girls Fours: Buckingha | 4V Girls | girls | 4V | 2 | 5:50 | 49.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=211027) |
| 2012-04-07 | Mayor's Cup -- Boys Varsity Fours: Buckingha | 2nd Four | boys | 2V | 2 | 4:27.7 | 14.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2005895) |
| 2012-04-07 | Mayor's Cup -- Boys Varsity Fours: Buckingha | 3rd Four | boys | 3V | 2 | 4:22.7 | 9.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2005895) |
| 2012-04-07 | Mayor's Cup -- Boys Varsity Fours: Buckingha | 4th Four | boys | 4V | 2 | 5:05.4 | 39.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2005895) |
| 2012-04-07 | Mayor's Cup -- Boys Varsity Fours: Buckingha | Varsity Four | boys | 1V | 2 | 4:27.7 | 15.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2005895) |
| 2012-04-14 | Cambridge Rindge & Latin School Girls  vs. T | 2nd Varsity 4+ | girls | 2V | 1 | 4:30 | 22.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9882077) |
| 2012-04-14 | Cambridge Rindge & Latin School Girls  vs. T | Varsity Four | girls | 1V | 1 | 4:21 | 6.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9882077) |
| 2012-04-14 | Fours: Cambridge Rindge & Latin School vs. T | Varsity 4 (Exhibition) | UNKNOWN | 1V | 1 | 4:22.3 | 18.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9909002) |
| 2012-04-14 | Fours: Cambridge Rindge & Latin School vs. T | Varsity 4 (Exhibition) | UNKNOWN | 2V | 2 | 4:41.0 | 18.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9909002) |
| 2012-04-14 | Fours: Cambridge Rindge & Latin School vs. T | Varsity Four | UNKNOWN | 1V | 1 | 4:12.6 | 24.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9909002) |
| 2012-04-14 | Fours: Cambridge Rindge & Latin School vs. T | Varsity Four | UNKNOWN | 2V | 3 | 4:39.2 | 26.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9909002) |
| 2012-04-15 | Fours: Bancroft School vs. Canterbury, CRLS, | 1G4 | girls | 1V | 1 | 6:26.7 | 16.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4488928) |
| 2012-04-15 | Fours: Bancroft School vs. Canterbury, CRLS, | 2B4 | boys | 2V | 1 | 6:02.1 | 15.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4488928) |
| 2012-04-15 | Fours: Bancroft School vs. Canterbury, CRLS, | 2G4 | girls | 2V | 1 | 7:07.8 | 7.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4488928) |
| 2012-04-15 | Fours: Bancroft School vs. Canterbury, CRLS, | 3B4 | boys | 3V | 1 | 6:04.0 | 53.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4488928) |
| 2012-04-15 | Fours: Bancroft School vs. Canterbury, CRLS, | 3B4 | boys | 3V | 2 | 6:57.0 | 53.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4488928) |
| 2012-04-15 | Fours: Bancroft School vs. Canterbury, CRLS, | 3G4 | girls | 3V | 1 | 6:44.1 | 57.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4488928) |
| 2012-04-15 | Fours: Bancroft School vs. Canterbury, CRLS, | 3G4 | girls | 3V | 2 | 7:41.6 | 57.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4488928) |
| 2012-04-15 | Fours: Bancroft School vs. Canterbury, CRLS, | Varsity Four | UNKNOWN | 1V | 1 | 5:21.9 | 0.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4488928) |
| 2012-04-25 | Belmont Hill  vs. CRLS & CRI | 2ND 4 | UNKNOWN | 2V | 2 | 4:35.5 | 31.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5037659) |
| 2012-04-25 | Belmont Hill  vs. CRLS & CRI | 3RD 4 | UNKNOWN | 3V | 2 | 4:32.8 | 25.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5037659) |
| 2012-04-25 | Belmont Hill  vs. CRLS & CRI | 4th 4 | UNKNOWN | 4V | 2 | 5:21.0 | 54.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5037659) |
| 2012-04-25 | Belmont Hill  vs. CRLS & CRI | Varsity Four | UNKNOWN | 1V | 2 | 4:14.4 | 20.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5037659) |
| 2012-05-09 | Girls' Fours: Newton Country Day School vs.  | 2nd Varsity Four | girls | 2V | 1 | 4:54.31 | 2.71s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3246919) |
| 2012-05-09 | Girls' Fours: Newton Country Day School vs.  | 3rd Varsity Four | girls | 3V | 2 | 5:31.65 | 31.76s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3246919) |
| 2012-05-09 | Girls' Fours: Newton Country Day School vs.  | 4th Varsity Four | girls | 4V | 2 | 5:49.79 | 21.74s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3246919) |
| 2012-05-09 | Girls' Fours: Newton Country Day School vs.  | Varsity Four | girls | 1V | 2 | 4:58.75 | 14.25s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3246919) |
| 2012-05-12 | Davison Cup -Girls fours | Girls 2V fours | girls | 2V | 1 | 5:01.5 | 13.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8540413) |
| 2012-05-12 | Davison Cup -Girls fours | Girls 3V fours | girls | 3V | 1 | 5:21.8 | 9.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8540413) |
| 2012-05-12 | Davison Cup -Girls fours | Girls 4V fours | girls | 4V | 1 | 5:22.8 | 4.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8540413) |
| 2012-05-12 | Davison Cup -Girls fours | Girls 5V fours | girls | 5V | 1 | 5:57.7 | 15.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8540413) |
| 2012-05-12 | Davison Cup -Girls fours | Varsity Four | girls | 1V | 1 | 4:50.4 | 10.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8540413) |
| 2012-05-12 | Davison Cup- Boys fours | Boys 2V fours | boys | 2V | 1 | 4:44.6 | 4.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5110980) |
| 2012-05-12 | Davison Cup- Boys fours | Boys 3V fours | boys | 3V | 1 | 4:56.6 | 16.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5110980) |
| 2012-05-12 | Davison Cup- Boys fours | Boys 3V fours | boys | 3V | 2 | 5:13.3 | 16.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5110980) |
| 2012-05-12 | Davison Cup- Boys fours | Varsity Four | boys | 1V | 1 | 4:27.4 | 2.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5110980) |
| 2012-05-19 | NEIRA Championship 2012 | boys 1V 4+ - Heat 1 | boys | 1V | 5 | 5:13.437 | 12.69s | [neira-championship-pdf](http://www.neirarowing.org/documents/2012NEIRA.pdf) |
| 2012-05-19 | NEIRA Championship 2012 | boys 2V 4+ - Heat 3 | boys | 2V | 5 | 5:35.125 | 22.11s | [neira-championship-pdf](http://www.neirarowing.org/documents/2012NEIRA.pdf) |
| 2012-05-19 | NEIRA Championship 2012 | girls 2V 4+ - Heat 1 | girls | 2V | 3 | 6:04.266 | 15.44s | [neira-championship-pdf](http://www.neirarowing.org/documents/2012NEIRA.pdf) |

### 2011 (37 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2011-04-09 | Cambridge Mayor's Cup: Cambridge Rindge & La | 2nd Boat | girls | 2V | 2 | 5:03.6 | 0.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1350472) |
| 2011-04-09 | Cambridge Mayor's Cup: Cambridge Rindge & La | 3rd Boat | girls | 3V | 2 | 5:09 | 5.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1350472) |
| 2011-04-09 | Cambridge Mayor's Cup: Cambridge Rindge & La | Varsity Four | girls | 1V | 2 | 4:45.7 | 4.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1350472) |
| 2011-04-09 | Mayor's Cup (Fours): Cambridge Rindge & Lati | 2nd Varsity Four | UNKNOWN | 2V | 1 | 4:32.9 | 5.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9992737) |
| 2011-04-09 | Mayor's Cup (Fours): Cambridge Rindge & Lati | 3rd Varsity Four | UNKNOWN | 3V | 3 | 4:51.6 | 16.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9992737) |
| 2011-04-09 | Mayor's Cup (Fours): Cambridge Rindge & Lati | Varsity Four | UNKNOWN | 1V | 1 | 4:13.8 | 2.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9992737) |
| 2011-04-13 | Cambridge Rindge & Latin School Girls vs. Ne | 2nd Four | girls | 2V | 1 | 4:49.2 | 4.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9404329) |
| 2011-04-13 | Cambridge Rindge & Latin School Girls vs. Ne | 3rd Four | girls | 3V | 2 | 4:58.3 | 5.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9404329) |
| 2011-04-13 | Cambridge Rindge & Latin School Girls vs. Ne | Varsity Four | girls | 1V | 1 | 4:42.2 | 5.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9404329) |
| 2011-04-16 | Fours: Bancroft School vs. So. Kent, Canterb | 1G4 | girls | 1V | 1 | 6:11.3 | 28.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1011233) |
| 2011-04-16 | Fours: Bancroft School vs. So. Kent, Canterb | 2B4 | boys | 2V | 1 | 5:57.3 | 4.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1011233) |
| 2011-04-16 | Fours: Bancroft School vs. So. Kent, Canterb | 2G4 | girls | 2V | 1 | 6:07.4 | 5.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1011233) |
| 2011-04-16 | Fours: Bancroft School vs. So. Kent, Canterb | 2G4 | girls | 2V | 2 | 6:13.3 | 5.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1011233) |
| 2011-04-16 | Fours: Bancroft School vs. So. Kent, Canterb | 3B4 | boys | 3V | 1 | 6:10.1 | 30.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1011233) |
| 2011-04-16 | Fours: Bancroft School vs. So. Kent, Canterb | Varsity Four | UNKNOWN | 1V | 1 | 5:28.5 | 21.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1011233) |
| 2011-04-23 | CRLS vs. Thayer Academy | Boys 1st Four | boys | 1V | 1 | 4:08.8 | 13.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5078471) |
| 2011-04-23 | CRLS vs. Thayer Academy | Boys 1st Four | boys | 1V | 3 | 4:35.3 | 26.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5078471) |
| 2011-04-23 | CRLS vs. Thayer Academy | Girls 1st Four | girls | 1V | 1 | 4:45.3 | 19.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5078471) |
| 2011-04-27 | Belmont Hill  vs. CRLS & CRI | 2V | UNKNOWN | 2V | 3 | 5:07.8 | 42.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8753573) |
| 2011-04-27 | Belmont Hill  vs. CRLS & CRI | 3V/4V | UNKNOWN | 3V | 3 | 5:07.7 | 43.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8753573) |
| 2011-04-27 | Belmont Hill  vs. CRLS & CRI | Varsity Four | UNKNOWN | 1V | 2 | 4:24.3 | 5.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8753573) |
| 2011-05-18 | Cambridge Rindge & Latin School vs. Winsor S | 2nd 4+ | UNKNOWN | 2V | 2 | 4:38.8 | 11.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9729182) |
| 2011-05-18 | Cambridge Rindge & Latin School vs. Winsor S | 3rd 4+ | UNKNOWN | 3V | 2 | 4:46 | 14.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9729182) |
| 2011-05-18 | Cambridge Rindge & Latin School vs. Winsor S | 4th 4+ | UNKNOWN | 4V | 2 | 5:39.2 | 60.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9729182) |
| 2011-05-18 | Cambridge Rindge & Latin School vs. Winsor S | Varsity Four | UNKNOWN | 1V | 2 | 4:26.2 | 4.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9729182) |
| 2011-05-21 | NEIRA Championship 2011 | boys 1V 4+ - Heat 2 | boys | 1V | 3 | 5:34.652 | 6.48s | [neira-championship-pdf](http://www.neirarowing.org/documents/2011NEIRA_Results.pdf) |
| 2011-05-21 | NEIRA Championship 2011 | boys 1V 4+ - Petite Final | boys | 1V | 4 | 6:02.854 | 10.03s | [neira-championship-pdf](http://www.neirarowing.org/documents/2011NEIRA_Results.pdf) |
| 2011-05-21 | NEIRA Championship 2011 | girls 1V 4+ - Heat 2 | girls | 1V | 4 | 6:07.918 | 15.17s | [neira-championship-pdf](http://www.neirarowing.org/documents/2011NEIRA_Results.pdf) |
| 2011-09-18 | CRI Rumble on the River | Junior Men's 2- | boys | UNKNOWN | 3 | 9:25.0 | 19.00s | [herenow](https://legacy.herenow.com/results/#/races/17/results) |
| 2011-09-18 | CRI Rumble on the River | Junior Men's 4+ | boys | UNKNOWN | 5 | 8:12.0 | 32.00s | [herenow](https://legacy.herenow.com/results/#/races/17/results) |
| 2011-09-18 | CRI Rumble on the River | Junior Men's 4+ | boys | UNKNOWN | 8 | 8:47.0 | 67.00s | [herenow](https://legacy.herenow.com/results/#/races/17/results) |
| 2011-09-18 | CRI Rumble on the River | Junior Men's 4+ Sprint | boys | UNKNOWN | 6 | 0:45.0 | 5.00s | [herenow](https://legacy.herenow.com/results/#/races/17/results) |
| 2011-09-18 | CRI Rumble on the River | Junior Men's 4+ Sprint | boys | UNKNOWN | UNKNOWN | UNKNOWN |  | [herenow](https://legacy.herenow.com/results/#/races/17/results) |
| 2011-09-18 | CRI Rumble on the River | Junior Women's 4+  | girls | UNKNOWN | 3 | 9:27.0 | 43.00s | [herenow](https://legacy.herenow.com/results/#/races/17/results) |
| 2011-09-18 | CRI Rumble on the River | Junior Women's 4+  | girls | UNKNOWN | 5 | 10:15.0 | 91.00s | [herenow](https://legacy.herenow.com/results/#/races/17/results) |
| 2011-09-18 | CRI Rumble on the River | Junior Women's 4+ Sprint | girls | UNKNOWN | 5 | 0:54.0 | 10.00s | [herenow](https://legacy.herenow.com/results/#/races/17/results) |
| 2011-09-18 | CRI Rumble on the River | Junior Women's 4+ Sprint | girls | UNKNOWN | 6 | 0:55.0 | 11.00s | [herenow](https://legacy.herenow.com/results/#/races/17/results) |

### 2010 (35 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2010-04-03 | Mayor's Cup: BB&N Girls vs. CRLS | 2nd Varsity Four | girls | 2V | 2 | 4:49 | 19.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7822042) |
| 2010-04-03 | Mayor's Cup: BB&N Girls vs. CRLS | 3rd Varsity Four | girls | 3V | 2 | 5:08 | 30.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7822042) |
| 2010-04-03 | Mayor's Cup: BB&N Girls vs. CRLS | 4th Varsity Fours | girls | 4V | 3 | 5:03 | 37.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7822042) |
| 2010-04-03 | Mayor's Cup: BB&N Girls vs. CRLS | Varsity Four | girls | 1V | 2 | 4:42 | 10.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7822042) |
| 2010-04-03 | Mayor's Cup: Buckingham, Browne & Nichols Sc | 2nd Fours | UNKNOWN | 2V | 2 | 4:22.1 | 1.78s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6738486) |
| 2010-04-03 | Mayor's Cup: Buckingham, Browne & Nichols Sc | 3rd Fours ( with BB&N 4th) | UNKNOWN | 3V | 3 | 4:36.9 | 20.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6738486) |
| 2010-04-03 | Mayor's Cup: Buckingham, Browne & Nichols Sc | Varsity Four | UNKNOWN | 1V | 2 | 4:11.3 | 9.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6738486) |
| 2010-04-07 | Cambridge Rindge & Latin School (girls) vs.  | 2nd Fours | girls | 2V | 1 | 4:56 | 2.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9655283) |
| 2010-04-07 | Cambridge Rindge & Latin School (girls) vs.  | 3rd Fours | girls | 3V | 1 | 5:10.1 | 12.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9655283) |
| 2010-04-07 | Cambridge Rindge & Latin School (girls) vs.  | 4th Fours | girls | 4V | 1 | 5:13.3 | 32.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9655283) |
| 2010-04-07 | Cambridge Rindge & Latin School (girls) vs.  | Varsity Four | girls | 1V | 1 | 4:46 | 11.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9655283) |
| 2010-04-21 | Belmont Hill School vs. CRLS, CRI | 2nd Boat | UNKNOWN | 2V | 3 | 4:46.9 | 36.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5716225) |
| 2010-04-21 | Belmont Hill School vs. CRLS, CRI | 3rd Boat | UNKNOWN | 3V | 2 | 5:37.7 | 56.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5716225) |
| 2010-04-21 | Belmont Hill School vs. CRLS, CRI | Varsity Four | UNKNOWN | 1V | 3 | 4:39.9 | 21.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=5716225) |
| 2010-04-24 | Cambridge, Rindge & Lation School vs. Thayer | 2nd Varsity Four | boys | 2V | 2 | 4:22.8 | 0.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8676092) |
| 2010-04-24 | Cambridge, Rindge & Lation School vs. Thayer | 3rd Varsity Four | boys | 3V | 2 | 4:57.8 | 21.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8676092) |
| 2010-04-24 | Cambridge, Rindge & Lation School vs. Thayer | Novice Four | girls | Novice | 1 | 5:20.0 | 16.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8676092) |
| 2010-04-24 | Cambridge, Rindge & Lation School vs. Thayer | Varsity Four | boys | 1V | 1 | 4:20.7 | 15.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8676092) |
| 2010-05-08 | Davison Cup | 1st Eight | girls | 1V | 1 | 4:49.3 | 26.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4945474) |
| 2010-05-08 | Davison Cup | 1st Eight | girls | 1V | 1 | 5:14.18 | 5.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4945474) |
| 2010-05-08 | Davison Cup | 1st Four | boys | 1V | 2 | 5:02.7 | 11.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4945474) |
| 2010-05-08 | Davison Cup | 3rd Four | boys | 3V | 2 | 5:34.8 | 15.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4945474) |
| 2010-05-08 | Davison Cup | 3rd Four | girls | 3V | 1 | 5:58.67 | 12.82s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4945474) |
| 2010-05-08 | Davison Cup | 4th Four | girls | 4V | 2 | 6:06.52 | 3.65s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4945474) |
| 2010-05-08 | Davison Cup | 4th Four and Novice | girls | Novice | 1 | 5:30 | 5.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4945474) |
| 2010-05-08 | Davison Cup | Other | girls | UNKNOWN | 1 | 5:43.05 | 0.75s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4945474) |
| 2010-05-08 | Davison Cup | Other | girls | UNKNOWN | 1 | 5:35.85 | 11.93s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4945474) |
| 2010-05-12 | Winsor vs. Cambridge Rindge & Latin | 2nd Four | UNKNOWN | 2V | 2 | 4:50 | 15.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1764718) |
| 2010-05-12 | Winsor vs. Cambridge Rindge & Latin | 3rd Four | UNKNOWN | 3V | 2 | 5:10 | 28.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1764718) |
| 2010-05-12 | Winsor vs. Cambridge Rindge & Latin | 4th Four | UNKNOWN | 4V | 2 | 5:30 | 36.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1764718) |
| 2010-05-12 | Winsor vs. Cambridge Rindge & Latin | Varsity Four | UNKNOWN | 1V | 2 | 4:39 | 16.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=1764718) |
| 2010-05-15 | Middlesex vs. Pomfret & CRLS | 3rd Fours | girls | 3V | 2 | 7:26.4 | 41.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8413145) |
| 2010-05-15 | Middlesex vs. Pomfret & CRLS | 4th Fours | girls | 4V | 2 | 7:53.0 | 51.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8413145) |
| 2010-05-15 | Middlesex vs. Pomfret & CRLS | Other | girls | UNKNOWN | 3 | 7:06.1 | 38.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8413145) |
| 2010-05-15 | Middlesex vs. Pomfret & CRLS | Other | girls | UNKNOWN | 3 | 6:42.5 | 12.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8413145) |

### 2009 (24 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2009-04-04 | 2009 Mayors Cup: BB&N Boys Fours vs. CRLS Bo | 2nd Fours | boys | 2V | 2 | 4:51.07 | 6.33s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8753667) |
| 2009-04-04 | 2009 Mayors Cup: BB&N Boys Fours vs. CRLS Bo | 3rd Fours | boys | 3V | 1 | 5:17.15 | 15.42s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8753667) |
| 2009-04-04 | 2009 Mayors Cup: BB&N Boys Fours vs. CRLS Bo | Varsity Four | boys | 1V | 2 | 4:58.82 | 28.86s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8753667) |
| 2009-04-04 | BB&N Girls vs. CRLS | Fourth Varsity Four | girls | 4V | 2 | 6:12.5 | 66.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8426067) |
| 2009-04-04 | BB&N Girls vs. CRLS | Second Varisty Four | girls | UNKNOWN | 2 | 5:11.1 | 17.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8426067) |
| 2009-04-04 | BB&N Girls vs. CRLS | Varsity Four | girls | 1V | 2 | 5:12.2 | 24.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=8426067) |
| 2009-05-02 | Middlesex School Boys Fours vs. BB&N and Cam | Second Four | boys | 2V | 3 | 7:01.3 | 107.30s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3428238) |
| 2009-05-02 | Middlesex School Boys Fours vs. BB&N and Cam | Third Four | boys | 3V | 3 | 5:34.6 | 17.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3428238) |
| 2009-05-02 | Middlesex School Boys Fours vs. BB&N and Cam | Varsity Four | boys | 1V | 3 | 5:19.3 | 24.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3428238) |
| 2009-05-02 | Middlesex School Girls Fours vs. BBN and Cam | Fourth Boats | girls | UNKNOWN | 3 | 6:27.1 | 38.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6231134) |
| 2009-05-02 | Middlesex School Girls Fours vs. BBN and Cam | Second Boat | girls | 2V | 3 | 5:59.5 | 21.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6231134) |
| 2009-05-02 | Middlesex School Girls Fours vs. BBN and Cam | Third Boats | girls | UNKNOWN | 3 | 6:04.4 | 29.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6231134) |
| 2009-05-02 | Middlesex School Girls Fours vs. BBN and Cam | Varsity Four | girls | 1V | 3 | 5:50.6 | 20.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=6231134) |
| 2009-05-09 | Davison Cup : Derryfield School vs. Brewster | 1st Four | boys | 1V | 3 | 5:24.2 | 26.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9903554) |
| 2009-05-09 | Davison Cup : Derryfield School vs. Brewster | 2nd Four | boys | 2V | 3 | 5:25.6 | 17.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9903554) |
| 2009-05-09 | Davison Cup : Derryfield School vs. Brewster | 3rd Boat | girls | 3V | 1 | 5:59.5 | 11.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9903554) |
| 2009-05-09 | Davison Cup : Derryfield School vs. Brewster | 3rd Four | boys | 3V | 2 | 5:57 | 20.50s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9903554) |
| 2009-05-09 | Davison Cup : Derryfield School vs. Brewster | 4th Boat/Novice | girls | Novice | 1 | 5:53.5 | 9.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9903554) |
| 2009-05-09 | Davison Cup : Derryfield School vs. Brewster | Other | girls | UNKNOWN | 3 | 5:56.0 | 12.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9903554) |
| 2009-05-09 | Davison Cup : Derryfield School vs. Brewster | Other | girls | UNKNOWN | 1 | 6:24.3 | 3.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9903554) |
| 2009-05-13 | The Winsor School vs. Cambridge Rindge and L | 2nd four | UNKNOWN | 2V | 2 | 5:49.9 | 24.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4665689) |
| 2009-05-13 | The Winsor School vs. Cambridge Rindge and L | 3rd four | UNKNOWN | 3V | 2 | 6:02.4 | 30.10s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4665689) |
| 2009-05-13 | The Winsor School vs. Cambridge Rindge and L | 4th four | UNKNOWN | 4V | 2 | 6:35.8 | 54.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4665689) |
| 2009-05-13 | The Winsor School vs. Cambridge Rindge and L | Varsity Four | UNKNOWN | 1V | 2 | 5:28.8 | 15.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4665689) |

### 2008 (16 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2008-04-05 | Cambridge Mayor's Cup - CRLS vs. BB&N (Girls | 2nd Four | girls | 2V | 2 | 4:56 | 2.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4933388) |
| 2008-04-05 | Cambridge Mayor's Cup - CRLS vs. BB&N (Girls | 3rd Four | girls | 3V | 2 | 5:06 | 20.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4933388) |
| 2008-04-05 | Cambridge Mayor's Cup - CRLS vs. BB&N (Girls | 4th Four | girls | 4V | 2 | 5:27 | 14.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4933388) |
| 2008-04-05 | Cambridge Mayor's Cup - CRLS vs. BB&N (Girls | Varsity Four | girls | 1V | 2 | 4:47 | 6.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=4933388) |
| 2008-04-05 | Cambridge Mayors Cup - CRLS v BB&N (Boys Fou | 2nd Fours | boys | 2V | 2 | 4:53.00 | 11.55s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3558769) |
| 2008-04-05 | Cambridge Mayors Cup - CRLS v BB&N (Boys Fou | Varsity Four | boys | 1V | 2 | 4:28.40 | 9.98s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=3558769) |
| 2008-05-03 | BB&N girls vs. Middlesex, CRLS | 2nd Varsity Four | girls | 2V | 3 | 5:02.5 | 31.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9361586) |
| 2008-05-03 | BB&N girls vs. Middlesex, CRLS | 3rd Varsity Four | girls | 3V | 3 | 5:24.0 | 40.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9361586) |
| 2008-05-03 | BB&N girls vs. Middlesex, CRLS | 4th Varsity Four | girls | 4V | 3 | 4:58.0 | 12.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9361586) |
| 2008-05-03 | BB&N girls vs. Middlesex, CRLS | Varsity Four | girls | 1V | 2 | 4:40.3 | 10.40s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9361586) |
| 2008-05-14 | Cambridge Rindge & Latin School vs. Winsor S | 2nd Four | UNKNOWN | 2V | 2 | 4:59 | 7.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2037302) |
| 2008-05-14 | Cambridge Rindge & Latin School vs. Winsor S | 3rd Four | UNKNOWN | 3V | 2 | 5:05.4 | 29.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2037302) |
| 2008-05-14 | Cambridge Rindge & Latin School vs. Winsor S | 4th Four | UNKNOWN | 4V | 2 | 5:13.1 | 9.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2037302) |
| 2008-05-14 | Cambridge Rindge & Latin School vs. Winsor S | Varsity Four | UNKNOWN | 1V | 2 | 4:58.6 | 7.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2037302) |
| 2008-05-17 | Belmont Hill School (5th/6th) vs. CRLS | Other | UNKNOWN | UNKNOWN | 2 | 4:07.6 | 1.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=917658) |
| 2008-05-17 | Belmont Hill School (5th/6th) vs. CRLS | Other | UNKNOWN | UNKNOWN | 2 | 4:34.2 | 18.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=917658) |

### 2007 (13 results)

| Date | Regatta | Event | Squad | Boat | Place | Time | Margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2007-04-07 | Cambridge Mayor's Cup: Cambridge Rindge & La | 2nd Four | girls | 2V | 2 | 4:48 | 9.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9376190) |
| 2007-04-07 | Cambridge Mayor's Cup: Cambridge Rindge & La | 3rd Four | girls | 3V | 2 | 5:04 | 18.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9376190) |
| 2007-04-07 | Cambridge Mayor's Cup: Cambridge Rindge & La | 4th Four | girls | 4V | 2 | 5:06 | 14.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9376190) |
| 2007-04-07 | Cambridge Mayor's Cup: Cambridge Rindge & La | Varsity Four | girls | 1V | 2 | 4:43 | 7.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=9376190) |
| 2007-04-07 | Cambridge Mayors Cup: BB&N Boys vs. CRLS Boy | Second Four | boys | 2V | 2 | 4:49.0 | 18.70s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7404922) |
| 2007-05-09 | Cambridge Rindge & Latin School Girls vs. Wi | 2nd boat | girls | 2V | 2 | 5:29.1 | 8.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7072913) |
| 2007-05-09 | Cambridge Rindge & Latin School Girls vs. Wi | 3rd boat | girls | 3V | 2 | 5:59.4 | 24.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7072913) |
| 2007-05-09 | Cambridge Rindge & Latin School Girls vs. Wi | 4th boat | girls | 4V | 2 | 5:45.1 | 8.80s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7072913) |
| 2007-05-09 | Cambridge Rindge & Latin School Girls vs. Wi | Varsity Four | girls | 1V | 2 | 5:20.3 | 11.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=7072913) |
| 2007-05-12 | Middlesex School Girls  vs. Bromfield, CRLS, | Second fours | girls | 2V | 4 | 5:41.6 | 19.90s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2130236) |
| 2007-05-12 | Middlesex School Girls  vs. Bromfield, CRLS, | Varsity Four | girls | 1V | 3 | 5:19.2 | 11.20s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2130236) |
| 2007-05-12 | Middlesex School Girls  vs. Bromfield, CRLS, | fourth fours | girls | 4V | 3 | 5:36.5 | 12.00s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2130236) |
| 2007-05-12 | Middlesex School Girls  vs. Bromfield, CRLS, | third four | girls | 3V | 4 | 5:49.5 | 32.60s | [row2k](https://www.row2k.com/results/resultspage.cfm?UID=2130236) |
