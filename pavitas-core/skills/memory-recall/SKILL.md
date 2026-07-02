---
name: memory-recall
description: Checks Supermemory, chat history, Littlebird Log, and email —
in that order — before saying information isn't available or asking Pavi
for something that might already be stored. Fires on recall-shaped asks
(contacts, rates, past decisions, "did I already..."), not general
knowledge or brand-new requests.
---

# Memory Recall

## Check order
1. Supermemory — `mcp__Supermemory_MCP__recall` (pavi@paviproczko.com,
   containerTag sm_project_default). Empty result ≠ proof — recall lags
   behind writes. Don't report "not saved" off a single empty check.
2. Chat history — `conversation_search` / `recent_chats`. Catches things
   discussed but never distilled into a Supermemory write.
3. Littlebird Log — Notion DB 28d089eb-... via Composio. Often has the raw
   note before (or instead of) a Supermemory entry.
4. Email — Slashy `list_messages`/`read_thread`, never Gmail MCP (drops
   HTML-only mail). Use when the fact plausibly arrived via correspondence.

## When this runs
Recall-shaped asks only: "what's X's email," "what did we decide about Y,"
"did I already set this up," "where's the note on..." Skip for general
knowledge, open research, or requests with nothing yet to recall.

## Stopping condition
All four checked and empty → tell Pavi what was checked, then ask directly.
No silent guessing, no fabrication, no skipping straight to asking.

## Don't
Don't re-run mid-session for something already surfaced in this conversation.
