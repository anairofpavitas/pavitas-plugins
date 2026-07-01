---
name: audiobook-script-analyzer
description: Analyze audiobook script PDFs or Word documents to extract chapter structure, word counts, and page counts. Use when the user uploads an audiobook script and wants to analyze it for narration prep, when they need chapter breakdowns, file naming conventions for audio files, word/page counts excluding front/back matter, or when they want to create chapters in Notion. Triggers include "analyze this script", "new audiobook project", "chapter breakdown", "audiobook analysis", or uploading a PDF/Word file with audiobook content.
---

# Audiobook Script Analyzer

Analyze audiobook scripts to extract chapter structure, generate file naming conventions, and optionally sync to Notion.

## Workflow

1. **Get input from user**
   - Script file (PDF, DOCX, or TXT)
   - Book short name — use EXACTLY as provided, never modify
   - May suggest options based on title patterns, but user's choice is final and used verbatim

2. **Run analysis script**
   ```bash
   python3 scripts/analyze_script.py "<filepath>" --short-name "<SHORT_NAME>" --output "<output.xlsx>"
   ```

3. **Review results with user**
   - Show summary: word count, page count, chapter count
   - Present chapter list showing ACTUAL detected page counts per chapter (not averages)
   - Confirm file naming looks correct

4. **Generate deliverables**
   - Excel spreadsheet (for copy/paste to Notion or standalone use)
   - Optionally create/update Notion records

## File Naming Convention

Format: `[File Number]_[Book Short Name]_[Chapter Title]`

### File Number — three digits, zero-padded

- **`000`** — Opening billboard, if the publisher provides one. Detect by scanning the project folder for `billboards*.pdf` or similar before numbering begins. Most major publishers (Aethon, Podium, Recorded Books, Blackstone, Audible direct) supply a billboard.
- **`001`** — First chapter or section. This might be a Prologue, Chapter 1, Introduction, or whatever appears first in the manuscript.
- Increments by 1 for every recorded item in the order it appears in the manuscript.
- **Sections include** Prologues, Epilogues, Interludes, Introductions, Afterwords, Parts/Acts — anything delineated as its own section (typically by bold or title-styled text). Always include these in the numbering sequence in source order.
- File number is NOT the same as chapter number when non-chapter sections exist. Example with billboard + prologue: `000_Billboard, 001_Prologue, 002_Chapter 1, 003_Chapter 2…`

### Book Short Name — verbatim

- Use the short name **exactly** as the user provided, preserving spaces, case, and punctuation.
- User says "Loop Bound 1" → `Loop Bound 1` (with spaces, if that's what they wrote) OR `LoopBound1` (no spaces, if that's what they wrote). Do not transform.
- User says "DotF16" → `DotF16`
- User says "Exlian Syndrome 5" → `Exlian Syndrome 5`
- NEVER shorten, abbreviate, strip spaces, change case, or otherwise modify the short name.

### Chapter/Section Title — header only

- Use the title text as it appears in the manuscript.
- **Strip subtitles.** Anything after a delimiter (`:`, `—`, `-`) following the main header is a subtitle and gets removed.
  - `Chapter 1: A dark day` → `Chapter 1`
  - `Chapter 7 — The Long Climb` → `Chapter 7`
  - `Epilogue: What's to Come` → `Epilogue`
- **If the header is only a number, do NOT add the word "Chapter".**
  - Source `3` → `3` (file name fragment), full file name `003_Pretend Book 2_3`
- **Special section names stand alone:** `Prologue`, `Epilogue`, `Interlude`, `Introduction`, `Afterword`, `Billboard`.
- **POV-split duplicates** (e.g., dual-POV books where Ch 19 splits into Logan and Alyndra POV chapters): retain the POV indicator so each file name is unique. `Chapter 19` and `Chapter 19 Alyndra` are distinct chapter titles, both valid. Flag the user for confirmation.
- Remove invalid filename characters: `: / \ < > " | ? *`

### Examples

Standard book (no billboard):
- `001_DotF16_Prologue`
- `002_DotF16_Chapter One`
- `015_Exlian Syndrome 4_Interlude`
- `048_Stray Cat Strut 7_Epilogue`

Book with publisher billboard:
- `000_LoopBound1_Billboard`
- `001_LoopBound1_Chapter 1`
- `036_LoopBound1_Epilogue`

Book where chapter headers are just numbers:
- `001_Pretend Book 3_1`
- `069_Pretend Book 3_Epilogue`

## Chapter Detection

