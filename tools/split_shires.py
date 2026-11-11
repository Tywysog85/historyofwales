"""Cut Powys and Gwynedd into their historic shires along the real old borders, and save them as src/geo/shires.json.

The council areas in src/geo/la.json have Powys and Gwynedd whole. The Kingdoms maps need Montgomeryshire, Radnorshire and
Brecknockshire, and Caernarfonshire and Meirionnydd. Those old borders mostly follow rivers and hill ridges: Radnorshire and
Brecknockshire are parted by the River Wye (Gwy) and then the Elan and Claerwen; Radnorshire and Montgomeryshire by the
Kerry Hills and the hills south of Llangurig; Caernarfonshire and Meirionnydd by the Glaslyn and Dwyryd estuaries and the
Moelwyn ridge. The lines below trace them by hand from known places on each side, so they are close but not survey-exact.

Run once after changing a line (needs: pip install shapely). build.py reads the result; the website build does not need shapely.
"""
import json, os, re
from shapely.geometry import Polygon
from shapely.ops import unary_union

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
geo = json.load(open(os.path.join(ROOT, "src", "geo", "map.json")))
la = json.load(open(os.path.join(ROOT, "src", "geo", "la.json")))
sc, k, minx, maxy = geo["sc"], geo["k"], geo["minx"], geo["maxy"]


def P(lon, lat):
    return ((lon - minx) * k * sc, (maxy - lat) * sc)


def poly(d):
    rings = [[(float(a), float(b)) for a, b in re.findall(r"(-?[\d.]+) (-?[\d.]+)", r)] for r in re.findall(r"M([^MZ]+)Z", d)]
    return unary_union([Polygon(r).buffer(0) for r in rings if len(r) > 2])


def side(line, far_lat):
    """The area between a border line (lon, lat points, east to west or west to east) and a far-off latitude."""
    pts = [P(*p) for p in line]
    a, b = line[0], line[-1]
    return Polygon(pts + [P(b[0], far_lat), P(a[0], far_lat)]).buffer(0)


# Montgomeryshire | Radnorshire: the Kerry Hills, then south of Llangurig, west to the Ceredigion border.
MONT_RAD = [(-2.90, 52.42), (-3.05, 52.425), (-3.12, 52.435), (-3.22, 52.452), (-3.30, 52.445), (-3.38, 52.425), (-3.45, 52.40),
            (-3.52, 52.385), (-3.58, 52.372), (-3.66, 52.37), (-3.74, 52.38), (-3.95, 52.385)]
# Radnorshire | Brecknockshire: the Wye from Hay up past Builth to the Elan, then the Elan and Claerwen west.
RAD_BRE = [(-2.90, 52.09), (-3.05, 52.085), (-3.125, 52.077), (-3.17, 52.06), (-3.21, 52.043), (-3.27, 52.033), (-3.31, 52.046),
           (-3.335, 52.075), (-3.36, 52.11), (-3.39, 52.14), (-3.405, 52.154), (-3.42, 52.18), (-3.44, 52.214), (-3.47, 52.245),
           (-3.50, 52.27), (-3.52, 52.287), (-3.57, 52.282), (-3.63, 52.272), (-3.70, 52.262), (-3.78, 52.258), (-3.95, 52.26)]
# Caernarfonshire | Meirionnydd: out of Tremadog Bay up the Traeth Bach and Glaslyn, over the Moelwyn, north of Blaenau, east.
CAE_MEI = [(-4.30, 52.85), (-4.16, 52.895), (-4.105, 52.915), (-4.075, 52.935), (-4.055, 52.955), (-4.035, 52.975),
           (-4.00, 52.995), (-3.96, 53.012), (-3.92, 53.018), (-3.86, 53.01), (-3.78, 52.995), (-3.60, 52.98)]


def path(g):
    polys = [g] if g.geom_type == "Polygon" else [x for x in g.geoms if x.geom_type == "Polygon"]
    out = []
    for p in polys:
        if p.area < 4:
            continue
        for ring in [p.exterior] + list(p.interiors):
            c = list(ring.coords)[:-1]
            out.append("M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in c) + " Z")
    return " ".join(out)


powys, gwynedd = poly(la["Powys"]), poly(la["Gwynedd"])
mont = powys.intersection(side(MONT_RAD, 53.5))
bre = powys.intersection(side(RAD_BRE, 51.0))
rad = powys.difference(mont).difference(bre)
mei = gwynedd.intersection(side(CAE_MEI, 52.0))
cae = gwynedd.difference(mei)
out = {"Montgomeryshire": path(mont), "Radnorshire": path(rad), "Brecknockshire": path(bre), "Meirionnydd": path(mei), "Caernarfonshire": path(cae)}
for n, g in [("Montgomeryshire", mont), ("Radnorshire", rad), ("Brecknockshire", bre), ("Meirionnydd", mei), ("Caernarfonshire", cae)]:
    print(f"{n}: area {g.area:.0f}")
json.dump(out, open(os.path.join(ROOT, "src", "geo", "shires.json"), "w"), indent=0)
