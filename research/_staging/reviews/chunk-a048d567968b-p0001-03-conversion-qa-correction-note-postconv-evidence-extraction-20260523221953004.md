---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523221953004
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
supplemental_source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-supplement-postconv-evidence-extraction-20260523221953004.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1 in manifest/frontmatter; Dario Pulgar support visually reviewed on rendered images page-0007.jpg and page-0008.jpg / printed pages 7 and 8"
literal_support: "page-0007.jpg supports the Dario Pulgar full-name, Chilean descriptor, Chile state film distribution role, and fleeing-after-1973 passage; page-0008.jpg supports the mother-tongue Spanish sentence, English/French language passage, and Vision Habitat distribution-rights/off-shore printing-materials role passage."
conversion_confidence: medium-high
conversion_qa_concern: "The previously reported missing rendered page-0008.jpg condition is not present in this checkout. The active blocker is still citation integrity: derivative chunk metadata assigns this material to page 1, but the image-reviewed family-relevant evidence is printed/rendered pages 7-8."
uncertainty: "This note preserves the disagreement between derivative transcripts/chunk metadata and image-reviewed evidence. It does not edit raw sources, converted Markdown, chunks, or page Markdown."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision visually checked the rendered source images for the Dario Pulgar evidence in `CHUNK-a048d567968b-P0001-03`.

## Findings

- `page-0007.jpg` is present and visibly supports the Dario Pulgar paragraph covering his full name, Chilean descriptor, Chile state-film distribution role under Allende, and flight after Pinochet's 1973 overthrow of the Allende government.
- `page-0008.jpg` is present and visibly supports the sentence `His mother tongue was Spanish`, the English/French language detail, and the Vision Habitat work passage about acquiring distribution rights and locating off-shore printing materials.
- The page-reference discrepancy remains unresolved: the chunk is assigned to page 1 by the manifest/frontmatter, while the family-relevant support is image-reviewed on printed/rendered pages 7 and 8 and appears inside a chunk body that continues through later converted page metadata.

## Staging Decision

Do not promote the related Dario Pulgar claims yet. The existing atomic claims remain appropriate as staged drafts, but they should stay on `hold_for_conversion_qa` until conversion QA corrects or formally documents the page-boundary/citation issue.

No kinship relationship is stated in this chunk, so the existing negative relationship note should remain `do_not_promote`.
