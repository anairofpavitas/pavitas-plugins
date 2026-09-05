# raw-capture

Three skills that turn raw captured writing into clean, structured output. Loads as `raw-capture:<name>`.

Ported from the Zo Computer family — `dictation-to-draft`, `dictation-to-brainstorm`, `dictation-to-commandments` — with the transcription pipeline removed. The Zo skills weld the judgment to one ingest path (ElevenLabs Scribe v2 → `condense.py` → a vault tree), which is why they don't travel. The judgment is independent of all of it.

## Skills

| Skill | What it does |
|---|---|
| `raw-capture:clean-draft` | Recovers manuscript prose. His words, cleaned — false starts, self-corrections, instructions, formatting — never improved. |
| `raw-capture:sort-brainstorm` | Sorts thinking-out-loud into the Bible's own nine sections, then asks what doesn't hold together. Nothing it produces is canon. |
| `raw-capture:fill-commandments` | Fills a Five Commandments skeleton and crisis matrix, checks the matrix against the resolution, optionally appends a verbatim beat pass. |

## Input

Two modes, and they have **inverted strengths**:

| | Text mode (pasted transcript) | Page mode (photographed handwriting) |
|---|---|---|
| Word accuracy | Exact | Fallible, uncalibrated |
| Proper nouns | As transcribed | Highest-risk element |
| Self-corrections | Inferred from wording | **Explicit** — a strikethrough isn't a judgment call |
| Instruction detection | 2 of 3 signals — weakest | **3 of 3** — margin, box, arrow |
| Structural moves | **Never applied** | May apply on a clear arrow |

Neither is a degraded version of the other. `clean-draft/references/triage.md` is the authority, and every skill reports which mode it ran in.

**Audio is out of scope.** Claude's model reads text and images; it does not hear. Transcribe upstream (superwhisper, Letterly, Scribe on Zo) and paste the result in — **raw**, ideally, since a source that has already stripped false starts destroyed the evidence separating a self-correction from an instruction. The skills say so in their report when that's the case.

## Shared references

`clean-draft/references/` is the core, read by all three:

- `faithfulness.md` — priority order, the five permitted changes, the forbidden list, corrections, instruction detection and tiers, the notes format. The reason for the port.
- `triage.md` — input mode, then session type. The two-mode signal map lives here.
- `fiction-formatting.md` — fiction convention and LitRPG system blocks.

The other two skills reference these by relative path rather than restating them. In the Zo family, two of the three said "read `dictation-to-draft`'s Stage 1 and follow it exactly" — pointing at another skill's prose, which is what made it fragile.

`fill-commandments/references/five-commandments.md` is an **operative copy**. The canonical source is `Documents/Writing/Five Commandments - method.md` on Zo; when they disagree, that file wins and the copy is the bug.

## Output

Cleaned output in the conversation by default, with a `## Notes` section. Files only when Pavi says where, or when a folder is connected and he asks — using the Zo filename conventions so anything produced here drops into the vault by hand without renaming.

**Never edits an existing prose file in place.** That's `writing-desk`'s proposals-only rule, stated so it survives outside the vault.

## What was deliberately left behind

Stage 1 (the Scribe curl, `keyterms` encoding, `no_verbatim`, `~/.zo_secrets`), Stage 1.5 and `condense.py`, the pause table, the `Dictation/` tree, the `audio/processed/` move and the purge contract, and the `knitrpg-vault-sync` git rules. All of it transmission, none of it judgment.

The lexicon changed character rather than being dropped: it was a Scribe API parameter capped at 100 keyterms, which is why a per-session shortlist existed. As reading context there's no cap — all ~282 names load, and the selection logic is obsolete.

## Connectors

None bundled. No `.mcp.json`, no `agents/`, no `commands/`.

## Relationship to creative-writing

`creative-writing:dictate` was a `model: haiku` command whose stated job — "accept transcribed text, clean dictation artifacts" — is exactly `clean-draft`'s trigger. It now delegates here rather than competing.
