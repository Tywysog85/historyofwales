"""Real Welsh voices: download free recordings of the site's Welsh words and phrases from Lingua Libre (on Wikimedia
Commons) and keep them on the site as small MP3s in src/static/audio/.

Run after `python3 build.py` (it reads the play buttons in _site). For each Welsh word or phrase the site can play, it looks
for a Lingua Libre recording of exactly that text, preferring the speakers who recorded the most of our words so the
voices stay consistent. Each file is trimmed of silence, evened in loudness and saved as <slug>.mp3, named the same way
the play buttons look for it (lower case, accents dropped, spaces and punctuation as hyphens). The speaker, licence and
Commons page of each go into src/audio_credits.json, which welsh.html shows. MP3s that are not in that file (your own
recordings) are never touched. A clip made by the Welsh computer voice (tools/make_voice.py, "kind": "voice") is
replaced as soon as a real recording of the same words turns up.

Wikimedia is blocked from Claude's cloud computer, so this runs on GitHub: .github/workflows/fetch-audio.yml (start it
from the Actions tab, or it runs by itself when this file changes on a claude/ branch). Needs ffmpeg.
"""
import glob, html, json, os, re, subprocess, sys, tempfile, time, unicodedata, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
OUT = os.path.join(ROOT, "src", "static", "audio")
CREDITS = os.path.join(ROOT, "src", "audio_credits.json")
API = "https://commons.wikimedia.org/w/api.php"
UA = "HistoryOfWalesSiteBuilder/1.0 (https://historyofwales.cymru; static site build)"
LL = re.compile(r"^File:LL-Q9309 \(cym\)-(?P<who>[^-]+)-(?P<w>.+)\.(?:wav|ogg|oga|flac|mp3)$", re.I)
OLD = re.compile(r"^File:Cy-(?P<w>.+)\.(?:ogg|oga|wav|flac|mp3)$", re.I)


def slug(w):
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", w).strip("-")


def key(w):
    """How two spellings of the same text are matched: lower case, curly apostrophes made straight, no end stops."""
    w = unicodedata.normalize("NFC", w).lower().replace("’", "'").replace("‘", "'")
    return re.sub(r"[\s.!?,]+$", "", re.sub(r"\s+", " ", w)).strip()


def api(**params):
    params.update(format="json", formatversion="2")
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60) as r:
                return json.loads(r.read())
        except Exception as ex:  # noqa: BLE001
            print("  retry:", ex)
            time.sleep(2 ** attempt)
    raise SystemExit("Commons did not answer")


def wanted():
    """Every Welsh text the site has a play button for."""
    import cymraeg as CYM
    import data as D
    texts = set()
    for f in glob.glob(os.path.join(ROOT, "_site", "*.html")):
        for m in re.finditer(r'data-hear="([^"]+)"', open(f, encoding="utf-8").read()):
            texts.add(html.unescape(m.group(1)))
    texts.update(w[1] for w in CYM.WORDS)
    for sec in CYM.PHRASES:
        texts.update(p[0] for p in sec[5])
    texts.update(w[0] for w in D.WORDS)
    return sorted(t for t in texts if t.strip())


def recordings():
    """All Welsh Lingua Libre files on Commons (and the older Cy-... files): key -> [(title, speaker)]."""
    found = {}

    def add(title):
        m = LL.match(title)
        if m:
            found.setdefault(key(m.group("w")), []).append((title, m.group("who")))
            return True
        m = OLD.match(title)
        if m:
            found.setdefault(key(m.group("w")), []).append((title, ""))
            return True
        return False

    todo, done, odd = ["Category:Lingua Libre pronunciation-cym", "Category:Welsh pronunciation"], set(), []
    while todo and len(done) < 60:
        cat = todo.pop(0)
        if cat in done:
            continue
        done.add(cat)
        cont = {}
        while True:
            r = api(action="query", list="categorymembers", cmtitle=cat, cmtype="file|subcat", cmlimit="500", **cont)
            for m in r.get("query", {}).get("categorymembers", []):
                if m.get("ns") == 14:
                    todo.append(m["title"])
                elif not add(m["title"]) and len(odd) < 25:
                    odd.append(m["title"])
            if "continue" not in r:
                break
            cont = {"cmcontinue": r["continue"]["cmcontinue"]}
            time.sleep(0.3)
        print(f"{cat}: {sum(len(v) for v in found.values())} files so far")
    print("Names not understood, for example:", odd)
    return found


AUDIO_EXT = re.compile(r"\.(?:wav|ogg|oga|flac|mp3)$", re.I)
PREFIX = re.compile(r"^(?:LL-Q9309 \(cym\)-[^-]+-|Cy-gb-|Cy-|Welsh[- ]|cy[- ])", re.I)
FREE = re.compile(r"^(?:CC0|CC BY(?:-SA)? [\d.]+|Public domain|PD)", re.I)


