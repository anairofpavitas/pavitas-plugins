---
name: audiobook-kickoff
description: End-to-end intake orchestrator for a new audiobook narration project. Triggers when a script (PDF/Word) arrives with "new project", "new book", "set this one up", or a publisher confirms a booking. Chains script analysis, folder setup, Notion records, and business docs. Calls leaf skills — does not duplicate their logic.
---

# Audiobook Kickoff

Sequence for standing up a new Pavitas Productions project. Read each leaf skill at its step; don't improvise past them.

## 0. Intake

Confirm or extract: title, author, publisher (load `publisher-relations:publisher-profiles` for contacts/terms), deadline, script file. Rate is $350/PFH unless the publisher profile or Pavi says otherwise — flag any deviation, don't absorb it silently.

Missing facts get asked or flagged. Never invented (deadline, publisher contact, contract terms).

## 1. Script analysis

Read and follow `audiobook-script-analyzer`. Output: chapter structure, per-chapter word counts, total words/pages excluding front/back matter, file naming convention, estimated finished hours (word count ÷ ~9,300 words/finished hour as a starting estimate — label it an estimate).

## 2. Folders

Read and follow `audiobook-project-setup` (Assets / Chapters / CRX structure). On Zo, create under `/home/workspace/Audiobooks/[Title]/`.

## 3. Notion records

In Audiobook Projects DB: project entry with title, author, publisher, deadline, PFH estimate, status. In Chapters DB: one entry per chapter, related to the project (relation property `nMOv`), with word counts and naming-convention filenames. IDs in `pavitas-core:workspace-context`. If Work Dates are wanted, propose a schedule back-planned from the deadline with a 2-chapter buffer; Pavi approves before writing dates.

## 4. Business docs (when applicable)

If a contract or invoice is needed now, read `business-documentation`. Otherwise note the invoice trigger (usually on delivery) in the project entry.

## 5. Close

Report: chapters created (count), folder path, Notion links, deadline math (chapters/day required), and `⚠️ Gaps:` for anything unverified. Offer a handoff if setup continues in Claude Code.

## Verification before reporting done

- Spot-check 3 chapters: word counts match the script.
- Front/back matter excluded from PFH math.
- Folder tree matches the setup skill's spec exactly.
- Chapter count in Notion equals chapter count in the analysis.
