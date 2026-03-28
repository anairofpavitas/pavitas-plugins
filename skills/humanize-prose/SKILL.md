---
name: humanize-prose
description: Apply anti-AI writing rules to prose output to strip generated-sounding patterns and produce human-quality reflective, personal, or essay-style writing. Triggers whenever writing prose, essays, reflections, personal narratives, or any long-form non-technical content. Use this skill automatically when asked to write, rewrite, polish, or edit any prose that should sound human and authentic — including essays, memoir, first-person reflection, blog posts, narration copy, or creative nonfiction. Also triggers when the user says "make this sound more human," "remove AI-isms," "this sounds generated," "strip the AI out of this," or similar. Apply proactively whenever writing prose even without explicit request — this skill should be the default mode for all non-technical writing.
---

# Humanize Prose

Apply these rules to all prose output. They exist because LLMs produce predictable patterns that trained readers recognize immediately. Every item below is a failure mode to eliminate.

---

## Sentence Structure

**No "what [x] was [y]" constructions.**
- ❌ "What started to change things was the residency."
- ✓ "The residency changed things."

**No isolated theatrical punches.**
Short sentences dropped for dramatic effect signal construction. Keep the thought connected.
- ❌ "And that was the moment everything shifted."
- ✓ Fold the point into the surrounding thought or cut it.

**No reversed constructions for rhetorical impact.**
- ❌ "Things got worse, not better."
- ✓ "Things got worse."

**No tricolon escalation.**
Three items that build in weight or length = assembled rhetoric. Break the pattern or cut to two.

---

## Punctuation

**No em dashes as dramatic pause markers.**
Em dashes in LLM output almost always signal a theatrical beat. Options: restructure the sentence, use a comma, or cut the clause.
- ❌ "He knew the answer — but couldn't say it."
- ✓ "He knew the answer and couldn't say it." or "He knew the answer. Saying it was another matter."

---

## Word-Level Habits

Strip these on sight:

| Word/Phrase | Why It's a Problem |
|---|---|
| genuinely | false casualness |
| actually | false casualness |
| clearly | false casualness / condescending |
| obviously | condescending, padding |
| simply | condescending, padding |
| here's the thing | announces instead of delivers |
| here's where | announces instead of delivers |
| that's the point | announces instead of delivers |
| it's worth noting | throat-clearing |
| importantly | padding |

---

## Paragraph Structure

**No tidy thesis restatements at paragraph endings.**
Closing a paragraph with a resonant summary line is a generated pattern. Real reflective writing doesn't wrap up that cleanly. End mid-thought if necessary.

**No transitional throat-clearing at section openings.**
- ❌ "Closely related to this is..."
- ❌ "Worth noting here is..."
- ✓ Just move into the topic.

**No signposting sentences.**
If a sentence describes what the next sentence will say, cut it. The next sentence should do the work itself.

---

## Voice and Perspective

**Stay in first person for personal writing.**
Don't shift to "you" to generalize a personal experience. If it happened to the person writing, it's "I" throughout.

**Don't universalize individual experience.**
- ❌ "This is what tends to happen when singers are trained classically."
- ✓ "This is what happened to me."

**Only include what's traceable to the source.**
When working from a transcript, interview, or source material: no added detail, reflection, or phrasing that the person didn't actually say or express. If it's not in the source, it doesn't belong in the output.

---

## Tone

**No aphoristic closing lines designed to resonate.**
- ❌ "The bridge wasn't a technique. It was knowledge."
- ❌ "In the end, it wasn't about the voice. It was about trust."
These are profundity performances. Cut them.

**Match the register of the source material.**
If the source is plain and conversational, the output is plain and conversational. Don't elevate.

**Prefer the simpler sentence.**
Given two options that say the same thing, use the one with fewer words and less syntactic ornament.

---

## Quick Self-Check Before Output

Before finalizing any prose, scan for:
- [ ] Any "what [x] was [y]" constructions?
- [ ] Any em dashes used for dramatic effect?
- [ ] Any isolated short sentences dropped for punch?
- [ ] Any "genuinely," "actually," "clearly," "obviously," "simply"?
- [ ] Any "here's the thing / here's where / that's the point"?
- [ ] Any paragraph ending with a tidy resonant summary?
- [ ] Any second-person shift in personal writing?
- [ ] Any experience universalized beyond what the source supports?
- [ ] Any closing aphorism?

If any box would be checked: revise before delivering.
