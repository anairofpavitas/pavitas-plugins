# Changelog — Plugins

All notable changes to pavitas-plugins **plugins** are documented here.
Skills have their own changelog at `skills/CHANGELOG.md`.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Version numbers are independent from the skills version sequence.

---

## [Unreleased]

### Added
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
