"""Make the spoken versions of the long reads (src/listen.py explains the whole feature).

Runs on GitHub (.github/workflows/listen.yml): Hugging Face, Microsoft and ElevenLabs cannot be reached from Claude's
cloud computer. The words come from src/listen.py's spoken(), so the sound always matches the page.

    python3 tools/make_listen.py script <id> <en|cy>       the words exactly as they will be read, to check them
    python3 tools/make_listen.py plan <shards>              which files need making, split into shards (JSON, for the workflow)
    python3 tools/make_listen.py make <shard> <shards> DIR  make this shard's files: DIR/<id>-<lang>.m4a and .json
    python3 tools/make_listen.py merge DIR                  put DIR/*.json into src/listen.json
    python3 tools/make_listen.py sample DIR                 short clips of every voice in tools/listen_request.json "sample"

Which voice reads each language, and what to make, is set in tools/listen_request.json:
    "en" / "cy":  a key of VOICES below, e.g. "azure:en-GB-RyanNeural" or "piper:gwryw-gogledd-pro"
    "only":       long-read ids to make again even if nothing changed ([] = only the new and the changed ones)
    "redo":       true makes every file again (after changing the voice)
    "sample":     {"id": "glyndwr", "sections": 2, "voices": [...]} for listening tests, or null

Every file is made section by section (the opening, then one per heading); the time each section starts is saved, so
the player can jump to a heading. Pauses between paragraphs, before headings and around quotes are added here, so all
voices are paced alike. The finished file is evened out in loudness (ffmpeg loudnorm) and saved as AAC (.m4a), which
every browser plays, at 32 kbit/s mono: clear speech at about 14 MB an hour.

Keys (GitHub repository secrets, never in the code): AZURE_SPEECH_KEY and AZURE_SPEECH_REGION for Microsoft;
ELEVENLABS_API_KEY for ElevenLabs. Kokoro and Piper are free and need none.
"""
import array, glob, json, os, re, subprocess, sys, tempfile, time, urllib.error, urllib.request, wave
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
import features as F  # noqa: E402
import listen as L  # noqa: E402
sys.path.insert(0, os.path.join(ROOT, "tools"))
import welsh_words as WW  # noqa: E402

_CY = set()


def cy_words():
    """Every word in the Welsh text of the long reads (for telling the Welsh words in the English text)."""
    if not _CY:
        for x in F.STORIES:
            for s in L.spoken(x, "cy"):
                for _, t in s["parts"]:
                    _CY.update(WW.tokens(t))
    return _CY

REQUEST = os.path.join(ROOT, "tools", "listen_request.json")
UA = "HistoryOfWalesSiteBuilder/1.0 (https://historyofwales.cymru; static site build)"
CACHE = os.path.join(tempfile.gettempdir(), "listen-voices")

# key: (engine, language, the engine's own voice name, name shown in the player)
VOICES = {
    # Microsoft Azure neural voices (paid, about $16 per million characters; 0.5 million free a month on the F0 tier)
    "azure:en-GB-RyanNeural": ("azure", "en", "en-GB-RyanNeural", "Ryan"),
    "azure:en-GB-SoniaNeural": ("azure", "en", "en-GB-SoniaNeural", "Sonia"),
    "azure:en-GB-OllieMultilingualNeural": ("azure", "en", "en-GB-OllieMultilingualNeural", "Ollie"),
    "azure:en-GB-AdaMultilingualNeural": ("azure", "en", "en-GB-AdaMultilingualNeural", "Ada"),
    # the same two multilingual voices told to say each Welsh word and name the Welsh way (tools/welsh_words.py)
    "azure:en-GB-OllieMultilingualNeural+cy": ("azure", "en", "en-GB-OllieMultilingualNeural+cy", "Ollie"),
    "azure:en-GB-AdaMultilingualNeural+cy": ("azure", "en", "en-GB-AdaMultilingualNeural+cy", "Ada"),
    "azure:cy-GB-AledNeural": ("azure", "cy", "cy-GB-AledNeural", "Aled"),
    "azure:cy-GB-NiaNeural": ("azure", "cy", "cy-GB-NiaNeural", "Nia"),
    # Kokoro (free, Apache 2.0, hexgrad/Kokoro-82M): British English voices, and its best American one for comparison
    "kokoro:bm_george": ("kokoro", "en", "bm_george", "George"),
    "kokoro:bm_fable": ("kokoro", "en", "bm_fable", "Fable"),
    "kokoro:bm_lewis": ("kokoro", "en", "bm_lewis", "Lewis"),
    "kokoro:bm_daniel": ("kokoro", "en", "bm_daniel", "Daniel"),
    "kokoro:bf_emma": ("kokoro", "en", "bf_emma", "Emma"),
    "kokoro:bf_isabella": ("kokoro", "en", "bf_isabella", "Isabella"),
    "kokoro:af_heart": ("kokoro", "en", "af_heart", "Heart"),
    # Bangor University's BU-TTS Welsh voice through Piper (free, the one on the site's play buttons)
    "piper:gwryw-gogledd-pro": ("piper", "cy", "gwryw-gogledd-pro", "BU-TTS"),
    # ElevenLabs (paid): voice ids are set when an account exists
}
for _k in list(os.environ.get("LISTEN_EXTRA_VOICES", "").split(",")):  # "elevenlabs:<id>:<en|cy>:<Name>" for tests
    if _k.count(":") == 3:
        _eng, _id, _lang, _nm = _k.split(":")
        VOICES[f"{_eng}:{_id}"] = (_eng, _lang, _id, _nm)

