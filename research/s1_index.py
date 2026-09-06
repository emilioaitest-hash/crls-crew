#!/usr/bin/env python3
"""Step 1: pull row2k NEIRA index pages for all years, extract every regatta link."""
import re, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import fetch, strip_tags, has_crls

BASE = "https://www.row2k.com/results/"
YEARS = list(range(2026, 1996, -1))

# also pull the unfiltered high school index for MA in case NEIRA filter misses things
index_urls = []
for y in YEARS:
    index_urls.append((y, f"https://www.row2k.com/results/index.cfm?year={y}&league=NEIRA"))

regattas = {}   # uid -> dict
DATE_RE = re.compile(r"(?i)>\s*((?:Sun|Mon|Tues|Tue|Wednes|Wed|Thurs|Thu|Fri|Satur|Sat)[a-z]*day?,\s+\w+\s+\d{1,2},\s+\d{4})\s*<")
LINK_RE = re.compile(r'href="(resultspage\.cfm\?UID=([0-9A-Fa-f]+)[^"]*)"[^>]*>(.*?)</a>(.*?)(?=<li|</li|<ul|</ul|$)', re.S)

for y, url in index_urls:
    html = fetch(url)
    if not html or "resultspage" not in html:
        print(f"{y}: no data")
        continue
    # Split page by date headers so each regatta gets its date
    # find positions of date strings
    parts = []
    for m in re.finditer(r"(?i)((?:Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday),\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4})", html):
        parts.append((m.start(), m.group(1)))
    def date_for(pos):
        d = "UNKNOWN"
        for p, s in parts:
            if p <= pos:
                d = s
            else:
                break
        return d
    cnt = 0
    for m in re.finditer(r'href="(/results/resultspage\.cfm\?UID=([0-9A-Fa-f]+)[^"]*)"[^>]*>(.*?)</a>([^<]{0,200})', html, re.S):
        href, uid, title, tail = m.group(1), m.group(2), m.group(3), m.group(4)
        title = strip_tags(title).strip()
        venue = tail.replace(",", " ").strip()
        venue = re.sub(r"\s+", " ", venue).strip(" ,")
        d = date_for(m.start())
        if uid not in regattas:
            regattas[uid] = {"uid": uid, "year": y, "date_str": d, "title": title,
                             "venue": venue, "url": "https://www.row2k.com" + href.split("&cat")[0]}
            cnt += 1
    print(f"{y}: {cnt} regattas (total {len(regattas)})")

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "neira_index.json")
json.dump(list(regattas.values()), open(out, "w"), indent=1)
print("TOTAL", len(regattas), "->", out)
# how many mention CRLS in the title
t = [r for r in regattas.values() if has_crls(r["title"])]
print("Title mentions CRLS:", len(t))
for r in sorted(t, key=lambda x: (x["year"], x["date_str"])):
    print(" ", r["year"], r["date_str"], "|", r["title"][:100])
