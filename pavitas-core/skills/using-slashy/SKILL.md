---
name: using-slashy
description: Shared Slashy MCP reference for email and calendar mechanics. Load alongside any skill that calls Slashy tools. Prevents re-deriving params across skills. Pair with pavitas-core:output-quality for email body prose.
---

# Using Slashy

Single source of truth for Slashy MCP mechanics. Email skills reference this instead of restating parameters.

## `inbox_email` — required on nearly every call

`inbox_email: "pavi@paviproczko.com"` — Pavi's only connected inbox. Pass explicitly on every Slashy email and calendar call.

## Reading mail — `list_messages`

Takes a single query string `q`, not structured filter params. Superhuman's structured filters map to query syntax:

| Old Superhuman param | Slashy `q` value |
|---|---|
| `is_unread: true, labels: ["INBOX"]` | `"is:unread in:inbox"` |
| `is_starred: true` | `"is:starred"` |
| `from: ["x@example.com"]` | `"from:x@example.com"` |
| `to: ["x@example.com"]` | `"to:x@example.com"` |
| date range | `"after:2026/06/01 before:2026/06/30"` |
| category filter | `"category:important"` or `"category:other"` |
| todo state | `"todo:reply"` or `"todo:followup"` |

## Reading a thread — `read_thread`

Requires `inbox_email`. For read-receipt / open-tracking data: add `include_tracking: true`. **No bulk equivalent exists** — Superhuman's `get_read_status_feed` has no Slashy counterpart. Tracking data requires one `read_thread` call per thread.

## Drafting — `draft_email`

`body` is required and must be **literal HTML**. There is no `instructions` field for AI-writer delegation. Claude writes the body directly; voice-matching comes from `pavitas-core:output-quality`, not this tool.

Delete a draft: `draft_email(inbox_email=..., delete=true, draft_id=...)` — folded into the same tool, not a separate discard call.

## Sending — `send_email`

Requires explicit user approval every time. Sends immediately unless `scheduled_at` is set (must be ≥5 min from now). No default undo grace period — every send is final the moment confirmed.

`cancel_scheduled_email` cancels only sends scheduled ≥5 min out. It cannot reverse an immediate send.

## Calendar — `create_event` vs. `update_event`

Slashy splits Superhuman's single `create_or_update_event` into two tools:
- `event_id` **not known** → `create_event`
- `event_id` **is known** → `update_event`

Both require `inbox_email` and `datetime_human` — a natural-language echo of the time used for validation (e.g. `"Thursday July 3 at 2pm CT"`).

## Availability — `get_available_times`

Param shape changed from Superhuman's `get_availability`:

| Superhuman | Slashy |
|---|---|
| `participants` | `emails` |
| `duration_minutes` | `min_duration_minutes` |
| `working_hours_only: true` | `business_hours_only: true` + `business_start_hour` / `business_end_hour` |
| RFC3339 date range | `start_date` / `end_date` (ISO date or `"today"` / `"next_week"`) |
| _(not available)_ | `display_timezone` — use for cross-timezone scheduling |

## Labeling and archiving — `label_email`

Replaces Superhuman's `update_thread`. Key action values:

| Slashy `action` | Superhuman equivalent |
|---|---|
| `"archive"` | `mark_done` |
| `"trash"` | `trash_thread` |
| `"spam"` | `mark_spam` |
| `"todo"` | _(new — reply / followup / clear / dismissed; no Superhuman equivalent)_ |

## Deep links

`read_thread` and `draft_email` may return a `link` field — a clickable URL to open the thread or draft directly in Slashy. Include it in output when present. Superhuman had no equivalent.
