# The royal family trees of Wales (family-trees.html). build.py turns this into the page.
# House rules (see EDITORIAL.md): proud voice, nothing negative about anyone, Arthur is
# Athrwys ap Meurig "in Welsh tradition", contested links given in the tradition's own words.
# For the early generations the old royal genealogies are the only witness, so dates are
# estimates and marked "c.". Every line has English and Welsh.
#
# A person:  T(name, dates, role=(en, cy), note=(en, cy), link="person-x.html", crown=True, kids=[...])
#   name     a string, or (English, Cymraeg) where the name differs
#   crown    True for anyone who appears as a ruler on the kings pages
#   id       anchor on the page; made from the English name when left out
#   goto     (anchor, English, Cymraeg): a link to the same family in another tree
#   gap      True for a row that stands for several generations
# A tree:    dict(id, en, cy, realm, era, introEn, introCy, root)


def T(name, dates="", role=("", ""), note=("", ""), link=None, crown=False, kids=(), id=None, goto=None, gap=False):
    return dict(name=name if isinstance(name, tuple) else (name, name), dates=dates, role=role, note=note,
                link=link, crown=crown, kids=list(kids), id=id, goto=goto, gap=gap)


P = lambda s: f"person-{s}.html"  # noqa: E731

# ------------------------------------------------------------------ Gwynedd
GWYNEDD = T("Merfyn Frych", "d. 844", ("King of Gwynedd", "Brenin Gwynedd"),
  ("Came from Manaw in Welsh tradition, and won the throne through his mother Esyllt, of the line of Cunedda. Married Nest, daughter of the royal house of Powys.",
   "Daeth o Fanaw yn ôl traddodiad Cymru, ac enillodd yr orsedd drwy ei fam Esyllt, o linach Cunedda. Priododd Nest, o dŷ brenhinol Powys."), crown=True, kids=[
 T("Rhodri Mawr", "c. 820–878", ("King of Gwynedd, Powys and Seisyllwg", "Brenin Gwynedd, Powys a Seisyllwg"),
   ("Rhodri the Great. Married Angharad, sister of the last king of Seisyllwg, and became the first king to rule most of Wales. Every later royal house of Wales traced its line to him.",
    "Priododd Angharad, chwaer brenin olaf Seisyllwg, a daeth yn frenin cyntaf i reoli’r rhan fwyaf o Gymru. Olrheiniodd pob tŷ brenhinol diweddarach yng Nghymru ei linach ato ef."),
   P("rhodri-mawr"), crown=True, id="rhodri-mawr", kids=[
  T("Merfyn ap Rhodri", "d. 904", note=("In Welsh tradition he received Powys as his share of his father’s kingdom.", "Yn ôl traddodiad Cymru, cafodd Bowys yn gyfran o deyrnas ei dad.")),
  T("Cadell ap Rhodri", "d. 909", ("King of Seisyllwg", "Brenin Seisyllwg"), ("Father of Hywel Dda and founder of the house of Dinefwr.", "Tad Hywel Dda a sylfaenydd tŷ Dinefwr."),
    crown=True, id="cadell-stub", goto=("cadell-ap-rhodri", "The house of Dinefwr", "Tŷ Dinefwr")),
  T("Anarawd ap Rhodri", "d. 916", ("King of Gwynedd", "Brenin Gwynedd"),
    ("Avenged his father at the battle of Conwy in 881, ‘Dial Rhodri’, Rhodri’s revenge.", "Dialodd am ei dad ym mrwydr Conwy yn 881, ‘Dial Rhodri’."), crown=True, kids=[
   T("Idwal Foel ab Anarawd", "d. 942", ("King of Gwynedd", "Brenin Gwynedd"), ("‘The Bald’. He fell fighting the English in 942.", "‘Y Moel’. Syrthiodd yn ymladd y Saeson yn 942."), crown=True, kids=[
    T("Iago ab Idwal", "d. 979", ("King of Gwynedd", "Brenin Gwynedd"), crown=True),
    T("Ieuaf ab Idwal", "d. 988", ("King of Gwynedd", "Brenin Gwynedd"), crown=True, kids=[
     T("Hywel ab Ieuaf", "d. 985", ("King of Gwynedd", "Brenin Gwynedd"), crown=True),
     T("Cadwallon ab Ieuaf", "d. 986", ("King of Gwynedd", "Brenin Gwynedd"), crown=True)]),
    T("Meurig ab Idwal", "d. 986", kids=[
     T("Idwal ap Meurig", "d. 996", kids=[
      T("Iago ab Idwal ap Meurig", "d. 1039", ("King of Gwynedd", "Brenin Gwynedd"), crown=True, kids=[
       T("Cynan ab Iago", "d. c. 1060", note=("Lived in exile in Dublin, and married Ragnhild, of the royal house of the Norse kings of Dublin.",
                                                "Bu’n byw’n alltud yn Nulyn, a phriododd Ragnhild, o dŷ brenhinol brenhinoedd Llychlynnaidd Dulyn."), kids=[
        T("Gruffudd ap Cynan", "c. 1055–1137", ("King of Gwynedd", "Brenin Gwynedd"),
          ("Born in exile in Ireland. He won Gwynedd at Mynydd Carn in 1081, escaped Norman captivity and left his kingdom strong. Married Angharad, daughter of Owain ab Edwin.",
           "Fe’i ganed yn alltud yn Iwerddon. Enillodd Wynedd ym Mynydd Carn yn 1081, dihangodd o garchar y Normaniaid a gadawodd ei deyrnas yn gryf. Priododd Angharad, merch Owain ab Edwin."),
          P("gruffudd-ap-cynan"), crown=True, kids=[
         T("Gwenllian ferch Gruffudd", "c. 1097–1136", ("Princess of Gwynedd and of Deheubarth", "Tywysoges Gwynedd a Deheubarth"),
           ("Married Gruffudd ap Rhys of Deheubarth. She led an army against the Normans at Cydweli in 1136. Mother of the Lord Rhys.",
            "Priododd Gruffudd ap Rhys o Ddeheubarth. Arweiniodd fyddin yn erbyn y Normaniaid yng Nghydweli yn 1136. Mam yr Arglwydd Rhys."),
           P("gwenllian"), id="gwenllian", goto=("gruffudd-ap-rhys", "Her family in Deheubarth", "Ei theulu yn Neheubarth")),
         T("Susanna ferch Gruffudd", note=("Married Madog ap Maredudd, the last king of all Powys.", "Priododd Madog ap Maredudd, brenin olaf Powys gyfan."),
           goto=("madog-ap-maredudd", "Her family in Powys", "Ei theulu ym Mhowys")),
         T("Cadwaladr ap Gruffudd", "d. 1172", note=("Brother of Owain Gwynedd and his comrade at Crug Mawr in 1136.", "Brawd Owain Gwynedd a’i gymrawd yng Nghrug Mawr yn 1136.")),
         T("Owain Gwynedd", "c. 1100–1170", ("King of Gwynedd", "Brenin Gwynedd"),
           ("Beat the Normans at Crug Mawr in 1136 and turned back Henry II in 1165. The first to call himself Prince of the Welsh.",
            "Trechodd y Normaniaid yng Nghrug Mawr yn 1136 a throi Harri II yn ôl yn 1165. Y cyntaf i’w alw ei hun yn Dywysog y Cymry."),
           P("owain-gwynedd"), crown=True, kids=[
          T("Hywel ab Owain Gwynedd", "d. 1170", ("Prince and poet", "Tywysog a bardd"), ("His poems in praise of Gwynedd are among the finest of the age.", "Mae ei gerddi i Wynedd ymhlith goreuon yr oes."), crown=True),
          T("Angharad ferch Owain", note=("Married Gruffudd Maelor, prince of northern Powys.", "Priododd Gruffudd Maelor, tywysog gogledd Powys."),
            goto=("gruffudd-maelor", "Her family in Powys", "Ei theulu ym Mhowys")),
          T("Madog ab Owain Gwynedd", "fl. 1170", note=("Welsh tradition holds that he sailed west across the ocean and found a new land, three centuries before Columbus.",
                                                          "Yn ôl traddodiad Cymru, hwyliodd tua’r gorllewin dros y cefnfor a darganfod tir newydd, dair canrif cyn Columbus.")),
          T("Cynan ab Owain Gwynedd", "d. 1174", ("Lord of Meirionnydd", "Arglwydd Meirionnydd"), crown=True),
          T("Dafydd ab Owain Gwynedd", "d. 1203", ("Prince of Gwynedd east of the Conwy", "Tywysog Gwynedd i’r dwyrain o Gonwy"), crown=True),
          T("Rhodri ab Owain Gwynedd", "d. 1195", ("Prince of Gwynedd west of the Conwy", "Tywysog Gwynedd i’r gorllewin o Gonwy"), crown=True),
          T("Iorwerth Drwyndwn", "d. c. 1174", note=("Married Marared, daughter of Madog ap Maredudd, king of Powys.", "Priododd Marared, merch Madog ap Maredudd, brenin Powys."), kids=[
           T("Llywelyn Fawr", "1173–1240", ("Prince of Gwynedd, ruler of most of Wales", "Tywysog Gwynedd, rheolwr y rhan fwyaf o Gymru"),
             ("Llywelyn the Great, Llywelyn ab Iorwerth. Married Siwan, daughter of King John of England. The other Welsh rulers did homage to him at Aberdyfi in 1216.",
              "Llywelyn ab Iorwerth. Priododd Siwan, merch y Brenin John o Loegr. Talodd rheolwyr eraill Cymru wrogaeth iddo yn Aberdyfi yn 1216."),
             P("llywelyn-fawr"), crown=True, id="llywelyn-fawr", kids=[
            T("Gwladus Ddu", "d. 1251", note=("‘The Dark’. Married Ralph Mortimer, a lord of the March. Through her the blood of Llywelyn Fawr ran on to Edward IV and to Elizabeth of York, the queen of Harri Tudur.",
                                               "‘Y Ddu’. Priododd Ralph Mortimer, arglwydd yn y Mers. Drwyddi hi rhedodd gwaed Llywelyn Fawr ymlaen at Edward IV ac at Elisabeth o Efrog, brenhines Harri Tudur."),
              id="gwladus-ddu", goto=("bosworth", "The road to Bosworth", "Y ffordd i Bosworth")),
            T("Dafydd ap Llywelyn", "c. 1212–1246", ("Prince of Wales", "Tywysog Cymru"),
              ("Son of Siwan. In 1244 he made Prince of Wales his formal title.", "Mab Siwan. Yn 1244 gwnaeth Tywysog Cymru yn deitl ffurfiol iddo."), crown=True),
            T("Gruffudd ap Llywelyn Fawr", "c. 1198–1244", note=("Llywelyn’s elder son. He married Senana, and their sons carried the fight for Wales on.",
                                                               "Mab hynaf Llywelyn. Priododd Senana, a pharhaodd eu meibion y frwydr dros Gymru."), id="gruffudd-ap-llywelyn-fawr", kids=[
             T("Owain Goch ap Gruffudd", "d. c. 1282", ("Shared the rule of Gwynedd, 1246–1255", "Rhannodd reolaeth Gwynedd, 1246–1255"), crown=True),
             T("Dafydd ap Gruffudd", "1238–1283", ("Prince of Wales", "Tywysog Cymru"),
               ("Led the fight on for six months after Cilmeri, the last prince of an independent Wales.", "Arweiniodd y frwydr am chwe mis wedi Cilmeri, tywysog olaf Cymru annibynnol."), crown=True),
             T("Llywelyn ap Gruffudd", "c. 1223–1282", ("Prince of Wales", "Tywysog Cymru"),
               ("Llywelyn ein Llyw Olaf, Llywelyn the Last. Recognised as Prince of Wales at the Treaty of Montgomery in 1267. Married Eleanor de Montfort. He fell at Cilmeri on 11 December 1282.",
                "Llywelyn ein Llyw Olaf. Fe’i cydnabuwyd yn Dywysog Cymru yng Nghytundeb Trefaldwyn yn 1267. Priododd Eleanor de Montfort. Syrthiodd yng Nghilmeri ar 11 Rhagfyr 1282."),
               P("llywelyn-ap-gruffudd"), crown=True, kids=[
              T("Gwenllian ferch Llywelyn", "1282–1337", ("Princess of Wales", "Tywysoges Cymru"),
                ("Only child of the last prince. She was taken as a baby to the priory of Sempringham in Lincolnshire, and lived there all her life. Wales remembers her today.",
                 "Unig blentyn y tywysog olaf. Fe’i cymerwyd yn faban i briordy Sempringham yn Swydd Lincoln, a bu fyw yno weddill ei hoes. Mae Cymru’n ei chofio heddiw."),
                id="gwenllian-ferch-llywelyn")]),
             T("Rhodri ap Gruffudd", "d. c. 1315", kids=[
              T("Tomas ap Rhodri", "d. 1363", kids=[
               T("Owain Lawgoch", "c. 1330–1378", ("Rightful Prince of Wales", "Tywysog Cymru drwy hawl"),
                 ("Owain of the Red Hand, the last of the house of Aberffraw. A famous captain in the service of France, he claimed his birthright as Prince of Wales in 1372.",
                  "Olaf tŷ Aberffraw. Capten enwog yng ngwasanaeth Ffrainc, a hawliodd ei etifeddiaeth yn Dywysog Cymru yn 1372."),
                 P("owain-lawgoch"), crown=True)])])])])])])])])])])])])])])])

