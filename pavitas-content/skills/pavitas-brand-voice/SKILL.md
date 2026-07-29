---
name: pavitas-brand-voice
description: Pavitas Productions brand perspective for @pavitasproductions content. Use when deciding what a post should be about — reads the week's source material and returns candidate topics, angles, and cross-source connections, each cited. Governs perspective, standing, and angle selection. Does not govern word choice, phrasing, or format. Distinct from @pavi.spins.yarns (fiber arts).
---

# Pavitas Productions — Perspective & Angles

## Scope

**This skill decides what's worth talking about, from what position, and what connects to what.** Output is a cited slate of candidate topics.

**It does not write copy.** No phrasing rules, no banned words, no format specs, no tone policing. A human writer takes the slate and writes. If asked for finished copy, hand over the slate and say the writing step belongs downstream.

## The position

This is the voice. Not the vocabulary — the seat Pavi is speaking from.

- **Practitioner, not commentator.** Every topic has to be something he did, chose, noticed, or got wrong inside the work. If the only available stance is "here's what's happening in the industry," it isn't a topic yet — find the chair he was sitting in when it mattered to him. Demote anything he could have written without having been there.
- **Standing before opinion.** Nine years, hundreds of finished hours, LitRPG/progression/sci-fi, Aethon / Podium / Recorded Books / Blackstone / Audible direct. He can assert from that. Topics that only work if the audience grants him authority in a domain he hasn't actually worked in get demoted or reframed to what he does know.
- **The audience is already inside the genre.** Cultivation, system apocalypse, dungeon core, gamelit-vs-LitRPG are common ground. A topic that only works after explaining the genre is aimed at the wrong room.
- **Craft is one problem in different materials.** Narration, Story Grid, opera, improv, acting, crochet. Cross-discipline topics are a feature, not a stretch — they're usually the strongest thing on the slate.
- **Person behind the voice, not personality account.** Personal material earns its place by explaining the work. Dogs, Chicago, Colin, the booth at 6am — in when they carry a craft point, out when they're content for content's sake.

## Specificity floor

A candidate is not a topic until it has **one concrete anchor**: a named book, a specific line, a dated session, a decision with a before and after, a number, a mistake.

- Fails: "Recording is harder than people think."
- Passes: "Chapter 14 took four takes because the antagonist's grief kept coming out as anger."

If no anchor exists in the source material, mark the candidate `NEEDS ANCHOR` and name exactly what's missing. **Never invent one.**

## Subject vs. angle

A subject is what it's about. An angle is the claim, tension, or reversal inside it. Return angles.

| Subject | Angle |
|---|---|
| Finished book 3 | Book 3's villain needed a *smaller* voice than book 2's, and I didn't work that out until the last chapter |
| Story Grid session | The scene wasn't broken — the value shift was happening to the wrong character |
| Doing an audition | I stopped reading for the character and started reading for the author's ear |

Every candidate carries one sentence stating its tension. If you can't write that sentence, it's a subject, not a topic.

## Source material

Pull from these. Cite every one you use.

| Source | Where | What it gives |
|---|---|---|
| Pavitas Content DB — Littlebird Pavitas digest | https://www.notion.so/eb0089eb3ccc83928e5c017c1f66a70c?v=702089eb3ccc82f4a2d2080fa27c25c1 | Week's session and project narrative |
| Pavitas Content DB — Perplexity industry brief | same DB | Genre and industry signal |
| Audiobook Projects DB | https://app.notion.com/p/a33eb55fdef34b19852484ddde4c3be8 — statuses Recording / Batched / Submitted / Editing / Approved / Standing By | Title, author, publisher, word count, dates, status |
| Littlebird Log — past 14 days | Notion search; filter Pavitas, recording, narration, craft, Story Grid, audition, booth, session, publisher, release | Dated craft observations, the raw stuff |
| Release calendar | Audiobook Projects dates ≤30 days; author-friend drops ≤14 days noted in the Log | Timing pressure |

The `content-intel` agent gathers these. This skill reads what it returns.

## Privacy

**Excluded from candidate generation entirely, regardless of how strong the pattern is:**

- Anything under an explicit Privacy Flag in the source material. Littlebird Log entries carry these. Honor them without exception.
- Health, medical, and sexual-health content. Diagnoses, prescriptions, symptoms, lab results, appointments, providers.
- Relationship and therapy content. Couples work, counseling, conflict with Colin or family.
- Third-party private information — anyone's health, finances, or personal circumstances, named or identifiable.

Financial specifics are excluded too: rates, invoice amounts, revenue figures, tax detail. A general point about how the business works can survive; the numbers don't.

**This rule outranks connection strength.** In a real July 2026 pass, the single strongest recurrence across two weeks of material was a health-vs-hustle pattern named in three consecutive digests. It was correctly discarded. When a privacy-blocked thread has a publishable half — the craft or scheduling side with the medical side removed — you may carry the safe half forward, but say in the candidate that you split it and what you left out.

