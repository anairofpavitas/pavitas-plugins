# pavitas-core — Pavitas Skill Ecosystem (Claude.ai layer)

Ships as a single plugin (v2.0.0). Bundled skills load as `pavitas-core:<name>`.

Refactored 2026-06-10 per the skills audit; plugin-packaged same day. Canon lives in `anairofpavitas/pavitas-plugins`; every other agent pulls from here.

## Architecture

```
META          skill-router                 → goal → load-set dispatch
CONSTRAINTS   safety-rails                 → conduct rules (always-on)
              workspace-context            → IDs, routing, facts (always-on)
              output-quality               → prose + visual standards (always-on)
ORCHESTRATORS morning-review               → replaces daily-briefing
              audiobook-kickoff            → new-project intake chain
              story-session                → fiction work, Story Grid
              content-pipeline             → two-brand social routing
              infra-session                → Zo / MCP / repo work
LEAVES        (unchanged, loaded on demand) business-documentation,
              publisher-profiles, writing-workshop ×4, brand voices ×2,
              decision-framework (patched), handoff (trimmed),
              relational-emotional-regulation, mcp-wrapper-builder,
              autoresearch, proof, using-slashy (Slashy mechanics,
              loaded by slashy-ops plugin)
```

Layering rules: constraints never contain procedures; orchestrators never contain execution detail (they name leaves); leaves never route. Facts (IDs, paths) live in `pavitas-core:workspace-context` only — nothing else hard-codes them.

## Hooks: shared agent log with Zo (added 2026-10-22)

`hooks/hooks.json` runs `hooks/agent_log.py` in every Claude Code session on any machine with this plugin enabled.

- **SessionStart** (new, resumed, or cleared session): prints Zo's briefing of the last 24 hours across every machine and agent (agent sessions, what Ambient heard, the longest Activity Journal stretches, yesterday's digest). Claude Code adds it to the session's context. Times out quietly after about 6 seconds if Zo is slow. It also starts a background catch-up that sends any earlier session on this machine that ended without the SessionEnd hook (crash, closed terminal).
- **SessionEnd**: returns at once and, in a detached background process, sends Zo a trimmed copy of the session (prompts, reply openings and endings, files changed; tool output left out; secret-looking strings redacted). Zo has Claude Haiku write a 1–3 sentence entry with decisions and open threads, stores only that entry in `journal.db` → `agent_sessions`, and discards the text.
- **Setup per machine (once):** `python3 ~/.claude/plugins/marketplaces/pavitas-plugins/pavitas-core/hooks/agent_log.py setup`. It asks for the Zo agent token (kept on Zo at `Projects/agent-log/.agent-token`) and the machine name (`office-macbook`, `studio-macbook`, matching the Activity Journal), saves them in `~/.config/pavitas/` with owner-only permissions, and tests the connection. Never commit the token.
- **Check:** `python3 …/agent_log.py status`. In a session, `/hooks` lists both hooks with source "plugin".
- **Off switch:** `export PAVITAS_AGENT_LOG=0` for one shell or script, or `"disableAllHooks": true` in `~/.claude/settings.json` for everything.
- **No token:** the hooks print one line saying the log isn't set up and send nothing except an anonymous "a hook ran" ping to Zo (`/api/context/agent-ping`). In cloud sessions (Cowork, Claude Code on the web) there is deliberately no token; those read the briefing through the Zo connector instead (`python3 /home/workspace/Projects/agent-log/zo_agent.py now`).
- Zo's own chats aren't hooked; Zo's nightly job logs them and writes the daily digest. Details: `Projects/agent-log/README.md` on Zo.

## Evaluation rubrics (run via autoresearch, quarterly)

**morning-review**
- [ ] Email sourced from Cora brief; zero direct inbox calls
- [ ] Four calendars pulled, today+tomorrow only
- [ ] 3-3-3 present; ≥1 non-production item surfaced
- [ ] Presented in chat before any Notion write; published only on explicit OK
- [ ] Littlebird entry uses canonical DB ID; Notes section at top; America/Chicago dates

**audiobook-kickoff**
- [ ] Word counts match script on a 3-chapter spot check
- [ ] Front/back matter excluded from PFH math
- [ ] Folder tree matches audiobook-production:audiobook-project-setup spec
- [ ] Notion chapter count = analysis chapter count; relation property set
- [ ] No fabricated metadata; gaps flagged with ⚠️

**story-session**
- [ ] Story Grid terminology throughout
- [ ] Style profile loaded/created before any prose compilation
- [ ] Output passes prose-rules spot read
- [ ] Session state updated at close

**content-pipeline**
- [ ] Exactly one brand loaded; correct brand for subject
- [ ] Pavitas → topic slate, verified, zero copy; spins-yarns → draft
- [ ] Slate or draft reviewed before any posting step
- [ ] Platform-fit pass completed (spins-yarns drafts only)

**infra-session**
- [ ] Routing correct (Slashy not Gmail; Composio Notion for DBs; Zo proxy for files)
- [ ] Destructive ops previewed
- [ ] Changelog entry written (correct file)
- [ ] Smoke test run and results stated; handoff written if mid-task
