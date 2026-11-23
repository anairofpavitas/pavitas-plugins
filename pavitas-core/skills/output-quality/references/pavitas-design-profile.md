# Pavitas design profile

The house look for anything Claude makes for Pavi or for Pavitas Productions.
Source of truth: the **Pavitas Productions Design System** on Claude Design
(claude.ai artifact `6kHUcd2HYBdPiqGk9ShNE1`, moved from Claude Design Nov 9, 2026).
When this file and that artifact disagree, the artifact wins. Read its
`project/README.md` and `project/colors_and_type.css` for anything not here.

## Two modes

| | Brand-facing | Personal working pages |
|---|---|---|
| What | Website pieces, client one-sheets, invoices, contracts, decks for publishers or authors | Pages, docs and dashboards made for Pavi himself (time maps, checklists, boards, trip docs) |
| Emoji | None. Bold words and the coral accent carry emphasis | Yes, a few, as section markers. Pavi asked for flair on Nov 10: "little images, emojis, color… easier to care about" |
| Themes | Light only (parchment). No full-page dark slate | Light and dark. Dark uses the ink scale (see below) |
| Imagery | Cinematic fantasy key art or a warm gradient placeholder. No stock photos | Small inline SVG marks, icons, badges. No stock photos |

Both modes use the same palette, type and motifs.

## Palette

| Token | Hex | Job |
|---|---|---|
| Ink | `#394851` | Primary. Text, primary buttons, brand mark |
| Stone | `#c7bca2` | Secondary buttons, quiet surfaces, badge fill |
| Parchment | `#f7f4eb` | Main light surface |
| Coral | `#e66b5e` | The one pop per screen: active underline, a tag, a focus ring, one hero flourish |
| Rust | `#793e2d` | Editorial emphasis: pull quotes, rules, drop caps |
| Olive | `#666441` | Foliage accent, tags |
| Oxblood | `#62403d` | Links, quieter emphasis |

Rule of thirds: ink + stone + parchment are about 95% of pixels. Coral in small
doses, never a coral wall and never a coral primary button. Rust, olive and
oxblood are seasoning.

Tonal steps: ink 900 `#1f2830`, 800 `#2b3740`, 600 `#4c5c66`, 500 `#6a7780`,
300 `#b8bfc5`, 100 `#ebeef0`. Parchment 50 `#fbf9f2`, 200 `#efeadc`, 300 `#e4ddca`.
Stone 100 `#e3dcc9`, 400 `#b0a487`, 500 `#908365`.
Status, muted: ok `#5c6e3b`, warn `#a6763a`, danger = rust, info `#4a5f6e`.

**Dark mode (personal pages only):** background ink 900, raised surfaces ink 800,
text parchment 100, secondary text ink 300, rules stone 500 at low opacity.
Coral and stone stay as they are; lift rust to `#c0745c` and olive to `#a7a46e`
so they read on dark.

## Type

- **Mrs Eaves everywhere** (licensed TTFs live in the design system artifact).
  Display and H2: Mrs Eaves Smart Ligatures *Italic*. H3: Mrs Eaves Italic or Bold.
  Body: Mrs Eaves Roman, 17–18px, line-height about 1.6. Labels, nav, buttons:
  Mrs Eaves Small Caps, uppercase, tracking 0.08em.
- **On claude.ai pages** only Google Fonts load. Use the profile's own fallback,
  **Libre Baskerville** (with Georgia behind it); keep the italic-display,
  small-caps-label rhythm.
- In .docx/.pdf use Mrs Eaves if installed, else Baskerville, else Georgia.
- Scale (minor third): 12, 14, 17, 19, 22, 28, 36, 48, 64, 88.

## Shape and depth

- Radius 4–6px on cards and buttons. Only the logo badge is a circle. No pills.
- Flat. Shadows barely there (`0 1px 2px rgba(57,72,81,.08)`). No glass, no blur.
- Spacing on a 4px base: 4, 8, 12, 16, 24, 32, 48, 64, 96.
- Motion: fades and a gentle reveal, 140–220ms. No parallax or springs.
- Focus: always visible, a 3px coral-tinted ring.

## Signature moves

- **Torn-paper edge** between sections (SVGs in the artifact's `project/assets/`).
  The single most recognizable move. One or two per page, not every section.
- **Three-column blocks**: three promises, three stats, three cards.
- **Big number, small-caps label** for stats.
- **Strikethrough hook** ("Get Lost ~~FOUND~~…"), brand-facing copy only, rarely.
- Buttons: ink primary, stone secondary, ink with a 3px coral underline for the one
  button that should pop.
- Icons: filled shapes (Phosphor Fill is the stand-in), ink on parchment. Never coral.

## Quick token block for a claude.ai page

```css
:root{--bg:#f7f4eb;--surface:#fbf9f2;--sunk:#efeadc;--fg:#394851;--fg2:#6a7780;
--stone:#c7bca2;--coral:#e66b5e;--rust:#793e2d;--olive:#666441;--oxblood:#62403d;
--rule:rgba(57,72,81,.14)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#1f2830;
--surface:#2b3740;--sunk:#263039;--fg:#f7f4eb;--fg2:#b8bfc5;--rust:#c0745c;
--olive:#a7a46e;--oxblood:#d49a8f;--rule:rgba(247,244,235,.14);color-scheme:dark}}
:root[data-theme="dark"]{/* same dark values */}
```
