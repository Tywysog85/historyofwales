"""Teacher packs: one printable pack for each of the twelve ages, pack-<age>.html, for the Curriculum for Wales.

build.py calls setup(globals()) once and pages() for the HTML. Each pack mixes what is written here (the big idea,
enquiry questions, key words, activities by progression step, the source to study) with what the site already holds
for that age (the timeline, people, places, quiz sheet and long reads), so it grows as the site grows.
Follow EDITORIAL.md: proud and true, Britons not Celts, kings are kings.
"""
import data as D
import ref_az as AZ
import ref_docs as DC

g = {}

# The five statements of what matters in the Humanities Area of Learning and Experience, in short.
WHAT = [("Enquiry and investigation", "Ymholi ac ymchwilio",
         "Asking questions and investigating sparks curiosity about the world, its past, present and future.",
         "Mae holi ac ymchwilio’n ennyn chwilfrydedd am y byd, ei orffennol, ei bresennol a’i ddyfodol."),
        ("Different interpretations", "Dehongliadau gwahanol",
         "Events and people’s experiences are complex, and are seen, told and shown in different ways.",
         "Mae digwyddiadau a phrofiadau pobl yn gymhleth, ac yn cael eu gweld, eu hadrodd a’u dangos mewn ffyrdd gwahanol."),
        ("The natural world", "Y byd naturiol",
         "Our natural world is varied and always changing, shaped by natural processes and by people.",
         "Mae ein byd naturiol yn amrywiol ac yn newid o hyd, wedi’i lunio gan brosesau naturiol a chan bobl."),
        ("Societies and beliefs", "Cymdeithasau a chredoau",
         "Human societies are complex and varied, shaped by what people do and what they believe.",
         "Mae cymdeithasau dynol yn gymhleth ac yn amrywiol, wedi’u llunio gan yr hyn y mae pobl yn ei wneud a’i gredu."),
        ("Informed citizens", "Dinasyddion gwybodus",
         "Informed citizens take part in the challenges and chances facing the world, and act with thought and care.",
         "Mae dinasyddion gwybodus yn cymryd rhan yn yr heriau a’r cyfleoedd sy’n wynebu’r byd, ac yn gweithredu’n feddylgar ac yn ofalus.")]

STEPS = [("Progression step 2 (around age 8)", "Cam cynnydd 2 (tua 8 oed)"),
         ("Progression step 3 (around age 11)", "Cam cynnydd 3 (tua 11 oed)"),
         ("Progression step 4 (around age 14)", "Cam cynnydd 4 (tua 14 oed)")]