## Connection discovery

Single-source updates are fine and often necessary. **Cross-source connections are the reason to bother.** Rank by scarcity — a link nobody else could draw beats a clean announcement.

Look for six patterns:

**1. Collision** — the industry brief claims something his week contradicts or complicates.
*e.g. The trade story is a voice built in audio being carried into a TV pipeline; the same week he shipped a system for keeping character voices consistent across a series.*

**2. Recurrence** — the same idea shows up two or more times inside 14 days. He's already chewing on it, which means he has something to say.
*e.g. The same Story Grid failure mode — characters acting on their own volition instead of being driven by the environment — logged in two consecutive digests.*

**3. Transfer** — a principle from one discipline explains a decision in another.
*e.g. A note about a character slipping from institutional into private register is a writing correction and a narration correction in the same breath.*

**4. Timing** — a craft moment sitting next to a release date or a deadline, so the reflection and the announcement are the same post.

**5. Lineage** — a decision on this book traceable to something established on an earlier one. Progression is the genre; it's also the account.
*e.g. Re-splitting already-recorded epigraphs on book 8 so the file structure matches books 1–7.*

**6. Absence** — something conspicuously missing. A project that stalled. A voice he can't find. A discipline that went quiet.

Name the pattern on every candidate that has one.

## Source conflicts

Source material is fallible. Digests are synthesized by other agents and have been caught carrying fabricated names, inconsistent labels, and stale status. A fact can pass every citation check and still be wrong.

When two sources disagree:

1. **Never resolve it silently.** Picking the more convenient reading is the most likely failure mode of this whole skill.
2. Prefer the more recent source, and prefer a database record over a narrative summary for structured facts (dates, counts, status).
3. State the conflict as a constraint on the candidate — what disagrees, what each source says, and what the writer must confirm with Pavi before publishing.
4. If the conflict is load-bearing for the angle, the candidate drops to `Needs work` until it's resolved.

Watch specifically for: project status contradicted between a digest and a same-day journal entry, lesson or version numbering that shifts between sources, author names that are pen names, and dates in ambiguous formats.

## Output — the topic slate

Ranked, 5–9 candidates. One block each:

```
### [N]. [Angle sentence — the claim or tension, one line]

**Anchor:** [the concrete thing]
**Pattern:** [Collision / Recurrence / Transfer / Timing / Lineage / Absence / Single-source]
**Why now:** [one line — what makes this week the week]
**Sources:**
  - [Page title] — [URL] — [date]
  - [Page title] — [URL] — [date]
**Strength:** [High / Medium / Needs work] — [one clause of reasoning]
**Open questions:** [what the writer needs from Pavi that the sources don't answer, or "none"]
**Constraints:** [source conflicts, unverified credits, privacy splits, things not to claim — omit if none]
```

Then a closing line: what the week's material is thin on, and what would fix it next week.

**When `/pavitas-content:weekly` is the caller,** it posts a Notion table with fixed columns. Map to them: Angle → Angle, Pattern → Pattern, Why now → Why now, Anchor + Sources → Anchor & source material, Constraints → Constraints & credits, Open questions → Open questions, and the verification result → Confidence. Strength doesn't get a column there; it decides row order instead, strongest connection first.

## Verification

**Required before any slate is handed off.** Run it as a separate pass — ideally a subagent that did not build the slate.

Check every candidate for:

1. **URL resolution** — each cited link opens a real page whose title matches what's claimed.
2. **Fact-to-source** — every number, date, name, and quoted phrase appears in a cited source. Not paraphrased from memory of it.
3. **Citation accuracy** — the specific section named actually contains the fact. Crediting the right document but the wrong section is the common miss.
4. **Inference labeled** — arithmetic (day counts, elapsed time, totals) and anything derived rather than stated is marked as inference, not asserted as fact.
5. **Status claims current** — "shipped," "delivered," "passed," "verified" are checked against the most recent source, not the most flattering one.
6. **Conflicts surfaced** — every disagreement between sources appears as a constraint, not a silent choice.
7. **Privacy** — nothing excluded above has leaked in, including via a split thread.

Correct what fails, and keep a short record of what the verification caught. That record is useful signal about which sources are drifting.

## Accuracy constraints

Not style. Risk.

- Credit author, publisher, and release date accurately. Uncertain → flag it, don't guess. Empty fields in the projects DB are common; a digest mention is not confirmation.
- Nothing embargoed.
- No endorsement claimed that wasn't given.
- No claim about another narrator, author, publisher, or their work beyond what a cited source states. Industry news is an occasion for a topic, not a subject to comment on.
- Never invent an anchor, a quote, a date, or a source. Every factual claim on the slate traces to a cited entry. If it came from inference, label it inference.

## Quality over cadence

If the week's material yields three real candidates, return three. If it yields none, say so and name what's missing. A padded slate wastes the writer's time and produces the thin posts it was meant to prevent.
