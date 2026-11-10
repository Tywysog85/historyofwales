# Skills learnt

This file collects the techniques and lessons from building History of Wales. Add a new entry every time something new is learnt. Each entry says what was done and how, plus any gotcha worth remembering.

---

## Publishing and hosting

### GitHub Pages via GitHub Actions
- Every push to `main` runs `.github/workflows/deploy.yml`. It runs `python3 build.py` and publishes `_site/` to Pages.
- One-time setup: **Settings → Pages → Source → GitHub Actions**.
- You can watch a deploy under the repo's **Actions** tab. If a run fails on GitHub's side for no clear reason, **Re-run jobs** usually fixes it.
- The build step sets environment variables. `SITE_URL=https://historyofwales.cymru/` makes the sitemap and canonical links use the real domain. `GOATCOUNTER=historyofwales` turns stats on.

### Moving to a new repository
- Push the same history to the new repo, then set up Pages there again (Source → GitHub Actions).
- Before deleting the old repo, make sure the new site is live. Deleting is done in **Settings → Danger Zone → Delete this repository**.

### Custom domain (historyofwales.cymru at 123-reg)
- At 123-reg, open **Manage DNS** for the domain and add these records:
  - Four **A** records for `@` pointing at GitHub Pages: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.
  - A **CNAME** for `www` pointing at `tywysog85.github.io`.
- In GitHub, go to **Settings → Pages → Custom domain**, enter `historyofwales.cymru` and save. The repo also keeps a `CNAME` file (`src/static/CNAME`) so the setting survives deploys.
- Once the certificate is issued, tick **Enforce HTTPS**.
- Gotcha: "Token is expired" at 123-reg means the login session timed out. Log in again.
- Gotcha: a GoDaddy "Domain Connect" pop-up can appear. You don't need it; add the records by hand.

### Google Search Console
- Add the site as a property, choose the **HTML file** verification method, and download the file Google gives you.
- Put the file in `src/static/` so it is published at the site root. Then click **Verify**. Keep the file there for good.
- Submit `sitemap.xml` under **Sitemaps**. `build.py` writes it, along with `robots.txt`.

### Visitor statistics (GoatCounter)
- Free and doesn't use cookies, so no cookie banner is needed. Sign up with the code `historyofwales`; the dashboard is https://historyofwales.goatcounter.com.
- The site adds the counting script only when the `GOATCOUNTER` variable is set at build time.

---

## Building the site

### Static site, no framework
- Content lives in Python data files (`src/data.py`, `src/more.py`, `src/ages.py`, `src/long.py`, `src/photos.py`, `src/towns.py`). `build.py` turns them into 100+ HTML pages.
- The home page and the timeline page share one script (`src/app.js`). The script checks which parts exist on the page (the timeline, the hero sky, the map) and skips the rest.

### Bilingual pages (English / Cymraeg)
- On the home and timeline pages, each element carries `data-cy="…"`, and the EN/CY toggle swaps the text. The choice is remembered in the browser.
- The other pages use `bi()` in `build.py`, which writes both languages as `.l-en` and `.l-cy` spans that CSS shows or hides.
- Welsh dates use CC/OC instead of BC/AD.

### Adding a new age (era)
- Define the age in `src/ages.py`, with a story, blurb and teaching notes. `data.py` inserts it in order.
- Events are reassigned to ages by year. People and places are moved in with explicit lists.
- Give each new age a colour token in `src/head.html` (`--e-<id>`) and a `[data-era]` rule.

### Photos from Wikimedia Commons
- Link to the image directly with `https://commons.wikimedia.org/wiki/Special:FilePath/<File name>?width=640`, and credit it with a link to the file page.
- Every photo has a fallback: if it fails to load, the illustration shows instead.
- To find real file names, search the web limited to commons.wikimedia.org.

### Search
- `build.py` writes `search.json`, an index of events, people, places and pages. `src/static/search.js` opens a search box from the magnifier button or the `/` key.

### Offline support
- `src/static/sw.js` caches pages. **Change the cache name** (`history-of-wales-vN`, now v6) whenever the site's look changes a lot, so returning visitors get the new version.

---

## Design and polish

### Hero sky (canvas animation)
- The background is drawn on a `<canvas>`: stars, rolling ridges, a moon, a silhouette of Yr Wyddfa (Eryri) and a red dragon flying towards the summit.
- The dragon is drawn from vector paths (Path2D), and its wings flap by squashing them vertically.
- Phones get their own flight path so the dragon never covers the text.
- Visitors who turn on "reduce motion" see a still picture.

### Stopping things jumping on load (layout shift)
- If an element's styling is added by a script, the element changes size after the page appears and pushes its neighbours. That is why the menu jumped.
- Fix: put the CSS for anything visible at load into the page's main stylesheet, not into a script.

### Word spacing in display fonts
- The Gloock display font has tight word spaces. `word-spacing: .1em` on headings, the logo and the tagline makes phrases like "of Kings" read clearly.

### Letter animations
- The "Cymru" letters animate with a CSS `@keyframes` rule. A negative `translateY` makes them drop down into place; a positive one makes them rise.

