---
name: deal-tracker
description: Track active deals and relationship touchpoints via email using Slashy. Surfaces deal threads, checks read receipts per thread, flags what needs follow-up. Triggers on "deal tracker", "check my deals", "deal status", "open deals", "relationship pipeline".
---

# Deal Tracker

Email-based relationship and deal tracking. Surfaces threads, checks open-tracking per thread, flags needed follow-ups.

Tool mechanics: `pavitas-core:using-slashy`. IDs: `pavitas-core:workspace-context`.

## Step 1 — Find active deal threads

Three passes:
```
list_messages(inbox_email="pavi@paviproczko.com", q="is:starred in:inbox")
list_messages(inbox_email="pavi@paviproczko.com", q="todo:followup")
list_messages(inbox_email="pavi@paviproczko.com", q="category:important")
```

Also surface any threads Pavi names explicitly.

## Step 2 — Read each deal thread

For each thread: `read_thread(inbox_email="pavi@paviproczko.com", thread_id=...)`.

Extract: last activity date, outstanding question or ask, who holds the ball.

## Step 3 — Check read receipts (per-thread loop)

No bulk read-receipt tool exists in Slashy — one call per thread with tracking:

```
read_thread(
  inbox_email="pavi@paviproczko.com",
  thread_id=<id>,
  include_tracking=true
)
```

Run this for each thread where Pavi sent the most recent email (5–10 threads). The `tracking` field in the response shows open status. If a sent email hasn't been opened: flag as "not yet opened — consider follow-up."

No bulk feed exists. This is N calls, not one. That's expected.

## Step 4 — Present deal status

```
📊 DEAL TRACKER — [Date]

[Deal name / thread subject]
Status: [active · stalled · awaiting their move · needs follow-up]
Last activity: [date]
Ball with: [Pavi / them]
Read receipt: [opened · not opened · tracking unavailable]
Next action: [what needs to happen]
[Slashy deep link]

---
[repeat per deal]

🔔 NEEDS FOLLOW-UP NOW
[Deals where action is on Pavi]
```

## Step 5 — Take action (on request)

- **Archive resolved thread:** `label_email(inbox_email=..., email_id=..., action="archive")`
- **Mark for follow-up:** `label_email(inbox_email=..., email_id=..., action="todo")`
- **Draft a follow-up:** hand to `batch-draft-writer` or compose inline per `pavitas-core:output-quality`
