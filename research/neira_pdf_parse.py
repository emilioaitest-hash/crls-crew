#!/usr/bin/env python3
"""Parse NEIRA championship PDFs (3-column layout) into event blocks.

Layout: each page has 3 columns. Within a column, blocks look like:
    G3rd4                      <- event code (sometimes on its own line)
    Heat 1  /  Grand Final
    <code> H1  OFFICIAL
    LnFOrderEntry Time
    <lane> <order> <Entry words...> <time>
"""
import sys, re, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdfrows import words_with_pos

COLS = [(0, 232), (232, 486), (486, 10000)]
TIME = re.compile(r"^\d{1,2}:\d{2}(?:\.\d{1,3})?$")
EVCODE = re.compile(r"^(G|B)(1st|2nd|3rd|4th|5th|1|2|3|4|5)?(4|8|x|1x|2x|4x)$", re.I)


def detect_cols(items, min_gap=12):
    """Find column bands from vertical empty gaps in x-coverage."""
    if not items:
        return COLS
    spans = []
    for (y, x, w) in items:
        spans.append((x, x + max(6.0, 5.2 * len(w))))
    spans.sort()
    merged = []
    for a, b in spans:
        if merged and a <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])
    if len(merged) < 2:
        return [(0, 10000)]
    bounds = [0.0]
    for i in range(len(merged) - 1):
        gap = merged[i + 1][0] - merged[i][1]
        if gap >= min_gap:
            bounds.append((merged[i][1] + merged[i + 1][0]) / 2.0)
    bounds.append(10000.0)
    cols = list(zip(bounds[:-1], bounds[1:]))
    # keep only reasonably wide columns
    cols = [(a, b) for a, b in cols if b - a > 40]
    return cols or COLS


def col_of(x, cols):
    for i, (a, b) in enumerate(cols):
        if a <= x < b:
            return i
    return len(cols) - 1


def page_columns(items, ytol=2.5):
    """-> list of columns, each a list of (y, [(x,word)]) top to bottom."""
    cols_def = detect_cols(items)
    cols = [[] for _ in cols_def]
    for (y, x, w) in items:
        cols[col_of(x, cols_def)].append((y, x, w))
    out = []
    for c in cols:
        groups = {}
        for (y, x, w) in c:
            key = None
            for k in groups:
                if abs(k - y) <= ytol:
                    key = k
                    break
            if key is None:
                key = y
                groups[key] = []
            groups[key].append((x, w))
        rows = []
        for y in sorted(groups, reverse=True):
            ws = sorted(groups[y], key=lambda t: t[0])
            rows.append((y, ws))
        out.append(rows)
    return out


def parse_pdf(path, year):
    """Return list of {event_code, round, status, entries:[{order,entry,time,lane}]}"""
    blocks = []
    for items in words_with_pos(path):
        for col in page_columns(items):
            cur = None
            pending_code = None
            pending_round = None
            for y, ws in col:
                toks = [w for x, w in ws]
                line = " ".join(toks)
                # Event code alone
                if len(toks) == 1 and EVCODE.match(toks[0]):
                    pending_code = toks[0]
                    continue
                if re.match(r"(?i)^(Heat|Grand Final|Final|Petite Final|Semi|Time Trial|Rep)\b", line) and not TIME.search(line):
                    pending_round = line
                    continue
                # header line: "<CODE> H1 OFFICIAL" / "<CODE> GF OFFICIAL"
                m = re.match(r"(?i)^([GB](?:1st|2nd|3rd|4th|5th|6th)?(?:4|8|1x|2x|4x|x))\s+(H\d+|GF|PF|F|TT|SF\d*)\s+(OFFICIAL|UNOFFICIAL)\b", line)
                if m:
                    cur = {"event_code": m.group(1), "round": m.group(2),
                           "status": m.group(3), "entries": [], "year": year}
                    blocks.append(cur)
                    pending_code = None
                    pending_round = None
                    continue
                if re.match(r"(?i)^Ln\s*F?\s*Order\s*Entry", line) or \
                   re.sub(r"\s+", "", line).lower().startswith(("lnforderentry", "lnorderentry")):
                    continue
                # entry row: ends with a time
                if cur is not None and toks and TIME.match(toks[-1]):
                    t = toks[-1]
                    rest = toks[:-1]
                    nums = []
                    while rest and re.fullmatch(r"\d{1,2}", rest[0]):
                        nums.append(int(rest.pop(0)))
                        if len(nums) == 2:
                            break
                    # sometimes lane+order fused with entry e.g. "2Winsor"
                    if rest and re.match(r"^\d{1,2}[A-Za-z]", rest[0]):
                        m2 = re.match(r"^(\d{1,2})([A-Za-z].*)$", rest[0])
                        nums.append(int(m2.group(1)))
                        rest[0] = m2.group(2)
                    entry = " ".join(rest).strip()
                    if not entry:
                        continue
                    lane = nums[0] if len(nums) >= 1 else None
                    order = nums[1] if len(nums) >= 2 else (nums[0] if nums else None)
                    if len(nums) >= 2:
                        lane, order = nums[0], nums[1]
                    cur["entries"].append({"lane": lane, "order": order,
                                           "entry": entry, "time": t})
    return blocks


CRLS = re.compile(r"\bCRLS\b|Cambridge\s*R|Rindge", re.I)

if __name__ == "__main__":
    y = sys.argv[1]
    bl = parse_pdf(f"neira_pdf/{y}.pdf", int(y))
    n = 0
    for b in bl:
        hit = [e for e in b["entries"] if CRLS.search(e["entry"])]
        if hit:
            n += 1
            print(f"--- {b['event_code']} {b['round']} {b['status']}")
            for e in sorted(b["entries"], key=lambda e: e["order"] or 99):
                mark = "  <<<" if CRLS.search(e["entry"]) else ""
                print(f"     {e['order']}  {e['entry']:24s} {e['time']}{mark}")
    print(f"\n{y}: {len(bl)} blocks, {n} with CRLS")
