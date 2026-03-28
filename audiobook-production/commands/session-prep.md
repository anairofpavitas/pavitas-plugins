---
description: Prepare for a recording session. Pulls today's chapters from Notion, checks deadline proximity, loads pickup notes from last session, and surfaces any publisher communications.
---

# Recording Session Prep

Run before sitting down at the mic. Gets Pavi oriented on where he left off and what's ahead.

## Execution Steps

1. **Check Notion Audiobook Projects** for the active project (Status = "In Production" or most recent)
2. **Pull chapter status** from Chapters database:
   - Which chapters are marked "Record" (not yet started)
   - Which chapters are marked "Done"
   - Current completion percentage
3. **Check for pickups** — search Notion and local files for any flagged retake notes from previous sessions
4. **Calculate deadline math**:
   - Days remaining until delivery
   - Estimated hours remaining (remaining chapters × avg pages per chapter ÷ pages-per-hour rate)
   - Flag if pace needs to increase
5. **Check Gmail** for any recent publisher emails about the active project (last 48 hours)
6. **Check Google Calendar** for today's recording blocks and any conflicts

## Output Format

```
🎙️ SESSION PREP — [Book Title] ([Short Name])

📊 Progress: [X]/[Total] chapters complete ([%])
📅 Deadline: [Date] — [N] days remaining
⏱️ Estimated remaining: ~[N] hours

📋 NEXT UP
- [File Number]_[ShortName]_[Chapter Title] — [N] pages
- [File Number]_[ShortName]_[Chapter Title] — [N] pages
- [File Number]_[ShortName]_[Chapter Title] — [N] pages

🔧 PICKUPS FROM LAST SESSION
- [Any flagged retakes or notes]
- [Or "None — clean session"]

📧 PUBLISHER UPDATES
- [Any recent emails, or "No new communications"]

💡 PACE CHECK
- [On track / Need to increase pace / Ahead of schedule]
```

## Notes

- If it's a Tuesday or Friday, note that dogs are at camp — clear runway for recording
- If therapy or other appointments are on today's calendar, note the available recording windows around them
- Never interrupt a recording session suggestion with non-production items
