---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260530214712519
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256_recorded: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
converted_sha256_observed: da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
chunk_sha256_observed: d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d
chunk_manifest: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json
page_reference: page 5
page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
page_image_checked: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg
page_image_available: false
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260530214712519.md
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Page 5 Remains Blocked

This revision pass did not edit raw sources, converted Markdown, chunk files, page Markdown, or canonical wiki pages.

## Disagreement Preserved

The assigned chunk for `CHUNK-fb0a0000636f-P0005-01` contains the older work-history sequence:

```text
1979 - 1982
United Nations Centre for Human Settlements (HABITAT)
Nairobi, Kenya
Development Support Communications Officer
```

It continues with National Film Board of Canada, Chile Films, and CITELCO entries for 1974-1970.

The conversion job's `page-markdown/page-0005.md` contains a different page-5 transcription, beginning:

```text
1999
National Trust Fund for Protected Areas in Peru (PROFONANPE)
Peru
Consultant
```

and continuing with TVE, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture entries.

The aggregate converted Markdown includes both derivative page-5 candidates. The chunk manifest also repeats `CHUNK-fb0a0000636f-P0005-01` with different character counts and SHA-256 values. Current observed hashes for the converted file and chunk differ from the hashes recorded in the assigned chunk/manifest metadata.

## Current Blocker

The referenced rendered page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` is absent in this workspace. Without the image or a repaired conversion package, this worker cannot decide whether source page 5 is the 1999/1998 text or the 1979-1970 text.

## Recommended Correction Path

1. Restore or regenerate the authoritative page 5 image from `raw/sources/CV of Dario Arturo Pulgar.pdf`.
2. Reconcile `page-markdown/page-0005.md`, the aggregate converted file, the chunk file, and the duplicate manifest entries.
3. Rerun proof review only after one controlling page-5 transcription and current hashes are established.
4. Treat any surviving work-history claims as about the CV subject until a separate identity-bearing page bridges the source to a canonical person.

