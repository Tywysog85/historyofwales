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

### Showing up in Google and Bing (November 2026)
- `src/seo.py` does it for every page, so new pages need nothing extra. `page()` in `build.py` calls it.
- Titles are cut to about 65 characters and descriptions to 160, at a word. Long titles drop the " · History of Wales" ending first.
- Hub pages get titles in the words people search for, such as "Welsh history timeline" and "Welsh legends, myths and folk tales". They are set in `TITLES` in `seo.py`. The page itself does not change.
- Each page carries structured data (JSON-LD). It holds the page's own type (Person, TouristAttraction, Article), the site's name "History of Wales" / "Hanes Cymru", and a breadcrumb trail read from the crumbs at the top of the page. Test a page at https://search.google.com/test/rich-results.
- `sitemap.xml` gives each page the date it last really changed, and lists its pictures. The build compares each page with the fingerprints in the live `seo-lastmod.json`, so unchanged pages keep their old date. Set `SEO_OFFLINE=1` to skip that look-up.
- Builds must give the same page every time, or every page looks changed. Don't use Python's `hash()` for ids, because it changes on every run. Use `zlib.crc32` instead.
- After each deploy, `tools/indexnow.py` sends the pages that changed today to IndexNow, which Bing, Yandex and others share. The key file `<key>.txt` sits at the site root. Send a plain User-Agent: IndexNow answered 403 to Python's default one. The deploy log shows "Sent N changed pages ... HTTP 200" when it works.
- Bing Webmaster Tools: sign in at https://www.bing.com/webmasters with a Microsoft account and choose **Import from Google Search Console**. That brings the site and sitemap across with no new file.

### Visitor statistics (GoatCounter)
- Free and doesn't use cookies, so no cookie banner is needed. Sign up with the code `historyofwales`; the dashboard is https://historyofwales.goatcounter.com.
- The site adds the counting script only when the `GOATCOUNTER` variable is set at build time.

---

## Building the site

### Static site, no framework
- Content lives in Python data files in `src/` (the table in `README.md` says which file holds what). `build.py` turns them into about 200 HTML pages.
- The home page and the timeline page share one script (`src/app.js`). The script checks which parts exist on the page (the timeline, the hero sky, the map) and skips the rest.

### Bilingual pages (English / Cymraeg)
- On the home and timeline pages, each element carries `data-cy="…"`, and the EN/CY toggle swaps the text. The choice is remembered in the browser.
- The other pages use `bi()` in `build.py`, which writes both languages as `.l-en` and `.l-cy` spans that CSS shows or hides.
- Welsh dates use CC/OC instead of BC/AD.

### Photos from Wikimedia Commons
- Link to the image directly with `https://commons.wikimedia.org/wiki/Special:FilePath/<File name>?width=640`, and credit it with a link to the file page.
- Every photo has a fallback: if it fails to load, the illustration shows instead.
- To find real file names, search the web limited to commons.wikimedia.org.

