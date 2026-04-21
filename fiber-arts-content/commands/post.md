---
description: Generate Instagram/Facebook + Reels/Shorts content for @pavi.spins.yarns. Pulls Littlebird activity digest + Perplexity crochet brief + active projects from Notion, picks the strongest angles, drafts one image/carousel post (IG+FB) and one short-form video script (Reels+YT Shorts), and posts both as a parent page in the Pavi Spins Yarns Social Media Content Digests database. Autonomous — no review step.
---

# Spinning Yarns Content Generation

Fully autonomous. Gather → pick → draft → post. No intermediate review. Flag problems, don't pause for permission.

## Phase 1 — Gather

Spawn the `fiber-arts-content-intel` agent. It returns a structured brief with:
- Latest Littlebird Pavi Spins Yarns activity digest (from the Spinning Yarns DB)
- Latest Perplexity Weekly Crochet Briefing (from same DB) — includes Instagram Sweep section if present
- Active crochet projects (WIP status, yarn in hand, current row/stage)
- Recent Littlebird Log signal for fiber-arts activity (past 14 days)
- Upcoming community moments (LYS Day, MAL/CAL deadlines, book launches in her lane)
- Flagged moments

If the agent flags a missing input (no digest or no brief for this week), continue anyway — use what's available. Do not block on missing inputs.

If the user has supplied specific project details in the current conversation (yarn, pattern, designer, WIP observation), treat those as highest-priority signal — they override the agent's recency sort.

## Phase 2 — Pick angles

Load the `spinning-yarns-brand-voice` skill. Apply the angle hierarchy:

1. **Active WIP / FO / yarn acquisition** — something Pavi made, is making, or just bought. Always the strongest angle when there's a specific observation attached.
2. **Technique reflection** — Tunisian, interlocking, reversible stitches, mosaic, stitch geometry. Process-forward, specific, teachable.
3. **Designer / publication amplification** — when a launch, book, or drop fits her lane (editorial garment crochet, Tunisian, reversible/interlocking, indie dyer work). Credit the designer, don't subsume them.
4. **LYS / community moment** — LYS Day, Chicago shops, MAL/CAL participation, fiber events.
5. **Narrator crossover** — the overlap between booth and hook. Use sparingly. Only when there's a real parallel, not forced.

Pick **two distinct angles** for the two pieces — don't double up. Prefer tiers 1–2 when the signal supports them.

**Angle pairing logic:**
- If Pavi supplied a specific WIP/FO with an observation in conversation, that's almost always Piece 1 (image/carousel).
- Technique reflection usually works better as short-form video (demonstrable, thinking-out-loud).
- Narrator crossover can work either format but rarely both at once.
- Designer amplification works better as a single image/carousel than as video.

**Quality gate:** If only one angle meets the bar, produce one piece. If zero meet the bar, produce zero and explain why. Don't pad.

## Phase 3 — Draft

### Piece 1: Image/Carousel post (IG + FB, same copy)

