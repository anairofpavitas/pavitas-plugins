---
name: mcp-wrapper-builder
description: Build a new MCP server wrapper hosted on paviproczko.zo.space so external tools (Perplexity, Claude.ai, Little Bird) can connect to a Zo-mediated service. Use when Pavi says "make an MCP wrapper", "wrap X as an MCP server", "new MCP proxy", "expose X to Perplexity/Little Bird", or similar. Runs from Claude.ai chat, operating Zo through the Zo Computer MCP proxy (Claude reasons; Zo executes). Two avenues — (1) OAuth-shim-backed (Perplexity-compatible, the default) and (2) standard URL-only. Handles slug generation, the JSON-RPC scaffold, the OAuth shim wiring, smoke testing, doc updates, and post-deploy connection troubleshooting.
metadata:
  author: paviproczko.zo.space
  runs_from: claude.ai chat via the "Zo Computer" MCP proxy
---
# MCP Wrapper Builder

Repeatable process for standing up a new MCP server wrapper on `paviproczko.zo.space`. Two avenues:

- **Avenue 2 — OAuth-shim-backed (DEFAULT, most common).** Adds the two per-slug `.well-known/oauth-protected-resource` pointer routes that wire the wrapper into the shared OAuth 2.1 + DCR shim. Required for **Perplexity** (it refuses any new remote MCP server without automatic registration). Also fine for Claude.ai / Little Bird.
- **Avenue 1 — Standard URL-only.** Just the JSON-RPC route. No `.well-known` pointers. Use only when the target client does *not* require OAuth registration and Pavi explicitly wants the leaner setup.

> If Pavi doesn't specify, assume **Avenue 2**.

In both avenues the **slug is the real secret** — the OAuth handshake is theater (the Bearer token is never validated). URL-only access, no API key field needed by the client.

---

## Execution model (READ FIRST)

This skill runs from **Claude.ai chat**. Claude is the brain; Zo is the environment and the hands. There is **no second AI in the loop** — Zo executes mechanically on Claude's behalf (do not route through `ask_zo`).

**Two walls** separate Claude from Zo. Both force the same workaround:

1. **Secrets.** Zo Secrets live in the route runtime on Zo. Claude never sees them. Never ask Pavi to paste a secret into chat.
2. **Network.** Claude's own container is firewalled from `paviproczko.zo.space`. Even non-secret probes (curling the live site) cannot run from Claude's side.

**Therefore:**

- Everything that touches the live site, the route runtime, Zo Secrets, or Zo files runs **through the `Zo Computer:*` proxy tools** — never Claude's local `bash_tool`.
- Claude's local `bash_tool` is used **only** to read this skill's own reference files (e.g. to copy the scaffold). Nothing else.
- The deployed wrapper is unaffected by any of this: it's a route running on Zo, reading Zo Secrets natively at runtime. Build path ≠ product. Same wrapper whether built from chat or in-Zo.

**Tool map** (Zo-native name → proxy tool Claude calls):

| Action | Proxy tool |
|---|---|
| run a shell command / curl / smoke test on Zo | `Zo Computer:bash` |
| deploy or rewrite a route | `Zo Computer:write_space_route` |
| read / edit / write a Zo file | `Zo Computer:read_file` / `edit_file` / `write_file` |
| inspect a deployed route | `Zo Computer:get_space_route` / `list_space_routes` |
| read runtime errors | `Zo Computer:get_space_errors` |

### Preflight (ALWAYS, before step 1)
All `Zo Computer:*` tools are **deferred**. Before building:
1. `tool_search` for the ones this run needs (`write_space_route`, `bash`, `read_file`/`edit_file`, `get_space_errors`).
2. **Verify the loaded param schema** — do not assume `path`/`route_type`/`code` names; confirm them from the tool definition the search returns.

---

## Build steps

### 1. Generate + confirm a slug (ALWAYS, never skip)
Pavi's standing rule: never pick a slug silently. Produce **3** candidate slugs of the form `<service>-mcp-<word>-<word>-<word>`, present them, and **wait for Pavi to pick** before deploying.

Generate them **inline** — it's pure word selection, no network or secrets, so a round-trip to Zo is unnecessary. Use the canonical word list in `scripts/gen-slugs.ts` as the source pool and apply its normalization (lowercase, strip a trailing `-mcp`, keep `[a-z0-9-]`, three distinct words). The script is kept as the reference word list, not as something to execute.

### 2. Decide the tool dispatch mode
The JSON-RPC scaffold (`references/json-rpc-scaffold.ts`) is identical every time — only the `TOOLS` registry and `callTool` body change. Pick how each tool resolves:

- **internal-rest** (memory / supermemory pattern): tool dispatches to an existing `/api/...` REST route on `http://localhost:3099`. Best when the logic already lives in REST routes — single source of truth, no duplication. **Preferred when REST routes already exist.**
- **upstream-proxy** (composio pattern): forward the JSON-RPC straight to an upstream MCP server URL (mint/cache a session, attach the upstream auth header). Best when wrapping another MCP server. See `references/json-rpc-scaffold.ts` comments for the proxy variant. **Gotcha:** `await upstream.arrayBuffer()` (or `.text()`) and return a fresh `Response` — never stream `upstream.body` through, it causes Cloudflare 502s on SSE.
- **direct**: implement the tool inline (shell out via `child_process`, or `fetch` an external API with a server-side key from Zo Secrets). Best when there's no REST layer and no upstream MCP.

