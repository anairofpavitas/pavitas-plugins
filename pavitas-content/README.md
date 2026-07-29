# Pavitas Content Plugin

Weekly social content angle briefs for Pavitas Productions — audiobook narration work, craft reflection, LitRPG/progression/sci-fi genre presence.

Distinct from `spins-yarns-content` (which handles @pavi.spins.yarns, the crochet side).

**This plugin does not write copy.** It surfaces the angles worth writing about and hands over the verified facts behind each one. A human professional writes the hooks, captions, hashtags, and scripts.

## Commands

| Command | What it does |
|---------|-------------|
| `/pavitas-content:weekly` | Build this week's angle brief. Autonomous — pulls inputs from Notion, picks every angle that clears the bar, documents the source material, and posts to the Pavitas Content DB in one pass. |

## Skills (reusable across future commands)

- `pavitas-brand-voice` — Perspective and angle guide. Governs where Pavi is standing when a topic is chosen (practitioner not commentator, standing before opinion, audience already inside the genre), the specificity floor every angle has to clear, six connection patterns for finding what's worth saying, privacy exclusions, source-conflict handling, and a required verification pass. It does not govern word choice, phrasing, or format — a human writer owns all of that.

## Agents

- `content-intel` — Parallel Notion gatherer. Pulls Littlebird digest, Perplexity brief, Audiobook Projects status, recent Littlebird Log signal. Returns every item with its page title, URL, and date so angles can be cited without re-querying. Surfaces source conflicts without resolving them, quarantines privacy-flagged entries, and reports raw recurrence across the window.

## Connectors

- **Notion** — Pavitas Content DB (source + destination), Audiobook Projects DB, Littlebird Log DB

## Source/destination DB

Single Notion database serves as both input source and output destination:

- **Input:** weekly Littlebird Pavitas digest + Perplexity industry brief entries
- **Output:** `Pavitas Angle Brief [YYYY-MM-DD]` pages with one row per angle

URL: https://www.notion.so/eb0089eb3ccc83928e5c017c1f66a70c

## Output format

Each run creates one Notion page with a table of angle rows. Columns:

| Angle | Pattern | Why now | Anchor & source material | Constraints & credits | Open questions | Confidence |

`Pattern` is how the angle was found — Collision (industry signal against Pavi's week), Recurrence (same idea twice inside 14 days), Transfer (a principle from one discipline explaining another), Timing, Lineage (this book's decision traceable to an earlier one), Absence, or Single-source. Rows are ordered by connection scarcity, strongest first. `Anchor & source material` leads with the one concrete detail that makes the angle exist, then the supporting facts and citations. `Constraints & credits` carries embargo dates, required tags, handles, unresolved source conflicts, and privacy splits. `Open questions` is what the writer needs to ask Pavi. `Confidence` reports verification status.

No format or platform is prescribed. That call belongs to the writer.

## Quality gate

An angle clears the bar when it has a reason to exist this week and one concrete anchor behind it — a named book, a specific line, a dated session, a decision with a before and after, a number, a mistake. There's no target number of angles — the skill surfaces every one that qualifies and pads nothing. Zero is a valid week.

Every brief goes through a verification pass before posting, run by a subagent that didn't build it: URLs resolve, every number and quote traces to a cited source, inference is labeled, status claims match the most recent source, conflicts are surfaced rather than silently resolved.

## Hard rules (non-negotiable)

- Never claim endorsement not given
- Never surface embargoed work
- Credit author + publisher + release date accurately — if uncertain, flag it
- Privacy: nothing flagged private, no health or medical content, no relationship or therapy content, no third-party private information, no financial specifics. Outranks angle strength.
- Never invent an anchor, quote, date, or source
- No copy. A hook, caption, hashtag, or script line in the output means something went wrong.

## Install

Add to your `pavitas-plugins` marketplace. The `.mcp.json` requests the Notion connector — you'll be prompted to approve on first run if not already connected.
