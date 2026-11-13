"""Find repeated wording across the built site (run after build.py).

    python3 tools/check_repeats.py            # English pages
    python3 tools/check_repeats.py cy         # Welsh pages

It lists, for every page:
  SAME PAGE   two cards in one list that open the same page
  SAME TEXT   two cards in one list with the very same words
  SIMILAR     two cards in one list that say nearly the same thing (shared phrases or many shared words)
  REPEAT      a sentence of nine words or more that appears twice on one page
Each hit is a pair to give its own wording (Ifan, 13 November 2026): keep both cards when they open different pages,
and rewrite one so each says something that fits its own page. Dates, feast days and source notes repeat by nature;
read the list with sense rather than chasing every line.
"""
import collections, glob, os, re, sys

from bs4 import BeautifulSoup

SITE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_site")
ROOT = os.path.join(SITE, "cy") if sys.argv[1:] == ["cy"] else SITE
STOP = set("the of and a in to was is at for on by with his her their from that as an it he she they who which".split())


def words(s):
    return re.sub(r"[^\w\s]", " ", s.lower()).split()


def phrases(w):
    return {tuple(w[i:i + 5]) for i in range(len(w) - 4) if sum(x not in STOP for x in w[i:i + 5]) >= 3}


def card_rows(soup):
    groups = collections.defaultdict(list)
    for c in soup.select(".wl-card, a.chap, li, article"):
        h, p = c.find(["h3", "h4"]), c.find("p")
        if not h or not p:
            continue
        a = c if c.name == "a" else c.select_one("a.wl, a.wl-go, a[href]")
        groups[id(c.parent)].append((a.get("href") if a else None, h.get_text(" ", strip=True), p.get_text(" ", strip=True)))
    return groups.values()


def check(path):
    soup = BeautifulSoup(open(path, encoding="utf-8").read(), "lxml")
    for t in soup.select("header, footer, nav, script, style, template, .refs"):
        t.decompose()
    out = []
    for rows in card_rows(soup):
        for href, n in collections.Counter(r[0] for r in rows if r[0] and not r[0].startswith("http")).items():
            if n > 1:
                out.append(f"SAME PAGE  {href} x{n}")
        for i, a in enumerate(rows):
            for b in rows[i + 1:]:
                if a[0] == b[0] or " · " in a[2] + b[2] or min(len(a[2].split()), len(b[2].split())) < 10:
                    continue
                if a[2] == b[2]:
                    out.append(f"SAME TEXT  {a[1]} | {b[1]}")
                    continue
                wa, wb = words(a[2]), words(b[2])
                ca, cb = {w for w in wa if w not in STOP and len(w) > 2}, {w for w in wb if w not in STOP and len(w) > 2}
                if len(phrases(wa) & phrases(wb)) >= 2 or len(ca & cb) / max(1, len(ca | cb)) >= 0.35:
                    out.append(f"SIMILAR    {a[1]} | {b[1]}\n             {a[2][:110]}\n             {b[2][:110]}")
    main = soup.find("main") or soup.body
    sents = [x.strip() for x in re.split(r"(?<=[.!?])\s+", main.get_text(" ", strip=True)) if len(x.split()) >= 9]
    out += [f"REPEAT x{n}   {s[:140]}" for s, n in collections.Counter(sents).items() if n > 1]
    return out


if __name__ == "__main__":
    total = 0
    for f in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        hits = check(f)
        if hits:
            print(f"== {os.path.relpath(f, SITE)}")
            print("\n".join("   " + h for h in hits))
            total += len(hits)
    print(f"{total} to look at")
