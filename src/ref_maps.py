"""Maps through time (maps.html): every stage of the kingdoms map from src/kingdoms.py, laid out one after another,
plus the two modern changes the home page map skips (1974 and 1996), and links to read more for each stage.
Groups use the same blocks as src/kingdoms.py (modern council areas, with Powys and Gwynedd cut into their old shires)."""
from kingdoms import AN, CAE, MEI, CON, DEN, FLI, WRE, MON, RAD, BRE, CER, PEM, CAR, SWA, RED, OCHRE, GREEN, BLUE, VIOLET, GREY, GOLD, TEAL, PINK

MODERN = [
 dict(id="m1974", en="1974: eight new counties", cy="1974: wyth sir newydd",
  nEn="In 1974 the thirteen old shires were replaced by eight larger counties, and old Welsh names came back onto the map: Gwynedd, Powys, Dyfed and Gwent, with Clwyd and the three Glamorgans. The borders shown here are close but not exact.",
  nCy="Yn 1974 disodlwyd y tair hen sir ar ddeg gan wyth sir fwy, a daeth hen enwau Cymraeg yn ôl i’r map: Gwynedd, Powys, Dyfed a Gwent, gyda Chlwyd a’r tair Morgannwg. Mae’r ffiniau a ddangosir yma’n agos ond nid yn union.",
  groups=[["Gwynedd", "Gwynedd", RED, [AN, CAE, MEI, CON]], ["Clwyd", "Clwyd", OCHRE, [DEN, FLI, WRE]], ["Powys", "Powys", GOLD, [MON, RAD, BRE]],
          ["Dyfed", "Dyfed", GREEN, [CER, PEM, CAR]], ["West Glamorgan", "Gorllewin Morgannwg", TEAL, [SWA, "Neath Port Talbot"], ["W. Glam", "G. Morgannwg"]],
          ["Mid Glamorgan", "Morgannwg Ganol", BLUE, ["Bridgend", "Rhondda Cynon Taf", "Merthyr Tydfil", "Caerphilly"], ["Mid Glam", "M. Ganol"]],
          ["South Glamorgan", "De Morgannwg", PINK, ["Cardiff", "Vale of Glamorgan"], ["", ""]], ["Gwent", "Gwent", VIOLET, ["Blaenau Gwent", "Torfaen", "Monmouthshire", "Newport"]]]),
 dict(id="m1996", en="1996: the twenty-two councils", cy="1996: y dau gyngor ar hugain",
  nEn="In 1996 the eight counties gave way to twenty-two councils, which still run schools, roads and local services. Gwynedd, Powys and Ceredigion kept their ancient names.",
  nCy="Yn 1996 rhoddodd yr wyth sir le i ddau gyngor ar hugain, sy’n dal i redeg ysgolion, ffyrdd a gwasanaethau lleol. Cadwodd Gwynedd, Powys a Cheredigion eu henwau hynafol.",
  groups=None),  # filled in below: one group per council
]
_C = [RED, OCHRE, GREEN, BLUE, VIOLET, GOLD, TEAL, PINK]
_COUNCILS = [("Isle of Anglesey", "Ynys Môn", [AN]), ("Gwynedd", "Gwynedd", [CAE, MEI]), ("Conwy", "Conwy", [CON]), ("Denbighshire", "Sir Ddinbych", [DEN]),
             ("Flintshire", "Sir y Fflint", [FLI]), ("Wrexham", "Wrecsam", [WRE]), ("Powys", "Powys", [MON, RAD, BRE]), ("Ceredigion", "Ceredigion", [CER]),
             ("Pembrokeshire", "Sir Benfro", [PEM]), ("Carmarthenshire", "Sir Gaerfyrddin", [CAR]), ("Swansea", "Abertawe", [SWA]),
             ("Neath Port Talbot", "Castell-nedd Port Talbot", ["Neath Port Talbot"]), ("Bridgend", "Pen-y-bont ar Ogwr", ["Bridgend"]),
             ("Vale of Glamorgan", "Bro Morgannwg", ["Vale of Glamorgan"]), ("Cardiff", "Caerdydd", ["Cardiff"]), ("Rhondda Cynon Taf", "Rhondda Cynon Taf", ["Rhondda Cynon Taf"]),
             ("Merthyr Tydfil", "Merthyr Tudful", ["Merthyr Tydfil"]), ("Caerphilly", "Caerffili", ["Caerphilly"]), ("Blaenau Gwent", "Blaenau Gwent", ["Blaenau Gwent"]),
             ("Torfaen", "Torfaen", ["Torfaen"]), ("Monmouthshire", "Sir Fynwy", ["Monmouthshire"]), ("Newport", "Casnewydd", ["Newport"])]
MODERN[1]["groups"] = [[en, cy, _C[i % len(_C)], blocks, ["", ""]] for i, (en, cy, blocks) in enumerate(_COUNCILS)]
# the councils big enough to carry a name on the map
for gr in MODERN[1]["groups"]:
    if gr[0] in ("Gwynedd", "Powys", "Ceredigion", "Carmarthenshire", "Pembrokeshire", "Isle of Anglesey", "Conwy"):
        gr[4] = ["Môn", "Môn"] if gr[0] == "Isle of Anglesey" else [gr[0], gr[1]] if gr[0] != "Carmarthenshire" else ["Carmarthen", "Caerfyrddin"]

SEE = {
 "c50": ["battles.html#b-mon60", "a-z.html#az-ordovices", "a-z.html#az-silures", "era-ancient.html"],
 "c150": ["era-roman.html", "a-z.html#az-isca", "place-caerleon.html", "place-segontium.html"],
 "c600": ["era-saints.html", "a-z.html#az-hen-ogledd", "a-z.html#az-gwynedd", "saints.html"],
 "c878": ["person-rhodri-mawr.html", "family-trees.html"],
 "c945": ["person-hywel-dda.html", "laws.html", "story-hywel.html"],
 "c1000": ["kings.html", "a-z.html#az-deheubarth", "a-z.html#az-powys"],
 "c1057": ["person-gruffudd-ap-llywelyn.html", "story-unconquered.html"],
 "c1200": ["a-z.html#az-pura-wallia", "a-z.html#az-march", "person-yr-arglwydd-rhys.html", "person-llywelyn-fawr.html", "castles.html"],
 "c1267": ["documents.html#doc-montgomery", "person-llywelyn-ap-gruffudd.html", "a-z.html#az-principality"],
 "c1284": ["documents.html#doc-rhuddlan", "battles.html#b-cilmeri", "castles.html", "a-z.html#az-iron-ring"],
 "c1404": ["documents.html#doc-pennal", "documents.html#doc-indenture", "person-owain-glyndwr.html", "story-glyndwr.html"],
 "c1536": ["documents.html#doc-union", "a-z.html#az-acts-of-union", "a-z.html#az-shire", "a-z.html#az-great-sessions"],
 "m1974": ["a-z.html#az-welsh-office", "topic-law.html"],
 "m1996": ["topic-law.html", "towns.html"],
 "today": ["a-z.html#az-senedd", "documents.html#doc-devolution", "place-senedd.html", "topic-law.html"],
}
