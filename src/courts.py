"""The courts of Wales in 3D: walk through the courts of the kings and princes, one page each (court-<id>.html).

Asked for by Ifan, 14 November 2026: "Can we add more 3D courts such as Sycharth", and "research how it and the
other courts would have looked". Llys Rhosyr (src/llys.py, llys-rhosyr.html) was the first; these follow it.

HOW A COURT IS MADE
  - The words: one entry in COURTS below: its stops (English and Welsh), the sources each stop rests on, a note on
    what is known and what is imagined, and the page's title and description. The stops are printed on the page as
    ordinary text too, for readers without 3D and for search engines.
  - The 3D: tools/court-<id>.src.js builds the scene (land, buildings, where you stand at each stop) on the shared
    court engine, bundled into src/static/court-<id>.js (see SKILLS.md, "More courts in 3D").
  - The sources: CITES below, keyed "ct-...". A [[cite:key]] marker after a sentence becomes a § chip on the page
    (src/cites.py). The 3D panel shows the same sources by name under each stop.

RULES (EDITORIAL.md): proud and true. Say what the dig found, what the poet says, and what we have imagined, and keep
those apart. Kings are kings; Owain Glyndŵr is Prince of Wales.
"""
import json
import re

g = {}

_MARK = re.compile(r"\[\[cite:[a-z0-9,\- ]+\]\]")


def _plain(s):
    return _MARK.sub("", s)


