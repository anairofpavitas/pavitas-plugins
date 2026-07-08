# PDF Viewer Plugin

View, annotate, and sign PDFs in a live interactive viewer. Built around
Pavitas Productions' actual PDF jobs: marking up narration scripts for
the booth, reviewing and signing publisher contracts, filling contractor
tax forms, and handling business documents — then downloading the
annotated copy.

> Adapted from Anthropic's generic `pdf-viewer` plugin. Same commands,
> same local PDF server; the examples and workflows were rewritten for a
> solo audiobook-narration operation.

## What It Does

- **Prep narration scripts** — mark pronunciations, character voice
  cues, breath/pause beats, emphasis, pickup/retake spots, chapter
  breaks, typos, and author questions, section by section, reviewing
  each batch in the viewer
- **Review & sign publisher contracts** — highlight the terms that
  matter (rate/PFH, deadline, rights, pickup clause), then place your
  signature
- **Fill forms** — W-9s, vendor setup, direct-deposit, onboarding, with
  live field-by-field preview
- **Handle business docs** — annotate invoices, proofs, and PDF
  deliverables before they go out
- **Stamp** — APPROVED, PICKUP, REVIEW, DRAFT, or any custom label
- **Download** — export the annotated PDF from the viewer toolbar

## Commands

| Command | What it does |
|---------|-------------|
| `/pdf-viewer:open` | Open a PDF in the interactive viewer |
| `/pdf-viewer:annotate` | Mark up a script for the booth, or review a contract |
| `/pdf-viewer:fill-form` | Fill a W-9, vendor, or onboarding form interactively |
| `/pdf-viewer:sign` | Place your signature or initials on a contract |

## When to use this vs. just reading a PDF

This plugin is for **interactive, visual workflows** — seeing the
document, marking it up, and downloading an annotated copy.

If you just want a **summary, chapter breakdown, or word/page counts**
from a script, don't use this plugin — Claude reads PDFs natively (or
use the audiobook-script-analyzer skill), which is faster for pure
ingestion.

## How It Works

This plugin uses a **local MCP server** (`@modelcontextprotocol/server-pdf`)
that runs on your machine via `npx`. No API keys or remote services —
the PDF server starts automatically when the plugin loads.

## Requirements

- Node.js >= 18
- Internet only if you open a remote HTTPS PDF

## Supported PDF Sources

- Local files (script PDFs, contracts, and forms in your working
  directory) — the common case
- Any direct HTTPS PDF URL (use the direct PDF link, not a landing page)

## Signature Disclaimer

`/pdf-viewer:sign` places a **visual** signature image on the page. It is
not a certified or cryptographic digital signature. For legally binding
e-signatures, use a dedicated signing service — if a publisher sends a
DocuSign/Adobe Sign link, use that.
