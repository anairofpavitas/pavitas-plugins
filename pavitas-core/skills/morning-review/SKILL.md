---
name: morning-review
description: Morning briefing orchestrator. Triggers on "good morning", "morning briefing", "daily briefing", "start my day", "what's on today", "brief me", or any morning greeting implying an overview. Three phases — gather + check-ins, present for review, publish to Notion on explicit approval. Email intelligence comes from Cora's brief, never direct inbox triage. Replaces the former daily-briefing skill.
---

# Morning Review

Replaces daily-briefing. Cora owns email triage; this skill consumes her brief.
IDs and tool routing: `pavitas-core:workspace-context`. Conduct rules: `pavitas-core:safety-rails`.

## Phase 1 — Gather + check in

Run data pulls in parallel, silently:

1. **Calendar** — today + tomorrow across all four: `primary`, `Studio Schedule`, `Colin`, `Events`. Don't miss Events (cultural calendar).
2. **Cora brief** — fetch the latest brief (Cora MCP: list, then show). Extract: action-required items with who/what/urgency, anything awaiting Pavi's reply. Do NOT run any direct inbox searches. If no brief exists from the last 24h, say so and offer to skip email rather than triaging manually.
3. **Littlebird Log** — entries from the past 7 days INCLUDING comments. Carryforward rules: `[x]`/✅/strikethrough/(DONE) → skip; open `[ ]` not cancelled → carry with "(carried from [date])"; comment-sourced tasks labeled "(from Littlebird comment on [date])".
4. **Production** — active project in Audiobook Projects DB: title, chapter progress, deadline, on-track buffer (chapters with Work Date ≤ today vs. actually complete).
5. **Joanne check** — when was the last weekly Story Grid submission?

Then ask, in one message: ✍️ Writing — yesterday and today's plan? 🧶 Crochet — any hook time or project updates? 📝 Tasks — anything floating in your head?

## Phase 2 — Present

Compile and show in chat. Structure tasks with **3-3-3**:

- 🎯 **Deep Focus (~3h)** — ONE primary project. Usually narration or writing. Writing takes this slot when a Joanne deadline approaches, Pavi prioritizes it, or no narration deadline presses.
- ⚡ **Quick Wins + Scheduled** — max three items, ≤30 min each; scheduled events carry times. Extras → Overflow with dates if time-sensitive.
- 💛 **Habits + Joy** — 1) Crochet (always, with project), 2) Writing (always, even 15 min), 3) flexible: pups walk, Colin time, vocal practice, improv, reading.

End with a balance check: studio vs. creative, work vs. Colin/personal. Nudges are light — max ONE pattern note per briefing, only after 3+ occurrences, always with an out. Pavi over-prioritizes recording; nudge the other direction. New tasks surfaced here → create in Tasks DB immediately (Status=Inbox).

Ask for adjustments. Iterate until approved.

## Phase 3 — Publish (only on explicit OK)

Create a Littlebird Log entry (IDs in `pavitas-core:workspace-context`), title "Daily Briefing — [Date]", in this order: **📝 Notes Throughout the Day at the very top** (empty, with divider) → Calendar (today/tomorrow) → Production → Email (from Cora brief) → 3-3-3 with checkbox tasks (`- [ ]`) → Writing check-in (incl. weekly submission status) → Crochet → Balance Check → timestamp footer. Confirm with the page link.

**During the day:** "I finished X" → acknowledge, update the task's source entry, confirm "✅ Marked complete in [source]".

## Hard rules

- All three check-ins, every time.
- Never publish without explicit approval.
- Zero direct email triage — Cora brief or nothing.
- Decision Framework escalation: if check-ins surface a should-vs-want conflict or recurring avoidance, suggest `pavitas-core:decision-framework` once; don't push.
