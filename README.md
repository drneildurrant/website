# neildurrant.com

The personal site of Neil Durrant — writer, philosopher, ethicist, technologist, heretic. A static landing page plus the **Mantrabytes** decoder, served from this repo via GitHub Pages, and the front door to a small ecosystem of "—bytes" reading tools.

```
neildurrant.com             → this repo (GitHub Pages)
  /decoder/                 → Mantrabytes (mātṛkā mantra coder/decoder)
tantrabytes.neildurrant.com → private repo · Azure Static Web Apps
monobytes.neildurrant.com   → private repo · Azure Static Web Apps
viz.neildurrant.com         → private repo · Azure Static Web Apps
substack.neildurrant.com    → external (Substack)
```

## What's in this repo

| Path | What it is |
|------|------------|
| `index.html` | The home page — a single self-contained file (inline CSS + JS) |
| `decoder/index.html` | Mantrabytes — the mātṛkā mantra coder/decoder (self-contained) |
| `posts.json` | "Latest writing" list, auto-refreshed from the Substack RSS feed |
| `quotes.json` | Hand-curated pull quotes rotated on the home page |
| `scripts/fetch_substack.py` | Regenerates `posts.json` from the feed (stdlib only) |
| `.github/workflows/refresh-substack.yml` | Weekly job that runs the fetch script |
| `CNAME` | Custom domain (`neildurrant.com`) for GitHub Pages |
| `docs/` | Maintainer documentation (see below) |

## Run it locally

No build step — it's plain static files. Serve the folder and open it:

```bash
python3 -m http.server 8000
# → http://localhost:8000/         (home)
# → http://localhost:8000/decoder/ (Mantrabytes)
```

(`file://` mostly works too, but a server avoids CORS issues with the `posts.json` / `quotes.json` fetches.)

## Deploy

Push to `main` → GitHub Pages redeploys `neildurrant.com` automatically. There is no staging branch. See [`docs/DEPLOY.md`](docs/DEPLOY.md).

## Documentation

- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — how the site and the wider subdomain ecosystem fit together, and the public/private boundary.
- [`docs/BRAND.md`](docs/BRAND.md) — the visual brand system (palette, type, the ND mark) shared across every surface.
- [`docs/DEPLOY.md`](docs/DEPLOY.md) — deploying, and how to update content (writing, quotes, project cards).
- [`CLAUDE.md`](CLAUDE.md) — orientation for AI assistants and new maintainers.