# Pauses, in seconds: before and after each kind of line. Gentle, like someone reading to a room.
PAUSE = {"title": (0.3, 0.9), "head": (1.1, 0.6), "para": (0, 0.55), "quote": (0.25, 0.4), "cite": (0, 0.7),
         "row": (0, 0.35), "end": (0.9, 0.6)}
SPEED = {"kokoro": 0.95, "piper": 1.0, "azure": 0.97, "elevenlabs": 1.0}
BITRATE = "32k"  # was 40k until 14 Nov 2026; any file made at another rate is remade on the next run (see jobs())


def request():
    try:
        return json.load(open(REQUEST, encoding="utf-8"))
    except FileNotFoundError:
        return {}


# ---------------------------------------------------------------- engines: each turns text into 16-bit mono samples

class Engine:
    rate = 24000

    def say(self, text, kind):  # -> array('h')
        raise NotImplementedError

    def section(self, parts):
        """One section: [(kind, text)] -> (samples, rate). Default: line by line, with our own pauses."""
        out = array.array("h")
        for i, (kind, text) in enumerate(parts):
            before, after = PAUSE.get(kind, (0, 0.5))
            if i == 0 and kind == "head":
                before = 0
            out.extend(silence(before, self.rate))
            out.extend(trim(self.say(text, kind), self.rate))
            out.extend(silence(after, self.rate))
        return out


def silence(s, rate):
    return array.array("h", bytes(2 * int(s * rate)))


def trim(a, rate, thr=350):
    """Drop the quiet at both ends of one line (engines add their own), keeping 40 ms."""
    n, i, j = len(a), 0, len(a)
    while i < n and abs(a[i]) < thr:
        i += 1
    while j > i and abs(a[j - 1]) < thr:
        j -= 1
    pad = int(0.04 * rate)
    return a[max(0, i - pad):min(n, j + pad)]


def from_float(x):
    """numpy / torch float audio (-1..1) -> array('h')."""
    import numpy as np
    x = np.asarray(x.detach().cpu().numpy() if hasattr(x, "detach") else x, dtype="float32")
    return array.array("h", (np.clip(x, -1, 1) * 32767).astype("<i2").tobytes())


def get(url, dst):
    if not os.path.exists(dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=300) as r, open(dst + ".part", "wb") as f:
            f.write(r.read())
        os.replace(dst + ".part", dst)
    return dst


