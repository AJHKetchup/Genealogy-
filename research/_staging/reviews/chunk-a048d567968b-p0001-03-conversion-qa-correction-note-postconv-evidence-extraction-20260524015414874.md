---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524015414874
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; family-relevant Dario Pulgar passages are visually supported on rendered page-0007.jpg and page-0008.jpg / printed pages 7-8"
literal_support: "page-0007.jpg supports the Dario Pulgar Chilean, Chile state-film distribution, and 1973 flight passages; page-0008.jpg supports `His mother tongue was Spanish`, the English/French language passage, and Dario's Vision Habitat distribution-rights work."
conversion_confidence: medium-high
conversion_qa_concern: "The rendered image missing during earlier proof review, page-0008.jpg, is present in this checkout and supports the mother-tongue/language and Vision Habitat role text. The remaining blocker is not literal wording but unresolved page/chunk citation disagreement: the chunk and manifest assign page 1 while the source images and converted page metadata place support on later printed/source pages."
uncertainty: "This note does not alter source text or resolve the authoritative citation. Claims should remain staged until conversion QA reconciles or documents the multi-page material embedded in the assigned page-1 chunk."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction revision reviewed the existing staged packet and claim drafts for `CHUNK-a048d567968b-P0001-03` in light of the proof-review requests.

## Current Finding

The family-relevant Dario Pulgar passages are substantively supported by the derivative transcript and by the rendered page images now present in the checkout:

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` supports the Dario Pulgar full-name context, the Chilean descriptor, the Chile state-film distribution role under Allende, and the statement that he fled after Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present and supports the sentence `His mother tongue was Spanish`, the English/French language context, and the statement that Dario worked on acquiring distribution rights and locating off-shore printing materials for Vision Habitat.

## Remaining Blocker

The page-reference disagreement remains unresolved. The chunk manifest assigns `CHUNK-a048d567968b-P0001-03` to page 1, while the chunk body contains converted page metadata and text for later pages and the family-relevant Dario Pulgar evidence is on rendered/printed pages 7 and 8. This should remain a conversion/page-boundary QA hold before canonical promotion.

## Staging Impact

The existing staged source packet, six Dario Pulgar claim drafts, and negative relationship note already document the visual support and preserve `promotion_recommendation: hold_for_conversion_qa` or `do_not_promote` as appropriate. No raw source, converted Markdown, chunk Markdown, or page Markdown was edited in this revision.