### Gallery pictures from Wikimedia Commons (November 2026)
- Wikimedia Commons is blocked from Claude's cloud computer, so the picture research ran on Ifan's Mini-PC through Remote Control, in a work folder inside `D:\Website\historyofwales.cymru\_work\` (deleted when finished).
- How the PC found them: match each subject to its Wikipedia/Wikidata entry (lead image, Wikidata image, Commons category), gather candidates with the Commons API, keep only Public domain, CC0, CC BY and CC BY-SA (never NC or ND), look at every thumbnail, then download a 1400 px copy and record the author and licence.
- `python tools/gallery_import.py <research folder>` turns that into web pictures: `src/static/gallery/<id>.webp` (fits 1280 x 1000, for the big-picture viewer) and `<id>-s.webp` (fits 600 x 800, for the grid), plus the credits in `src/gallery_photos.py`. Fitting in a box, not just a width, keeps tall portraits small: 260 pictures came to 48 MB.
- The research record is `tools/gallery_research.json` (with a confidence and note for each pick) and `tools/gallery_research_notes.txt`. Welsh captions are in `tools/gallery_cy.json`; pictures left out are listed in `tools/gallery_skip.json`.
- Categories, titles and links for pictures without a page of their own are in `src/gallery.py`. To add a picture, add its subject there, put its credit line in `src/gallery_photos.py` and its two WebP files in `src/static/gallery/`.
- Each picture's credit (photographer, licence with link, Commons file page) shows in the viewer, under the photo on its place or person page, and in the full list at the bottom of the gallery.
- Getting files from Ifan's PC into the repo: the PC's Git is not signed in for Claude, so Ifan commits and pushes with GitHub Desktop (File, Add local repository, pick the folder, type a summary, Commit, Push origin).

### Shared files keep pages small (November 2026)
- Every page used to carry the same 100 KB of CSS inside it, and the home page, timeline and quiz each carried the same 430 KB of data and script. `shared_assets()` in `build.py` now moves them into `site.css`, `data.js` and `app.js` after the pages are built, so a browser downloads them once and keeps them. Pages became 60 to 70% smaller.
- Each link ends in `?v=` and a fingerprint of the file, made from its contents, so a changed file always gets a new address and nobody keeps an old copy. Nothing to raise by hand.
- `data.js` and `app.js` load with `defer`, so the opening screen paints before the home page's big script runs. After changing the opening, still run `node tools/hero_jump_check.js` (one land position).
- Sections far down the home page use `content-visibility: auto` (end of `src/v6.css`), so the browser only lays them out as they come near.
- Keep writing CSS in the same places (`src/head.html`, `src/*.css`, the `*_CSS` strings in `build.py`). The move happens by itself.
- To check a change like this did not alter the look, screenshot each page before and after with reduced motion and compare the pictures pixel by pixel (Pillow `ImageChops.difference`).

### A shorter front page on phones (November 2026)
- On phones (700px wide or less) the home page shows 4 long reads, 4 legends, 4 games and 6 people instead of 12, and hides "Words to know". Each section keeps its "All …" button, so nothing is lost. This took the phone home page from about 28,000 to 19,000 pixels tall.
- The rules are at the end of `src/v6.css` ("Phones: a shorter front page"); the 6-or-12 people choice is in `renderPeople()` in `src/app.js`. The era and field filters for people scroll sideways on phones instead of wrapping onto many lines.
- To measure, open the home page in Playwright as a Pixel 7, turn off `content-visibility` with an added style, and print each section's height.

### Collectable cards and sets (November 2026)
- Every person, place and legend page is a card; reading the page collects it. The sets are in `src/sets.py` (29 sets, 220 cards): add a set by adding a line there. `build.py` stops with an error if a card in a set does not exist.
- The cards are drawn by `card_html()` and `set_html()` in `build.py`: on the journey page ("Your cards", `journey.html#cards`) and in a "Collect the set" box on each page that belongs to a set. The card picture is the page's photo, the gallery picture, the legend picture, or the person's initials.
- `paintSets()` in `src/static/site.js` marks the collected cards from the journey on the reader's device, shows "New card" and "Set complete" messages, and remembers finished sets in `j.s`. Two badges go with them: Collector (one set) and Keeper of treasures (five sets).
- To test, put keys such as `person:owain-gwynedd` into `localStorage["hc-journey"].v` in Playwright, then open a page in that set.

### Read further links: Dictionary of Welsh Biography, Coflein, Welsh Wikipedia (November 2026)
- `tools/fetch_sources.py` asks English Wikipedia for each person's and place's Wikidata item (following redirects), then asks Wikidata for the Dictionary of Welsh Biography id, the Coflein id and the Welsh Wikipedia article. It writes `src/source_links.json`.
- It runs on GitHub (`.github/workflows/fetch-sources.yml`), because Wikimedia is blocked from Claude's cloud computer. It runs when the script changes on a claude/ branch, on the 1st of each month, or from the Actions tab.
- `further()` in `build.py` draws the "Read further" buttons. In Welsh the Dictionary link goes to bywgraffiadur.cymru and the Wikipedia link to cy.wikipedia.org.

### Today's picture to share (November 2026)
- `today.html` shows a square 1080 x 1080 picture for today's best On this day entry, in English and in Cymraeg (`_site/cards/today-en.jpg` and `today-cy.jpg`), with ready-to-paste words and hashtags.
- `today_pick()` in `build.py` chooses the entry: events first, then entries that have a page, then entries whose page has a photo. The date is the date in Wales (Europe/London). `make_square()` in `tools/cards.py` draws the picture.
- The daily 04:15 UTC rebuild remakes it, so it changes every morning. It needs Pillow, like the share pictures.

### Real Welsh voices from Lingua Libre (November 2026)
- `tools/fetch_audio.py` runs on GitHub (`.github/workflows/fetch-audio.yml`). It collects every Welsh word and phrase the site can play, finds Lingua Libre recordings of exactly that text on Commons, and saves trimmed MP3s in `src/static/audio/`. Speakers who recorded the most of our words are preferred, so voices stay consistent.
- Credits go in `src/audio_credits.json` and show on `welsh.html`, grouped by speaker. MP3s not listed there are your own recordings and are never replaced.
- Wikimedia answers "429 too many requests" if downloads go too fast, so the script waits between files and tries again.
- Every workflow that commits back now runs `git pull --rebase` before `git push`, so it cannot collide with other work pushed at the same time.

### A fuller timeline (November 2026)
- New events go in `src/events2.py`, in the same shape as `EVENTS` in `data.py`, with the age written out (ancient, roman, saints, kings, medieval, tudor, industrial, modern, today). `data.py` adds them at the very end and stops if a place id does not exist.
- Give a day ("MM-DD") only when it is certain: dated events also feed On this day and Today's picture.
- For recent events, check the facts with a web search first (Wikipedia and most news sites are blocked from Claude's cloud computer, but search results still show headlines), and keep claims made by supporters worded as their claims.
- Years under 10,000 are shown without a comma (2026, not 2,026): `fmt()` in `src/app.js`.

### Wales in 10 minutes (November 2026)
- `wales-in-10.html`: the whole story in short steps beside a map that stays in view (on the right on computers, at the top on phones). The words are in `src/story10.py` (`STEPS`), the places marked at each step in `PINS` (place ids from `data.py`).
- Each step names a map stage: an id from `KINGDOMS` in `src/kingdoms.py`, or `land` (all Wales in one colour) or `first` (the oldest places). `build.py` stops if a stage or place id does not exist.
- `src/wales10.js` recolours the council-area blocks as each step reaches the middle of the screen (an IntersectionObserver), names each realm at the middle of its land, and drops the pins in. Styles are in `src/wales10.css`; movement is switched off for people who ask for reduced motion.
- Keep each step to about 120 words, and keep it proud (EDITORIAL.md).
- The map's look: `_soften()` in `build.py` turns the long straight shire cuts into gently wandering lines (the same nudge on both sides of a border, so no gaps). Each block's outline is drawn in its own fill colour so the modern council lines vanish and only the realms show. Under the blocks sit a soft sea glow and a cream coastline; over them a faint paper grain (an SVG noise filter). The sea has its own gradient, ripples, sea names and a compass. The colours are made deeper for this map by `PAL` in `src/wales10.js`.
- The old shires inside Powys and Gwynedd follow the real borders (the Wye and Elan between Radnorshire and Brecknockshire, the Kerry Hills above Radnorshire, the Glaslyn estuary and the Moelwyn between Caernarfonshire and Meirionnydd). `tools/split_shires.py` cuts them once with shapely (`pip install shapely`) and saves `src/geo/shires.json`, which `build.py` reads, so the website build itself needs nothing extra. Both the home page Kingdoms map and this page use them.
- Realm names are nudged apart in `src/wales10.js` (`spread`) when two would touch, separately for English and Welsh.

### The page for addresses that do not exist (November 2026)
- `not_found_page()` in `build.py` writes `404.html`. GitHub Pages shows it for any address that does not exist. It has `<base href="/">` so its links work from any depth, and `noindex` so Google leaves it out. It is left out of the sitemap.

### Install invitation and the journey hint (November 2026)
- The end of `src/static/site.js` counts the days someone visits (`hc-days` in local storage). On the third day it invites them to put the site on their home screen: Android and desktop Chrome get the browser's own install box (the `beforeinstallprompt` event), iPhones get the two steps (Share, then Add to Home Screen). "Not now" is remembered (`hc-install-no`). Preview it with `?install=1` on any address.
- The journey circle in the menu bar explains itself once, on the second page someone reads (`hc-hint`). Preview with `?hint=1`.
- The journey circle's screen-reader name says how many pages have been read, and the menu button has a name even on phones where the word "Menu" is hidden.

### What's new, the news feed and the weekly email (November 2026)
- **Whenever something visitors would care about goes live, add a line at the top of `NEWS` in `src/whatsnew.py`** (date, English and Welsh title, one sentence each, link). It feeds `whatsnew.html`, the "New on the site" strip on the home page (first three lines) and the news feed `feed.xml`.
- Returning visitors see "New" labels on lines added since their last look, and a red dot on the menu button until they open What's new (`hc-news-seen` in local storage, the newest date is on the menu button as `data-news`). First-time visitors see nothing marked new.
- `feed.xml` is an Atom feed of the news plus today's anniversaries from On this day. `deploy.yml` now also rebuilds the site every morning at 04:15 UTC (`schedule`) so the feed carries each day's anniversaries.
- **The weekly email** uses Brevo (brevo.com). Its free plan has no time limit and no card: up to 300 emails a day, with a small Brevo logo at the foot of each email. (Kit and MailerLite were ruled out: Kit's sign-up pushes a paid trial, and MailerLite's free plan cannot send our own email design through its API.) Four settings switch it on:
  1. `EMAIL_FORM`: the link to the Brevo sign-up form (Brevo → Contacts → Forms → the form → Share → copy link). Repository variable in GitHub (Settings → Secrets and variables → Actions → Variables → New repository variable). The site then shows a "Sign up for the weekly email" button on the home page, What's new and the foot of every page. Until then those places show "What's new" and "News feed".
  2. `BREVO_LIST_ID`: the number of the Brevo list the form adds people to (Brevo → Contacts → Lists, the ID column). Repository variable.
  3. `BREVO_SENDER`: the email address the weekly email comes from. It must be added and confirmed in Brevo first (Settings → Senders, domains and dedicated IPs → Senders → Add a sender). Repository variable.
  4. `BREVO_API_KEY`: a Brevo API key (Brevo → your name, top right → SMTP & API → API keys → Generate a new API key). Stored as a GitHub **secret** (same page, Secrets tab, New repository secret). Never paste it anywhere else.
- When more than about 300 people have signed up, the free plan's 300 a day is no longer enough for one send, and the email needs Brevo's cheapest paid plan or a split send.
- `.github/workflows/weekly-email.yml` runs every Monday at 07:00 UTC: it builds the site, and `tools/weekly_email.py` writes "This week in Welsh history" (the anniversaries of the next seven days and anything added in the last week) and asks Brevo to send it (it makes a campaign for the list and sends it at once). Run `python3 tools/weekly_email.py` after a build to preview the email. It can also be started by hand from the Actions tab (Run workflow).

### Share pictures and the Share button (November 2026)
- Every page made by `page()` in `build.py` gets its own share picture, the 1200 x 630 card that WhatsApp, Facebook and X show: `_site/cards/<page>.jpg`, drawn by `tools/cards.py` with Pillow (the page's kind and age in the age's colour, its title in Gloock, its description, the site's address, and its photo on the right, or the red dragon where there is no photo). Fonts are in `tools/fonts/` (SIL Open Font Licence).
- They are made during the build, so nothing is stored in the repo. The GitHub build installs Pillow first (`deploy.yml`). Without Pillow, or with `CARDS=0`, the build skips them and pages use `og.png`. Making all 490 takes about 20 seconds.
- To see how a page will look when shared, open `_site/cards/<page>.jpg` after a build. Facebook keeps old pictures for a while: paste the address into the Facebook Sharing Debugger and press "Scrape again" to refresh one.
- The Share button sits under each page's title (`SHARE_BTN` in `build.py`). Phones open their own share sheet (`navigator.share`); computers get WhatsApp, Facebook, X, email and "Copy the link" (end of `src/static/site.js`).

### Photos kept on the site (November 2026)
- `tools/fetch_photos.py` finds every photo the built pages still load from Wikimedia Commons, downloads each one once and saves `src/static/photos/<id>.webp` (fits 1280 x 1000) and `<id>-s.webp` (fits 600 x 800). `src/photo_files.json` says which Commons file each is. `photo_url()` in `build.py` then uses the local copy; the credit links still go to the Commons file page.
- Wikimedia is blocked from Claude's cloud computer, so it runs on GitHub: `.github/workflows/fetch-photos.yml`. It runs by itself when the script changes on a `claude/` branch, or start it from the Actions tab (Fetch photos from Wikimedia Commons → Run workflow, pick the branch). It commits the pictures to that branch. Run it again whenever new Commons photos are added, so they too are kept on the site.

### Search
- `build.py` writes `search.json`, an index of events, people, places and pages. `src/static/search.js` opens a search box from the magnifier button or the `/` key.
- Every king and prince is in it: each ruler on a kingdom page has an anchor (`kings-gwynedd.html#k-cadfan-ap-iago`, made by `ruler_anchor()`), and the line lights up when opened from search. All 827 castle sites are in it too, not only those with a story.
- Old spellings and English names find the Welsh ones through `ALIAS` in `search.js` (Llewellyn → Llywelyn, Caernarvon → Caernarfon). Add a line there when someone searches for a spelling that finds nothing.
- When a word finds nothing as typed, search undoes Welsh mutations (`MUT`: Nghymru → Cymru, Fangor → Bangor), then tries the nearest word in the index (one letter out for short words, two for long), and says "Showing results for …".

### The reference pages: Look it up, the A–Z and quick answers (November 2026)
- `reference.html` (Look it up), `a-z.html` and `questions.html` are built by `src/refpages.py`, which `build.py` loads with `RP.setup(globals())` so it can use `bi()`, `page()`, `hero()` and the rest. Keeping the new pages in their own file means other work on `build.py` rarely clashes with them.
- The words are in `src/ref_az.py` (`A(id, English, Welsh, text, text, see)`) and the questions in `src/ref_faq.py` (`Q(...)` in sections). `see` lists pages to read more; a link to a page the site does not have is left out and named at the end of the build, so entries can point at pages that are still to come.
- `questions.html` carries FAQPage data and `a-z.html` DefinedTermSet data, so search engines can show the answers directly.
- Each entry is in search as its own result (kinds `term` and `question`), and the filter box on each page hides what does not match as you type.
- `towns.html` comes from `src/ref_towns.py`: towns by council area, `T(English, Welsh, meaning, meaning, history, history, see, geo)`, and `ELEMENTS`, the words of place names (list a mutated form such as `fach` or `bont` as its own word). The decoder on the page splits any typed name into the longest known words from the left, so add a word to `ELEMENTS` when a common name comes out in unknown pieces.
- Town positions come from the free GeoNames list inside the Python package `geonamescache` (from PyPI): run `python3 tools/towns_geo.py` after adding towns; it writes `src/towns_geo.json` and names any it cannot find, which then need a `geo=(lat, lon)` by hand.
- `battles.html` comes from `src/ref_battles.py` (`B(...)`, with `win` set to `w` for a Welsh victory, `l` for a Welsh stand, `o` for a battle or rising); a battle with `geo=None` is listed but left off the map and marked so.
- Every battle also says who it was against: the `VS` dict at the bottom of `src/ref_battles.py` gives each battle id one or more keys from `AGAINST` (rome, saxons, vikings, irish, welsh, normans, english, roses, civil, france, risings, abroad). The build stops if a battle has none, and the page turns them into filter buttons with counts.
- `documents.html` comes from `src/ref_docs.py`. Each document's `words` is a kind and two texts: `quote` (exact words from a named published translation), `welsh` (the Welsh original, with an English version) or `short` (what it says, in our own words). Use `short` whenever the exact wording is not certain: never put words in quotation marks that a document does not contain.
- The topic guides (`topics.html`, `topic-<id>.html`) come from `src/ref_topics.py`. Each topic has a short intro in our words and lists of ids (people, A–Z terms, quick answers, documents, battles, places) that are gathered from the rest of the site. Timeline events are picked by a pattern (`ev`), with `xev` to leave out titles that match by accident; when more than 24 match, the page spreads its picks evenly through time. After adding a topic, look at its Key moments list for strays.
- `maps.html` draws every stage of the home page's kingdoms map (`src/kingdoms.py`) plus 1974 and 1996 (`src/ref_maps.py`) as plain SVG with no script. The council-area outlines are written once in a hidden `<defs>` and each map reuses them with `<use href="#mla-N" fill=...>`, so fifteen maps cost little more than one. Names on the maps are `<tspan class="l-en">`/`l-cy` so the language switch works inside SVG too.
- A link to one entry on a reference page (`a-z.html#az-...`, `documents.html#doc-...`, `battles.html#b-...`) is shown with that entry's own name, not the page's.
- `sites.html`, the historic sites map, shows Cadw's scheduled monuments. The Welsh Government's map server (DataMapWales, a GeoServer) can't be reached from the cloud, so `.github/workflows/fetch-sites.yml` runs `tools/sites_fetch.py` on GitHub and commits `tools/data/sites_cadw.json` (layer `inspire-wg:Cadw_SAM`, about 4,200 monuments with English and Welsh type and period) and `sites_guardian.json` (`geonode:cadw_guardianshipmonuments`, the 130 sites Cadw opens to visitors). It runs again on the 2nd of each month. `tools/data/sites_probe.txt` records what the server offered, so field names can be checked without access to the server.
- Gotcha: pick a server layer by its exact name. A loose match on "SAM" picked up a marine "GRABSAMPLES" layer with 96,000 features. The script now refuses any layer that isn't 100 to 20,000 features, and never fails the run, because a failed run emails Ifan.
- `src/ref_sites.py` sorts Cadw's 250 site types into eleven kinds a visitor would recognise. The map reuses `src/static/castles.js`, which reads `window.CMAP` (or `window.CASTLES`). Its wording, record link, hash prefix and group order can be overridden by keys in the payload (`t`, `rec`, `hp`, `order`, `hi0`), so one script serves both maps.

### Offline support
- `src/static/sw.js` caches pages. **Change the cache name** (`history-of-wales-vN`, now v6) whenever the site's look changes a lot, so returning visitors get the new version.

---

## Design and polish

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
- The age posters sit in a flex row. The hovered one gets a bigger `flex-grow`, which animates. On phones the same cards become a sideways swipe row with scroll-snap.
- Gotcha: text inside a card that should wrap must not sit in a CSS grid with a wide sibling, or the grid stretches and the title is cut off. A flex column fixed it.

### Games and "Your journey"
- `src/static/play.js` runs the daily challenge, the map game, Welsh names, the "which figure" quiz and word pairs. Each game page gets its data from `build.py` as a `PLAY` object.
- The daily challenge picks its event from the date, so everyone gets the same one each day. Results, streaks and badges are saved in the visitor's own browser (localStorage, key `hc-journey`). Nothing is sent anywhere, so no cookie banner is needed.
- The map game turns a tap into latitude and longitude by reversing the map projection, then measures the distance in kilometres.
- Pages mark themselves with `data-track="person:slug"` (or era, place, story, legend) and `site.js` ticks them off for the journey page.

### Checking a big change
- Load every built page in a headless browser at phone width and report script errors and sideways scrolling. This caught a game card that was wider than the phone screen.
- Make contact sheets (several screenshots tiled into one image) to review many pages quickly, in English and Welsh.

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

### Pull quotes, fact tables and "read the full story" links (November 2026)

Learnt while building the Hywel Dda page (`src/hywel.py`). Long-read paragraphs now understand two more codes:

- `> The quote | Where it comes from` makes a large pull quote with its source underneath.
- `|| Left | Right` makes one row of a two-column table. Rows next to each other join into one table (used for "at a glance" facts and the value of a cat).

A long read can also say who and what it is about, with `people=[...]`, `places=[...]` and `events=[...]` (event titles in English). `build.py` then adds a "The full story" card to those person and place pages, and a "Read the long read" link to those events on the age pages and on the timeline (the timeline gets them through `SL` in the page data). One list in the story does all the linking.


### A long read in its own file, a new picture, and a sweep for banned words (November 2026)

Learnt while building the Iolo Morganwg long read (`src/iolo.py`, `story-iolo.html`).

- **Own file for a big long read.** Put the `STORY` dict in its own file (like `src/hywel.py` and `src/iolo.py`) and add it to the end of `STORIES` in `src/features.py`. The same file can hold a person's longer text and a new place: the place tuple is added to `MORE_PLACES` at the bottom of `src/places2.py`, and its longer text goes in `PLACE_LONG` in `src/long.py`.
- **A new picture.** Each picture is a small function in `src/art.py` that returns SVG shapes. Add it to `MOTIF` and give it a moon position in `MOON`, then use its name as `art=` in the story. To look at it quickly, render `art.scene("name", "#b08a3e")` into a small HTML file and screenshot it with Playwright. `_gorsedd` (a stone circle under the three rays of the Nod Cyfrin) is the example.
- **Fix wording at the source.** `REWORD` in `src/pride.py` hides old wording at build time, but the old words stay in the files. For a rule the owner feels strongly about (Iolo is never called a forger), change the original line in `data.py`, `more.py`, `long.py` or `features.py` and delete the `REWORD` pair.
- **Sweep the built site.** After building, search every page and `_site/search.json` for the banned words (for Iolo: forger, forged, ffug, laudanum, invented, dyfeisiedig). Search with plain `grep -l "word" _site/*` rather than a long regular expression: the pages are single long lines and a regex with `.{0,120}` on both sides can run for minutes.
### A long person page with headings, and a map of places (November 2026)

Learnt while expanding Arthur's page (`src/arthur.py`).

- A person page now understands the same codes as a long read (`## `, `> `, `|| `). If any line of the person's long text starts with one, `person_page()` in `build.py` lays it out like a long read; otherwise it stays as plain paragraphs. So any person can be given headings, pull quotes and a fact table just by writing them in.
- `PERSON_EXTRA` in `build.py` adds extra sections to one person's page. Arthur's adds "The line of Arthur" (a row of boxes with arrows, which turns into a column on phones) and "Arthur's Wales", a numbered map.
- A map of places needs no map library: draw `geo["outline"]` from `src/geo/map.json` in an SVG and place each pin with `x = (lon - minx) * k * sc`, `y = (maxy - lat) * sc` (the same sums the kingdoms map uses). Each pin links to its numbered entry in the list beside it, and `li:target` lights the entry up.
- When two pins sit on top of each other, move one aside with `NUDGE` and draw a short line back to the real spot. Keep pins well inside the SVG's `viewBox`, or the edge cuts them off.

### Kings and princes pages (November 2026)
- All the royal lines live in `src/royal.py`: one entry per kingdom, each with a list of rulers. `R(...)` is a ruler (sort year, dates, name, English note, Welsh note, optional link), `H(...)` a heading inside the list, `N(...)` a short note between rulers.
- `build.py` makes `kings.html` (all of Wales: Gruffudd ap Llywelyn first, then kings who ruled most of Wales, the Princes of Wales, the kingdoms, and every ruler in one list by century) and one `kings-<id>.html` per kingdom.
- The combined list merges a ruler who held several kingdoms into one line, with a chip for each kingdom. `HOME_REALM` in `build.py` picks which note is shown.
- Person and place pages link back to every kingdom list that names them, automatically. The kingdoms map legend links each realm to its page through `KGLINK` in `build.py`.
- Welsh dates are made from the English ones by `cy_dates()`: "c." becomes "tua", "d." becomes "m.".
- For the earliest kings, mark dates "c." and say the genealogies are the witness, rather than leaving people out.
- The kingdoms of the Old North (Rheged, Gododdin, Strathclyde, Elfed, Efrog) are in the `NORTH` list in `src/royal.py`, marked `group="north"`, so `kings.html` shows them in their own "Yr Hen Ogledd" section. A ruler linked to a poet's page (`P("taliesin")`) makes that poet's page link back to the kingdom.

### Royal family trees (November 2026)
- The trees live in `src/trees.py` and become `family-trees.html`. Each person is `T(name, dates, role, note, link, crown, kids=[...])`; a person's children go in `kids`, so the tree is written exactly as it is shaped. Put the child who carries the line on **last**, so the main line runs to the bottom.
- `goto=(anchor, English, Welsh)` links a person to the same family in another tree (Gwenllian of Gwynedd to her husband in Deheubarth). `gap=True` makes a dashed row standing for several generations; say how many in `FT_GEN` in `build.py`.
- The tree is plain nested lists. The joining lines are CSS borders on each list item (`::before` for the upright, `::after` for the elbow); a person with only one child sits straight below with no indent, which keeps fifteen generations readable on a phone.
- Tapping a name walks up the lists to the founder, lights that line and counts the generations. A link like `family-trees.html#ft-owain-glyndwr` opens the page with that line already lit.
- "The road to Bosworth" is a CSS grid with named areas (`grid-template-areas`): four columns on wide screens so the lines meet in the middle, one column on phones.
- Person pages and kingdom pages link to the trees automatically (`ft_link_for_person`, `ft_link_for_realm`). If two trees show the same person, give the copy an `id` of its own, or the build stops.
- Python checks brackets for you: if a long nested tree will not load, a short script with `tokenize` shows which opening bracket was never closed.

### Welsh word of the day and Learn Welsh page (November 2026)
- Everything is in `src/cymraeg.py`: `WORDS` (one per day: word, sound guide, meaning, a Welsh example with its English, a history note in both languages, and a link), `FIXED_DAYS` (dates that always get the same word, such as Gŵyl Dewi on 1 March), `PHRASES` (the sections on `welsh.html`) and `LETTERS` (how Welsh sounds).
- `build.py` writes `welsh.js`: the words as data, then `src/welsh.js`. Ordinary days take the next word from a shuffled order that is fixed by a seed, so every visitor sees the same word on the same date and the order only changes when words are added. The day comes from the visitor's own clock. Raise `WELSH_JS_VER` in `build.py` when `src/welsh.js` changes, so phones fetch the new file.
- Any element with `data-wotd` becomes a word-of-the-day card (home page language section and `welsh.html`); `data-wotd-week` lists the last seven days. Any button with `data-hear="Welsh text"` and `data-guide="sound guide"` plays it.
- Sound: a matching MP3 in `src/static/audio/` is played first (file name = the Welsh in lower case, accents dropped, spaces as hyphens, e.g. `bore-da.mp3`, `gwyl-dewi.mp3`). Otherwise the device speaks: a Welsh voice if it has one (Microsoft Edge on Windows does), else an English voice reading the sound guide. Credit any freely licensed recording in `AUDIO_CREDITS`; the credit then shows on `welsh.html`.
- Wikimedia Commons and Lingua Libre (free Welsh recordings) cannot be reached from Claude's cloud sessions, so recordings have to be downloaded on the PC or recorded by a Welsh speaker.

### Saints of Wales pages (November 2026)
- All the saints live in `src/saints.py`: one entry per region (the old kingdoms, plus "Across the sea" for Brittany and Cornwall), each with saints made by `S(...)`: id, English and Welsh names, dates, feast day as `(day, month)` or `None` when unsure, notes, and the llannau named after them.
- Every llan is listed once in `LL` with its latitude and longitude. Places outside Wales are marked `away=True`: they show as dashed chips but are left off the map. The build stops with an error if a saint names a place missing from `LL`.
- Coordinates came from the free GeoNames list of places with 500+ people (inside the Python package `geonamescache`, which can be downloaded from PyPI when Wikipedia and OpenStreetMap are blocked), plus map reading for the smallest hamlets.
- The map is drawn at build time: each llan becomes a dot on the same outline of Wales as the home page map, using the same sums (`x = (lon - minx) * k * sc`, `y = (maxy - lat) * sc` from `src/geo/map.json`). `src/static/saints.js` adds the saint picker, the tap card, the llan name decoder (it undoes the soft mutation after "llan") and "today's saint".
- Region pages link to the matching kings page and back; person and place pages link to their saints region automatically through `saints_links()` in `build.py`.

### Adding a legend, and the sections of the Legends page (November 2026)
- The first seven legends are in `LEGENDS` in `src/features.py`; the rest are in `src/legends2.py`, in the same shape (id, era, art, place, titles, summaries, tale `pEn`/`pCy` with `## ` sub-headings, and the history behind it `hEn`/`hCy`).
- `GROUPS` in `src/legends2.py` sets the sections of `legends.html` and the order of the legend pages (the "next legend" button follows it). Every legend id must be in exactly one group: the build stops and names the missing or extra id if not. The home page shows the four in `LEGENDS_HOME` in `features.py`.
- Every legend needs an `art` key. New legends use their own key (`horse`, `boar`, `hare` ...) which `_STAND_IN` in `src/art.py` points at an existing scene for now. To give one its own lifelike picture, add a scene function for that key; the legend text never changes.
- Arthur has a page among the legends (`legend-arthur.html`, "King Arthur, the sleeping king"), at the owner's request, but he is never called a myth, legend or fiction (see `EDITORIAL.md`): the page opens "Welsh tradition holds that Arthur was Athrwys ap Meurig", tells the tales Wales tells of him, and its history box is headed "The king behind the tales" (`hLabelEn`/`hLabelCy`). `links` adds buttons under the history box, here to `person-arthur.html`.
- `mabinogion.html` is built by `mabinogion_page()` in `build.py` from `src/mabinogion.py`: the intro (same paragraph codes as long reads, so `|| left | right` makes the table of manuscripts) and the eleven tales in `GROUPS`. A tale with `link` gets a "Read the tale" button; one without is told in full on the card and is listed in search. When a tale gets its own legend page, put its file name in `link`. The page is linked from the Legends page (under the Four Branches), the menu, the footer and search.
- The "Storyteller" badge (`src/static/site.js`) is for reading ten legends, so it does not need changing when legends are added.

### More famous people and Welsh world firsts (November 2026)
- New people go in `src/people2a.py` (to 1750), `people2b.py` (1750–1914), `people2c.py` (politics, writing, art, science since 1914) `people2d.py` (music, stage and screen, sport) , `people2e.py` (more for every age, from prehistory to today) or `people2f.py` (people from published lists such as the 100 Welsh Heroes). Each is one `P(...)` line: slug, age, dates, English and Welsh names and epithets, Wikipedia title, field, short bio in both languages, the longer story as paragraphs in both languages, and `first=` if they did something first. Dates like `c. 31,000 BC` or `d. AD 61` sort correctly within an age (`_born` in `data.py`); people whose dates tie keep their file order. `src/people2.py` gathers them; `data.py` and `long.py` add them at their ends, so every person gets a page, a search entry and a place in the sitemap with no other change.
- Every person on the site has a field in `FIELD` in `src/people2.py` (the chips under the age chips in the People section). A person added anywhere else needs a line there too, or the build check below fails.
- Firsts live in `FIRSTS` (by person) and `OTHER_FIRSTS` (by place or nation) in `src/people2.py`. `"world"` means a first or record for the world; `"wales"` means a first for Wales or Britain, or a Welsh first abroad. They feed `firsts.html`, the gold badge on person pages, the gold tag on People cards and the ★ Firsts chip. Where a first rests on tradition (Madog), the text says so.
- The People section reads `?field=` on the address, so `index.html?field=sport#people` opens with sport picked and `?field=first` shows the firsts. Person pages link their field this way.
- Quick check after adding people: `python3 -c "import sys; sys.path.insert(0,'src'); import data, people2; print([p[0] for p in data.PEOPLE if p[0] not in people2.FIELD])"` must print `[]`.
- Person photos: Wikipedia, Wikimedia and Wikidata are blocked from the cloud, so look them up on the owner's Mini-PC through Remote Control (Node `fetch` or PowerShell). Ask the Wikipedia API for each article's free lead image (`action=query&prop=pageimages&piprop=name&pilicense=free&redirects=1`, up to 40 titles a call), then ask the Commons API for each file's credit (`prop=imageinfo&iiprop=extmetadata&iiextmetadatafilter=Artist|LicenseShortName`). Commons answers 429 to a bare User-Agent: send one with the site address, such as `HistoryOfWalesSite/1.0 (https://historyofwales.cymru)`, and pause a second between calls. Put the results in `src/photos2.py` as slug → (file, caption EN, caption CY, credit); `photos.py` merges them, and the credit prints after "Photo: Wikimedia Commons". A lead image is not always the person (a map, a coat of arms, a grave, an album cover): skip it, or write a caption that says what it shows.

### The four notes in the top folder (November 2026)

`README.md` says what the site is and where things live. `EDITORIAL.md` holds the owner's rules for how it is written. `TODO.md` lists the open jobs. `SKILLS.md` is this file. The owner wants them kept clean and tidy: when something changes, edit the line that is there instead of adding a new one at the bottom, delete finished jobs from `TODO.md`, and keep the counts in `README.md` true.

### Adding or splitting an age (November 2026)

The ages are layered: `src/data.py` holds the original four, `src/ages.py` adds Saints and Kings, and `src/ages9.py` adds Roman Wales, Tudor and Stuart Wales and Wales Today. Each layer is applied at the bottom of `data.py`.

To add an age:
1. Write its `dict` (id, names, span, blurb, two story paragraphs, in English and Welsh) in `src/ages9.py`, and add teacher notes to `TEACH` there.
2. Put it in the `ERAS = [...]` line at the bottom of `data.py`, and extend `age()` so events move into it by year. Move people and places with the `*_PEOPLE` sets and `PLACE_ERA`.
3. Give it a colour in `COL` and a picture in `ERA_ART` (`build.py`), the same colour as `--e-<id>` plus a `[data-era="<id>"]` rule in `src/head.html`, and a name in `ERA_NAMES` in `src/static/play.js`.
4. Update the words that count the ages: the heading in `src/body.html`, the footer column in `build.py` and the "ages" badge in `src/static/site.js`.

With nine posters in a row, a closed poster is too narrow for its title, so closed posters print the title up the side (`writing-mode: vertical-rl` with `text-orientation: sideways`, so apostrophes turn with the letters) and the open one prints it normally.

### On this day in Welsh history (November 2026)

- The entries live in `src/onthisday.py`, one row each: day (`"MM-DD"`), year (or `None` for a saint's day or custom), kind (`ev`, `born`, `died`, `feast`, `custom`), title and one line in English and Welsh, and a link to a page on the site. Timeline events in `src/data.py` that have a day are added automatically, so never type one twice.
- Saints' feast days are not typed here: `otd_rows()` adds every saint with a feast day in `src/saints.py`, so the Saints of Wales calendar and On this day always agree. A row in `onthisday.py` with the link `"saint:<id>"` gives that saint fuller words and links to their saint page.
- `build.py` (`otd_rows()`) merges and sorts them and writes `onthisday.json` for the home page panel, plus `onthisday.html`, the whole year with today's card ringed in red.
- The home panel (`renderToday()` in `src/app.js`) first shows the dated timeline events, then switches to the JSON once it loads. The ‹ › buttons step through the year (a leap year, so 29 February is a day too). On a day with no entry it says so and shows the nearest dates either side, so there is never an empty box.
- To fill a gap: `python3 -c` over `onthisday.OTD` lists the empty days. Only add a date you can stand behind. Wikipedia's "<year> in Wales" pages (1700s onwards) list dated events, births and deaths, and the Catholic calendar for Wales (liturgyoffice.org) gives the saints' feast days; both can be read with Claude's web fetch tool even though the network blocks Wikipedia directly.
- `$()` in `app.js` never returns null (it hands back a dummy element), so test for a home-page box with `document.getElementById`.

### The copyright notice

- In the UK copyright is automatic: nothing needs registering. The notice just makes ownership plain and helps if someone does copy.
- The © line at the bottom of every page is made by `footer()` in `build.py`. The name in it is `COPYRIGHT_OWNER` (English) and `COPYRIGHT_OWNER_CY` (Welsh) just above that function; the year updates itself (2026, then 2026–2027 and so on).
- It claims only the site's own text and design. Photos (Wikimedia Commons) and the 3D dragon stay credited to their creators, as listed in README.md.

### Welsh literature, the great books and the Triads (November 2026)

Three pages: `literature.html` (the ages of Welsh literature, with a cynghanedd example), `books.html` (the manuscripts and first printed books) and `triads.html` (Trioedd Ynys Prydain).

- **Where the words live.** All the text is in `src/literature.py`: `AGES`, `BOOK_GROUPS`, `TRIAD_GROUPS` and the intro lists. `literature_page()`, `books_page()` and `triads_page()` in `build.py` lay them out. To add a book or a triad, copy one entry in `literature.py`; it appears on the page and in search by itself.
- **Quotes with a translation.** In an age's text, a line written `> Welsh words — English words | source` shows the Welsh in large italics with the English underneath (`lit_prose()`).
- **Triads that open on a tap.** Each triad is a `<details>` box, so it works with no script. A tiny script copies one of them into "Triad of the day", chosen by the day of the year.
- **Pictures.** A picture is either a gallery id (already on the site, with its credit) or a Commons tuple: file, author, licence, licence link, caption EN, caption CY, width, height. Commons files are kept on the site by the "Fetch photos" workflow (run it from the Actions tab after adding new ones).
- **Picture research when Commons is blocked.** Put categories and search words in `tools/commons_research_in.json` and push it to a `claude/` branch. The "Look up pictures on Wikimedia Commons" workflow (`tools/commons_research.py`) commits a list with licences and small previews to `_research/<name>/`, which can be looked at before choosing. Delete the `_research` folder before merging. Keep `max` under about 400 and leave out search words that catch unrelated pictures (a search for "Yny lhyvyr hwnn" filled the list with book fairs).
- **Poet pages link back.** Anyone listed in an age's `people` gets a "Welsh literature" link on their person page (`lit_link()`).

### The castles map (November 2026)

`castles.html` shows every castle site in Wales on one map that you can drag and zoom, with who built each one. Welsh-built castles are red and drawn on top.

- **The parts.** `src/castles_data.json` is the list of sites (827). `src/castles.py` holds the hand-written part: the five colour groups, the kinds of castle, and for the best-known castles who built them, when, a short note in English and Welsh, links and a photo. `src/castles.css` and `src/static/castles.js` draw the page; `castles_page()` in `build.py` puts it together. To add a story to a castle, add one `add(...)` line in `src/castles.py` (its Q-number is in `castles_data.json`). When `castles.js` changes, raise the number after `castles.js?v=` in `build.py`.
- **Getting Wikidata when Wikidata is blocked.** The cloud machines cannot reach Wikidata, Wikipedia or Commons. A free (CC0) copy of Wikidata's medieval castles is kept on GitHub by the Shelf project, and GitHub can be reached. `tools/castles_from_wikidata.py` reads that copy, keeps only the sites inside Wales (tested against the county shapes in `src/geo/la.json`), drops ruins of other things that were tagged as castles, and writes `castles_data.json`. The lists `DROP` and `FORCE` at the top fix the odd mistake by hand.
- **Shaded relief from real heights.** `tools/bake_relief.py` downloads open height tiles (Mapzen Terrarium, from Amazon S3, which can be reached), shades the hills as if lit from the north-west, darkens England and the sea, and saves two pictures in the site's own map projection (`relief-1200.webp`, and `relief-3600.webp` for close zoom). The projection numbers come from `src/geo/map.json`, so dots, county lines and relief all line up.
- **Dates in Welsh.** `castle_date_cy()` in `build.py` turns "late 12th–13th century" into "diwedd y 12fed–13eg ganrif" and "1280s" into "1280au". The page is sent the Welsh form of each date; there is no second copy of the rule in the JavaScript.
- **Photos are linked straight from Commons** with the author and licence beside each one. A photo that fails to load is hidden, and the card still works.
- **Big maps stay light.** The county lines are joined into long lines and rounded to whole map units (`county_lines()`), which cut them from 146 KB to 25 KB.

## The opening screen (November 2026)

### How the opening screen is layered
- Back to front: the painted sky on a `<canvas>` (`#sky`: stars, moon, Milky Way, mist), the 3D mountains, moor and castle (`#land3d`), then the 3D dragon (`#sky3d`). Details in the entries below.
- Phones get their own flight path so the dragon never covers the text.
- Visitors who turn on "reduce motion", or whose device cannot draw 3D, see the painted mountain, castle and flag dragon instead.

### A sky that follows the real time of day (November 2026)

The home page sky is drawn in `src/app.js`. `sunOverWales()` works out how high the sun is over mid Wales from the clock alone (no location permission, no network), and `setSky()` blends between four palettes in `SKIES` (night, dawn, day, dusk) once a minute. Every colour in the scene reads from `SKY`, so a new palette is one line. To preview one, add `?sky=night`, `?sky=dawn`, `?sky=day` or `?sky=dusk` to the home page address.

Keep the day palette dark enough for the light text to stay readable: the words sit on the sky, so "day" is a deep blue, not a pale one.

On wide screens (1100 pixels and up) the opening screen is capped at 60rem tall in `src/v6.css` so no empty band opens above the numbers, the mountain is sized to fit inside the right edge (`ew`, `ex0` in `draw()`), a Milky Way of faint stars (`milky`) fills the left of the night sky, and `drawCastle()` puts a castle on a crag at the right: a great keep, round towers, a twin-towered gatehouse with firelight in the gate, lit windows that flicker, and Y Ddraig Goch flying from the top. The castle is drawn in its own units (1 unit = `s`), so to change it edit the `tower(x, width, height, merlons)` and `slit(x, y, height, n)` calls. The dragon is the real artwork of the national flag, kept as vector text in `DSVG` in `src/app.js` (from the flag-icons project, MIT licence, credited in a comment there and in README.md). Hand-drawn dragons were tried twice and the owner rejected them as fake, so do not redraw it by hand. `svgImage()` turns the artwork into a picture. `flagArt()` paints the flat flag with it on a hidden canvas, and `drawCastle()` draws that in 48 thin slices, each lifted and shaded by a wave, so it billows like cloth. `drawDragon()` uses the same artwork, mirrored and a little brighter, as the stand-in for the dragon in the sky on devices that cannot show the lifelike one.

Other effects in the same file: shooting stars (`drawMeteors`, night only), the dragon's fire (`fireAt`, every 9 to 16 seconds or when tapped; `DPOS` is where the dragon is for the tap test), and tilt (the `deviceorientation` listener feeds the same `mouse` value the pointer does; skipped on iOS, which asks permission). The glint on "Cymru" is CSS in `src/v6.css` (`@keyframes glint`), using a gradient clipped to the text; the letters need extra `padding-block` or their tails are cut off.

### The site name above "Cymru" on the home page (November 2026)

On the home page the words "History of Wales" (Welsh: "Hanes Cymru") sit above the big "Cymru", not in the top bar. `HERO_NAME` in `build.py` writes them one letter per box (`_letters()`), and the same CSS rule as "Cymru" (`.hero h1 span, .hero .hero-name b` in `src/head.html` and `src/v6.css`) makes every letter drop in and glint. The home top bar has no name or mountain; it starts with the links, and on screens wider than 1480 pixels it shows four more (`NAV_HOME_MORE` in `build.py`). Every other page keeps "History of Wales" in the top bar as the way home.

### The lifelike dragon in the sky

The dragon that flies across the opening screen is a real 3D model with a skeleton, so its wings beat properly. It is drawn with three.js on its own see-through canvas (`#sky3d`) laid over the painted sky.

- `src/static/dragon.glb` is the model: one mesh, its textures and one "flying" animation of 13 seconds. It came from the Ethereal Engine "Open Asset Kit, Basic" (`assets/fantasy/Dragon.glb`), which says its assets are Creative Commons but names no author. See the credit in README.md and the open question in TODO.md. The original is 35 MB; it was cut to 1.7 MB by keeping only the flying animation, shrinking the textures to 1024 pixels as WebP and converting the material (gltf-transform: `metalRough`, `resample`, `prune`, `textureCompress`, `quantize`).
- `tools/dragon3d.src.js` is the code that loads and lights the model. It is bundled with three.js and the landscape code into `src/static/hero3d.js` (see "The 3D mountains and castle" for how to rebuild).
- `src/app.js` still decides where the dragon is, how big, and when it breathes fire (`drawDragon()`), and hands that to `HCD3.frame()` each frame. `flames()` paints the fire on a small canvas of its own, which is handed over with the rest and shown as a glowing sheet at the dragon's mouth, so that the fire shows in front of the mountains.
- The 3D files load only on the home page, after the page itself, and only when the device has WebGL, is not in data-saver mode and has not asked for reduced motion. Otherwise, or if loading fails or takes over 15 seconds, the flag dragon is shown.
- To watch the fire without waiting, add `?fire=1` to the address (it works with `?sky=night` and the others).
- To test with a headless browser, start Chromium with `--use-gl=swiftshader --enable-unsafe-swiftshader`; without WebGL you will only see the stand-in.

### The 3D mountains and castle

Behind the dragon, the mountains, the moor and the castle are real 3D too, drawn on a second see-through canvas (`#land3d`) between the painted sky and the dragon. The code is `tools/land3d.src.js`.

- **The mountains are Yr Wyddfa and its horseshoe, from real height data**, seen from the Capel Curig side. `tools/eryri_heights.py` downloads the height tiles; `tools/bake_eryri.py` turns them into three files in `src/static/`: `eryri-h.png` (heights), `eryri-c.webp` (colour: grass, scree, rock, snow) and `eryri-n.webp` (fine relief for the light). The survey data is smooth, so the script sharpens it and adds crag detail on steep, high ground, and heights are drawn 1.3 times taller. The feet of the mountains are tinted to the colour of the valley mist, so that the range rises out of it (the mist is a cool grey painted on the 2D canvas, and its colour is passed to the 3D code as `mist`). Never make ground see-through or cut it away: the red glow of the sky then shows through the hole as a red blob. The one hill that stood too close to the eye is levelled into the valley floor in `buildLand` instead.
- **What makes the mountains look real.** Four things, found by trial: (1) the moon lights them from the side (`moonL` in `tools/land3d.src.js`), and the bake casts real shadows from the ridges for that same direction (`LIGHT` in `tools/bake_eryri.py`): the two must always match, so change both together and bake again; (2) the bake carves gullies where water would gather (flow down the real heights, with noise added so streams wander: without the noise they run in ruled lines); (3) colour is laid by what the ground is (grass and heather low down, scree, bare rock where it is steep, snow where it can lie); (4) the crags are a real photograph of rock (`rock.webp`) laid on steep ground from the side by the shader. Laying a picture on cliffs from above smears it into streaks, and drawing regular ledges into the heights gives fingerprint lines, so do neither.
- **The castle shows on every screen.** On phones and tall windows it stands on its crag at the foot of the mountains, in the strip below the buttons, with the moor in front, so they read as one scene (`ground` in `draw()` in `src/app.js`).
- **Stars are soft glowing points, never plus signs.** `STAR` in `src/app.js` paints one glowing star in three tints (white, blue-white, warm) and the sky stamps it at varied sizes with a gentle twinkle.
- **Nothing in the opening picture may depend on the height of the window.** On Android the address bar hides as you scroll, the window grows, and anything sized from it jumps. On phones the mountains take a fixed share of the strip below the buttons (`eh` in `draw()` in `src/app.js`).
- **Measure where things rest, not where they are mid-animation.** The buttons slide up 22 px as they arrive; measuring them mid-slide put the land 22 px low, and it then jumped up. `measure()` in `src/app.js` reads their resting place from the layout, and the land waits for the fonts. `node tools/hero_jump_check.js` (with the site served on port 8000) lists every position the land is drawn at while the page loads: there must be exactly one line.
- **The dragon stays below the menu bar.** `drawDragon` in `src/app.js` measures the bottom of the menu bar and lowers the flight just enough for the raised wingtips to clear it (`WING_UP`; try other values with `?wing=0.5` on the address).
- **When `hero3d.js` changes, raise the number after `hero3d.js?v=`** in `src/app.js`, or visitors keep the old copy in their browser.
- **The castle is built from plain shapes in code** (`buildCastle`): keep, stair turret, round towers with spreading feet and battlements, curtain walls, twin-towered gatehouse. It is clad in a photograph of slate walling (`stone.webp`), darkened towards the foot, lit by the moon with real shadows, with firelight at the gate and windows. The flag is a 3D cloth that carries the same flag painting as before (`flagArt()` in `src/app.js`).
- **The crag and the moor** use a photograph of mossy rock (`rock.webp`). `tools/bake_textures.py` makes the web-sized textures and their relief maps from the original photographs.
- **Only the flag moves**, so after one full picture only the small patch of screen around the flag is drawn again each frame. A full picture is drawn again when the window, the sky, the mouse position or the scroll changes.
- `src/app.js` decides where the summit and the castle go (`HCL3.frame()` in `draw()`). Until the 3D is ready only the sky shows, then the land fades in. On wide screens it waits for the castle too, so mountains and castle arrive together. If the device cannot draw 3D, or the visitor asks for reduced motion, the old painted mountain and castle are used.
- **The opening is staged** so nothing arrives half-drawn: sky and title letters first; the words and buttons under the title fade up from 0.9 s (`src/v6.css`); the land fades in when ready but never before 1.2 s; the dragon waits until the land has finished fading in and then starts at the beginning of its flight (`DT0` in `drawDragon()`).
- To rebuild `src/static/hero3d.js` after changing anything in `tools/*.src.js`: in a folder with `three` (0.160) and `esbuild` from npm, run `npx esbuild hero3d.src.js --bundle --minify --format=esm --target=es2019 --outfile=hero3d.js` and copy the result to `src/static/`.
- To test 3D without a graphics card, start Chromium with `--use-gl=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist`.

### Photographs for the legend pictures

- Seven legends (the hound, owl, starling, Llyn y Fan Fach, the drowned forest, Arthur's lake, the cauldron) show a real photograph from Wikimedia Commons in place of the drawn scene: `LEGEND_PHOTOS` in `src/art.py` holds the file, photographer, licence, a line saying what the picture shows, and where the subject sits in the frame. `photo_scene()` draws it; the legend page prints the credit under the tale (`legend_credit` in `build.py`).
- Only legend pages and legend cards use the photographs. Other pages that share an art key (and the newer legends that borrow a scene as a stand-in) keep the drawn scene. To give another legend a photograph, add its art key to `LEGEND_PHOTOS` and to `PICKS` in `tools/fetch_legend_photos.py`.
- Getting the files: Commons is blocked from the cloud, but not from GitHub. `tools/fetch_legend_photos.py` runs in the "Fetch photos" workflow when it changes on a `claude/` branch and commits `src/static/legends/<key>.webp` (1600 px) and `<key>-s.webp` (700 px) to the branch; then `git pull`. Commons only serves standard widths (1920, 1280, 960 ...), so ask for one of those and shrink.
- Choosing: fetch several candidates under temporary names the same way, look at them all on one contact sheet, keep the best and delete the rest before merging. Prefer Featured and Quality pictures; CC0, public domain, CC BY and CC BY-SA only.

### Looking up Commons pictures from GitHub (November 2026)

- Commons is blocked from Claude's cloud computer, so picture research runs on GitHub too. Write what to look for in `tools/commons_research_in.json` (your own branch name in `branch`, Commons categories, searches, or exact file names, and an `out` folder) and push it to that `claude/` branch. The look-up only runs on the branch named in `branch` (or when started by hand from the Actions tab), so other threads that merge main never run it; put `branch` back to `""` before merging. It never fails the run, so Ifan gets no failure emails. The "Look up pictures on Wikimedia Commons" workflow runs `tools/commons_research.py` and commits `<out>/found.json` (title, size, licence, author, description of every file) and a small preview of each (`<out>/<n>.jpg`). `git pull`, make a contact sheet of the previews with Pillow, and pick by eye.
- The first run also lists the subcategories it met; run it again on those to go deeper (that is how the Peniarth 28 drawings and the dragons in the margins of NLW MS 20143A were found).
- The `_research/` folder is only for choosing. Delete it before merging.
- To check a page before its Commons pictures are kept on the site, the Playwright screenshot script can answer the Commons links with the previews (`page.route`), so the page looks as it will live.

### The Laws of Hywel Dda page (November 2026)

- `laws.html` is built by `laws_page()` in `build.py` from `src/laws.py` (text, pictures, worth table, quiz, words) and styled by `src/laws.css`. Chapters use the same paragraph codes as long reads. A chapter can carry a block of its own: `books=True`, `officers=True`, `worth=True`, `gallery=True`, or `split=True` (the after-seven-years table, placed after the paragraph ending "item by item:").
- Pictures are listed once in `FIGS` (Commons file, maker, licence, captions) and drawn by `law_fig()` with the full credit. They load from Commons until the "Fetch photos" workflow keeps copies on the site.
- `LAW_LINKED` in `build.py` puts a card for the page in "The full story" on the people and places it names.

## Dragon pictures for the legend pages

- The red and white dragons on the legend, symbols and play pages are still pictures of the 3D dragon (`src/static/dragon-red.webp`, `dragon-white.webp`), placed in the scene by `_dragons` in `src/art.py`. Never draw dragons by hand.
- To make them again: bundle `tools/render_dragons.src.js` with esbuild, put it beside `dragon.glb` with a page holding `<canvas id="c">`, open it in headless Chromium (`?t=0.3` for red, `?white=1&t=0.52&turn=1.2&tilt=0.2` for white) and screenshot the canvas with a see-through background. Crop, mirror the white one so they face each other, and save as WebP 760 px wide.
- The white dragon is the same model with the red taken out of its skin in the shader, so the scales keep their light and dark.
- The hero's dark veil dulls pictures on the left; `.hero-art:has(image)::after` in `src/v6.css` uses a lighter veil where the art holds a picture.

## Keeping the PC copy updated and tidy

- Ifan's PC copy (`D:\Website\historyofwales.cymru`) updates itself every day through a Windows scheduled task, "History of Wales daily update", at 09:00 (or as soon as the PC is next on). It runs `D:\Website\historyofwales-daily\update-historyofwales.ps1`: pull main (fast-forward only, skipped if there are local changes), `python build.py`, then move leftover files that are neither in the repo nor made by the build to the Recycle Bin. Anything that could be Ifan's own (photos, documents) is only listed. Each run is written to `daily.log` in the same folder.
- It was set up through a Remote Control session on the PC, because the remote folder tools can read and copy files but cannot delete them.
- To stop it: Task Scheduler, then disable or delete "History of Wales daily update".

## Working together

- Ifan sends a screenshot plus a short note, and each change is made, checked and published within minutes.
- Small visual tweaks are published one at a time so each can be seen live.
