"""Then and now: drag between an old picture of a Welsh castle, abbey or town and a photograph of the same place today.

Ifan asked for these on 14 November 2026. Each pair shows on its place page (place-<id>.html, under the photo) and all of
them on then-and-now.html. The old pictures are the Buck brothers' engravings of the 1740s, prints of the late 1700s and
early 1800s from the National Library of Wales, and the colour photochrom prints of about 1895 in the Library of Congress;
today's photographs are from Wikimedia Commons (mostly Geograph). Only free pictures: public domain, CC0, CC BY, CC BY-SA.

The pictures are kept on the site: src/static/thennow/<id>-then.webp and <id>-now.webp (1200 px wide) and -s copies
(640 px), cut to the same frame by tools/thennow_make.py so the two line up as closely as the old artist's view allows.
The slider is src/static/thennow.js; the styles are src/thennow.css.

Each pair:
    id      the file name of its pictures
    place   the place page it belongs on (src/data.py PLACES id), or None
    link    the page its title opens when there is no place page; a town-<slug>.html link also shows the pair on that town page
    cat     "castles", "churches" or "towns"
    en, cy  its name
    then    (Commons file, artist, licence, licence link, date EN, date CY, what it shows EN, CY)
    now     (Commons file, photographer, licence, licence link, what it shows EN, CY)
    what    (EN, CY): what has changed between the two, in a sentence or two
    ar      width / height of the pictures
"""
from html import escape as _e
from urllib.parse import quote as _q

COMMONS = "https://commons.wikimedia.org/wiki/"
PD = "https://creativecommons.org/publicdomain/mark/1.0/"
CC0 = "https://creativecommons.org/publicdomain/zero/1.0/deed.en"
BYSA2 = "https://creativecommons.org/licenses/by-sa/2.0"
BYSA3 = "https://creativecommons.org/licenses/by-sa/3.0"
BYSA4 = "https://creativecommons.org/licenses/by-sa/4.0"
BY2 = "https://creativecommons.org/licenses/by/2.0"
BY4 = "https://creativecommons.org/licenses/by/4.0"

CATS = [
    ("castles", "Castles", "Cestyll"),
    ("churches", "Abbeys and cathedrals", "Abatai ac eglwysi cadeiriol"),
    ("towns", "Towns, bridges and valleys", "Trefi, pontydd a dyffrynnoedd"),
]

PC = "Photochrom Print Collection, Library of Congress"
LOC = "Library of Congress"
BUCK = "Samuel and Nathaniel Buck"
C1895 = ("About 1895", "Tua 1895")
C1890 = ("About 1890", "Tua 1890")


def _p(id, place, cat, en, cy, then, now, what, ar, link=None):
    return dict(id=id, place=place, link=link, cat=cat, en=en, cy=cy, then=then, now=now, what=what, ar=ar)


def _old(f, by, lic, licu, when, en, cy):
    return (f, by, lic, licu, when[0], when[1], en, cy)