# ---------- the sources ----------
CITES = {
    "ct-coflein-sycharth": dict(
        short=("Coflein", "Coflein"), t="Sycharth Castle (NPRN 306999)",
        by=("Royal Commission on the Ancient and Historical Monuments of Wales, Coflein", "Comisiwn Brenhinol Henebion Cymru, Coflein"),
        note=("The national record of the site: a ditched motte about 50 m across and 10.6 m high with a summit 26 m across, a crescent-shaped bailey 64 m by 32 m on the south-west, "
              "two timber-framed buildings found on the motte top in 1962–63, and the mill, fishponds, warren and deer park of the poem.",
              "Cofnod cenedlaethol y safle: tomen â ffos o’i chwmpas, tua 50 m ar draws a 10.6 m o uchder, â chopa 26 m ar draws, beili ar ffurf cilgant 64 m wrth 32 m i’r de-orllewin, "
              "dau adeilad ffrâm bren a ganfuwyd ar ben y domen yn 1962–63, a melin, pysgodlynnoedd, cwningar a pharc ceirw’r gerdd."),
        url="https://coflein.gov.uk/en/site/306999", url_cy="https://coflein.gov.uk/cy/safle/306999"),
    "ct-hague-1966": dict(
        short=("Hague and Warhurst, 1966", "Hague a Warhurst, 1966"), t="Excavations at Sycharth Castle, Denbighshire, 1962–63",
        by=("D. B. Hague and C. Warhurst, Archaeologia Cambrensis 115 (1966), pp. 108–127", "D. B. Hague a C. Warhurst, Archaeologia Cambrensis 115 (1966), tt. 108–127"),
        note=("The excavation report: the remains of two timber buildings on the motte top, burnt oak from the fire of 1403, and blue roofing slates.",
              "Adroddiad y cloddio: olion dau adeilad pren ar ben y domen, derw wedi’i losgi yn nhân 1403, a llechi to gleision."),
        url=None, lang="en"),
    "ct-williams-pba": dict(
        short=("Proceedings of the British Academy", "Proceedings of the British Academy"),
        t="More than ‘skimble-skamble stuff’: the medieval Welsh poetry associated with Owain Glyndŵr",
        by=("Gruffydd Aled Williams, Proceedings of the British Academy 181 (2012), pp. 1–33", "Gruffydd Aled Williams, Proceedings of the British Academy 181 (2012), tt. 1–33"),
        note=("Reads Iolo Goch’s poem on Sycharth line by line beside the archaeology: the moat, the bridge, the gate for a hundred loads, the timber “couples”, the tiled roof that was most likely slate, the chimney, "
              "the glass windows, the cloister of Westminster and the bell tower of St Patrick’s, and “the fairest timber court” in the kingdom.",
              "Darllen cerdd Iolo Goch i Sycharth fesul llinell ochr yn ochr â’r archaeoleg: y ffos, y bont, y porth i gant o lwythi, y “cyplau” pren, y to teils a oedd yn fwyaf tebyg yn llechi, y simnai, "
              "y ffenestri gwydr, clostr Westminster a chlochdy Padrig, a “thecaf llys bren” y deyrnas."),
        url="https://www.thebritishacademy.ac.uk/documents/2088/pba181p001.pdf", lang="en"),
    "ct-williams-bar": dict(
        short=("British Academy Review, 2011", "British Academy Review, 2011"), t="The Welsh poetry associated with Owain Glyndŵr (the Sir John Rhŷs Memorial Lecture, 2010)",
        by=("Gruffydd Aled Williams, British Academy Review 17 (March 2011), pp. 18–22", "Gruffydd Aled Williams, British Academy Review 17 (Mawrth 2011), tt. 18–22"),
        note=("The house on the motte had a “likely H-shaped plan, consisting of a central hall with flanking wings”; the digging of the 1960s suggests that Iolo’s tiles were in fact slates.",
              "Roedd gan y tŷ ar y domen “gynllun siâp H tebygol”, neuadd ganol ag adain bob ochr; mae cloddio’r 1960au yn awgrymu mai llechi oedd teils Iolo mewn gwirionedd."),
        url="https://www.thebritishacademy.ac.uk/documents/778/BAR17-08-Williams.pdf", lang="en"),
    "ct-iolo-sycharth": dict(
        short=("Iolo Goch, c. 1390", "Iolo Goch, tua 1390"), t="Llys Owain Glyndŵr yn Sycharth",
        by=("Iolo Goch, edited by Dafydd Johnston in Gwaith Iolo Goch (University of Wales Press, 1988), poem X, and with a translation in Iolo Goch: Poems (Gomer, 1993)",
            "Iolo Goch, golygwyd gan Dafydd Johnston yn Gwaith Iolo Goch (Gwasg Prifysgol Cymru, 1988), cerdd X, a chyda chyfieithiad yn Iolo Goch: Poems (Gomer, 1993)"),
        note=("The poem itself, sung at Sycharth before the rising: the moat, the bridge and the gate, the court on the green hill, the lofts, the chimney and the glass, the church-like hall, "
              "the orchard, vineyard, mill, dovecot, fishpond, warren and deer park, Margaret and the children, and a house where no lock was needed.",
              "Y gerdd ei hun, a ganwyd yn Sycharth cyn y gwrthryfel: y ffos, y bont a’r porth, y llys ar y bryn gwyrdd, y llofftydd, y simnai a’r gwydr, y neuadd fel eglwys, "
              "y berllan, y winllan, y felin, y colomendy, y pysgodlyn, y gwningar a’r parc ceirw, Marged a’r plant, a thŷ lle nad oedd angen clo."),
        url="https://en.wikipedia.org/wiki/Owain_Glynd%C5%B5r%27s_Court", lang="en"),
    "ct-hague-drawing": dict(
        short=("RCAHMW drawing", "Llun CBHC"), t="Reconstruction of Sycharth Castle, Llansilin",
        by=("Douglas Hague, ink drawing, Royal Commission on the Ancient and Historical Monuments of Wales (People’s Collection Wales)", "Douglas Hague, llun inc, Comisiwn Brenhinol Henebion Cymru (Casgliad y Werin Cymru)"),
        note=("The excavator’s own picture of how Sycharth may have looked, drawn after the dig.",
              "Llun y cloddiwr ei hun o sut olwg a allai fod ar Sycharth, a dynnwyd wedi’r cloddio."),
        url="https://www.peoplescollection.wales/items/27855", lang="en"),
    "ct-museum-timber": dict(
        short=("Amgueddfa Cymru, 2017", "Amgueddfa Cymru, 2017"), t="Owain Glyndŵr and a timber from Sycharth",
        by=("Dafydd Wiliam, Principal Curator of Historic Buildings, Amgueddfa Cymru – Museum Wales, 15 September 2017", "Dafydd Wiliam, Prif Guradur Adeiladau Hanesyddol, Amgueddfa Cymru, 15 Medi 2017"),
        note=("A great oak beam, with a mortice cut in it, was found when the moat was drained in the 1890s. The museum holds part of it; it may be from the bridge over the moat.",
              "Cafwyd trawst derw mawr, â mortais wedi’i dorri ynddo, pan sychwyd y ffos yn yr 1890au. Mae rhan ohono gan yr amgueddfa; gall ddod o’r bont dros y ffos."),
        url="https://museum.wales/blog/1842/Owain-Glyndr-and-a-timber-from-Sycharth/", lang="en"),
    "ct-gatehouse-sycharth": dict(
        short=("Gatehouse", "Gatehouse"), t="Sycharth Castle, Llansilin",
        by=("The Gatehouse record of castles in Wales, drawing on the Cadw scheduling report and the Clwyd-Powys Archaeological Trust record",
            "Cofnod Gatehouse o gestyll Cymru, yn seiliedig ar adroddiad rhestru Cadw a chofnod Ymddiriedolaeth Archaeolegol Clwyd-Powys"),
        note=("The house in the poem was framed with posts and trusses, with upper rooms, a tiled roof and a chimney; a geophysical survey in 2009 found a second enclosure to the north.",
              "Roedd y tŷ yn y gerdd wedi’i fframio â physt a thrawstiau, ag ystafelloedd uchaf, to teils a simnai; canfu arolwg geoffisegol yn 2009 ail glostir i’r gogledd."),
        url="https://gatehouse-gazetteer.info/Welshsites/292.html", lang="en"),
    "ct-coflein-aber-llys": dict(
        short=("Coflein", "Coflein"), t="Llys at Aber, Abergwyngregyn (NPRN 309171)",
        by=("Royal Commission on the Ancient and Historical Monuments of Wales, Coflein", "Comisiwn Brenhinol Henebion Cymru, Coflein"),
        note=("One of the main residences of the princes of Gwynedd in the 13th century: a hall with a cross-wing at either end, 11.2 m by 8.0 m inside, found by excavation in 1993 at the foot of the castle mound, with 13th- and 14th-century material; "
              "repairs recorded in 1289 and 1303; remains still visible in the early 16th century; parchmarks photographed from the air in July 2006.",
              "Un o brif gartrefi tywysogion Gwynedd yn y drydedd ganrif ar ddeg: neuadd ag adain groes ym mhob pen, 11.2 m wrth 8.0 m y tu mewn, a ganfuwyd wrth gloddio yn 1993 wrth droed y domen, gyda deunydd o’r drydedd a’r bedwaredd ganrif ar ddeg; "
              "atgyweiriadau yn 1289 a 1303; olion i’w gweld o hyd ar ddechrau’r unfed ganrif ar bymtheg; ôl sychder a dynnwyd o’r awyr ym mis Gorffennaf 2006."),
        url="https://coflein.gov.uk/en/site/309171", url_cy="https://coflein.gov.uk/cy/safle/309171"),
    "ct-coflein-aber-mound": dict(
        short=("Coflein", "Coflein"), t="Aber Castle Mound, Pen y Mwd (NPRN 95692)",
        by=("Royal Commission on the Ancient and Historical Monuments of Wales, Coflein", "Comisiwn Brenhinol Henebion Cymru, Coflein"),
        note=("A steep-sided mound about 36 m across and 6.6 m high, with a level summit about 17 m by 14 m and traces of a ditch on the south side; the excavated hall lies at its foot to the south-east.",
              "Tomen serth tua 36 m ar draws a 6.6 m o uchder, â chopa gwastad tua 17 m wrth 14 m ac olion ffos ar yr ochr ddeheuol; mae’r neuadd a gloddiwyd wrth ei throed i’r de-ddwyrain."),
        url="https://coflein.gov.uk/en/site/95692", url_cy="https://coflein.gov.uk/cy/safle/95692"),
    "ct-coflein-aber": dict(
        short=("Coflein", "Coflein"), t="Aber, Abergwyngregyn (NPRN 33000)",
        by=("Royal Commission on the Ancient and Historical Monuments of Wales, Coflein", "Comisiwn Brenhinol Henebion Cymru, Coflein"),
        note=("A settlement of importance before the conquest, guarding the crossing to Anglesey over the Lafan Sands, where the Roman road from Chester crossed the river; the seat of Llywelyn ap Gruffudd, where Gwenllian was born and Eleanor died in 1282; Dafydd ap Gruffudd was captured on the nearby Bera mountain in 1283.",
              "Anheddiad o bwys cyn y goresgyniad, yn gwarchod y groesfan i Fôn dros Draeth Lafan, lle croesai’r ffordd Rufeinig o Gaer yr afon; cartref Llywelyn ap Gruffudd, lle ganed Gwenllian a lle bu farw Elinor yn 1282; daliwyd Dafydd ap Gruffudd ar fynydd y Bera gerllaw yn 1283."),
        url="https://coflein.gov.uk/en/site/33000", url_cy="https://coflein.gov.uk/cy/safle/33000"),
    "ct-johnstone-aber": dict(
        short=("Johnstone, 1993 and 1997", "Johnstone, 1993 a 1997"), t="The royal courts of thirteenth-century Gwynedd",
        by=("Neil Johnstone, Archaeology in Wales 33 (1993), pp. 68–69, and ‘An investigation into the location of the royal courts of thirteenth-century Gwynedd’, in N. Edwards (ed.), Landscape and Settlement in Medieval Wales (Oxbow, 1997)",
            "Neil Johnstone, Archaeology in Wales 33 (1993), tt. 68–69, ac ‘An investigation into the location of the royal courts of thirteenth-century Gwynedd’, yn N. Edwards (gol.), Landscape and Settlement in Medieval Wales (Oxbow, 1997)"),
        note=("The report of the 1993 dig at Aber, which found the hall with its cross-wings, and the search for the courts of the princes across Gwynedd.",
              "Adroddiad cloddio 1993 yn Aber, a ganfu’r neuadd a’i hadenydd croes, a’r chwilio am lysoedd y tywysogion ar draws Gwynedd."),
        url=None, lang="en"),
    "ct-aber-2010": dict(
        short=("Medievalists.net, 2010", "Medievalists.net, 2010"), t="Finding traces of the Princes of Gwynedd",
        by=("Medievalists.net, October 2010, on the excavation led by John G. Roberts of the Snowdonia National Park with Gwynedd Archaeological Trust and the Aber heritage partnership, supported by Cadw",
            "Medievalists.net, Hydref 2010, am y cloddio dan arweiniad John G. Roberts o Barc Cenedlaethol Eryri gydag Ymddiriedolaeth Archaeolegol Gwynedd a phartneriaeth dreftadaeth Aber, gyda chefnogaeth Cadw"),
        note=("“We have opened a large portion of field near the motte and the foundations of a medieval hall”: pottery and a brooch date it to the 13th and 14th centuries, and the site proved more complex and extensive than first thought.",
              "Agorwyd rhan fawr o’r cae ger y domen a sylfeini neuadd ganoloesol: mae crochenwaith a thlws yn ei dyddio i’r drydedd a’r bedwaredd ganrif ar ddeg, a phrofodd y safle’n fwy cymhleth ac eang na’r disgwyl."),
        url="https://www.medievalists.net/2010/10/finding-traces-of-the-princes-of-gwynedd/", lang="en"),
    "ct-gatehouse-aber": dict(
        short=("Gatehouse", "Gatehouse"), t="Aber Castle, Pen-y-Mwd, and Ty’n-y-Mwd llys",
        by=("The Gatehouse record of castles in Wales", "Cofnod Gatehouse o gestyll Cymru"),
        note=("Brings together the records of the mound and the court: the mound never excavated, attributed by some to Hugh of Avranches and Robert of Rhuddlan in the late 11th century and by others to the princes; Leland in the 16th century saw part of the building still standing; the debate over Pen y Bryn.",
              "Yn dwyn ynghyd gofnodion y domen a’r llys: ni chloddiwyd y domen erioed, ac fe’i priodolir gan rai i Hugh o Avranches a Robert o Ruddlan ddiwedd yr unfed ganrif ar ddeg a chan eraill i’r tywysogion; gwelodd Leland yn yr unfed ganrif ar bymtheg ran o’r adeilad yn sefyll o hyd; y ddadl am Ben y Bryn."),
        url="https://gatehouse-gazetteer.info/Welshsites/86.html", lang="en"),
    "ct-gatehouse-penybryn": dict(
        short=("Gatehouse", "Gatehouse"), t="Pen-y-bryn, Aber (Twr Llewelyn, Garth Celyn)",
        by=("The Gatehouse record of castles in Wales, with the Cadw scheduling and listing records", "Cofnod Gatehouse o gestyll Cymru, gyda chofnodion rhestru Cadw"),
        note=("A scheduled monument and a listed building on the rising ground east of the Afon Aber: a house with a round tower of four storeys at its west end, its main range tree-ring dated to 1619–24; some sources hold the tower to be mostly medieval, and Paul Remfry proposes an early llys here.",
              "Heneb gofrestredig ac adeilad rhestredig ar y tir sy’n codi i’r dwyrain o afon Aber: tŷ â thŵr crwn pedwar llawr yn ei ben gorllewinol, a’i brif ran wedi’i dyddio drwy gylchoedd coed i 1619–24; mae rhai ffynonellau’n credu bod y tŵr yn ganoloesol gan mwyaf, ac mae Paul Remfry yn cynnig llys cynnar yma."),
        url="https://www.gatehouse-gazetteer.info/Welshsites/1148.html", lang="en"),
    "ct-wiki-garthcelyn": dict(
        short=("Wikipedia", "Wikipedia"), t="Garth Celyn",
        by=("Wikipedia", "Wikipedia"),
        note=("Pen y Bryn within the double bank and ditch of Garth Celyn, an enclosure 90–100 m across; the Garth Celyn Trust’s view that the royal court stood here; Llywelyn ap Gruffudd’s letters of November 1282 to the Archbishop of Canterbury, dated at “Garth Kelyn”; Leland’s palace by “the Moode”.",
              "Pen y Bryn o fewn clawdd dwbl a ffos Garth Celyn, lloc 90–100 m ar draws; barn Ymddiriedolaeth Garth Celyn mai yma y safai’r llys brenhinol; llythyrau Llywelyn ap Gruffudd at Archesgob Caergaint ym mis Tachwedd 1282, wedi’u dyddio yn “Garth Kelyn”; plas Leland ger “the Moode”."),
        url="https://en.wikipedia.org/wiki/Garth_Celyn", lang="en"),
    "ct-hurlock": dict(
        short=("Hurlock, 2011", "Hurlock, 2011"), t="Wales and the Crusades, c. 1095–1291",
        by=("Kathryn Hurlock, University of Wales Press, 2011, pp. 111–112 and 193–199", "Kathryn Hurlock, Gwasg Prifysgol Cymru, 2011, tt. 111–112 a 193–199"),
        note=("Archbishop Peckham’s terms of November 1282: an estate in England for Llywelyn if he gave up Wales, and the crusade for Dafydd; Llywelyn’s refusal to abandon the people his forefathers had protected since “the days of Kamber son of Brutus”.",
              "Telerau’r Archesgob Peckham ym mis Tachwedd 1282: ystad yn Lloegr i Lywelyn pe rhoddai Gymru i fyny, a’r groesgad i Ddafydd; gwrthodiad Llywelyn i gefnu ar y bobl a amddiffynnodd ei gyndadau ers “dyddiau Camber fab Brutus”."),
        url=None, lang="en"),
    "ct-peckham": dict(
        short=("Registrum Peckham", "Registrum Peckham"), t="Registrum Epistolarum Fratris Johannis Peckham, Archiepiscopi Cantuariensis",
        by=("edited by C. Trice Martin, volume 2 (Rolls Series, 1884)", "golygwyd gan C. Trice Martin, cyfrol 2 (Rolls Series, 1884)"),
        note=("The archbishop’s own letter book, which keeps the answers of Llywelyn, his council and the men of Snowdon in November 1282.",
              "Llyfr llythyrau’r archesgob ei hun, sy’n cadw atebion Llywelyn, ei gyngor a gwŷr Eryri ym mis Tachwedd 1282."),
        url=None, lang="la"),
    "ct-laws": dict(
        short=("The Law of Hywel Dda", "Cyfraith Hywel Dda"), t="The Law of Hywel Dda: Law Texts from Mediaeval Wales",
        by=("Dafydd Jenkins (translator and editor), Gomer, 1986: the Laws of the Court", "Dafydd Jenkins (cyfieithydd a golygydd), Gomer, 1986: Cyfraith y Llys"),
        note=("The twenty-four officers of the court and their places in the hall: the edling facing the king across the fire, the judge of the court by the pillar, the priest of the household and the pencerdd beside them, the penteulu and the household troop at the far end.",
              "Pedwar swyddog ar hugain y llys a’u lleoedd yn y neuadd: yr edling gyferbyn â’r brenin ar draws y tân, ynad llys wrth y golofn, offeiriad teulu a’r pencerdd yn eu hymyl, y penteulu a’r osgordd yn y pen draw."),
        url=None, lang="en"),
    "ct-wiki-dafydd": dict(
        short=("Wikipedia", "Wikipedia"), t="Dafydd ap Llywelyn",
        by=("Wikipedia", "Wikipedia"),
        note=("Son of Llywelyn the Great and Siwan; ruler of Gwynedd from 1240; styled himself Prince of Wales from 1244; died at Abergwyngregyn in February 1246 and was buried at Aberconwy.",
              "Mab Llywelyn Fawr a Siwan; rheolwr Gwynedd o 1240; galwai ei hun yn Dywysog Cymru o 1244; bu farw yn Abergwyngregyn ym mis Chwefror 1246 a’i gladdu yn Aberconwy."),
        url="https://en.wikipedia.org/wiki/Dafydd_ap_Llywelyn", url_cy="https://cy.wikipedia.org/wiki/Dafydd_ap_Llywelyn", lang="en"),
    "ct-wiki-dafyddg": dict(
        short=("Wikipedia", "Wikipedia"), t="Dafydd ap Gruffydd",
        by=("Wikipedia", "Wikipedia"),
        note=("Brother of Llywelyn ap Gruffudd; Prince of Wales after Llywelyn’s death in December 1282; captured in the mountains of Snowdonia in June 1283 and put to death at Shrewsbury that October.",
              "Brawd Llywelyn ap Gruffudd; Tywysog Cymru wedi marw Llywelyn ym mis Rhagfyr 1282; daliwyd ym mynyddoedd Eryri ym mis Mehefin 1283 a’i ladd yn Amwythig y mis Hydref hwnnw."),
        url="https://en.wikipedia.org/wiki/Dafydd_ap_Gruffydd", url_cy="https://cy.wikipedia.org/wiki/Dafydd_ap_Gruffudd", lang="en"),
}

