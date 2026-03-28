---
description: Generate the full morning briefing. Spawns parallel agents to gather calendar, email, Notion tasks, and production status, then presents the 3-3-3 organized daily plan for review before publishing to Notion Littlebird Log.
---

# Daily Briefing

Three-phase interactive process: gather → present → publish.

## Phase 1: Parallel Data Gathering + Check-ins

Spawn these agents simultaneously:

### Agent: calendar-intel
- Pull today's events from ALL 4 Google Calendars
- Pull tomorrow's events (preview)
- Flag: birthdays, cultural events (museum free days), dog camp days (Tues/Fri)
- Flag: therapy appointments, recording blocks, client calls
- Note if dogs are at Camp Run-A-Pup today (Tuesdays and Fridays)

### Agent: email-triage
- Search Gmail for emails from last 48 hours (unread priority)
- Apply Cora-style triage:
  - 🔴 ACTION REQUIRED — needs response/decision, extract specific action and deadline
  - 🟢 FYI — important but no action needed
  - 💤 AWAITING REPLY — sent emails from past 7 days with no response
  - 🏷️ PROMOS — bare-bones one-line summaries, star any writing/narration/tech relevant
  - 📰 NEWSLETTERS — categorized digest (improv/creative, finance, tech/tools, deliveries)
- VIP senders: publishers (Aethon, Podium, Recorded Books, Blackstone, Portal Books, Audible), Joanne Mitchell, Seth Ring, Colin, Gray Talent Group, Michelle Bratland (CPA), Tim Grahl
- Extract action items with deadlines from every actionable email

### Agent: notion-tracker
- Check Littlebird Log entries from past 7 days, INCLUDING comments on those entries
- Check Tasks database for items with Status = "Inbox" or "Active"
- Identify carryforward tasks from previous briefings not yet completed
- Check when last Joanne submission was sent (weekly accountability)
- Check active audiobook project status (completion %, deadline proximity)

### Interactive Check-ins (after agents return)
Ask Pavi sequentially:
1. "Any writing plans for today?"
2. "Crochet project updates?"
3. "Any outstanding tasks or to-dos on your mind?"

## Phase 2: Compile and Present

Organize into 3-3-3 format:

```
📅 TODAY — [Day], [Date]

[Calendar events organized by calendar source]

🔮 TOMORROW — [Day], [Date]
[Tomorrow preview]

🎙️ ACTIVE PROJECT: [Book Title]
[Progress %, deadline, pace check]

📧 EMAIL INTELLIGENCE
[Cora-style triage sections]

📋 CARRYFORWARD FROM PREVIOUS DAYS
[Uncompleted items from past Littlebird Log entries]

✅ Today's 3-3-3

🎯 THE 3 (Deep Focus — ~3 hours)
[Primary deep work block]

⚡ THE 3 (Quick Wins + Scheduled)
1. [item]
2. [item]
3. [item]

💛 THE 3 (Habits + Joy)
1. [item]
2. [item]
3. [item]

🎯 Balance Check
[Assessment of work/creative/personal balance for the day]
```

Present in chat. Ask: "Any adjustments or additions before I publish?"

## Phase 3: Publish to Notion

On Pavi's explicit OK:
1. Create new entry in Littlebird Log database
2. Title format: `📋 Daily Briefing — [Date]`
3. Populate AI summary field with one-sentence overview
4. Include full briefing content
5. Tag appropriately

## Balance Logic

- If calendar is all-recording with no creative/personal time → nudge
- If Joanne submission is overdue (> 7 days) → mention gently
- If 3+ days without writing mentioned → note it
- Core principle: balance recording work with writing, creative projects, and personal life
