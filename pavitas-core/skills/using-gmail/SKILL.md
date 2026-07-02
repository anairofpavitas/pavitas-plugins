---
name: using-gmail
description: Shared Gmail reference for email tool mechanics — native Gmail first, Composio Gmail fallback, Cora last resort. Load alongside any skill that touches email. Prevents re-deriving tool syntax across skills. Pair with pavitas-core:output-quality for email body prose.
---

# Using Gmail

Single source of truth for email tool mechanics. Replaces `using-slashy` (retired 2026-07-02). Email skills reference this instead of restating parameters.

## Routing order — static, not trial-and-error

Each operation below has ONE default tool. Only escalate a tier if that tool errors, is disconnected, or has no capability for the operation — never call a lower tier "just in case," and never retry the same tier twice before escalating.

1. **Native Gmail** (Google Workspace connector) — default for search, read, draft, and labeling. No sending, no attachment download.
2. **Composio Gmail** (`gmail` toolkit, already connected) — default for sending and attachment download, since native Gmail has neither; fallback for everything else if native errors.
3. **Cora** — last resort only, if both native Gmail AND Composio are unavailable. Search / read / reply-draft only — no send, no attachment download, no new-thread compose.

Calendar is NOT part of this waterfall — always use native Google Calendar tools (see `pavitas-core:workspace-context`).

## Routing table

| Operation | Tier 1 — Native Gmail (default) | Tier 2 — Composio Gmail (fallback, Tier 1 for send/attachments) | Tier 3 — Cora (last resort) |
|---|---|---|---|
| Search / list threads | `search_threads` (real Gmail query syntax — `from:`, `to:`, `is:unread`, `after:YYYY/MM/DD`, `has:attachment`, etc.; `view: THREAD_VIEW_MINIMAL` for snippets) | `GMAIL_FETCH_EMAILS` or `GMAIL_LIST_THREADS` | `cora_email_search` (`query` param, same Gmail syntax) |
| Read a thread/message | `get_thread` (`threadId`, `messageFormat: FULL_CONTENT`) | `GMAIL_FETCH_MESSAGE_BY_THREAD_ID` or `GMAIL_FETCH_MESSAGE_BY_MESSAGE_ID` | `cora_email_show` (`id` param) |
| Create / list a draft | `create_draft`, `list_drafts` (no attachments supported natively) | `GMAIL_CREATE_EMAIL_DRAFT`, `GMAIL_GET_DRAFT`, `GMAIL_UPDATE_DRAFT`, `GMAIL_LIST_DRAFTS` (attachments supported) | `cora_email_draft` — reply-only, async (queues a background draft that appears in Gmail later), no new-thread compose |
| **Send an email** | not available — native Gmail has no send tool at all | `GMAIL_SEND_EMAIL` (new), `GMAIL_SEND_DRAFT` (from an existing draft), `GMAIL_REPLY_TO_THREAD` (in-thread reply) — this is the default for sending, not a fallback | no send capability — if Composio is down, save/report the draft and flag it to Pavi rather than failing silently |
| **Download an attachment** | not available — native Gmail can only report that `attachment_ids` exist, not fetch them | `GMAIL_GET_ATTACHMENT` (`message_id`, `attachment_id`, `file_name` — get the IDs from a `format=full` fetch first) — this is the default for attachments, not a fallback | no attachment capability |
| Label / archive / trash / spam | `label_message`, `label_thread`, `unlabel_message`, `unlabel_thread`, `apply_sensitive_message_label` / `apply_sensitive_thread_label` (trash/spam), `list_labels`, `create_label` | `GMAIL_BATCH_MODIFY_MESSAGES`, `GMAIL_ADD_LABEL_TO_EMAIL`, `GMAIL_LIST_LABELS` | not available |
| Contact lookup | not available | `GMAIL_SEARCH_PEOPLE` | not available |
| Read-receipt / open-tracking | **dropped.** This was a Slashy-only feature (`include_tracking` on `read_thread`) with no equivalent anywhere in the new chain. Don't attempt it; note the gap if asked for it. |

## Mechanics notes

- Native Gmail `search_threads` / `get_thread` take real Gmail search syntax directly (`from:`, `to:`, `is:unread`, `after:YYYY/MM/DD`, `has:attachment`, label IDs via `list_labels`) — no query-string translation needed, unlike the old Slashy `q` mapping.
- Composio Gmail sends are immediate and irreversible — no scheduled-send, no undo window. Confirm recipients, subject, body, and attachments before calling `GMAIL_SEND_EMAIL`.
- Composio drafts round-trip through `GMAIL_CREATE_EMAIL_DRAFT` → (Pavi reviews) → `GMAIL_SEND_DRAFT`, mirroring the old Slashy draft-then-send flow.
- `GMAIL_GET_ATTACHMENT` needs `attachment_id`, which only appears in a fully-hydrated message — Composio `GMAIL_FETCH_MESSAGE_BY_MESSAGE_ID` with `format=full`, since native Gmail's `attachment_ids` pointer isn't enough to fetch the bytes.
- Cora's `cora_email_draft` is fire-and-forget: it queues a reply and returns immediately; the draft shows up in Gmail later, not instantly. Don't treat the tool call as confirmation the draft exists yet.
- Known risk carried over from the old Slashy-only setup: watch for HTML-only email bodies rendering empty when read via native Gmail — escalate to Composio (`GMAIL_FETCH_MESSAGE_BY_MESSAGE_ID`) if a message looks suspiciously blank.

## Deep links

Neither native Gmail nor Composio return a one-click UI link the way Slashy did. If Pavi needs to jump to a message, construct a standard Gmail URL: `https://mail.google.com/mail/u/0/#inbox/<message_id>`.