# ---------- the courts ----------
COURTS = [
    dict(
        id="sycharth", era="medieval", lat=52.8245, lon=-3.1808, year="c. 1390",
        name=("Sycharth", "Sycharth"),
        title=("Sycharth: the court of Owain Glyndŵr", "Sycharth: llys Owain Glyndŵr"),
        eyebrow=("Walk through it in 3D", "Cerddwch drwyddo mewn 3D"),
        sub=("Cross the moat, climb the green hill and step inside the timber court that Iolo Goch sang about, as it stood around 1390, before the rising.",
             "Croeswch y ffos, dringwch y bryn gwyrdd a chamwch i mewn i’r llys pren y canodd Iolo Goch iddo, fel y safai tua 1390, cyn y gwrthryfel."),
        crumbs=("era-medieval.html", "The age of the princes", "Oes y tywysogion"),
        seo=("Sycharth in 3D: walk through Owain Glyndŵr’s court · History of Wales",
             "Walk through Sycharth, the moated timber court of Owain Glyndŵr, Prince of Wales, in 3D: the bridge, the bailey, the house on the motte, the fishpond and the deer park, with Iolo Goch’s poem and what the excavators found."),
        card=("Sycharth in 3D", "Sycharth mewn 3D",
              "Cross the moat into Owain Glyndŵr’s timber court on its green hill, as Iolo Goch sang it.",
              "Croeswch y ffos i lys pren Owain Glyndŵr ar ei fryn gwyrdd, fel y canodd Iolo Goch iddo."),
        more=[("person-owain-glyndwr.html", "Owain Glyndŵr", "Owain Glyndŵr"), ("person-iolo-goch.html", "Iolo Goch", "Iolo Goch"),
              ("place-sycharth.html", "Visit Sycharth", "Ymweld â Sycharth"), ("ride-glyndwr.html", "Ride with Glyndŵr, 1400", "Marchogaeth gyda Glyndŵr, 1400")],
        stops=[
            dict(id="bridge", t=("The bridge over the moat", "Y bont dros y ffos"), src=["ct-iolo-sycharth", "ct-williams-pba", "ct-museum-timber"],
                 p=(["You are in the valley of the Cynllaith, in the lordship of Cynllaith in Powys, around 1390. Ahead is Sycharth, the chief house of Owain Glyndŵr, lord of Glyndyfrdwy and Cynllaith, heir of the princes of Powys.",
                     "The poet Iolo Goch came here as a guest and made a poem of what he saw. It begins with the water. A moat rings the court like a golden ring, a bridge crosses it, and the gate is wide enough, he says, for a hundred loads to pass.[[cite:ct-williams-pba,ct-iolo-sycharth]]",
                     "When the moat was drained in the 1890s a great oak beam was found in it, with a mortice cut for a joint. It may be from this bridge.[[cite:ct-museum-timber]]"],
                    ["Rydych yn nyffryn Cynllaith, yn arglwyddiaeth Cynllaith ym Mhowys, tua 1390. O’ch blaen mae Sycharth, prif dŷ Owain Glyndŵr, arglwydd Glyndyfrdwy a Chynllaith, etifedd tywysogion Powys.",
                     "Daeth y bardd Iolo Goch yma’n westai a chanu cerdd i’r hyn a welodd. Mae’n dechrau â’r dŵr. Mae ffos o amgylch y llys fel modrwy aur, mae pont drosti, ac mae’r porth yn ddigon llydan, meddai, i gant o lwythi fynd drwyddo.[[cite:ct-williams-pba,ct-iolo-sycharth]]",
                     "Pan sychwyd y ffos yn yr 1890au cafwyd ynddi drawst derw mawr, â mortais wedi’i thorri ar gyfer uniad. Efallai ei fod o’r bont hon.[[cite:ct-museum-timber]]"])),
            dict(id="bailey", t=("The bailey", "Y beili"), src=["ct-coflein-sycharth", "ct-iolo-sycharth", "ct-williams-pba"],
                 p=(["Inside the gate is the bailey, a crescent of level ground 64 metres across, wrapped around the foot of the mound.[[cite:ct-coflein-sycharth]] Here stood the kitchen and bakehouse, the stables, and lodgings for the household and guests.",
                     "Iolo reached for the finest buildings he knew to praise them: the bell tower of St Patrick’s in Dublin, “fruit of French workmanship”, and the cloister of Westminster, “a gentle enclosure”. "
                     "He sings of nine halls alike, and a wardrobe by each one: nine was the poets’ number for plenty.[[cite:ct-williams-pba]]"],
                    ["Y tu mewn i’r porth mae’r beili, cilgant o dir gwastad 64 metr ar draws, wedi’i lapio am droed y domen.[[cite:ct-coflein-sycharth]] Yma safai’r gegin a’r popty, y stablau, a llety i’r teulu a’r gwesteion.",
                     "Estynnodd Iolo am yr adeiladau gorau a wyddai i’w canmol: clochdy Padrig yn Nulyn, “Ffrengig ffrwyth”, a chlostr Westminster, “clostir esmwyth”. "
                     "Mae’n canu am naw neuadd gyfartal, a chwpwrdd dillad wrth bob un: naw oedd rhif y beirdd am ddigonedd.[[cite:ct-williams-pba]]"])),
            dict(id="motte", t=("The court on the green hill", "Y llys ar y bryn gwyrdd"), src=["ct-coflein-sycharth", "ct-hague-1966", "ct-williams-pba"],
                 p=(["Above the bailey rises the motte, an earthen mound about 50 metres across and more than 10 metres high, with its own ditch. On its flat top, 26 metres across, stands Owain’s house.[[cite:ct-coflein-sycharth]]",
                     "The excavators found the remains of two timber buildings up here, one about 13 metres (43 feet) long.[[cite:ct-coflein-sycharth,ct-hague-1966]] "
                     "Iolo called it “tecaf llys bren o’r deyrnas”, the fairest timber court in the kingdom.[[cite:ct-williams-pba]]"],
                    ["Uwchben y beili mae’r domen, twmpath pridd tua 50 metr ar draws a mwy na 10 metr o uchder, â’i ffos ei hun. Ar ei phen gwastad, 26 metr ar draws, saif tŷ Owain.[[cite:ct-coflein-sycharth]]",
                     "Canfu’r cloddwyr olion dau adeilad pren yma, un tua 13 metr (43 troedfedd) o hyd.[[cite:ct-coflein-sycharth,ct-hague-1966]] "
                     "Galwodd Iolo ef yn “decaf llys bren o’r deyrnas”.[[cite:ct-williams-pba]]"])),
            dict(id="frame", t=("Coupled work", "Gwaith cwplws"), src=["ct-williams-pba", "ct-williams-bar", "ct-gatehouse-sycharth"],
                 p=(["Look at the timber. Iolo did: “Cyplau sydd, gwaith cwplws ŷnt, / Cwpledig pob cwpl ydynt”, there are couples, they are coupled work, each couple joined to the next.[[cite:ct-williams-pba]] "
                     "The frame is of posts and trusses, every joint pegged: the carpenter’s masterpiece, and Owain’s pride.[[cite:ct-gatehouse-sycharth]]",
                     "The house most likely had an H-shaped plan: a hall in the middle with a wing at each end.[[cite:ct-williams-bar]] To Iolo it was shaped like a church, “croes eglwys”, with its arms.[[cite:ct-williams-pba]]"],
                    ["Edrychwch ar y pren. Dyna a wnaeth Iolo: “Cyplau sydd, gwaith cwplws ŷnt, / Cwpledig pob cwpl ydynt”.[[cite:ct-williams-pba]] "
                     "Mae’r ffrâm o byst a thrawstiau, a phob uniad wedi’i begio: campwaith y saer, a balchder Owain.[[cite:ct-gatehouse-sycharth]]",
                     "Mae’n fwyaf tebyg fod gan y tŷ gynllun siâp H: neuadd yn y canol ag adain ym mhob pen.[[cite:ct-williams-bar]] I Iolo roedd ar ffurf eglwys, “croes eglwys”, â’i breichiau.[[cite:ct-williams-pba]]"])),
            dict(id="hall", t=("The hall, the chimney and the glass", "Y neuadd, y simnai a’r gwydr"), src=["ct-williams-pba", "ct-williams-bar", "ct-hague-1966"],
                 p=(["Step inside. Most halls of the time had a fire in the middle of the floor, with the smoke left to find its own way out. Owain’s house has a chimney, a mark of a great house.[[cite:ct-williams-pba]]",
                     "The windows are glazed, “capelau â gwydrau gwiw”, chapels with fine glass, Iolo says: glass was common in churches but a rare luxury in a home.[[cite:ct-williams-pba]] "
                     "Every roof, he says, was tiled. The diggers found blue roofing slates, and Iolo’s “tiles” were most likely slate.[[cite:ct-williams-bar,ct-hague-1966]]"],
                    ["Camwch i mewn. Roedd tân yng nghanol y llawr yn y rhan fwyaf o neuaddau’r cyfnod, a’r mwg yn cael canfod ei ffordd ei hun allan. Mae simnai yn nhŷ Owain, arwydd o dŷ mawr.[[cite:ct-williams-pba]]",
                     "Mae gwydr yn y ffenestri, “capelau â gwydrau gwiw”, medd Iolo: roedd gwydr yn gyffredin mewn eglwysi ond yn foethusrwydd prin mewn cartref.[[cite:ct-williams-pba]] "
                     "Roedd teils ar bob to, meddai. Canfu’r cloddwyr lechi to gleision, ac mae’n fwyaf tebyg mai llechi oedd “teils” Iolo.[[cite:ct-williams-bar,ct-hague-1966]]"])),
            dict(id="lofts", t=("Lofts for the poets", "Llofftydd y beirdd"), src=["ct-williams-pba", "ct-iolo-sycharth"],
                 p=(["“Llys barwn, lle syberwyd, / Lle daw beirdd aml, lle da byd”: a lord’s court, a place of courtesy, where many poets come, a place of the good life.[[cite:ct-williams-pba]]",
                     "High on the timber pillars are lofts, where guests sleep. Iolo says there were four, and that they had become eight, so many poets came: there was a bed for every one.[[cite:ct-williams-pba]]"],
                    ["“Llys barwn, lle syberwyd, / Lle daw beirdd aml, lle da byd.”[[cite:ct-williams-pba]]",
                     "Yn uchel ar y pileri pren mae llofftydd, lle mae’r gwesteion yn cysgu. Mae Iolo’n dweud bod pedair, ac iddynt ddod yn wyth, cymaint o feirdd a ddeuai: roedd gwely i bob un.[[cite:ct-williams-pba]]"])),
            dict(id="table", t=("No hunger, no thirst", "Dim newyn, dim syched"), src=["ct-williams-pba", "ct-iolo-sycharth"],
                 p=(["At Owain’s table there is wine and mead, ale, white bread and meat, and a cook at work in the kitchen. Iolo says you would rarely see a latch or a lock at Sycharth, and no one there ever knew hunger or thirst.[[cite:ct-iolo-sycharth,ct-williams-pba]]",
                     "Here is Margaret, Owain’s wife, daughter of Sir David Hanmer: “A gwraig orau o’r gwragedd, / Gwyn fy myd o’i gwin a’i medd!”, the best of women, and blessed am I by her wine and mead. "
                     "Their children are “nythaid teg o benaethau”, a fair nest of lords.[[cite:ct-williams-pba]]"],
                    ["Wrth fwrdd Owain mae gwin a medd, cwrw, bara gwyn a chig, a chogydd wrth ei waith yn y gegin. Dywed Iolo mai anaml y gwelech glicied neu glo yn Sycharth, ac na wyddai neb yno erioed beth oedd newyn na syched.[[cite:ct-iolo-sycharth,ct-williams-pba]]",
                     "Dyma Farged, gwraig Owain, merch Syr Dafydd Hanmer: “A gwraig orau o’r gwragedd, / Gwyn fy myd o’i gwin a’i medd!” "
                     "Mae eu plant yn “nythaid teg o benaethau”.[[cite:ct-williams-pba]]"])),
            dict(id="estate", t=("Fishpond, mill and dovecot", "Pysgodlyn, melin a cholomendy"), src=["ct-coflein-sycharth", "ct-williams-pba", "ct-iolo-sycharth"],
                 p=(["From the top of the motte you see the whole estate, as Iolo walked it in his poem. Below is the fishpond, deep and full of fish; its banks can still be seen today.[[cite:ct-williams-pba]] "
                     "On the river is the mill, and there is a stone dovecot, an orchard and a vineyard, and peacocks in the yard.[[cite:ct-williams-pba,ct-iolo-sycharth]]",
                     "A woollen mill later stood by the Cynllaith just west of here, probably on the site of Sycharth’s own corn mill.[[cite:ct-coflein-sycharth]]"],
                    ["O ben y domen gwelwch yr ystad gyfan, fel y cerddodd Iolo hi yn ei gerdd. Islaw mae’r pysgodlyn, yn ddwfn ac yn llawn pysgod; gellir gweld ei gloddiau heddiw.[[cite:ct-williams-pba]] "
                     "Ar yr afon mae’r felin, ac mae colomendy carreg, perllan a gwinllan, a pheunod ar y buarth.[[cite:ct-williams-pba,ct-iolo-sycharth]]",
                     "Yn ddiweddarach safai melin wlân ar lan y Cynllaith ychydig i’r gorllewin, yn ôl pob tebyg ar safle melin ŷd Sycharth ei hun.[[cite:ct-coflein-sycharth]]"])),
            dict(id="park", t=("The deer park", "Y parc ceirw"), src=["ct-coflein-sycharth", "ct-iolo-sycharth"],
                 p=(["Look east, up the wooded hill. That is the deer park, with a lodge in it, and below it a rabbit warren.[[cite:ct-coflein-sycharth]] Down the valley are the hay meadows and the cornfields, the ploughs and the horses.[[cite:ct-iolo-sycharth]]",
                     "The woods on that hill are still called Parc Sycharth."],
                    ["Edrychwch tua’r dwyrain, i fyny’r bryn coediog. Dyna’r parc ceirw, â chaban hela ynddo, ac islaw iddo gwningar.[[cite:ct-coflein-sycharth]] I lawr y dyffryn mae’r dolydd gwair a’r caeau ŷd, yr erydr a’r meirch.[[cite:ct-iolo-sycharth]]",
                     "Parc Sycharth yw enw’r coed ar y bryn hwnnw o hyd."])),
            dict(id="prince", t=("Owain, Prince of Wales", "Owain, Tywysog Cymru"), src=["ct-williams-pba"],
                 p=(["Owain ap Gruffudd Fychan was descended from the princes of Powys through his father and from the line of the Lord Rhys of Deheubarth through his mother, Elen. Iolo calls him “gorau Cymro”, the best of Welshmen.[[cite:ct-williams-pba]]",
                     "On 16 September 1400 his followers proclaimed him Prince of Wales at Glyndyfrdwy, his other house, across the Berwyn. Within four years he held most of Wales, called a Senedd at Machynlleth and wrote to the King of France as an equal."],
                    ["Roedd Owain ap Gruffudd Fychan yn disgyn o dywysogion Powys drwy ei dad, ac o linach yr Arglwydd Rhys o Ddeheubarth drwy ei fam, Elen. Mae Iolo’n ei alw’n “orau Cymro”.[[cite:ct-williams-pba]]",
                     "Ar 16 Medi 1400 cyhoeddodd ei ddilynwyr ef yn Dywysog Cymru yng Nglyndyfrdwy, ei dŷ arall, dros y Berwyn. O fewn pedair blynedd daliai’r rhan fwyaf o Gymru, galwodd Senedd ym Machynlleth ac ysgrifennodd at Frenin Ffrainc fel cydradd."])),
            dict(id="fire", t=("May 1403", "Mai 1403"), src=["pl-wiki-sycharth", "ct-williams-pba"],
                 p=(["In May 1403 Henry, the English king’s eldest son, marched up the valley with an army to take Owain. He found Sycharth empty. He burned the whole place, and the houses of Owain’s tenants around it, and went on to burn Glyndyfrdwy too, as he wrote to his father.[[cite:pl-wiki-sycharth,ct-williams-pba]]",
                     "Owain was not there to be taken. He fought on for years, and was never captured and never betrayed. Sycharth was never rebuilt, but the court lives on in Iolo’s poem."],
                    ["Ym Mai 1403 gorymdeithiodd Harri, mab hynaf brenin Lloegr, i fyny’r dyffryn â byddin i ddal Owain. Cafodd Sycharth yn wag. Llosgodd y lle i gyd, a thai deiliaid Owain o’i amgylch, ac aeth ymlaen i losgi Glyndyfrdwy hefyd, fel yr ysgrifennodd at ei dad.[[cite:pl-wiki-sycharth,ct-williams-pba]]",
                     "Nid oedd Owain yno i’w ddal. Ymladdodd ymlaen am flynyddoedd, ac ni chafodd ei ddal na’i fradychu erioed. Ni chodwyd Sycharth eto, ond mae’r llys yn byw yng ngherdd Iolo."])),
            dict(id="spade", t=("What the spade found", "Yr hyn a ganfu’r rhaw"), src=["ct-hague-1966", "ct-coflein-sycharth", "ct-gatehouse-sycharth", "ct-hague-drawing"],
                 p=(["In 1962 and 1963 the archaeologists Douglas Hague and C. Warhurst dug part of the top of the motte. They found the remains of two timber buildings, burnt oak from the fire, and blue roofing slates.[[cite:ct-hague-1966,ct-williams-pba]] "
                     "Surveys with instruments since then have found traces of buildings in the bailey and a second enclosure to the north.[[cite:ct-gatehouse-sycharth]]",
                     "Cadw looks after the mound today. Stand on it and you are standing where Owain’s house stood, with the fishpond banks below and Parc Sycharth on the hill."],
                    ["Yn 1962 a 1963 cloddiodd yr archaeolegwyr Douglas Hague a C. Warhurst ran o ben y domen. Canfuwyd olion dau adeilad pren, derw wedi’i losgi yn y tân, a llechi to gleision.[[cite:ct-hague-1966,ct-williams-pba]] "
                     "Ers hynny mae arolygon ag offerynnau wedi canfod olion adeiladau yn y beili ac ail glostir i’r gogledd.[[cite:ct-gatehouse-sycharth]]",
                     "Cadw sy’n gofalu am y domen heddiw. Safwch arni ac rydych yn sefyll lle safai tŷ Owain, â chloddiau’r pysgodlyn islaw a Pharc Sycharth ar y bryn."])),
        ],
        known=(["Known from the ground: the motte, its ditch, the crescent bailey and the fishpond banks, measured by the Royal Commission and Cadw; two timber buildings on the motte top, burnt oak and roofing slates, found in 1962–63.",
                "Known from the poem: the moat and bridge, the gate, the timber frame with its lofts, the chimney, glass windows and tiled (slate) roofs, the H-shaped house, and the mill, dovecot, orchard, vineyard, fishpond, warren and deer park.",
                "Imagined: the exact size and height of each building, the layout of the bailey, and where the mill, dovecot and orchard stood. We have kept to the plan of a hall with a wing at each end, set on the motte top within the size the excavators found, and drawn the bailey buildings after other Welsh courts of the time."],
               ["Yn hysbys o’r tir: y domen, ei ffos, y beili cilgant a chloddiau’r pysgodlyn, wedi’u mesur gan y Comisiwn Brenhinol a Cadw; dau adeilad pren ar ben y domen, derw wedi’i losgi a llechi to, a ganfuwyd yn 1962–63.",
                "Yn hysbys o’r gerdd: y ffos a’r bont, y porth, y ffrâm bren a’i llofftydd, y simnai, y ffenestri gwydr a’r toeau teils (llechi), y tŷ siâp H, a’r felin, y colomendy, y berllan, y winllan, y pysgodlyn, y gwningar a’r parc ceirw.",
                "Wedi’i ddychmygu: union faint ac uchder pob adeilad, trefn y beili, a lle safai’r felin, y colomendy a’r berllan. Rydym wedi cadw at gynllun neuadd ag adain ym mhob pen, ar ben y domen o fewn y maint a ganfu’r cloddwyr, ac wedi tynnu adeiladau’r beili ar sail llysoedd Cymreig eraill y cyfnod."]),
        ld=dict(name="Sycharth", description="The moated court of Owain Glyndŵr, Prince of Wales, on a motte in the Cynllaith valley, praised by Iolo Goch about 1390 and burned in 1403."),
    ),
    dict(
        id="aber", era="medieval", lat=53.2337, lon=-4.0139, year="c. 1280",
        name=("Garth Celyn", "Garth Celyn"),
        title=("Garth Celyn: the princes’ court at Aber", "Garth Celyn: llys y tywysogion yn Aber"),
        eyebrow=("Walk through it in 3D", "Cerddwch drwyddo mewn 3D"),
        sub=("Walk into the hall at Abergwyngregyn, between the mountains and the sea, where Siwan died, Gwenllian was born and Llywelyn, Prince of Wales, gave his answer in 1282.",
             "Cerddwch i mewn i’r neuadd yn Abergwyngregyn, rhwng y mynyddoedd a’r môr, lle bu farw Siwan, lle ganed Gwenllian, ac o ble rhoddodd Llywelyn, Tywysog Cymru, ei ateb yn 1282."),
        crumbs=("era-medieval.html", "The age of the princes", "Oes y tywysogion"),
        seo=("Garth Celyn in 3D: the princes’ court at Aber · History of Wales",
             "Walk through the court of the princes of Gwynedd at Abergwyngregyn in 3D: the hall with its two wings found by excavation, the mound Pen y Mwd, Pen y Bryn on the hill, and the stories of Siwan, Eleanor, Gwenllian and Llywelyn’s answer of 1282."),
        card=("Garth Celyn in 3D", "Garth Celyn mewn 3D",
              "Walk into the princes’ hall at Aber, between the mountains and the sea, where Llywelyn gave his answer in 1282.",
              "Cerddwch i neuadd y tywysogion yn Aber, rhwng y mynyddoedd a’r môr, lle rhoddodd Llywelyn ei ateb yn 1282."),
        more=[("person-llywelyn-ap-gruffudd.html", "Llywelyn ap Gruffudd", "Llywelyn ap Gruffudd"), ("person-siwan.html", "Siwan", "Siwan"),
              ("person-eleanor-de-montfort.html", "Eleanor de Montfort", "Elinor de Montfort"), ("person-gwenllian-ferch-llywelyn.html", "Gwenllian", "Gwenllian"),
              ("place-garthcelyn.html", "Visit Aber", "Ymweld ag Aber")],
        stops=[
            dict(id="arrive", t=("Between the mountains and the sea", "Rhwng y mynyddoedd a’r môr"), src=["ct-coflein-aber", "ct-coflein-aber-llys"],
                 p=(["You are at Abergwyngregyn, Aber for short, on the north coast of Gwynedd, around 1280. Behind you rise the Carneddau. In front of you the land falls to the Menai and the Lafan Sands, and across the water lies Ynys Môn.[[cite:ct-coflein-aber]]",
                     "Roads meet here. The Roman road from Chester crossed the river at Aber, and at low tide travellers went out over the Lafan Sands to cross to Môn.[[cite:ct-coflein-aber]] "
                     "Here the princes of Gwynedd kept a court, a llys, which they called Garth Celyn.",
                     "The princes moved with their household from court to court through the year. In the 1200s Aber was one of their chief homes.[[cite:ct-coflein-aber-llys]]"],
                    ["Rydych yn Abergwyngregyn, neu Aber, ar arfordir gogledd Gwynedd, tua 1280. Y tu ôl i chi mae’r Carneddau. O’ch blaen mae’r tir yn disgyn at y Fenai a Thraeth Lafan, a dros y dŵr mae Ynys Môn.[[cite:ct-coflein-aber]]",
                     "Mae ffyrdd yn cyfarfod yma. Croesai’r ffordd Rufeinig o Gaer yr afon yn Aber, ac ar drai âi teithwyr allan dros Draeth Lafan i groesi i Fôn.[[cite:ct-coflein-aber]] "
                     "Yma cadwai tywysogion Gwynedd lys, a’i alw’n Garth Celyn.",
                     "Symudai’r tywysogion gyda’u llys o lys i lys drwy’r flwyddyn. Yn y drydedd ganrif ar ddeg roedd Aber yn un o’u prif gartrefi.[[cite:ct-coflein-aber-llys]]"])),
            dict(id="hall", t=("The hall and its two wings", "Y neuadd a’i dwy adain"), src=["ct-coflein-aber-llys", "ct-johnstone-aber", "ct-aber-2010"],
                 p=(["In 1993 archaeologists digging in the field at the foot of the mound found the stone footings of a hall with a cross-wing at each end. Inside, the hall measured 11.2 by 8 metres, and the pottery and a brooch found with it date it to the 1200s and 1300s.[[cite:ct-coflein-aber-llys,ct-johnstone-aber,ct-aber-2010]]",
                     "A hall in the middle and a wing at each end was the plan of a great house: the hall for the household, one wing for the prince’s own chamber, the other for the food and drink. This was a palace, not a castle: a place to live, to feast and to govern."],
                    ["Yn 1993 canfu archaeolegwyr a oedd yn cloddio yn y cae wrth droed y domen sylfeini carreg neuadd ag adain groes ym mhob pen. Y tu mewn roedd y neuadd yn 11.2 wrth 8 metr, ac mae’r crochenwaith a’r tlws a gafwyd gyda hi yn ei dyddio i’r 1200au a’r 1300au.[[cite:ct-coflein-aber-llys,ct-johnstone-aber,ct-aber-2010]]",
                     "Neuadd yn y canol ac adain ym mhob pen oedd cynllun tŷ mawr: y neuadd i’r teulu a’r osgordd, un adain i ystafell y tywysog ei hun, a’r llall i’r bwyd a’r ddiod. Plas oedd hwn, nid castell: lle i fyw, i wledda ac i lywodraethu."])),
            dict(id="mound", t=("Pen y Mwd", "Pen y Mwd"), src=["ct-coflein-aber-mound", "ct-gatehouse-aber", "ct-coflein-aber-llys"],
                 p=(["Beside the court rises the mound called Pen y Mwd, about 36 metres across and 6.6 metres high, with a level top about 17 by 14 metres. There are traces of a ditch on its south side.[[cite:ct-coflein-aber-mound]]",
                     "No one has ever dug into it, so no one knows who raised it. Some say the Normans threw it up in the 1090s, in the few years when they pushed into Gwynedd before the Welsh drove them out; others that the princes built it themselves.[[cite:ct-gatehouse-aber]] "
                     "Either way, the princes made it part of their court, as at Castell Prysor, Crogen and Rhug, where a house stood at the foot of a mound that gave it standing and a place of refuge.[[cite:ct-coflein-aber-llys]]",
                     "The look-out tower on its top is our own imagining."],
                    ["Wrth ymyl y llys cyfyd y domen a elwir Pen y Mwd, tua 36 metr ar draws a 6.6 metr o uchder, â phen gwastad tua 17 wrth 14 metr. Mae olion ffos ar ei hochr ddeheuol.[[cite:ct-coflein-aber-mound]]",
                     "Ni chloddiodd neb iddi erioed, felly ni ŵyr neb pwy a’i cododd. Dywed rhai i’r Normaniaid ei chodi yn y 1090au, yn yr ychydig flynyddoedd pan wthion nhw i Wynedd cyn i’r Cymry eu gyrru allan; eraill mai’r tywysogion eu hunain a’i cododd.[[cite:ct-gatehouse-aber]] "
                     "Y naill ffordd neu’r llall, gwnaeth y tywysogion hi’n rhan o’u llys, fel yng Nghastell Prysor, Crogen a’r Rhug, lle safai tŷ wrth droed tomen a roddai fri iddo a lle i lochesu.[[cite:ct-coflein-aber-llys]]",
                     "Ein dychymyg ni yw’r tŵr gwylio ar ei phen."])),
            dict(id="siwan", t=("Across the water to Llan-faes", "Dros y dŵr i Lan-faes"), src=["dwb-siwan", "wiki-siwan"],
                 p=(["From the top of the mound you look out over the Lafan Sands to Ynys Môn. Over there, on the shore near where Beaumaris stands today, is Llan-faes.",
                     "Siwan, wife of Llywelyn the Great and daughter of King John of England, died here at Aber on 2 February 1237. She had been Llywelyn’s partner in ruling and his envoy to the English court time and again. "
                     "He had her buried across the water at Llan-faes, and there he founded a friary of Franciscans in her memory.[[cite:dwb-siwan,wiki-siwan]]",
                     "Her stone coffin survives, and can be seen today in the church at Beaumaris.[[cite:wiki-siwan]]"],
                    ["O ben y domen edrychwch dros Draeth Lafan at Ynys Môn. Draw acw, ar y lan yn ymyl lle saif Biwmares heddiw, mae Llan-faes.",
                     "Bu farw Siwan, gwraig Llywelyn Fawr a merch y Brenin John o Loegr, yma yn Aber ar 2 Chwefror 1237. Bu’n gymar i Lywelyn wrth reoli, ac yn gennad drosto i lys Lloegr dro ar ôl tro. "
                     "Claddodd ef hi dros y dŵr yn Llan-faes, a sefydlodd yno frodordy o Ffransisiaid er cof amdani.[[cite:dwb-siwan,wiki-siwan]]",
                     "Mae ei harch garreg wedi goroesi, ac mae i’w gweld heddiw yn eglwys Biwmares.[[cite:wiki-siwan]]"])),
            dict(id="dafydd", t=("Dafydd, Prince of Wales", "Dafydd, Tywysog Cymru"), src=["ct-wiki-dafydd"],
                 p=(["Siwan’s son, Dafydd ap Llywelyn, followed his father as ruler of Gwynedd in 1240. In 1244 he became the first to take princeps Wallie, Prince of Wales, as his formal title, and he asked the Pope to take Wales under his protection as a kingdom in its own right.[[cite:ct-wiki-dafydd]]",
                     "He rallied the princes of Wales and won back much of what had been lost, but died young, here at Aber, in February 1246, and was buried beside his father at Aberconwy.[[cite:ct-wiki-dafydd]]",
                     "The west wing, beyond the dais, held the prince’s own chamber, with a room above it. Its plan is from the dig; its height and its windows are imagined."],
                    ["Dilynodd mab Siwan, Dafydd ap Llywelyn, ei dad yn rheolwr Gwynedd yn 1240. Yn 1244 ef oedd y cyntaf i gymryd princeps Wallie, Tywysog Cymru, yn deitl ffurfiol, a gofynnodd i’r Pab gymryd Cymru dan ei nawdd fel teyrnas yn ei hawl ei hun.[[cite:ct-wiki-dafydd]]",
                     "Cynullodd dywysogion Cymru ac ennill yn ôl lawer o’r hyn a gollwyd, ond bu farw’n ifanc, yma yn Aber, ym mis Chwefror 1246, a’i gladdu wrth ochr ei dad yn Aberconwy.[[cite:ct-wiki-dafydd]]",
                     "Yn yr adain orllewinol, y tu hwnt i’r llwyfan, roedd ystafell y tywysog ei hun, ac ystafell uwch ei phen. O’r cloddio y daw ei chynllun; dychmygwyd ei huchder a’i ffenestri."])),
            dict(id="inside", t=("Inside the hall", "Y tu mewn i’r neuadd"), src=["ct-laws"],
                 p=(["Step inside. The fire burns on a hearth in the middle of the floor, and the smoke finds its way out through a louvre in the roof. At the upper end, on the dais, sits the prince. At the lower end are the doors to the buttery and the pantry.",
                     "The Laws of Hywel Dda give everyone at court a place in the hall. The edling, the heir, sits facing the prince across the fire. Between the edling and the nearest pillar sits the judge of the court, then the priest of the household, then the pencerdd, the chief poet, who sings first in the hall. "
                     "At the far end sits the penteulu, the captain of the household troop, with his warband around him.[[cite:ct-laws]]",
                     "Twenty-four officers served the court, from the steward and the chief falconer to the cook and the doorkeeper, each with his own seat, his own share of the meat and mead, and his own gifts from the prince at the great feasts.[[cite:ct-laws]]"],
                    ["Camwch i mewn. Mae’r tân yn llosgi ar aelwyd yng nghanol y llawr, a’r mwg yn canfod ei ffordd allan drwy lwfer yn y to. Yn y pen uchaf, ar y llwyfan, eistedd y tywysog. Yn y pen isaf mae’r drysau i’r bwtri a’r pantri.",
                     "Mae Cyfraith Hywel Dda yn rhoi ei le yn y neuadd i bawb yn y llys. Eistedd yr edling, yr etifedd, gyferbyn â’r tywysog ar draws y tân. Rhwng yr edling a’r golofn agosaf eistedd ynad llys, yna offeiriad teulu, yna’r pencerdd, sy’n canu gyntaf yn y neuadd. "
                     "Yn y pen draw eistedd y penteulu, capten gosgordd y llys, a’r osgordd o’i amgylch.[[cite:ct-laws]]",
                     "Roedd pedwar swyddog ar hugain yn gwasanaethu’r llys, o’r distain a’r penhebogydd i’r cog a’r drysor, pob un â’i sedd ei hun, ei gyfran ei hun o’r cig a’r medd, a’i roddion ei hun gan y tywysog ar y gwyliau mawr.[[cite:ct-laws]]"])),
            dict(id="eleanor", t=("Eleanor and Gwenllian, June 1282", "Elinor a Gwenllian, Mehefin 1282"), src=["pl-dwb-eleanor", "ct-coflein-aber"],
                 p=(["Llywelyn ap Gruffudd, Prince of Wales, married Eleanor de Montfort, daughter of Simon de Montfort, at Worcester in 1278. She had been promised to him years before, but when she sailed to join him in 1275 English ships took her at sea, and she was held for three years before she could come to Wales.[[cite:pl-dwb-eleanor]]",
                     "Here at Aber, on 19 June 1282, Eleanor gave birth to their daughter, Gwenllian, and died. She was buried at the friary of Llan-faes, the house Llywelyn the Great had founded for Siwan.[[cite:pl-dwb-eleanor,ct-coflein-aber]]",
                     "The cradle by the bed is our own picture of that summer."],
                    ["Priododd Llywelyn ap Gruffudd, Tywysog Cymru, ag Elinor de Montfort, merch Simon de Montfort, yng Nghaerwrangon yn 1278. Roedd hi wedi’i haddo iddo flynyddoedd ynghynt, ond pan hwyliodd i ymuno ag ef yn 1275 cipiwyd hi ar y môr gan longau Lloegr, a’i chadw am dair blynedd cyn y gallai ddod i Gymru.[[cite:pl-dwb-eleanor]]",
                     "Yma yn Aber, ar 19 Mehefin 1282, ganed eu merch, Gwenllian, a bu farw Elinor. Claddwyd hi ym mrodordy Llan-faes, y tŷ a sefydlodd Llywelyn Fawr er cof am Siwan.[[cite:pl-dwb-eleanor,ct-coflein-aber]]",
                     "Ein darlun ni o’r haf hwnnw yw’r crud wrth y gwely."])),
            dict(id="letters", t=("Garth Celyn, November 1282", "Garth Celyn, Tachwedd 1282"), src=["ct-hurlock", "ct-wiki-garthcelyn", "ct-peckham", "pl-dwb-llywelyn"],
                 p=(["In the autumn of 1282 Wales was at war. John Peckham, Archbishop of Canterbury, came into Snowdonia to make peace. He offered Llywelyn a great estate in England if he would give Wales up to King Edward.[[cite:ct-hurlock]]",
                     "Llywelyn dated his answers to the archbishop here, at “Garth Kelyn”.[[cite:ct-wiki-garthcelyn]] He would not abandon the people whom his forefathers had protected since “the days of Kamber son of Brutus”. His reply has been compared to the Declaration of Arbroath.[[cite:ct-hurlock]]",
                     "The men of Snowdon sent their own answer: even if their prince should give them up to the king, they would not do homage to any stranger, whose language, customs and laws they did not know.[[cite:ct-peckham]]",
                     "A month later, on 11 December 1282, Llywelyn was killed near Builth.[[cite:pl-dwb-llywelyn]]"],
                    ["Yn hydref 1282 roedd Cymru mewn rhyfel. Daeth John Peckham, Archesgob Caergaint, i Eryri i geisio heddwch. Cynigiodd ystad fawr yn Lloegr i Lywelyn pe rhoddai Gymru i fyny i’r Brenin Edward.[[cite:ct-hurlock]]",
                     "Dyddiodd Llywelyn ei atebion i’r archesgob yma, yn “Garth Kelyn”.[[cite:ct-wiki-garthcelyn]] Ni fynnai gefnu ar y bobl a amddiffynnodd ei gyndadau ers “dyddiau Camber fab Brutus”. Cymharwyd ei ateb â Datganiad Arbroath.[[cite:ct-hurlock]]",
                     "Anfonodd gwŷr Eryri eu hateb eu hunain: hyd yn oed pe rhoddai eu tywysog hwy i fyny i’r brenin, ni wnaent wrogaeth i unrhyw estron nad adwaenent ei iaith, ei arferion na’i gyfreithiau.[[cite:ct-peckham]]",
                     "Fis yn ddiweddarach, ar 11 Rhagfyr 1282, lladdwyd Llywelyn ger Llanfair-ym-Muallt.[[cite:pl-dwb-llywelyn]]"])),
            dict(id="garthcelyn", t=("Pen y Bryn", "Pen y Bryn"), src=["ct-wiki-garthcelyn", "ct-gatehouse-penybryn"],
                 p=(["Look across the river to the hill. That is Pen y Bryn, a house standing within a double bank and ditch 90 to 100 metres across, which Cadw protects as a scheduled monument.[[cite:ct-wiki-garthcelyn,ct-gatehouse-penybryn]]",
                     "The Garth Celyn Trust holds that the princes’ court stood here, on the hill, and that this is Garth Celyn itself. The house has a round stone tower four storeys high, which some believe is medieval at heart.[[cite:ct-wiki-garthcelyn,ct-gatehouse-penybryn]]",
                     "Where exactly the court stood, in the valley by the mound or on the hill, is still argued over, and both places belong to the story of Aber. We have drawn the hall where the excavators found it, and a stone house and tower on the hill, as many believe stood there. Pen y Bryn is a private home today."],
                    ["Edrychwch dros yr afon at y bryn. Dyna Ben y Bryn, tŷ sy’n sefyll o fewn clawdd dwbl a ffos 90 i 100 metr ar draws, a warchodir gan Cadw yn heneb gofrestredig.[[cite:ct-wiki-garthcelyn,ct-gatehouse-penybryn]]",
                     "Mae Ymddiriedolaeth Garth Celyn yn credu mai yma, ar y bryn, y safai llys y tywysogion, ac mai dyma Garth Celyn ei hun. Mae gan y tŷ dŵr carreg crwn pedwar llawr o uchder, ac mae rhai’n credu ei fod yn ganoloesol yn ei galon.[[cite:ct-wiki-garthcelyn,ct-gatehouse-penybryn]]",
                     "Mae dadlau o hyd am union safle’r llys, yn y dyffryn wrth y domen neu ar y bryn, ac mae’r ddau le’n perthyn i hanes Aber. Rydym wedi tynnu’r neuadd lle cafodd y cloddwyr hi, a thŷ a thŵr carreg ar y bryn, fel y cred llawer y safent yno. Cartref preifat yw Pen y Bryn heddiw."])),
            dict(id="bera", t=("Dafydd on the Bera, June 1283", "Dafydd ar y Bera, Mehefin 1283"), src=["ct-coflein-aber", "ct-wiki-dafyddg"],
                 p=(["Look south-east, up the valley towards the mountains. After Llywelyn fell, his brother Dafydd ap Gruffudd took up the fight as Prince of Wales, and held out in the mountains of Snowdonia into the summer of 1283.[[cite:ct-wiki-dafyddg]]",
                     "In June 1283 he was taken on the Bera, the mountain above this valley.[[cite:ct-coflein-aber]] He was brought to Shrewsbury and put to death there that October.[[cite:ct-wiki-dafyddg]]",
                     "Up this valley too is Rhaeadr Fawr, the Aber Falls, at the end of a path the princes’ people knew."],
                    ["Edrychwch tua’r de-ddwyrain, i fyny’r dyffryn tua’r mynyddoedd. Wedi i Lywelyn syrthio, cododd ei frawd Dafydd ap Gruffudd y frwydr yn Dywysog Cymru, a daliodd ei dir ym mynyddoedd Eryri hyd haf 1283.[[cite:ct-wiki-dafyddg]]",
                     "Ym mis Mehefin 1283 daliwyd ef ar y Bera, y mynydd uwchben y dyffryn hwn.[[cite:ct-coflein-aber]] Aed ag ef i Amwythig a’i ladd yno y mis Hydref hwnnw.[[cite:ct-wiki-dafyddg]]",
                     "I fyny’r dyffryn hwn hefyd mae Rhaeadr Fawr, ar ben llwybr a adwaenai pobl y tywysogion."])),
            dict(id="spade", t=("What the spade found", "Yr hyn a ganfu’r rhaw"), src=["ct-coflein-aber-llys", "ct-gatehouse-aber", "ct-johnstone-aber", "ct-aber-2010"],
                 p=(["The court was not forgotten. After the conquest it was kept in repair: work is recorded in 1289 and 1303, and when John Leland came by in the 1530s part of the building was still standing.[[cite:ct-coflein-aber-llys,ct-gatehouse-aber]]",
                     "In 1993 the hall with its cross-wings was found in the field beside Pen y Mwd. In the dry summer of 2006 its lines showed in the grass and were photographed from the air, and in 2010 and 2011 the Snowdonia National Park, Gwynedd Archaeological Trust and Cadw dug again, with the schoolchildren of the area coming to watch. "
                     "The site proved larger and more complex than anyone had thought.[[cite:ct-coflein-aber-llys,ct-johnstone-aber,ct-aber-2010]]",
                     "The remains have been covered over again to keep them safe. Stand in the field by the mound, and you are standing in the court of the princes of Gwynedd."],
                    ["Nid anghofiwyd y llys. Wedi’r goresgyniad fe’i cadwyd mewn cyflwr da: cofnodir gwaith yn 1289 a 1303, a phan ddaeth John Leland heibio yn y 1530au roedd rhan o’r adeilad yn sefyll o hyd.[[cite:ct-coflein-aber-llys,ct-gatehouse-aber]]",
                     "Yn 1993 cafwyd y neuadd a’i hadenydd croes yn y cae wrth ymyl Pen y Mwd. Yn haf sych 2006 dangosodd ei llinellau yn y glaswellt a thynnwyd eu llun o’r awyr, ac yn 2010 a 2011 cloddiodd Parc Cenedlaethol Eryri, Ymddiriedolaeth Archaeolegol Gwynedd a Cadw eto, a phlant ysgol yr ardal yn dod i wylio. "
                     "Profodd y safle’n fwy ac yn fwy cymhleth nag a feddyliodd neb.[[cite:ct-coflein-aber-llys,ct-johnstone-aber,ct-aber-2010]]",
                     "Mae’r olion wedi’u gorchuddio eto i’w cadw’n ddiogel. Safwch yn y cae wrth y domen, ac rydych yn sefyll yn llys tywysogion Gwynedd."])),
        ],
        known=(["Known from the ground: the mound Pen y Mwd and the ditch on its south side, measured by the Royal Commission; a stone hall with a cross-wing at each end, 11.2 by 8 metres inside, found in 1993 and dug again in 2010–11, with pottery and a brooch of the 1200s and 1300s; the double bank and ditch round Pen y Bryn on the hill across the river.",
                "Known from the records: Siwan’s death at Aber in 1237, Dafydd ap Llywelyn’s in 1246, and Eleanor’s in 1282 after Gwenllian was born; Llywelyn’s answers of November 1282 dated at Garth Celyn; Dafydd ap Gruffudd taken on the Bera in 1283; repairs in 1289 and 1303; part of the building still standing in the 1530s.",
                "Imagined: which way the hall ran, how high its walls stood and what its roofs were made of; the upper rooms of the wings; the yard, its fence, the kitchen, the stable, the oven and the forge; the look-out on the mound; the houses of the township, the church, the mill and the bridge; and the house and tower on Pen y Bryn, drawn as many believe they stood. We have limewashed the walls and roofed the hall with slate from the hills nearby."],
               ["Yn hysbys o’r tir: y domen Pen y Mwd a’r ffos ar ei hochr ddeheuol, wedi’u mesur gan y Comisiwn Brenhinol; neuadd garreg ag adain groes ym mhob pen, 11.2 wrth 8 metr y tu mewn, a ganfuwyd yn 1993 ac a gloddiwyd eto yn 2010–11, gyda chrochenwaith a thlws o’r 1200au a’r 1300au; y clawdd dwbl a’r ffos o amgylch Pen y Bryn ar y bryn dros yr afon.",
                "Yn hysbys o’r cofnodion: marw Siwan yn Aber yn 1237, marw Dafydd ap Llywelyn yn 1246, a marw Elinor yn 1282 wedi geni Gwenllian; atebion Llywelyn ym mis Tachwedd 1282 wedi’u dyddio yng Ngarth Celyn; dal Dafydd ap Gruffudd ar y Bera yn 1283; atgyweirio yn 1289 a 1303; rhan o’r adeilad yn sefyll o hyd yn y 1530au.",
                "Wedi’i ddychmygu: i ba gyfeiriad y rhedai’r neuadd, pa mor uchel oedd ei muriau ac o beth y gwnaed ei thoeau; ystafelloedd uchaf yr adenydd; y buarth, ei ffens, y gegin, y stabl, y popty a’r efail; y tŵr gwylio ar y domen; tai’r drefgordd, yr eglwys, y felin a’r bont; a’r tŷ a’r tŵr ar Ben y Bryn, fel y cred llawer y safent. Rydym wedi gwyngalchu’r muriau a thoi’r neuadd â llechi o’r bryniau gerllaw."]),
        ld=dict(name="Garth Celyn, Abergwyngregyn", description="The court of the princes of Gwynedd at Aber, between Snowdonia and the Menai: a stone hall with two cross-wings found by excavation beside the mound Pen y Mwd, where Siwan died in 1237 and Gwenllian was born in 1282."),
    ),
]

