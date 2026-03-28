# Writing Workshop

A Cowork plugin that helps writers get words on the page through guided conversation.

## Skills

### project-setup
Sets up a new writing project from scratch — creates the folder, generates project instructions and reference files, walks you through the premise/characters/style, optionally kicks off a style profile, and registers the project in a manifest. Start here when beginning something new.

### writing-interview
Interviews you through a scene, chapter, or piece one small question at a time, then compiles your answers into a rough prose draft with an appendix of suggestions, unanswered questions, and logical deductions.

### style-mirror
Analyzes your prose style from sample text and produces a reusable style profile. When a profile exists for your project, the writing-interview skill applies it automatically during compilation.

### writing-nudge
Sets up recurring writing prompts for a project — creates a session state file, wires up a scheduled task, and establishes end-of-session / start-of-session hooks for continuity. Between writing-interview sessions, the scheduled task reads the state file and current draft, generates a single concrete interview question, and delivers it via the writer's chosen method (email, iMessage, or file-only). Replies feed back into the next writing-interview session.

## Typical Workflow

1. **New project?** Say "set up a new writing project" → project-setup walks you through it
2. **Ready to write?** Mount the project folder, say "let's do a writing interview" → writing-interview pulls the scene out of you
3. **Want style consistency?** Provide sample text → style-mirror builds a profile that writing-interview uses automatically
4. **Want momentum between sessions?** Say "set up writing reminders" → writing-nudge creates a recurring prompt that keeps the story alive in your head

## How the Skills Connect

- **project-setup** creates the project folder and files that all other skills reference.
- **style-mirror** produces a style profile that **writing-interview** applies during compilation and **writing-nudge** reads for tone context.
- **writing-interview** runs the live session. At the end, **writing-nudge**'s update protocol saves session state for the next prompt.
- **writing-nudge** sends prompts between sessions. At the start of the next **writing-interview** session, any replies get folded in as interview answers.

## Style Profiles

Style profiles are saved as `[project-name]-style.md` files. Store them in your project folder or any directory you'll mount in future sessions. The plugin finds them by project name.

## Usage

Say things like:
- "new writing project" / "set up a project" / "start a new book"
- "interview me" / "help me write" / "let's do a writing session"
- "build a style profile from this sample"
- "match my style" / "continue in this style"
- "set up writing reminders" / "writing nudge" / "remind me to write"
