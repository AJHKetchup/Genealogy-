---
type: conversion_review_note
status: blocked
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530073343003"
subject: "Entry 172 row-control QA"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530073343003.md"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 QA Still Blocked

Prior proof review requested targeted conversion QA against the original page image, assigned chunk, current converted Markdown, and source packet.

## Findings

- The assigned chunk records entry `172` as the Pulgar/Arriagada row: child `Jose del Carmen Segundo Pulgar Arriagada`, father transcribed as `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`.
- The current converted Markdown records entry `172` as a different Burgos/de la Cruz row: child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at about 10 p.m. at `En esta`.
- The raw source PNG was not found in `raw/sources` in this checkout.
- The conversion job directory contains the manifest, page Markdown, visual JSON, and work order, but no page image.
- Existing staged crop assets support the Pulgar/Arriagada parent and informant fields at crop level. They do not include enough full-page context to certify the row number/control.

## QA Conclusion

This worker cannot certify which physical row controls entry `172` from the original full image. The dependent source packet, claims, and relationship candidates remain staged at `hold_for_conversion_qa`.

Preserve the father field only as `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar [?]`; do not promote `Jose del Carmen Pulgar S.` until full-image QA certifies the suffix.

## Required Next Step

Restore or locate the original full page/source image for SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, then rerun targeted conversion QA and proof review before any canonical claim, relationship, identity merge, Dario-line attachment, or wiki update.

