# The clearing of Mynydd Epynt in 1940: the long read (story-epynt.html), its timeline events, the fuller place page
# text for place-epynt.html, and the sources beside the claims.
# features.py adds STORY to the long reads; data.py adds EVENTS to the timeline; long.py takes PLACE_LONG;
# cites.py takes CITES.
# Asked for by Ifan, 13 November 2026: "A page on Mynydd Epynt and how the farmers were made to leave Epynt".
# Told like the Tryweryn long read (src/tryweryn.py). House rules (EDITORIAL.md): proud; nothing negative about the people
# of Welsh history; the Welsh are never "Celts".
# Sources checked November 2026 (keys in CITES below):
#   NFU Cymru, "Epynt: A lost community" (Clare Williams, 29 June 2020): 219 people, 54 farms; letters from 2 March 1940,
#     the day after St David's Day at Capel y Babell; a month's extension; school and chapel closed in June; last family
#     left Sunday 30 June, guns from Monday 1 July; Thomas Morgan of Glandŵr; Gwybedog; Neuadd Llwyd and Ivor Morgan
#     (Lee Waters's grandfather); Beryl Lake, the last baby born on Epynt (Ben Lake's grandmother); boundary moved west.
#   Angharad Tomos, Nation.Cymru, 2 June 2020: the officer in September 1939 and the farm names; deadline end of April;
#     Plygain at Capel y Babell, Christmas 1939; Peate and the old woman of Waunlwyd, aged 82, "mae'n ddiwedd byd yma";
#     Glyn Powell; the Atgofion Epynt page; the mock village with its mock graves.
#   Literature Wales, Ifor ap Glyn, "Remember Epynt" (30 June 2020): 219 people, 54 farms, Cilieni school, Babell chapel.
#   Llangammarch Wells community site, "Epynt clearances": 54 homes, 219 people, a school, a church and the Drovers Arms
#     closed; acquisition complete by 30 June 1940; SENTA.
#   Hansard, House of Commons, 25 April 1940, vol. 360 cc349-50: Jim Griffiths's question on Welsh land taken.
#   Coflein NPRN 307124 (Drover's Arms): four droving inns, the Griffin, Tafarn y Mynydd, the Spite and the Drovers Arms;
#     exterior restored by the MoD in the 1990s.
#   Amgueddfa Cymru, Collections Online F2022.5.31: Iorwerth Peate's negatives, Epynt, June 1940.
#   Nation.Cymru review of Herbert Hughes, Mynydd Epynt a'r Troad Allan yn 1940 (Y Lolfa 2023; Gomer 1997), 29 July 2023:
#     Peate measured and photographed the homes on the last day; Cilieni school's first Welsh books in 1903; T. C. Thomas's
#     play Sound of Stillness.
#   Brecon & Radnor Express, 5 February 2026 (Grŵp Epynt, 85 years): the slates with the farm names put back, about 300
#     visitors, the slate listing everyone at the Epynt Centre, a tree, Dyfed Cynan's Iorwerth o'r Epynt.
#   Wikipedia "Epynt clearance" and "Mynydd Epynt" with their sources: Euros Lewis, "the death blow to Welsh-speaking
#     Breconshire"; mock village 1988; Disgwylfa reopened as the Epynt Centre in 2009; the Epynt Way 2004.
#   Nation.Cymru, 15 June 2026 (Colli Epynt): the Preseli plans six years later and Brwydr y Preseli, abandoned.
#   Diocese of St Davids, Pobl Dewi, September 2025: Waldo Williams's Preseli, 1946.
# The farm count is given as 54 homes (most sources; some say 52 farms received notices). The people as 219.
# Paragraph codes (see prose() in build.py): "## Heading", "> Quote | Source", "|| Left | Right", "!! picture key".

_SA2 = ("CC BY-SA 2.0", "https://creativecommons.org/licenses/by-sa/2.0/")
_SA4 = ("CC BY-SA 4.0", "https://creativecommons.org/licenses/by-sa/4.0/")

# Pictures from Wikimedia Commons, found with tools/commons_research.py (November 2026): file, maker, licence, licence link,
# caption EN, caption CY, width, height.
FIGS = {
 "ep-babell-stone": ("Babell chapel - geograph.org.uk - 1176170.jpg", "Graham Horn", *_SA2,
   "The datestone of Capel y Babell, still on the site today: ‘Pabell, Addoldy y Trefnyddion Calfinaidd, Adeiladwyd A.D. 1857’, the Calvinistic Methodists’ house of worship, built in 1857",
   "Carreg ddyddiad Capel y Babell, sydd ar y safle hyd heddiw: ‘Pabell, Addoldy y Trefnyddion Calfinaidd, Adeiladwyd A.D. 1857’", 640, 428),
 "ep-red-flag": ("Red flag at Sennybridge Artillery Range - geograph.org.uk - 7766637.jpg", "Alan Hughes", *_SA2,
   "The red flag flies at the edge of the range on Mynydd Epynt: when it is up, the guns are firing",
   "Mae’r faner goch yn chwifio ar ymyl y maes tanio ar Fynydd Epynt: pan fydd i fyny, mae’r gynnau’n tanio", 1400, 1050),
 "ep-peate": ("Iorwerth C Peate gyda'i greadigaeth, Amgueddfa Werin Cymru yn Sain Ffagan (1465876).jpg", "Geoff Charles", *_SA4,
   "Iorwerth Peate at St Fagans, the museum he created, photographed by Geoff Charles. In June 1940 he went up to Epynt to record the homes before they were lost",
   "Iorwerth Peate yn Sain Ffagan, yr amgueddfa a greodd, llun gan Geoff Charles. Ym Mehefin 1940 aeth i fyny i Epynt i gofnodi’r cartrefi cyn eu colli", 1250, 1252),
 "ep-drovers": ("Drover's Arms Inn on Epynt mountain - geograph.org.uk - 157616.jpg", "Nigel Davies", *_SA2,
   "The Drovers Arms, the old drovers’ inn that closed in 1940. It still stands on the range, its outside restored, its inside a shelter for soldiers",
   "Y Drovers Arms, hen dafarn y porthmyn a gaeodd yn 1940. Mae’n dal i sefyll ar y maes, a’i du allan wedi’i adfer a’i du mewn yn gysgod i filwyr", 640, 480),
 "ep-babell": ("Babell chapel - geograph.org.uk - 1176161.jpg", "Graham Horn", *_SA2,
   "The site of Capel y Babell today, with the graves of the people of the mountain still among the trees",
   "Safle Capel y Babell heddiw, a beddau pobl y mynydd yn dal i sefyll ymysg y coed", 640, 427),
}

