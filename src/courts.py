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
