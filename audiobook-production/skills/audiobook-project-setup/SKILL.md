---
name: audiobook-project-setup
description: Create folder hierarchy for new audiobook projects. Triggers include "prepare folders for audiobook", "new audiobook project folders", "set up audiobook directory", "create audiobook folder structure", or any request to create folders/directories for an audiobook project. Creates a standardized folder structure with Assets, Chapters, and CRX subfolders.
---

# Audiobook Project Setup

Create the standard folder hierarchy for a new audiobook project.

## Workflow

1. Ask for the book's short title
2. Ask where to save the folder structure (request directory access if needed)
3. Create the folder structure in the specified location:

```
[Location]/[Short Title]/
├── [Short Title] Assets
├── [Short Title] Chapters
└── [Short Title] CRX
```
## What goes where

- **`[Short Title] Assets` — audio assets ONLY.** Music beds, sound
  reference, voice-match files, anything that plays. No documents.
- **Book folder root** — every non-audio file: the script PDF, the
  billboards PDF, script-analysis spreadsheets, pronunciation lists,
  character notes, author notes.
- **`[Short Title] Chapters`** — recorded chapter audio.
- **`[Short Title] CRX`** — corrections/pickups.

Do NOT create a `[Short Title] Project` folder. Nuendo creates its own
when the session is first saved.
```
## Implementation

Use `mcp__cowork__request_cowork_directory` to get access to the user's chosen location, then:

```bash
mkdir -p "[Location]/[Short Title]" "[Location]/[Short Title]/[Short Title] Assets" "[Location]/[Short Title]/[Short Title] Chapters" "[Location]/[Short Title]/[Short Title] CRX"
```

Replace `[Short Title]` with the user-provided title and `[Location]` with the mounted path.