The script detects these section types:
- Prologue, Epilogue, Interlude, Introduction, Afterword
- "Chapter One", "CHAPTER 1", "Chapter Twenty-Three", etc.
- Part markers (Part One, Part 1)
- Act markers (Act One, Act 1)

Front matter (before first chapter) and back matter (after last chapter/epilogue) are automatically excluded from word/page counts.

**Page counts are actual detected values** — the script identifies where each chapter starts and ends in the PDF and calculates exact page counts, not estimates or averages.

## Notion Integration

When user wants Notion sync:

### 1. Search for existing book
```
Search Audiobook Projects database for book title (long or short form)
Database URL: https://www.notion.so/a33eb55fdef34b19852484ddde4c3be8
Data source: collection://28321020-d7f5-4619-aafd-28c3faccf815
```

### 2. Create book if not found
Create page in Audiobook Projects with:
- `Project name`: Full book title
- `Book Short Title`: Short name used for files
- `Word Count`: Total from analysis (excluding front/back matter)
- `Manuscript Pages`: Total story pages from analysis
- `Status`: "Standing By"

### 3. Create chapters
For each chapter (including the billboard at 000 if present), create page in Chapters database:
- Data source: `collection://a9ad76f7-aa1c-4423-9c7b-71905a721958`
- `Chapter Title` (Notion title property): full **file name** from this analysis (e.g., `001_LoopBound1_Chapter 1`). NOT just the chapter heading. The file name IS the Notion record name.
- `Numbers`: file number (0 for billboard, 1+ for sections in appearance order)
- `Pages`: page count for that chapter
- `Chapter Word count`: word count for that chapter
- `Project`: Relation to the audiobook record
- `Status`: "Record"

### 4. Update book if fields empty/incorrect
If book already exists, ALWAYS check and update these fields:
- `Book Short Title` — set to the short name used for files
- `Word Count` — set to total from analysis (excluding front/back matter)  
- `Manuscript Pages` — set to total story pages from analysis

Update any that are empty or have different values than the analysis.

### 5. Distribute chapters across workdays (default)

Runs automatically during project onboarding. Skip only if the user explicitly opts out. This is the single source of truth for the recording schedule — no Google Calendar duplication.

**Prerequisites:**
- Book record must have `Dates` field populated (start_date, end_date)
- `Pages per day` is **optional**. If present on the book record (formula or manual override), use it as the daily target. If absent, auto-compute: `target = ceil(total_pages / weekday_count)`.

**Algorithm:**
1. Get date range from book's `Dates` field (start_date → end_date)
2. Generate weekdays (Mon–Fri) from start_date through end_date INCLUSIVE. **Both endpoints are valid recording days** — the end_date is BOTH the last recording day AND the delivery day. Skip Saturdays and Sundays.
3. Determine `target` pages-per-day (see Prerequisites above)
4. Assign chapters to workdays in chronological order (by `Numbers` field):
   - For each weekday, add chapters until cumulative pages ≥ target
   - Move to next weekday and repeat
   - Continue until all chapters are assigned
5. Update each chapter's `Work Date` field
6. Verify: every chapter has a Work Date, none falls on a weekend, last Work Date ≤ end_date

**Example:**
- Book dates: January 6-16, 2026
- Pages per day: 39
- Workdays: Jan 6 (Mon), 7 (Tue), 8 (Wed), 9 (Thu), 10 (Fri), 13 (Mon), 14 (Tue), 15 (Wed), 16 (Thu)
- Chapter 1 (7 pages) + Chapter 2 (8 pages) + Chapter 3 (7 pages) + Chapter 4 (9 pages) + Chapter 5 (7 pages) = 38 pages → Jan 6
- Chapter 6 (8 pages) + Chapter 7 (8 pages) + Chapter 8 (8 pages) + Chapter 9 (8 pages) + Chapter 10 (9 pages) = 41 pages → Jan 7
- ...and so on

**Notes:**
- Chapters are assigned in sequential order (by Numbers field)
- Each chapter gets exactly one work date
- Distribution aims for roughly equal pages per day but won't be perfect
- Last workday may have fewer or more pages depending on remainder

## Dependencies

Required Python packages:
- `pdfplumber` - PDF text extraction
- `python-docx` - Word document handling  
- `openpyxl` - Excel spreadsheet generation

Install with:
```bash
pip install pdfplumber python-docx openpyxl --break-system-packages
```

## Output

The spreadsheet contains:
1. **Summary section** (top)
   - Book title and short name
   - Total word count (story only)
   - Total story pages
   - Number of chapters
   - Front/back matter page counts

2. **Chapter table**
   - Sequential number
   - Chapter title
   - Generated file name
   - Page count
   - Start/end pages
   - Word count
