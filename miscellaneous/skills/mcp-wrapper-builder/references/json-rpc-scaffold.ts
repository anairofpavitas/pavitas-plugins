// ============================================================================
// CANONICAL MCP JSON-RPC 2.0 SERVER SCAFFOLD
// ----------------------------------------------------------------------------
// Deploy as a zo.space API route: write_space_route(path="/<slug>", route_type="api", code=...)
//
// This skeleton is IDENTICAL across every wrapper. Only TWO things change:
//   1. SERVER_INFO.name
//   2. The TOOLS registry + the body of callTool()
//
// Pick ONE of the three dispatch modes below. The transport plumbing
// (initialize / ping / tools/list / tools/call / batch / SSE) never changes.
//
//   - internal-rest   → dispatch each tool to an existing /api/... REST route
//                       on http://localhost:3099 (memory / supermemory pattern).
//                       PREFERRED when REST routes already exist.
//   - upstream-proxy  → forward JSON-RPC to another MCP server URL
//                       (composio pattern). Mint/cache a session, attach auth.
//   - direct          → implement the tool inline (shell out, or fetch an
//                       external API with a server-side key from Zo Secrets).
//
// The block below is the internal-rest variant (the default). The
// upstream-proxy and direct variants are documented as comments at the bottom.
// ============================================================================

import type { Context } from "hono";

const INTERNAL_BASE = "http://localhost:3099";
const PROTOCOL_VERSION = "2024-11-05"; // fallback only — initialize echoes the client's version when sent
const SERVER_INFO = { name: "CHANGEME-mcp", version: "1.0.0" }; // <-- set name

type ToolDef = {
  name: string;
  description: string;
  inputSchema: any;
  // dispatch maps the tool args to an internal REST call.
  dispatch: (args: any) => { method: string; path: string; body?: any };
};

// ---------------------------------------------------------------------------
// TOOLS registry — the ONLY part you rewrite per wrapper.
// Each tool: name, description (the LLM reads this — be precise), JSON-schema
// inputSchema, and a dispatch() returning {method, path, body}.
// ---------------------------------------------------------------------------
const TOOLS: ToolDef[] = [
  {
    name: "example_tool",
    description:
      "Replace me. One precise sentence the calling LLM uses to decide when to invoke this tool.",
    inputSchema: {
      type: "object",
      properties: {
        q: { type: "string", description: "Search terms" },
        limit: { type: "number", description: "Max results (default 5)" },
      },
      required: ["q"],
    },
    // GET → args become query params; POST/PUT/DELETE → args become JSON body.
    dispatch: (a) => ({ method: "GET", path: "/api/example/search", body: a }),
  },
];

const PUBLIC_TOOLS = TOOLS.map(({ name, description, inputSchema }) => ({
  name,
  description,
  inputSchema,
}));

// ---------------------------------------------------------------------------
// callTool — internal-rest dispatch. GET args → querystring, else JSON body.
// ---------------------------------------------------------------------------
async function callTool(name: string, args: any): Promise<any> {
  const tool = TOOLS.find((t) => t.name === name);
  if (!tool) throw new Error(`unknown tool: ${name}`);
  const d = tool.dispatch(args || {});
  let url = INTERNAL_BASE + d.path;
  const init: RequestInit = { method: d.method, headers: {} };
  if (d.method === "GET") {
    const params = new URLSearchParams();
    for (const [k, v] of Object.entries(d.body || {})) {
      if (v !== undefined && v !== null) params.set(k, String(v));
    }
    const qs = params.toString();
    if (qs) url += `?${qs}`;
  } else {
    (init.headers as any)["Content-Type"] = "application/json";
    init.body = JSON.stringify(d.body || {});
  }
  const res = await fetch(url, init);
  const text = await res.text();
  let json: any;
  try {
    json = JSON.parse(text);
  } catch {
    json = { raw: text };
  }
  return json;
}

// ===========================================================================
// EVERYTHING BELOW IS TRANSPORT PLUMBING — copy verbatim, do not edit.
// ===========================================================================

function rpcOk(id: any, result: any) {
  return { jsonrpc: "2.0", id: id ?? null, result };
}

function rpcError(id: any, code: number, message: string) {
  return { jsonrpc: "2.0", id: id ?? null, error: { code, message } };
}

async function handleRpc(req: any): Promise<any | null> {
  if (!req || typeof req !== "object") return rpcError(null, -32600, "invalid request");
  const { method, id } = req;
  const params = req.params;
  const isNotification = id === undefined || id === null;

  if (method === "initialize") {
    // Echo the client's requested protocol version when it sends one; fall
    // back to the constant otherwise. Strict clients dislike being handed a
    // version they didn't ask for. No client sends one → identical to old behavior.
    const clientVersion = params?.protocolVersion;
    return rpcOk(id, {
      protocolVersion: clientVersion || PROTOCOL_VERSION,
      capabilities: { tools: { listChanged: false } },
      serverInfo: SERVER_INFO,
    });
  }

  if (method === "notifications/initialized" || method === "initialized") return null;
  if (method === "ping") return rpcOk(id, {});

  if (method === "tools/list") {
    return rpcOk(id, { tools: PUBLIC_TOOLS });
  }

  if (method === "tools/call") {
    const toolName = params?.name;
    const args = params?.arguments ?? {};
    try {
      const result = await callTool(toolName, args);
      return rpcOk(id, {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      });
    } catch (err: any) {
      return rpcOk(id, {
        content: [{ type: "text", text: err?.message || String(err) }],
        isError: true,
      });
    }
  }

  if (isNotification) return null;
  return rpcError(id, -32601, `method not found: ${method}`);
}

