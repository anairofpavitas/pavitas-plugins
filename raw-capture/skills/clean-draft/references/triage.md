# Triage — input mode, then session type

Read by all three `raw-capture` skills. Two questions, in this order:

1. **What am I holding, and what evidence does it carry?** → input mode
2. **What kind of session is this?** → which skill runs

Get the first one wrong and you apply rules to evidence that isn't there. Get the second one wrong and you either strip his thinking as filler or summarize prose he actually drafted.

---

# Part 1 — Input mode

## Text mode — a transcript he pasted

He transcribed it elsewhere (superwhisper, Letterly, Monologue, a Scribe run on Zo, anything) and handed you the text.

**What you have:** the exact words, whatever the transcriber produced.
**What you don't have:** pauses, timing, confidence scores.

### Consequences — these are not optional adjustments

**The instruction test loses a third of its evidence.** Boundary *is* the pause. Without it you are running on register and frame break alone. Per the asymmetric-failure rule in `faithfulness.md`, the bias tightens rather than the standard relaxing:

- Act only when register **and** frame break are both unambiguous.
- **Never apply a structural move.** Flag every one, without exception.
- Local reversible edits (paragraph break, rename, cut the last sentence) may still be applied when both signals are clean.

**There is no pause table.** Sentence and paragraph breaks come from punctuation and line breaks in the transcript. Scene breaks require explicit content support — a shift of time, place, or POV that the text itself carries. Never infer a scene break from paragraph density.

**There is no confidence signal.** Suspected mishearings can only be caught from context. Prefer flagging to correcting.

### Ask for it raw

Transcripts should arrive **uncleaned** wherever the source allows. If the upstream transcriber already stripped false starts — Letterly's cleanup, Scribe with `no_verbatim=true`, most superwhisper modes — then the evidence separating a self-correction from an instruction was destroyed before you saw it.

That's workable. It is not invisible. **Say so in the report:** "source appears pre-cleaned; false-start evidence unavailable." Never imply you had full evidence when you didn't.

---

## Page mode — photographs of handwritten pages

You read the image directly. No transcription service is involved.

**What you have:** every mark he made, including the ones that show intent.
**What you don't have:** any calibrated sense of whether you read a word correctly.

### The confidence gap — state it plainly

In a speech-to-text pipeline, `logprob` is produced by a *different mechanism* than the transcription, which is why it can catch its own errors. Here, the reading and the flagging are the same act. **You can be confidently wrong, and a misread word will look like an ordinary word rather than a flag.**

Two mitigations, both required:

1. **The lexicon.** Load the KnitRPG name files when they're reachable (`Notes/KnitRPG - Yarn-Fantasy Character Names.md`, `… Place Names.md`, `… Companies & Factions.md` — roughly 282 entries). Cross-check every proper noun against them. Anything that doesn't match a known name gets flagged, not accepted. This is the closest thing to a confidence score available, and it is why the lexicon matters *more* in page mode than it ever did in the audio pipeline.
   - Unlike the old Scribe path, this is reading context rather than an API parameter, so the 100-keyterm cap is gone. Load all of them.
   - If the lexicon isn't reachable this session, **say so in the report** and flag proper nouns more aggressively.
2. **Never transcribe a proper noun you can't read confidently.** Flag it. A wrong name that looks right is worse than a gap.

### Signal map

| Mark on the page | Read as | Confidence |
|---|---|---|
| Strikethrough / crossed out | Discarded variant. Keep the replacement, log the struck text verbatim. | **High** — unambiguous |
| Abandoned line, struck or trailing | False start. Drop, log it. | High |
| Caret + insertion | Apply the insertion at the caret. | High |
| Arrow, or circled block with a destination arrow | Move instruction. Apply and mark the seam. | **High** — unambiguous |
| Margin note, boxed aside, bracketed line, visibly different pen | Note to self. Strip from prose, preserve verbatim. | **High** |
| Blank line, indent | Paragraph break | — |
| Explicit break mark (rule, `* * *`, centred marks) | Scene break | — |
| **Page break** | **Nothing.** Not a scene break, not a paragraph break. | — |
| Underline | Emphasis only where his own convention says so. **Never infer italics from it.** | — |
| Numbered lists, lettered options, ruled tables | **Structure, not prose.** Preserve as structure. | — |
| Low legibility | `[?word]` | — |
| Unreadable | `[illegible]` — never guess | — |

