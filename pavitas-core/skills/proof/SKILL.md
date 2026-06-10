---
name: proof
description: "Work with Proof documents via proofeditor.ai (vendor-provided agent skill). Load ONLY on explicit Proof signals: a proofeditor.ai URL, the phrases \"Proof doc\", \"open in Proof\", \"put this in Proof\", or an installed Proof default mode. Does NOT trigger on \"proofread\", \"proof this\", \"check my proof\", or any editing/review request that does not name the Proof Editor product."
---

# Proof

> **Disambiguation:** This skill is for the Proof Editor product (proofeditor.ai) only. Requests to proofread, proof, or review text are ordinary editing tasks — do not use this skill or its API for them.

Proof is a collaborative markdown editor for agents and humans. Use the hosted web API at `https://www.proofeditor.ai`.

Every write must include `by: "ai:<agent-name>"` so Proof can track who wrote what.
Presence uses `X-Agent-Id: ai:<agent-name>` when joining state or posting presence. A bearer/share token authenticates document access. `by` records authorship.

## Default Behavior

If the user shares a Proof URL:
- Join the doc immediately.
- Show presence right away.
- Read the current state before editing.
- Work in the Proof doc unless the user explicitly asks you to move elsewhere.

When creating new docs, follow this priority order:
1. If persistent instructions already define a Proof default mode, use it.
2. Otherwise default to `collaborative_docs`.

Supported default modes:
- `all_new_markdown`: new markdown artifacts you create go to Proof by default.
- `collaborative_docs`: plans, specs, bug writeups, reports, memos, proposals, drafts, and similar iterative docs go to Proof by default.
- `explicit_only`: only use Proof when the user explicitly asks.

Boundary rules:
- Existing repo-tracked markdown files stay local unless the user explicitly asks to move or share them in Proof.
- Do not silently replace local project docs with Proof links.
- If the task is code-adjacent local documentation, keep it local unless the user asks for Proof.

## Shared URLs And Auth

Shared URL format:

```text
https://www.proofeditor.ai/d/<slug>?token=<token>
```

Use one of:
- `Authorization: Bearer <token>` (preferred)
- `x-share-token: <token>`
- `?token=<token>`

`by` controls authorship. `X-Agent-Id` controls presence identity. Bearer/share tokens authenticate document access.

## If Proof Looks Wrong

Use one reporting tool call:

```bash
curl -sS -X POST "https://www.proofeditor.ai/api/bridge/report_bug" \
  -H "Content-Type: application/json" \
  -d '{
    "summary":"Short bug summary",
    "context":"What you were trying to do and what looked wrong.",
    "slug":"<slug-if-you-have-it>",
    "evidence":[
      {
        "kind":"http_response",
        "method":"POST",
        "url":"https://www.proofeditor.ai/api/agent/<slug>/edit/v2",
        "status":500,
        "requestId":"<x-request-id>"
      }
    ]
  }'
```

If the response returns `status: "needs_more_info"`, ask the suggested questions and call the same endpoint again.

If you want reference code while debugging or preparing the report, you can optionally inspect:
- `https://github.com/EveryInc/proof-sdk`

## Existing Proof Docs

When a Proof URL is provided:
1. Extract `slug` and `token`.
2. Join immediately by reading state with `X-Agent-Id` or by posting presence with `X-Agent-Id`/`agentId`.
3. Read the doc.
4. Reply with a short confirmation like `Connected in Proof and ready.`
5. Then keep working inside Proof.

Read state and show presence on read:

```bash
curl -sS "https://www.proofeditor.ai/api/agent/<slug>/state" \
  -H "Authorization: Bearer <token>" \
  -H "X-Agent-Id: <your-agent-id>"
```

Shared links also support content negotiation:

```bash
curl -sS -H "Accept: application/json" "https://www.proofeditor.ai/d/<slug>?token=<token>"
curl -sS -H "Accept: text/markdown" "https://www.proofeditor.ai/d/<slug>?token=<token>"
```

Update presence explicitly:

```bash
curl -sS -X POST "https://www.proofeditor.ai/api/agent/<slug>/presence" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -H "X-Agent-Id: <your-agent-id>" \
  -d '{
    "agentId":"<your-agent-id>",
    "status":"reading",
    "summary":"Joining the doc"
  }'
```

Presence identity can be supplied as `X-Agent-Id`, `agentId`, or `agent.id`. Prefer `X-Agent-Id: ai:<agent-name>`.