# ------------------------------------------------------------------ Deheubarth
DEHEUBARTH = T("Cadell ap Rhodri", "d. 909", ("King of Seisyllwg", "Brenin Seisyllwg"),
  ("Son of Rhodri Mawr and Angharad. His share of his father’s kingdom was Seisyllwg, the land of Ceredigion and Ystrad Tywi.",
   "Mab Rhodri Mawr ac Angharad. Ei gyfran ef o deyrnas ei dad oedd Seisyllwg, gwlad Ceredigion ac Ystrad Tywi."),
  crown=True, id="cadell-ap-rhodri", goto=("rhodri-mawr", "His father, in the Gwynedd tree", "Ei dad, yng nghoeden Gwynedd"), kids=[
 T("Clydog ap Cadell", "d. 920", ("King of Seisyllwg", "Brenin Seisyllwg"), ("Ruled with his brother Hywel.", "Rheolodd gyda’i frawd Hywel."), crown=True),
 T("Hywel Dda", "c. 880–950", ("King of Deheubarth, then of most of Wales", "Brenin Deheubarth, yna’r rhan fwyaf o Gymru"),
   ("Hywel the Good. Married Elen, daughter of Llywarch ap Hyfaidd, king of Dyfed, and joined Dyfed and Seisyllwg as Deheubarth. He gave Wales its law.",
    "Priododd Elen, merch Llywarch ap Hyfaidd, brenin Dyfed, ac unodd Ddyfed a Seisyllwg yn Ddeheubarth. Rhoddodd ei gyfraith i Gymru."),
   P("hywel-dda"), crown=True, kids=[
  T("Owain ap Hywel Dda", "d. 988", ("King of Deheubarth", "Brenin Deheubarth"),
    ("The oldest Welsh royal genealogies are thought to have been gathered at his court.", "Credir mai yn ei lys ef y casglwyd yr achau brenhinol Cymreig hynaf."), crown=True, kids=[
   T("Maredudd ab Owain", "d. 999", ("King of Deheubarth, Gwynedd and Powys", "Brenin Deheubarth, Gwynedd a Phowys"), ("He ruled most of Wales.", "Rheolodd y rhan fwyaf o Gymru."), crown=True, kids=[
    T("Angharad ferch Maredudd", note=("Mother of two great kings. With Llywelyn ap Seisyll she had Gruffudd, king of all Wales; with Cynfyn ap Gwerystan she had Bleddyn, founder of the royal house of Powys.",
                                         "Mam dau frenin mawr. Gyda Llywelyn ap Seisyll cafodd Gruffudd, brenin Cymru gyfan; gyda Chynfyn ap Gwerystan cafodd Bleddyn, sylfaenydd tŷ brenhinol Powys."),
      id="angharad-ferch-maredudd", kids=[
     T("Gruffudd ap Llywelyn", "c. 1010–1063", ("King of all Wales, 1055–1063", "Brenin Cymru gyfan, 1055–1063"),
       ("Son of Llywelyn ap Seisyll. He took Gwynedd and Powys in 1039 and the rest of Wales by 1055: the one king of all Wales.",
        "Mab Llywelyn ap Seisyll. Cymerodd Wynedd a Phowys yn 1039 a gweddill Cymru erbyn 1055: unig frenin Cymru gyfan."),
       P("gruffudd-ap-llywelyn"), crown=True),
     T("Bleddyn ap Cynfyn", "d. 1075", ("King of Gwynedd and Powys", "Brenin Gwynedd a Phowys"), ("Founder of the house of Mathrafal.", "Sylfaenydd tŷ Mathrafal."),
       crown=True, id="bleddyn-stub", goto=("bleddyn-ap-cynfyn", "The house of Mathrafal", "Tŷ Mathrafal"))])]),
   T("Einion ab Owain", "d. 984", note=("Fell in battle in 984, in his father’s lifetime.", "Syrthiodd mewn brwydr yn 984, yn ystod oes ei dad."), kids=[
    T("Cadell ab Einion", kids=[
     T("Tewdwr ap Cadell", kids=[
      T("Rhys ap Tewdwr", "d. 1093", ("King of Deheubarth", "Brenin Deheubarth"),
        ("Fought beside Gruffudd ap Cynan at Mynydd Carn in 1081. He fell near Brecon in 1093, the last to be called king of Deheubarth.",
         "Ymladdodd ochr yn ochr â Gruffudd ap Cynan ym Mynydd Carn yn 1081. Syrthiodd ger Aberhonddu yn 1093, yr olaf i’w alw’n frenin Deheubarth."), crown=True, kids=[
       T("Nest ferch Rhys", "c. 1085–c. 1136", note=("Called ‘the Helen of Wales’. Her children were forebears of the FitzGeralds of Ireland and of Gerallt Gymro.",
                                                      "Fe’i gelwid yn ‘Helen Cymru’. Roedd ei phlant yn gyndeidiau i’r FitzGeraldiaid yn Iwerddon ac i Erallt Gymro."), link=P("nest"), kids=[
        T("Angharad ferch Nest", note=("Married William de Barri of Manorbier.", "Priododd William de Barri o Faenorbŷr."), kids=[
         T("Gerallt Gymro", "c. 1146–1223", ("Scholar and churchman", "Ysgolhaig ac eglwyswr"),
           ("Gerald of Wales. He wrote the Journey through Wales and the Description of Wales, and fought for St Davids to be an archbishopric.",
            "Ysgrifennodd y Daith drwy Gymru a’r Disgrifiad o Gymru, ac ymladdodd i wneud Tyddewi yn archesgobaeth."), P("gerallt-gymro"))])]),
       T("Gruffudd ap Rhys", "c. 1081–1137", ("Prince of Deheubarth", "Tywysog Deheubarth"),
         ("Married Gwenllian, daughter of Gruffudd ap Cynan of Gwynedd. He rose in 1116 and won back part of his father’s kingdom.",
          "Priododd Gwenllian, merch Gruffudd ap Cynan o Wynedd. Cododd yn 1116 ac enillodd ran o deyrnas ei dad yn ôl."),
         crown=True, id="gruffudd-ap-rhys", goto=("gwenllian", "Gwenllian, in the Gwynedd tree", "Gwenllian, yng nghoeden Gwynedd"), kids=[
        T("Anarawd ap Gruffudd", "d. 1143", ("Prince of Deheubarth", "Tywysog Deheubarth"), crown=True),
        T("Cadell ap Gruffudd", "d. 1175", ("Prince of Deheubarth", "Tywysog Deheubarth"), ("Won back Carmarthen and Llansteffan for the Welsh.", "Enillodd Gaerfyrddin a Llansteffan yn ôl i’r Cymry."), crown=True),
        T("Maredudd ap Gruffudd", "1130–1155", ("Prince of Deheubarth", "Tywysog Deheubarth"), crown=True),
        T(("Rhys ap Gruffudd, the Lord Rhys", "Rhys ap Gruffudd, yr Arglwydd Rhys"), "1132–1197", ("Prince of Deheubarth, ruler of all south Wales", "Tywysog Deheubarth, rheolwr holl dde Cymru"),
          ("Son of Gwenllian. Married Gwenllian, daughter of Madog ap Maredudd of Powys. He held the first eisteddfod, at Cardigan, in 1176.",
           "Mab Gwenllian. Priododd Gwenllian, merch Madog ap Maredudd o Bowys. Cynhaliodd yr eisteddfod gyntaf, yn Aberteifi, yn 1176."),
          P("yr-arglwydd-rhys"), crown=True, id="lord-rhys", kids=[
         T("Gwenllian ferch Rhys", note=("The genealogies make her the wife of Ednyfed Fychan, the steward of Llywelyn Fawr, and so a foremother of the Tudors.",
                                          "Yn ôl yr achau, hi oedd gwraig Ednyfed Fychan, distain Llywelyn Fawr, ac felly un o hynafiaid y Tuduriaid."),
           id="gwenllian-ferch-rhys", goto=("ednyfed-fychan", "The Tudors of Penmynydd", "Tuduriaid Penmynydd")),
         T("Maelgwn ap Rhys", "d. 1231", ("Lord of Ceredigion", "Arglwydd Ceredigion"), crown=True),
         T("Rhys Gryg", "d. 1234", ("Lord of Ystrad Tywi", "Arglwydd Ystrad Tywi"), ("Held Dinefwr, and fought beside Llywelyn Fawr.", "Daliodd Ddinefwr, ac ymladdodd ochr yn ochr â Llywelyn Fawr."), crown=True),
         T("Gruffudd ap Rhys ap Gruffudd", "d. 1201", ("Prince of Deheubarth", "Tywysog Deheubarth"), ("Eldest son of the Lord Rhys.", "Mab hynaf yr Arglwydd Rhys."), crown=True, kids=[
          T("Owain ap Gruffudd", "d. 1235", kids=[
           T("Maredudd ab Owain", "d. 1265", ("Lord in Ceredigion", "Arglwydd yng Ngheredigion"), id="maredudd-ab-owain-1265", kids=[
            T("Owain ap Maredudd", "d. 1275", kids=[
             T("Llywelyn ab Owain", "d. 1309", kids=[
              T("Tomas ap Llywelyn", "d. 1343", note=("Heir of the Lord Rhys in the senior line. His two daughters carried the blood of Deheubarth to Owain Glyndŵr and to the Tudors.",
                                                       "Etifedd yr Arglwydd Rhys yn yr hen linach. Dygodd ei ddwy ferch waed Deheubarth at Owain Glyndŵr ac at y Tuduriaid."), id="tomas-ap-llywelyn", kids=[
               T("Elen ferch Tomas", note=("Married Gruffudd Fychan, lord of Glyndyfrdwy, of the royal house of Powys. Mother of Owain Glyndŵr.",
                                            "Priododd Gruffudd Fychan, arglwydd Glyndyfrdwy, o dŷ brenhinol Powys. Mam Owain Glyndŵr."),
                 id="elen-ferch-tomas", goto=("owain-glyndwr", "Her son Owain Glyndŵr", "Ei mab Owain Glyndŵr")),
               T("Marged ferch Tomas", note=("Married Tudur ap Goronwy of Penmynydd on Ynys Môn. Grandmother of Owain Tudur, and so a foremother of Harri Tudur.",
                                              "Priododd Tudur ap Goronwy o Benmynydd ar Ynys Môn. Mam-gu Owain Tudur, ac felly un o hynafiaid Harri Tudur."),
                 id="marged-ferch-tomas", goto=("tudur-ap-goronwy", "The Tudors of Penmynydd", "Tuduriaid Penmynydd"))])])])])])])])])])])])])])])])