STORY = dict(id="epynt", era="modern", art="horse", mins=16, figs=FIGS,
  people=["iorwerth-peate", "jim-griffiths", "waldo-williams", "john-penry", "gwynfor-evans"],
  places=["epynt", "celyn"],
  events=["The letters come to Epynt", "The clearing of Epynt", "Epynt remembered, 85 years on"],
  links=[("place-epynt.html", "Mynydd Epynt on the map", "Mynydd Epynt ar y map"),
         ("story-tryweryn.html", "Cofiwch Dryweryn: the drowning of Capel Celyn", "Cofiwch Dryweryn: boddi Capel Celyn"),
         ("person-iorwerth-peate.html", "Iorwerth Peate", "Iorwerth Peate"),
         ("person-waldo-williams.html", "Waldo Williams, poet of Preseli", "Waldo Williams, bardd y Preselau"),
         ("story-welsh-not.html", "The Welsh Not, and how the language was kept alive", "Y Welsh Not, a sut y cadwyd yr iaith yn fyw"),
         ("story-language.html", "The story of the Welsh language", "Hanes yr iaith Gymraeg"),
         ("era-modern.html", "Modern Wales", "Cymru fodern")],
  en="Cofiwch Epynt: the clearing of the mountain, 1940",
  cy="Cofiwch Epynt: clirio’r mynydd, 1940",
  sumEn="In the summer of 1940 the War Office took Mynydd Epynt in Breconshire for an artillery range. 219 people from 54 homes, a whole Welsh-speaking community with its chapel, school and inn, were made to leave, and they never went back. The story of the people of the mountain, and how Wales remembers them.",
  sumCy="Yn haf 1940 cymerodd y Swyddfa Ryfel Fynydd Epynt ym Mrycheiniog yn faes tanio. Gorfodwyd 219 o bobl o 54 o gartrefi, cymuned Gymraeg gyfan gyda’i chapel, ei hysgol a’i thafarn, i adael, ac nid aethant byth yn ôl. Hanes pobl y mynydd, a sut y mae Cymru’n eu cofio.",
  pEn=[
   "Drive over Mynydd Epynt today and you will see red flags, warning signs and the tracks of tanks. Listen, and you may hear the guns. What you will not see are the farms. Until the summer of 1940 this upland in the north of old Brycheiniog was home to a Welsh-speaking community that had farmed it for generations, with its chapel, its school, its inn, its eisteddfod and its own way of life. In a few months it was gone. The people were given their notices, the mountain was taken for an army range, and the day after the last family left, the shells began to fall. This is their story, and why Wales says Cofiwch Epynt, remember Epynt.",
   "|| The mountain | Mynydd Epynt, the high plateau between the Usk, the Irfon and the Wye, in Brycheiniog (Breconshire)",
   "|| The community | 219 people in 54 homes, with Capel y Babell, Cilieni school and the Drovers Arms",
   "|| The land taken | About 30,000 acres, for what became the Sennybridge Training Area",
   "|| The letters | From 2 March 1940, the day after St David’s Day",
   "|| The last day | Sunday 30 June 1940; the guns began on Monday 1 July",
   "|| The words that stayed | ‘Mae’n ddiwedd byd yma’: it is the end of the world here",
   "|| Remembered | 80 years on in 2020; 85 years on in 2025, with the farm names put back on the land",
   "## The way of horses",
   "Mynydd Epynt is a long, high plateau, between 400 and 478 metres above the sea, lying between Builth and Llanwrtyd to the north and Sennybridge and Brecon to the south. The rivers Cilieni, Nant Brân, Ysgir and Honddu run off it to the Usk, and the Duhonw runs down to the Wye. Its name is old and its meaning is argued over, but the best-known reading is ‘the way of horses’, from an old word for a horse.[[cite:ep-wiki-mynydd]]",
   "People have crossed it since the Bronze Age, whose cairns and stones still stand at the meeting of the old tracks. Later the same tracks became drovers’ roads, along which the cattle and sheep of Wales were walked to the markets of England, and four inns stood on the northern side of the mountain to serve the drovers: the Griffin, Tafarn y Mynydd, the Spite and the Drovers Arms.[[cite:ep-coflein-drovers]] On its southern slopes, at Cefn Brith near Llangamarch, John Penry was born in 1563, the man who pleaded with Queen Elizabeth for preachers who would speak to the people of Wales in their own language.",
   "## A Welsh world on the mountain",
   "In 1939 the mountain was alive. On farms with names like Ffos yr Hwyaid, Gilfach yr Haidd, Cefnbryn Isaf, Llwynteg Uchaf, Glandŵr, Gwybedog and Waunlwyd, families farmed sheep and cattle on land their fathers and grandfathers had farmed before them. They spoke Welsh at home, in the fields and at chapel.[[cite:ep-tomos]]",
   "The heart of it was Capel y Babell, built by the Calvinistic Methodists in 1857. There the people were baptised, married and buried; there they held their eisteddfod and their gymanfa ganu. At four o’clock on Christmas morning 1939, the last Christmas any of them would spend on the mountain, they walked and rode through the dark to the Plygain at the Babell, to sing the old carols as their people had for centuries.[[cite:ep-tomos]] Children went to Cilieni school, where Welsh books had first been ordered in 1903, and the families looked after one another: a white sheet hung outside a house told the neighbours that help was needed there.[[cite:ep-review-hughes,ep-wiki-mynydd]]",
   "!! ep-babell-stone",
   "## The officer who could not spell the names",
   "In September 1939, as war began, an army officer came to the school, driven in a small brown car. He had a list of the farms of the mountain, and he could not spell their names, so he asked the schoolchildren to help him find them on the map.[[cite:ep-tomos]] Nobody yet knew why.",
   "By the new year the people were worried. On 1 March 1940 they gathered at Capel y Babell, as always, to keep St David’s Day. The next day, 2 March, the letters began to arrive.[[cite:ep-nfu]] The War Office needed the mountain for artillery training, for the war. Every family was to leave its home by the end of April.[[cite:ep-tomos]]",
   "!! ep-red-flag",
   "## Wales speaks up",
   "It was lambing time. Asking a hill farmer to move his flock in April is asking him to lose a year’s work, and the families asked for more time. They were given one more month, and then a final day: 30 June 1940.[[cite:ep-nfu,ep-tomos]]",
   "Welsh members of Parliament and public men spoke up for them, but in the spring of 1940 every objection was answered with the war.[[cite:ep-wiki-clearance]] On 25 April 1940 Jim Griffiths, member for Llanelli, asked the Minister of Agriculture in the House of Commons how much land in Wales the government departments had taken and how many farm people had lost their homes, and he begged him to ask them to look for other sites. The minister answered that some 49,000 acres had been taken in three years, that he had no figure for the people displaced, and that he did not feel justified in urging the departments to exclude Wales.[[cite:ep-hansard-1940]]",
   "## The last days",
   "In June the school and the chapel closed, and the army began pulling out the hedges.[[cite:ep-nfu]] One by one the families went down off the mountain with their furniture and their animals. One woman would not go without her own front door, and took it with her.[[cite:ep-tomos]]",
   "One man came to see them go and to keep what he could. Iorwerth Peate of the National Museum of Wales, the scholar of Welsh folk life who would later found the Folk Museum at St Fagans, came up to Epynt in June 1940 to measure and photograph the homes before they were lost. His photographs are kept by Amgueddfa Cymru today.[[cite:ep-review-hughes,ep-museum-peate]] At Waunlwyd he found an old woman of eighty-two sitting in her armchair, weeping. She had been born in that house, and so had her father and her grandfather. She asked him where he came from. When he said Cardiff, she told him to go back there as fast as he could, and said:[[cite:ep-tomos]]",
   "> Mae’n ddiwedd byd yma. (It is the end of the world here.) | An old woman of Waunlwyd, aged 82, to Iorwerth Peate, June 1940",
   "Those words became the name of the story. Herbert Hughes gave them to his history of the clearing, ‘Mae’n ddiwedd byd yma’, in 1997.",
   "!! ep-peate",
   "On Sunday 30 June 1940, a grey day, the last family left the mountain. On Monday 1 July the guns began firing.[[cite:ep-nfu,ep-tomos]] In all, 219 people from 54 homes had gone, and with them Capel y Babell, Cilieni school, a church and the Drovers Arms.[[cite:ep-llangammarch,ep-lw-poem]] The same summer the bombs began to fall on Cardiff and Swansea.",
   "## The fire on the hearth at Glandŵr",
   "Many believed they would come home when the war was over. Some left their keys in the doors, and some kept their houses fit to live in and went on ploughing their fields.[[cite:ep-wiki-clearance]] Thomas Morgan of Glandŵr went back day after day to light the fire in his own hearth, to keep the house alive. The soldiers warned him again and again. Then one day he came back and the house was gone. An officer told him: ‘We’ve blown up the farmhouse. You won’t need to come here anymore.’[[cite:ep-nfu]]",
   "Elwyn Davies of Merthyr Cynog was ten years old in 1940. His grandmother’s home was Gwybedog. ‘Just a week after she left,’ he remembered, ‘they flattened her house.’[[cite:ep-nfu]]",
   "## Scattered",
   "The families went where they could find a farm or a roof: to the valleys below the mountain, to Radnorshire, and many to Carmarthenshire, some twenty miles and more from home. Ivor Morgan of Neuadd Llwyd, a young farmer of thirty-two, went to Llwyn Wennol at Gwynfe; his grandson, the Senedd member Lee Waters, said that Epynt stayed alive in his mind to the end of his days. The last baby born on the mountain, Beryl Lake, was the grandmother of Ben Lake, member of Parliament for Ceredigion, who has called the clearing a significant but often overlooked chapter in the history of Wales.[[cite:ep-nfu]]",
   "Glyn Powell’s family was among those put out in 1940. In the 1950s he was sent back to Epynt as a soldier on National Service, and slept in the cowshed of Ffos yr Hwyaid, a farm he had known as a home. In his nineties he was still campaigning, and he passed the story on to his daughter and her children.[[cite:ep-tomos]]",
   "## The language pushed back",
   "In 1940 the north of Breconshire was Welsh-speaking country, and Epynt was one of its strongholds.[[cite:ep-nation-2026]] When its people were scattered, many of them into places where English was spoken more, the Welsh-speaking heartland, Y Fro Gymraeg, lost ground in the east, and the line where Welsh was the language of everyday life moved west.[[cite:ep-nfu,ep-wiki-clearance]] A local way of speaking Welsh was lost with them, and so were the names: the army called the old farms Farm 1, Farm 2 and so on.[[cite:ep-brecon-85]]",
   "The storyteller and historian Euros Lewis, who has gathered the memories of the people of the mountain, called the clearing ‘the death blow to Welsh-speaking Breconshire’.[[cite:ep-wiki-clearance]]",
   "## The mountain under the guns",
   "Mynydd Epynt became the heart of the Sennybridge Training Area, the largest military training area in Wales, and so it remains. Most of the old buildings, the farmhouses, the chapels and their graveyards, were destroyed by shellfire and explosives. In 1988 the army built a mock village on the mountain for training in street fighting, with a mock chapel and mock gravestones.[[cite:ep-wiki-clearance,ep-tomos]] Sheep still graze the range, but the old rights of way across it are closed.[[cite:ep-wiki-mynydd,ep-wiki-clearance]]",
   "A few things survive. The Drovers Arms still stands; the Ministry of Defence restored its outside in the 1990s, though inside it is empty.[[cite:ep-coflein-drovers]] Disgwylfa, one of the farms taken in 1940, became the Epynt Centre, and in 2004 the Epynt Way was opened, a path of some 65 kilometres around the edge of the range for walkers, riders and cyclists.[[cite:ep-wiki-mynydd,ep-epyntway]]",
   "!! ep-drovers",
   "## Never again: the Preseli hills",
   "Epynt taught Wales what could happen when the land was wanted in London. When the war ended, the War Office wanted more: land near Trawsfynydd, Tregaron and Llyn y Fan Fach, and above all the Preseli hills of Pembrokeshire. This time Wales was ready. In 1947 Plaid Cymru vowed not to give an inch.[[cite:ep-wiki-clearance]] In the Preseli hills the farmers, the chapels and the people of the district stood together in Brwydr y Preseli, the battle for Preseli, and the poet Waldo Williams wrote his great poem Preseli in 1946 in defence of the hills of his boyhood. The plan was dropped.[[cite:ep-nation-2026,ep-waldo]] What Epynt lost, Preseli kept.",
   "Twenty-five years after Epynt, another Welsh-speaking community, Capel Celyn in Cwm Tryweryn, was taken from its people, this time for Liverpool’s water. By then the whole nation stood up for it, and Cofiwch Dryweryn became the cry of Wales. Cofiwch Epynt is its older sister.",
   "## Cofiwch Epynt",
   "For years the story of Epynt was told mostly at the firesides of the families who had lost their homes. Then it was written down. Herbert Hughes gathered the memories, the photographs and the names of the farms and where every family went, and published ‘Mae’n ddiwedd byd yma’: Mynydd Epynt a’r Troad Allan yn 1940 in 1997, and in English An Uprooted Community: A History of Epynt in 1998. Y Lolfa has published both books again, the Welsh one in 2023.[[cite:ep-review-hughes]] T. C. Thomas made the story of Glandŵr into a play, Sound of Stillness.[[cite:ep-review-hughes]]",
   "In June 2020, eighty years on, the National Poet of Wales, Ifor ap Glyn, wrote a poem in Welsh and English for the 219 people and the 54 farms. The English version, Remember Epynt, begins: ‘Now only shells / till the soil at Llwynteg-ucha’.[[cite:ep-lw-poem]] Glyn Powell’s daughter Bethan, with Menter Iaith Brycheiniog, made the Atgofion Epynt page, where the names of the lost farms are remembered day by day.[[cite:ep-tomos]] In 2022 ITV Wales told the story in its series Vanished Wales.[[cite:ep-itv]]",
   "In 2025, eighty-five years on, the descendants of the families came together as Grŵp Epynt. At an open day on the range, slates carved with the old Welsh names of the farms lined the way; they were then taken back and set at the places where the farms had stood, so that Farm 1 and Farm 2 have their names again. About three hundred people came, many of them the children and grandchildren of the people of 1940, and they visited the site of Capel y Babell, Cilieni school and the Drovers Arms. At the Epynt Centre a slate bearing the names of everyone who had to leave was unveiled, and a tree was planted. A play, Iorwerth o’r Epynt, went round the schools of the district.[[cite:ep-brecon-85]]",
   "!! ep-babell",
   "The people of Epynt asked for nothing but to stay in their own homes and speak their own language on their own mountain. They gave up their homes for a war they did not choose, and most never saw them again. But they are not forgotten. Their farms have their names back, their story is told in Welsh and in English, and on walls and road signs in Brycheiniog two words are painted that every Welsh person should know. Cofiwch Epynt.",
  ],
  pCy=[
   "Gyrrwch dros Fynydd Epynt heddiw ac fe welwch faneri coch, arwyddion rhybudd ac olion tanciau. Gwrandewch, ac efallai y clywch y gynnau. Yr hyn na welwch yw’r ffermydd. Hyd haf 1940 roedd yr ucheldir hwn yng ngogledd yr hen Frycheiniog yn gartref i gymuned Gymraeg a fu’n ei ffermio ers cenedlaethau, gyda’i chapel, ei hysgol, ei thafarn, ei heisteddfod a’i ffordd ei hun o fyw. Mewn ychydig fisoedd roedd wedi mynd. Cafodd y bobl eu rhybuddion, cymerwyd y mynydd yn faes tanio i’r fyddin, a thrannoeth i’r teulu olaf adael dechreuodd y sieliau ddisgyn. Dyma eu hanes, a pham y mae Cymru’n dweud Cofiwch Epynt.",
   "|| Y mynydd | Mynydd Epynt, y llwyfandir uchel rhwng Wysg, Irfon a Gwy, ym Mrycheiniog",
   "|| Y gymuned | 219 o bobl mewn 54 o gartrefi, gyda Chapel y Babell, ysgol Cilieni a’r Drovers Arms",
   "|| Y tir a gymerwyd | Tua 30,000 o erwau, i greu’r hyn a ddaeth yn Faes Hyfforddi Pontsenni",
   "|| Y llythyrau | O 2 Mawrth 1940, y diwrnod ar ôl Gŵyl Dewi",
   "|| Y diwrnod olaf | Dydd Sul 30 Mehefin 1940; dechreuodd y gynnau ddydd Llun 1 Gorffennaf",
   "|| Y geiriau a arhosodd | ‘Mae’n ddiwedd byd yma’",
   "|| Cofio | 80 mlynedd yn 2020; 85 mlynedd yn 2025, gydag enwau’r ffermydd yn ôl ar y tir",
   "## Ffordd y meirch",
   "Llwyfandir hir ac uchel yw Mynydd Epynt, rhwng 400 a 478 metr uwchben y môr, rhwng Llanfair-ym-Muallt a Llanwrtyd i’r gogledd a Phontsenni ac Aberhonddu i’r de. Mae afonydd Cilieni, Nant Brân, Ysgir a Honddu yn llifo oddi arno i afon Wysg, a’r Duhonw i lawr i afon Gwy. Mae ei enw’n hen ac mae dadl am ei ystyr, ond yr esboniad mwyaf adnabyddus yw ‘ffordd y meirch’, o hen air am geffyl.[[cite:ep-wiki-mynydd]]",
   "Mae pobl wedi ei groesi ers Oes yr Efydd, ac mae carneddau a meini’r oes honno’n dal i sefyll lle mae’r hen lwybrau’n cwrdd. Yn ddiweddarach daeth yr un llwybrau’n ffyrdd y porthmyn, a yrrai wartheg a defaid Cymru i farchnadoedd Lloegr, a safai pedair tafarn ar ochr ogleddol y mynydd i’w gwasanaethu: y Griffin, Tafarn y Mynydd, y Spite a’r Drovers Arms.[[cite:ep-coflein-drovers]] Ar ei lethrau deheuol, yng Nghefn Brith ger Llangamarch, y ganed John Penri yn 1563, y gŵr a ymbiliodd ar y Frenhines Elisabeth am bregethwyr a fyddai’n siarad â phobl Cymru yn eu hiaith eu hunain.",
   "## Byd Cymraeg ar y mynydd",
   "Yn 1939 roedd y mynydd yn fyw. Ar ffermydd ag enwau fel Ffos yr Hwyaid, Gilfach yr Haidd, Cefnbryn Isaf, Llwynteg Uchaf, Glandŵr, Gwybedog a Waunlwyd, roedd teuluoedd yn ffermio defaid a gwartheg ar dir a ffermiwyd gan eu tadau a’u teidiau o’u blaen. Siaradent Gymraeg ar yr aelwyd, yn y caeau ac yn y capel.[[cite:ep-tomos]]",
   "Capel y Babell, a godwyd gan y Methodistiaid Calfinaidd yn 1857, oedd y galon. Yno y bedyddiwyd, y priodwyd ac y claddwyd y bobl; yno y cynhalient eu heisteddfod a’u cymanfa ganu. Am bedwar o’r gloch fore Nadolig 1939, y Nadolig olaf a dreuliodd yr un ohonynt ar y mynydd, cerddasant a marchogasant drwy’r tywyllwch i’r Plygain yn y Babell, i ganu’r hen garolau fel y gwnaeth eu pobl ers canrifoedd.[[cite:ep-tomos]] Âi’r plant i ysgol Cilieni, lle archebwyd llyfrau Cymraeg am y tro cyntaf yn 1903, ac roedd y teuluoedd yn gofalu am ei gilydd: dywedai cynfas wen y tu allan i dŷ wrth y cymdogion fod angen help yno.[[cite:ep-review-hughes,ep-wiki-mynydd]]",
   "!! ep-babell-stone",
   "## Y swyddog na fedrai sillafu’r enwau",
   "Ym mis Medi 1939, wrth i’r rhyfel ddechrau, daeth swyddog o’r fyddin i’r ysgol mewn car bach brown. Roedd ganddo restr o ffermydd y mynydd, ac ni fedrai sillafu eu henwau, felly gofynnodd i blant yr ysgol ei helpu i’w cael ar y map.[[cite:ep-tomos]] Doedd neb yn gwybod pam eto.",
   "Erbyn y flwyddyn newydd roedd y bobl yn poeni. Ar 1 Mawrth 1940 daethant ynghyd yng Nghapel y Babell, fel bob amser, i gadw Gŵyl Dewi. Drannoeth, 2 Mawrth, dechreuodd y llythyrau gyrraedd.[[cite:ep-nfu]] Roedd ar y Swyddfa Ryfel angen y mynydd i ymarfer y gynnau mawr, ar gyfer y rhyfel. Roedd pob teulu i adael ei gartref erbyn diwedd Ebrill.[[cite:ep-tomos]]",
   "!! ep-red-flag",
   "## Cymru’n codi ei llais",
   "Roedd hi’n dymor wyna. Mae gofyn i ffermwr mynydd symud ei braidd ym mis Ebrill yn gofyn iddo golli gwaith blwyddyn, a gofynnodd y teuluoedd am ragor o amser. Cawsant fis arall, ac yna ddiwrnod olaf: 30 Mehefin 1940.[[cite:ep-nfu,ep-tomos]]",
   "Cododd aelodau seneddol Cymru a gwŷr cyhoeddus eu llais drostynt, ond yng ngwanwyn 1940 atebwyd pob gwrthwynebiad â’r rhyfel.[[cite:ep-wiki-clearance]] Ar 25 Ebrill 1940 gofynnodd Jim Griffiths, yr aelod dros Lanelli, i’r Gweinidog Amaeth yn Nhŷ’r Cyffredin faint o dir yng Nghymru a gymerwyd gan adrannau’r llywodraeth a faint o bobl y tir a gollodd eu cartrefi, ac ymbiliodd arno i ofyn iddynt chwilio am safleoedd eraill. Atebodd y gweinidog fod tua 49,000 o erwau wedi’u cymryd mewn tair blynedd, nad oedd ganddo ffigur am y bobl a symudwyd, ac na theimlai fod cyfiawnhad dros annog yr adrannau i adael Cymru allan.[[cite:ep-hansard-1940]]",
   "## Y dyddiau olaf",
   "Ym mis Mehefin caeodd yr ysgol a’r capel, a dechreuodd y fyddin dynnu’r gwrychoedd.[[cite:ep-nfu]] Fesul un aeth y teuluoedd i lawr oddi ar y mynydd gyda’u dodrefn a’u hanifeiliaid. Gwrthododd un wraig fynd heb ddrws ffrynt ei thŷ ei hun, ac aeth ag ef gyda hi.[[cite:ep-tomos]]",
   "Daeth un gŵr i’w gweld yn mynd ac i gadw’r hyn a allai. Daeth Iorwerth Peate o Amgueddfa Genedlaethol Cymru, ysgolhaig bywyd gwerin Cymru a fyddai’n sefydlu’r Amgueddfa Werin yn Sain Ffagan yn ddiweddarach, i fyny i Epynt ym Mehefin 1940 i fesur a thynnu lluniau o’r cartrefi cyn eu colli. Mae Amgueddfa Cymru yn cadw ei luniau heddiw.[[cite:ep-review-hughes,ep-museum-peate]] Yn Waunlwyd cafodd hyd i hen wraig 82 oed yn eistedd yn ei chadair freichiau, yn wylo. Yn y tŷ hwnnw y ganed hi, a’i thad a’i thaid hefyd. Gofynnodd iddo o ble y deuai. Pan ddywedodd Caerdydd, dywedodd wrtho am fynd yn ôl yno cyn gynted ag y gallai, a meddai:[[cite:ep-tomos]]",
   "> Mae’n ddiwedd byd yma. | Hen wraig o Waunlwyd, 82 oed, wrth Iorwerth Peate, Mehefin 1940",
   "Daeth y geiriau hynny’n enw ar yr hanes. Rhoddodd Herbert Hughes hwy’n deitl i’w hanes am y clirio, ‘Mae’n ddiwedd byd yma’, yn 1997.",
   "!! ep-peate",
   "Ddydd Sul 30 Mehefin 1940, diwrnod llwyd, gadawodd y teulu olaf y mynydd. Ddydd Llun 1 Gorffennaf dechreuodd y gynnau danio.[[cite:ep-nfu,ep-tomos]] At ei gilydd roedd 219 o bobl o 54 o gartrefi wedi mynd, a chyda hwy aeth Capel y Babell, ysgol Cilieni, eglwys a’r Drovers Arms.[[cite:ep-llangammarch,ep-lw-poem]] Yr un haf dechreuodd y bomiau ddisgyn ar Gaerdydd ac Abertawe.",
   "## Y tân ar aelwyd Glandŵr",
   "Credai llawer y byddent yn dod adref pan fyddai’r rhyfel drosodd. Gadawodd rhai eu hallweddau yn y drysau, a chadwodd rhai eu tai yn addas i fyw ynddynt a dal ati i aredig eu caeau.[[cite:ep-wiki-clearance]] Âi Thomas Morgan o Glandŵr yn ôl ddydd ar ôl dydd i gynnau’r tân ar ei aelwyd ei hun, i gadw’r tŷ yn fyw. Rhybuddiodd y milwyr ef dro ar ôl tro. Yna un diwrnod daeth yn ôl ac roedd y tŷ wedi mynd. Meddai swyddog wrtho: ‘We’ve blown up the farmhouse. You won’t need to come here anymore.’ (Rydyn ni wedi chwythu’r ffermdy i fyny. Fydd dim angen i chi ddod yma eto.)[[cite:ep-nfu]]",
   "Roedd Elwyn Davies o Ferthyr Cynog yn ddeg oed yn 1940. Gwybedog oedd cartref ei nain. ‘Wythnos yn unig ar ôl iddi adael,’ cofiai, ‘fe chwalon nhw ei thŷ hi.’[[cite:ep-nfu]]",
   "## Ar chwâl",
   "Aeth y teuluoedd lle gallent gael fferm neu do uwch eu pennau: i’r cymoedd islaw’r mynydd, i Sir Faesyfed, a llawer i Sir Gaerfyrddin, ugain milltir a mwy o gartref. Aeth Ivor Morgan o Neuadd Llwyd, ffermwr ifanc tri deg dau oed, i Lwyn Wennol yng Ngwynfe; dywedodd ei ŵyr, yr aelod o’r Senedd Lee Waters, fod Epynt wedi aros yn fyw yn ei feddwl hyd ddiwedd ei ddyddiau. Y baban olaf a aned ar y mynydd, Beryl Lake, oedd nain Ben Lake, aelod seneddol Ceredigion, a alwodd y clirio yn bennod bwysig ond a anghofir yn aml yn hanes Cymru.[[cite:ep-nfu]]",
   "Roedd teulu Glyn Powell ymhlith y rhai a drowyd allan yn 1940. Yn y 1950au anfonwyd ef yn ôl i Epynt yn filwr ar Wasanaeth Cenedlaethol, a chysgodd ym meudy Ffos yr Hwyaid, fferm a adwaenai fel cartref. Yn ei nawdegau roedd yn dal i ymgyrchu, a throsglwyddodd yr hanes i’w ferch a’i phlant hithau.[[cite:ep-tomos]]",
   "## Yr iaith yn cilio",
   "Yn 1940 roedd gogledd Brycheiniog yn fro Gymraeg, ac Epynt yn un o’i chadarnleoedd.[[cite:ep-nation-2026]] Pan wasgarwyd pobl Epynt, llawer ohonynt i fannau lle siaredid mwy o Saesneg, collodd y Fro Gymraeg dir yn y dwyrain, a symudodd y ffin lle’r oedd y Gymraeg yn iaith bob dydd tua’r gorllewin.[[cite:ep-nfu,ep-wiki-clearance]] Collwyd tafodiaith leol gyda hwy, a’r enwau hefyd: galwodd y fyddin yr hen ffermydd yn Farm 1, Farm 2 ac yn y blaen.[[cite:ep-brecon-85]]",
   "Galwodd y storïwr a’r hanesydd Euros Lewis, sydd wedi casglu atgofion pobl y mynydd, y clirio yn ‘ergyd farwol i Frycheiniog Gymraeg’.[[cite:ep-wiki-clearance]]",
   "## Y mynydd dan y gynnau",
   "Daeth Mynydd Epynt yn galon Maes Hyfforddi Pontsenni, y maes hyfforddi milwrol mwyaf yng Nghymru, ac felly y mae o hyd. Dinistriwyd y rhan fwyaf o’r hen adeiladau, y ffermdai, y capeli a’u mynwentydd, gan sieliau a ffrwydron. Yn 1988 cododd y fyddin bentref ffug ar y mynydd i ymarfer ymladd mewn strydoedd, gyda chapel ffug a cherrig beddau ffug.[[cite:ep-wiki-clearance,ep-tomos]] Mae defaid yn dal i bori’r maes, ond mae’r hen hawliau tramwy ar ei draws ar gau.[[cite:ep-wiki-mynydd,ep-wiki-clearance]]",
   "Mae ambell beth wedi goroesi. Mae’r Drovers Arms yn dal i sefyll; adferodd y Weinyddiaeth Amddiffyn ei du allan yn y 1990au, er ei fod yn wag y tu mewn.[[cite:ep-coflein-drovers]] Daeth Disgwylfa, un o’r ffermydd a gymerwyd yn 1940, yn Ganolfan Epynt, ac yn 2004 agorwyd Ffordd Epynt, llwybr o tua 65 cilometr o amgylch ymyl y maes i gerddwyr, marchogion a beicwyr.[[cite:ep-wiki-mynydd,ep-epyntway]]",
   "!! ep-drovers",
   "## Byth eto: y Preselau",
   "Dysgodd Epynt i Gymru beth allai ddigwydd pan fyddai Llundain am gael y tir. Pan ddaeth y rhyfel i ben, roedd y Swyddfa Ryfel am gael rhagor: tir ger Trawsfynydd, Tregaron a Llyn y Fan Fach, ac yn bennaf oll fryniau’r Preselau yn Sir Benfro. Y tro hwn roedd Cymru’n barod. Yn 1947 addunedodd Plaid Cymru na fyddai’n ildio modfedd.[[cite:ep-wiki-clearance]] Yn y Preselau safodd y ffermwyr, y capeli a phobl yr ardal gyda’i gilydd ym Mrwydr y Preseli, ac ysgrifennodd y bardd Waldo Williams ei gerdd fawr Preseli yn 1946 i amddiffyn bryniau ei blentyndod. Rhoddwyd y gorau i’r cynllun.[[cite:ep-nation-2026,ep-waldo]] Yr hyn a gollodd Epynt, fe’i cadwodd y Preselau.",
   "Bum mlynedd ar hugain ar ôl Epynt, cymerwyd cymuned Gymraeg arall, Capel Celyn yng Nghwm Tryweryn, oddi ar ei phobl, y tro hwn er mwyn dŵr Lerpwl. Erbyn hynny safodd y genedl gyfan drosti, a daeth Cofiwch Dryweryn yn gri Cymru. Cofiwch Epynt yw ei chwaer hŷn.",
   "## Cofiwch Epynt",
   "Am flynyddoedd adroddid hanes Epynt yn bennaf wrth aelwydydd y teuluoedd a gollodd eu cartrefi. Yna fe’i hysgrifennwyd. Casglodd Herbert Hughes yr atgofion, y lluniau ac enwau’r ffermydd a lle’r aeth pob teulu, a chyhoeddodd ‘Mae’n ddiwedd byd yma’: Mynydd Epynt a’r Troad Allan yn 1940 yn 1997, ac yn Saesneg An Uprooted Community: A History of Epynt yn 1998. Mae’r Lolfa wedi cyhoeddi’r ddau lyfr eto, yr un Cymraeg yn 2023.[[cite:ep-review-hughes]] Trodd T. C. Thomas hanes Glandŵr yn ddrama, Sound of Stillness.[[cite:ep-review-hughes]]",
   "Ym Mehefin 2020, wedi pedwar ugain mlynedd, ysgrifennodd Bardd Cenedlaethol Cymru, Ifor ap Glyn, gerdd i gofio’r 219 o bobl a’r 54 o ffermydd, yn Gymraeg ac yn Saesneg. Mae’r fersiwn Saesneg, Remember Epynt, yn dechrau: ‘Now only shells / till the soil at Llwynteg-ucha’ (Dim ond sieliau / sy’n trin y pridd yn Llwynteg-ucha bellach).[[cite:ep-lw-poem]] Gwnaeth Bethan, merch Glyn Powell, gyda Menter Iaith Brycheiniog, y dudalen Atgofion Epynt, lle cofir enwau’r ffermydd a gollwyd ddydd ar ôl dydd.[[cite:ep-tomos]] Yn 2022 adroddodd ITV Cymru yr hanes yn ei gyfres Vanished Wales.[[cite:ep-itv]]",
   "Yn 2025, wedi wyth deg pump o flynyddoedd, daeth disgynyddion y teuluoedd ynghyd fel Grŵp Epynt. Ar ddiwrnod agored ar y maes, roedd llechi wedi’u naddu â hen enwau Cymraeg y ffermydd yn leinio’r ffordd; yna aed â hwy yn ôl a’u gosod lle safai’r ffermydd gynt, fel bod gan Farm 1 a Farm 2 eu henwau eto. Daeth tua thri chant o bobl, llawer ohonynt yn blant ac wyrion pobl 1940, ac ymwelsant â safle Capel y Babell, ysgol Cilieni a’r Drovers Arms. Yng Nghanolfan Epynt dadorchuddiwyd llechen yn dwyn enwau pawb y bu’n rhaid iddynt adael, a phlannwyd coeden. Aeth drama, Iorwerth o’r Epynt, o amgylch ysgolion yr ardal.[[cite:ep-brecon-85]]",
   "!! ep-babell",
   "Ni ofynnodd pobl Epynt am ddim ond cael aros yn eu cartrefi eu hunain a siarad eu hiaith eu hunain ar eu mynydd eu hunain. Rhoesant eu cartrefi i ryfel na ddewisasant, ac ni welodd y rhan fwyaf ohonynt hwy byth eto. Ond nid ydynt wedi’u hanghofio. Mae gan eu ffermydd eu henwau’n ôl, adroddir eu hanes yn Gymraeg ac yn Saesneg, ac ar waliau ac arwyddion ffyrdd ym Mrycheiniog mae dau air wedi’u paentio y dylai pob Cymro a Chymraes eu gwybod. Cofiwch Epynt.",
  ],
)

