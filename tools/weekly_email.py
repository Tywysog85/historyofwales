"""The weekly email, "This week in Welsh history", sent every Monday morning by .github/workflows/weekly-email.yml.

It reads what build.py wrote (_site/onthisday.json and _site/whatsnew.json), picks the anniversaries of the seven days
ahead and anything added to the site in the last week, and hands the email to Kit (kit.com) to send to everyone signed up.
It only sends when the KIT_API_KEY secret is set in GitHub (see SKILLS.md, "The weekly email"). Without it, it prints the
email and stops, which is also how to preview it:   python3 tools/weekly_email.py
"""
import datetime, html, json, os, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.environ.get("SITE_URL", "https://historyofwales.cymru/")
KIND_ORDER = {"ev": 0, "custom": 2, "feast": 3}


def build(today):
    otd = json.load(open(os.path.join(ROOT, "_site", "onthisday.json"), encoding="utf-8"))
    news = json.load(open(os.path.join(ROOT, "_site", "whatsnew.json"), encoding="utf-8"))
    days = [today + datetime.timedelta(days=k) for k in range(7)]
    parts = [f'<p>Bore da! Here is the week ahead in Welsh history, from <a href="{SITE}">History of Wales</a>.</p>']
    for d in days:
        rows = [r for r in otd if r[0] == d.strftime("%m-%d")]
        rows.sort(key=lambda r: (r[1] is None, KIND_ORDER.get(r[2], 1)))
        if not rows:
            continue
        parts.append(f'<h3 style="margin:22px 0 6px">{d.strftime("%A %-d %B")}</h3>')
        for r in rows[:2]:
            when = f"{r[1]}: " if r[1] is not None else ""
            link = SITE + (r[7] or "onthisday.html")
            parts.append(f'<p style="margin:0 0 10px"><b>{html.escape(when)}<a href="{html.escape(link)}">{html.escape(r[3])}</a>.</b> {html.escape(r[5])}</p>')
    week_ago = (today - datetime.timedelta(days=7)).isoformat()
    fresh = [n for n in news if n[0] > week_ago]
    if fresh:
        parts.append('<h3 style="margin:26px 0 6px">New on the site this week</h3>')
        for d, te, tc, se, sc, link in fresh[:6]:
            parts.append(f'<p style="margin:0 0 10px"><b><a href="{html.escape(SITE + link)}">{html.escape(te)}</a>.</b> {html.escape(se)}</p>')
    parts.append(f'<p style="margin-top:26px">Today’s <a href="{SITE}daily.html">daily challenge</a> is waiting. Diolch am ddarllen.</p>')
    end = days[-1]
    span = f"{today.day}–{end.day} {end.strftime('%B')}" if today.month == end.month else f"{today.day} {today.strftime('%B')} – {end.day} {end.strftime('%B')}"
    return f"This week in Welsh history: {span}", "".join(parts)


def main():
    today = datetime.datetime.now(datetime.timezone.utc).date()
    subject, content = build(today)
    key = os.environ.get("KIT_API_KEY", "").strip()
    if not key:
        print(subject, "\n", content)
        print("\nNo KIT_API_KEY set, so nothing was sent.")
        return
    now = datetime.datetime.now(datetime.timezone.utc)
    body = {"subject": subject, "content": content, "description": subject, "preview_text": "The anniversaries of the week ahead, and what is new on History of Wales.",
            "public": True, "published_at": now.isoformat(), "send_at": (now + datetime.timedelta(minutes=10)).isoformat(),
            "email_address": None, "thumbnail_url": None, "thumbnail_alt": None}
    req = urllib.request.Request("https://api.kit.com/v4/broadcasts", data=json.dumps(body).encode(), method="POST",
                                 headers={"X-Kit-Api-Key": key, "Content-Type": "application/json", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print("Kit accepted the email:", r.status, subject)
    except urllib.error.HTTPError as err:
        print("Kit refused the email:", err.code, err.read().decode()[:500])
        sys.exit(1)


if __name__ == "__main__":
    main()
