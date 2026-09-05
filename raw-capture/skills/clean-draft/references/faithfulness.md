# Faithfulness — the shared core

Read by all three `raw-capture` skills. `clean-draft` obeys it throughout. `sort-brainstorm` obeys it wherever it preserves prose verbatim. `fill-commandments` obeys it in Part 1 for the matrix cells and in Part 2 entire.

**The governing principle: his words are the artifact.** You are a transcriptionist with judgment, not an editor. Every instinct you have to improve the prose is wrong here. Suppress it.

---

## Priority order

When these conflict, the earlier one wins.

1. Faithfulness to what he wrote or said
2. Correct handling of errors and corrections
3. Correct handling of instructions
4. Formatting conventions

---

## 1. Faithfulness

You may change exactly five categories of thing:

- Filler words (um, uh, like, you know, I mean) when they carry no meaning
- False starts and restarts
- Obvious transcription or reading errors
- Edits he explicitly instructed
- Punctuation, capitalization, paragraphing, formatting

Everything else is untouchable.

**Explicitly forbidden**, even where the prose is weak:

- Substituting a better word for his word
- Reordering clauses within a sentence
- Adding transitions, connective tissue, or sensory detail
- Combining or splitting his sentences for rhythm
- Tightening redundancy that he actually wrote
- Rewriting dialogue to sound more natural

If a passage is genuinely a mess — a rambling sentence that collapses under itself — **leave it and flag it in the notes.** Do not fix it. He will decide. A first draft is allowed to be bad; a draft with your sentences in it is contaminated.

The one narrow exception: when a sentence is grammatically incomplete purely because of the capture medium (a dropped verb from a mid-sentence restart, a word lost at a line break), repair the mechanics **with his own words**. Never with new ones.

---

## 2. Errors and self-corrections

**Immediate restart** — "He walked— he strode into the hall." → Keep the last complete version. Drop the abandoned fragment.

**Explicit correction** — "the tower was grey, no, make that black" → Apply it. Delete the correction language. Result: "the tower was black."

**Stutter or repetition** — "the the the door" → Collapse.

**Two complete, materially different versions** — Keep the later one in the output. Log the earlier one verbatim in the notes with its anchor. He may have preferred the first.

**Never blend.** If he put it two ways, pick one of his two. Do not synthesize a third sentence combining the best of both. That is the single most damaging thing you can do here, because it produces prose that reads like his and isn't.

**Suspected reading errors.** Flag any word you suspect is wrong. Inline: `[?word]`. Invented terms, character names, and fantasy vocabulary are the usual suspects. If context makes the intended word obvious, correct it and log the correction. If it doesn't, flag rather than guess.

**Unrecoverable text** — `[inaudible]` or `[illegible]`, with an anchor. Never invent filler to bridge a gap.

See `triage.md` for how the evidence behind these rules differs by input mode — self-corrections are inferred in text mode and explicit (struck through) in page mode.

---

## 3. Instructions

He interrupts to direct the manuscript: move a passage, insert text, cut something, rename a character. There is no fixed command vocabulary — he phrases these naturally.

**The failure modes are asymmetric.** Missing an instruction costs him thirty seconds of editing. Falsely detecting one deletes prose he can't recover. **Bias hard toward under-acting.**

### Detection — three signals

All three present = confident. Fewer = flag, don't act.

- **Register** — the line addresses the manuscript rather than living inside it. Second person, imperative, or referring to text as an object: "that paragraph," "what I just said," "the bit about the tavern," "up above."
- **Boundary** — the line sits apart from the surrounding prose. What supplies this differs by mode; see `triage.md`. **In text mode there is no boundary signal at all.**
- **Frame break** — it references the writing process, not the story world. Editorial vocabulary, structural language, "note to self."

### Response tiers

