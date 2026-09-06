#!/usr/bin/env python3
"""Parse neira.qra.org live championship HTML (structured tables)."""
import re, sys, os, json

EVENT_MAP = {
    "Girl's First Four w/Cox": ("girls", "1V", "4+"),
    "Girl's Second Four w/Cox": ("girls", "2V", "4+"),
    "Girl's Third Four w/Cox": ("girls", "3V", "4+"),
    "Girl's Fourth Four w/Cox": ("girls", "4V", "4+"),
    "Boy's First Four w/Cox": ("boys", "1V", "4+"),
    "Boy's Second Four w/Cox": ("boys", "2V", "4+"),
    "Boy's Third Four w/Cox": ("boys", "3V", "4+"),
    "Boy's Fourth Four w/Cox": ("boys", "4V", "4+"),
    "Girl's First Eight": ("girls", "1V", "8+"),
    "Girl's Second Eight": ("girls", "2V", "8+"),
    "Girl's Third Eight": ("girls", "3V", "8+"),
    "Boy's First Eight": ("boys", "1V", "8+"),
    "Boy's Second Eight": ("boys", "2V", "8+"),
    "Boy's Third Eight": ("boys", "3V", "8+"),
}


def parse(html):
    """-> list of {event, squad, boat, boat_class, round, status, entries}"""
    out = []
    # split on event divs
    parts = re.split(r'<div class="event">', html)
    for p in parts[1:]:
        ev = re.match(r"([^<]+)</div>", p)
        if not ev:
            continue
        ev_name = ev.group(1).strip()
        body = p
        # rounds
        for rm in re.finditer(
                r'<span class="race">([^<]+)</span>\s*<br>\s*<span class="raceTime">(.*?)</span>\s*<table.*?</table>',
                body, re.S):
            rnd = rm.group(1).strip()
            meta = re.sub(r"<[^>]+>", " ", rm.group(2))
            status = "OFFICIAL" if "OFFICIAL" in meta.upper() else "UNKNOWN"
            tm = re.search(r"(\d{1,2}:\d{2}\s*[AP]M\s+\w+)", meta)
            entries = []
            for tr in re.finditer(r"<tr>(.*?)</tr>", rm.group(0), re.S):
                tds = re.findall(r'<td class="result">(.*?)</td>', tr.group(1), re.S)
                if len(tds) != 3:
                    continue
                order = re.sub(r"<[^>]+>", "", tds[0]).strip()
                name = re.sub(r"<[^>]+>", "", tds[1]).strip().replace("&amp;", "&")
                res = re.sub(r"<[^>]+>", "", tds[2]).strip()
                entries.append({"order": int(order) if order.isdigit() else None,
                                "entry": name, "time": res})
            if entries:
                sq, boat, cls = EVENT_MAP.get(ev_name, (None, None, None))
                out.append({"event": ev_name, "squad": sq, "boat": boat,
                            "boat_class": cls, "round": rnd, "status": status,
                            "race_time": tm.group(1) if tm else None,
                            "entries": entries})
    return out


CRLS = re.compile(r"\bCRLS\b|Cambridge\s*R|Rindge", re.I)

if __name__ == "__main__":
    h = open(sys.argv[1] if len(sys.argv) > 1 else "cache/neira_qra_2026.html",
             encoding="utf-8", errors="replace").read()
    bl = parse(h)
    print("blocks:", len(bl))
    for b in bl:
        hit = [e for e in b["entries"] if CRLS.search(e["entry"])]
        if hit:
            print(f"--- {b['event']} | {b['round']} | {b['status']} | {b['race_time']}")
            for e in b["entries"]:
                m = " <<<" if CRLS.search(e["entry"]) else ""
                print(f"     {e['order']} {e['entry']:20s} {e['time']}{m}")
