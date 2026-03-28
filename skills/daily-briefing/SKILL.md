---
name: daily-briefing
description: Generate a comprehensive morning briefing combining calendar, email, production status, tasks, and personal check-ins. Triggers include "good morning", "morning briefing", "daily briefing", "start my day", "what's on today", or any morning greeting. Features Cora-style intelligent email triage (contextual understanding, action extraction, smart prioritization). This is a three-phase interactive process that asks about writing, crochet, and tasks before generating the briefing, presents it for review, then saves to Notion upon user approval. Integrates with Decision Framework skill to track narrative vs reality patterns and suggest deeper analysis when appropriate. Uses the 3-3-3 method for task organization.
---

# Daily Briefing

## Overview

Generate a personalized morning briefing that combines calendar events, email triage, production status, extracted tasks, and personal accountability check-ins. The briefing is presented in chat first for review and adjustments, then saved to Notion's Littlebird Log upon user approval.

**Core principle**: Balance recording work with writing, creative projects, and personal life. The briefing actively nudges toward maintaining this balance rather than defaulting to production-only days.

## Three-Phase Workflow

### Phase 1: Data Gathering + Interactive Check-ins

1. **Pull calendar data** (today + tomorrow)
2. **Triage emails** (VIPs from last 48 hours, promos, newsletter digest, awaiting reply)
3. **Check Notion** (Littlebird Database, previous Littlebird Log entries from past week, **including comments on those entries**)
4. **Check production status** (active audiobook project)
5. **ASK USER**: Writing plans for today?
6. **ASK USER**: Crochet project updates?
7. **ASK USER**: Any outstanding tasks or to-dos on your mind?
8. **Check**: When was last Joanne submission? (weekly accountability)

### Phase 2: Present & Review

1. Compile full briefing with all sections
2. **Present briefing in chat** for user review
3. Ask if any adjustments or additions needed
4. Make requested changes

### Phase 3: Publish to Notion

1. User gives explicit OK to publish
2. Create new entry in Notion "Littlebird Log"
3. Include task tracking (references for later updates)
4. Add motivational nudges based on calendar balance
5. Confirm save with link to Notion entry

---

## Data Sources

### Calendars (Google Calendar)

Pull from four calendars:
- `primary` — Main calendar (client calls, meetings, personal)
- `Studio Schedule` — Work schedule, 10,000-foot view of workload and studio time
- `Colin` — Shared calendar from husband's Google account
- `Events` — Cultural events (museum free days, festivals, craft fairs, etc.)

**Time range**: Today + Tomorrow only

```
Use: list_gcal_events or list_calendars first to get calendar IDs
Parameters:
  - calendar_id: "primary", then find IDs for "Studio Schedule", "Colin", "Events"
  - time_min: Start of today (RFC3339)
  - time_max: End of tomorrow (RFC3339)
```

**Output format**:
```
📅 TODAY — [Day, Date]

• [Time] - [Event name] ([Calendar source if not primary])
• [Time] - [Event name]
...

🎭 CULTURAL EVENTS (from Events calendar)
• [Event] — [Date/details]

🔮 TOMORROW

• [Time] - [Event name]
...
```

### Email Triage (Gmail) — Cora-Style Intelligence

The goal is NOT to list emails, but to **understand what they mean for Pavi** and extract actionable intelligence. Think like a smart executive assistant who knows the context of your work and relationships.

#### Philosophy (Inspired by Cora from every.to)

- **Context-aware**: Know that Seth Ring is an author you work with, Blackstone is a publisher, Joanne is your mentor
- **Action-focused**: Extract the actual "what do I need to do" not just "you have an email"
- **Smart prioritization**: Truly urgent vs. just unread
- **Noise filtering**: Separate signal from noise without you having to scan everything
- **Relationship memory**: Reference previous interactions when relevant

**Future capability** (not yet active): Auto-archiving noise. Currently Cora handles this, but the skill should be ready to add this feature.

#### ⏰ Email Scope — IMPORTANT

**All email searches are time-bounded to keep briefings relevant and fast:**

| Email Category | Time Window | Rationale |
|----------------|-------------|-----------|
| VIP emails | Last 48 hours (`newer_than:2d`) | Anything older is probably handled or can wait |
| Promotional | Last 24 hours (`newer_than:1d`) | Promos expire quickly; stale sales aren't useful |
| Newsletters | Last 24 hours (`newer_than:1d`) | Yesterday's news is old news |
| Awaiting Reply | Last 7 days (`newer_than:7d`) | Follow-up window; older threads are cold |