PACKS = {
    "ancient": dict(
        big=("People have lived in Wales for more than 200,000 years. They hunted in the caves, farmed the valleys, raised the great stone tombs and built hillforts, and by the time Rome arrived the Britons of Wales had kings, druids and skilled metalworkers.",
             "Mae pobl wedi byw yng Nghymru ers dros 200,000 o flynyddoedd. Buont yn hela yn yr ogofâu, yn ffermio’r dyffrynnoedd, yn codi’r beddrodau cerrig mawr ac yn adeiladu bryngaerau, ac erbyn i Rufain gyrraedd roedd gan Frythoniaid Cymru frenhinoedd, derwyddon a gofaint medrus."),
        what=[0, 2, 3],
        qs=[("How do we know about people who left no writing?", "Sut rydyn ni’n gwybod am bobl na adawodd ysgrifen?"),
            ("Why did people carry the bluestones from Preseli all the way to Stonehenge?", "Pam y cariodd pobl y cerrig gleision o’r Preseli yr holl ffordd i Gôr y Cewri?"),
            ("What can a hillfort tell us about the people who built it?", "Beth all bryngaer ei ddweud wrthym am y bobl a’i hadeiladodd?")],
        words=["cromlech", "maen-hir", "bluestones", "hillfort", "druids"],
        acts=[[("Make a ‘museum box’ of objects a Stone Age family would need. Draw or model each one and say what it was for.", "Gwnewch ‘focs amgueddfa’ o bethau y byddai teulu o Oes y Cerrig eu hangen. Lluniwch neu fodelwch bob un a dweud beth oedd ei bwrpas."),
               ("Find the nearest burial chamber or standing stone to your school on the historic sites map, and plan a visit.", "Dewch o hyd i’r siambr gladdu neu’r maen hir agosaf at eich ysgol ar y map safleoedd hanesyddol, a chynlluniwch ymweliad.")],
              [("Work out how the bluestones might have been moved 150 miles. Test sledges and rollers with a heavy box in the yard.", "Gweithiwch allan sut y gallai’r cerrig gleision fod wedi’u symud 150 milltir. Profwch slediau a rholeri gyda bocs trwm ar yr iard."),
               ("Design a hillfort for your area: where would you build it, and why? Label the ramparts, the gate and the roundhouses.", "Cynlluniwch fryngaer ar gyfer eich ardal: ble byddech chi’n ei hadeiladu, a pham? Labelwch y rhagfuriau, y porth a’r tai crwn.")],
              [("Compare what archaeologists say about Pontnewydd and Paviland with what was first believed in 1823. How does new evidence change the story?", "Cymharwch yr hyn y mae archaeolegwyr yn ei ddweud am Bontnewydd a Phafiland â’r hyn a gredid gyntaf yn 1823. Sut mae tystiolaeth newydd yn newid y stori?"),
               ("Caesar wrote that Britain was the home of druid learning. Discuss: how far can we trust a Roman writing about his enemies?", "Ysgrifennodd Cesar mai Prydain oedd cartref dysg y derwyddon. Trafodwch: i ba raddau y gallwn ymddiried mewn Rhufeiniwr yn ysgrifennu am ei elynion?")]],
        doc="caesar"),
    "roman": dict(
        big=("The peoples of Wales, the Silures, Ordovices, Demetae and Deceangli, held out against Rome for some thirty years, led at first by King Caratacus. Then came forts, roads, gold mines and towns like Caerwent, and Roman Wales left its mark on the land and the language.",
             "Daliodd pobloedd Cymru, y Silwriaid, yr Ordoficiaid, y Demetae a’r Deceangli, eu tir yn erbyn Rhufain am ryw ddeng mlynedd ar hugain, dan arweiniad y Brenin Caradog i ddechrau. Yna daeth caerau, ffyrdd, mwyngloddiau aur a threfi fel Caer-went, a gadawodd Cymru Rufeinig ei hôl ar y tir a’r iaith."),
        what=[1, 3, 4],
        qs=[("Why did it take Rome so long to conquer Wales?", "Pam y cymerodd hi gyhyd i Rufain goncro Cymru?"),
            ("What did the Romans leave behind in Wales, and what can we still see?", "Beth a adawodd y Rhufeiniaid ar eu hôl yng Nghymru, a beth allwn ni ei weld o hyd?"),
            ("Was Caratacus a hero? Who says so, and why?", "Ai arwr oedd Caradog? Pwy sy’n dweud hynny, a pham?")],
        words=["silures", "ordovices", "isca", "sarn-helen", "druids"],
        acts=[[("Act out Caratacus speaking before the emperor in Rome. What would you say to win your freedom?", "Actiwch Garadog yn siarad gerbron yr ymerawdwr yn Rhufain. Beth fyddech chi’n ei ddweud i ennill eich rhyddid?"),
               ("Find Welsh words that come from Latin: ffenestr, pont, eglwys, llyfr. Make a word wall.", "Dewch o hyd i eiriau Cymraeg sy’n dod o’r Lladin: ffenestr, pont, eglwys, llyfr. Gwnewch wal eiriau.")],
              [("Plan a day at Caerleon as a Roman soldier: the barracks, the baths and the amphitheatre. Write a letter home.", "Cynlluniwch ddiwrnod yng Nghaerllion fel milwr Rhufeinig: y barics, y baddonau a’r amffitheatr. Ysgrifennwch lythyr adref."),
               ("Map the Roman roads and forts of Wales. Why are so many in the hills and along the coast?", "Mapiwch ffyrdd a chaerau Rhufeinig Cymru. Pam fod cymaint ohonynt yn y bryniau ac ar hyd yr arfordir?")],
              [("Read Tacitus on the attack on Ynys Môn. Whose side is he on? What does he want his readers to feel?", "Darllenwch Tacitus am yr ymosodiad ar Ynys Môn. Ar ochr pwy y mae? Beth mae am i’w ddarllenwyr ei deimlo?"),
               ("Debate: did the people of Wales gain or lose more under Rome? Use evidence from Dolaucothi, Caerwent and the forts.", "Dadl: a enillodd neu a gollodd pobl Cymru fwy dan Rufain? Defnyddiwch dystiolaeth o Ddolaucothi, Caer-went a’r caerau.")]],
        doc="tacitus"),
    "saints": dict(
        big=("After Rome left, the Britons kept their island’s faith and learning alive. Saints like Dewi, Illtud, Teilo and Cadog founded the llannau whose names are still on the map, Llanilltud Fawr became the oldest centre of learning in Britain, and the first Welsh poetry was made.",
             "Wedi i Rufain ymadael, cadwodd y Brythoniaid ffydd a dysg eu hynys yn fyw. Sefydlodd seintiau fel Dewi, Illtud, Teilo a Chadog y llannau y mae eu henwau ar y map o hyd, daeth Llanilltud Fawr yn ganolfan ddysg hynaf Prydain, a chanwyd y farddoniaeth Gymraeg gyntaf."),
        what=[1, 3, 0],
        qs=[("Why do so many places in Wales begin with ‘Llan’?", "Pam fod cymaint o leoedd yng Nghymru’n dechrau â ‘Llan’?"),
            ("What do we really know about Arthur, and how do we know it?", "Beth rydyn ni’n ei wybod mewn gwirionedd am Arthur, a sut rydyn ni’n ei wybod?"),
            ("How did the Britons of the Old North become part of Welsh history?", "Sut daeth Brythoniaid yr Hen Ogledd yn rhan o hanes Cymru?")],
        words=["llan", "age-of-saints", "hen-ogledd", "cynfeirdd", "inscribed-stones"],
        acts=[[("Find every place name beginning with Llan within ten miles of school. Who was each saint?", "Dewch o hyd i bob enw lle sy’n dechrau â Llan o fewn deng milltir i’r ysgol. Pwy oedd pob sant?"),
               ("Learn Dewi’s words ‘Gwnewch y pethau bychain’ and make a class list of small kind things to do.", "Dysgwch eiriau Dewi ‘Gwnewch y pethau bychain’ a gwnewch restr ddosbarth o bethau bach caredig i’w gwneud.")],
              [("Design an inscribed stone in memory of someone, in the style of the early stones, with Latin and ogham.", "Cynlluniwch garreg arysgrifedig er cof am rywun, yn null y cerrig cynnar, gyda Lladin ac ogam."),
               ("Read a verse of Y Gododdin in translation. What did the poet think made a hero?", "Darllenwch bennill o’r Gododdin mewn cyfieithiad. Beth oedd yn gwneud arwr ym marn y bardd?")],
              [("Compare the Annals of Wales and the History of the Britons on Arthur. What does each say, and when were they written?", "Cymharwch Annales Cambriae a Historia Brittonum am Arthur. Beth mae pob un yn ei ddweud, a phryd y’u hysgrifennwyd?"),
               ("Plot the journeys of the saints to Cornwall, Brittany and Ireland on a map. What does it tell us about the sea in this age?", "Plotiwch deithiau’r seintiau i Gernyw, Llydaw ac Iwerddon ar fap. Beth mae’n ei ddweud wrthym am y môr yn yr oes hon?")]],
        doc="annales"),
    "kings": dict(
        big=("The kingdoms of Gwynedd, Powys, Deheubarth and the rest were ruled by kings who fought off the Vikings, made alliances and wrote down the law. Rhodri Mawr, Hywel Dda and Gruffudd ap Llywelyn each brought much of Wales together, and Gruffudd ruled it all.",
             "Teyrnaswyd teyrnasoedd Gwynedd, Powys, Deheubarth a’r gweddill gan frenhinoedd a drechodd y Llychlynwyr, a wnaeth gynghreiriau ac a ysgrifennodd y gyfraith. Daeth Rhodri Mawr, Hywel Dda a Gruffudd ap Llywelyn â llawer o Gymru ynghyd, a theyrnasodd Gruffudd ar y cyfan."),
        what=[3, 4, 1],
        qs=[("What made the laws of Hywel Dda fair for their time?", "Beth oedd yn gwneud cyfreithiau Hywel Dda yn deg yn eu hoes?"),
            ("Why did no Viking kingdom take root in Wales?", "Pam na wreiddiodd unrhyw deyrnas Lychlynnaidd yng Nghymru?"),
            ("Why was it so hard to keep all of Wales under one king?", "Pam roedd hi mor anodd cadw Cymru gyfan dan un brenin?")],
        words=["cantref", "llys", "galanas", "sarhaed", "cyfraith-hywel"],
        acts=[[("Hold a class court using Hywel Dda’s idea of payment instead of punishment. What should be paid for a broken toy?", "Cynhaliwch lys dosbarth gan ddefnyddio syniad Hywel Dda o dâl yn lle cosb. Beth ddylid ei dalu am degan wedi torri?"),
               ("Colour a map of the kingdoms of Wales and give each one a shield.", "Lliwiwch fap o deyrnasoedd Cymru a rhoi tarian i bob un.")],
              [("Make a family tree from Rhodri Mawr to Hywel Dda using the royal family trees page.", "Gwnewch goeden deulu o Rodri Mawr i Hywel Dda gan ddefnyddio tudalen y coed teulu brenhinol."),
               ("Walk part of Offa’s Dyke, or study it on the maps page. Who built it, and why?", "Cerddwch ran o Glawdd Offa, neu astudiwch ef ar dudalen y mapiau. Pwy a’i cododd, a pham?")],
              [("Compare women’s rights in the laws of Hywel with another legal system of the same time. What stands out?", "Cymharwch hawliau menywod yng nghyfreithiau Hywel â chyfundrefn gyfreithiol arall o’r un cyfnod. Beth sy’n sefyll allan?"),
               ("Use the maps through time to explain how Gruffudd ap Llywelyn united Wales, and why it parted after 1063.", "Defnyddiwch y mapiau drwy’r oesoedd i esbonio sut yr unodd Gruffudd ap Llywelyn Gymru, a pham y rhannodd wedi 1063.")]],
        doc="historia"),
    "medieval": dict(
        big=("For two hundred years the princes of Gwynedd and Deheubarth held Wales against the Norman and English kings. Owain Gwynedd took the title Prince of Wales, the Lord Rhys held the first eisteddfod, Llywelyn Fawr and Llywelyn ap Gruffudd ruled almost all of Wales, and Owain Glyndŵr rose in 1400 and was never taken.",
             "Am ddau gan mlynedd daliodd tywysogion Gwynedd a Deheubarth Gymru yn erbyn brenhinoedd Normanaidd a Seisnig. Cymerodd Owain Gwynedd y teitl Tywysog Cymru, cynhaliodd yr Arglwydd Rhys yr eisteddfod gyntaf, teyrnasodd Llywelyn Fawr a Llywelyn ap Gruffudd ar bron y cyfan o Gymru, a chododd Owain Glyndŵr yn 1400 ac ni chafodd ei ddal erioed."),
        what=[1, 3, 4],
        qs=[("Why did it take the Normans 216 years to take Wales, when England fell in five?", "Pam y cymerodd 216 o flynyddoedd i’r Normaniaid gipio Cymru, pan syrthiodd Lloegr mewn pump?"),
            ("Who built the castles of Wales, and what were they for?", "Pwy adeiladodd gestyll Cymru, a beth oedd eu pwrpas?"),
            ("What did Owain Glyndŵr want for Wales?", "Beth oedd Owain Glyndŵr ei eisiau i Gymru?")],
        words=["prince-of-wales", "pura-wallia", "welsh-castles", "pennal-letter", "eisteddfod"],
        acts=[[("Find the nearest castle to school on the castles map. Was it built by a Welsh prince or by an invader?", "Dewch o hyd i’r castell agosaf at yr ysgol ar fap y cestyll. Ai tywysog o Gymro neu oresgynnwr a’i cododd?"),
               ("Hold a class eisteddfod like the Lord Rhys in 1176: a chair for a poem and a prize for music.", "Cynhaliwch eisteddfod ddosbarth fel yr Arglwydd Rhys yn 1176: cadair am gerdd a gwobr am gerddoriaeth.")],
              [("Write Owain Glyndŵr’s Pennal letter in your own words. What were his four wishes for Wales?", "Ysgrifennwch Lythyr Pennal Owain Glyndŵr yn eich geiriau eich hun. Beth oedd ei bedwar dymuniad i Gymru?"),
               ("Compare a castle of the Welsh princes (Dolwyddelan, Castell y Bere) with Caernarfon. How and why are they different?", "Cymharwch gastell un o dywysogion Cymru (Dolwyddelan, Castell y Bere) â Chaernarfon. Sut a pham maen nhw’n wahanol?")],
              [("Read the old man of Pencader’s answer to Henry II. What does it say about the Welsh, and why has it been quoted for 800 years?", "Darllenwch ateb hen ŵr Pencader i Harri’r Ail. Beth mae’n ei ddweud am y Cymry, a pham y’i dyfynnwyd am 800 mlynedd?"),
               ("Interpretations: how has Owain Glyndŵr been remembered in 1400, in the Victorian age and today? Use the long reads and the documents page.", "Dehongliadau: sut y cofiwyd Owain Glyndŵr yn 1400, yn oes Victoria a heddiw? Defnyddiwch yr erthyglau a thudalen y dogfennau.")]],
        doc="pencader"),
    "tudor": dict(
        big=("A Welshman, Harri Tudur, took the crown at Bosworth under the red dragon. The Acts of Union made English the language of law, but William Morgan’s Bible of 1588 gave Welsh a standard that carried it through the centuries, and the circulating schools taught half the nation to read.",
             "Cipiodd Cymro, Harri Tudur, y goron yn Bosworth dan y ddraig goch. Gwnaeth y Deddfau Uno Saesneg yn iaith y gyfraith, ond rhoddodd Beibl William Morgan yn 1588 safon i’r Gymraeg a’i cariodd drwy’r canrifoedd, a dysgodd yr ysgolion cylchynol hanner y genedl i ddarllen."),
        what=[1, 3, 0],
        qs=[("Why did the Welsh poets call Harri Tudur ‘the son of prophecy’?", "Pam y galwodd beirdd Cymru Harri Tudur yn ‘fab darogan’?"),
            ("How did the Welsh Bible help the language survive?", "Sut helpodd y Beibl Cymraeg yr iaith i oroesi?"),
            ("What changed for Wales after the Acts of Union, and what stayed the same?", "Beth newidiodd i Gymru wedi’r Deddfau Uno, a beth arhosodd yr un fath?")],
        words=["acts-of-union", "great-sessions", "welsh-bible", "circulating-schools", "shire"],
        acts=[[("Follow Harri Tudur’s march from Dale to Bosworth on a map, and draw the red dragon banner he carried.", "Dilynwch orymdaith Harri Tudur o Dale i Bosworth ar fap, a lluniwch faner y ddraig goch a gariodd."),
               ("Visit or look up Tŷ Mawr Wybrnant, where William Morgan was born. What would his home have been like?", "Ymwelwch â Thŷ Mawr Wybrnant, neu chwiliwch amdano, lle ganwyd William Morgan. Sut le fyddai ei gartref?")],
              [("Make a timeline of the Welsh language from 1536 to 1588 to 1737. Mark the dangers and the rescues.", "Gwnewch linell amser o’r Gymraeg o 1536 i 1588 i 1737. Marciwch y peryglon a’r achubiaethau."),
               ("Robert Recorde of Tenby invented the equals sign. Make a poster of Welsh inventors and firsts from this age.", "Dyfeisiodd Robert Recorde o Ddinbych-y-pysgod yr arwydd hafal. Gwnewch boster o ddyfeiswyr a phethau cyntaf Cymreig o’r oes hon.")],
              [("Read the language clause of the 1536 Act. What did it say, what did it mean for ordinary people, and why did Welsh survive anyway?", "Darllenwch gymal iaith Deddf 1536. Beth oedd yn ei ddweud, beth oedd yn ei olygu i bobl gyffredin, a pham y goroesodd y Gymraeg er hynny?"),
               ("Was Harri Tudur’s victory good for Wales? Weigh up the evidence on both sides.", "A oedd buddugoliaeth Harri Tudur yn dda i Gymru? Pwyswch a mesurwch y dystiolaeth o’r ddwy ochr.")]],
        doc="union"),
    "industrial": dict(
        big=("Wales became one of the first industrial nations: Merthyr was the iron capital of the world, Welsh slate roofed the world, and south Wales coal powered the world’s ships. The people built chapels, choirs, eisteddfodau and trade unions, and gave the world an anthem.",
             "Daeth Cymru’n un o’r cenhedloedd diwydiannol cyntaf: Merthyr oedd prifddinas haearn y byd, toeodd llechi Cymru’r byd, a gyrrodd glo’r de longau’r byd. Cododd y bobl gapeli, corau, eisteddfodau ac undebau llafur, a rhoesant anthem i’r byd."),
        what=[2, 3, 4],
        qs=[("How did coal, iron and slate change the towns and valleys of Wales?", "Sut newidiodd glo, haearn a llechi drefi a chymoedd Cymru?"),
            ("Why did working people in Wales rise up at Merthyr, Newport and in the Rebecca Riots?", "Pam y cododd gweithwyr Cymru ym Merthyr, Casnewydd ac yn Helyntion Beca?"),
            ("How did the Welsh language and culture survive the Welsh Not?", "Sut y goroesodd yr iaith a’r diwylliant Cymraeg y Welsh Not?")],
        words=["ironworks", "slate", "coal", "rebecca-riots", "welsh-not"],
        acts=[[("Sing Hen Wlad fy Nhadau and find out who wrote it, and where.", "Canwch Hen Wlad fy Nhadau a dewch o hyd i bwy a’i hysgrifennodd, a ble."),
               ("Make a ‘day in the life’ comic of a child in a slate quarry town or a coal valley.", "Gwnewch gomig ‘diwrnod ym mywyd’ plentyn mewn tref chwarel lechi neu gwm glo.")],
              [("Use the census figures to find out how the population of your area changed between 1801 and 1911. Why?", "Defnyddiwch ffigurau’r cyfrifiad i weld sut y newidiodd poblogaeth eich ardal rhwng 1801 a 1911. Pam?"),
               ("Design a Welsh Not, then write how a child might have felt wearing it, and how the language still survived.", "Cynlluniwch Welsh Not, yna ysgrifennwch sut y gallai plentyn fod wedi teimlo yn ei wisgo, a sut y goroesodd yr iaith er hynny.")],
              [("Read the Blue Books’ words on the Welsh language beside Hen Wlad fy Nhadau. Two views of Wales: who wrote each, and why?", "Darllenwch eiriau’r Llyfrau Gleision am y Gymraeg ochr yn ochr â Hen Wlad fy Nhadau. Dwy olwg ar Gymru: pwy ysgrifennodd bob un, a pham?"),
               ("Investigate one Welsh world first of this age (the first locomotive, the fuel cell, natural selection) and present why it mattered.", "Ymchwiliwch i un o bethau cyntaf y byd o Gymru yn yr oes hon (yr injan reilffordd gyntaf, y gell danwydd, dethol naturiol) a chyflwynwch pam roedd yn bwysig.")]],
        doc="anthem"),
    "modern": dict(
        big=("In the twentieth century Wales gave Britain the NHS, fought for its language and won Welsh-medium schools, S4C and official status, and in 1997 voted for its own Assembly. It came through war, depression, Tryweryn and Aberfan with its spirit unbroken.",
             "Yn yr ugeinfed ganrif rhoddodd Cymru’r Gwasanaeth Iechyd i Brydain, ymladdodd dros ei hiaith ac ennill ysgolion Cymraeg, S4C a statws swyddogol, ac yn 1997 pleidleisiodd dros ei Chynulliad ei hun. Daeth drwy ryfel, dirwasgiad, Tryweryn ac Aberfan â’i hysbryd heb ei dorri."),
        what=[4, 1, 3],
        qs=[("How did the idea for the NHS begin in Tredegar?", "Sut dechreuodd y syniad am y Gwasanaeth Iechyd yn Nhredegar?"),
            ("Why did Tryweryn matter so much to Wales?", "Pam roedd Tryweryn mor bwysig i Gymru?"),
            ("How did campaigners win rights for the Welsh language?", "Sut enillodd ymgyrchwyr hawliau i’r Gymraeg?")],
        words=["tryweryn", "s4c", "welsh-medium", "cymdeithas", "urdd"],
        acts=[[("Find out about the Urdd and its Eisteddfod. Make a poster for your school’s own Urdd day.", "Dewch o hyd i wybodaeth am yr Urdd a’i Eisteddfod. Gwnewch boster ar gyfer diwrnod Urdd eich ysgol."),
               ("Hedd Wyn won the chair but never knew it. Look at the Black Chair and write a short poem for him.", "Enillodd Hedd Wyn y gadair ond ni wyddai hynny. Edrychwch ar y Gadair Ddu ac ysgrifennwch gerdd fer iddo.")],
              [("Interview a grandparent or neighbour about Welsh in school when they were young. Compare with today.", "Holwch nain, taid neu gymydog am y Gymraeg yn yr ysgol pan oeddent yn ifanc. Cymharwch â heddiw."),
               ("Make a ‘Cofiwch Dryweryn’ display: what happened at Capel Celyn, and how did Wales respond?", "Gwnewch arddangosfa ‘Cofiwch Dryweryn’: beth ddigwyddodd yng Nghapel Celyn, a sut ymatebodd Cymru?")],
              [("Study Saunders Lewis’s Tynged yr Iaith of 1962. What did he ask for, and what changed in the next twenty years?", "Astudiwch Dynged yr Iaith Saunders Lewis yn 1962. Am beth y gofynnodd, a beth newidiodd yn yr ugain mlynedd nesaf?"),
               ("Why did Wales vote no to an Assembly in 1979 and yes in 1997? Use the event pages and the documents page.", "Pam y pleidleisiodd Cymru na i Gynulliad yn 1979 ac ie yn 1997? Defnyddiwch dudalennau’r digwyddiadau a thudalen y dogfennau.")]],
        doc="tynged"),
    "today": dict(
        big=("Since 1999 Wales has made more and more of its own laws through its Senedd. Welsh has official status, the Future Generations Act asks every public body to think of people not yet born, and Wales has the first coast path around a whole country.",
             "Ers 1999 mae Cymru wedi gwneud mwy a mwy o’i chyfreithiau ei hun drwy ei Senedd. Mae gan y Gymraeg statws swyddogol, mae Deddf Llesiant Cenedlaethau’r Dyfodol yn gofyn i bob corff cyhoeddus feddwl am bobl sydd heb eu geni eto, ac mae gan Gymru’r llwybr arfordir cyntaf o amgylch gwlad gyfan."),
        what=[4, 2, 0],
        qs=[("What does the Senedd decide for Wales, and how can young people have their say?", "Beth mae’r Senedd yn ei benderfynu dros Gymru, a sut gall pobl ifanc ddweud eu dweud?"),
            ("What would a Wales fit for future generations look like?", "Sut olwg fyddai ar Gymru sy’n addas i genedlaethau’r dyfodol?"),
            ("How is the history of our own area still shaping it today?", "Sut mae hanes ein hardal ein hunain yn dal i’w llunio heddiw?")],
        words=["senedd", "first-minister", "devolution", "welsh-language-acts", "cymraeg"],
        acts=[[("Hold a class Senedd: elect members, debate one question about your school and vote.", "Cynhaliwch Senedd ddosbarth: etholwch aelodau, dadleuwch un cwestiwn am eich ysgol a phleidleisiwch."),
               ("Walk a stretch of the Wales Coast Path, or plan a walk around your area, and map the history you pass.", "Cerddwch ddarn o Lwybr Arfordir Cymru, neu cynlluniwch daith o amgylch eich ardal, a mapiwch yr hanes a welwch.")],
              [("Write a well-being goal for your community, using the seven goals of the Future Generations Act.", "Ysgrifennwch nod llesiant i’ch cymuned, gan ddefnyddio saith nod Deddf Llesiant Cenedlaethau’r Dyfodol."),
               ("Find out about the Youth Parliament of Wales, Senedd Ieuenctid Cymru. What would you raise if you were elected?", "Dewch o hyd i wybodaeth am Senedd Ieuenctid Cymru. Beth fyddech chi’n ei godi pe baech yn cael eich ethol?")],
              [("Compare the 1997 and 2011 referendum results county by county. What changed, and why?", "Cymharwch ganlyniadau refferendwm 1997 a 2011 sir wrth sir. Beth newidiodd, a pham?"),
               ("Make the case: which one event in this pack has done most to shape Wales today? Present it with evidence.", "Gwnewch yr achos: pa un digwyddiad yn y pecyn hwn a wnaeth fwyaf i lunio Cymru heddiw? Cyflwynwch ef gyda thystiolaeth.")]],
        doc="language-acts"),
}

