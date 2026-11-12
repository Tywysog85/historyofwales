"""A proper Welsh voice for every play button that has no real recording yet.

tools/fetch_audio.py brings in real speakers from Lingua Libre first. For any Welsh word or phrase still without one,
this script makes the sound with Piper, an open speech engine, using its Welsh voices trained by Bangor University's
language technology unit (Uned Technolegau Iaith, techiaith). That is a real Welsh voice reading Welsh, not a phone's
English voice guessing at the spelling.

Because nobody can listen to hundreds of clips by hand, it checks itself: a Welsh speech recogniser (techiaith's
wav2vec2 model) writes down what each test clip says, and the voice whose clips come back closest to the real spelling
is the one used for the site. The real Lingua Libre recordings are put through the same test as a yardstick. The
scores go in _research/voice/report.txt.

Clips are saved as src/static/audio/<slug>.mp3 (trimmed and evened like the real recordings) and credited in
src/audio_credits.json with "kind": "voice", so welsh.html can thank the voice's makers. A real recording always wins:
fetch_audio.py replaces a voice clip as soon as one turns up, and this script never touches a real recording or your own.

Hugging Face is blocked from Claude's cloud computer, so this runs on GitHub (.github/workflows/welsh-voice.yml).
Run after `python3 build.py` and `python3 tools/fetch_audio.py`. Needs ffmpeg and `pip install piper-tts`;
the recogniser also needs `pip install torch transformers` (without them the first voice is used, unchecked).
"""
import json, os, re, subprocess, sys, tempfile, unicodedata, urllib.request, wave

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import fetch_audio as FA  # noqa: E402

OUT = FA.OUT
CREDITS = FA.CREDITS
REPORT = os.path.join(ROOT, "_research", "voice")
CACHE = os.path.join(tempfile.gettempdir(), "piper-voices")
HF = "https://huggingface.co/rhasspy/piper-voices/resolve/main/"
VOICES = [  # Piper's Welsh voices trained on Bangor University's BU-TTS recordings (dataset licence CC BY)
    ("bu_tts", "cy/cy_GB/bu_tts/medium/cy_GB-bu_tts-medium"),
]
LENGTH = 1.15  # a touch slower than normal speech, for learners
REDO = "--redo" in sys.argv  # make every voice clip again (after changing the voice or the settings)


