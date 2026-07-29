---
description: Build this week's Pavitas Productions angle brief. Pulls Littlebird digest + Perplexity brief + active projects from Notion, picks every angle that clears the bar, and posts them as rows in the Pavitas Content database with verified source material. Autonomous — no review step. Angles and facts only; a human writer owns all copy.
---

# Pavitas Weekly Angle Brief

Fully autonomous. Gather → pick → document → post. No intermediate review. Flag problems, don't pause for permission.

**This skill does not write copy.** No hooks, captions, hashtags, scripts, beats, or on-screen text. A human professional writes all of that. The job here is to surface the angles worth writing about and hand over the verified material behind each one.

## Phase 1 — Gather

Spawn the `content-intel` agent. It returns a structured brief with:

- Littlebird Pavitas digest (from Pavitas Content DB, this week) — plus a second `Source = Zo` activity digest some weeks, which doesn't always agree with the Littlebird one
- Perplexity industry brief (from same DB, this week)
- Active Audiobook Projects status
- Recent Littlebird Log signal (past 14 days)
- Upcoming releases
- **Conflicts** — facts two sources disagree on, returned unresolved
- **Privacy-Flagged** — topic area only, not for use
- **Raw Recurrence** — what repeats across the window and on which dates

Every item arrives with a page title, URL, and date. Carry those citations through to the brief; don't re-query Notion for them, and don't drop them.

The agent does not pre-select. `Raw Recurrence` is pattern-matching with no judgment attached — it reports what repeats, not what's worth writing about. Picking is Phase 2's job.

If the agent flags a missing input (no digest or no brief for this week), continue anyway — use what's available. Do not block on missing inputs. Conflicts and privacy flags are not missing inputs — they carry into Phase 2 and Phase 3 as constraints.

## Phase 2 — Pick angles

Load the `pavitas-brand-voice` skill. It governs whether an angle is on-brand — not how anything gets written. Apply its position rules, specificity floor, subject-vs-angle test, and privacy exclusions.

Find angles by looking for the skill's six connection patterns across sources — Collision, Recurrence, Transfer, Timing, Lineage, Absence. An angle drawn from a single source is fine and often necessary; label it Single-source.

Pick **every angle that clears the bar.** There is no target number. Order rows by connection scarcity — a link nobody else could draw ranks above a clean single-source update. Keep angles distinct; don't file the same story twice under different framings.

**Quality gate:** An angle clears the bar when it has a reason to exist this week and one concrete anchor behind it — a named book, a specific line, a dated session, a decision with a before and after, a number, a mistake. Anything that fails either test doesn't go in. Zero qualifying angles is a valid outcome — say so and explain why. Never pad to hit a count.

## Phase 3 — Build the angle brief

For each angle that cleared the gate, document seven fields. Facts only.

- **Angle** — one sentence stating the claim or tension. Not the subject. "Finished book 3" is a subject; "book 3's villain needed a smaller voice than book 2's" is an angle.
- **Pattern** — Collision, Recurrence, Transfer, Timing, Lineage, Absence, or Single-source.
- **Why now** — why this week and not next. The timeliness argument.
- **Anchor & source material** — lead with the one concrete anchor, then the supporting facts a writer can't derive alone: title, author, publisher, release date, chapter or hour counts, specific moments, links. Cite each source by page title, URL, and date.
- **Constraints & credits** — embargo dates, who must be tagged, handles, release-date gates, unresolved source conflicts, privacy splits, anything that would be an error if gotten wrong.
- **Open questions** — what the writer needs from Pavi that the sources don't answer. "None" if nothing.
- **Confidence** — verification status. Flag anything unverified so it gets checked before it goes out. If the verification pass came back clean, say "verified."

Do not suggest a format, platform, or asset treatment. That's the writer's call.

Three rules survive from the old draft phase, as facts rather than style:

- Every angle carries one concrete anchor. No anchor, no angle — and never invent one.
- Credits are accurate — author, publisher, release date. If uncertain, flag it in Confidence rather than guessing.
- Source conflicts are surfaced in Constraints, never resolved silently by picking the more convenient reading.

## Phase 3.5 — Verify

**Required. Do not skip because the run is autonomous — that's the reason it matters.**

Spawn a subagent that did not build the brief and have it check every angle against the skill's verification list: URLs resolve, every number and quoted phrase appears in a cited source, the cited section actually contains the fact, inference is labeled as inference, status claims match the most recent source, conflicts are surfaced, and nothing privacy-excluded has leaked in.

Correct what fails before posting. Carry what the verification caught into Phase 5.

## Phase 4 — Post to Notion

**Target DB:** https://www.notion.so/eb0089eb3ccc83928e5c017c1f66a70c?v=702089eb3ccc82f4a2d2080fa27c25c1

Create **ONE parent page** titled:

```
Pavitas Angle Brief [YYYY-MM-DD]
```

Set properties:

- **Date** field → today's date (use `date` command via bash if unsure)
- **Source** field → "Claude"

Inside the parent page, create a table with one row per angle. Columns:

| Angle | Pattern | Why now | Anchor & source material | Constraints & credits | Open questions | Confidence |

Order rows by connection scarcity, strongest first.

If zero angles cleared the gate, create the page anyway with a single block titled "No angles this week" and a one-sentence explanation of what was missing.

## Phase 5 — Report back

After posting, return a one-screen summary to Pavi:

- Notion page URL
- Each angle in one sentence, with its pattern
- What the verification pass caught and corrected
- Any flagged issues (missing inputs, release-date risks, credits that need verification, unresolved source conflicts)

No postamble. No "Let me know if you need changes."

## Hard rules (enforced at every phase)

- Never claim an endorsement that wasn't given
- Never surface embargoed work
- Credit author + publisher + release date accurately — if uncertain, flag it
- **Privacy.** Nothing under a Privacy Flag in the source material. No health, medical, or sexual-health content. No relationship or therapy content. No third-party private information. No financial specifics — rates, invoice amounts, revenue, tax detail. This outranks how strong the angle is. See the skill's Privacy section for the split-thread rule.
- Never invent an anchor, quote, date, or source. Inference gets labeled as inference.
- Quality over cadence — one strong angle beats three weak ones
- No copy. If output contains a hook, caption, hashtag, or script line, it's wrong.
