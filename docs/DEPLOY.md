# Deploy & content updates

## How deploy works

- Hosting: **GitHub Pages**, serving the repo root on the `main` branch.
- Custom domain: **`neildurrant.com`** via the `CNAME` file (don't delete it — Pages needs it each deploy).
- **Push to `main` → Pages rebuilds and the site goes live** (usually < 1 min). There is no staging branch, so:
  - Test locally first (`python3 -m http.server 8000`).
  - `push = live`. Treat it accordingly.
- The subdomain bots (`tantrabytes.` / `monobytes.` / `viz.`) deploy from the **private `sanskrit-tantra` repo** via Azure Static Web Apps — nothing in this repo affects them. See `docs/ARCHITECTURE.md`.

## Updating content

### Latest writing (`posts.json`)

Auto-maintained — you normally don't touch it.

- `.github/workflows/refresh-substack.yml` runs **weekly** (cron `0 19 * * 0` = Mon 05:00 Australian Eastern / 19:00 UTC Sun) and on manual dispatch.
- It runs `scripts/fetch_substack.py`, which pulls the Substack **"Provocations"** feed (`https://neildurrant.substack.com/feed`), writes the newest few posts to `posts.json`, and commits **only if it changed** (no churn). Pages then redeploys.
- The home page fetches `posts.json` and shows the top 3.
- To refresh now: run the workflow via *Actions → Refresh Substack posts → Run workflow*, or `python3 scripts/fetch_substack.py` locally and commit.

> Note: the workflow file's header comment historically said "every 6 hours" — the actual schedule is weekly (the cron above). Trust the cron.

### Pull quotes (`quotes.json`)

Hand-curated. Edit the `quotes` array — each entry is `{ "text": "...", "cite": "..." }`, verbatim from the corpus translations with a `text-id + verse` citation. The home page rotates through them client-side. Keep ≥ 2 entries (rotation needs at least two).

### Project cards ("What I'm building")

In `index.html`, the `#work` grid. Current cards (in order):

| Card | Status | Link |
|---|---|---|
| Tantrabytes | Live | `tantrabytes.neildurrant.com` |
| Mantrabytes | Live | `/decoder/` |
| Monobytes | Live | `monobytes.neildurrant.com` |
| Viz | Live | `viz.neildurrant.com` |
| Eurobytes | Soon | — |

Card patterns:
- **Live** tool → `<a class="card pc" href="…">` with `<span class="badge">Live</span>` and a `<span class="card-cta">Enter →</span>`. The `pc` class adds the crimson top-edge signature.
- **Coming** tool → `<div class="card soon">` with `<span class="badge dev">Soon</span>` and no link.
- Keep live cards before "Soon" cards.

### Theme / colours

All tokens live in the `:root` block of `index.html` (and mirrored in `decoder/index.html`). See `docs/BRAND.md`. Changing a token there reflows the whole page.

## Gotchas

- Don't remove `CNAME` — the custom domain breaks until it's restored.
- Keep pages self-contained (inline CSS/JS); there's no build to bundle assets.
- The Google Fonts `<link>` must stay in `<head>` or headings fall back to system serif/sans.
