"""Find the latitude and longitude of every town in src/ref_towns.py and save them in src/towns_geo.json.

    python3 tools/towns_geo.py

Uses the free GeoNames list of places with 500+ people, which ships inside the Python package geonamescache
(downloaded from PyPI, which the cloud machines can reach). A town given its own `geo` in ref_towns.py is left alone.
Names GeoNames spells differently are in SAME below. A town that cannot be found stops the script: add a `geo` for it.
"""
import glob, json, os, subprocess, sys, tempfile, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
import ref_towns as T  # noqa: E402

SAME = {"blaenau ffestiniog": "blaenau-ffestiniog", "st asaph": "saint asaph", "st davids": "saint davids", "hay-on-wye": "hay"}
EXTRA = {"aberdaron": (52.8045, -4.7130), "corwen": (52.9790, -3.3770), "mumbles": (51.5700, -3.9930), "pontardawe": (51.7220, -3.8520)}

tmp = tempfile.mkdtemp()
subprocess.run([sys.executable, "-m", "pip", "download", "geonamescache", "--no-deps", "-q", "-d", tmp], check=True)
z = zipfile.ZipFile(glob.glob(os.path.join(tmp, "*.whl"))[0])
cities = json.loads(z.read("geonamescache/data/cities500.json")).values()
wales = {}
for c in cities:
    if c["countrycode"] == "GB" and c["admin1code"] == "WLS":
        wales.setdefault(c["name"].lower(), (round(c["latitude"], 4), round(c["longitude"], 4)))
out, missing = {}, []
for la, towns in T.TOWNS.items():
    for t in towns:
        if t["geo"]:
            continue
        k = t["en"].lower()
        k = SAME.get(k, k)
        if k in EXTRA:
            out[t["en"]] = EXTRA[k]
        elif k in wales:
            out[t["en"]] = wales[k]
        else:
            missing.append(t["en"])
if missing:
    sys.exit("Not found, give these a geo in src/ref_towns.py: " + ", ".join(missing))
json.dump(out, open(os.path.join(ROOT, "src", "towns_geo.json"), "w"), ensure_ascii=False, indent=0, sort_keys=True)
print(f"Saved {len(out)} places to src/towns_geo.json")
