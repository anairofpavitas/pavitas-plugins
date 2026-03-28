---
description: Process a dictated audio transcript into clean prose. Removes false starts, filler words, and dictation artifacts while preserving the author's natural voice.
---

# Dictation Processing

Clean up dictated first drafts. Pavi uses dictation for discovery drafts — the raw transcript needs cleaning but the voice should be preserved.

## Execution

1. **Accept input**: transcribed text (from Perplexity Fiction Transcription Space or other source)
2. **Clean dictation artifacts**:
   - Remove false starts and restarts
   - Remove filler words (um, uh, like, you know)
   - Fix sentence boundaries (dictation often runs sentences together)
   - Correct obvious word substitutions from speech-to-text errors
   - Standardize punctuation
3. **Preserve voice**:
   - Keep Pavi's natural phrasing and word choices
   - Don't "improve" the prose — just clean the transcription noise
   - Maintain the discovery-draft energy
4. **Flag uncertainties**:
   - Mark any words or phrases that might be transcription errors
   - Note character names or invented terms that might be misspelled
5. **Output**: clean draft ready for revision

## Rules
- First pass only — don't edit for quality, just for transcription cleanliness
- Pavi's anchor phrase: "Let me see what happens next" — this is his writing mindset, respect it
- If the transcript includes stage directions or notes-to-self ("note: check this later"), preserve them as inline comments
- For LitRPG content: system messages and stat blocks may be dictated conversationally — format them properly
