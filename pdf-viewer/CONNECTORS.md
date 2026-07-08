# Connectors

## Local MCP Server

This plugin uses a **local MCP server** instead of a remote connector.
The PDF server runs on your machine via `npx`.

| Category | Server | How it runs |
|----------|--------|-------------|
| PDF viewer & annotator | `@modelcontextprotocol/server-pdf` | Local stdio via `npx` (auto-installed) |

### Requirements
- Node.js >= 18
- Internet access only if you open a remote HTTPS PDF (local script and
  contract files need no network)
- No API keys or authentication needed
