"""Make src/geo/north.json: the outline of northern Britain, Wales, Man and the east of Ireland for the map of the Old North
(story-hen-ogledd.html, src/hen_ogledd.py).

Natural Earth 1:10m "admin 0 map units" (public domain): download ne_10m_admin_0_map_units.geojson from
https://github.com/nvkelso/natural-earth-vector (geojson folder) and pass its path:  python3 tools/north_map.py <path>
Needs shapely (pip install shapely). The projection is the one the kingdoms map uses (x = (lon - minx) * k * sc,
y = (maxy - lat) * sc, with k = cos of the middle latitude), so build.py's pin_map() can place pins on it.
"""
import json, math, os, sys
from shapely.geometry import shape, box, Polygon, MultiPolygon
from shapely.ops import unary_union

MINX, MAXX, MINY, MAXY = -6.75, 0.35, 52.25, 56.75   # lon / lat of the frame
W = 600

src = json.load(open(sys.argv[1], encoding="utf-8"))
want = {"Wales": "wales", "England": "land", "Scotland": "land", "Isle of Man": "land", "Ireland": "ire", "N. Ireland": "ire"}
k = math.cos(math.radians((MINY + MAXY) / 2))
sc = W / ((MAXX - MINX) * k)
H = round((MAXY - MINY) * sc, 1)
frame = box(MINX - .4, MINY - .4, MAXX + .4, MAXY + .4)   # a little beyond the frame, so the cut edges fall outside the picture
layers = {}
for f in src["features"]:
    n = f["properties"].get("NAME")
    if n in want:
        g = shape(f["geometry"]).intersection(frame).simplify(0.006, preserve_topology=True)
        layers.setdefault(want[n], []).append(g)


def path(g):
    polys = [g] if isinstance(g, Polygon) else list(getattr(g, "geoms", []))
    out = []
    for p in polys:
        if p.is_empty or p.area < 0.0004:   # drop the smallest islets
            continue
        pts = [((x - MINX) * k * sc, (MAXY - y) * sc) for x, y in p.exterior.coords]
        out.append("M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts[:-1]) + "Z")
    return "".join(out)


res = dict(W=W, H=H, minx=MINX, maxy=MAXY, k=k, sc=sc, **{name: path(unary_union(gs)) for name, gs in layers.items()})
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "geo", "north.json")
json.dump(res, open(out, "w", encoding="utf-8"), separators=(",", ":"))
print(out, W, H, {k_: len(v) for k_, v in res.items() if isinstance(v, str)})
