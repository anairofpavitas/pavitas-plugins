---
description: Transcribe a crochet pattern from a YouTube video URL or website. Output as a properly formatted standard crochet pattern document (PDF or Notion entry).
---

# Pattern Transcription

Convert video tutorials or web patterns into standard written crochet pattern format.

## Input
- YouTube URL (will fetch and transcribe)
- Website URL (will scrape pattern content and images)
- Verbal description from Pavi

## Output Format: Standard Crochet Pattern

Every pattern document must include:

1. **Header**: Pattern name, designer credit, source URL
2. **Materials**: Yarn type/weight, hook size, other supplies
3. **Gauge/Tension**: If mentioned
4. **Finished Size**: If mentioned
5. **Abbreviations**: All abbreviations used, defined (US terms default)
6. **Special Stitches**: Any non-standard stitches with instructions
7. **Pattern Body**: Complete step-by-step instructions with stitch counts
   - Organized by rows/rounds
   - Stitch counts in parentheses at end of each row/round
   - Clear section breaks for repeating patterns
8. **Finishing**: Assembly, blocking, weaving in ends
9. **Notes**: Any tips from the original tutorial

## Formatting Rules
- Use US crochet terminology (sc, dc, hdc, etc.) unless Pavi specifies UK terms
- Include stitch counts at end of every row/round
- For mosaic crochet: include chart notes and color change instructions
- For Tunisian crochet: specify forward and return passes separately
- Sanitize for clean PDF output via the pdf skill

## Storage
- Save formatted pattern to crochet/ folder, organized by article type (blanket, garment, accessory, etc.)
- Optionally post to Notion Littlebird Log for reference
- Always credit the original designer

## Rules
- Never claim Pavi designed a pattern he transcribed from someone else
- Include original source URL for attribution
- If a video is unclear on a specific step, flag it rather than guess
- For paid patterns found online, note that the original should be purchased and do NOT transcribe the full pattern — only assist with patterns the user has access to
