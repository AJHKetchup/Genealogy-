---
type: conversion_review_note
status: blocked
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530110059001"
subject: "Entry 172 targeted conversion QA blocker"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
reported_source_path: "raw/sources/Registro de Nacimientos, CircunscripciÃ³n de Los Ãngeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530110059001.md"
conversion_confidence: derivative_conflict_full_image_not_available
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 QA Blocked

Proof review requested targeted QA against the original page image, assigned chunk, current converted Markdown, and source packet.

## Finding

- The assigned chunk records entry `172` as the Pulgar/Arriagada birth row.
- The current converted Markdown records entry `172` as a Burgos/de la Cruz row.
- The reported source PNG is absent from `raw/sources` in this checkout, and no PNG for this source was found under `raw`.
- Without the full source image, this worker cannot certify which physical row controls entry `172`.

## QA Conclusion

The evidence remains blocked. Dependent source packets, claims, relationship candidates, and identity/conflict notes should stay at `hold_for_conversion_qa`.

Preserve the father field only as `Jose del Carmen Pulgar` in staged claims. Do not promote `Jose del Carmen Pulgar S.` or infer an expanded suffix until full-image row-control QA certifies the terminal mark.

## Required Follow-Up

Restore or locate the full source image for SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, then rerun targeted conversion QA and proof review before any canonical claim, relationship, identity merge, Dario-line attachment, or wiki update.
