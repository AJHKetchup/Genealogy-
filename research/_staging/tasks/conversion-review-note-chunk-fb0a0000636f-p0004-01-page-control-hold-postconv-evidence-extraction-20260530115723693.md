---
type: research_task
status: draft
task_id: "evidence-extraction:CHUNK-fb0a0000636f-P0004-01"
worker: "postconv-evidence-extraction-20260530115723693"
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
literal_support: "Derivative chunk text preserves 1988-1989 FAO/Ndola, 1988 CIDA/Ethiopia, 1986-1987 WIF/Rome, WIF project countries, and 1982-1985 independent communications consultant entries. Current converted Markdown also contains 2000 IBRD/Bolivia, Peru and 1999-2000 Antamina/Huarmey, Peru text near the earlier page-4 section."
conversion_confidence: low_for_page_control
conversion_qa_concern: "The assigned chunk, current converted Markdown, duplicate chunk manifest records, prior image-reviewed page-control evidence, and absent page-4 image still disagree. This evidence-extraction revision cannot determine which physical page controls the 1982-1989 entries."
uncertainty: "This note preserves the conflict and does not edit raw sources, converted Markdown, chunks, or page Markdown. Source-prep/conversion QA must restore or regenerate page control before any dependent claim can be promoted."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: CHUNK-fb0a0000636f-P0004-01 Page-Control Hold

The staged packet and atomic claims for Dario Arturo Pulgar's derivative 1982-1989 work-history entries remain blocked for conversion QA.

The assigned chunk currently contains the 1988-1989 FAO/Ndola entry, the 1988 CIDA/Ethiopia entry, the 1986-1987 WIF/Rome entry with project countries, and the 1982-1985 independent communications consultant entry. The current converted Markdown also contains 2000 IBRD / Bolivia, Peru and 1999-2000 Antamina / Huarmey, Peru entries near its earlier page-4 section, while the 1982-1989 entries appear later in the converted file. This preserves the derivative transcript conflict rather than resolving it.

The chunk manifest repeats `CHUNK-fb0a0000636f-P0004-01` for the same path/page with different counts and hashes, and neither manifest hash matches the current on-disk chunk hash. The current converted file hash also does not match the converted hash recorded in the chunk front matter. The expected page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0004.jpg` was absent during this revision.

Do not promote the dependent source packet or claims. The next source-prep/conversion QA step should restore or regenerate `page-0004.jpg`, reconcile the duplicate manifest entries and current file hashes, determine which physical page contains the 1982-1989 text, and then regenerate or refresh staged claims before proof review.
