"""A walk through Llys Rhosyr in 3D (llys-rhosyr.html).

Llys Rhosyr, at Niwbwrch on Ynys Môn, was one of the royal courts of the princes of Gwynedd. Sand buried it in the 1330s
and archaeologists uncovered its footings in the 1990s. This page lets you walk through it as it might have looked in
the days of Llywelyn ab Iorwerth, with eight stops that tell what happened there.

The 3D court is made in code by tools/llys3d.src.js, bundled into src/static/llys3d.js, and loaded only when the visitor
presses "Enter the court", so the page itself stays light. The words for each stop live here, in STOPS, and are also
printed on the page as ordinary text, for readers without 3D and for search engines. Where you stand at each stop is
set in the JS (STOPS there, by the same id).
"""
import json

g = {}

STOPS = [
    dict(id="gate", t=("The gate", "Y porth"),
         p=(["You are on Ynys Môn, near the shore where the Menai Strait meets the sea, in the 1230s. This is Llys Rhosyr, one of the royal courts of the princes of Gwynedd, "
             "and the centre of the commote of Menai.",
             "A stone wall rings the court. Through this gate came everyone: the prince and his household, messengers, poets, and the people of the commote bringing their dues of food."],
            ["Rydych ar Ynys Môn, ger y lan lle mae Afon Menai’n cwrdd â’r môr, yn y 1230au. Dyma Lys Rhosyr, un o lysoedd brenhinol tywysogion Gwynedd, "
             "a chanolfan cwmwd Menai.",
             "Mae mur cerrig o amgylch y llys. Drwy’r porth hwn y deuai pawb: y tywysog a’i osgordd, negeswyr, beirdd, a phobl y cwmwd yn dod â’u dyledion o fwyd."])),
    dict(id="hall", t=("The great hall", "Y neuadd"),
         p=(["The heart of the court. Here the prince feasted, gave judgement and heard his poets. Its doors face each other across the hall, and two rows of posts hold up the roof.",
             "The Laws of Hywel Dda set out where every officer of the court sat, and what each received. The gostegwr, the silentiary, called the hall to silence when the prince wished to speak, "
             "and fined anyone who would not be quiet."],
            ["Calon y llys. Yma y gwleddai’r tywysog, y rhoddai farn ac y gwrandawai ar ei feirdd. Mae ei drysau’n wynebu ei gilydd ar draws y neuadd, a dwy res o byst yn dal y to.",
             "Mae Cyfreithiau Hywel Dda yn nodi lle eisteddai pob swyddog yn y llys, a’r hyn a gâi pob un. Y gostegwr a alwai’r neuadd i dawelwch pan fynnai’r tywysog siarad, "
             "a dirwyo unrhyw un na fyddai’n dawel."])),
    dict(id="hearth", t=("The hearth", "Yr aelwyd"),
         p=(["A fire burned in the middle of the floor, and its smoke found its way out through the thatch. Around it the court ate and drank, and listened.",
             "The Laws say that when the prince wished for a song, the pencerdd, the chief poet, sang first: first a song of God, then a song of the prince. "
             "The household bard, the bardd teulu, sang after him, and before a battle he sang to the warband Unbennaeth Prydain, The Sovereignty of Britain."],
            ["Llosgai tân yng nghanol y llawr, a’i fwg yn canfod ei ffordd allan drwy’r to gwellt. O’i amgylch y bwytâi ac yr yfai’r llys, ac y gwrandawai.",
             "Dywed y Cyfreithiau mai’r pencerdd a ganai gyntaf pan ddymunai’r tywysog gân: yn gyntaf cân i Dduw, yna cân i’r tywysog. "
             "Canai’r bardd teulu ar ei ôl, a chyn brwydr canai i’r osgordd Unbennaeth Prydain."])),
    dict(id="seat", t=("The prince’s seat", "Sedd y tywysog"),
         p=(["At the upper end of the hall, on a raised floor, sat the prince, under the arms of Gwynedd: four lions on gold and red. "
             "Llywelyn ab Iorwerth, Llywelyn Fawr, Prince of Aberffraw and Lord of Snowdon, ruled almost all of Wales from courts like this one.",
             "Around him sat the officers of his court: the penteulu, captain of the warband; the offeiriad teulu, the household priest; the distain, the steward; "
             "the ynad llys, the judge; the hebogydd, the falconer, who was allowed only three drinks in the hall so that the hawks would never be neglected."],
            ["Ym mhen uchaf y neuadd, ar lawr uwch, eisteddai’r tywysog, dan arfbais Gwynedd: pedwar llew ar aur a choch. "
             "Llywelyn ab Iorwerth, Llywelyn Fawr, Tywysog Aberffraw ac Arglwydd Eryri, a reolai bron y cyfan o Gymru o lysoedd fel hwn.",
             "O’i amgylch eisteddai swyddogion ei lys: y penteulu, capten yr osgordd; offeiriad y teulu; y distain, y stiward; "
             "ynad y llys, y barnwr; yr hebogydd, na châi ond tair diod yn y neuadd, fel na fyddai’r hebogau byth yn cael eu hesgeuluso."])),
    dict(id="chamber", t=("The chamber", "Yr ystafell"),
         p=(["Beside the hall stood the ystafell, the prince’s own rooms, away from the noise of the feast. The Laws give the gwas ystafell, the chamberlain, the care of it.",
             "The Laws give the queen her own officers too. When she wished for a song in her chamber, the household bard sang to her, quietly, so as not to disturb the hall."],
            ["Wrth ymyl y neuadd safai’r ystafell, ystafelloedd y tywysog ei hun, i ffwrdd o sŵn y wledd. Mae’r Cyfreithiau’n rhoi’r gofal amdani i was yr ystafell.",
             "Mae’r Cyfreithiau’n rhoi ei swyddogion ei hun i’r frenhines hefyd. Pan fynnai gân yn ei hystafell, canai’r bardd teulu iddi, yn dawel, rhag tarfu ar y neuadd."])),
    dict(id="kitchen", t=("The kitchen and stores", "Y gegin a’r storfeydd"),
         p=(["The court lived on the land around it. The people of the commote paid their dues in food: bread and meat, butter and cheese, oats for the horses and honey for the mead.",
             "The prince’s officers in the commote, the maer and the rhaglaw, gathered the dues and kept order, and the court’s own cook, butler and mead-brewer turned them into feasts."],
            ["Roedd y llys yn byw ar y tir o’i amgylch. Talai pobl y cwmwd eu dyledion mewn bwyd: bara a chig, menyn a chaws, ceirch i’r meirch a mêl i’r medd.",
             "Casglai swyddogion y tywysog yn y cwmwd, y maer a’r rhaglaw, y dyledion a chadw trefn, a throai cogydd, trulliad a meddydd y llys hwy’n wleddoedd."])),
    dict(id="wall", t=("Eryri across the water", "Eryri dros y dŵr"),
         p=(["Look east, across the Menai Strait, to the mountains of Eryri. They were the fortress of Gwynedd, and Ynys Môn, Môn Mam Cymru, was its granary.",
             "The princes did not stay in one place. They moved with their household from court to court through the year, and Rhosyr was one of many courts of Gwynedd, almost one in every commote."],
            ["Edrychwch tua’r dwyrain, dros Afon Menai, at fynyddoedd Eryri. Hwy oedd caer Gwynedd, ac Ynys Môn, Môn Mam Cymru, oedd ei hysgubor.",
             "Nid arhosai’r tywysogion mewn un lle. Symudent gyda’u gosgordd o lys i lys drwy’r flwyddyn, ac roedd Rhosyr yn un o lysoedd niferus Gwynedd, bron un ym mhob cwmwd."])),
    dict(id="sands", t=("Buried by the sands", "Wedi’i chladdu gan y tywod"),
         p=(["After 1282 the court passed to the king’s officers, and in 1303 the town of Niwbwrch, Newborough, was founded beside it for Welsh families moved from Llan-faes when Beaumaris was built. "
             "Then, in the 1330s, great storms blew the sand of the dunes over the court and buried it.",
             "It lay hidden for more than six hundred years, until the Gwynedd Archaeological Trust uncovered its footings between 1992 and 1996. You can walk among them today. "
             "St Fagans National Museum of History has rebuilt its hall and chamber as Llys Llywelyn."],
            ["Wedi 1282 aeth y llys i swyddogion y brenin, ac yn 1303 sefydlwyd tref Niwbwrch wrth ei ymyl ar gyfer teuluoedd o Gymry a symudwyd o Lan-faes pan godwyd Biwmares. "
             "Yna, yn y 1330au, chwythodd stormydd mawr dywod y twyni dros y llys a’i gladdu.",
             "Bu’n guddiedig am fwy na chwe chan mlynedd, nes i Ymddiriedolaeth Archaeolegol Gwynedd ddadorchuddio ei sylfeini rhwng 1992 a 1996. Gallwch gerdded yn eu plith heddiw. "
             "Mae Amgueddfa Werin Cymru, Sain Ffagan, wedi ailgodi ei neuadd a’i hystafell fel Llys Llywelyn."])),
]

