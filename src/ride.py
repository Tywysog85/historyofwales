"""Ride with Glyndŵr, 1400: a story in which you make the choices (ride-glyndwr.html).

You answer Owain Glyndŵr's call in September 1400 as an archer, a bard or a rider, and follow the rising to 1415.
Every scene is a real moment, and each one has a "What really happened" box that links to that event's own page.
Your choices change what you do and how you are remembered (your renown), never what happened: the history is the history.

build.py calls setup(globals()) once, then page(). The story itself runs in src/static/ride.js, which reads RIDE (below)
from the page. It saves your place on this device, and finishing the ride earns the "Glyndŵr's companion" badge.

To add a scene: add it to NODES with an id, and point a choice from an earlier scene at it ("to"). Each scene has:
  d     the date (en, cy)          p    the place (en, cy)         at   (lat, lon) for the map, or None to stay put
  y     the year, for the bar      t    ([English paragraphs], [Welsh paragraphs])
  r     a line for each role       f    (en, cy, [event page slugs]) for "What really happened"
  c     the choices: dict(t=(en, cy), to=next scene, add=renown, say=(en, cy) shown at the top of the next scene,
        set=role (first scene only), bonus={role: extra renown})
"""
import json

import data as D
import eventpages as EP

g = {}

ROLES = {
    "archer": ("Archer", "Saethydd", "➶"),
    "bard": ("Bard", "Bardd", "♪"),
    "rider": ("Rider", "Marchog", "♞"),
}

PLACES = {
    "glyn": (52.982, -3.385), "ruthin": (53.114, -3.311), "pool": (52.66, -3.15), "conwy": (53.280, -3.829),
    "hyddgen": (52.52, -3.78), "pilleth": (52.30, -3.07), "carm": (51.857, -4.31), "mach": (52.59, -3.85),
    "harlech": (52.860, -4.109), "milford": (51.71, -5.03), "woodbury": (52.25, -2.33), "pennal": (52.585, -3.92),
}