def search_more(texts, have):
    """Recordings named some other way (e.g. "Cy-diolch.ogg" outside the categories): ask Commons search for each text
    that has none yet, and keep only audio files whose name, without prefix and ending, is exactly that text."""
    added = 0
    for t in texts:
        if key(t) in have or len(key(t)) < 2:
            continue
        r = api(action="query", list="search", srsearch=f'intitle:"{key(t)}" filetype:audio', srnamespace="6", srlimit="20")
        for m in r.get("query", {}).get("search", []):
            title = m["title"]
            name = title[5:] if title.startswith("File:") else title
            if not AUDIO_EXT.search(name):
                continue
            core = PREFIX.sub("", AUDIO_EXT.sub("", name)).replace("_", " ")
            if key(core) == key(t):
                lm = LL.match(title)
                have.setdefault(key(t), []).append((title, lm.group("who") if lm else ""))
                added += 1
        time.sleep(0.4)
    print(f"Commons search found {added} more recordings")


def info(titles):
    out = {}
    for i in range(0, len(titles), 40):
        r = api(action="query", titles="|".join(titles[i:i + 40]), prop="imageinfo", iiprop="url|extmetadata")
        for p in r.get("query", {}).get("pages", []):
            ii = (p.get("imageinfo") or [{}])[0]
            md = ii.get("extmetadata", {})
            artist = re.sub(r"<[^>]+>", "", md.get("Artist", {}).get("value", "")).strip()
            out[p["title"]] = dict(url=ii.get("url"), page=ii.get("descriptionurl"), artist=html.unescape(artist),
                                   licence=md.get("LicenseShortName", {}).get("value", ""))
        time.sleep(0.3)
    return out


def convert(src, dst):
    """Even the loudness, then trim the silence (and any click at the very start) from both ends."""
    af = ("loudnorm=I=-18:TP=-2,"
          "silenceremove=start_periods=1:start_duration=0.12:start_threshold=-28dB:start_silence=0.15:detection=rms,areverse,"
          "silenceremove=start_periods=1:start_duration=0.05:start_threshold=-38dB:start_silence=0.25:detection=rms,areverse")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", src, "-af", af, "-ac", "1", "-ar", "44100", "-b:a", "64k", dst], check=True)
    # A very short result means the trim was too keen: keep the evened, untrimmed sound instead.
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", dst], capture_output=True, text=True).stdout.strip()
    if not out or float(out) < 0.45:
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", src, "-af", "loudnorm=I=-18:TP=-2", "-ac", "1", "-ar", "44100", "-b:a", "64k", dst], check=True)


def main():
    os.makedirs(OUT, exist_ok=True)
    credits = json.load(open(CREDITS, encoding="utf-8")) if os.path.exists(CREDITS) else {}
    texts = wanted()
    have = recordings()
    search_more(texts, have)
    # Speakers who recorded most of our words come first, so neighbouring buttons tend to share a voice.
    score = {}
    for t in texts:
        for _, who in have.get(key(t), []):
            score[who] = score.get(who, 0) + 1
    picks = {}
    for t in texts:
        s = slug(t)
        if not s or s in picks:
            continue
        if os.path.exists(os.path.join(OUT, s + ".mp3")) and s not in credits:
            continue  # someone's own recording: keep it
        options = sorted(have.get(key(t), []), key=lambda x: (-score.get(x[1], 0), x[0]))
        if options:
            picks[s] = (t, options[0][0])
    print(f"{len(texts)} Welsh texts on the site; recordings found for {len(picks)}")
    meta = info(sorted({f for _, f in picks.values()}))
    done = 0
    with tempfile.TemporaryDirectory() as tmp:
        for s, (t, title) in sorted(picks.items()):
            m = meta.get(title)
            if not m or not m["url"]:
                continue
            if m["licence"] and not FREE.match(m["licence"]):
                print("  not a free licence, skipped:", title, m["licence"])
                continue
            if credits.get(s, {}).get("file") == title and os.path.exists(os.path.join(OUT, s + ".mp3")):
                continue
            raw = os.path.join(tmp, "in" + os.path.splitext(m["url"])[1])
            ok = False
            for attempt in range(5):
                try:
                    with urllib.request.urlopen(urllib.request.Request(m["url"], headers={"User-Agent": UA}), timeout=60) as r, open(raw, "wb") as f:
                        f.write(r.read())
                    convert(raw, os.path.join(OUT, s + ".mp3"))
                    ok = True
                    break
                except Exception as ex:  # noqa: BLE001  (Wikimedia answers 429 when we go too fast: wait and try again)
                    print("  waiting:", t, ex)
                    time.sleep(10 * (attempt + 1))
            if not ok:
                print("  skipped", t)
                continue
            who = LL.match(title).group("who") if LL.match(title) else (m["artist"] or "Wikimedia Commons")
            credits[s] = dict(text=t, file=title, speaker=who, licence=m["licence"] or "CC BY-SA 4.0", page=m["page"])
            done += 1
            time.sleep(1.5)
    with open(CREDITS, "w", encoding="utf-8") as f:
        json.dump(dict(sorted(credits.items())), f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"Saved {done} new recordings; {len(credits)} recordings credited in {CREDITS}")
    def real(s):
        return (s in credits and credits[s].get("kind") != "voice") or (s not in credits and os.path.exists(os.path.join(OUT, s + ".mp3")))
    missing = [t for t in texts if not real(slug(t))]
    print(f"Still no recording for {len(missing)}: " + ", ".join(missing[:80]))


if __name__ == "__main__":
    main()
