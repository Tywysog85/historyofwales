"""The weekly quiz (weekly-quiz.html): ten new questions every Monday, the same for everyone, with a leaderboard.

Each week is written once and then kept in src/quiz_weeks.json, so a week's questions and answers never change after it
is made (the leaderboard scores against them). The build adds any missing weeks up to a year ahead; a week that has
gone out is never rewritten. To change a question, edit quiz_weeks.json by hand.

Every question comes from what the site already says (On this day, the people, the places, Words to know, the tales),
in English and Welsh, so the facts and the wording follow the site's own rules. A week has:
  * three or four questions on the week's anniversaries (the same days the Monday email covers): in which year, what
    happened on a day, who was born or died, whose feast day it is
  * a figure from history, a photograph of a place to name, a place from a clue, a Welsh word, which came first,
    and a tale from Wales (never Arthur: his story is history on this site, not a tale)
Nothing comes round again until everything of its kind has been used.

The answer key for the leaderboard (worker/, a Cloudflare Worker) is written by `python3 src/weeklyquiz.py worker`.
"""
import datetime, json, os, random, re, sys, zlib

HERE = os.path.dirname(os.path.abspath(__file__))
WEEKS_FILE = os.path.join(HERE, "quiz_weeks.json")
HIDDEN_FILE = os.path.join(HERE, "quiz_hidden.json")   # nicknames taken off the leaderboard (Ifan's say)
FIRST = datetime.date(2026, 11, 9)   # week 1 (a Monday)
AHEAD = 53   # weeks written ahead of today

MON_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
MON_CY = ["Ionawr", "Chwefror", "Mawrth", "Ebrill", "Mai", "Mehefin", "Gorffennaf", "Awst", "Medi", "Hydref", "Tachwedd", "Rhagfyr"]
# words too common to give a name away
_COMMON = {"saint", "sant", "santes", "king", "brenin", "prince", "tywysog", "lord", "arglwydd", "the", "and", "of", "ap", "ab", "ferch", "verch",
           "castle", "castell", "abbey", "abaty", "church", "eglwys", "cathedral", "eglwys", "lady", "sir", "great", "mawr", "fawr", "with", "from",
           "wales", "cymru", "welsh", "bishop", "esgob", "queen", "brenhines", "y", "yr", "a", "o", "an", "fort", "caer", "hill", "bryn"}


def monday(d):
    return d - datetime.timedelta(days=d.weekday())


def week_no(wk):
    return (datetime.date.fromisoformat(wk) - FIRST).days // 7 + 1


def _date(md, y, cy):
    m, d = map(int, md.split("-"))
    return f"{d} {(MON_CY if cy else MON_EN)[m - 1]}" + (f" {y}" if y is not None else "")


_YEAR = re.compile(r"\b(1[0-9]{3}|20[0-9]{2}|[1-9][0-9]{2})\b")


def _blank(s):
    return _YEAR.sub("____", s)


def _tokens(name):
    return {w for w in re.findall(r"[\wâêîôûŵŷäëïöüÿáéíóú’']+", name.lower()) if len(w) > 3 and w not in _COMMON}


def _leaks(name, *texts):
    toks = _tokens(name)
    low = " ".join(texts).lower()
    return any(re.search(r"\b" + re.escape(t) + r"\b", low) for t in toks)


def _span_cy(s):
    """A life span in Welsh, as the people pages write it."""
    s = s.replace("fl. c. ", "fl. tua ").replace("c. ", "tua ").replace("d. ", "m. ").replace("b. ", "g. ").replace(" BC", " CC").replace(" AD", " OC")
    return "" if re.search(r"[A-Za-z]{4,}", s) else s   # "6th century", "born 1960": left out rather than half in English


def _hide(s, names):
    """s with any word of the names hidden, so a summary does not give its own answer away."""
    for t in set().union(*(_tokens(n) for n in names)):
        s = re.sub(r"(?i)\b" + re.escape(t) + r"\b", "____", s)
    return s


def _first_sentence(s):
    m = re.match(r"(.+?[.!?])(\s|$)", s)
    return m.group(1) if m else s


