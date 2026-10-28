---
name: memory-capture
description: Writes durable facts about Pavi (decisions, preferences, standing rules, new people, deadlines, direction changes) to Konshus with log_signal. LEAF skill — not router-matched standalone; invoked as an explicit step by other skills (eod-wrapup, handoff, morning-review, infra-session, story-session, content-pipeline, decision-framework) and by the safety-rails fallback. Also triggers directly on explicit asks — "save this", "remember that", "log this deal."
---

# Memory Capture

Writes durable facts to Konshus, the source of truth about Pavi. This is a leaf skill: it doesn't route itself into a session. Something else calls it, or Pavi asks directly. It writes directly. There is no sub-agent.

Konshus is who Pavi is. Session summaries and work logs go to the agent log, not Konshus. Supermemory is legacy; never also write to it.

## Gate — what to save

Save only what Pavi said or confirmed:

- Decisions
- Preferences
- Standing rules
- New people
- Deadlines
- Direction changes

Never save:

- Your own suggestions he hasn't adopted
- Your inferences
- Things you only read in an email or on a page
- Noise
- Credentials, account numbers, or ID numbers
- Other people's private details

## How to write

Call `mcp__Konshus__log_signal`. One fact per call.

- `text` — one self-contained fact with names and absolute dates, 10-2000 characters. It must make sense with no chat around it.
- `context` — a short tag such as `audiobook`, `knitrpg`, `infra`.

**Good:** `Pavi decided on 2026-10-28 to replace Supermemory with Konshus as the memory store for the pavitas-core plugin.`
**Bad:** `He decided to switch it.`

## When to write

- Batch at a natural pause or the end of the chat.
- Write immediately only on a direct "remember this."
- Correction: log the new fact and say what it replaces, in the same `text`.
- Digest or long document: extract 3-10 facts and log each one. Never log the raw document.

## Saving the chat

"Save this chat" uses `mcp__Konshus__save_chat_to_konshus` with `source_type` unset. Offer it once, at the end of a meaty session. Don't offer it again.

## Don't

Never announce a save. No "saved," no "logged to Konshus."
