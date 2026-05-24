---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524060628523
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-postconv-evidence-extraction-20260524060628523.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
page_reference: "assigned page 1; Dario Pulgar support visually verified on rendered/printed pages 7 and 8"
literal_support: "Page-0007.jpg supports the Dario Pulgar Chilean/Chile film-distribution/fleeing-1973 paragraph. Page-0008.jpg supports the Spanish mother-tongue, English/French language, and Vision Habitat distribution-rights/off-shore printing-materials work passages."
conversion_confidence: medium-high
conversion_qa_concern: "This revision verified that page-0008.jpg is present locally and supports the previously unverified mother-tongue sentence. Promotion remains blocked until the page/chunk citation discrepancy is corrected or formally documented by conversion QA."
uncertainty: "The unresolved issue is authoritative page reference rather than substantive disagreement over the Dario Pulgar wording. The source remains memoir evidence, not a vital or official employment record."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This worker added additive staged files for the Dario Pulgar evidence and preserved the prior proof-review blocker.

## Visual Checks

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` visibly supports the Dario Pulgar full-name passage, the Chilean descriptor, the Chile state-film role under Allende, and the statement that he fled after Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present locally and visibly supports the Spanish mother-tongue sentence, the English/French language context, and the Vision Habitat distribution-rights/off-shore printing-materials work context.

## Remaining QA Blocker

The controller assignment, chunk frontmatter, and chunk manifest assign `CHUNK-a048d567968b-P0001-03` to page 1, while the family-relevant support belongs to rendered/printed pages 7 and 8 and the chunk body includes later converted page metadata.

This is a conversion page-boundary/citation problem, not a contradiction in the Dario Pulgar claim substance. Related claims should remain staged with `promotion_recommendation: hold_for_conversion_qa`. The negative relationship note remains `do_not_promote` because this chunk states no kinship relationship.
