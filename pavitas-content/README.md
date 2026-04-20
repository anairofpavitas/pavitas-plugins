# Pavitas Content Plugin

Weekly social content generation for Pavitas Productions — audiobook narration work, craft reflection, LitRPG/progression/sci-fi genre presence.

Distinct from `fiber-arts-content` (which handles @pavi.spins.yarns, the crochet side).

## Commands

| Command | What it does |
|---------|-------------|
| `/pavitas-content:weekly` | Generate this week's content (1 image/carousel post + 1 short-form video script). Autonomous — pulls inputs from Notion, picks angles, drafts, and posts to the Pavitas Content DB in one pass. |

## Skills (reusable across future commands)

- `pavitas-brand-voice` — Voice guide. Genre-literate, dry, first-person, craft-forward. Banned phrases, hard rules, angle hierarchy, format specs.

## Agents

- `content-intel` — Parallel Notion gatherer. Pulls Littlebird digest, Perplexity brief, Audiobook Projects status, recent Littlebird Log signal.

## Connectors

- **Notion** — Pavitas Content DB (source + destination), Audiobook Projects DB, Littlebird Log DB

## Source/destination DB

Single Notion database serves as both input source and output destination:
- **Input:** weekly Littlebird Pavitas digest + Perplexity industry brief entries
- **Output:** `Pavitas Content Generation [YYYY-MM-DD]` pages with generated content rows

URL: https://www.notion.so/eb0089eb3ccc83928e5c017c1f66a70c

## Output format

Each run creates one Notion page with a table of content rows. Columns:
Content Type | Platforms | Hook | Body | Visual/Video Brief | Hashtags | Notes for SM Manager | Visual Assets

Visual assets are described as text briefs only — no Canva generation. Intended for a future Claude design package to reference.

## Quality gate

If the week's inputs don't produce two strong pieces, produces one. If nothing meets the bar, produces zero and explains why. Quality over cadence.

## Hard rules (non-negotiable)

- Never mention, endorse, compare, or critique AI narration
- Never claim endorsement not given
- Never post embargoed work
- Credit author + publisher + release date accurately
- Never use: "honored to announce," "journey," "passion project," "dream role," "delve," "landscape" or "navigate" as metaphors

## Install

Add to your `pavitas-plugins` marketplace. The `.mcp.json` requests the Notion connector — you'll be prompted to approve on first run if not already connected.
