---
description: Process an incoming publisher email. Auto-identifies the publisher, loads their profile, extracts action items, deadlines, and key decisions, and suggests next steps.
---

# Publisher Email Intake

When Pavi shares or forwards a publisher email, this command processes it.

## Execution

1. **Identify the publisher** from sender domain, name, or context
2. **Load publisher profile** from stored data (contact, payment terms, active projects)
3. **Cross-reference Notion** — check Audiobook Projects for any active projects with this publisher
4. **Extract from the email**:
   - Action items (things Pavi needs to do)
   - Deadlines (explicit or implied)
   - Key decisions (anything requiring a yes/no or choice)
   - Financial details (rate changes, payment mentions, contract terms)
   - New project offers (title, author, word count, timeline)
5. **Present structured summary**:

```
📧 PUBLISHER INTAKE — [Publisher Name]

From: [Contact Name] ([email])
Re: [Subject/Topic]
Project: [Book Title] (if applicable)

📋 ACTION ITEMS
1. [Action] — by [deadline if stated]
2. [Action]

🔑 DECISIONS NEEDED
- [Decision point]

💰 FINANCIAL
- [Any rate/payment/contract mentions]

📅 DATES
- [Any deadlines or scheduling mentions]

💡 SUGGESTED RESPONSE
[One-line recommendation on what to do]

Draft a reply? [Y/N]
```

6. If Pavi wants a reply, draft in **Biz Mode** (present full draft for review, never send directly)

## Rules
- Always check stored rates before discussing money — flag if publisher mentions a different rate
- New project offers: estimate FH from word count (÷ 9,300) and calculate projected invoice
- If email mentions a project Pavi hasn't heard of, flag it clearly
- Professional, warm, efficient tone for all drafted replies — sign as "Pavi"
