---
name: sg-sync
description: >-
  Maintenance routine that keeps the distilled knowledge base current. Use when a new lesson
  worksheet is added to Lessons/, a new feedback file or folder is added, or the student says
  the distilled theory is out of date. Re-distills methodology.md, appends to error-taxonomy
  .md and progress-log.md, extends the glossary, and refreshes the "Where the student is"
  blocks. Never edits the source files.
---

# sg-sync — keep the brain current

You maintain the `knowledge/` base and the orientation blocks so the cockpit stays accurate
as the program grows. **Integrate, never overwrite**; the source folders are read-only.

## Step 1 — find what's new
- List everything in `Lessons/` and every `* Feedback/` folder.
- Compare against the **Coverage** table in `knowledge/methodology.md` and the rounds in
  `knowledge/progress-log.md`. Identify lessons and feedback rounds not yet distilled.

## Step 2 — for each NEW lesson
- Extract its model: structure, constraints, gates, the conforming shapes/examples, and the
  "where it goes wrong" traps.
- Integrate into `knowledge/methodology.md` (extend the relevant sections; add a new section
  if it's a new lesson stage). Add a row to the **Coverage** table.
- Add any new load-bearing terms to `knowledge/glossary.md`.

## Step 3 — for each NEW feedback round
- Parse the per-event verdict table and the score.
- Append a row to the `progress-log.md` score table and fill the per-event verdict grid.
- If a "Prediction vs. The Standard" section is present, add a calibration-ledger row.
- Extract failure modes: add **new** cards to `error-taxonomy.md` (cited to this round) and
  re-weight the frequency of existing ones. Keep each card's real-example citations current.

## Step 4 — refresh orientation
- Rewrite the "Where the student is" block in `CLAUDE.md` and the matching line in
  `methodology.md`: active lesson, best score, converged vs. open planes, calibration gap.
- Recompute the per-plane mastery map and the "what to grind next" diagnosis in
  `progress-log.md`.

## Step 5 — report
Show a concise summary of exactly what changed (files touched, rows/cards added, blocks
rewritten). Do **not** modify anything under `Lessons/` or the `* Feedback/` folders — they
are the pristine record everything else is distilled from.
