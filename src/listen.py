"""Long reads read aloud (Ifan, 14 November 2026: "Make the audio sound good, a real person reading the text").

Every long read can be listened to in English and in Welsh. The sound is made ahead of time by tools/make_listen.py on
GitHub (.github/workflows/listen.yml), kept as files on the repository's "listen" release (so the repository itself
stays small), and copied into the site at listen/<id>-<lang>.m4a when the site is deployed (deploy.yml).

This module is shared by the build and the tool, so both read exactly the same words:
- spoken(x, lang): the long read as it is read aloud, in sections (the opening, then one per "## " heading).
- MANIFEST: src/listen.json, written by the tool: for each long read and language, the file, its length, the time
  each section starts (so the player can jump to a heading), the voice and a hash of the words. When the words change,
  the hash no longer matches and the next run of the workflow makes that file again.
- player(x): the Listen box under the byline (nothing at all for a long read that has no sound yet).
The player itself is src/static/listen.js; it loads no sound until the reader presses Play.
"""
import hashlib, html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST_PATH = os.path.join(HERE, "listen.json")
try:
    MANIFEST = json.load(open(MANIFEST_PATH, encoding="utf-8"))
except FileNotFoundError:
    MANIFEST = {}

# Who reads, shown small in the player. Filled in from the manifest's "voice" (see VOICES in tools/make_listen.py).
CREDIT = {
    "azure": ("Read by a Microsoft neural voice", "Darllenir gan lais niwral Microsoft"),
    "kokoro": ("Read by the Kokoro open voice", "Darllenir gan lais agored Kokoro"),
    "piper": ("Read by Bangor University's Welsh voice", "Darllenir gan lais Cymraeg Prifysgol Bangor"),
    "elevenlabs": ("Read by an ElevenLabs voice", "Darllenir gan lais ElevenLabs"),
}

# ---------------------------------------------------------------- the words read aloud

ORD_EN = ["", "the First", "the Second", "the Third", "the Fourth", "the Fifth", "the Sixth", "the Seventh", "the Eighth",
          "the Ninth", "the Tenth", "the Eleventh", "the Twelfth", "the Thirteenth"]
ORD_CY = ["", "Cyntaf", "Ail", "Trydydd", "Pedwerydd", "Pumed", "Chweched", "Seithfed", "Wythfed", "Nawfed", "Degfed",
          "Unfed ar Ddeg", "Deuddegfed", "Trydydd ar Ddeg"]
RULERS = ("Edward|Henry|Harri|Richard|Rhisiart|William|Gwilym|Charles|Siarl|James|Iago|George|Siôr|Elizabeth|Elisabeth|"
          "Mary|Mari|John|Ioan|Robert|Louis|Philip|Philippe|Gregory|Innocent|Pius|Urban|Leo|Alexander|Alecsander|David|Dafydd|"
          "Malcolm|Edmund|Stephen|Steffan|Anne|Victoria|Fictoria|Paul|Pawl|Clement|Benedict|Boniface|Celestine|Martin|Constantine|Cystennin")
ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13}


def _regnal(t, cy):
    """Henry VII -> Henry the Seventh; Harri VII -> Harri’r Seithfed; Edward I -> Edward y Cyntaf."""
    def one(m):
        name, n = m.group(1), ROMAN[m.group(2)]
        if not cy:
            return f"{name} {ORD_EN[n]}"
        return f"{name}’r {ORD_CY[n]}" if name[-1].lower() in "aeiouwy" else f"{name} y {ORD_CY[n]}"
    # a capitalised name, then a Roman number standing on its own. A single letter (I, V, X) only after a ruler's
    # name, so "When I" or "Part V" are left alone.
    t = re.sub(r"\b([A-Z][a-zâêîôûŵŷ’']+) (XIII|XII|XI|IX|VIII|VII|VI|IV|III|II)\b", one, t)
    return re.sub(rf"\b({RULERS}) (X|V|I)\b(?![’'][a-z])", one, t)


