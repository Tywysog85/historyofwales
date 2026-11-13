"""Check every link from the site to other websites, and list the ones that are broken.

Run by .github/workflows/check-links.yml once a week (the cloud computer Claude works on cannot reach most websites).
It reads the built pages in _site/, finds each outside address once, and asks each website for it, gently: a few
requests at a time to any one website, with a pause between them, and a browser-like "who is asking" line.

Only clear answers count as broken: "not found" (404), "gone" (410), or a website that no longer exists (no such name).
Many websites turn away automatic checkers (401, 403, 429, 5xx, timeouts); those are listed apart as "could not check",
because a person opening them in a browser usually gets the page.

Writes link-report.md (for the GitHub issue the workflow keeps up to date) and prints a summary.
"""
import collections
import concurrent.futures as cf
import html
import os
import re
import socket
import sys
import threading
import time
import urllib.error
import urllib.request

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SITE = os.path.join(ROOT, "_site")
OWN = ("historyofwales.cymru", "tywysog85.github.io", "localhost")
SKIP_HOSTS = ("fonts.googleapis.com", "fonts.gstatic.com", "gc.zgo.at", "historyofwales.goatcounter.com")
HREF = re.compile(r'\shref="(https?://[^"#\s]+)(?:#[^"]*)?"')
UA = "Mozilla/5.0 (compatible; HistoryOfWalesLinkCheck/1.0; +https://historyofwales.cymru/about.html)"
PER_HOST = 3          # requests at once to any one website
PAUSE = 0.4           # seconds each worker waits after a request to the same website
TIMEOUT = 25


def pages():
    for base, _, files in os.walk(SITE):
        for f in files:
            if f.endswith(".html"):
                yield os.path.join(base, f)


def collect():
    where = collections.defaultdict(list)
    for p in pages():
        rel = os.path.relpath(p, SITE).replace(os.sep, "/")
        with open(p, encoding="utf-8") as fh:
            for m in HREF.finditer(fh.read()):
                url = html.unescape(m.group(1))
                host = url.split("/")[2].split(":")[0].lower()
                if host.endswith(OWN) or host in SKIP_HOSTS:
                    continue
                if len(where[url]) < 3:
                    where[url].append(rel)
    return where


_locks = collections.defaultdict(lambda: threading.Semaphore(PER_HOST))


def ask(url):
    host = url.split("/")[2].lower()
    with _locks[host]:
        result = None
        for method in ("HEAD", "GET"):
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "text/html,*/*;q=0.8", "Accept-Language": "en-GB,cy;q=0.8"})
            try:
                with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                    result = ("ok", r.status, r.geturl())
                    break
            except urllib.error.HTTPError as e:
                result = ("http", e.code, "")
                if e.code in (404, 410) and method == "GET":
                    break
                if e.code in (400, 403, 404, 405, 406, 429, 500, 501, 503):   # many servers answer HEAD badly: try a real GET
                    continue
                break
            except urllib.error.URLError as e:
                reason = e.reason
                if isinstance(reason, socket.gaierror):
                    result = ("dns", 0, str(reason))
                    break
                result = ("error", 0, str(reason)[:120])
            except Exception as e:  # timeouts, bad certificates, dropped connections
                result = ("error", 0, str(e)[:120])
        time.sleep(PAUSE)
        return url, result


def main():
    if not os.path.isdir(SITE):
        sys.exit("Build the site first (python3 build.py), so that _site/ exists.")
    where = collect()
    urls = sorted(where)
    print(f"{len(urls)} different outside addresses on {sum(1 for _ in pages())} pages")
    broken, unsure, done = [], [], 0
    with cf.ThreadPoolExecutor(max_workers=24) as ex:
        for url, (kind, code, note) in ex.map(ask, urls):
            done += 1
            if done % 500 == 0:
                print(f"  {done} checked", flush=True)
            if kind == "ok":
                continue
            if (kind == "http" and code in (404, 410)) or kind == "dns":
                broken.append((url, code or "no such website", where[url]))
            else:
                unsure.append((url, code or note, where[url]))
    http_only = [u for u in urls if u.startswith("http://")]

    def rows(items):
        return "\n".join(f"- {u} ({c}): on {', '.join(p)}" for u, c, p in items)

    report = [f"Weekly check of every link from the site to other websites ({len(urls)} addresses). "
              "Made by tools/check_links.py; this issue is updated each week, and closes itself when nothing is broken.", ""]
    report += [f"## Broken ({len(broken)})", "", rows(broken) or "None.", ""]
    report += [f"## Plain http:// links ({len(http_only)})", "", "\n".join(f"- {u}: on {', '.join(where[u])}" for u in http_only) or "None.", ""]
    report += [f"## Could not check ({len(unsure)})", "",
               "These websites turned the checker away or were slow. They usually open fine in a browser, so they are not counted as broken.", "",
               "<details><summary>Show them</summary>", "", rows(unsure) or "None.", "", "</details>", ""]
    with open(os.path.join(ROOT, "link-report.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(report))
    with open(os.path.join(ROOT, "link-count.txt"), "w") as fh:
        fh.write(str(len(broken)))
    print(f"Broken: {len(broken)}. Plain http: {len(http_only)}. Could not check: {len(unsure)}.")
    for u, c, p in broken:
        print(f"BROKEN {c} {u} (on {', '.join(p)})")


if __name__ == "__main__":
    main()