This means older unread emails won't appear in briefings. If something important slipped through, Pavi can always search manually.

#### VIP Emails (Requires Your Attention)

Search for unread emails **from the last 48 hours** from priority senders and **summarize what they actually need**:

**VIP Categories**:
- Publishers: Blackstone, Portal Books, Tantor, Podium, Dreamscape
- Authors: Seth Ring, and any names from active audiobook projects
- Story Grid: Joanne Mitchell, Story Grid official
- Government/Tax: IRS, Illinois Department of Revenue, tax-related
- Mortgage: Loan servicer, mortgage company
- Personal important: Colin, family members

```
Use: search_gmail_messages + read_gmail_thread for context
Query examples:
  - "is:unread newer_than:2d from:blackstone OR from:portal OR from:tantor"
  - "is:unread newer_than:2d (from:irs.gov OR subject:tax OR from:illinois.gov)"
  - "is:unread newer_than:2d (subject:mortgage OR from:loan)"
  - "is:unread newer_than:2d from:seth" (for active author)
  - "is:unread newer_than:2d from:joanne OR from:storygrid"
```

**For each VIP email, provide**:
1. Who it's from (with context: "Seth Ring, your DotF author")
2. What they actually need (not just subject line)
3. Urgency level (🔴 urgent / 🟡 this week / 🟢 when convenient)
4. Suggested action or response approach

**Output format**:
```
📧 EMAIL INTELLIGENCE (last 48 hours)

🔴 NEEDS ACTION TODAY

**Blackstone** — Contract for DotF 17
They're waiting on your signature for the next book. Contract attached.
→ Action: Review terms, sign, return (15 min)

**Seth Ring** — Character voice question  
Asking how you're planning to voice the new antagonist in book 17.
→ Action: Quick reply with your approach (5 min)

🟡 THIS WEEK

**Portal Books** — Pickup notes for Exlian 4
12 pickups flagged from QC. Non-urgent, batch when ready.
→ Action: Schedule 30-min pickup session

🟢 FYI (No action needed)

**Joanne Mitchell** — Story Grid newsletter
Monthly craft essay on midpoint shifts. Worth reading when you have downtime.

📭 No VIP emails from last 48 hours — inbox is clear!
```

#### Promotional Emails (Quick Scan)

Scan promotional emails for a bare-bones summary. The goal is quick assessment — just enough to know if anything's worth opening.

```
Use: search_gmail_messages
Query: "category:promotions newer_than:1d"
```

**Processing**:
- One line per promo, max 5-6 words
- Format: **Sender** — [what it is]
- Flag anything potentially relevant with ⭐
- Group by rough category if helpful

**Output format**:
```
🏷️ PROMOS ([count] items from last 24h)

⭐ Hobbii — 40% off winter yarns
⭐ Anthropic — Claude feature update
Amazon — Echo device sale
B&H Photo — Studio gear clearance
Audible — 2-for-1 credit sale
Software Co — Renewal reminder
[X more skippable promos]
```

#### Newsletter & Info Digest

Scan newsletters and updates, creating a **scannable keyword digest** so you can spot anything worth investigating without reading everything.

```
Use: search_gmail_messages
Query: "category:updates newer_than:1d"
```

**Processing**:
- Group by topic area
- Extract 2-3 keywords that capture the content
- Flag anything that seems personally relevant based on your interests
- Note pure noise that can be ignored

**Output format**:
```
📰 NEWSLETTER DIGEST ([count] items from last 24h)

🎧 Audio/Narration
   Audiobook Creators Guild • rate survey • industry trends
   Findaway Voices • new royalty reporting feature ⭐ (relevant)

💰 Business/Finance  
   Bench • Q4 tax prep reminder
   Wave • invoice template updates

🛠️ Tech/Tools
   Anthropic • Claude update announcement ⭐ (relevant)
   Notion • new calendar view feature

🎨 Creative/Craft
   Ravelry digest • trending patterns

📦 Skip-worthy: [X] items
   Generic sales, software upsells, webinar invites
```

#### Awaiting Reply (Smart Filtering)

Search sent emails from past 7 days and **intelligently determine** which actually need responses.

```
Use: search_gmail_messages
Query: "in:sent newer_than:7d"
Then: read_gmail_thread for each to understand context
```

