#!/usr/bin/env python3
"""Assemble every source into 02-results.json + 02-results.md.

Sources, in order of authority for a given race:
  1. neira.qra.org structured HTML       (2026 championship, official)
  2. NEIRA championship PDFs             (2011-2026, official, vote-verified)
  3. HereNow Breeze API                  (MPSRA + other regattas, computed from
                                          raw start/finish timestamps)
  4. row2k NEIRA dual/tri-meet results   (2007-2026, as submitted by coaches)
"""
import json, os, re, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s3_build as S
from qra_parse import parse as qra_parse, EVENT_MAP

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_JSON = os.path.join(HERE, "02-results.json")
OUT_MD = os.path.join(HERE, "02-results.md")

# ---------------------------------------------------------------- NEIRA champs
NEIRA_VENUE = {
    2011: "Lake Quinsigamond, Worcester, MA", 2012: "Lake Quinsigamond, Worcester, MA",
    2013: "Lake Quinsigamond, Worcester, MA", 2014: "Lake Quinsigamond, Worcester, MA",
    2015: "Lake Quinsigamond, Worcester, MA", 2016: "Lake Quinsigamond, Worcester, MA",
    2017: "Lake Quinsigamond, Worcester, MA", 2018: "Lake Quinsigamond, Worcester, MA",
    2019: "Lake Quinsigamond, Worcester, MA", 2022: "Lake Quinsigamond, Worcester, MA",
    2023: "Lake Quinsigamond, Worcester, MA", 2024: "Lake Quinsigamond, Worcester, MA",
    2025: "Lake Quinsigamond, Worcester, MA", 2026: "Lake Quinsigamond, Worcester, MA",
}
NEIRA_DATE = {
    2011: "2011-05-21", 2012: "2012-05-19", 2013: "2013-05-18", 2014: "2014-05-31",
    2015: "2015-05-30", 2016: "2016-05-28", 2017: "2017-05-27", 2018: "2018-05-26",
    2019: "2019-05-25", 2022: "2022-05-28", 2023: "2023-05-27", 2024: "2024-05-25",
    2025: "2025-05-24", 2026: "2026-05-23",
}
NEIRA_PDF_URL = {
    2011: "http://www.neirarowing.org/documents/2011NEIRA_Results.pdf",
    2012: "http://www.neirarowing.org/documents/2012NEIRA.pdf",
    2013: "http://www.neirarowing.org/documents/2013NEIRA_Results.pdf",
    2014: "http://www.neirarowing.org/documents/2014NEIRA_Results.pdf",
    2015: "http://www.neirarowing.org/documents/2015NEIRAResults.pdf",
    2016: "http://www.neirarowing.org/documents/2016NEIRAResults.pdf",
    2017: "http://neira.qra.org/PDF/2017NEIRA.pdf",
    2018: "https://neirarowing.org/documents/2018NEIRAResults.pdf",
    2019: "https://www.row2k.com/results/files/20190525NEIRA.pdf",
    2022: "https://neirarowing.org/documents/2022NEIRA.pdf",
    2023: "https://neirarowing.org/documents/2023NEIRAResults.pdf",
    2024: "https://neirarowing.org/documents/2024NEIRAResults.pdf",
    2025: "https://neirarowing.org/documents/2025NEIRAResults.pdf",
    2026: "https://neirarowing.org/wp-content/uploads/2026/06/2026_NEIRA.pdf",
}
CODE_RE = re.compile(r"^([GB])(1st|2nd|3rd|4th|5th|6th)?(4|8|1x|2x|4x|x)$", re.I)
ROUND_NAME = {"GF": "Grand Final", "PF": "Petite Final", "TT": "Time Trial", "F": "Final"}


def decode_code(code):
    m = CODE_RE.match(code or "")
    if not m:
        return None, None, None
    squad = "girls" if m.group(1).upper() == "G" else "boys"
    boat = {"1st": "1V", "2nd": "2V", "3rd": "3V", "4th": "4V",
            "5th": "5V", "6th": "6V"}.get((m.group(2) or "").lower())
    cls = m.group(3).lower()
    cls = {"4": "4+", "8": "8+"}.get(cls, cls)
    return squad, boat, cls


def round_label(r):
    if r in ROUND_NAME:
        return ROUND_NAME[r]
    if re.match(r"^H\d+$", r or ""):
        return "Heat " + r[1:]
    if re.match(r"^F\d+$", r or ""):
        return "Final " + r[1:]
    if re.match(r"^SF\d*$", r or ""):
        return "Semifinal"
    return r