class Pool:
    """Everything a quiz can be made from, with what has already been used."""

    def __init__(self, otd, people, places, place_pic, words, tales, events, page_pic):
        self.otd = [r for r in otd if r[2] in ("ev", "born", "died", "feast") and r[0] != "02-29"]
        self.people = [p for p in people if p[5] and p[3]]
        self.places = places
        self.place_pic = place_pic   # place id -> (picture, credit) for the photographs
        self.words = words
        self.tales = tales
        self.events = [e for e in events if e[1] and e[1] > 0]
        self._pp = page_pic          # page -> small picture, or None
        self.used = {"otd": set(), "person": set(), "pic": set(), "clue": set(), "word": set(), "tale": set(), "first": set()}

    def page_pic(self, r):
        """The picture of an On this day row (a site path), or None."""
        for p in r[9:11]:
            if p and not p.startswith(("i:", "http")):
                return p
        return self.page_pic_for(r[7]) if r[7] else None

    def page_pic_for(self, page):
        return self._pp(page) if page else None

    def take(self, kind, items, key, rng):
        """The next unused item (in a fixed shuffled order); when all are used, start again."""
        left = [x for x in items if key(x) not in self.used[kind]]
        if not left:
            self.used[kind] = set()
            left = list(items)
        x = rng.choice(left)
        self.used[kind].add(key(x))
        return x


def _opts(rng, right, wrong, label):
    """Four options with the right one in a random place: (options, answer index). Wrong ones that read the same as
    another option are passed over."""
    xs, seen = [right], {label(right)[0].lower()}
    for w in wrong:
        if label(w)[0].lower() not in seen and len(xs) < 4:
            xs.append(w); seen.add(label(w)[0].lower())
    if len(xs) < 4:
        raise ValueError("not enough different options")
    rng.shuffle(xs)
    return [label(x) for x in xs], xs.index(right)


def _otd_key(r):
    return f"{r[0]}|{r[1]}|{r[3]}"


def q_year(P, r, rng):
    y = r[1]
    cands = sorted({e[1] for e in P.events if 8 <= abs(e[1] - y) <= 160} | {y + d for d in (-40, -25, 25, 40, 60) if y + d < 2026})
    wrong = []
    for c in rng.sample(cands, len(cands)):
        if all(abs(c - w) >= 6 for w in wrong + [y]):
            wrong.append(c)
        if len(wrong) == 3:
            break
    xs = sorted([y] + wrong)
    return dict(k="year", tw=[_date(r[0], None, False), _date(r[0], None, True)], h=["In which year did this happen?", "Ym mha flwyddyn y digwyddodd hyn?"],
                t=[_blank(r[3]), _blank(r[4])], c=[_blank(r[5]), _blank(r[6])], o=[[str(x), str(x)] for x in xs], a=xs.index(y),
                x=[f"{_date(r[0], y, False)}. {r[5]}", f"{_date(r[0], y, True)}. {r[6]}"], l=r[7], p=P.page_pic(r))


def q_what(P, r, rng):
    y = r[1]
    others = [x for x in P.otd if x[2] == "ev" and x[1] and x[0] != r[0] and x[3] != r[3] and abs(x[1] - y) <= 120]
    if len(others) < 3:
        others = [x for x in P.otd if x[2] == "ev" and x[1] and x[0] != r[0] and x[3] != r[3]]
    wrong = rng.sample(others, min(len(others), 8))
    o, a = _opts(rng, r, wrong, lambda x: [x[3], x[4]])
    return dict(k="what", tw=[_date(r[0], None, False), _date(r[0], None, True)], h=[f"What happened on {_date(r[0], y, False)}?", f"Beth ddigwyddodd ar {_date(r[0], y, True)}?"],
                o=o, a=a, x=[r[5], r[6]], l=r[7], p=P.page_pic(r))


def q_born(P, r, rng):
    y = r[1]
    others = [x for x in P.otd if x[2] in ("born", "died") and x[3] != r[3] and x[1] and abs(x[1] - y) <= 150 and not _leaks(x[3], r[5]) and not (_tokens(x[3]) & _tokens(r[3]))]
    if len(others) < 3:
        others = [x for x in P.otd if x[2] in ("born", "died") and x[3] != r[3] and x[1] and not _leaks(x[3], r[5])]
    seen, wrong = {r[3]}, []
    for x in rng.sample(others, len(others)):
        if x[3] not in seen:
            seen.add(x[3]); wrong.append(x)
        if len(wrong) == 6:
            break
    o, a = _opts(rng, r, wrong, lambda x: [x[3], x[4]])
    born = r[2] == "born"
    return dict(k="born", tw=[_date(r[0], None, False), _date(r[0], None, True)], h=[f"Who {'was born' if born else 'died'} on {_date(r[0], y, False)}?",
                                   f"Pwy {'a anwyd' if born else 'fu farw'} ar {_date(r[0], y, True)}?"],
                c=[r[5], r[6]], o=o, a=a, x=[f"{r[3]}. {r[5]}", f"{r[4]}. {r[6]}"], l=r[7], p=P.page_pic(r))


