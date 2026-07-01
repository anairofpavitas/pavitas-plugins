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
              content-pipeline             → two-brand social drafting
              infra-session                → Zo / MCP / repo work
LEAVES        (unchanged, loaded on demand) business-documentation,
              publisher-profiles, writing-workshop ×4, brand voices ×2,
              decision-framework (patched), handoff (trimmed),
              relational-emotional-regulation, mcp-wrapper-builder,
              autoresearch, proof, using-slashy (Slashy mechanics,
              loaded by slashy-ops plugin)
```

Layering rules: constraints never contain procedures; orchestrators never contain execution detail (they name leaves); leaves never route. Facts (IDs, paths) live in `pavitas-core:workspace-context` only — nothing else hard-codes them.

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
- [ ] Exactly one brand voice loaded; correct brand for subject
- [ ] Zero AI-narration content
- [ ] Draft reviewed before any posting step
- [ ] Platform-fit pass completed

**infra-session**
- [ ] Routing correct (Slashy not Gmail; Composio Notion for DBs; Zo proxy for files)
- [ ] Destructive ops previewed
- [ ] Changelog entry written (correct file)
- [ ] Smoke test run and results stated; handoff written if mid-task
