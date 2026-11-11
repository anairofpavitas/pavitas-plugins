# Daily Operations Plugin

Daily workflow orchestration for Pavi Proczko — handoffs, task capture, and reviews.

## Commands

| Command | What it does |
|---------|-------------|
| `/daily-ops:handoff` | Create/read/update session handoff in Littlebird Log |
| `/daily-ops:triage` | Quick mid-day email scan (email only) |
| `/daily-ops:task` | Instant task capture to Notion Tasks database |
| `/daily-ops:review` | End-of-day review with carryforward tracking |

The morning briefing command and its three sub-agents (calendar-intel, email-triage, notion-tracker) were retired on 2026-11-11.

## Connectors

- **Google Calendar** — All 4 calendars: Primary, Studio, Cultural Events, Colin's shared
- **Gmail** — Email triage, VIP monitoring, awaiting-reply tracking
- **Notion** — Littlebird Log, Littlebird Database, Tasks database, Audiobook Projects

## Integrates With

- `decision-framework` skill — pattern detection for narrative vs. reality
