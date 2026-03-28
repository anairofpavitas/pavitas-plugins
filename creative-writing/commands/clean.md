---
description: Run anti-AI-isms cleaning on a prose draft. Strips generated-sounding patterns using the humanize-prose skill.
---

# Prose Cleaning

Apply the full humanize-prose skill ruleset to a draft.

## What Gets Cleaned

Per the anti-AI-isms skill:
- **Sentence structure**: Remove "As [character] [verbed], [they] [verbed]" constructions, eliminate simultaneous action chains, vary sentence openings
- **Punctuation**: Remove performative em-dashes and semicolons used for fake sophistication, cut unnecessary ellipses
- **Word-level**: Strip "simply", "merely", "rather", "quite", "indeed", "certainly" filler; kill "a sense of [noun]" constructions; eliminate "couldn't help but"; replace "found himself [verb]ing" with direct action
- **Paragraph structure**: Break up paragraphs that follow feeling→thought→action→reflection template; vary paragraph length
- **Voice and tone**: Remove emotional stage directions that tell the reader what to feel; cut retrospective narration that summarizes instead of showing; eliminate philosophical tangents that don't serve the scene

## Input
- Pasted text, uploaded file, or referenced draft

## Output
- Cleaned version with changes highlighted or summarized
- Brief note on what was changed and why
- Don't rewrite the entire voice — preserve Pavi's natural style, just strip the AI patterns

## Rules
- This cleans prose, it doesn't rewrite it
- Preserve Pavi's voice — he prefers writing that sounds "natural and unpolished, not rhetorically tidy"
- If the prose is already clean, say so. Don't manufacture changes.