NODES = {
    "start": dict(
        d=("September 1400", "Medi 1400"), p=("Edeyrnion, in the valley of the Dee", "Edeirnion, yn nyffryn Dyfrdwy"), at="glyn", y=1400,
        t=(["Word is running along the valley of the Dee, from farm to farm and hall to hall. Owain ap Gruffudd, lord of Glyndyfrdwy and Cynllaith, "
            "of the line of the princes of Powys and Deheubarth, is calling his people to him.",
            "For a hundred years the Welsh have lived under hard laws in their own land. Now the lord of Ruthin, Reginald Grey, has taken Owain’s land, "
            "and, the story goes, kept back the king’s summons so that Owain would look disloyal. Owain has had enough. Who are you, who answers his call?"],
           ["Mae’r newydd yn rhedeg ar hyd dyffryn Dyfrdwy, o fferm i fferm ac o neuadd i neuadd. Mae Owain ap Gruffudd, arglwydd Glyndyfrdwy a Chynllaith, "
            "o linach tywysogion Powys a Deheubarth, yn galw ei bobl ato.",
            "Ers can mlynedd bu’r Cymry’n byw dan gyfreithiau caled yn eu gwlad eu hunain. Nawr mae arglwydd Rhuthun, Reginald Grey, wedi cymryd tir Owain, "
            "ac, yn ôl yr hanes, wedi cadw gwŷs y brenin yn ôl er mwyn i Owain ymddangos yn anffyddlon. Mae Owain wedi cael digon. Pwy ydych chi, sy’n ateb ei alwad?"]),
        c=[dict(t=("An archer from the hills, with a bow of yew", "Saethydd o’r bryniau, gyda bwa ywen"), set="archer", to="proclaim",
                say=("You string your bow and walk down the valley to Glyndyfrdwy.", "Rydych yn llinynnu eich bwa ac yn cerdded i lawr y dyffryn i Lyndyfrdwy.")),
           dict(t=("A bard, who keeps the old songs and prophecies", "Bardd, sy’n cadw’r hen ganeuon a’r daroganau"), set="bard", to="proclaim",
                say=("You take your harp, and your memory of the old prophecies, down to Glyndyfrdwy.", "Rydych yn mynd â’ch telyn, a’ch cof am yr hen ddaroganau, i lawr i Lyndyfrdwy.")),
           dict(t=("A rider, the fastest messenger in Edeyrnion", "Marchog, y negesydd cyflymaf yn Edeirnion"), set="rider", to="proclaim",
                say=("You saddle your horse. Owain will need someone to carry his word.", "Rydych yn cyfrwyo eich ceffyl. Bydd Owain angen rhywun i gludo ei air."))]),

    "proclaim": dict(
        d=("16 September 1400", "16 Medi 1400"), p=("Glyndyfrdwy", "Glyndyfrdwy"), at="glyn", y=1400.7,
        t=(["In the hall at Glyndyfrdwy, Owain stands before his family and friends: his eldest son Gruffudd, his brother Tudur, his wife Margaret’s brothers "
            "Gruffudd and Philip Hanmer, and the seer Crach Ffinnant. One by one they kneel, and they proclaim him Prince of Wales.",
            "Outside, the men of the valley cheer. There is a Prince of Wales of Welsh blood again, for the first time since Llywelyn, the last prince, fell in 1282."],
           ["Yn y neuadd yng Nglyndyfrdwy, mae Owain yn sefyll o flaen ei deulu a’i gyfeillion: ei fab hynaf Gruffudd, ei frawd Tudur, brodyr ei wraig Marged, "
            "Gruffudd a Philip Hanmer, a’r daroganwr Crach Ffinnant. Fesul un maen nhw’n penlinio, ac yn ei gyhoeddi’n Dywysog Cymru.",
            "Y tu allan, mae dynion y dyffryn yn bloeddio. Mae Tywysog Cymru o waed Cymreig unwaith eto, am y tro cyntaf ers i Lywelyn, y tywysog olaf, syrthio yn 1282."]),
        r=dict(archer=("You stand at the back with the other bowmen, and your heart is pounding.", "Rydych yn sefyll yn y cefn gyda’r saethwyr eraill, a’ch calon yn curo."),
               bard=("Crach Ffinnant catches your eye. The prophecies spoke of a son of destiny, y Mab Darogan. Is this the man?",
                     "Mae Crach Ffinnant yn dal eich llygad. Soniai’r daroganau am y Mab Darogan. Ai hwn yw’r dyn?"),
               rider=("Before the cheering has stopped, Owain’s steward is looking for a fast horse to carry the news.",
                      "Cyn i’r bloeddio ddistewi, mae stiward Owain yn chwilio am geffyl cyflym i gludo’r newydd.")),
        f=("Owain Glyndŵr was proclaimed Prince of Wales at Glyndyfrdwy on 16 September 1400. The day is kept today as Owain Glyndŵr Day.",
           "Cyhoeddwyd Owain Glyndŵr yn Dywysog Cymru yng Nglyndyfrdwy ar 16 Medi 1400. Cedwir y dydd heddiw fel Diwrnod Owain Glyndŵr.", ["glyndwrs-rising"]),
        c=[dict(t=("Kneel and swear yourself to Owain", "Penlinio a thyngu llw i Owain"), to="ruthin", add=1,
                say=("Owain takes your hand. “Then come with me,” he says.", "Mae Owain yn cymryd eich llaw. “Yna dewch gyda mi,” meddai.")),
           dict(t=("Ask Owain why he is doing this", "Gofyn i Owain pam mae’n gwneud hyn"), to="why", add=1)]),

    "why": dict(
        d=("16 September 1400", "16 Medi 1400"), p=("Glyndyfrdwy", "Glyndyfrdwy"), at="glyn", y=1400.7,
        t=(["Owain looks at you for a long moment, then answers.",
            "“Grey has taken my land, and when I asked Parliament for justice, the lords laughed. ‘What do we care for barefoot Welsh dogs?’ they said. "
            "Our people may not hold office in the king’s towns in Wales, nor own a house inside their walls. I am of the blood of the princes. I will not see Wales treated so.”"],
           ["Mae Owain yn edrych arnoch am amser hir, yna’n ateb.",
            "“Mae Grey wedi cymryd fy nhir, a phan ofynnais i’r Senedd am gyfiawnder, chwerthin wnaeth yr arglwyddi. ‘Beth yw’r ots gennym am gŵn Cymreig troednoeth?’ medden nhw. "
            "Ni chaiff ein pobl ddal swydd yn nhrefi’r brenin yng Nghymru, na bod yn berchen ar dŷ o fewn eu muriau. Rwyf o waed y tywysogion. Ni welaf Gymru’n cael ei thrin felly.”"]),
        f=("Owain had studied law in London and served the king in war. He turned to arms only after the courts and Parliament gave him no justice.",
           "Roedd Owain wedi astudio’r gyfraith yn Llundain ac wedi gwasanaethu’r brenin mewn rhyfel. Trodd at y cleddyf dim ond wedi i’r llysoedd a’r Senedd wrthod cyfiawnder iddo.",
           ["glyndwrs-rising"]),
        c=[dict(t=("“Then I am with you.”", "“Yna rydw i gyda chi.”"), to="ruthin", add=1,
                say=("Owain nods. “Good. We ride at dawn.”", "Mae Owain yn nodio. “Da. Rydym yn cychwyn gyda’r wawr.”"))]),

    "ruthin": dict(
        d=("18 September 1400", "18 Medi 1400"), p=("Ruthin", "Rhuthun"), at="ruthin", y=1400.72,
        t=(["Two days later, at dawn, Owain’s men ride into Ruthin, the town of Reginald Grey, while the September fair fills the streets. "
            "By evening the town is theirs, and Grey’s men are shut up behind the castle walls.",
            "Then the host sweeps on, faster than any letter can warn of it: Denbigh, Rhuddlan, Flint, Hawarden, Holt, Oswestry. "
            "In a single week the whole of the north east knows the name of Owain Glyndŵr."],
           ["Ddeuddydd yn ddiweddarach, gyda’r wawr, mae gwŷr Owain yn marchogaeth i mewn i Ruthun, tref Reginald Grey, tra bo ffair mis Medi’n llenwi’r strydoedd. "
            "Erbyn yr hwyr y dref yw eu heiddo nhw, ac mae gwŷr Grey wedi’u cau y tu ôl i furiau’r castell.",
            "Yna mae’r fyddin yn ysgubo ymlaen, yn gyflymach nag y gall unrhyw lythyr rybuddio amdani: Dinbych, Rhuddlan, y Fflint, Penarlâg, Holt, Croesoswallt. "
            "Mewn un wythnos mae’r gogledd-ddwyrain i gyd yn gwybod enw Owain Glyndŵr."]),
        r=dict(archer=("Your arrows keep the castle gate shut while the host passes through the town.", "Mae eich saethau’n cadw porth y castell ar gau tra bo’r fyddin yn mynd drwy’r dref."),
               bard=("That night by the fire, you make the first verses of a new song.", "Y noson honno wrth y tân, rydych yn llunio penillion cyntaf cân newydd."),
               rider=("You ride ahead of the host, telling every Welsh township that Owain is coming.", "Rydych yn marchogaeth o flaen y fyddin, yn dweud wrth bob trefgordd Gymreig fod Owain yn dod.")),
        f=("Ruthin was attacked on 18 September 1400, two days after the proclamation. In the week that followed Owain’s men struck the English-held towns of the north east, from Denbigh to Oswestry.",
           "Ymosodwyd ar Ruthun ar 18 Medi 1400, ddeuddydd wedi’r cyhoeddi. Yn yr wythnos wedyn trawodd gwŷr Owain drefi’r gogledd-ddwyrain a oedd yn nwylo’r Saeson, o Ddinbych i Groesoswallt.",
           ["glyndwrs-rising"]),
        c=[dict(t=("Ride on south with the host, towards the Severn", "Mynd ymlaen tua’r de gyda’r fyddin, at afon Hafren"), to="pool", add=1)]),

    "pool": dict(
        d=("24 September 1400", "24 Medi 1400"), p=("On the Severn, near Welshpool", "Ar lan Hafren, ger y Trallwng"), at="pool", y=1400.73,
        t=(["By the River Severn the host meets an army raised in haste from Shropshire and Staffordshire. Owain’s men are tired from a week of riding; the enemy is fresh.",
            "But Owain learned war in the king’s own armies. He knows that a rising is not won in a week, and that the hills of Wales are his greatest friend."],
           ["Ar lan afon Hafren mae’r fyddin yn cwrdd â llu a godwyd ar frys o swyddi Amwythig a Stafford. Mae gwŷr Owain wedi blino ar ôl wythnos o farchogaeth; mae’r gelyn yn ffres.",
            "Ond dysgodd Owain grefft rhyfel ym myddinoedd y brenin ei hun. Mae’n gwybod nad mewn wythnos yr enillir gwrthryfel, ac mai bryniau Cymru yw ei ffrind gorau."]),
        f=("Near Welshpool the rising met its first hard fight, and Owain took his men into the hills. King Henry IV marched through north Wales that autumn and found no army to fight.",
           "Ger y Trallwng cafodd y gwrthryfel ei frwydr galed gyntaf, ac aeth Owain â’i wŷr i’r bryniau. Martsiodd y Brenin Harri IV drwy ogledd Cymru’r hydref hwnnw heb gael byddin i’w hymladd.", []),
        c=[dict(t=("Hold the ford while the others get away", "Dal y rhyd tra bo’r lleill yn dianc"), to="conwy", add=2, bonus=dict(archer=1),
                say=("You hold the ford until the last of Owain’s men are across, then slip away into the dusk. All winter the king’s men hunt for Owain, and find no one.",
                     "Rydych yn dal y rhyd nes bod yr olaf o wŷr Owain drosodd, yna’n diflannu i’r cyfnos. Drwy’r gaeaf mae gwŷr y brenin yn chwilio am Owain, heb gael neb.")),
           dict(t=("Fall back into the hills, as Owain orders", "Cilio i’r bryniau, fel y mae Owain yn gorchymyn"), to="conwy", add=1,
                say=("The host melts into the hills. All winter the king’s men hunt for Owain, and find no one.",
                     "Mae’r fyddin yn diflannu i’r bryniau. Drwy’r gaeaf mae gwŷr y brenin yn chwilio am Owain, heb gael neb."))]),

    "conwy": dict(
        d=("Good Friday, 1 April 1401", "Dydd Gwener y Groglith, 1 Ebrill 1401"), p=("Conwy", "Conwy"), at="conwy", y=1401.25,
        t=(["Now, at Easter, Owain’s cousins strike. Rhys and Gwilym ap Tudur, of Penmynydd in Anglesey, have a plan.",
            "While the garrison of Conwy Castle is at church in the town for the Good Friday service, a carpenter comes to the castle gate, saying he has work to do. "
            "The gate opens. A moment later about forty men are inside, and one of the greatest castles King Edward ever built belongs to the Welsh."],
           ["Nawr, adeg y Pasg, mae cefndryd Owain yn taro. Mae gan Rhys a Gwilym ap Tudur, o Benmynydd ym Môn, gynllun.",
            "Tra bo garsiwn Castell Conwy yn yr eglwys yn y dref ar gyfer gwasanaeth Dydd Gwener y Groglith, daw saer at borth y castell, gan ddweud bod ganddo waith i’w wneud. "
            "Mae’r porth yn agor. Eiliad wedyn mae tua deugain o ddynion y tu mewn, ac mae un o’r cestyll mwyaf a gododd y Brenin Edward erioed yn eiddo i’r Cymry."]),
        r=dict(archer=("You wait in the trees with the other bowmen, ready to cover the gate.", "Rydych yn aros yn y coed gyda’r saethwyr eraill, yn barod i amddiffyn y porth."),
               bard=("You will tell this story for the rest of your life.", "Byddwch yn adrodd yr hanes hwn am weddill eich oes."),
               rider=("It was you who brought word from Owain that the time had come.", "Chi ddaeth â’r gair gan Owain fod yr amser wedi dod.")),
        f=("Rhys and Gwilym ap Tudur took Conwy Castle on Good Friday 1401 and held it for some three months. Their family, the Tudors of Penmynydd, would one day give England its kings.",
           "Cipiodd Rhys a Gwilym ap Tudur Gastell Conwy ar Ddydd Gwener y Groglith 1401 a’i ddal am ryw dri mis. Byddai eu teulu, Tuduriaid Penmynydd, un dydd yn rhoi ei brenhinoedd i Loegr.",
           ["conwy-taken-on-good-friday"]),
        c=[dict(t=("Go in behind the carpenter", "Mynd i mewn y tu ôl i’r saer"), to="hyddgen", add=2, bonus=dict(rider=1),
                say=("You are through the gate before the church bells in the town stop ringing.", "Rydych drwy’r porth cyn i glychau’r eglwys yn y dref beidio â chanu.")),
           dict(t=("Keep watch on the road from the town", "Cadw golwg ar y ffordd o’r dref"), to="hyddgen", add=1,
                say=("When the garrison comes running back from church, they find the gates shut against them.", "Pan ddaw’r garsiwn yn rhedeg yn ôl o’r eglwys, maen nhw’n cael y pyrth ar gau yn eu herbyn."))]),

    "hyddgen": dict(
        d=("Summer 1401", "Haf 1401"), p=("Mynydd Hyddgen, on Pumlumon", "Mynydd Hyddgen, ar Bumlumon"), at="hyddgen", y=1401.5,
        t=(["High on the bare slopes of Pumlumon, Owain has only a few hundred men. Coming up the valley towards them are some fifteen hundred: "
            "Flemings from Pembroke and English from the south, sent to finish the rising once and for all.",
            "They have Owain surrounded. His captains look to him. Owain draws his sword."],
           ["Yn uchel ar lethrau noeth Pumlumon, dim ond ychydig gannoedd o ddynion sydd gan Owain. Yn dod i fyny’r cwm tuag atynt mae rhyw bymtheg cant: "
            "Ffleminiaid o Benfro a Saeson o’r de, wedi’u hanfon i roi diwedd ar y gwrthryfel unwaith ac am byth.",
            "Mae Owain wedi’i amgylchynu. Mae ei gapteiniaid yn edrych arno. Mae Owain yn tynnu ei gleddyf."]),
        r=dict(archer=("This is your hour. Every arrow you own is in your belt.", "Dyma eich awr chi. Mae pob saeth sydd gennych yn eich gwregys."),
               bard=("You remember the old poems of the few who stood against the many.", "Rydych yn cofio’r hen gerddi am yr ychydig a safodd yn erbyn y llawer."),
               rider=("Your horse is fresh and the slope is steep. A charge from here would be like a river in flood.", "Mae eich ceffyl yn ffres a’r llethr yn serth. Byddai rhuthr oddi yma fel afon yn gorlifo.")),
        f=("The battle of Hyddgen, on the slopes of Pumlumon in 1401, was Owain’s first great victory. Two white quartz stones there are still called Cerrig Cyfamod Glyndŵr, the stones of Glyndŵr’s covenant.",
           "Brwydr Hyddgen, ar lethrau Pumlumon yn 1401, oedd buddugoliaeth fawr gyntaf Owain. Gelwir dwy garreg cwarts wen yno hyd heddiw yn Gerrig Cyfamod Glyndŵr.",
           ["victory-at-hyddgen"]),
        c=[dict(t=("Charge down the mountain with Owain", "Rhuthro i lawr y mynydd gydag Owain"), to="rally", add=2, bonus=dict(rider=1),
                say=("Owain’s men come down the mountain like a storm. The great army breaks and runs for the valleys.",
                     "Daw gwŷr Owain i lawr y mynydd fel storm. Mae’r fyddin fawr yn torri ac yn ffoi am y cymoedd.")),
           dict(t=("Hold the high ground and loose arrows", "Dal y tir uchel a saethu"), to="rally", add=2, bonus=dict(archer=1),
                say=("Arrow after arrow falls among them. When Owain charges at last, the great army breaks and runs for the valleys.",
                     "Mae saeth ar ôl saeth yn disgyn yn eu plith. Pan mae Owain yn rhuthro o’r diwedd, mae’r fyddin fawr yn torri ac yn ffoi am y cymoedd."))]),

    "rally": dict(
        d=("Autumn 1401", "Hydref 1401"), p=("Owain’s camp in the hills", "Gwersyll Owain yn y bryniau"), at="hyddgen", y=1401.8,
        t=(["After Hyddgen the news runs through Wales like fire through dry heather. Welsh students leave Oxford and Cambridge to join Owain, "
            "and Welsh labourers in England put down their tools and walk home. Owain is no longer a lord with a quarrel. He is the hope of a nation.",
            "Now he looks beyond Wales. He has written to the King of Scots and to the lords of Ireland, and he needs someone to carry the letters."],
           ["Wedi Hyddgen mae’r newydd yn rhedeg drwy Gymru fel tân drwy rug sych. Mae myfyrwyr o Gymru’n gadael Rhydychen a Chaergrawnt i ymuno ag Owain, "
            "ac mae llafurwyr o Gymry yn Lloegr yn rhoi eu harfau gwaith i lawr ac yn cerdded adref. Nid arglwydd â chweryl yw Owain mwyach. Ef yw gobaith cenedl.",
            "Nawr mae’n edrych y tu hwnt i Gymru. Mae wedi ysgrifennu at Frenin yr Alban ac at arglwyddi Iwerddon, ac mae angen rhywun arno i gludo’r llythyrau."]),
        f=("After Hyddgen, Parliament heard that Welsh students had left Oxford and Cambridge, and Welsh workers had left England, to join Owain.",
           "Wedi Hyddgen, clywodd y Senedd fod myfyrwyr o Gymru wedi gadael Rhydychen a Chaergrawnt, a gweithwyr o Gymry wedi gadael Lloegr, i ymuno ag Owain.",
           ["victory-at-hyddgen"]),
        c=[dict(t=("Carry Owain’s letters north", "Cludo llythyrau Owain i’r gogledd"), to="letters", add=2, bonus=dict(rider=1)),
           dict(t=("Stay with the host in Wales", "Aros gyda’r fyddin yng Nghymru"), to="brynglas", add=1,
                say=("You spend the winter with Owain’s men in the hills. In April the news comes that Owain has captured Reginald Grey himself, near Ruthin.",
                     "Rydych yn treulio’r gaeaf gyda gwŷr Owain yn y bryniau. Ym mis Ebrill daw’r newydd fod Owain wedi dal Reginald Grey ei hun, ger Rhuthun."))]),

    "letters": dict(
        d=("Winter 1401", "Gaeaf 1401"), p=("On the road to Scotland", "Ar y ffordd i’r Alban"), at=None, y=1401.9,
        t=(["You carry letters sealed with Owain’s seal. The first is for Robert III, King of Scots. Owain writes to him as a cousin: both, he says, "
            "are descended from Brutus, the first crowned king of Britain, and the Scots and the Welsh stand together against a common foe.",
            "Another is for the lords of Ireland. Owain asks them to send help across the sea, for the old prophecy says the two peoples will help each other before the victory comes."],
           ["Rydych yn cludo llythyrau dan sêl Owain. Mae’r cyntaf i Robert III, Brenin yr Alban. Mae Owain yn ysgrifennu ato fel cefnder: mae’r ddau, meddai, "
            "yn ddisgynyddion i Brutus, brenin coronog cyntaf Prydain, ac mae’r Albanwyr a’r Cymry’n sefyll gyda’i gilydd yn erbyn gelyn cyffredin.",
            "Mae un arall i arglwyddi Iwerddon. Mae Owain yn gofyn iddynt anfon cymorth dros y môr, oherwydd mae’r hen ddarogan yn dweud y bydd y ddwy bobl yn helpu ei gilydd cyn i’r fuddugoliaeth ddod."]),
        f=("In 1401 Owain wrote to Robert III of Scotland, calling him cousin through their shared descent from Brutus, and to the lords of Ireland, asking for their help.",
           "Yn 1401 ysgrifennodd Owain at Robert III o’r Alban, gan ei alw’n gefnder drwy eu tras gyffredin o Brutus, ac at arglwyddi Iwerddon, yn gofyn am eu cymorth.",
           ["owain-writes-to-scotland-and-ireland"]),
        c=[dict(t=("Ride home in time for the summer", "Marchogaeth adref erbyn yr haf"), to="brynglas", add=1,
                say=("The roads are long, but by spring you are home. Wales has not stood still: in April Owain captured Reginald Grey himself, near Ruthin.",
                     "Mae’r ffyrdd yn hir, ond erbyn y gwanwyn rydych adref. Nid yw Cymru wedi aros yn llonydd: ym mis Ebrill daliodd Owain Reginald Grey ei hun, ger Rhuthun."))]),

    "brynglas": dict(
        d=("22 June 1402", "22 Mehefin 1402"), p=("Bryn Glas, above Pilleth", "Bryn Glas, uwchben Pyllalai"), at="pilleth", y=1402.47,
        t=(["Grey’s family must now pay ten thousand marks to get him back. And now the men of Herefordshire are marching into Maelienydd "
            "under Sir Edmund Mortimer, uncle of the young Earl of March.",
            "Owain’s captain, Rhys Gethin, has men on the hill of Bryn Glas, and more hidden in the valley behind. "
            "Many of Mortimer’s own archers are Welshmen from Maelienydd. Whose side will they choose?"],
           ["Rhaid i deulu Grey dalu deng mil o farciau i’w gael yn ôl. A nawr mae gwŷr swydd Henffordd yn martsio i mewn i Faelienydd "
            "dan Syr Edmund Mortimer, ewythr Iarll ifanc y Mers.",
            "Mae gan gapten Owain, Rhys Gethin, wŷr ar fryn Bryn Glas, a mwy yn guddiedig yn y cwm y tu ôl. "
            "Cymry o Faelienydd yw llawer o saethwyr Mortimer ei hun. Ochr pwy fyddan nhw’n ei dewis?"]),
        r=dict(archer=("You know some of the archers in Mortimer’s ranks. You grew up with men like them.", "Rydych yn adnabod rhai o’r saethwyr yn rhengoedd Mortimer. Cawsoch eich magu gyda dynion fel nhw."),
               bard=("You call a verse across the valley, in Welsh, so that only the Welsh will understand it.", "Rydych yn galw pennill ar draws y cwm, yn Gymraeg, fel mai dim ond y Cymry fydd yn ei ddeall."),
               rider=("You ride between Rhys Gethin and the hidden men, carrying the signal.", "Rydych yn marchogaeth rhwng Rhys Gethin a’r gwŷr cudd, yn cludo’r arwydd.")),
        f=("At Bryn Glas, near Pilleth, on 22 June 1402, Owain’s army won a great victory and captured Edmund Mortimer. Mortimer later joined Owain and married his daughter Catrin.",
           "Ym Mryn Glas, ger Pyllalai, ar 22 Mehefin 1402, enillodd byddin Owain fuddugoliaeth fawr a dal Edmund Mortimer. Yn ddiweddarach ymunodd Mortimer ag Owain a phriodi ei ferch Catrin.",
           ["battle-of-bryn-glas"]),
        c=[dict(t=("Wait hidden in the valley for the signal", "Aros yn gudd yn y cwm am yr arwydd"), to="storms", add=2,
                say=("Mortimer’s army climbs the hill. Then the hidden men rise behind it, and the Welsh archers in Mortimer’s ranks turn their bows. The day is Owain’s, and Mortimer himself is taken.",
                     "Mae byddin Mortimer yn dringo’r bryn. Yna mae’r gwŷr cudd yn codi y tu ôl iddi, ac mae’r saethwyr Cymreig yn rhengoedd Mortimer yn troi eu bwâu. Owain biau’r dydd, a deliwyd Mortimer ei hun.")),
           dict(t=("Stand on the crest in plain view", "Sefyll ar y grib yng ngolwg pawb"), to="storms", add=2, bonus=dict(archer=1),
                say=("Mortimer’s army comes straight up the hill at you. Then the Welsh archers in his own ranks turn their bows, and the hidden men rise behind him. The day is Owain’s, and Mortimer himself is taken.",
                     "Daw byddin Mortimer yn syth i fyny’r bryn atoch. Yna mae’r saethwyr Cymreig yn ei rengoedd ei hun yn troi eu bwâu, ac mae’r gwŷr cudd yn codi y tu ôl iddo. Owain biau’r dydd, a deliwyd Mortimer ei hun."))]),

    "storms": dict(
        d=("September 1402", "Medi 1402"), p=("The mountains of Wales", "Mynyddoedd Cymru"), at=None, y=1402.7,
        t=(["King Henry is furious. He sends three great armies into Wales at once, from Chester, from Shrewsbury and from Hereford. "
            "Owain does not meet them. He takes his people into the mountains, and waits.",
            "Then the weather turns. Rain, hail and snow sweep the hills in early September. Rivers burst, tents are torn away, and the king’s own tent "
            "is blown down on top of him in the night. Within weeks all three armies have gone home with nothing."],
           ["Mae’r Brenin Harri’n gandryll. Mae’n anfon tair byddin fawr i Gymru ar yr un pryd, o Gaer, o’r Amwythig ac o Henffordd. "
            "Nid yw Owain yn eu cyfarfod. Mae’n mynd â’i bobl i’r mynyddoedd, ac yn aros.",
            "Yna mae’r tywydd yn troi. Mae glaw, cenllysg ac eira’n ysgubo’r bryniau ddechrau mis Medi. Mae afonydd yn gorlifo, pebyll yn cael eu rhwygo i ffwrdd, "
            "ac mae pabell y brenin ei hun yn cael ei chwythu i lawr ar ei ben yn y nos. O fewn wythnosau mae’r tair byddin wedi mynd adref heb ddim."]),
        r=dict(archer=("You shelter in a cave above the valley and watch the king’s camp drown.", "Rydych yn cysgodi mewn ogof uwchben y cwm ac yn gwylio gwersyll y brenin yn boddi."),
               bard=("The English soldiers whisper that Owain is a magician who commands the storm. You do nothing to tell them otherwise.",
                     "Mae milwyr Lloegr yn sibrwd mai dewin yw Owain sy’n rheoli’r storm. Nid ydych yn gwneud dim i’w darbwyllo fel arall."),
               rider=("You ride the high tracks no stranger knows, keeping Owain’s bands in touch with each other.", "Rydych yn marchogaeth y llwybrau uchel nad oes dieithryn yn eu hadnabod, gan gadw bandiau Owain mewn cysylltiad.")),
        f=("In September 1402 Henry IV’s three armies were driven out of Wales by terrible storms. English chroniclers wrote that Owain could raise the weather by magic, and two hundred years later Shakespeare had him say, “I can call spirits from the vasty deep.”",
           "Ym mis Medi 1402 gyrrwyd tair byddin Harri IV o Gymru gan stormydd ofnadwy. Ysgrifennodd croniclwyr Lloegr y gallai Owain godi’r tywydd drwy hud, a dau gan mlynedd yn ddiweddarach rhoddodd Shakespeare y geiriau yn ei enau: “I can call spirits from the vasty deep.”", []),
        c=[dict(t=("Let the weather fight for Wales", "Gadael i’r tywydd ymladd dros Gymru"), to="south", add=1,
                say=("The winter passes quietly in the hills. In the spring Owain gathers the largest host Wales has seen in a hundred years.",
                     "Mae’r gaeaf yn mynd heibio’n dawel yn y bryniau. Yn y gwanwyn mae Owain yn casglu’r fyddin fwyaf a welodd Cymru ers can mlynedd.")),
           dict(t=("Make a song of Owain and the storm", "Llunio cân am Owain a’r storm"), to="south", add=1, bonus=dict(bard=2),
                say=("The song travels faster than any army. By Christmas they are singing it in halls from Môn to Gwent.",
                     "Mae’r gân yn teithio’n gyflymach nag unrhyw fyddin. Erbyn y Nadolig maen nhw’n ei chanu mewn neuaddau o Fôn i Went."))]),

    "south": dict(
        d=("July 1403", "Gorffennaf 1403"), p=("The Tywi valley and Carmarthen", "Dyffryn Tywi a Chaerfyrddin"), at="carm", y=1403.5,
        t=(["Owain rides south with a great host. In the valley of the Tywi, the old heartland of Deheubarth and of his mother’s people, the country rises to meet him. "
            "Llandovery opens its gates. Llandeilo welcomes him. The castles of Dryslwyn and Newcastle Emlyn are handed over to him.",
            "Then Owain comes to Carmarthen, the greatest town of the south west, and within days it is his. Wales from the Dee to the Tywi now looks to one prince."],
           ["Mae Owain yn marchogaeth tua’r de gyda byddin fawr. Yn nyffryn Tywi, hen galon Deheubarth a chartref teulu ei fam, mae’r wlad yn codi i’w gyfarfod. "
            "Mae Llanymddyfri’n agor ei phyrth. Mae Llandeilo’n ei groesawu. Mae cestyll Dryslwyn a Chastellnewydd Emlyn yn cael eu rhoi yn ei ddwylo.",
            "Yna daw Owain i Gaerfyrddin, tref fwyaf y de-orllewin, ac o fewn dyddiau mae’n eiddo iddo. Mae Cymru o Ddyfrdwy i Dywi bellach yn edrych at un tywysog."]),
        r=dict(archer=("At Carmarthen you are on the walls with the first of Owain’s men.", "Yng Nghaerfyrddin rydych ar y muriau gyda’r cyntaf o wŷr Owain."),
               bard=("At Llandeilo the people bring out bread and ale and ask you for every word of news about Owain.", "Yn Llandeilo mae’r bobl yn dod â bara a chwrw allan ac yn gofyn i chi am bob gair o newydd am Owain."),
               rider=("You ride ahead to Dryslwyn with Owain’s terms, and come back with the keys.", "Rydych yn marchogaeth o’r blaen i Ddryslwyn gyda thelerau Owain, ac yn dod yn ôl gyda’r allweddi.")),
        f=("In July 1403 Owain swept through the Tywi valley. Llandovery, Dryslwyn and Newcastle Emlyn came over to him, and Carmarthen was taken.",
           "Ym mis Gorffennaf 1403 ysgubodd Owain drwy ddyffryn Tywi. Daeth Llanymddyfri, Dryslwyn a Chastellnewydd Emlyn drosodd ato, a chipiwyd Caerfyrddin.",
           ["owain-sweeps-the-south"]),
        c=[dict(t=("Stay to hold Carmarthen", "Aros i ddal Caerfyrddin"), to="mach", add=1,
                say=("You keep the walls of Carmarthen through the winter. In the spring a rider comes: Owain wants every captain at Machynlleth.",
                     "Rydych yn cadw muriau Caerfyrddin drwy’r gaeaf. Yn y gwanwyn daw marchog: mae Owain eisiau pob capten ym Machynlleth.")),
           dict(t=("Ride north with Owain", "Marchogaeth i’r gogledd gydag Owain"), to="mach", add=1,
                say=("You ride north at Owain’s side, through a country that is his from end to end.", "Rydych yn marchogaeth i’r gogledd wrth ochr Owain, drwy wlad sy’n eiddo iddo o un pen i’r llall."))]),

    "mach": dict(
        d=("1404", "1404"), p=("Machynlleth", "Machynlleth"), at="mach", y=1404.4,
        t=(["It is the summer of Owain’s glory. The great castles of Harlech and Aberystwyth, built to hold Wales down, are his now. "
            "At Machynlleth he calls a parliament, and four men come from every commote in Wales to sit in it.",
            "Before envoys from Scotland, France and Castile, Owain is crowned Prince of Wales. He has a Great Seal, a Chancellor and a plan. Wales is a nation again."],
           ["Dyma haf gogoniant Owain. Mae cestyll mawr Harlech ac Aberystwyth, a godwyd i gadw Cymru dan draed, yn eiddo iddo nawr. "
            "Ym Machynlleth mae’n galw senedd, a daw pedwar dyn o bob cwmwd yng Nghymru i eistedd ynddi.",
            "Gerbron llysgenhadon o’r Alban, Ffrainc a Chastîl, coronir Owain yn Dywysog Cymru. Mae ganddo Sêl Fawr, Canghellor a chynllun. Mae Cymru’n genedl unwaith eto."]),
        r=dict(archer=("You are one of the guard at the door, your bow polished and your coat new.", "Rydych yn un o’r gwarchodlu wrth y drws, eich bwa’n loyw a’ch côt yn newydd."),
               bard=("You stand at the back of the hall and know you will sing of this day for the rest of your life.", "Rydych yn sefyll yng nghefn y neuadd ac yn gwybod y byddwch yn canu am y dydd hwn am weddill eich oes."),
               rider=("Owain’s ambassadors are leaving for France, and they need a rider who knows the roads.", "Mae llysgenhadon Owain yn gadael am Ffrainc, ac mae angen marchog arnynt sy’n adnabod y ffyrdd.")),
        f=("In 1404 Owain Glyndŵr held a parliament at Machynlleth with four men from every commote, and was crowned before envoys from Scotland, France and Castile.",
           "Yn 1404 cynhaliodd Owain Glyndŵr senedd ym Machynlleth gyda phedwar dyn o bob cwmwd, a’i goroni gerbron llysgenhadon o’r Alban, Ffrainc a Chastîl.",
           ["harlech-and-aberystwyth", "parliament-at-machynlleth"]),
        c=[dict(t=("Go with the ambassadors to Paris", "Mynd gyda’r llysgenhadon i Baris"), to="paris", add=2, bonus=dict(rider=1)),
           dict(t=("Go to Harlech, Owain’s new court", "Mynd i Harlech, llys newydd Owain"), to="court", add=2, bonus=dict(bard=1))]),

    "paris": dict(
        d=("14 July 1404", "14 Gorffennaf 1404"), p=("Paris", "Paris"), at=None, y=1404.53,
        t=(["You ride with Owain’s ambassadors, his Chancellor Gruffudd Young and his wife’s kinsman John Hanmer, all the way to Paris. "
            "There, before the court of Charles VI of France, they seal a treaty of alliance.",
            "Wales and France are allies now. Owain’s envoys are received as the ambassadors of a prince, and the French promise an army to help him."],
           ["Rydych yn marchogaeth gyda llysgenhadon Owain, ei Ganghellor Gruffudd Young a pherthynas ei wraig John Hanmer, yr holl ffordd i Baris. "
            "Yno, gerbron llys Siarl VI o Ffrainc, maen nhw’n selio cytundeb cynghrair.",
            "Mae Cymru a Ffrainc yn gynghreiriaid bellach. Croesewir llysgenhadon Owain fel llysgenhadon tywysog, ac mae’r Ffrancwyr yn addo byddin i’w helpu."]),
        f=("On 14 July 1404 in Paris, Owain’s ambassadors Gruffudd Young and John Hanmer sealed a treaty of alliance with Charles VI of France.",
           "Ar 14 Gorffennaf 1404 ym Mharis, seliodd llysgenhadon Owain, Gruffudd Young a John Hanmer, gytundeb cynghrair â Siarl VI o Ffrainc.",
           ["wales-and-france-make-a-treaty"]),
        c=[dict(t=("Sail home with the news", "Hwylio adref gyda’r newydd"), to="french", add=1,
                say=("Owain hears your news at Harlech and clasps your hand. In February he seals a great agreement with Mortimer and the Earl of Northumberland. Then, in the summer, the French sails come.",
                     "Mae Owain yn clywed eich newydd yn Harlech ac yn gafael yn eich llaw. Ym mis Chwefror mae’n selio cytundeb mawr gyda Mortimer ac Iarll Northumberland. Yna, yn yr haf, daw hwyliau Ffrainc."))]),

    "court": dict(
        d=("Winter 1404 to 1405", "Gaeaf 1404 i 1405"), p=("Harlech", "Harlech"), at="harlech", y=1404.9,
        t=(["Harlech is Owain’s court now, and his home. His wife Margaret and their children live in the castle above the sea. "
            "Bards come from every corner of Wales, and the hall is full of music, Welsh law and talk of the future.",
            "In February a great agreement is sealed between Owain, Edmund Mortimer and the Earl of Northumberland, the Tripartite Indenture. "
            "Owain’s share is a greater Wales, reaching east as far as the Severn, the Trent and the Mersey."],
           ["Harlech yw llys Owain nawr, a’i gartref. Mae ei wraig Marged a’u plant yn byw yn y castell uwchben y môr. "
            "Daw beirdd o bob cwr o Gymru, ac mae’r neuadd yn llawn cerddoriaeth, cyfraith Cymru a sôn am y dyfodol.",
            "Ym mis Chwefror selir cytundeb mawr rhwng Owain, Edmund Mortimer ac Iarll Northumberland, y Cytundeb Tridarn. "
            "Cyfran Owain yw Cymru fwy, yn ymestyn i’r dwyrain hyd at afonydd Hafren, Trent a Merswy."]),
        r=dict(archer=("You walk the walls at night and watch the sea for French sails.", "Rydych yn cerdded y muriau yn y nos ac yn gwylio’r môr am hwyliau Ffrainc."),
               bard=("Owain asks you to sing at his table. You sing of Hyddgen and Bryn Glas, and the hall roars.", "Mae Owain yn gofyn i chi ganu wrth ei fwrdd. Rydych yn canu am Hyddgen a Bryn Glas, ac mae’r neuadd yn rhuo."),
               rider=("You carry Owain’s letters up and down Wales, to every captain and every commote.", "Rydych yn cludo llythyrau Owain ar hyd a lled Cymru, at bob capten a phob cwmwd.")),
        f=("Harlech was Owain’s court and home from 1404. In February 1405 the Tripartite Indenture divided the realm between Owain, Mortimer and Northumberland.",
           "Harlech oedd llys a chartref Owain o 1404. Ym mis Chwefror 1405 rhannodd y Cytundeb Tridarn y deyrnas rhwng Owain, Mortimer a Northumberland.",
           ["harlech-and-aberystwyth", "the-tripartite-indenture"]),
        c=[dict(t=("Ride south to meet the French", "Marchogaeth i’r de i gyfarfod y Ffrancwyr"), to="french", add=1,
                say=("In the summer, the word comes from the watchers on the coast: French sails in the west.", "Yn yr haf, daw’r gair gan y gwylwyr ar yr arfordir: hwyliau Ffrainc yn y gorllewin."))]),

    "french": dict(
        d=("August 1405", "Awst 1405"), p=("Milford Haven", "Aberdaugleddau"), at="milford", y=1405.6,
        t=(["A French fleet sails into Milford Haven with an army of some two and a half thousand men. Owain meets them with thousands of his own. "
            "Together they take the town of Haverfordwest, then Carmarthen, and then they do something no Welsh prince had done in two hundred years.",
            "They march across Wales and into England, as far as Woodbury Hill, a few miles from Worcester. King Henry comes with his army and stands on the hill opposite. "
            "For eight days the two hosts face each other across the valley."],
           ["Mae llynges o Ffrainc yn hwylio i mewn i Aberdaugleddau gyda byddin o ryw ddwy fil a hanner o ddynion. Mae Owain yn eu cyfarfod gyda miloedd o’i wŷr ei hun. "
            "Gyda’i gilydd maen nhw’n cipio tref Hwlffordd, yna Caerfyrddin, ac yna’n gwneud rhywbeth nad oedd yr un tywysog Cymreig wedi’i wneud ers dau gan mlynedd.",
            "Maen nhw’n martsio ar draws Cymru ac i mewn i Loegr, hyd at Woodbury Hill, ychydig filltiroedd o Gaerwrangon. Daw’r Brenin Harri gyda’i fyddin a sefyll ar y bryn gyferbyn. "
            "Am wyth diwrnod mae’r ddwy fyddin yn wynebu ei gilydd ar draws y cwm."]),
        r=dict(archer=("From Woodbury Hill you can see the towers of Worcester. You are further from home than anyone in your family has ever been.", "O Woodbury Hill gallwch weld tyrau Caerwrangon. Rydych ymhellach o adref nag y bu neb o’ch teulu erioed."),
               bard=("A French knight asks you to teach him a Welsh song. He sings it badly, but with great joy.", "Mae marchog o Ffrainc yn gofyn i chi ddysgu cân Gymraeg iddo. Mae’n ei chanu’n wael, ond gyda llawenydd mawr."),
               rider=("At night you lead a French captain down to look at the king’s camp fires.", "Yn y nos rydych yn arwain capten o Ffrainc i lawr i edrych ar danau gwersyll y brenin.")),
        f=("A French army landed at Milford Haven in August 1405. With Owain’s men they marched into England as far as Woodbury Hill near Worcester, where they faced King Henry’s army for several days.",
           "Glaniodd byddin o Ffrainc yn Aberdaugleddau ym mis Awst 1405. Gyda gwŷr Owain martsiodd i mewn i Loegr hyd at Woodbury Hill ger Caerwrangon, lle wynebodd fyddin y Brenin Harri am rai dyddiau.",
           ["the-french-land"]),
        c=[dict(t=("Hold the hill and wait for the king to attack", "Dal y bryn ac aros i’r brenin ymosod"), to="pennal", add=2, bonus=dict(archer=1),
                say=("The king never comes up the hill. After eight days, short of food, both armies turn for home. Owain has marched an army into England and brought it home again.",
                     "Nid yw’r brenin byth yn dod i fyny’r bryn. Wedi wyth diwrnod, yn brin o fwyd, mae’r ddwy fyddin yn troi am adref. Mae Owain wedi martsio byddin i mewn i Loegr a dod â hi adref eto.")),
           dict(t=("Ride out in the skirmishes between the lines", "Marchogaeth allan i’r sgarmesoedd rhwng y ddwy fyddin"), to="pennal", add=2, bonus=dict(rider=1),
                say=("There are skirmishes in the valley, and you come back with a tale to tell. After eight days, short of food, both armies turn for home.",
                     "Mae sgarmesoedd yn y cwm, ac rydych yn dod yn ôl gyda stori i’w hadrodd. Wedi wyth diwrnod, yn brin o fwyd, mae’r ddwy fyddin yn troi am adref."))]),

    "pennal": dict(
        d=("31 March 1406", "31 Mawrth 1406"), p=("Pennal, by the Dyfi", "Pennal, ger y Dyfi"), at="pennal", y=1406.25,
        t=(["At Pennal, near the River Dyfi, Owain and his council write a letter to the King of France. It is the clearest picture we have of the Wales he wanted.",
            "The Welsh church must be free, with St Davids as the seat of an archbishop. Its priests must speak Welsh. And Wales must have two universities, "
            "one in the north and one in the south, so that its young people need not go to England to learn."],
           ["Ym Mhennal, ger afon Dyfi, mae Owain a’i gyngor yn ysgrifennu llythyr at Frenin Ffrainc. Dyma’r darlun cliriaf sydd gennym o’r Gymru yr oedd ef ei heisiau.",
            "Rhaid i eglwys Cymru fod yn rhydd, gyda Thyddewi’n sedd i archesgob. Rhaid i’w hoffeiriaid siarad Cymraeg. A rhaid i Gymru gael dwy brifysgol, "
            "un yn y gogledd ac un yn y de, fel na fydd rhaid i’w phobl ifanc fynd i Loegr i ddysgu."]),
        r=dict(archer=("You stand guard at the door while the council writes. You cannot read the Latin, but you understand what it means.", "Rydych yn gwarchod y drws tra bo’r cyngor yn ysgrifennu. Ni allwch ddarllen y Lladin, ond rydych yn deall beth yw ei ystyr."),
               bard=("You think of the students who walked home from Oxford to join Owain. One day, perhaps, they will have a university of their own.", "Rydych yn meddwl am y myfyrwyr a gerddodd adref o Rydychen i ymuno ag Owain. Un dydd, efallai, bydd ganddynt brifysgol eu hunain."),
               rider=("You carry the sealed letter to the ship that will take it to France.", "Rydych yn cludo’r llythyr dan sêl i’r llong a fydd yn mynd ag ef i Ffrainc.")),
        f=("The Pennal Letter of 31 March 1406 set out Owain’s plan for Wales: an independent Welsh church and two universities. The University of Wales was not founded until 1893.",
           "Gosododd Llythyr Pennal, 31 Mawrth 1406, gynllun Owain i Gymru: eglwys Gymreig annibynnol a dwy brifysgol. Ni sefydlwyd Prifysgol Cymru tan 1893.",
           ["the-pennal-letter"]),
        c=[dict(t=("Carry the dream back to Harlech", "Cludo’r freuddwyd yn ôl i Harlech"), to="harlech", add=1,
                say=("The years that follow are hard. The king’s son, the young Prince Henry, brings great guns from England.", "Mae’r blynyddoedd sy’n dilyn yn galed. Daw mab y brenin, y Tywysog Harri ifanc, â gynnau mawr o Loegr.")),
           dict(t=("Stay in the hills with Owain’s captains", "Aros yn y bryniau gyda chapteiniaid Owain"), to="harlech", add=1,
                say=("The years that follow are hard. The king’s son, the young Prince Henry, brings great guns from England.", "Mae’r blynyddoedd sy’n dilyn yn galed. Daw mab y brenin, y Tywysog Harri ifanc, â gynnau mawr o Loegr."))]),

    "harlech": dict(
        d=("Winter 1408 to 1409", "Gaeaf 1408 i 1409"), p=("Harlech", "Harlech"), at="harlech", y=1408.9,
        t=(["The stone balls of the great guns batter the walls of Aberystwyth until it falls in 1408. Now the guns are at Harlech.",
            "Inside are Owain’s wife Margaret, his family, and Edmund Mortimer, who holds the castle to the last. Owain himself is outside, gathering men to break the siege. "
            "In February 1409, worn down by hunger, Harlech falls. Owain does not."],
           ["Mae peli cerrig y gynnau mawr yn pwnio muriau Aberystwyth nes iddi syrthio yn 1408. Nawr mae’r gynnau yn Harlech.",
            "Y tu mewn mae Marged gwraig Owain, ei deulu, ac Edmund Mortimer, sy’n dal y castell hyd y diwedd. Mae Owain ei hun y tu allan, yn casglu gwŷr i dorri’r gwarchae. "
            "Ym mis Chwefror 1409, wedi’i threchu gan newyn, mae Harlech yn syrthio. Nid yw Owain yn syrthio."]),
        r=dict(archer=("You are with Owain in the hills, watching the smoke of the guns drift out over the sea.", "Rydych gydag Owain yn y bryniau, yn gwylio mwg y gynnau’n drifftio allan dros y môr."),
               bard=("You make an elegy for Harlech, and you make it proud.", "Rydych yn llunio marwnad i Harlech, ac rydych yn ei gwneud yn falch."),
               rider=("You ride through the night to bring Owain the news. He listens without a word.", "Rydych yn marchogaeth drwy’r nos i ddod â’r newydd i Owain. Mae’n gwrando heb air.")),
        f=("Aberystwyth fell to the king’s guns in 1408 and Harlech in February 1409. Owain was not inside, and he was never captured.",
           "Syrthiodd Aberystwyth i ynnau’r brenin yn 1408 a Harlech ym mis Chwefror 1409. Nid oedd Owain y tu mewn, ac ni chafodd ei ddal erioed.",
           ["harlech-and-aberystwyth"]),
        c=[dict(t=("Go into the hills with Owain", "Mynd i’r bryniau gydag Owain"), to="end", add=2),
           dict(t=("Carry Owain’s word to the last bands in the north", "Cludo gair Owain at y bandiau olaf yn y gogledd"), to="end", add=2, bonus=dict(rider=1))]),

    "end": dict(
        d=("1415", "1415"), p=("The hills of Wales", "Bryniau Cymru"), at=None, y=1415,
        t=(["For years Owain fights on from the hills. In 1415 the new king, Henry V, offers him a pardon. Owain does not take it. The next year the offer is made again, and no answer comes.",
            "Then nothing more is heard of him. He is never captured, and in all those years no one betrays him. One chronicler wrote that very many said he had died, "
            "but the seers said he had not. Welsh tradition holds that he sleeps with his men in a cave, until Wales needs him again."],
           ["Am flynyddoedd mae Owain yn ymladd ymlaen o’r bryniau. Yn 1415 mae’r brenin newydd, Harri V, yn cynnig pardwn iddo. Nid yw Owain yn ei gymryd. Y flwyddyn wedyn cynigir eto, ac nid oes ateb yn dod.",
            "Yna ni chlywir dim mwy amdano. Ni chaiff ei ddal byth, ac yn yr holl flynyddoedd hynny nid oes neb yn ei fradychu. Ysgrifennodd un croniclydd fod llawer iawn yn dweud ei fod wedi marw, "
            "ond fod y daroganwyr yn dweud nad oedd. Mae traddodiad Cymru’n dal ei fod yn cysgu gyda’i wŷr mewn ogof, hyd nes y bydd Cymru ei angen eto."]),
        f=("Owain Glyndŵr disappears from the record after 1415. He was never captured and never betrayed. His rising day, 16 September, is Owain Glyndŵr Day.",
           "Mae Owain Glyndŵr yn diflannu o’r cofnodion wedi 1415. Ni chafodd ei ddal ac ni chafodd ei fradychu. Dydd ei wrthryfel, 16 Medi, yw Diwrnod Owain Glyndŵr.",
           ["owain-is-never-taken"]),
        c=[]),
}