# ------------------------------------------------------------------ Powys
POWYS = T("Bleddyn ap Cynfyn", "d. 1075", ("King of Gwynedd and Powys", "Brenin Gwynedd a Phowys"),
  ("Son of Angharad, daughter of Maredudd ab Owain, and half-brother of Gruffudd ap Llywelyn. Founder of the house of Mathrafal, and a reviser of the laws of Hywel Dda.",
   "Mab Angharad, merch Maredudd ab Owain, a hanner brawd Gruffudd ap Llywelyn. Sylfaenydd tŷ Mathrafal, a diwygiwr cyfreithiau Hywel Dda."),
  crown=True, id="bleddyn-ap-cynfyn", goto=("angharad-ferch-maredudd", "His mother, in the Deheubarth tree", "Ei fam, yng nghoeden Deheubarth"), kids=[
 T("Cadwgan ap Bleddyn", "d. 1111", ("King of Powys", "Brenin Powys"), ("A leader of the great Welsh rising of 1094.", "Un o arweinwyr gwrthryfel mawr 1094."), crown=True),
 T("Iorwerth ap Bleddyn", "d. 1111", ("King of Powys", "Brenin Powys"), crown=True),
 T("Maredudd ap Bleddyn", "d. 1132", ("King of Powys", "Brenin Powys"), crown=True, kids=[
  T("Gruffudd ap Maredudd", "d. 1128", kids=[
   T("Owain Cyfeiliog", "c. 1130–1197", ("Prince of southern Powys, and poet", "Tywysog de Powys, a bardd"),
     ("In his poem Hirlas Owain he toasts his warriors from the long blue drinking horn. He founded the abbey of Ystrad Marchell in 1170.",
      "Yn ei gerdd Hirlas Owain mae’n yfed iechyd ei filwyr o’r corn yfed hir glas. Sefydlodd abaty Ystrad Marchell yn 1170."), crown=True, kids=[
    T("Gwenwynwyn ab Owain", "d. 1216", ("Prince of Powys Wenwynwyn", "Tywysog Powys Wenwynwyn"), ("Gave his name to southern Powys, and hoped to lead all of Wales.", "Rhoddodd ei enw i dde Powys, a gobeithiai arwain Cymru gyfan."), crown=True, kids=[
     T("Gruffudd ap Gwenwynwyn", "d. 1286", ("Prince of Powys Wenwynwyn", "Tywysog Powys Wenwynwyn"), crown=True)])])]),
  T("Madog ap Maredudd", "d. 1160", ("The last king of all Powys", "Brenin olaf Powys gyfan"),
    ("Married Susanna, daughter of Gruffudd ap Cynan of Gwynedd. Praised by his poet Cynddelw Brydydd Mawr. After him the kingdom was divided in two.",
     "Priododd Susanna, merch Gruffudd ap Cynan o Wynedd. Fe’i molwyd gan ei fardd Cynddelw Brydydd Mawr. Ar ei ôl rhannwyd y deyrnas yn ddwy."),
    crown=True, id="madog-ap-maredudd", kids=[
   T("Marared ferch Madog", note=("Married Iorwerth Drwyndwn of Gwynedd. Mother of Llywelyn Fawr.", "Priododd Iorwerth Drwyndwn o Wynedd. Mam Llywelyn Fawr."),
     goto=("llywelyn-fawr", "Her son Llywelyn Fawr", "Ei mab Llywelyn Fawr")),
   T("Gwenllian ferch Madog", note=("Married the Lord Rhys of Deheubarth.", "Priododd yr Arglwydd Rhys o Ddeheubarth."),
     goto=("lord-rhys", "The Lord Rhys", "Yr Arglwydd Rhys")),
   T("Gruffudd Maelor", "d. 1191", ("Prince of Powys Fadog", "Tywysog Powys Fadog"),
     ("Married Angharad, daughter of Owain Gwynedd.", "Priododd Angharad, merch Owain Gwynedd."), crown=True, id="gruffudd-maelor", kids=[
    T("Madog ap Gruffudd Maelor", "d. 1236", ("Prince of Powys Fadog", "Tywysog Powys Fadog"),
      ("Founded the Cistercian abbey of Glyn y Groes (Valle Crucis) near Llangollen in 1201.", "Sefydlodd abaty Sistersaidd Glyn y Groes ger Llangollen yn 1201."), crown=True, kids=[
     T("Gruffudd ap Madog", "d. 1269", ("Prince of Powys Fadog", "Tywysog Powys Fadog"), ("Built the castle of Dinas Brân above Llangollen.", "Cododd gastell Dinas Brân uwchben Llangollen."), crown=True, kids=[
      T("Madog ap Gruffudd", "d. 1277", ("Prince of Powys Fadog", "Tywysog Powys Fadog"), crown=True),
      T("Gruffudd Fychan", "d. 1289", ("Lord of Glyndyfrdwy", "Arglwydd Glyndyfrdwy"), crown=True, kids=[
       T(("Two generations", "Dwy genhedlaeth"), note=("Madog Crypl and Gruffudd of Rhuddallt, lords of Glyndyfrdwy.", "Madog Crypl a Gruffudd o Ruddallt, arglwyddi Glyndyfrdwy."), gap=True, id="glyndyfrdwy", kids=[
        T("Gruffudd Fychan ap Gruffudd", "d. c. 1370", ("Lord of Glyndyfrdwy and Cynllaith", "Arglwydd Glyndyfrdwy a Chynllaith"),
          ("Married Elen, daughter of Tomas ap Llywelyn, of the house of Dinefwr.", "Priododd Elen, merch Tomas ap Llywelyn, o dŷ Dinefwr."),
          goto=("elen-ferch-tomas", "Elen, in the Deheubarth tree", "Elen, yng nghoeden Deheubarth"), kids=[
         T("Owain Glyndŵr", "c. 1359–c. 1415", ("Prince of Wales, 1400–1415", "Tywysog Cymru, 1400–1415"),
           ("Heir of Powys Fadog through his father and of Deheubarth through his mother. Proclaimed Prince of Wales on 16 September 1400. His cousins Rhys and Gwilym ap Tudur fought at his side.",
            "Etifedd Powys Fadog drwy ei dad a Deheubarth drwy ei fam. Fe’i cyhoeddwyd yn Dywysog Cymru ar 16 Medi 1400. Ymladdodd ei gefndryd Rhys a Gwilym ap Tudur wrth ei ochr."),
           P("owain-glyndwr"), crown=True, id="owain-glyndwr")])])])])])])])])])

