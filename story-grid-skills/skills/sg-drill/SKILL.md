---
name: sg-drill
description: >-
  Generates fresh targeted practice worksheets in the lesson format. Use when the student
  wants extra reps — by default weighted to their weak spot (Ideological plane, determinate-
  sign selection), but any plane / pole / shape / 1B vehicle can be requested. Produces
  blank beat prompts with explicit constraints, plus an answer-key rationale that mirrors
  the worked-example style of the Lessons/ folder.
---

# sg-drill — the practice generator

You produce focused practice sets so the student can build instinct between submissions.

## Before you start
Read `knowledge/methodology.md` (for the target's reference content and gate) and
`knowledge/progress-log.md` (to confirm the current weak spot). Match the *format and tone*
of the worksheets in `Lessons/`.

## What to generate
- **Default focus: Ideological + determinate signs**, since that is the open front. If the
  student names a plane / pole / direction / shape / vehicle, target that instead.
- A short **reference reminder** for the target (the gate, the one test that matters here).
- **N blank beat prompts** (default 5). Each gives the S1 / S2 / S3 slots *and a constraint
  to satisfy*, e.g.:
  - "Negative pole, recoil direction. Ideological. S2 must waver on a determinate sign."
  - "Positive pole, receive direction. Social. Name the on-camera audience in S1."
  - (1B) "Antagonist vehicle: Institution. S3 must individuate into a representative."
- Vary characters and settings; never reuse a scenario within a sheet, and avoid copying the
  worksheet's own examples.

## The answer key
After a clear divider, give a **rationale key**: for each prompt, state what a conforming
beat *must do* (which gate, what makes the sign determinate, where the consequence lands)
and **one** worked example. Tell the student to write theirs *first*, then compare — the key
is for checking, not copying.

## Output
Offer to save the worksheet to `workbench/` as a dated drill file (e.g.
`workbench/drill_ideological_<date>.md`) so completed reps accumulate. Ask the student for
the date if you need one. When they finish a drill, suggest running `story-grid-skills:sg-grade`
or `story-grid-skills:sg-edit` on their answers.
