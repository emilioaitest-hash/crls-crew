#!/usr/bin/env python3
"""Master builder: row2k NEIRA + HereNow (MPSRA/NEIRA champs) -> results records."""
import json, os, re, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import fetch
from row2k_parse import parse_page
import herenow

HERE = os.path.dirname(os.path.abspath(__file__))

# --- CRLS identification -------------------------------------------------
CRLS_POS = re.compile(r"\bCRLS\b|Cambridge\s*R(?:LS|L\b|indge|\s*&\s*L)|Rindge", re.I)
CRLS_NEG = re.compile(r"Cambridge\s+Boat\s+Club|\bCBC\b|Community\s+Rowing|\bCRI\b", re.I)


def is_crls(name):
    if not name:
        return False
    if CRLS_NEG.search(name):
        return False
    if CRLS_POS.search(name):
        return True
    return bool(re.fullmatch(r"\s*Cambridge\s*", name, re.I))


MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}


def norm_date(s):
    if not s:
        return "UNKNOWN"
    m = re.search(r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),\s*(\d{4})", s)
    if m:
        return f"{int(m.group(3)):04d}-{MONTHS[m.group(1)]:02d}-{int(m.group(2)):02d}"
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return m.group(0)
    return "UNKNOWN"


# --- gender / boat inference --------------------------------------------
def gender_from(text):
    if not text:
        return None
    t = text.lower()
    has_g = bool(re.search(r"\bgirls?\b|\bwomens?\b|\bg\d|\d\s*g\b|\bg4\b|\bg8\b", t))
    has_b = bool(re.search(r"\bboys?\b|\bmens?\b|\bb\d|\d\s*b\b|\bb4\b|\bb8\b", t))
    if has_g and not has_b:
        return "girls"
    if has_b and not has_g:
        return "boys"
    return None


ORD = [
    (r"\b(?:1st|first|1)\s*(?:varsity|v)?\b|\b1v\b|\bvarsity\b", "1V"),
    (r"\b(?:2nd|second|2)\s*(?:varsity|v)?\b|\b2v\b", "2V"),
    (r"\b(?:3rd|third|3)\s*(?:varsity|v)?\b|\b3v\b", "3V"),
    (r"\b(?:4th|fourth|4)\s*(?:varsity|v)?\b|\b4v\b", "4V"),
    (r"\b(?:5th|fifth|5)\s*(?:varsity|v)?\b|\b5v\b", "5V"),
    (r"\b(?:6th|sixth|6)\s*(?:varsity|v)?\b|\b6v\b", "6V"),
]


def boat_label(event, entry_extra=""):
    """Normalised boat label from an event/flight header."""
    t = (event or "").lower()
    if re.search(r"novice|freshman|frosh", t):
        m = re.search(r"\b(1st|first|2nd|second|3rd|third)\b", t)
        rank = {"1st": "1st", "first": "1st", "2nd": "2nd", "second": "2nd",
                "3rd": "3rd", "third": "3rd"}.get(m.group(1)) if m else None
        return f"{rank} Novice" if rank else "Novice"
    ORD_WORDS = {"1": "1V", "1st": "1V", "first": "1V",
                 "2": "2V", "2nd": "2V", "second": "2V",
                 "3": "3V", "3rd": "3V", "third": "3V",
                 "4": "4V", "4th": "4V", "fourth": "4V",
                 "5": "5V", "5th": "5V", "fifth": "5V",
                 "6": "6V", "6th": "6V", "sixth": "6V"}
    # "<ordinal> varsity", "<ordinal> boat/four/fours/eight", "3V", "3B4"
    m = re.search(r"\b(1st|2nd|3rd|4th|5th|6th|first|second|third|fourth|fifth|sixth)\s+"
                  r"(?:varsity|boat|four|fours|eight|eights|8|4)\b", t)
    if m:
        return ORD_WORDS[m.group(1)]
    m = re.search(r"\b([1-6])\s*v\b", t)
    if m:
        return ORD_WORDS[m.group(1)]
    m = re.search(r"\b([1-6])[bg]4\b", t)
    if m:
        return ORD_WORDS[m.group(1)]
    # bare "varsity four/eight" with no ordinal -> first boat
    if re.search(r"\bvarsity\b|\byouth\b", t):
        return "1V"
    return None


def to_sec(t):
    if not t:
        return None
    m = re.match(r"^(?:(\d+):)?(\d{1,2}):(\d{2}(?:\.\d+)?)$", t)
    if m:
        h = int(m.group(1) or 0)
        return h * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    m = re.match(r"^(\d{1,2}):(\d{2}(?:\.\d+)?)$", t)
    if m:
        return int(m.group(1)) * 60 + float(m.group(2))
    return None


def margin(a, b):
    sa, sb = to_sec(a), to_sec(b)
    if sa is None or sb is None:
        return None
    d = abs(sa - sb)
    return f"{d:.2f}s"


