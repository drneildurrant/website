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

## The Liminex Spiral — the journey-map mark (LOCKED)

The adopted mark for the **Liminex** surfaces (the Spiral IA: **Engage → Encounter → Explore → Examine**). It is not decorative: the spiral is the journey, and a single crimson dot says *where you are*. This is a deliberate reframing of the crimson signature — on this mark crimson marks **position / active state**, not a static "core."

Canonical implementation: `spiralSVG()` in `sanskrit-tantra/fred.html`. Parameters (locked):

- **Geometry** — a 3.5-turn **logarithmic** spiral. `viewBox="0 0 26 26"`, centre `(13,13)`, `rMax = 11`, growth `b = 0.11`. The gentle `b` is intentional: the textbook golden-spiral value (`b ≈ 0.30`) collapses the inner turns to sub-pixel size, so all 3.5 turns only *read* at `b ≈ 0.11`.
- **Chirality + orientation** — the figure is **mirrored** (angle = `phase − t`, not `t + phase`) and rotated by `phase = π/4 + π/18` (≈55°) so the **mouth opens to the NW** (Ganesha's protective position on the mandala). The mouth is fixed; only the dot moves between stations.
- **The line** — `stroke: var(--muted)`, `stroke-width: 0.8`, round caps. Fine but sharp.
- **The four stations** — placed by compass bearing + which coil (turn, counted in from the mouth):

  | # | Station | Invitation | Call | Bearing | Coil |
  |---|---|---|---|---|---|
  | 0 | Engage | *cross the threshold* | Find your tribe | N | turn 1 |
  | 1 | Encounter | *come inside* | Choose your Encounter | SW | turn 1 |
  | 2 | Explore | *look further* | Find your heritage | E | turn 2 |
  | 3 | Examine | *you've arrived* | Plumb the depths ‡ | — | the core (centre) |

  Each station surface carries a **three-part header lockup** — implemented on Encounter, the
  template for the rest:
  - **eyebrow** — the STATION name (e.g. "ENCOUNTER"), mono uppercase.
  - **invitation** — the line beneath it: the visitor's movement/state. Read down the column it
    is a deliberate progression: *cross the threshold → come inside → look further → you've arrived.*
  - **call** — the imperative heading in the body: what the station offers (its CTA).

  Invitation and call are per-station and must not be swapped. Note the noun "*the threshold*" is
  the **brand** line ("Liminex · the threshold", *limen* = the product's name); Engage's invitation
  is the verb form, "*cross the threshold*". ‡ Examine's call is **provisional** — "Plumb the depths"
  vs. a "Find your …" parallel (e.g. "Find your ground"); to be locked when Examine is designed.

  Each station is an **empty grey holder** — `fill: var(--bg)`, `stroke: var(--faint)`, `stroke-width: 0.5`. The station for the **current page** is filled solid `var(--crimson)` ("you are here"). Exactly one dot is crimson per page; the rest stay holders. Dot radii taper inward: `[1.05, 0.92, 0.8, 0.9]`.

- **Sizing** — 48px in a page header lockup (≈1.2× the two-line wordmark height). Scales by the SVG `width`/`height`; `viewBox` is fixed at 26.

The same `spiralSVG` should be **lifted into one shared file** as each Liminex page ships; per-page each surface declares only its active station index (`ACTIVE`). This is a different mark from the shelved ND monogram below — the Spiral is the Liminex journey-map; the ND monogram remains a separate, unadopted neildurrant.com identity option.

## Applying the brand to a new surface

1. Load the fonts: `Cormorant Garamond:ital,wght@0,400;0,600;1,400` + `Lexend:wght@300;400;500`.
2. Copy the `:root` tokens; back the surface with `--bg`, text in `--ink`, headings in Cormorant.
3. Use crimson only as a signature — links, active states, a single CTA — never as a fill-everything colour.
4. For a dual reading layout, dark on the left (Śiva), light parchment on the right (Śakti).
