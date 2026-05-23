---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523205826590
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; chunk body contains converted page metadata and text for printed/source pages 7-10; Dario Pulgar support appears in derivative transcript text for printed/source pages 7-8"
literal_support: "Derivative converted text states that Dario Pulgar was a Chilean UN Habitat Secretariat colleague, had been the number two man in Chile's state film distribution system under Allende, fled after Pinochet's 1973 overthrow, had Spanish as his mother tongue, was fluent in English and had learned French in Montreal, and worked on Vision Habitat distribution rights and off-shore printing materials."
conversion_confidence: low-to-medium
conversion_qa_concern: "The conversion job manifest lists page-images/page-0007.jpg and page-images/page-0008.jpg with hashes, but in this checkout both image files are absent and the page-images directory is absent. Existing staged records disagree: an earlier correction note reports page-0007.jpg/page-0008.jpg visual checks, while the currently staged source packet and claim drafts record that this worker cannot independently recheck those rendered images. The chunk manifest still assigns the chunk to page 1 even though the family-relevant support appears in embedded later-page text."
uncertainty: "The derivative transcript is internally clear, but the authoritative page citation and image-level transcription proof remain unresolved in the current workspace. This note does not alter source text and does not overrule prior visual-check notes; it documents the present evidentiary conflict for proof review."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision preserves the disagreement between the derivative transcript, prior staged visual-check notes, and the current workspace state for `CHUNK-a048d567968b-P0001-03`.

## Current Workspace Check

- The controller-assigned chunk is `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md`.
- The chunk manifest assigns that chunk to page 1.
- The chunk body includes later converted page metadata and transcribed text for printed/source pages 7-10.
- The conversion job manifest lists `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` and `page-0008.jpg`.
- In this checkout, both listed image files are absent, and the conversion job directory contains `page-markdown/`, `work-orders/`, `manifest.json`, and `README.md`, but no `page-images/` directory.

## Family-Relevant Transcript Support

The derivative converted text remains useful as staged evidence for Dario Pulgar but should not be promoted while the conversion/page citation is unresolved. It supports these staged, person-first narrative points:

- Dario Pulgar stayed on with the UN Habitat Secretariat group and was described as a Chilean colleague.
- Dario had been the number two man in Chile's state film distribution system under Allende while still in his twenties.
- Dario had fetched up at "The Board" after fleeing Pinochet's 1973 overthrow of the Allende government.
- The transcript says Dario's mother tongue was Spanish, that he was fluent in English, and that he had learned French in Montreal.
- Dario was primarily occupied with acquiring distribution rights and determining where off-shore printing materials were for Vision Habitat.

## Staging Decision

Keep the existing source packet and atomic Dario Pulgar claim drafts in staging with `promotion_recommendation: hold_for_conversion_qa`. The staged negative relationship note remains `do_not_promote` because the chunk states no kinship relationship.

Required follow-up before canonical promotion:

- Restore or regenerate the listed rendered page images, especially `page-0007.jpg` and `page-0008.jpg`, without editing raw sources or converted Markdown.
- Visually verify the Dario Pulgar passages against the source images.
- Reconcile the page-reference discrepancy between assigned page 1 and the transcript/image evidence for printed/source pages 7-8.
