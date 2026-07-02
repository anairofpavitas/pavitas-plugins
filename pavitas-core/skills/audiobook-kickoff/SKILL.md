---
name: audiobook-kickoff
description: End-to-end intake orchestrator for a new audiobook narration project. Triggers when a script (PDF/Word) arrives with "new project", "new book", "set this one up", or a client confirms a booking. Chains script analysis, folder setup, Notion records, and business docs. Calls leaf skills — does not duplicate their logic.
---

# Audiobook Kickoff

Sequence for standing up a new Pavitas Productions project. Read each leaf skill at its step; don't improvise past them.

## 0. Intake

Confirm or extract: title, author, client, deadline, script file. Rate is $350/PFH unless Pavi says otherwise — flag any deviation, don't absorb it silently.

Missing facts get asked or flagged. Never invented (deadline, client contact, contract terms, delivery method). For client context, check the Audiobook Projects DB for prior projects with the same client.

## 1. Script analysis

Spawn `audiobook-production:script-scout` (Task tool, `subagent_type: script-scout`) with the script file. It runs the full chapter-structure analysis per its own File Naming Convention (source of truth: `audiobook-production:audiobook-script-analyzer`) and returns chapter list, file names, per-chapter page counts, and total word count excluding front/back matter. Compute the estimate yourself from its word count — script-scout returns raw counts, not rate math: estimated finished hours = word count ÷ ~9,300 words/finished hour (a starting estimate — label it as such).

## 2. Folders

`audiobook-production:audiobook-project-setup` is Cowork-native (it needs Mac filesystem access) — from Cowork, read and follow it. From Claude.ai, create the same structure on Zo under `/home/workspace/Audiobooks/[Title]/`:

```
[Short Title]/
├── [Short Title] Assets
├── [Short Title] Chapters
└── [Short Title] CRX
```

If Pavi wants the folders on his Mac and the session is in Claude.ai, note it as a Cowork follow-up rather than improvising access.

## 3. Notion records

If Work Dates are wanted, propose a schedule back-planned from the deadline with a 2-chapter buffer yourself — this is a judgment call, not something to hand off. Present it and get Pavi's explicit OK before anything gets written.

Then spawn `audiobook-production:production-tracker` (Task tool, `subagent_type: production-tracker`) with: script-scout's chapter output, book metadata (title, author, client, deadline, PFH estimate, status), and the approved Work Dates if any. It searches for an existing book record, creates or updates the Audiobook Projects entry, and creates one Chapters DB entry per chapter (relation property `nMOv`) with the naming-convention filenames and word counts. IDs in `pavitas-core:workspace-context`.

## 4. Business docs (when applicable)

If a contract or invoice is needed now, read `business-documentation`. Otherwise note the invoice trigger (usually on delivery) in the project entry.

## 5. Close

Report: chapters created (count), folder path, Notion links, deadline math (chapters/day required), and `⚠️ Gaps:` for anything unverified. Offer a handoff if setup continues in Claude Code or Cowork.

## Verification before reporting done

- Spot-check 3 chapters: word counts match the script (compare against script-scout's returned data — no need to re-read the manuscript).
- Front/back matter excluded from PFH math.
- Folder tree matches the structure above exactly.
- Chapter count in Notion equals chapter count in script-scout's output.