def q_feast(P, r, rng):
    others = [x for x in P.otd if x[2] == "feast" and x[3] != r[3] and x[0] != r[0]]
    wrong = rng.sample(others, min(len(others), 8))
    o, a = _opts(rng, r, wrong, lambda x: [x[3], x[4]])
    return dict(k="feast", tw=[_date(r[0], None, False), _date(r[0], None, True)], h=[f"Whose feast day falls on {_date(r[0], None, False)}?", f"Gŵyl pwy sydd ar {_date(r[0], None, True)}?"],
                o=o, a=a, x=[f"{r[3]}, {_date(r[0], None, False)}. {r[5]}", f"{r[4]}, {_date(r[0], None, True)}. {r[6]}"], l=r[7], p=P.page_pic(r))


def q_who(P, rng, skip=()):
    for _ in range(200):
        p = P.take("person", P.people, lambda p: p[0], rng)
        if p[3] in skip or _leaks(p[3], p[5], p[6]):
            continue
        bio_en, bio_cy = _first_sentence(p[7]), _first_sentence(p[8])
        if _leaks(p[3], bio_en, bio_cy) or _leaks(p[4], bio_en, bio_cy):
            bio_en = bio_cy = ""
        same = [x for x in P.people if x[1] == p[1] and x[0] != p[0] and not (_tokens(x[3]) & _tokens(p[3]))]
        if len(same) < 3:
            same = [x for x in P.people if x[0] != p[0] and not (_tokens(x[3]) & _tokens(p[3]))]
        wrong = rng.sample(same, min(len(same), 8))
        o, a = _opts(rng, p, wrong, lambda x: [x[3], x[4]])
        span, span_cy = p[2], _span_cy(p[2])
        return dict(k="who", h=["Which figure from Welsh history is this?", "Pa ffigwr o hanes Cymru yw hwn?"],
                    t=[f"‘{p[5]}’", f"‘{p[6]}’"], c=[" · ".join(x for x in (span, bio_en) if x), " · ".join(x for x in (span_cy, bio_cy) if x)],
                    o=o, a=a, x=[p[7], p[8]], l=f"person-{p[0]}.html", p=P.page_pic_for(f"person-{p[0]}.html"))
    raise RuntimeError("no person")


def _kind(name):
    for w in ("Castle", "Abbey", "Cathedral", "Cave", "Priory", "Hall", "House", "Mine", "Fort", "Chapel", "Church", "Bridge"):
        if w.lower() in name.lower():
            return w
    return ""


def q_pic(P, rng):
    have = [p for p in P.places if p["id"] in P.place_pic]
    pl = P.take("pic", have, lambda p: p["id"], rng)
    P.used["clue"].add(pl["id"])
    k = _kind(pl["en"])
    same = [x for x in have if x["id"] != pl["id"] and _kind(x["en"]) == k and k]
    rng.shuffle(same)
    if len(same) < 3:
        era = [x for x in have if x["id"] != pl["id"] and x["era"] == pl["era"] and x not in same]
        rng.shuffle(era)
        same += era
    if len(same) < 3:
        same += [x for x in have if x["id"] != pl["id"] and x not in same]
    wrong = same[:8]
    o, a = _opts(rng, pl, wrong, lambda x: [x["en"], x["cy"]])
    pic, cr = P.place_pic[pl["id"]]
    return dict(k="pic", h=["Which place is this?", "Pa le yw hwn?"], ph=pic, cr=cr, o=o, a=a, x=[pl["dEn"], pl["dCy"]], l=f"place-{pl['id']}.html")


