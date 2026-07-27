# miscellaneous

The catch-all plugin. Four standalone skills that earn their keep but don't
belong to any single domain plugin — they were previously loose in the repo's
root `skills/` folder, which meant they never installed from the marketplace.
Bundling them here makes them installable without forcing an artificial home
inside `audiobook-production`, `daily-ops`, or `creative-writing`.

## Skills

| Skill | What it does |
|-------|--------------|
| `business-documentation` | Generates brand-consistent Pavitas Productions business documents — invoices, contracts — with the logo set, brand colors, and standard company/payment details. |
| `cora-email` | Drives the Cora AI email assistant through its CLI: daily briefs, email todos, inbox triage, reply drafting, and chat. |
| `mcp-wrapper-builder` | Builds and deploys new MCP server wrappers on `paviproczko.zo.space` so external tools (Perplexity, Claude.ai, Little Bird) can reach a Zo-mediated service. Covers slug generation, the JSON-RPC scaffold, the OAuth shim, smoke testing, and post-deploy troubleshooting. |
| `relational-emotional-regulation` | A structured thinking partner for relational conflict, real-time regulation, and prep for hard conversations. Explicitly not a substitute for therapy. |

## Connectors

None. This plugin ships no `.mcp.json` — `cora-email` works through the `cora`
CLI, `mcp-wrapper-builder` operates Zo through the Zo Computer MCP proxy
(configured at the client level, not per-plugin), and the other two skills need
no external service.

## Install

```
/plugin install miscellaneous@pavitas-plugins
```

## Notes

`business-documentation` carries eight logo PNGs (badge and wordmark, each in
black / white / color / color-on-background). Keep them alongside `SKILL.md` —
the skill references them by relative path.

`mcp-wrapper-builder` keeps its `references/` (JSON-RPC scaffold, OAuth shim
notes, troubleshooting) and `scripts/` (`gen-slugs.ts`, `smoke-test.sh`)
subdirectories. Same rule: relative paths from `SKILL.md`.
