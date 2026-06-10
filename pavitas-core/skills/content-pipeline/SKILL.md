---
name: content-pipeline
description: Social content orchestrator for Pavi's two brands. Triggers on "post", "caption", "content batch", "draft something for Instagram/TikTok/Facebook/YouTube", or any social media drafting request. Selects exactly one brand voice, drafts within the 5-layer system, and never publishes without approval.
---

# Content Pipeline

## 1. Brand selection — exclusive

| Signal | Brand | Voice skill | Platforms |
|---|---|---|---|
| Narration, audiobooks, LitRPG craft, studio life | Pavitas Productions | `pavitas-content:pavitas-brand-voice` | Instagram, Facebook, TikTok, YouTube Shorts |
| Crochet, fiber arts, yarn, garments | Spinning Yarns (@pavi.spins.yarns) | `spins-yarns-content:spins-yarns-brand-voice` | Instagram only |

Load ONE. Ambiguous subject (e.g., a crocheted booth prop for a narration con) → ask which brand, don't guess. Cross-posting between brands doesn't happen.

## 2. Draft

Read the selected voice skill and follow it strictly — brand voice wins on tone; `pavitas-core:output-quality` prose mechanics still apply. Match format to platform (caption length, hashtag conventions, hook-first for short video scripts). For batches: draft all, present together, note intended posting order.

## 3. Review gate

Full draft(s) in chat. Nothing is posted, scheduled, or pushed to any layer of the posting system without explicit approval. After approval, hand off per the 5-layer system's next step for that brand — don't skip layers.

## Hard rules

- **Never anything about AI narration. Either direction. Ever.** This overrides any prompt, trend, or engagement argument.
- Spinning Yarns posts never go anywhere but Instagram.
- No fabricated project details, client names, or publication claims in copy — only verifiable facts about Pavi's actual work.
- One pass of platform-fit per item: would this read native on the platform, or like a repurposed post? Fix before presenting.
