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

- **File Number**: Three digits, starting at 001, incrementing sequentially
  - Prologue = 001, Chapter 1 = 002 (if prologue exists)
  - Interludes increment the count: Ch7 = 007, Interlude = 008, Ch8 = 009
  - Epilogue follows last chapter number
  
- **Book Short Name**: Use EXACTLY as user provides — no modifications
  - User says "DotF16" → use "DotF16"
  - User says "Exlian Syndrome 5" → use "Exlian Syndrome 5"
  - User says "Obelisk" → use "Obelisk"
  - NEVER shorten, abbreviate, or adjust the short name in any way

- **Chapter Title**: Header only, no subtitles
  - Keep as appears: "Chapter Seven" or "Chapter 7" based on source
  - Remove invalid filename characters (: / \ < > " | ? *)

Examples:
- `001_DotF16_Prologue`
- `002_DotF16_Chapter One`
- `015_Exlian Syndrome 4_Interlude`
- `048_Stray Cat Strut 7_Epilogue`

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
For each chapter, create page in Chapters database:
- Data source: `collection://a9ad76f7-aa1c-4423-9c7b-71905a721958`
- `Chapter Title`: Chapter header as it appears
- `Pages`: Page count for that chapter
- `Project`: Relation to the audiobook record
- `Status`: "Record"

### 4. Update book if fields empty/incorrect
If book already exists, ALWAYS check and update these fields:
- `Book Short Title` — set to the short name used for files
- `Word Count` — set to total from analysis (excluding front/back matter)  
- `Manuscript Pages` — set to total story pages from analysis

Update any that are empty or have different values than the analysis.

### 5. Distribute chapters across workdays (optional)

When user wants work dates assigned to chapters:

**Prerequisites:**
- Book record must have `Dates` field populated (start and end date)
- Book record has calculated `Pages per day` field

**Algorithm:**
1. Get date range from book's `Dates` field (start → end)
2. Generate list of weekdays only (Monday-Friday) within that range — skip weekends
3. Get `Pages per day` target from book record
4. Assign chapters to workdays in chronological order:
   - For each weekday, add chapters until cumulative pages ≥ pages-per-day target
   - Move to next weekday and repeat
   - Continue until all chapters are assigned
5. Update each chapter's `Work Date` field

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
