---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524003001254
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
page_reference: "assigned page 1; family-relevant support visually checks to rendered source images page-0007.jpg and page-0008.jpg / printed pages 7 and 8"
conversion_confidence: medium-high
conversion_qa_concern: "The rendered source images page-0007.jpg and page-0008.jpg are present in this checkout and visually support the Dario Pulgar passages. The unresolved blocker is the page/chunk metadata disagreement: the assignment and chunk manifest label this as page 1, while the relevant support belongs to printed/source pages 7 and 8 and the chunk body continues into later converted page text."
uncertainty: "This note documents current-worker review of existing staged evidence and preserves the disagreement between derivative transcript metadata and image-reviewed evidence. It does not alter raw sources, converted Markdown, chunks, or page Markdown."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note: CHUNK-a048d567968b-P0001-03

This current-worker revision reviewed the staged Dario Pulgar extraction after prior proof review held the claims for conversion QA. No raw source, converted Markdown, chunk, or page Markdown files were edited.

## Image-Reviewed Evidence

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` is present in this checkout. It supports the Dario Pulgar full-name paragraph, including the Chilean descriptor, the statement that he had been the number two man in Chile's state film distribution system under Allende while still in his twenties, and the statement that he fled after Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present in this checkout. It supports the statements that Dario's mother tongue was Spanish, that he was fluent in English and had learned French in Montreal, and that he was primarily occupied with acquiring distribution rights and determining where off-shore printing materials were.

## Preserved Disagreement

The earlier missing-image concern for the mother-tongue sentence is resolved in this checkout because `page-0008.jpg` is now present. The page-reference blocker remains unresolved. The task assignment and chunk manifest identify `CHUNK-a048d567968b-P0001-03` as page 1, while the visually checked family-relevant evidence belongs to printed/source pages 7 and 8, and the chunk body embeds later converted page metadata and text.

## Recommendation

Keep the related Dario Pulgar claims and source packet at `promotion_recommendation: hold_for_conversion_qa`. The evidence is textually and visually supported as memoir/context evidence, but it should not be promoted until conversion QA corrects or explicitly documents the authoritative citation and page boundary for this contaminated page-1 chunk.
