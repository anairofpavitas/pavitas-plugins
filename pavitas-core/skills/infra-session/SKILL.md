---
name: infra-session
description: Infrastructure work orchestrator — Zo Computer operations, MCP wrappers, automations, skill maintenance, repo work. Triggers on "Zo work", "build a wrapper", "fix the automation", "update the skill", "repo", or any agent-ecosystem engineering request. Enforces the split-brain rule and changelog discipline.
---

# Infra Session

## Architecture rule (the split-brain fix)

Claude reasons and decides; Zo executes mechanically through the proxy tools. Don't ask Zo's agent to plan or reason — send it concrete commands (`Zo Computer:bash`, `read_file`, `write_file`). Don't replicate Zo-side state in your head — read it.

## Route by task

| Task | Read and follow |
|---|---|
| New MCP wrapper on zo.space | `mcp-wrapper-builder` (OAuth-shim avenue is the default) |
| Zo-side workflow that has a skill | `pavitas-core:workspace-context` → `references/zo-skill-index.md`, then the Zo skill |
| Skill creation/editing | `/mnt/skills/examples/skill-creator/SKILL.md` for authoring; this repo's conventions for structure |
| Skill optimization with evals | `autoresearch` against the rubric in the target skill's `references/rubric.md` (or §rubrics in the repo README) |
| Scheduled agent / cron | Zo `Skills/zo-automate-something`. Cron strings are UTC — convert from America/Chicago explicitly and state both in comments |

## Session discipline

1. **Before changing anything:** read the current state of the file/route/automation. Never edit from memory of a past session.
2. **Destructive ops** (delete route, drop table, overwrite skill): preview the exact change, get the OK (`pavitas-core:safety-rails`).
3. **After changes:** smoke test (wrapper → connection test; skill → trigger test; automation → dry run where possible). State what was verified, not what should work.
4. **Changelog:** skills changes → `skills/CHANGELOG.md`; plugin/root → root `CHANGELOG.md`. Every session that touches the repo writes an entry.
5. **Memory:** the moment a save-worthy decision or fact lands (a model choice, a tool/route decision, a resolved tradeoff) — not only at close — run `pavitas-core:memory-capture`.
6. **Close:** if mid-task, write a `pavitas-core:handoff`. Infra half-states are expensive to reconstruct.

## Model selection (when creating agents)

Claude subscription models: Opus for complex reasoning, Sonnet for moderate, Haiku for simple/high-volume. Justify anything else.
