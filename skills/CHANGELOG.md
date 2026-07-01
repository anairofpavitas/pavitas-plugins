# Changelog — Skills

All notable changes to pavitas-plugins **skills** are documented here.
Plugins have their own changelog at `CHANGELOG.md` (repo root).

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Version numbers are independent from the plugins version sequence.

Skills change frequently — additions, refinements after real-world use,
reference file updates, and debrief-driven edits all get logged here.

---

## [Unreleased]

### Changed
- **morning-briefing, eod-wrapup, batch-draft-writer, meeting-scheduler,
  deal-tracker** — relocated from standalone `skills/` to the new
  `slashy-ops` plugin (see root `CHANGELOG.md`) so they update as one
  plugin install rather than five separate uploads. Content unchanged
  except internal cross-references now namespaced (e.g.
  `slashy-ops:batch-draft-writer`).

---

## [2026-06-30] Superhuman → Slashy migration — skill layer

### Added
- **pavitas-core:using-slashy** — New shared Slashy MCP reference skill. Single source of truth for `inbox_email` requirement, `list_messages` query syntax, `draft_email` literal-HTML-body constraint, `send_email` approval/no-undo behavior, `create_event`/`update_event` split, `get_available_times` param shape, per-thread `read_thread(include_tracking=true)` pattern (no bulk read-receipt feed in Slashy), `label_email` action map, and Slashy deep links. Added to skill-router coverage manifest. Email skills reference this instead of re-deriving mechanics.
- **morning-briefing** — Email-first morning intelligence using Slashy. Three `list_messages` inbox passes (unread, starred, todo:reply) + calendar events in parallel; `read_thread` per VIP or flagged thread; Claude synthesizes email + calendar directly (no `query_email_and_calendar` equivalent in Slashy). References `pavitas-core:using-slashy`.
- **eod-wrapup** — End-of-day email and calendar wrap using Slashy. Today's email passes + tomorrow calendar preview + Littlebird Log comparison; `read_thread` for follow-up threads; `label_email(action="archive")` for confirmed-done threads. References `pavitas-core:using-slashy`.
- **batch-draft-writer** — Batch email drafting using Slashy. Write-review-save loop, one draft at a time. Literal HTML body required — no `instructions` delegation (Slashy has no AI-writer field); voice fidelity comes from `pavitas-core:output-quality`. Send is a separate explicit step with no undo window. References `pavitas-core:using-slashy`.
- **meeting-scheduler** — End-to-end meeting scheduling using Slashy. `get_available_times` with corrected param shape (`emails`, `min_duration_minutes`, `business_hours_only`, `display_timezone`). Branches on `create_event` vs. `update_event` based on whether `event_id` is known (Slashy splits Superhuman's single `create_or_update_event`). Optional confirmation email via `draft_email` + explicit `send_email`. References `pavitas-core:using-slashy`.
- **deal-tracker** — Email-based deal and relationship tracker using Slashy. Three `list_messages` passes (starred, followup, important); `read_thread` per deal thread; per-thread `read_thread(include_tracking=true)` loop for open-tracking data (N calls, not one — no bulk feed in Slashy). Fixes pre-existing bug: `Superhuman_Mail.get_read_statuses` was never a real tool name; rewritten as per-thread tracking loop. References `pavitas-core:using-slashy`.

### Changed
- **pavitas-core:workspace-context** — Email routing table updated: both rows (reading/search and drafting/sending) now point to Slashy tools with `pavitas-core:using-slashy` for mechanics. Gmail MCP ban carried over unchanged — that constraint is about Gmail's HTML-drop bug, not Superhuman-specific.
- **pavitas-core:skill-router** — Coverage manifest updated: `using-slashy` added to pavitas-core (13 total); five email-ops skills added to User skills (14 total). Five routing entries added to dispatch table.
- **pavitas-core:decision-framework** — Two Superhuman MCP references updated to Slashy `list_messages`/`read_thread` in the evidence-gathering sections (~line 74, ~lines 129–132). Reference/advisory text only — framework behavior unchanged.

### Notes
- The five leaf skills (morning-briefing, eod-wrapup, batch-draft-writer, meeting-scheduler, deal-tracker) are new additions to this repo. Their prior Superhuman versions existed only in Claude.ai's `/mnt/skills/user` storage (user-uploaded, not GitHub-backed). These GitHub-tracked Slashy-native versions should be installed to replace those uploads.
- Infrastructure layer (Zo automations, Zo rules, Connections-Index.md) was fully migrated in a prior session — this change covers the skill layer only.
- Smoke test: Slashy MCP is available in this environment (`mcp__Slashy__*` tools present). Full trigger-test of all 7 files should run in a Claude.ai Web session where Pavi can review live inbox/calendar results before trusting the skills in production.

---

## [2026-06-10] skills-v2 refactor — shipped as pavitas-core plugin v2.0.0

### Added
- pavitas-core plugin packaging (.claude-plugin/plugin.json); bundled skills namespaced as pavitas-core:<name>
- skill-router (meta: goal → load-set dispatch)
- safety-rails, workspace-context, output-quality (constraint layer)
- audiobook-kickoff, story-session, content-pipeline, infra-session (orchestrators)

### Changed
- daily-briefing → morning-review (712→~70 lines; email triage delegated to Cora)
- handoff trimmed 383→~80 lines, behavior preserved; universal handoff-offer rule added to safety-rails (substantive multi-step sessions)
- decision-framework: Gmail references patched to Superhuman
- zo-workspace-orientation → workspace-context (+ references/zo-skill-index.md)
- design-elevation + humanize-prose → output-quality (+ references preserved)

### Removed
- enterprise-search ×3 (re-taught default behavior)
- Duplicate plugin loader entries (enterprise-search, writing-workshop)

### Reversed from audit
- Hunt-family merge cancelled: three skills are distinct systems; router disambiguates instead.

---

## [1.4.0] — 2026-06-03

### Added
- **mcp-wrapper-builder** — Claude-side port of the Zo-native skill for
  standing up new MCP server wrappers on paviproczko.zo.space. Runs from
  claude.ai chat, operating Zo through the Zo Computer MCP proxy (Claude
  reasons; Zo executes mechanically — no second AI, never routed through
  `ask_zo`). Two avenues: OAuth-shim-backed (default, Perplexity-compatible)
  and standard URL-only. Retargets the execution layer from Zo-native calls
  to `Zo Computer:*` proxy tools, with a deferred-tool preflight (tool_search
  + schema verification) and an explicit two-wall model: Zo Secrets are
  invisible to Claude and Claude's container is firewalled from zo.space, so
  all site/secret/file actions route through the proxy, never Claude's local
  bash. Slug generation done inline (gen-slugs.ts kept as the canonical word
  list); smoke-test.sh materialized-if-absent onto Zo and run via
  `Zo Computer:bash`. Doc/memory updates (MCP-Proxies.md, Connections-Index.md,
  project_mcp_proxy.md) via proxy file tools plus a Supermemory save step.
  Scaffold fix: `initialize` now echoes the client's requested
  protocolVersion, falling back to the 2024-11-05 constant — affects only new
  builds, existing proxies untouched. SKILL.md + 3 reference files
  (json-rpc-scaffold, oauth-shim, troubleshooting) + 2 scripts (gen-slugs,
  smoke-test).

---

## [1.3.0] — 2026-05-17

### Changed
- **pocket-hunt** — Refinement release merging improvements developed with
  the skill in Perplexity back into the canonical version. Trigger
  description expanded with explicit phrases ("pocket hunt", "quick hunt",
  "noticing walk", "start a hunt", "let's hunt", "take me on a walk") so the
  skill fires more reliably. The end-of-hunt feedback loop now classifies
  into three buckets instead of two — this-hunt only / forever preference
  (memory) / skill update (file edit) — with durable taste preferences saved
  to Supermemory rather than forcing a file edit. New explicit rule that
  seed prompts always precede clues and are never baked into clue 1; the
  hunt flow is reordered so summary/confirmation happens before seeds. Adds
  a Tooling section mapping each hunt beat to a Claude-native tool
  (WebSearch, WebFetch, Claude in Chrome, Supermemory, canvas-design,
  pdf/docx, scheduled-tasks). rungs.md: rung 4 (combinatorial) now reminds
  Claude to keep a running role tally in chat between clue stretches.

---

## [1.2.0] — 2026-05-17

### Added
- **pleasure-hunt** — Miniaturized intimate scavenger hunt skill for sexual
  pleasure, intimacy, and exploration, built for gay men. Companion to
  pocket-hunt and scavenger-hunt-designer; lightweight like the former but
  generated entirely upfront like the latter's pre-built mode. Four modes
  (solo / partner / group / cruising), four boundary tiers (low / medium /
  high / extreme), include/exclude/dealer's-choice equipment handling, a
  user-named-or-Claude-suggested activity option, a three-beat escalation
  arc with an optional elegant-exit beat, optional timer-paced clues, and
  discreet dating-app integration. Three foundational principles: the user
  holds the controls, consent and enthusiasm are the engine, and discretion
  and safety woven in without preaching. Includes a living long-horizon goal
  ledger (practices to deepen, not a checklist). SKILL.md + 5 reference files
  (boundary-tiers, equipment, long-horizon-goals, hunt-modes, clue-patterns).

---

## [1.1.0] — 2026-05-11

### Added
- **pocket-hunt** — Lightweight on-the-go scavenger hunt skill for presence
  anchoring during walks, bike rides, or travel. Companion skill to
  scavenger-hunt-designer but designed for live, in-the-moment use. Four
  commitment rungs (notice / capture / single-find / combinatorial), three
  hunt shapes (open exploration / travel hunt / destination-with-delivery),
  companion support for humans and dogs, parallel-activity integration
  (crochet, journal, sketchbook), environment-aware design (shop-rich /
  shop-sparse / foraging-friendly), and an extensible side-quest catalog.
  Three foundational principles: phone-away between pings, override anywhere
  anytime, and a structured end-of-hunt feedback loop with classification at
  debrief only. SKILL.md + 7 reference files (rungs, seed-prompts,
  companion-integration, environment-context, parallel-activity, hunt-shapes,
  side-quests).

---

## [1.0.0] — 2026-05-11

### Added
- Skills folder formally versioned.
- **scavenger-hunt-designer** — Designs walking scavenger hunts for small
  groups where players come home with stuff. Conversational intake,
  neighborhood/weather/date research, three-beat structure, two-stage clues,
  mode-aware design with project × mode pairings, and dual delivery modes
  (live turn-by-turn vs pre-built self-contained markdown). SKILL.md + 4
  reference files (clue-patterns, project-roles, delivery-live,
  delivery-prebuilt).
- **cora-email** — Wraps the `cora` CLI for AI-powered email assistance.
  Covers checking briefs, managing todos, drafting replies, and chatting with
  Cora's AI assistant. Triggers on questions about email, inbox, briefs, or
  email todos.

---

## [0.1.0] — [DATE — fill in: first commit date of the skills folder]

### Added
- Skills folder established. Nine skills added before formal versioning:
- **audiobook-project-setup** — Creates standardized folder hierarchy for new
  audiobook projects (Assets, Chapters, CRX subfolders).
- **audiobook-script-analyzer** — Analyzes audiobook script PDFs or Word
  documents to extract chapter structure, word counts, and page counts.
  Supports chapter breakdowns, file naming conventions, and Notion project
  creation.
- **business-documentation** — Generates invoices, contracts, and other
  business documents for Pavitas Productions with brand-consistent design.
- **daily-briefing** — Comprehensive morning briefing combining calendar,
  email, production status, tasks, and personal check-ins. Three-phase
  interactive process using the 3-3-3 method. Saves to Notion Littlebird Log.
- **decision-framework** — Structured decision-making using frameworks that
  challenge narratives with evidence. Covers time audits, cooling-off
  protocols, incremental value analysis, and pre-commitment post-mortems.
- **design-elevation** — Applies professional design thinking to all visual
  outputs. Activates whenever Claude creates presentations, spreadsheets,
  HTML artifacts, PDFs, or documents.
- **handoff** — Manages session handoffs between claude.ai and Claude Code
  using Notion Littlebird Log. Autonomously analyzes conversation to compose
  handoff notes.
- **humanize-prose** — Applies anti-AI writing rules to strip generated-
  sounding patterns and produce human-quality reflective, personal, or
  essay-style writing.
- **relational-emotional-regulation** — Structured thinking partner for
  processing relational conflicts, regulating during emotional dysregulation,
  and preparing for hard conversations.

2026-06-10 — skills-v2.1: full-ecosystem audit addendum. Removed writing-workshop (story-session now self-contained: interview + style-matching inlined, nudge dropped). Removed publisher-relations:publisher-profiles and all stored publisher/client data (business-documentation client profiles deleted; ACX delivery specs moved to workspace-context). skill-router gains a coverage manifest — every installed skill must have a routing home; audits diff against it. audiobook-kickoff genericized to "client", folder step notes audiobook-project-setup is Cowork-native. spins-yarns-brand-voice: Threads removed (Instagram only), stale fiber-arts-content reference removed. mcp-wrapper-builder metadata domain corrected to zo.space. Pending next session: merge fiber-arts-content into spins-yarns-content, then update the manifest and content-pipeline reference.

2026-06-10 — fiber-arts-content merge follow-up (Web): skill-router coverage manifest updated — "Pending" merge line resolved; fiber-arts-content added to "Removed — never reference." content-pipeline verified unchanged: its voice reference (spins-yarns-content:spins-yarns-brand-voice) keeps the same namespace after the merge, so no edit was needed.
