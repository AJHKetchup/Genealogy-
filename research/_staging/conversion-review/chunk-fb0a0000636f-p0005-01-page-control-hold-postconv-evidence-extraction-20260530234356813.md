---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260530234356813
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256_recorded_in_chunk: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
converted_sha256_observed: da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
chunk_sha256_observed: d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d
chunk_manifest: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json
page_reference: page 5
page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
page_image: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530234356813.md
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Page 5 Control Still Blocked

This evidence-extraction revision did not run source preparation or document conversion and did not edit raw sources, converted Markdown, chunks, page Markdown, manifests, or canonical wiki pages.

## Current Derivative Disagreement

Assigned chunk/current aggregate converted file:

```text
1979 - 1982
United Nations Centre for Human Settlements (HABITAT)
Nairobi, Kenya
Development Support Communications Officer
```

Conversion-job page Markdown:

```text
1999
National Trust Fund for Protected Areas in Peru (PROFONANPE)
Peru
Consultant
```

## QA Blocker

The chunk manifest contains duplicate entries for `CHUNK-fb0a0000636f-P0005-01` with conflicting character counts and hashes. The observed aggregate converted hash is `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`, while the chunk metadata records `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`. The observed chunk hash is `d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d`, which does not match either page-5 manifest entry. The expected rendered page image path was not present in this worker pass.

## Recommendation

Keep all page-5 claims and identity attachments on `hold_for_conversion_qa`. Conversion QA should restore or regenerate the authoritative page image or inspect the original PDF page, reconcile duplicate manifest entries and hash drift, and certify which derivative text controls physical page 5.