PAIRS = [
    _p("conwy", "conwy", "castles", "Conwy Castle", "Castell Conwy",
       _old("Castle and suspension bridge, Conway (i.e. Conwy), Wales-LCCN2001703465.jpg", PC, "Public domain", PD, C1895,
            "Thomas Telford’s suspension bridge and the castle, from the river", "Pont grog Thomas Telford a’r castell, o’r afon"),
       ("Conwy Castle And Conwy Suspension Bridge - geograph.org.uk - 4667194.jpg", "Rude Health", "CC BY-SA 2.0", BYSA2,
        "the castle and the suspension bridge", "y castell a’r bont grog"),
       ("Telford’s suspension bridge of 1826 still runs to the castle gate. In the 1890s it carried every cart and coach into Conwy; since the new road bridge opened beside it in 1958 it has been kept for people on foot.",
        "Mae pont grog Telford o 1826 yn dal i redeg at borth y castell. Yn y 1890au roedd pob cert a choets yn ei chroesi i Gonwy; ers agor y bont ffordd newydd wrth ei hochr yn 1958, cerddwyr yn unig sy’n ei defnyddio."),
       1.4362),
    _p("caerffili", "caerffili", "castles", "Caerphilly Castle", "Castell Caerffili",
       _old("The castle, Caerphilly, Wales-LCCN2001703448.jpg", PC, "Public domain", PD, C1895,
            "the castle across the dry bed of its lake", "y castell dros wely sych ei lyn"),
       ("Caerphilly Castle and moat - geograph.org.uk - 4499797.jpg", "Gareth James", "CC BY-SA 2.0", BYSA2,
        "the castle across its lake", "y castell dros ei lyn"),
       ("In the 1890s the great lakes round Caerphilly had long drained away, leaving meadow and a stream. They were flooded again in the 1950s, and the castle stands in its water once more, the second largest castle in Britain.",
        "Yn y 1890au roedd llynnoedd mawr Caerffili wedi hen sychu, gan adael dôl a nant. Cawsant eu llenwi eto yn y 1950au, ac mae’r castell yn sefyll yn ei ddŵr unwaith eto, yr ail gastell mwyaf ym Mhrydain."),
       1.4366),
    _p("rhaglan", "rhaglan", "castles", "Raglan Castle", "Castell Rhaglan",
       _old("Raglan Castle, I., Wales-LCCN2002708065.jpg", PC, "Public domain", PD, C1895,
            "the gatehouse under ivy", "y porthdy dan eiddew"),
       ("The Gatehouse, Raglan Castle - geograph.org.uk - 8377487.jpg", "Stuart Wilding", "CC BY-SA 2.0", BYSA2,
        "the gatehouse today", "y porthdy heddiw"),
       ("Victorian visitors loved Raglan wrapped in ivy. The ivy was stripped away in the 1900s to save the stone, and the towers of Sir William ap Thomas and his son William Herbert stand clear again.",
        "Roedd ymwelwyr Oes Victoria wrth eu bodd â Rhaglan dan eiddew. Tynnwyd yr eiddew yn y 1900au i achub y garreg, ac mae tyrau Syr William ap Thomas a’i fab William Herbert i’w gweld yn glir eto."),
       1.3540),
    _p("penfro", "penfro", "castles", "Pembroke Castle", "Castell Penfro",
       _old("The castle, Pembroke, Wales-LCCN2001703529.jpg", PC, "Public domain", PD, C1895,
            "the castle on its rock above the Mill Pond", "y castell ar ei graig uwchben y Pwll Melin"),
       ("Pembroke Castle 1.jpg", "Athena Flickr", "CC BY 2.0", BY2,
        "the castle from the Mill Pond", "y castell o’r Pwll Melin"),
       ("Henry Tudor, the Welshman who took the crown in 1485, was born in this castle in 1457. In the 1890s it was a ruin; from 1928 Sir Ivor Philipps rebuilt its walls and towers, and trees now cover the rock below.",
        "Ganwyd Harri Tudur, y Cymro a gipiodd y goron yn 1485, yn y castell hwn yn 1457. Adfail oedd yn y 1890au; o 1928 ymlaen ailgododd Syr Ivor Philipps ei furiau a’i dyrau, ac mae coed bellach yn gorchuddio’r graig oddi tano."),
       1.9188),
    _p("cricieth", "cricieth", "castles", "Criccieth Castle", "Castell Cricieth",
       _old("From the parade, Criccieth Castle, Wales-LCCN2001703467.jpg", PC, "Public domain", PD, C1895,
            "the castle on its headland, from the parade", "y castell ar ei bentir, o’r promenâd"),
       ("Criccieth Castle and beach - geograph.org.uk - 5540597.jpg", "Mark Percy", "CC BY-SA 2.0", BYSA2,
        "the castle and the beach", "y castell a’r traeth"),
       ("Llywelyn ab Iorwerth built the castle on this headland in the 1230s. The little seaside town below has grown along the shore since the 1890s, but the castle still watches over Bae Ceredigion.",
        "Llywelyn ab Iorwerth a gododd y castell ar y pentir hwn yn y 1230au. Mae’r dref glan môr fach oddi tano wedi tyfu ar hyd y traeth ers y 1890au, ond mae’r castell yn dal i wylio dros Fae Ceredigion."),
       1.3556),
    _p("dolwyddelan2", "dolwyddelan", "castles", "Dolwyddelan Castle", "Castell Dolwyddelan",
       _old("The east view of Dolwyddelan Castle - in the county of Caernarvon.jpeg", BUCK, "Public domain", PD, ("1742", "1742"),
            "the east view of the castle", "golwg o’r dwyrain ar y castell"),
       ("Dolwyddelan Castle Path.jpg", "Nicolas Raymond", "CC BY-SA 4.0", BYSA4,
        "the keep on its ridge", "y gorthwr ar ei grib"),
       ("Llywelyn ab Iorwerth’s keep was roofless when the Bucks drew it in 1742. Between 1848 and 1850 it was given back a top storey and battlements, which is why it looks more whole today than it did then.",
        "Roedd gorthwr Llywelyn ab Iorwerth heb do pan dynnodd y brodyr Buck ei lun yn 1742. Rhwng 1848 a 1850 cafodd lawr uchaf a bylchfuriau newydd, a dyna pam ei fod yn edrych yn fwy cyflawn heddiw nag yr oedd bryd hynny."),
       1.6000),
    _p("caernarfon", "caernarfon", "castles", "Caernarfon Castle", "Castell Caernarfon",
       _old("The south east view of Caernarvon Castle (1131028).jpg", BUCK, "CC0", CC0, ("1742", "1742"),
            "the south-east view across the Seiont", "golwg o’r de-ddwyrain dros afon Seiont"),
       ("June 2025 - Caernarfon Castle - 05.jpg", "ohefin", "CC BY-SA 2.0", BYSA2,
        "the castle across the harbour", "y castell dros yr harbwr"),
       ("The towers the Bucks drew in 1742 stand as they did, with their bands of coloured stone. Where trading ships tied up below the walls there are now small boats, and a swing bridge crosses the Seiont.",
        "Mae’r tyrau a dynnodd y brodyr Buck yn 1742 yn sefyll fel yr oeddent, gyda’u bandiau o garreg liw. Lle bu llongau masnach wrth y muriau mae cychod bach heddiw, ac mae pont sy’n troi yn croesi’r Seiont."),
       2.4000),
    _p("beaumaris", "beaumaris", "castles", "Beaumaris Castle", "Castell Biwmares",
       _old("Beaumaris Castle (1131274).jpg", "Benjamin Ralph, engraved by John Ryland", "CC0", CC0, ("About 1780", "Tua 1780"),
            "the castle from the land, with the Menai behind", "y castell o’r tir, gyda’r Fenai y tu ôl"),
       ("Beaumaris Castle and Moat - geograph.org.uk - 2389381.jpg", "Christine Matthews", "CC BY-SA 2.0", BYSA2,
        "the outer walls across the moat", "y muriau allanol dros y ffos"),
       ("Beaumaris was begun in 1295 and never finished: its towers never reached their full height. Today the moat is full of water and the low outer walls rise straight out of it.",
        "Dechreuwyd Biwmares yn 1295 ac ni chafodd ei orffen erioed: ni chyrhaeddodd ei dyrau eu huchder llawn. Heddiw mae’r ffos yn llawn dŵr a’r muriau allanol isel yn codi’n syth ohoni."),
       1.6227),
    _p("chepstow", "chepstow", "castles", "Chepstow Castle", "Castell Cas-gwent",
       _old("Castle, I, Chepstow, Wales-LCCN2002696539.jpg", PC, "Public domain", PD, C1895,
            "the castle on its cliff above the Wye", "y castell ar ei glogwyn uwchben Gwy"),
       ("Chepstow Castle from North bank.jpg", "Andy Dingley", "CC BY-SA 3.0", BYSA3,
        "the castle from the far bank of the Wye", "y castell o lan bellaf Gwy"),
       ("Begun soon after 1067, Chepstow is one of the oldest stone castles in Britain. Its long line of walls on the cliff above the Wye has hardly changed since the 1890s.",
        "Cafodd ei ddechrau’n fuan ar ôl 1067, ac mae Cas-gwent yn un o’r cestyll carreg hynaf ym Mhrydain. Prin fod llinell hir ei furiau ar y clogwyn uwchben Gwy wedi newid ers y 1890au."),
       1.3546),
    _p("dolbadarn", "dolbadarn", "castles", "Dolbadarn Castle", "Castell Dolbadarn",
       _old("Dolbadarn Castle, Llanberis, Wales-LCCN2001703500.jpg", PC, "Public domain", PD, C1895,
            "the round tower above Llyn Peris", "y tŵr crwn uwchben Llyn Peris"),
       ("Dolbadarn Castle, Just above Llyn Peris in Llanberis (16156431945).jpg", "Garry Platt", "CC BY 2.0", BY2,
        "the tower and the mountains of Eryri", "y tŵr a mynyddoedd Eryri"),
       ("Llywelyn ab Iorwerth’s round tower has guarded the pass of Llanberis for eight hundred years. Between the two pictures almost nothing has changed but the weather.",
        "Mae tŵr crwn Llywelyn ab Iorwerth wedi gwarchod Bwlch Llanberis ers wyth can mlynedd. Rhwng y ddau lun, prin fod dim wedi newid ond y tywydd."),
       1.3545),
    _p("rhuddlan", "rhuddlan", "castles", "Rhuddlan Castle", "Castell Rhuddlan",
       _old("Rhuddlan Castle, Rhyl, Wales-LCCN2001703539.jpg", PC, "Public domain", PD, C1895,
            "cattle in the Clwyd below the castle", "gwartheg yn afon Clwyd o dan y castell"),
       ("Castell Rhuddlan (52846055358).jpg", "Simaron", "CC BY-SA 2.0", BYSA2,
        "the castle above the Clwyd", "y castell uwchben afon Clwyd"),
       ("In the 1890s cattle came down to drink in the Clwyd under the castle walls. Today the banks are grassed and fenced, and the twin towers of the gatehouses stand over the river as they did.",
        "Yn y 1890au deuai gwartheg i yfed yn afon Clwyd o dan furiau’r castell. Heddiw mae’r glannau dan laswellt a ffens, ac mae tyrau dwbl y pyrth yn sefyll uwchben yr afon fel cynt."),
       1.3504),
    _p("aberystwyth", None, "castles", "Aberystwyth Castle", "Castell Aberystwyth",
       _old("The castle, Aberystwith, Wales-LCCN2001703410.jpg", PC, "Public domain", PD, C1895,
            "the ruins on the headland", "yr adfeilion ar y pentir"),
       ("Aberystwyth Castle - view from southeast - geograph.org.uk - 3183943.jpg", "Rob Farrow", "CC BY-SA 2.0", BYSA2,
        "the ruins from the south-east", "yr adfeilion o’r de-ddwyrain"),
       ("Owain Glyndŵr held this castle from 1404 to 1408. Its broken towers by the sea were already a park for visitors in the 1890s, and the paths and lawns are still there today.",
        "Owain Glyndŵr oedd yn dal y castell hwn o 1404 hyd 1408. Roedd ei dyrau drylliedig ger y môr eisoes yn barc i ymwelwyr yn y 1890au, ac mae’r llwybrau a’r lawntiau yno o hyd."),
       1.3592, link="town-aberystwyth.html"),
    _p("swansea", None, "castles", "Swansea Castle", "Castell Abertawe",
       _old("Swansea castle (1128961).jpg", "Paul Sandby, engraved by Richard Bernard Godfrey", "CC0", CC0, ("1786", "1786"),
            "the castle among the houses of the town", "y castell ymhlith tai’r dref"),
       ("Swansea Castle 2018.jpg", "Tiia Monto", "CC BY-SA 4.0", BYSA4,
        "the castle in the middle of the city", "y castell yng nghanol y ddinas"),
       ("In 1786 houses and workshops crowded round the castle, with its arcaded parapet high on the wall. The houses have gone, and the castle now stands open in the heart of the city.",
        "Yn 1786 roedd tai a gweithdai’n gwasgu o gwmpas y castell, gyda rhes o fwâu’n uchel ar ei fur. Mae’r tai wedi mynd, ac mae’r castell bellach yn sefyll yn agored yng nghanol y ddinas."),
       1.5111, link="town-swansea.html"),
    _p("carew", "carewcross", "castles", "Carew Castle", "Castell Caeriw",
       _old("Carew castle May 1 1820 (1133191).jpg", "Charles Norris, engraved by Daniel Havell", "CC0", CC0, ("1820", "1820"),
            "the castle across the mill pond", "y castell dros y pwll melin"),
       ("Carew Castle across Mill Pond.JPG", "M Packwood Ace", "CC BY-SA 3.0", BYSA3,
        "the castle across the mill pond", "y castell dros y pwll melin"),
       ("Sir Rhys ap Thomas, Henry Tudor’s great Welsh ally, made Carew his home and held a famous tournament here in 1507. Two hundred years after this print, the castle still looks into the same still water.",
        "Gwnaeth Syr Rhys ap Thomas, cynghreiriad mawr Cymreig Harri Tudur, Gaeriw yn gartref iddo, a chynhaliodd dwrnamaint enwog yma yn 1507. Ddau gan mlynedd ar ôl y print hwn, mae’r castell yn dal i edrych i’r un dŵr llonydd."),
       1.7694),
    _p("powis", "powis", "castles", "Powis Castle", "Castell Powys",
       _old("Powis Castle, Montgomeryshire (1131074).jpg", "Richard Bernard Godfrey", "CC0", CC0, ("1775", "1775"),
            "the castle on its rock", "y castell ar ei graig"),
       ("Powis Castle, terraces and grounds - geograph.org.uk - 6681771.jpg", "Julian Paren", "CC BY-SA 2.0", BYSA2,
        "the red castle above its garden terraces", "y castell coch uwchben terasau’r ardd"),
       ("Powis began as the stronghold of the rulers of Powys. In 1775 it stood on bare rock; today the garden terraces below it, first laid out around 1700, are hung with great yews and flowers.",
        "Dechreuodd Castell Powys fel cadarnle rheolwyr Powys. Yn 1775 safai ar graig foel; heddiw mae terasau’r ardd oddi tano, a osodwyd gyntaf tua 1700, yn llawn ywen fawr a blodau."),
       1.4768),
    _p("penrhyn", "penrhyn", "castles", "Penrhyn Castle", "Castell Penrhyn",
       _old("Penrhyn Castle, Bangor, Wales-LCCN2001703418.jpg", PC, "Public domain", PD, C1895,
            "the keep above the trees of the park", "y gorthwr uwchben coed y parc"),
       ("The Keep at Penrhyn Castle - geograph.org.uk - 8382278.jpg", "TCExplorer", "CC BY-SA 2.0", BYSA2,
        "the keep from the park", "y gorthwr o’r parc"),
       ("Penrhyn is not a medieval castle at all: Thomas Hopper built it between 1820 and 1837 on the site of the old house of the Penrhyn family. It has belonged to the National Trust since 1951.",
        "Nid castell canoloesol yw Penrhyn o gwbl: Thomas Hopper a’i cododd rhwng 1820 a 1837 ar safle hen dŷ teulu’r Penrhyn. Mae’n eiddo i’r Ymddiriedolaeth Genedlaethol ers 1951."),
       1.3687),
    _p("tintern", "tintern", "churches", "Tintern Abbey", "Abaty Tyndyrn",
       _old("Tintern Abbey. S.W. I. LCCN2017659756.jpg", LOC, "Public domain", PD, C1890,
            "the abbey church from the south-west", "eglwys yr abaty o’r de-orllewin"),
       ("Tintern Abbey and Courtyard.jpg", "Saffron Blaze", "CC BY-SA 3.0", BYSA3,
        "the abbey church and the cloister floors", "eglwys yr abaty a lloriau’r clas"),
       ("The Crown bought Tintern in 1901 and took the ivy off its walls. The grass in front was dug away to show the floors of the monks’ buildings, laid out beside the church the Cistercians began in 1131.",
        "Prynodd y Goron Dyndyrn yn 1901 a thynnu’r eiddew oddi ar ei furiau. Codwyd y glaswellt o’i flaen i ddangos lloriau adeiladau’r mynachod, wrth yr eglwys a ddechreuodd y Sistersiaid yn 1131."),
       1.3488),
    _p("tintern2", "tintern", "churches", "Tintern Abbey from the Wye", "Abaty Tyndyrn o afon Gwy",
       _old("Abbey from the ferry, Tintern, England-LCCN2002708164.jpg", PC, "Public domain", PD, C1895,
            "the abbey from the ferry across the Wye", "yr abaty o’r fferi ar draws Gwy"),
       ("Tintern Abbey and River Wye 2004-07-25.jpg", "Chris McKenna", "CC BY-SA 4.0", BYSA4,
        "the abbey above the Wye", "yr abaty uwchben Gwy"),
       ("A ferry once took visitors over the Wye to the abbey. The ferry has gone and the trees have grown, but the old church still rises above the river on the Welsh bank.",
        "Ar un adeg roedd fferi’n cludo ymwelwyr dros Wy i’r abaty. Mae’r fferi wedi mynd a’r coed wedi tyfu, ond mae’r hen eglwys yn dal i godi uwchben yr afon ar lan Cymru."),
       1.4101),
    _p("llandaf", "llandaf", "churches", "Llandaff Cathedral", "Eglwys Gadeiriol Llandaf",
       _old("The N. W. view of the church & palace of Llandaffe in the county of Glamorgan (1132826).jpg", BUCK, "CC0", CC0, ("1741", "1741"),
            "the north-west view of the cathedral", "golwg o’r gogledd-orllewin ar yr eglwys gadeiriol"),
       ("Llandaff Cathedral (8061939916).jpg", "Peter Broster", "CC BY 2.0", BY2,
        "the cathedral from the north", "yr eglwys gadeiriol o’r gogledd"),
       ("When the Bucks drew Llandaff in 1741 its west end was a roofless ruin. It was rebuilt in the 1840s to 1860s, when John Prichard of Llandaff gave it a new spire, and mended again after a bomb fell on it in 1941.",
        "Pan dynnodd y brodyr Buck lun Llandaf yn 1741 roedd ei phen gorllewinol yn adfail heb do. Fe’i hailgodwyd rhwng y 1840au a’r 1860au, pan roddodd John Prichard o Landaf feindwr newydd iddi, a’i thrwsio eto wedi i fom ddisgyn arni yn 1941."),
       2.2000),
    _p("stdavids2", "stdavids", "churches", "St Davids Cathedral", "Eglwys Gadeiriol Tyddewi",
       _old("The south east view of St. David's Church & Palace - in the county of Pembroke- April 5th 1740 (1132350).jpg", BUCK, "CC0", CC0, ("1740", "1740"),
            "the cathedral and the Bishop’s Palace from the south-east", "yr eglwys gadeiriol a Llys yr Esgob o’r de-ddwyrain"),
       ("St David's Cathedral and Bishop's Palace from the south-east - geograph.org.uk - 2824026.jpg", "Christopher Hilton", "CC BY-SA 2.0", BYSA2,
        "the cathedral and the palace from the south-east", "yr eglwys gadeiriol a’r llys o’r de-ddwyrain"),
       ("Dewi Sant’s church in its hollow by the sea, drawn on 5 April 1740. The cathedral was restored by George Gilbert Scott from the 1860s, and the great Bishop’s Palace beside it is kept today by Cadw.",
        "Eglwys Dewi Sant yn ei phant ger y môr, wedi’i darlunio ar 5 Ebrill 1740. Adferwyd yr eglwys gadeiriol gan George Gilbert Scott o’r 1860au ymlaen, ac mae Llys yr Esgob mawr wrth ei hochr yng ngofal Cadw heddiw."),
       2.4000),
    _p("neathabbey", "neathabbey", "churches", "Neath Abbey", "Abaty Nedd",
       _old("Neath Abbey, Glamorganshire (1132733).jpg", "John Preston Neale, engraved by William Raymond Smith", "CC0", CC0, ("1813", "1813"),
            "the ruins of the abbey", "adfeilion yr abaty"),
       ("Neath Abbey - 49875049267.jpg", "hugh llewelyn", "CC BY-SA 2.0", BYSA2,
        "the ruins on their lawns", "yr adfeilion ar eu lawntiau"),
       ("Founded in 1130, Neath was one of the richest abbeys in Wales, and its poets praised it as a palace. In 1813 its ruins were overgrown and heaped with fallen stone; today they stand cleared on open lawns.",
        "Sefydlwyd Abaty Nedd yn 1130, ac roedd yn un o abatai cyfoethocaf Cymru; canodd y beirdd ei glod fel plas. Yn 1813 roedd yr adfeilion yn wyllt ac yn llawn cerrig wedi cwympo; heddiw maent yn sefyll yn glir ar lawntiau agored."),
       1.4859),
    _p("llanthony", "llanthony", "churches", "Llanthony Priory", "Priordy Llanddewi Nant Hodni",
       _old("Llanthony Abbey, Monmouthshire (1130057).jpg", "Unknown artist", "CC0", CC0, ("About 1835", "Tua 1835"),
            "cattle grazing in the ruined priory", "gwartheg yn pori yn adfail y priordy"),
       ("Llanthony Priory - geograph.org.uk - 2031203.jpg", "Philip Pankhurst", "CC BY-SA 2.0", BYSA2,
        "the arches of the nave", "bwâu corff yr eglwys"),
       ("Welsh tradition holds that Dewi Sant had a cell in this valley, which gives Llanddewi Nant Hodni its name. In the 1830s cattle grazed in the nave; today it is a lawn, and part of the priory is a small inn.",
        "Yn ôl traddodiad Cymru roedd gan Ddewi Sant gell yn y cwm hwn, a dyna sy’n rhoi ei enw i Landdewi Nant Hodni. Yn y 1830au roedd gwartheg yn pori yng nghorff yr eglwys; lawnt sydd yno heddiw, ac mae rhan o’r priordy yn dafarn fach."),
       1.5949),
    _p("menai", "menai", "towns", "Menai Suspension Bridge", "Pont Grog y Borth",
       _old("Menai Straits Suspension Bridge LCCN2017650157.jpg", LOC, "Public domain", PD, C1890,
            "the bridge from the Anglesey shore", "y bont o lan Môn"),
       ("Menai Suspension Bridge - geograph.org.uk - 5483242.jpg", "Stephen McKay", "CC BY-SA 2.0", BYSA2,
        "the bridge over the Menai Strait", "y bont dros Afon Menai"),
       ("Thomas Telford’s bridge of 1826 was the first great suspension bridge in the world. Its iron chains were changed for steel ones in 1938 to 1940, but the stone towers and the line of the deck are just as he made them.",
        "Pont Thomas Telford o 1826 oedd y bont grog fawr gyntaf yn y byd. Newidiwyd ei chadwyni haearn am rai dur rhwng 1938 a 1940, ond mae’r tyrau carreg a llinell y ffordd yn union fel y gwnaeth ef hwy."),
       1.3605),
    _p("pontcysyllte", "pontcysyllte", "towns", "Pontcysyllte Aqueduct", "Traphont Pontcysyllte",
       _old("Pontycysylltau Aqueduct, Llangollen, Wales-LCCN2001703515.jpg", PC, "Public domain", PD, C1895,
            "the aqueduct high above the Dee", "y draphont yn uchel uwchben Dyfrdwy"),
       ("Pontcysyllte aqueduct and River Dee - 52517387748.jpg", "kitmasterbloke", "CC BY 2.0", BY2,
        "the aqueduct above the wooded gorge", "y draphont uwchben y ceunant coediog"),
       ("Telford and Jessop’s aqueduct of 1805 still carries the canal in its iron trough 38 metres above the Dee. The trees of the gorge have grown thick since the 1890s, and since 2009 it has been a World Heritage Site.",
        "Mae traphont Telford a Jessop o 1805 yn dal i gario’r gamlas yn ei chafn haearn 38 metr uwchben Dyfrdwy. Mae coed y ceunant wedi tewhau ers y 1890au, ac ers 2009 mae’n Safle Treftadaeth y Byd."),
       1.4194),
    _p("llangollen", "llangollen", "towns", "Llangollen and the Dee", "Llangollen a Dyfrdwy",
       _old("General view, Llangollen, Wales-LCCN2001703511.jpg", PC, "Public domain", PD, C1895,
            "a fisherman with his coracle on the Dee", "pysgotwr gyda’i gwrwgl ar afon Dyfrdwy"),
       ("The River Dee at Llangollen, Denbighshire - geograph.org.uk - 5156529.jpg", "Roger Kidd", "CC BY-SA 2.0", BYSA2,
        "the Dee and the old bridge", "Dyfrdwy a’r hen bont"),
       ("In the 1890s a fisherman still carried his coracle, the little round boat of the Britons, on his back to the river. The old stone bridge, counted among the Seven Wonders of Wales, still carries the road into the town.",
        "Yn y 1890au roedd pysgotwr yn dal i gario’i gwrwgl, cwch bach crwn y Brythoniaid, ar ei gefn i’r afon. Mae’r hen bont garreg, un o Saith Rhyfeddod Cymru, yn dal i gario’r ffordd i’r dref."),
       1.3432),
    _p("tenby2", None, "towns", "Tenby", "Dinbych-y-pysgod",
       _old("Tenby, Wales-LCCN2001703554.jpg", PC, "Public domain", PD, C1895,
            "the harbour and the town on its rock", "yr harbwr a’r dref ar ei chraig"),
       ("Tenby Harbour - geograph.org.uk - 3983172.jpg", "Dylan Moore", "CC BY-SA 2.0", BYSA2,
        "the harbour and North Beach", "yr harbwr a’r Traeth Gogleddol"),
       ("Tenby was already a favourite seaside town in the 1890s. The harbour, the beach and the houses along the cliff top are much the same today, painted now in bright colours.",
        "Roedd Dinbych-y-pysgod eisoes yn hoff dref glan môr yn y 1890au. Mae’r harbwr, y traeth a’r tai ar ben y clogwyn yn debyg iawn heddiw, wedi’u peintio bellach mewn lliwiau llachar."),
       1.3657, link="town-tenby.html"),
    _p("betws", None, "towns", "Pont-y-pair, Betws-y-Coed", "Pont-y-pair, Betws-y-coed",
       _old("Roman bridge II, Bettws-y-Coed (i.e. Betws), Wales-LCCN2001703444.jpg", PC, "Public domain", PD, C1895,
            "the bridge over the Llugwy", "y bont dros afon Llugwy"),
       ("Pont y Pair Bridge, Betws-y-Coed - geograph.org.uk - 2412602.jpg", "Peter S", "CC BY-SA 2.0", BYSA2,
        "the bridge and the falls below it", "y bont a’r rhaeadr oddi tani"),
       ("The 1890s print called it the Roman bridge, but Pont-y-pair, the bridge of the cauldron, was built in the 1400s. It still carries the road over the rocks of the Llugwy.",
        "Galwodd print y 1890au hi’n bont Rufeinig, ond codwyd Pont-y-pair yn y 1400au. Mae’n dal i gario’r ffordd dros greigiau afon Llugwy."),
       1.3585, link="town-betws-y-coed.html"),
    _p("beddgelert", None, "towns", "Beddgelert", "Beddgelert",
       _old("Llewellyn Hotel, Beddgelert, Wales-LCCN2001703429.jpg", PC, "Public domain", PD, C1895,
            "the Prince Llewelyn inn by the bridge", "tafarn y Tywysog Llywelyn wrth y bont"),
       ("The Prince Llewelyn Hotel, Beddgelert - geograph.org.uk - 7588144.jpg", "Bill Harrison", "CC BY-SA 2.0", BYSA2,
        "the inn by the bridge today", "y dafarn wrth y bont heddiw"),
       ("The inn by the bridge over the Colwyn is named for Llywelyn ab Iorwerth, whose faithful hound Gelert gave the village its name in Welsh tradition. It has grown since the 1890s, but the bridge and the river are unchanged.",
        "Mae’r dafarn wrth y bont dros afon Colwyn wedi’i henwi ar ôl Llywelyn ab Iorwerth, y rhoddodd ei gi ffyddlon Gelert ei enw i’r pentref yn ôl traddodiad Cymru. Mae wedi tyfu ers y 1890au, ond mae’r bont a’r afon heb newid."),
       1.3615, link="legend-gelert.html"),
    _p("ybala", "ybala", "towns", "Bala and Llyn Tegid", "Y Bala a Llyn Tegid",
       _old("Town and lake, Bala, Wales-LCCN2001703413.jpg", PC, "Public domain", PD, C1895,
            "the town and the lake", "y dref a’r llyn"),
       ("Overlooking Lake Bala and Bala town - geograph.org.uk - 3037162.jpg", "Peter Morgan", "CC BY-SA 2.0", BYSA2,
        "Llyn Tegid from the hill", "Llyn Tegid o’r bryn"),
       ("Llyn Tegid is the largest natural lake in Wales. The fields of the 1890s have given way to woods, but the lake and the hills of Penllyn beyond look just the same.",
        "Llyn Tegid yw’r llyn naturiol mwyaf yng Nghymru. Mae coed wedi tyfu lle bu caeau’r 1890au, ond mae’r llyn a bryniau Penllyn y tu hwnt yn edrych yn union yr un fath."),
       1.3736),
]

