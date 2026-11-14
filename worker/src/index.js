/* The weekly quiz leaderboard for historyofwales.cymru (a Cloudflare Worker, free plan).

   GET  /board?week=YYYY-MM-DD&pid=…   this week's top 20, how many have played, your own place, and last week's top 3
   POST /score {week, pid, nick, ans, secs}   adds a score, once per player a week

   The score is worked out here from the answers, with the answer key that deploy.yml writes into gen.json from
   src/quiz_weeks.json, so nobody can claim 10/10 without the right answers. Each week has its own small database
   (a Durable Object); it keeps only the nickname, the score, the time, when it was added and the random code the
   visitor's browser made (pid), and deletes itself twelve weeks after the week ends. No IP addresses, names or
   emails are stored. Nicknames on the list in src/quiz_hidden.json are never shown. */
import { DurableObject } from "cloudflare:workers";
import GEN from "./gen.json";

const ORIGINS = ["https://historyofwales.cymru", "https://www.historyofwales.cymru", "https://tywysog85.github.io", "http://localhost:8000", "http://127.0.0.1:8000"];
const HIDDEN = new Set((GEN.hidden || []).map((s) => s.toLowerCase()));
const KEEP_MS = 12 * 7 * 864e5;   // twelve weeks
const DAY = 864e5;

// rude words, in English and Welsh. ANYWHERE ones are caught inside other letters once spaces, dots and number-letters
// are taken out; WORDS only on their own (so Contractor, Peacock and Grape are fine)
const ANYWHERE = ["fuck", "shit", "cunt", "twat", "wank", "bastard", "bitch", "slut", "whore", "nigg", "retard", "spastic", "hitler", "nazi",
  "penis", "vagina", "asshole", "cachu", "ffwc", "pidyn", "bastad", "porn"];
const WORDS = ["fuk", "dick", "cock", "prick", "piss", "arse", "fag", "dyke", "tranny", "paki", "rape", "sex", "boob", "tits", "cont", "coc", "twll", "hwr",
  "pen ol", "kkk", "isis", "jew", "nonce", "sperm", "cum"];

