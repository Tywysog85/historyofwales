# Visiting: who looks after each place, its official page, postcode and how to get in (November 2026).
# Ifan asked that people can visit these places. Each place page shows a "Visiting" box, and the map card shows
# a short line with the official link and directions.
#
# We never copy opening times or prices: they change. We link the official page instead, and say only what is
# stable (free, ticketed, open land, private). Postcodes come from the official pages; leave pc="" when there is none.
#
# V(who, url, pc, entry, also=[...], note=(en, cy))
#   who    a key of WHO below, or (English, Welsh) for anyone else
#   url    the official page for opening times and prices ("" if there is none)
#   pc     postcode for satnav
#   entry  a key of ENTRY below
#   also   other bodies on the same site: [(who, url, what en, what cy)]
#   note   one short line that helps a visitor (optional)

WHO = {
    "cadw": ("Cadw", "Cadw"),
    "nt": ("the National Trust", "yr Ymddiriedolaeth Genedlaethol"),
    "amg": ("Amgueddfa Cymru – Museum Wales", "Amgueddfa Cymru"),
    "church": ("the parish church", "yr eglwys blwyf"),
    "council": ("the local council", "y cyngor lleol"),
    "nrw": ("Natural Resources Wales", "Cyfoeth Naturiol Cymru"),
    "private": ("private owners", "perchnogion preifat"),
    "town": ("the town, open to all", "y dref, yn agored i bawb"),
}

ENTRY = {
    "free": ("Free entry", "Mynediad am ddim"),
    "ticket": ("Paid entry: see the official page for prices", "Tâl mynediad: gweler y dudalen swyddogol am brisiau"),
    "open": ("Open land: free, at any reasonable time", "Tir agored: am ddim, ar unrhyw adeg resymol"),
    "outside": ("Private land: see it from the road or public footpath", "Tir preifat: gwelwch ef o’r ffordd neu’r llwybr cyhoeddus"),
    "partfree": ("Grounds free; some parts paid", "Y tir am ddim; tâl am rai rhannau"),
    "church": ("Free; open in daytime, services permitting", "Am ddim; ar agor yn ystod y dydd, pan nad oes gwasanaeth"),
}

CADW = "https://cadw.gov.wales/visit/places-to-visit/"
NT = "https://www.nationaltrust.org.uk/visit/wales/"


def V(who, url, pc, entry, also=(), note=None):
    return dict(who=who, url=url, pc=pc, entry=entry, also=list(also), note=note)


