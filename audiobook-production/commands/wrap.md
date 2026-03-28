---
description: Wrap up a completed audiobook project. Marks chapters complete in Notion, calculates finished hours, generates invoice, and drafts delivery confirmation email to publisher.
---

# Project Wrap

Run when all chapters are recorded, QC'd, and ready for delivery. Handles the administrative close-out.

## Execution Steps

### 1. Verify Completion
- Pull all chapters from Notion for this project
- Confirm every chapter Status = "Done"
- If any chapters are not "Done", list them and ask Pavi to confirm they should be marked complete

### 2. Calculate Finished Hours
- Sum total audio duration across all chapter files
- If audio files are accessible, calculate from actual file durations
- If not, estimate from page count (industry average: ~2.5 pages per finished minute, or ~150 pages per finished hour — but confirm with Pavi as his pace varies)
- Present: total finished hours, total pages, words per finished hour

### 3. Update Notion
- Set project Status to "Delivered" (or "Final QC" if awaiting publisher review)
- Update finished hours field
- Record delivery date

### 4. Generate Invoice
- Use the business-documentation skill
- Pull publisher billing info from stored profiles
- Calculate: finished hours × PFH rate ($350 default)
- Apply any negotiated adjustments
- Include project title, book number, author name
- Output: branded PDF invoice with Pavitas Productions logo

### 5. Draft Delivery Email
- Professional tone, signed as "Pavi"
- Include: project title, total finished hours, delivery method confirmation
- Attach or reference the invoice
- If delivering via Box: confirm upload location
- If delivering via FTP (Blackstone): confirm FTP upload complete
- Present in Biz Mode for review before sending

### 6. Archival
- Suggest moving project folder to completed/archive location
- Update any tracking spreadsheets if maintained

## Output

Present a wrap summary:
```
📦 PROJECT WRAP — [Book Title]

✅ Chapters: [X] complete
⏱️ Finished Hours: [N] FH
💰 Invoice: $[Amount] ($350 × [N] PFH)
📧 Delivery email: drafted for review
📁 Files: [delivery method and location]
```
