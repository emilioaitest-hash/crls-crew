#!/usr/bin/env python3
"""Discover every HereNow race containing a CRLS entry, via Breeze OData."""
import json, subprocess, sys, os, time, re
from collections import defaultdict

API = "https://newwebrole2023.azurewebsites.net/breeze/BreezeApi"
HERE = os.path.dirname(os.path.abspath(__file__))


def q(path):
    for _ in range(3):
        try:
            out = subprocess.run(["curl", "-s", "--max-time", "120", "-A", "Mozilla/5.0",
                                  "-H", "Accept: application/json", API + path],
                                 capture_output=True, timeout=150)
            return json.loads(out.stdout.decode("utf-8", errors="replace"))
        except Exception:
            time.sleep(2)
    return None


PATTERNS = ["Cambridge%20Rindge", "CRLS", "Cambridge%20RLS", "Cambridge%20R%26L"]

entries = {}
for pat in PATTERNS:
    skip = 0
    while True:
        d = q(f"/Entries?$filter=substringof('{pat}',Name)&$select=Id,Name,EventId&$orderby=Id&$top=200&$skip={skip}")
        if not d or not isinstance(d, list) or not d:
            break
        for e in d:
            entries[e["Id"]] = {"name": e["Name"], "event_id": e["EventId"]}
        print(f"  {pat}: +{len(d)} (total {len(entries)})", flush=True)
        if len(d) < 200:
            break
        skip += 200

print("total CRLS entries:", len(entries))
ev_ids = sorted({v["event_id"] for v in entries.values() if v["event_id"]})
print("distinct events:", len(ev_ids))

# map events -> races
ev2race = {}
B = 20
for i in range(0, len(ev_ids), B):
    chunk = ev_ids[i:i + B]
    filt = "%20or%20".join(f"Id%20eq%20{e}" for e in chunk)
    d = q(f"/Events?$filter={filt}&$select=Id,RaceId,Name")
    if isinstance(d, list):
        for e in d:
            ev2race[e["Id"]] = (e.get("RaceId"), e.get("Name"))
    else:
        print("   !! event batch failed:", str(d)[:120], flush=True)
        for e in chunk:                     # fall back to single lookups
            d1 = q(f"/Events?$filter=Id%20eq%20{e}&$select=Id,RaceId,Name")
            if isinstance(d1, list) and d1:
                ev2race[d1[0]["Id"]] = (d1[0].get("RaceId"), d1[0].get("Name"))
    print(f"  events {i+len(chunk)}/{len(ev_ids)} -> {len(ev2race)} mapped", flush=True)

race_ids = sorted({r for (r, n) in ev2race.values() if r})
print("distinct races:", len(race_ids))

races = {}
for i in range(0, len(race_ids), 15):
    chunk = race_ids[i:i + 15]
    filt = "%20or%20".join(f"Id%20eq%20{r}" for r in chunk)
    d = q(f"/Races?$filter={filt}&$select=Id,Name,StartDate,Subtitle")
    if not isinstance(d, list):
        d = []
        for r in chunk:
            d1 = q(f"/Races?$filter=Id%20eq%20{r}&$select=Id,Name,StartDate,Subtitle")
            if isinstance(d1, list):
                d += d1
    for r in d:
        races[r["Id"]] = {"id": r["Id"], "name": r.get("Name"),
                          "date": (r.get("StartDate") or "")[:10],
                          "subtitle": r.get("Subtitle")}
    print(f"  races {i+len(chunk)}/{len(race_ids)} -> {len(races)}", flush=True)

out = sorted(races.values(), key=lambda r: r["date"] or "")
json.dump(out, open(os.path.join(HERE, "herenow_crls_races.json"), "w"), indent=1)
for r in out:
    print(f"{r['id']:>7}  {r['date']}  {r['name']}  | {r['subtitle']}")
print("TOTAL races with CRLS:", len(out))