BY_ID = {}
BY_PLACE = {}
BY_PAGE = {}  # a town (or other) page that shows a pair without being its place page: link -> pairs


def _index():
    BY_ID.clear()
    BY_PLACE.clear()
    BY_PAGE.clear()
    for p in PAIRS:
        BY_ID[p["id"]] = p
        if p.get("place"):
            BY_PLACE.setdefault(p["place"], []).append(p)
        elif (p.get("link") or "").startswith("town-"):
            BY_PAGE.setdefault(p["link"], []).append(p)


_index()


def _bi(en, cy):
    return f'<span class="l-en" lang="en">{en}</span><span class="l-cy" lang="cy">{cy}</span>'


def _cred(f, by, lic, licu):
    lic_cy = lic.replace("Public domain", "Parth cyhoeddus")
    return (f'{_e(by)}, <a href="{_e(licu)}" target="_blank" rel="noopener license">{_bi(_e(lic), _e(lic_cy))}</a>, '
            f'<a href="{COMMONS}File:{_q(f.replace(" ", "_"), safe="")}" target="_blank" rel="noopener">Wikimedia Commons</a>')


def figure(p, small=False):
    """The slider for one pair. Without JavaScript the two pictures show side by side."""
    t, n = p["then"], p["now"]
    ar = p["ar"]
    w = 1200
    h = round(w / ar)
    sfx = "-s" if small else ""
    when_en, when_cy = t[4], t[5]
    alt_t = _e(f"{p['en']}, {when_en}: {t[6]}")
    alt_n = _e(f"{p['en']} today: {n[4]}")
    srcset = lambda kind: f'thennow/{p["id"]}-{kind}-s.webp 640w, thennow/{p["id"]}-{kind}.webp 1200w'
    sizes = "(max-width: 960px) 100vw, 60rem"
    img = lambda kind, alt: (f'<img src="thennow/{p["id"]}-{kind}{sfx}.webp" srcset="{srcset(kind)}" sizes="{sizes}" width="{w}" height="{h}" '
                             f'alt="{alt}" loading="lazy" decoding="async">')
    label = _e(f"{p['en']}: drag to compare {when_en} with today / Llusgwch i gymharu {when_cy} â heddiw")
    return (f'<figure class="thn" data-thn="{p["id"]}"><div class="thn-stage" style="--ar:{ar:.4f}">'
            + img("now", alt_n)
            + f'<div class="thn-then">{img("then", alt_t)}</div>'
            + f'<span class="thn-tag thn-tag-then">{_bi(_e(when_en), _e(when_cy))}</span><span class="thn-tag thn-tag-now">{_bi("Today", "Heddiw")}</span>'
            + '<span class="thn-handle" aria-hidden="true"></span>'
            + f'<input class="thn-range" type="range" min="0" max="100" step="any" value="50" aria-label="{label}"></div>'
            + f'<div class="thn-bar"><button type="button" data-thn-go="100">{_bi("Then", "Ddoe")}</button><button type="button" data-thn-go="50">{_bi("Half and half", "Hanner a hanner")}</button>'
            + f'<button type="button" data-thn-go="0">{_bi("Now", "Heddiw")}</button><span class="thn-hint">{_bi("Drag across the picture", "Llusgwch ar draws y llun")}</span></div>'
            + f'<figcaption><p class="thn-what">{_bi(p["what"][0], p["what"][1])}</p>'
            + f'<span class="thn-cr"><b>{_bi("Then", "Ddoe")}:</b> {_bi(_e(t[6]), _e(t[7]))} · {_cred(t[0], t[1], t[2], t[3])}</span>'
            + f'<span class="thn-cr"><b>{_bi("Now", "Heddiw")}:</b> {_bi(_e(n[4]), _e(n[5]))} · {_cred(n[0], n[1], n[2], n[3])}</span>'
            + "</figcaption></figure>")


