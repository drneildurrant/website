# Brand system

The visual identity shared across every surface (`neildurrant.com`, the decoder, and the bots/viz in the `sanskrit-tantra` repo). The canonical implementation is the `:root` block at the top of `index.html` — this doc explains the *why* and keeps the values in one readable place.

## Origins — a baseline for reflection

The system reflects, but does not slavishly follow, the **2021 Colette Werden "Branding Vision + Strategy"** (in OneDrive `Business/Marketing Plan/`). That deck was peak-Nietzschean Neil (death metal, the dark side, gothic/blackletter, a greyscale + Crimson/Ultramarine/Yellow "three-pillar" kit, Cardo + Lexend). Since then the work turned toward **Tantrism**, so the brand matured from provocateur → contemplative scholar. The deck is treated as a **baseline for reflection, not a spec**: greyscale and the static-texture idea were kept; the gothic and the full three-colour kit were dropped.

## Palette — greyscale + one crimson

Cool greyscale foundation ("nothing is black and white; everything is grey"), with a single **crimson** accent reframed as **Śakti-red** (not Nietzschean fire). Colour is used sparingly — live-work CTAs, links, active states.

| Token | Hex | Role |
|---|---|---|
| `--bg` | `#0b0c0d` | page background (dark) |
| `--ink` | `#d8dbdd` | body text on dark |
| `--bright` | `#f2f4f5` | headings / emphasis on dark |
| `--warm` | `#b7bcbf` | secondary (cool grey) |
| `--tan` | `#9aa0a3` | tertiary (mid grey) |
| `--muted` | `#7c8286` | muted text |
| `--faint` | `#565b5e` | faint text / hairlines |
| `--crimson` | `#cc2f3d` | primary accent (Śakti) |
| `--crimson-bright` | `#e2616c` | accent text on dark / hovers |
| crimson deep | `#9e1f2a` | accent on light backgrounds |

On the **reader bots**, the layout is the **Śiva / Śakti polarity**: the chat column is dark (Śiva), the reading pane is light parchment (Śakti) — `--r-bg #e8eaeb`, `--r-ink #1c1f21`. See the `sanskrit-tantra` repo for those files.

## Typography

- **Cormorant Garamond** (serif) — wordmark, headings. Literary/contemplative.
- **Lexend** (sans, weight 300/400/500) — body and UI.
- Loaded from Google Fonts. Devanagari/other scripts fall back to system fonts (or Shobhika in the bots).

## Texture

The home page's fixed SVG grain layer doubles as the brand's "static texture" — flat at a glance, detailed on closer inspection.

## The ND mark (placeholder — not yet adopted)

A sacred-geometry monogram was designed but **shelved pending sign-off**: a straight-line **N** (Śiva) and a curved **D** (Śakti) sharing a central vertical axis (the suṣumnā), inside the bindu-circle, with a crimson bindu at centre. There are `TODO(brand mark)` placeholders in `index.html` (hero + favicon) marking where it goes if adopted.

## Applying the brand to a new surface

1. Load the fonts: `Cormorant Garamond:ital,wght@0,400;0,600;1,400` + `Lexend:wght@300;400;500`.
2. Copy the `:root` tokens; back the surface with `--bg`, text in `--ink`, headings in Cormorant.
3. Use crimson only as a signature — links, active states, a single CTA — never as a fill-everything colour.
4. For a dual reading layout, dark on the left (Śiva), light parchment on the right (Śakti).
