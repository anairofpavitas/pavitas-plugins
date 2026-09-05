# The crisis matrix, scope, and output order

---

## Scope — declared before anything else

The same commandment vocabulary operates at four levels, and a filled form is useless without knowing which one it describes.

| Scope | What it covers | Filename token |
| --- | --- | --- |
| **Global** | The whole story | `global` |
| **Quadrant** | One of four quadrants | `q1` … `q4` |
| **Sequence** | A named sequence (Arrival · Apprenticing and the Trunk Show · The Hunt) | slugged sequence name |
| **Scene** | A single scene, by its `<Sequence> - NN` handle | `arrival-02` |

If he declares it, take it. **If he does not, ask once.** Do not guess, and do not infer it from content. A scene crisis and its quadrant's crisis can be the same words at different altitudes, and mislabeling one contaminates the other.

**Check upward.** If a scene-scope commandment looks like it is also serving as its sequence's or quadrant's, say so in the analysis. Per `Bible/06 - Outline.md`, a global commandment will *likely* appear as a quadrant commandment, but that is not guaranteed — so this is an observation to report, **never an assumption to encode.**

---

## Working order vs. output order

### What he produces

1. **Crisis** — the dilemma
2. **The matrix** — pros and cons of each branch
3. **The question** — the either/or the crisis poses
4. **Climax** — which branch the protagonist actually takes
5. **Inciting Incident** — backfilled
6. **Turning Point** — backfilled
7. **Before-context / After-context** — arrives whenever it arrives

Not arbitrary. `Bible/06 - Outline.md` already records it: *"Pavi's working order, observed on the handwritten pages: Crisis → Climax → Resolution first, with II and TP backfilled underneath."* This skill formalizes an existing habit rather than imposing a new workflow.

### What he reads

Story order, matching the Bible table:

**Before-context → Inciting Incident → *Progressive Complications* → Turning Point → *Progressive Complications* → Crisis (+ matrix) → Climax → Resolution (+ After-context)**

---

## The matrix

Render as a real 2×2, not as prose.

**Type:** best bad choice · irreconcilable goods — taken from what he said. `Not stated` if he didn't classify it.

| | **Pros** | **Cons** |
| --- | --- | --- |
| **Choice A** — *his phrasing* | what it gains or preserves | what it costs or risks |
| **Choice B** — *his phrasing* | | |

**The question:** one either/or sentence, in his words where he gave one.

**Climax:** which branch, plus the matrix cells that activate — the cons he accepted and the pros he forfeited.

**Empty cells stay empty and are carried into the analysis.** A choice with no cons is not a choice, and a blank cell is the fastest available diagnostic. **Never fill one in to make the table look complete.**

**His phrasing of a choice *is* the choice.** Preserve the wording exactly in the matrix cells.

---

## Matrix → resolution linkage

The highest-value output in the skill. The After-context section maps every **con of the chosen branch** and every **forfeited pro of the rejected branch** onto what actually appears in the Resolution.

| Matrix cell | Branch | Manifests in R as | |
| --- | --- | --- | --- |
| Con A2 | taken | *what shows up on the page* | ✓ |
| Pro B1 | forfeited | — | `Not stated` |

**Unclaimed cells are the finding.** A cost named in the crisis that never surfaces in the resolution means the crisis had no teeth — the character paid nothing, and the scene is structurally free.

**Report every unclaimed cell explicitly.** Do not let a clean-looking table hide one.

---

## Before / after context

**Before-context** goes at the top: what has been going on in the story leading into the Inciting Incident. Orientation reads better before the beats than after them.

**After-context** folds into the Resolution section, and is where the linkage table lives.

---

## Part 2 — the beat pass

Triggered separately, appended to the same output under a `## Part 2 — Beats` heading. It may arrive in the same session or a later one; if later, append rather than creating a second file.

**Faithfulness rules apply here in full.** These are sentences intended for the page. Read `../../clean-draft/references/faithfulness.md` and obey it: no paraphrase, no smoothing, no improved verbs. Self-corrections resolve to his last version with the discarded version logged. Instructions are executed, not transcribed.

### Shape

Each event is a triad, **antagonist → protagonist → antagonist**, in that order. One sentence per role is the default reading of "three sentence events." **If he gives more than one sentence for a role, take all of it** — the triad shape is the invariant, the sentence count is not. Never truncate to force a three-line shape, and never pad to reach one.

```markdown
### II — Inciting Incident

**Event 1**
- **A:** <verbatim>
- **P:** <verbatim>
- **A:** <verbatim>
```

### Grouping

Triads group under their commandment, in story order:

**II → *PC* → TP → *PC* → Crisis → CL → R**

```markdown
### PC — narrowing (un-numbered, between II and TP)
```

```markdown
### PC — collapse (un-numbered, between TP and Crisis)
```

Either run may be empty in a given session, but **the first being empty is a finding, not a default.**

Each triad is tagged with whether it is **the moment of the commandment itself** or **a version of what would appear on the page** — he distinguishes these, and the distinction decides whether a line is structural notation or draftable prose. If he doesn't say, mark it `unspecified` rather than choosing.