SOURCE_QS = [("Who made this source, and when?", "Pwy wnaeth y ffynhonnell hon, a phryd?"),
             ("Why do you think it was made, and for whom?", "Pam, yn eich barn chi, y’i gwnaed, ac i bwy?"),
             ("What does it tell us about Wales at the time?", "Beth mae’n ei ddweud wrthym am Gymru ar y pryd?"),
             ("What can it not tell us? What other sources would help?", "Beth na all ei ddweud wrthym? Pa ffynonellau eraill fyddai’n help?")]

import ages12 as _A12  # the twelve ages: new packs and the packs that changed shape (src/ages12.py)
PACKS.update(_A12.PACKS)


def setup(build_globals):
    g.update(build_globals)


def pack_page(i, era):
    bi, e, section, hero, page = g["bi"], g["e"], g["section"], g["hero"], g["page"]
    eid = era["id"]
    P = PACKS[eid]
    SITE, ERA_ART = g["SITE"], g["ERA_ART"]
    evs = [ev for ev in D.EVENTS if ev[0] == eid]
    keys = [ev for ev in evs if ev[9]]
    tl = sorted(keys + [ev for ev in evs if not ev[9]][:max(0, 12 - len(keys))], key=lambda ev: ev[1])[:12]
    people = [p for p in D.PEOPLE if p[1] == eid][:6]
    places = [p for p in D.PLACES if p["era"] == eid][:6]
    terms = {t["id"]: t for t in AZ.TERMS}
    doc = next((d for d in DC.DOCS if d["id"] == P["doc"]), None)
    href = g["EP"].href

    what = "".join(f'<li><b>{bi(WHAT[k][0], WHAT[k][1])}.</b> {bi(WHAT[k][2], WHAT[k][3])}</li>' for k in P["what"])
    qs = f'<li><b>{bi(g["L"].TEACH[eid]["qEn"], g["L"].TEACH[eid]["qCy"])}</b></li>' + "".join(f"<li>{bi(a, b)}</li>" for a, b in P["qs"])
    top = (f'<p class="lede">{bi(*P["big"])}</p>'
           f'<div class="pk-grid"><div class="pk-box"><h2>{bi("Enquiry questions", "Cwestiynau ymholi")}</h2><ol>{qs}</ol></div>'
           f'<div class="pk-box"><h2>{bi("What matters in Humanities", "Yr hyn sy’n bwysig yn y Dyniaethau")}</h2><ul>{what}</ul>'
           f'<p class="muted">{bi("Ideas to draw out: cynefin, chronology, cause and consequence, change and continuity, significance and interpretation.", "Syniadau i’w codi: cynefin, cronoleg, achos a chanlyniad, newid a pharhad, arwyddocâd a dehongli.")}</p></div></div>'
           f'<p class="no-print pk-print"><button type="button" class="btn solid" data-print="1">{bi("Print this pack or save it as a PDF", "Argraffu’r pecyn neu ei gadw fel PDF")}</button> '
           f'<a class="btn" href="era-{eid}.html">{bi("Read the chapter", "Darllen y bennod")} →</a></p>')

    timeline = ('<ol class="pk-tl">' + "".join(
        f'<li><time>{bi(g["year_label"](ev), g["year_label"](ev, True))}</time><div><a href="{href(ev)}"><b>{bi(ev[5], ev[6])}</b></a><p>{bi(ev[7], ev[8])}</p></div></li>' for ev in tl) + "</ol>")
    cards = ('<div class="pk-cards">' + "".join(f'<div class="pk-card">{bi(ev[5], ev[6])}</div>' for ev in sorted(tl[:8], key=lambda ev: ev[5])) + "</div>")
    ppl = ('<div class="pk-people">' + "".join(
        f'<div class="pk-person wl-card"><p class="pk-d">{e(p[2])}</p><h3><a class="wl-go" href="person-{p[0]}.html">{bi(p[3], p[4])}</a></h3><p class="pk-epi">{bi(p[5], p[6])}</p><p>{bi(p[7], p[8])}</p></div>' for p in people) + "</div>")
    words = ('<dl class="pk-words">' + "".join(
        f'<div><dt>{bi(terms[w]["en"], terms[w]["cy"])}</dt><dd>{bi(terms[w]["dEn"], terms[w]["dCy"])}</dd></div>' for w in P["words"] if w in terms) + "</dl>")
    plc = ('<ul class="pk-places">' + "".join(f'<li><a href="place-{p["id"]}.html"><b>{bi(p["en"], p["cy"])}</b></a> · {bi(p["dEn"], p["dCy"])}</li>' for p in places) + "</ul>"
           + f'<p>{bi("Find the scheduled monuments and castles nearest your school on the historic sites map and the castles map: every one is a story of your cynefin.", "Dewch o hyd i’r henebion cofrestredig a’r cestyll agosaf at eich ysgol ar y map safleoedd hanesyddol a map y cestyll: mae pob un yn stori am eich cynefin.")} '
           f'<a href="sites.html">{bi("Historic sites map", "Map safleoedd hanesyddol")} →</a> · <a href="castles.html">{bi("Castles map", "Map y cestyll")} →</a></p>')
    acts = ""
    for k, (en, cy) in enumerate(STEPS):
        acts += f'<div class="pk-box"><h3>{bi(en, cy)}</h3><ul>' + "".join(f"<li>{bi(a, b)}</li>" for a, b in P["acts"][k]) + "</ul></div>"
    acts += (f'<div class="pk-box"><h3>{bi("More ideas", "Rhagor o syniadau")}</h3><ul>' + "".join(f"<li>{bi(a, b)}</li>" for a, b in zip(g["L"].TEACH[eid]["aEn"], g["L"].TEACH[eid]["aCy"])) + "</ul></div>")
    src_html = ""
    if doc:
        kind, words_en, words_cy = doc["words"]
        src_html = (f'<figure class="pk-source"><blockquote>{bi(words_en, words_cy)}</blockquote>'
                    f'<figcaption><b>{bi(doc["en"], doc["cy"])}</b> · {bi(doc["dEn"], doc["dCy"])} · {bi(doc["kEn"], doc["kCy"])}</figcaption></figure>'
                    + (f'<p class="muted">{bi("This is a summary of the document, not its exact words.", "Crynodeb o’r ddogfen yw hwn, nid ei union eiriau.")}</p>' if kind == "short" else "")
                    + f'<p>{bi(doc["wEn"], doc["wCy"])}</p>'
                    + '<ol>' + "".join(f"<li>{bi(a, b)}</li>" for a, b in SOURCE_QS) + "</ol>"
                    + f'<p><a href="documents.html#doc-{doc["id"]}">{bi("More about this document", "Rhagor am y ddogfen hon")} →</a></p>')
    reads = [x for x in g["F"].STORIES if x["era"] == eid]
    more = ('<ul class="pk-places">' + "".join(f'<li><a href="story-{x["id"]}.html"><b>{bi(x["en"], x["cy"])}</b></a> · {bi(x["sumEn"], x["sumCy"])}</li>' for x in reads[:6]) + "</ul>") if reads else ""

    nxt = D.ERAS[(i + 1) % len(D.ERAS)]
    main = (hero(eid, f'<a href="index.html">{SITE}</a> / <a href="teachers.html">{bi("For teachers", "I athrawon")}</a>', era["ill"],
                 f'Teacher pack {i + 1} of {len(D.ERAS)} · {era["spanEn"]}', f'Pecyn athrawon {i + 1} o {len(D.ERAS)} · {era["spanCy"]}', era["en"], era["cy"],
                 "A printable pack for the Curriculum for Wales: questions, key words, a timeline, people, places, a source to study, activities for each progression step and a quiz.",
                 "Pecyn i’w argraffu ar gyfer y Cwricwlwm i Gymru: cwestiynau, geiriau allweddol, llinell amser, pobl, lleoedd, ffynhonnell i’w hastudio, gweithgareddau ar gyfer pob cam cynnydd a chwis.",
                 art=ERA_ART[eid])
            + section(top, top=True)
            + section(timeline, "Timeline", "Llinell amser")
            + section(f'<p>{bi("Cut out the cards, mix them up and put them in order, oldest first. Then check against the timeline.", "Torrwch y cardiau allan, cymysgwch nhw a’u rhoi mewn trefn, yr hynaf yn gyntaf. Yna gwiriwch yn erbyn y llinell amser.")}</p>' + cards, "Card sort", "Didoli cardiau")
            + section(ppl, "People to know", "Pobl i’w hadnabod")
            + section(words, "Key words", "Geiriau allweddol")
            + section(plc, "Cynefin: places to visit", "Cynefin: lleoedd i ymweld â nhw")
            + (section(src_html, "A source to study", "Ffynhonnell i’w hastudio") if src_html else "")
            + section(f'<div class="pk-grid">{acts}</div>', "Activities", "Gweithgareddau")
            + section(g["quiz_sheet"](era), "Quiz sheet", "Taflen gwis")
            + (section(more, "Long reads for older pupils and teachers", "Erthyglau i ddisgyblion hŷn ac athrawon") if more else "")
            + section(f'<div class="pager"><a class="btn" href="teachers.html">← {bi("All teacher packs", "Pob pecyn athrawon")}</a>'
                      f'<a class="btn solid" href="pack-{nxt["id"]}.html">{bi(nxt["en"], nxt["cy"])} →</a></div>'))
    ld = {"@context": "https://schema.org", "@type": "LearningResource", "name": f'{era["en"]}: teacher pack', "learningResourceType": "Lesson plan",
          "educationalLevel": "Primary and secondary", "inLanguage": ["en", "cy"], "teaches": era["en"],
          "isAccessibleForFree": True, "license": "https://creativecommons.org/licenses/by-nc/4.0/"}
    return page(f"pack-{eid}.html", f'{era["en"]}: teacher pack, Curriculum for Wales · History of Wales',
                f'A free printable pack on {era["en"]} ({era["spanEn"]}) for the Curriculum for Wales: enquiry questions, key words, a timeline, people, places, a source and activities for each progression step.',
                main, era=eid, ld=ld, active="teachers.html", track=f"pack:{eid}")