UI = dict(
    canvas=("A 3D picture of Llys Rhosyr, a royal court of the princes of Gwynedd. The stops below tell the same story in words.",
            "Llun 3D o Lys Rhosyr, un o lysoedd brenhinol tywysogion Gwynedd. Mae’r arosfannau isod yn adrodd yr un hanes mewn geiriau."),
    tour=("Next stop", "Yr arhosfan nesaf"), next=("Next", "Nesaf"), prev=("Back", "Yn ôl"), again=("Back to the gate", "Yn ôl i’r porth"),
    close=("Close", "Cau"), fs=("Full screen", "Sgrin lawn"), stop=("Stop {n} of {of}", "Arhosfan {n} o {of}"),
    help=("Walk with W A S D or the arrow keys. Drag to look around. Click a gold marker to go to it.",
          "Cerddwch gyda W A S D neu’r bysellau saeth. Llusgwch i edrych o gwmpas. Cliciwch ar nod aur i fynd ato."),
    helpTouch=("Walk with the circle. Drag to look around. Tap a gold marker to go to it.",
               "Cerddwch gyda’r cylch. Llusgwch i edrych o gwmpas. Tapiwch nod aur i fynd ato."),
)


def setup(build_globals):
    g.update(build_globals)


def page():
    bi, section, hero, SITE, e = g["bi"], g["section"], g["hero"], g["SITE"], g["e"]
    top = hero("medieval", f'<a href="index.html">{SITE}</a> / <a href="era-medieval.html">{bi("The age of the princes", "Oes y tywysogion")}</a>', "book",
               "Walk through it in 3D", "Cerddwch drwyddo mewn 3D", "Llys Rhosyr: the court of the princes", "Llys Rhosyr: llys y tywysogion",
               "Step inside a royal court of Gwynedd as it might have looked in the days of Llywelyn Fawr. Walk the great hall, sit by the hearth and stand before the prince’s seat.",
               "Camwch i mewn i un o lysoedd brenhinol Gwynedd fel y gallai fod wedi edrych yn nyddiau Llywelyn Fawr. Cerddwch y neuadd fawr, eisteddwch wrth yr aelwyd a sefwch o flaen sedd y tywysog.",
               art="castle")
    stage = (f'<div class="ll-stage" id="ll-stage"><img class="ll-poster" src="gallery/anci-llys-rhosyr.webp" alt="" width="1400" height="1050" loading="lazy" decoding="async">'
             f'<div class="ll-start"><p>{bi("The court is drawn on your device, so it takes a moment to load (about 0.5 MB).", "Caiff y llys ei dynnu ar eich dyfais, felly mae’n cymryd eiliad i lwytho (tua 0.5 MB).")}</p>'
             f'<button type="button" class="btn solid ll-go" id="ll-go">{bi("Enter the court", "Mynd i mewn i’r llys")} →</button></div>'
             f'<p class="ll-fail-msg">{bi("Your browser cannot show 3D here. The stops below tell the whole story.", "Ni all eich porwr ddangos 3D yma. Mae’r arosfannau isod yn adrodd yr holl hanes.")}</p></div>'
             f'<p class="muted ll-note">{bi("The buildings are imagined from the stone footings the archaeologists found. No one knows exactly how high the walls stood or how the roofs were made. The photograph shows the footings today (RobinLeicester, CC BY-SA 4.0).", "Mae’r adeiladau wedi’u dychmygu o’r sylfeini cerrig a ganfu’r archaeolegwyr. Ni ŵyr neb yn union pa mor uchel oedd y muriau na sut y gwnaed y toeau. Mae’r ffotograff yn dangos y sylfeini heddiw (RobinLeicester, CC BY-SA 4.0).")}</p>')
    words = "".join(f'<li id="stop-{s["id"]}"><h3>{bi(*s["t"])}</h3>' + "".join(f"<p>{bi(a, b)}</p>" for a, b in zip(*s["p"])) + "</li>" for s in STOPS)
    more = (f'<p class="more-row"><a class="btn" href="laws.html">{bi("The Laws of Hywel Dda", "Cyfreithiau Hywel Dda")} →</a> '
            f'<a class="btn" href="person-llywelyn-fawr.html">{bi("Llywelyn Fawr", "Llywelyn Fawr")} →</a> '
            f'<a class="btn" href="place-aberffraw.html">{bi("Aberffraw", "Aberffraw")} →</a></p>')
    main = (top + f'<section class="game-sec"><div class="wrap">{stage}</div></section>'
            + section(f'<ol class="ll-stops">{words}</ol>{more}', "The eight stops", "Yr wyth arhosfan"))
    data = dict(stops=[dict(id=s["id"], t=list(s["t"]), p=[s["p"][0], s["p"][1]]) for s in STOPS], ui={k: list(v) for k, v in UI.items()})
    extra = (f'<script>var LLYS={json.dumps(data, ensure_ascii=False, separators=(",", ":"))};</script>\n'
             '<script>addEventListener("DOMContentLoaded",function(){var b=document.getElementById("ll-go"),s=document.getElementById("ll-stage");if(!b||!s)return;'
             'var ok=false;try{var c=document.createElement("canvas");ok=!!(window.WebGLRenderingContext&&(c.getContext("webgl2")||c.getContext("webgl")))}catch(e){}'
             'if(!ok){s.classList.add("fail");return}'
             'b.onclick=function(){var cy=document.documentElement.lang==="cy";b.disabled=true;b.textContent=cy?"Wrthi’n llwytho…":"Loading…";s.classList.add("on");'
             'LLYS.cy=cy;import("./llys3d.js?v=1").then(function(m){m.start(s,LLYS)}).catch(function(){s.classList.add("fail")})}})</script>\n')
    ld = {"@context": "https://schema.org", "@type": "LandmarksOrHistoricalBuildings", "name": "Llys Rhosyr",
          "description": "A royal court of the princes of Gwynedd at Niwbwrch, Ynys Môn, buried by sand in the 1330s and excavated 1992 to 1996.",
          "geo": {"@type": "GeoCoordinates", "latitude": 53.16, "longitude": -4.37}}
    return g["page"]("llys-rhosyr.html", "Llys Rhosyr in 3D: walk through a court of the princes of Gwynedd · History of Wales",
                     "Walk through Llys Rhosyr, a royal court of the princes of Gwynedd on Ynys Môn, in 3D: the great hall, the hearth, the prince’s seat and the chamber, with the story of each.",
                     main, era="medieval", ld=ld, active="play.html", track="game:llys", extra=extra)


