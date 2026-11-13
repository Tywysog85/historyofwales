# Twelve ages (November 2026): Ifan asked for twelve instead of nine.
#   * Ancient Wales splits into the Stone Age (id "ancient", so era-ancient.html keeps working) and
#     Bronze and Iron Age Britons (new id "britons").
#   * The Age of Princes (id "medieval") now ends in 1282, and Glyndŵr's Wales (new id "glyndwr") runs 1282 to 1485.
#   * The Age of Revival (new id "revival") covers the 1700s, between Tudor and Stuart Wales and Industrial Wales.
# data.py calls apply() at the very end, after every other file has added its events, people and places, so anything
# added later in the old ids is moved into the right age by year. build.py calls remap() for long reads, legends and tales.
# build.py also needs a colour (COL), a drawing (ERA_ART), a question (ERA_Q) and src/head.html a colour for each id;
# src/pictures.py needs a picture (ERA). Follow EDITORIAL.md: proud and true, Britons not Celts, kings are kings.
import re

ORDER = ["ancient", "britons", "roman", "saints", "kings", "medieval", "glyndwr", "tudor", "revival", "industrial", "modern", "today"]

# where each age begins and ends, for anything dated by year (events, On this day, games)
BOUNDS = ((-2500, "ancient"), (48, "britons"), (410, "roman"), (800, "saints"), (1100, "kings"), (1284, "medieval"),
          (1485, "glyndwr"), (1700, "tudor"), (1800, "revival"), (1914, "industrial"), (1997, "modern"))


def era_of_year(y):
    for lim, eid in BOUNDS:
        if y < lim:
            return eid
    return "today"


# ---------- the four new or reshaped ages ----------
STONE = dict(en="The Stone Age", cy="Oes y Cerrig", spanEn="230,000 – 2500 BC", spanCy="230,000 – 2500 CC", ill="dolmen",
  blurbEn="Neanderthals, ice-age hunters, the first farmers and the builders of the great stone tombs.",
  blurbCy="Neanderthaliaid, helwyr oes yr iâ, y ffermwyr cyntaf a chodwyr y beddrodau cerrig mawr.",
  storyEn=[
    "People reached the land we call Wales long before it was an island. Neanderthals sheltered in Pontnewydd Cave above the River Elwy some 230,000 years ago, and their teeth are the oldest human remains ever found in Wales. Around 33,000 years ago modern humans buried a young man in red ochre in Paviland Cave on Gower, with rods of mammoth ivory and shells beside him: the oldest ceremonial burial known in western Europe. Then the ice returned, and for thousands of years the land lay empty.",
    "As the ice melted, hunters followed the herds back into the valleys, and one of them cut zigzag lines into a horse’s jaw in Kendrick’s Cave on the Great Orme. Families of the Middle Stone Age made beads at Nab Head in Pembrokeshire and left their footprints in the mud of the Severn shore. Around 4000 BC the first farmers came, cleared the woods and raised great tombs for their dead: Tinkinswood, Pentre Ifan, Bryn Celli Ddu and Barclodiad y Gawres, where stones carved with spirals and zigzags still stand. Stone axes from Graig Lwyd above Penmaenmawr travelled the length of Britain, and the bluestones of the Preseli Hills were carried some 150 miles to stand at Stonehenge."],
  storyCy=[
    "Cyrhaeddodd pobl y tir a alwn yn Gymru ymhell cyn iddo fod yn ynys. Cysgododd Neanderthaliaid yn Ogof Bontnewydd uwchben afon Elwy tua 230,000 o flynyddoedd yn ôl, a’u dannedd hwy yw’r olion dynol hynaf a gafwyd erioed yng Nghymru. Tua 33,000 o flynyddoedd yn ôl claddodd bodau dynol modern ddyn ifanc mewn ocr coch yn Ogof Pafiland ar Benrhyn Gŵyr, gyda gwiail o ifori mamoth a chregyn wrth ei ochr: y gladdedigaeth seremonïol hynaf y gwyddys amdani yng ngorllewin Ewrop. Yna dychwelodd yr iâ, a bu’r tir yn wag am filoedd o flynyddoedd.",
    "Wrth i’r iâ doddi, dilynodd helwyr yr anifeiliaid yn ôl i’r dyffrynnoedd, a thorrodd un ohonynt linellau igam-ogam ar ên ceffyl yn Ogof Kendrick ar y Gogarth. Gwnaeth teuluoedd Oes Ganol y Cerrig fwclis yn Nab Head yn Sir Benfro, a gadael ôl eu traed ym mwd glannau Hafren. Tua 4000 CC daeth y ffermwyr cyntaf, clirio’r coedwigoedd a chodi beddrodau mawr i’w meirw: Llwyneliddon, Pentre Ifan, Bryn Celli Ddu a Barclodiad y Gawres, lle mae cerrig wedi’u cerfio â throellau a phatrymau igam-ogam yn sefyll o hyd. Teithiodd bwyeill carreg o Graig Lwyd uwchben Penmaenmawr ar hyd a lled Prydain, a chludwyd cerrig gleision y Preseli ryw 150 milltir i sefyll yng Nghôr y Cewri."])

BRITONS = dict(id="britons", en="Bronze and Iron Age Britons", cy="Brythoniaid Oes yr Efydd a’r Haearn", spanEn="2500 BC – AD 48", spanCy="2500 CC – 48 OC", ill="mtn",
  blurbEn="Copper miners, gold-workers, hillfort kings and druids: the Britons before Rome.",
  blurbCy="Mwynwyr copr, gofaint aur, brenhinoedd y bryngaerau a’r derwyddon: y Brythoniaid cyn Rhufain.",
  storyEn=[
    "Around 2500 BC people in Wales learned to work copper and gold, and soon to mix copper with tin to make bronze. On the Great Orme miners with tools of bone and stone dug kilometres of tunnels after copper ore, in one of the largest prehistoric mines in the world, and Welsh copper travelled across Britain and over the sea. The finest work of the age is the gold cape of Mold, beaten from a single ingot of gold some 3,900 years ago. The chiefs of the Bronze Age were laid under cairns such as Bryn Cader Faner, and the Caergwrle bowl, of shale inlaid with tin and gold, shows a boat riding the waves.",
    "From about 700 BC iron came into use, and the hills were crowned with forts: hundreds of them, from Tre’r Ceiri high on Yr Eifl to Castell Henllys in Pembrokeshire, where roundhouses stand again on their old foundations. Their people were Britons, speaking the British tongue from which Welsh grew, and the Romans would learn the names of their peoples: the Silures, the Ordovices, the Demetae and the Deceangli. At Llyn Cerrig Bach on Ynys Môn they gave swords, spears, chariot fittings and a slave chain to the waters, and Môn was the great stronghold of the druids. In 54 BC Caswallon, as Welsh tradition remembers Cassivellaunus, led the Britons against Julius Caesar, and when the Roman army reached the borders of Wales in AD 48 it met kings and warriors ready to fight."],
  storyCy=[
    "Tua 2500 CC dysgodd pobl yng Nghymru weithio copr ac aur, ac yn fuan gymysgu copr â thun i wneud efydd. Ar y Gogarth cloddiodd mwynwyr ag offer o asgwrn a charreg gilometrau o dwneli ar ôl mwyn copr, yn un o’r mwyngloddiau cynhanesyddol mwyaf yn y byd, a theithiodd copr Cymru ar draws Prydain a thros y môr. Gwaith gorau’r oes yw mantell aur yr Wyddgrug, a guriwyd o un darn o aur tua 3,900 o flynyddoedd yn ôl. Gosodwyd penaethiaid Oes yr Efydd dan garneddau fel Bryn Cader Faner, ac mae powlen Caergwrle, o siâl wedi’i addurno â thun ac aur, yn dangos cwch yn marchogaeth y tonnau.",
    "O tua 700 CC daeth haearn i’w ddefnyddio, a choronwyd y bryniau â chaerau: cannoedd ohonynt, o Dre’r Ceiri yn uchel ar yr Eifl i Gastell Henllys yn Sir Benfro, lle mae tai crwn yn sefyll eto ar eu hen sylfeini. Brythoniaid oedd eu pobl, yn siarad yr iaith Frythoneg y tyfodd y Gymraeg ohoni, a byddai’r Rhufeiniaid yn dysgu enwau eu pobloedd: y Silwriaid, yr Ordofigiaid, y Demetae a’r Deceangli. Yn Llyn Cerrig Bach ar Ynys Môn rhoesant gleddyfau, gwaywffyn, offer cerbydau rhyfel a chadwyn caethweision i’r dyfroedd, ac Ynys Môn oedd cadarnle mawr y derwyddon. Yn 54 CC arweiniodd Caswallon, fel y cofia traddodiad Cymru am Cassivellaunus, y Brythoniaid yn erbyn Iŵl Cesar, a phan gyrhaeddodd byddin Rhufain ffiniau Cymru yn 48 OC cyfarfu â brenhinoedd a rhyfelwyr a oedd yn barod i ymladd."])

PRINCES = dict(spanEn="1100 – 1282", spanCy="1100 – 1282",
  blurbEn="Castles, poetry and the princes of Gwynedd and Deheubarth against Norman and English power.",
  blurbCy="Cestyll, barddoniaeth a thywysogion Gwynedd a Deheubarth yn erbyn grym y Normaniaid a Lloegr.",
  p2En="In the north, Llywelyn ap Iorwerth, Llywelyn Fawr, made himself master of almost all of Wales, married Siwan, daughter of King John, and drew the other rulers of Wales under the lead of Gwynedd. His grandson Llywelyn ap Gruffudd went further: in the Treaty of Montgomery of 1267 the English crown recognised him as Prince of Wales. War with Edward I followed, and on 11 December 1282 Llywelyn was killed near Cilmeri. ‘Do you not see the end of the world?’ asked the poet Gruffudd ab yr Ynad Coch in his great elegy. Llywelyn’s brother Dafydd fought on into 1283, and Edward ringed Gwynedd with castles to hold what he had won.",
  p2Cy="Yn y gogledd gwnaeth Llywelyn ap Iorwerth, Llywelyn Fawr, ei hun yn feistr ar bron y cyfan o Gymru, priododd Siwan, merch y Brenin John, a thynnodd reolwyr eraill Cymru dan arweiniad Gwynedd. Aeth ei ŵyr Llywelyn ap Gruffudd ymhellach: yng Nghytundeb Trefaldwyn yn 1267 cydnabu coron Lloegr ef yn Dywysog Cymru. Dilynodd rhyfel ag Edward I, ac ar 11 Rhagfyr 1282 lladdwyd Llywelyn ger Cilmeri. ‘Poni welwch-chwi ddiwedd y byd?’ gofynnodd y bardd Gruffudd ab yr Ynad Coch yn ei farwnad fawr. Ymladdodd Dafydd, brawd Llywelyn, ymlaen i 1283, a chododd Edward gylch o gestyll o amgylch Gwynedd i ddal yr hyn a enillodd.")

