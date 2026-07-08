# Productivity Plugin

A productivity plugin primarily designed for [Cowork](https://claude.com/product/cowork), Anthropic's agentic desktop application — though it also works in Claude Code. Task management, workplace memory, and a visual dashboard — Claude learns your people, projects, and terminology so it can act like a colleague, not a chatbot.

Customized for **Pavitas Productions LLC** (Pavi Proczko, audiobook narration).

## Installation

```
claude plugins add knowledge-work-plugins/productivity
```

## What It Does

This plugin gives Claude a persistent understanding of your work:

- **Task management** — A markdown task list (`TASKS.md`) that Claude reads, writes, and executes against. Add tasks naturally, and Claude tracks status, triages stale items, and syncs with Notion.
- **Workplace memory** — A two-tier memory system that teaches Claude your shorthand, people, projects, and terminology. Say "check what Recorded Books said about the LitRPG delivery date" and Claude knows exactly which project and publisher.
- **Visual dashboard** — A local HTML file that gives you a board view of your tasks and a live view of what Claude knows about your workplace. Edit from the board or the file — they stay in sync.

## Commands

| Command | What it does |
|---------|--------------|
| `/start` | Initialize tasks + memory, open the dashboard |
| `/update` | Triage stale items, check memory for gaps, sync from Notion if applicable |
| `/update --comprehensive` | Deep scan email and calendar — flag missed todos and suggest new memories |

## Skills

| Skill | Description |
|-------|--------------|
| `memory-management` | Two-tier memory system — CLAUDE.md for working memory, memory/ directory for deep storage |
| `task-management` | Markdown-based task tracking using a shared TASKS.md file |

## Example Workflows

### Getting Started

```
You: /start

Claude: [Creates TASKS.md, CLAUDE.md, memory/ directory, and dashboard.html]
        [Opens the dashboard in your browser]
        [Asks about your current projects and clients to seed memory]
```

### Adding Tasks Naturally

```
You: I need to finish the pickup session for the Aethon title by Friday,
     send Podium the delivery confirmation, and follow up with the
     client about the pronunciation guide

Claude: [Adds all three tasks to TASKS.md with context]
        [Dashboard updates automatically]
```

### Morning Sync

```
You: /update --comprehensive

Claude: [Scans email and calendar for new action items]
        [Flags: "Aethon delivery is due tomorrow — still open"]
        [Suggests: "New contact mentioned in email: Maria Chen,
         production coordinator at Blackstone — add to memory?"]
        [Updates stale tasks and fills memory gaps]
```

### Workplace Shorthand

Once memory is populated, Claude decodes your shorthand instantly:

```
You: ping Recorded Books about the Ashwood delivery

Claude: "Message Recorded Books about the delivery date for Ashwood
         Reborn (LitRPG, book 3), currently in final QC"
```

No clarifying questions. No round trips.

## Data Sources

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

**Connected for Pavitas Productions:**
- Knowledge base + project tracker (Notion) — reference docs and task syncing, same workspace
- Email (Gmail) and calendar (Google Calendar) — native connectors, no plugin MCP entry needed

**Not used:**
- Chat — no team chat tool
- Office suite MCP — business documents (invoices, contracts) are generated directly as .docx/.xlsx files

See [CONNECTORS.md](CONNECTORS.md) for alternative tools in each category.
