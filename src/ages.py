# Six ages: adds the Age of Saints and the Age of Kings, and reshapes the neighbouring ages.
# Applied by data.py after everything else is merged.

SAINTS = dict(id="saints", en="The Age of Saints", cy="Oes y Seintiau", spanEn="410 – 800", spanCy="410 – 800", ill="cross",
  blurbEn="After Rome: new kingdoms, wandering saints, the first Welsh poems and the birth of a nation.",
  blurbCy="Ar ôl Rhufain: teyrnasoedd newydd, seintiau crwydrol, y cerddi Cymraeg cyntaf a geni cenedl.",
  storyEn=[
    "When Roman rule ended in 410, the west of Britain did not fall silent. Kingdoms such as Gwynedd, Powys, Dyfed and Gwent grew out of the old tribal lands, ruled by kings like Maelgwn Gwynedd. Along the sea lanes between Ireland, Wales, Cornwall and Brittany travelled holy men and women: Dewi, Illtud, Teilo, Padarn, Beuno and Gwenfrewi, among many others. The churches they founded are remembered in hundreds of place names beginning with Llan.",
    "In these centuries the British language became Welsh, and the people began to call themselves Cymry, ‘fellow countrymen’. The earliest Welsh poetry, by Aneirin and Taliesin, was composed for warriors of the Old North. As Anglo-Saxon kingdoms pushed west, defeats such as the Battle of Chester cut the Welsh off from their kin in the north, and Offa’s Dyke later marked a frontier that still shapes the border."],
  storyCy=[
    "Pan ddaeth rheolaeth Rufain i ben yn 410, ni thawelodd gorllewin Prydain. Tyfodd teyrnasoedd fel Gwynedd, Powys, Dyfed a Gwent o’r hen diroedd llwythol, dan frenhinoedd fel Maelgwn Gwynedd. Ar hyd llwybrau’r môr rhwng Iwerddon, Cymru, Cernyw a Llydaw teithiai dynion a menywod sanctaidd: Dewi, Illtud, Teilo, Padarn, Beuno a Gwenfrewi, ymhlith llawer eraill. Cofir yr eglwysi a sefydlwyd ganddynt mewn cannoedd o enwau lleoedd sy’n dechrau â Llan.",
    "Yn y canrifoedd hyn y trodd y Frythoneg yn Gymraeg, ac y dechreuodd y bobl alw’u hunain yn Gymry, sef ‘cyd-wladwyr’. Cyfansoddwyd y farddoniaeth Gymraeg gynharaf, gan Aneirin a Thaliesin, i ryfelwyr yr Hen Ogledd. Wrth i deyrnasoedd Eingl-Sacsonaidd wthio tua’r gorllewin, torrodd colledion fel Brwydr Caer y Cymry oddi wrth eu perthnasau yn y gogledd, a nododd Clawdd Offa yn ddiweddarach ffin sy’n dal i lunio’r gororau."])

KINGS = dict(id="kings", en="The Age of Kings", cy="Oes y Brenhinoedd", spanEn="800 – 1100", spanCy="800 – 1100", ill="crown",
  blurbEn="Rhodri, Hywel and Gruffudd: kings who drew Wales together against Vikings and English.",
  blurbCy="Rhodri, Hywel a Gruffudd: brenhinoedd a dynnodd Gymru ynghyd yn erbyn y Llychlynwyr a’r Saeson.",
  storyEn=[
    "In the ninth century Wales was still a patchwork of kingdoms, but a few rulers began to stitch it together. Rhodri Mawr inherited Gwynedd and gained Powys and Seisyllwg, and in 856 he defeated a Viking army on Ynys Môn. His grandson Hywel Dda ruled most of Wales in peace and gave his name to the Welsh laws, which protected the rights of women and children and settled quarrels with compensation rather than revenge.",
    "Vikings raided the coasts and left their names on places such as Swansea, Anglesey and the islands of Skokholm and Skomer. In 1055 Gruffudd ap Llywelyn became the only king ever to rule all of Wales, before he was killed in 1063 after an English invasion. Within a generation the Normans had arrived, and the age of kings gave way to the age of castles and princes."],
  storyCy=[
    "Yn y nawfed ganrif roedd Cymru’n dal yn glytwaith o deyrnasoedd, ond dechreuodd ambell reolwr eu gwnïo ynghyd. Etifeddodd Rhodri Mawr Wynedd ac enillodd Bowys a Seisyllwg, ac yn 856 trechodd fyddin o Lychlynwyr ar Ynys Môn. Rheolodd ei ŵyr Hywel Dda y rhan fwyaf o Gymru mewn heddwch, a rhoddwyd ei enw ar gyfreithiau Cymru, a oedd yn diogelu hawliau menywod a phlant ac yn setlo cwerylon drwy iawndal yn hytrach na dial.",
    "Ysbeiliodd y Llychlynwyr yr arfordir a gadael eu henwau ar leoedd fel Swansea, Anglesey ac ynysoedd Sgogwm a Sgomer. Yn 1055 daeth Gruffudd ap Llywelyn yr unig frenin erioed i reoli Cymru gyfan, cyn ei ladd yn 1063 ar ôl ymosodiad gan y Saeson. O fewn cenhedlaeth roedd y Normaniaid wedi cyrraedd, ac ildiodd oes y brenhinoedd i oes y cestyll a’r tywysogion."])

