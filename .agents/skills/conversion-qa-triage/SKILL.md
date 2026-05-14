---
name: conversion-qa-triage
description: Review converted genealogy documents after source conversion and before evidence extraction. Use to flag likely transcription/OCR mistakes, name drift, skipped or high-value pages, page regions needing careful reread, and pages that are especially relevant to the family history, without editing raw sources, converted Markdown, chunks, or canonical wiki pages.
---

# Conversion QA Triage

Use this skill after `raw/converted/` and `raw/chunks/` exist and before source packets or claims are staged. The job is to ask "are we sure?" about the conversion while preserving the converted document as the verbatim artifact.

## Inputs

- Converted Markdown under `raw/converted/`.
- Chunk manifests and chunk files under `raw/chunks/`.
- Conversion job manifests, page images, page Markdown, and extracted crops under `raw/codex-conversion-jobs/`.
- Canonical family context from `wiki/people/`, `wiki/families/`, `wiki/relationships/`, `wiki/sources/`, `wiki/claims/`, and `wiki/narratives/`.

## Outputs

Write review artifacts only under `research/_conversion-review/`:

- `research/_conversion-review/triage/<source-or-job>.md`
- `research/_conversion-review/page-queues/<source-or-job>.md`
- `research/_conversion-review/corrections/<source-or-job>.md`
- `research/_conversion-review/qc-pages.json`

Start from the automatic QC artifacts when present:

- `research/_conversion-review/qc-index.json`
- `research/_conversion-review/qc-pages.json`
- `research/_conversion-review/triage/<converted-source>.md`
- `research/_conversion-review/page-queues/<converted-source>.md`
- `research/_conversion-review/corrections/<converted-source>.md`

The automatic pass is a filter, not authority. Confirm or refine its suspected readings against the page image and converted source.

Pages with a non-`pass` decision in `qc-pages.json` hold only the overlapping evidence-extraction chunks as `blocked_needs_reread`. Leave clean pages available; the goal is targeted reread, not freezing a 1,000-page archive because ten pages matter.

Legacy conversions that merely copied OCR, preserved a page image, or omitted required page sections should be treated as `reread-page`, even if they do not contain obvious placeholder text.

Do not edit `raw/sources/`, `raw/converted/`, `raw/chunks/`, conversion job page Markdown, or canonical wiki pages during QA triage.

## What To Look For

1. High-value family pages:
   - Pages mentioning known family surnames, given names, spouses, children, places, occupations, institutions, addresses, ships, records, or dates.
   - Pages where only a small section is relevant, such as one paragraph, table row, caption, signature, marginal note, or photo.

2. Likely conversion errors:
   - Known names misread as plausible alternatives, such as `Dario` becoming `David`.
   - Repeated nearby evidence that suggests a name, place, or institution was mistranscribed.
   - Broken page order, missing page headings, missing table columns, missing footnotes, or abrupt gaps.
   - Unmarked uncertainty where handwriting, low contrast, seals, or damaged text should have been marked `[?]` or `[illegible]`.

3. Family-context cross-checks:
   - Compare suspicious readings against canonical names and variants already present in the wiki.
   - Treat the wiki as a clue source, not as permission to rewrite the transcription.
   - Phrase corrections as hypotheses: "likely Dario, verify against page image," not as silent replacements.

## Triage Note Contract

Every triage note should include:

- Source path.
- Converted file path.
- Chunk manifest path.
- Conversion job manifest path when available.
- Reviewed page or chunk range.
- Source reliability class and reliability score when knowable.
- Conversion confidence for the reviewed page/region: `high`, `medium`, `low`, or `unknown`.
- Family relevance score: `none`, `low`, `medium`, `high`, or `critical`.
- Pages or regions queued for careful reread.
- Suspicious readings with literal converted text, suspected reading, reason, and verification target.
- Recommended next action: `pass`, `spot-check`, `reread-page`, `reread-region`, `rerun-conversion`, or `hold-for-human`.

## Rules

- Never normalize the converted Markdown in place.
- Never turn a suspected correction into a claim.
- Do not demote uncertainty just because the wiki has a familiar name.
- Do not confuse source reliability with conversion confidence. A clear transcript of a weak source remains weak evidence; a reliable source with a garbled conversion still needs reread.
- If family relevance is high but conversion confidence is low, queue the exact page/region for careful review before evidence extraction.
- If a 1,000-page source has only three relevant pages, make those pages obvious in the page queue and let the rest pass as low priority.
