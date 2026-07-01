---
name: pocket-hunt
description: Run lightweight on-the-go scavenger hunts for presence anchoring on a walk, bike, or trip — solo, with companions, or with dogs. Triggers include "pocket hunt", "quick hunt", "noticing walk", "start a hunt", "let's hunt", or "take me on a walk". Distinct from scavenger-hunt-designer (pre-planned event-style hunts).
---

# Pocket hunts

A lightweight scavenger hunt skill for in-the-moment presence anchoring. Designed to be used live, on-the-go, with minimal friction. Distinct from `hunt-skills:scavenger-hunt-designer`, which is for pre-planned event-style hunts.

The skill is built around three foundational principles. These override anything else:

## Three foundational principles

**1. Phone away between pings.** When you send a clue, the user puts their phone away. They walk, notice, hunt. They return to the chat only when they have something to share — a find, a photo, a description, a no-luck-but-here's-what-happened. **Never ping mid-hunt.** The pause between clues is the practice. Don't ask "how's it going?" If they're gone, they're gone — they'll come back when they're ready.

**2. Override anywhere, anytime.** The user can change the hunt at any point: downgrade, upgrade, skip a clue, regenerate the current one, start fresh, add or remove a companion, name their own seed, end early, switch hunt shape. Accept and adapt without resistance. Don't ask "are you sure?" Don't suggest staying the course. Don't push back. Their instinct in the moment is more authoritative than the plan.

**3. Feedback loop.** Feedback can come mid-hunt or at the end. The classification of feedback is the debrief's job, never mid-hunt.

**Mid-hunt feedback:** acknowledge briefly, apply to the current hunt if applicable, bank the raw feedback as-is. Don't classify, don't ask follow-up questions about scope, don't derail into meta-conversation. Return to the hunt.

**End-of-hunt debrief, in order:**
1. Recap each piece of banked feedback the user gave during the hunt.
2. For each one, ask whether it's a forever change or just for this hunt.
3. Ask if there's any additional feedback that didn't come up during the walk.
4. Classify each final item into one of three buckets:
   - **this-hunt only** — already applied, no further action
   - **forever preference (memory)** — a durable taste/pattern preference that should color all future hunts but doesn't require a structural file edit. Save to Supermemory via `mcp__mcp-supermemory-ai__memory` (e.g. "Remember that I prefer found-object combinatorial hunts over commercial gift bags").
   - **skill update (file edit)** — an actual structural or rule change to the skill. Edit the relevant `SKILL.md` or references file.
5. Apply memory updates immediately at the user's OK. Offer to apply skill file edits now, or save them for later.

The user is the only one who can correctly classify forever-vs-temporary, and they usually need distance from the hunt to do it well. The debrief is where that distance lives. Never try to classify in-flight.

---

## Intake: parse first, ask only what's missing

Before asking anything, parse the user's opening message for inferable axes. Only ask about what isn't named or strongly implied.

The axes:

- **Rung** (commitment level — see `references/rungs.md`)
- **Travel scale** (walking, biking, driving, mixed)
- **Range** (this block / neighborhood / wider area / specific destination)
- **Environment** (shop-rich / shop-sparse / residential / found-object / mixed — see `references/environment-context.md`)
- **Companion** (solo / human / non-human / mixed — see `references/companion-integration.md`)
- **Parallel activity** (none / crochet / journal / sketchbook / etc. — see `references/parallel-activity.md`)
- **Hunt shape** (open exploration / travel hunt / destination-with-delivery — see `references/hunt-shapes.md`)
- **Long-form opt-in** (named end state / play by ear)
- **Duration** (approximate)

### Example parsing

> *"I'm heading out on a walk with the dogs to a local park in Portage Park. I'll be walking through residential streets. I've got about an hour. Let's start a hunt."*

Extracts: walking ✓, dogs (non-human companion) ✓, Portage Park / residential / shop-sparse ✓, ~1 hour ✓, open exploration (inferable from no destination) ✓.

Still to ask: rung, parallel activity, long-form opt-in.

### When the opening is bare

If the user says "let's start a hunt" with no context, ask the full set, but keep it conversational — 2–3 questions at a time, react, ask the next round. Don't dump a flight booking form.

### Smart-default order

Lead with: rung, range, companion. Those three shape everything else. Then environment, parallel activity, duration. Hunt shape comes last because it's often inferable from range + duration.

---

## Research

Once intake is gathered, do a quick research pass before generating the first clue. Light, focused, not exhaustive.

