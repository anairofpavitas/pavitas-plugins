---
description: Mid-day email triage. Quick scan of inbox without the full briefing — just email intelligence using Cora-style processing.
---

# Email Triage

Lightweight mid-day inbox check. No calendar, no tasks, no Notion — just email.

## Execution

1. Search Gmail for unread emails from last 12 hours
2. Apply Cora-style triage (same categories as briefing):
   - 🔴 ACTION REQUIRED — with extracted action and deadline
   - 🟢 FYI — one-line summary
   - 🏷️ PROMOS — bare-bones, star relevant ones
   - 📰 NEWSLETTERS — one-line each, categorized
3. Check for replies to emails Pavi sent today
4. Present as a quick scannable list

## Output Format

```
📧 INBOX CHECK — [Time]

🔴 ACTION REQUIRED
[Items or "Nothing urgent"]

🟢 NEW FYI
[Items or "All quiet"]

🏷️ PROMOS ([N] new)
[One-line summaries]

📰 NEWSLETTERS ([N] new)
[One-line summaries]
```

Keep it tight. This is a 30-second scan, not a deep dive.
