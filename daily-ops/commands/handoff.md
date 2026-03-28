---
description: Create, read, or update session handoff notes in Notion Littlebird Log. Maintains continuity when switching between claude.ai (Web), Claude Code (CLI), and Cowork.
---

# Session Handoff

Manage session handoffs for cross-environment continuity.

## Detect Intent

- "read handoff" / "check handoff" / "where did we leave off" → READ
- "create handoff" / "save handoff" / "save our progress" → CREATE
- "update handoff" / "add to handoff" → UPDATE

## READ

1. Search Littlebird Log for most recent entry tagged "Session Handoff"
2. Present the full handoff content
3. Offer to pick up where it left off

## CREATE

1. Analyze current conversation autonomously — DO NOT ask Pavi to describe what happened
2. Detect primary project/topic by scanning for:
   - Audiobook project names (Exlian, DotF, etc.)
   - Writing projects (Jim & Percy, The Bookstore)
   - Story Grid work
   - Technical/workflow/skill building
   - Crochet projects
3. Extract:
   - Completed actions (created, fixed, built, decided, finished)
   - Open loops (started but unfinished, "next we should", TODOs)
   - Technical context (file paths, database IDs, code state)
   - Decisions made
4. Compose structured handoff:

```
🔄 [Project Name] - [Date] - [Environment]

## Environment
[Source] → [Target] (e.g., "claude.ai (Web) → Claude Code (CLI)")

## Session Focus
[1-2 sentence summary]

## What We Accomplished
- [Completed item]
- [Completed item]

## In Progress / Next Actions
- [ ] [Open task]
- [ ] [Open task]

## Context Notes
[Technical details, file locations, decisions the next session needs]
```

5. Present draft for review
6. On "save it" / "publish" → create in Littlebird Log with tag "Session Handoff"
7. AI summary field: one-sentence session summary

## UPDATE

1. Find most recent Session Handoff entry
2. Analyze conversation since that handoff
3. Move completed items from "In Progress" to "Accomplished"
4. Add new items to both sections
5. Present updated handoff for review
6. On approval, update the Notion page

## Topic Shift Detection

If conversation covered 2+ distinct topics:
- Ask: "One handoff covering both, or two separate handoffs?"
- If separate: create two Littlebird Log entries

## Environment Indicator in Title
- Web-created: `🔄 [Project] - [Date] - Web`
- CLI-created: `🔄 [Project] - [Date] - CLI`
- Cowork-created: `🔄 [Project] - [Date] - Cowork`
