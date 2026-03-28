# Daily Operations Plugin

Daily workflow orchestration for Pavi Proczko — briefings, handoffs, task capture, and reviews.

## Commands

| Command | What it does |
|---------|-------------|
| `/daily-ops:briefing` | Full morning briefing with parallel data gathering, 3-3-3 plan, publish to Notion |
| `/daily-ops:handoff` | Create/read/update session handoff in Littlebird Log |
| `/daily-ops:triage` | Quick mid-day email scan (email only, no full briefing) |
| `/daily-ops:task` | Instant task capture to Notion Tasks database |
| `/daily-ops:review` | End-of-day review with carryforward tracking |

## Sub-Agents

| Agent | Role |
|-------|------|
| `calendar-intel` | Pulls all 4 Google Calendars, detects conflicts, flags camp days |
| `email-triage` | Cora-style intelligent email processing with VIP awareness |
| `notion-tracker` | Littlebird Log, Tasks, comments, accountability checks |

## Connectors

- **Google Calendar** — All 4 calendars
- **Gmail** — Email triage and awaiting-reply tracking
- **Notion** — Littlebird Log, Tasks database, Audiobook Projects

## Integrates With

- `decision-framework` skill — pattern detection for narrative vs. reality
- `audiobook-production` plugin — pulls active project status into briefing