function clean(s) {
  return s.toLowerCase().normalize("NFKD").replace(/[\u0300-\u036f]/g, "")
    .replace(/0/g, "o").replace(/1|!|\|/g, "i").replace(/3/g, "e").replace(/4|@/g, "a").replace(/5|\$/g, "s").replace(/7/g, "t").replace(/8/g, "b");
}
function rude(nick) {
  const s = clean(nick), squashed = s.replace(/[^a-z]/g, "");
  return ANYWHERE.some((w) => squashed.includes(w)) || WORDS.some((w) => new RegExp("(^|[^a-z])" + w + "s?([^a-z]|$)").test(s));
}
function nickOk(n) {
  return typeof n === "string" && /^[\p{L}\p{N}][\p{L}\p{N} '’._-]{1,23}$/u.test(n) && !/https?:|www\.|@|\.(com|net|org|uk|cymru|wales)\b/i.test(n) && !rude(n);
}

// Monday of the week a moment falls in, by the date in Wales
function weekOf(ms) {
  const parts = new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/London", year: "numeric", month: "2-digit", day: "2-digit", weekday: "short" }).formatToParts(new Date(ms));
  const get = (t) => parts.find((p) => p.type === t).value;
  const back = { Mon: 0, Tue: 1, Wed: 2, Thu: 3, Fri: 4, Sat: 5, Sun: 6 }[get("weekday")];
  const d = new Date(Date.UTC(+get("year"), +get("month") - 1, +get("day")) - back * DAY);
  return d.toISOString().slice(0, 10);
}
function prevWeek(wk) { return new Date(Date.parse(wk + "T00:00:00Z") - 7 * DAY).toISOString().slice(0, 10); }

// a score can be sent for this week, or for last week in the first 14 hours of Monday (for players far to the west),
// or for next week in the last 14 hours of Sunday (players far to the east)
function weekOpen(wk, now) {
  return [now, now - 14 * 3600e3, now + 14 * 3600e3].some((t) => weekOf(t) === wk);
}

function cors(req) {
  const o = req.headers.get("Origin");
  return {
    "Access-Control-Allow-Origin": o && ORIGINS.includes(o) ? o : ORIGINS[0],
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "86400",
    "Vary": "Origin",
  };
}
function json(req, body, status = 200, extra = {}) {
  return new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json; charset=utf-8", ...cors(req), ...extra } });
}

export class Board extends DurableObject {
  constructor(ctx, env) {
    super(ctx, env);
    this.sql = ctx.storage.sql;
    this.sql.exec("CREATE TABLE IF NOT EXISTS s (pid TEXT PRIMARY KEY, nick TEXT NOT NULL, score INTEGER NOT NULL, secs INTEGER NOT NULL, at INTEGER NOT NULL)");
    this.recent = new Map();   // in memory only, never stored: how many scores each connection sent lately
  }

  top(n) {
    const rows = this.sql.exec("SELECT nick, score, secs FROM s ORDER BY score DESC, secs ASC, at ASC LIMIT ?", n + 40).toArray();
    return rows.filter((r) => !HIDDEN.has(r.nick.toLowerCase())).slice(0, n).map((r) => [r.nick, r.score, r.secs]);
  }

  you(pid) {
    const me = this.sql.exec("SELECT nick, score, secs, at FROM s WHERE pid = ?", pid).toArray()[0];
    if (!me) return null;
    const better = this.sql.exec("SELECT COUNT(*) AS n FROM s WHERE score > ? OR (score = ? AND (secs < ? OR (secs = ? AND at < ?)))",
      me.score, me.score, me.secs, me.secs, me.at).one().n;
    return { nick: me.nick, score: me.score, secs: me.secs, rank: better + 1 };
  }

  players() { return this.sql.exec("SELECT COUNT(*) AS n FROM s").one().n; }

  async view(pid) { return { players: this.players(), top: this.top(20), you: pid ? this.you(pid) : null }; }

  async add(week, pid, nick, score, secs, conn) {
    const now = Date.now();
    const seen = (this.recent.get(conn) || []).filter((t) => now - t < 600e3);
    if (seen.length >= 40) return { error: "busy" };   // a whole class on one school connection still gets through
    seen.push(now); this.recent.set(conn, seen);
    if (this.recent.size > 5000) this.recent.clear();
    if (this.players() >= 20000) return { error: "busy" };
    this.sql.exec("INSERT OR IGNORE INTO s (pid, nick, score, secs, at) VALUES (?, ?, ?, ?, ?)", pid, nick, score, secs, now);
    if ((await this.ctx.storage.getAlarm()) == null) {
      await this.ctx.storage.setAlarm(Date.parse(week + "T00:00:00Z") + 7 * DAY + KEEP_MS);
    }
    return this.view(pid);
  }

  async alarm() { await this.ctx.storage.deleteAll(); }   // twelve weeks after the week ends, the whole board goes
}

async function hashed(s) {
  const b = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s + weekOf(Date.now())));
  return [...new Uint8Array(b)].slice(0, 8).map((x) => x.toString(16).padStart(2, "0")).join("");
}

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: cors(req) });
    const stub = (wk) => env.BOARD.get(env.BOARD.idFromName(wk));

    if (url.pathname === "/board" && req.method === "GET") {
      const wk = url.searchParams.get("week") || weekOf(Date.now());
      const pid = (url.searchParams.get("pid") || "").slice(0, 40);
      if (!GEN.keys[wk]) return json(req, { error: "week" }, 404);
      const [now, last] = await Promise.all([stub(wk).view(pid), GEN.keys[prevWeek(wk)] ? stub(prevWeek(wk)).view("") : null]);
      return json(req, { week: wk, ...now, last: last ? last.top.slice(0, 3) : [] }, 200, { "Cache-Control": pid ? "no-store" : "public, max-age=20" });
    }

    if (url.pathname === "/score" && req.method === "POST") {
      let b;
      try { b = await req.json(); } catch (e) { return json(req, { error: "bad" }, 400); }
      const key = GEN.keys[b.week];
      if (!key || !weekOpen(b.week, Date.now())) return json(req, { error: "week" }, 400);
      const pid = String(b.pid || "");
      if (!/^[a-z0-9]{8,40}$/i.test(pid)) return json(req, { error: "bad" }, 400);
      const nick = String(b.nick || "").trim().replace(/\s+/g, " ");
      if (!nickOk(nick)) return json(req, { error: "nick" }, 400);
      const ans = Array.isArray(b.ans) ? b.ans : [];
      if (ans.length !== key.length || !ans.every((a) => Number.isInteger(a) && a >= 0 && a < 4)) return json(req, { error: "bad" }, 400);
      const score = ans.filter((a, i) => a === key[i]).length;
      const secs = Math.round(Number(b.secs));
      if (!(secs >= 5 && secs <= 3 * 3600)) return json(req, { error: "bad" }, 400);
      // the connection's address is only used, scrambled with the week, to stop one machine sending many scores; it is never stored
      const conn = await hashed(req.headers.get("CF-Connecting-IP") || "");
      const r = await stub(b.week).add(b.week, pid, nick, score, secs, conn);
      if (r.error) return json(req, r, 429);
      return json(req, { week: b.week, nick: r.you ? r.you.nick : nick, ...r }, 200, { "Cache-Control": "no-store" });
    }

    if (url.pathname === "/") return json(req, { ok: true, about: "Leaderboard for the weekly quiz at https://historyofwales.cymru/weekly-quiz.html" });
    return json(req, { error: "not found" }, 404);
  },
};
