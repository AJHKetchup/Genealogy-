---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260531005238122
subject: CV of Dario Arturo Pulgar page 5 control conflict
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_path: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
source_file_observed: absent at recorded path during this extraction revision
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256_recorded: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
converted_sha256_observed: da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
chunk_sha256_observed: d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d
page_reference: page 5
confidence: high
literal_support: Assigned chunk presents 1979-1970 work-history text; conversion-job page-markdown/page-0005.md presents competing 1999-1997 consulting text.
conversion_confidence: blocked
conversion_qa_concern: Physical page 5 cannot be certified because the source PDF/page image is unavailable locally, derivative texts conflict, manifest entries are duplicated, and observed hashes differ from recorded metadata.
uncertainty: High for which derivative text controls physical page 5.
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Page 5 Still Blocked

Proof review requested source-prep/conversion QA before promotion. This revision did not edit raw sources, converted Markdown, chunks, page Markdown, source packets from prior workers, or canonical files.

Observed state:

- Assigned chunk/current aggregate text presents a 1979-1970 work-history page with HABITAT/Nairobi, NFB/Montreal, Chile Films/Santiago, and CITELCO/Santiago entries.
- `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` presents a different 1999-1997 consulting page with PROFONANPE/Peru, TVE/London, Arca Consulting/Lesotho, Klohn Crippen/Huaraz, and SNC Lavalin/Maracaibo entries.
- The chunk manifest contains duplicate `CHUNK-fb0a0000636f-P0005-01` entries with conflicting character counts and hashes.
- Observed converted and chunk hashes do not match the recorded metadata.
- `raw/sources/CV of Dario Arturo Pulgar.pdf` was absent at the recorded path during this pass.
- No `page-0005` rendered image was found under the conversion job tree; only page Markdown, visual JSON, and work order derivatives were present.

Action needed: restore or regenerate authoritative access to physical page 5, compare that image/PDF page against both derivative readings, repair the duplicate manifest/hash metadata through the conversion workflow, and then rerun proof review on any retained work-history and identity-bridge claims.