# ------------------------------------------------------------------ Glywysing and Gwent
GWENT = T("Tewdrig ap Llywarch", "fl. c. 600", ("King of Gwent and Glywysing, and saint", "Brenin Gwent a Glywysing, a sant"),
  ("He gave up the crown for a hermit’s life at Tintern, then took up his sword again and drove the Saxons back at the ford on the Wye.",
   "Rhoddodd y goron heibio am fywyd meudwy yn Nhyndyrn, yna cododd ei gleddyf eto a gyrru’r Saeson yn ôl wrth y rhyd ar afon Gwy."), crown=True, kids=[
 T("Meurig ap Tewdrig", "fl. c. 625", ("King of Gwent and Glywysing", "Brenin Gwent a Glywysing"),
   ("Married Onbrawst, daughter of Gwrgan Fawr of Ergyng.", "Priododd Onbrawst, merch Gwrgan Fawr o Ergyng."), crown=True, kids=[
  T(("Athrwys ap Meurig (Arthur)", "Athrwys ap Meurig (Arthur)"), "c. 605–655", ("King of Gwent and Glywysing", "Brenin Gwent a Glywysing"),
    ("Welsh tradition holds that this king was Arthur, whose court was at Caerleon. Other historians may see it differently.",
     "Yn ôl traddodiad Cymru, y brenin hwn oedd Arthur, a’i lys yng Nghaerllion. Gall haneswyr eraill weld pethau’n wahanol."),
    P("arthur"), crown=True, id="athrwys", kids=[
   T("Morgan Mwynfawr ab Athrwys", "fl. c. 665–710", ("King of Glywysing", "Brenin Glywysing"),
     ("‘The Generous’. Welsh tradition holds that Morgannwg, Glamorgan, takes its name from him.", "‘Mwynfawr’. Yn ôl traddodiad Cymru, ar ei ôl ef yr enwyd Morgannwg."), crown=True, kids=[
    T(("The kings of the south-east", "Brenhinoedd y de-ddwyrain"), note=("The genealogies trace the later kings of Glywysing and Gwent back to this line, among them Ffernfael and Brochfael ap Meurig, who sought the friendship of Alfred of Wessex.",
                                                                           "Mae’r achau’n olrhain brenhinoedd diweddarach Glywysing a Gwent yn ôl i’r llinach hon, yn eu plith Ffernfael a Brochfael ap Meurig, a geisiodd gyfeillgarwch Alfred o Wessex."),
      gap=True, id="gwent-kings", kids=[
     T("Morgan Hen ab Owain", "c. 930–974", ("King of Glywysing and Gwent", "Brenin Glywysing a Gwent"),
       ("Morgan the Old. He joined Glywysing and Gwent into one kingdom and lived to a great age.", "Morgan Hen. Unodd Glywysing a Gwent yn un deyrnas a bu fyw i oedran mawr."), crown=True)])])])])])