GLYNDWR = dict(id="glyndwr", en="Glyndŵr’s Wales", cy="Cymru Glyndŵr", spanEn="1282 – 1485", spanCy="1282 – 1485", ill="harp",
  blurbEn="Risings against the conqueror, a golden age of poetry, and Owain Glyndŵr, Prince of Wales.",
  blurbCy="Gwrthryfeloedd yn erbyn y concwerwr, oes aur barddoniaeth, ac Owain Glyndŵr, Tywysog Cymru.",
  storyEn=[
    "After 1282 Wales was a conquered land. The Statute of Rhuddlan of 1284 divided Gwynedd into English shires under English criminal law, Edward I’s great castles rose at Conwy, Caernarfon, Harlech and Beaumaris, and Welsh people were kept out of the new walled towns. Yet the Welsh would not give up. Rhys ap Maredudd rose in 1287, Madog ap Llywelyn in 1294 and Llywelyn Bren in 1316, and Owain Lawgoch, the last heir of the princes of Gwynedd, claimed his right from France until he was murdered in 1378. The poets kept faith too. This was the golden age of the cywydd: Dafydd ap Gwilym sang of love and of the woods, Iolo Goch of the open-handed courts of the uchelwyr, and the White Book of Rhydderch and the Red Book of Hergest saved the Mabinogion for all time.",
    "In September 1400 Owain Glyndŵr, heir of the princes of Powys and Deheubarth, was proclaimed Prince of Wales at Glyndyfrdwy. His rising swept the country: victories at Hyddgen and Bryn Glas, Conwy Castle taken on Good Friday 1401, Harlech and Aberystwyth won in 1404. He held a parliament at Machynlleth, made a treaty with France, and in the Pennal Letter of 1406 set out his plans for a Welsh church and two universities. He was never captured, and no one knows where he lies. After him came harsh penal laws, but the poets of the gentry, Guto’r Glyn and Lewys Glyn Cothi among them, kept singing in the great houses, and they foretold a mab darogan, a son of prophecy, who would win back the crown of Britain. In 1485 he came."],
  storyCy=[
    "Ar ôl 1282 roedd Cymru’n wlad wedi’i goresgyn. Rhannodd Statud Rhuddlan yn 1284 Wynedd yn siroedd Seisnig dan gyfraith droseddol Lloegr, cododd cestyll mawr Edward I yng Nghonwy, Caernarfon, Harlech a Biwmares, a chadwyd y Cymry allan o’r trefi caerog newydd. Ond nid ildiai’r Cymry. Cododd Rhys ap Maredudd yn 1287, Madog ap Llywelyn yn 1294 a Llywelyn Bren yn 1316, a hawliodd Owain Lawgoch, etifedd olaf tywysogion Gwynedd, ei hawl o Ffrainc nes ei lofruddio yn 1378. Cadwodd y beirdd y ffydd hefyd. Dyma oes aur y cywydd: canodd Dafydd ap Gwilym am gariad a’r coed, Iolo Goch am lysoedd hael yr uchelwyr, ac achubodd Llyfr Gwyn Rhydderch a Llyfr Coch Hergest y Mabinogion am byth.",
    "Ym mis Medi 1400 cyhoeddwyd Owain Glyndŵr, etifedd tywysogion Powys a Deheubarth, yn Dywysog Cymru yng Nglyndyfrdwy. Ysgubodd ei wrthryfel drwy’r wlad: buddugoliaethau yn Hyddgen a Bryn Glas, cipio Castell Conwy ar Ddydd Gwener y Groglith 1401, ac ennill Harlech ac Aberystwyth yn 1404. Cynhaliodd senedd ym Machynlleth, gwnaeth gytundeb â Ffrainc, ac yn Llythyr Pennal yn 1406 gosododd ei gynlluniau am eglwys Gymreig a dwy brifysgol. Ni chafodd ei ddal erioed, ac nid oes neb yn gwybod ble mae’n gorwedd. Ar ei ôl daeth cyfreithiau penyd llym, ond daliodd beirdd yr uchelwyr, Guto’r Glyn a Lewys Glyn Cothi yn eu plith, i ganu yn y plastai mawr, a phroffwydasant am fab darogan a fyddai’n ennill coron Prydain yn ôl. Yn 1485 fe ddaeth."])

TUDOR = dict(spanEn="1485 – 1700", spanCy="1485 – 1700",
  blurbEn="A Welsh king, union with England, a Bible in Welsh, civil war and the first chapels.",
  blurbCy="Brenin o Gymro, uno â Lloegr, Beibl Cymraeg, rhyfel cartref a’r capeli cyntaf.",
  cutEn="From 1731 the circulating schools",
  endEn="Welsh books multiplied, from the little Bible of 1630, cheap enough for a family to own, to the Welsh almanacs printed at Shrewsbury from the 1690s, and the ground was ready for the great revival of the century to come.",
  cutCy="O 1731 ymlaen dysgodd ysgolion cylchynol",
  endCy="Amlhaodd llyfrau Cymraeg, o’r Beibl Bach yn 1630, a oedd yn ddigon rhad i deulu ei brynu, i’r almanaciau Cymraeg a argraffwyd yn Amwythig o’r 1690au ymlaen, ac roedd y tir yn barod ar gyfer adfywiad mawr y ganrif i ddod.")

REVIVAL = dict(id="revival", en="The Age of Revival", cy="Oes yr Adfywiad", spanEn="1700 – 1800", spanCy="1700 – 1800", ill="chapel",
  blurbEn="Schools in every parish, a great awakening, hymns, scholars, harpers and the eisteddfod reborn.",
  blurbCy="Ysgolion ym mhob plwyf, deffroad mawr, emynau, ysgolheigion, telynorion a’r eisteddfod wedi’i haileni.",
  storyEn=[
    "The eighteenth century woke Wales up. In 1707 Edward Lhuyd showed that Welsh was one of a family of ancient languages, and Theophilus Evans’s Drych y Prif Oesoedd of 1716 told the Welsh the story of their own past. From the 1730s Griffith Jones, rector of Llanddowror, sent teachers from parish to parish in circulating schools that taught people of every age to read the Bible in Welsh; by his death in 1761 more than 158,000 scholars had passed through them, and the Welsh were becoming one of the most literate peoples in Europe. In 1735 Howell Harris of Trefeca and Daniel Rowland of Llangeitho began to preach, and the Methodist revival spread across the land. William Williams of Pantycelyn gave it hundreds of hymns, among them the one the world sings as ‘Guide me, O thou great Redeemer’, and Ann Griffiths of Dolwar Fach wrote verses still counted among the finest in the language.",
    "Wales found its old learning again too. The Morris brothers of Môn, Lewis, Richard and William, gathered manuscripts and poets around them; in 1751 Welshmen in London founded the Honourable Society of Cymmrodorion, the Gwyneddigion followed in 1770, and their eisteddfod at Corwen in 1789 began the eisteddfod as the nation knows it. Evan Evans, Ieuan Fardd, brought the poetry of the princes back to light, harpers such as John Parry, Parri Ddall, played the triple harp in the great houses, and in 1792 Iolo Morganwg held the first Gorsedd of the Bards of the Island of Britain on Primrose Hill in London, bringing the bardic tradition of Wales before the world. By the century’s end the first great ironworks were rising at Merthyr, copper was pouring from Parys Mountain, and a people who could read, sing and argue in their own language were ready for the age of industry."],
  storyCy=[
    "Deffrodd y ddeunawfed ganrif Gymru. Yn 1707 dangosodd Edward Lhuyd fod y Gymraeg yn un o deulu o ieithoedd hynafol, ac adroddodd Drych y Prif Oesoedd Theophilus Evans yn 1716 hanes eu gorffennol eu hunain wrth y Cymry. O’r 1730au ymlaen anfonodd Griffith Jones, rheithor Llanddowror, athrawon o blwyf i blwyf mewn ysgolion cylchynol a ddysgai bobl o bob oed i ddarllen y Beibl yn Gymraeg; erbyn ei farw yn 1761 roedd dros 158,000 o ddisgyblion wedi bod drwyddynt, ac roedd y Cymry’n dod yn un o bobloedd mwyaf llythrennog Ewrop. Yn 1735 dechreuodd Howell Harris o Drefeca a Daniel Rowland o Langeitho bregethu, a lledodd y diwygiad Methodistaidd drwy’r wlad. Rhoddodd William Williams Pantycelyn gannoedd o emynau iddo, yn eu plith yr un a gân y byd fel ‘Guide me, O thou great Redeemer’, sef ‘Arglwydd, arwain trwy’r anialwch’, ac ysgrifennodd Ann Griffiths o Ddolwar Fach benillion a gyfrifir o hyd ymhlith y gorau yn yr iaith.",
    "Daeth Cymru o hyd i’w hen ddysg hefyd. Casglodd Morrisiaid Môn, Lewis, Richard a William, lawysgrifau a beirdd o’u cwmpas; yn 1751 sefydlodd Cymry Llundain Anrhydeddus Gymdeithas y Cymmrodorion, dilynodd y Gwyneddigion yn 1770, a dechreuodd eu heisteddfod yng Nghorwen yn 1789 yr eisteddfod fel yr adwaen y genedl hi. Daeth Evan Evans, Ieuan Fardd, â barddoniaeth y tywysogion i’r golau eto, canodd telynorion fel John Parry, Parri Ddall, y delyn deires yn y plastai mawr, ac yn 1792 cynhaliodd Iolo Morganwg Orsedd gyntaf Beirdd Ynys Prydain ar Fryn y Briallu yn Llundain, gan ddwyn traddodiad barddol Cymru gerbron y byd. Erbyn diwedd y ganrif roedd y gweithfeydd haearn mawr cyntaf yn codi ym Merthyr, roedd copr yn llifo o Fynydd Parys, ac roedd pobl a allai ddarllen, canu a dadlau yn eu hiaith eu hunain yn barod ar gyfer oes diwydiant."])

