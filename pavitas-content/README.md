# Pavitas Content Plugin

Weekly social content angle briefs for Pavitas Productions — audiobook narration work, craft reflection, LitRPG/progression/sci-fi genre presence.

Distinct from `spins-yarns-content` (which handles @pavi.spins.yarns, the crochet side).

**This plugin does not write copy.** It surfaces the angles worth writing about and hands over the verified facts behind each one. A human professional writes the hooks, captions, hashtags, and scripts.

## Commands

| Command | What it does |
|---------|-------------|
| `/pavitas-content:weekly` | Build this week's angle brief. Autonomous — pulls inputs from Notion, picks every angle that clears the bar, documents the source material, and posts to the Pavitas Content DB in one pass. |

## Skills (reusable across future commands)

- `pavitas-brand-voice` — Voice guide. Genre-literate, dry, first-person, craft-forward. Banned phrases, hard rules, angle hierarchy, format specs. Within `/weekly` it governs only whether an angle is on-brand, not how anything gets written.

## Agents

- `content-intel` — Parallel Notion gatherer. Pulls Littlebird digest, Perplexity brief, Audiobook Projects status, recent Littlebird Log signal.

## Connectors

- **Notion** — Pavitas Content DB (source + destination), Audiobook Projects DB, Littlebird Log DB

## Source/destination DB

Single Notion database serves as both input source and output destination:

- **Input:** weekly Littlebird Pavitas digest + Perplexity industry brief entries
- **Output:** `Pavitas Angle Brief [YYYY-MM-DD]` pages with one row per angle

URL: https://www.notion.so/eb0089eb3ccc83928e5c017c1f66a70c

## Output format

Each run creates one Notion page with a table of angle rows. Columns:

| Angle | Tier | Why now | Source material | Constraints & credits | Confidence |

`Tier` maps to the angle hierarchy (1 = active project/release, 5 = personal). `Source material` carries the facts a writer can't derive alone — titles, authors, publishers, release dates, specific moments. `Constraints & credits` carries embargo dates, required tags, and handles. `Confidence` flags anything unverified.

No format or platform is prescribed. That call belongs to the writer.

## Quality gate

An angle clears the bar when it has a reason to exist this week and at least one concrete, verifiable detail behind it. There's no target number of angles — the skill surfaces every one that qualifies and pads nothing. Zero is a valid week.

## Hard rules (non-negotiable)

- Never claim endorsement not given
- Never surface embargoed work
- Credit author + publisher + release date accurately — if uncertain, flag it
- No copy. A hook, caption, hashtag, or script line in the output means something went wrong.

## Install

Add to your `pavitas-plugins` marketplace. The `.mcp.json` requests the Notion connector — you'll be prompted to approve on first run if not already connected.