# ------------------------------------------------------------------ The Tudors
TUDOR = T("Ednyfed Fychan", "d. 1246", ("Distain (steward) of Gwynedd", "Distain Gwynedd"),
  ("Chief minister of Llywelyn Fawr and of Dafydd ap Llywelyn, and a famous warrior. The genealogies make his wife Gwenllian, daughter of the Lord Rhys.",
   "Prif weinidog Llywelyn Fawr a Dafydd ap Llywelyn, a rhyfelwr enwog. Yn ôl yr achau, ei wraig oedd Gwenllian, merch yr Arglwydd Rhys."),
  id="ednyfed-fychan", goto=("gwenllian-ferch-rhys", "Gwenllian, in the Deheubarth tree", "Gwenllian, yng nghoeden Deheubarth"), kids=[
 T("Goronwy ab Ednyfed", "d. 1268", note=("Distain of Llywelyn ap Gruffudd, the last prince.", "Distain Llywelyn ap Gruffudd, y tywysog olaf."), kids=[
  T("Tudur Hen ap Goronwy", "d. 1311", note=("Lord of Penmynydd on Ynys Môn.", "Arglwydd Penmynydd ar Ynys Môn."), kids=[
   T("Goronwy ap Tudur", "d. 1331", kids=[
    T("Tudur ap Goronwy", "d. 1367", note=("Married Marged, daughter of Tomas ap Llywelyn of the house of Dinefwr, whose sister Elen was the mother of Owain Glyndŵr.",
                                           "Priododd Marged, merch Tomas ap Llywelyn o dŷ Dinefwr, a’i chwaer Elen oedd mam Owain Glyndŵr."),
      id="tudur-ap-goronwy", goto=("marged-ferch-tomas", "Marged, in the Deheubarth tree", "Marged, yng nghoeden Deheubarth"), kids=[
     T(("Rhys and Gwilym ap Tudur", "Rhys a Gwilym ap Tudur"), "d. 1412, 1413", note=("Cousins and captains of Owain Glyndŵr. They took Conwy castle for him on Good Friday 1401.",
                                                                                   "Cefndryd a chapteiniaid Owain Glyndŵr. Cipiwyd castell Conwy ganddynt drosto ar Ddydd Gwener y Groglith 1401.")),
     T("Maredudd ap Tudur", "d. 1406", note=("Married Marged, daughter of Dafydd Fychan.", "Priododd Marged, merch Dafydd Fychan."), kids=[
      T("Owain Tudur", "c. 1400–1461", note=("Served at the court of Henry V and married his widow, Queen Catherine of Valois. He gave his life for the house of Lancaster in 1461.",
                                             "Gwasanaethodd yn llys Harri V a phriododd ei weddw, y Frenhines Catrin o Valois. Rhoddodd ei fywyd dros dŷ Lancaster yn 1461."), id="owain-tudur", kids=[
       T(("Jasper Tudur", "Siasbar Tudur"), "c. 1431–1495", ("Earl of Pembroke", "Iarll Penfro"),
         ("Harri’s uncle and guardian. He kept the boy safe through fourteen years of exile in Brittany and France, and stood beside him at Bosworth.",
          "Ewythr a gwarcheidwad Harri. Cadwodd y bachgen yn ddiogel drwy bedair blynedd ar ddeg o alltudiaeth yn Llydaw a Ffrainc, a safodd wrth ei ochr yn Bosworth.")),
       T(("Edmund Tudur", "Edmwnd Tudur"), "c. 1430–1456", ("Earl of Richmond", "Iarll Richmond"),
         ("Half-brother of King Henry VI. Married Margaret Beaufort, heiress of the house of Lancaster, and died at Carmarthen before his son was born.",
          "Hanner brawd y Brenin Harri VI. Priododd Marged Beaufort, etifeddes tŷ Lancaster, a bu farw yng Nghaerfyrddin cyn geni ei fab."), kids=[
        T("Harri Tudur", "1457–1509", ("King Henry VII, 1485–1509", "Y Brenin Harri VII, 1485–1509"),
          ("Born at Pembroke castle. He landed at Dale in 1485, marched through Wales gathering men, and won the crown at Bosworth under the red dragon. Married Elizabeth of York, heir of Llywelyn Fawr through the Mortimers.",
           "Fe’i ganed yng nghastell Penfro. Glaniodd yn Dale yn 1485, gorymdeithiodd drwy Gymru yn casglu gwŷr, ac enillodd y goron yn Bosworth dan y ddraig goch. Priododd Elisabeth o Efrog, etifeddes Llywelyn Fawr drwy’r Mortimeriaid."),
          P("harri-tudur"), crown=True, id="harri-tudur", kids=[
         T(("Arthur Tudur", "Arthur Tudur"), "1486–1502", ("Prince of Wales", "Tywysog Cymru"),
           ("Named for Arthur, whom Harri honoured as his forefather. He held his court at Ludlow as Prince of Wales.",
            "Fe’i henwyd ar ôl Arthur, a anrhydeddai Harri fel ei gyndad. Cadwodd ei lys yn Llwydlo fel Tywysog Cymru.")),
         T(("Margaret Tudor", "Marged Tudur"), "1489–1541", ("Queen of Scots", "Brenhines yr Alban"),
           ("Her great-grandson James VI of Scotland took the English crown in 1603. Every king and queen since descends from her, and so from Harri Tudur.",
            "Cymerodd ei gor-ŵyr Iago VI o’r Alban goron Lloegr yn 1603. Mae pob brenin a brenhines ers hynny yn disgyn ohoni hi, ac felly o Harri Tudur.")),
         T(("Henry VIII", "Harri VIII"), "1491–1547", ("King of England", "Brenin Lloegr"), ("His three children all wore the crown after him.", "Gwisgodd ei dri phlentyn y goron ar ei ôl."), kids=[
          T(("Elizabeth I", "Elisabeth I"), "1533–1603", ("Queen of England", "Brenhines Lloegr"),
            ("The last of the Tudors. She founded Jesus College, Oxford, for the Welsh in 1571, and in her reign William Morgan put the whole Bible into Welsh (1588).",
             "Yr olaf o’r Tuduriaid. Sefydlodd Goleg yr Iesu, Rhydychen, i’r Cymry yn 1571, ac yn ei theyrnasiad rhoddodd William Morgan y Beibl cyfan yn Gymraeg (1588)."))])])])])])])])])])])

