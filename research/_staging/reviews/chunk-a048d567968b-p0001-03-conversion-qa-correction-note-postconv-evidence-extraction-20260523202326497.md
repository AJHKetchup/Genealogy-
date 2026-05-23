---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523202326497
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_path: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; Dario Pulgar support appears in derivative page Markdown/page metadata for printed/source pages 7 and 8; manifest lists rendered images page-0007.jpg and page-0008.jpg, but the current checkout lacks the Habitat Revisited page-images directory"
literal_support: "page-markdown/page-0007.md and the assigned chunk contain the Dario Pulgar Chilean/Chile state film distribution/fleeing-1973 paragraph; page-markdown/page-0008.md and the assigned chunk contain `His mother tongue was Spanish`, the English/French language passage, and the Vision Habitat distribution-rights/off-shore printing-materials passage."
conversion_confidence: medium
conversion_qa_concern: "This revision could not independently verify against rendered source images because the Habitat Revisited conversion-job directory contains page-markdown, work-orders, README, and manifest files, but no page-images directory. This preserves the disagreement between earlier staged notes that cite rendered page-image review and the current checkout where those images are unavailable. The authoritative blocker remains the page-boundary/citation conflict: the chunk manifest assigns page 1 while the family-relevant support is tied by derivative page Markdown to pages 7 and 8."
uncertainty: "The derivative transcript is internally consistent and family-relevant, but this note does not alter raw sources, converted Markdown, chunks, page Markdown, or prior review notes. Treat the staged claims as memoir-source contextual evidence only after conversion QA resolves image availability and authoritative page reference."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This worker reviewed `CHUNK-a048d567968b-P0001-03` for the proof-review revision request.

## Current Staged State

- The source packet `research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md` remains an appropriate draft packet for the Dario Pulgar evidence and keeps `promotion_recommendation: hold_for_conversion_qa`.
- Six atomic claim drafts already exist for Dario Pulgar: Chilean descriptor, Chile state film distribution role, fleeing after the 1973 Pinochet overthrow, mother tongue Spanish, English/French language context, and Vision Habitat distribution-rights work. They all retain `promotion_recommendation: hold_for_conversion_qa`.
- The negative relationship candidate remains correct: this chunk states no kinship relationship for Dario Pulgar and should not be promoted as a tree relationship.
- The existing research task `research/_staging/research-tasks/chunk-a048d567968b-p0001-03-conversion-qa-page-boundary.md` correctly captures the remaining conversion QA work.

## Revision Finding

The family-relevant Dario Pulgar text is present in the assigned chunk and in derivative page Markdown:

```text
A couple of my UN Habitat Secretariat confreres stayed on, notably Dario Pulgar,
a raspy-voiced, incredibly energetic, dynamic Chilean.
```

```text
In Chile under Allende, though still in his twenties, Dario had been the number two man in Chile's state film distribution system.
```

```text
His mother tongue was Spanish, but he was fluent in English and had learned French in Montreal in six weeks, he said.
```

```text
Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were.
```

The current checkout does not contain the Habitat Revisited conversion-job `page-images` directory. The manifest still lists `page-images/page-0007.jpg` and `page-images/page-0008.jpg`, and earlier staged correction/proof-review notes cite image checks for those pages, but this worker cannot repeat the visual check from the present files. Derivative `page-markdown/page-0007.md` and `page-markdown/page-0008.md` support the text, but they are not a substitute for the requested image-level conversion QA.

## Promotion Recommendation

Keep all Dario Pulgar claims from this chunk at `hold_for_conversion_qa`. The evidence is useful family-context material, but canonical promotion should wait until conversion QA restores or documents the missing rendered source images and resolves whether citation should use assigned page 1, printed/source pages 7-8, rendered image paths, or regenerated chunk/page metadata.
