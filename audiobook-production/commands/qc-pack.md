---
description: Generate a QC spreadsheet package for the active audiobook project. Creates Excel file with chapter rows, hyperlinks to audio files, and status tracking columns.
---

# QC Pack Generator

Produces the Quality Control spreadsheet that accompanies audio file delivery. Used during self-QC and for publisher QC review.

## Required Input

- **Project** — auto-detect from active project in Notion, or ask Pavi
- **Audio file location** — local path to the Chapters folder containing recorded files
- **QC type** — "self" (Pavi's own review) or "publisher" (for delivery)

## Spreadsheet Structure

Each row = one chapter file:

| Column | Content |
|--------|---------|
| File Number | 001, 002, etc. |
| File Name | Full filename (e.g., `001_DotF16_Prologue`) |
| Chapter Title | Chapter title as it appears in script |
| Pages | Page count from script analysis |
| Audio Link | Hyperlink to local audio file (for self-QC) |
| Status | Blank for publisher QC; checkable for self-QC |
| Pickup Notes | Column for flagging retakes needed |
| Timestamp | Where in the file the issue occurs |

## Execution Steps

1. Pull chapter data from Notion Chapters database for the active project
2. Scan the audio file directory for matching filenames
3. Match chapter records to audio files
4. Flag any mismatches (chapter in Notion but no audio file, or audio file with no chapter record)
5. Generate Excel file using openpyxl:
   - Hyperlinks use local file paths (not URLs) for macOS compatibility
   - Note: macOS sandbox restrictions may prevent hyperlinks from opening directly — include a note about this in the spreadsheet header
6. For publisher QC: omit audio links, include only file name and status columns
7. Save to project's CRX folder

## Output

- Excel file: `[ShortName]_QC_Pack_[Date].xlsx`
- Summary: total files, any missing/extra files flagged
- If mismatches found, present them before generating the file

## Known Constraints

- macOS sandbox restrictions can block hyperlink-to-local-file functionality in some apps
- If generating for Blackstone delivery, use their FTP folder naming convention
- For Audible direct, include ACX spec compliance notes (RMS, noise floor, peak levels)