Common statuses: `reading`, `thinking`, `acting`, `waiting`, `completed`, `error`.

## Reading Comments

Read comment threads from:

```text
GET /api/agent/<slug>/state?kinds=comment
```

Comment bodies, replies, and resolved state live in `marks` on the state response. For comment marks, `thread` is the chronological message list and includes the root comment as `thread[0]`; legacy `text` remains the root comment body. Replies created with `resolve: true` include `resolvedHere: true` on that message, while top-level `resolved` reflects the thread's current state. Standalone `comment.resolve` and `comment.unresolve` only change top-level `resolved`; they do not add a thread message. `state.marks` is a union of mark kinds, and `?kinds=comment` filters it server-side for comment workflows.

- Read `state.marks[*].thread` for comment messages.
- Use comma-separated semantic filters when you intentionally need multiple families, for example `?kinds=comment,suggestion,provenance`.
- Use `/snapshot` for block refs and `edit/v2` only. It does not include comment thread bodies.
- Use the comment mark's `markId` as the reply/resolve target. `threadId` is read metadata.
- Public `/ops` supports resolving and unresolving comments; it does not support deleting comments.
- Use `/events/pending` or `/events/stream` to notice activity and decide when to refresh `state`. Do not treat events as the source of comment text.
- `text.settled` is a sparse wake signal for normal text edits after collab persistence settles. Refresh `state` before interpreting or editing; the event data intentionally includes hashes/revisions, not document content, and the actor is `system:collab`.

Common mark kinds:

| Kind | Use |
|---|---|
| `comment` | Review comments, replies, and resolved state |
| `authored` | Provenance UI metadata |
| `insert`, `delete`, `replace` | Track-changes suggestions |

Filter aliases: `comment`, `suggestion`, and `provenance` expand to the concrete mark kinds above.

## Updating The Title

Use the title endpoint for document metadata:

```bash
curl -sS -X PUT "https://www.proofeditor.ai/api/documents/<slug>/title" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"title":"Updated document title"}'
```

Authenticate with `Authorization: Bearer <token>` or `x-share-token: <token>`.

## Deleting A Document

Only the document owner can delete a Proof doc. Use the owner credential returned at creation time, or a same-origin Every owner session in the browser:

```bash
curl -sS -X DELETE "https://www.proofeditor.ai/api/documents/<slug>" \
  -H "Authorization: Bearer <ownerSecret>"
```

Viewer, commenter, and editor share tokens cannot delete documents. Browser cookie based deletes require a strict same-origin request, so do not rely on tokenized viewer links or copied Library rows for deletion authority. A successful delete returns `shareState: "DELETED"` and later reads return deleted-document responses.

## Creating A New Proof Doc

Create a shared document:

```bash
curl -sS -X POST https://www.proofeditor.ai/share/markdown \
  -H "Content-Type: application/json" \
  -d '{"title":"My Document","markdown":"# Hello\n\nFirst draft."}'
```

Save:
- `slug`
- `accessToken`
- `ownerSecret`
- `shareUrl`
- `tokenUrl`
- `_links`

When Proof is the default for the task:
1. Create the doc.
2. Return the live Proof link to the user.
3. Join the doc immediately.
4. Keep working there.

## Choosing An Edit Strategy

| Task | Recommended API | Why |
|---|---|---|
| Precise paragraph or section rewrite | `edit/v2` | Block refs plus mutation-base locking |
| Simple append, replace, or insert | `edit/v2` | Use block refs from `/snapshot` |
| Human-reviewed edits | `ops` | Suggestions and comments in track changes |
| Large rewrite proposal | `ops` + `rewrite.apply` | Produces reviewable changes |

Edit hierarchy for content changes:
1. Prefer `/snapshot` + `/edit/v2` block operations (`replace_block`, `insert_before`, `insert_after`, `delete_block`, `replace_range`) for targeted edits.
2. Use `find_replace_in_block` or `find_replace_in_doc` for literal replacements when the exact text is known.
3. Use `ops` comments/suggestions when the human should review before accepting.
4. Use full-document `rewrite.apply` only as a last resort. It is the bluntest path and can be blocked while live collaborators are connected.

## Snapshot And Edit V2

Get a snapshot:

```bash
curl -sS "https://www.proofeditor.ai/api/agent/<slug>/snapshot" \
  -H "Authorization: Bearer <token>"
```

