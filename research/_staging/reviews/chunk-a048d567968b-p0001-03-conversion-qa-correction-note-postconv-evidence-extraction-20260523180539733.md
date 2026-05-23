---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523180539733
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
page_reference: "assigned page 1; family-relevant support visually checked on rendered page images page-0007.jpg and page-0008.jpg / printed pages 7 and 8"
literal_support: "page-0007.jpg supports the Dario Pulgar Chilean/Chile film distribution/fleeing-1973 paragraph; page-0008.jpg supports `His mother tongue was Spanish`, English/French language context, and Vision Habitat distribution-rights work."
conversion_confidence: medium
conversion_qa_concern: "The source images for printed pages 7 and 8 are present and visually support the family-relevant passages, including the mother-tongue sentence. The remaining blocker is the derivative citation/page-boundary discrepancy: the chunk manifest assigns page 1 while the body contains later page metadata and support from rendered/printed pages 7-8."
uncertainty: "The Dario Pulgar passages appear accurately transcribed on the checked images, but canonical citation should not be promoted until conversion/page-boundary QA determines the authoritative page reference."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision preserves the disagreement between the derivative chunk metadata and the image-reviewed evidence. No raw source, converted Markdown, chunk Markdown, or page Markdown was edited.

## Image Review

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` is present and visibly supports the full-name paragraph identifying Dario Pulgar, describing him as Chilean, stating that he had been the number two man in Chile's state film distribution system under Allende, and stating that he fled after Pinochet's 1973 overthrow.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present and visibly supports `His mother tongue was Spanish`, the English/French language context, and the statement that Dario was primarily occupied with acquiring distribution rights and locating off-shore printing materials.

## Remaining Blocker

The proof-review missing-image blocker for page 8 is no longer active in this checkout, but the page-reference blocker remains. `CHUNK-a048d567968b-P0001-03` is assigned to page 1 in the chunk frontmatter and manifest, while the family-relevant evidence is on rendered/printed pages 7 and 8 and the chunk body includes later page metadata. Keep all related promotable Dario Pulgar claims on `hold_for_conversion_qa` until the authoritative citation/page boundary is corrected or documented by conversion QA.