ENDINGS = {
    "archer": ("You go home at last to the hills, and hang your bow of yew above the fire. When your grandchildren ask about it, you tell them of Hyddgen and Bryn Glas, and of the prince who never surrendered.",
               "Rydych yn mynd adref i’r bryniau o’r diwedd, ac yn crogi eich bwa ywen uwchben y tân. Pan fydd eich wyrion yn holi amdano, rydych yn sôn wrthynt am Hyddgen a Bryn Glas, ac am y tywysog na ildiodd erioed."),
    "bard": ("You never stop singing of Owain. Your verses pass from mouth to mouth for seventy years, until a man of the Tudor blood of Penmynydd takes the crown at Bosworth, and the bards say the prophecy has come true at last.",
             "Nid ydych byth yn peidio â chanu am Owain. Mae eich penillion yn mynd o enau i enau am saith deg mlynedd, nes i ŵr o waed Tuduriaid Penmynydd gipio’r goron yn Bosworth, a’r beirdd yn dweud bod y ddarogan wedi dod yn wir o’r diwedd."),
    "rider": ("You ride the roads of Wales for the rest of your life, and in every hall you stop at, someone asks for news of Owain. You always give the same answer: he is only sleeping.",
              "Rydych yn marchogaeth ffyrdd Cymru am weddill eich oes, ac ym mhob neuadd lle rydych yn aros, mae rhywun yn gofyn am newyddion am Owain. Rydych bob amser yn rhoi’r un ateb: dim ond cysgu y mae."),
}

