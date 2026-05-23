---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523182341078
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
page_reference: "assigned page 1; converted chunk body contains later page metadata/text; prior staged notes locate Dario Pulgar support on rendered/printed pages 7 and 8"
literal_support: "Converted text includes `Dario Pulgar`, `the number two man in Chile's state film distribution system`, `after fleeing Pinochet's overthrow of the Allende government in 1973`, `His mother tongue was Spanish`, and `Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were`."
conversion_confidence: medium
conversion_qa_concern: "The converted transcript is internally clear, and prior correction notes report visual checks on page-0007.jpg and page-0008.jpg. In this checkout, the conversion job manifest still lists those image paths, but no matching page-images files were found, so this worker could not independently verify the image-reviewed evidence. The chunk manifest still assigns the chunk to page 1 while the relevant text belongs to later printed/source pages."
uncertainty: "This note preserves the disagreement between derivative chunk/page metadata and prior image-reviewed evidence. It does not alter the source text or resolve the authoritative citation."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision addresses the proof-review follow-up for `CHUNK-a048d567968b-P0001-03` without editing raw sources, converted Markdown, chunk Markdown, or page Markdown.

## Current Check

- The converted chunk contains clear Dario Pulgar passages with family-relevant identity, language, occupation/role, and displacement context.
- The conversion job manifest lists rendered image paths for `page-0007.jpg` and `page-0008.jpg`.
- A filesystem check found no `page-000*.jpg` files under the conversion job directory in this checkout, so this worker could not independently repeat the prior visual verification.
- Earlier staged correction notes report that `page-0007.jpg` supported the Dario Pulgar Chile/film-distribution/fleeing-1973 paragraph and that `page-0008.jpg` supported the mother-tongue/language and Vision Habitat distribution-rights passages.

## Remaining Blocker

Keep all promotable Dario Pulgar claims from this chunk on `hold_for_conversion_qa`. The blocker is not the wording of the converted transcript; it is the unresolved evidence control problem: assigned page 1 conflicts with later converted/printed page references, and the rendered page images cited by prior visual-review notes are not available in the current checkout for independent confirmation.

## Staging Action

The staged research task `research/_staging/research-tasks/chunk-a048d567968b-p0001-03-conversion-qa-page-boundary.md` was updated to remove the stale statement that `page-0008.jpg` is present in this checkout. Existing staged claim drafts already retain `promotion_recommendation: hold_for_conversion_qa`, so they were not promoted or rewritten.