TREES = [
 dict(id="gwynedd", root=GWYNEDD, realm="gwynedd", era="medieval", en="Gwynedd: the house of Aberffraw", cy="Gwynedd: tŷ Aberffraw",
  introEn="From Merfyn Frych and Rhodri Mawr to Llywelyn the Last and Owain Lawgoch. The princes of Wales came from this line, and its daughters married into every other royal house.",
  introCy="O Ferfyn Frych a Rhodri Mawr i Lywelyn ein Llyw Olaf ac Owain Lawgoch. O’r llinach hon y daeth tywysogion Cymru, a phriododd ei merched i bob tŷ brenhinol arall."),
 dict(id="deheubarth", root=DEHEUBARTH, realm="deheubarth", era="kings", en="Deheubarth: the house of Dinefwr", cy="Deheubarth: tŷ Dinefwr",
  introEn="Rhodri Mawr’s son Cadell, his grandson Hywel Dda, and the Lord Rhys. Through two sisters of this line, the blood of Deheubarth came to Owain Glyndŵr and to the Tudors.",
  introCy="Cadell fab Rhodri Mawr, ei ŵyr Hywel Dda, a’r Arglwydd Rhys. Drwy ddwy chwaer o’r llinach hon, daeth gwaed Deheubarth at Owain Glyndŵr ac at y Tuduriaid."),
 dict(id="powys", root=POWYS, realm="powys", era="kings", en="Powys: the house of Mathrafal", cy="Powys: tŷ Mathrafal",
  introEn="Bleddyn ap Cynfyn and his heirs, who ruled Powys from Mathrafal. After 1160 the line divided into Powys Wenwynwyn in the south and Powys Fadog in the north, whose heir was Owain Glyndŵr.",
  introCy="Bleddyn ap Cynfyn a’i etifeddion, a reolodd Bowys o Fathrafal. Wedi 1160 rhannodd y llinach yn Bowys Wenwynwyn yn y de a Phowys Fadog yn y gogledd, ac Owain Glyndŵr oedd ei hetifedd."),
 dict(id="gwent", root=GWENT, realm="glywysing", era="saints", en="Gwent and Glywysing: the house of Tewdrig", cy="Gwent a Glywysing: tŷ Tewdrig",
  introEn="The kings of the south-east, from the saint-king Tewdrig to Athrwys ap Meurig, whom Welsh tradition holds was Arthur.",
  introCy="Brenhinoedd y de-ddwyrain, o’r sant-frenin Tewdrig i Athrwys ap Meurig, sef Arthur yn ôl traddodiad Cymru."),
 dict(id="tudor", root=TUDOR, realm=None, era="tudor", en="The Tudors of Penmynydd", cy="Tuduriaid Penmynydd",
  introEn="From Ednyfed Fychan, steward of Llywelyn Fawr, to Harri Tudur and the throne. Every king and queen of Britain since 1603 descends from this Welsh family of Ynys Môn.",
  introCy="O Ednyfed Fychan, distain Llywelyn Fawr, i Harri Tudur a’r orsedd. Mae pob brenin a brenhines ym Mhrydain ers 1603 yn disgyn o’r teulu Cymreig hwn o Ynys Môn."),
]

