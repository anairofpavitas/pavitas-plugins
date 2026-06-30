---
name: skill-router
description: Load-set dispatcher for Pavi's skill ecosystem. Use at the start of any substantive request to decide which skills to read before working. Match the goal to one profile in the table and read ONLY those SKILL.md files. Triggers on any new task, topic pivot, or session start.
---

# Skill Router

Constraints are always in force — read them once per session if not already loaded:
`pavitas-core:safety-rails`, `pavitas-core:workspace-context`, `pavitas-core:output-quality`.

Match the user's goal to ONE profile. Read that profile's skills. Do not read others.

| Goal signal | Profile | Load |
|---|---|---|
| Morning greeting, "what's on today", "brief me" | morning-review | `pavitas-core:morning-review` (calls `pavitas-core:decision-framework` by reference) |
| New book, script uploaded, "new audiobook project" | audiobook-kickoff | `pavitas-core:audiobook-kickoff` → `audiobook-script-analyzer`, `audiobook-project-setup` (Cowork-native), `business-documentation` |
| Invoice, contract, client correspondence | biz-admin | `business-documentation` |
| Fiction drafting, "interview me", Jim & Percy, Story Grid work | story-session | `pavitas-core:story-session` (self-contained — interview and style-matching are inlined) |
| Social post, caption, content batch | content-pipeline | `pavitas-core:content-pipeline` → ONE brand voice (pavitas xor spins-yarns) |
| Zo work, MCP, automation, repo, skill maintenance | infra-session | `pavitas-core:infra-session` → `mcp-wrapper-builder`, `autoresearch` as needed |
| Scavenger hunt (planned group/date event) | play | `scavenger-hunt-designer` |
| Pocket hunt, noticing walk, quick hunt on the go | play | `pocket-hunt` |
| Pleasure hunt, intimate/foreplay/cruising hunt | play | `pleasure-hunt` |
| Conflict, "I'm spiraling", "help me think through", activation | support | `relational-emotional-regulation` ONLY |
| "Save handoff", "read handoff", session end | handoff | `pavitas-core:handoff` |
| Decision check, impulse purchase, time allocation | decide | `pavitas-core:decision-framework` |
| proofeditor.ai URL, "Proof doc", "open in Proof" (NOT proofread/proofing) | docs | `pavitas-core:proof` |
| "email brief", "morning email check", "what's in my inbox", "email briefing" | morning-briefing | `morning-briefing` (references `pavitas-core:using-slashy`) |
| "EOD wrapup", "end of day", "wrap up my day", "eod" | eod-wrapup | `eod-wrapup` (references `pavitas-core:using-slashy`) |
| "batch drafts", "draft multiple emails", "help me draft a few emails" | batch-draft | `batch-draft-writer` (references `pavitas-core:using-slashy`) |
| "schedule a meeting", "find time for a call", "book time with", "meeting scheduler" | meeting-scheduler | `meeting-scheduler` (references `pavitas-core:using-slashy`) |
| "deal tracker", "check my deals", "deal status", "open deals" | deal-tracker | `deal-tracker` (references `pavitas-core:using-slashy`) |

## Rules

- One profile per session unless the user pivots. On pivot, re-route.
- Never load both brand voices in one session.
- The **support** profile suppresses everything else — no router talk, no other skills, no task management. Just the skill.
- The three hunt skills are distinct systems, not variants. Route by the signals above; if ambiguous, ask which flavor.
- If no profile matches, proceed with constraints only. Don't force a skill onto a task that doesn't need one.
- Loading a profile means reading the orchestrator's SKILL.md; the orchestrator names which leaves to read and when. Don't pre-load leaves the orchestrator hasn't called for.

## Coverage manifest

Every installed skill must appear in this list with a routing home. A skill not listed here is invisible to the system — when installing or removing a skill, update this manifest in the same change. Any audit of the ecosystem starts by diffing installed skills against this list.

**pavitas-core (13):** skill-router (this file) · safety-rails, workspace-context, output-quality (always-on constraints) · morning-review, audiobook-kickoff, story-session, content-pipeline, infra-session (orchestrators) · handoff, decision-framework, proof (direct-routed) · using-slashy (shared Slashy mechanics reference — loaded by email skills).

**User skills (14):** audiobook-script-analyzer, audiobook-project-setup, business-documentation (audiobook-kickoff / biz-admin) · mcp-wrapper-builder, autoresearch (infra-session) · scavenger-hunt-designer, pocket-hunt, pleasure-hunt (play) · relational-emotional-regulation (support) · morning-briefing, eod-wrapup, batch-draft-writer, meeting-scheduler, deal-tracker (email-ops — all reference using-slashy).

**Brand plugins (2):** pavitas-content:pavitas-brand-voice, spins-yarns-content:spins-yarns-brand-voice (content-pipeline). spins-yarns-content also carries the crochet pattern/log/project commands (CLI-side; absorbed from fiber-arts-content 2026-06-10).

**Environment notes:** audiobook-project-setup is Cowork-native (needs Mac filesystem access); from Claude.ai, folder creation happens on Zo instead — see audiobook-kickoff. autoresearch runs in Claude Code.

**Removed — never reference:** writing-workshop (all four skills; interview/style-matching now live inside story-session), publisher-relations:publisher-profiles, enterprise-search (all three), daily-briefing, zo-workspace-orientation, design-elevation, humanize-prose (merged into output-quality), fiber-arts-content (merged into spins-yarns-content — its old voice guidance is dead; spins-yarns-brand-voice is the only voice source).
