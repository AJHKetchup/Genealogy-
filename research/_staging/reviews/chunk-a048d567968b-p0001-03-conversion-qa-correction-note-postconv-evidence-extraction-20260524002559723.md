---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524002559723
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
page_reference: "assigned page 1; visually checked support appears on rendered source images page-0007.jpg and page-0008.jpg / printed pages 7 and 8"
conversion_confidence: medium-high
conversion_qa_concern: "The rendered source images page-0007.jpg and page-0008.jpg are present in this checkout and visually support the Dario Pulgar passages. The remaining blocker is unresolved page/chunk metadata: the assignment and chunk manifest label this as page 1, while the family-relevant support is printed/source pages 7 and 8 and the chunk body continues into later converted page text."
uncertainty: "This note documents visual support and preserves the disagreement between derivative chunk metadata and image-reviewed evidence. It does not correct raw sources, converted Markdown, chunks, or page Markdown."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note: CHUNK-a048d567968b-P0001-03

This worker did not edit raw sources, converted Markdown, chunks, or page Markdown. The staged Dario Pulgar claims and source packet should remain held for conversion QA.

## Image-Reviewed Evidence

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` is present. It visibly supports the Dario Pulgar full-name paragraph, including the Chilean descriptor, the statement that he had been the number two man in Chile's state film distribution system under Allende while still in his twenties, and the statement that he fled after Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present. It visibly supports the statements that Dario's mother tongue was Spanish, that he was fluent in English and had learned French in Montreal, and that he was primarily occupied with acquiring distribution rights and determining where off-shore printing materials were.

## Preserved Disagreement

The earlier image-availability blocker for the mother-tongue claim is resolved in this checkout, but the citation/page-reference blocker is not resolved. The assignment and chunk manifest identify `CHUNK-a048d567968b-P0001-03` as page 1. The chunk body contains embedded converted text and metadata for later printed/source pages, and the family-relevant Dario Pulgar evidence visually checks to printed/source pages 7 and 8.

## Recommendation

Keep the related staged claims, identity/conflict notes, relationship negative-evidence note, and source packet at `promotion_recommendation: hold_for_conversion_qa` or `do_not_promote` as already staged. Do not promote the Dario Pulgar claims until the authoritative page citation or regenerated chunk/page metadata reconciles the assigned page 1 reference with the image-reviewed pages 7 and 8 evidence.