### Checking quality
- Take screenshots at computer width (1280px) and phone width (390px) with Playwright before publishing.
- Run axe-core for accessibility. Headings must go in order (h1 → h2 → h3). A visually hidden heading (`.vh`) can fill a gap.
- Run Lighthouse for performance, accessibility, best practice and SEO. The home page scored 92/100/100/100.

## The redesign (November 2026)

### Illustrations drawn in code
- `src/art.py` draws every scene picture (castle, cromlech, dragons, longship, pithead and so on) as SVG: a night sky, a moon, three rolling ridges, then one flat "paper-cut" shape in front. `scene("castle", colour)` returns the picture.
- This suits the site because Claude cannot open Wikimedia photos to check them, but can look at a drawing it made. To add a scene, write a small function that returns SVG shapes and add it to `MOTIF`.
- Gotcha: make a contact sheet of all scenes and look at it before using them. Two scenes had parts in the wrong place on the first try.

### New kinds of content
- `src/features.py` holds the long reads (`STORIES`), legends (`LEGENDS`), symbols and traditions (`SYMBOLS`), quick facts (`FACTS`) and the "which figure are you" quiz. Each item has English and Welsh text side by side.
- In a long read, a paragraph that starts with `## ` becomes a sub-heading.
- `build.py` makes a page for each one and adds them to the search index and the sitemap.

### One menu and footer for every page
- `nav()` and `footer()` in `build.py` now make the menu and footer for all pages, including the home page (the home page template just says `__NAV__` and `__FOOTER__`).
- The full-screen menu, the scroll progress bar, the back-to-top button and the fade-in-on-scroll effect live in `src/static/site.js`, which every page loads.

### Fade-in on scroll, safely
- Elements with the class `rv` start invisible and fade in when they scroll into view (IntersectionObserver).
- Safety net: the hiding only applies once a tiny script in the page head has added the class `js`, and if `site.js` has not started after 2.5 seconds everything is shown anyway. Content must never depend on a script loading.
- Gotcha when testing: the site uses smooth scrolling, so a test script must scroll with `behavior: "instant"`, or the page never really moves and nothing fades in.

### Page-to-page transitions
- One line of CSS, `@view-transition { navigation: auto }`, makes modern browsers cross-fade between pages. Older browsers ignore it.

### Hover accordion (the ages)
- The six age posters sit in a flex row. The hovered one gets a bigger `flex-grow`, which animates. On phones the same cards become a sideways swipe row with scroll-snap.
- Gotcha: text inside a card that should wrap must not sit in a CSS grid with a wide sibling, or the grid stretches and the title is cut off. A flex column fixed it.

### Games and "Your journey"
- `src/static/play.js` runs the daily challenge, the map game, Welsh names, the "which figure" quiz and word pairs. Each game page gets its data from `build.py` as a `PLAY` object.
- The daily challenge picks its event from the date, so everyone gets the same one each day. Results, streaks and badges are saved in the visitor's own browser (localStorage, key `hc-journey`). Nothing is sent anywhere, so no cookie banner is needed.
- The map game turns a tap into latitude and longitude by reversing the map projection, then measures the distance in kilometres.
- Pages mark themselves with `data-track="person:slug"` (or era, place, story, legend) and `site.js` ticks them off for the journey page.

### Checking a big change
- Load every built page in a headless browser at phone width and report script errors and sideways scrolling. This caught a game card that was wider than the phone screen.
- Make contact sheets (several screenshots tiled into one image) to review many pages quickly, in English and Welsh.

---

### The changing map and adding places (November 2026)

The Kingdoms view colours the council areas in `src/geo/la.json`. Each moment in time lives in `src/kingdoms.py` as a list of groups: name in English and Welsh, a colour, and the areas it covers. To add a moment, copy one and change the groups; the slider, the Play button and the labels pick it up by themselves. Labels are placed at the middle of each group's area by `renderKg()` in `src/app.js`.

Two modern areas are too big for the old kingdoms, so `_split_la()` in `build.py` cuts Powys into Montgomeryshire, Radnorshire and Brecknockshire, and Gwynedd into Caernarfonshire and Meirionnydd, along lines of latitude and longitude. Move those lines there if a border looks wrong.

A trap worth remembering: `element.hidden = false` does nothing on SVG shapes. Use `toggleAttribute("hidden", ...)`. This is why the Kingdoms map once showed no colours at all.

New historic sites go in `src/places2.py` (`_p(id, English, Welsh, age, latitude, longitude, year, picture, source, text EN, text CY)`). A place without a photo is fine; it gets its drawn picture.

### The proud voice, and adding a long read (November 2026)

The owner's rules for how the site speaks are written at the top of `src/pride.py`: proud of Wales and its people, nothing that runs down the figures of Welsh history, Arthur is a king (never "myth" or "legend"), and contested points are given in the tradition's own words ("Welsh tradition holds", "Owain wrote") so the page stays both proud and true.

To add a long read, add a `dict` to `STORIES` in `src/pride2.py` (id, age, picture, minutes, titles, summary, paragraphs in English and Welsh; a paragraph starting `## ` is a sub-heading). The page, the card, search and the journey pick it up.

