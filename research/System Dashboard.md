# System Dashboard

Generated: 2026-05-16T16:23:05Z

## Source Conversion

- Sources: 49
- Local source cache entries: 0
- Cloud-registered sources awaiting local cache: 49
- Conversion jobs: 4
- Converted Markdown files: 4
- Usability: conversion_not_started: 48, usable_for_extraction: 1

## Source Prep First Gate

- Gate ready: false
- Registered sources: 49
- Pending registered sources: 48
- Source statuses: cloud_registered: 48, converted: 1
- Source-prep page tasks: 5
- Blocking page tasks: 0
- Blocking task statuses: none
- Next step: Finish R2 restore/intake plus Docling/Gemini source conversion before downstream research agents run.

## R2 Source Intake

- Status: skipped-missing-config
- Last heartbeat status: skipped-missing-config
- Remote raw files seen: 0
- New remote files: 0
- Changed remote files: 0
- Removed remote files: 0
- Preflight: `research/_indexes/r2-source-intake-preflight.json`
- Preflight status: missing_config
- Missing required config: R2_BUCKET, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY
- Intake candidate report: `research/r2-intake-candidates.md`
- Intake candidate registers: 3
- Pending intake candidates: 0
- Intake candidate statuses: none
- R2 manifest: `raw/r2-raw-sources.json`
- Source-prep manifest: `raw/source-prep-manifest.json`
- State: `none`

## Research Readiness

- Usable sources: 1
- Sources needing conversion or page repair: 48
- QC pages: 0
- Analyzer pages scanned: 8
- Analyzer upgrade candidates: 0
- Analyzer staging opportunity pages: 2
- Analyzer staging recommendations: claim: 2, source_packet: 2
- Analyzer staging readiness: blocked_pending_conversion_qa: 2
- Analyzer staging backlog: `research/_indexes/research-staging-backlog.json`
- Analyzer staging backlog items: 2
- Analyzer staging backlog ready: 0
- Analyzer staging backlog blocked: 2
- Analyzer staging backlog readiness: blocked_pending_conversion_qa: 2
- Analyzer research leads: 15
- Analyzer lead page references: 18
- Analyzer lead classifications: ambiguous_marker: 1, person_name: 3, titled_name: 11
- Analyzer lead review statuses: low_signal: 1, repeated_unresolved_lead: 3, unresolved_lead: 11
- Analyzer external research requests: 3
- Analyzer external research statuses: blocked_pending_conversion_qa: 3
- External research request notes: 3
- Staging drafts: claims: 0, identity: 0, relationships: 0, source_packets: 0

## Page Upgrades

- Index: `research/_indexes/page-upgrades.json`
- Markdown: `research/page-upgrades.md`
- Active page upgrade requests: 0
- Critical or high relevance requests: 0
- Pro/reread requests: 0
- Analyzer requests written last run: 0

## Next Actions

- **high** `source_prep_gate`: Finish R2 restore/intake plus Docling/Gemini source conversion before downstream research agents run. (48 registered source(s) are not converted yet.)

## Queues

| Queue | Tasks | Status Counts |
| --- | ---: | --- |
| conversion_qa | 4 | todo: 4 |
| evidence_extraction | 8 | blocked_pending_conversion_qa: 8 |
| external_research | 3 | blocked_pending_conversion_qa: 3 |
| research_leads | 14 | blocked_pending_conversion_qa: 14 |
| research_questions | 2 | blocked_pending_conversion_qa: 2 |
| source_prep | 5 | done: 5 |
| source_prep_batches | 0 | none |

## Queue Blockers

| Blocker | Blocking Tasks | Blocked Tasks | Blocked Queues | Next Step |
| --- | ---: | ---: | --- | --- |
| pending_conversion_qa | 4 | 27 | evidence_extraction: 8, external_research: 3, research_leads: 14, research_questions: 2 | Complete conversion-QA tasks, then regenerate queues to release extraction, lead, external-research, and research-question work. |

## Conversion QA Unblock Plan

- Plan: `research/_indexes/conversion-qa-unblock-plan.json`
- Next focus: `research/conversion-qa-next.md`
- Open conversion-QA tasks: 4
- Blocked downstream tasks: 29
- Blocked queues: evidence_extraction: 8, external_research: 3, research_leads: 14, research_questions: 2, research_staging_backlog: 2
- Top unblock task: `conversion-qa:raw-converted-ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex-md`
- Top unblock count: 24

## Storage

- R2 raw files: 49
- R2 raw bytes: 8230789331
- R2 durable derived assets: 0
- R2 durable derived asset bytes: 0
- Storage lifecycle status: active
- Storage lifecycle ranked pages: 5
- Storage lifecycle retention: cold_retain: 3, preserve_raw: 2
- Deaccession candidates: 0
- Deaccession records: 0

## Final Site

- Status: ready
- Status report: `research/_indexes/final-site-status.json`
- Manifest: `site/site-manifest.json`
- Search index: `site/search-index.json` (2 entries)
- Source wiki pages: 2
- Utility pages: 2
- Manifest pages: 4
- HTML files: 4
- Missing entry points: 0
- Missing manifest outputs: 0
- Missing source pages from manifest: 0

## Blockers

- None
