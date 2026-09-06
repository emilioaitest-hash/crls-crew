#!/usr/bin/env python3
"""Step 2: fetch every NEIRA regatta result page (parallel, cached), flag CRLS ones."""
import json, os, sys, concurrent.futures as cf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import fetch, strip_tags, has_crls, cache_path

HERE = os.path.dirname(os.path.abspath(__file__))
idx = json.load(open(os.path.join(HERE, "neira_index.json")))
print("regattas:", len(idx))

def work(r):
    html = fetch(r["url"], sleep=0.0)
    if not html:
        return (r["uid"], False, 0)
    txt = strip_tags(html)
    return (r["uid"], has_crls(txt), len(txt))

hits = []
done = 0
with cf.ThreadPoolExecutor(max_workers=10) as ex:
    for uid, hit, n in ex.map(work, idx):
        done += 1
        if hit:
            hits.append(uid)
        if done % 200 == 0:
            print(f"  {done}/{len(idx)} fetched, {len(hits)} CRLS hits", flush=True)

hitset = set(hits)
for r in idx:
    r["crls"] = r["uid"] in hitset
json.dump(idx, open(os.path.join(HERE, "neira_index.json"), "w"), indent=1)
crls = [r for r in idx if r["crls"]]
print("CRLS-containing regattas:", len(crls))
from collections import Counter
c = Counter(r["year"] for r in crls)
for y in sorted(c):
    print(" ", y, c[y])
