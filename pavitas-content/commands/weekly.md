---
description: Generate this week's Pavitas Productions content. Pulls Littlebird digest + Perplexity brief + active projects from Notion, picks the strongest angles, drafts one image/carousel post (IG+FB) and one short-form video script (TikTok+YT Shorts), and posts both as rows in the Pavitas Content database. Autonomous — no review step. Visual brief only, no Canva generation.
---

# Pavitas Weekly Content Generation

Fully autonomous. Gather → pick → draft → post. No intermediate review. Flag problems, don't pause for permission.

## Phase 1 — Gather

Spawn the `content-intel` agent. It returns a structured brief with:
- Littlebird Pavitas digest (from Pavitas Content DB, this week)
- Perplexity industry brief (from same DB, this week)
- Active Audiobook Projects status
- Recent Littlebird Log signal (past 14 days)
- Upcoming releases
- Flagged moments

If the agent flags a missing input (no digest or no brief for this week), continue anyway — use what's available. Do not block on missing inputs.

## Phase 2 — Pick angles

Load the `pavitas-brand-voice` skill. Apply the angle hierarchy:

1. Active project / release / recording update
2. Craft reflection (narration, Story Grid, improv, singing, acting)
3. Author friend / publisher work to amplify
4. LitRPG/genre industry moment
5. Personal, filtered through "person behind the voice"

Pick **two distinct angles** for the two pieces — don't double up. Prefer higher-tier angles when the signal supports them.

**Angle pairing logic:**
- If there's a live release or recording update, that's almost always Piece 1 (image/carousel).
- Craft reflection usually works better as short-form video (it's a thinking-out-loud format).
- Personal angles can work either format — pick based on what the visual/video needs are.

**Quality gate:** If only one angle meets the bar, produce one piece. If zero meet the bar, produce zero and explain why. Don't pad.

## Phase 3 — Draft

### Piece 1: Image/Carousel post (IG + FB, same copy)

Format:
- **Hook** — first line (grabs scroll, under 10 words ideal)
- **Caption** — 100–180 words, first person, dry, specific
- **Alt text** — always include, describe image for screen readers
- **Hashtags** — 3–6, clustered at end
- **Visual brief** — describe what the asset should show (text description, no generation). Call out if carousel (2–6 slides) vs single image. Specify text overlays if any.

### Piece 2: Short-form video script (TikTok + YT Shorts, same video)

Format:
- **Hook: 1.5 seconds** — visual + spoken. Thumb-stopping.
- **Beats: 15–45 seconds total** — numbered (1, 2, 3...)
- **On-screen text callouts** — explicitly marked per beat
- **Closing beat** — not "follow for more." Leave the thought.
- **Video brief** — what's on camera per beat (booth? product? B-roll?), audio treatment notes

### Brand voice non-negotiables (from pavitas-brand-voice skill)
- No AI narration mentions (positive, negative, neutral — none)
- No "honored to announce," "journey," "passion project," "dream role"
- No "delve," "landscape," "navigate" as metaphor
- First person, dry, specific, genre-literate
- One concrete detail per post minimum
- Credit author + publisher + release date accurately
- Never post embargoed work

## Phase 4 — Post to Notion

**Target DB:** https://www.notion.so/eb0089eb3ccc83928e5c017c1f66a70c?v=702089eb3ccc82f4a2d2080fa27c25c1

Create **ONE parent page** titled:
```
Pavitas Content Generation [YYYY-MM-DD]
```

Set properties:
- **Date** field → today's date (use `date` command via bash if unsure)
- **Source** field → "Claude"

Inside the parent page, create a table/database with rows for each piece. Columns:

| Content Type | Platforms | Hook | Body | Visual/Video Brief | Hashtags | Notes for SM Manager | Visual Assets |

**Row 1 (image/carousel):**
- Content Type: `Image/Carousel`
- Platforms: `Instagram, Facebook`
- Hook: [hook line]
- Body: [full caption + alt text]
- Visual/Video Brief: [what asset should show, # of slides if carousel]
- Hashtags: [3–6 tags]
- Notes for SM Manager: [posting timing suggestion, any credit/tag requirements, release-date constraints]
- Visual Assets: `[To be created in Canva — see Visual Brief]`

**Row 2 (short-form video):**
- Content Type: `Short-form Video`
- Platforms: `TikTok, YouTube Shorts`
- Hook: [hook beat — visual + spoken, 1.5s]
- Body: [full numbered beat breakdown with on-screen text]
- Visual/Video Brief: [per-beat shot description, audio notes]
- Hashtags: [3–6 tags]
- Notes for SM Manager: [shoot timing, any props/setup needed, release-date constraints]
- Visual Assets: `[To be recorded — see Video Brief]`

If producing only one piece, include one row and add a second block titled "Why only one piece this week" with a one-sentence explanation.

## Phase 5 — Report back

After posting, return a one-screen summary to Pavi:
- Notion page URL
- Angle 1 (one sentence)
- Angle 2 (one sentence)
- Any flagged issues (missing inputs, release-date risks, author/publisher credits that need verification)

No postamble. No "Let me know if you need changes."

## Hard rules (enforced at every phase)

- Never mention AI narration in any form
- Never claim endorsement not given
- Never post embargoed work
- Credit author + publisher + release date accurately — if uncertain, flag for Pavi
- Quality over cadence — one strong piece beats two weak ones