def clean(t, lang):
    """One line of the long read as it should be spoken: no source markers, no codes, numbers that read well."""
    cy = lang == "cy"
    t = re.sub(r"\s*\[\[cite:[^\]]*\]\]", "", t)            # the § source chips
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)          # a [link](address) keeps its words
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    t = _regnal(t, cy)
    t = re.sub(r"\bc\. ?(?=\d)", "tua " if cy else "about ", t)
    t = re.sub(r"(\d)\s*[–—-]\s*(\d)", r"\1 i \2" if cy else r"\1 to \2", t)   # 1067–1283
    t = re.sub(r"\bSt\.? (?=[A-Z])", "Saint ", t) if not cy else t
    t = t.replace(" & ", " a " if cy else " and ").replace("§", "")
    t = re.sub(r"(\d)%", r"\1 y cant" if cy else r"\1 per cent", t)
    t = t.replace("…", "...").replace(" – ", ", ").replace(" — ", ", ").replace("—", ", ")
    return re.sub(r"\s+", " ", t).strip()


def spoken(x, lang):
    """The long read as read aloud: a list of sections, each {"head": heading or None, "parts": [(kind, text)]}.
    kind is title, head, para, quote, cite or row. The first section is the opening (title and summary and anything
    before the first heading); every "## " heading starts a new section, in the same order as the page's headings."""
    cy = lang == "cy"
    title, summary = (x["cy"], x["sumCy"]) if cy else (x["en"], x["sumEn"])
    pars = x["pCy"] if cy else x["pEn"]
    secs = [{"head": None, "parts": [("title", clean(title, lang)), ("para", clean(summary, lang))]}]
    for p in pars:
        if not isinstance(p, str) or not p.strip():
            continue
        if p.startswith("!! ") or p.startswith("%%"):           # pictures and maps: nothing to say
            continue
        if p.startswith("## "):
            secs.append({"head": clean(p[3:], lang), "parts": [("head", clean(p[3:], lang))]})
        elif p.startswith("> "):
            q, _, c = p[2:].partition(" | ")
            secs[-1]["parts"].append(("quote", clean(q, lang)))
            if c.strip():
                secs[-1]["parts"].append(("cite", clean(c, lang)))
        elif p.startswith("|| "):
            a, _, b = p[3:].partition(" | ")
            a, b = clean(a, lang).rstrip(":"), clean(b, lang)
            secs[-1]["parts"].append(("row", f"{a}: {b}" if b else a))
        else:
            secs[-1]["parts"].append(("para", clean(p, lang)))
    secs[-1]["parts"].append(("end", "Diolch am wrando ar Hanes Cymru." if cy else "Thank you for listening to History of Wales."))
    return secs


def words_hash(x, lang):
    return hashlib.sha1(json.dumps(spoken(x, lang), ensure_ascii=False).encode("utf-8")).hexdigest()[:12]


def chars(x, lang):
    return sum(len(t) for s in spoken(x, lang) for _, t in s["parts"])


# ---------------------------------------------------------------- the player on the page

def _clock(s):
    s = int(round(s))
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60}:{s % 60:02d}"


def _mins(s):
    return max(1, int(round(s / 60)))


