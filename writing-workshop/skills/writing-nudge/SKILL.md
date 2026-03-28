---
name: writing-nudge
description: >
  Set up recurring writing prompts for a project — creates a session state file, wires up a scheduled
  task, and establishes the end-of-session / start-of-session workflow for maintaining continuity.
  Use this skill whenever the user says "set up writing reminders," "writing nudge," "recurring writing
  prompts," "remind me to write," "motivate me to keep writing," "set up writing check-ins," or any
  variation where the user wants automated prompts to keep momentum on a writing project. Also triggers
  when the user wants to add a nudge system to an existing project, or when setting up a new project
  and they mention wanting regular prompts. If the user has just finished a writing interview session
  and mentions wanting to be reminded to continue, suggest this skill proactively.
---

# Writing Nudge

This skill is part of the **writing-workshop** plugin and designed to work alongside the **writing-interview** and **style-mirror** skills. It extends the interview workflow beyond live sessions by sending the writer periodic prompts — single concrete interview questions grounded in where they left off — so the story stays alive between sessions.

The nudge questions follow the same principles as the writing-interview skill: small, concrete, sensory, grounded in what was last written. They're not plot suggestions or homework — they're the kind of question that makes the writer start seeing the next scene in their head. If the writer replies, that reply feeds directly into the next writing-interview session as if they'd answered the question live.

## Why This Works

Writers lose momentum between sessions. The blank page is intimidating after days away. A well-timed question — specific, grounded in the last scene, easy to answer in a sentence — keeps the story alive in the writer's head even when they're not at the desk. It lowers the activation energy for the next session.

## What You're Building

Three things:

1. **A session state file** (`writing-session-state.md`) in the project folder — the bridge between sessions. It tracks where the story left off, what comes next, open questions, and the next interview question to ask. This file is what allows the scheduled task to generate questions without conversation context.
2. **A scheduled task** that reads the state file + current draft + style profile (from the style-mirror skill, if one exists), generates a single interview question, and delivers it via the writer's chosen notification method.
3. **A workflow contract** — at the end of every writing-interview session, the state file gets updated. At the start, any replies get folded in as interview answers.

## Setup Process

### Step 1: Gather Project Context

You need four things. Check the conversation and project files before asking — don't re-ask what you already know.

1. **Which project?** Identify the project folder, the current draft file, and the style profile (if one exists — this will be a `*-style.md` file created by the style-mirror skill).
2. **Where did the story leave off?** Read the most recent draft to understand the last scene, the last beat written, and what the natural next territory is.
3. **Schedule.** When and how often? Get specific: days of the week and time of day. Default suggestion if they're unsure: twice a week (Tuesdays and Fridays at noon) — frequent enough to maintain momentum, sparse enough not to become noise.
4. **Notification method.** How should the prompt reach them? Options and their tradeoffs:

   | Method | Pros | Cons |
   |--------|------|------|
   | **Email (Gmail)** | Clean sender/reply separation. Can include context recap. Reply thread is searchable. | Less immediate than a text. |
   | **iMessage** | Hits the phone directly. Casual, low-friction. | Sends as self-to-self (shows as both sent and received). Replies are indistinguishable from the prompt in the thread — harder to parse programmatically. |
   | **None (file only)** | No notification noise. Prompt logged to state file. | Writer has to remember to check. Defeats the nudge purpose for most people. |

   If the writer is unsure, recommend **email** — it's the cleanest round-trip for prompt → reply → next session integration. Be honest about the iMessage limitations.

   If they choose a notification method, get the relevant contact info (email address or phone number). If they want to decide later, proceed with "file only" and note the placeholder in the scheduled task.

### Step 2: Create the Session State File

Create `writing-session-state.md` in the project folder using the template in `references/state-file-template.md`. Read the template, then fill it in based on the current draft and project context.

Key sections to populate:

