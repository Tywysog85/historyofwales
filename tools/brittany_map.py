"""Make the outline map of Wales, Cornwall and Brittany for the long read on the Britons in Brittany (story-brittany.html).

Reads Natural Earth (public domain, naturalearthdata.com) 1:10m land, map units (Wales) and states/provinces (Cornwall,
Devon and the five departments of historic Brittany), from the copies Natural Earth keeps on GitHub, clips them to the
box below, projects them and writes src/geo/brittany.json: the SVG paths and the numbers src/brittany.py needs to place
its pins. Run it once (needs `pip install shapely`); the result is committed, so the build does not need it.
"""
import json, math, os, urllib.request

from shapely.geometry import box, shape, mapping
from shapely.ops import unary_union

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NE = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/"
W_, E_, S_, N_ = -6.9, -0.6, 46.85, 53.55  # the box: Ynys Môn and the Dee down to the Loire
LAT0 = 50.2
W = 600  # width of the map in SVG units
K = math.cos(math.radians(LAT0))
SC = W / ((E_ - W_) * K)
H = round((N_ - S_) * SC, 1)


def load(name, cache):
    p = os.path.join(cache, name)
    if not os.path.exists(p):
        urllib.request.urlretrieve(NE + name, p)
    return json.load(open(p, encoding="utf-8"))


def xy(lon, lat):
    return ((lon - W_) * K * SC, (N_ - lat) * SC)


def path(geom, tol):
    g = geom.intersection(box(W_, S_, E_, N_)).simplify(tol, preserve_topology=True)
    out = []
    polys = [g] if g.geom_type == "Polygon" else list(getattr(g, "geoms", []))
    for p in polys:
        if p.geom_type != "Polygon" or p.area < 2e-4:  # leave out the smallest islets
            continue
        for ring in [p.exterior] + list(p.interiors):
            pts = [xy(*c) for c in ring.coords]
            out.append("M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z")
    return " ".join(out)


def main(cache=os.environ.get("NE_CACHE", "/tmp")):
    land = load("ne_10m_land.geojson", cache)
    mu = load("ne_10m_admin_0_map_units.geojson", cache)
    a1 = load("ne_10m_admin_1_states_provinces.geojson", cache)
    clip = box(W_ - 1, S_ - 1, E_ + 1, N_ + 1)
    land_g = unary_union([shape(f["geometry"]).intersection(clip) for f in land["features"] if shape(f["geometry"]).intersects(clip)])
    wales = unary_union([shape(f["geometry"]) for f in mu["features"] if f["properties"]["NAME"] == "Wales"])
    def a1u(names, admin):
        return unary_union([shape(f["geometry"]) for f in a1["features"] if f["properties"]["admin"] == admin and f["properties"]["name"] in names])
    corn = a1u({"Cornwall"}, "United Kingdom")
    devon = a1u({"Devon", "Plymouth", "Torbay"}, "United Kingdom")
    breizh = a1u({"Finistère", "Côtes-d'Armor", "Morbihan", "Ille-et-Vilaine", "Loire-Atlantique"}, "France")
    tol = 0.004
    out = dict(W=W, H=H, w=W_, n=N_, k=K, sc=SC, credit="Natural Earth (public domain)",
               land=path(land_g, tol), wales=path(wales, tol), cornwall=path(corn, tol), devon=path(devon, tol), brittany=path(breizh, tol))
    json.dump(out, open(os.path.join(ROOT, "src", "geo", "brittany.json"), "w", encoding="utf-8"))
    print("wrote src/geo/brittany.json", {k: len(v) for k, v in out.items() if isinstance(v, str)})


if __name__ == "__main__":
    main()
