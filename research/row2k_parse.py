#!/usr/bin/env python3
"""row2k results page parser: extract results-block tables -> events with placings."""
import re, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import fetch, strip_tags, CRLS_RE

CELL = re.compile(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>")
ROW = re.compile(r"(?is)<tr[^>]*>(.*?)</tr>")
BLOCK = re.compile(r'(?is)<div class="results-block">(.*?)</div>')
TIME_RE = re.compile(r"^\d{1,2}:\d{2}(?:\.\d{1,3})?$|^\d{1,2}:\d{2}:\d{2}(?:\.\d+)?$")


def clean(s):
    s = re.sub(r"(?is)<!--.*?-->", " ", s)
    s = strip_tags(s)
    return re.sub(r"\s+", " ", s).strip()


def parse_page(html):
    """Return dict with meta + list of event blocks."""
    txt = strip_tags(html)
    out = {"distance": None, "conditions": None, "comments": None,
           "submitted_by": None, "venue": None, "date_str": None,
           "title": None, "events": []}

    m = re.search(r"(?is)<h1[^>]*>(.*?)</h1>", html)
    if m:
        out["title"] = clean(m.group(1))
    m = re.search(r"(?im)^\s*Distance:\s*(.+)$", txt)
    if m:
        out["distance"] = m.group(1).strip()
    m = re.search(r"(?is)\bConditions:\s*(.+?)\n\s*(?:Comments:|RESULTS)", txt)
    if m:
        out["conditions"] = re.sub(r"\s+", " ", m.group(1)).strip()
    m = re.search(r"(?is)\bComments:\s*(.+?)\n\s*RESULTS", txt)
    if m:
        out["comments"] = re.sub(r"\s+", " ", m.group(1)).strip()[:2000]
    m = re.search(r"(?im)Submitted by\s+(.+)$", txt)
    if m:
        out["submitted_by"] = m.group(1).strip()[:80]
    # header line: "May 9, 2026 - Charles River Powerhouse"
    m = re.search(r"(?im)^\s*((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4})\s*-\s*(.+)$", txt)
    if m:
        out["date_str"] = m.group(1).strip()
        out["venue"] = m.group(2).strip()
    else:
        m = re.search(r"(?im)^\s*((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4})\s*$", txt)
        if m:
            out["date_str"] = m.group(1).strip()

    for b in BLOCK.findall(html):
        rows = ROW.findall(b)
        if not rows:
            continue
        header = None
        entries = []
        for i, r in enumerate(rows):
            cells = [clean(c) for c in CELL.findall(r)]
            cells = [c for c in cells]
            if not cells:
                continue
            joined = " ".join(cells).strip()
            if i == 0 and (len(cells) == 1 or "bgcolor" in r.lower() or "<b>" in r.lower()):
                if joined:
                    header = joined
                    continue
            if not joined:
                continue
            # entry row: [team, time] or [place, team, time] or [team, time, margin]
            nonempty = [c for c in cells if c]
            if len(nonempty) < 2:
                # maybe a sub-header inside block
                if nonempty and not TIME_RE.match(nonempty[0]):
                    if header is None:
                        header = nonempty[0]
                continue
            time_i = None
            for j, c in enumerate(nonempty):
                if TIME_RE.match(c):
                    time_i = j
                    break
            if time_i is None:
                continue
            t = nonempty[time_i]
            name_parts = [c for j, c in enumerate(nonempty) if j != time_i and not re.match(r"^\d+\.?$", c)]
            team = name_parts[0] if name_parts else ""
            extra = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""
            entries.append({"team": team, "time": t, "extra": extra})
        if entries:
            for k, e in enumerate(entries, 1):
                e["place"] = k
            out["events"].append({"event": header or "UNKNOWN", "entries": entries})
    return out


if __name__ == "__main__":
    idx = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "neira_index.json")))
    crls = [r for r in idx if r.get("crls")]
    from collections import Counter
    hdr = Counter()
    for r in crls:
        h = fetch(r["url"])
        p = parse_page(h)
        for ev in p["events"]:
            hdr[ev["event"]] += 1
    for k, v in hdr.most_common(200):
        print(v, "|", k)