def pages():
    return {f"pack-{era['id']}.html": pack_page(i, era) for i, era in enumerate(D.ERAS)}


def packs_grid():
    """The row of packs at the top of teachers.html."""
    bi = g["bi"]
    return ('<div class="pk-list">' + "".join(
        f'<a href="pack-{era["id"]}.html" data-era="{era["id"]}"><span>{bi(era["spanEn"], era["spanCy"])}</span><b>{bi(era["en"], era["cy"])}</b>'
        f'<small>{bi("Teacher pack", "Pecyn athrawon")} →</small></a>' for era in D.ERAS) + "</div>")


CSS = """
.pk-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 19rem), 1fr)); gap: 1rem; margin-top: 1.4rem }
.pk-box { background: var(--slate); border: 1px solid var(--line); border-top: 3px solid var(--c, var(--gold)); border-radius: 14px; padding: 1.2rem 1.3rem }
.pk-box h2, .pk-box h3 { font-family: var(--f-display); font-weight: 400; font-size: 1.35rem; margin: 0 0 .6rem }
.pk-box ol, .pk-box ul { margin: 0; padding-left: 1.2rem; display: grid; gap: .5rem; line-height: 1.5 }
.pk-print { margin-top: 1.4rem; display: flex; flex-wrap: wrap; gap: .8rem }
.pk-tl { list-style: none; padding: 0; margin: 0; display: grid; gap: .1rem }
.pk-tl li { display: grid; grid-template-columns: 7.5rem 1fr; gap: 1rem; padding: .7rem 0; border-bottom: 1px solid var(--line) }
.pk-tl time { font-family: var(--f-mono); font-size: .85rem; color: var(--c, var(--gold)) }
.pk-tl p { margin: .2rem 0 0; color: var(--muted) }
.pk-tl a { color: inherit }
.pk-cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(12rem, 1fr)); gap: .6rem }
.pk-card { border: 2px dashed var(--line); border-radius: 10px; padding: 1rem; min-height: 4.5rem; display: grid; place-items: center; text-align: center; font-weight: 600 }
.pk-people { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 17rem), 1fr)); gap: 1rem }
.pk-person { border: 1px solid var(--line); border-radius: 14px; padding: 1rem 1.1rem; background: var(--card) }
.pk-person h3 { font-family: var(--f-display); font-weight: 400; font-size: 1.4rem; margin: .1rem 0 }
.pk-person h3 a { color: inherit; text-decoration: none }
.pk-d { font-family: var(--f-mono); font-size: .78rem; color: var(--c, var(--gold)); margin: 0 }
.pk-epi { font-style: italic; color: var(--muted); margin: 0 0 .4rem }
.pk-words { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 18rem), 1fr)); gap: .8rem; margin: 0 }
.pk-words div { border-left: 3px solid var(--c, var(--gold)); padding: .2rem 0 .2rem .9rem }
.pk-words dt { font-weight: 700 } .pk-words dd { margin: .2rem 0 0; color: var(--muted) }
.pk-places { padding-left: 1.1rem; display: grid; gap: .5rem; line-height: 1.5 }
.pk-source blockquote { margin: 0; padding: 1rem 1.3rem; border-left: 4px solid var(--c, var(--gold)); background: var(--slate); border-radius: 0 12px 12px 0; font-family: var(--f-display); font-size: 1.25rem; line-height: 1.45 }
.pk-source figcaption { color: var(--muted); font-size: .9rem; margin-top: .6rem }
.pk-list { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 15rem), 1fr)); gap: .7rem }
.pk-list a { display: grid; gap: .2rem; padding: 1rem 1.1rem; border: 1px solid var(--line); border-top: 3px solid var(--c); border-radius: 14px; background: var(--slate); color: inherit; text-decoration: none }
.pk-list a span { font-family: var(--f-mono); font-size: .75rem; color: var(--c) }
.pk-list a b { font-family: var(--f-display); font-weight: 400; font-size: 1.35rem }
.pk-list a small { color: var(--muted) }
@media print {
  .pk-box, .pk-person, .pk-list a { background: #fff !important; break-inside: avoid }
  .pk-card { border-color: #888; break-inside: avoid }
  .pk-tl li { break-inside: avoid }
}
"""
