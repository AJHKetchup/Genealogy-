---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0004-01
worker: postconv-evidence-extraction-20260527120035293
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0004-01
chunk_manifest: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json
page_reference: page 4
literal_support: "Derivative chunk text preserves 1988-1989 FAO / Ndola, Zambia / Training and Communication Advisor; 1988 CIDA / Ethiopia / Communication Consultant; 1986-1987 WIF / Rome, Italy / Rural Communications and Extension Advisor; 1982-1985 Independent communications consultant / Canadian International Development Agency."
conversion_confidence: low_for_page_control
conversion_qa_concern: "The chunk manifest lists CHUNK-fb0a0000636f-P0004-01 twice for the same page/path with different chars and sha256 values. Proof review reports that the existing rendered page-4 image and current converted page 4 support 2000 IBRD and 1999-2000 Antamina text, not the 1982-1989 entries preserved in the referenced chunk/source packet."
uncertainty: "High for using any 1982-1989 employment claim as page-4 evidence until targeted source-prep/conversion QA reconciles the duplicate manifest records, current chunk hash, converted file page sequence, and physical page image."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Page 4 Proof Review Revision

This revision preserves the disagreement between derivative transcripts and image-reviewed evidence. The referenced chunk file is internally readable and supports staged occupational claims for the CV subject, identified by document title as Dario Arturo Pulgar, for FAO in Ndola in 1988-1989, CIDA in Ethiopia in 1988, WIF in Rome in 1986-1987, and independent communications consulting for CIDA in 1982-1985.

Those claims must remain held. The manifest has duplicate `CHUNK-fb0a0000636f-P0004-01` entries for the same path/page, and prior proof review found that the rendered page-4 image/current converted page 4 instead support a 2000 IBRD entry and a 1999-2000 Antamina entry. The converted file later also contains the 1982-1989 text after the page-6 section, but this extraction task cannot decide the controlling physical page or edit conversion outputs.

## Staged Drafts Reviewed

- `research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md` already has `promotion_recommendation: hold_for_conversion_qa`.
- Atomic claims `chunk-fb0a0000636f-p0004-01-001` through `005` already have `promotion_recommendation: hold_for_conversion_qa` and should not be proof-promoted until page control is corrected.
- `research/_staging/relationships/chunk-fb0a0000636f-p0004-01-no-family-relationship-stated.md` remains a negative relationship note with `promotion_recommendation: do_not_promote`.
- `research/_staging/research-tasks/chunk-fb0a0000636f-p0004-01-conversion-qa-needed-20260527114912066.md` already requests targeted conversion QA and remains the proper next action.

## Required Next Action

Run targeted source-prep/conversion QA outside this evidence-extraction task. Reconcile the duplicate manifest entries, determine which physical page controls the 1982-1989 employment text, regenerate affected source packets or staged claims through the normal workflow, and rerun proof review before any canonical claim, relationship, merge, or wiki update.