def place_block(pid, page=None):
    """The Then and now section for a place page (or, with page, a town page), or "" when it has no pair."""
    ps = BY_PAGE.get(page) if page else BY_PLACE.get(pid)
    if not ps:
        return ""
    more = f'<p><a class="go" href="then-and-now.html">{_bi("More places then and now", "Rhagor o leoedd ddoe a heddiw")} →</a></p>'
    return "".join(figure(p) for p in ps) + more


def page_main(link_of):
    """The body of then-and-now.html (after the hero). link_of(pair) gives the page each title opens."""
    chips = (f'<button type="button" class="thn-chip on" data-cat="all" aria-pressed="true">{_bi("All", "Y cyfan")} <i>{len(PAIRS)}</i></button>'
             + "".join(f'<button type="button" class="thn-chip" data-cat="{c}" aria-pressed="false">{_bi(en, cy)} <i>{sum(1 for p in PAIRS if p["cat"] == c)}</i></button>'
                       for c, en, cy in CATS if any(p["cat"] == c for p in PAIRS)))
    cards = ""
    for p in PAIRS:
        href = link_of(p)
        name = _bi(_e(p["en"]), _e(p["cy"]))
        h = f'<a href="{href}">{name}</a>' if href else name
        cards += (f'<article class="thn-card" id="{p["id"]}" data-cat="{p["cat"]}"><h2>{h}</h2>'
                  f'<p class="thn-when">{_bi(_e(p["then"][4]) + " · today", _e(p["then"][5]) + " · heddiw")}</p>{figure(p)}</article>')
    return (f'<div class="thn-chips" role="toolbar" aria-label="Show / Dangos">{chips}</div><div class="thn-list">{cards}</div>')