| Confidence & scope | Action |
| --- | --- |
| Confident, local, reversible (paragraph break, cut last sentence, rename, scene break, insert a line) | Apply silently. Log it in notes. |
| Confident, structural (move a block, insert a long passage elsewhere) | Apply. Mark the boundary: `<!-- moved per instruction @anchor -->` |
| Ambiguous | **Do not act.** Leave the words in the prose exactly as written. Flag inline: `<!-- ?? possible instruction: "..." @anchor -->` |

### Hard limits

- Never delete more than one sentence on inference alone. If an apparent instruction implies cutting more, flag it and leave the text.
- **Dialogue guard:** characters say "move that over there" too. An instruction candidate inside quoted speech, or in the middle of an active scene beat with no separation on either side, is prose. Full stop.
- Never act on an instruction you only half-understood. Flag it.
- **Text mode only:** with two of three signals available, act only when register *and* frame break are both unambiguous, and **never apply a structural move** — flag every one. See `triage.md`.

### Notes to self

"note: check the timeline here," "remember he doesn't know about the sword yet" — these are never prose and never instructions. Strip them from the output, preserve them verbatim in the notes with anchors.

---

## The notes are not optional

Everything that isn't prose goes into the notes: instructions applied, ambiguous candidates left alone, discarded variants, notes to self, uncertain readings, new proper nouns, and anything you chose not to touch.

The notes are the record of what you decided and what you weren't sure about, and **the only place a discarded version of a sentence survives.** Write them as carefully as the output.

```markdown
## Notes

### Instructions applied
- @anchor — "<what he wrote>" → <what you did>

### Ambiguous — not acted on
- @anchor — "<what he wrote>" → left in prose, flagged

### Discarded variants
- @anchor — earlier version: "<verbatim>"

### Notes to self
- @anchor — "<verbatim>"

### Uncertain reading
- @anchor — "[?word]" → suspected: <guess, or "no guess">

### New proper nouns — file these yourself
- <term> (character | place | faction | item | stitch) @anchor

### Flagged for his judgment
- @anchor — <rambling passage left intact, or anything you chose not to touch>
```

Omit any section that has nothing in it. Never omit a section that does.

---

## The notes are prose first, lists second

The template above is the **floor, not the ceiling.** His existing notes files (`Dictation/notes/*.notes.md`) set the actual standard, and they read like a letter explaining your reasoning — not a changelog.

**Header.** Beyond date and source: which scene and sequence this is, the spine file if there is one, and provenance — where the text came from and what it was processed with. If anything about the session was unusual (unusually sparse, long gaps mid-sentence, a source that arrived pre-cleaned), say so up front and say how it changed your decisions.

**Lead with a prose section for every structural or ambiguous call.** Before the bulleted lists, walk through anything that moved, was cut, or was nearly cut. For each one:

- Quote what he said or wrote, **verbatim and marked as verbatim**, with its anchor.
- Say what you did and where the seam is — name the HTML comment marker he can delete once he's read it.
- Say what it cost. How many sentences dropped, whether the material returns later, whether anything was actually lost or only resequenced.
- **Offer the reversal in concrete terms.** "If you want him lying down there and standing up again, it goes straight back." He should never have to ask how to undo something.

**Say what you chose not to do, and why.** This is as valuable as what you did. If a passage described a table but named no values, building it would mean inventing them — so it stayed prose. Name the one thing that would unlock it: *give me the weight steps and it becomes a table in one pass.* Same for a phrase you left inline because setting it off would have meant splitting his sentence.

**Carry standing decisions forward.** Formatting conventions established in earlier sessions — how journal lines are set, how system blocks are formatted — should be named and applied, with the session they came from. Where you applied one, say so. Where you couldn't, say why.

**Address him directly, second person, and invite correction.** "Say the word if the paragraphing runs too fine or too coarse." The notes are a conversation about judgment calls, not a receipt.

The structured lists still follow, and still carry everything. The prose is what makes them usable.

---

## Never edit an existing prose file in place

Output is new text in the conversation, or a new file. His manuscript files are his. Applying anything to them is his act, not yours — including a correction you're certain about.
