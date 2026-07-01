---
name: eod-wrapup
description: End-of-day email and calendar wrap using Slashy. Reviews what came in today, surfaces loose threads, sets up tomorrow's email context. Triggers on "EOD wrapup", "end of day", "wrap up my day", "end of day email check", "eod".
---

# EOD Wrapup

End-of-day email and calendar review. Surfaces unresolved threads, sets tomorrow's context.

Tool mechanics: `pavitas-core:using-slashy`. IDs: `pavitas-core:workspace-context`.

## Step 1 — Gather today's activity (run in parallel)

**Email:**
- `list_messages(inbox_email="pavi@paviproczko.com", q="after:[today ISO date] in:inbox")`
- `list_messages(inbox_email="pavi@paviproczko.com", q="todo:reply OR todo:followup")`
- `list_messages(inbox_email="pavi@paviproczko.com", q="is:starred")`

**Calendar:**
- `list_calendar_events` — today (what happened / is still pending)
- `list_calendar_events` — tomorrow (what to prep for)

**Littlebird Log:** Pull today's briefing entry to compare the 3-3-3 against what actually happened.

## Step 2 — Read threads that need follow-up

For any thread flagged `todo:reply`, `todo:followup`, or starred: `read_thread(inbox_email="pavi@paviproczko.com", thread_id=...)`.

Claude synthesizes email + calendar directly — no `query_email_and_calendar` tool exists in Slashy.

## Step 3 — Present review

```
🌙 EOD WRAPUP — [Date]

📧 EMAIL STATUS
🔴 Still needs reply: [threads with link]
💤 Awaiting their reply: [threads with link]
✅ Handled today: [threads or "none logged"]

📅 TODAY
[What was scheduled, what actually happened]

🔮 TOMORROW — [Date]
[Events to prep for · any email threads to have ready]

📝 CARRY FORWARD
[Anything from today that needs tomorrow action]
```

## Step 4 — Close out

On any threads Pavi confirms are done:
`label_email(inbox_email="pavi@paviproczko.com", email_id=..., action="archive")`

Update today's Littlebird Log entry with completion notes if requested.

## Step 5 — Save durable facts

Run `pavitas-core:memory-capture`. Not optional — even a quiet day usually resolves at least one thread into a fact worth keeping (a deadline confirmed, a thread that closed with a decision, a contact that became a commitment).

If Pavi has been working 45+ min continuously, suggest a break before wrapping.