class Piper(Engine):
    HF = "https://huggingface.co/rhasspy/piper-voices/resolve/main/cy/cy_GB/bu_tts/medium/cy_GB-bu_tts-medium"

    def __init__(self, speaker):
        from piper import PiperVoice
        onnx = get(self.HF + ".onnx", os.path.join(CACHE, "bu_tts.onnx"))
        get(self.HF + ".onnx.json", onnx + ".json")
        cfg = json.load(open(onnx + ".json", encoding="utf-8"))
        self.voice = PiperVoice.load(onnx)
        self.sid = (cfg.get("speaker_id_map") or {}).get(speaker)
        self.rate = cfg["audio"]["sample_rate"]
        print(f"Piper bu_tts, speaker {speaker} ({self.sid}), {self.rate} Hz; speakers: {sorted(cfg.get('speaker_id_map') or {})}")

    def say(self, text, kind):
        path = os.path.join(tempfile.gettempdir(), "listen-piper.wav")
        with wave.open(path, "wb") as wf:
            try:
                from piper import SynthesisConfig
                self.voice.synthesize_wav(text, wf, syn_config=SynthesisConfig(speaker_id=self.sid, length_scale=1 / SPEED["piper"]))
            except ImportError:
                self.voice.synthesize(text, wf, speaker_id=self.sid, length_scale=1 / SPEED["piper"])
        with wave.open(path) as wf:
            return array.array("h", wf.readframes(wf.getnframes()))


class Kokoro(Engine):
    def __init__(self, voice):
        from kokoro import KPipeline
        self.voice = voice
        self.pipe = KPipeline(lang_code=voice[0], repo_id="hexgrad/Kokoro-82M")  # 'b' British, 'a' American

    def say(self, text, kind):
        out = array.array("h")
        for _, _, audio in self.pipe(text, voice=self.voice, speed=SPEED["kokoro"], split_pattern=r"\n+"):
            if audio is not None:
                out.extend(from_float(audio))
        return out


class Azure(Engine):
    """Microsoft's neural voices. One request per section (a few paragraphs, with breaks written into the SSML), which
    keeps well inside the free tier's limit of 20 requests a minute."""
    MAX = 3500  # characters of text in one request (a request may not give more than 10 minutes of sound)

    def __init__(self, voice):
        voice, _, mode = voice.partition("+")
        self.voice, self.lang, self.welsh = voice, voice[:5], mode == "cy"
        self.key, self.region = os.environ["AZURE_SPEECH_KEY"], os.environ.get("AZURE_SPEECH_REGION", "uksouth")
        self.last = 0.0

    def ssml(self, parts):
        body = ""
        for i, (kind, text) in enumerate(parts):
            before, after = PAUSE.get(kind, (0, 0.5))
            if before and i:
                body += f'<break time="{int(before * 1000)}ms"/>'
            body += WW.mark(escape(text), cy_words(), lambda run: f'<lang xml:lang="cy-GB">{run}</lang>') if self.welsh else escape(text)
            if after:
                body += f'<break time="{int(after * 1000)}ms"/>'
        rate = f"{round((SPEED['azure'] - 1) * 100):+d}%"
        return (f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="{self.lang}">'
                f'<voice name="{self.voice}">' + (body if self.welsh else f'<prosody rate="{rate}">{body}</prosody>') + '</voice></speak>')
        # (<lang> is not allowed inside <prosody>, so the Welsh-aware voices keep their own pace)

    def post(self, ssml):
        url = f"https://{self.region}.tts.speech.microsoft.com/cognitiveservices/v1"
        for attempt in range(8):
            wait = 3.2 - (time.time() - self.last)  # at most about 19 requests a minute
            if wait > 0:
                time.sleep(wait)
            self.last = time.time()
            req = urllib.request.Request(url, data=ssml.encode("utf-8"), method="POST", headers={
                "Ocp-Apim-Subscription-Key": self.key, "Content-Type": "application/ssml+xml",
                "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm", "User-Agent": "historyofwales-listen"})
            try:
                with urllib.request.urlopen(req, timeout=300) as r:
                    data = r.read()
                return array.array("h", data[44:])  # past the 44-byte WAV header
            except urllib.error.HTTPError as ex:
                if ex.code in (429, 500, 502, 503, 504):
                    time.sleep(10 * (attempt + 1))
                    continue
                raise SystemExit(f"Azure said {ex.code}: {ex.read()[:300]!r}")
            except (urllib.error.URLError, TimeoutError):
                time.sleep(10 * (attempt + 1))
        raise SystemExit("Azure did not answer after 8 tries")

    def section(self, parts):
        out, chunk, size = array.array("h"), [], 0
        for p in parts + [None]:
            if p is None or (chunk and size + len(p[1]) > self.MAX):
                out.extend(self.post(self.ssml(chunk)))
                chunk, size = [], 0
            if p is not None:
                chunk.append(p)
                size += len(p[1])
        return out


