# Changelog — Plugins

All notable changes to pavitas-plugins **plugins** are documented here.
Skills have their own changelog at [`CHANGELOG-skills.md`](./CHANGELOG-skills.md).

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Version numbers are independent from the skills version sequence.

---

## [1.11.0] — 2026-07-29

### Changed
- **`pavitas-content` no longer writes copy.** `/pavitas-content:weekly` produced
  finished drafts — hooks, captions, alt text, hashtags, a 1.5-second video hook,
  numbered beats, on-screen text callouts. A human professional now owns all of
  that. The command was rewritten as an angle brief: it surfaces what's worth
  writing about and hands over the verified material behind each angle. Phase 3
  went from "Draft" to "Build the angle brief," and every copy artifact was cut.
  A hard rule was added at the bottom — if the output contains a hook, caption,
  hashtag, or script line, the run is wrong. Without an explicit stop, a model
  reading the old instructions drifts back toward drafting.
- **No fixed angle count.** The command picked exactly two distinct angles and
  paired them to formats (release → carousel, craft reflection → short-form
  video). It now picks every angle that clears the quality gate, with no target
  number, and prescribes no format or platform. The angle-pairing logic was
  format-driven, so it went with the formats.
- **Notion output restructured.** Columns were all copy artifacts:
  `Content Type | Platforms | Hook | Body | Visual/Video Brief | Hashtags |
  Notes for SM Manager | Visual Assets`. Now:
  `Angle | Tier | Why now | Source material | Constraints & credits | Confidence`.
  `Source material` carries the facts a writer can't derive alone; `Constraints
  & credits` is the old SM-manager column doing factual work (embargoes, required
  tags, handles); `Confidence` flags anything unverified. Page title changed from
  `Pavitas Content Generation [YYYY-MM-DD]` to `Pavitas Angle Brief [YYYY-MM-DD]`.
- **AI is greenlit as a topic.** The ban on mentioning AI narration in any form
  was removed from the command's Phase 3, its hard rules, the plugin README, and
  the `pavitas-brand-voice` skill's topic list. AI angles now compete on the same
  hierarchy as everything else. No stance guidance is supplied — Pavi or his
  writer supplies it.
- **Brand-voice phrase bans no longer bind `/weekly`.** The banned-phrase list
  (`journey`, `passion project`, `delve`) is copy territory. The skill still
  loads, but scoped to judging whether an angle is on-brand. The list stays
  intact in `pavitas-brand-voice` for the commands that do still draft.
- `pavitas-content` bumped to 1.1.0; marketplace description updated.

### Note
- `pavitas-brand-voice` still carries format specs and a "two strong pieces"
  quality line, both now stale for `/weekly` but live for `content-pipeline` and
  `/spins-yarns-content:post`. Left in place deliberately.

---

## [1.10.0] — 2026-07-27

### Fixed
- **Four plugins were invisible in the marketplace.** `audiobook-production`,
  `daily-ops`, `creative-writing`, and `spins-yarns-content` each declared their
  MCP servers with `"type": "url"` — not a valid server type (`stdio`, `http`,
  `sse`, `ws` are). The invalid type made each plugin fail to load, so it never
  reached the marketplace listing and never showed up on install. Only 8 of the
  12 plugins were actually reachable. Changed all nine server entries across the
  four files to `"type": "http"`, matching `productivity`'s working config. The
  correlation was exact: every plugin with a valid `.mcp.json` (or none at all)
  loaded; every plugin with `"type": "url"` did not.
- Removed the non-schema `"note"` field from all nine of those server entries —
  a second, independent failure mode sitting in the same files. The information
  wasn't dropped: each note's content now lives in that plugin's README
  `## Connectors` section. Three of the four READMEs had been carrying abridged
  versions of these notes, so this also restored detail that had drifted
  (`audiobook-production`: Littlebird Log, delivery confirmations, script
  storage; `daily-ops`: the four calendar names, VIP monitoring, Littlebird
  Database; `spins-yarns-content`: Perplexity crochet trends as a `/weekly` input).
