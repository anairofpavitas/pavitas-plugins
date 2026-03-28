---
name: style-mirror
description: >
  Analyzes a writer's prose style from sample text and produces a reusable style profile, then
  applies that style when writing or rewriting prose. Captures the full fingerprint: sentence
  rhythm, vocabulary, voice, dialogue style, description density, POV handling, pacing. Use
  this skill when the user wants to continue writing in the style of an existing project, match
  a specific prose style, create or update a style profile, apply a saved style to new writing,
  or rewrite a draft to match a target style. Triggers on "match my style," "write like this,"
  "continue in this style," "style profile," "analyze my writing style," "make it sound like
  the rest of the book," or any request to maintain stylistic consistency across sections of a
  work. Also triggers when the writing-interview skill is compiling a draft and a style profile
  exists or needs to be created for the project.
---

# Style Mirror

You analyze prose style and reproduce it. Not "inspired by" — matched. The goal is that a reader moving from a section the writer wrote to a section produced with this skill wouldn't notice the seam.

## The Content Firewall

This is critical: the style profile captures HOW the writer writes, never WHAT they wrote about. The sample text is a specimen — you're studying the brushstrokes, not the painting.

When building a profile, do not absorb or carry forward any of the following from the sample text:
- Plot events, character names, setting details, or world-building specifics
- Thematic content or narrative direction
- Specific metaphors or images (note the *type* of metaphor the writer uses, not the specific metaphors themselves)
- Dialogue content (note how dialogue is structured and tagged, not what characters say)

When applying a profile to new writing, the content comes entirely from the writer's interview answers or the draft being rewritten. The profile governs rhythm, structure, density, register, and technique. It never injects story material from the sample.

If a quoted example in the profile happens to share subject matter with the new scene, ignore the content of that example and follow only the structural pattern it illustrates.

## Two Modes

### Mode 1: Build a Style Profile

The writer provides sample text (pasted, uploaded, or pointed to a file). You analyze it and produce a style profile document.

### Mode 2: Apply a Style

You take a draft (from the writing-interview skill, or any rough text) and rewrite it to match a style profile. Or you write new prose that conforms to the profile from the start.

Both modes can happen in the same session. Analyze, then apply.

## Building a Style Profile

### What to Analyze

When given sample text (minimum ~500 words, ideally 1000+), break down these dimensions:

**Sentence Architecture**
- Average sentence length (word count). Note the range, not just the mean.
- How often do very short sentences appear? Where do they tend to land (scene openings, action beats, emotional moments)?
- How long do the longest sentences run? What do they tend to carry (description, interiority, action chains)?
- Sentence openers: how often do sentences start with the subject vs. a dependent clause vs. an action vs. a sensory detail? What's the dominant pattern?
- Use of fragments. How often, in what context.

**Paragraph Shape**
- Typical paragraph length (sentence count).
- Do paragraphs tend to be uniform or varied?
- How do paragraphs end? Mid-action, mid-thought, with a conclusion, on dialogue?
- Single-sentence paragraphs: how often, for what purpose?

**Vocabulary and Register**
- Reading level / complexity. Is the language plain, literary, somewhere between?
- Specific word preferences. Does the writer favor certain verbs, adjectives, or constructions? (e.g., uses "got" freely vs. avoids it, prefers Anglo-Saxon over Latinate words, etc.)
- Profanity level and style.
- Jargon or domain-specific language and how it's integrated.

**Voice and POV**
- POV and tense (third close past, first present, omniscient, etc.)
- Psychic distance: how close are we to the character's thoughts? Does the narration dip into their internal voice, or stay observational?
- How are thoughts rendered? Italicized direct thought, indirect free style, tagged internal monologue?
- Does the narrative voice have personality, or is it transparent?

**Dialogue**
- Tag style: "said" dominant, action beats, untagged, mixed?
- How does dialogue sit relative to action? Interleaved tightly, or in longer exchanges?
- Character voice differentiation through speech patterns, vocabulary, rhythm.
- Dialect or accent rendering approach.

**Description and Sensory Detail**
- Density: how much description per scene? Sparse, moderate, lush?
- Which senses get used most?
- How is description delivered? Woven into action, in dedicated passages, through character perception?
- Figurative language: frequency and type of metaphor/simile. Are they plain or elaborate?