class ElevenLabs(Engine):
    """ElevenLabs, paragraph by paragraph, each told the text either side so the reading flows on."""
    def __init__(self, voice):
        self.voice, self.key = voice, os.environ["ELEVENLABS_API_KEY"]
        self.model = os.environ.get("ELEVENLABS_MODEL", "eleven_multilingual_v2")

    def say(self, text, kind):
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice}?output_format=pcm_24000"
        body = json.dumps({"text": text, "model_id": self.model,
                           "voice_settings": {"stability": 0.55, "similarity_boost": 0.75, "speed": SPEED["elevenlabs"]}}).encode()
        for attempt in range(6):
            req = urllib.request.Request(url, data=body, method="POST", headers={"xi-api-key": self.key, "Content-Type": "application/json"})
            try:
                with urllib.request.urlopen(req, timeout=300) as r:
                    return array.array("h", r.read())
            except urllib.error.HTTPError as ex:
                if ex.code in (429, 500, 502, 503):
                    time.sleep(10 * (attempt + 1))
                    continue
                raise SystemExit(f"ElevenLabs said {ex.code}: {ex.read()[:300]!r}")
        raise SystemExit("ElevenLabs did not answer after 6 tries")


_ENGINES = {}


def engine(key):
    if key not in VOICES:
        raise SystemExit(f"tools/make_listen.py: unknown voice {key!r}; the voices are {sorted(VOICES)}")
    if key not in _ENGINES:
        kind, _, name, _ = VOICES[key]
        _ENGINES[key] = {"piper": Piper, "kokoro": Kokoro, "azure": Azure, "elevenlabs": ElevenLabs}[kind](name)
    return _ENGINES[key]


# ---------------------------------------------------------------- one whole long read

def render(x, lang, key, out_path, sections=None):
    """Make one file. Returns (seconds, [start of each heading's section in seconds])."""
    eng = engine(key)
    secs = L.spoken(x, lang)[:sections] if sections else L.spoken(x, lang)
    pcm, marks = array.array("h"), []
    for i, s in enumerate(secs):
        if i:
            marks.append(len(pcm) / eng.rate)
        pcm.extend(eng.section(s["parts"]))
        print(f"  {x['id']}-{lang}: section {i + 1}/{len(secs)}, {len(pcm) / eng.rate / 60:.1f} min", flush=True)
    raw = out_path + ".pcm"
    with open(raw, "wb") as f:
        f.write(pcm.tobytes())
    mp3 = out_path.endswith(".mp3")
    codec = ["-c:a", "libmp3lame", "-b:a", "64k"] if mp3 else ["-c:a", "aac", "-aac_coder", "twoloop", "-b:a", BITRATE, "-movflags", "+faststart"]
    meta = ["-metadata", f"title={x['cy'] if lang == 'cy' else x['en']}", "-metadata", "artist=Hanes Cymru" if lang == "cy" else "artist=History of Wales",
            "-metadata", "album=Hanes Cymru · History of Wales"]
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le", "-ar", str(eng.rate), "-ac", "1", "-i", raw,
                    "-af", "loudnorm=I=-18:TP=-1.5:LRA=11,aresample=24000", "-ac", "1", "-ar", "24000", *codec, *meta, out_path], check=True)
    os.remove(raw)
    return len(pcm) / eng.rate, marks