# how you are remembered, by renown (thresholds are set from the most a rider of each kind can earn, see _max_renown)
RANKS = [(0, "One of Owain’s faithful", "Un o ffyddloniaid Owain"),
         (0.6, "A captain of Owain’s host", "Capten ym myddin Owain"),
         (0.85, "A hero of the rising, remembered in song", "Arwr y gwrthryfel, a gofir mewn cân")]


def setup(build_globals):
    g.update(build_globals)


def _max_renown(role, at="start", memo=None):
    memo = {} if memo is None else memo
    if at in memo:
        return memo[at]
    best = 0
    for c in NODES[at]["c"]:
        r = c.get("set") or role
        best = max(best, c.get("add", 0) + c.get("bonus", {}).get(r, 0) + _max_renown(r, c["to"], memo))
    memo[at] = best
    return best


def _check():
    for k, n in NODES.items():
        for c in n["c"]:
            assert c["to"] in NODES, (k, c["to"])
        for s in n.get("f", ("", "", []))[2]:
            assert s in EP.SLUG, (k, s)


def _xy(at):
    geo = g["geo"]
    lat, lon = PLACES[at]
    return round((lon - geo["minx"]) * geo["k"] * geo["sc"], 1), round((geo["maxy"] - lat) * geo["sc"], 1)


