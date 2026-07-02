---
name: morning-review
description: Morning briefing orchestrator. Triggers on "good morning", "morning briefing", "daily briefing", "start my day", "what's on today", "brief me", or any morning greeting implying an overview. Three phases — gather + check-ins, present for review, publish to Notion on explicit approval. Email intelligence comes from Cora's brief, never direct inbox triage. Replaces the former daily-briefing skill.
---

# Morning Review

Replaces daily-briefing. Cora owns email triage; this skill consumes her brief.
IDs and tool routing: `pavitas-core:workspace-context`. Conduct rules: `pavitas-core:safety-rails`.

## Phase 1 — Gather + check in

Spawn the `morning-intel` sub-agent (Task tool, `subagent_type: morning-intel`) to pull calendar, Cora brief, Littlebird carryforward, production status, and the Joanne check in one call. It returns structured data — don't re-query any of its five sources yourself.

While that's running (or right after), ask Pavi, in one message: ✍️ Writing — yesterday and today's plan? 🧶 Crochet — any hook time or project updates? 📝 Tasks — anything floating in your head?

## Phase 2 — Present

Compile the agent's data plus the check-in answers and show in chat. Structure tasks with **3-3-3**:

- 🎯 **Deep Focus (~3h)** — ONE primary project. Usually narration or writing. Writing takes this slot when a Joanne deadline approaches, Pavi prioritizes it, or no narration deadline presses.
- ⚡ **Quick Wins + Scheduled** — max three items, ≤30 min each; scheduled events carry times. Extras → Overflow with dates if time-sensitive.
- 💛 **Habits + Joy** — 1) Crochet (always, with project), 2) Writing (always, even 15 min), 3) flexible: pups walk, Colin time, vocal practice, improv, reading.

End with a balance check: studio vs. creative, work vs. Colin/personal. Nudges are light — max ONE pattern note per briefing, only after 3+ occurrences, always with an out. Pavi over-prioritizes recording; nudge the other direction. New tasks surfaced here → create in Tasks DB immediately (Status=Inbox).

Ask for adjustments. Iterate until approved.

## Phase 3 — Publish (only on explicit OK)

Create a Littlebird Log entry (IDs in `pavitas-core:workspace-context`), title "Daily Briefing — [Date]", in this order: **📝 Notes Throughout the Day at the very top** (empty, with divider) → Calendar (today/tomorrow) → Production → Email (from Cora brief) → 3-3-3 with checkbox tasks (`- [ ]`) → Writing check-in (incl. weekly submission status) → Crochet → Balance Check → timestamp footer. Confirm with the page link.

Then run `pavitas-core:memory-capture`. Not optional — check-ins and the day's plan often surface a deadline, decision, or preference update that the published page doesn't capture as an atomic, recallable fact.

**During the day:** "I finished X" → acknowledge, update the task's source entry, confirm "✅ Marked complete in [source]".

## Hard rules

- All three check-ins, every time.
- Never publish without explicit approval.
- Zero direct email triage — Cora brief or nothing.
- Decision Framework escalation: if check-ins surface a should-vs-want conflict or recurring avoidance, suggest `pavitas-core:decision-framework` once; don't push.
