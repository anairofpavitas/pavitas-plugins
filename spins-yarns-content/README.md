# Spins Yarns Content Plugin

Weekly social content generation for @pavi.spins.yarns (Spinning Yarns with Pavi) — the crochet / fiber arts account.

Distinct from `pavitas-content` (audiobook narration brand) and from the older `fiber-arts-content` plugin (pattern transcription, project logs, one-off drafts). This plugin is the **weekly automated drop**: gather inputs → pick angles → draft → generate visuals in Canva → post to Notion.

## Commands

| Command | What it does |
|---------|-------------|
| `/spins-yarns-content:weekly` | Generate this week's content drop (2 Instagram posts + 1 Threads post). Autonomous — pulls Littlebird crochet brief + Perplexity crochet trends from Notion, picks angles, drafts posts, generates Canva visual assets, and posts everything back to the Spinning Yarns Notion DB as a single structured page. |

## Skills

- `spins-yarns-brand-voice` — Voice guide for the crochet account. Tactile, specific, dry, occasionally self-deprecating. Hashtag and length rules. Banned patterns (rhetorical-question openers, engagement-bait closers).

## Agents

- `spins-yarns-intel` — Parallel Notion gatherer. Pulls today-dated Littlebird crochet brief and Perplexity crochet trends entries. Returns raw signal only — no angle picking, no drafting.

## Connectors

- **Notion** (via `.mcp.json`) — Spinning Yarns Content DB (source + destination)
- **Canva** — Used at runtime to generate visual assets. Requires the Canva connector to be active in your claude.ai setup (tools surface as `mcp__claude_ai_Canva__*`).

## Source / destination DB

One Notion database, both input and output:

- **URL:** https://www.notion.so/348089eb3ccc80a19b0bd181953bdacc?v=348089eb3ccc8005a5f9000ce76c846c
- **Input:** weekly Littlebird crochet brief + Perplexity crochet trends pages (dated with the current date)
- **Output:** `Pavi Spins Yarns Weekly Content Generation [YYYY-MM-DD]` page with the week's drafted posts as structured rows

## Output format

Each run creates one Notion page. The page contains a block/table with one row per post. Columns:

`Platform | Hook | Full Caption | Alt Text | Hashtags | Visual Brief | Post Day | Visual Assets`

Page properties set on the parent page:
- **Date** → current date
- **Source** → `Claude`

## Post rules (enforced)

- Every post includes one concrete craft detail (stitch, yarn, hook size, tension note, gauge, hook hand, etc.)
- Voice: tactile, specific, dry. Occasional self-deprecation.
- No rhetorical questions as openers
- No engagement-bait closers ("which would you make?", "tell me yours below")
- Hashtags: 3–5, lowercase, clustered at end
- IG: 60–120 words. Threads: one post, under 300 characters.

## Quality gate — do not invent projects

If the Littlebird crochet brief has fewer than 3 workable topics for the week, return fewer posts and flag the gap. Never invent projects, stitches, yarn choices, or progress that didn't happen.

## Install

Add to your `pavitas-plugins` marketplace. The `.mcp.json` requests the Notion connector on first run. Canva must already be connected via claude.ai for visual asset generation; if it isn't, the command will still produce drafts + visual briefs and flag that the assets weren't generated.
