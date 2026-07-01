# hunt-skills

Three scavenger-hunt skills bundled so they install and update as one plugin instead of three
separate uploads. Loads as `hunt-skills:<name>`.

## Skills

| Skill | What it does |
|---|---|
| `hunt-skills:scavenger-hunt-designer` | Event-style walking hunts for small groups — date walks, group adventures, couples outings — where players come home with stuff. Live or pre-built delivery. |
| `hunt-skills:pocket-hunt` | Lightweight, turn-by-turn hunts for in-the-moment presence anchoring on a walk, bike, or trip — solo, with companions, or with dogs. |
| `hunt-skills:pleasure-hunt` | Compact, upfront intimate hunts for sexual pleasure, intimacy, and exploration — solo, with a partner, with a group, or cruising. Built for gay men. |

## Why these three are bundled, not merged

Each is a distinct system with its own intake, structure, and delivery model — a prior audit
considered merging them into one skill and reversed that decision (see `skills/CHANGELOG.md`,
2026-06-10 entry: "Hunt-family merge cancelled: three skills are distinct systems; router
disambiguates instead"). Bundling as one plugin only changes how they ship and update; each
skill's frontmatter `description` still does the disambiguation work so the right one loads
for "pocket hunt" vs. "scavenger hunt" vs. "pleasure hunt" requests. `pocket-hunt` and
`pleasure-hunt` cross-reference `scavenger-hunt-designer` (and each other) by namespaced name
for tone-matching and distinctness callouts.

## Connectors

None bundled — each skill uses whatever `WebSearch`/`WebFetch` and file tools the session
already has for light research (weather, neighborhood shops, local events) and optional
closing artifacts. No `.mcp.json`.

## No agents

Skill-only plugin, no `agents/` or `commands/`. All three skills are designed to run live,
in the main conversation, with the user in the loop turn-by-turn (`pocket-hunt`) or as a
single upfront generation the user takes and runs themselves (`scavenger-hunt-designer`
pre-built mode, `pleasure-hunt`). None of them do the kind of multi-source data-gathering or
isolated-context evaluation that would justify a sub-agent hop, and two of them are explicit
about minimizing friction and latency — a sub-agent round trip would work against that.