def player(x, e):
    """The Listen box for one long read, one copy per language (welshpages.split keeps the page's own). e = html escape."""
    got = MANIFEST.get(x["id"], {})
    out = ""
    for lang in ("en", "cy"):
        m = got.get(lang)
        if not m:
            continue
        cy = lang == "cy"
        who = CREDIT.get(m.get("engine", ""), ("", ""))[1 if cy else 0]
        if m.get("voice_name"):
            who += f" ({m['voice_name']})"
        marks = ",".join(f"{t:.2f}" for t in m.get("marks", []))
        T = (lambda en, c: c if cy else en)
        out += (f'<div class="listen l-{lang} no-print" lang="{lang}" data-id="{e(x["id"])}" data-src="listen/{e(m["file"])}?v={e(m["hash"])}" '
                f'data-secs="{m["secs"]:.1f}" data-marks="{marks}" data-title="{e(x["cy"] if cy else x["en"])}">'
                f'<button type="button" class="ls-go" aria-label="{T("Listen to this long read", "Gwrando ar yr erthygl hon")}">'
                f'<svg viewBox="0 0 24 24" aria-hidden="true"><path class="i-play" d="M8 5.5v13l11-6.5z"/><path class="i-pause" d="M7 5h4v14H7zM13 5h4v14h-4z"/></svg></button>'
                f'<div class="ls-txt"><b>{T("Listen to this long read", "Gwrando ar yr erthygl hon")}</b>'
                f'<small><span class="ls-len">{_mins(m["secs"])} {T("min", "munud")}</span> · {e(who)}</small></div>'
                f'<button type="button" class="ls-resume" hidden></button>'
                f'<div class="ls-more" hidden>'
                f'<div class="ls-bar"><input type="range" class="ls-seek" min="0" max="{m["secs"]:.1f}" step="1" value="0" aria-label="{T("Position", "Safle")}"><span class="ls-ticks" aria-hidden="true"></span></div>'
                f'<div class="ls-row"><span class="ls-time">0:00 / {_clock(m["secs"])}</span><span class="ls-sec" aria-live="polite"></span></div>'
                f'<div class="ls-row ls-ctl">'
                f'<button type="button" class="ls-back" aria-label="{T("Back 15 seconds", "Yn ôl 15 eiliad")}">−15</button>'
                f'<button type="button" class="ls-fwd" aria-label="{T("Forward 30 seconds", "Ymlaen 30 eiliad")}">+30</button>'
                f'<button type="button" class="ls-prev" aria-label="{T("Previous section", "Adran flaenorol")}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5h2.5v14H6zM20 5.5v13L9.5 12z"/></svg></button>'
                f'<button type="button" class="ls-next" aria-label="{T("Next section", "Adran nesaf")}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15.5 5H18v14h-2.5zM4 5.5v13L14.5 12z"/></svg></button>'
                f'<button type="button" class="ls-rate" aria-label="{T("Speed", "Cyflymder")}">1×</button>'
                f'<a class="ls-dl" download>{T("Download", "Lawrlwytho")}</a>'
                f'</div></div></div>')
    return out


def has_audio(x):
    return bool(MANIFEST.get(x["id"]))


