---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524083533630
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-postconv-evidence-extraction-20260524083533630.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
page_reference: "assigned page 1; Dario Pulgar support visually verified on rendered/printed pages 7 and 8; converted metadata is offset"
literal_support: "Page-0007.jpg supports the Dario Pulgar full-name, Chilean descriptor, Chile state-film role, and 1973 fleeing context. Page-0008.jpg supports the Spanish mother-tongue sentence, English/French language context, and Vision Habitat distribution-rights/off-shore printing-materials work passage."
conversion_confidence: medium-high
conversion_qa_concern: "The rendered page images are present and support the Dario Pulgar wording. Promotion remains blocked because the controller assignment, chunk frontmatter, and chunk manifest cite page 1 while the visual evidence is on printed pages 7 and 8 and the converted Markdown metadata does not align cleanly."
uncertainty: "The remaining issue is authoritative citation/page-boundary integrity rather than a substantive conflict in the Dario Pulgar wording. The source is memoir evidence, not a vital or official employment record."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision adds worker-specific staged evidence while preserving the proof-review blocker.

## Visual Check

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` visually supports the Dario Pulgar full-name passage, the Chilean descriptor, the Chile state-film role under Allende, and the statement that he fled after Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present and visually supports `His mother tongue was Spanish`, the English/French language context, and the Vision Habitat distribution-rights/off-shore printing-materials work context.

## Remaining QA Blocker

The disagreement must remain visible: `CHUNK-a048d567968b-P0001-03` is assigned to page 1 by the controller, chunk frontmatter, and manifest, while the image-reviewed evidence appears on rendered/printed pages 7 and 8. The converted chunk also carries page metadata that does not cleanly match those rendered page numbers.

Keep related Dario Pulgar claims in staging with `promotion_recommendation: hold_for_conversion_qa` until conversion QA corrects or formally documents the authoritative page citation. The relationship note is `do_not_promote` because this chunk states no kinship relationship.
