---
description: Clean a dictated or handwritten draft. Delegates to raw-capture:clean-draft — the full interpretive layer (faithfulness rules, self-corrections, instruction handling, fiction formatting) lives there.
---

# Dictation Processing

Superseded. This command is a pointer, kept so the `/dictate` trigger keeps resolving.

**Load `raw-capture:clean-draft` and follow it.** Do not process the input from this file.

That skill handles both input modes — a pasted transcript or photographed handwriting — and carries the rules this command used to approximate: the priority order, the five permitted changes and the forbidden list, never-blend, the three-signal instruction test with its asymmetric-failure bias, the lexicon cross-check, and the notes contract.

If the material turns out to be thinking-out-loud rather than prose, or Five Commandments slots being filled, its triage will route to `raw-capture:sort-brainstorm` or `raw-capture:fill-commandments` instead.