# Timeline (same shape as EVENTS in data.py; titles must match STORY["events"] so the timeline links here).
# "The clearing of Epynt" itself is in src/more.py (its date and words are updated there).
EVENTS = [
 ("modern", 1940, 0, 0, "03-02", "The letters come to Epynt", "Y llythyrau’n cyrraedd Epynt",
  "The day after the people of Mynydd Epynt keep St David’s Day at Capel y Babell, the War Office letters begin to arrive: every family must leave its home so that the mountain can become an artillery range.",
  "Y diwrnod ar ôl i bobl Mynydd Epynt gadw Gŵyl Dewi yng Nghapel y Babell, mae llythyrau’r Swyddfa Ryfel yn dechrau cyrraedd: rhaid i bob teulu adael ei gartref er mwyn i’r mynydd ddod yn faes tanio.", 0, "epynt", "Epynt_clearance"),
 ("today", 2025, 0, 0, "", "Epynt remembered, 85 years on", "Cofio Epynt, 85 mlynedd yn ddiweddarach",
  "Descendants of the families cleared from Mynydd Epynt gather as Grŵp Epynt. Slates carved with the old Welsh names of the farms are set back where the farms stood, and a slate with the names of everyone who had to leave is unveiled at the Epynt Centre.",
  "Daw disgynyddion y teuluoedd a gliriwyd o Fynydd Epynt ynghyd fel Grŵp Epynt. Gosodir llechi â hen enwau Cymraeg y ffermydd yn ôl lle safai’r ffermydd, a dadorchuddir llechen ag enwau pawb y bu’n rhaid iddynt adael yng Nghanolfan Epynt.", 0, "epynt", "Epynt_clearance"),
]

