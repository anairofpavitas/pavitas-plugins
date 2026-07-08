---
description: Open a PDF in the interactive viewer
argument-hint: "[path-or-url]"
---

> If you need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

# Open PDF

Display a PDF document in the live viewer. Use this when Pavi wants to
**see** a document — not just extract its text.

## Instructions

1. If a URL or file path is given, call `display_pdf` with it
2. If no path given, call `list_pdfs` first to show available documents
   (scripts usually live under the project's `Assets` folder)
3. After displaying, offer next steps based on the document type:
   - **Narration script / manuscript** → "Want me to mark this up for
     the booth — pronunciations, character cues, breath/pause, pickups,
     and flag any typos or author questions?"
   - **Publisher contract** (Aethon, Podium, Recorded Books, Blackstone,
     Audible) → "Want me to highlight the key terms — rate, PFH,
     deadline, rights, pickup/revision clause — and drop review notes?"
   - **Tax / onboarding form** (W-9, direct-deposit, vendor setup) →
     "This has fillable fields — shall I help you fill it?"
   - **Invoice / business PDF** → "Want me to review it or annotate
     anything before it goes out?"

## Supported Sources

- Local files (paths, or drag-and-drop into your working directory) —
  the common case: script PDFs, contracts, and forms
- Any direct HTTPS PDF URL (use the direct PDF link, not a landing page)

## When NOT to use this

If Pavi just wants a summary, a chapter breakdown, or word/page counts
from a script, **do not** open the viewer — use Claude's native Read
tool (or the audiobook-script-analyzer skill) on the PDF path instead.
The viewer is for interactive, visual markup.
