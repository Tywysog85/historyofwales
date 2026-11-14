"""The weekly email, "This week in Welsh history", sent every Monday morning by .github/workflows/weekly-email.yml.

It hands the email to Brevo (brevo.com, free plan: 300 emails a day, no time limit) to send to everyone on the sign-up list.
It only sends when BREVO_API_KEY (a GitHub secret), BREVO_LIST_ID and BREVO_SENDER are set (see SKILLS.md, "The weekly
email"). Without them it writes the email to email-preview.html (open it in a browser) and stops:
    python3 build.py && python3 tools/weekly_email.py

It reads what build.py wrote (_site/onthisday.json and _site/whatsnew.json) and picks, for the seven days ahead:
  * a story of the week (the best anniversary that has its own page, else one of the long reads in turn), with its share picture
  * the anniversaries day by day, coloured by their age, as on the site
  * anything added to the site in the last week, with pictures
  * a Welsh word of the week from src/cymraeg.py
The look follows the site: night blue, gold and dragon red, Gloock for headings. The banner at the top is
src/static/email/head.jpg (drawn by tools/email_header.py). Pictures load from the live site, so they are the share
pictures that the deploy makes (cards/<page>.jpg). Email programs ignore most modern CSS, so the layout is tables with
the styles written on each element.
"""
import datetime, html, json, os, sys, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
SITE = os.environ.get("SITE_URL", "https://historyofwales.cymru/")
SITE_DIR = os.path.join(ROOT, "_site")
KIND_ORDER = {"ev": 0, "born": 1, "died": 1, "custom": 2, "feast": 3}
KIND_TAG = {"born": "Born", "died": "Died", "feast": "Feast day", "custom": "Tradition"}
# the colours of the nine ages (src/head.html)
ERA = {"ancient": "#d39a62", "roman": "#e58fb4", "saints": "#b9a0ea", "kings": "#e8c65a", "medieval": "#f26a62",
       "tudor": "#62c6c4", "industrial": "#93a0e0", "modern": "#7cc495", "today": "#f59a4a"}
ERA_NAME = {"ancient": "Ancient Wales", "roman": "Roman Wales", "saints": "Age of the Saints", "kings": "Age of the Kings",
            "medieval": "The Princes", "tudor": "Tudor Wales", "industrial": "Industrial Wales", "modern": "Twentieth-century Wales",
            "today": "Wales today"}
NIGHT, SLATE, SLATE2, LINE, INK, MUTED, GOLD, RED = "#0e1118", "#171c27", "#202736", "#2e3647", "#ece9e1", "#a3aab8", "#e8c65a", "#e2453d"
SERIF = "Gloock,'Iowan Old Style','Palatino Linotype',Georgia,serif"
SANS = "Figtree,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "'JetBrains Mono',Menlo,Consolas,monospace"
e = lambda s: html.escape(str(s), quote=True)
# Outlook's dark mode repaints plain background colours (night blue turned grey); it leaves background pictures alone, so
# every dark panel also carries its colour as a one-colour gradient
bg = lambda c: f"background-color:{c};background-image:linear-gradient({c},{c})"
# the great days of the Welsh year always lead the email when they fall in its week: (title in onthisday.json, page to show)
GREAT_DAYS = {"03-01": ("Saint David’s Day", "person-dewi-sant.html"), "09-16": ("Owain Glyndŵr Day", "person-owain-glyndwr.html"),
              "12-11": ("Death at Cilmeri", "person-llywelyn-ap-gruffudd.html", "Llywelyn, Our Last Prince"), "01-25": ("Saint Dwynwen’s Day", "legend-dwynwen.html")}


def page_of(link):
    """The page a link points at, without its #part, if it is a page of the site that has a share picture."""
    p = (link or "").split("#")[0]
    if not p.endswith(".html") or "/" in p or p in ("index.html", "404.html") or not os.path.exists(os.path.join(SITE_DIR, p)):
        return None
    cards = os.path.join(SITE_DIR, "cards")
    if os.path.isdir(cards) and not os.path.exists(os.path.join(cards, p[:-5] + ".jpg")):
        return None   # a local build with pictures says this one has none
    return p


def card(p):
    return f"{SITE}cards/{p[:-5]}.jpg"


