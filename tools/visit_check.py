"""Check that the day planner in the browser (src/static/visitplan.js) makes the same days as the one in src/visitplan.py,
which makes the ready-made days out. Run it after changing either:  python3 tools/visit_check.py
It plans every ready-made day and a few hundred others (towns, lengths, interests, free entry, swaps) in Python, then the
same in Node with the real visitplan.js, and lists any day that differs. Needs Node."""
import json, os, random, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
sys.path.insert(0, SRC)
import data as D, visit as VS, ref_sites as ST, thumbs as TH, gallery_photos as GP, ref_towns as RT, towns as TW, visitplan as VP  # noqa: E402

geo = json.load(open(os.path.join(SRC, "geo", "map.json"), encoding="utf-8"))
VP.setup(dict(D=D, VS=VS, ST=ST, TH=TH, GP=GP, RT=RT, TW=TW, SRC=SRC, e=str, card_pic=lambda h: None, geo=geo))
S = VP.stops()
T = VP.towns()
ix = {s["id"]: i for i, s in enumerate(S)}
rnd = random.Random(7)
cases = []
for a in VP.AREAS:
    cases.append(dict(start=list(a[3][2:]), len="day", kinds=[], free=0, out=0, ex=[], first=None, pins=a[7].split(), fill=0))
for n in range(300):
    t = rnd.choice(T)
    c = dict(start=[t[2], t[3]], len=rnd.choice(list(VP.LENGTHS)), kinds=sorted(rnd.sample(range(6), rnd.choice([6, 6, 3, 2, 1]))),
             free=rnd.random() < .25, out=rnd.random() < .2, ex=[], first=None, pins=[], fill=1)
    if n % 5 == 0:
        f = rnd.randrange(len(S))
        c["first"], c["start"] = f, [S[f]["lat"], S[f]["lon"]]
    if n % 7 == 0:
        c["ex"] = [S[j]["id"] for j in rnd.sample(range(len(S)), 15)]
    cases.append(c)
for c in cases:
    r = VP.plan(S, tuple(c["start"]), c["len"], c["kinds"] or None, c["free"], c["out"], c["ex"], c["first"], [ix[p] for p in c["pins"]], bool(c["fill"]))
    c["want"] = [S[j]["id"] for j in r]

js = open(os.path.join(SRC, "static", "visitplan.js"), encoding="utf-8").read()
runner = """
const fs = require('fs');
const [payload, cases] = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
global.window = { VPD: payload };
global.document = { documentElement: { classList: { contains: () => false } }, getElementById: () => null };
eval(fs.readFileSync(process.argv[3], 'utf8'));
const IX = {}; payload.s.forEach((r, i) => IX[r[0]] = i);
let bad = 0;
cases.forEach((c, n) => {
  const got = window.VP_PLAN(c.start, c.len, c.kinds, c.free, c.out, c.ex, c.first, c.pins.map(p => IX[p]), !!c.fill);
  if (got.join() !== c.want.join()) { bad++; console.log('case ' + n + ' differs:\\n  python ' + c.want.join(' ') + '\\n  js     ' + got.join(' ')); }
});
console.log(cases.length + ' days planned, ' + bad + ' differ');
process.exit(bad ? 1 : 0);
"""
with tempfile.TemporaryDirectory() as d:
    pj, rj = os.path.join(d, "in.json"), os.path.join(d, "run.js")
    json.dump([VP._payload(S, T), cases], open(pj, "w", encoding="utf-8"), ensure_ascii=False)
    open(rj, "w").write(runner)
    sys.exit(subprocess.call(["node", rj, pj, os.path.join(SRC, "static", "visitplan.js")]))
