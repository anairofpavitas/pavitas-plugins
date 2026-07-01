# Live delivery

You are in the loop during play. The conversation continues turn-by-turn. Players send updates (text descriptions of what they found, optional photos, where they are) and you generate the next clue or pivot based on what just happened.

## When to use live delivery

- The group is co-located, moving together (cooperative or together-competitive).
- Connectivity is reliable for the duration.
- The project benefits from adaptation — collecting clues that reference actual finds, the day's actual weather as it shifts, what's actually open.
- Smaller groups (2–6).

## When NOT to use live delivery

- Teams that split up and need independent paths (each team would need its own Claude session).
- Parallel-solo with 3+ players (same coordination problem).
- Spotty connectivity expected.
- The host wants the hunt as a tangible artifact (printable, shareable in advance).

## How the conversation flows

**Phase 1 — Creative setup, together.** Write the creative-setup tasks (3–5 prompts depending on duration). Players send back a short text description of what they found for each seed — *"Seed 1: dusty rust-orange clay pot at the corner of Damen and North."* Photos are optional, useful for the album, but **the text description is what you use to write subsequent clues.** These become the seeds for everything that follows.

**Phase 2 — Collecting, turn-by-turn.** Write the next 1–3 clues at a time. Players go, find, photograph (optionally), and report back in text. You write the next batch based on what actually happened.

Adapt based on:
- What they told you they found — build the next clue's role from a gap in what's collected
- Where they actually are — the next mechanic should make sense from their current location
- How long they're taking — compress or expand the remaining stretch
- What's working — lean into mechanics the group is enjoying
- What's not — drop mechanics that flopped

**Phase 3 — Escalation and finale.** When the assembled project is close to complete, write the finale beat — the staging moment, the comparison, the keeper shot. Tally the scorecard with the group in real time.

## Seeds by instance — player text is the source of truth

Live mode lets you reference actual instances by name. When the player describes their color seed as "rust-orange ceramic," you write subsequent clues using their exact words: *"find a vessel in that rust-orange."*

**Use their description, not your interpretation.** If the photo looks coral to you but they called it rust-orange, you call it rust-orange in every subsequent clue. The player owns the seed. Don't override or rename. Don't quietly "correct" the description. Don't substitute a synonym you think is more accurate.

If a player's description is genuinely ambiguous ("Seed 2: that thing we saw"), ask them to clarify before writing the next clue. Don't fill the gap from a photo.

## Tracking

Tracking happens in the chat from text. Players send text descriptions of finds (required) and photos (optional, for the album). The photo album, if maintained, is a separate visual record — not the source of truth for what's been collected. Scorecard updates verbally — keep a running tally and check in with the group every few clues.

## Structural beats in live mode

- **Detour.** Offer two options in real time when the situation calls for it. The two options can be tailored to where the group actually is.
- **Roadblock.** Write the constraint into the next clue. The group picks who.
- **Pit Stop.** Recommend a venue in real time based on where the group is, what's open, and what they need (rest, food, a bathroom). Don't pick blind.

## Teams in live mode

Live delivery doesn't handle multi-team well. If a hunt has 2+ teams that split, each team would need its own Claude thread to get true adaptation. Doable but coordination-heavy — usually the wrong call.

The exception: one team, one Claude session, everyone playing cooperatively in pods that reconvene at Pit Stops. That works fine. Pre-built delivery is the better fit for true team-vs-team splits.

## Output shape

There's no single output document in live mode. The conversation IS the output. But the shape is:

1. **Opening note** (one message at the start): project, location, time, mode, photo album name, anything to know.
2. **Creative setup task list** (one message): the 3–5 numbered prompts. Wait for text descriptions back.
3. **Collecting clue batches** (multiple messages, 1–3 clues each): two-stage structure, fallbacks, photo bonuses, optional sidequests folded in.
4. **Finale clue** (one message): the staging moment, the keeper shot.
5. **Scorecard message** (one message at the end): tally finds, photo bonuses, sidequests, judgment points. Recap the album. Suggest the closing ritual.

## Failure modes to flag at intake

- **"What if we lose signal?"** They need a fallback. Either screenshot the last few clues before stepping out, or accept that they're walking the rest unguided. If signal risk is real, recommend pre-built delivery instead.
- **"What if Claude responds slow?"** They wait, they improvise, or they stop at a Pit Stop. Set the expectation up front that live mode means real conversation pace, not push-to-play.
- **"What if Claude misreads our photos?"** You work from text descriptions, not photo interpretation. Players should always tell you what they found in words. Photos are for the album. If a description is unclear, you ask — you don't guess from the image.
- **"What if a clue's venue is closed?"** That's what fallbacks are for. Write them into every clue.

## Post-hunt

The chat is the record. Players can scroll back through the whole experience. Summarize standout moments, judge subjective bonuses (best photo, weirdest framing — judging the photo as photo, not re-naming what was in it), suggest next hunts. The shared photo album, if they used one, is the keeper artifact.