def q_clue(P, rng):
    ok = [p for p in P.places if not _leaks(p["en"], p["dEn"], p["dCy"]) and not _leaks(p["cy"], p["dEn"], p["dCy"])]
    pl = P.take("clue", ok, lambda p: p["id"], rng)
    k = _kind(pl["en"])
    pool = [x for x in P.places if x["id"] != pl["id"] and not _leaks(x["en"], pl["dEn"])]
    same = [x for x in pool if k and _kind(x["en"]) == k]
    rng.shuffle(same)
    if len(same) < 3:
        era = [x for x in pool if x["era"] == pl["era"] and x not in same and not (_kind(x["en"]) and not k)]
        rng.shuffle(era)
        same += era
    if len(same) < 3:
        same += [x for x in pool if x not in same]
    wrong = same[:8]
    o, a = _opts(rng, pl, wrong, lambda x: [x["en"], x["cy"]])
    return dict(k="clue", h=["Which place in Wales is this?", "Pa le yng Nghymru yw hwn?"], c=[pl["dEn"], pl["dCy"]], o=o, a=a,
                x=[f"{pl['en']} ({pl['year']}). {pl['dEn']}", f"{pl['cy']} ({pl['year']}). {pl['dCy']}"], l=f"place-{pl['id']}.html",
                p=P.place_pic.get(pl["id"], (None,))[0])


def q_word(P, rng):
    w = P.take("word", P.words, lambda w: w[0], rng)
    meaning = lambda x: re.sub(r"\s*\(.*?\)", "", x[3])
    others = [x for x in P.words if x[0] != w[0] and meaning(x) != meaning(w)]
    wrong = rng.sample(others, 8)
    o, a = _opts(rng, w, wrong, lambda x: [meaning(x), meaning(x)])
    return dict(k="word", h=[f"What does the Welsh word ‘{w[0]}’ mean?", f"Beth yw ystyr y gair ‘{w[0]}’ yn Saesneg?"], o=o, a=a,
                x=[f"{w[0]} ({w[2]}): {w[3]}. {w[6]}", f"{w[0]}: {w[3]}. {w[7]}"], l=(w[8] if len(w) > 8 else "") or "welsh.html")


def q_first(P, rng):
    for _ in range(400):
        anchor = rng.choice(P.events)
        if anchor[5] in P.used["first"]:
            continue
        near = [e for e in P.events if 0 < abs(e[1] - anchor[1]) <= 250 and e[5] not in P.used["first"]]
        rng.shuffle(near)
        pick = [anchor]
        for e in near:
            if all(abs(e[1] - x[1]) >= 15 for x in pick) and all(not _leaks(e[5], x[5]) for x in pick):
                pick.append(e)
            if len(pick) == 4:
                break
        if len(pick) < 4:
            continue
        for e in pick:
            P.used["first"].add(e[5])
        first = min(pick, key=lambda e: e[1])
        rng.shuffle(pick)
        order = sorted(pick, key=lambda e: e[1])
        return dict(k="first", h=["Which of these came first?", "Pa un o’r rhain ddaeth gyntaf?"], o=[[e[5], e[6]] for e in pick], a=pick.index(first),
                    x=["In order: " + "; ".join(f"{e[5]} ({e[1]})" for e in order) + ".", "Yn eu trefn: " + "; ".join(f"{e[6]} ({e[1]})" for e in order) + "."])
    raise RuntimeError("no events")


def q_tale(P, rng):
    t = P.take("tale", P.tales, lambda t: t["id"], rng)
    wrong = rng.sample([x for x in P.tales if x["id"] != t["id"]], 8)
    o, a = _opts(rng, t, wrong, lambda x: [x["en"], x["cy"]])
    return dict(k="tale", h=["Which tale from Wales is this?", "Pa chwedl o Gymru yw hon?"], c=[_hide(t["sumEn"], [t["en"], t["cy"]]), _hide(t["sumCy"], [t["en"], t["cy"]])], o=o, a=a,
                x=[f"{t['en']}. {t['sumEn']}", f"{t['cy']}. {t['sumCy']}"], l=t["link"], p=P.page_pic_for(t["link"]))


