---
description: Track current crochet project status. Query active projects from Notion, update progress, support stitch/technique decisions.
---

# Project Tracker

Quick status check and update for active crochet projects.

## Usage

- "Crochet project status" → show all active projects
- "Update [project] status" → update a specific project
- "What's the status on my cardigan?" → query a specific project

## Source of truth

Active project state lives in the **Notion Littlebird Log** (entries tagged "Crochet Project") — never in this file. To show status:

1. Query the Littlebird Log for recent "Crochet Project" entries
2. Group by project name, surface the most recent update per project
3. Present compactly:

```
🧶 ACTIVE CROCHET PROJECTS

1. [Project name]
   Technique: [stitch / construction detail from latest entry]
   Status: [latest status]
   Last update: [date]

2. ...
```

If no entries are found, say so — don't reconstruct project state from memory.

## Stitch Research Support

When Pavi is researching technique options (e.g., stretchy waistband stitches), help by:
- Describing stitch properties (stretch, drape, density)
- Comparing options side by side
- Suggesting swatches to test
- Noting gauge implications

Log any decision made back to the Littlebird Log via `/spins-yarns-content:log`.

## Rules
- Use proper crochet terminology
- Pavi is advanced — don't explain basics unless asked
- For Tunisian crochet, specify forward/return pass details
- Store technique notes for future reference