INDUSTRIAL = dict(spanEn="1800 – 1914", spanCy="1800 – 1914")

# ---------- what moves where ----------
# people by the year they were born (data._born): a later rule wins
STAY_PRINCES = {"gwenllian-ferch-llywelyn"}          # born 1282, her story is the end of the princes
STAY_TUDOR = {"elihu-yale"}
STAY_INDUSTRIAL = set()
TO_REVIVAL = {"ann-griffiths", "john-evans-waunfawr"}  # born after 1770, but their work belongs to the revival
# places: an ancient place stays in the Stone Age only if its date is 2500 BC or older
PLACE_TO = {"blaenavon": "industrial", "ybala": "revival"}
# long reads, legends and tales that have no year of their own
ITEM_TO = {("story", "glyndwr"): "glyndwr", ("story", "longbow"): "glyndwr", ("legend", "owain"): "glyndwr",
           ("story", "iolo"): "revival"}

KEYS = {"The Red Lady of Paviland", "Builders of the dolmens", "Copper from the Great Orme", "The Mold gold cape", "The hillfort tribes",
        "The druids of Môn", "Caswallon against Caesar", "Statute of Rhuddlan", "Dafydd ap Gwilym", "Parliament at Machynlleth",
        "The Pennal Letter", "The circulating schools", "The Methodist revival", "Pantycelyn’s first hymns", "The Corwen eisteddfod",
        "The first Gorsedd", "Lhuyd shows Welsh has sister tongues"}

EVENTS_NEW = [
 ("britons", -54, 0, 0, "", "Caswallon against Caesar", "Caswallon yn erbyn Cesar",
  "Julius Caesar crosses to Britain a second time and is met by Cassivellaunus, the Caswallon of Welsh tradition, who leads the Britons against him. Within months Caesar has gone back to Gaul.",
  "Mae Iŵl Cesar yn croesi i Brydain am yr eildro ac yn cael ei wynebu gan Cassivellaunus, Caswallon traddodiad Cymru, sy’n arwain y Brythoniaid yn ei erbyn. O fewn misoedd mae Cesar wedi mynd yn ôl i Âl.",
  1, "", "Cassivellaunus"),
]


def _bc_year(text):
    m = re.search(r"([\d,]+)\s*BC", text or "")
    return -int(m.group(1).replace(",", "")) if m else None


def _year(text):
    m = re.search(r"(\d{3,4})", text or "")
    return int(m.group(1)) if m else None


def event_era(era, y):
    if era in ("ancient", "britons"):
        return "ancient" if y < -2500 else "britons" if y < 48 else era
    if era in ("medieval", "glyndwr"):
        return "glyndwr" if y >= 1284 else "medieval"
    if era in ("tudor", "revival", "industrial", "modern", "today"):  # by year, so the timeline never jumps back an age
        return era_of_year(max(y, 1485))
    return era


def person_era(pid, era, born):
    if era == "ancient":
        return "ancient" if born and born < -2500 else "britons"
    if era == "medieval" and born >= 1254 and pid not in STAY_PRINCES:
        return "glyndwr"
    if era == "tudor" and born >= 1660 and pid not in STAY_TUDOR:
        return "revival"
    if era == "industrial" and ((born and born < 1770 and pid not in STAY_INDUSTRIAL) or pid in TO_REVIVAL):
        return "revival"
    return era


def place_era(p):
    era, pid = p["era"], p["id"]
    if pid in PLACE_TO:
        return PLACE_TO[pid]
    if era == "ancient":
        y = _bc_year(p["year"])
        return "ancient" if y is not None and y <= -2500 else "britons"
    if era == "medieval":
        y = _year(p["year"])
        return "glyndwr" if y and y >= 1283 else era
    if era == "tudor":
        y = _year(p["year"])
        return "revival" if y and 1700 <= y < 1800 else era
    if era == "industrial":
        y = _year(p["year"])
        return "revival" if y and y < 1800 else era
    return era


def remap(kind, x):
    """The age for a long read, legend, tale or other item that carries only an age, not a year."""
    era = x["era"]
    if (kind, x.get("id")) in ITEM_TO:
        return ITEM_TO[(kind, x.get("id"))]
    return "britons" if era == "ancient" else era


def apply(ns):
    """Called at the end of data.py with its globals: reshape ERAS and move every event, person and place."""
    by = {x["id"]: x for x in ns["ERAS"]}
    anc, med, tud, ind = by["ancient"], by["medieval"], by["tudor"], by["industrial"]
    anc.update(STONE)
    for k in ("spanEn", "spanCy", "blurbEn", "blurbCy"):
        med[k] = PRINCES[k]
    med["storyEn"] = [med["storyEn"][0], PRINCES["p2En"]]
    med["storyCy"] = [med["storyCy"][0], PRINCES["p2Cy"]]
    for k in ("spanEn", "spanCy", "blurbEn", "blurbCy"):
        tud[k] = TUDOR[k]
    for lang in ("En", "Cy"):
        t = tud["story" + lang][-1]
        tud["story" + lang] = tud["story" + lang][:-1] + [t[:t.index(TUDOR["cut" + lang])] + TUDOR["end" + lang]]
    ind.update(INDUSTRIAL)
    by.update(britons=BRITONS, glyndwr=GLYNDWR, revival=REVIVAL)
    ns["ERAS"] = [by[k] for k in ORDER]

    keys = KEYS
    evs = [(event_era(ev[0], ev[1]),) + ev[1:] for ev in ns["EVENTS"]] + EVENTS_NEW
    ns["EVENTS"] = sorted([ev[:9] + (1,) + ev[10:] if ev[5] in keys else ev for ev in evs], key=lambda ev: ev[1])
    born = ns["_born"]
    order = {k: n for n, k in enumerate(ORDER)}
    ns["_ERA_ORDER"] = order
    ns["PEOPLE"] = sorted([(p[0], person_era(p[0], p[1], born(p))) + p[2:] for p in ns["PEOPLE"]], key=lambda p: (order[p[1]], born(p)))
    ns["PLACES"] = [dict(p, era=place_era(p)) for p in ns["PLACES"]] + NEW_PLACES


# ---------- new places of the Age of Revival ----------
def _P(id, en, cy, era, lat, lon, year, ill, wiki, dEn, dCy):
    return dict(id=id, en=en, cy=cy, era=era, lat=lat, lon=lon, year=year, ill=ill, src=wiki, dEn=dEn, dCy=dCy)


NEW_PLACES = [
 _P("trefeca", "Trefeca", "Trefeca", "revival", 51.981, -3.248, "1752", "chapel", "Trefeca",
    "The home of Howell Harris near Talgarth, where in 1752 he gathered a Christian ‘family’ of some 120 people who worked at up to sixty crafts and ran a printing press.",
    "Cartref Howell Harris ger Talgarth, lle casglodd yn 1752 ‘deulu’ Cristnogol o ryw 120 o bobl a weithiai ar hyd at drigain o grefftau ac a redai wasg argraffu."),
 _P("llangeitho", "Llangeitho", "Llangeitho", "revival", 52.219, -4.021, "1735", "chapel", "Llangeitho",
    "The Ceredigion village where Daniel Rowland preached for more than fifty years. Thousands came from all over Wales on communion Sundays, and his statue stands outside Capel Gwynfil.",
    "Y pentref yng Ngheredigion lle bu Daniel Rowland yn pregethu am dros hanner can mlynedd. Deuai miloedd o bob rhan o Gymru ar Suliau cymun, ac mae ei gerflun yn sefyll y tu allan i Gapel Gwynfil."),
 _P("llanddowror", "Llanddowror", "Llanddowror", "revival", 51.803, -4.532, "1716–1761", "book", "Llanddowror",
    "The Carmarthenshire parish of Griffith Jones, whose circulating schools taught Wales to read. He was rector here from 1716 and lies buried at its church of St Teilo.",
    "Plwyf Griffith Jones yn Sir Gaerfyrddin, a’i ysgolion cylchynol a ddysgodd Gymru i ddarllen. Bu’n rheithor yma o 1716 ac mae wedi’i gladdu yn eglwys Teilo Sant."),
 _P("pantycelyn", "Pantycelyn", "Pantycelyn", "revival", 52.004, -3.720, "1748–1791", "harp", "William_Williams_Pantycelyn",
    "The farmhouse near Llandovery that was home to William Williams, the great hymn writer of Wales, from his marriage until his death. He took his bardic name from it.",
    "Y ffermdy ger Llanymddyfri a fu’n gartref i William Williams, emynydd mawr Cymru, o’i briodas hyd ei farw. Oddi wrtho y cymerodd ei enw."),
]

