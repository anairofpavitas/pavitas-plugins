---
name: memory-capture
description: Writes durable facts (decisions, deadlines, contacts, direction changes) to Supermemory for cross-platform recall. LEAF skill — not router-matched standalone; invoked as an explicit step by other skills (eod-wrapup, handoff, morning-review, infra-session, story-session, content-pipeline, decision-framework) and by the safety-rails fallback. Also triggers directly on explicit asks — "save this", "remember that", "log this deal."
---

# Memory Capture

Writes durable, cross-platform-recallable facts to Supermemory. This is a leaf skill — it doesn't route itself into a session. Something else calls it: another skill's explicit step, or a direct ask.

## Two memory stores — don't confuse them

Claude.ai's own native memory already runs in the background on claude.ai — no tool call, nothing this does, nothing it can see or edit. Supermemory is a second, independent store, and the two don't dedupe against each other. Write here anyway: Supermemory is what Zo, Perplexity, and every other non-claude.ai surface can actually read. "Claude already remembers this" is not a reason to skip capture.

## Execution

Don't write to Supermemory from here directly. Spawn the `memory-capture` sub-agent (Task tool, `subagent_type: memory-capture`) and hand it:

- The raw fact(s) or context to capture — verbatim is fine, let the agent extract/format
- Source identifier if known (e.g. `claude-chat`, `zo-compactor`, `claude-code`) — default to `claude-chat` if not obvious
- Today's date
- A category hint if you have one (decision / deadline / project-status / etc.) — optional, the agent infers it if omitted

The agent owns the save/don't-save judgment call, the one-memory-per-fact rule, metadata tag formatting, expiry markers, and digest handling (extracting 3–10 atomic facts from a long document rather than saving it raw). Don't announce the save to Pavi — just do it. If the agent reports back what it wrote, surface that only if it's relevant to what Pavi's currently looking at.

## When to call this

Any time you (or the skill orchestrating you) notice a durable fact worth keeping: a deadline, a decision, a new contact, a direction change, a preference update. If in doubt about whether something's save-worthy, spawn the agent anyway and let it make that call — it's cheap.
