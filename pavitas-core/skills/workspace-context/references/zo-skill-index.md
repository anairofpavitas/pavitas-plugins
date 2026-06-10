# Zo-Side Skill Routing Index

When operating Pavi's Zo Computer (via the MCP proxy), check whether a Zo-side skill exists before improvising. `read_file` the listed SKILL.md and follow it.

Discovery: `list_files /home/workspace/Skills`. First moves when context is thin: `read_file /home/workspace/AGENTS.md`, then `Documents/Connections-Index.md`.

| Trigger | Zo skill path |
|---|---|
| Email digest, inbox scan, auto-archive | `Skills/email-digest/SKILL.md` |
| Important/urgent email check | `Skills/zo-important-email-digest/SKILL.md` |
| Cora brief, todos, memories | `Skills/cora/SKILL.md` |
| Monthly expenses, "send expenses to Michelle" | `Skills/expense-tracker/SKILL.md` |
| New audiobook project / Notion chapter setup | `Skills/new-audiobook-project/SKILL.md` |
| FTP upload of finished chapters | `Skills/ftp-audiobooks/SKILL.md` |
| Littlebird handoff / journal sync | `Skills/littlebird-handoff/SKILL.md` |
| Monologue notes sync | `Skills/monologue-sync/SKILL.md` |
| Morning Nudges Notion dashboard | `Skills/morning-nudge-notion/SKILL.md` |
| Automation health check (Cora CLI, Ollama, DuckDB, agents) | `Skills/automation-health-monitor/SKILL.md` |
| Phone call / reservation / errand delegation | `Skills/duckbill/SKILL.md` |
| Delegate to Manus | `Skills/delegate-to-manus/SKILL.md` |
| TTS / voice samples | `Skills/elevenlabs/SKILL.md` |
| AI avatar video | `Skills/heygen/SKILL.md` |
| PDF generation | `Skills/zo-generate-pdf/SKILL.md` |
| EPUB/PDF -> markdown | `Skills/zo-epub-to-markdown/SKILL.md`, `Skills/zo-pdf-to-markdown/SKILL.md` |
| Google Workspace ops | `Skills/gws-best-practices/SKILL.md` |
| GitHub gh CLI | `Skills/github/SKILL.md` |
| zo.space site / page / slidedeck / blog | `Skills/zo-create-site/SKILL.md` + variants |
| Deep topic research | `Skills/zo-research-topic/SKILL.md` |
| Scheduled agent / automation | `Skills/zo-automate-something/SKILL.md` |
| Build an MCP server (Zo-side) | `Skills/mcp-builder/SKILL.md` |
| Persona build | `Skills/persona-builder/SKILL.md` |
| Prompt improvement | `Skills/prompt-improver/SKILL.md` |
| Share/export a skill | `Skills/share-skill/SKILL.md` |
| Semantic workspace search | `Skills/semantic-search/SKILL.md` |
| Weather | `Skills/weather/SKILL.md` |
| YouTube transcript/video | `Skills/youtube/SKILL.md` |
| Image resize / metadata strip | `Skills/zo-resize-image/SKILL.md`, `Skills/remove-photo-metadata/SKILL.md` |
| Cancel a subscription | `Skills/just-fucking-cancel/SKILL.md` |

Zo memory decay tiers when storing: `permanent`, `stable` (90d), `active` (14d), `session` (24h), `checkpoint` (4h).

Note: Zo-side copies of `daily-briefing`, `pavitas-core:decision-framework`, `business-documentation`, `prose-humanizer`, `design-elevation` are superseded by the canonical pavitas-plugins versions. Migrate or pointer-stub them (see MIGRATION.md).