LONG = {
 "trefeca": (
  ["## The home of Howell Harris",
   "Trefeca lies between Talgarth and Llangors Lake in Breconshire. Howell Harris was born here in 1714, and from here he rode out in 1735 to preach across Wales, one of the leaders of the Methodist revival.[[cite:ag-wiki-trefeca]]",
   "## The family at Trefeca",
   "In 1752 Harris gathered a Christian community around his home, Teulu Trefeca, the family of Trefeca. A gift of £900 from Madam Sidney Griffith of Cefnamlwch let him enlarge the house and add a chapel, an infirmary, a bathhouse, a dovecote and a fishpond, all built in a new ‘Gothick’ style, among the first in Wales. At its height some 120 people lived there, working at up to sixty crafts and trades. Harris set up a woollen school with eight looms, helped to found the first agricultural society in Wales in 1754, and from 1758 a printing press at Trefeca printed books.[[cite:ag-cadw-trefeca]]",
   "John Wesley preached at Trefeca more than once, and in 1768 the Countess of Huntingdon opened a college for preachers nearby.[[cite:ag-wiki-trefeca,ag-cadw-trefeca]]",
   "## Trefeca today",
   "In 1842 the Calvinistic Methodists opened a college in Harris’s old home, and today Coleg Trefeca is a centre of the Presbyterian Church of Wales, with a small museum to Howell Harris and his family.[[cite:ag-wiki-trefeca]]"],
  ["## Cartref Howell Harris",
   "Saif Trefeca rhwng Talgarth a Llyn Syfaddan yn Sir Frycheiniog. Ganed Howell Harris yma yn 1714, ac oddi yma y marchogodd allan yn 1735 i bregethu ar draws Cymru, yn un o arweinwyr y diwygiad Methodistaidd.[[cite:ag-wiki-trefeca]]",
   "## Teulu Trefeca",
   "Yn 1752 casglodd Harris gymuned Gristnogol o gwmpas ei gartref, Teulu Trefeca. Gyda rhodd o £900 gan Madam Sidney Griffith o Gefnamlwch helaethodd y tŷ ac ychwanegu capel, clafdy, tŷ ymolchi, colomendy a phwll pysgod, i gyd yn null newydd y ‘Gothick’, ymhlith y cyntaf yng Nghymru. Ar ei anterth roedd tua 120 o bobl yn byw yno, yn gweithio ar hyd at drigain o grefftau. Sefydlodd Harris ysgol wlân ag wyth gwŷdd, helpodd i sefydlu’r gymdeithas amaethyddol gyntaf yng Nghymru yn 1754, ac o 1758 argraffai gwasg yn Nhrefeca lyfrau.[[cite:ag-cadw-trefeca]]",
   "Pregethodd John Wesley yn Nhrefeca fwy nag unwaith, ac yn 1768 agorodd Iarlles Huntingdon goleg i bregethwyr gerllaw.[[cite:ag-wiki-trefeca,ag-cadw-trefeca]]",
   "## Trefeca heddiw",
   "Yn 1842 agorodd y Methodistiaid Calfinaidd goleg yn hen gartref Harris, a heddiw mae Coleg Trefeca yn ganolfan i Eglwys Bresbyteraidd Cymru, gydag amgueddfa fach i Howell Harris a’i deulu.[[cite:ag-wiki-trefeca]]"]),
 "llangeitho": (
  ["## Daniel Rowland’s village",
   "Daniel Rowland was born in 1713 at Pantybeudy, Nantcwnlle, a few miles from Llangeitho, and served as curate here. Around 1735, under the preaching of Griffith Jones, he was gripped by a deep conviction, and he began to preach with a fire that drew people from far away.[[cite:ag-dwb-rowland]]",
   "## The heart of Welsh Methodism",
   "Llangeitho became the gathering place of the Methodists of Wales. On communion Sundays thousands came from every part of the country, walking over the mountains to hear him.[[cite:ag-dwb-rowland]] Around 1763 he lost his curacy, and he went on preaching to his people in the chapel built for him in the village, the New Church, which became Capel Gwynfil.[[cite:ag-dwb-rowland,ag-lb-rowland]]",
   "He died on 16 October 1790 and was buried at Llangeitho.[[cite:ag-dwb-rowland]]",
   "## Llangeitho today",
   "In 1883 a white marble statue of Rowland by Edward Griffiths of Chester was raised in front of Capel Gwynfil. He stands in the clothes of an eighteenth-century clergyman, his right arm raised and a book open in his hand, still preaching to the road.[[cite:ag-lb-rowland]]"],
  ["## Pentref Daniel Rowland",
   "Ganed Daniel Rowland yn 1713 ym Mhantybeudy, Nantcwnlle, ychydig filltiroedd o Langeitho, a bu’n gurad yma. Tua 1735, dan bregethu Griffith Jones, daeth argyhoeddiad dwfn drosto, a dechreuodd bregethu â thân a dynnai bobl o bell.[[cite:ag-dwb-rowland]]",
   "## Calon Methodistiaeth Cymru",
   "Daeth Llangeitho yn fan cyfarfod Methodistiaid Cymru. Ar Suliau cymun deuai miloedd o bob rhan o’r wlad, gan gerdded dros y mynyddoedd i’w glywed.[[cite:ag-dwb-rowland]] Tua 1763 collodd ei guradiaeth, ac aeth ymlaen i bregethu i’w bobl yn y capel a godwyd iddo yn y pentref, yr Eglwys Newydd, a ddaeth yn Gapel Gwynfil.[[cite:ag-dwb-rowland,ag-lb-rowland]]",
   "Bu farw ar 16 Hydref 1790 a’i gladdu yn Llangeitho.[[cite:ag-dwb-rowland]]",
   "## Llangeitho heddiw",
   "Yn 1883 codwyd cerflun marmor gwyn o Rowland gan Edward Griffiths o Gaer o flaen Capel Gwynfil. Saif yng ngwisg clerigwr o’r ddeunawfed ganrif, ei fraich dde wedi’i chodi a llyfr ar agor yn ei law, yn dal i bregethu i’r ffordd.[[cite:ag-lb-rowland]]"]),
 "llanddowror": (
  ["## The rector of Llanddowror",
   "Griffith Jones was born in 1683 in the parish of Penboyr in Carmarthenshire. Ordained in 1708, he became rector of Llanddowror in 1716, appointed by his patron Sir John Philipps of Picton.[[cite:ag-dwb-gjones]]",
   "## The circulating schools",
   "His great work was the Welsh circulating schools. A teacher would stay in a parish for three months or so, usually in winter when farm work was light, teaching children and grown men and women to read the Bible in Welsh, and then move on to the next parish. By 1737 there were 37 schools with 2,400 scholars. Each year he reported their progress in Welch Piety, and by his death the schools had numbered 3,495 and taught more than 158,000 scholars.[[cite:ag-dwb-gjones]] With his friend and patron Bridget Bevan of Laugharne, who carried the schools on after him until 1779, he made the Welsh a nation of readers.[[cite:ag-dwb-gjones,ag-ciw-llanddowror]]",
   "He died at Madam Bevan’s home in Laugharne on 8 April 1761 and was buried at Llanddowror church.[[cite:ag-dwb-gjones]]",
   "## Llanddowror today",
   "The church of St Teilo stands beside the A477, about two miles south-west of St Clears. Its west tower is late medieval and its font of the fifteenth century; the rest was rebuilt in 1865.[[cite:ag-ciw-llanddowror]]"],
  ["## Rheithor Llanddowror",
   "Ganed Griffith Jones yn 1683 ym mhlwyf Penboyr yn Sir Gaerfyrddin. Fe’i hordeiniwyd yn 1708, a daeth yn rheithor Llanddowror yn 1716, wedi’i benodi gan ei noddwr Syr John Philipps o Gastell Pictwn.[[cite:ag-dwb-gjones]]",
   "## Yr ysgolion cylchynol",
   "Ei waith mawr oedd ysgolion cylchynol Cymru. Arhosai athro mewn plwyf am ryw dri mis, fel arfer yn y gaeaf pan oedd gwaith y fferm yn ysgafn, gan ddysgu plant a dynion a merched mewn oed i ddarllen y Beibl yn Gymraeg, ac yna symud ymlaen i’r plwyf nesaf. Erbyn 1737 roedd 37 o ysgolion a 2,400 o ddisgyblion. Bob blwyddyn adroddai eu hynt yn Welch Piety, ac erbyn ei farw roedd 3,495 o ysgolion wedi bod, ac roeddent wedi dysgu dros 158,000 o ddisgyblion.[[cite:ag-dwb-gjones]] Gyda’i gyfaill a’i noddwr Bridget Bevan o Dalacharn, a gariodd yr ysgolion ymlaen ar ei ôl hyd 1779, gwnaeth y Cymry yn genedl o ddarllenwyr.[[cite:ag-dwb-gjones,ag-ciw-llanddowror]]",
   "Bu farw yng nghartref Madam Bevan yn Nhalacharn ar 8 Ebrill 1761, a’i gladdu yn eglwys Llanddowror.[[cite:ag-dwb-gjones]]",
   "## Llanddowror heddiw",
   "Saif eglwys Teilo Sant wrth ymyl yr A477, tua dwy filltir i’r de-orllewin o Sanclêr. Mae ei thŵr gorllewinol o ddiwedd yr Oesoedd Canol a’i bedyddfaen o’r bymthegfed ganrif; ailadeiladwyd y gweddill yn 1865.[[cite:ag-ciw-llanddowror]]"]),
 "pantycelyn": (
  ["## The hymn writer’s home",
   "Pantycelyn is a farmhouse down a lane near Pentre-tŷ-gwyn, a few miles from Llandovery. It was the family home of Dorothy Williams, mother of William Williams, and he lived here from his marriage in 1748 or 1749 until his death in 1791. The house may go back to the late sixteenth century, and it has stayed in the family ever since.[[cite:ag-lb-pantycelyn]]",
   "## Pantycelyn",
   "William Williams was one of the leaders of the Methodist revival alongside Howell Harris and Daniel Rowland, and he rode thousands of miles across Wales to preach. He is remembered above all as the sweet singer of Wales: his hymns are sung in chapels to this day, and ‘Arglwydd, arwain trwy’r anialwch’ is sung around the world as ‘Guide me, O thou great Redeemer’. So close is the man to the place that Wales has called him simply Pantycelyn for more than two hundred years.",
   "He lies in the churchyard of St Mary’s on the north-eastern edge of Llandovery, on the site of the Roman fort of Alabum.[[cite:ag-wiki-llanfair]]"],
  ["## Cartref yr emynydd",
   "Ffermdy i lawr lôn ger Pentre-tŷ-gwyn, ychydig filltiroedd o Lanymddyfri, yw Pantycelyn. Hwn oedd cartref teulu Dorothy Williams, mam William Williams, a bu ef yn byw yma o’i briodas yn 1748 neu 1749 hyd ei farw yn 1791. Efallai fod y tŷ yn mynd yn ôl i ddiwedd yr unfed ganrif ar bymtheg, ac mae wedi aros yn y teulu byth ers hynny.[[cite:ag-lb-pantycelyn]]",
   "## Pantycelyn",
   "Roedd William Williams yn un o arweinwyr y diwygiad Methodistaidd gyda Howell Harris a Daniel Rowland, a marchogodd filoedd o filltiroedd drwy Gymru i bregethu. Fe’i cofir yn anad dim fel pêr ganiedydd Cymru: cenir ei emynau yn y capeli hyd heddiw, a chenir ‘Arglwydd, arwain trwy’r anialwch’ ledled y byd fel ‘Guide me, O thou great Redeemer’. Mor agos yw’r dyn at y lle fel mai Pantycelyn yn unig yw ei enw yng Nghymru ers dros ddau gan mlynedd.",
   "Mae’n gorwedd ym mynwent eglwys y Santes Fair ar gyrion gogledd-ddwyrain Llanymddyfri, ar safle caer Rufeinig Alabum.[[cite:ag-wiki-llanfair]]"]),
}

