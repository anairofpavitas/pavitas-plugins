# Pavitas Productions Plugin Suite

Nine custom Claude Code / Cowork plugins designed for Pavi Proczko's audiobook narration business, creative work, and personal projects.

> **v2/v2.1 refactor (2026-06-10):** the suite consolidated from nine plugins to six. `publisher-relations`, `enterprise-search`, and `writing-workshop` were removed; `fiber-arts-content` merged into `spins-yarns-content` v2.0.0; the core skill architecture shipped as the `pavitas-core` plugin v2.0.0. History: [CHANGELOG.md](CHANGELOG.md) (plugins) and [skills/CHANGELOG.md](skills/CHANGELOG.md) (skills).
>
> **slashy-ops added (2026-07-01):** five email/calendar skills (previously migrated off Superhuman Mail to Slashy MCP as standalone `skills/` entries) packaged into a seventh plugin so they install and update together. Requires `pavitas-core` for shared mechanics.
>
> **story-grid-skills added (2026-07-01):** five previously-standalone Story Grid mentorship
> coaching skills (sg-grade, sg-edit, sg-drill, sg-spar, sg-sync) packaged into an eighth
> plugin so they install and update together. No dependency on other plugins.
>
> **hunt-skills added (2026-07-01):** three previously-standalone scavenger-hunt skills
> (scavenger-hunt-designer, pocket-hunt, pleasure-hunt) packaged into a ninth plugin so they
> install and update together. Skill-only — no agents or commands; each skill runs live in
> the main conversation and a sub-agent hop would only add latency. No dependency on other
> plugins.
>
> **audiobook-production skills bundled (2026-07-01):** `audiobook-script-analyzer` and
> `audiobook-project-setup`, previously standalone `skills/` uploads, moved into the
> `audiobook-production` plugin itself so the whole workflow (commands, agents, skills)
> installs and updates as one unit. Plugin count unaffected by this change.

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
claude plugin install slashy-ops@pavitas-plugins
claude plugin install story-grid-skills@pavitas-plugins
claude plugin install hunt-skills@pavitas-plugins
```

## Plugin Overview

| Plugin | Version | Commands | Agents | Skills | Connectors |
|--------|---------|----------|--------|--------|------------|
| **audiobook-production** | 1.1.0 | 4 | 4 | 2 | Notion, Calendar, Gmail, Box |
| **daily-ops** | 1.0.0 | 5 | 3 | — | Calendar, Gmail, Notion |
| **creative-writing** | 1.0.0 | 5 | 2 | — | Notion |
| **pavitas-content** | 1.0.0 | 1 | 1 | 1 | Notion (session) |
| **spins-yarns-content** | 2.0.0 | 5 | 1 | 1 | Notion; Canva (session) |
| **pavitas-core** | 2.0.0 | — | — | 13 | — |
| **slashy-ops** | 1.0.0 | — | — | 5 | Slashy (session) |
| **story-grid-skills** | 1.0.0 | — | — | 5 | — |
| **hunt-skills** | 1.0.0 | — | — | 3 | — |
| **TOTAL** | | **20** | **11** | **30** | |

Connectors marked *(session)* are not bundled in the plugin's `.mcp.json` — they use whatever connection the claude.ai / Cowork session already has. pavitas-content bundles no `.mcp.json` at all; Canva is used at runtime by `/spins-yarns-content:weekly` for visual assets.

## All Commands Quick Reference

### Audiobook Production
- `/audiobook-production:new-project` — Full parallel project onboarding
- `/audiobook-production:session-prep` — Pre-recording briefing
- `/audiobook-production:qc-pack` — QC spreadsheet generation
- `/audiobook-production:wrap` — Project close-out + invoice
- Skills: `audiobook-production:audiobook-script-analyzer` (file naming convention, chapter→workday distribution — source of truth for `new-project`/`script-scout`/`production-tracker`), `audiobook-production:audiobook-project-setup` (Cowork-native folder creation)

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
Skill-only plugin (no slash commands) — 13 skills load as `pavitas-core:<name>`. See next section.

### Slashy Ops (email + calendar, Slashy MCP)
Skill-only plugin (no slash commands) — 5 skills load as `slashy-ops:<name>`. See "slashy-ops: Email + Calendar Operations" section below.

### Story Grid Skills (beat-writing mentorship coaching)
Skill-only plugin (no slash commands) — 5 skills load as `story-grid-skills:<name>`. See "story-grid-skills: Beat-Writing Mentorship Coaching" section below.

### Hunt Skills (scavenger-hunt family)
Skill-only plugin (no slash commands) — 3 skills load as `hunt-skills:<name>`. See "hunt-skills: The Scavenger-Hunt Family" section below.

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

## slashy-ops: Email + Calendar Operations

Packaged 2026-07-01 so the five skills below install and update as one plugin rather than five separate uploads. All five defer to `pavitas-core:using-slashy` for tool mechanics, `pavitas-core:output-quality` for email prose, and `pavitas-core:workspace-context` for IDs/routing — `pavitas-core` must be installed alongside this plugin.

| Skill | Role |
|-------|------|
| `slashy-ops:morning-briefing` | Email-first morning intelligence — inbox passes + calendar snapshot, Claude synthesizes both |
| `slashy-ops:eod-wrapup` | End-of-day email/calendar wrap — open threads, resolved threads, tomorrow preview |
| `slashy-ops:batch-draft-writer` | Write/review/save loop for multiple drafts; literal HTML body (no AI-writer delegation); explicit send per draft |
| `slashy-ops:meeting-scheduler` | Availability lookup → create/update calendar event → optional confirmation email |
| `slashy-ops:deal-tracker` | Deal/relationship thread tracking with per-thread read-receipt checks |

History: migrated off Superhuman Mail to Slashy 2026-06-30, packaged as a standalone plugin 2026-07-01. Full record: [skills/CHANGELOG.md](skills/CHANGELOG.md), [CHANGELOG.md](CHANGELOG.md). Details: [slashy-ops/README.md](slashy-ops/README.md).

## story-grid-skills: Beat-Writing Mentorship Coaching

Packaged 2026-07-01 from five previously-standalone Story Grid coaching skills so they
install and update as one plugin. No dependency on other plugins — operates entirely on
local project files (`knowledge/`, `Lessons/`, `* Feedback/`, `workbench/`).

| Skill | Role |
|-------|------|
| `story-grid-skills:sg-grade` | Mock examiner — dry-run PASS/REVISE verdict + score before real submission |
| `story-grid-skills:sg-edit` | Socratic line editor — mechanics pass + full conformance battery |
| `story-grid-skills:sg-drill` | Practice-worksheet generator — targeted reps with an answer-key rationale |
| `story-grid-skills:sg-spar` | Brainstorming / pressure-testing partner |
| `story-grid-skills:sg-sync` | Knowledge-base maintenance — distills new lessons/feedback, never edits source files |

Not to be confused with `creative-writing` (original fiction drafting, e.g. Jim & Percy) —
this plugin coaches the beat-writing submission cycle for the Story Grid mentorship program.
Details: [story-grid-skills/README.md](story-grid-skills/README.md).

## hunt-skills: The Scavenger-Hunt Family

Packaged 2026-07-01 from three previously-standalone scavenger-hunt skills so they install
and update as one plugin. No dependency on other plugins. Skill-only — no agents or
commands: all three run live in the main conversation, and a sub-agent hop would only add
latency to what are deliberately low-friction, real-time skills.

| Skill | Role |
|-------|------|
| `hunt-skills:scavenger-hunt-designer` | Event-style walking hunts for small groups — date walks, group adventures, couples outings — live or pre-built delivery |
| `hunt-skills:pocket-hunt` | Lightweight, turn-by-turn hunts for in-the-moment presence anchoring on a walk, bike, or trip — solo, with companions, or with dogs |
| `hunt-skills:pleasure-hunt` | Compact, upfront intimate hunts for sexual pleasure, intimacy, and exploration — solo, partner, group, or cruising |

Three distinct systems, not a merged skill — a prior audit considered merging them and
reversed that decision (see `skills/CHANGELOG.md`, 2026-06-10 entry). Each skill's
frontmatter `description` still does the disambiguation work; `pocket-hunt` and
`pleasure-hunt` cross-reference the others by namespaced name for tone-matching and
distinctness callouts. Details: [hunt-skills/README.md](hunt-skills/README.md).

## Shared Skills (repo `skills/` folder)

Standalone skills the plugins reference:
- `business-documentation` — used by audiobook-production (wrap) and the biz-admin routing profile

Moved into pavitas-core in skills-v2 — update any older references:
- `humanize-prose` and `design-elevation` → `pavitas-core:output-quality`
- `decision-framework` → `pavitas-core:decision-framework`
- `handoff` → `pavitas-core:handoff` (daily-ops keeps its `/handoff` command)

Moved into audiobook-production (2026-07-01) — update any older references:
- `audiobook-script-analyzer` → `audiobook-production:audiobook-script-analyzer`
- `audiobook-project-setup` → `audiobook-production:audiobook-project-setup`

The `skills/` folder also carries standalone personal skills — including `relational-emotional-regulation` and `mcp-wrapper-builder` — see [skills/CHANGELOG.md](skills/CHANGELOG.md). The hunt family (`scavenger-hunt-designer`, `pocket-hunt`, `pleasure-hunt`) moved out of this folder into the `hunt-skills` plugin — see above.

## Connector Requirements

Plugins that bundle an `.mcp.json` use remote MCP connectors via OAuth:
- **Notion**: https://mcp.notion.com/mcp
- **Google Calendar**: https://gcal.mcp.claude.com/mcp
- **Gmail**: https://gmail.mcp.claude.com/mcp
- **Box**: https://mcp.box.com

Authenticate each connector once; plugins share the authentication. Canva is connected at the claude.ai session level (not bundled) — without it, `/spins-yarns-content:weekly` still produces drafts and visual briefs and flags that assets weren't generated.
