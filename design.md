# Design system — Data Guy Story (locked by the Hallmark full redesign, PR #24)

This file locks the system every page on the site shares. Pages differ only in
shape. A page that needs something outside this file gets the file updated
first, not a one-off override.

## Brand (kept, from pre-flight)

- Tree logo (`images/logo.svg`), deep green accent `#0d766d` /
  `#075e57`, ink `#182b36`, muted `#526672`, surface `#f5faf8`,
  border `#d9e8e3`. Dark mode mirrors in `assets/css/custom.css`
  (`:root` / `.dark` blocks).
- Type: Hextra's faces as found (no new webfont). Display weight 750,
  letter-spacing tight on heads only. No tracked-caps labels anywhere
  (gate 67): labels are the body face, a step smaller, sentence case,
  untracked.
- Voice: Calvin's own words, Vietnamese, first-person. Copy changes only
  when a gate names them, and are listed in the PR body.

## Tokens

All colours and fonts go through `:root` tokens in `assets/css/custom.css`
(existing `--dgs-*` set, plus `--dgs2-*` for the homepage). No literal colour
or `font-family` past a token block. New site-wide rules live in the
"Hallmark whole-site" block at the end of `custom.css`, scoped so they never
restyle a single page by accident.

## Chrome (Hextra-owned structure, site-owned skin)

- Navbar, search, sidebar, TOC, footer: structure stays Hextra's; the skin
  is `custom.css` only, except where a gate forces a template override
  (decorative SVGs get `aria-hidden="true"` via overridden partials).
- Search field edge meets 3:1 (muted border). Theme toggle is a 44px hit
  target. Shortcut hints are 11px or more. `prefers-reduced-motion` kills
  theme transitions site-wide. `overflow-x: clip` on `html` and `body`.
  Disabled controls have a visible style.

## Page patterns

- **Hero (Settled):** headline, one sentence, actions — and the hero fills
  its screen (gates 44c/44d/79). The homepage hero is a poster greeting;
  hub pages open with their lead, not a wall of cards.
- **Doors:** one tint band (`--dgs-surface`), not a row of identical cards.
  Sections inside a band are split by hairlines, never by bordered cards.
- **Links:** underlined verb labels. Never an arrow glued to a link
  (gate 63), never a bare arrow as a link, never an emoji as an icon
  (gate 30a).
- **Rows:** notes, blog and bottom-of-page items are hairline rows, not
  cards. Grids never orphan one item on the last row (gate F20): an odd
  last card spans the full width.
- **Hubs:** a hub page is a lead, its doors, then its lists. Lists keep
  every word; only their markers change (no arrow prefixes).
- **Articles:** prose width stays capped (wiki 52rem). Article templates
  are Hextra's; only the skin and the gates above apply.

## What this system does not cover

- Hextra's compiled Tailwind utilities (gates 48, 74): tokenising the
  theme's own palette is a theme fork, not a redesign. Listed as remaining.
- `/docs/` (the v1 "Sổ tay"): NOT deleted in this redesign — retiring it
  is a content decision, so it is proposed in the PR body with a redirect
  map, not executed.

## Verification

- Production Hugo build (`hugo --gc --minify`, Hugo 0.156.0 + Go 1.26).
- `sloplint` render pass on the built homepage and hub pages; static pass
  on the built site. Homepage-scoped gates are clean; theme-utility gates
  above are the known remainder.