PRINCES_P1_EN = "From 1100 the Welsh rulers fought a long contest with the Norman lords who had seized the south and east and built castles and lordships in the March. In the Great Revolt of 1136 Gwenllian died leading an army, and Owain Gwynedd and the Lord Rhys made Gwynedd and Deheubarth strong again. Their courts were full of poets, and in 1176 the Lord Rhys held the first recorded eisteddfod at Cardigan."
PRINCES_P1_CY = "O 1100 ymlaen bu rheolwyr Cymru mewn ymryson hir â’r arglwyddi Normanaidd a oedd wedi cipio’r de a’r dwyrain ac wedi codi cestyll ac arglwyddiaethau yn y Mers. Yng Ngwrthryfel Mawr 1136 bu farw Gwenllian yn arwain byddin, a gwnaeth Owain Gwynedd a’r Arglwydd Rhys Wynedd a Deheubarth yn gryf unwaith eto. Roedd eu llysoedd yn llawn beirdd, ac yn 1176 cynhaliodd yr Arglwydd Rhys yr eisteddfod gyntaf y gwyddys amdani yn Aberteifi."

SAINTS_PEOPLE = {"dewi-sant", "taliesin", "aneirin", "illtud", "maelgwn-gwynedd"}
KINGS_PEOPLE = {"rhodri-mawr", "asser", "hywel-dda", "gruffudd-ap-llywelyn", "gruffudd-ap-cynan"}

NEW_PLACES = [
 dict(id="offasdyke", en="Offa’s Dyke", cy="Clawdd Offa", era="saints", lat=52.343, lon=-3.049, year="c. 784", ill="mtn", src="Offa%27s_Dyke",
  dEn="The great earthwork raised by King Offa of Mercia along the Welsh frontier. Long stretches survive, followed today by a national trail.",
  dCy="Y clawdd pridd mawr a godwyd gan y Brenin Offa o Fersia ar hyd ffin Cymru. Mae darnau hir wedi goroesi, a llwybr cenedlaethol yn eu dilyn heddiw."),
 dict(id="eliseg", en="Pillar of Eliseg", cy="Piler Eliseg", era="kings", lat=52.989, lon=-3.186, year="c. 850", ill="stone", src="Pillar_of_Eliseg",
  dEn="A broken stone cross near Valle Crucis, raised by Cyngen of Powys in honour of his great-grandfather Elisedd. Its worn Latin text traced the kings of Powys back to Roman times.",
  dCy="Croes garreg doredig ger Glyn y Groes, a godwyd gan Gyngen o Bowys er anrhydedd i’w hen dad-cu Elisedd. Roedd ei harysgrif Ladin dreuliedig yn olrhain brenhinoedd Powys yn ôl i oes Rhufain."),
 dict(id="maenachwyfan", en="Maen Achwyfan", cy="Maen Achwyfan", era="kings", lat=53.295, lon=-3.300, year="c. 1000", ill="cross", src="Maen_Achwyfan_Cross",
  dEn="The tallest wheel-headed cross in Britain, carved around 1000 near Whitford in Flintshire, with patterns that show Viking influence.",
  dCy="Y groes ben-olwyn dalaf ym Mhrydain, a gerfiwyd tua 1000 ger Chwitffordd yn Sir y Fflint, gyda phatrymau sy’n dangos dylanwad y Llychlynwyr."),
]

TEACH = {
 "saints": dict(qEn="How did the Age of Saints shape Wales?", qCy="Sut luniodd Oes y Seintiau Gymru?",
  aEn=["Find three places near you whose names begin with Llan, and find out which saint each is named after.", "Read part of Y Gododdin in translation and discuss what it tells us about what warriors valued.", "Debate: does Offa’s Dyke still matter today?"],
  aCy=["Dewch o hyd i dri lle yn agos atoch sy’n dechrau â Llan, a darganfod ar ôl pa sant yr enwyd pob un.", "Darllenwch ran o’r Gododdin a thrafodwch beth mae’n ei ddweud am yr hyn roedd rhyfelwyr yn ei werthfawrogi.", "Dadl: ydy Clawdd Offa’n dal yn bwysig heddiw?"]),
 "kings": dict(qEn="How did Welsh kings hold their kingdoms together?", qCy="Sut cadwodd brenhinoedd Cymru eu teyrnasoedd ynghyd?",
  aEn=["Use the Kingdoms map to see how Rhodri Mawr, Hywel Dda and Gruffudd ap Llywelyn changed the shape of Wales.", "Read about the laws of Hywel Dda: choose one law and decide whether it was fair.", "Find Viking place names on the map of Wales and explain where they came from."],
  aCy=["Defnyddiwch fap y Teyrnasoedd i weld sut newidiodd Rhodri Mawr, Hywel Dda a Gruffudd ap Llywelyn siâp Cymru.", "Darllenwch am gyfreithiau Hywel Dda: dewiswch un gyfraith a phenderfynwch a oedd hi’n deg.", "Dewch o hyd i enwau lleoedd Llychlynnaidd ar fap Cymru ac esboniwch o ble y daethant."]),
}