def build_neira_champs():
    out = []
    p = os.path.join(HERE, "neira_champ_blocks.json")
    if not os.path.exists(p):
        return out
    for b in json.load(open(p)):
        y = b["year"]
        if y == 2026:
            continue                    # 2026 comes from the structured HTML
        crls = [e for e in b["entries"] if S.is_crls(e["entry"])]
        if not crls:
            continue
        squad, boat, cls = decode_code(b["event_code"])
        field = [e["entry"] for e in b["entries"]]
        winner = next((e for e in b["entries"] if e["place"] == 1), None)
        for c in crls:
            marg = None
            if c["place"] == 1:
                nxt = next((e for e in b["entries"] if e["place"] == 2), None)
                if nxt:
                    marg = S.margin(c["time"], nxt["time"])
            elif winner:
                marg = S.margin(c["time"], winner["time"])
            notes = [f"NEIRA Championship {round_label(b['round'])}",
                     f"event code {b['event_code']}"]
            if b.get("partial_field"):
                notes.append("field list incomplete: some rows unrecoverable from "
                             "the PDF's multi-column layout (CRLS row and placing "
                             "are from the PDF's own Order column)")
            out.append({
                "year": y, "date": NEIRA_DATE.get(y, "UNKNOWN"),
                "regatta": f"NEIRA Championship {y}",
                "venue": NEIRA_VENUE.get(y, "UNKNOWN"),
                "event": f"{squad or ''} {boat or ''} {cls or ''}".strip() + f" - {round_label(b['round'])}",
                "squad": squad or "UNKNOWN", "boat": boat or "UNKNOWN",
                "boat_class": cls, "place": c["place"], "time": c["time"],
                "margin": marg, "field": field, "athletes": [], "coxswain": None,
                "crls_entry_name": c["entry"],
                "source": "neira-championship-pdf",
                "source_url": NEIRA_PDF_URL.get(y, "https://neirarowing.org/results/"),
                "notes": "; ".join(notes),
            })
    return out


def build_neira_2026():
    out = []
    p = os.path.join(HERE, "cache", "neira_qra_2026.html")
    if not os.path.exists(p):
        return out
    blocks = qra_parse(open(p, encoding="utf-8", errors="replace").read())
    for b in blocks:
        crls = [e for e in b["entries"] if S.is_crls(e["entry"])]
        if not crls:
            continue
        field = [e["entry"] for e in b["entries"]]
        winner = next((e for e in b["entries"] if e["order"] == 1), None)
        for c in crls:
            marg = None
            if c["order"] == 1:
                nxt = next((e for e in b["entries"] if e["order"] == 2), None)
                if nxt:
                    marg = S.margin(c["time"], nxt["time"])
            elif winner:
                marg = S.margin(c["time"], winner["time"])
            out.append({
                "year": 2026, "date": NEIRA_DATE[2026],
                "regatta": "NEIRA Championship 2026",
                "venue": NEIRA_VENUE[2026],
                "event": f"{b['event']} - {b['round']}",
                "squad": b["squad"] or "UNKNOWN", "boat": b["boat"] or "UNKNOWN",
                "boat_class": b["boat_class"], "place": c["order"], "time": c["time"],
                "margin": marg, "field": field, "athletes": [], "coxswain": None,
                "crls_entry_name": c["entry"],
                "source": "neira-qra-official",
                "source_url": "http://neira.qra.org/",
                "notes": f"NEIRA Championship {b['round']}; {b['status']}"
                         + (f"; raced {b['race_time']}" if b.get("race_time") else ""),
            })
    return out


# ------------------------------------------------------------------ row2k redo
def build_row2k_v2():
    """row2k with the validated squad attribution."""
    from fetch import fetch
    from row2k_parse import parse_page
    from squad import assign
    idx = json.load(open(os.path.join(HERE, "neira_index.json")))
    pages = [r for r in idx if r.get("crls")]
    out = []
    for r in sorted(pages, key=lambda x: (x["year"], x["date_str"])):
        html = fetch(r["url"])
        if not html:
            continue
        p = parse_page(html)
        if not p["events"]:
            continue
        date = S.norm_date(p.get("date_str") or r.get("date_str"))
        venue = p.get("venue") or r.get("venue") or "UNKNOWN"
        title = re.sub(r"^NEIRA[^,]*,\s*", "", r["title"]).strip() or r["title"]
        squads, method = assign(p["events"], r["title"])
        for ev, sq in zip(p["events"], squads):
            ents = ev["entries"]
            crls_rows = [e for e in ents if S.is_crls(e["team"])]
            if not crls_rows:
                continue
            field = [e["team"] for e in ents]
            winner_time = ents[0]["time"] if ents else None
            for ce in crls_rows:
                g = S.gender_from(ce["team"]) or sq
                blab = S.boat_label(ev["event"])
                m = re.search(r"\b([1-6])V\b", ce["team"], re.I)
                if m:
                    blab = f"{m.group(1)}V"
                if re.search(r"novice", ce["team"] + " " + ev["event"], re.I):
                    blab = "Novice"
                place = ce["place"]
                marg = None
                if place == 1 and len(ents) > 1:
                    marg = S.margin(ce["time"], ents[1]["time"])
                elif place and place > 1:
                    marg = S.margin(ce["time"], winner_time)
                notes = [f"squad attribution: {method}"]
                if not g:
                    notes.append("squad could not be determined - recorded UNKNOWN")
                if ce["extra"]:
                    notes.append("extra: " + ce["extra"])
                if p.get("distance"):
                    notes.append("distance: " + p["distance"])
                if p.get("conditions"):
                    notes.append("conditions: " + p["conditions"][:180])
                out.append({
                    "year": r["year"], "date": date, "regatta": title, "venue": venue,
                    "event": ev["event"], "squad": g or "UNKNOWN",
                    "boat": blab or "UNKNOWN", "boat_class": None,
                    "place": place, "time": ce["time"], "margin": marg,
                    "field": field, "athletes": [], "coxswain": None,
                    "crls_entry_name": ce["team"],
                    "source": "row2k", "source_url": r["url"],
                    "notes": "; ".join(notes),
                })
    return out