PEOPLE = {
 "trefeca": ["howell-harris"],
 "llangeitho": ["daniel-rowland", "griffith-jones"],
 "llanddowror": ["griffith-jones"],
 "pantycelyn": ["pantycelyn", "howell-harris", "daniel-rowland"],
}

# the picture at the top of each new place page (src/pictures.py PAGE)
# (Trefeca has no picture kept on the site yet, so it takes the picture of its age.)
PICTURES = {"place-llangeitho.html": "p:daniel-rowland", "place-llanddowror.html": "g:person-griffith-jones",
            "place-pantycelyn.html": "g:person-pantycelyn"}

# Sources beside the claims (merged into cites.S). Every one was opened and read when the text was written.
CITES = {
 "ag-wiki-trefeca": dict(short=("Wikipedia", "Wikipedia"), t="Trefeca", by=("Wikipedia", "Wikipedia"),
     note=("Between Talgarth and Llangorse Lake; birthplace and home of Howell Harris; Teulu Trefeca founded 1752 on the Moravian model; Wesley preached there in 1769; the Countess of Huntingdon’s college from 1768; the college of 1842; now Coleg Trefeca, with the Howell Harris Museum.",
           "Rhwng Talgarth a Llyn Syfaddan; man geni a chartref Howell Harris; sefydlu Teulu Trefeca yn 1752 ar batrwm y Morafiaid; pregethodd Wesley yno yn 1769; coleg Iarlles Huntingdon o 1768; coleg 1842; heddiw Coleg Trefeca, gydag Amgueddfa Howell Harris."),
     url="https://en.wikipedia.org/wiki/Trefeca", lang="en"),
 "ag-cadw-trefeca": dict(short=("Cadw", "Cadw"), t="Coleg Trefeca, listed building 6637", by=("Cadw, full report for listed buildings", "Cadw, adroddiad llawn ar adeiladau rhestredig"),
     note=("Grade II*; the £900 gift of Madam Sidney Griffith; chapel, infirmary, bathhouse, dovecote and fishpond in a ‘Modern Gothick’ style, 1752 to 1759; first agricultural society in Wales 1754; woollen school with eight looms 1756; printing press 1758 to 1806; about 120 people and up to 60 crafts.",
           "Gradd II*; rhodd £900 Madam Sidney Griffith; capel, clafdy, tŷ ymolchi, colomendy a phwll pysgod yn null y ‘Modern Gothick’, 1752 i 1759; y gymdeithas amaethyddol gyntaf yng Nghymru 1754; ysgol wlân ag wyth gwŷdd 1756; gwasg argraffu 1758 i 1806; tua 120 o bobl a hyd at 60 o grefftau."),
     url="https://cadwpublic-api.azurewebsites.net/reports/listedbuilding/FullReport?id=6637", lang="en"),
 "ag-dwb-rowland": dict(short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"), t="Rowland, Daniel (1713–1790), Methodist cleric",
     by=("Gomer Morgan Roberts, Dictionary of Welsh Biography, National Library of Wales", "Gomer Morgan Roberts, Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
     note=("Born 1713 at Pantybeudy, Nantcwnlle; conviction about 1735 under Griffith Jones; Llangeitho the centre of Welsh Methodism, with thousands on communion Sundays; deprived of his curacy about 1763; died 16 October 1790, buried at Llangeitho.",
           "Ganed 1713 ym Mhantybeudy, Nantcwnlle; argyhoeddiad tua 1735 dan Griffith Jones; Llangeitho yn ganolfan Methodistiaeth Cymru, gyda miloedd ar Suliau cymun; collodd ei guradiaeth tua 1763; bu farw 16 Hydref 1790, a’i gladdu yn Llangeitho."),
     url="https://biography.wales/article/s-ROWL-DAN-1713", url_cy="https://bywgraffiadur.cymru/article/s-ROWL-DAN-1713"),
 "ag-lb-rowland": dict(short=("British Listed Buildings", "British Listed Buildings"), t="Statue of Daniel Rowland at Capel Gwynfil, Llangeitho",
     by=("British Listed Buildings, from the Cadw listing (9918)", "British Listed Buildings, o restriad Cadw (9918)"),
     note=("A near life-size white marble statue of 1883 by Edward Griffiths of Chester, in the forecourt of Capel Gwynfil; Rowland founded the chapel about 1760.",
           "Cerflun marmor gwyn bron maint bywyd o 1883 gan Edward Griffiths o Gaer, o flaen Capel Gwynfil; sefydlodd Rowland y capel tua 1760."),
     url="https://britishlistedbuildings.co.uk/300009918-statue-of-daniel-rowland-at-capel-gwynfil-llangeitho", lang="en"),
 "ag-dwb-gjones": dict(short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"), t="Jones, Griffith (1683–1761), cleric and educational reformer",
     by=("Mary Clement, Dictionary of Welsh Biography, National Library of Wales", "Mary Clement, Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
     note=("Born at Pant-yr-efel, Penboyr; ordained 1708; rector of Llanddowror from 1716; 37 schools and 2,400 scholars in 1737; by his death 3,495 schools and over 158,000 scholars recorded in Welch Piety; died 8 April 1761 at Laugharne, buried at Llanddowror; Bridget Bevan kept the schools going until 1779.",
           "Ganed ym Mhant-yr-efel, Penboyr; ordeiniwyd 1708; rheithor Llanddowror o 1716; 37 o ysgolion a 2,400 o ddisgyblion yn 1737; erbyn ei farw 3,495 o ysgolion a dros 158,000 o ddisgyblion yn ôl Welch Piety; bu farw 8 Ebrill 1761 yn Nhalacharn, a’i gladdu yn Llanddowror; cadwodd Bridget Bevan yr ysgolion i fynd hyd 1779."),
     url="https://biography.wales/article/s-JONE-GRI-1683", url_cy="https://bywgraffiadur.cymru/article/s-JONE-GRI-1683"),
 "ag-ciw-llanddowror": dict(short=("Church in Wales", "Yr Eglwys yng Nghymru"), t="Church Heritage Record: St Teilo, Llanddowror",
     by=("The Church in Wales", "Yr Eglwys yng Nghymru"),
     note=("Late medieval west tower, the rest rebuilt in 1865 by Thomas David of Laugharne; a 15th-century font; on the A477 about 3 km south-west of St Clears; Griffith Jones and Bridget Bevan began the circulating schools.",
           "Tŵr gorllewinol o ddiwedd yr Oesoedd Canol, y gweddill wedi’i ailgodi yn 1865 gan Thomas David o Dalacharn; bedyddfaen o’r 15fed ganrif; ar yr A477 tua 3 km i’r de-orllewin o Sanclêr; dechreuodd Griffith Jones a Bridget Bevan yr ysgolion cylchynol."),
     url="https://heritage.churchinwales.org.uk/church-heritage-record-st-teilo-llanddowror-3715", lang="en"),
 "ag-lb-pantycelyn": dict(short=("British Listed Buildings", "British Listed Buildings"), t="Pantycelyn Farmhouse, Llanfair-ar-y-bryn",
     by=("British Listed Buildings, from the Cadw listing (10905)", "British Listed Buildings, o restriad Cadw (10905)"),
     note=("Grade II*; down a lane east of Pentre-tŷ-gwyn; the family home of Dorothy Williams, mother of William Williams; he lived there from his marriage in 1748 or 1749 until his death; possibly late 16th-century; still in the family.",
           "Gradd II*; i lawr lôn i’r dwyrain o Bentre-tŷ-gwyn; cartref teulu Dorothy Williams, mam William Williams; bu ef yn byw yno o’i briodas yn 1748 neu 1749 hyd ei farw; o ddiwedd yr 16eg ganrif efallai; yn dal yn y teulu."),
     url="https://britishlistedbuildings.co.uk/300010905-pantycelyn-farmhouse-llanfair-ar-y-bryn", lang="en"),
 "ag-wiki-llanfair": dict(short=("Wikipedia", "Wikipedia"), t="Llanfair-ar-y-bryn", by=("Wikipedia", "Wikipedia"),
     note=("William Williams Pantycelyn lived in the parish for much of his life and is buried at St Mary’s church, on the north-eastern edge of Llandovery, on the site of the Roman fort of Alabum.",
           "Bu William Williams Pantycelyn yn byw yn y plwyf am ran helaeth o’i oes ac mae wedi’i gladdu yn eglwys y Santes Fair, ar gyrion gogledd-ddwyrain Llanymddyfri, ar safle caer Rufeinig Alabum."),
     url="https://en.wikipedia.org/wiki/Llanfair-ar-y-bryn", lang="en"),
}

# ---------- teaching: the enquiry question and ideas on teachers.html (long.TEACH) ----------
TEACH = {
 "ancient": dict(qEn="How do we know about people who left no writing?", qCy="Sut rydyn ni’n gwybod am bobl na adawodd ysgrifen?",
  aEn=["Compare Paviland Cave and Pentre Ifan: what do a burial and a tomb tell us about what people believed?", "Use the map to find the burial chamber nearest your school, and plan a visit or a virtual tour.", "Debate: how did people move the bluestones from Preseli to Stonehenge?"],
  aCy=["Cymharwch Ogof Pafiland a Phentre Ifan: beth mae claddedigaeth a beddrod yn ei ddweud wrthym am gredoau pobl?", "Defnyddiwch y map i ddod o hyd i’r siambr gladdu agosaf at eich ysgol, a chynlluniwch ymweliad.", "Dadl: sut y symudodd pobl y cerrig gleision o’r Preseli i Gôr y Cewri?"]),
 "britons": dict(qEn="Who were the Britons of the Bronze and Iron Ages, and what did they leave us?", qCy="Pwy oedd Brythoniaid Oes yr Efydd ac Oes yr Haearn, a beth a adawsant inni?",
  aEn=["Look closely at the Mold gold cape: who might have worn it, and what does it tell us about the people who made it?", "Find the hillfort nearest your school on the map. Why was it built where it is?", "Debate: what can Caesar and Tacitus tell us about the Britons, and what might they get wrong?"],
  aCy=["Edrychwch yn fanwl ar fantell aur yr Wyddgrug: pwy allai fod wedi’i gwisgo, a beth mae’n ei ddweud am y bobl a’i gwnaeth?", "Dewch o hyd i’r fryngaer agosaf at eich ysgol ar y map. Pam y’i codwyd yn y fan honno?", "Dadl: beth all Cesar a Tacitus ei ddweud wrthym am y Brythoniaid, a beth allen nhw ei gael yn anghywir?"]),
 "medieval": dict(qEn="How did the princes of Wales hold their country for two hundred years?", qCy="Sut y daliodd tywysogion Cymru eu gwlad am ddau gan mlynedd?",
  aEn=["Put the turning points from 1100 to 1282 in order and decide which mattered most.", "Read about Gwenllian and Llywelyn ap Gruffudd, and write a short poem or elegy in the style of a poet of the princes.", "Investigate a castle of the Welsh princes, such as Dolbadarn or Castell y Bere: where was it built, and why there?"],
  aCy=["Rhowch y trobwyntiau o 1100 i 1282 mewn trefn a phenderfynwch pa un oedd bwysicaf.", "Darllenwch am Wenllian a Llywelyn ap Gruffudd, ac ysgrifennwch gerdd neu farwnad fer yn null un o feirdd y tywysogion.", "Ymchwiliwch i un o gestyll tywysogion Cymru, fel Dolbadarn neu Gastell y Bere: ble y’i codwyd, a pham yno?"]),
 "glyndwr": dict(qEn="Why did the Welsh keep rising after 1282, and what did Owain Glyndŵr want for Wales?", qCy="Pam y daliodd y Cymry i godi ar ôl 1282, a beth oedd Owain Glyndŵr ei eisiau i Gymru?",
  aEn=["Investigate Edward I’s castles: were they built to defend, to control, or to impress?", "Write Owain Glyndŵr’s Pennal Letter in your own words. What did he want for the church and for learning in Wales?", "Read a cywydd by Dafydd ap Gwilym in translation, and write your own poem in praise of a place you love."],
  aCy=["Ymchwiliwch i gestyll Edward I: ai i amddiffyn, i reoli neu i greu argraff y’u codwyd?", "Ysgrifennwch Lythyr Pennal Owain Glyndŵr yn eich geiriau eich hun. Beth oedd ei eisiau i’r eglwys ac i ddysg yng Nghymru?", "Darllenwch gywydd gan Ddafydd ap Gwilym mewn cyfieithiad, ac ysgrifennwch eich cerdd eich hun i ganmol lle rydych yn ei garu."]),
 "tudor": dict(qEn="Did the Tudors help Wales or harm it?", qCy="Ai helpu Cymru neu ei niweidio wnaeth y Tuduriaid?",
  aEn=["Compare the Acts of Union with the Welsh Bible of 1588: one pushed Welsh out of the courts, the other put it in every church. Which mattered more?", "Find out about the first Welsh chapel at Llanfaches in 1639. Why did people want to worship in their own way?", "Write a letter home from a Welsh soldier after the battle of St Fagans in 1648."],
  aCy=["Cymharwch y Deddfau Uno â Beibl Cymraeg 1588: gwthiodd y naill y Gymraeg o’r llysoedd, a rhoddodd y llall hi ym mhob eglwys. Pa un oedd bwysicaf?", "Darganfyddwch am y capel Cymraeg cyntaf yn Llanfaches yn 1639. Pam roedd pobl eisiau addoli yn eu ffordd eu hunain?", "Ysgrifennwch lythyr adref gan filwr o Gymro ar ôl brwydr Sain Ffagan yn 1648."]),
 "revival": dict(qEn="How did Wales become a nation of readers, hymn singers and eisteddfodau?", qCy="Sut y daeth Cymru’n genedl o ddarllenwyr, cantorion emynau ac eisteddfodau?",
  aEn=["Find out how Griffith Jones’s circulating schools worked, and plan a three-month school of your own.", "Sing or read a hymn by Pantycelyn and talk about the pictures in its words.", "Hold a class eisteddfod with a chair for the best poem, as the Gwyneddigion did at Corwen in 1789."],
  aCy=["Darganfyddwch sut roedd ysgolion cylchynol Griffith Jones yn gweithio, a chynlluniwch eich ysgol dri mis eich hun.", "Canwch neu darllenwch emyn gan Bantycelyn a thrafodwch y lluniau yn ei eiriau.", "Cynhaliwch eisteddfod ddosbarth gyda chadair am y gerdd orau, fel y gwnaeth y Gwyneddigion yng Nghorwen yn 1789."]),
}

# one short question on each age's home page card (build.py ERA_Q)
ERA_Q = {
 "ancient": ("Who were the first people of Wales, and who raised its great stone tombs?", "Pwy oedd pobl gyntaf Cymru, a phwy a gododd ei beddrodau cerrig mawr?"),
 "britons": ("Who built the hillforts of Wales, and who were the druids of Môn?", "Pwy a gododd fryngaerau Cymru, a phwy oedd derwyddon Môn?"),
 "glyndwr": ("Why did Owain Glyndŵr rise, and what did he want for Wales?", "Pam y cododd Owain Glyndŵr, a beth oedd ei eisiau i Gymru?"),
 "revival": ("How did Wales become a nation of readers, hymns and eisteddfodau?", "Sut y daeth Cymru’n genedl o ddarllenwyr, emynau ac eisteddfodau?"),
}

# the Visiting box on the new place pages (src/visit.py)
VISIT = dict(
 trefeca=("church", "", "", "free", ("Coleg Trefeca is a church centre; the Howell Harris Museum there is open by appointment.", "Canolfan eglwysig yw Coleg Trefeca; mae Amgueddfa Howell Harris yno ar agor drwy drefniant.")),
 llangeitho=("town", "", "", "open", ("Rowland’s statue stands in front of Capel Gwynfil, beside the road to Aberystwyth.", "Saif cerflun Rowland o flaen Capel Gwynfil, wrth y ffordd i Aberystwyth.")),
 llanddowror=("church", "", "SA33 4HL", "church", ("St Teilo’s church stands beside the A477, south-west of St Clears.", "Saif eglwys Teilo Sant wrth yr A477, i’r de-orllewin o Sanclêr.")),
 pantycelyn=("private", "", "", "outside", ("The farmhouse is a private home. Williams’s grave is at St Mary’s church, Llanfair-ar-y-bryn, on the edge of Llandovery.", "Cartref preifat yw’r ffermdy. Mae bedd Williams yn eglwys y Santes Fair, Llanfair-ar-y-bryn, ar gyrion Llanymddyfri.")),
)

# ---------- teacher packs (src/teachpacks.py PACKS): the new ages, and the ages that changed shape ----------
PACKS = {
 "ancient": dict(
  big=("People have lived in Wales for more than 200,000 years. Neanderthals sheltered at Pontnewydd, a young man was buried with honour at Paviland, hunters followed the herds as the ice melted, and the first farmers raised great stone tombs that still stand on our hills.",
       "Mae pobl wedi byw yng Nghymru ers dros 200,000 o flynyddoedd. Cysgododd Neanderthaliaid ym Mhontnewydd, claddwyd dyn ifanc gydag anrhydedd ym Mhafiland, dilynodd helwyr yr anifeiliaid wrth i’r iâ doddi, a chododd y ffermwyr cyntaf feddrodau cerrig mawr sy’n dal i sefyll ar ein bryniau."),
  what=[0, 2, 3],
  qs=[("Why did people carry the bluestones from Preseli all the way to Stonehenge?", "Pam y cariodd pobl y cerrig gleision o’r Preseli yr holl ffordd i Gôr y Cewri?"),
      ("What does the burial at Paviland tell us about how people cared for their dead?", "Beth mae’r gladdedigaeth ym Mhafiland yn ei ddweud wrthym am sut roedd pobl yn gofalu am eu meirw?"),
      ("How did farming change the way people lived?", "Sut newidiodd ffermio y ffordd roedd pobl yn byw?")],
  words=["cromlech", "maen-hir", "bluestones"],
  acts=[[("Make a ‘museum box’ of objects a Stone Age family would need. Draw or model each one and say what it was for.", "Gwnewch ‘focs amgueddfa’ o bethau y byddai teulu o Oes y Cerrig eu hangen. Lluniwch neu fodelwch bob un a dweud beth oedd ei bwrpas."),
         ("Find the nearest burial chamber or standing stone to your school on the historic sites map, and plan a visit.", "Dewch o hyd i’r siambr gladdu neu’r maen hir agosaf at eich ysgol ar y map safleoedd hanesyddol, a chynlluniwch ymweliad.")],
        [("Work out how the bluestones might have been moved 150 miles. Test sledges and rollers with a heavy box in the yard.", "Gweithiwch allan sut y gallai’r cerrig gleision fod wedi’u symud 150 milltir. Profwch slediau a rholeri gyda bocs trwm ar yr iard."),
         ("Copy the spirals and zigzags carved on the stones of Barclodiad y Gawres. What might they have meant?", "Copïwch y troellau a’r patrymau igam-ogam a gerfiwyd ar gerrig Barclodiad y Gawres. Beth allen nhw fod wedi’i olygu?")],
        [("Compare what archaeologists say about Pontnewydd and Paviland with what was first believed in 1823. How does new evidence change the story?", "Cymharwch yr hyn y mae archaeolegwyr yn ei ddweud am Bontnewydd a Phafiland â’r hyn a gredid gyntaf yn 1823. Sut mae tystiolaeth newydd yn newid y stori?"),
         ("The first farmers came about 4000 BC. Was farming a step forward for everyone? Weigh up what was gained and lost.", "Daeth y ffermwyr cyntaf tua 4000 CC. Oedd ffermio’n gam ymlaen i bawb? Pwyswch a mesurwch yr hyn a enillwyd ac a gollwyd.")]],
  doc=None),
 "britons": dict(
  big=("Before Rome, the Britons of Wales mined copper on the Great Orme, beat gold into the Mold cape, built hundreds of hillforts and gave treasures to the lake at Llyn Cerrig Bach. They had kings, druids and skilled smiths, and their British tongue grew into Welsh.",
       "Cyn Rhufain, cloddiodd Brythoniaid Cymru gopr ar y Gogarth, curo aur yn fantell yr Wyddgrug, codi cannoedd o fryngaerau a rhoi trysorau i’r llyn yn Llyn Cerrig Bach. Roedd ganddynt frenhinoedd, derwyddon a gofaint medrus, a thyfodd eu hiaith Frythoneg yn Gymraeg."),
  what=[0, 3, 1],
  qs=[("What can a hillfort tell us about the people who built it?", "Beth all bryngaer ei ddweud wrthym am y bobl a’i hadeiladodd?"),
      ("Why did people give swords and treasures to the waters at Llyn Cerrig Bach?", "Pam y rhoddodd pobl gleddyfau a thrysorau i’r dyfroedd yn Llyn Cerrig Bach?"),
      ("Who were the druids, and how do we know about them?", "Pwy oedd y derwyddon, a sut rydyn ni’n gwybod amdanynt?")],
  words=["britons", "brythonic", "hillfort", "druids", "silures", "ordovices"],
  acts=[[("Design a hillfort for your area: where would you build it, and why? Label the ramparts, the gate and the roundhouses.", "Cynlluniwch fryngaer ar gyfer eich ardal: ble byddech chi’n ei hadeiladu, a pham? Labelwch y rhagfuriau, y porth a’r tai crwn."),
         ("Draw the Mold gold cape and decorate a paper cape of your own with the same patterns.", "Lluniwch fantell aur yr Wyddgrug ac addurnwch fantell bapur eich hun â’r un patrymau.")],
        [("Imagine you are a miner on the Great Orme 4,000 years ago. Write a day in your life underground.", "Dychmygwch eich bod yn fwynwr ar y Gogarth 4,000 o flynyddoedd yn ôl. Ysgrifennwch ddiwrnod yn eich bywyd dan y ddaear."),
         ("Visit Castell Henllys, or look at it online: how have the roundhouses been built again, and how do we know what they looked like?", "Ymwelwch â Chastell Henllys, neu edrychwch arno ar-lein: sut yr ailgodwyd y tai crwn, a sut rydyn ni’n gwybod sut olwg oedd arnynt?")],
        [("Caesar wrote that Britain was the home of druid learning. Discuss: how far can we trust a Roman writing about his enemies?", "Ysgrifennodd Cesar mai Prydain oedd cartref dysg y derwyddon. Trafodwch: i ba raddau y gallwn ymddiried mewn Rhufeiniwr yn ysgrifennu am ei elynion?"),
         ("Compare the Britons in Caesar with Caswallon in the Welsh Triads and the Brut. Why do the two pictures differ?", "Cymharwch y Brythoniaid yng ngwaith Cesar â Chaswallon yn y Trioedd a’r Brut. Pam mae’r ddau ddarlun yn wahanol?")]],
  doc="caesar"),
 "medieval": dict(
  big=("For almost two hundred years the princes of Gwynedd and Deheubarth held Wales against the Norman and English kings. Owain Gwynedd took the title Prince of Wales, the Lord Rhys held the first eisteddfod, and Llywelyn Fawr and his grandson Llywelyn ap Gruffudd ruled almost all of Wales, until Llywelyn fell at Cilmeri in 1282.",
       "Am bron i ddau gan mlynedd daliodd tywysogion Gwynedd a Deheubarth Gymru yn erbyn brenhinoedd Normanaidd a Seisnig. Cymerodd Owain Gwynedd y teitl Tywysog Cymru, cynhaliodd yr Arglwydd Rhys yr eisteddfod gyntaf, a theyrnasodd Llywelyn Fawr a’i ŵyr Llywelyn ap Gruffudd ar bron y cyfan o Gymru, nes i Lywelyn syrthio yng Nghilmeri yn 1282."),
  what=[1, 3, 4],
  qs=[("Why did it take the Normans 216 years to take Wales, when England fell in five?", "Pam y cymerodd 216 o flynyddoedd i’r Normaniaid gipio Cymru, pan syrthiodd Lloegr mewn pump?"),
      ("Who built the castles of the princes, and what were they for?", "Pwy adeiladodd gestyll y tywysogion, a beth oedd eu pwrpas?"),
      ("What did the title Prince of Wales mean to Llywelyn ap Gruffudd?", "Beth oedd ystyr y teitl Tywysog Cymru i Lywelyn ap Gruffudd?")],
  words=["prince-of-wales", "pura-wallia", "welsh-castles", "treaty-montgomery", "gogynfeirdd", "eisteddfod"],
  acts=[[("Find the nearest castle to school on the castles map. Was it built by a Welsh prince or by an invader?", "Dewch o hyd i’r castell agosaf at yr ysgol ar fap y cestyll. Ai tywysog o Gymro neu oresgynnwr a’i cododd?"),
         ("Hold a class eisteddfod like the Lord Rhys in 1176: a chair for a poem and a prize for music.", "Cynhaliwch eisteddfod ddosbarth fel yr Arglwydd Rhys yn 1176: cadair am gerdd a gwobr am gerddoriaeth.")],
        [("Tell the story of Gwenllian’s stand at Kidwelly in 1136 as a comic strip.", "Adroddwch hanes safiad Gwenllian yng Nghydweli yn 1136 fel stribed comig."),
         ("Compare a castle of the Welsh princes (Dolwyddelan, Castell y Bere) with Caernarfon. How and why are they different?", "Cymharwch gastell un o dywysogion Cymru (Dolwyddelan, Castell y Bere) â Chaernarfon. Sut a pham maen nhw’n wahanol?")],
        [("Read the old man of Pencader’s answer to Henry II. What does it say about the Welsh, and why has it been quoted for 800 years?", "Darllenwch ateb hen ŵr Pencader i Harri’r Ail. Beth mae’n ei ddweud am y Cymry, a pham y’i dyfynnwyd am 800 mlynedd?"),
         ("Read part of Gruffudd ab yr Ynad Coch’s elegy for Llywelyn. Why did the poet feel it was the end of the world?", "Darllenwch ran o farwnad Gruffudd ab yr Ynad Coch i Lywelyn. Pam y teimlai’r bardd mai diwedd y byd ydoedd?")]],
  doc="pencader"),
 "glyndwr": dict(
  big=("After the fall of the princes in 1282 Wales was ruled by its conquerors, but the Welsh rose again and again, and their poets lived through a golden age. In 1400 Owain Glyndŵr was proclaimed Prince of Wales; he held a parliament at Machynlleth, planned a Welsh church and universities, and was never taken.",
       "Wedi cwymp y tywysogion yn 1282 rheolwyd Cymru gan ei choncwerwyr, ond cododd y Cymry dro ar ôl tro, a bu eu beirdd fyw drwy oes aur. Yn 1400 cyhoeddwyd Owain Glyndŵr yn Dywysog Cymru; cynhaliodd senedd ym Machynlleth, cynlluniodd eglwys a phrifysgolion Cymreig, ac ni chafodd ei ddal erioed."),
  what=[1, 3, 4],
  qs=[("What did Owain Glyndŵr want for Wales?", "Beth oedd Owain Glyndŵr ei eisiau i Gymru?"),
      ("Why did Edward I build such great castles in Wales?", "Pam y cododd Edward I gestyll mor fawr yng Nghymru?"),
      ("How did the poets keep Welsh culture alive without princes?", "Sut y cadwodd y beirdd ddiwylliant Cymru’n fyw heb dywysogion?")],
  words=["statute-rhuddlan", "iron-ring", "glyndwr-rising", "pennal-letter", "tripartite-indenture", "cywyddwyr"],
  acts=[[("Design a banner for Owain Glyndŵr, with the four lions of Gwynedd, and say what it stands for.", "Cynlluniwch faner i Owain Glyndŵr, gyda phedwar llew Gwynedd, a dywedwch beth mae’n ei gynrychioli."),
         ("Follow Glyndŵr’s rising on the map: Glyndyfrdwy, Hyddgen, Bryn Glas, Harlech and Machynlleth.", "Dilynwch wrthryfel Glyndŵr ar y map: Glyndyfrdwy, Hyddgen, Bryn Glas, Harlech a Machynlleth.")],
        [("Write Owain Glyndŵr’s Pennal letter in your own words. What were his wishes for Wales?", "Ysgrifennwch Lythyr Pennal Owain Glyndŵr yn eich geiriau eich hun. Beth oedd ei ddymuniadau i Gymru?"),
         ("Play Ride with Glyndŵr, 1400, and explain the choices you made.", "Chwaraewch Marchogaeth gyda Glyndŵr, 1400, ac esboniwch y dewisiadau a wnaethoch.")],
        [("Interpretations: how has Owain Glyndŵr been remembered in 1400, in the Victorian age and today? Use the long reads and the documents page.", "Dehongliadau: sut y cofiwyd Owain Glyndŵr yn 1400, yn oes Victoria a heddiw? Defnyddiwch yr erthyglau a thudalen y dogfennau."),
         ("Read a cywydd of Dafydd ap Gwilym or Iolo Goch in translation. What does it tell us about Welsh life after the conquest?", "Darllenwch gywydd gan Ddafydd ap Gwilym neu Iolo Goch mewn cyfieithiad. Beth mae’n ei ddweud wrthym am fywyd yng Nghymru wedi’r goncwest?")]],
  doc="pennal"),
 "tudor": dict(
  big=("A Welshman, Harri Tudur, took the crown at Bosworth under the red dragon. The Acts of Union made English the language of law, but William Morgan’s Bible of 1588 gave Welsh a standard that carried it through the centuries, and the first chapels and Welsh books prepared the way for the revival to come.",
       "Cipiodd Cymro, Harri Tudur, y goron yn Bosworth dan y ddraig goch. Gwnaeth y Deddfau Uno Saesneg yn iaith y gyfraith, ond rhoddodd Beibl William Morgan yn 1588 safon i’r Gymraeg a’i cariodd drwy’r canrifoedd, a pharatôdd y capeli cyntaf a’r llyfrau Cymraeg y ffordd ar gyfer yr adfywiad i ddod."),
  what=[1, 3, 0],
  qs=[("Why did the Welsh poets call Harri Tudur ‘the son of prophecy’?", "Pam y galwodd beirdd Cymru Harri Tudur yn ‘fab darogan’?"),
      ("How did the Welsh Bible help the language survive?", "Sut helpodd y Beibl Cymraeg yr iaith i oroesi?"),
      ("What changed for Wales after the Acts of Union, and what stayed the same?", "Beth newidiodd i Gymru wedi’r Deddfau Uno, a beth arhosodd yr un fath?")],
  words=["acts-of-union", "great-sessions", "welsh-bible", "nonconformity", "shire"],
  acts=[[("Follow Harri Tudur’s march from Dale to Bosworth on a map, and draw the red dragon banner he carried.", "Dilynwch orymdaith Harri Tudur o Dale i Bosworth ar fap, a lluniwch faner y ddraig goch a gariodd."),
         ("Visit or look up Tŷ Mawr Wybrnant, where William Morgan was born. What would his home have been like?", "Ymwelwch â Thŷ Mawr Wybrnant, neu chwiliwch amdano, lle ganwyd William Morgan. Sut le fyddai ei gartref?")],
        [("Make a timeline of the Welsh language from 1536 to 1588 to 1630. Mark the dangers and the rescues.", "Gwnewch linell amser o’r Gymraeg o 1536 i 1588 i 1630. Marciwch y peryglon a’r achubiaethau."),
         ("Robert Recorde of Tenby invented the equals sign. Make a poster of Welsh inventors and firsts from this age.", "Dyfeisiodd Robert Recorde o Ddinbych-y-pysgod yr arwydd hafal. Gwnewch boster o ddyfeiswyr a phethau cyntaf Cymreig o’r oes hon.")],
        [("Read the language clause of the 1536 Act. What did it say, what did it mean for ordinary people, and why did Welsh survive anyway?", "Darllenwch gymal iaith Deddf 1536. Beth oedd yn ei ddweud, beth oedd yn ei olygu i bobl gyffredin, a pham y goroesodd y Gymraeg er hynny?"),
         ("Was Harri Tudur’s victory good for Wales? Weigh up the evidence on both sides.", "A oedd buddugoliaeth Harri Tudur yn dda i Gymru? Pwyswch a mesurwch y dystiolaeth o’r ddwy ochr.")]],
  doc="union"),
 "revival": dict(
  big=("In the eighteenth century Wales came alive. Griffith Jones’s circulating schools taught a nation to read the Bible in Welsh, the Methodist revival of Howell Harris, Daniel Rowland and Pantycelyn filled the land with preaching and hymns, and scholars, harpers and poets brought back the eisteddfod and the Gorsedd.",
       "Yn y ddeunawfed ganrif daeth Cymru’n fyw. Dysgodd ysgolion cylchynol Griffith Jones genedl i ddarllen y Beibl yn Gymraeg, llanwodd diwygiad Methodistaidd Howell Harris, Daniel Rowland a Phantycelyn y wlad â phregethu ac emynau, a daeth ysgolheigion, telynorion a beirdd â’r eisteddfod a’r Orsedd yn ôl."),
  what=[3, 1, 0],
  qs=[("How did the circulating schools teach so many people to read?", "Sut y dysgodd yr ysgolion cylchynol gymaint o bobl i ddarllen?"),
      ("Why did so many people follow the Methodist preachers?", "Pam y dilynodd cymaint o bobl y pregethwyr Methodistaidd?"),
      ("Why did the eisteddfod and the Gorsedd matter to the Welsh of the 1700s, and why do they still matter?", "Pam roedd yr eisteddfod a’r Orsedd yn bwysig i Gymry’r 1700au, a pham maen nhw’n dal yn bwysig?")],
  words=["circulating-schools", "methodist-revival", "cymanfa", "eisteddfod", "gorsedd", "triple-harp"],
  acts=[[("Find out how Griffith Jones’s circulating schools worked, and plan a three-month school of your own.", "Darganfyddwch sut roedd ysgolion cylchynol Griffith Jones yn gweithio, a chynlluniwch eich ysgol dri mis eich hun."),
         ("Listen to the triple harp and draw one, counting its three rows of strings.", "Gwrandewch ar y delyn deires a lluniwch un, gan gyfrif ei thair rhes o dannau.")],
        [("Sing ‘Arglwydd, arwain trwy’r anialwch’ by Pantycelyn and talk about the journey in its words.", "Canwch ‘Arglwydd, arwain trwy’r anialwch’ gan Bantycelyn a thrafodwch y daith yn ei eiriau."),
         ("Hold a class eisteddfod with a chair for the best poem, as the Gwyneddigion did at Corwen in 1789.", "Cynhaliwch eisteddfod ddosbarth gyda chadair am y gerdd orau, fel y gwnaeth y Gwyneddigion yng Nghorwen yn 1789.")],
        [("Read Griffith Jones’s words from Welch Piety. Why did he insist on teaching in Welsh?", "Darllenwch eiriau Griffith Jones o Welch Piety. Pam y mynnai ddysgu yn Gymraeg?"),
         ("Iolo Morganwg held the first Gorsedd in 1792. How did his vision shape the way Wales sees itself today?", "Cynhaliodd Iolo Morganwg yr Orsedd gyntaf yn 1792. Sut y lluniodd ei weledigaeth y ffordd y mae Cymru’n ei gweld ei hun heddiw?")]],
  doc="welch-piety"),
}


def refs(R):
    """Reading lists for the ages that changed (src/refs2.py PAGES): also shown on every person and place page of that age."""
    P, B, W, L = R.P, R.B, R.W, R.L
    museum = (W, "Amgueddfa Cymru", "Collections Online", "museum.wales",
              "The treasures of prehistoric Wales, such as the Llyn Cerrig Bach hoard and the finds from Paviland, in the national collection.",
              "Trysorau Cymru gynhanesyddol, megis celc Llyn Cerrig Bach a’r darganfyddiadau o Bafiland, yn y casgliad cenedlaethol.", "https://museum.wales/collections/online/")
    coflein = (W, "Royal Commission on the Ancient and Historical Monuments of Wales", "Coflein", "coflein.gov.uk",
               "The national record of the historic sites of Wales, from cave and cromlech to hillfort.", "Cofnod cenedlaethol safleoedd hanesyddol Cymru, o ogof a chromlech i fryngaer.", "https://coflein.gov.uk/")
    return {
     "era-ancient": L(R.PREHIST,
                      (B, "Stephen Aldhouse-Green (ed.)", "Paviland Cave and the ‘Red Lady’: A Definitive Report", "Western Academic and Specialist Press, 2000",
                       "The full study of the oldest ceremonial burial in western Europe.", "Yr astudiaeth lawn o’r gladdedigaeth seremonïol hynaf yng ngorllewin Ewrop."),
                      (B, "Frances Lynch", "Megalithic Tombs and Long Barrows in Britain", "Shire Archaeology, 1997",
                       "The great stone tombs of the first farmers, Pentre Ifan and Bryn Celli Ddu among them.", "Beddrodau cerrig mawr y ffermwyr cyntaf, Pentre Ifan a Bryn Celli Ddu yn eu plith."),
                      museum, coflein, R.CADW),
     "era-britons": L(R.PREHIST, R.CAESAR,
                      (B, "Barry Cunliffe", "Iron Age Communities in Britain", "Routledge, fourth edition 2005",
                       "The standard account of the hillfort peoples of Britain before Rome.", "Yr hanes safonol am bobloedd y bryngaerau ym Mhrydain cyn Rhufain."),
                      (B, "Simon James", "The Atlantic Celts: Ancient People or Modern Invention?", "British Museum Press, 1999",
                       "The Britons as the ancient writers knew them.", "Y Brythoniaid fel yr adwaenai’r hen awduron hwy."),
                      museum, coflein, R.CADW),
     "era-medieval": L(R.BRUT_Y_TYWYSOGYON, R.GERALD, R.PRYCE_ACTS, R.LITTERE, R.R_R_DAVIES_AGE, R.TURVEY, R.JBS, R.YLF.LORD_RHYS, R.YLF.LLYWELYN_GREAT),
     "era-glyndwr": L(R.REVOLT, R.YLF.GLYNDWR_PRINCE, R.ADAM_USK, R.R_R_DAVIES_AGE, R.BOWEN,
                      (B, "A. D. Carr", "Owen of Wales: The End of the House of Gwynedd", "University of Wales Press, 1991",
                       "The life of Owain Lawgoch, the last heir of the princes.", "Bywyd Owain Lawgoch, etifedd olaf y tywysogion."),
                      (B, "Ralph A. Griffiths", "Conquerors and Conquered in Medieval Wales", "Alan Sutton, 1994",
                       "Wales between the conquest of 1282 and the coming of the Tudors.", "Cymru rhwng concwest 1282 a dyfodiad y Tuduriaid."),
                      (W, "Swansea University", "Dafydd ap Gwilym", "dafyddapgwilym.net",
                       "Every poem of Dafydd ap Gwilym, in Welsh with English translations.", "Holl gerddi Dafydd ap Gwilym, yn Gymraeg gyda chyfieithiadau Saesneg.", "https://dafyddapgwilym.net/"),
                      R.GLANMOR),
     "era-revival": L((P, "Griffith Jones", "Welch Piety", "London, yearly from 1737",
                       "Griffith Jones’s own yearly reports on the circulating schools.", "Adroddiadau blynyddol Griffith Jones ei hun ar yr ysgolion cylchynol."),
                      R.GHJ_FOUND,
                      (B, "Prys Morgan", "The Eighteenth Century Renaissance", "Christopher Davies, 1981",
                       "How the Welsh of the 1700s rediscovered their history, poetry and music.", "Sut yr ailddarganfu Cymry’r 1700au eu hanes, eu barddoniaeth a’u cerddoriaeth."),
                      (B, "Derec Llwyd Morgan", "The Great Awakening in Wales", "Epworth Press, 1988",
                       "The Methodist revival of Harris, Rowland and Pantycelyn.", "Diwygiad Methodistaidd Harris, Rowland a Phantycelyn."),
                      (B, "Geraint H. Jenkins (ed.)", "A Rattleskull Genius: The Many Faces of Iolo Morganwg", "University of Wales Press, 2005",
                       "Iolo Morganwg, poet, scholar and founder of the Gorsedd, seen from every side.", "Iolo Morganwg, bardd, ysgolhaig a sylfaenydd yr Orsedd, o bob ochr."),
                      R.DWB),
    }
