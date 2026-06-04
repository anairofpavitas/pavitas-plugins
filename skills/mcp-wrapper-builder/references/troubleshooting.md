# Connection-failure playbook

> **Execution note (Claude-via-proxy).** Claude's own container CANNOT reach
> `paviproczko.zo.space` and CANNOT see Zo Secrets. Every `curl` probe, log
> read, and `get_space_errors` call below runs ON Zo — issue them through the
> `Zo Computer:bash` / `Zo Computer:get_space_errors` proxy tools, never local
> Bash. (Deferred tools: `tool_search` to load them first.)


Deploying successfully ≠ the client connects. When Pavi reports a connection
failure, **diagnose root cause before touching the routes again.** Re-running
the build blindly wastes a slug and usually doesn't fix anything.

## Triage order

### 1. Re-run the smoke test
Run the smoke test ON Zo via `Zo Computer:bash` (materialize the script first
if absent — see SKILL.md step 5):

```bash
bash Skills/mcp-wrapper-builder/scripts/smoke-test.sh <slug> [oauth|standard]
```
This isolates **server broken** (smoke test fails) vs **client handshake
broken** (smoke test passes but the client still won't connect). Everything
below assumes you've read the smoke-test output.

### 2. Perplexity: "Server does not support automatic registration"
The `oauth-protected-resource` pointers are missing or wrong — i.e. Avenue 1 was
used where Avenue 2 was needed, or only one of the two variants was created.
- Verify BOTH variants return the RFC 9728 JSON:
  - `https://paviproczko.zo.space/<slug>/.well-known/oauth-protected-resource`
  - `https://paviproczko.zo.space/.well-known/oauth-protected-resource/<slug>`
- Verify the shared `/.well-known/oauth-authorization-server` resolves and
  `/composio-mcp-oauth/register` returns `token_endpoint_auth_method` of `none`
  (or `client_secret_post`) — **never `client_secret_basic`** (Perplexity rejects).
- Fix: add the missing pointer route(s). See `oauth-shim.md`.

### 3. 502 / hang on connect, SSE involved (upstream-proxy)
The wrapper streamed `upstream.body` straight through `new Response()`.
Cloudflare 502s on streamed SSE. Fix: `await upstream.text()` (or
`.arrayBuffer()`), parse, and return a **fresh** Response. See the
`parseUpstream` helper in `json-rpc-scaffold.ts` (Variant A).

### 4. `tools/list` returns empty
- **internal-rest:** the TOOLS registry is empty, or a dispatch threw. Curl the
  underlying `/api/...` route directly on `localhost:3099` to confirm it works.
- **upstream-proxy:** the upstream session wasn't minted (bad/missing API key),
  or the upstream's own `tools/list` is empty (e.g. Composio with 0 toolkits
  configured). Check `get_space_errors` and the upstream session response.
- Check the server logs:
  ```bash
  # via Zo Computer:get_space_errors, then on Zo:
  tail -n 100 /dev/shm/zosite-*.log
  ```

### 5. Client probes a `.well-known` variant you didn't create
Some clients hit `/.well-known/oauth-protected-resource/<slug>`, others hit
`/<slug>/.well-known/oauth-protected-resource`. If only one exists, the client
that probes the other fails. **Both must exist.** This is the most common
"deployed fine, won't connect" cause.

### 6. Secrets not available
upstream-proxy / direct modes read `process.env.<KEY>`. If the wrapper returns
`... not set in Zo Secrets`, the key is missing from the route's runtime env.
Confirm the secret exists and that you tested via `Zo Computer:bash`
(local Bash can't see Zo secrets).

## Useful live probes

```bash
URL="https://paviproczko.zo.space/<slug>"

# tools/list
curl -s -X POST "$URL" -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | jq .

# initialize
curl -s -X POST "$URL" -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' | jq .

# both .well-known variants (oauth mode)
curl -s "$URL/.well-known/oauth-protected-resource" | jq .
curl -s "https://paviproczko.zo.space/.well-known/oauth-protected-resource/<slug>" | jq .

# shared auth-server metadata
curl -s "https://paviproczko.zo.space/.well-known/oauth-authorization-server" | jq .

# SSE accept header (some clients send this — must still get a valid frame)
curl -s -X POST "$URL" -H 'content-type: application/json' \
  -H 'accept: text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

## What NOT to do
- Don't rotate/replace the slug as a "fix" — that changes the secret and the URL
  Pavi already pasted into the client, and rarely addresses the actual fault.
- Don't recreate the shared `/composio-mcp-oauth/*` routes — they're shared; if
  they're broken, repair in place (every wrapper depends on them).
- Don't claim success off a clean deploy. Confirm the client actually connects.