def button(href, text, bg=GOLD, fg=NIGHT):
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="{bg}" style="border-radius:99px">'
            f'<a href="{e(href)}" style="display:inline-block;padding:12px 24px;font:700 15px/1 {SANS};color:{fg};text-decoration:none;border-radius:99px">{text}</a>'
            '</td></tr></table>')


def kicker(text, colour):
    return f'<p style="margin:0 0 8px;font:700 12px/1.4 {SANS};letter-spacing:.12em;text-transform:uppercase;color:{colour}">{text}</p>'


def section(title_en, title_cy):
    return (f'<tr><td style="padding:36px 32px 6px"><table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%"><tr>'
            f'<td style="font:400 26px/1.15 {SERIF};color:{INK}">{title_en}</td></tr>'
            f'<tr><td style="padding-top:4px;font:400 14px/1.4 {SANS};color:{MUTED}">{title_cy}</td></tr>'
            f'<tr><td style="padding-top:12px"><div style="width:44px;height:3px;background:{GOLD};font-size:0;line-height:0">&nbsp;</div></td></tr></table></td></tr>')


def pick_story(week, days):
    """The anniversary whose share picture matches it best (a person for a birth or death, a long read or event page for an
    event), preferring births and events to deaths; else one of the long reads in turn."""
    best = None
    for i, (d, rows) in enumerate(days):
        for r in rows:
            great = GREAT_DAYS.get(r[0])
            p = page_of(great[1]) if great and great[0] == r[3] else page_of(r[7])
            if not p:
                continue
            if great and great[0] == r[3]:
                fit = -1
            elif p.startswith("person-"):
                fit = 0
            elif p.startswith(("story-", "event-")) and r[2] == "ev":
                fit = 1
            elif p.startswith(("legend-", "place-")):
                fit = 2
            else:
                continue
            score = (fit, r[2] == "died", r[1] is None, i)
            if best is None or score < best[0]:
                best = (score, d, r, p)
    if best:
        _, d, r, p = best
        tag = KIND_TAG.get(r[2])
        when = d.strftime("%A %-d %B") + (f" · {tag + ' ' if tag in ('Born', 'Died') else ''}{r[1]}" if r[1] is not None else "")
        great = GREAT_DAYS.get(r[0])
        title = great[2] if great and great[0] == r[3] and len(great) > 2 else r[3]
        return {"page": p, "kicker": f"{ERA_NAME.get(r[8], 'Welsh history')} · {when}", "colour": ERA.get(r[8], GOLD),
                "title": title, "text": r[5]}
    stories = sorted(f for f in os.listdir(SITE_DIR) if f.startswith("story-") and f.endswith(".html") and page_of(f))
    if not stories:
        return None
    p = stories[week % len(stories)]
    src = open(os.path.join(SITE_DIR, p), encoding="utf-8").read()
    grab = lambda name: (src.split(f'<meta property="og:{name}" content="', 1)[1].split('"', 1)[0] if f'og:{name}" content="' in src else "")
    title = html.unescape(grab("title")).split(" | ")[0].split(" · ")[0]
    return {"page": p, "kicker": "A long read for the week", "colour": GOLD, "title": title, "text": html.unescape(grab("description"))}


def word_of_week(week):
    try:
        import cymraeg as C
    except Exception:
        return None
    w = C.WORDS[week % len(C.WORDS)]
    return {"word": w[1], "say": w[2], "means": w[3], "cy": w[4], "en": w[5], "note": w[6], "link": w[8]}


