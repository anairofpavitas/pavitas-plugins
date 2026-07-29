---
description: Build this week's Pavitas Productions angle brief. Pulls Littlebird digest + Perplexity brief + active projects from Notion, picks every angle that clears the bar, and posts them as rows in the Pavitas Content database with verified source material. Autonomous — no review step. Angles and facts only; a human writer owns all copy.
---

# Pavitas Weekly Angle Brief

Fully autonomous. Gather → pick → document → post. No intermediate review. Flag problems, don't pause for permission.

**This skill does not write copy.** No hooks, captions, hashtags, scripts, beats, or on-screen text. A human professional writes all of that. The job here is to surface the angles worth writing about and hand over the verified material behind each one.

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

Load the `pavitas-brand-voice` skill. It governs whether an angle is on-brand — not how anything gets written.

Apply the angle hierarchy:

1. Active project / release / recording update
2. Craft reflection (narration, Story Grid, improv, singing, acting)
3. Author friend / publisher work to amplify
4. LitRPG/genre industry moment
5. Personal, filtered through "person behind the voice"

Pick **every angle that clears the bar.** There is no target number. Prefer higher-tier angles when the signal supports them, and keep angles distinct — don't file the same story twice under different framings.

**Quality gate:** An angle clears the bar when it has a reason to exist this week and at least one concrete, verifiable detail behind it. Anything that fails either test doesn't go in. Zero qualifying angles is a valid outcome — say so and explain why. Never pad to hit a count.

## Phase 3 — Build the angle brief

For each angle that cleared the gate, document six fields. Facts only.

- **Angle** — one sentence. What this post is about.
- **Tier** — which level of the hierarchy above it came from (1–5).
- **Why now** — why this week and not next. The timeliness argument.
- **Source material** — the verified facts a writer can't derive alone: title, author, publisher, release date, narration details, chapter or hour counts, specific moments, links.
- **Constraints & credits** — embargo dates, who must be tagged, handles, release-date gates, anything that would be an error if gotten wrong.
- **Confidence** — flag anything unverified so it gets checked before it goes out. If nothing is uncertain, say "verified."

Do not suggest a format, platform, or asset treatment. That's the writer's call.

Two rules survive from the old draft phase, as facts rather than style:

- Every angle carries at least one concrete, verifiable detail.
- Credits are accurate — author, publisher, release date. If uncertain, flag it in Confidence rather than guessing.

## Phase 4 — Post to Notion

**Target DB:** https://www.notion.so/eb0089eb3ccc83928e5c017c1f66a70c?v=702089eb3ccc82f4a2d2080fa27c25c1

Create **ONE parent page** titled:

```
Pavitas Angle Brief [YYYY-MM-DD]
```

Set properties:

- **Date** field → today's date (use `date` command via bash if unsure)
- **Source** field → "Claude"

Inside the parent page, create a table with one row per angle. Columns:

| Angle | Tier | Why now | Source material | Constraints & credits | Confidence |

If zero angles cleared the gate, create the page anyway with a single block titled "No angles this week" and a one-sentence explanation of what was missing.

## Phase 5 — Report back

After posting, return a one-screen summary to Pavi:

- Notion page URL
- Each angle in one sentence, with its tier
- Any flagged issues (missing inputs, release-date risks, credits that need verification)

No postamble. No "Let me know if you need changes."

## Hard rules (enforced at every phase)

- Never claim an endorsement that wasn't given
- Never surface embargoed work
- Credit author + publisher + release date accurately — if uncertain, flag it
- Quality over cadence — one strong angle beats three weak ones
- No copy. If output contains a hook, caption, hashtag, or script line, it's wrong.