BY_ID = {c["id"]: c for c in COURTS}

UI = dict(
    canvas=("A 3D picture of {name}. The stops below tell the same story in words.", "Llun 3D o {name}. Mae’r arosfannau isod yn adrodd yr un hanes mewn geiriau."),
    tour=("Next stop", "Yr arhosfan nesaf"), next=("Next", "Nesaf"), prev=("Back", "Yn ôl"), again=("Back to the start", "Yn ôl i’r dechrau"),
    close=("Close", "Cau"), fs=("Full screen", "Sgrin lawn"), stop=("Stop {n} of {of}", "Arhosfan {n} o {of}"), src=("Sources", "Ffynonellau"),
    help=("Walk with W A S D or the arrow keys. Drag to look around. Click a gold marker to go to it.",
          "Cerddwch gyda W A S D neu’r bysellau saeth. Llusgwch i edrych o gwmpas. Cliciwch ar nod aur i fynd ato."),
    helpTouch=("Walk with the circle. Drag to look around. Tap a gold marker to go to it.",
               "Cerddwch gyda’r cylch. Llusgwch i edrych o gwmpas. Tapiwch nod aur i fynd ato."),
)

# The start screen: "Enter the court" loads the 3D. "See it in pictures" (and every device that cannot or should not
# draw 3D: no WebGL, data saver, a slow connection, 1 GB of memory or less) shows the still pictures made from the 3D
# (src/static/court/<id>-<stop>.webp, made by tools/court_stills.js) with the same words, one stop at a time.
START_JS = """addEventListener("DOMContentLoaded",function(){var s=document.getElementById("ll-stage"),b=document.getElementById("ll-go"),pb=document.getElementById("ll-pics");if(!s||!b)return;
var cy=document.documentElement.lang==="cy",T=function(p){return cy?p[1]:p[0]},ok=false;try{var c=document.createElement("canvas");ok=!!(window.WebGLRenderingContext&&(c.getContext("webgl2")||c.getContext("webgl")))}catch(e){}
var n=navigator.connection||{},slow=n.saveData||/(^|-)(2g|3g)$/.test(n.effectiveType||"")||(navigator.deviceMemory&&navigator.deviceMemory<=1);
function esc(t){return t.replace(/[&<>]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;"}[c]})}
function pics(){var i=0,st=LLYS.stops,box=document.createElement("div");box.className="ll-ui ll-stills";
box.innerHTML='<img class="ll-still" alt=""><div class="ll-panel"><p class="ll-n"></p><h2 tabindex="-1"></h2><div class="ll-txt"></div><p class="ll-src"></p><div class="ll-btns"><button type="button" class="btn" data-k="prev">← '+T(LLYS.ui.prev)+'</button><button type="button" class="btn solid" data-k="next">'+T(LLYS.ui.next)+' →</button></div></div>';
s.appendChild(box);s.classList.add("ready","pics");var im=box.querySelector("img");
function show(k){i=(k+st.length)%st.length;var q=st[i];im.src="court/"+LLYS.id+"-"+q.id+".webp";im.alt=T(q.t);box.querySelector(".ll-n").textContent=T(LLYS.ui.stop).replace("{n}",i+1).replace("{of}",st.length);
box.querySelector("h2").textContent=T(q.t);box.querySelector(".ll-txt").innerHTML=T(q.p).map(function(p){return"<p>"+esc(p)+"</p>"}).join("");
box.querySelector(".ll-src").textContent=q.src?T(LLYS.ui.src)+": "+T(q.src).join(" · "):"";box.querySelector('[data-k="prev"]').disabled=i===0;box.querySelector('[data-k="next"]').textContent=(i===st.length-1?T(LLYS.ui.again):T(LLYS.ui.next))+" →"}
box.addEventListener("click",function(e){var t=e.target.closest("button");if(!t)return;show(i+(t.dataset.k==="prev"?-1:1));box.querySelector("h2").focus({preventScroll:true})});show(0)}
pb.onclick=pics;if(!ok){s.classList.add("fail");pics();return}if(slow)s.classList.add("slow");
b.onclick=function(){b.disabled=true;b.textContent=cy?"Wrthi’n llwytho…":"Loading…";s.classList.add("on");LLYS.cy=cy;import("__JS__").then(function(m){m.start(s,LLYS)}).catch(function(){s.classList.add("fail");pics()})}})"""


