# Story Grid Skills Plugin

Skill-only plugin (no slash commands) for the Story Grid beat-writing mentorship program —
grading, editing, drilling, sparring, and syncing the distilled knowledge base against the
real grader's bar. Loads as `story-grid-skills:<name>`.

Not to be confused with **creative-writing**, which covers original fiction drafting
(Jim & Percy). This plugin is the coaching harness around the submission cycle: a student
works beats in `workbench/`, submits them against worked examples in `Lessons/`, gets real
feedback in `* Feedback/` folders, and these skills keep a distilled `knowledge/` base (plus
`CLAUDE.md` orientation) in sync with that record.

## Skills

| Skill | Role |
|-------|------|
| `story-grid-skills:sg-grade` | Mock examiner — dry-run PASS/REVISE verdict + score before real submission |
| `story-grid-skills:sg-edit` | Socratic line editor — mechanics pass + full conformance battery, diagnoses without rewriting unless asked |
| `story-grid-skills:sg-drill` | Practice-worksheet generator — targeted reps with an answer-key rationale |
| `story-grid-skills:sg-spar` | Brainstorming / pressure-testing partner — seeds ideas, challenges known misconceptions |
| `story-grid-skills:sg-sync` | Knowledge-base maintenance — distills new lessons/feedback into `knowledge/`, never edits source files |

## Expected project layout

These skills assume a working directory shaped like:

```
knowledge/
  methodology.md
  error-taxonomy.md
  glossary.md
  progress-log.md
Lessons/
* Feedback/          (one or more folders, e.g. "Round 1 Feedback")
workbench/            (student drafts, drills, dry-run verdicts)
CLAUDE.md             (orientation: "Where the student is")
```

`Lessons/` and `* Feedback/` folders are treated as a read-only pristine record — only
`sg-sync` writes to `knowledge/`, and it only ever integrates, never overwrites source files.

## Typical flow

1. `sg-spar` to brainstorm/pressure-test a beat idea.
2. Draft the beat in `workbench/`.
3. `sg-edit` for a Socratic line-edit pass, or `sg-drill` for extra targeted reps first.
4. `sg-grade` for a mock-examiner dry run before the real submission.
5. After real feedback comes back (or a new lesson drops), `sg-sync` to fold it into
   `knowledge/` and refresh the orientation blocks.

## Connectors

None — this plugin operates entirely on local project files.
