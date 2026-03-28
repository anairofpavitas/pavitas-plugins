---
name: project-setup
description: >
  Sets up a new writing project from scratch — creates the folder, generates project instructions
  and reference files from templates, walks the writer through filling in premise/characters/style,
  optionally kicks off a style profile, and registers the project in a manifest. Use this skill
  whenever the user says "new writing project," "set up a project," "start a new book," "create
  a project folder," "initialize a writing project," or any variation of wanting to begin a new
  fiction or nonfiction writing project from zero. Also triggers on "project setup," "new story
  setup," "set up my novel," or when a user references the writing-workshop plugin and wants to
  start something new. If the user seems to be starting a new creative writing project and doesn't
  have their files organized yet, suggest this skill proactively.
---

# Project Setup

You're setting up a new writing project. The goal: by the end of this process, the writer has a project folder with everything they need to start working — instructions that tell future Claude sessions how to collaborate on this project, a reference file for continuity tracking, and optionally a style profile to match.

## Why This Exists

Starting a writing project with Claude requires a few things to be in place: a project instructions file (so each session knows the workflow, the do's and don'ts, and the project context), a reference file (so characters, world-building, and scene history stay consistent across sessions), and ideally a style profile (so compiled drafts sound like the writer). Setting all this up by hand is tedious and easy to forget. This skill does it through conversation.

## The Process

### Step 1: Name and Location

Ask two things:

1. **Project name.** This becomes the folder name and the prefix for all project files. Keep it simple — one or two words, no special characters. If they give you a long title, suggest a short working name.

2. **Where should the folder live?** Check if a workspace folder is mounted. If so, offer it as the default. If not, ask them to specify a path or select a folder. The project folder will be created as a subdirectory at this location.

Create the folder. If it already exists, stop and ask — don't overwrite.

### Step 2: The Interview

Walk through these questions to populate the project files. Keep it conversational — don't dump all questions at once. One or two per turn, following the energy of the conversation.

**Core (required):**
- What's this project? (Genre, format — novel, novella, short story, series)
- Give me the premise in 2-3 sentences. (Protagonist, central conflict, what makes it interesting)
- POV and tense? (First person present, third close past, etc. If they're unsure, help them think through it based on the genre and story they described)

**Characters (at least the protagonist):**
- Who's the main character? Name, key physical details, anything about how they talk or carry themselves.
- Any other characters already in mind? (Don't push — if they only have the protagonist, that's fine. The reference file gets updated as the project develops.)

**World-building (if applicable):**
- Anything about the setting that needs to stay consistent? (Magic systems, technology level, social structures, terminology)
- For contemporary/realistic fiction, this might just be "where and when does it take place?"

**Style (optional but valuable):**
- Do you have existing prose from this project to build a style profile from?
- If not, are there reference authors or works that capture the feel you're going for?
- If they have sample text, offer to run the style-mirror skill after setup is complete.

**Workflow preferences (project-specific):**
- Anything specific to how you want to work on THIS project that might differ from your defaults? (e.g., "I want to write this one in strict scene-sequel structure" or "Don't ask about romance subplots, there aren't any" or "This one's comedy — keep the interview light")

### Step 3: Generate the Files

Create three files in the project folder:

#### `[project-name]-instructions.md`

This is the project's instruction file — it tells future sessions how to work on this project. Use the template from `references/project-template-instructions.md` in the writing-workshop plugin as the structural base, but fill it in with everything from the interview. The key sections:

- **What This Is**: The premise, populated from the interview
- **How We Work**: Keep the standard writing-workshop workflow and do's/don'ts from the template. Add any project-specific preferences the writer mentioned.
- **Style Reference**: Point to the style profile file if one exists or will be created. If not, note the reference authors/works they mentioned, or leave it as "to be created from early drafts."
- **Project Reference**: Point to the reference file.

#### `[project-name]-reference.md`

The continuity tracker. Use `references/project-template-reference.md` as the base. Populate with:

- **Characters**: Everything from the interview, formatted for quick reference. Name, role, physical details, speech patterns.
- **World-Building**: Setting details, rules, terminology from the interview.
- **Scene History**: Empty for now — this gets populated after each writing session.

#### `[project-name]-style.md` (only if they provided sample text)

If the writer provided sample text during setup, run the style-mirror analysis and save the profile. If they mentioned reference authors but don't have their own samples, note this in the instructions file — the profile will be built later from edited drafts.

### Step 4: Register in Manifest

Check for `projects.json` in the writing-workshop plugin directory. If it doesn't exist, create it. Add an entry for the new project:

```json
{
  "projects": [
    {
      "name": "Project Name",
      "slug": "project-name",
      "path": "/path/to/project-folder",
      "created": "2026-03-21",
      "genre": "progression fantasy",
      "status": "active",
      "has_style_profile": false
    }
  ]
}
```

If the plugin directory is read-only, save `projects.json` in the project folder itself and let the writer know where it is.

### Step 5: Summary and Next Steps

Show the writer what was created:
- List the files and what each one does
- If a style profile wasn't created, mention that they can build one anytime with the style-mirror skill once they have edited prose they're happy with
- Suggest their first session: "Mount this folder and say 'let's do a writing interview' to start your first scene"

## Edge Cases

**Writer already has a folder with some files:**
Don't bulldoze it. Check what's there. If they have a reference file but no instructions, just create what's missing. If the folder has drafts but no project files, offer to set up the project infrastructure around what exists.

**Writer is vague on premise:**
That's fine — some people discover the story by writing it. Fill in what you can, mark the rest as TBD, and move on. The instructions and reference files can be updated later. Don't make them feel like they need everything figured out before they can start.

**Writer wants to convert an existing project:**
If they have a project that's been going without these files, help them build the files from what they know. Ask about characters already established, scenes already written, and any style they've developed. This is setup in reverse — archaeology, not architecture.

**Multiple POV or tense:**
Some projects switch POV between characters or timelines. Note this in the instructions file clearly, including which characters get which POV/tense treatment.

## Integration with Other Skills

- **style-mirror**: If the writer provides sample text, hand off to style-mirror for profile generation. The style profile file should be saved in the project folder with the naming convention `[project-name]-style.md`.
- **writing-interview**: The instructions file this skill generates is what the writing-interview skill reads at the start of each session to know how to work on the project.
- **humanize-prose**: The instructions file inherits the anti-AI-writing rules by default through the writing-interview's compile phase. No special configuration needed.