def setup(build_globals):
    g.update(build_globals)


def games():
    """Rows for GAMES in build.py (play.html), one per court."""
    return [(f"court-{c['id']}.html", "llys", c["card"][0], c["card"][1], c["card"][2], c["card"][3], "Explore in 3D", "Crwydro mewn 3D", c["era"]) for c in COURTS]


def _src_name(k, cy):
    s = g["CITE"].S.get(k) if g.get("CITE") else None
    if not s:
        return k
    return s["short"][1 if cy else 0]


def page(c):
    bi, section, hero, SITE, e = g["bi"], g["section"], g["hero"], g["SITE"], g["e"]
    cid = c["id"]
    href, en_c, cy_c = c["crumbs"]
    top = hero(c["era"], f'<a href="index.html">{SITE}</a> / <a href="{href}">{bi(en_c, cy_c)}</a> / <a href="play.html">{bi("Play", "Chwarae")}</a>', "book",
               c["eyebrow"][0], c["eyebrow"][1], c["title"][0], c["title"][1], c["sub"][0], c["sub"][1], art="castle")
    stage = (f'<div class="ll-stage" id="ll-stage"><img class="ll-poster" src="court/{cid}-poster.webp" alt="" width="1200" height="675" loading="lazy" decoding="async">'
             f'<div class="ll-start"><p>{bi("The court is drawn on your device, so it takes a moment to load. On a slow connection, look at it in pictures instead.", "Caiff y llys ei dynnu ar eich dyfais, felly mae’n cymryd eiliad i lwytho. Ar gysylltiad araf, edrychwch arno mewn lluniau yn lle hynny.")}</p>'
             f'<p class="ll-gos"><button type="button" class="btn solid ll-go" id="ll-go">{bi("Enter the court", "Mynd i mewn i’r llys")} →</button> '
             f'<button type="button" class="btn ll-pics" id="ll-pics">{bi("See it in pictures", "Ei weld mewn lluniau")}</button></p></div>'
             f'<p class="ll-fail-msg">{bi("Your browser cannot show 3D here, so here it is in pictures.", "Ni all eich porwr ddangos 3D yma, felly dyma fe mewn lluniau.")}</p></div>'
             f'<p class="muted ll-note">{bi("Pictures drawn in 3D on this site, from the excavation, the records and the poem. See below for what we know and what we have imagined.", "Lluniau 3D a dynnwyd ar y wefan hon, o’r cloddio, y cofnodion a’r gerdd. Gweler isod yr hyn a wyddom a’r hyn a ddychmygwyd.")}</p>')
    words = "".join(f'<li id="stop-{s["id"]}"><h3>{bi(*s["t"])}</h3>' + "".join(f"<p>{bi(a, b)}</p>" for a, b in zip(*s["p"])) + "</li>" for s in c["stops"])
    known = "".join(f"<li>{bi(a, b)}</li>" for a, b in zip(*c["known"]))
    keys = []
    for s in c["stops"]:
        for k in s["src"]:
            if k not in keys:
                keys.append(k)
    S = g["CITE"].S
    srcs = "".join(
        f'<li><a href="{e(S[k]["url"])}" target="_blank" rel="noopener"><cite>{e(S[k]["t"])}</cite> ↗</a>, {bi(*S[k]["by"])}. {bi(*S[k]["note"])}</li>' if S[k].get("url")
        else f'<li><cite>{e(S[k]["t"])}</cite>, {bi(*S[k]["by"])}. {bi(*S[k]["note"])}</li>' for k in keys if k in S)
    more = '<p class="more-row">' + " ".join(f'<a class="btn" href="{h}">{bi(a, b)} →</a>' for h, a, b in c["more"]) + "</p>"
    others = [o for o in COURTS if o["id"] != cid]
    other = ('<p class="more-row">' + f'<a class="btn" href="llys-rhosyr.html">{bi("Llys Rhosyr in 3D", "Llys Rhosyr mewn 3D")} →</a> '
             + " ".join(f'<a class="btn" href="court-{o["id"]}.html">{bi(o["card"][0], o["card"][1])} →</a>' for o in others) + "</p>")
    n = len(c["stops"])
    main = (top + f'<section class="game-sec"><div class="wrap">{stage}</div></section>'
            + section(f'<ol class="ll-stops">{words}</ol>{more}', f"The {n} stops", f"Y {n} arhosfan")
            + section(f'<ul class="ct-known">{known}</ul>', "What we know, and what we have imagined", "Yr hyn a wyddom, a’r hyn a ddychmygwyd")
            + section(f'<ol class="ct-srcs">{srcs}</ol>', "How we know", "Sut y gwyddom")
            + section(other, "More courts in 3D", "Rhagor o lysoedd mewn 3D"))
    data = dict(name=list(c["name"]),
                stops=[dict(id=s["id"], t=list(s["t"]), p=[[_plain(x) for x in s["p"][0]], [_plain(x) for x in s["p"][1]]],
                            src=[[_src_name(k, False) for k in s["src"]], [_src_name(k, True) for k in s["src"]]]) for s in c["stops"]],
                ui={k: [v[0].replace("{name}", c["name"][0]), v[1].replace("{name}", c["name"][1])] for k, v in UI.items()})
    v = g["_static_fp"](f"court-{cid}.js")
    extra = (f'<script>var LLYS={json.dumps(data, ensure_ascii=False, separators=(",", ":"))};LLYS.id="{cid}";</script>\n'
             '<script>' + START_JS.replace("__JS__", f"./court-{cid}.js?v={v}") + '</script>\n')
    ld = {"@context": "https://schema.org", "@type": "LandmarksOrHistoricalBuildings", "name": c["ld"]["name"], "description": c["ld"]["description"],
          "geo": {"@type": "GeoCoordinates", "latitude": c["lat"], "longitude": c["lon"]}}
    return g["page"](f"court-{cid}.html", c["seo"][0], c["seo"][1], main, era=c["era"], ld=ld, active="play.html", track=f"game:court-{cid}", extra=extra)