- **pavitas-core:memory-recall** — SKILL.md frontmatter was not valid YAML. The
  `description:` value wrapped across four lines with no continuation indent, so
  a parser read line 2 as a new key and failed the whole block. Converted to a
  `>-` folded scalar; description text unchanged. Caught by the repo-wide
  frontmatter check added for this release.

### Added
- **miscellaneous** v1.0.0 — new plugin, thirteenth in the marketplace. Four
  skills had been sitting loose in the repo's root `skills/` folder, which meant
  they were readable in the repo but never installed from the marketplace:
  `business-documentation` (with its 8 brand logo PNGs),
  `cora-email`, `mcp-wrapper-builder` (with its `references/` and `scripts/`
  subdirectories), and `relational-emotional-regulation`. Moved into
  `miscellaneous/skills/` via `git mv` so history follows them. No `.mcp.json` —
  `cora-email` drives a CLI, `mcp-wrapper-builder` works through the Zo Computer
  proxy configured at the client level, and the other two need no external
  service.

### Changed
- Marketplace manifest bumped 1.9.0 → 1.10.0 (new plugin; the bump also busts
  any cached copy of the old manifest) and the `miscellaneous` entry appended to
  `plugins`, bringing the array to 13.
- Root cleanup: `skills/CHANGELOG.md` → `CHANGELOG-skills.md` at the repo root,
  with its header rewritten so the cross-link to `CHANGELOG.md` still resolves
  from the new location. Eight stale `skills/CHANGELOG.md` references across
  README.md, `hunt-skills/README.md`, `slashy-ops/README.md`, and two
  `pavitas-core` skills were repointed. The now-empty `skills/` directory was
  deleted, as was `commands/`, which held only an empty `README` and no commands.
- Root README: added a `miscellaneous` entry to the plugin overview, and
  rewrote the "Shared Skills (repo `skills/` folder)" section — it described a
  folder that no longer exists — into a redirect table pointing the four moved
  skills at their new `miscellaneous:<name>` addresses.

---

## [Unreleased]

### Added
- **xcode-skills** v1.0.0 — bundled Apple's seven official Xcode/Swift skills
  (`swiftui-specialist`, `swiftui-whats-new-27`, `uikit-app-modernization`,
  `modernize-tests`, `c-bounds-safety`, `audit-xcode-security-settings`,
  `device-interaction`) unmodified into plugin form. New `development`-category
  plugin; no dependency on other plugins.
- **pdf-viewer** v0.3.0 — added Anthropic's generic `pdf-viewer` plugin
  (interactive view / annotate / fill-form / sign over a local
  `@modelcontextprotocol/server-pdf` MCP), customized for a solo narration
  operation. Rewrote every example off the generic defaults (arXiv papers,
  anonymous contracts, bare W-9s) onto Pavi's real PDF jobs: narration script
  prep with a defined markup convention (pronunciations=blue notes, character
  cues=teal, breath/pause `/`,`//`, emphasis=underline, PICKUP stamps=red,
  chapter breaks, typo strikethroughs, amber `Q:` author questions), publisher
  contract review + signing (Aethon/Podium/Recorded Books/Blackstone/Audible,
  with a DocuSign hand-off note), and contractor tax forms (W-9 with standing
  Pavitas Productions LLC field context and a hard stop on guessing EIN/address/
  bank numbers). `open`/`annotate`/`sign`/`fill-form` commands and the `view-pdf`
  skill point summaries and chapter breakdowns back to Read / the
  audiobook-script-analyzer skill, and the skill explicitly excludes AI voice
  generation. Plugin and skill names unchanged; author set to Pavitas Productions
  per the productivity-plugin precedent. Marketplace manifest bumped to 1.8.0.