VISIT = {
    # ---------- royal seats and castles of the princes ----------
    "dinefwr": V("cadw", CADW + "castell-dinefwr", "SA19 6RT", "free",
                 also=[("nt", NT + "dinefwr", "the park, the car park and Newton House (paid)", "y parc, y maes parcio a Thŷ Newton (tâl)")],
                 note=("Park at the National Trust car park and walk up through the deer park.", "Parciwch ym maes parcio’r Ymddiriedolaeth Genedlaethol a cherdded i fyny drwy’r parc ceirw.")),
    "aberffraw": V("town", "", "", "open", note=("The court has gone; walk to the old bridge and St Beuno’s church.", "Mae’r llys wedi mynd; cerddwch at yr hen bont ac eglwys Beuno.")),
    "mathrafal": V("private", "", "", "outside", note=("The earthworks are by the junction of the A495 and B4389, near Meifod.", "Mae’r cloddiau ger cyffordd yr A495 a’r B4389, ger Meifod.")),
    "garthcelyn": V("town", "", "", "open", note=("Pen y Bryn is a private house. The village and the path to Aber Falls are open to all.", "Tŷ preifat yw Pen y Bryn. Mae’r pentref a’r llwybr i Raeadr Fawr yn agored i bawb.")),
    "llysrhosyr": V("cadw", CADW + "llys-rhosyr", "LL61 6SG", "free"),
    "dolbadarn": V("cadw", CADW + "castell-dolbadarn", "LL55 4UB", "free"),
    "ybere": V("cadw", CADW + "castell-y-bere", "LL36 9TS", "free"),
    "dolwyddelan": V("cadw", CADW + "castell-dolwyddelan", "LL25 0JD", "free",
                     note=("The keep is open on set days; the grounds belong to the farm below.", "Mae’r gorthwr ar agor ar ddyddiau penodol; mae’r tir yn eiddo i’r fferm islaw.")),
    "dinasemrys": V("nt", NT + "craflwyn-and-beddgelert", "LL55 4NG", "open",
                    note=("Start from the National Trust car park at Craflwyn; the path is steep and rough.", "Dechreuwch o faes parcio’r Ymddiriedolaeth Genedlaethol yng Nghraflwyn; mae’r llwybr yn serth ac yn arw.")),
    "cricieth": V("cadw", CADW + "castell-cricieth", "LL52 0DP", "ticket"),
    "dolforwyn": V("cadw", CADW + "castell-dolforwyn", "", "free"),
    "dryslwyn": V("cadw", CADW + "castell-dryslwyn", "", "free"),
    "carregcennen": V("cadw", CADW + "castell-carreg-cennen", "SA19 6UA", "ticket",
                      note=("Tickets from Castell Farm at the foot of the hill, which runs the site with Cadw.", "Tocynnau o Fferm y Castell wrth droed y bryn, sy’n rhedeg y safle gyda Cadw.")),
    "ewloe": V("cadw", CADW + "castell-ewloe", "CH5 3BZ", "free"),
    "deganwy": V("town", "", "", "open", note=("Footpaths climb to the two summits from the town.", "Mae llwybrau’n dringo i’r ddau gopa o’r dref.")),
    "dinasbran": V(("Denbighshire County Council, with Cadw", "Cyngor Sir Ddinbych, gyda Cadw"), "", "", "open",
                   note=("A steep, exposed climb from Llangollen: wear good shoes.", "Dringfa serth ac agored o Langollen: gwisgwch esgidiau da.")),
    "cwmhir": V(("Abbey Cwmhir Hall and the village", "Neuadd Abaty Cwm-hir a’r pentref"), "", "", "open"),
    "powis": V("nt", NT + "powis-castle-and-garden", "SY21 8RF", "ticket"),
    "kidwelly": V("cadw", CADW + "kidwelly-castle", "SA17 5BQ", "ticket"),
    "llanymddyfri": V("town", "", "", "open", note=("The castle mound and the statue are beside the main car park.", "Mae tomen y castell a’r cerflun wrth ymyl y prif faes parcio.")),
    "cilmeri": V("town", "", "", "open", note=("The memorial is beside the A483 at Cilmeri, west of Builth Wells.", "Mae’r gofeb wrth ymyl yr A483 yng Nghilmeri, i’r gorllewin o Lanfair-ym-Muallt.")),
    "cardigan": V(("Cardigan Castle (Cadwgan Building Preservation Trust)", "Castell Aberteifi (Ymddiriedolaeth Cadwgan)"), "https://www.cardigancastle.com", "SA43 1JA", "ticket"),
}


CSS = """
.visit-box{margin:2rem 0 0;padding:1.2rem 1.3rem 1rem;border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:14px;background:var(--card)}
.visit-box h2{margin:0 0 .7rem;font-size:1.2rem}
.visit-box dl{margin:0;display:grid;gap:.55rem}
.visit-box dl>div{display:grid;grid-template-columns:9.5rem 1fr;gap:.2rem 1rem}
.visit-box dt{font-weight:700;color:var(--muted);font-size:.9rem}
.visit-box dd{margin:0}
.visit-box a{color:var(--gold)}
.visit-box b{letter-spacing:.03em}
.visit-note{margin:.8rem 0 0}
.visit-small{margin:.6rem 0 0;font-size:.85rem;color:var(--muted)}
@media(max-width:560px){.visit-box dl>div{grid-template-columns:1fr}}
.pl-links{margin-top:1.6rem;display:grid;gap:.5rem}
.pl-links .eyebrow{margin:0}
.pl-people{display:flex;flex-wrap:wrap;gap:.5rem;margin:0}
.pl-people a{display:inline-flex;padding:.45rem .8rem;border:1px solid var(--line);border-radius:999px;color:var(--ink);text-decoration:none;font-size:.9rem;font-weight:600;background:var(--card)}
.pl-people a:hover{border-color:var(--gold);color:var(--gold)}
.pc-visit{font-size:.88rem;margin:.2rem 0 .6rem;color:var(--muted)}
.pc-visit a{color:var(--gold)}
"""
