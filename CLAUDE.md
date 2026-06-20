# CLAUDE.md — orientation for AI assistants & new maintainers

Read this first. Full detail is in [`docs/`](docs/); this is the quick map.

## What this repo is

The **public** static site for `neildurrant.com` — a single-file home page (`index.html`) plus the **Mantrabytes** decoder (`decoder/index.html`), served by **GitHub Pages**. No build step, no framework, no npm. Pages are self-contained (inline `<style>` + `<script>`).

## Hard rules

- **`push = live`.** GitHub Pages deploys `main` on push; there's no staging. Test locally (`python3 -m http.server 8000`) before pushing. Only commit/push when the user asks.
- **Keep it buildless.** Don't introduce bundlers, frameworks, or npm. Prefer inline CSS/JS and same-origin static files.
- **Don't delete `CNAME`** (`neildurrant.com`) — the custom domain breaks without it.
- **Public/private boundary — do not cross it.** The reading bots (`tantrabytes.` / `monobytes.` / `viz.`) live in the **private** `drneildurrant/sanskrit-tantra` repo and deploy via Azure Static Web Apps. They bundle ~135 MB of password-gated reading editions. **Never** move that content into this public repo. See `docs/ARCHITECTURE.md`.

## Where things are

| Want to change… | Edit |
|---|---|
| Home page copy/layout | `index.html` |
| Decoder | `decoder/index.html` |
| Colours / fonts (brand) | `:root` in `index.html` (+ `decoder/index.html`); see `docs/BRAND.md` |
| "Latest writing" | auto from Substack via `scripts/fetch_substack.py` — usually don't hand-edit `posts.json` |
| Pull quotes | `quotes.json` |
| Project cards | `#work` grid in `index.html` (`docs/DEPLOY.md` has the card pattern) |

## Brand in one line

Cool greyscale + a single **crimson (Śakti-red)** accent, **Cormorant Garamond + Lexend**, static-grain texture. The 2021 brand deck is a *baseline for reflection, not a spec*. There's a shelved ND sacred-geometry mark (`TODO(brand mark)` placeholders in `index.html`). Details: `docs/BRAND.md`.

## Docs index

- `docs/ARCHITECTURE.md` — ecosystem topology, data flows, the public/private boundary
- `docs/BRAND.md` — palette, type, the ND mark, how to apply the brand
- `docs/DEPLOY.md` — deploying + updating content (writing, quotes, cards)
