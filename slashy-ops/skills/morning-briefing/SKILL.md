---
name: morning-briefing
description: Email-first morning intelligence using Slashy. Surfaces unread priorities, calendar snapshot, and threaded context on anything flagged — without Cora mediation. Use when Pavi wants a focused inbox + calendar picture rather than the full pavitas-core:morning-review. Triggers on "email brief", "morning email check", "what's in my inbox", "email briefing".
---

# Morning Briefing

Focused email + calendar intelligence at day start. Not a full day orchestrator — that's `pavitas-core:morning-review`. This skill goes deep on inbox and calendar without Cora mediation.

Tool mechanics: `pavitas-core:using-slashy`. Email body prose: `pavitas-core:output-quality`. IDs and routing: `pavitas-core:workspace-context`.

## Step 1 — Gather (run in parallel)

**Inbox scan — three passes:**
- `list_messages(inbox_email="pavi@paviproczko.com", q="is:unread in:inbox")`
- `list_messages(inbox_email="pavi@paviproczko.com", q="is:starred")`
- `list_messages(inbox_email="pavi@paviproczko.com", q="todo:reply")`

**Calendar:**
- `list_calendar_events` — today across all four calendars: primary, Studio Schedule, Colin, Events
- `list_calendar_events` — tomorrow preview

## Step 2 — Read priority threads

For each thread flagged unread, starred, or action-required: `read_thread(inbox_email="pavi@paviproczko.com", thread_id=...)`.

VIP senders — always read in full regardless of flag: publishers (Aethon, Podium, Recorded Books, Blackstone, Portal Books, Audible), Joanne Mitchell, Seth Ring, Colin, Gray Talent Group, Michelle Bratland, Tim Grahl.

## Step 3 — Synthesize and present

Claude synthesizes email + calendar directly. No `query_email_and_calendar` exists in Slashy — that synthesis is Claude's job here.

```
📧 MORNING EMAIL BRIEF — [Date]

🔴 ACTION REQUIRED
[Thread subject · sender · what action · deadline if visible · link]

🟢 FYI
[One line per thread · link]

💤 AWAITING REPLY
[Sent threads with no reply after 3+ days — q="from:pavi@paviproczko.com after:[3 days ago]"]

📅 TODAY
[Events by calendar]

🔮 TOMORROW
[Brief preview]
```

Include Slashy deep links (`link` field from `read_thread`) wherever returned — one-click access.

## Step 4 — Offer to act

Ask: "Anything to action now, or should I capture the to-dos?"

On request: create Notion Tasks (DB ID in `pavitas-core:workspace-context`, Status=Inbox) for any action-required items.
