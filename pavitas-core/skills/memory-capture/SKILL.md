---
name: memory-capture
description: Writes durable facts (decisions, deadlines, contacts, direction changes) to Supermemory for cross-platform recall. LEAF skill — not router-matched standalone; invoked as an explicit step by other skills (eod-wrapup, handoff, morning-review, infra-session, story-session, content-pipeline, decision-framework) and by the safety-rails fallback. Also triggers directly on explicit asks — "save this", "remember that", "log this deal", "make a note of that."
---

# Memory Capture

Writes durable, cross-platform-recallable facts to Supermemory. This is a leaf skill — it doesn't route itself into a session. Something else calls it: another skill's explicit step, or a direct ask. Don't announce the save — just do it.

## Two memory stores — don't confuse them

Claude.ai's own native memory already runs in the background on claude.ai — no tool call, nothing this skill does, nothing it can see or edit. Supermemory (this skill) is a second, independent store. **The two don't dedupe against each other.** Write here anyway: Supermemory is what Zo, Perplexity, and every other non-claude.ai surface can actually read — native memory doesn't reach them. "Claude already remembers this" is not a reason to skip this skill; it just means claude.ai has it and nowhere else does yet.

## Tool

- `mcp__Supermemory_MCP__memory` — the only write path. Its own description says not to use any other memory tool, and per `pavitas-core:workspace-context` this is the canonical Supermemory MCP (as pavi@paviproczko.com) — **not** the separate `mcp__Supermemory__*` (`add`/`search`/`list`/`delete`/`profile`) tools, which are a different, Zo-routed connector.
  - `content` (required, string) — the memory text. See **Metadata tag** below for what goes in it.
  - `containerTag` — always `"sm_project_default"`. See **Destination**.
  - `action` — `"save"` (default) to write, `"forget"` to remove a stale one.
- `mcp__Supermemory_MCP__recall` — search (`query`, `containerTag: "sm_project_default"`) before writing anything that might already be captured. If a stale version turns up, `forget` it before saving the update, rather than leaving both live.

Neither tool exposes a structured metadata parameter or a TTL/expiry field — `content` is a single string, full stop. The metadata and expiry requirements below are real, but both are satisfied by folding the information into that string, not by passing extra parameters the tool doesn't have.

## Save

- Deadlines and time-sensitive commitments
- Project status changes and decisions made
- New clients, collaborators, or contacts
- Creative decisions and direction changes
- Personal context updates (preferences, constraints, working style)
- Anything a future agent would need to recall

## Don't save

- Promotional content, transactional notifications, operational noise
- Raw digest/long-form content — extract atomic facts instead (see **Digest handling**), archive the raw content to filesystem only
- Anything already captured in a prior memory — `recall` first; update, don't duplicate
- Conversational filler with no durable signal

## Write rule

One memory per fact. Never bundle. Each entry must be self-contained, specific (names/dates/versions), and actionable.

**Good:** "Pavi decided to use Claude Sonnet 4 as the default model tier for Zo compactor as of 2026-06-17"
**Bad:** "Pavi made several decisions about the Zo pipeline including model selection, routing, and connector configuration"

## Destination

Always `containerTag: "sm_project_default"` (My Space). Never `"pavi"` or any other container — there is no other project configured to write into.

## Expiry

No TTL parameter exists on the tool, so expiry is advisory text carried inside `content`, enforced the next time a session `recall`s the memory and notices it's stale — then `forget`s it. Append a marker per category:

| Category | Marker |
|---|---|
| Daily intelligence (Littlebird/Cora insights) | `(review: <date + 30d>)` |
| Project status | `(review: <date + 90d>)` |
| Decisions and preferences | none — permanent |
| Deadlines | `(expires: <deadline date + 7d>)` |

## Digest handling

When a digest/long document arrives (Littlebird, Cora, financial): extract 3–10 atomic facts and write each as its own `memory` call. Never save the raw document to Supermemory.

## Metadata tag — required on every write

Lead every `content` string with a bracketed tag, then the fact itself, one sentence:

```
[source: <agent-or-session-identifier> | date: YYYY-MM-DD | data_source: <littlebird|cora|financial|conversation|other>] <the fact>
```

`source` examples: `claude-chat`, `zo-compactor`, `claude-code`.

**Full example** (decision, permanent, no expiry marker):
`[source: claude-chat | date: 2026-06-17 | data_source: conversation] Pavi decided to use Claude Sonnet 4 as the default model tier for Zo compactor as of 2026-06-17.`

**Full example** (deadline, with expiry marker):
`[source: claude-chat | date: 2026-06-25 | data_source: conversation] Client contract for Narration Co. is due 2026-07-02. (expires: 2026-07-09)`
