---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-ff8bc4b91301-P0007-01"
worker: "postconv-evidence-extraction-20260530195408710"
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_path: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/page-0007-chunk-01.md"
chunk_id: "CHUNK-ff8bc4b91301-P0007-01"
page_reference: "page 7"
page_image_reviewed: "raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg"
converted_sha256_in_manifest: "ff8bc4b9130169ba6f4ecc103ba089ba6bf26c7162f5dfebbf3bae9ebd3a7271"
converted_sha256_observed_live: "97c8a1cbf4db9e4e39f2044e3260d5938381e2a89583f8e49e6777c77d13444c"
chunk_sha256_in_manifest: "511daeea5d138807c31846591196acd9ca54ff8b7bf65079ba6ffa73e689dd30"
chunk_sha256_observed_live: "81b76a003a65386659eb70b70724fdcc076b7ded89c4559747ff0767f2c8b90e"
conversion_confidence: medium
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Page 7 Dario Paragraph

The existing page image `page-0007.jpg` visibly supports the Dario Pulgar paragraph at the bottom of page 7. The material wording in the chunk matches the image for the page-local Dario claims:

- `Dario Pulgar` is named as one of the narrator's UN Habitat Secretariat confreres who stayed on.
- He is described as a Chilean.
- The paragraph says that, under Allende and while still in his twenties, Dario had been the number two man in Chile's state film distribution system.
- The paragraph says he reached `"The Board"` after fleeing Pinochet's 1973 overthrow of the Allende government.

This note does not mark the evidence promotion-ready. It preserves the unresolved derivative provenance problem: the current live hashes for both the converted Markdown and page chunk differ from the hashes recorded in the manifest and chunk front matter. Older staged drafts also cited stale `CHUNK-8791cef1980e-P0007-01` metadata. A conversion QA pass should reconcile the derivative file state and then a separate identity-bridge review should compare this proof-reviewed page-local evidence with proof-reviewed CV or family evidence.