def pages():
    return {f"court-{c['id']}.html": page(c) for c in COURTS}


CSS = """
.ct-known { display: grid; gap: .7rem; padding-left: 1.2rem; max-width: 52rem }
.ct-known li { line-height: 1.6 }
.ct-srcs { display: grid; gap: .8rem; padding-left: 1.4rem; max-width: 56rem; font-size: .95rem; line-height: 1.55 }
.ll-src { font-size: .8rem; color: var(--muted, #b9b2a3); margin: .2rem 0 0 }
.ll-gos { display: flex; flex-wrap: wrap; gap: .6rem; margin: 0 }
.ll-pics { font-size: 1rem; padding: .85rem 1.2rem; backdrop-filter: blur(6px) }
.ll-stage.slow .ll-pics { order: -1 }
.ll-stage.pics .ll-poster, .ll-stage.pics .ll-start, .ll-stage.pics .ll-fail-msg { display: none }
.ll-still { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover }
.ll-stills .ll-panel { pointer-events: auto }
@media (max-width: 700px) { .ll-stage.pics { aspect-ratio: auto; display: grid } .ll-stage.pics .ll-stills { position: static; display: grid } .ll-stage.pics .ll-still { position: static; aspect-ratio: 16 / 9; height: auto }
  .ll-stage.pics .ll-panel { position: static; width: auto; max-height: none; border-radius: 0; border: 0 } }
"""
