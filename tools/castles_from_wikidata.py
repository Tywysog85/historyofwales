"""Make src/castles_data.json, the list of castle sites shown on castles.html.

    python3 tools/castles_from_wikidata.py /tmp/castles-src

Source: a Wikidata snapshot (CC0) of every item that is a castle or a kind of castle
(motte, ringwork, tower house and so on) with coordinates, saved on GitHub by the Shelf project
(github.com/yosefliberman770-source/shelf, data/historical/raw/wikidata-medieval). Many of the
Welsh items were imported from Cadw and Coflein records, so they carry Welsh names.

Steps: keep the points that fall inside Wales (the council areas in src/geo/la.json, plus a short
reach out to sea for coastal castles); drop hillforts, Roman forts, barrows, bridges, field names
and duplicate "parts" records; drop the border sites that are in England; add a few by hand.
The hand-written notes on who built each castle are in src/castles.py, not here.
"""
import json, math, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cache = sys.argv[1] if len(sys.argv) > 1 else "/tmp/castles-src"
os.makedirs(cache, exist_ok=True)
COMMIT = "369b6871cddc736f155f721a00315673776d061d"
BASE = f"https://raw.githubusercontent.com/yosefliberman770-source/shelf/{COMMIT}/data/historical/raw/wikidata-medieval/original/"
for f in ("castle.tsv", "castle.names.tsv", "labels.tsv"):
    if not os.path.exists(os.path.join(cache, f)):
        subprocess.run(["curl", "-sf", "--retry", "4", "-o", os.path.join(cache, f), BASE + f], check=True)

G = json.load(open(os.path.join(ROOT, "src", "geo", "map.json")))
LA = json.load(open(os.path.join(ROOT, "src", "geo", "la.json")))
sc, k, minx, maxy = G["sc"], G["k"], G["minx"], G["maxy"]


def proj(lat, lon):
    return ((lon - minx) * k * sc, (maxy - lat) * sc)


def polys(d):
    out, cur = [], []
    for cmd, x, y in re.findall(r"([MLZ]?)\s*(-?[\d.]+)[ ,](-?[\d.]+)", d):
        if cmd == "M" and cur:
            out.append(cur)
            cur = []
        cur.append((float(x), float(y)))
    if cur:
        out.append(cur)
    return out


LAP = {n: polys(d) for n, d in LA.items()}


def inside(p, poly):
    x, y = p
    c = False
    for i in range(len(poly)):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % len(poly)]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c


def segd(p, a, b):
    (px, py), (ax, ay), (bx, by) = p, a, b
    dx, dy = bx - ax, by - ay
    L = dx * dx + dy * dy
    t = 0 if L == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L))
    return math.hypot(px - ax - t * dx, py - ay - t * dy)


def locate(lat, lon):
    p = proj(lat, lon)
    for n, ps in LAP.items():
        if any(inside(p, poly) for poly in ps):
            return n, 0.0
    best = (None, 1e9)
    for n, ps in LAP.items():
        for poly in ps:
            for i in range(len(poly)):
                d = segd(p, poly[i], poly[(i + 1) % len(poly)])
                if d < best[1]:
                    best = (n, d)
    return best


def qid(s):
    return s.strip("<>").rsplit("/", 1)[1]


LABEL = {}
for line in open(os.path.join(cache, "labels.tsv"), encoding="utf-8"):
    f = line.rstrip("\n").split("\t")
    if len(f) > 1 and f[0].startswith("<"):
        m = re.match(r'"(.*)"@en', f[1])
        LABEL[qid(f[0])] = m.group(1) if m else f[1]
NAMES = {}
for line in open(os.path.join(cache, "castle.names.tsv"), encoding="utf-8"):
    if line.startswith("?"):
        continue
    f = line.rstrip("\n").split("\t")
    NAMES[qid(f[0])] = dict(x.split(":", 1) for x in f[1].strip('"').split("|") if ":" in x)

# kinds that make an item a castle for this map, and kinds that on their own do not
GOOD = {"motte-and-bailey castle", "motte", "ringwork castle", "fortified manor house", "castle ruin", "peel tower",
        "Welsh princes' castles", "tower house", "siege castle", "enclosure castle", "manor house", "moated site", "concentric castle"}
