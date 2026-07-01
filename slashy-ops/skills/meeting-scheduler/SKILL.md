---
name: meeting-scheduler
description: Schedule meetings using Slashy — finds mutual availability, creates or updates the calendar event, and optionally drafts a confirmation email. Triggers on "schedule a meeting", "find time for a call", "set up a meeting with", "book time with [person]", "meeting scheduler".
---

# Meeting Scheduler

End-to-end meeting scheduling: availability → calendar event → optional confirmation email.

Tool mechanics: `pavitas-core:using-slashy`. Email prose: `pavitas-core:output-quality`. IDs: `pavitas-core:workspace-context`.

## Step 1 — Gather inputs

Ask Pavi or infer from context:
- Participant email(s)
- Duration (minutes)
- Preferred date range
- Timezone of participants (for cross-timezone — needed for `display_timezone`)
- New event or rescheduling an existing one? If rescheduling, get the `event_id`.

## Step 2 — Find availability

```
get_available_times(
  inbox_email="pavi@paviproczko.com",
  emails=[participant emails],
  min_duration_minutes=<duration>,
  start_date="<ISO date or 'today'>",
  end_date="<ISO date or 'next_week'>",
  business_hours_only=true,
  business_start_hour=9,
  business_end_hour=18,
  display_timezone="<participant timezone if cross-timezone>"
)
```

Note: Slashy uses `emails` (not `participants`), `min_duration_minutes` (not `duration_minutes`), `business_hours_only` (not `working_hours_only`).

Present the top 3 slots. Ask Pavi to choose.

## Step 3 — Create or update event

**Branch on event_id:**

**New event** (`event_id` not known):
```
create_event(
  inbox_email="pavi@paviproczko.com",
  summary="<title>",
  start_datetime="<ISO 8601>",
  end_datetime="<ISO 8601>",
  attendees=[<emails>],
  datetime_human="<e.g. 'Thursday July 3 at 2pm CT'>"
)
```

**Existing event** (`event_id` is known):
```
update_event(
  inbox_email="pavi@paviproczko.com",
  event_id="<id>",
  <only the fields that changed>,
  datetime_human="<natural language echo of the new time>"
)
```

Confirm the event link with Pavi.

## Step 4 — Confirmation email (optional)

If Pavi wants an invite or confirmation note sent:

1. Compose HTML body per `pavitas-core:output-quality`. Present in chat.
2. Pavi approves body.
3. `draft_email(inbox_email="pavi@paviproczko.com", to=[...], subject="...", body="...")`
4. On explicit "send it": `send_email(inbox_email="pavi@paviproczko.com", draft_id="...")` — no undo after confirmation.
