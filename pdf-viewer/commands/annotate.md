---
description: Mark up a PDF — narration scripts for the booth, or contracts for review
argument-hint: "[path-or-url]"
---

> If you need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

# Annotate PDF

Walk through a document with Pavi, proposing and applying annotations
section by section. He reviews each batch in the live viewer before you
continue.

Two default flavors: **script prep** (the everyday job — marking a
manuscript for recording) and **contract review** (highlighting terms
before signing). Detect which from the document and lead with it.

## Script prep — the narration markup convention

This is the primary use. When Pavi opens a manuscript, he's prepping it
for the booth. Map his marks to viewer annotations like this:

| Pavi's mark | Annotation | Convention |
|-------------|------------|------------|
| Pronunciation note | `note` (sticky) on the word | blue; content = phonetic respelling, e.g. `KAI-oss` or `vel = "vell"` |
| Character voice cue | `note` | teal; e.g. `Percy — dry, low, clipped` |
| Breath / pause mark | `freetext` `//` on the line, or `highlight` the punctuation | gray; single `/` short beat, `//` full pause |
| Emphasis / stress | `underline` the word (or `highlight`) | mark the operative word only |
| Pickup / retake mark | `stamp` `PICKUP` + `circle` the spot | red; where a line needs a re-record |
| Chapter / section break | `stamp` `CH ##` or a `rectangle` divider + `freetext` label | mark scene/POV shifts too |
| Typo / manuscript error | `strikethrough` + `note` with the fix | red; these get flagged back to the publisher |
| Author / publisher question | `note` (sticky) | amber; prefix `Q:` e.g. `Q: is "Vel" one syllable?` |

Keep the color discipline — Pavi should be able to scan a page and know
a red circle means pickup, an amber sticky means "ask the author."

### Workflow (script prep)

1. **Open** — `display_pdf` (or reuse an existing `viewUUID`)
2. **Read** — `interact` -> `get_text` on the page range in play
   (<=20 pages) so you know the names, invented terms, and hard words
3. **Propose** — describe the batch before applying:
   > "On page 12 I'll drop pronunciation notes on 'X<NAME>' and
   > 'Aetherius', a character cue for the guard, mark two breath
   > pauses in the long sentence, and flag one typo ('teh'). Good?"
4. **Apply** — on approval, `interact` with batched commands:
   `add_annotations` (+ `highlight_text`/`underline` for emphasis) then
   `get_screenshot` of that page
5. **Review** — show the screenshot, take edits
6. **Iterate** — next page/scene, repeat
7. **Finish** — remind Pavi he can download the marked-up PDF from the
   viewer toolbar. If typos or author questions piled up, offer to
   collect them into a list for the publisher (and, if he wants, log it
   to the Notion Littlebird Log).

## Contract review

For a publisher agreement, highlight and note the terms that matter:
rate / per-finished-hour, deadline and delivery date, rights granted,
exclusivity, the pickup/revision clause, and payment timing. Stamp
`REVIEW` on anything ambiguous and drop a `note` with the question.

1. `display_pdf`
2. `interact` -> `get_text` to read the clauses
3. Propose the highlights + notes, apply on approval, screenshot
4. When done, hand off to `/pdf-viewer:sign` to place his signature

## Manual mode

If Pavi gives explicit instructions ("mark every 'Kael' with the
pronunciation", "stamp PICKUP on page 40"), skip the proposal and
execute directly. Still confirm with a screenshot.

## Tips

- Prefer `highlight_text` over manual `rects` — it finds coordinates
  automatically
- Batch related annotations in one `interact` call, 3-5 per page so
  review stays easy
- End every batch with `get_screenshot`
- Recurring invented names? Note the pronunciation once at first
  appearance, then only re-mark if the reading changes