def build_herenow_all():
    """Every HereNow race that contains a CRLS entry."""
    p = os.path.join(HERE, "herenow_crls_races.json")
    if not os.path.exists(p):
        ids = [(i, "") for i in [20189, 20208, 20232, 20311, 20384, 20425, 20503,
                                 20561, 20678, 20689, 20942, 21031, 21055, 21141,
                                 21187, 21232, 21280, 21341, 21378, 21436]]
    else:
        ids = [(r["id"], "") for r in json.load(open(p))]
    recs = S.build_herenow(ids, "herenow")
    for r in recs:
        r.setdefault("boat_class", None)
    return recs


# --------------------------------------------------------------------- helpers
def dedupe(records):
    """Drop duplicate (date, event, boat, time) rows, preferring better sources."""
    PRIORITY = {"neira-qra-official": 0, "neira-championship-pdf": 1,
                "herenow": 2, "herenow-mpsra": 2, "row2k": 3}
    best = {}
    for r in records:
        key = (r["date"], r["squad"], r["boat"], r["time"],
               re.sub(r"\W+", "", (r["regatta"] or "").lower())[:24])
        p = PRIORITY.get(r["source"], 9)
        if key not in best or p < PRIORITY.get(best[key]["source"], 9):
            best[key] = r
    return list(best.values())


def sort_key(r):
    return (r.get("date") or "9999", r.get("squad") or "", r.get("boat") or "")


def build_timeteam():
    """USRowing Northeast Youth Championships (time-team live timing)."""
    p = os.path.join(HERE, "timeteam_crls.json")
    if not os.path.exists(p):
        return []
    out = []
    for r in json.load(open(p)):
        rows = r["rows"]
        crls = [x for x in rows if S.is_crls((x.get("club") or "") + " " + (x.get("entry_name") or ""))]
        if not crls:
            continue
        field = [x.get("club") or x.get("entry_name") for x in rows]
        ev = r.get("event_name") or ""
        squad = "girls" if re.search(r"\bwomen", ev, re.I) else (
                "boys" if re.search(r"\bmen", ev, re.I) else None)
        m = re.search(r"(\d)(?:st|nd|rd|th)?\s*(?:varsity|V)\b", ev, re.I)
        boat = f"{m.group(1)}V" if m else ("1V" if re.search(r"youth", ev, re.I) else None)
        cls = None
        mc = re.search(r"(8\+|4\+|4x\+?|2x|1x|2-)", ev)
        if mc:
            cls = mc.group(1)
        date = (r.get("start") or "")[:10] or "UNKNOWN"
        for c in crls:
            out.append({
                "year": int(r["year"]), "date": date,
                "regatta": r.get("regatta") or "USRowing Northeast Youth Championships",
                "venue": "Mercer Lake, West Windsor, NJ",
                "event": f"{ev} - {r.get('round')}".strip(" -"),
                "squad": squad or "UNKNOWN", "boat": boat or "UNKNOWN",
                "boat_class": cls, "place": c.get("place"), "time": c.get("time"),
                "margin": (c.get("margin") or "").lstrip("+") + "s"
                          if c.get("margin") else None,
                "field": field, "athletes": [],
                "coxswain": None,
                "crls_entry_name": c.get("entry_name") or c.get("club"),
                "source": "usrowing-timeteam",
                "source_url": f"https://usrowing.regatta.time-team.com/"
                              f"usrowing-northeast-youth/{r['year']}/races/{r['race_id']}",
                "notes": f"USRowing Northeast Youth Championships (Youth Nationals qualifier); "
                         f"{r.get('round')}; stroke: {c.get('stroke') or 'UNKNOWN'}",
            })
    return out


if __name__ == "__main__":
    allr = []
    n_qra = build_neira_2026(); allr += n_qra; print("NEIRA 2026 (qra html):", len(n_qra))
    n_pdf = build_neira_champs(); allr += n_pdf; print("NEIRA champ pdfs:", len(n_pdf))
    tt = build_timeteam(); allr += tt; print("USRowing regionals:", len(tt))
    hn = build_herenow_all(); allr += hn; print("HereNow:", len(hn))
    r2 = build_row2k_v2(); allr += r2; print("row2k:", len(r2))

    allr = dedupe(allr)
    allr.sort(key=sort_key)
    print("after dedupe:", len(allr))
    json.dump({"races": allr}, open(os.path.join(HERE, "part_all.json"), "w"), indent=1)
