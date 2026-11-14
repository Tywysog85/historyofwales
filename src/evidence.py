"""Evidence labels: a small tag that says how we know about an event or a person (Ifan, 14 November 2026).

There are exactly three labels, in Ifan's words. Do not add others, and never use "myth", "legend",
"tradition", "later account" or "literary character" as a label (EDITORIAL.md):

  archaeology      known from what has been found in the ground and the monuments that still stand
  early chronicle  handed down in the early chronicles, poems, stories, genealogies and Lives of the saints
  recorded         written down at the time or soon after (inscriptions of the time count as recorded)

Where the labels show:
  - teachers' worksheets: the "match the event to the date" sheets, the pack timelines and the card sort (on screen and printed)
  - the People page cards and the top of every person page
  - the timeline rows of the first five ages (to 1100), on timeline.html and the age pages; after 1100 nearly everything is recorded

How an item gets its label: the defaults below by age, then the lists of exceptions. A new event or person
in the first five ages that does not fit its age's default goes into one of the lists, by its English title
(events) or its slug (people). Everything from 1100 on is "recorded" unless it is in a list.
"""

LABELS = {
    "a": ("archaeology", "archaeoleg"),
    "c": ("early chronicle", "cronicl cynnar"),
    "r": ("recorded", "wedi’i gofnodi"),
}

KEY_EN = [("archaeology", "known from what has been found in the ground and the monuments that still stand"),
          ("early chronicle", "handed down in the early chronicles, poems, stories, genealogies and Lives of the saints"),
          ("recorded", "written down at the time or soon after")]
KEY_CY = [("archaeoleg", "yr hyn a wyddom o’r hyn a gafwyd yn y ddaear a’r henebion sy’n dal i sefyll"),
          ("cronicl cynnar", "wedi’i drosglwyddo yn y croniclau cynnar, y cerddi, y storïau, yr achau a bucheddau’r seintiau"),
          ("wedi’i gofnodi", "wedi’i ysgrifennu ar y pryd neu’n fuan wedyn")]

# The ages where the timeline rows wear a label (before 1100).
EARLY = ("ancient", "britons", "roman", "saints", "kings")

# ---------- events: default by age ----------
EVENT_DEFAULT = {"ancient": "a", "britons": "a", "roman": "r", "saints": "c", "kings": "r"}

# ---------- events: exceptions, by English title ----------
EVENT_CHRONICLE = {
    "Brutus comes to the Island of Britain", "The faith of Christ reaches Britain",
    "Brân Fendigaid brings the faith from Rome", "Joseph of Arimathea comes to Ynys Wydrin",
    "King Lleurwg sends to Rome", "Julius and Aaron", "The Déisi in Dyfed",
    "The songs of Heledd", "Madog sails west",
}
EVENT_RECORDED = {
    # Britons: Caesar, Tacitus and the Roman writers
    "Caswallon against Caesar", "Caesar writes of the Druids of Britain", "The druids of Môn", "The peoples of Wales",
    # the Age of Saints: writings and inscriptions of the time
    "Rome lets go", "Pelagius", "Patrick goes to Ireland", "A bishop of the Britons in Gaul",
    "Riothamus, king of the Britons, crosses to Gaul", "Gildas writes", "The wisest of kings", "The Tywyn stone",
    "Wales accepts the Roman Easter",
}
EVENT_ARCHAEOLOGY = {
    # Rome's forts, towns, roads and mines
    "A fortress at Usk", "The fortress at Caerleon", "The fort of Segontium", "Roman gold at Dolaucothi",
    "The amphitheatre at Caerleon", "Sarn Helen", "Caerwent, town of the Silures", "A fort at Cardiff", "Caer Gybi",
    # the Age of Saints
    "Offa’s Dyke",
}

# ---------- people: default by age ----------
PERSON_DEFAULT = {"ancient": "a", "britons": "c", "roman": "c", "saints": "c", "kings": "r"}

# ---------- people: exceptions, by slug ----------
PERSON_RECORDED = {
    "caswallon", "cynfelyn",  # Caesar; the coins and the Roman writers
    "caratacus", "buddug", "macsen-wledig", "pelagius",
    "riothamus", "patrick", "gildas", "maelgwn-gwynedd", "samson",
}
PERSON_CHRONICLE = {"madog"}  # Madog ab Owain Gwynedd
PERSON_ARCHAEOLOGY = {"red-lady-of-paviland"}


def event_kind(ev):
    """'a', 'c' or 'r' for an event tuple of data.py."""
    t = ev[5]
    if t in EVENT_CHRONICLE:
        return "c"
    if t in EVENT_RECORDED:
        return "r"
    if t in EVENT_ARCHAEOLOGY:
        return "a"
    return EVENT_DEFAULT.get(ev[0], "r")


def person_kind(p):
    """'a', 'c' or 'r' for a person tuple of data.py."""
    s = p[0]
    if s in PERSON_CHRONICLE:
        return "c"
    if s in PERSON_RECORDED:
        return "r"
    if s in PERSON_ARCHAEOLOGY:
        return "a"
    return PERSON_DEFAULT.get(p[1], "r")


def tag(kind, bi):
    """The small tag, in both languages (bi from build.py)."""
    en, cy = LABELS[kind]
    return f'<span class="evi" data-k="{kind}">{bi(en, cy)}</span>'


def key(bi):
    """One line that says what the three labels mean (for the worksheets, the People page and the timeline)."""
    def one(items):
        return " · ".join(f'<span class="evi" data-k="{k}">{t}</span> {d}' for k, (t, d) in zip("acr", items))
    return (f'<p class="evi-key"><span class="l-en" lang="en"><b>How we know:</b> {one(KEY_EN)}.</span>'
            f'<span class="l-cy" lang="cy"><b>Sut rydyn ni’n gwybod:</b> {one(KEY_CY)}.</span></p>')


def check(events, people):
    """Stop the build if an exception names an event or person that no longer exists (a title changed)."""
    titles = {ev[5] for ev in events}
    slugs = {p[0] for p in people}
    bad = [t for t in EVENT_CHRONICLE | EVENT_RECORDED | EVENT_ARCHAEOLOGY if t not in titles]
    bad += [s for s in PERSON_RECORDED | PERSON_CHRONICLE | PERSON_ARCHAEOLOGY if s not in slugs]
    if bad:
        raise SystemExit("src/evidence.py names events or people that are not on the site: " + ", ".join(sorted(bad)))


CSS = """
.evi { display: inline-block; vertical-align: .1em; font-family: var(--f-mono); font-size: .7rem; font-weight: 400; letter-spacing: .02em; line-height: 1.3;
  padding: .08rem .45rem; border-radius: 999px; border: 1px solid currentColor; white-space: nowrap; font-style: normal; text-transform: none }
.evi[data-k="a"] { color: #8fc3a0 }
.evi[data-k="c"] { color: #e8c65a }
.evi[data-k="r"] { color: #9fb8d8 }
.evi-key { font-size: .88rem; color: var(--muted); line-height: 1.8; margin: .4rem 0 1rem }
.evi-key .evi { margin: 0 .15rem }
h3 .evi, h4 .evi, b + .evi, a + .evi { margin-left: .45rem }
.plaque > .evi { justify-self: start }
.person-meta .evi { align-self: center; font-size: .78rem }
.pk-card .evi { display: block; margin: .4rem auto 0; width: max-content }
@media print {
  .evi { color: #000 !important; border-color: #000 !important }
  .evi[data-k="c"] { border-style: dashed !important }
  .evi[data-k="a"] { border-style: dotted !important }
  .evi-key { color: #000 !important }
}
"""
