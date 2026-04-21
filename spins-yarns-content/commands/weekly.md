---
description: Generate this week's @pavi.spins.yarns content drop. Pulls today-dated Littlebird crochet brief + Perplexity crochet trends from the Pavi Spins Yarns Notion DB, drafts 2 Instagram posts + 1 Threads post, generates visual assets in Canva, and posts everything back to Notion as one structured page. Autonomous — no intermediate review step. Never invents projects; if fewer than 3 workable topics exist, produces fewer posts and flags the gap.
---

# Pavi Spins Yarns Weekly Content Generation

Fully autonomous. Gather → pick → draft → generate visuals → post → report. Flag problems, don't pause for permission. Quality over cadence — never fabricate craft details.

## Phase 1 — Gather

Spawn the `spins-yarns-intel` agent. It returns a structured brief with:
- Littlebird crochet brief (today-dated, from Pavi Spins Yarns Content DB)
- Perplexity crochet trends (today-dated, from same DB)
- Workable topic inventory + count

**If the agent flags `⚠️ Missing: Littlebird crochet brief`**: stop and report back to Pavi. The Littlebird brief is the only source of truth for actual projects / stitches / yarn this week — without it, we can't produce content without inventing. Say so. Don't guess.

**If the agent flags `⚠️ Missing: Perplexity crochet trends`**: continue anyway. The trends brief is nice-to-have; Littlebird is load-bearing.

## Phase 2 — Pick angles

Load the `spins-yarns-brand-voice` skill. Apply its angle hierarchy:

1. Active project update (specific stitch / tension / modification on a real, named project)
2. Technique spotlight (stitch behavior, gauge observation, hook-hand note)
3. Frog / fail / course-correction
4. Material note (yarn behavior, hook ergonomics)
5. Trend-adjacent commentary — only if Perplexity surfaced something AND Littlebird provides the craft anchor

### Post count decision (do not invent)

- **Workable topics ≥ 3** → produce 2 Instagram posts + 1 Threads post (3 total, 3 distinct angles).
- **Workable topics = 2** → produce 2 posts total (1 IG + 1 Threads, OR 2 IG), picking the two strongest. Flag the gap in the output.
- **Workable topics = 1** → produce 1 post, pick the best-fit platform. Flag the gap.
- **Workable topics = 0** → produce zero posts. Report why. Done.

Never pad. A thin post costs more than a skipped slot.

### Platform pairing logic

- **Process / WIP / swatch content** → Instagram (carries the image weight, needs the 60–120 word breathing room for tactile description).
- **Dry one-liner observations, frog moments, trend commentary** → Threads (the compressed 300-char format rewards the punchline).
- Pick distinct angles per post — don't double up on the same stitch / project / moment.

### Post day assignment

Assign a target post day for each piece within the week. Default rhythm:
- IG #1 → early week (Mon/Tue)
- Threads → mid week (Wed)
- IG #2 → late week (Fri/Sat)

Adjust if an input flags a time-sensitive moment.

## Phase 3 — Draft

Draft each post strictly per the `spins-yarns-brand-voice` skill specs.

### Instagram post format
- **Hook** — first line, observational, under 12 words, no rhetorical question
- **Full caption** — 60–120 words total, tactile / specific / dry, one concrete craft detail minimum
- **Alt text** — always include, plain description for screen readers
- **Hashtags** — 3–5, lowercase, clustered at end as one block
- **Visual brief** — text description of what the image/carousel should show; call out single image vs. 2–6 slide carousel; specify any text overlays
- **Post day** — assigned above

### Threads post format
- **Full post** — single post, under 300 characters *including* hashtags and spaces. Count before finalizing.
- **Hook** — the first sentence; record it separately too for the Notion table
- **Hashtags** — 3–5, lowercase, clustered at end, counted in the 300-char budget
- **Alt text** — if the Threads post includes an image, include alt text; otherwise `N/A`
- **Visual brief** — image concept if applicable; otherwise `Text-only post`
- **Post day** — assigned above

### Voice non-negotiables (from spins-yarns-brand-voice skill)
- Tactile, specific, dry. Occasional self-deprecation (one beat per post max).
- No rhetorical questions as openers. No engagement-bait closers.
- One concrete craft detail per post, minimum (stitch / yarn / hook / tension / gauge / row count).
- Never invent projects, stitches, yarn, or progress.
- Never mention AI narration, AI-generated patterns, or AI-generated imagery.
- Credit any pattern not Pavi's own; never show in-progress paid-pattern work others can't access.

