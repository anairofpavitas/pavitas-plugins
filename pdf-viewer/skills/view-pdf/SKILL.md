---
name: view-pdf
description: Interactive PDF viewer. Use when the user wants to open, show, or view a PDF and collaborate on it visually — mark up a narration script, review or sign a publisher contract, fill a form, highlight, stamp, or review markup together. Not for summarization, chapter breakdowns, or text extraction (use native Read / the audiobook-script-analyzer skill instead).
---

# PDF Viewer — Interactive Document Workflows

You have access to a local PDF server that renders documents in a live
viewer and lets you annotate, fill forms, and place signatures with
real-time visual feedback. This is tuned for Pavitas Productions' PDF
work: narration scripts, publisher contracts, and contractor forms.

## When to use this skill

**Use the PDF viewer when Pavi wants interactivity:**
- "Mark up this script for recording" / "prep this chapter"
- "Show me this contract and highlight the rate and deadline"
- "Sign this Aethon agreement on the last page" / "initial every page"
- "Help me fill out this W-9"
- "Flag the typos and any pronunciations I should check"
- "Stamp the pickups on page 40"

**Do NOT use the viewer for pure ingestion:**
- "Summarize this manuscript" -> native Read tool
- "Give me the chapter breakdown / word counts" -> audiobook-script-analyzer
- "What does the exclusivity clause say?" -> Read

The viewer's value is showing Pavi the document and collaborating on
markup — not streaming text back to you.

## Narration script prep — markup convention

The everyday job. When Pavi opens a manuscript he's prepping it for the
booth. Map his marks to annotations, and hold the color discipline so a
page scans at a glance:

| Pavi's mark | Annotation | Convention |
|-------------|------------|------------|
| Pronunciation note | `note` on the word | blue; phonetic respelling, e.g. `KAI-oss` |
| Character voice cue | `note` | teal; e.g. `Percy — dry, low` |
| Breath / pause | `freetext` `/` or `//` on the line | gray; `/` short beat, `//` full pause |
| Emphasis / stress | `underline` the operative word | mark the one word |
| Pickup / retake | `stamp` `PICKUP` + `circle` | red |
| Chapter / section break | `stamp` `CH ##` or `rectangle` divider + label | mark POV/scene shifts too |
| Typo / manuscript error | `strikethrough` + `note` with fix | red; flag to publisher |
| Author / publisher question | `note`, prefix `Q:` | amber |

At the end of a prep pass, offer to collect the red typos and amber
`Q:` notes into a single list for the publisher.

## Tools

### `list_pdfs`
List available local PDFs and allowed local directories. No arguments.

### `display_pdf`
Open a PDF in the interactive viewer. **Call once per document.**
- `url` — local file path or HTTPS URL
- `page` — initial page (optional, default 1)
- `elicit_form_inputs` — if `true`, prompts the user to fill form
  fields before displaying (use for interactive form-filling)

Returns a `viewUUID` — pass this to every `interact` call. Calling
`display_pdf` again creates a **separate** viewer; interact calls with
the new UUID won't reach the one Pavi is looking at.

Also returns `formFields` (name, type, page, bounding box) if the PDF
has fillable fields — use these coordinates for signature placement.

### `interact`
All follow-up actions after `display_pdf`. Pass `viewUUID` plus one or
more commands. **Batch multiple commands in one call** via the
`commands` array — they run sequentially. End batches with
`get_screenshot` to verify changes visually.

**Annotation actions:**
- `add_annotations` — add markup (see types below)
- `update_annotations` — modify existing (id + type required)
- `remove_annotations` — delete by id array
- `highlight_text` — auto-find text by query and highlight it
  (preferred over manual rects for text markup)

**Navigation actions:**
- `navigate` (page), `search` (query), `find` (query, silent),
  `search_navigate` (matchIndex), `zoom` (scale 0.5–3.0)

