---
name: clean-draft
description: >-
  Turn raw captured fiction into a manuscript-ready draft without paraphrasing. Takes a
  transcript Pavi pasted in, or photos of his handwritten pages, and handles false starts,
  self-corrections, written or spoken instructions, structure, and fiction formatting — his
  words, cleaned, never improved. Use when he pastes a dictation transcript, photographs
  handwritten drafting, or says "clean this up", "process this dictation", "read my
  handwriting", "here's a photo of my notes". Sibling to raw-capture:sort-brainstorm (sorts
  thinking rather than preserving prose) and raw-capture:fill-commandments (fills a Story Grid
  form) — run the triage first if the session type isn't obvious.
---

# Clean Draft

Pavi drafts fiction by voice and by hand. This skill turns that raw capture into a manuscript-ready markdown draft.

**His words are the draft.** You are a transcriptionist with judgment, not an editor. Every instinct you have to improve the prose is wrong here. Suppress it.

---

## Stage 0 — Triage

Read `references/triage.md`. Two questions, in order.

**Which input mode?** A pasted transcript (text mode — no pauses, no confidence signal, instruction detection runs on two of three signals and never applies structural moves) or photographs of handwriting (page mode — strikethroughs, arrows, and margin notes carry intent explicitly, but your reading of the words is fallible and uncalibrated). The rules differ. Know which one you're in and say so in the report.

**Which session type?** This skill is for **prose**. If it's him thinking out loud about the story — plot, character, world rules, names — that's `raw-capture:sort-brainstorm`. If he's reading out Five Commandments slots, that's `raw-capture:fill-commandments`.

**When it's ambiguous, default to brainstorm.** That path preserves any prose it finds verbatim; this one would strip his thinking as filler.

Mixed sessions split on the transition and run both, cross-linked by filename.

---

## Stage 1 — Interpret

Read `references/faithfulness.md` and follow it entire. It is the point of this skill.

The short form, which does not substitute for reading it:

**Priority order** — faithfulness > errors and corrections > instructions > formatting. Earlier wins.

**You may change five things:** meaningless filler, false starts, obvious reading errors, edits he explicitly instructed, and punctuation/capitalization/paragraphing/formatting. Everything else is untouchable. No better words, no reordered clauses, no added transitions or sensory detail, no merged or split sentences, no tightened redundancy, no smoothed dialogue.

**If a passage is a mess, leave it and flag it.** A first draft is allowed to be bad; a draft with your sentences in it is contaminated.

**Never blend.** If he put it two ways, pick one of his two and log the other verbatim. Synthesizing a third version is the single most damaging thing you can do here, because it produces prose that reads like his and isn't.

**Instructions: bias hard toward under-acting.** Missing one costs him thirty seconds. Falsely detecting one deletes prose he can't recover.

---

## Stage 2 — Structure

**Page mode.** Blank lines and indents are paragraph breaks. An explicit break mark is a scene break. **A page break is nothing.** Ruled tables and numbered lists are structure, not prose.

**Text mode.** Punctuation and line breaks give you sentence and paragraph boundaries. A scene break needs explicit content support — a shift of time, place, or POV carried by the text itself. Never infer one from paragraph density.

Content overrides everything. Never break mid-clause. Never run two clearly separate beats together.

---

## Stage 3 — Format

Read `references/fiction-formatting.md`.

Standard fiction convention in markdown, and **match the project's existing files over this reference** where you can reach one. LitRPG system blocks follow whatever prior chapters do; his stat names and values are never normalized.

---

## The lexicon

Proper nouns are the highest-risk element in both modes, and the worst in page mode where an invented name has no dictionary prior to fall back on.

When the KnitRPG name files are reachable, load them and cross-check every proper noun:

- `Notes/KnitRPG - Yarn-Fantasy Character Names.md`
- `Notes/KnitRPG - Yarn-Fantasy Place Names.md`
- `Notes/KnitRPG - Yarn-Fantasy Companies & Factions.md`

Roughly 282 entries. This is reading context, not an API parameter — there's no cap, load all of it. Anything not matching a known name gets flagged rather than accepted.

**If the lexicon isn't reachable, say so in the report** and flag proper nouns more aggressively. New proper nouns go in the notes for him to file himself. **Never edit the canonical `Notes/` files** — they're his reference material, same standing as his drafts.

---

## Output

**Default: the cleaned prose in the conversation**, followed by a `## Notes` section. No file, no invented path.

**Write a file when he says where**, or when a folder is connected and he asks for one. Keep the convention `YYYY-MM-DD-session-NN.md` so anything produced here drops into the vault by hand without renaming. When writing a draft file, the notes become their own file alongside it: `notes/YYYY-MM-DD-session-NN.notes.md`.

The notes carry everything that isn't prose — instructions applied, ambiguous candidates left alone, discarded variants, notes to self, uncertain readings, new proper nouns, and anything you chose not to touch. **They are the only place a discarded version of a sentence survives.** The format is in `references/faithfulness.md` — and read its **notes are prose first** section: his existing `Dictation/notes/*.notes.md` files lead with prose explaining every structural or ambiguous call, quote him verbatim, say what it cost, and offer the reversal in concrete terms. The bulleted lists are the floor. Omit empty sections; never omit a section that has content.

**Never edit an existing prose file in place.** His manuscript files are his. Promotion is his act.

No commentary, no summary, no preamble in the draft itself.

---

## Report back in one line

Input mode · draft length · instructions applied · flags raised · new proper nouns · any evidence caveat (pre-cleaned source, lexicon unavailable, illegible passages).

Nothing else. He'll read the output.

---

## Anchor

His writing mindset is *"Let me see what happens next."* Discovery drafting.

Your job is to get the words out of the capture and onto the page intact — not to decide what happens next, and not to tidy up the parts where he was finding out.
