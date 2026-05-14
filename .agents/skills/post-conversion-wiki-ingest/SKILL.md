---
name: post-conversion-wiki-ingest
description: Stage converted genealogy sources for wiki research after `raw/converted/` and `raw/chunks/` exist. Use when Codex needs to turn prepared source Markdown or chunks into reviewable `research/_staging/` source-packet drafts without editing canonical wiki pages.
---

# Post-Conversion Wiki Ingest

Use this skill after source preparation and conversion QA triage are complete. The goal is to create reviewable staging drafts from converted sources while keeping raw sources, converted Markdown, chunks, conversion QA notes, and canonical wiki pages unchanged.

## Workflow

1. Confirm the prepared source package exists:
   - Original source in `raw/sources/`.
   - Converted Markdown in `raw/converted/`.
   - Page-scoped chunks and manifest in `raw/chunks/`.
   - Conversion QA triage notes and page queues in `research/_conversion-review/`, when present.
2. Read the relevant converted file, chunk manifest, QA page queue, and only the chunks needed for the assigned source or page range.
3. Create or update draft material under `research/_staging/source-packets/`.
4. Keep transcription, translation, interpretation, uncertainty, and promotion recommendation separate.
5. Log recommendations in the final response. Do not update `wiki/index.md` or canonical wiki folders.

## Staging Output

Every staged source-packet draft must include:

- Source path.
- Converted file path.
- Chunk or page references.
- Literal transcription or literal support.
- Translation when needed.
- Interpretation separated from source text.
- Uncertainty notes.
- Candidate entities, claims, relationships, conflicts, and research tasks.
- Promotion recommendation: `promote`, `revise`, `hold`, or `reject`.

## Guardrails

- Do not edit `raw/sources/`, `raw/converted/`, or `raw/chunks/`.
- Do not treat `research/_conversion-review/corrections/` as corrected source text. It is a queue of suspected readings that must be checked against the image or converted source.
- Do not write to canonical `wiki/source-packets/`, `wiki/claims/`, `wiki/relationships/`, `wiki/people/`, or `wiki/families/`.
- Do not summarize a source as a substitute for literal transcription.
- Do not merge identities or assert relationships while staging.
- Treat chunks as navigation/provenance artifacts, not evidence conclusions.
