---
name: batch-draft-writer
description: Write multiple email drafts in one session using Slashy. Pavi reviews and approves each body before it's saved; nothing sends without separate explicit approval. Triggers on "batch drafts", "draft multiple emails", "write drafts for", "batch email writing", "help me draft a few emails".
---

# Batch Draft Writer

Write multiple email drafts in sequence. One at a time: write → Pavi approves → save to Slashy. Nothing sends until Pavi explicitly says "send it" on a specific draft.

Tool mechanics: `pavitas-core:using-slashy`. Voice and prose: `pavitas-core:output-quality`. IDs: `pavitas-core:workspace-context`.

## No AI-writer delegation

Slashy's `draft_email` takes a **literal HTML `body`** — there is no `instructions` field to hand drafting to an AI writer. Claude writes every body directly, following `pavitas-core:output-quality` for voice fidelity.

## Step 1 — Establish the draft list

Ask or infer: which threads or recipients need drafts? For each, collect:
- **Replies:** thread ID — locate with `list_messages(inbox_email="pavi@paviproczko.com", q="...")` if not provided
- **New threads:** recipient email, subject, intent

For any reply: `read_thread(inbox_email="pavi@paviproczko.com", thread_id=...)` to get full context before drafting.

## Step 2 — Draft loop

Repeat for each draft:

1. **Write the body** — compose in HTML per `pavitas-core:output-quality`. Present in chat first.
2. **Pavi reviews** — iterate until approved.
3. **Save the draft** — `draft_email(inbox_email="pavi@paviproczko.com", to=[...], subject="...", body="<html>...", thread_id="..."[if reply])`.
4. Report back with the Slashy draft link if returned.
5. Advance to the next draft.

## Step 3 — Summary

After all drafts are saved:

```
✉️ DRAFTS SAVED — [Date]

1. [Subject] → [Recipient] · [link]
2. [Subject] → [Recipient] · [link]
...

Drafts are ready to review and send. Send requires explicit approval per email — no undo window on immediate sends.
```

## Sending (separate explicit flow)

When Pavi says "send it" for a specific draft:
`send_email(inbox_email="pavi@paviproczko.com", draft_id="...")`

No undo after confirmation. Confirm the draft_id before calling.