Use `mutationBase.token` as `baseToken` and use `blocks[].ref` as the block target from `/snapshot`. Treat `ref` as an opaque request token. `ordinalRef` is a human-readable display hint. Mutation base tokens are content-addressed over normalized document content, marks, and access epoch, so returning to a previous exact state can return a previously seen token. In a batched `operations` array, every `ref`, `fromRef`, and `toRef` is resolved against the same base snapshot before any operation is applied. Full successful `/edit/v2` responses include the next `mutationBase.token` and fresh `snapshot.blocks[].ref` values; reuse both when chaining another block-ref edit.

Apply block operations:

```bash
curl -sS -X POST "https://www.proofeditor.ai/api/agent/<slug>/edit/v2" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -H "Idempotency-Key: <unique-key>" \
  -d '{
    "by":"ai:codex",
    "baseToken":"mt1:<token-from-snapshot>",
    "operations":[
      {"op":"replace_block","ref":"<block-ref-from-snapshot>","block":{"markdown":"Updated paragraph."}},
      {"op":"insert_after","ref":"<block-ref-from-snapshot>","blocks":[{"markdown":"## New section"}]}
    ]
  }'
```

Supported ops:
- `replace_block`
- `insert_before`
- `insert_after`
- `delete_block`
- `replace_range`
- `find_replace_in_block`
- `find_replace_in_doc`

`find_replace_in_doc` performs literal document-wide replacements. It defaults to `occurrence: "all"` and returns per-block counts in `operationResults`. Treat `operationResults.blockMatches[].ref` as reporting/display data; it is an ordinal such as `b3`, not an opaque snapshot ref. For follow-up mutations, re-read `/snapshot` and use `blocks[].ref`.

Validate a proposed batch without writing by adding `?dryRun=1` or `?validate=1` to `/edit/v2`. Dry-run responses include `valid`, `appliedCount`, and per-op `results[]`; no document mutation, events, or broadcasts occur.
Use `?return=minimal` on `/edit/v2` to receive `ok`, `revision`, `appliedCount`, next `mutationBase`, and optional `warnings`. Minimal responses are token-only and omit fresh block refs; re-read `/snapshot` before another `/edit/v2` mutation that needs `blocks[].ref`. `post_commit_verification_pending` means the write committed but post-commit verification or snapshot refresh had not completed before the response; read `/state` or `/snapshot` to confirm convergence before retrying.

## Comments, Suggestions, And Rewrites

Primary endpoint:

```text
POST /api/agent/<slug>/ops
```

`/ops` requires `baseToken` from `mutationBase.token` on `/state` or `/snapshot`. Successful `/ops` responses include the next `mutationBase.token`; reuse it as the next `baseToken` when chaining writes.

- `/ops` uses top-level `type` for single operations, or top-level `operations` for comment batches.
- `/edit/v2` uses top-level `operations`, and each entry uses `op`.

Supported ops:
- `comment.add`
- `comment.reply`
- `comment.resolve`
- `comment.unresolve`
- `suggestion.add`
- `suggestion.accept`
- `suggestion.reject`
- `rewrite.apply`

Public `/ops` does not support `comment.delete` or `suggestion.resolve`.

Examples:

```json
{"type":"comment.add","by":"ai:codex","baseToken":"mt1:<token-from-state-or-snapshot>","quote":"anchor text","text":"Comment body"}
{"type":"comment.reply","by":"ai:codex","baseToken":"mt1:<token-from-state-or-snapshot>","markId":"comment-123","text":"Reply text"}
{"type":"comment.reply","by":"ai:codex","baseToken":"mt1:<token-from-state-or-snapshot>","markId":"comment-123","text":"Fixed.","resolve":true}
{"by":"ai:codex","baseToken":"mt1:<token-from-state-or-snapshot>","operations":[{"type":"comment.reply","markId":"comment-123","text":"Fixed first.","resolve":true},{"type":"comment.resolve","markId":"comment-456"}]}
{"type":"comment.resolve","by":"ai:codex","baseToken":"mt1:<token-from-state-or-snapshot>","markId":"comment-123"}
{"type":"comment.unresolve","by":"ai:codex","baseToken":"mt1:<token-from-state-or-snapshot>","markId":"comment-123"}
{"type":"suggestion.add","by":"ai:codex","baseToken":"mt1:<token-from-state-or-snapshot>","kind":"replace","quote":"old text","content":"new text"}
{"type":"suggestion.add","by":"ai:codex","baseToken":"mt1:<token-from-state-or-snapshot>","kind":"replace","quote":"old text","content":"new text","status":"accepted"}
{"type":"suggestion.accept","by":"ai:codex","baseToken":"mt1:<token-from-state-or-snapshot>","markId":"suggestion-123"}
{"type":"suggestion.reject","by":"ai:codex","baseToken":"mt1:<token-from-state-or-snapshot>","markId":"suggestion-123"}
{"type":"rewrite.apply","by":"ai:codex","baseToken":"mt1:<token-from-state-or-snapshot>","content":"# Rewritten markdown"}
```