- **productivity** v1.3.0 — customized Anthropic's generic productivity plugin
  (task management + two-tier workplace memory + dashboard) for a solo
  operation instead of a team: dropped chat and separate project-tracker
  categories (no Slack, no Asana/Linear/Jira), Notion covers both knowledge
  base and project tracker, Gmail/Google Calendar are native connectors
  (no plugin `.mcp.json` entries needed), Composio documented as fallback
  routing (preferred for Notion per standing routing rule, backup for
  Gmail/Calendar/Drive). Memory lookup flow now checks Supermemory before
  asking the user to explain a person/project/term, to avoid duplicating
  or re-asking what's already durably recorded. Zo Computer added as an
  extra `/update --comprehensive` scan source (its own memory.duckdb) and
  as the recommended home for anything recurring (`create_automation`
  outlives any single session), with a tool-priority note (direct Zo MCP
  tools over `ask_zo`). Marketplace manifest bumped to 1.7.0.
- **hunt-skills** v1.0.0 — new plugin packaging three previously-standalone scavenger-hunt
  skills (scavenger-hunt-designer, pocket-hunt, pleasure-hunt) so they install and update
  together. Moved as-is, with internal cross-references namespaced
  (`hunt-skills:scavenger-hunt-designer`, `hunt-skills:pocket-hunt`). No dependency on other
  plugins. Skill-only — no agents or commands; each skill runs live in the main conversation
  and a sub-agent hop would only add latency. Marketplace manifest bumped to 1.6.0.
- **audiobook-production** v1.1.0 — absorbed `audiobook-script-analyzer` and
  `audiobook-project-setup`, previously standalone skills uploaded separately
  under `skills/`, as a bundled `skills/` directory inside the plugin
  itself — so the whole audiobook workflow (commands, agents, skills)
  installs and updates as one unit. Moved as-is, no content changes beyond
  namespacing (`audiobook-production:audiobook-script-analyzer`,
  `audiobook-production:audiobook-project-setup`). `pavitas-core:audiobook-kickoff`
  and `pavitas-core:skill-router`'s dispatch table and coverage manifest
  updated to route to the namespaced skills. Marketplace manifest bumped to
  1.6.0.
- **story-grid-skills** v1.0.0 — new plugin packaging five previously-standalone Story
  Grid mentorship coaching skills (sg-grade, sg-edit, sg-drill, sg-spar, sg-sync) so they
  install and update together. Moved as-is, with internal cross-references namespaced
  (`story-grid-skills:sg-grade`, `story-grid-skills:sg-edit`). No dependency on other
  plugins. Marketplace manifest bumped to 1.5.0.
- **slashy-ops** v1.0.0 — new plugin packaging the five Slashy-based email/
  calendar skills (morning-briefing, eod-wrapup, batch-draft-writer,
  meeting-scheduler, deal-tracker) that previously shipped as unnamespaced
  standalone skills under `skills/`. Moved as-is, no content changes beyond
  namespacing internal cross-references (`slashy-ops:batch-draft-writer`).
  All five require `pavitas-core` installed for `using-slashy`,
  `output-quality`, and `workspace-context`. Marketplace manifest bumped to
  1.4.0. `pavitas-core:skill-router`'s coverage manifest and dispatch table
  updated to route to the namespaced skills and list the new plugin.

### Changed
- **spins-yarns-content** v2.0.0 — absorbed fiber-arts-content. Gains
  `/pattern`, `/log`, and `/project` commands (cleaned: stale hardcoded
  project lists removed — the Notion Littlebird Log is the only project
  source of truth) and a rewritten `/post` that defers entirely to the
  `spins-yarns-brand-voice` skill. Old pun-heavy voice guidance deleted,
  not migrated. Threads removed from `/weekly`, README, and plugin
  metadata — the brand is Instagram-only (2 IG posts/week), aligning the
  plugin with its own voice skill and content-pipeline's hard rule.
  Marketplace manifest bumped to 1.3.0.
