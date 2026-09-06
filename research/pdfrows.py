#!/usr/bin/env python3
"""Extract NEIRA championship PDFs by clustering words on y-coordinate."""
import sys, re, json, os
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTTextLine

def words_with_pos(path):
    pages = []
    for pageno, layout in enumerate(extract_pages(path), 1):
        items = []
        for el in layout:
            if not isinstance(el, LTTextContainer):
                continue
            for line in el:
                if not isinstance(line, LTTextLine):
                    continue
                # split line into words with positions
                cur = ""
                x0 = None
                lastx = None
                y = None
                for ch in line:
                    if not isinstance(ch, LTChar):
                        continue
                    c = ch.get_text()
                    if y is None:
                        y = round(ch.y0, 1)
                    if c.strip() == "":
                        if cur:
                            items.append((y, x0, cur))
                            cur = ""
                            x0 = None
                        continue
                    if x0 is None:
                        x0 = ch.x0
                    cur += c
                    lastx = ch.x1
                if cur:
                    items.append((y, x0, cur))
        pages.append(items)
    return pages


def rows(items, ytol=2.0):
    """Cluster items into rows by y, sort by x."""
    out = []
    used = [False] * len(items)
    order = sorted(range(len(items)), key=lambda i: (-items[i][0], items[i][1]))
    i = 0
    groups = []
    for i in order:
        if used[i]:
            continue
        y = items[i][0]
        grp = [items[i]]
        used[i] = True
        for j in order:
            if used[j]:
                continue
            if abs(items[j][0] - y) <= ytol:
                grp.append(items[j])
                used[j] = True
        grp.sort(key=lambda t: t[1])
        groups.append((y, grp))
    groups.sort(key=lambda g: -g[0])
    for y, grp in groups:
        out.append([(round(x, 1), w) for (_, x, w) in grp])
    return out


if __name__ == "__main__":
    p = sys.argv[1]
    for pn, items in enumerate(words_with_pos(p), 1):
        print(f"\n=============== PAGE {pn}")
        for r in rows(items):
            print("  " + " | ".join(f"{w}" for x, w in r))