### 3. Write the JSON-RPC MCP route
Read `references/json-rpc-scaffold.ts` (local `bash_tool` is fine for reading the skill's own files), set `SERVER_INFO.name`, fill the `TOOLS` array (name, description, inputSchema, dispatch), and adjust `callTool` for the chosen mode. Deploy with **`Zo Computer:write_space_route`** (`path="/<slug>"`, `route_type="api"`, `code=...`).

> The scaffold's `initialize` now echoes the client's requested `protocolVersion` when one is sent, falling back to the constant otherwise. No action needed — it's baked in. Existing proxies are untouched; this only affects wrappers built from this scaffold going forward.

### 4. (Avenue 2 only) Wire the OAuth shim
Create the **two** per-slug pointer routes — both point at the shared auth server. Template + full explanation in `references/oauth-shim.md`. The shared shim (`/.well-known/oauth-authorization-server` + `/composio-mcp-oauth/{register,authorize,token}`) already exists; **do not recreate it.** Deploy each pointer with `Zo Computer:write_space_route`.

- `/<slug>/.well-known/oauth-protected-resource`
- `/.well-known/oauth-protected-resource/<slug>`

Both return: `{"resource":"https://paviproczko.zo.space/<slug>","authorization_servers":["https://paviproczko.zo.space"]}`

### 5. Smoke test (runs ON Zo)
The smoke test curls the live site, so it cannot run from Claude's container. **Materialize it on Zo if absent, then run it via `Zo Computer:bash`:**

1. Check for `Skills/mcp-wrapper-builder/scripts/smoke-test.sh` on Zo (`Zo Computer:read_file` or a `ls` via `Zo Computer:bash`).
2. If missing, write it there with `Zo Computer:write_file` using the copy in this bundle (`scripts/smoke-test.sh`). It's idempotent — the bundle is the single source of truth; the Zo copy is a materialized cache.
3. Run it:
   ```bash
   bash Skills/mcp-wrapper-builder/scripts/smoke-test.sh <slug> [oauth|standard] [probe-tool] [probe-json-args]
   ```
Checks `tools/list`, runs a probe `tools/call` if you pass one, verifies both `.well-known` variants (oauth mode) and the shared auth-server metadata. **All checks must pass before reporting success.**

### 6. Update the docs (MANDATORY — Pavi will not re-explain this)
All on Zo, via `Zo Computer:read_file` + `edit_file`/`write_file`. Per Pavi's rule, rewrite each artifact **in full** if it changed — no partial diffs.
- **`Documents/MCP-Proxies.md`** — add the wrapper under "Active proxies" with its URL, tool list, slug + set-date, and an explicit **OAuth shim: wired** or **OAuth shim: none (standard)** line. Update the at-a-glance shim table near the top too.
- **`Documents/Connections-Index.md`** — add a row to the section 3 proxy table and bump "Last updated".
- **Auto-memory `project_mcp_proxy.md`** — add the proxy entry with slug, dispatch mode, shim status, and `rotate by <+1 year>` date.
- **Supermemory** — save the new proxy (name, slug, dispatch mode, shim status, date) so it's recallable in future sessions.

### 7. Tell Pavi how to connect
Give the URL. For the client's API-key/token field: **leave it blank** (URL-only). Mention which clients it's verified for.

---

## If the skill runs clean but the connection fails

Deploying successfully ≠ the client connects. When Pavi reports a connection failure, **troubleshoot — don't just re-run the build.** Full playbook in `references/troubleshooting.md`. All probes run on Zo via `Zo Computer:bash` / `Zo Computer:get_space_errors`. Fast triage:

1. **Re-run the smoke test** — isolates whether the server itself is broken vs. the client handshake.
2. **Perplexity "does not support automatic registration"** → the `.well-known/oauth-protected-resource` pointers are missing or wrong (Avenue 1 used where Avenue 2 was needed). Add them.
3. **502 / hang on connect, SSE involved** → upstream-proxy streamed `upstream.body` directly. Buffer it first.
4. **`tools/list` empty** → upstream session not minted, or the TOOLS registry is empty / the dispatch threw. Check `Zo Computer:get_space_errors` and `/dev/shm/zosite-*.log` (on Zo).
5. **Client probes a `.well-known` variant you didn't create** → some clients hit `/.well-known/.../<slug>`, others `/<slug>/.well-known/...`. Both must exist.

---

## Reference map
- `references/json-rpc-scaffold.ts` — the canonical MCP JSON-RPC 2.0 server skeleton (all three dispatch modes documented inline; protocol-version echo baked in).
- `references/oauth-shim.md` — how the shared shim works + the per-slug pointer template.
- `references/troubleshooting.md` — connection-failure playbook.
- `scripts/gen-slugs.ts` — canonical slug word list / normalization reference (generate inline; don't execute).
- `scripts/smoke-test.sh` — parametrized post-deploy verifier; materialize on Zo and run via `Zo Computer:bash`.