- **audiobook-production** (`/new-project`, `agents/production-tracker`) —
  Chapter Work Date distribution now runs automatically during onboarding as
  a default step. Distributes chapters by page count across all weekdays
  (Mon–Fri) in the book's `Dates` range; both start_date and end_date are
  valid recording days (end_date is BOTH the last recording day and the
  delivery day). Spec lives in
  `skills/audiobook-script-analyzer/SKILL.md` § "Distribute chapters across
  workdays". `Standing By` status string corrected to the actual Notion
  option.
- **audiobook-production** (`agents/production-tracker`) — Chapter `Record
  Name` now stores the full file name (e.g.,
  `001_LoopBound1_Chapter 1`), not the chapter heading alone. Fixes a
  long-standing mistranslation where script-scout produced correct file
  names but production-tracker wrote only the chapter heading into Notion.
- **audiobook-script-analyzer** — "Distribute chapters across workdays"
  promoted from optional to default. `Pages per day` field no longer
  required; auto-computed from `ceil(total_pages / weekday_count)` when
  absent. Algorithm clarified: both endpoints of the `Dates` range are
  valid recording days.
- **audiobook-script-analyzer** — File Naming Convention expanded. Opening
  billboards numbered `000`; first chapter or section starts at `001`. When
  a chapter header is only a number, omit the word "Chapter". POV-split
  duplicates retain their POV indicator as the unique differentiator. Short
  name rule reinforced: use VERBATIM as the user provides it, never modify
  spacing or case.
- **audiobook-production** (`agents/script-scout`) — File Naming section
  now points to `skills/audiobook-script-analyzer/SKILL.md` as the single
  source of truth rather than redefining the convention.

### Removed
- **fiber-arts-content** — merged into spins-yarns-content (above). Its
  `/post` voice guidance (pun-mandatory, engagement-bait closers,
  #narratorlife) was superseded by `spins-yarns-brand-voice` and deleted.
- **audiobook-production** (`/new-project`) — Agent 4 (calendar-setup) and
  all Google Calendar event creation from the onboarding flow. Notion
  `Work Date` is now the single source of truth for the recording schedule;
  Pavi views it via Notion's calendar view. Eliminates drift between
  Google Calendar and Notion.

---

## [1.2.0] — [DATE — fill in]

### Added
- **pavitas-content** — Weekly @pavitasproductions social content generation:
  1 image/carousel (IG + FB) + 1 short-form video script (TikTok + Shorts),
  drafted from Notion inputs.
- **spins-yarns-content** — Weekly @pavi.spins.yarns social content
  generation: 2 IG posts + 1 Threads post, drafted from Notion Littlebird
  crochet brief + Perplexity trends, with Canva visual assets.

---

## [1.1.0] — ~2026-03-30

### Added
- **enterprise-search** — Customized cross-tool search across email, chat,
  docs, and wikis. Commands: search, digest. Skills: knowledge-synthesis,
  search-strategy, source-management.
- **writing-workshop** — Writing workshop plugin. Skills: writing-interview,
  writing-nudge, project-setup, style-mirror.

---

## [1.0.0] — [DATE — fill in]

### Added
- Initial release. Five plugins covering core Pavitas Productions workflows:
  - **audiobook-production** — End-to-end audiobook production: script
    analysis, recording prep, QC, delivery, invoicing. Commands: new-project,
    session-prep, qc-pack, wrap.
  - **daily-ops** — Daily workflow orchestration: briefings, handoffs, email
    triage, task capture, day reviews. Commands: briefing, handoff, triage,
    tasks, review.
  - **publisher-relations** — Publisher relationship management: email intake,
    invoicing, status tracking, reply drafting. Commands: intake, invoice,
    status, reply.
  - **creative-writing** — Story Grid fiction toolkit: scene analysis, mentor
    submissions, prose cleaning, dictation processing. Commands: scene, submit,
    clean, dictate, stuck.
  - **fiber-arts-content** — Crochet documentation and Instagram content for
    @pavi.spins.yarns. Commands: pattern, log, post, project.