# Fuller text for the place page place-epynt.html (long.py PLACE_LONG).
PLACE_LONG = (
 ["## The mountain",
  "Mynydd Epynt is the high moorland plateau of north Brycheiniog, between the valleys of the Usk, the Irfon and the Wye. Its name is usually read as ‘the way of horses’. The old tracks across it, used since the Bronze Age, became drovers’ roads, and four droving inns stood on its northern side.[[cite:ep-wiki-mynydd,ep-coflein-drovers]]",
  "## 1940",
  "Until 1940 the mountain was home to a Welsh-speaking farming community, with Capel y Babell, Cilieni school and the Drovers Arms. In the spring of 1940 the War Office took about 30,000 acres for an artillery range. 219 people from 54 homes had to leave, the last on 30 June 1940, and the guns began the next day. Iorwerth Peate of the National Museum came to record the homes, and an old woman of Waunlwyd told him: ‘Mae’n ddiwedd byd yma’, it is the end of the world here.[[cite:ep-nfu,ep-llangammarch,ep-tomos]]",
  "## Today",
  "The mountain is the heart of the Sennybridge Training Area, the largest military training area in Wales. The Drovers Arms, its outside restored in the 1990s, still stands on the range. The Epynt Centre at Disgwylfa, on the B4519 between Upper Chapel and Garth, is open to visitors, with a slate bearing the names of the people who had to leave, and the Epynt Way, about 65 kilometres long, goes round the edge of the range.[[cite:ep-coflein-drovers,ep-epyntway,ep-brecon-85]]"],
 ["## Y mynydd",
  "Mynydd Epynt yw llwyfandir rhostir uchel gogledd Brycheiniog, rhwng dyffrynnoedd Wysg, Irfon a Gwy. Darllenir ei enw fel arfer fel ‘ffordd y meirch’. Daeth yr hen lwybrau ar ei draws, a ddefnyddiwyd ers Oes yr Efydd, yn ffyrdd y porthmyn, a safai pedair tafarn y porthmyn ar ei ochr ogleddol.[[cite:ep-wiki-mynydd,ep-coflein-drovers]]",
  "## 1940",
  "Hyd 1940 roedd y mynydd yn gartref i gymuned ffermio Gymraeg, gyda Chapel y Babell, ysgol Cilieni a’r Drovers Arms. Yng ngwanwyn 1940 cymerodd y Swyddfa Ryfel tua 30,000 o erwau yn faes tanio. Bu’n rhaid i 219 o bobl o 54 o gartrefi adael, yr olaf ar 30 Mehefin 1940, a dechreuodd y gynnau drannoeth. Daeth Iorwerth Peate o’r Amgueddfa Genedlaethol i gofnodi’r cartrefi, a dywedodd hen wraig o Waunlwyd wrtho: ‘Mae’n ddiwedd byd yma.’[[cite:ep-nfu,ep-llangammarch,ep-tomos]]",
  "## Heddiw",
  "Mae’r mynydd yn galon Maes Hyfforddi Pontsenni, y maes hyfforddi milwrol mwyaf yng Nghymru. Mae’r Drovers Arms, a’i du allan wedi’i adfer yn y 1990au, yn dal i sefyll ar y maes. Mae Canolfan Epynt yn Nisgwylfa, ar y B4519 rhwng Capel Uchaf a’r Garth, ar agor i ymwelwyr, gyda llechen yn dwyn enwau’r bobl y bu’n rhaid iddynt adael, ac mae Ffordd Epynt, tua 65 cilometr o hyd, yn mynd o amgylch ymyl y maes.[[cite:ep-coflein-drovers,ep-epyntway,ep-brecon-85]]"],
)

