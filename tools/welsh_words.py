"""Find the Welsh words inside an English sentence, so an English voice can be told to say them the Welsh way.

Used by tools/make_listen.py for Microsoft's multilingual English voices: each Welsh word or name is wrapped in
<lang xml:lang="cy-GB">, so "Llywelyn", "Glyndŵr" and "Aberffraw" are said as a Welsh speaker says them, in the same
voice. A word counts as Welsh when it also appears in the Welsh text of the long reads and has a spelling only Welsh
uses (ll, dd, ŵ, ŷ, a circumflex, rh at the start, wy, ydd, aw...). Names that look Welsh but are read the English or
Latin way are in NOT_WELSH; add to it if a sample shows one said wrongly.
"""
import re

MARK = re.compile(r"ll|dd|[ŵŷâêîôûŴŶÂÊÎÔÛ]|^rh|wy|yw|ydd|aw|^cy[mfnrw]|^gw[aeiouy]|^ys[gtb]|^[bcdfgmnpt]w[bcdfglmnrst]|ff[aeiouwy]|wr$|yn$|edd$|og$|wg$|eu", re.I)
NOT_WELSH = set("""Cardiff Cardiff’s Merthyr Swansea Newport Brutus Lucius Julius Tacitus Claudia Tiberius Brittonum Archaiology Magnus
Pughe Tours Pudens Eleutherius Albanactus Theodosius Aurelian Humphrey Riothamus Cambriae Columbus Aeneas Tertullian Vaughan
UNESCO Griffith Locrinus Edmund Caratacus Ostorius Ursula Pelagius Taburniae Dumbarton Diodorus Michael Pandrasus Silvius Corineus
Cunobelinus Cassius Caractacus Sulpicius Jerusalem Verulamium Potitus Malmesbury Powell Israel Bute Hughesovka Butetown Agincourt
Artorius ARTORIUS Ascanius Turonus Goemagot Humber Britanniae Theophilus Archaeologia Camulodunum Suetonius Togodumnus Silurum Rufina
Aulus Irenaeus Gallaecia Calpurnius Arviragus Wearyall Faganus Duvianus Cornhill Marcus Coroticus Berniae Cumbria Griffiths Humphries
Crawshay Gilchrist Chile Cornouaille Euric Sidonius Dumnonia Waroch Lanildut Ildut Gwenole Lucan Laertius Pythagoras Paulinus Turner
Universal Tehuelche Campbell Woodbury Northumberland Northumbria Cnut Ingimund Russel Wallace Guglielmo Spillers Guildhall Bush Burgess
MAURICIUS Brandenburg Kentucky Khumric Helenus Assaracus Trinovantum Loegria Regum Triumphs Faerie Pytheas Hecataeus Herodotus Belgae
Buchanan Collis Christopher Doeg Padouca Pittsburgh Jefferson Southey Myth Publius Syphax Paullus Perseus Manlius Frontinus Pudenziana
Moselle Augusta Severus Poetovio Segontium Publicius Constantius Graecina Plautius Eusebius Eborius Restitutus Adelfius Haddan Stubbs
Lullingstone Chalice Aurelius Mellons Chur Rachel Bromwich Patricius Calpornius Victoricus Voclut Nidum MacNeill Muirchú Nemthur Lawrence
Survival Grenfell Allan Stillness Awakes Stourbridge Millfield Rumpole Cuckoo Scoundrels Salesbury Artegall Glencoe Utilisation Plymouth
Petersburg Ellesmere Lucy Brunel Hamburg Mountaineer Charles-Edwards Idylls Jeffrey Nennius Walliae Coriosolitae Maximianus Dionotus
Fleuriot Britannorum Anthemius Riotimus Bituriges Bourges Apollinaris Childebert Iudual Kastell-Paol Roscoff Tewkesbury Mill Villemarqué
Jaffrennou Cumberland Ecclefechan Galloway Brunanburh Arthuret Gillian Furry Pomponius Marseille Marcellinus Diviciacus Aedui Tullius
Quintus Divitiacus Carnutes Cyril Restaurata Maximus Linus Charlotte Richard French Glastonbury Missouri Charles William Williams Saunders
Hughes Mount Lloyd Lloydia Gruffydd Clun Llanymynech Taffy Re-united Survival Alwyn Elwyn Crug Hill Valley Law Log Well Bill Fallen
Powell Griffin Domnall Wallace Llewellyn Dollar Hall Ball Wall Mall Hollow Valleys Allies Fell Sully Billy Holly Kelly Shelley Melly Cornwall Middle College Still Colliery Gallic All Pillar Pillars Hills Sellar Small Stalling
Unwilling Talley Thelwall Seville Goodwill Valle Addressed Powells Wye Rhine Rhineland Caerphilly Kidwelly Crickhowell Llandovery Cymbeline Rhos-on-Sea Llywelyns""".split())
STRONG = re.compile(r"^ll|[ŵŷâêîôûŴŶÂÊÎÔÛ]|^rh(?!ine)|.wy|ydd|^cy[mfnrw]|^gw[aeiouy]|ych|[^aeiou]dd[aeiouwy]?$|^.{2,}ll[aeiouwy]?$(?<!all)(?<!ill)(?<!ell)", re.I)
ALWAYS = set("Owain Fychan Glyndyfrdwy Ifor Iolo Dewi Teilo Padarn Deiniol Cadfan Beuno Tysilio Cadwaladr Caerleon Caernarfon Aberystwyth Gwent Dyfed Morgannwg Môn Eryri Gwent Ceredigion Brycheiniog Ystrad".split())


def is_welsh(w, cy_words):
    base = re.sub(r"[’'](s|r)?$", "", w)
    if base in NOT_WELSH or not w[:1].isupper():
        return False
    if base in ALWAYS or STRONG.search(base):
        return True
    return base in cy_words and bool(MARK.search(base))


WORD = re.compile(r"[A-Za-zÀ-ÿŵŷŴŶ]+(?:[-’'][A-Za-zÀ-ÿŵŷŴŶ]+)*")


def tokens(t):
    return WORD.findall(t)


def mark(text, cy_words, wrap):
    """text with each run of Welsh words passed through wrap(run) (the rest unchanged)."""
    out, last, run = [], 0, None
    spans = []
    for m in WORD.finditer(text):
        if is_welsh(m.group(0), cy_words):
            tail = re.search(r"[’'](s|r)$", m.group(0))   # "Llywelyn’s": the ’s is English, said outside
            spans.append((m.start(), m.end() - (len(tail.group(0)) if tail else 0), bool(tail)))
    # join neighbours ("Owain Glyndŵr", "Pwyll Pendefig Dyfed") so a name is said in one breath
    groups = []
    for a, b, cut in spans:
        if groups and not groups[-1][2] and text[groups[-1][1]:a] in (" ", "-", " ap ", " ab ", " ferch ", " y ", " yr ", " o ", " fab "):
            groups[-1][1], groups[-1][2] = b, cut
        else:
            groups.append([a, b, cut])
    for a, b, _ in groups:
        out.append(text[last:a])
        out.append(wrap(text[a:b]))
        last = b
    out.append(text[last:])
    return "".join(out)