def build(today):
    otd = json.load(open(os.path.join(SITE_DIR, "onthisday.json"), encoding="utf-8"))
    news = json.load(open(os.path.join(SITE_DIR, "whatsnew.json"), encoding="utf-8"))
    week = today.isocalendar()[1]
    days = []
    for k in range(7):
        d = today + datetime.timedelta(days=k)
        rows = sorted((r for r in otd if r[0] == d.strftime("%m-%d")), key=lambda r: (r[1] is None, KIND_ORDER.get(r[2], 1)))
        days.append((d, rows))
    story = pick_story(week, days)
    end = days[-1][0]
    span = f"{today.day}–{end.day} {end.strftime('%B')}" if today.month == end.month else f"{today.day} {today.strftime('%B')} – {end.day} {end.strftime('%B')}"
    subject = f"This week in Welsh history: {span}"
    if story:
        subject += f" · {story['title']}"
    preview = (f"{story['title']}, and the week ahead in Welsh history." if story else "The anniversaries of the week ahead, and what is new on History of Wales.")

    out = []
    # the banner and the dates
    out.append(f'<tr><td style="padding:0"><a href="{SITE}"><img src="{SITE}email/head.jpg" width="600" alt="This week in Welsh history · Yr wythnos hon yn hanes Cymru" '
               f'style="display:block;width:100%;max-width:600px;height:auto;border:0;{bg(NIGHT)};color:{INK};font:400 28px {SERIF}"></a></td></tr>')
    out.append(f'<tr><td style="padding:22px 32px 0"><table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>'
               f'<td style="border:1px solid {LINE};border-radius:99px;padding:7px 14px;font:700 13px/1 {MONO};color:{GOLD};letter-spacing:.04em">{e(span.upper())} {end.year}</td></tr></table>'
               f'<p style="margin:18px 0 0;font:400 17px/1.6 {SANS};color:{INK}"><b style="font-family:{SERIF};font-weight:400;font-size:20px">Bore da!</b> '
               f'Here is the week ahead in Welsh history: the kings, saints, poets and fighters whose days fall this week, and what is new on the site.</p></td></tr>')

    # story of the week
    if story:
        url = SITE + story["page"]
        out.append(section("Story of the week", "Stori’r wythnos"))
        out.append(f'<tr><td style="padding:14px 32px 0"><table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="{SLATE}" style="{bg(SLATE)};border:1px solid {LINE};border-radius:16px;overflow:hidden">'
                   f'<tr><td style="padding:0"><a href="{e(url)}"><img src="{e(card(story["page"]))}" width="536" alt="{e(story["title"])}" style="display:block;width:100%;height:auto;border:0;border-radius:16px 16px 0 0"></a></td></tr>'
                   f'<tr><td style="padding:22px 24px 26px">{kicker(e(story["kicker"]), story["colour"])}'
                   f'<p style="margin:0 0 10px;font:400 28px/1.15 {SERIF};color:{INK}"><a href="{e(url)}" style="color:{INK};text-decoration:none">{e(story["title"])}</a></p>'
                   f'<p style="margin:0 0 20px;font:400 16px/1.6 {SANS};color:{MUTED}">{e(story["text"])}</p>{button(url, "Read the story &rarr;")}</td></tr></table></td></tr>')

    # the week, day by day
    out.append(section("The week ahead", "Yr wythnos i ddod"))
    any_rows = False
    for d, rows in days:
        if not rows:
            continue
        any_rows = True
        colour = ERA.get(rows[0][8], GOLD)
        items = []
        for r in rows[:3]:
            link = SITE + (r[7] or "onthisday.html")
            tag = KIND_TAG.get(r[2])
            meta = " · ".join(x for x in ((str(r[1]) if r[1] is not None else ""), tag or "") if x)
            items.append(f'<p style="margin:0 0 14px;font:400 15px/1.55 {SANS};color:{MUTED}">'
                         + (f'<span style="font:700 12px/1 {MONO};color:{ERA.get(r[8], GOLD)};letter-spacing:.05em">{e(meta.upper())}</span><br>' if meta else "")
                         + f'<a href="{e(link)}" style="font:400 19px/1.35 {SERIF};color:{INK};text-decoration:none">{e(r[3])}</a><br>{e(r[5])}</p>')
        out.append(f'<tr><td style="padding:14px 32px 0"><table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="border-top:1px solid {LINE}"><tr>'
                   f'<td width="64" valign="top" style="padding:16px 0 0;width:64px">'
                   f'<p style="margin:0;font:700 11px/1 {SANS};letter-spacing:.14em;color:{MUTED}">{d.strftime("%a").upper()}</p>'
                   f'<p style="margin:4px 0 0;font:400 38px/1 {SERIF};color:{colour}">{d.day}</p>'
                   f'<p style="margin:4px 0 0;font:700 11px/1 {SANS};letter-spacing:.14em;color:{MUTED}">{d.strftime("%b").upper()}</p></td>'
                   f'<td valign="top" style="padding:16px 0 0 12px">{"".join(items)}</td></tr></table></td></tr>')
    if not any_rows:
        out.append(f'<tr><td style="padding:14px 32px 0;font:400 15px/1.6 {SANS};color:{MUTED}">A quiet week in the calendar. '
                   f'<a href="{SITE}onthisday.html" style="color:{GOLD}">Browse every day of the year</a>.</td></tr>')
    out.append(f'<tr><td style="padding:4px 32px 0"><a href="{SITE}onthisday.html" style="font:700 14px/1 {SANS};color:{GOLD};text-decoration:none">Every day of the year in Welsh history &rarr;</a></td></tr>')

    # new on the site
    week_ago = (today - datetime.timedelta(days=7)).isoformat()
    fresh = [n for n in news if n[0] > week_ago and "/" not in n[5]]
    if fresh:
        out.append(section("New on the site", "Newydd ar y wefan"))
        rows = []
        for i, (d, te, tc, se, sc, link) in enumerate(fresh[:4]):
            url, p = SITE + link, page_of(link)
            if i == 0 and p:
                rows.append(f'<tr><td style="padding:14px 0 6px"><a href="{e(url)}"><img src="{e(card(p))}" width="536" alt="{e(te)}" style="display:block;width:100%;height:auto;border:0;border-radius:12px"></a></td></tr>'
                            f'<tr><td style="padding:8px 0 18px"><p style="margin:0 0 6px;font:400 22px/1.25 {SERIF}"><a href="{e(url)}" style="color:{INK};text-decoration:none">{e(te)}</a></p>'
                            f'<p style="margin:0;font:400 15px/1.55 {SANS};color:{MUTED}">{e(se)}</p></td></tr>')
                continue
            img = (f'<td width="132" valign="top" style="width:132px;padding:0 14px 0 0"><a href="{e(url)}"><img src="{e(card(p))}" width="132" alt="" '
                   f'style="display:block;width:132px;height:auto;border:0;border-radius:8px"></a></td>') if p else ""
            short = se if len(se) < 150 else se[:se.rfind(" ", 0, 145)].rstrip(",;:") + "…"
            rows.append(f'<tr><td style="padding:14px 0;border-top:1px solid {LINE}"><table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%"><tr>{img}'
                        f'<td valign="top"><p style="margin:0 0 4px;font:400 18px/1.3 {SERIF}"><a href="{e(url)}" style="color:{INK};text-decoration:none">{e(te)}</a></p>'
                        f'<p style="margin:0;font:400 14px/1.5 {SANS};color:{MUTED}">{e(short)}</p></td></tr></table></td></tr>')
        more = len(fresh) - 4
        out.append(f'<tr><td style="padding:0 32px"><table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">{"".join(rows)}</table></td></tr>')
        out.append(f'<tr><td style="padding:4px 32px 0"><a href="{SITE}whatsnew.html" style="font:700 14px/1 {SANS};color:{GOLD};text-decoration:none">'
                   + (f"And {more} more new on the site &rarr;" if more > 0 else "Everything new on the site &rarr;") + '</a></td></tr>')

    # Welsh word of the week
    w = word_of_week(week)
    if w:
        out.append(f'<tr><td style="padding:36px 32px 0"><table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="{SLATE2}" style="{bg(SLATE2)};border-radius:16px;border-left:4px solid {RED}">'
                   f'<tr><td style="padding:22px 24px">{kicker("Welsh word of the week · Gair yr wythnos", RED)}'
                   f'<p style="margin:0;font:400 40px/1.1 {SERIF};color:{INK}">{e(w["word"])}</p>'
                   f'<p style="margin:6px 0 14px;font:400 15px/1.4 {SANS};color:{MUTED}">say <b style="color:{INK};font-family:{MONO};font-size:14px">{e(w["say"])}</b> &nbsp;·&nbsp; {e(w["means"])}</p>'
                   f'<p style="margin:0 0 4px;font:400 italic 17px/1.5 {SERIF};color:{INK}">“{e(w["cy"])}”</p>'
                   f'<p style="margin:0 0 14px;font:400 14px/1.5 {SANS};color:{MUTED}">{e(w["en"])}</p>'
                   f'<p style="margin:0 0 16px;font:400 15px/1.6 {SANS};color:{MUTED}">{e(w["note"])}</p>'
                   f'<a href="{SITE}welsh.html" style="font:700 14px/1 {SANS};color:{GOLD};text-decoration:none">Learn a Welsh word every day &rarr;</a></td></tr></table></td></tr>')

    # the weekly quiz: a taste of this week's first question, and last week's top three from the leaderboard
    out.append(quiz_block(today))

    # sign-off and footer
    out.append(f'<tr><td style="padding:44px 32px 0"><p style="margin:0;font:400 44px/1 {SERIF};color:{INK}">Diolch<span style="color:{RED}">.</span></p>'
               f'<p style="margin:10px 0 0;font:400 15px/1.6 {SANS};color:{MUTED}">Thank you for reading. Wales is a small country with a long memory; this is a way in. '
               f'If a friend would enjoy this, send it on: they can sign up at <a href="{SITE}" style="color:{GOLD}">historyofwales.cymru</a>.</p>'
               f'<p style="margin:6px 0 0;font:400 15px/1.6 {SANS};color:{MUTED}">Diolch am ddarllen. Hwyl fawr tan ddydd Llun nesaf.</p></td></tr>')
    out.append(f'<tr><td style="padding:32px 32px 36px"><div style="height:1px;background:{LINE};font-size:0;line-height:0">&nbsp;</div>'
               f'<p style="margin:18px 0 0;font:400 12px/1.6 {SANS};color:#7d8494">History of Wales · Hanes Cymru · <a href="{SITE}" style="color:#7d8494">historyofwales.cymru</a><br>'
               'You are getting this because you signed up on the website. '
               '<a href="{{ unsubscribe }}" style="color:#7d8494">Unsubscribe</a> · <a href="{{ mirror }}" style="color:#7d8494">View in your browser</a></p></td></tr>')

    body = "".join(out)
    doc = f'''<!doctype html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="x-apple-disable-message-reformatting">
<meta name="color-scheme" content="dark light">
<meta name="supported-color-schemes" content="dark light">
<title>{e(subject)}</title>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;700&family=Gloock&display=swap" rel="stylesheet">
<style>
  body {{ margin:0; padding:0; {bg(NIGHT)}; }}
  a {{ color:{GOLD}; }}
  @media (max-width:620px) {{
    .shell td[style*="padding:14px 32px"], .shell td[style*="padding:36px 32px"], .shell td[style*="padding:22px 32px"],
    .shell td[style*="padding:4px 32px"], .shell td[style*="padding:0 32px"], .shell td[style*="padding:44px 32px"],
    .shell td[style*="padding:32px 32px"] {{ padding-left:18px !important; padding-right:18px !important; }}
  }}
</style>
</head>
<body style="margin:0;padding:0;{bg(NIGHT)}">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:{NIGHT}">{e(preview)}&#8199;&#65279;&#847;&#8199;&#65279;&#847;&#8199;&#65279;&#847;&#8199;&#65279;&#847;</div>
<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="{NIGHT}" style="{bg(NIGHT)}"><tr><td align="center" style="padding:16px 8px 24px">
<table role="presentation" class="shell" cellpadding="0" cellspacing="0" border="0" width="600" bgcolor="{NIGHT}" style="width:100%;max-width:600px;{bg(NIGHT)};border:1px solid {LINE};border-radius:18px;overflow:hidden">
{body}
</table></td></tr></table>
</body>
</html>'''
    return subject, preview, doc


