---
name: handoff
description: Manage session handoffs between claude.ai (Web) and Claude Code (CLI) using Notion Littlebird Log. Triggers include "read handoff", "check handoff", "what's the handoff", "create handoff", "save handoff", "write handoff", "update handoff", "add to handoff", or natural variations like "create a handoff for this session", "check what we left off on", "update the handoff with our progress". Autonomously analyzes conversation to compose handoff notes—no manual input required. Critical for maintaining continuity across Pavi's audiobook narration, writing, and creative projects when switching between Claude interfaces.
---

# Session Handoff

## Overview

Maintain seamless continuity between claude.ai (Web) and Claude Code (CLI) sessions by creating, reading, and updating structured handoff notes in Notion's Littlebird Log database.

**Core principle**: Handoffs should capture enough context that the "other Claude" can pick up exactly where you left off—like a really good shift change at a hospital. No hunting, no re-explaining.

---

## Commands

### Read Handoff
**Triggers**: "read handoff", "check handoff", "what's the handoff", "check what we left off on", "where did we leave off", "any handoff notes"

**Action**:
1. Search Littlebird Log for most recent "Session Handoff" tagged entry
2. Present the handoff content clearly
3. Offer to continue from where it left off

```
Use: Notion:notion-search
Query: "Session Handoff" in Littlebird Log
Then: Notion:notion-fetch to get full content
```

**Output format**:
```
📋 **Latest Handoff Found**

**[Title]**
Created: [Date/Time] | Last edited: [Date/Time]

---

[Full handoff content]

---

Ready to pick up where you left off? What would you like to tackle first?
```

### Create Handoff
**Triggers**: "create handoff", "save handoff", "write handoff", "make a handoff", "create a handoff for this session", "save our progress"

**Action**:
1. Analyze current conversation to extract:
   - Primary project/topic being worked on
   - What was accomplished this session
   - What's in progress or next
   - Critical context the other environment needs
2. Compose structured handoff note autonomously
3. Present to user for review
4. On approval, save to Littlebird Log with "Session Handoff" tag

**Analysis approach**:
- Scan conversation for project names (Exlian Syndrome, Defiance of the Fall, Story Grid work, The Bookstore, etc.)
- Identify completed actions (created files, made decisions, finished tasks)
- Find open loops (things started but not finished, next steps mentioned)
- Extract technical context (file paths, database IDs, API details, code state)
- Note any blockers or dependencies

**Output format** (for review):
```
📝 **Handoff Draft**

Here's what I've captured from our session:

---

**🔄 [Project Name] - [Today's Date] - Web**

## Environment
claude.ai (Web) → Claude Code (CLI)

## Session Focus
[1-2 sentence summary of what we were working on]

## What We Accomplished
- [Completed item 1]
- [Completed item 2]
- [Completed item 3]

## In Progress / Next Actions
- [ ] [Open task 1]
- [ ] [Open task 2]
- [ ] [Blocked/waiting item if any]

## Context Notes
[Technical details, file locations, decisions made, anything the CLI session needs to know]

---

Does this look right? I can adjust anything before saving. Say **"save it"** or **"publish"** when ready.
```

### Update Handoff
**Triggers**: "update handoff", "add to handoff", "update the handoff with our progress", "append to handoff"

**Action**:
1. Search for most recent "Session Handoff" entry
2. Analyze conversation since last handoff (or since session start)
3. Identify new accomplishments and updated next actions
4. Present updated handoff for review
5. On approval, update the existing Notion entry

**Update approach**:
- Move completed items from "In Progress" to "What We Accomplished"
- Add new in-progress items
- Update context notes with new information
- Preserve original session focus unless topic shifted significantly

**Output format** (for review):
```
📝 **Handoff Update Draft**

Found the existing handoff: **[Title]**

Here's the updated version:

---

[Full updated handoff content]

---

Changes made:
- ✅ Moved [X] to accomplished
- ➕ Added [Y] to in progress
- 📝 Updated context notes with [Z]

Ready to save the update? Say **"save it"** when ready.
```

---

## Notion Integration

### Database Details
- **Database Name**: Littlebird Log
- **Database ID**: `28d089eb3ccc80da90fbd861352103a8`
- **Data Source ID**: `28d089eb-3ccc-80ca-87a0-000bf7143e2a`

### Entry Structure
- **Title**: `🔄 [Project Name] - [Date] - Web` (or `CLI` for CLI-created handoffs)
- **Tags**: "Session Handoff" (select field)
- **AI**: One-sentence session summary (text field)
- **Content**: Full handoff note in markdown

### Search Pattern
```
Use: Notion:notion-search
Query: "Session Handoff" 
Data source URL: collection://28d089eb-3ccc-80ca-87a0-000bf7143e2a
```

### Create Pattern
```
Use: Notion:notion-create-pages
Parent: data_source_id: "28d089eb-3ccc-80ca-87a0-000bf7143e2a"
Properties:
  - Title: "🔄 [Project] - [Date] - Web"
  - Tags: "Session Handoff"
  - AI: "[One-sentence summary]"
Content: [Full handoff markdown]
```

### Update Pattern
```
Use: Notion:notion-update-page
Page ID: [from search result]
Command: replace_content or update_properties
```

---

## Autonomous Composition Logic

### Project Detection
Scan conversation for these project indicators:

**Audiobook Projects**:
- "Exlian Syndrome" / "ES" + book number
- "Defiance of the Fall" / "DotF" + book number
- Seth Ring projects
- Blackstone, Portal Books, Tantor mentions
- Recording, narration, pickup, chapter references