# The marriages that bound the royal houses together: (house A, house B, English, Cymraeg, anchor)
MARRIAGES = [
 ("Deheubarth", "Powys", "Angharad, daughter of Maredudd ab Owain, was the mother of Gruffudd ap Llywelyn, king of all Wales, and of Bleddyn ap Cynfyn, who founded the royal house of Powys.",
  "Angharad, merch Maredudd ab Owain, oedd mam Gruffudd ap Llywelyn, brenin Cymru gyfan, a Bleddyn ap Cynfyn, a sefydlodd dŷ brenhinol Powys.", "angharad-ferch-maredudd"),
 ("Gwynedd", "Deheubarth", "Gwenllian, daughter of Gruffudd ap Cynan, married Gruffudd ap Rhys. Their son was the Lord Rhys.",
  "Priododd Gwenllian, merch Gruffudd ap Cynan, â Gruffudd ap Rhys. Eu mab oedd yr Arglwydd Rhys.", "gwenllian"),
 ("Gwynedd", "Powys", "Susanna, daughter of Gruffudd ap Cynan, married Madog ap Maredudd, the last king of all Powys.",
  "Priododd Susanna, merch Gruffudd ap Cynan, â Madog ap Maredudd, brenin olaf Powys gyfan.", "madog-ap-maredudd"),
 ("Powys", "Gwynedd", "Marared, daughter of Madog ap Maredudd, married Iorwerth Drwyndwn. Their son was Llywelyn Fawr.",
  "Priododd Marared, merch Madog ap Maredudd, ag Iorwerth Drwyndwn. Eu mab oedd Llywelyn Fawr.", "llywelyn-fawr"),
 ("Powys", "Deheubarth", "Gwenllian, daughter of Madog ap Maredudd, married the Lord Rhys.",
  "Priododd Gwenllian, merch Madog ap Maredudd, â’r Arglwydd Rhys.", "lord-rhys"),
 ("Deheubarth", "Powys", "Elen, of the line of the Lord Rhys, married Gruffudd Fychan of Powys Fadog. Their son was Owain Glyndŵr.",
  "Priododd Elen, o linach yr Arglwydd Rhys, â Gruffudd Fychan o Bowys Fadog. Eu mab oedd Owain Glyndŵr.", "owain-glyndwr"),
 ("Deheubarth", "Penmynydd", "Marged, Elen’s sister, married Tudur ap Goronwy of Penmynydd. Their grandson was Owain Tudur.",
  "Priododd Marged, chwaer Elen, â Thudur ap Goronwy o Benmynydd. Eu hŵyr oedd Owain Tudur.", "tudur-ap-goronwy"),
 ("Gwynedd", "Mortimer", "Gwladus Ddu, daughter of Llywelyn Fawr, married Ralph Mortimer. Her line led to Elizabeth of York, the queen of Harri Tudur.",
  "Priododd Gwladus Ddu, merch Llywelyn Fawr, â Ralph Mortimer. Arweiniodd ei llinach at Elisabeth o Efrog, brenhines Harri Tudur.", "gwladus-ddu"),
]