def data():
    _check()
    ev_title = {EP.SLUG[i]: [ev[5], ev[6]] for i, ev in enumerate(D.EVENTS)}
    nodes = {}
    for k, n in NODES.items():
        x = dict(d=list(n["d"]), p=list(n["p"]), y=n["y"], t=[n["t"][0], n["t"][1]],
                 c=[{kk: (list(v) if isinstance(v, tuple) else v) for kk, v in c.items()} for c in n["c"]])
        if n.get("at"):
            x["xy"] = _xy(n["at"])
        if n.get("r"):
            x["r"] = {r: list(v) for r, v in n["r"].items()}
        if n.get("f"):
            x["f"] = [n["f"][0], n["f"][1], [[s, ev_title[s][0], ev_title[s][1]] for s in n["f"][2]]]
        nodes[k] = x
    maxes = {r: _max_renown(r, "proclaim") for r in ROLES}
    return dict(start="start", nodes=nodes, roles={k: list(v) for k, v in ROLES.items()}, ends={k: list(v) for k, v in ENDINGS.items()},
                ranks=[list(r) for r in RANKS], max=maxes)


def _map():
    geo = g["geo"]
    dots = "".join(f'<circle class="rd-dot" cx="{x}" cy="{y}" r="5"/>' for x, y in sorted({_xy(a) for a in PLACES}))
    return (f'<svg class="rd-map" id="rd-map" viewBox="-10 -10 700 691" role="img" aria-label="Map of Wales showing your road / Map o Gymru yn dangos eich taith">'
            f'<path class="land" d="{geo["outline"]}"/>{dots}<polyline id="rd-path" class="rd-path" points=""/>'
            f'<g id="rd-here" class="rd-here" transform="translate(-50,-50)"><circle class="rd-ring" r="16"/><circle r="8"/></g></svg>')