- **Current Position** — what scene, what happened, where the draft ends
- **What Comes Next** — the natural next territory based on where the draft left off
- **Open Questions** — anything unresolved from the project context (character details TBD, timeline questions, world-building gaps)
- **Threads to Track** — objects, consequences, or setups that need payoff
- **Interview Position** — set to "Not yet started" with a concrete first question based on where the draft ends
- **Reply Log** — empty, ready for entries

The first question matters. It should be sensory and specific — something that makes the writer see the next moment. "What does Yuri see when he steps into the library?" is better than "What happens next in the story?"

### Step 3: Create the Scheduled Task

Use the `create_scheduled_task` tool with these parameters:

- **taskId:** `{project-name}-writing-prompt` (kebab-case, e.g., `bookstore-writing-prompt`)
- **description:** `Send {writer} a writing prompt based on the current {project} state`
- **cronExpression:** Based on the schedule from Step 1 (e.g., `0 12 * * 2,5` for Tue/Fri at noon)
- **prompt:** Build from the template in `references/task-prompt-template.md`. Read it and fill in the project-specific details: project folder path, state file name, draft file name, style profile name, notification method, and contact info.

The task prompt must be entirely self-contained — future runs have no conversation context. It should include:

1. Explicit file paths for the state file, draft, and style profile
2. Instructions to generate a single concrete interview question (small, specific, grounded in the last beat)
3. Instructions to compose a short message (2-4 sentences: context line + question + optional nudge)
4. The notification step (send via chosen method, or log to file if no method chosen)
5. Instructions to update the Reply Log section of the state file with the generated prompt and date

### Step 4: Confirm the Workflow

Explain to the writer what will happen going forward:

- **End of writing sessions:** You (Claude) will update `writing-session-state.md` with where you stopped, open questions, and the next interview question. No action needed from the writer.
- **Between sessions:** The scheduled task fires on schedule, reads the state file, generates a question, and delivers it.
- **Start of writing sessions:** You (Claude) will check for any replies to the prompt (via the chosen notification channel) and fold them into the interview as if the writer had answered the question live.
- **If they don't respond:** That's fine. The prompt is a nudge, not homework. The next session picks up from the state file regardless.

Also recommend they do a manual "Run now" on the task from the Scheduled section in the sidebar to pre-approve any tool permissions the task needs (especially for notification methods that use external services).

## Integration with Writing-Interview Sessions

This skill doesn't replace the writing-interview skill — it feeds into it. The relationship:

- **writing-interview** runs the live session: asks questions, collects answers, compiles drafts.
- **writing-nudge** keeps the thread warm between sessions: sends one question, collects one optional reply.
- **style-mirror** provides the style profile that both the live interview (during compilation) and the nudge task (for tone context) reference.

When a writing-interview session ends, this skill's end-of-session protocol kicks in to update the state file. When the next writing-interview session begins, this skill's start-of-session protocol checks for replies first.

## End-of-Session Update Protocol

This isn't part of setup — it's the ongoing maintenance. After every writing-interview session (or any writing session) on a project that has a writing-nudge configured, update the state file:

```markdown
**Last updated:** {today's date}
**Last session type:** {Interview / Compilation / Revision / Discussion}
**Current draft file:** {filename}

## Current Position
{What scene, what beat, where the draft now ends}

## What Comes Next
{The natural next territory}

## Interview Position
**Phase:** {Where we are — mid-interview, post-compilation, etc.}
**Next question to ask:** {A concrete, specific question for the next nudge}
```

The "Next question to ask" field is the most important. Make it good — sensory, specific, grounded. This is what the scheduled task will build from.

## Start-of-Session Reply Check

At the start of a writing session, check for replies:

- **Email:** Search Gmail for recent threads with the project's prompt subject line. Read any replies.
- **iMessage:** Check recent messages to/from the writer's number. Look for messages that appear to be responses to a writing prompt (content-based judgment since iMessage doesn't clearly distinguish sender in self-to-self threads).
- **File only:** Check the Reply Log in the state file for any manually added entries.

If a reply exists, treat it as an interview answer. Acknowledge it, fold it into context, and continue the interview from there rather than re-asking the same question.
