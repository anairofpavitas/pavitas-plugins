---
name: handoff
description: Manage session handoffs between claude.ai (Web) and Claude Code (CLI) via the Notion Littlebird Log. Triggers on "read handoff", "create handoff", "save handoff", "update handoff", "check what we left off on", "where did we leave off", and natural variations. Composes handoff notes autonomously from the conversation — no manual input required.
---

# Session Handoff

A good handoff is a hospital shift change: the other Claude picks up with zero hunting and zero re-explaining.

## Notion target

- **Database:** Littlebird Log (IDs in `pavitas-core:workspace-context`)
- **Title:** `🔄 [Project] - [Date] - Web` (CLI sessions use `- CLI`)
- **Tags:** "Session Handoff" (multi-select — pass values as a JSON array string, e.g. `["Session Handoff"]`) · **AI Summary field:** one-sentence session summary
- Search: query "Session Handoff" against the Littlebird data source. Create: new page in that data source with the properties above and the handoff markdown as content. Update: replace content / update properties on the found page.

## Read

1. Find the most recent "Session Handoff" entry.
2. Present it, flag its age if >3 days, offer to continue from where it left off.

## Create

1. Analyze the conversation autonomously — extract:
   - **Project** (Exlian Syndrome, DotF, Story Grid work, infra, etc. — detect from content)
   - **Accomplished** — files created, decisions made, tasks finished
   - **In progress / next** — open loops, explicit next steps, half-done work
   - **Context the other environment needs** — file paths, IDs, API details, code state, blockers
2. Compose in this structure:

```markdown
## Environment
[Web | CLI] — [date, America/Chicago]

## Session Focus
[One or two sentences]

## What We Accomplished
- [Concrete, past-tense items]

## In Progress / Next Actions
- [ ] [Actionable, specific — paths and IDs included]

## Context Notes
[Anything the other Claude can't infer: gotchas, decisions and their reasons, state]
```

3. Present the draft for review. On approval, save and confirm with the link.

**Multi-topic sessions:** related topics → one handoff. Genuinely distinct topics → ask: one combined or two separate?

## Update

Find today's (or the named) handoff entry, merge new progress into the existing sections — don't duplicate, don't lose prior content. Present the delta, save on OK.

## Rules

- Never save without showing the draft first.
- Specifics over summaries: "Created `skills/skill-router/SKILL.md`, 40 lines" beats "worked on skills."
- Include exact IDs and paths — the other environment has no conversation memory.
- One sentence in the AI field, written for a six-week-later skim.
