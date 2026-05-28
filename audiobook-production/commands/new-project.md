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
- If not found: create new record with Status = "Standby" (or "Standing By" — match the actual DB option)
- Create chapter records in Notion Chapters database
  - Each chapter: record name, quantity of pages, Status = "Record"
  - Relate each chapter to the parent book record
- **Assign `Work Date` on each chapter record** to match the recording schedule produced by Agent 4 (calendar-setup). Each chapter's Work Date = the calendar day Pavi is recording it. Distribute chapters across the recording window in the same order they appear in the book.

### Agent 3: folder-setup
- Create standardized folder structure:
  ```
  [Book Short Name]/
  ├── Assets/
  ├── Chapters/
  └── CRX/
  ```

### Agent 4: calendar-setup
- **BEFORE creating any events:** pull all events from Pavi's other calendars (primary `pavi@paviproczko.com`, Events `c_fb4b7a14c6d341ed9afa87061b525156db2058eaab394d54c349211cc5c26106@group.calendar.google.com`, Colin's `colin.t.funk@gmail.com`, plus Bookings & Rehearsal if accessible) across the full recording window. Treat any opaque (non-transparent) event as a hard block. Transparent all-day banners (NYC Potential, Camp Run A Pup, MCA Free Day) don't block.
- Plan recording blocks that avoid those conflicts. Default Pavi's recording window to 10 AM–12 PM CT when clear; shift the same day if a morning conflict exists rather than skipping the day.
- Create recording block events on Studio Schedule calendar (`paviproczko.com_pvq1muo01o05os0nvnq4tqrkko@group.calendar.google.com`)
- Set delivery deadline event with 48-hour warning reminder
- After placement, **re-verify no overlap** with primary/Events/Colin's calendars; report any unavoidable conflicts to Pavi instead of silently leaving them
- Output the final per-day chapter assignment back to Agent 2 so chapter Work Dates can be populated
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