Use `suggestion.accept` or `suggestion.reject` to finish suggestions.

Batch `/ops` supports existing-thread comment mutations (`comment.reply`, `comment.resolve`, and `comment.unresolve`) in a top-level `operations` array. It uses one `baseToken` and persists the batch as one authoritative marks mutation.

Use `ops` when you want the human to review changes in track changes.

## Events And Presence

Poll for pending events:

```bash
curl -sS "https://www.proofeditor.ai/api/agent/<slug>/events/pending?after=0" \
  -H "Authorization: Bearer <token>"
```

Subscribe to new live events:

```bash
curl -N "https://www.proofeditor.ai/api/agent/<slug>/events/stream" \
  -H "Authorization: Bearer <token>"
```

Only pass `after=<cursor>` or `Last-Event-ID: <cursor>` when you intentionally want replay. Without a cursor, the stream starts with new events created after connection.
Event frames include `id:`, `event: <type>`, and JSON `data:`. The stream sends heartbeat comments and closes periodically; planned closes include an id-only `event: cursor` frame so clients can reconnect with the last seen `id`.
`text.settled` means visible text changed through live collaboration and the persisted state has settled. Treat it as a prompt to refresh `state` and decide whether to act; it does not carry the edited text.

Ack processed events:

```bash
curl -sS -X POST "https://www.proofeditor.ai/api/agent/<slug>/events/ack" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"upToId":123,"by":"ai:codex"}'
```

If you are staying in the loop while a human reviews changes, keep presence updated so the doc shows what you are doing.

## Error Handling

| Error | Meaning | Action |
|---|---|---|
| `401/403` | Bad or missing auth | Re-read token from URL and retry with bearer token |
| `404` | Slug not found | Verify slug and environment |
| `400 INVALID_BASE_TOKEN` | `baseToken` is malformed | Re-read `state` or `snapshot` and send the exact `mutationBase.token` |
| `409 BASE_TOKEN_REQUIRED` | `baseToken` is missing | Re-read `state` or `snapshot` and include `mutationBase.token` |
| `400 PRECISE_REF_REQUIRED` | Live edit needs a snapshot block ref | Re-read `/snapshot` and use `blocks[].ref` |
| `400 INVALID_REF` | The block ref cannot be resolved in the current block map | Re-read `/snapshot` and retry with `blocks[].ref` |
| `409 AUTHORITATIVE_BASE_UNAVAILABLE` | Yjs authority unavailable | Re-read `state` or `snapshot`, then retry with `mutationBase.token` when present |
| `409 STALE_BASE` | Your `baseToken` is stale | Use the fresh snapshot and retry with its `mutationBase.token` and `blocks[].ref` values |
| `409 STALE_BLOCK_REF` | Your snapshot block ref belongs to a different document or `baseToken` | Re-read `/snapshot` and retry with fresh `mutationBase.token` plus `blocks[].ref` |
| `409 ANCHOR_NOT_FOUND` | Search anchor missing | Re-read state and choose a tighter anchor |
| `413 YJS_UPDATE_TOO_LARGE` | Mutation is too large for the Yjs update fuse | Reduce or split the write before retrying |
| `422` | Invalid payload | Fix required fields and schema |
| `429` | Rate limit | Back off and retry with jitter |

Guidelines:
- Re-read `/snapshot` before retries that depend on block refs; send the new `mutationBase.token` and `blocks[].ref`.
- If the behavior still looks wrong after a normal retry, call `POST /api/bridge/report_bug` with the request/response, request ID, slug, and a short context note.
- Include `by` on every write.
- Prefer `content` and markdown payloads as canonical text input.
- Use `Idempotency-Key` on `edit/v2` requests so retries stay safe.

## Discovery

- Discovery JSON: `https://www.proofeditor.ai/.well-known/agent.json`
- Docs: `https://www.proofeditor.ai/agent-docs`
- Setup: `https://www.proofeditor.ai/agent-setup`
- Report bug tool: `https://www.proofeditor.ai/api/bridge/report_bug`
- Open-source reference: `https://github.com/EveryInc/proof-sdk`