# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~project tracker` might mean Asana, Linear, Jira, or any other project tracker with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories (chat, project tracker, knowledge base, etc.) rather than specific products. The `.mcp.json` pre-configures specific MCP servers, but any MCP server in that category works.

## Connectors for this plugin (customized for Pavitas Productions LLC)

Pavi runs Pavitas Productions as a solo operation — there's no team chat tool or separate project tracker. Notion is the single hub for both reference material and task tracking (the "AI Biz OS"), Google Workspace (Gmail, Google Calendar) handles email and scheduling, and Zo Computer (a persistent remote environment) extends things beyond any single session.

| Category | Placeholder | Connected for Pavitas | Other options |
|----------|-------------|-----------------------|---------------|
| Chat | `~~chat` | Not used — no team chat tool | Slack, Microsoft Teams, Discord |
| Email | `~~email` | Gmail (native connector — no plugin MCP entry needed) | Microsoft 365 |
| Calendar | `~~calendar` | Google Calendar (native connector — no plugin MCP entry needed) | Microsoft 365 |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Guru, Coda |
| Project tracker | `~~project tracker` | Notion (Tasks database doubles as the tracker) | Asana, Linear, Atlassian (Jira/Confluence), monday.com, ClickUp |
| Office suite | `~~office suite` | Not used — documents (invoices, contracts, scripts) are generated as .docx/.xlsx files directly, not through a connected office suite MCP | Microsoft 365 |

Since Notion covers both knowledge base and project tracker for Pavitas, `/productivity:update`'s "sync from project tracker" step and its "check knowledge base" step both point at the same Notion workspace — don't expect two separate external sources.

## Fallback routing: Composio

Composio is connected as a general-purpose gateway (not a per-category MCP with its own URL, so it isn't listed in `.mcp.json` the way Notion is). Use it as a backup path when a primary connector is unavailable or misbehaving:

- **Notion:** Composio's Notion actions are the *preferred* route for database operations (matches Pavi's standing routing rule); the native Notion MCP in `.mcp.json` is the fallback.
- **Gmail, Google Calendar, Google Drive:** the native first-party connectors are preferred; if one of them errors out mid-session, Composio's equivalents cover the same ground rather than blocking the task.

Don't proactively switch to Composio if the native connector is working fine — it's a backup, not a default.

## Zo Computer

Zo (`paviproczko.zo.space`) is Pavi's own always-on remote environment — it keeps running when his local machine and Cowork session aren't. That makes it useful for more than just another data source:

- **Extra scan source:** In `/productivity:update --comprehensive`, also query Zo's own memory (DuckDB at `/home/workspace/.zo/data/memory.duckdb`, via `bun /home/workspace/.zo/memory/scripts/memory.ts hybrid "query"`) alongside email/calendar/Notion. This surfaces context Zo has already picked up independently of this session.
- **Home for anything recurring:** If a workflow here should run on a schedule (a daily `/update`, a standing reminder), prefer a Zo automation (`create_automation`) over a one-off scheduled task tied to this session — it survives regardless of which surface (Cowork, Claude Code, claude.ai) is open, or whether Pavi's computer is even on.
- **Tool priority:** When touching Zo, call its MCP tools directly — `bash`, `read_file`, `write_file`, `create_automation`, `send_sms_to_user`, `send_telegram_message`, etc. Use `ask_zo` only as a fallback when no direct tool covers the need, not as the default entry point.

## Supermemory vs. this plugin's local memory

This plugin's `CLAUDE.md` / `memory/` directory and Pavi's Supermemory are **not the same thing** and shouldn't duplicate each other:

- `CLAUDE.md` / `memory/` — fast, local decoder ring for shorthand (nicknames, acronyms, project codenames) scoped to wherever this plugin is running.
- Supermemory — the durable, cross-platform system for facts that matter beyond one session (decisions, deadlines, contacts, direction changes), written via the `memory-capture` skill.

Before asking Pavi to explain a person, project, or term during bootstrap or gap-filling, check Supermemory first. Only ask if it's genuinely not there. Don't copy full Supermemory entries into `CLAUDE.md` wholesale — pull just what's needed for the decoder ring.
