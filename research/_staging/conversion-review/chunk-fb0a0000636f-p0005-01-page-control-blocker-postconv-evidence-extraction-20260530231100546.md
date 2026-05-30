---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260530231009332
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256_recorded: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
converted_sha256_observed: da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
chunk_sha256_observed: d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d
page_reference: page 5
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Page 5 Control Blocker

Do not promote page-5 CV work-history claims from `CHUNK-fb0a0000636f-P0005-01` until conversion QA resolves physical page control.

Observed during evidence extraction:

- Assigned chunk and current aggregate converted file contain 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries.
- Conversion job page file `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` contains different entries beginning with 1999 PROFONANPE and TVE.
- `page-images/page-0005.jpg` is absent in the conversion job folder.
- The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with different counts and hashes.
- Observed hashes differ from recorded metadata: converted file observed `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`; assigned chunk observed `d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d`.

Needed QA action: restore or regenerate the rendered physical page 5 image, reconcile the manifest and hash drift, then certify which derivative text controls page 5 before proof review or canonical promotion.
