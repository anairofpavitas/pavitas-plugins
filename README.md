# Pavitas Productions Plugin Suite

Nine custom Claude Code / Cowork plugins designed for Pavi Proczko's audiobook narration business, creative work, and personal projects.

## Installation

```bash
# Add the marketplace
claude plugin marketplace add [path-or-repo]/pavitas-plugins

# Install individual plugins
claude plugin install audiobook-production@pavitas-plugins
claude plugin install daily-ops@pavitas-plugins
claude plugin install publisher-relations@pavitas-plugins
claude plugin install creative-writing@pavitas-plugins
claude plugin install fiber-arts-content@pavitas-plugins
claude plugin install pavitas-content@pavitas-plugins
claude plugin install spins-yarns-content@pavitas-plugins
claude plugin install enterprise-search@pavitas-plugins
claude plugin install writing-workshop@pavitas-plugins
```

## Plugin Overview

| Plugin | Commands | Agents | Skills | Connectors |
|--------|----------|--------|--------|------------|
| **audiobook-production** | 4 | 4 | — | Notion, Calendar, Gmail, Box |
| **daily-ops** | 5 | 3 | — | Calendar, Gmail, Notion |
| **publisher-relations** | 4 | — | 1 | Gmail, Notion, Box |
| **creative-writing** | 5 | 2 | — | Notion |
| **fiber-arts-content** | 4 | — | — | Notion |
| **pavitas-content** | 1 | 1 | 1 | Notion |
| **spins-yarns-content** | 1 | 1 | 1 | Notion, Canva |
| **enterprise-search** | 2 | — | 3 | Slack/Discord, Gmail, Drive/Box, Wiki, PM, CRM |
| **writing-workshop** | — | — | 4 | — |
| **TOTAL** | **26** | **11** | **10** | — |

## All Commands Quick Reference

### Audiobook Production
- `/audiobook-production:new-project` — Full parallel project onboarding
- `/audiobook-production:session-prep` — Pre-recording briefing
- `/audiobook-production:qc-pack` — QC spreadsheet generation
- `/audiobook-production:wrap` — Project close-out + invoice

### Daily Operations
- `/daily-ops:briefing` — Morning briefing (3-3-3 method)
- `/daily-ops:handoff` — Session handoff management
- `/daily-ops:triage` — Mid-day email check
- `/daily-ops:tasks` — Quick task capture to Notion
- `/daily-ops:review` — End-of-day retrospective

### Publisher Relations
- `/publisher-relations:intake` — Process publisher email
- `/publisher-relations:invoice` — Generate branded invoice
- `/publisher-relations:status` — Active projects by publisher
- `/publisher-relations:reply` — Draft reply in Biz Mode

### Creative Writing
- `/creative-writing:scene` — Story Grid scene analysis
- `/creative-writing:submit` — Mentor submission prep
- `/creative-writing:clean` — Anti-AI prose cleaning
- `/creative-writing:dictate` — Dictation transcript processing
- `/creative-writing:stuck` — One actionable step to get unstuck

### Fiber Arts & Content
- `/fiber-arts-content:pattern` — Pattern transcription (video/web → PDF)
- `/fiber-arts-content:log` — Save to Notion + crochet/ folder
- `/fiber-arts-content:post` — Instagram draft for @pavi.spins.yarns
- `/fiber-arts-content:project` — Track active crochet projects

### Pavitas Content (audiobook brand social)
- `/pavitas-content:weekly` — Weekly @pavitasproductions drop: 1 image/carousel (IG+FB) + 1 short-form video script (TikTok+Shorts), drafted from Notion inputs

### Spins Yarns Content (crochet brand social)
- `/spins-yarns-content:weekly` — Weekly @pavi.spins.yarns drop: 2 IG posts + 1 Threads post, drafted from today-dated Littlebird crochet brief + Perplexity trends, with Canva visual assets

### Enterprise Search
- `/enterprise-search:search` — Cross-tool search across email, chat, docs, wikis in one query
- `/enterprise-search:digest` — Daily or weekly activity digest across connected sources

### Writing Workshop
Skill-only plugin (no slash commands) — `writing-interview`, `writing-nudge`, `project-setup`, `style-mirror`

## Shared Dependencies

These existing skills are referenced by multiple plugins:
- `humanize-prose` — Used by creative-writing (clean command) and publisher-relations (email drafting)
- `business-documentation` — Used by audiobook-production (wrap) and publisher-relations (invoice)
- `design-elevation` — Used by any plugin generating visual documents
- `decision-framework` — Used by daily-ops when patterns emerge
- `audiobook-script-analyzer` — Used by audiobook-production (new-project)
- `audiobook-project-setup` — Used by audiobook-production (folder creation)
- `handoff` — Functionality absorbed into daily-ops plugin

## Connector Requirements

All plugins use remote MCP connectors via OAuth:
- **Notion**: https://mcp.notion.com/mcp
- **Google Calendar**: https://gcal.mcp.claude.com/mcp
- **Gmail**: https://gmail.mcp.claude.com/mcp
- **Box**: https://mcp.box.com

Authenticate each connector once; plugins share the authentication.
