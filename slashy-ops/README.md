# slashy-ops

Five email and calendar operations skills, all built directly on Slashy MCP. Bundled together so updates ship as one plugin install instead of five separate skill uploads.

## Skills

| Skill | What it does |
|---|---|
| `slashy-ops:morning-briefing` | Email-first morning intelligence — unread/starred/reply-flagged inbox passes + calendar snapshot, Claude synthesizes both directly |
| `slashy-ops:eod-wrapup` | End-of-day email and calendar wrap — what's still open, what's resolved, tomorrow's preview |
| `slashy-ops:batch-draft-writer` | Write multiple email drafts in a review-then-save loop; nothing sends without separate explicit approval |
| `slashy-ops:meeting-scheduler` | Availability lookup → create or update calendar event → optional confirmation email |
| `slashy-ops:deal-tracker` | Deal/relationship thread tracking with per-thread read-receipt checks |

## Shared mechanics

All five skills defer to `pavitas-core:using-slashy` for Slashy tool syntax (`inbox_email`, `list_messages` query strings, `draft_email`'s literal-HTML-body requirement, `send_email` approval/no-undo behavior, `create_event`/`update_event` branching, `get_available_times` params, per-thread tracking, `label_email` actions). That skill is the single source of truth — these five stay logic-only.

Email body prose defers to `pavitas-core:output-quality`. IDs and tool routing defer to `pavitas-core:workspace-context`.

## Requires

- `pavitas-core` plugin installed (for `using-slashy`, `output-quality`, `workspace-context`)
- Slashy MCP connected, inbox `pavi@paviproczko.com`

## History

Migrated from Superhuman Mail to Slashy 2026-06-30 — see `skills/CHANGELOG.md` in the repo root for the full migration record. Packaged as a standalone plugin 2026-07-01 so the five skills update together rather than as individual uploads.
