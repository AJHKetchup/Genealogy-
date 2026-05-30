---
type: research_task
status: draft
task_id: "evidence-extraction:CHUNK-fb0a0000636f-P0004-01"
worker: "postconv-evidence-extraction-20260530103214813"
task_type: conversion_review_correction_note
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
source_sha256: "07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
converted_sha256_observed: "da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288"
converted_sha256_recorded_in_chunk: "fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md"
chunk_id: "CHUNK-fb0a0000636f-P0004-01"
current_chunk_sha256: "c8536868c8f59d4340eb31173302f11866a5475823353b2409109b0574980f15"
manifest_chunk_sha256_values: "5e6aed90f2420572473987255df4bbec4de8750bd2f9701a9b71b2896f27a43f; 504f69374f1d289f20e70388a7653b8f8673e10ae649490cb6df74fe04fc3112"
chunk_manifest: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json"
page_reference: "page 4"
page_image_expected: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0004.jpg"
page_image_present_during_revision: false
literal_support: "Derivative chunk text preserves 1988-1989 FAO/Ndola, 1988 CIDA/Ethiopia, 1986-1987 WIF/Rome, WIF project countries, and 1982-1985 independent communications consultant entries."
conversion_confidence: low_for_page_control
conversion_qa_concern: "Duplicate manifest records, a current chunk hash that matches neither manifest entry, changed converted-file hash, missing page-4 image, and prior proof-review reports that page-4 image/current converted evidence supports different 2000/1999-2000 text."
uncertainty: "This note preserves the disagreement between derivative transcripts and page-control review. It does not rerun source preparation, regenerate page images, edit raw/converted/chunk files, or certify the physical page containing the 1982-1989 entries."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: CHUNK-fb0a0000636f-P0004-01 Page Control Hold

This revision preserves the staged derivative evidence for Dario Arturo Pulgar's reported 1982-1989 work-history entries, but it does not make those entries promotion-ready.

The assigned chunk currently transcribes the 1982-1989 entries, while the manifest lists the same `CHUNK-fb0a0000636f-P0004-01` id/path twice with different character counts and hashes. The current on-disk chunk hash is `c8536868c8f59d4340eb31173302f11866a5475823353b2409109b0574980f15`, which matches neither manifest record. The current converted file hash is `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`, while the chunk front matter records `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`.

Prior proof review reported that physical page-4 control evidence showed 2000 IBRD / Bolivia, Peru and 1999-2000 Antamina / Huarmey, Peru entries rather than the derivative 1982-1989 entries. During this revision pass, the expected page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0004.jpg` was not present, so this evidence extractor cannot resolve page control.

Keep the source packet and all dependent atomic claims on `hold_for_conversion_qa`. The next source-prep/conversion QA step should restore or regenerate the page-4 image, reconcile the duplicate manifest entries and current hashes, decide which physical page contains the 1982-1989 text, and then regenerate or refresh the affected staged claims through the normal workflow before proof review.