def quiz_block(today):
    """This week's quiz (src/quiz_weeks.json), with last week's champions when the leaderboard is up."""
    wk = (today - datetime.timedelta(days=today.weekday())).isoformat()
    try:
        weeks = json.load(open(os.path.join(ROOT, "src", "quiz_weeks.json"), encoding="utf-8"))
    except (OSError, ValueError):
        weeks = {}
    w = weeks.get(wk)
    champs = []
    lb = os.environ.get("LEADERBOARD_URL", "").rstrip("/")
    try:
        if not lb:   # the address the live site uses (deploy.yml finds it)
            with urllib.request.urlopen(SITE + "quiz/index.json", timeout=20) as r:
                lb = (json.loads(r.read().decode()).get("lb") or "").rstrip("/")
        if lb and w:
            with urllib.request.urlopen(urllib.request.Request(f"{lb}/board?week={wk}", headers={"User-Agent": "historyofwales-email"}), timeout=20) as r:
                champs = json.loads(r.read().decode()).get("last") or []
    except Exception as err:   # no leaderboard yet, or it could not be reached: the email goes without it
        print("Leaderboard not read:", err)
    url = SITE + "weekly-quiz.html"
    teaser = ""
    if w:
        q = w["qs"][0]
        line = (q.get("t") or q["h"])[0]
        teaser = (f'<p style="margin:0 0 6px;font:700 12px/1.4 {SANS};letter-spacing:.12em;text-transform:uppercase;color:{GOLD}">Question 1</p>'
                  f'<p style="margin:0 0 18px;font:400 21px/1.3 {SERIF};color:{INK}">{e(q["h"][0])}' + (f'<br><span style="color:{MUTED};font-size:17px">{e(line)}</span>' if q.get("t") else "") + '</p>')
    rows = ""
    for i, (nick, score, secs) in enumerate(champs[:3]):
        rows += (f'<tr><td width="34" style="width:34px;padding:6px 0;font:400 18px/1 {SANS}">{["&#129351;", "&#129352;", "&#129353;"][i]}</td>'
                 f'<td style="padding:6px 0;font:700 16px/1.3 {SANS};color:{INK}">{e(nick)}</td>'
                 f'<td align="right" style="padding:6px 0;font:400 14px/1 {MONO};color:{MUTED}">{score}/10 &middot; {secs // 60}:{secs % 60:02d}</td></tr>')
    champ_html = (f'<p style="margin:22px 0 6px;font:700 12px/1.4 {SANS};letter-spacing:.12em;text-transform:uppercase;color:{MUTED}">Last week’s champions</p>'
                  f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">{rows}</table>') if rows else ""
    num = f" · week {w['n']}" if w else ""
    return (section("The weekly quiz" + num, "Cwis yr wythnos")
            + f'<tr><td style="padding:14px 32px 0"><table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="{SLATE}" style="{bg(SLATE)};border:1px solid {LINE};border-radius:16px">'
              f'<tr><td style="padding:22px 24px 24px"><p style="margin:0 0 16px;font:400 16px/1.6 {SANS};color:{MUTED}">Ten new questions are out, three of them on the anniversaries in this email. One go each, and a leaderboard to climb.</p>'
              f'{teaser}{button(url, "Take this week’s quiz &rarr;", RED, "#ffffff")}{champ_html}'
              f'<p style="margin:20px 0 0;font:400 14px/1.5 {SANS};color:{MUTED}">And every morning, a new <a href="{SITE}daily.html" style="color:{GOLD}">daily challenge</a>.</p></td></tr></table></td></tr>')


def api(path, body, key):
    req = urllib.request.Request("https://api.brevo.com/v3" + path, data=json.dumps(body).encode(), method="POST",
                                 headers={"api-key": key, "Content-Type": "application/json", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        txt = r.read().decode()
        return json.loads(txt) if txt.strip() else {}


def main():
    today = datetime.datetime.now(datetime.timezone.utc).date()
    if len(sys.argv) > 1 and sys.argv[1][:4].isdigit():      # preview another week: python3 tools/weekly_email.py 2026-11-16
        today = datetime.date.fromisoformat(sys.argv[1])
    subject, preview, doc = build(today)
    key, lst, sender = (os.environ.get(k, "").strip() for k in ("BREVO_API_KEY", "BREVO_LIST_ID", "BREVO_SENDER"))
    if not (key and lst and sender):
        out = os.path.join(ROOT, "email-preview.html")
        open(out, "w", encoding="utf-8").write(doc)
        print(subject, f"\n{len(doc) // 1024} KB, written to {out}")
        print("BREVO_API_KEY, BREVO_LIST_ID and BREVO_SENDER are not all set, so nothing was sent.")
        return
    try:
        made = api("/emailCampaigns", {"name": subject, "subject": subject, "sender": {"name": "History of Wales", "email": sender},
                                       "htmlContent": doc, "recipients": {"listIds": [int(lst)]}, "previewText": preview}, key)
        api(f"/emailCampaigns/{made['id']}/sendNow", {}, key)
        print("Brevo is sending:", subject)
    except urllib.error.HTTPError as err:
        print("Brevo refused the email:", err.code, err.read().decode()[:500])
        sys.exit(1)


if __name__ == "__main__":
    main()