function rpcResponse(payload: any, accept: string | undefined): Response {
  if (payload === null) return new Response(null, { status: 202 });
  const wantsSSE = !!accept && accept.includes("text/event-stream");
  if (wantsSSE) {
    const sse = `event: message\ndata: ${JSON.stringify(payload)}\n\n`;
    return new Response(sse, {
      status: 200,
      headers: { "Content-Type": "text/event-stream", "Cache-Control": "no-cache" },
    });
  }
  return new Response(JSON.stringify(payload), {
    status: 200,
    headers: { "Content-Type": "application/json" },
  });
}

export default async (c: Context) => {
  const method = c.req.method;

  if (method === "GET") {
    return new Response(
      JSON.stringify({
        name: SERVER_INFO.name,
        version: SERVER_INFO.version,
        protocol: PROTOCOL_VERSION,
        transport: "http",
        message: `${SERVER_INFO.name} MCP wrapper. POST JSON-RPC 2.0 requests to this endpoint.`,
      }),
      { status: 200, headers: { "Content-Type": "application/json" } },
    );
  }

  if (method !== "POST") return new Response("method not allowed", { status: 405 });

  const accept = c.req.header("accept");

  let body: any = null;
  try {
    const text = await c.req.text();
    body = text ? JSON.parse(text) : null;
  } catch {
    return rpcResponse(rpcError(null, -32700, "parse error"), accept);
  }

  if (body === null) return rpcResponse(rpcError(null, -32600, "empty body"), accept);

  // JSON-RPC batch support.
  if (Array.isArray(body)) {
    const responses = (await Promise.all(body.map((r) => handleRpc(r)))).filter((r) => r !== null);
    if (responses.length === 0) return new Response(null, { status: 202 });
    return rpcResponse(responses, accept);
  }

  const response = await handleRpc(body);
  return rpcResponse(response, accept);
};

// ===========================================================================
// VARIANT A — upstream-proxy (composio pattern)
// ---------------------------------------------------------------------------
// Replace the TOOLS registry + callTool with session minting + forwarding.
// tools/list and tools/call forward to the upstream MCP server.
//
//   const UPSTREAM_API_BASE = "https://backend.example.dev/api/v3.1";
//   let cachedSessionUrl: string | null = null;
//   let cachedTools: any[] | null = null;
//
//   async function createSession(apiKey: string): Promise<string> {
//     const res = await fetch(`${UPSTREAM_API_BASE}/session`, {
//       method: "POST",
//       headers: { "Content-Type": "application/json", "x-api-key": apiKey },
//       body: JSON.stringify({ user_id: "pavi" }),
//     });
//     if (!res.ok) throw new Error(`session create ${res.status}`);
//     const data = await res.json();
//     const url = data?.mcp?.url;
//     if (!url) throw new Error("session response missing mcp.url");
//     return url;
//   }
//
//   async function getSessionUrl(apiKey: string): Promise<string> {
//     if (!cachedSessionUrl) cachedSessionUrl = await createSession(apiKey);
//     return cachedSessionUrl;
//   }
//
//   // CRITICAL SSE GOTCHA: always read the body to a STRING/arrayBuffer and
//   // return a FRESH Response. NEVER pass upstream.body to new Response(...) —
//   // streaming SSE through causes Cloudflare 502s.
//   function parseUpstream(text: string): any {
//     const t = text.trim();
//     if (t.startsWith("event:") || t.includes("\ndata:")) {
//       for (const line of t.split("\n")) {
//         if (line.startsWith("data:")) return JSON.parse(line.slice(5).trim());
//       }
//       throw new Error("upstream SSE had no data line");
//     }
//     return JSON.parse(t);
//   }
//
//   async function callUpstream(apiKey: string, payload: any, retried = false): Promise<any> {
//     const url = await getSessionUrl(apiKey);
//     const res = await fetch(url, {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//         Accept: "application/json, text/event-stream",
//         "x-api-key": apiKey,
//       },
//       body: JSON.stringify(payload),
//     });
//     if ((res.status === 401 || res.status === 404) && !retried) {
//       cachedSessionUrl = null;             // session expired → re-mint once
//       return callUpstream(apiKey, payload, true);
//     }
//     const text = await res.text();         // <-- await the text, not .body
//     if (!res.ok) throw new Error(`upstream ${res.status}: ${text.slice(0, 300)}`);
//     return parseUpstream(text);
//   }
//
//   // In handleRpc: tools/list → getTools(apiKey) (cache upstream tools/list);
//   // tools/call → callUpstream(apiKey, {jsonrpc, id, method:"tools/call", params}).
//   // Read the server key from process.env inside the POST handler:
//   //   const apiKey = process.env.UPSTREAM_API_KEY; (use mcp__zo__run_bash for secrets)
//
// ===========================================================================
// VARIANT B — direct
// ---------------------------------------------------------------------------
// Implement the tool inline. Two common shapes:
//
//   // (1) shell out to a local CLI (cora pattern):
//   import { promisify } from "node:util";
//   import { exec as _exec } from "node:child_process";
//   const exec = promisify(_exec);
//   async function callTool(name, args) {
//     // build an argv string with single-quote escaping; never interpolate raw
//     const safe = (s: string) => `'${String(s).replace(/'/g, `'\\''`)}'`;
//     const { stdout } = await exec(`/path/to/cli ${name} ${safe(args.q)} --format json`);
//     return JSON.parse(stdout);
//   }
//
//   // (2) fetch an external API with a server-side key (key never leaves Zo):
//   async function callTool(name, args) {
//     const res = await fetch(`https://api.example.com/${name}`, {
//       method: "POST",
//       headers: { Authorization: `Bearer ${process.env.EXAMPLE_API_KEY}` },
//       body: JSON.stringify(args),
//     });
//     return res.json();
//   }
// ===========================================================================
