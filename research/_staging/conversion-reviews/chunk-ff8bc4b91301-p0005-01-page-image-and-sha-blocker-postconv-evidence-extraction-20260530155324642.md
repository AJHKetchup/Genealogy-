---
type: conversion_review
status: draft
task_id: "evidence-extraction:CHUNK-ff8bc4b91301-P0005-01"
worker: "postconv-evidence-extraction-20260530155227038"
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: "fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256_expected: "ff8bc4b9130169ba6f4ecc103ba089ba6bf26c7162f5dfebbf3bae9ebd3a7271"
converted_sha256_observed_live: "97c8a1cbf4db9e4e39f2044e3260d5938381e2a89583f8e49e6777c77d13444c"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/page-0005-chunk-01.md"
chunk_id: "CHUNK-ff8bc4b91301-P0005-01"
page_reference: "page 5"
page_image: "raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0005.jpg"
page_image_status: "missing_during_revision"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Page 5 Pulgar Hold

This evidence-extraction revision did not run source preparation or document conversion. The page-5 blockers remain:

- The chunk and manifest record converted SHA `ff8bc4b9130169ba6f4ecc103ba089ba6bf26c7162f5dfebbf3bae9ebd3a7271`.
- The live converted file currently hashes to `97c8a1cbf4db9e4e39f2044e3260d5938381e2a89583f8e49e6777c77d13444c`.
- The referenced page image `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0005.jpg` is absent.

Keep all page-5 Pulgar evidence at `hold_for_conversion_qa`. After the image is restored or regenerated and the converted-file SHA mismatch is reconciled, visually proof the `Pulgar` line and then run a separate identity-bridge review against same-source `Dario Pulgar` and any CV or canonical Pulgar identity candidates.
