#!/usr/bin/env bash
# Post-deploy verifier for an MCP wrapper on paviproczko.zo.space.
#
#   bash smoke-test.sh <slug> [oauth|standard] [probe-tool-name] [probe-json-args]
#
#   <slug>              full path slug, e.g. memory-mcp-velvet-anchor-drifts
#   oauth|standard      verify .well-known pointers (oauth, default) or skip (standard)
#   probe-tool-name     optional: a tool to exercise via tools/call
#   probe-json-args     optional: JSON args for the probe tool (default {})
#
# Exits non-zero if any required check fails. ALL checks must pass before
# reporting success to Pavi.

set -uo pipefail

SLUG="${1:-}"
MODE="${2:-oauth}"
PROBE_TOOL="${3:-}"
PROBE_ARGS="${4:-{}}"

if [[ -z "$SLUG" ]]; then
  echo "usage: bash smoke-test.sh <slug> [oauth|standard] [probe-tool] [probe-json-args]" >&2
  exit 1
fi

BASE="https://paviproczko.zo.space"
URL="$BASE/$SLUG"
fail=0

pass() { echo "  PASS  $1"; }
bad()  { echo "  FAIL  $1"; fail=1; }

jq_ok() { command -v jq >/dev/null 2>&1; }

echo
echo "Smoke testing $URL  (mode: $MODE)"
echo

# --- 1. tools/list ---------------------------------------------------------
LIST=$(curl -s -X POST "$URL" -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}')
if jq_ok; then
  COUNT=$(echo "$LIST" | jq '.result.tools | length' 2>/dev/null)
else
  COUNT=$(echo "$LIST" | grep -o '"name"' | wc -l | tr -d ' ')
fi
if [[ "${COUNT:-0}" =~ ^[0-9]+$ && "${COUNT:-0}" -gt 0 ]]; then
  pass "tools/list returned $COUNT tool(s)"
else
  bad "tools/list returned no tools — body: ${LIST:0:200}"
fi

# --- 2. initialize ---------------------------------------------------------
INIT=$(curl -s -X POST "$URL" -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}')
if echo "$INIT" | grep -q '"serverInfo"'; then
  pass "initialize returned serverInfo"
else
  bad "initialize did not return serverInfo — body: ${INIT:0:200}"
fi

# --- 3. optional probe tools/call -----------------------------------------
if [[ -n "$PROBE_TOOL" ]]; then
  CALL=$(curl -s -X POST "$URL" -H 'content-type: application/json' \
    -d "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/call\",\"params\":{\"name\":\"$PROBE_TOOL\",\"arguments\":$PROBE_ARGS}}")
  if echo "$CALL" | grep -q '"content"'; then
    pass "tools/call $PROBE_TOOL returned content"
  else
    bad "tools/call $PROBE_TOOL failed — body: ${CALL:0:200}"
  fi
fi

# --- 4. oauth .well-known checks ------------------------------------------
if [[ "$MODE" == "oauth" ]]; then
  V1=$(curl -s "$URL/.well-known/oauth-protected-resource")
  if echo "$V1" | grep -q '"authorization_servers"'; then
    pass "root .well-known variant present (/<slug>/.well-known/...)"
  else
    bad "root .well-known variant missing — body: ${V1:0:200}"
  fi

  V2=$(curl -s "$BASE/.well-known/oauth-protected-resource/$SLUG")
  if echo "$V2" | grep -q '"authorization_servers"'; then
    pass "path .well-known variant present (/.well-known/.../<slug>)"
  else
    bad "path .well-known variant missing — body: ${V2:0:200}"
  fi

  AS=$(curl -s "$BASE/.well-known/oauth-authorization-server")
  if echo "$AS" | grep -q '"registration_endpoint"'; then
    pass "shared auth-server metadata present"
  else
    bad "shared auth-server metadata missing — body: ${AS:0:200}"
  fi
else
  echo "  SKIP  .well-known checks (standard mode)"
fi

echo
if [[ "$fail" -eq 0 ]]; then
  echo "All checks passed."
else
  echo "One or more checks FAILED — see references/troubleshooting.md before reporting success."
fi
exit "$fail"
