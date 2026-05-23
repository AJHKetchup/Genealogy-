---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523211307066
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
chunk_id: CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; visually checked support on rendered source images page-0007.jpg and page-0008.jpg"
conversion_confidence: medium-high
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note: Dario Pulgar Page 7-8 Support

This revision found the rendered source images available in `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/`, including `page-0007.jpg` and `page-0008.jpg`.

Visual check results:

- `page-0007.jpg` visibly supports the Dario Pulgar full-name paragraph, including the Chilean descriptor, the Chile state film distribution role under Allende, and the statement that he fled after Pinochet's overthrow of the Allende government in 1973.
- `page-0008.jpg` visibly supports the sentence `His mother tongue was Spanish`, the English/French language statement, and the statement that Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were.

The derivative transcription and rendered page images now agree on the family-relevant wording. The remaining blocker is the page/chunk reference discrepancy: the assigned chunk and manifest say page 1, while the supporting rendered/printed source pages are 7 and 8 and the chunk body includes converted page metadata continuing beyond the assigned page. For that reason, the revised Dario Pulgar packet and claim drafts remain `promotion_recommendation: hold_for_conversion_qa`.