def page():
    bi, e, section, hero, SITE = g["bi"], g["e"], g["section"], g["hero"], g["SITE"]
    intro = hero("medieval", f'<a href="index.html">{SITE}</a> / <a href="play.html">{bi("Play", "Chwarae")}</a>', "book",
                 "A story where you choose", "Stori lle rydych chi’n dewis", "Ride with Glyndŵr, 1400", "Marchogaeth gyda Glyndŵr, 1400",
                 "September 1400. Owain Glyndŵr calls Wales to rise. Answer as an archer, a bard or a rider, and follow the rising for fifteen years. Every scene really happened.",
                 "Medi 1400. Mae Owain Glyndŵr yn galw ar Gymru i godi. Atebwch fel saethydd, bardd neu farchog, a dilyn y gwrthryfel am bymtheg mlynedd. Digwyddodd pob golygfa go iawn.",
                 art="horse")
    game = (f'<div class="rd-grid"><div class="rd-side"><div class="rd-mapbox">{_map()}</div>'
            f'<div class="rd-bar" aria-hidden="true"><span>1400</span><i><b id="rd-bar"></b></i><span>1415</span></div>'
            f'<div class="rd-log-box"><h2 class="h3">{bi("Your chronicle", "Eich cronicl")}</h2><ol id="rd-log" class="rd-log"></ol></div></div>'
            f'<div class="rd-story" id="rd-story" aria-live="polite"><noscript><p>{bi("This story needs JavaScript. The real history is below.", "Mae angen JavaScript ar gyfer y stori hon. Mae’r hanes go iawn isod.")}</p></noscript></div></div>')
    ev = [x for x in D.EVENTS if 1400 <= x[1] <= 1415]
    real = (f'<p class="muted">{bi("These are the events the story follows. Each has its own page.", "Dyma’r digwyddiadau y mae’r stori’n eu dilyn. Mae gan bob un ei dudalen ei hun.")}</p>'
            f'<ol class="era-events">{"".join(g["event_li"](x) for x in ev)}</ol>'
            f'<p class="more-row"><a class="btn" href="story-glyndwr.html">{bi("Read the long read: Owain Glyndŵr", "Darllen yr erthygl: Owain Glyndŵr")} →</a> '
            f'<a class="btn" href="person-owain-glyndwr.html">{bi("Owain Glyndŵr", "Owain Glyndŵr")}</a> '
            f'<a class="btn" href="play.html">← {bi("All games", "Pob gêm")}</a></p>')
    main = intro + f'<section class="game-sec"><div class="wrap">{game}</div></section>' + section(real, "The real history, 1400 to 1415", "Yr hanes go iawn, 1400 i 1415")
    extra = (f'<script>var RIDE={json.dumps(data(), ensure_ascii=False, separators=(",", ":"))};</script>\n'
             '<script src="ride.js?v=1" defer></script>\n')
    ld = {"@context": "https://schema.org", "@type": "Game", "name": "Ride with Glyndŵr, 1400", "alternateName": "Marchogaeth gyda Glyndŵr, 1400",
          "description": "An interactive story: follow Owain Glyndŵr’s rising from 1400 to 1415 as an archer, a bard or a rider.", "inLanguage": ["en", "cy"],
          "about": {"@type": "Person", "name": "Owain Glyndŵr", "sameAs": g["WIKI"] + "Owain_Glynd%C5%B5r"}}
    return g["page"]("ride-glyndwr.html", "Ride with Glyndŵr, 1400: a story where you choose · History of Wales",
                     "Answer Owain Glyndŵr’s call in 1400 as an archer, a bard or a rider, and follow the rising to 1415. Every scene really happened.",
                     main, era="medieval", og_type="website", ld=ld, active="play.html", track="game:ride", extra=extra)


