---
name: sort-brainstorm
description: >-
  Sort a raw story-development session into usable structure. Where raw-capture:clean-draft
  recovers prose, this takes the soup — free-form thinking that jumps between plot, character,
  world rules, lore, and names — and sorts it into the Bible's own nine sections, formats each
  category the way that category wants to be read, and returns astute questions about what
  doesn't hold together. Works from a pasted transcript or photos of handwritten notes. Use
  when Pavi says "process this brainstorm", "sort this session", "this one's brainstorming not
  writing", or hands over material that turns out to be thinking-out-loud rather than
  manuscript. Nothing it produces is canon.
---

# Sort Brainstorm

Pavi talks and writes through story problems. This skill turns that into structure he can use.

The governing principle is the **inverse** of `raw-capture:clean-draft`. There, his words *are* the draft and your job is to preserve them. Here, his words are **raw material** and your job is to sort them. You may reorganize freely, group by subject, and put things in an order he did not produce them in.

What you may still never do is **invent**. Reorganizing is the job. Adding is not.

---

## Stage 0 — Triage

Read `../clean-draft/references/triage.md`. Input mode first, then session type.

**Input mode** changes what evidence you have. Text mode: no pauses, so topic boundaries come from paragraph structure and subject shifts in the content. Page mode: a new page, a horizontal rule, or a heading is the topic boundary — and margin notes, strikethroughs, and arrows carry intent explicitly.

**Session type.** This skill is for thinking-out-loud. Sustained narration with dialogue and a character moving through a scene is `raw-capture:clean-draft`. Five Commandments slots being *filled* is `raw-capture:fill-commandments` — the tell against this skill is whether the slots are being filled or being **questioned**. Recording a crisis is that skill; debating what the crisis should be is this one.

**When it's ambiguous, this is the default.** It's the safer error: this path quotes prose verbatim, so nothing is lost.

Mixed sessions split on the transition and run both, cross-linked by filename in each header.

**Prose caught inside a brainstorm session is preserved verbatim, in a blockquote, exactly as produced.** Do not summarize a passage he actually drafted. Mark it `> [drafted aloud @anchor]` and leave it whole. If there's more than a paragraph of it, note in the report that the session contains draftable prose so he can decide whether to run `clean-draft` on that segment.

---

## Stage 1 — Sort

Read `references/bible-categories.md` and follow it entire: the eleven categories, their Bible destinations, and the formatting each one requires.

The parts most often got wrong:

- **Rules get the full triplet.** `**Rule:** … — **Cost:** … — **Limit:** …`, with `Not stated` where he didn't cover one. Missing costs and limits are the single most useful thing this skill surfaces. Never fill one in.
- **Lore distinguishes belief from truth.** He draws that line deliberately. Losing it destroys the point of the material.
- **Alternatives stay alternatives.** `Option A / Option B`. Do not pick.
- **One sentence, one primary category**, with `→ see Rules` cross-references. Never duplicate full text.

---

## Stage 2 — Analyse

Four sections, after the sorted content, specified in `references/bible-categories.md`:

**Settled vs. still open** · **Questions worth answering** (3–7, each anchored to something he actually said) · **What landed** (honest, name the mechanism, don't manufacture enthusiasm) · **Next session starter** (one question, sensory and specific).

**Ask, don't prescribe.** No "you should."

**The bible check is conditional.** If `Bible/` is reachable this session, check every claim against it — a question he already answered in `99 - Decision Log.md` is noise, and a contradiction with something 🔒 is the most valuable thing you can find. **If it isn't reachable, say the check wasn't run.** Never skip it silently.

---

## The canon rules — non-negotiable

Brainstorming sits at the **bottom** of the authority ladder. It has less standing than the draft and less than his handwritten notes.

- **Everything you output is 🟡.** Proposed, awaiting his call. Never 🔒. Never phrased as settled. Even something he stated flatly gets "sounded decided" rather than "decided" — he is thinking out loud, and a firm tone in a brainstorm is not a decision.
- **Nothing is canon.** Not the names, not the rules, not the arc. A brainstorm file is raw layer.
- **Never invent.** No supplied motive, mechanism, name, or connective logic. If a thought is incomplete, write it incomplete. `Not stated` is a valid and useful output.
- **Preserve his language.** Coined terms, place names, creature names, idiosyncratic phrasing — exactly as produced. Never substitute a more standard word for one he made up.
- **Mark uncertainty.** Garbled or unclear terms in *italics* with *(unclear)*. Never guess at what a mangled fantasy word was supposed to be. In page mode, cross-check every proper noun against the lexicon when it's reachable (see `clean-draft` SKILL.md).
- **Abandoned ideas are kept.** If he tried something and talked himself out of it, it goes under Discarded with his stated reason. Rejected options are evidence about the shape of the problem.
- **Never write into `Bible/`.** Promotion into the bible happens through a bible sweep — a separate deliberate act with Pavi in the loop.
- **Never edit an existing prose file in place.**

---

## Output

**Default: the sorted session in the conversation**, followed by a `## Notes` section.

**Write files when he says where**, or when a folder is connected and he asks. Convention: `YYYY-MM-DD-brainstorm-NN.md`, notes alongside at `notes/YYYY-MM-DD-brainstorm-NN.notes.md`.

Unlike a prose draft, a sorted brainstorm is **not transient** — it stays until its contents have been swept into the bible. The notes stay permanently.

The header carries: date, source, and which categories are present. If the session was mixed, name the sibling file.

### Notes format

```markdown
## Notes

### Uncertain reading
- @anchor — "*term* (unclear)" → suspected: <guess, or "no guess">

### New proper nouns — file these yourself
- <term> (character | place | faction | item | stitch) @anchor

### Discarded
- @anchor — "<verbatim>" → his stated reason, or "no reason given"

### Prose drafted aloud
- @anchor — <length> — preserved verbatim in the session file / handed to clean-draft

### Contradictions with the bible
- @anchor — "<what he said>" ⚠️ collides with <Bible file>: "<the 🔒 line>"

### Couldn't categorize
- @anchor — "<verbatim>" → parked for 00 - Braindump
```

Omit empty sections; never omit one with content. Lead the notes with prose on any judgment call that isn't self-evident — see the **notes are prose first** section of `../clean-draft/references/faithfulness.md`.

---

## Report back in one line

Input mode · categories found · item counts per category · question count · new proper nouns · contradictions flagged (or that the bible check didn't run) · any evidence caveat.

Nothing else. He'll read the output.

---

## Handoff

The natural next step is **"sweep the bible"**, which diffs the sorted file against every bible section and reports New / Extended / Contradicted / Drift / Questions. Say so in the report. **Do not run it unasked** — promotion into canon is his call, not a chained automation.

---

## The Notion path

He also runs this in Notion's AI Meeting Notes when he's working there. The custom-instructions text is `references/notion-instructions.md` — same content, expressed as a summary-format prompt. Keep the two in sync when either changes; **the skill is authoritative and the Notion asset follows it.**

---

## Anchor

He is thinking out loud, which means he is allowed to be wrong, to contradict himself, and to trail off. The soup is not a defect in the capture; it is what discovery sounds like.

Your job is to sort it so he can see what he has — not to resolve it, not to decide for him, and not to make it sound more finished than it is.
