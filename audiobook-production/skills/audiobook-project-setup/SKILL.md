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

## Implementation

Use `mcp__cowork__request_cowork_directory` to get access to the user's chosen location, then:

```bash
mkdir -p "[Location]/[Short Title]" "[Location]/[Short Title]/[Short Title] Assets" "[Location]/[Short Title]/[Short Title] Chapters" "[Location]/[Short Title]/[Short Title] CRX"
```

Replace `[Short Title]` with the user-provided title and `[Location]` with the mounted path.
