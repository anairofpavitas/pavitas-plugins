---
name: story-session
description: Fiction writing session orchestrator for Pavi's LitRPG/speculative work (active project; Jim & Percy short story). Triggers on "writing session", "let's write", "interview me", "work on the story", scene work, or Story Grid analysis requests. Routes to the writing-workshop leaf skills and enforces Story Grid methodology throughout.
---

# Story Session

All fiction work runs in Story Grid terms: 5 Commandments, obligatory scenes and conventions, value shifts. Stuck on a scene → check for a missing obligatory scene. Stuck broadly → propose ONE small step, never a full plan.

## Route by session type

| Pavi wants | Read and follow |
|---|---|
| New project from zero | `writing-workshop:project-setup` |
| Get words out by talking ("interview me", "pull it out of me") | `writing-workshop:writing-interview` |
| Match/maintain prose style, compile interview output | `writing-workshop:style-mirror` (load or create the project's style profile BEFORE compiling any prose) |
| Recurring prompts / momentum system | `writing-workshop:writing-nudge` |
| Critique / analysis of a draft | No leaf — Story Grid analysis directly: identify the scene's value shift, Commandments present/missing, genre conventions |

## Session order (when drafting)

1. Open: check the project's session state file (writing-nudge convention) or last handoff for where things stand.
2. Work: interview → compile via style-mirror. Prose mechanics obey `pavitas-core:output-quality`; the style profile wins on voice.
3. Close: update session state; if mentor-relevant, note Joanne submission status. Offer a `pavitas-core:handoff` if work continues elsewhere.

## Rules

- Style profile before prose compilation, always. No profile → create one first from existing project text.
- Pavi's words from interviews are source material — nothing added the source doesn't support.
- Don't editorialize on the story's merit unprompted; craft feedback uses Story Grid vocabulary, specific scene references, no generic praise.
- Mentor context: Joanne Mitchell, weekly submissions. Surface the deadline only when it's actually close.
