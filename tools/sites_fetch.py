"""Fetch the historic sites of Wales for sites.html. Runs on GitHub (.github/workflows/fetch-sites.yml), because the
Welsh Government's map server and Wikidata cannot be reached from where the site is built.

Source: Cadw's list of scheduled monuments, published on DataMapWales (Open Government Licence). Each monument is
kept as a point (the middle of its outline) with its name and whatever type and period fields the layer has.

Writes:
  tools/data/sites_cadw.json   every monument: {"n": name, "lat", "lon", "p": {other short fields}}
  tools/data/sites_probe.txt   what the server offered, so the layer and field names can be checked from the cloud
"""
import json, os, re, sys, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "tools", "data")
os.makedirs(OUT, exist_ok=True)
UA = {"User-Agent": "historyofwales-site-builder/1.0 (+https://historyofwales.cymru)"}
OWS = "https://datamap.gov.wales/geoserver/ows"
probe = []


def get(url, timeout=180):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def layers():
    """Layer names on the server that look like Cadw's scheduled monuments."""
    try:
        xml = get(OWS + "?service=WFS&version=1.1.0&request=GetCapabilities").decode("utf-8", "replace")
    except Exception as ex:  # noqa: BLE001
        probe.append(f"GetCapabilities failed: {ex}")
        return []
    names = re.findall(r"<(?:wfs:)?Name>([^<]+)</(?:wfs:)?Name>", xml)
    hits = [n for n in names if re.search(r"SAM|[Ss]chedul|[Mm]onument|Cadw", n)]
    probe.append(f"{len(names)} layers; matching: {hits}")
    return hits


def centre(geom):
    pts = []

    def walk(c):
        if isinstance(c, (list, tuple)) and len(c) >= 2 and isinstance(c[0], (int, float)) and isinstance(c[1], (int, float)):
            pts.append(c[:2])
        elif isinstance(c, (list, tuple)):
            for x in c:
                walk(x)
    walk((geom or {}).get("coordinates"))
    if not pts:
        return None
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    a, b = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    return (a, b) if a > 40 else (b, a)  # (lat, lon), whichever order the server used


def fetch(layer):
    q = urllib.parse.urlencode({"service": "WFS", "version": "1.0.0", "request": "GetFeature", "typeName": layer,
                                "outputFormat": "application/json", "srsName": "EPSG:4326"})
    data = json.loads(get(OWS + "?" + q, timeout=600))
    feats = data.get("features", [])
    probe.append(f"{layer}: {len(feats)} features")
    if feats:
        probe.append("fields: " + json.dumps(feats[0].get("properties", {}), ensure_ascii=False)[:1500])
        probe.append("geometry: " + json.dumps(feats[0].get("geometry"))[:300])
        if len(feats) > 1:
            probe.append("second: " + json.dumps(feats[1].get("properties", {}), ensure_ascii=False)[:1500])
    return feats


LAYERS = {"sites_cadw.json": "inspire-wg:Cadw_SAM",                      # every scheduled monument
          "sites_guardian.json": "geonode:cadw_guardianshipmonuments"}    # the sites Cadw looks after and opens to visitors


def rows_of(feats):
    rows = []
    for f in feats:
        c = centre(f.get("geometry"))
        p = {k: (v.strip() if isinstance(v, str) else v) for k, v in (f.get("properties") or {}).items()}
        if not c:
            continue
        name = next((str(v) for k, v in p.items() if re.search(r"name|enw", k, re.I) and v and not re.search(r"cy|welsh", k, re.I)), "")
        short = {k: v for k, v in p.items() if v not in (None, "") and len(str(v)) < 200 and not re.search(r"shape|area|len|geom|fid|objectid|^Report$|easting|northing|DesignationDate", k, re.I)}
        rows.append({"n": name, "lat": round(c[0], 5), "lon": round(c[1], 5), "p": short})
    return rows


def main():
    layers()  # only to note what the server offers
    for out, layer in LAYERS.items():
        try:
            feats = fetch(layer)
        except Exception as ex:  # noqa: BLE001
            probe.append(f"{layer}: failed: {ex}")
            continue
        if not 100 <= len(feats) <= 20000:  # not the layer we expected: keep nothing rather than the wrong thing
            probe.append(f"{layer}: {len(feats)} features is not a list of monuments; skipped")
            continue
        rows = rows_of(feats)
        probe.append(f"{out}: kept {len(rows)}")
        json.dump(rows, open(os.path.join(OUT, out), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "sites_probe.txt"), "w", encoding="utf-8").write("\n".join(probe) + "\n")
    print("\n".join(probe))


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:  # noqa: BLE001  never fail the run (a failed run emails the site owner); say what went wrong instead
        probe.append(f"stopped: {type(ex).__name__}: {ex}")
        open(os.path.join(OUT, "sites_probe.txt"), "w", encoding="utf-8").write("\n".join(probe) + "\n")
        print("\n".join(probe))
