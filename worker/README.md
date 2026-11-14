# The weekly quiz leaderboard

A Cloudflare Worker (free plan) that keeps the leaderboard for `weekly-quiz.html`. See SKILLS.md, "The weekly quiz and its leaderboard".

- `GET /board?week=YYYY-MM-DD&pid=…` the week's top 20, how many have played, your own place, and last week's top 3
- `POST /score` `{week, pid, nick, ans, secs}` adds a score, once per player a week; the score is worked out here

It is put up by `.github/workflows/deploy.yml` once the `CLOUDFLARE_API_TOKEN` secret is set. The answer key
(`src/gen.json`) is written at deploy time by `python3 src/weeklyquiz.py worker` and is not committed.
