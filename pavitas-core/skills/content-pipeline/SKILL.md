---
name: content-pipeline
description: Social content orchestrator for Pavi's two brands. Triggers on "post", "caption", "content batch", "draft something for Instagram/TikTok/Facebook/YouTube", or any social media request. Selects exactly one brand, then routes — Pavitas Productions produces a cited topic slate for a human writer, Spinning Yarns drafts finished copy. Never publishes without approval.
---

# Content Pipeline

## 1. Brand selection — exclusive

| Signal | Brand | Skill | Produces | Platforms |
|---|---|---|---|---|
| Narration, audiobooks, LitRPG craft, studio life | Pavitas Productions | `pavitas-content:pavitas-brand-voice` | Topic slate — no copy | Instagram, Facebook, TikTok, YouTube Shorts |
| Crochet, fiber arts, yarn, garments | Spinning Yarns (@pavi.spins.yarns) | `spins-yarns-content:spins-yarns-brand-voice` | Finished copy | Instagram only |

Load ONE. Ambiguous subject (e.g., a crocheted booth prop for a narration con) → ask which brand, don't guess. Cross-posting between brands doesn't happen.

**The two brands no longer do the same job.** Pavitas copy is written by a human professional; this skill's Pavitas output stops at the angle. Spinning Yarns still drafts. Don't let the request's phrasing override this — "write me a caption about the Aethon book" is still a Pavitas request and still returns a slate.

## 2a. Pavitas path — topic slate

Read `pavitas-content:pavitas-brand-voice` and follow it. It owns the position, the specificity floor, the subject-vs-angle distinction, the six connection patterns, privacy exclusions, source-conflict handling, and the output block format. Don't restate any of that here.

Two differences from the `/pavitas-content:weekly` batch run:

- **The subject is usually given.** Pavi names what he wants a post about. That narrows the job to finding the angle inside it — the claim, tension, or reversal — not scanning the week for candidates. Return 1–3 angles on the named subject rather than a full 5–9 slate.
- **Source material still gets pulled.** An ad-hoc request doesn't lower the anchor or citation bar. If the anchor isn't in the sources, mark it `NEEDS ANCHOR` and name what's missing rather than filling the gap from the conversation.

Run the verification pass before handing anything over. It's required regardless of how small the request was.

If no angle on the named subject clears the specificity floor, say so and name what's missing. Don't return a subject dressed as an angle.

## 2b. Spinning Yarns path — draft

Read `spins-yarns-content:spins-yarns-brand-voice` and follow it strictly — brand voice wins on tone; `pavitas-core:output-quality` prose mechanics still apply. Match format to platform. For batches: draft all, present together, note intended posting order.

## 3. Review gate

Slate or draft goes to Pavi in chat. Nothing is posted, scheduled, or pushed to any layer of the posting system without explicit approval.

- **Pavitas:** after approval the slate goes to the writer. Offer to add it to the Pavitas Content DB alongside the weekly briefs. Never carry it further than the angle.
- **Spinning Yarns:** after approval, hand off per the 5-layer system's next step — don't skip layers.

## 4. Memory

Run `pavitas-core:memory-capture` the moment a save-worthy call lands — brand chosen for an ambiguous subject, a direction change mid-slate, a platform-fit fix — not only after the review gate closes.

## Hard rules

- **No Pavitas copy.** A hook, caption, hashtag, or script line in a Pavitas output means the run is wrong. If pushed for finished copy, hand over the slate and say the writing step belongs downstream.
- Spinning Yarns posts never go anywhere but Instagram.
- No fabricated project details, client names, publication claims, anchors, quotes, dates, or sources — only what a cited source states.
- Platform-fit pass applies to Spinning Yarns drafts: would this read native on the platform, or like a repurposed post? Fix before presenting. Pavitas slates prescribe no platform; that call belongs to the writer.
