// Faster repeat visits, and the site still opens offline.
// - Pages (HTML) are fetched fresh when online and served from the cache when offline.
// - Files with a version in their address (site.js?v=…, hero3d.js?v=7) never change under that address,
//   so they come straight from the cache once fetched (cache first).
// - Pictures, fonts and the 3D files come from the cache at once and are checked in the background,
//   so a picture that is replaced under the same name shows from the next visit (stale while revalidate).
// - Sound files are left alone: browsers ask for them in pieces, which a cache cannot answer.
const PAGES = "history-of-wales-v7";
const FILES = "history-of-wales-files-1";
const MAX_FILES = 600; // oldest files are dropped past this, so the cache never grows without end
const ASSET = /\.(?:webp|jpe?g|png|gif|svg|ico|glb|woff2?|css|js|webmanifest)$/i;

self.addEventListener("install", (e) => { self.skipWaiting(); e.waitUntil(caches.open(PAGES).then((c) => c.addAll(["./", "./index.html"]))); });
self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== PAGES && k !== FILES).map((k) => caches.delete(k)))));
  self.clients.claim();
});

let puts = 0;
function keep(req, res) {
  if (!res || !res.ok || res.type !== "basic" || res.status !== 200) return;
  const copy = res.clone();
  caches.open(FILES).then((c) => c.put(req, copy).then(() => {
    if (++puts % 25) return;
    c.keys().then((ks) => { for (let i = 0; i < ks.length - MAX_FILES; i++) c.delete(ks[i]); });
  }));
}

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET" || req.headers.has("range")) return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;
  const versioned = url.searchParams.has("v");
  if (versioned || ASSET.test(url.pathname)) {
    e.respondWith(caches.open(FILES).then((c) => c.match(req).then((hit) => {
      const net = fetch(req).then((res) => { keep(req, res); return res; });
      if (hit) {
        if (!versioned) e.waitUntil(net.catch(() => {})); // refresh in the background
        return hit;
      }
      return net;
    })));
    return;
  }
  e.respondWith(fetch(req).then((res) => {
    if (res.ok && res.type === "basic") { const copy = res.clone(); caches.open(PAGES).then((c) => c.put(req, copy)); }
    return res;
  }).catch(() => caches.match(req).then((r) => r || caches.match("./index.html"))));
});
