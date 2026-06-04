---
description: Full parallel project onboarding for a new audiobook. Analyzes script, creates folder structure, populates Notion databases, and drafts publisher confirmation email.
---

# New Audiobook Project Setup

Run this command when Pavi receives a new audiobook project. This orchestrates the full onboarding pipeline.

## Required Input

Ask Pavi for:
1. **Script file** — PDF or DOCX uploaded or path provided
2. **Book short name** — Suggest based on title (first letters of each word, e.g., "Defiance of the Fall" → DotF). For series, append book number (e.g., Exlian5). Use the user's chosen short name VERBATIM in all downstream operations (no spacing/case modifications).
3. **Publisher** — Check Notion Audiobook Projects for existing publisher records
4. **Project dates** — Start date and end date for the recording window. The END date is BOTH the last recording day AND the delivery day (it's a valid recording day, not a buffer).
5. **Rate** — Default $350 PFH unless specified otherwise

## Parallel Execution Plan

Spawn these three sub-agents simultaneously:

### Agent 1: script-scout
- Analyze uploaded script for chapter structure
- Extract word count (excluding front/back matter)
- Detect chapters, prologues, epilogues, interludes, opening billboards
- Generate file names per `skills/audiobook-script-analyzer/SKILL.md` § "File Naming Convention" — that document is the source of truth. Key rules: opening billboard = `000`, first section = `001`, three-digit zero-padded sequential, short name VERBATIM, subtitles stripped, no "Chapter" prefix when header is just a number, POV indicator retained on POV-split duplicates.
- Output: chapter list with page counts, file names, total word count, plus a billboard entry (000) if one is present in the project folder

### Agent 2: production-tracker
- Search Notion Audiobook Projects for existing book record
- If found: update fields (short title, word count, manuscript pages)
- If not found: create new record with Status = "Standing By" (the actual Notion option)
- Create chapter records in Notion Chapters database
  - **Record Name = file name from script-scout output** (full file name, e.g., `001_LoopBound1_Chapter 1` — NOT just the chapter heading)
  - Set Numbers, Pages, Chapter Word count, Status = "Record"
  - Relate each chapter to the parent book record
- **Distribute Work Dates across weekdays.** Using the book record's `Dates` field (start → end), generate all weekdays in the range (Mon–Fri, both endpoints inclusive as valid recording days). Distribute chapter records across those weekdays roughly evenly by page count, in chapter order. Algorithm spec: `skills/audiobook-script-analyzer/SKILL.md` § "Distribute chapters across workdays". This runs automatically — no user gate, no Google Calendar involvement.

### Agent 3: folder-setup
- Create standardized folder structure:
  ```
  [Book Short Name]/
  ├── Assets/
  ├── Chapters/
  └── CRX/
  ```

## After All Agents Complete

1. **Generate QC spreadsheet** — Excel file with chapter rows (title, file name, page count)
2. **Present summary** to Pavi for review:
   - Total word count → estimated finished hours (word count ÷ 9,300 = approx PFH)
   - Chapter count (including billboard if present)
   - Recording window: start → end (end = delivery day)
   - Per-day chapter distribution (so Pavi can sanity-check the schedule before it ships in Notion)
   - Estimated invoice amount (PFH × rate)
3. **Draft publisher confirmation email** — confirm receipt of manuscript, recording window, expected delivery date
4. Present email draft in Biz Mode (full review before sending)

## Edge Cases

- If script has graphical chapter headers, flag for manual review
- If chapter numbering is inconsistent, present best guess and ask for confirmation
- If book is part of a series, check Notion for previous books in series to maintain naming consistency
