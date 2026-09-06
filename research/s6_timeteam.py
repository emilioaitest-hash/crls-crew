#!/usr/bin/env python3
"""Scan USRowing Northeast Youth Championships (time-team) race pages for CRLS.

Each race page SSRs a __NEXT_DATA__ blob containing race_crew/round_crew with
club names. Times are rendered client-side, so we record what the SSR payload
proves (entry present, bib, sort order, status) and mark the time UNKNOWN
unless the payload actually carries it.
"""
import json, re, os, sys, subprocess, time, concurrent.futures as cf

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache", "timeteam")
os.makedirs(CACHE, exist_ok=True)
BASE = "https://usrowing.regatta.time-team.com/usrowing-northeast-youth"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
CRLS = re.compile(r"\bCRLS\b|Cambridge\s+Rindge", re.I)


def get(url, tag):
    p = os.path.join(CACHE, tag + ".html")
    if os.path.exists(p) and os.path.getsize(p) > 1000:
        return open(p, encoding="utf-8", errors="replace").read()
    for _ in range(3):
        try:
            out = subprocess.run(["curl", "-s", "--max-time", "45", "-A", UA, url],
                                 capture_output=True, timeout=60)
            t = out.stdout.decode("utf-8", errors="replace")
            if len(t) > 1000:
                open(p, "w", encoding="utf-8").write(t)
                return t
        except Exception:
            time.sleep(2)
    return ""


def nextdata(html):
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except Exception:
        return None


def races_for(year):
    html = get(f"{BASE}/{year}/races", f"{year}_races")
    d = nextdata(html)
    if not d:
        return {}, {}
    qs = d["props"]["pageProps"]["dehydratedState"]["queries"]
    data = qs[0]["state"]["data"]
    return data.get("race", {}), data.get("regatta", {})


def scan(year):
    races, reg = races_for(year)
    print(f"{year}: {len(races)} races", flush=True)
    if not races:
        return []
    regname = list(reg.values())[0]["name"] if reg else "USRowing Northeast Youth Championships"

    def one(rid_r):
        rid, r = rid_r
        html = get(f"{BASE}/{year}/races/{rid}", f"{year}_{rid}")
        d = nextdata(html)
        if not d:
            return None
        data = d["props"]["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]
        crews = data.get("race_crew") or data.get("round_crew") or {}
        rows = []
        for cid, c in crews.items():
            e = c.get("entry") or {}
            club = (e.get("club") or {}).get("name") or e.get("name") or ""
            # finish time / position live on the crew record
            res = c.get("adjusted_result")
            pos = c.get("adjusted_pos")
            plus = c.get("adjusted_plus")
            if not res:
                for t in (c.get("times") or []):
                    if (t.get("location_name") or "").lower() == "finish":
                        tot = t.get("total") or {}
                        res = res or tot.get("result")
                        pos = pos or tot.get("pos")
                        plus = plus or tot.get("plus")
            rows.append({"club": club, "entry_name": e.get("name"),
                         "bib": c.get("bib"), "sort_order": c.get("sort_order"),
                         "status": c.get("status"), "stroke": e.get("stroke_fullname"),
                         "time": res, "place": pos, "margin": plus,
                         "penalty": c.get("penalty")})
        if not any(CRLS.search((x["club"] or "") + " " + (x["entry_name"] or "")) for x in rows):
            return None
        return {"race_id": rid, "year": year, "regatta": regname,
                "event_code": r.get("event_code"), "event_name": r.get("event_name"),
                "round": r.get("round_type_name"), "start": r.get("start_datetime"),
                "string": r.get("string"), "rows": rows}

    out = []
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        for res in ex.map(one, list(races.items())):
            if res:
                out.append(res)
    return out


if __name__ == "__main__":
    allr = []
    for y in (sys.argv[1:] or ["2024", "2025", "2026"]):
        allr += scan(y)
    json.dump(allr, open(os.path.join(HERE, "timeteam_crls.json"), "w"), indent=1)
    print("\nCRLS races found:", len(allr))
    for r in allr:
        print(f"--- {r['year']} {r['event_name']} {r['round']} | {r['string']}")
        for x in sorted(r["rows"], key=lambda z: z["place"] or z["sort_order"] or 99):
            mark = " <<<" if CRLS.search((x["club"] or "") + " " + (x["entry_name"] or "")) else ""
            print(f"      {x['place']}  {x['time']}  {x['margin']}  {x['club']}{mark}")
