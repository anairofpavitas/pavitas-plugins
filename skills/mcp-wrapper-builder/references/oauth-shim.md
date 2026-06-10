# OAuth shim (Avenue 2)

Perplexity refuses any new remote MCP server that doesn't advertise OAuth 2.1 +
Dynamic Client Registration — it shows `[API_CLIENTS_ERROR] Server does not
support automatic registration`. The shim satisfies that handshake. It is
**theater**: the Bearer token is never validated by the wrapper. The **slug is
still the only real secret**, and the client's API-key field stays blank.

## Architecture: one shared shim, per-slug pointers

There is **ONE** shared auth server, reused by every wrapper. Each new wrapper
adds only its own two `oauth-protected-resource` pointer routes.

```
SHARED (already deployed — do NOT recreate):
  /.well-known/oauth-authorization-server      RFC 8414 metadata
  /composio-mcp-oauth/register                 DCR — mints dummy client creds
  /composio-mcp-oauth/authorize                302 redirect with ?code=&state=
  /composio-mcp-oauth/token                    returns a random Bearer token

PER-SLUG (create these two for every Avenue-2 wrapper):
  /<slug>/.well-known/oauth-protected-resource         (root variant)
  /.well-known/oauth-protected-resource/<slug>         (path variant)
```

> The `composio-mcp-oauth` name is historical, not Composio-specific — it's the
> shared shim for all wrappers. Don't rename it.

## Why two pointer routes

Different clients probe different URL shapes. Some hit
`/<slug>/.well-known/oauth-protected-resource`, others hit
`/.well-known/oauth-protected-resource/<slug>`. **Both must exist** or the
client that probes the missing one fails to connect. This is the #1 cause of a
"deployed fine but won't connect" report.

## Per-slug pointer template

Both routes return the same body. Deploy each with the `Zo Computer:write_space_route` proxy tool
(`path=..., route_type="api", code=...`):

```ts
import type { Context } from "hono";

const BASE = "https://paviproczko.zo.space";

export default (c: Context) =>
  c.json({
    resource: `${BASE}/<slug>`,
    authorization_servers: [BASE],
  });
```

Returns (RFC 9728):

```json
{
  "resource": "https://paviproczko.zo.space/<slug>",
  "authorization_servers": ["https://paviproczko.zo.space"]
}
```

## The shared routes (reference — already deployed)

You should not need to recreate these. Documented here so you can verify or
repair them.

**`/.well-known/oauth-authorization-server`** (RFC 8414):

```ts
import type { Context } from "hono";
const BASE = "https://paviproczko.zo.space";
const OAUTH = `${BASE}/composio-mcp-oauth`;
export default (c: Context) =>
  c.json({
    issuer: BASE,
    authorization_endpoint: `${OAUTH}/authorize`,
    token_endpoint: `${OAUTH}/token`,
    registration_endpoint: `${OAUTH}/register`,
    response_types_supported: ["code"],
    grant_types_supported: ["authorization_code"],
    code_challenge_methods_supported: ["S256"],
    token_endpoint_auth_methods_supported: ["none", "client_secret_post"],
    scopes_supported: ["mcp"],
  });
```

**`/composio-mcp-oauth/register`** (DCR). Mints a dummy `client_id`/
`client_secret`. **MUST echo `token_endpoint_auth_method` as `none` (or
`client_secret_post`) — never `client_secret_basic`, or Perplexity rejects it.**

```ts
import type { Context } from "hono";
import { randomUUID } from "node:crypto";
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
};
export default async (c: Context) => {
  if (c.req.method === "OPTIONS") return new Response(null, { status: 204, headers: CORS });
  const body = await c.req.json().catch(() => ({}));
  const client_id = `cmcp-${randomUUID().slice(0, 8)}`;
  const client_secret = randomUUID().replace(/-/g, "");
  const authMethod =
    body.token_endpoint_auth_method === "client_secret_post"
      ? "client_secret_post"
      : "none";
  return new Response(
    JSON.stringify({
      client_id,
      client_secret,
      client_id_issued_at: Math.floor(Date.now() / 1000),
      client_secret_expires_at: 0,
      redirect_uris: body.redirect_uris || [],
      grant_types: body.grant_types || ["authorization_code"],
      response_types: ["code"],
      token_endpoint_auth_method: authMethod,
    }),
    { status: 201, headers: { "Content-Type": "application/json", ...CORS } },
  );
};
```

**`/composio-mcp-oauth/authorize`** — 302 redirect back to `redirect_uri` with a
random `code` (and the `state` echoed):

```ts
import type { Context } from "hono";
import { randomUUID } from "node:crypto";
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};
export default (c: Context) => {
  if (c.req.method === "OPTIONS") return new Response(null, { status: 204, headers: CORS });
  const redirectUri = c.req.query("redirect_uri");
  const state = c.req.query("state") || "";
  if (!redirectUri)
    return new Response(
      JSON.stringify({ error: "invalid_request", error_description: "redirect_uri required" }),
      { status: 400, headers: { "Content-Type": "application/json", ...CORS } },
    );
  const code = randomUUID().replace(/-/g, "");
  const url = new URL(redirectUri);
  url.searchParams.set("code", code);
  if (state) url.searchParams.set("state", state);
  return Response.redirect(url.toString(), 302);
};
```

**`/composio-mcp-oauth/token`** — returns a random Bearer token (never checked):

```ts
import type { Context } from "hono";
import { randomUUID } from "node:crypto";
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
};
export default async (c: Context) => {
  if (c.req.method === "OPTIONS") return new Response(null, { status: 204, headers: CORS });
  return new Response(
    JSON.stringify({
      access_token: randomUUID().replace(/-/g, ""),
      token_type: "Bearer",
      expires_in: 3600,
      scope: "mcp",
    }),
    { status: 200, headers: { "Content-Type": "application/json", ...CORS } },
  );
};
```

## Avenue 1 (standard, no shim)

Skip every `.well-known` route. Deploy only the JSON-RPC route. Use only when
the target client does **not** require OAuth registration and Pavi explicitly
wants the leaner setup. The slug is still the secret. Note it as **OAuth shim:
none (standard)** in the docs.
