#!/usr/bin/env python3
"""NEIRA championship PDF extraction with cross-strategy majority voting.

For each (event_code, round) block and each team within it, take the time
agreed by the MOST validated strategies. Cells without a strict majority are
dropped and reported, never guessed.
"""
import sys, os, re, json
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import neira_champ as NC
import neira_pdf_parse as N

CRLS = N.CRLS

STRATEGIES = [
    ("fixed", [(0, 232), (232, 486), (486, 10000)]),
    ("fixed", [(0, 240), (240, 495), (495, 10000)]),
    ("fixed", [(0, 236), (236, 490), (490, 10000)]),
    ("auto", 12), ("auto", 18), ("auto", 8), ("auto", 25),
]


def extract_year(path, year):
    # votes[(code,round)][team] = Counter(time)
    votes = defaultdict(lambda: defaultdict(Counter))
    orders = defaultdict(lambda: defaultdict(Counter))
    nstrat = 0
    for mode in STRATEGIES:
        try:
            bl = NC.parse_with(path, year, mode)
        except Exception:
            continue
        nstrat += 1
        seen_keys = set()
        for b in bl:
            if not NC.valid(b):
                continue
            k = (b["event_code"], b["round"])
            if k in seen_keys:
                continue          # duplicate block in same strategy -> ambiguous
            seen_keys.add(k)
            for e in b["entries"]:
                votes[k][e["entry"]][e["time"]] += 1
                orders[k][e["entry"]][e["order"]] += 1

    blocks = []
    dropped = []
    for k, teams in votes.items():
        entries = []
        for team, c in teams.items():
            (t, n), = c.most_common(1)
            total = sum(c.values())
            if n * 2 <= total:            # no strict majority
                dropped.append((year, k, team, dict(c)))
                continue
            (o, _), = orders[k][team].most_common(1)
            if o is None:                 # no usable Order value -> unusable row
                dropped.append((year, k, team, {"reason": "no order"}))
                continue
            entries.append({"entry": team, "time": t, "order": o, "votes": n, "total": total})
        if len(entries) < 2:
            continue
        entries.sort(key=lambda e: e["order"])
        for e in entries:
            e["place"] = e["order"]        # place is the source's own Order column
        seq = [e["order"] for e in entries]
        partial = seq != list(range(1, len(seq) + 1))
        blocks.append({"year": year, "event_code": k[0], "round": k[1],
                       "entries": entries, "partial_field": partial})
    return blocks, dropped


if __name__ == "__main__":
    years = sys.argv[1:] or ["2011", "2012", "2013", "2014", "2015", "2016",
                             "2017", "2018", "2019", "2022", "2023", "2024",
                             "2025", "2026"]
    allb, alld = [], []
    for y in years:
        p = f"neira_pdf/{y}.pdf"
        if not os.path.exists(p):
            continue
        bl, dr = extract_year(p, int(y))
        cb = [b for b in bl if any(CRLS.search(e["entry"]) for e in b["entries"])]
        print(f"{y}: {len(bl)} blocks, {len(cb)} with CRLS, {len(dr)} dropped cells")
        allb += bl
        alld += dr
    json.dump(allb, open("neira_champ_blocks.json", "w"), indent=1)
    print("TOTAL blocks:", len(allb))
    print("\nCRLS results:")
    for b in sorted(allb, key=lambda b: (b["year"], b["event_code"], b["round"])):
        hit = [e for e in b["entries"] if CRLS.search(e["entry"])]
        if not hit:
            continue
        for h in hit:
            print(f"  {b['year']} {b['event_code']:7s} {b['round']:4s} "
                  f"place {h['place']}/{len(b['entries'])}  {h['time']}  "
                  f"(votes {h['votes']}/{h['total']})")
    if alld:
        print("\nDROPPED (ambiguous, excluded):")
        for d in alld[:30]:
            print("  ", d)