**Pacing and Scene Construction**
- How are scenes entered? In media res, with setting, with action?
- Transition style between beats within a scene.
- How are scenes exited?
- Ratio of action to interiority to dialogue to description.

**Distinctive Patterns**
- Anything specific to this writer that doesn't fit the above categories. Recurring structural moves, signature rhythms, unusual punctuation choices, specific ways they handle time jumps, flashbacks, or exposition.

### The Profile Document

Output the profile as a markdown file named `[project-name]-style.md`. Structure it with the sections above, but write it as practical guidance, not academic analysis. The profile should be usable as a reference document — someone (or an AI) reading it should be able to write prose that matches.

For each dimension, include:
- What the writer does (the pattern)
- A specific example from the sample text (quoted)
- What to avoid (the anti-pattern for this writer's style)

Keep it concrete. "Sentences average 12 words, rarely exceed 25. Short fragments appear 2-3 times per page, almost always during action or emotional impact" is useful. "The writing has a varied rhythm" is not.

End the profile with a section called **Style DNA** — 3-5 sentences that capture the essence of this writer's style in plain language. This is the quick-reference version someone would read before writing.

### Updating an Existing Profile

If a style profile already exists and the writer provides new sample text:
- Analyze the new text against the existing profile
- Note what's consistent and what's evolved
- Update the profile, marking what changed and why
- Preserve the original observations where they still hold

The profile should reflect the current state of the writer's style for this project, not a historical average.

## Applying a Style

### From a Style Profile

When rewriting prose to match a profile:

1. Read the profile first. Internalize the patterns.
2. Rewrite sentence by sentence, matching:
   - Sentence length distribution (don't make every sentence the same length — match the *variation pattern*)
   - Opener patterns
   - Vocabulary register
   - Psychic distance
   - Description density
   - Dialogue formatting
3. After the rewrite, do a self-check: read the rewritten passage against the sample text. Does it feel like the same writer? If not, identify what's off and fix it.

The hardest thing to match is rhythm. Word choice is easy to adjust; the *feel* of how sentences move into each other is where most style-matching breaks down. Pay attention to how the original writer connects sentences — do they use conjunctions, juxtaposition, temporal markers, or just let the reader bridge the gap?

### From a Description (No Sample Text)

When the writer describes a target style without providing samples:
- Ask for reference authors or works if they have them (not to copy, but to calibrate)
- Build a lighter-weight profile from their description
- Write a short test passage (2-3 paragraphs) and ask if it matches what they're going for
- Adjust based on their feedback before writing the full draft

### What NOT to Do When Applying Style

- **Don't flatten the writer's rough-draft energy.** If the source material (from an interview, say) has raw, urgent phrasing, keep that even if the style profile is more polished. Style-matching is about the *craft patterns*, not about removing the writer's spontaneous voice.
- **Don't overcorrect.** If the profile says the writer uses short sentences, that doesn't mean every sentence should be short. Match the distribution, not the extreme.
- **Don't invent content to fill style patterns.** If the style profile shows the writer uses a lot of sensory detail but the source draft is light on it, don't add sensory details that aren't in the source material. Flag it in notes instead.
- **Don't lose the humanize-prose rules.** Style-matching sits on top of the anti-AI-writing rules, not instead of them. A style-matched draft should still pass the humanize-prose self-check.

## Integration with Writing-Interview

When the writing-interview skill is compiling a draft:

- If a style profile exists for the current project (check if the writer has mentioned the project name, or if a `[project]-style.md` file is available), apply it during compilation automatically.
- If no profile exists and this is a continuing project, ask before compiling: "Do you have sample text from earlier in this project I should match, or should I just compile raw?"
- If this is a new project with no profile and no samples, compile raw and offer to build a profile from the compiled draft itself once the writer has reviewed and edited it to their satisfaction.

The interview skill should never be blocked by the absence of a style profile. Raw compilation is always the fallback.

## File Management

Style profiles are saved to the writer's working directory as `[project-name]-style.md`. If the writer has a project folder structure, save them there. If not, save to the current working directory.

When loading a profile, check for it by project name. If the writer references a project you've worked on before but the profile isn't in the current directory, ask where it might be.
