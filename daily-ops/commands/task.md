---
description: Quick task capture to Notion Tasks database. Takes natural language task description and creates it immediately with Status=Inbox.
---

# Quick Task Capture

Instant task creation. No fuss.

## Usage

Pavi says something like:
- "Task: call Michelle about Q1 taxes"
- "Add to tasks: order new pop filter"
- "Remember to email Julie about DotF 17 deadline"
- "To do: submit scene to Joanne by Friday"

## Execution

1. Extract task description from natural language
2. Extract deadline if mentioned (convert to America/Chicago timezone)
3. Create in Notion Tasks database:
   - Title: task description
   - Status: "Inbox"
   - Due date: if mentioned
   - Tags: auto-detect (audiobook, writing, personal, business, crochet)
4. Confirm creation with one line: "✅ Added to Inbox: [task]"

## Rules

- Don't ask for clarification unless genuinely ambiguous
- Default to Status = "Inbox" always
- If Pavi says "urgent" or "today", still use Inbox but add a priority flag if the field exists
- If the task references a specific project, add the project relation if possible
- Data source ID for Tasks: 2ff089eb-3ccc-8121-9f00-000b2cf26253