CSS = """
/* ---------- long reads read aloud (src/listen.py, src/static/listen.js) ---------- */
.listen { display: grid; grid-template-columns: auto minmax(0, 1fr) auto; align-items: center; gap: .4rem 1rem; margin: 0 0 1.6rem; padding: .8rem 1rem .8rem .8rem; border: 1px solid var(--line); border-radius: 18px; background: var(--card) }
.listen .ls-go { width: 3.4rem; height: 3.4rem; border-radius: 50%; border: 0; display: grid; place-items: center; background: var(--c, var(--gold)); color: #0c0f16; cursor: pointer; transition: transform .15s var(--ease) }
.listen .ls-go:hover { transform: scale(1.06) }
.listen .ls-go svg { width: 1.5rem; height: 1.5rem; fill: currentColor }
.listen .i-pause, .listen.playing .i-play { display: none }
.listen.playing .i-pause { display: inline }
.listen .ls-txt { min-width: 0 }
.listen .ls-txt b { display: block; font: 600 1.02rem var(--f-body); color: var(--ink) }
.listen .ls-txt small { display: block; font: 500 .74rem var(--f-mono); color: var(--muted); letter-spacing: .02em; margin-top: .15rem }
.listen .ls-resume { font: 600 .78rem var(--f-mono); color: var(--c, var(--gold)); background: none; border: 1px solid var(--line); border-radius: 999px; padding: .5rem .9rem; min-height: 44px; cursor: pointer }
.listen .ls-resume:hover { border-color: var(--c, var(--gold)) }
.listen .ls-more { grid-column: 1 / -1; display: grid; gap: .5rem; padding-top: .3rem }
.listen .ls-more[hidden], .listen .ls-resume[hidden] { display: none }
.listen .ls-bar { position: relative; height: 28px }
.listen .ls-seek { position: absolute; inset: 0; width: 100%; margin: 0; accent-color: var(--c, var(--gold)); cursor: pointer; background: transparent }
.listen .ls-ticks { position: absolute; left: 0; right: 0; top: 50%; height: 0; pointer-events: none }
.listen .ls-ticks i { position: absolute; top: -7px; width: 2px; height: 14px; border-radius: 1px; background: var(--muted); opacity: .55 }
.listen .ls-row { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: .4rem 1rem; font: 500 .78rem var(--f-mono); color: var(--muted) }
.listen .ls-sec { color: var(--ink); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: 100% }
.listen .ls-ctl { justify-content: flex-start; gap: .4rem }
.listen .ls-ctl button, .listen .ls-ctl a { min-width: 44px; min-height: 40px; padding: 0 .75rem; border-radius: 999px; border: 1px solid var(--line); background: none; color: var(--ink); font: 600 .8rem var(--f-mono); cursor: pointer; display: inline-grid; place-items: center; text-decoration: none }
.listen .ls-ctl svg { width: 1rem; height: 1rem; fill: currentColor }
.listen .ls-ctl button:hover, .listen .ls-ctl a:hover { border-color: var(--c, var(--gold)) }
.listen .ls-ctl .ls-dl { margin-left: auto; color: var(--muted) }
.listen.err .ls-txt small::after { content: " · " attr(data-err) }
/* a small bar at the foot of the screen while the sound plays and the box is out of sight */
.ls-mini { position: fixed; left: 50%; transform: translateX(-50%); bottom: calc(16px + env(safe-area-inset-bottom, 0px)); z-index: 25; width: min(34rem, calc(100vw - 32px)); display: flex; align-items: center; gap: .6rem; padding: .4rem .5rem .4rem .4rem; border-radius: 999px; border: 1px solid var(--line); background: rgba(21,26,37,.95); -webkit-backdrop-filter: blur(8px); backdrop-filter: blur(8px); color: var(--ink); font-size: .86rem; animation: fade .3s both }
.ls-mini[hidden] { display: none }
.ls-mini button { flex: none; width: 2.6rem; height: 2.6rem; border-radius: 50%; border: 0; display: grid; place-items: center; background: var(--c, var(--gold)); color: #0c0f16; cursor: pointer }
.ls-mini button svg { width: 1.1rem; height: 1.1rem; fill: currentColor }
.ls-mini .i-pause, .ls-mini.playing .i-play { display: none }
.ls-mini.playing .i-pause { display: inline }
.ls-mini a { flex: 1; min-width: 0; color: inherit; text-decoration: none; display: flex; flex-direction: column }
.ls-mini a b { font-weight: 600; overflow: hidden; white-space: nowrap; text-overflow: ellipsis }
.ls-mini a small { font: 500 .72rem var(--f-mono); color: var(--muted) }
.ls-mini .ls-mbar { position: absolute; left: 1.4rem; right: 1.4rem; bottom: 0; height: 2px; background: var(--line); border-radius: 2px; overflow: hidden }
.ls-mini .ls-mbar i { display: block; height: 100%; width: 0; background: var(--c, var(--gold)) }
body.ls-on .toc-pill { bottom: calc(80px + env(safe-area-inset-bottom, 0px)) }
/* "Listen from here" beside each heading, once the reader has started listening */
.prose h2 .ls-here { margin-left: .5rem; vertical-align: middle; width: 2rem; height: 2rem; border-radius: 50%; border: 1px solid var(--line); background: none; color: var(--c, var(--gold)); cursor: pointer; display: inline-grid; place-items: center; padding: 0 }
.prose h2 .ls-here svg { width: .85rem; height: .85rem; fill: currentColor }
.prose h2 .ls-here:hover { border-color: var(--c, var(--gold)) }
@media (max-width: 560px) {
  .listen { grid-template-columns: auto minmax(0, 1fr) }
  .listen .ls-resume { grid-column: 1 / -1; justify-self: start }
  .listen .ls-ctl .ls-dl { margin-left: 0 }
}
@media (prefers-reduced-motion: reduce) { .listen .ls-go, .ls-mini { transition: none; animation: none } }
@media print { .listen, .ls-mini, .ls-here { display: none !important } }
"""