def make_week(P, wk):
    """The ten questions for the week starting on Monday wk (a date)."""
    rng = random.Random(zlib.crc32(wk.isoformat().encode()))
    days = {(wk + datetime.timedelta(days=i)).strftime("%m-%d") for i in range(7)}
    rows = [r for r in P.otd if r[0] in days and _otd_key(r) not in P.used["otd"]]
    if len(rows) < 3:   # a second year round: the same days again, any not yet asked first
        rows += [r for r in P.otd if r[0] in days and r not in rows]
    evs = [r for r in rows if r[2] == "ev" and r[1]]
    bd = [r for r in rows if r[2] in ("born", "died") and r[1] and r[1] > 0 and not _leaks(r[3], r[5], r[6])]
    fe = [r for r in rows if r[2] == "feast"]
    rng.shuffle(evs); rng.shuffle(bd); rng.shuffle(fe)
    week = []   # this week's anniversaries: two events, a birth or death, a feast or another event, a fourth if there is one
    plan = evs[:2] + bd[:1] + (fe[:1] or evs[2:3] or bd[1:2])
    rest = [r for r in evs[2:] + bd[1:] + fe[1:] if r not in plan]
    plan += rest[:1]
    names = set()
    for i, r in enumerate(plan[:4]):
        P.used["otd"].add(_otd_key(r))
        if r[2] == "ev":
            week.append(q_year(P, r, rng) if (i % 2 == 0) else q_what(P, r, rng))
        elif r[2] == "feast":
            week.append(q_feast(P, r, rng))
        else:
            names.add(r[3])
            week.append(q_born(P, r, rng))
    tw = week[:3]
    extra = week[3:4]
    qs = tw + [q_who(P, rng, names), q_pic(P, rng), q_word(P, rng), q_first(P, rng), q_clue(P, rng), q_tale(P, rng)]
    qs += extra or [q_who(P, rng, names)]
    while len(qs) < 10:
        qs.insert(3, q_first(P, rng) if len(qs) % 2 else q_who(P, rng, names))
    for q in qs:
        for k in [k for k, v in q.items() if v in (None, "", [])]:
            del q[k]
    return dict(n=week_no(wk.isoformat()), qs=qs[:10])


def load():
    try:
        with open(WEEKS_FILE, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def ensure(P, today=None):
    """Add any missing weeks, from week 1 to AHEAD weeks after today; weeks already written are kept as they are."""
    weeks = load()
    for key, wk in sorted(weeks.items()):   # mark what has been asked, so new weeks ask about other things
        for q in wk["qs"]:
            k = q["k"]
            if k == "who" and q.get("l"):
                P.used["person"].add(q["l"][7:-5])
            elif k == "pic":
                P.used["pic"].add(q["l"][6:-5]); P.used["clue"].add(q["l"][6:-5])
            elif k == "clue":
                P.used["clue"].add(q["l"][6:-5])
            elif k == "tale":
                P.used["tale"].update(t["id"] for t in P.tales if t["link"] == q.get("l"))
            elif k == "first":
                P.used["first"].update(o[0] for o in q["o"])
            elif k == "word":
                P.used["word"].add(re.search(r"‘(.+?)’", q["h"][0]).group(1))
    asked = {  # the anniversaries already asked about
(q.get("x") or [""])[0] for wk in weeks.values() for q in wk["qs"] if q.get("tw")}
    for r in P.otd:
        if any(r[5] in a for a in asked):
            P.used["otd"].add(_otd_key(r))
    today = today or datetime.date.today()
    end = monday(today) + datetime.timedelta(weeks=AHEAD)
    wk, added = FIRST, 0
    while wk <= end:
        key = wk.isoformat()
        if key not in weeks:
            weeks[key] = make_week(P, wk)
            added += 1
        wk += datetime.timedelta(weeks=1)
    if added:
        with open(WEEKS_FILE, "w", encoding="utf-8") as f:
            f.write("{\n" + ",\n".join(f"{json.dumps(k)}: {json.dumps(weeks[k], ensure_ascii=False, separators=(',', ':'))}" for k in sorted(weeks)) + "\n}\n")
    return weeks, added


def hidden():
    try:
        with open(HIDDEN_FILE, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


if __name__ == "__main__" and sys.argv[1:] == ["worker"]:
    # the answer key and the hidden nicknames for the leaderboard (worker/src/gen.json), made in deploy.yml before the worker goes up
    ws = load()
    out = dict(keys={k: [q["a"] for q in w["qs"]] for k, w in ws.items()}, hidden=[h.lower() for h in hidden()])
    path = os.path.join(os.path.dirname(HERE), "worker", "src", "gen.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, separators=(",", ":"))
    print(f"Wrote the answer key for {len(out['keys'])} weeks to {path}")
