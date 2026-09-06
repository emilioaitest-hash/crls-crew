#!/usr/bin/env python3
"""Robust NEIRA championship PDF extraction.

Runs several column-splitting strategies, validates each parsed block
(orders unique & sequential, times monotonically increasing with order),
then merges. Conflicting times for the same (event, round, team) are
reported rather than silently picked.
"""
import sys, os, re, json, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdfrows import words_with_pos
import neira_pdf_parse as N

TIME = N.TIME
CRLS = N.CRLS


def to_sec(t):
    m = re.match(r"^(\d{1,2}):(\d{2}(?:\.\d+)?)$", t)
    return int(m.group(1)) * 60 + float(m.group(2)) if m else None


def parse_with(path, year, colmode):
    """colmode: ('fixed', bands) or ('auto', min_gap)"""
    blocks = []
    for items in words_with_pos(path):
        if colmode[0] == "fixed":
            bands = colmode[1]
        else:
            bands = N.detect_cols(items, min_gap=colmode[1])
        cols = [[] for _ in bands]
        for (y, x, w) in items:
            cols[N.col_of(x, bands)].append((y, x, w))
        for c in cols:
            groups = {}
            for (y, x, w) in c:
                key = next((k for k in groups if abs(k - y) <= 2.5), None)
                if key is None:
                    key = y
                    groups[key] = []
                groups[key].append((x, w))
            rowlist = [(y, sorted(groups[y], key=lambda t: t[0]))
                       for y in sorted(groups, reverse=True)]
            cur = None
            for y, ws in rowlist:
                toks = [w for x, w in ws]
                line = " ".join(toks)
                m = re.match(r"(?i)^([GB](?:1st|2nd|3rd|4th|5th|6th)?(?:4|8|1x|2x|4x|x))\s+(H\d+|GF|PF|F\d*|TT|SF\d*)\s+(OFFICIAL|UNOFFICIAL)\b", line)
                if m:
                    cur = {"event_code": m.group(1), "round": m.group(2),
                           "status": m.group(3), "entries": [], "year": year}
                    blocks.append(cur)
                    continue
                if re.sub(r"\s+", "", line).lower().startswith(("lnforderentry", "lnorderentry")):
                    continue
                if cur is not None and toks and TIME.match(toks[-1]):
                    t = toks[-1]
                    rest = toks[:-1]
                    nums = []
                    while rest and re.fullmatch(r"\d{1,2}", rest[0]) and len(nums) < 2:
                        nums.append(int(rest.pop(0)))
                    if rest and re.match(r"^\d{1,2}[A-Za-z]", rest[0]):
                        m2 = re.match(r"^(\d{1,2})([A-Za-z].*)$", rest[0])
                        nums.append(int(m2.group(1)))
                        rest = [m2.group(2)] + rest[1:]
                    entry = " ".join(rest).strip()
                    if not entry or re.search(r"\d:\d", entry):
                        continue
                    lane = nums[0] if nums else None
                    order = nums[1] if len(nums) >= 2 else (nums[0] if nums else None)
                    cur["entries"].append({"lane": lane, "order": order,
                                           "entry": entry, "time": t})
    return blocks


def valid(b):
    """Accept a parsed block if it is internally self-consistent.

    NEIRA PDFs print an explicit Order column, so placings come from the
    source itself and we do NOT require the orders to be contiguous -- a
    block where the column split dropped a row is still usable (it is
    flagged partial later so the recorded field is marked incomplete).
    """
    es = [e for e in b["entries"] if e["order"] is not None]
    if len(es) < 2:
        return False
    orders = [e["order"] for e in es]
    if len(set(orders)) != len(orders):
        return False
    if max(orders) > 8 or min(orders) < 1:
        return False
    if len(es) > 8:            # NEIRA heats/finals are max 6-8 lanes;
        return False           # more means two columns got merged
    es2 = sorted(es, key=lambda e: e["order"])
    secs = [to_sec(e["time"]) for e in es2]
    if any(s is None for s in secs):
        return False
    for a, b2 in zip(secs, secs[1:]):
        if b2 < a - 0.001:
            return False
    # spread sanity: winner to last within 90s in a real race
    if secs[-1] - secs[0] > 90:
        return False
    # sanity: plausible race times 3:00-12:00
    if not all(150 < s < 900 for s in secs):
        return False
    return True


def extract_year(path, year):
    strategies = [("fixed", [(0, 232), (232, 486), (486, 10000)]),
                  ("auto", 12), ("auto", 18), ("auto", 8),
                  ("fixed", [(0, 240), (240, 495), (495, 10000)])]
    best = {}      # (code, round) -> block
    conflicts = []
    for mode in strategies:
        try:
            bl = parse_with(path, year, mode)
        except Exception as ex:
            continue
        for b in bl:
            if not valid(b):
                continue
            k = (b["event_code"], b["round"])
            if k not in best:
                best[k] = b
            else:
                old = {e["entry"]: e["time"] for e in best[k]["entries"]}
                new = {e["entry"]: e["time"] for e in b["entries"]}
                for team in set(old) & set(new):
                    if old[team] != new[team]:
                        conflicts.append((year, k, team, old[team], new[team]))
                if len(b["entries"]) > len(best[k]["entries"]):
                    best[k] = b
    return list(best.values()), conflicts


if __name__ == "__main__":
    years = sys.argv[1:] or ["2011", "2012", "2013", "2014", "2015", "2016",
                             "2017", "2018", "2019", "2022", "2023", "2024"]
    allb = []
    allc = []
    for y in years:
        p = f"neira_pdf/{y}.pdf"
        if not os.path.exists(p):
            continue
        bl, cf = extract_year(p, int(y))
        crls_b = [b for b in bl if any(CRLS.search(e["entry"]) for e in b["entries"])]
        print(f"{y}: {len(bl)} valid blocks, {len(crls_b)} with CRLS, {len(cf)} conflicts")
        allb += bl
        allc += cf
    json.dump(allb, open("neira_champ_blocks.json", "w"), indent=1)
    print("\nTOTAL valid blocks:", len(allb))
    if allc:
        print("CONFLICTS (need review):")
        for c in allc[:40]:
            print("  ", c)
