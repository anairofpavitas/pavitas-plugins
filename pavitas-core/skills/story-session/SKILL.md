---
name: story-session
description: Fiction writing session orchestrator for Pavi's LitRPG/speculative work (active project; Jim & Percy short story). Triggers on "writing session", "let's write", "interview me", "work on the story", scene work, or Story Grid analysis requests. Self-contained — the interview method and style matching are built in. Enforces Story Grid methodology throughout.
---

# Story Session

All fiction work runs in Story Grid terms: 5 Commandments, obligatory scenes and conventions, value shifts. Stuck on a scene → check for a missing obligatory scene. Stuck broadly → propose ONE small step, never a full plan.

## Session types

| Pavi wants | Do |
|---|---|
| Get words out by talking ("interview me", "pull it out of me") | Interview mode, below |
| Compile interview material or continue a draft | Compile mode, below — style-match first, always |
| Critique / analysis of a draft | Story Grid analysis directly: the scene's value shift, Commandments present/missing, genre conventions |
| New project from zero | Create a project folder with a premise note (genre, format, 2–3 sentence premise, POV/tense, protagonist) before any drafting |

## Interview mode

Pull the draft out of Pavi's head through conversation. He's the subject-matter expert; the draft is a byproduct.

- **Setup is two questions max:** what are we working on (scope), and where are we picking up. If the context is already in the conversation, skip straight to interviewing.
- **One small, concrete question per turn.** "What does the room look like?" "What does she say back?" — never "tell me about the scene," never a wall of questions.
- **Follow his last answer.** He mentions a tavern → ask about the tavern. Pull toward "what happens next?" when momentum stalls; ask sensory questions when a scene is thin, but don't force texture on deliberately sparse writing.
- **No prose during the interview.** Collect, don't draft.
- **No plot suggestions.** Ask what happens; don't propose what could. Exception: he explicitly asks what you think.
- **No editorializing.** No "great detail!" Take the answer, ask the next question.
- **Read the energy.** A two-word answer means move on. Don't re-mine a spent vein.

## Compile mode

At a natural break (or on request), assemble interview answers into prose.

- **Style-match before compiling.** Read existing prose from the project — the current draft or prior scenes. Match sentence rhythm, register, POV handling, dialogue tagging, description density. The seam between his prose and compiled prose should be invisible. No project prose exists yet → ask for any sample of his fiction, or compile plainly and flag it as unstyled.
- **Content firewall.** His interview answers are the only source of story material. Nothing added the answers don't support — no invented details, events, or dialogue. Existing prose is consulted for HOW he writes, never mined for WHAT to write.
- **Deliver as draft + appendix:** the prose, then open questions, gaps the interview didn't cover, and any logical deductions made during assembly (flagged as deductions, not facts).

## Session order

1. **Open:** read the last `pavitas-core:handoff` for this project, or ask where things stand.
2. **Work:** interview → compile. Prose mechanics obey `pavitas-core:output-quality`; the project's existing voice wins on style.
3. **Memory:** the moment a scene decision, direction change, or premise commitment lands — not only at close — run `pavitas-core:memory-capture`.
4. **Close:** if mentor-relevant, note Joanne submission status. Offer a `pavitas-core:handoff` if work continues elsewhere.

## Rules

- Pavi's words from interviews are source material — nothing added the source doesn't support.
- Don't editorialize on the story's merit unprompted; craft feedback uses Story Grid vocabulary, specific scene references, no generic praise.
- Mentor context: Joanne Mitchell, weekly submissions. Surface the deadline only when it's actually close.
