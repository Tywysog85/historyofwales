"""Tell Bing (and Yandex, Seznam, Naver, which share IndexNow) about pages that changed today.

Run by the deploy workflow just after the site goes live:
    python3 tools/indexnow.py https://historyofwales.cymru/

It reads seo-lastmod.json from the live site (written by build.py, see src/seo.py),
picks the pages whose "last changed" date is today, and sends their addresses to IndexNow.
The key file proving the site is ours is at <site>/<key>.txt. This never fails the run.
"""
import datetime, json, sys, time, urllib.error, urllib.request
from urllib.parse import urlparse

sys.path.insert(0, __file__.rsplit("/", 2)[0] + "/src")
from seo import INDEXNOW_KEY, LASTMOD_FILE  # noqa: E402


def main():
    base = (sys.argv[1] if len(sys.argv) > 1 else "https://historyofwales.cymru/").rstrip("/") + "/"
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    marks = {}
    for attempt in range(6):   # the new site can take a minute to appear everywhere
        try:
            req = urllib.request.Request(f"{base}{LASTMOD_FILE}?t={int(time.time())}", headers={"User-Agent": "historyofwales-indexnow"})
            with urllib.request.urlopen(req, timeout=20) as r:
                marks = json.loads(r.read().decode("utf-8"))
            if any(v[1] == today for v in marks.values()):
                break
        except Exception as ex:
            print("Could not read the page dates yet:", ex)
        time.sleep(20)
    urls = sorted(base + ("" if p == "index.html" else p) for p, v in marks.items() if v[1] == today)
    if not urls:
        print("No pages changed today; nothing to send.")
        return
    body = json.dumps({"host": urlparse(base).hostname, "key": INDEXNOW_KEY, "keyLocation": f"{base}{INDEXNOW_KEY}.txt",
                       "urlList": urls[:10000]}).encode("utf-8")
    # Some firewalls turn away Python's default "Python-urllib" name, so give a plain one. Try Bing directly if the shared address refuses.
    for endpoint in ("https://api.indexnow.org/indexnow", "https://www.bing.com/indexnow"):
        try:
            req = urllib.request.Request(endpoint, data=body, method="POST",
                                         headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "historyofwales-indexnow/1.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                print(f"Sent {len(urls)} changed pages to {endpoint}: HTTP {r.status}")
                return
        except urllib.error.HTTPError as ex:
            print(f"{endpoint} did not accept the list (no harm done): HTTP {ex.code} {ex.read()[:300]!r}")
        except Exception as ex:
            print(f"{endpoint} could not be reached (no harm done): {ex}")


if __name__ == "__main__":
    main()