### Consequences

**The instruction test runs at full strength.** Visual separation supplies the boundary: a margin, a box, a bracket, a different pen. Structural moves *may* be applied when an arrow makes the destination unambiguous — this is the one place page mode is stronger than the original audio pipeline.

**Self-corrections are explicit.** A strikethrough is not a judgment call. Where audio made you infer intent from "no, make that," the page shows it.

**Anchors are `p2 L14`** — page and line — where the audio pipeline used `@mm:ss`. Every notes entry carries one.

**Multi-page:** preserve page order, carry a running instruction log across pages, and never join a sentence across a page break without content support.

**Ruled tables matter specifically.** This is how Five Commandments pages arrive. Preserve the table as a table and hand it to `fill-commandments`.

---

## The two modes have inverted strengths

Neither is a degraded version of the other. Know which one you're in and report it.

| | Text mode | Page mode |
|---|---|---|
| Word accuracy | Exact | Fallible, uncalibrated |
| Proper nouns | As transcribed | Highest-risk element |
| Self-corrections | Inferred from wording | **Explicit** |
| Instruction detection | 2 of 3 signals — weakest | **3 of 3** — strongest |
| Structure | Punctuation, line breaks | Layout |
| Structural moves | **Never apply** | May apply on a clear arrow |

**Mixed input** — a pasted transcript plus photos of the same session, or pages that include a typed insert — runs each part under its own mode. Say which parts came from where.

---

# Part 2 — Session type

Three kinds of session, three skills. Run this on the material once you know the mode.

**Reads as prose** — sustained narration · dialogue with speech tags · a character moving through a scene · sensory detail delivered straight · he stays inside the story world for stretches at a time. → **`clean-draft`**

**Reads as brainstorm** — first person present about the work ("what if," "I'm thinking," "the problem is," "okay so") · options weighed aloud · questions asked of himself · craft vocabulary *about* the story rather than *in* it ("the arc," "this scene needs," "the magic system," "her want") · a thread abandoned mid-thought and another started. → **`sort-brainstorm`**

**Reads as commandments** — the word *crisis* early · commandment vocabulary used as slot names rather than as discussion ("the inciting incident is," not "I think the inciting incident might want to be") · pros and cons enumerated against two named options · a declared scope ("this is the Hunt sequence," "global," "Q1") · terse and listy rather than exploratory · **in page mode, a ruled table**. → **`fill-commandments`**

The tell between the last two is whether the slots are being **filled** or **questioned**. Recording a crisis is `fill-commandments`; debating what the crisis should be is `sort-brainstorm`.

| Session shape | Do this |
| --- | --- |
| Clearly prose throughout | `clean-draft` |
| Clearly brainstorm throughout | `sort-brainstorm` |
| Slots being filled, in his working order | `fill-commandments` |
| Brainstorm that hardens into a skeleton | Split at the hardening point. Run both, cross-linked. |
| Skeleton that drifts into drafted prose | That is the commandments beat pass arriving early. Keep it in `fill-commandments`, verbatim, and slot it. |
| Mixed prose and thinking | Split on the transition. Run both. Cross-link the outputs. |
| Genuinely ambiguous | **Default to `sort-brainstorm`.** It is the safer error: that path quotes prose verbatim in a blockquote, so nothing is lost, whereas `clean-draft` would strip his thinking as filler. |

**Prose caught inside a brainstorm session is preserved verbatim, in a blockquote, exactly as written.** Never summarize a passage he actually drafted.
