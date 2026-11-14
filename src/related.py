# Related reading at the end of every long read (November 2026, from a review Ifan passed on: "At the end, suggest
# closely related reading" — the Druids long read was offering the Welsh revival and Brittany, when the Bronze and Iron
# Age and the Roman conquest follow the subject far more naturally).
#
# For each long read: three other long reads on the same subject, closest first. build.py adds a fourth card, the age
# of Welsh history the long read belongs to (era-<age>.html), so a reader can always step back to the wider story.
# A new long read needs a line here; until it has one, build.py picks three by the people, places and events it shares
# with the others (and says so in the build log). An id that is not a long read stops the build.

RELATED = {
    # the Britons before and against Rome
    "druids": ["caradog", "learning", "celts"],
    "celts": ["druids", "language", "brittany"],
    "brutus": ["bruts", "bran", "wilson-blackett"],
    "bran": ["mabinogi", "caradog", "christianity"],
    "caradog": ["druids", "bran", "macsen"],
    "learning": ["druids", "christianity", "writers"],
    # Rome, the faith and the saints
    "macsen": ["brittany", "caradog", "hen-ogledd"],
    "christianity": ["joseph", "lucius", "patrick"],
    "joseph": ["christianity", "lucius", "bran"],
    "lucius": ["christianity", "joseph", "bruts"],
    "patrick": ["christianity", "learning", "brittany"],
    "brittany": ["macsen", "patrick", "celts"],
    "hen-ogledd": ["arthur", "writers", "macsen"],
    "arthur": ["wilson-blackett", "hen-ogledd", "brutus"],
    "wilson-blackett": ["arthur", "brutus", "christianity"],
    # kings, princes, books and castles
    "hywel": ["unconquered", "bruts", "rhys"],
    "unconquered": ["castles", "glyndwr", "hywel"],
    "nest": ["rhys", "castles", "writers"],
    "rhys": ["nest", "castles", "unconquered"],
    "madog": ["world", "rhys", "unconquered"],
    "castles": ["unconquered", "rhys", "glyndwr"],
    "glyndwr": ["longbow", "castles", "unconquered"],
    "longbow": ["glyndwr", "castles", "unconquered"],
    "mabinogi": ["bran", "writers", "bruts"],
    "writers": ["bruts", "mabinogi", "learning"],
    "bruts": ["brutus", "writers", "mabinogi"],
    # the language
    "language": ["welsh-not", "welsh-revival", "celts"],
    "welsh-not": ["language", "welsh-revival", "revival"],
    "welsh-revival": ["welsh-not", "language", "revival"],
    "iolo": ["druids", "celts", "writers"],
    # industry and the wider world
    "industry": ["coal", "firsts", "protest"],
    "coal": ["industry", "aberfan", "protest"],
    "firsts": ["industry", "world", "coal"],
    "protest": ["industry", "coal", "tryweryn"],
    "world": ["madog", "firsts", "industry"],
    # modern Wales
    "aberfan": ["coal", "tryweryn", "industry"],
    "tryweryn": ["mac", "epynt", "revival"],
    "epynt": ["tryweryn", "aberfan", "welsh-revival"],
    "revival": ["tryweryn", "welsh-revival", "mac"],
    "mac": ["fwa", "tryweryn", "revival"],
    "fwa": ["mac", "tryweryn", "revival"],
}


# Subjects for the filters on stories.html (November 2026, from a review Ifan passed on: "Subject, historical period and
# reading-time filters would help visitors choose something relevant"). The age and the reading time come from each long
# read itself; the subject comes from here. A long read can sit under more than one subject. A new long read needs a
# line in STORY_SUBJECTS; until it has one, build.py borrows the subjects of the long reads in its RELATED line (and says
# so in the build log). A subject that is not in SUBJECTS stops the build.
SUBJECTS = [  # (key, English, Welsh), in the order the chips show
    ("britons", "Britons and Rome", "Y Brythoniaid a Rhufain"),
    ("faith", "Faith and saints", "Ffydd a’r seintiau"),
    ("arthur", "Arthur and the Old North", "Arthur a’r Hen Ogledd"),
    ("kings", "Kings and princes", "Brenhinoedd a thywysogion"),
    ("war", "Castles and battles", "Cestyll a brwydrau"),
    ("books", "Books and chronicles", "Llyfrau a chroniclau"),
    ("language", "The Welsh language", "Yr iaith Gymraeg"),
    ("overseas", "Wales overseas", "Cymru dros y môr"),
    ("industry", "Industry and work", "Diwydiant a gwaith"),
    ("modern", "Protest and modern Wales", "Protest a’r Gymru fodern"),
]

STORY_SUBJECTS = {
    "druids": ["britons"],
    "celts": ["britons", "language"],
    "brutus": ["britons", "books"],
    "bran": ["britons", "faith"],
    "caradog": ["britons", "kings", "war"],
    "learning": ["britons", "faith"],
    "macsen": ["britons", "kings", "overseas"],
    "christianity": ["faith"],
    "joseph": ["faith"],
    "lucius": ["faith", "kings"],
    "patrick": ["faith", "overseas"],
    "brittany": ["overseas", "faith"],
    "hen-ogledd": ["arthur", "books"],
    "arthur": ["arthur", "kings"],
    "wilson-blackett": ["arthur"],
    "hywel": ["kings"],
    "unconquered": ["kings", "war"],
    "nest": ["kings"],
    "rhys": ["kings"],
    "madog": ["overseas", "kings"],
    "castles": ["war"],
    "glyndwr": ["war", "kings"],
    "longbow": ["war"],
    "mabinogi": ["books"],
    "writers": ["books"],
    "bruts": ["books"],
    "language": ["language"],
    "welsh-not": ["language"],
    "welsh-revival": ["language"],
    "iolo": ["books", "language"],
    "industry": ["industry"],
    "coal": ["industry"],
    "firsts": ["industry"],
    "world": ["overseas", "industry"],
    "protest": ["modern"],
    "aberfan": ["modern", "industry"],
    "tryweryn": ["modern"],
    "epynt": ["modern"],
    "revival": ["modern", "language"],
    "mac": ["modern"],
    "fwa": ["modern"],
}
