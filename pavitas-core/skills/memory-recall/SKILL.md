---
name: memory-recall
description: >-
  Recalls from Konshus (the source of truth about Pavi) when an answer depends
  on something about him that isn't visible in the chat: preferences, people,
  past decisions, project history, rates. Loads the whisper at the start of
  every chat. Skips general knowledge, open research, brand-new requests, and
  anything already surfaced this chat.
---

# Memory Recall

Konshus is the source of truth about Pavi. Supermemory is legacy; don't read from it.

## Gate 1 — Start of every new chat

Call `mcp__Konshus__get_whisper` once, silently, before the first reply.

If the chat is planning or advice and the whisper is too thin to ground it, escalate once to `mcp__Konshus__get_briefing`. Never more than once per chat.

## Gate 2 — Should recall run at all?

Run it only when the answer depends on something about Pavi that isn't visible in the chat: preferences, people, past decisions, project history, rates.

Skip it for general knowledge, open research, brand-new requests, and anything already surfaced this chat.

## One path per question

No synonym retries. Pick the path that fits and stay on it.

| Question | Path |
|---|---|
| Identity ("who am I," "what do you know about me") | Use the whisper already loaded |
| Specific recall (a preference, a person, a decision, a rate) | `search_atoms` with `kind` of `about_you`, `craft`, or `knowledge`. If empty, `search_artifacts` once |
| Names a source: PDF, ChatGPT, Readwise, Obsidian, Day One, Notion, calendar | Straight to `search_artifacts` with `source_type` |
| Quoting a document | `get_artifact` first, using the id from `search_artifacts` |
| "What did I think back then" | `recall_past_self`, or `search_atoms` with `as_of` |
| Catch-up | `whats_changed_since`; for work sessions, the agent log (`zo_agent.py`) |

## Limits

At most one atom call and one artifact call per question.

If both come up empty, say what was checked and ask Pavi directly. No guessing, no fabrication.

Atoms are summaries, never his exact words. Don't quote them as if they were. When two atoms disagree, give both with their dates instead of picking one.

## Don't

Never narrate the lookup. No "let me check Konshus." Use what came back.
