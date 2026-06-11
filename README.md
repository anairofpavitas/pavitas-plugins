# Pavitas Productions Plugin Suite

Six custom Claude Code / Cowork plugins designed for Pavi Proczko's audiobook narration business, creative work, and personal projects.

> **v2/v2.1 refactor (2026-06-10):** the suite consolidated from nine plugins to six. `publisher-relations`, `enterprise-search`, and `writing-workshop` were removed; `fiber-arts-content` merged into `spins-yarns-content` v2.0.0; the core skill architecture shipped as the `pavitas-core` plugin v2.0.0. History: [CHANGELOG.md](CHANGELOG.md) (plugins) and [skills/CHANGELOG.md](skills/CHANGELOG.md) (skills).

## Installation

```bash
# Add the marketplace
claude plugin marketplace add [path-or-repo]/pavitas-plugins

# Install individual plugins
claude plugin install audiobook-production@pavitas-plugins
claude plugin install daily-ops@pavitas-plugins
claude plugin install creative-writing@pavitas-plugins
claude plugin install pavitas-content@pavitas-plugins
claude plugin install spins-yarns-content@pavitas-plugins
claude plugin install pavitas-core@pavitas-plugins
```

## Plugin Overview

| Plugin | Version | Commands | Agents | Skills | Connectors |
|--------|---------|----------|--------|--------|------------|
| **audiobook-production** | 1.0.0 | 4 | 4 | — | Notion, Calendar, Gmail, Box |
| **daily-ops** | 1.0.0 | 5 | 3 | — | Calendar, Gmail, Notion |
| **creative-writing** | 1.0.0 | 5 | 2 | — | Notion |
| **pavitas-content** | 1.0.0 | 1 | 1 | 1 | Notion (session) |
| **spins-yarns-content** | 2.0.0 | 5 | 1 | 1 | Notion; Canva (session) |
| **pavitas-core** | 2.0.0 | — | — | 12 | — |
| **TOTAL** | | **20** | **11** | **14** | |

Connectors marked *(session)* are not bundled in the plugin's `.mcp.json` — they use whatever connection the claude.ai / Cowork session already has. pavitas-content bundles no `.mcp.json` at all; Canva is used at runtime by `/spins-yarns-content:weekly` for visual assets.

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
- `/daily-ops:task` — Quick task capture to Notion
- `/daily-ops:review` — End-of-day retrospective

### Creative Writing
- `/creative-writing:scene` — Story Grid scene analysis
- `/creative-writing:submit` — Mentor submission prep
- `/creative-writing:clean` — Anti-AI prose cleaning
- `/creative-writing:dictate` — Dictation transcript processing
- `/creative-writing:stuck` — One actionable step to get unstuck

### Pavitas Content (audiobook brand social)
- `/pavitas-content:weekly` — Weekly @pavitasproductions drop: 1 image/carousel (IG+FB) + 1 short-form video script (TikTok+Shorts), drafted from Notion inputs

### Spins Yarns Content (crochet brand, Instagram only)
- `/spins-yarns-content:weekly` — Weekly @pavi.spins.yarns drop: 2 IG posts, drafted from today-dated Littlebird crochet brief + Perplexity trends, with Canva visual assets
- `/spins-yarns-content:post` — One-off Instagram draft (defers to `spins-yarns-brand-voice`)
- `/spins-yarns-content:pattern` — Pattern transcription (video/web → PDF or Notion)
- `/spins-yarns-content:log` — Save pattern/project update to Notion + crochet/ folder
- `/spins-yarns-content:project` — Track active crochet projects via Littlebird Log

### Pavitas Core (skill architecture)
Skill-only plugin (no slash commands) — 12 skills load as `pavitas-core:<name>`. See next section.

## pavitas-core: Skill Architecture

Shipped 2026-06-10 as the skills-v2 refactor, packaged as a plugin (v2.0.0). This repo is the canon for the skill ecosystem; claude.ai and Cowork mount the same skills.

| Layer | Skills | Role |
|-------|--------|------|
| Meta | `skill-router` | Goal → load-set dispatch; owns the coverage manifest every installed skill must appear in |
| Constraints (always-on) | `safety-rails`, `workspace-context`, `output-quality` | Conduct rules; IDs/routing/facts; prose + visual standards |
| Orchestrators | `morning-review`, `audiobook-kickoff`, `story-session`, `content-pipeline`, `infra-session` | Domain workflows that name which leaf skills to load |
| Direct-routed | `handoff`, `decision-framework`, `proof` | Load on their own triggers |

Notes:
- `morning-review` replaces the old `daily-briefing` skill (712 → ~70 lines; email sourced from the Cora brief).
- `output-quality` absorbed `humanize-prose` and `design-elevation` (reference files preserved).
- `story-session` is self-contained — writing-workshop's interview and style-matching were inlined (skills-v2.1).
- Layering rules, eval rubrics, and migration details: [pavitas-core/README.md](pavitas-core/README.md) and [pavitas-core/MIGRATION.md](pavitas-core/MIGRATION.md).

## Shared Skills (repo `skills/` folder)

Standalone skills the plugins reference:
- `audiobook-script-analyzer` — used by audiobook-production (new-project); source of truth for the file naming convention and chapter→workday distribution
- `audiobook-project-setup` — used by audiobook-production (folder creation); Cowork-native — from claude.ai, folders are created on Zo instead
- `business-documentation` — used by audiobook-production (wrap) and the biz-admin routing profile

Moved into pavitas-core in skills-v2 — update any older references:
- `humanize-prose` and `design-elevation` → `pavitas-core:output-quality`
- `decision-framework` → `pavitas-core:decision-framework`
- `handoff` → `pavitas-core:handoff` (daily-ops keeps its `/handoff` command)

The `skills/` folder also carries standalone personal skills — including the hunt family (`scavenger-hunt-designer`, `pocket-hunt`, `pleasure-hunt`), `relational-emotional-regulation`, and `mcp-wrapper-builder` — see [skills/CHANGELOG.md](skills/CHANGELOG.md).

## Connector Requirements

Plugins that bundle an `.mcp.json` use remote MCP connectors via OAuth:
- **Notion**: https://mcp.notion.com/mcp
- **Google Calendar**: https://gcal.mcp.claude.com/mcp
- **Gmail**: https://gmail.mcp.claude.com/mcp
- **Box**: https://mcp.box.com

Authenticate each connector once; plugins share the authentication. Canva is connected at the claude.ai session level (not bundled) — without it, `/spins-yarns-content:weekly` still produces drafts and visual briefs and flags that assets weren't generated.