def jobs():
    """Every (id, lang) whose file is missing, out of date, read by another voice, or asked for again."""
    req, out = request(), []
    for x in F.STORIES:
        for lang in ("en", "cy"):
            key = req.get(lang)
            if not key:
                continue
            have = L.MANIFEST.get(x["id"], {}).get(lang)
            if (req.get("redo") or x["id"] in req.get("only", []) or not have or have.get("hash") != L.words_hash(x, lang)
                    or have.get("voice") != key or have.get("bitrate", "40k") != BITRATE):
                out.append((x["id"], lang))
    return out


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    by_id = {x["id"]: x for x in F.STORIES}
    if cmd == "script":
        for s in L.spoken(by_id[sys.argv[2]], sys.argv[3]):
            print("\n".join(f"[{k}] {t}" for k, t in s["parts"]), end="\n\n")
        return
    if cmd == "plan":
        n = int(sys.argv[2])
        js = jobs()
        # the longest first, dealt round the shards so each gets about the same amount of reading
        js.sort(key=lambda j: -L.chars(by_id[j[0]], j[1]))
        shards = [[] for _ in range(n)]
        for i, j in enumerate(js):
            shards[i % n if (i // n) % 2 == 0 else n - 1 - i % n].append(j)
        print(json.dumps({"count": len(js), "shards": [i for i in range(n) if shards[i]], "jobs": shards}))
        return
    if cmd == "make":
        k, n, out = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
        os.makedirs(out, exist_ok=True)
        req = request()
        js = json.loads(subprocess.run([sys.executable, __file__, "plan", str(n)], capture_output=True, text=True, check=True).stdout)["jobs"][k]
        for xid, lang in js:
            x, key = by_id[xid], req[lang]
            name = f"{xid}-{lang}.m4a"
            t0 = time.time()
            secs, marks = render(x, lang, key, os.path.join(out, name))
            eng, _, _, shown = VOICES[key]
            entry = {"file": name, "secs": round(secs, 1), "marks": [round(m, 2) for m in marks], "hash": L.words_hash(x, lang),
                     "voice": key, "engine": eng, "voice_name": shown, "bitrate": BITRATE, "bytes": os.path.getsize(os.path.join(out, name))}
            json.dump({"id": xid, "lang": lang, **entry}, open(os.path.join(out, f"{xid}-{lang}.json"), "w"), ensure_ascii=False)
            print(f"{name}: {secs / 60:.1f} min of sound in {(time.time() - t0) / 60:.1f} min, {entry['bytes'] / 1e6:.1f} MB", flush=True)
        return
    if cmd == "merge":
        m = dict(L.MANIFEST)
        for p in sorted(glob.glob(os.path.join(sys.argv[2], "*.json"))):
            j = json.load(open(p, encoding="utf-8"))
            m.setdefault(j.pop("id"), {})[j.pop("lang")] = j
        m = {k: m[k] for k in sorted(m) if k in by_id}  # long reads that no longer exist drop out
        with open(L.MANIFEST_PATH, "w", encoding="utf-8") as f:
            json.dump(m, f, ensure_ascii=False, indent=1)
            f.write("\n")
        print(f"src/listen.json: {sum(len(v) for v in m.values())} files for {len(m)} long reads")
        return
    if cmd == "sample":
        out = sys.argv[2]
        os.makedirs(out, exist_ok=True)
        s = request().get("sample") or {}
        x = by_id[s.get("id", "glyndwr")]
        if os.environ.get("AZURE_SPEECH_KEY"):  # what Microsoft offers for English and Welsh, to choose from
            region = os.environ.get("AZURE_SPEECH_REGION", "uksouth")
            req = urllib.request.Request(f"https://{region}.tts.speech.microsoft.com/cognitiveservices/voices/list",
                                         headers={"Ocp-Apim-Subscription-Key": os.environ["AZURE_SPEECH_KEY"]})
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    vs = [v for v in json.loads(r.read()) if v.get("Locale") in ("en-GB", "cy-GB") or "cy-GB" in (v.get("SecondaryLocaleList") or [])]
                json.dump(vs, open(os.path.join(out, "azure-voices.json"), "w"), ensure_ascii=False, indent=1)
                print(f"Azure: {len(vs)} English (UK) and Welsh voices listed in azure-voices.json")
            except Exception as ex:  # noqa: BLE001
                print(f"Azure voice list: {ex}")
        for key in s.get("voices", []):
            lang = VOICES[key][1]
            path = os.path.join(out, f"{x['id']}-{lang}-{key.replace(':', '-')}.mp3")
            try:
                secs, _ = render(x, lang, key, path, sections=s.get("sections", 2))
                print(f"{path}: {secs:.0f} s")
            except (Exception, SystemExit) as ex:  # noqa: BLE001  one voice failing should not stop the others
                print(f"{key}: failed: {ex}")
        return
    print(__doc__)


if __name__ == "__main__":
    main()
