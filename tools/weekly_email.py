"""The weekly email, "This week in Welsh history", sent every Monday morning by .github/workflows/weekly-email.yml.

It hands the email to Brevo (brevo.com, free plan: 300 emails a day, no time limit) to send to everyone on the sign-up list.
It only sends when BREVO_API_KEY (a GitHub secret), BREVO_LIST_ID and BREVO_SENDER are set (see SKILLS.md, "The weekly
email"). Without them it prints the email and stops, which is also how to preview it:   python3 tools/weekly_email.py

It reads what build.py wrote (_site/onthisday.json and _site/whatsnew.json), picks the anniversaries of the seven days
ahead and anything added to the site in the last week.
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


def api(path, body, key):
    req = urllib.request.Request("https://api.brevo.com/v3" + path, data=json.dumps(body).encode(), method="POST",
                                 headers={"api-key": key, "Content-Type": "application/json", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        txt = r.read().decode()
        return json.loads(txt) if txt.strip() else {}


def main():
    today = datetime.datetime.now(datetime.timezone.utc).date()
    subject, content = build(today)
    content += ('<p style="margin-top:30px;font-size:12px;color:#777">You are getting this because you signed up at historyofwales.cymru. '
                '<a href="{{ unsubscribe }}">Unsubscribe</a></p>')
    key, lst, sender = (os.environ.get(k, "").strip() for k in ("BREVO_API_KEY", "BREVO_LIST_ID", "BREVO_SENDER"))
    if not (key and lst and sender):
        print(subject, "\n", content)
        print("\nBREVO_API_KEY, BREVO_LIST_ID and BREVO_SENDER are not all set, so nothing was sent.")
        return
    try:
        made = api("/emailCampaigns", {"name": subject, "subject": subject, "sender": {"name": "History of Wales", "email": sender},
                                       "htmlContent": f'<div style="font-family:Georgia,serif;font-size:16px;line-height:1.55;max-width:600px">{content}</div>',
                                       "recipients": {"listIds": [int(lst)]}, "previewText": "The anniversaries of the week ahead, and what is new on History of Wales."}, key)
        api(f"/emailCampaigns/{made['id']}/sendNow", {}, key)
        print("Brevo is sending:", subject)
    except urllib.error.HTTPError as err:
        print("Brevo refused the email:", err.code, err.read().decode()[:500])
        sys.exit(1)


if __name__ == "__main__":
    main()
