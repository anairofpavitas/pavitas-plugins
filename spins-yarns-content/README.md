# Pavi Spins Yarns Content Plugin

Content and craft documentation for @pavi.spins.yarns (Pavi Spins Yarns) — the crochet / fiber arts account. **Instagram only.**

Distinct from `pavitas-content` (audiobook narration brand). As of v2.0.0 this plugin also covers pattern transcription, project logging, and project tracking (absorbed from a retired predecessor plugin).

## Commands

| Command | What it does |
|---------|-------------|
| `/spins-yarns-content:weekly` | Generate this week's content drop (2 Instagram posts). Autonomous — pulls Littlebird crochet brief + Perplexity crochet trends from Notion, picks angles, drafts posts, generates Canva visual assets, and posts everything back to the Pavi Spins Yarns Notion DB as a single structured page. |
| `/spins-yarns-content:post` | Draft a single one-off Instagram post. Defers entirely to the `spins-yarns-brand-voice` skill; requires a real craft detail to anchor. Review gate before anything is posted. |
| `/spins-yarns-content:pattern` | Transcribe a crochet pattern from YouTube/web into standard written format (PDF or Notion entry), with designer attribution. |
| `/spins-yarns-content:log` | Save a pattern or project update to Notion Littlebird Log and/or the organized crochet/ folder. |
| `/spins-yarns-content:project` | Show or update active crochet project status. Queries the Littlebird Log — project state is never hardcoded. |

## Skills

- `spins-yarns-brand-voice` — Voice guide for the crochet account. Tactile, specific, dry, occasionally self-deprecating. Hashtag and length rules. Banned patterns (rhetorical-question openers, engagement-bait closers). This skill is the single source of voice truth for the brand.

## Agents

- `spins-yarns-intel` — Parallel Notion gatherer. Pulls today-dated Littlebird crochet brief and Perplexity crochet trends entries. Returns raw signal only — no angle picking, no drafting.

## Connectors

- **Notion** (via `.mcp.json`) — Pavi Spins Yarns Content DB (source + destination for `/weekly`); Littlebird Log (patterns, project logs)
- **Canva** — Used at runtime by `/weekly` to generate visual assets. Requires the Canva connector to be active in your claude.ai setup (tools surface as `mcp__claude_ai_Canva__*`).

## Source / destination DB (`/weekly`)

One Notion database, both input and output:

- **URL:** https://www.notion.so/348089eb3ccc80a19b0bd181953bdacc?v=348089eb3ccc8005a5f9000ce76c846c
- **Input:** weekly Littlebird crochet brief + Perplexity crochet trends pages (dated with the current date)
- **Output:** `Pavi Spins Yarns Weekly Content Generation [YYYY-MM-DD]` page with the week's drafted posts as structured rows

## Output format (`/weekly`)

Each run creates one Notion page. The page contains a block/table with one row per post. Columns:

`Platform | Hook | Full Caption | Alt Text | Hashtags | Visual Brief | Post Day | Visual Assets`

Page properties set on the parent page:
- **Date** → current date
- **Source** → `Claude`

## Post rules (enforced)

- Instagram only — no other platforms, no cross-posting
- Every post includes one concrete craft detail (stitch, yarn, hook size, tension note, gauge, hook hand, etc.)
- Voice: tactile, specific, dry. Occasional self-deprecation.
- No rhetorical questions as openers
- No engagement-bait closers ("which would you make?", "tell me yours below")
- Hashtags: 3–5, lowercase, clustered at end
- IG: 60–120 words

## Quality gate — do not invent

If the Littlebird crochet brief has fewer than 2 workable topics for the week, return fewer posts and flag the gap. Never invent projects, stitches, yarn choices, or progress that didn't happen. Never claim authorship of transcribed patterns.

## Install

Add to your `pavitas-plugins` marketplace. The `.mcp.json` requests the Notion connector on first run. Canva must already be connected via claude.ai for visual asset generation; if it isn't, `/weekly` will still produce drafts + visual briefs and flag that the assets weren't generated.
