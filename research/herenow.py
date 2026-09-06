#!/usr/bin/env python3
"""HereNow Breeze API client - correct graph walk.
Entries live under Events; timing under Entry.EntryResults (per Flight).
Elapsed = FinishTime1 - StartTime1. Place = rank of elapsed within flight.
Verified vs official MPSRA 2025 PDF: CRLS G1V4+ Grand Final 06:44.8 -> matches.
"""
import json, os, re, sys, subprocess, time, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
os.makedirs(CACHE, exist_ok=True)
API = "https://newwebrole2023.azurewebsites.net/breeze/BreezeApi"
CRLS_RE = re.compile(r"\bCRLS\b|Cambridge\s+Rindge|Cambridge\s+R\s*&\s*L", re.I)


def get(url, tag):
    p = os.path.join(CACHE, "hn_" + tag + ".json")
    if os.path.exists(p) and os.path.getsize(p) > 100:
        try:
            return json.load(open(p))
        except Exception:
            pass
    for _ in range(3):
        try:
            out = subprocess.run(["curl", "-s", "--max-time", "120", "-A", "Mozilla/5.0",
                                  "-H", "Accept: application/json", url],
                                 capture_output=True, timeout=150)
            d = json.loads(out.stdout.decode("utf-8", errors="replace"))
            json.dump(d, open(p, "w"))
            time.sleep(0.2)
            return d
        except Exception:
            time.sleep(2)
    return None


def build_index(obj, idx=None):
    if idx is None:
        idx = {}
    stack = [obj]
    while stack:
        o = stack.pop()
        if isinstance(o, dict):
            if "$id" in o:
                idx[o["$id"]] = o
            stack.extend(o.values())
        elif isinstance(o, list):
            stack.extend(o)
    return idx


def D(o, idx):
    if isinstance(o, dict) and "$ref" in o and len(o) <= 2:
        return idx.get(o["$ref"], {})
    return o if isinstance(o, dict) else {}


def parse_dt(s):
    if not s:
        return None
    try:
        return datetime.datetime.strptime(s[:23], "%Y-%m-%dT%H:%M:%S.%f")
    except Exception:
        try:
            return datetime.datetime.strptime(s[:19], "%Y-%m-%dT%H:%M:%S")
        except Exception:
            return None


def fmt(sec, prec=1):
    if sec is None:
        return None
    m = int(sec // 60)
    s = sec - m * 60
    return f"{m}:{s:0{4 if prec==1 else 6}.{prec}f}"


def elapsed_seconds(er):
    st = parse_dt(er.get("StartTime1"))
    ft = parse_dt(er.get("FinishTime1"))
    if not st or not ft:
        return None
    d = (ft - st).total_seconds()
    if d <= 0 or d > 3600:
        return None
    return d


def extract(race_id, prec=1):
    """Return (meta, flights) where each flight has ranked rows."""
    d = get(f"{API}/GetAllRaceResultsData?raceId={race_id}", f"race{race_id}")
    if not d or not isinstance(d, dict) or "Events" not in d:
        return None, None
    idx = build_index(d)
    meta = {"race_id": d.get("Id"), "name": d.get("Name"), "subtitle": d.get("Subtitle"),
            "date": (d.get("StartDate") or "")[:10],
            "precision": d.get("TimingPrecision")}

    # collect every (flight, entry, entryresult)
    flights = {}   # flight_id -> {name, code, status, note, rows:[]}
    for ev in d.get("Events", []):
        ev = D(ev, idx) if "$ref" in ev else ev
        ev_name = ev.get("Name")
        trophy = ev.get("Trophy")
        for e in ev.get("Entries", []) or []:
            e = D(e, idx) if "$ref" in e else e
            name = e.get("Name") or ""
            for er in e.get("EntryResults", []) or []:
                er = D(er, idx) if "$ref" in er else er
                fl = D(er.get("Flight"), idx)
                fid = fl.get("ID") or er.get("FlightId")
                if fid is None:
                    continue
                if fid not in flights:
                    flights[fid] = {"flight_id": fid, "flight": fl.get("Name"),
                                    "code": fl.get("Code"), "status": fl.get("Status"),
                                    "note": fl.get("OfficialNote"),
                                    "start": fl.get("StartTime"),
                                    "event": ev_name, "trophy": trophy, "rows": []}
                flights[fid]["rows"].append({
                    "boat": name,
                    "entry_id": e.get("Id"),
                    "sec": elapsed_seconds(er),
                    "status": er.get("Status"),
                    "bow": er.get("EntryNumber"),
                    "place_override": er.get("FinishPlaceOverride"),
                })

    out = []
    for fid, f in flights.items():
        rows = f["rows"]
        # dedupe by entry_id
        seen = {}
        for r in rows:
            seen[r["entry_id"]] = r
        rows = list(seen.values())
        timed = [r for r in rows if r["sec"] is not None and (r["status"] or "OK") == "OK"]
        timed.sort(key=lambda r: r["sec"])
        for i, r in enumerate(timed, 1):
            r["place"] = r["place_override"] or i
            r["time"] = fmt(r["sec"], prec)
        for r in rows:
            if "place" not in r:
                r["place"] = None
                r["time"] = fmt(r["sec"], prec) if r["sec"] is not None else None
        rows.sort(key=lambda r: (r["place"] is None, r["place"] or 0))
        f["rows"] = rows
        out.append(f)
    out.sort(key=lambda f: (f.get("start") or "", str(f.get("code"))))
    return meta, out


if __name__ == "__main__":
    rid = sys.argv[1] if len(sys.argv) > 1 else "21341"
    meta, fls = extract(rid)
    print(json.dumps(meta, indent=1))
    for f in fls:
        if not f["rows"]:
            continue
        crls = [r for r in f["rows"] if CRLS_RE.search(r["boat"] or "")]
        mark = "  <<< CRLS" if crls else ""
        print(f"--- [{f['code']}] {f['flight']} ({f['status']}) {f['note'] or ''}{mark}")
        for r in f["rows"]:
            print(f"      {r['place']}  {r['boat']}  {r['time']}  {r['status']}")