**Writing Projects**:
- "The Bookstore" / Taras story
- Jim and Percy story
- Story Grid work, scene analysis
- Joanne Mitchell mentions

**Technical/Workflow**:
- MCP servers, Claude Code, skills
- Notion integration, automation
- Script development

**Business**:
- Invoicing, contracts, scheduling
- Publisher communications

### Accomplishment Extraction
Look for patterns indicating completed work:
- "Done", "finished", "completed", "created", "built"
- File creation confirmations
- Decision conclusions ("we decided", "let's go with")
- Problem resolutions ("fixed", "solved", "that works")

### In-Progress Detection
Look for patterns indicating open work:
- "Next we should", "tomorrow", "later"
- "Still need to", "haven't yet"
- Questions left unanswered
- "TODO", "blocked by", "waiting on"
- Partial implementations mentioned

### Context Extraction
Capture technical specifics:
- File paths mentioned
- Database IDs, API keys (redacted if sensitive)
- Version numbers, dependencies
- Commands used
- Error messages encountered and their resolutions

---

## Topic Shift Detection

When creating handoffs, detect if the conversation shifted topics significantly:

**Single-topic session**: Create one handoff note covering everything

**Multi-topic session**: 
- If topics are related (both audiobook work), combine into one handoff
- If topics are distinct (audiobook + then unrelated Notion work), ask:
  ```
  I noticed we covered two distinct topics this session:
  1. [Topic A summary]
  2. [Topic B summary]
  
  Should I create:
  - **One handoff** covering both?
  - **Two separate handoffs** for each topic?
  ```

---

## CLI Integration

This skill complements the CLI handoff commands:
- CLI: `/handoff create`, `/handoff update`, `/handoff read`
- Web: "create handoff", "update handoff", "read handoff"

Both use the same Littlebird Log database and "Session Handoff" tag, ensuring seamless handoffs regardless of which environment creates or reads them.

**Environment indicator in title**:
- Web-created: `🔄 [Project] - [Date] - Web`
- CLI-created: `🔄 [Project] - [Date] - CLI`

This makes it easy to see the handoff chain and know which environment last worked on something.

---

## Example Flows

### Read Handoff Example
**User**: "Check the handoff"

**Claude**:
```
[Searches Notion for latest Session Handoff]

📋 **Latest Handoff Found**

**🔄 Exlian Syndrome 4 - Jan 8, 2025 - CLI**
Created: Jan 8, 2025 3:45 PM | Last edited: Jan 8, 2025 4:12 PM

---

## Environment
Claude Code (CLI) → claude.ai (Web)

## Session Focus
Debugging the audiobook script analyzer skill and testing chapter extraction.

## What We Accomplished
- Fixed regex pattern for chapter detection
- Added word count calculation per chapter
- Tested on ES4 manuscript successfully

## In Progress / Next Actions
- [ ] Add page count estimation
- [ ] Create Notion integration for chapter database
- [ ] Test with DotF manuscript format

## Context Notes
- Script location: `/mnt/skills/user/audiobook-script-analyzer/scripts/analyze.py`
- Current regex handles "Chapter X" and "CHAPTER X" formats
- ES4 has 47 chapters, ~185k words total

---

Looks like CLI was working on the script analyzer. Want to pick up on the Notion integration piece, or tackle something else?
```

### Create Handoff Example
**User**: "Create a handoff"

**Claude**:
```
[Analyzes conversation]

📝 **Handoff Draft**

Here's what I've captured from our session:

---

**🔄 Daily Briefing Skill - Jan 9, 2025 - Web**

## Environment
claude.ai (Web) → Claude Code (CLI)

## Session Focus
Building out the handoff management skill for cross-environment continuity.

## What We Accomplished
- Drafted complete SKILL.md for handoff management
- Defined three core commands (read, create, update)
- Established Notion integration patterns
- Created autonomous composition logic

## In Progress / Next Actions
- [ ] Test skill with actual Notion integration
- [ ] Verify search query finds Session Handoff tags correctly
- [ ] Add skill to /mnt/skills/user/ directory

## Context Notes
- Skill file ready at: /home/claude/handoff-skill/SKILL.md
- Database ID: 28d089eb3ccc80da90fbd861352103a8
- Uses "Session Handoff" tag in Littlebird Log
- Title format: 🔄 [Project] - [Date] - [Environment]

---

Does this capture our session well? Say **"save it"** when ready!
```

**User**: "Save it"

**Claude**:
```
[Creates Notion page]

✅ Saved to Littlebird Log!

**🔄 Daily Briefing Skill - Jan 9, 2025 - Web**
[Link to Notion page]

CLI can pick up from here whenever you switch over. Anything else before we wrap?
```

---

## Key Reminders

1. **Analyze autonomously** — Never ask user to manually list what was accomplished; extract it from the conversation
2. **Present for review first** — Always show the draft before saving to Notion
3. **Include technical context** — File paths, IDs, commands matter for continuity
4. **Detect project automatically** — Use conversation signals to identify which project this handoff is for
5. **Environment indicator in title** — Always mark whether Web or CLI created the handoff
6. **One-sentence AI summary** — Populate the AI field with a crisp summary for quick scanning
7. **Checkbox format for next actions** — Use `- [ ]` so items can be marked complete in Notion
8. **Preserve handoff chain** — When reading, note where the previous session left off
9. **Handle multi-topic sessions** — Ask user preference if topics are distinct
10. **Same database as CLI** — Both environments share Littlebird Log with "Session Handoff" tag