# Sources beside the claims (cites.py merges these into S).
CITES = {
    "ep-nfu": dict(
        short=("NFU Cymru, 2020", "NFU Cymru, 2020"),
        t="Epynt: A lost community", by=("Clare Williams, NFU Cymru, 29 June 2020", "Clare Williams, NFU Cymru, 29 Mehefin 2020"),
        note=("219 people on 54 farms; the letters from 2 March 1940, the day after St David’s Day at Capel y Babell; a month’s extension; school and chapel closed in June; the last family left on Sunday 30 June and the guns began on Monday 1 July. Thomas Morgan of Glandŵr, Gwybedog, Neuadd Llwyd, Beryl Lake; the Welsh-speaking boundary moved west.",
              "219 o bobl ar 54 o ffermydd; y llythyrau o 2 Mawrth 1940, y diwrnod ar ôl Gŵyl Dewi yng Nghapel y Babell; mis o estyniad; cau’r ysgol a’r capel ym Mehefin; gadawodd y teulu olaf ddydd Sul 30 Mehefin a dechreuodd y gynnau ddydd Llun 1 Gorffennaf. Thomas Morgan o Glandŵr, Gwybedog, Neuadd Llwyd, Beryl Lake; symudodd ffin y Gymraeg tua’r gorllewin."),
        url="https://www.nfu-cymru.org.uk/news-and-information/epynt-a-lost-community/", lang="en"),
    "ep-tomos": dict(
        short=("Angharad Tomos, 2020", "Angharad Tomos, 2020"),
        t="‘It’s the end of the world’: why we should remember the clearing of Epynt 80 years on", by=("Angharad Tomos, Nation.Cymru, 2 June 2020", "Angharad Tomos, Nation.Cymru, 2 Mehefin 2020"),
        note=("The officer and the farm names in September 1939; notices to leave by the end of April 1940, a month more for lambing; the Plygain at Capel y Babell on Christmas morning 1939; Iorwerth Peate and the old woman of Waunlwyd, aged 82: ‘mae’n ddiwedd byd yma’; Glyn Powell; the mock village; the Atgofion Epynt page.",
              "Y swyddog ac enwau’r ffermydd ym Medi 1939; rhybudd i adael erbyn diwedd Ebrill 1940, a mis arall i wyna; y Plygain yng Nghapel y Babell fore Nadolig 1939; Iorwerth Peate a’r hen wraig o Waunlwyd, 82 oed: ‘mae’n ddiwedd byd yma’; Glyn Powell; y pentref ffug; tudalen Atgofion Epynt."),
        url="https://nation.cymru/opinion/its-the-end-of-the-world-why-we-should-remember-the-clearing-of-epynt-80-years-on", lang="en"),
    "ep-lw-poem": dict(
        short=("Literature Wales, 2020", "Llenyddiaeth Cymru, 2020"),
        t="Remember Epynt", by=("Ifor ap Glyn, National Poet of Wales, 30 June 2020 (Literature Wales)", "Ifor ap Glyn, Bardd Cenedlaethol Cymru, 30 Mehefin 2020 (Llenyddiaeth Cymru)"),
        note=("In June 1940, 219 people were moved from their homes on Epynt to make a firing range; Cilieni school and Babell chapel closed; 54 farms, a whole community, were lost.",
              "Ym Mehefin 1940 symudwyd 219 o bobl o’u cartrefi ar Epynt i greu maes tanio; caeodd ysgol Cilieni a chapel y Babell; collwyd 54 o ffermydd, cymuned gyfan."),
        url="https://www.literaturewales.org/our-projects/national-poet-wales/ifor-ap-glyn-creative-work/remember-epynt/", lang="en"),
    "ep-llangammarch": dict(
        short=("Llangammarch Wells", "Llangamarch"),
        t="Epynt clearances", by=("Llangammarch Wells community website", "Gwefan cymuned Llangamarch"),
        note=("To make the Sennybridge Training Area (SENTA) 54 homes had to be vacated and 219 people were obliged to leave; a school, a church and the Drovers Arms closed; the land was taken by 30 June 1940.",
              "I greu Maes Hyfforddi Pontsenni bu’n rhaid gwagio 54 o gartrefi a bu’n rhaid i 219 o bobl adael; caeodd ysgol, eglwys a’r Drovers Arms; cymerwyd y tir erbyn 30 Mehefin 1940."),
        url="https://www.llangammarch.wales/epynt-clearances", lang="en"),
    "ep-hansard-1940": dict(
        short=("Hansard, 1940", "Hansard, 1940"),
        t="Land Acquisition (Wales), House of Commons, 25 April 1940", by=("Hansard, Parliamentary Debates, volume 360, columns 349–350", "Hansard, Dadleuon Seneddol, cyfrol 360, colofnau 349–350"),
        note=("Jim Griffiths asks how much Welsh land has been taken and how many farm people displaced, and asks the departments to seek other sites; the minister gives about 49,000 acres in three years and says he would not feel justified in urging the departments to exclude Wales.",
              "Mae Jim Griffiths yn gofyn faint o dir Cymru a gymerwyd a faint o bobl y tir a symudwyd, ac yn gofyn i’r adrannau chwilio am safleoedd eraill; mae’r gweinidog yn rhoi tua 49,000 o erwau mewn tair blynedd ac yn dweud na theimlai gyfiawnhad dros annog yr adrannau i adael Cymru allan."),
        url="https://api.parliament.uk/historic-hansard/commons/1940/apr/25/land-acquisition-wales", lang="en"),
    "ep-coflein-drovers": dict(
        short=("Coflein", "Coflein"),
        t="Drover’s Arms, Duhonw (NPRN 307124)", by=("Royal Commission on the Ancient and Historical Monuments of Wales", "Comisiwn Brenhinol Henebion Cymru"),
        note=("One of four droving inns on the northern side of Mynydd Epynt, with the Griffin, Tafarn y Mynydd and the Spite; it fell into disrepair when the army took the mountain, and the Ministry of Defence restored its exterior in the 1990s.",
              "Un o bedair tafarn y porthmyn ar ochr ogleddol Mynydd Epynt, gyda’r Griffin, Tafarn y Mynydd a’r Spite; aeth yn adfail pan gymerodd y fyddin y mynydd, ac adferodd y Weinyddiaeth Amddiffyn ei du allan yn y 1990au."),
        url="https://coflein.gov.uk/en/site/307124", lang="en"),
    "ep-museum-peate": dict(
        short=("Amgueddfa Cymru", "Amgueddfa Cymru"),
        t="Quarter plate film negative, Ysgair Fechan valley, Epynt (F2022.5.31)", by=("Iorwerth Peate, June 1940; Amgueddfa Cymru – Museum Wales, Collections Online", "Iorwerth Peate, Mehefin 1940; Amgueddfa Cymru, Casgliadau Ar-lein"),
        note=("One of the photographs Iorwerth Peate took on Epynt in June 1940, kept in the national collection.",
              "Un o’r lluniau a dynnodd Iorwerth Peate ar Epynt ym Mehefin 1940, a gedwir yn y casgliad cenedlaethol."),
        url="https://museum.wales/collections/online/object/7e38b070-8709-331a-bbe7-e0aab8af6b2f", lang="en"),
    "ep-review-hughes": dict(
        short=("Nation.Cymru, 2023", "Nation.Cymru, 2023"),
        t="Review: Mynydd Epynt a’r Troad Allan yn 1940 by Herbert Hughes", by=("Nation.Cymru, 29 July 2023", "Nation.Cymru, 29 Gorffennaf 2023"),
        note=("Herbert Hughes’s history, first published by Gomer in 1997 and again by Y Lolfa in 2023, with a list of the farms and where their families went; Iorwerth Peate measured and photographed the homes on the last day; Cilieni school ordered Welsh books for the first time in 1903; T. C. Thomas’s play Sound of Stillness.",
              "Hanes Herbert Hughes, a gyhoeddwyd gyntaf gan Gomer yn 1997 ac eto gan Y Lolfa yn 2023, gyda rhestr o’r ffermydd a lle’r aeth eu teuluoedd; mesurodd Iorwerth Peate a thynnodd luniau o’r cartrefi ar y diwrnod olaf; archebodd ysgol Cilieni lyfrau Cymraeg am y tro cyntaf yn 1903; drama T. C. Thomas, Sound of Stillness."),
        url="https://nation.cymru/culture/review-mynydd-epynt-ar-troad-allan-yn-1940-by-herbert-hughes", lang="en"),
    "ep-brecon-85": dict(
        short=("Brecon & Radnor Express, 2026", "Brecon & Radnor Express, 2026"),
        t="Grŵp Epynt marks 85 years since clearance", by=("Luke Williams, Brecon & Radnor Express, 5 February 2026", "Luke Williams, Brecon & Radnor Express, 5 Chwefror 2026"),
        note=("Slates bearing the original Welsh names of the farms, which the army had called Farm 1, Farm 2 and so on, returned to their sites; about 300 visitors, many descendants; visits to Babell chapel, Cilieni school and the Drovers Arms; a slate listing everyone displaced unveiled at the Epynt Centre and a tree planted; the play Iorwerth o’r Epynt toured schools.",
              "Llechi ag enwau Cymraeg gwreiddiol y ffermydd, a alwyd gan y fyddin yn Farm 1, Farm 2 ac yn y blaen, wedi’u dychwelyd i’w safleoedd; tua 300 o ymwelwyr, llawer yn ddisgynyddion; ymweld â chapel y Babell, ysgol Cilieni a’r Drovers Arms; dadorchuddio llechen yn rhestru pawb a symudwyd yng Nghanolfan Epynt a phlannu coeden; aeth y ddrama Iorwerth o’r Epynt o amgylch ysgolion."),
        url="https://www.brecon-radnor.co.uk/news/grwp-epynt-marks-85-years-since-clearance-with-donation-to-hospital-876088", lang="en"),
    "ep-wiki-clearance": dict(
        short=("Wikipedia: Epynt clearance", "Wikipedia: Epynt clearance"),
        t="Epynt clearance", by=("Wikipedia, drawing on Herbert Hughes (1997, 1998), BBC News (2020), WalesOnline and Coflein", "Wikipedia, ar sail Herbert Hughes (1997, 1998), BBC News (2020), WalesOnline a Coflein"),
        note=("Keys left in the doors and fields still ploughed; Euros Lewis: ‘the death blow to Welsh-speaking Breconshire’; Y Fro Gymraeg shrank in the east; most buildings destroyed; the mock village of 1988; Plaid Cymru’s campaign of 1947 against more land being taken.",
              "Allweddau wedi’u gadael yn y drysau a chaeau’n dal i gael eu haredig; Euros Lewis: ‘ergyd farwol i Frycheiniog Gymraeg’; crebachodd y Fro Gymraeg yn y dwyrain; dinistriwyd y rhan fwyaf o’r adeiladau; y pentref ffug yn 1988; ymgyrch Plaid Cymru yn 1947 yn erbyn cymryd rhagor o dir."),
        url="https://en.wikipedia.org/wiki/Epynt_clearance", lang="en"),
    "ep-wiki-mynydd": dict(
        short=("Wikipedia: Mynydd Epynt", "Wicipedia: Mynydd Epynt"),
        t="Mynydd Epynt", by=("Wikipedia, drawing on Coflein and the Ordnance Survey", "Wikipedia, ar sail Coflein a’r Arolwg Ordnans"),
        note=("The plateau at 400 to 478 metres between the Usk, the Irfon and the Wye; the name read as ‘a pathway for horses’; Bronze Age monuments on the old routes; the white sheet custom; Disgwylfa reopened as the Epynt Centre in 2009; the Epynt Way opened in 2004.",
              "Y llwyfandir 400 i 478 metr rhwng Wysg, Irfon a Gwy; yr enw’n cael ei ddarllen fel ‘ffordd y meirch’; henebion Oes yr Efydd ar yr hen lwybrau; arfer y gynfas wen; ailagorodd Disgwylfa fel Canolfan Epynt yn 2009; agorwyd Ffordd Epynt yn 2004."),
        url="https://en.wikipedia.org/wiki/Mynydd_Epynt", url_cy="https://cy.wikipedia.org/wiki/Mynydd_Epynt"),
    "ep-epyntway": dict(
        short=("Epynt Way", "Ffordd Epynt"),
        t="The Epynt Way: a modern trail in an ancient landscape", by=("Epynt Way Association", "Cymdeithas Ffordd Epynt"),
        note=("A 65-kilometre path round the edge of the Sennybridge Training Area; the visitor centre at Disgwylfa, one of the original farmhouses, on the B4519 between Upper Chapel and Garth.",
              "Llwybr 65 cilometr o amgylch ymyl Maes Hyfforddi Pontsenni; y ganolfan ymwelwyr yn Nisgwylfa, un o’r ffermdai gwreiddiol, ar y B4519 rhwng Capel Uchaf a’r Garth."),
        url="https://epyntway.org/", lang="en"),
    "ep-itv": dict(
        short=("ITV Wales, 2022", "ITV Cymru, 2022"),
        t="Vanished Wales: the true story of Mynydd Epynt, a community lost forever in the dark days of WWII", by=("ITV News Wales, 25 May 2022", "ITV News Cymru, 25 Mai 2022"),
        note=("About 30,000 acres taken and more than 200 men, women and children ordered to leave; Ydwena Jones and Elwyn Davies remember.",
              "Tua 30,000 o erwau wedi’u cymryd a mwy na 200 o ddynion, menywod a phlant wedi’u gorchymyn i adael; mae Ydwena Jones ac Elwyn Davies yn cofio."),
        url="https://www.itv.com/news/wales/2022-05-25/the-true-story-of-a-community-lost-forever-in-the-dark-days-of-wwii", lang="en"),
    "ep-nation-2026": dict(
        short=("Nation.Cymru, 2026", "Nation.Cymru, 2026"),
        t="Event marks anniversary of forced displacements of Welsh-speaking community", by=("Mark Mansfield, Nation.Cymru, 15 June 2026", "Mark Mansfield, Nation.Cymru, 15 Mehefin 2026"),
        note=("Northern Breconshire was mostly Welsh-speaking in 1940. About six years after Epynt the War Office drew up plans for a training area in the Preseli hills; Brwydr y Preseli united farmers, chapels and the people, and the plans were abandoned.",
              "Roedd gogledd Brycheiniog yn Gymraeg ei iaith gan mwyaf yn 1940. Tua chwe blynedd ar ôl Epynt lluniodd y Swyddfa Ryfel gynlluniau am faes hyfforddi yn y Preselau; unodd Brwydr y Preseli ffermwyr, capeli a’r bobl, a rhoddwyd y gorau i’r cynlluniau."),
        url="https://nation.cymru/news/event-marks-anniversary-of-forced-displacements-of-welsh-speaking-community/", lang="en"),
    "ep-waldo": dict(
        short=("Pobl Dewi, 2025", "Pobl Dewi, 2025"),
        t="The poetry of the Preselis: Waldo Williams", by=("Diocese of St Davids, Pobl Dewi, September 2025", "Esgobaeth Tyddewi, Pobl Dewi, Medi 2025"),
        note=("Waldo Williams’s poem Preseli, written in 1946 against the plans to make the hills a permanent military training ground.",
              "Cerdd Waldo Williams, Preseli, a ysgrifennwyd yn 1946 yn erbyn y cynlluniau i wneud y bryniau’n faes hyfforddi milwrol parhaol."),
        url="https://stdavids.churchinwales.org.uk/en/about-us/pobl-dewi/pobl-dewi-september-2025/waldo-williams/", lang="en"),
}