# ------------------------------------------------------------------------
def build_row2k():
    idx = json.load(open(os.path.join(HERE, "neira_index.json")))
    crls_pages = [r for r in idx if r.get("crls")]
    races = []
    for r in sorted(crls_pages, key=lambda x: (x["year"], x["date_str"])):
        html = fetch(r["url"])
        if not html:
            continue
        p = parse_page(html)
        date = norm_date(p.get("date_str") or r.get("date_str"))
        venue = p.get("venue") or r.get("venue") or "UNKNOWN"
        title = p.get("title") or r["title"]
        title_gender = gender_from(title)
        # page-level: does the title name only one gender?
        tl = title.lower()
        only_boys = ("boys" in tl or "boy's" in tl) and not ("girls" in tl or "girl's" in tl)
        only_girls = ("girls" in tl or "girl's" in tl) and not ("boys" in tl or "boy's" in tl)
        for ev in p["events"]:
            ents = ev["entries"]
            crls_rows = [e for e in ents if is_crls(e["team"])]
            if not crls_rows:
                continue
            field = [e["team"] for e in ents]
            winner_time = ents[0]["time"] if ents else None
            for ce in crls_rows:
                g = (gender_from(ce["team"]) or gender_from(ev["event"])
                     or ("boys" if only_boys else None) or ("girls" if only_girls else None))
                blab = boat_label(ev["event"]) or None
                # entry-level override e.g. "CRLS 2V"
                m = re.search(r"\b([1-6])V\b", ce["team"], re.I)
                if m:
                    blab = f"{m.group(1)}V"
                if re.search(r"novice", ce["team"], re.I):
                    blab = "Novice"
                place = ce["place"]
                marg = None
                if place == 1 and len(ents) > 1:
                    marg = margin(ce["time"], ents[1]["time"])
                elif place and place > 1:
                    marg = margin(ce["time"], winner_time)
                notes = []
                if not g:
                    notes.append("squad UNKNOWN: row2k page combined boys+girls without gender labels")
                if ce["extra"]:
                    notes.append("extra: " + ce["extra"])
                if p.get("distance"):
                    notes.append("distance: " + p["distance"])
                races.append({
                    "year": r["year"], "date": date,
                    "regatta": title, "venue": venue,
                    "event": ev["event"], "squad": g or "UNKNOWN",
                    "boat": blab or "UNKNOWN",
                    "place": place, "time": ce["time"],
                    "margin": marg, "field": field,
                    "athletes": [], "coxswain": None,
                    "crls_entry_name": ce["team"],
                    "source": "row2k", "source_url": r["url"],
                    "notes": "; ".join(notes),
                })
    return races


def build_herenow(race_ids, source_label):
    races = []
    for rid, meta_hint in race_ids:
        meta, fls = herenow.extract(rid)
        if not meta or not fls:
            print("  !! no data for", rid)
            continue
        for f in fls:
            rows = [r for r in f["rows"] if r["boat"]]
            crls_rows = [r for r in rows if is_crls(r["boat"])]
            if not crls_rows:
                continue
            field = [r["boat"] for r in rows]
            winner = next((r for r in rows if r["place"] == 1), None)
            for cr in crls_rows:
                ev = f["flight"] or f["event"] or ""
                g = gender_from(ev) or gender_from(cr["boat"])
                blab = boat_label(ev)
                mc = re.search(r"(8\+|4\+|4x\+?|2x|1x|2-|4-)", ev)
                bclass = mc.group(1) if mc else None
                marg = None
                if cr["place"] == 1:
                    second = next((r for r in rows if r["place"] == 2), None)
                    if second:
                        marg = margin(cr["time"], second["time"])
                elif winner and cr["place"]:
                    marg = margin(cr["time"], winner["time"])
                cox = None
                m = re.search(r"\(([^)]+)\)\s*$", cr["boat"] or "")
                if m:
                    cox = m.group(1).strip()
                notes = []
                if f.get("note"):
                    notes.append(f["note"])
                if f.get("status"):
                    notes.append("flight status: " + str(f["status"]))
                notes.append("coxswain surname from HereNow entry label")
                races.append({
                    "year": int((meta["date"] or "0000")[:4]),
                    "date": meta["date"] or "UNKNOWN",
                    "regatta": meta["name"], "venue": meta.get("subtitle") or "UNKNOWN",
                    "event": ev, "squad": g or "UNKNOWN",
                    "boat": blab or "UNKNOWN", "boat_class": bclass,
                    "place": cr["place"], "time": cr["time"],
                    "margin": marg, "field": field,
                    "athletes": [], "coxswain": cox,
                    "crls_entry_name": cr["boat"],
                    "source": source_label,
                    "source_url": f"https://legacy.herenow.com/results/#/races/{rid}/results",
                    "notes": "; ".join(notes),
                })
    return races


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    out = []
    if what in ("all", "row2k"):
        r = build_row2k()
        print("row2k records:", len(r))
        json.dump(r, open(os.path.join(HERE, "part_row2k.json"), "w"), indent=1)
        out += r
    if what in ("all", "mpsra"):
        ids = [(20189, ""), (20208, ""), (20232, ""), (20311, ""), (20384, ""), (20425, ""),
               (20503, ""), (20561, ""), (20678, ""), (20689, ""), (20942, ""), (21031, ""),
               (21055, ""), (21141, ""), (21187, ""), (21232, ""), (21280, ""), (21341, ""),
               (21378, ""), (21436, ""), (21482, "")]
        r = build_herenow(ids, "herenow-mpsra")
        print("MPSRA records:", len(r))
        json.dump(r, open(os.path.join(HERE, "part_mpsra.json"), "w"), indent=1)
        out += r
    print("TOTAL", len(out))