**Extraction actions:**
- `get_text` — extract text from page ranges (max 20 pages). Use for
  reading content to decide what to annotate, NOT for summarization.
- `get_screenshot` — capture a page as an image (verify your annotations)

**Form action:**
- `fill_form` — fill named fields: `fields: [{name, value}, ...]`

## Annotation Types

All annotations need `id` (unique string), `type`, `page` (1-indexed).
Coordinates are PDF points (1/72 inch), origin **top-left**, Y increases
downward. US Letter is 612×792pt.

| Type | Key properties | Use for |
|------|----------------|---------|
| `highlight` | `rects`, `color?`, `content?` | Mark important text |
| `underline` | `rects`, `color?` | Emphasis / stress on a word |
| `strikethrough` | `rects`, `color?` | Typos / manuscript deletions |
| `note` | `x`, `y`, `content`, `color?` | Pronunciations, cues, author Qs |
| `freetext` | `x`, `y`, `content`, `fontSize?` | Breath/pause marks, visible labels |
| `rectangle` | `x`, `y`, `width`, `height`, `color?`, `fillColor?` | Section/chapter dividers |
| `circle` | `x`, `y`, `width`, `height`, `color?`, `fillColor?` | Circle a pickup spot |
| `line` | `x1`, `y1`, `x2`, `y2`, `color?` | Draw lines/arrows |
| `stamp` | `x`, `y`, `label`, `color?`, `rotation?` | PICKUP, REVIEW, APPROVED, CH ## |
| `image` | `imageUrl`, `x?`, `y?`, `width?`, `height?` | **Signatures, initials**, logos |

**Image annotations** accept a local file path or HTTPS URL (no data:
URIs). Dimensions auto-detected if omitted. Users can also drag & drop
images directly onto the viewer.

## Interactive Workflows

### Script prep (AI-driven)
1. `display_pdf` to open the manuscript
2. `interact` -> `get_text` on the page range to catch names, invented
   terms, and hard words
3. Propose a batch using the markup convention above (describe what
   you'll mark)
4. On approval, `interact` -> `add_annotations` (+ `underline`/
   `highlight_text` for emphasis) + `get_screenshot`
5. Show Pavi, take edits, iterate to the next scene
6. When done, remind him to download from the viewer toolbar; offer to
   collect typos + author questions into a publisher list

### Contract review + signing
1. `display_pdf`, `get_text` the clauses
2. Highlight rate/PFH, deadline, rights, exclusivity, pickup clause;
   `note` anything ambiguous; `stamp` REVIEW
3. Hand off to signing: check `formFields` for a signature field or ask
   which page/position, then `add_annotations` with `type: "image"`
4. `get_screenshot` to confirm placement; add a dated `freetext` if
   there's a date line

### Form filling (visual, not programmatic)
Handles W-9s and vendor forms with cryptic/unnamed fields where the
label is printed on the page, not in metadata.

1. `display_pdf` — inspect returned `formFields`
2. If names are cryptic (`Text1`, `f1_7`), `get_screenshot` and match
   bounding boxes to visual labels
3. Fill from known context (name, business name, email) or ask Pavi for
   sensitive values (EIN, address, bank numbers — never guess these)
4. `interact` -> `fill_form`, then `get_screenshot`
5. Pavi confirms or edits directly

For simple well-labeled forms, `display_pdf` with
`elicit_form_inputs: true` prompts him upfront instead.

## Supported Sources

- Local files (script PDFs, contracts, and forms under client MCP roots)
- Any direct HTTPS PDF URL (use the direct PDF link, not a landing page)

## Out of Scope

- **Summarization / chapter breakdowns / word counts** — use native
  Read or the audiobook-script-analyzer skill
- **Certified digital signatures** — image stamping only; use DocuSign/
  Adobe Sign for legally binding e-signatures
- **PDF creation** — this works on existing PDFs only
- **AI voice work** — this plugin marks up scripts for a human narrator;
  it does not do any voice generation