## Phase 4 — Generate visual assets in Canva

For each post that needs a visual (typically both IG posts; Threads optional):

1. Confirm the Canva connector is available (tools under `mcp__claude_ai_Canva__*`).
2. Use the visual brief as the design prompt. Specify:
   - Format: IG square (1080×1080) or carousel (2–6 slides, 1080×1350 or 1080×1080)
   - Text overlays if any (exact copy from the brief)
   - Any brand elements (Pavi Spins Yarns wordmark if available in assets)
3. Generate the design (e.g. `generate-design` or `generate-design-structured`), then export it (`export-design`) to a shareable format.
4. Capture the Canva design URL and/or export URL — both go into the Notion row under "Visual Assets".

**If Canva is not connected or generation fails:**
- Do not block the run. Produce the drafts and visual briefs anyway.
- Mark "Visual Assets" as `⚠️ Canva not available — see Visual Brief to generate manually` and flag it in the Phase 6 report.

## Phase 5 — Post to Notion

**Target DB:** https://www.notion.so/348089eb3ccc80a19b0bd181953bdacc?v=348089eb3ccc8005a5f9000ce76c846c

### Create the parent page

Title:
```
Pavi Spins Yarns Weekly Content Generation [YYYY-MM-DD]
```

Set properties:
- **Date** → today's date (use `date +%Y-%m-%d` via bash if unsure)
- **Source** → `Claude`

### Inside the parent page — add content rows

Create a table (or structured block) with one row per post. Columns:

| Platform | Hook | Full Caption | Alt Text | Hashtags | Visual Brief | Post Day | Visual Assets |

**Example row (Instagram):**
- Platform: `Instagram`
- Hook: *[first line of caption]*
- Full Caption: *[60–120 word caption, plain text]*
- Alt Text: *[screen-reader description]*
- Hashtags: *[3–5 lowercase hashtags, space-separated]*
- Visual Brief: *[carousel 3 slides, overlays: "Row 12 came out twice"; etc.]*
- Post Day: *[e.g. Tuesday]*
- Visual Assets: *[Canva design URL + export URL, or `⚠️ Canva not available — see Visual Brief`]*

**Example row (Threads):**
- Platform: `Threads`
- Hook: *[first sentence of post]*
- Full Caption: *[full post under 300 chars, including hashtags]*
- Alt Text: `N/A` or description if image included
- Hashtags: *[3–5 lowercase, already counted in the 300-char body]*
- Visual Brief: `Text-only post` or image concept
- Post Day: *[e.g. Wednesday]*
- Visual Assets: *[Canva URL if generated, or `N/A`]*

### If producing fewer than 3 posts

Include only the rows that were produced. Add a clearly-marked note block beneath the table:

```
⚠️ Gap report
- Requested cadence: 2 IG + 1 Threads (3 posts)
- Produced: [N] posts
- Reason: [e.g. Littlebird brief surfaced only 1 workable topic — "offset cardigan sleeve cap frog". Rest of week's sessions lacked concrete craft detail to anchor a post.]
```

## Phase 6 — Report back

After posting, return a one-screen summary to Pavi via SendUserMessage:

- Notion page URL
- Post count produced (e.g. `2 IG + 1 Threads` or `1 IG only — gap flagged`)
- Angle summary per post (one line each: platform + craft detail + post day)
- Canva status: `all assets generated` / `N of M generated` / `Canva not available — briefs only`
- Any flagged issues: missing Perplexity brief, low topic count, credit verifications needed, etc.

No postamble. No "Let me know if you need changes."

## Hard rules (enforced at every phase)

- **Never invent projects, stitches, yarn, hooks, tensions, or progress.** The Littlebird brief is the only source of truth.
- **Never mention AI narration** or AI-generated fiber-arts content of any kind.
- **Never credit Pavi** for a pattern transcribed or adapted from another designer.
- **Never post in-progress work** from paid patterns others can't access.
- **Quality over cadence.** 1 real post beats 3 fabricated ones. 0 posts beats 1 fake one.
- **Hashtag rules are non-negotiable:** 3–5, lowercase, clustered at end, counted in char/word budgets.