**INCLUDE** (likely needs response):
- Questions asked ("What do you think?", "Can you confirm?", "Let me know")
- Proposals or pitches awaiting feedback
- Invoices sent (check if payment received)
- Requests made that require action from recipient
- Follow-ups on previous unanswered threads

**EXCLUDE** (doesn't need response):
- Thank you emails
- Confirmations ("Got it", "Sounds good", "See you then")
- FYI/notifications ("Just letting you know...")
- Completed transactions
- Auto-replies you sent

**Output format**:
```
💤 AWAITING REPLY (last 7 days)

**Blackstone Accounting** — Invoice #2024-089 (sent 5 days ago)
$X,XXX for DotF 16. No payment confirmation yet.
→ If no response by Friday, follow up

**Author inquiry** — New project interest (sent 3 days ago)
You asked about their timeline and budget. Ball's in their court.
→ Wait until day 5, then gentle nudge

✅ Cleared: [X] sent emails don't need responses (confirmations, thank-yous)
```

#### Future: Auto-Archive Capability

**NOT YET ACTIVE** — Cora currently handles archiving.

When enabled, this section would:
- Identify emails that match "noise" patterns
- Archive them automatically after extracting any relevant info for digest
- Categories for auto-archive: marketing, sales pitches, subscription confirmations, automated notifications
- NEVER auto-archive: VIP senders, anything with actionable content, personal emails

---

## Notion Integration

### Database: Littlebird Database

Search for "Littlebird" in Notion to find the main notes database.

**Purpose**: Check for any notes with tasks or follow-ups that should appear in today's briefing.

```
Use: Notion search for "Littlebird"
Look for: Uncompleted tasks, recent notes with action items
```

### Previous Briefings: Littlebird Log

Check the past week's briefing entries for:
- Carried-forward tasks not yet completed
- **Comments on previous entries** (often contain task updates or additions)
- Patterns in writing/crochet check-ins
- Recurring themes or blockers

```
Use: Notion search for "Littlebird Log"
Then: Fetch recent entries from past 7 days
Also: Check comments/discussions on those entries
```

**Task carryforward rules**:
- If task marked `[x]`, ✅, strikethrough, or "(DONE)" → Skip it
- If task still `[ ]` and not explicitly cancelled → Include in today's briefing
- Note original source: "(carried from [date])"
- **If task from comment**: Note "(from Littlebird comment on [date])"

---

## Production Status

### Active Audiobook Project

Check Notion for the current active audiobook project:

```
Use: Notion search for active project or "Audiobook Production" database
Look for: Current project, chapter progress, deadline
```

**Information to extract**:
- Book title and author
- Current chapter / Total chapters
- Deadline date
- On-track status (using Work Date field if available)
- Any notes or blockers

**On-track calculation**:
- If Work Date field exists: Compare scheduled progress to actual
- Count chapters with Work Dates ≤ today as "should be done"
- Compare to chapters actually marked complete
- Calculate buffer: chapters ahead (+) or behind (-)

**Output format**:
```
🎙️ PRODUCTION

**[Book Title]** by [Author]
Progress: [X]/[Y] chapters ([Z]%)
Deadline: [Date] ([N] days)
Status: [On track ✅ / Behind ⚠️ / Ahead 🚀] — [+/-N chapters buffer]

[Any relevant notes: pickups needed, problem chapters, etc.]
```

---

## Task Organization: The 3-3-3 Method

Structure all tasks using the 3-3-3 framework for realistic daily planning:

### 🎯 THE 3: Deep Focus (~3 hours total)

**One primary project** that gets the bulk of your creative energy.

Criteria for Deep Focus:
- Requires concentration and creative energy
- Usually production work (narration) OR writing
- Single project, not a list
- Should feel like "the main thing" for the day

Examples:
- "Record chapters 12-14 of Exlian Syndrome 5"
- "Draft short story scene for Joanne submission"
- "Complete act analysis for Story Grid homework"

### ⚡ THE 3: Quick Wins + Scheduled (5-30 min each)

**Three items max** that are either:
- Quick tasks that can be knocked out
- Scheduled events/calls (mark with time)

Rules:
- No more than 3 items
- Each should be completable in under 30 minutes
- Include scheduled meetings/calls with times
- Put extra tasks in "Overflow" section

Examples:
- Reply to Seth's email (5 min)
- Review contract from Blackstone (15 min)
- Client call at 2pm (scheduled)

### 💛 THE 3: Habits + Joy

**Three daily practices** that maintain balance:

1. **Crochet** — Always included; note current project
2. **Writing** — Always included; can be practice, analysis, or drafting
3. **Flexible third slot** — Rotate based on needs:
   - Exercise / walk with pups
   - Quality time with Colin
   - Vocal practice
   - Reading/learning
   - Improv practice

### Overflow Section

Tasks that didn't fit in today's 3-3-3 but shouldn't be forgotten:
- Include date if time-sensitive
- Review in next briefing for possible inclusion
- Helps prevent overloading the day

---

## Writing Placement Logic

Writing can appear in different sections based on context:

**As Deep Focus** (🎯 THE 3):
- When there's a Joanne deadline approaching
- When user explicitly prioritizes writing that day
- When no active narration deadline is pressing

**As Quick Win** (⚡ THE 3):
- When it's a small task: "Review yesterday's draft" or "15 min freewrite"
- When paired with a heavy production day

**As Habit** (💛 THE 3):
- Default placement for daily writing practice
- When focus is on consistency over output
- "Even 15 minutes counts"

---

## Balance Check & Nudges

At the end of each briefing, assess the day's balance and provide gentle nudges when needed.

**Balance factors**:
- Studio time vs. creative time
- Work vs. personal/relationship
- Productivity vs. rest
- Consistency in writing/crochet practice

**Pattern tracking** (light touch):
- Note if writing hasn't been mentioned for 3+ days
- Note if crochet project seems stalled
- Note if calendar is unusually heavy or light
- Cross-reference with Decision Framework skill if available

**Nudge examples**:
- "📊 *Heavy studio day ahead. Consider protecting 30 min for writing or a walk with the pups.*"
- "💛 *Colin's calendar shows he's free this evening. Quality time opportunity?*"
- "⚠️ *Third day without writing mentioned. Even 15 minutes of Story Grid analysis counts!*"
- "🎭 *Reminder: [Event] is happening tomorrow — still planning to go?*"

**Pattern notes** (only when relevant):
- Surface after 3+ occurrences of same pattern
- Frame as observation, not judgment
- Always offer an out or alternative perspective
- Maximum ONE pattern note per briefing

---

## Output: Littlebird Log Entry

### Creating the Notion Entry

**Only after user explicitly approves the briefing**, create a new page in the **Littlebird Log** database:

```
Use: Notion search to find "Littlebird Log" database
Then: Notion create page in that database
Title: "Daily Briefing — [Date]"
```

**Note**: Littlebird Log is an existing Notion database that Pavi uses for notes, todos, and daily briefings. Search for it by name; do not create a new database.

### Entry Structure

The Notion entry should contain the COMPLETE briefing in this order:

```markdown
# Daily Briefing — [Full Date]

## 📝 Notes Throughout the Day

*Use this space to jot down thoughts, updates, and quick captures as the day progresses.*



---

## 📅 Calendar

### Today
[Events]

### Tomorrow  
[Events]

---

## 🎙️ Production

[Active project status]

---

## 📧 Email (last 48h)

### Action Required
[VIP emails]

### Promos
[Bare-bones promo list]

### Newsletter Digest
[Grouped newsletters]

### Awaiting Reply
[Pending responses]

---

## ✅ Today's 3-3-3

### 🎯 THE 3 (Deep Focus — ~3 hours)
**[Primary project]**
[Brief context: deadline, progress, or motivation]

---

### ⚡ THE 3 (Quick Wins + Scheduled — 5-30 min each)

1. [ ] [Task] — [brief context if helpful]
2. [ ] [Task] — [brief context if helpful]  
3. [ ] [Scheduled event] — [time] (scheduled)

**Overflow** *(for future briefings)*:
- [Task] — [date if time-sensitive]
- [Task]

---

### 💛 THE 3 (Habits + Joy)

1. [ ] 🧶 **Crochet** — [current project/progress]
2. [ ] ✍️ **Writing** — [today's approach]
3. [ ] [Third activity] — [brief note]

---

## 📚 Writing Check-in

Yesterday: [User's reflection]
Today's plan: [User's stated plan]

📚 Weekly submission: [Status]

---

## 🧶 Crochet

Yesterday: [User's reflection]
Today/Upcoming: [User's update]

Monthly project: [Status]
Outfit goal: [Progress]
Gift queue: [Upcoming occasions]

---

## 🎯 Balance Check

[Balance analysis + pattern notes if applicable]

---

*Generated: [Timestamp]*
```

### Task Tracking

For each task in the briefing:
- Note the source (email, previous briefing, Littlebird, Littlebird comment, check-in)
- When user reports completion, update the source:
  - If from email: No update needed (email is the source of truth)
  - If from previous briefing: Update that briefing entry
  - If from Littlebird: Update the Littlebird note
  - If from Littlebird comment: Note completion in current briefing
  - If from check-in: Already captured in this briefing

**Completion format**:
When user says "I finished [task]":
1. Acknowledge completion
2. Update relevant Notion entry if applicable
3. Note: "✅ Marked complete in [source]"

---

## Conversation Flow

### Opening (Claude initiates)

```
Good morning, Pavi! ☀️ Let me pull together your daily briefing.

[Gather calendar, email, Notion data silently — INCLUDING comments on recent Littlebird Log entries]

Before I compile everything, three quick check-ins:

✍️ **Writing**:
   • Yesterday — What did you accomplish writing-wise?
   • Today — What's your plan?

🧶 **Crochet**:
   • Yesterday — Did you get any hook time in?
   • Today — Any plans or project updates?

📝 **Tasks**:
   • Any outstanding to-dos floating in your head that need capturing?
```

### After User Responds

```
Perfect! Here's your briefing for review:

---

[Full briefing output with 3-3-3 structure]

---

Take a look and let me know if you'd like any adjustments or additions. When you're happy with it, just say "publish" or "save to Notion" and I'll create the entry in your Littlebird Log.
```

### User Requests Adjustments

```
[Make requested changes]

Here's the updated briefing:

---

[Updated briefing]

---

Anything else, or ready to publish?
```

### User Approves

```
[Create Notion entry]

Done! ✅ Saved to your Littlebird Log: [Link to Notion page]

Have a great day — you've got this! 💪
```

### Task Completion (During Day)

User: "I finished the Blackstone contract"

```
Got it! ✅ Marked the Blackstone contract as complete. 

[If from tracked source, update it]

Anything else from today's list you've tackled?
```

---

## Trigger Phrases

Activate this skill when user says:
- "Good morning" / "Morning!"
- "Daily briefing" / "Morning briefing"
- "Start my day" / "What's on today?"
- "Brief me" / "What do I have today?"
- Any morning greeting that implies wanting an overview

---

## Key Reminders

1. **Always ask about writing, crochet, AND tasks** — All three check-ins are required
2. **Present briefing in chat first** — User must explicitly OK before publishing to Notion
3. **Check previous Littlebird Log entries AND their comments** — Both content and comments for context and carried-forward tasks
4. **Use 3-3-3 structure for tasks** — Deep Focus, Quick Wins, Habits + Joy
5. **Tasks use checkbox format** — `• [ ] Task` so Pavi can mark `[x]` directly in Notion
6. **Skip completed tasks** — Look for `[x]`, ✅, strikethrough, or "(DONE)" markers
7. **Nudge toward balance** — Pavi tends to over-prioritize recording
8. **Save to Notion only after approval** — Never auto-publish
9. **Notes section is at THE TOP** — First section after the title, with divider, ready for day's captures
10. **Email triage is Cora-style** — Contextual intelligence, not just listing. Extract what they NEED, not just subject lines
11. **Email is time-bounded** — VIPs: 48h, Promos/Newsletters: 24h, Awaiting Reply: 7d
12. **Promos are bare-bones** — One line each, just enough to assess if worth opening
13. **Newsletter digest should be scannable** — Keywords + relevance flags (⭐) for things matching Pavi's interests
14. **Awaiting reply filter is smart** — Read the thread to determine if response is actually needed
15. **VIPs are specific** — Publishers, authors, Joanne, government/tax, mortgage, Colin/family
16. **On-track calculation uses Work Date field** — Not estimation, actual scheduling
17. **Four calendars** — Primary, Studio Schedule, Colin, Events (don't miss cultural events!)
18. **Pattern awareness is light-touch** — Only surface after 3+ occurrences, never guilt, always offer an out
19. **Decision framework suggestions are gentle** — Detect triggers, suggest once, don't force
20. **Maximum one pattern note per briefing** — Don't pile on; keep mornings supportive
21. **Writing placement is dynamic** — Can be Deep Focus, Quick Win, or Habit depending on context
22. **Overflow exists for non-urgent tasks** — Don't overload the 3-3-3; be realistic about what fits in a day
23. **Third Habit slot is flexible** — Rotate suggestions or ask user preference based on recent patterns
24. **Comment-sourced tasks get labeled** — Note "(from Littlebird comment)" when task originated from a comment