CSS = """
.rd-grid { display: grid; gap: 1.5rem; align-items: start }
@media (min-width: 900px) { .rd-grid { grid-template-columns: minmax(0, 1.25fr) minmax(0, .75fr) } .rd-side { position: sticky; top: 5.5rem; order: 2 } .rd-story { order: 1 } }
.rd-mapbox { border: 1px solid var(--line); border-radius: var(--r); background: var(--card); padding: .6rem }
.rd-map { width: 100%; height: auto; display: block; max-height: 46vh }
.rd-map .land { fill: #232b3c; stroke: #55617a; stroke-width: 1.2 }
.rd-dot { fill: #55617a }
.rd-path { fill: none; stroke: var(--gold); stroke-width: 4; stroke-dasharray: 10 8; stroke-linecap: round; stroke-linejoin: round }
.rd-here circle { fill: #d43c34; stroke: #fff; stroke-width: 2.5 }
.rd-here .rd-ring { fill: none; stroke: #d43c34; stroke-width: 3; animation: rd-pulse 2s infinite }
.rd-here { transition: transform .9s var(--ease) }
@keyframes rd-pulse { from { opacity: .9; r: 9 } to { opacity: 0; r: 26 } }
@media (prefers-reduced-motion: reduce) { .rd-here { transition: none } .rd-here .rd-ring { animation: none } }
@media (max-width: 899px) { .rd-map { max-height: 34vh } .rd-log-box { display: none } }
.rd-bar { display: flex; align-items: center; gap: .6rem; margin: .8rem 0; font: 500 .8rem var(--f-mono); color: var(--muted) }
.rd-bar i { flex: 1; height: 6px; border-radius: 6px; background: var(--line); overflow: hidden }
.rd-bar b { display: block; height: 100%; width: 0; background: linear-gradient(90deg, var(--gold), #d43c34); transition: width .8s var(--ease) }
.rd-log { list-style: none; margin: .4rem 0 0; padding: 0; display: grid; gap: .35rem; font-size: .92rem; color: var(--muted) }
.rd-log li { display: grid; grid-template-columns: 1.4rem 1fr; gap: .4rem }
.rd-log li::before { content: "✦"; color: var(--gold) }
.rd-log b { color: var(--ink, #ece9e1); font-weight: 600 }
.rd-card { border: 1px solid color-mix(in srgb, var(--gold) 30%, var(--line)); border-radius: var(--r); background: linear-gradient(170deg, color-mix(in srgb, var(--gold) 8%, var(--card)), var(--card) 60%); padding: clamp(1.2rem, 3vw, 2rem) }
.rd-card.in { animation: rd-in .6s var(--ease) }
@keyframes rd-in { from { opacity: 0; transform: translateY(12px) } to { opacity: 1; transform: none } }
@media (prefers-reduced-motion: reduce) { .rd-card.in { animation: none } }
.rd-when { font: 500 .8rem var(--f-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--gold); margin: 0 0 .3rem }
.rd-card h2 { margin: 0 0 1rem; font-size: clamp(1.6rem, 4vw, 2.3rem); line-height: 1.1 }
.rd-card h2:focus { outline: none }
.rd-say { border-left: 3px solid var(--gold); padding: .2rem 0 .2rem .9rem; font-style: italic; color: #e6dcc8 }
.rd-card p { font-size: 1.08rem; line-height: 1.65; margin: 0 0 .9rem }
.rd-role { display: flex; gap: .7rem; align-items: baseline; color: #e6dcc8 }
.rd-role i { font-style: normal; color: var(--gold); font-size: 1.2rem }
.rd-fact { margin: 1.2rem 0; border: 1px solid var(--line); border-radius: 14px; padding: .8rem 1rem; background: color-mix(in srgb, var(--card) 70%, #000) }
.rd-fact summary { cursor: pointer; font-weight: 700 }
.rd-fact p { font-size: .98rem; margin: .6rem 0 }
.rd-fact a { margin-right: .8rem; display: inline-block }
.rd-choices { list-style: none; padding: 0; margin: 1.4rem 0 0; display: grid; gap: .7rem }
.rd-choices button { width: 100%; text-align: left; font: inherit; font-size: 1.05rem; font-weight: 600; color: inherit; cursor: pointer; padding: 1rem 1.2rem; border-radius: 14px;
  border: 1px solid color-mix(in srgb, var(--gold) 45%, var(--line)); background: color-mix(in srgb, var(--gold) 10%, var(--card)); display: flex; gap: .8rem; align-items: center; transition: transform .2s, border-color .2s }
.rd-choices button:hover, .rd-choices button:focus-visible { border-color: var(--gold); transform: translateX(4px) }
.rd-choices button i { font-style: normal; color: var(--gold); font-size: 1.3rem; width: 1.5rem; text-align: center }
.rd-end { text-align: center }
.rd-rank { font: 400 clamp(1.4rem, 3.4vw, 2rem)/1.15 var(--f-display); color: var(--gold); margin: .3rem 0 1rem }
.rd-score { font: 500 .85rem var(--f-mono); color: var(--muted) }
.rd-again { display: flex; flex-wrap: wrap; gap: .6rem; justify-content: center; margin-top: 1.2rem }
.rd-resume { display: flex; flex-wrap: wrap; gap: .6rem; margin-top: 1rem }
"""
