#!/usr/bin/env python3
"""Squad (boys/girls) attribution for row2k combined pages.

Verified structural rule (confirmed against pages carrying explicit
"Race Order:" comments -- 2026 CRLS/Hopkins, 2024 Middlesex/CRLS,
2010 Middlesex/Pomfret/CRLS): on a combined "Boys & Girls" row2k page the
boys' result blocks are listed FIRST, then the girls' blocks, and the boat
rank sequence RESETS at the switch.

We split at the reset and then VALIDATE with times: the boys' group must be
faster. If the time test disagrees or is inconclusive, the page's squads are
left UNKNOWN rather than guessed.
"""
import re

RANK = [
    (r"\bsecond\s+(?:boat|four|fours|eight|varsity)|\b2nd\b|\b2v\b", 2),
    (r"\bthird\s+(?:boat|four|fours|eight|varsity)|\b3rd\b|\b3v\b", 3),
    (r"\bfourth\s+(?:boat|four|fours|eight|varsity)|\b4th\b|\b4v\b", 4),
    (r"\bfifth\s+(?:boat|four|fours|eight|varsity)|\b5th\b|\b5v\b", 5),
    (r"\bsixth\s+(?:boat|four|fours|eight|varsity)|\b6th\b|\b6v\b", 6),
    # rank 1 LAST: the bare "varsity" fallback must not swallow "2nd Varsity"
    (r"\bfirst\s+(?:boat|four|fours|eight|varsity)|\b1st\b|\b1v\b|"
     r"\bvarsity\s+(?:four|fours|eight|8|4)\b|^varsity$", 1),
]


def rank_of(event):
    t = (event or "").lower()
    if re.search(r"novice|freshman|frosh", t):
        return None
    for pat, r in RANK:
        if re.search(pat, t):
            return r
    return None          # "Other" / unlabelled


def to_sec(t):
    m = re.match(r"^(?:(\d+):)?(\d{1,2}):(\d{2}(?:\.\d+)?)$", t or "")
    if m:
        return int(m.group(1) or 0) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    m = re.match(r"^(\d{1,2}):(\d{2}(?:\.\d+)?)$", t or "")
    return int(m.group(1)) * 60 + float(m.group(2)) if m else None


def split_point(events):
    """Index where the girls' section starts, or None."""
    ranks = [rank_of(e["event"]) for e in events]
    seen_max = 0
    for i, r in enumerate(ranks):
        if r is None:
            # 'Other' after at least two ranked blocks -> likely the switch
            if i >= 2 and seen_max >= 2:
                return i
            continue
        if r <= seen_max:
            return i
        seen_max = max(seen_max, r)
    return None


def median(xs):
    xs = sorted(x for x in xs if x is not None)
    if not xs:
        return None
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def event_gender(event):
    """Gender named directly in the block header, if any."""
    t = (event or "").lower()
    g = bool(re.search(r"\bgirls?\b|\bgirl's\b|\bwomen\b|\bg\d\b|\b\dg\d?\b", t))
    b = bool(re.search(r"\bboys?\b|\bboy's\b|\bmen\b|\bb\d\b|\b\db\d?\b", t))
    if g and not b:
        return "girls"
    if b and not g:
        return "boys"
    return None


def assign(events, title):
    """-> (list of 'boys'/'girls'/None per event, method string)"""
    n = len(events)

    # 1. Highest confidence: every block names its own gender.
    per = [event_gender(e["event"]) for e in events]
    if all(p is not None for p in per) and n:
        return per, "each result block names its squad explicitly"

    tl = (title or "").lower()
    has_b = bool(re.search(r"\bboys?\b|\bboy's\b", tl))
    has_g = bool(re.search(r"\bgirls?\b|\bgirl's\b", tl))

    # 2. Single-gender page.
    if has_b and not has_g:
        return ["boys"] * n, "page title names boys only"
    if has_g and not has_b:
        return ["girls"] * n, "page title names girls only"

    # 3. Mixed page where SOME blocks are labelled: fill the rest structurally
    #    only if the labelled ones agree with the split we detect.
    sp = split_point(events)
    if sp is None or sp == 0 or sp >= n:
        if any(p is not None for p in per):
            return per, "partial: only blocks that name their squad are attributed"
        return [None] * n, "combined page, no detectable boys/girls split"

    a_times = [to_sec(e["entries"][0]["time"]) for e in events[:sp] if e["entries"]]
    b_times = [to_sec(e["entries"][0]["time"]) for e in events[sp:] if e["entries"]]
    ma, mb = median(a_times), median(b_times)
    if ma is None or mb is None:
        return per, "combined page, split found but times unusable"

    if mb - ma >= 10:
        guess = ["boys"] * sp + ["girls"] * (n - sp)
        method = (f"structural split at block {sp} (boat-rank reset); validated by "
                  f"times (median winner {ma:.1f}s vs {mb:.1f}s)")
    elif ma - mb >= 10:
        guess = ["girls"] * sp + ["boys"] * (n - sp)
        method = (f"structural split at block {sp}; time test indicates girls-first "
                  f"(median {ma:.1f}s vs {mb:.1f}s)")
    else:
        if any(p is not None for p in per):
            return per, ("partial: only blocks naming their squad are attributed "
                         f"(time test inconclusive: {ma:.1f}s vs {mb:.1f}s)")
        return [None] * n, (f"combined page, split at {sp} but time test "
                            f"inconclusive ({ma:.1f}s vs {mb:.1f}s)")

    # explicit labels win where present, and contradict -> abandon the guess
    for i, p in enumerate(per):
        if p is not None and p != guess[i]:
            return per, ("structural guess contradicted by an explicit block label; "
                         "only explicitly labelled blocks attributed")
    return [per[i] or guess[i] for i in range(n)], method