CSS = """
.ll-stage { position: relative; aspect-ratio: 16 / 9; border-radius: var(--r); overflow: hidden; border: 1px solid var(--line); background: #10141d; isolation: isolate }
@media (max-width: 700px) { .ll-stage { aspect-ratio: 3 / 4 } }
.ll-stage:fullscreen { aspect-ratio: auto; border-radius: 0 }
.ll-poster { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; filter: brightness(.55) saturate(.9) }
.ll-start { position: absolute; inset: auto 0 0 0; padding: 1.5rem; display: grid; gap: .8rem; justify-items: start; background: linear-gradient(transparent, rgba(8,10,16,.85)) }
.ll-start p { margin: 0; color: #e6dcc8; max-width: 34rem }
.ll-go { font-size: 1.15rem; padding: .9rem 1.4rem }
.ll-stage.ready .ll-poster, .ll-stage.ready .ll-start { display: none }
.ll-fail-msg { display: none; position: absolute; inset: auto 0 0 0; margin: 0; padding: 1.2rem 1.5rem; background: rgba(8,10,16,.9) }
.ll-stage.fail .ll-fail-msg { display: block } .ll-stage.fail .ll-start { display: none }
.ll-canvas { position: absolute; inset: 0; width: 100%; height: 100%; display: block; touch-action: none; outline: none }
.ll-ui { position: absolute; inset: 0; pointer-events: none; z-index: 2 }
.ll-ui > * { pointer-events: auto }
.ll-bar { position: absolute; top: .7rem; left: .7rem; right: .7rem; display: flex; flex-wrap: wrap; gap: .5rem; align-items: center }
.ll-bar .btn { padding: .45rem .9rem; font-size: .9rem; backdrop-filter: blur(6px) }
.ll-help { font-size: .82rem; color: #e6dcc8; background: rgba(8,10,16,.6); padding: .3rem .6rem; border-radius: 8px }
.ll-panel { position: absolute; right: .7rem; bottom: .7rem; width: min(25rem, calc(100% - 1.4rem)); max-height: calc(100% - 5rem); overflow: auto;
  background: rgba(12,15,22,.9); border: 1px solid color-mix(in srgb, var(--gold) 40%, var(--line)); border-radius: 16px; padding: 1rem 1.1rem; backdrop-filter: blur(8px) }
.ll-panel h2 { margin: 0 0 .5rem; font-size: 1.45rem }
.ll-panel h2:focus { outline: none }
.ll-panel p { font-size: .95rem; line-height: 1.55; margin: 0 0 .6rem }
.ll-n { font: 500 .75rem var(--f-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--gold) }
.ll-btns { display: flex; gap: .5rem; align-items: center; margin-top: .6rem }
.ll-btns .btn { padding: .4rem .8rem; font-size: .88rem }
.ll-x { position: absolute; top: .4rem; right: .5rem; background: none; border: 0; color: inherit; font-size: 1.6rem; line-height: 1; cursor: pointer; padding: .2rem .5rem }
.ll-stick { display: none; position: absolute; left: 1rem; bottom: 1rem; width: 110px; height: 110px; border-radius: 50%; border: 2px solid rgba(255,255,255,.45); background: rgba(8,10,16,.35); touch-action: none }
.ll-stick i { position: absolute; left: 50%; top: 50%; width: 46px; height: 46px; margin: -23px; border-radius: 50%; background: rgba(242,193,78,.85) }
@media (pointer: coarse) { .ll-stick { display: block } .ll-panel { bottom: auto; top: 3.6rem; max-height: 40% } .ll-help { display: none } }
.ll-note { font-size: .88rem; margin-top: .7rem }
.ll-stops { list-style: none; counter-reset: st; padding: 0; margin: 0; display: grid; gap: 1.2rem; grid-template-columns: repeat(auto-fill, minmax(min(100%, 330px), 1fr)) }
.ll-stops li { counter-increment: st; border: 1px solid var(--line); border-radius: 16px; background: var(--card); padding: 1.1rem 1.2rem }
.ll-stops h3::before { content: counter(st) ". "; color: var(--gold) }
.ll-stops p { font-size: .97rem; line-height: 1.6 }
"""
