---
name: workspace-context
description: Canonical IDs, tool routing, and workspace facts for Pavi's ecosystem. Always-on reference — read once per session. Replaces zo-workspace-orientation. For Zo-side skill routing during infra work, read references/zo-skill-index.md.
---

# Workspace Context

Facts and routing only. Behavioral rules live in `pavitas-core:safety-rails`.

## Canonical Notion identifiers (never search to find these)

| Database | Identifier |
|---|---|
| Tasks | data source `2ff089eb-3ccc-8121-9f00-000b2cf26253` |
| Littlebird Log 🪶 | DB `28d089eb-3ccc-80da-90fb-d861352103a8` / source `collection://28d089eb-3ccc-80ca-87a0-000bf7143e2a` |
| Audiobook Projects | `28321020-d7f5-4619-aafd-28c3faccf815` |
| Chapters | `a9ad76f7-aa1c-4423-9c7b-71905a721958` (relates to Projects via property `nMOv`) |
| Morning Nudges | source `f57fabf7-0273-4b03-b843-f10eed4bccb8` |

**Tasks DB defaults:** Status = "Inbox". Set Tag, Due Date, Priority, Recurring from context. When tasks/action items arise in any session, create them immediately — don't batch for later.

## Tool routing

| Task | Use |
|---|---|
| Notion database operations | Composio Notion preferred; native Notion MCP fallback |
| Email to Pavi himself | `send_email_to_user` (Zo) |
| Email to anyone else | Superhuman MCP draft → review → send |
| Email reading/search | Superhuman MCP. **Never** the Gmail MCP (drops HTML-only emails) |
| Cora data (briefs, inbox, todos) | Cora MCP tools, or Zo-side `cora` CLI during Zo sessions |
| Zo file ops / bash | `Zo Computer:bash`, `read_file`, `write_file` via the MCP proxy |
| Calendar | Native Google Calendar tools |
| "Make a note", no destination given | Littlebird Log |
| SMS to Pavi | `Zo Computer:send_sms_to_user` — only when asked or in agent contexts with something to report |

## Workspace facts

- Zo Computer: `paviproczko.zo.space` (remote Linux; all Zo paths under `/home/workspace/`)
- Mac home: `/Users/pavi2/`; canon skills repo: `/Users/pavi2/Documents/GitHub/pavitas-plugins/` (GitHub: anairofpavitas/pavitas-plugins)
- Changelogs: skills changes → `skills/CHANGELOG.md`; plugin/root changes → root `CHANGELOG.md`
- Zo memory: DuckDB at `/home/workspace/.zo/data/memory.duckdb`, CLI `bun /home/workspace/.zo/memory/scripts/memory.ts` (`hybrid "query"` preferred)
- Canonical Supermemory: Supermemory MCP as pavi@paviproczko.com — NOT the Zo-routed connector
- Workspace file mentions format as `` `file 'Documents/notes.md'` ``, relative to `/home/workspace`
- ACX/Audible-direct delivery specs: -23dB to -18dB RMS, -60dB noise floor, -3dB peak, 44.1kHz/192kbps MP3

## Domain conventions

- Writing/fiction → Story Grid framework and terminology
- Audio/recording → professional narration context; industry terms (PFH, punch-and-roll, RMS) without explanation
- Crochet/fiber arts → Fiber Arts persona
- Client named on a narration project → check the Audiobook Projects DB for prior context before responding

## Zo-side skills

During infra or Zo-mediated work, route to Zo's own skill library: read `references/zo-skill-index.md`.