To reword an existing line without hunting for it, add an `(old, new)` pair to `REWORD` in `src/pride.py`. It is applied to every event and person at build time. After building, check the new wording appears, because a pair that does not match is silently skipped.

When a page is removed (the Arthur legend became a long read), leave a redirect page at the old address in `build.py` so old links still work.

### The four notes in the top folder (November 2026)

`README.md` says what the site is and where things live. `EDITORIAL.md` holds the owner's rules for how it is written. `TODO.md` lists the open jobs. `SKILLS.md` is this file. The owner wants them kept clean and tidy: when something changes, edit the line that is there instead of adding a new one at the bottom, delete finished jobs from `TODO.md`, and keep the counts in `README.md` true.

## Working together

- Ifan sends a screenshot plus a short note, and each change is made, checked and published within minutes.
- Small visual tweaks are published one at a time so each can be seen live.
- Still open: a fluent Welsh speaker to proofread the Welsh, a check of the photos, and optional real voice recordings for the Welsh words (MP3s go in `src/static/audio/` as `slug.mp3`).

### Adding or splitting an age (November 2026)

The ages are layered: `src/data.py` holds the original four, `src/ages.py` adds Saints and Kings, and `src/ages9.py` adds Roman Wales, Tudor and Stuart Wales and Wales Today. Each layer is applied at the bottom of `data.py`.

To add an age:
1. Write its `dict` (id, names, span, blurb, two story paragraphs, in English and Welsh) in `src/ages9.py`, and add teacher notes to `TEACH` there.
2. Put it in the `ERAS = [...]` line at the bottom of `data.py`, and extend `age()` so events move into it by year. Move people and places with the `*_PEOPLE` sets and `PLACE_ERA`.
3. Give it a colour in `COL` and a picture in `ERA_ART` (`build.py`), the same colour as `--e-<id>` plus a `[data-era="<id>"]` rule in `src/head.html`, and a name in `ERA_NAMES` in `src/static/play.js`.
4. Update the words that count the ages: the heading in `src/body.html`, the footer column in `build.py` and the "ages" badge in `src/static/site.js`.

With nine posters in a row, a closed poster is too narrow for its title, so closed posters print the title up the side (`writing-mode: vertical-rl` with `text-orientation: sideways`, so apostrophes turn with the letters) and the open one prints it normally.

### A sky that follows the real time of day (November 2026)

The home page sky is drawn in `src/app.js`. `sunOverWales()` works out how high the sun is over mid Wales from the clock alone (no location permission, no network), and `setSky()` blends between four palettes in `SKIES` (night, dawn, day, dusk) once a minute. Every colour in the scene reads from `SKY`, so a new palette is one line. To preview one, add `?sky=night`, `?sky=dawn`, `?sky=day` or `?sky=dusk` to the home page address.

Keep the day palette dark enough for the light text to stay readable: the words sit on the sky, so "day" is a deep blue, not a pale one.

On wide screens (1100 pixels and up) the opening screen is capped at 60rem tall in `src/v6.css` so no empty band opens above the numbers, the mountain is sized to fit inside the right edge (`ew`, `ex0` in `draw()`), a Milky Way of faint stars (`milky`) fills the left of the night sky, and `drawCastle()` puts a castle on a crag at the right: a great keep, round towers, a twin-towered gatehouse with firelight in the gate, lit windows that flicker, and Y Ddraig Goch flying from the top. The castle is drawn in its own units (1 unit = `s`), so to change it edit the `tower(x, width, height, merlons)` and `slit(x, y, height, n)` calls. The dragon is drawn by one function, `ddraig()`: the standing dragon of the national flag (passant, facing left, in a 300 by 180 box). `flagArt()` paints the flat flag once on a hidden canvas, and `drawCastle()` draws it in 48 thin slices, each lifted and shaded by a wave, so it billows like cloth. `drawDragon()` uses the same `ddraig()` mirrored for the dragon in the sky, so changing the dragon changes both. Phones and tablets do not get the castle or the Milky Way.

Other effects in the same file: shooting stars (`drawMeteors`, night only), the dragon's fire (`fireAt`, every 9 to 16 seconds or when tapped; `DPOS` is where the dragon is for the tap test), and tilt (the `deviceorientation` listener feeds the same `mouse` value the pointer does; skipped on iOS, which asks permission). The glint on "Cymru" is CSS in `src/v6.css` (`@keyframes glint`), using a gradient clipped to the text; the letters need extra `padding-block` or their tails are cut off.

## The site name above "Cymru" (home page)

On the home page the words "History of Wales" (Welsh: "Hanes Cymru") sit above the big "Cymru", not in the top bar. `HERO_NAME` in `build.py` writes them one letter per box (`_letters()`), and the same CSS rule as "Cymru" (`.hero h1 span, .hero .hero-name b` in `src/head.html` and `src/v6.css`) makes every letter drop in and glint. The home top bar has no name or mountain; it starts with the links, and on screens wider than 1480 pixels it shows four more (`NAV_HOME_MORE` in `build.py`). Every other page keeps "History of Wales" in the top bar as the way home.