Format:
- **Hook** — first line (grabs scroll, under 10 words ideal). Pun is welcome but not mandatory.
- **Caption** — 80–160 words, first person, warm, specific. One concrete detail minimum (yarn, hook size, stitch, row count, designer name).
- **Alt text** — always include, describe image for screen readers.
- **Hashtags** — 6–10. Cluster: 2–3 broad (#crochet #fiberarts), 2–3 technique-specific (#tunisiancrochet #interlockingcrochet), 2–3 project-specific (pattern name, designer handle as tag, yarn brand).
- **Visual brief** — describe what the asset should show (text description, no generation). Call out if carousel (2–5 slides) vs single image. Specify text overlays if any.

### Piece 2: Short-form video script (Reels + YT Shorts, same video)

Format:
- **Hook: 1.5 seconds** — visual + spoken. Thumb-stopping.
- **Beats: 15–40 seconds total** — numbered (1, 2, 3...).
- **On-screen text callouts** — explicitly marked per beat.
- **Closing beat** — not "follow for more." Leave the thought.
- **Video brief** — what's on camera per beat (hands? fabric? yarn cake?), audio treatment notes.

### Brand voice non-negotiables (from spinning-yarns-brand-voice skill)
- No AI narration mentions, positive or negative
- No "journey," "delve," "landscape," "in today's world"
- No "you can't even tell it's not knitted" energy — crochet is beautiful as crochet
- First person, warm, specific, process-forward
- Puns welcome (it's a crochet account)
- One concrete detail per post minimum (yarn, hook, stitch, designer, row, technique)
- Credit designers + yarn brands + retailers accurately
- Never promote AI-generated patterns or AI narration

## Phase 4 — Post to Notion

**Target DB:** https://www.notion.so/348089eb3ccc80a19b0bd181953bdacc
**Data source:** collection://348089eb-3ccc-80b5-9a41-000b25bd0c63

Create **ONE parent page** in this DB titled:
```
Spinning Yarns Content Generation [YYYY-MM-DD]
```

Set properties:
- **Date** → today's date (use `date` command via bash if unsure)
- **Source** → `Claude`

Inside the parent page, structure content as follows:

```
## Summary
[1–2 sentences: which angles, any flags. Example: "Two pieces. One WIP post on the Sniegs Snow Sweater (pro-crochet stance angle), one technique short on interlocking crochet (tier-2 craft reflection)."]

---

# Piece 1 — Image/Carousel (Instagram + Facebook)
**Content Type:** Image / Carousel ([N] slides) or Single Image
**Platforms:** Instagram, Facebook (same copy both)
**Angle:** [one-sentence angle description with tier]

---

**Hook:**
> [hook line]

**Caption / Body:**
[full caption]

**Alt Text:**
[alt text]

**Hashtags:**
`#tag1` `#tag2` `#tag3` …

**Visual Brief:**
[per-slide or single-image shot description]

**Notes for SM Manager:**
[timing, tag verifications, any credits to confirm, props needed]

**Visual Assets:** `[To be shot by Pavi — see Visual Brief]`

---

# Piece 2 — Short-form Video (Reels + YouTube Shorts)
**Content Type:** Short-form Video (~N seconds)
**Platforms:** Instagram Reels, YouTube Shorts (same cut both)
**Angle:** [one-sentence angle description with tier]

---

**Hook (1.5s):**
- **Visual:** [what's on camera]
- **Spoken:** "[line]"
- **On-screen text:** `[text]`

**Beat Breakdown:**
1. **Beat 1 — Ns.** [shot]. Spoken: *"[line]"*. On-screen text: `[text]`
2. [repeat]

**Hashtags:**
`#tag1` `#tag2` …

**Video Brief:**
- [camera setup, B-roll, audio notes, caption style, pacing]

**Notes for SM Manager:**
[shoot timing, props, constraints]

**Visual Assets:** `[To be recorded — see Video Brief]`

---

## Flagged Issues
- [Any tags/handles/credits needing verification]
- [Any embargo or timing constraints]
- [Any inputs that came in thin or missing]
```

If producing only one piece, include one piece block and add a block titled "Why only one piece" with a one-sentence explanation.

## Phase 5 — Report back

After posting, return a one-screen summary to Pavi:
- Notion page URL
- Angle 1 (one sentence)
- Angle 2 (one sentence)
- Any flagged issues (missing inputs, designer handle verification, embargo check)

No postamble. No "Let me know if you need changes."

## Hard rules (enforced at every phase)

- Never mention AI narration in any form
- Never promote or positively reference AI-generated crochet patterns
- Never claim endorsement not given
- Credit designer + yarn brand + retailer accurately — if uncertain, flag
- Quality over cadence — one strong piece beats two weak ones
- Match caption length to Instagram norms (not too long)
- Puns are encouraged. Cheese is fine. Corporate tone is not.