NOT = {"contour fort", "promontory fort", "hillfort", "partial contour fort", "marsh fort", "level terrain fort", "hillslope fort",
       "round barrow", "tumulus", "castrum", "castellum", "ancient Roman structure", "cairn", "ringfort", "bridge", "bridge castle",
       "suburb", "village", "pub", "church building", "vicus"}
BADNAME = re.compile(r"placename|fieldname|alleged|unoccupied parts|uninhabited parts|additional area|outer bank|siegeworks|siege castles|remains of hall|\(part\)", re.I)
CASTNAME = re.compile(r"castle|castell|motte|mound|tomen|domen|mwnt|ringwork|twmp|tump|moat|tower|twr|tŵr|gastell|bailey|mount\b", re.I)
# border sites that the coarse council outlines put in Wales but are in England, and things that are not castles
DROP = {"Q17662008", "Q17676913", "Q7259293", "Q5945293", "Q17664144", "Q24661642", "Q24661630", "Q17642082", "Q17664622",
        "Q20593949", "Q7597996", "Q5049667", "Q18162412", "Q5057267", "Q29491623", "Q38621299", "Q39011692", "Q39009824",
        "Q17742221", "Q29499966", "Q24660398", "Q38599645", "Q24659469", "Q38909334", "Q250115"}
# castles inside hillforts, or just off the simplified coast, that the rules above would miss
FORCE = {"Q6912480", "Q7808013", "Q1936320", "Q20589985", "Q1048693", "Q15097770", "Q39011935", "Q38621638"}
FIX = {"Q1048693": ("Castell y Bere", "Castell y Bere"), "Q2704850": ("Castell Coch", "Castell Coch")}

KIND = [("Welsh princes' castles", "stone"), ("motte-and-bailey castle", "mb"), ("motte", "motte"), ("ringwork castle", "ring"),
        ("siege castle", "siege"), ("tower house", "tower"), ("peel tower", "tower"), ("fortified manor house", "house"),
        ("manor house", "house"), ("moated site", "moat"), ("country house", "mansion"), ("mansion", "mansion"), ("castle ruin", "stone")]

out = []
for line in open(os.path.join(cache, "castle.tsv"), encoding="utf-8"):
    if line.startswith("?"):
        continue
    f = line.rstrip("\n").split("\t")
    q = qid(f[0])
    m = re.match(r"POINT\((\S+) (\S+)\)", f[1])
    if not m:
        continue
    lon, lat = float(m.group(1)), float(m.group(2))
    if not (51.3 < lat < 53.5 and -5.7 < lon < -2.6) or q in DROP:
        continue
    la, d = locate(lat, lon)
    if d >= 0.7 and q not in FORCE:
        continue
    lab = re.match(r'"(.*)"@en', f[2])
    en = lab.group(1) if lab else ""
    cy = NAMES.get(q, {}).get("cy", "")
    if q in FIX:
        en, cy = FIX[q]
    types = {LABEL.get(qid(t), "") for t in f[13].strip('"').split("|")} if len(f) > 13 and f[13] else set()
    sl = int(f[12].strip('"')) if len(f) > 12 and f[12].strip('"').isdigit() else 0
    if q not in FORCE:
        if not (en or cy) or BADNAME.search(en):
            continue
        good = bool(types & GOOD)
        if types & NOT and not good:
            continue
        if not good and sl == 0 and not CASTNAME.search(en + " " + cy):
            continue
    kind = next((v for t, v in KIND if t in types), "")
    out.append(dict(q=q, en=en or cy, cy=cy or en, lat=round(lat, 5), lon=round(lon, 5), la=la, kind=kind,
                    y=(f[3][:4] if len(f) > 3 and f[3][:1] in "012" else ""), sl=sl, wp="Welsh princes' castles" in types))
out.sort(key=lambda r: (-r["sl"], r["en"]))
json.dump(out, open(os.path.join(ROOT, "src", "castles_data.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(out), "castle sites")
