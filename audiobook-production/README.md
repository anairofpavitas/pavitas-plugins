# Audiobook Production Plugin

End-to-end audiobook production management for Pavitas Productions LLC.

## Commands

| Command | What it does |
|---------|-------------|
| `/audiobook-production:new-project` | Full parallel project onboarding (script analysis → folders → Notion → calendar → confirmation email) |
| `/audiobook-production:session-prep` | Pre-recording briefing (next chapters, pickups, deadline math, publisher updates) |
| `/audiobook-production:qc-pack` | Generate QC spreadsheet with chapter status and audio file links |
| `/audiobook-production:wrap` | Close out a project (mark complete, calculate FH, generate invoice, draft delivery email) |

## Sub-Agents

| Agent | Role |
|-------|------|
| `script-scout` | Manuscript analysis, chapter detection, file naming, character/voice research |
| `production-tracker` | Notion database operations (Audiobook Projects + Chapters) |
| `qc-manager` | Pickup tracking, error logging, delivery spec verification |
| `business-ops` | Invoice generation, rate calculations, project estimates |

## Skills

| Skill | Role |
|-------|------|
| `audiobook-production:audiobook-script-analyzer` | Script analysis — chapter detection, word/page counts, file naming convention, chapter→workday distribution. Source of truth for `/new-project`, `script-scout`, and `production-tracker` |
| `audiobook-production:audiobook-project-setup` | Standardized folder creation (Assets/Chapters/CRX). Cowork-native — needs Mac filesystem access; from Claude.ai, folders are created on Zo instead |

Bundled 2026-07-01 (previously standalone uploads under the repo's shared `skills/` folder). Also referenced from outside this plugin: `pavitas-core:audiobook-kickoff` calls both by their namespaced name.

## Connectors

- **Notion** — Audiobook Projects database, Chapters database
- **Google Calendar** — Studio calendar for recording blocks and deadlines
- **Gmail** — Publisher communications
- **Box** — File delivery

## Setup

1. Install: `claude plugin install audiobook-production`
2. Ensure Notion, Google Calendar, Gmail, and Box connectors are authenticated
3. Other skills referenced: `business-documentation` (invoicing, on `/wrap`)

## Usage

```
/audiobook-production:new-project
# → Asks for script file, short name, publisher, deadline
# → Spawns 4 parallel agents to set everything up

/audiobook-production:session-prep
# → Auto-detects active project, shows what's next

/audiobook-production:qc-pack
# → Generates Excel QC spreadsheet for active project

/audiobook-production:wrap
# → Closes out project, generates invoice, drafts delivery email
```
