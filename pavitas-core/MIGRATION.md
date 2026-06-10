# MIGRATION

Order matters. Each step is independently safe.

## 0. Packaging (changed 2026-06-10)

The 12 new/changed skills now ship as ONE plugin: `pavitas-core` (`.claude-plugin/plugin.json` + `skills/`). Install/update is per-plugin, not per-skill. Bundled skills are referenced as `pavitas-core:<name>`; references to skills outside the bundle (audiobook leaves, hunts, writing-workshop, brand voices, etc.) are unchanged. Repo placement: add the `pavitas-core/` directory following the repo's existing plugin layout and register it in the marketplace manifest, matching the pattern of the existing plugin entries (writing-workshop, pavitas-content, etc.). The standalone Claude.ai copies of handoff, decision-framework, proof, zo-workspace-orientation, design-elevation, humanize-prose, and daily-briefing must be REMOVED once pavitas-core is installed — otherwise the old and namespaced versions both load.

## 1. Deletions (Claude.ai skill settings + repo)

- `enterprise-search` plugin (all three skills) — re-teaches default behavior, 650 lines. If you actually use it, say so and we'll collapse it to one ~60-line skill instead.
- Duplicate loader entries: `enterprise-search:*` and `writing-workshop:*` each appear twice in the loaded skill list. Remove the duplicate plugin install.

## 2. Replacements (upload from this drop, remove the old)

| New | Replaces | Notes |
|---|---|---|
| `pavitas-core:skill-router` | — (new) | Upload first; everything else assumes it |
| `pavitas-core:safety-rails` | — (new) | Extracted from userMemories + zo-orientation |
| `pavitas-core:workspace-context` | `zo-workspace-orientation` | 165→~60 always-on lines; Zo skill index moved to references/. **Verify domain: written as `paviproczko.zo.space`; old skill said `.zo.computer`** |
| `pavitas-core:output-quality` | `design-elevation` + `humanize-prose` | design-elevation's 5 reference files carried over; full prose rules preserved in `references/prose-rules.md` |
| `pavitas-core:morning-review` | `daily-briefing` | 712→~70 lines. Email triage subsystem deleted — Cora owns it. Tantor/Dreamscape dropped from any VIP context (never clients) |
| `pavitas-core:handoff` | `pavitas-core:handoff` (old) | 383→~80 lines, behavior preserved |
| `pavitas-core:decision-framework` | `pavitas-core:decision-framework` (old) | Same skill, Gmail references patched to Superhuman |
| `pavitas-core:audiobook-kickoff`, `pavitas-core:story-session`, `pavitas-core:content-pipeline`, `pavitas-core:infra-session` | — (new) | Orchestrators |

## 3. Keep as-is (no action)

audiobook-script-analyzer · audiobook-project-setup · business-documentation · publisher-relations:publisher-profiles · writing-workshop ×4 · pavitas-brand-voice · spins-yarns-brand-voice · scavenger-hunt-designer · pocket-hunt · pleasure-hunt · relational-emotional-regulation · mcp-wrapper-builder · autoresearch · proof — KEEP (vendor-provided by Proof Editor AI). Patched copy in this drop: frontmatter description tightened + disambiguation note added so it can't fire on "proofread"/"proof this". Body untouched for clean vendor diffs

**Audit correction:** the hunt merge proposed in the audit is REVERSED. The three hunt skills are distinct systems (event design / live presence-anchoring / upfront intimate play) with separate principles and reference libraries. Merging them would have built a monolith. The router disambiguates the triggers instead.

## 4. Zo-side dedupe (separate session — infra-session profile)

Zo's `/home/workspace/Skills` has divergent copies of: `daily-briefing`, `pavitas-core:decision-framework`, `business-documentation`, `prose-humanizer` (≈humanize-prose), `design-elevation`. Replace each with either the canonical version from this repo or a pointer stub ("superseded — see pavitas-plugins"). Also update Zo's `AGENTS.md` routing table to drop the superseded entries.

## 5. Resolved decisions (2026-06-10)

- Notion routing: Composio primary (notably better for search), native Notion MCP fallback. Confirmed.
- `pavitas-core:proof`: kept, trigger-patched (see §3). Vendor body unmodified.
- Domain: `paviproczko.zo.space` confirmed live via the Claude.ai connector registration; `.zo.computer` was stale.
