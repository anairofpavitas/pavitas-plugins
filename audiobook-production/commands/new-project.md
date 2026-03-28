---
description: Full parallel project onboarding for a new audiobook. Analyzes script, creates folder structure, populates Notion databases, sets calendar milestones, and drafts publisher confirmation email.
---

# New Audiobook Project Setup

Run this command when Pavi receives a new audiobook project. This orchestrates the full onboarding pipeline.

## Required Input

Ask Pavi for:
1. **Script file** — PDF or DOCX uploaded or path provided
2. **Book short name** — Suggest based on title (first letters of each word, e.g., "Defiance of the Fall" → DotF). For series, append book number (e.g., Exlian5)
3. **Publisher** — Check Notion Audiobook Projects for existing publisher records
4. **Deadline** — Recording window and final delivery date
5. **Rate** — Default $350 PFH unless specified otherwise

## Parallel Execution Plan

Spawn these sub-agents simultaneously:

### Agent 1: script-scout
- Analyze uploaded script for chapter structure
- Extract word count (excluding front/back matter)
- Detect chapters, prologues, epilogues, interludes
- Generate file naming convention: `[###]_[ShortName]_[Chapter Title]`
- No subtitles in file names — header only
- Output: chapter list with page counts, file names, total word count

### Agent 2: production-tracker
- Search Notion Audiobook Projects for existing book record
- If found: update fields (short title, word count, manuscript pages)
- If not found: create new record with Status = "Standby"
- Create chapter records in Notion Chapters database
  - Each chapter: record name, quantity of pages, Status = "Record"
  - Relate each chapter to the parent book record

### Agent 3: folder-setup
- Create standardized folder structure:
  ```
  [Book Short Name]/
  ├── Assets/
  ├── Chapters/
  └── CRX/
  ```

### Agent 4: calendar-setup
- Create recording block events on Studio calendar
- Set delivery deadline event with 48-hour warning reminder
- If deadline is tight (< 2 weeks for > 100k words), flag it

## After All Agents Complete

1. **Generate QC spreadsheet** — Excel file with chapter rows (title, file name, page count)
2. **Present summary** to Pavi for review:
   - Total word count → estimated finished hours (word count ÷ 9,300 = approx PFH)
   - Chapter count
   - Recording window with deadline
   - Estimated invoice amount (PFH × rate)
3. **Draft publisher confirmation email** — confirm receipt of manuscript, recording window, expected delivery date
4. Present email draft in Biz Mode (full review before sending)

## Edge Cases

- If script has graphical chapter headers, flag for manual review
- If chapter numbering is inconsistent, present best guess and ask for confirmation
- If book is part of a series, check Notion for previous books in series to maintain naming consistency