def get(url, dst):
    if not os.path.exists(dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": FA.UA}), timeout=300) as r, open(dst + ".part", "wb") as f:
            f.write(r.read())
        os.replace(dst + ".part", dst)
    return dst


def load_voices():
    from piper import PiperVoice
    out = []
    for name, path in VOICES:
        try:
            onnx = get(HF + path + ".onnx", os.path.join(CACHE, name + ".onnx"))
            get(HF + path + ".onnx.json", onnx + ".json")
            card = ""
            try:
                card = open(get(HF + os.path.dirname(path) + "/MODEL_CARD", os.path.join(CACHE, name + ".MODEL_CARD")), encoding="utf-8").read()
            except Exception:  # noqa: BLE001
                pass
            cfg = json.load(open(onnx + ".json", encoding="utf-8"))
            v = PiperVoice.load(onnx)
            speakers = sorted((cfg.get("speaker_id_map") or {}).items(), key=lambda x: x[1]) or [("", None)]
            for sname, sid in speakers[:8]:
                out.append(dict(name=name + (f":{sname}" if sname else ""), voice=v, sid=sid, card=card, path=path))
            print(f"Voice {name}: {len(speakers)} speaker(s)")
        except Exception as ex:  # noqa: BLE001
            print(f"Voice {name} not available: {ex}")
    return out


def clean(text):
    t = unicodedata.normalize("NFC", text).replace("’", "'").replace("‘", "'").replace("…", "").strip()
    return re.sub(r"\s+", " ", t)


def say(v, text, wav_path):
    with wave.open(wav_path, "wb") as wf:
        try:  # piper-tts 1.3 and later
            from piper import SynthesisConfig
            v["voice"].synthesize_wav(clean(text), wf, syn_config=SynthesisConfig(speaker_id=v["sid"], length_scale=LENGTH))
        except ImportError:  # older piper-tts
            v["voice"].synthesize(clean(text), wf, speaker_id=v["sid"], length_scale=LENGTH)


def plain(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z ]+", "", re.sub(r"[-']", " ", s)).split()


def cer(ref, hyp):
    a, b = " ".join(plain(ref)), " ".join(plain(hyp))
    if not a:
        return 0.0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return min(1.0, prev[-1] / len(a))


def asr_candidates():
    """techiaith's Welsh speech recognisers on Hugging Face (names change, so ask), then Whisper, which knows Welsh."""
    found = []
    try:
        url = "https://huggingface.co/api/models?author=techiaith&search=wav2vec2&limit=100"
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": FA.UA}), timeout=60) as r:
            ids = [m["id"] for m in json.loads(r.read())]
        print("techiaith wav2vec2 models:", ", ".join(ids))
        parts = {i: re.split(r"[-_]", i.lower().split("/")[1]) for i in ids}
        welsh = [i for i in ids if "cy" in parts[i] and "ft" in parts[i] and not any("lm" in p for p in parts[i])]
        found += sorted(welsh, key=lambda i: ("en" in parts[i], "1b" in parts[i], len(i)))
    except Exception as ex:  # noqa: BLE001
        print("Could not list techiaith models:", ex)
    return found[:3] + ["openai/whisper-small", "openai/whisper-medium"]


def recogniser(yard):
    """The first recogniser that understands the real recordings (yard: [(text, mp3)]) well enough to judge voices."""
    try:
        from transformers import pipeline
    except Exception as ex:  # noqa: BLE001
        print("No speech recogniser (transformers not installed):", ex)
        return None, ""
    for m in asr_candidates():
        try:
            if "whisper" in m:
                asr = pipeline("automatic-speech-recognition", model=m, generate_kwargs={"language": "welsh", "task": "transcribe"})
            else:
                asr = pipeline("automatic-speech-recognition", model=m)
            fn = (lambda wav, asr=asr: asr(wav)["text"])
            errs = [cer(t, fn(to_16k(mp3, os.path.join(tempfile.gettempdir(), "yard.wav")))) for t, mp3 in yard]
            score = sum(errs) / len(errs) if errs else 0
            print(f"Recogniser {m}: error {score:.3f} on {len(errs)} real recordings")
            if score < 0.5:
                return fn, f"{m} (error {score:.3f} on real recordings)"
        except Exception as ex:  # noqa: BLE001
            print(f"Recogniser {m} not available: {ex}")
    return None, ""


def to_16k(src, dst):
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", src, "-ac", "1", "-ar", "16000", dst], check=True)
    return dst


def main():
    import data as D
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(REPORT, exist_ok=True)
    credits = json.load(open(CREDITS, encoding="utf-8")) if os.path.exists(CREDITS) else {}
    texts = FA.wanted()

    def free(s):  # no real recording and none of your own: the voice may fill it
        if s in credits:
            return credits[s].get("kind") == "voice" and (REDO or not os.path.exists(os.path.join(OUT, s + ".mp3")))
        return not os.path.exists(os.path.join(OUT, s + ".mp3"))

    todo, seen = [], set()
    for t in texts:
        s = FA.slug(t)
        if s and s not in seen and free(s):
            seen.add(s)
            todo.append(t)
    print(f"{len(texts)} Welsh texts on the site; {len(todo)} need the Welsh voice")
    if not todo:
        return
    voices = load_voices()
    if not voices:
        raise SystemExit("No Welsh voice could be loaded")
    real = [(c["text"], os.path.join(OUT, k + ".mp3")) for k, c in sorted(credits.items())
            if c.get("kind") != "voice" and " " not in c["text"] and os.path.exists(os.path.join(OUT, k + ".mp3"))]
    asr, asr_name = recogniser(real[:: max(1, len(real) // 12)][:12])
    lines = [f"Speech recogniser: {asr_name or 'none'}"]
    with tempfile.TemporaryDirectory() as tmp:
        best = voices[0]
        if asr and len(voices) > 1:
            # The test: the ten words on the home page, then a spread of the rest.
            home = [w[0] for w in D.WORDS]
            test = home + [t for t in todo if t not in home][:: max(1, len(todo) // 30)][:30]
            yard = []
            for t in home:  # real recordings already on the site, as a yardstick for the recogniser
                mp3 = os.path.join(OUT, FA.slug(t) + ".mp3")
                if os.path.exists(mp3) and not free(FA.slug(t)):
                    heard = asr(to_16k(mp3, os.path.join(tmp, "y.wav")))
                    yard.append(cer(t, heard))
                    lines.append(f"real recording   {t!r:34} heard {heard!r}  error {yard[-1]:.2f}")
            if yard:
                lines.append(f"Real recordings: average error {sum(yard) / len(yard):.3f}\n")
            scores = []
            for v in voices:
                errs = []
                for t in test:
                    w = os.path.join(tmp, "t.wav")
                    say(v, t, w)
                    heard = asr(to_16k(w, os.path.join(tmp, "t16.wav")))
                    errs.append(cer(t, heard))
                    lines.append(f"{v['name']:28} {t!r:34} heard {heard!r}  error {errs[-1]:.2f}")
                score = sum(errs) / len(errs)
                scores.append((score, v["name"]))
                lines.append(f"== {v['name']}: average error {score:.3f}\n")
                print(f"{v['name']}: average error {score:.3f}")
                if score < min([s for s, _ in scores[:-1]] or [9]):
                    best = v
            lines.append("Ranking: " + ", ".join(f"{n} {s:.3f}" for s, n in sorted(scores)))
        print("Using", best["name"])
        lines.append(f"\nChosen voice: {best['name']}")
        made = 0
        for t in todo:
            s = FA.slug(t)
            w = os.path.join(tmp, s + ".wav")
            say(best, t, w)
            FA.convert(w, os.path.join(OUT, s + ".mp3"))
            credits[s] = dict(text=t, kind="voice", voice=best["name"], speaker="Welsh voice from Bangor University (techiaith), via Piper",
                              licence="see model card", page="https://huggingface.co/rhasspy/piper-voices/tree/main/" + os.path.dirname(best["path"]))
            made += 1
        lic = re.search(r"(?im)^\s*\*?\s*(?:license|licence)[^:\n]*:\s*(.+)$", best["card"] or "")
        if lic:
            for c in credits.values():
                if c.get("kind") == "voice":
                    c["licence"] = lic.group(1).strip(" *`")
    with open(CREDITS, "w", encoding="utf-8") as f:
        json.dump(dict(sorted(credits.items())), f, ensure_ascii=False, indent=1)
        f.write("\n")
    for v in voices:
        if v["card"]:
            open(os.path.join(REPORT, v["name"].split(":")[0] + ".MODEL_CARD.txt"), "w", encoding="utf-8").write(v["card"])
    open(os.path.join(REPORT, "report.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"Made {made} clips with the Welsh voice")


if __name__ == "__main__":
    main()
