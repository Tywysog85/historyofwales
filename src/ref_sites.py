"""The historic sites map (sites.html): Cadw's scheduled monuments, sorted into kinds a visitor would recognise.

The data is fetched on GitHub by tools/sites_fetch.py (.github/workflows/fetch-sites.yml) into tools/data/:
sites_cadw.json (every scheduled monument) and sites_guardian.json (the sites Cadw looks after and opens to visitors).
Contains public sector information licensed under the Open Government Licence v3.0 (Cadw, via DataMapWales).
"""
import re

# key, English, Welsh, colour, a line about them in English and Welsh
CATS = [
    ("burial", "Burial chambers and cairns", "Siambrau claddu a charneddau", "#d39a62",
     "Cromlechs, cairns and barrows where the first farmers and the Bronze Age people laid their dead.", "Cromlechi, carneddau a chrugiau lle gosododd y ffermwyr cyntaf a phobl Oes yr Efydd eu meirw."),
    ("stones", "Standing stones and circles", "Meini hirion a chylchoedd", "#e8c65a",
     "Meini hirion, stone circles, stone rows and henges, raised four and five thousand years ago.", "Meini hirion, cylchoedd cerrig, rhesi cerrig a henebion crwn, a godwyd bedair a phum mil o flynyddoedd yn ôl."),
    ("forts", "Hillforts and ancient homes", "Bryngaerau a hen gartrefi", "#e2453d",
     "The hillforts and farmsteads of the Iron Age Britons, and the round huts of the people before them.", "Bryngaerau a ffermydd Brythoniaid Oes yr Haearn, a chytiau crwn y bobl o’u blaen."),
    ("roman", "Roman sites", "Safleoedd Rhufeinig", "#e58fb4",
     "Forts, camps, roads, towns and villas from the centuries of Rome.", "Caerau, gwersylloedd, ffyrdd, trefi a filâu o ganrifoedd Rhufain."),
    ("crosses", "Crosses and inscribed stones", "Croesau a meini arysgrifedig", "#b9a0ea",
     "Stones carved with the names of early Welsh kings and saints, in Latin and ogham, and the great crosses.", "Cerrig wedi’u cerfio ag enwau brenhinoedd a seintiau cynnar Cymru, mewn Lladin ac ogam, a’r croesau mawr."),
    ("faith", "Churches, abbeys and holy wells", "Eglwysi, abatai a ffynhonnau sanctaidd", "#ffffff",
     "Chapels, abbeys, priories and the holy wells of the saints.", "Capeli, abatai, prioriaethau a ffynhonnau sanctaidd y seintiau."),
    ("castles", "Castles and town walls", "Cestyll a muriau trefi", "#f26a62",
     "Mottes, ringworks, stone castles and walled towns of the Middle Ages.", "Mwntiau, cylchfuriau, cestyll carreg a threfi caerog yr Oesoedd Canol."),
    ("dykes", "Dykes and old roads", "Cloddiau a hen ffyrdd", "#7cc495",
     "Offa’s Dyke, Wat’s Dyke, cross-ridge dykes, old roads and bridges.", "Clawdd Offa, Clawdd Wat, cloddiau trawsgefn, hen ffyrdd a phontydd."),
    ("industry", "Industry", "Diwydiant", "#93a0e0",
     "Mines, ironworks, furnaces, quarries, tramroads and the engine houses of the first industrial nation.", "Mwyngloddiau, gweithfeydd haearn, ffwrneisi, chwareli, tramffyrdd a thai injan y genedl ddiwydiannol gyntaf."),
    ("war", "Modern defences", "Amddiffynfeydd modern", "#62c6c4",
     "Gun batteries, pillboxes and defences of the last two centuries.", "Magnelfeydd, blychau pils ac amddiffynfeydd y ddwy ganrif ddiwethaf."),
    ("other", "Other monuments", "Henebion eraill", "#9aa3b5",
     "Deserted villages, moated sites, mills, farmsteads and more.", "Pentrefi gwag, safleoedd â ffos, melinau, ffermydd a rhagor."),
]
CAT_IX = {c[0]: i for i, c in enumerate(CATS)}

PERIOD_CY = {"Prehistoric": "Cynhanesyddol", "Medieval": "Canoloesol", "Post Medieval/Modern": "Ôl-ganoloesol/Modern", "Early Medieval": "Canoloesol cynnar",
             "Roman": "Rhufeinig", "Post Medieval": "Ôl-ganoloesol", "Bronze Age": "Oes yr Efydd", "Unknown": "Anhysbys", "Neolithic": "Neolithig",
             "Industrial": "Diwydiannol", "Modern": "Modern", "Iron Age": "Oes yr Haearn", "Victorian": "Fictoraidd"}


def classify(site_type, period, broad):
    t, per, bc = (site_type or "").lower(), period or "", broad or ""
    if per == "Roman" or re.search(r"roman|legionary|vicus|villa|marching camp|practice camp", t):
        return "roman"
    if re.search(r"inscribed|cross|ogham|pillar", t):
        return "crosses"
    if re.search(r"castle|motte|ringwork|tower house|town wall|town defen|gatehouse|palace|bailey", t):
        return "castles"
    if re.search(r"chapel|church|abbey|priory|friary|well|grange|cathedral|monast|hermit|nunnery|ecclesiast", t):
        return "faith"
    if re.search(r"barrow|cairn|tomb|burial|cist|cemetery|chamber", t):
        return "burial"
    if re.search(r"standing stone|stone circle|stone row|alignment|henge|cup.marked|stone setting|stone pair|timber circle", t):
        return "stones"
    if re.search(r"pillbox|battery|anti|radar|gun|bomb|searchlight|military|firing|observation post", t) or (bc == "Defence" and "Modern" in per):
        return "war"
    if bc == "Industrial" or re.search(r"mine|works|furnace|kiln|quarry|tramroad|railway|incline|engine|colliery|forge|mill|canal|aqueduct|leat|chimney|dam\b|level|shaft", t):
        return "industry"
    if re.search(r"dyke|linear earthwork|road|trackway|bridge|causeway|boundary", t):
        return "dykes"
    if per in ("Prehistoric", "Iron Age", "Bronze Age", "Neolithic") and re.search(r"fort|enclosure|rath|hut|settlement|platform|cave|camp|homestead|field", t):
        return "forts"
    if re.search(r"hillfort|promontory fort|\brath\b", t):
        return "forts"
    return "other"