# The road to Bosworth: three lines that met in Harri Tudur and his children.
# Each step: (name EN, name CY, dates, note EN, note CY, link)   a step with dates None is a gap row.
ROAD = dict(
 tudur=dict(en="Penmynydd: the line of Ednyfed Fychan", cy="Penmynydd: llinach Ednyfed Fychan", steps=[
  ("Ednyfed Fychan", "Ednyfed Fychan", "d. 1246", "Steward of Llywelyn Fawr", "Distain Llywelyn Fawr", "#ednyfed-fychan"),
  ("Goronwy ab Ednyfed", "Goronwy ab Ednyfed", "d. 1268", "", "", None),
  ("Tudur Hen", "Tudur Hen", "d. 1311", "Lord of Penmynydd", "Arglwydd Penmynydd", None),
  ("Goronwy ap Tudur", "Goronwy ap Tudur", "d. 1331", "", "", None),
  ("Tudur ap Goronwy", "Tudur ap Goronwy", "d. 1367", "", "", "#tudur-ap-goronwy")]),
 rhys=dict(en="Deheubarth: the blood of the Lord Rhys", cy="Deheubarth: gwaed yr Arglwydd Rhys", steps=[
  ("The Lord Rhys", "Yr Arglwydd Rhys", "1132–1197", "Prince of Deheubarth", "Tywysog Deheubarth", "person-yr-arglwydd-rhys.html"),
  ("Five generations of the house of Dinefwr", "Pum cenhedlaeth o dŷ Dinefwr", None, "", "", None),
  ("Tomas ap Llywelyn", "Tomas ap Llywelyn", "d. 1343", "", "", "#tomas-ap-llywelyn"),
  ("Marged ferch Tomas", "Marged ferch Tomas", "", "Sister of Owain Glyndŵr’s mother", "Chwaer mam Owain Glyndŵr", "#marged-ferch-tomas")]),
 llywelyn=dict(en="Gwynedd: the blood of Llywelyn Fawr", cy="Gwynedd: gwaed Llywelyn Fawr", steps=[
  ("Llywelyn Fawr", "Llywelyn Fawr", "1173–1240", "Prince of Gwynedd", "Tywysog Gwynedd", "person-llywelyn-fawr.html"),
  ("Gwladus Ddu", "Gwladus Ddu", "d. 1251", "Married Ralph Mortimer", "Priododd Ralph Mortimer", "#gwladus-ddu"),
  ("Seven generations of the Mortimers, lords of Wigmore and earls of March", "Saith cenhedlaeth o’r Mortimeriaid, arglwyddi Wigmore ac ieirll y Mers", None, "", "", None),
  ("Anne Mortimer", "Anne Mortimer", "1388–1411", "", "", None),
  ("Richard, Duke of York", "Rhisiart, Dug Efrog", "1411–1460", "", "", None),
  ("Edward IV", "Edward IV", "1442–1483", "King of England", "Brenin Lloegr", None),
  ("Elizabeth of York", "Elisabeth o Efrog", "1466–1503", "Queen of Harri Tudur", "Brenhines Harri Tudur", None)]),
 joined=[
  ("Maredudd ap Tudur", "Maredudd ap Tudur", "d. 1406", "Son of Tudur and Marged", "Mab Tudur a Marged", None),
  ("Owain Tudur", "Owain Tudur", "c. 1400–1461", "Married Queen Catherine of Valois", "Priododd y Frenhines Catrin o Valois", "#owain-tudur"),
  ("Edmund Tudur", "Edmwnd Tudur", "c. 1430–1456", "Married Margaret Beaufort", "Priododd Marged Beaufort", None),
  ("Harri Tudur", "Harri Tudur", "1457–1509", "King Henry VII, crowned after Bosworth, 1485", "Y Brenin Harri VII, a goronwyd wedi Bosworth, 1485", "person-harri-tudur.html")],
)
