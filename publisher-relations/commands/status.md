---
description: Show all active projects for a specific publisher or across all publishers. Pulls from Notion Audiobook Projects database.
---

# Publisher Status

Overview of active projects, grouped by publisher.

## Usage

- "Publisher status" — all publishers, all active projects
- "Aethon status" — just Aethon projects
- "What do I have active with Podium?"

## Execution

1. Search Notion Audiobook Projects database
2. Filter by Status = "Standby" OR "In Production" OR "Final QC"
3. Group by publisher
4. For each project, show:
   - Book title (short name)
   - Status
   - Deadline
   - Chapter progress (X/Total complete)
   - Days until deadline
   - Estimated remaining hours

## Output

```
📊 PUBLISHER STATUS

🏢 AETHON (Julie Holloway)
  📚 DotF 17 — In Production — 12/47 chapters (26%) — Deadline: Apr 15 (18 days)
  📚 DotF 18 — Standby — Not started — Deadline: TBD

🏢 PODIUM
  📚 [Title] — Final QC — 100% — Awaiting publisher review

🏢 RECORDED BOOKS
  [No active projects]

Total active: [N] projects across [N] publishers
```

## Rules
- Flag any project where deadline math is tight
- Note which publishers have overdue payments (if invoice tracking is available)
- If no active projects for a publisher, still list them to maintain awareness
