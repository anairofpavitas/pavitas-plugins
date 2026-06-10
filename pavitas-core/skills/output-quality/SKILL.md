---
name: output-quality
description: Always-on quality constraints for everything Claude produces for Pavi. Two halves — prose (strip AI-isms from all non-technical writing) and visual (elevate all presentations, documents, dashboards, HTML beyond defaults). Read once per session; apply automatically without announcing. For deep work, read the matching reference file. Merges the former humanize-prose and design-elevation skills.
---

# Output Quality

Apply silently. The user sees polished output, never the process.

## Prose (all non-technical writing)

Full rules and examples: `references/prose-rules.md`. The non-negotiables:

**Structure**
- No "what [x] was [y]" constructions ("What changed things was..." → "The residency changed things.")
- No isolated short sentences dropped for dramatic punch
- No reversed constructions for rhetorical impact ("worse, not better")
- No tricolon escalation; no em dashes as theatrical pause markers

**Word blocklist** — strip on sight: genuinely, actually, clearly, obviously, simply, importantly, "here's the thing," "here's where," "that's the point," "it's worth noting"

**Paragraphs and voice**
- No tidy thesis restatements at paragraph endings; no aphoristic closers; no signposting
- Personal writing stays first-person; never universalize individual experience
- Working from source material: nothing the source doesn't contain
- Prefer the simpler sentence, match the source's register

**Pre-delivery check:** scan for every item above. Any hit → revise before delivering.

## Visual (presentations, documents, spreadsheets, HTML, dashboards, PDFs)

Generic is a choice, not a constraint. Build functional first, then elevate before delivering:

1. **Typography** — intentional typefaces, dramatic scale for hierarchy (3–4x between levels), weight system
2. **Color** — one primary + one accent + grays, applied functionally, with restraint
3. **Layout** — 8pt spacing system, grid alignment, generous margins, asymmetry where it guides attention
4. **Format polish** — slides: one idea per slide, 48–64pt headlines; sheets: styled headers, banding, right-aligned numbers, no gridlines; HTML: hover states, 0.2s transitions; docs: 1in+ margins, running headers

For substantial visual work, read before delivering: `references/interrogation-checklist.md`, then pull moves from `references/technique-catalog.md` and `references/reference-library.md`. Philosophy and bold-vs-restraint judgment: `references/design-philosophy.md`. Systematic order of operations: `references/elevation-protocol.md`.

**Quality gate:** no defaults remain; every choice explainable; consistent throughout; would survive a design director's review. Deliver with confidence — no hedging, no "here's a draft."

## Does NOT apply

Plain conversation, code without UI, technical documentation where house style governs, and any output where a brand-voice skill is loaded (brand voice wins on tone; prose rules still apply to mechanics).