**Always research:**
- Weather for the next few hours at the user's location — `WebSearch` for forecast, or `WebFetch` against a weather source if a precise read is needed
- Day of week + time of day implications (what's open, what's quiet, what's busy)

**Research if relevant to the hunt:**
- Specific neighborhood landscape (shops, parks, cafes) when the user named one — `WebSearch` with tight queries like *"Portage Park Chicago independent shops"* or *"yarn store Andersonville Chicago"*
- Wider Chicago-area events (street fairs, festivals, farmers markets, public events) when the user is exploring widely or hasn't picked a neighborhood — especially May–October. *"Chicago events this weekend"*
- Specific shop types when the user names them ("yarn stores," "ceramics," "specialty art supplies")

**Ambient context the user can request anytime:**
- "What's happening in the city today?"
- "What festivals are coming up this month?"
- "Where's a farmers market near me right now?"
- "What stores in [neighborhood] would have [thing]?"

Bake research into seed prompts and clue mechanics naturally. Don't dump research at the user as a list. Use it to shape what you generate.

---

## The hunt flow

**1. Summary + confirmation.** After intake, summarize the hunt in 4–6 lines: rung, shape, range, companion, duration, named end state if any. Wait for user confirmation before sending seed prompts.

**2. Generate seeds.** 3 seed prompts, varied patterns from `references/seed-prompts.md`, adapted to environment and rung. Solo prompts for solo hunts. Conversation prompts for engaged human companions. Mixed for dog companions. Photographing each seed is required for rung 2+. The user shares back text descriptions (authoritative) and optional photos. Text wins if they conflict.

**Seeds always come before clues. Never bake seed prompts into clue 1.** Send the seed prompts first as a standalone message. The user works through them and returns with their three seeds. Only then do you generate the first clue stretch, built around what they found. The seeds are the lens; clues come second.

**3. Generate clue stretches.** 1–3 clues at a time. Each clue follows the two-stage structure (where to go + what to do/find). Use path-aware clue mechanics when there's distance to cover — instructions on what to notice between points, not just at the destination. Rung determines verbs (notice / photograph / find / acquire / combine).

**4. Side-quest offers.** Between clue stretches, occasionally offer a side quest based on context. See `references/side-quests.md`. Always optional. Skippable without penalty.

**5. Extend / upgrade / downgrade / end.** After each clue stretch in *play-by-ear* mode, offer the user a choice: another stretch at current rung, upgrade rung, downgrade rung, or end. In *long-form opt-in* mode with a named end state, don't ask — continue toward the end state, but accept any override mid-stream.

**6. Closure.** When the hunt ends (named end state reached, time up, or user calls it), run the debrief in this order:
   - Brief acknowledgement of how the hunt landed
   - Ask if they want anything generated from photos/notes (collage, social post, journal pages, etc.) — exit cleanly if no
   - Recap banked feedback from during the hunt
   - For each banked item, ask: forever or just this hunt?
   - Ask if there's any additional feedback that didn't come up during the walk
   - Classify final feedback set (this-hunt only / forever preference / skill update)
   - Apply forever preferences via Supermemory immediately (with the user's OK). Offer to apply skill file edits now or save for later.

If a destination-with-delivery hunt: also ask how the delivery went. Light, curious, no scoring.

---

## Side-quest rotation

See `references/side-quests.md` for the catalog. Conditions for offering:
- User has been hunting for >30 min (energy to add a beat)
- No side quest in the current hunt yet
- Context fits (e.g., "person you know in the area" needs commercial access for gift items; "pit stop" needs nearby cafes/bars)

Don't deploy more than one side quest per hunt unless the user requests another. Skippable without consequence — skip, generate the next regular clue.

---

## Tooling

Map each beat to the right tool. Be invisible about tool choice — the user is on a walk, they want clues, not infrastructure.

- **Weather + day-of context:** `WebSearch` for a quick forecast. `WebFetch` if you need a precise read from a specific weather source.
- **Neighborhood research / open-now / events:** `WebSearch` with tight 2–5 word queries. Prefer this over rendering a full page.
- **Specific shop check (hours, status, menu):** `WebFetch` against the URL. Escalate to Claude in Chrome (`mcp__Claude_in_Chrome__*`) only if the page is JS-rendered or requires interaction.
- **Photos from the user:** the user attaches photos directly in chat. Read them with the file tools. **Text descriptions remain authoritative** — never override the user's naming based on what the photo looks like.
- **Forever preferences from the debrief:** `mcp__mcp-supermemory-ai__memory`, written from Pavi's perspective ("Remember that I prefer found-object hunts in residential environments").
- **Closing artifacts (if the user wants one):** photo collage or visual via `canvas-design` skill, social posts as drafts in chat, journal pages via the `pdf` or `docx` skill. Always offer, never force.
- **Scheduling a recurring hunt prompt** (e.g., weekly Sunday morning nudge): `mcp__scheduled-tasks__create_scheduled_task`. Only on user request.

---

## What to never do

- Never ping the user mid-hunt to ask how it's going. Wait for their return.
- Never resist an override. Apply and continue.
- Never reinterpret player text descriptions from photos. Text is authoritative.
- Never classify feedback mid-hunt. Bank it, return to the hunt, classify at debrief.
- Never deploy a conversation-seed prompt when the companion is in "along for the walk, not playing" mode.
- Never force a closing output. Ask, exit cleanly if they decline.
- Never generate clues that require travel beyond the user's stated range or travel mode (no "drive 20 min east" if they're walking).
- Never scold for skipping, downgrading, or ending early.

## Tone

Match `hunt-skills:scavenger-hunt-designer`. Sentences not paragraphs. Active voice. Contractions fine. No corporate gloss, no twee phrasing. Treat the user as an adult on a walk, not a child on a field trip. Clue text is concrete and specific. Seed prompts have a little poetry where it earns it, but never overwrites.

Shift warmer and quieter for solo-presence hunts. Shift more playful for companion hunts. Shift practical and short for travel-hunt clue language. The rung determines the register.
