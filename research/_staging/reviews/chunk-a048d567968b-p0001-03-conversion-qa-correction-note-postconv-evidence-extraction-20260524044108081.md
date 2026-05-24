---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524044108081
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
chunk_id: CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
assigned_page_reference: "page_start 1, page_end 1"
image_pages_checked:
  - "raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg"
  - "raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg"
conversion_confidence: medium-high
conversion_qa_concern: "The relevant Dario Pulgar wording is visually supported on rendered source images page-0007.jpg and page-0008.jpg, but the chunk manifest still assigns CHUNK-a048d567968b-P0001-03 to page 1 while the supporting passages belong to printed/source pages 7 and 8 and the chunk body continues into later converted page text."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note: CHUNK-a048d567968b-P0001-03

This revision confirms that the prior missing-image blocker for the mother-tongue passage is no longer present in this checkout. The rendered source image `page-0008.jpg` exists and visually supports the converted sentence:

```text
His mother tongue was Spanish, but he was fluent in English and had
learned French in Montreal in six weeks, he said.
```

The rendered source image `page-0007.jpg` visually supports the Dario Pulgar full-name context and the Chile/film-distribution/displacement passage:

```text
A couple of my UN Habitat Secretariat confreres stayed on, notably Dario Pulgar,
a raspy-voiced, incredibly energetic, dynamic Chilean. In Chile under Allende,
though still in his twenties, Dario had been the number two man in Chile's state film
distribution system. He had fetched up at "The Board" after fleeing Pinochet's
overthrow of the Allende government in 1973.
```

The evidence disagreement should still be preserved. The chunk manifest assigns this chunk to page 1, but the chunk body embeds text labeled as converted page 8 and surrounding later pages; the rendered images checked here show the family-relevant Dario Pulgar support on printed/source pages 7 and 8. This is a citation/page-boundary reconciliation issue, not a current disagreement over the literal wording of the Dario passages.

The existing staged Dario Pulgar claims and source packet should remain at `promotion_recommendation: hold_for_conversion_qa` until an authoritative page reference is corrected or documented for canonical citation. No family relationship is stated in this chunk.
