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
| New book, script uploaded, "new audiobook project" | audiobook-kickoff | `pavitas-core:audiobook-kickoff` → `audiobook-script-analyzer`, `audiobook-project-setup`, `business-documentation`, `publisher-relations:publisher-profiles` |
| Invoice, contract, publisher correspondence | biz-admin | `business-documentation`, `publisher-relations:publisher-profiles` |
| Fiction drafting, "interview me", Jim & Percy, Story Grid work | story-session | `pavitas-core:story-session` → `writing-workshop:*` as directed |
| Social post, caption, content batch | content-pipeline | `pavitas-core:content-pipeline` → ONE brand voice (pavitas xor spins-yarns) |
| Zo work, MCP, automation, repo, skill maintenance | infra-session | `pavitas-core:infra-session` → `mcp-wrapper-builder`, `autoresearch` as needed |
| Scavenger hunt (planned group/date event) | play | `scavenger-hunt-designer` |
| Pocket hunt, noticing walk, quick hunt on the go | play | `pocket-hunt` |
| Pleasure hunt, intimate/foreplay/cruising hunt | play | `pleasure-hunt` |
| Conflict, "I'm spiraling", "help me think through", activation | support | `relational-emotional-regulation` ONLY |
| "Save handoff", "read handoff", session end | handoff | `pavitas-core:handoff` |
| Decision check, impulse purchase, time allocation | decide | `pavitas-core:decision-framework` |
| proofeditor.ai URL, "Proof doc", "open in Proof" (NOT proofread/proofing) | docs | `pavitas-core:proof` |

## Rules

- One profile per session unless the user pivots. On pivot, re-route.
- Never load both brand voices in one session.
- The **support** profile suppresses everything else — no router talk, no other skills, no task management. Just the skill.
- The three hunt skills are distinct systems, not variants. Route by the signals above; if ambiguous, ask which flavor.
- If no profile matches, proceed with constraints only. Don't force a skill onto a task that doesn't need one.
- Loading a profile means reading the orchestrator's SKILL.md; the orchestrator names which leaves to read and when. Don't pre-load leaves the orchestrator hasn't called for.
