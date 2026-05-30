---
type: conversion_review_note
status: blocked
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: postconv-evidence-extraction-20260530042028956
subject: "Entry 172 row-control QA"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 QA Blocked

Targeted conversion QA was requested by prior proof review. This worker compared the assigned chunk, current converted Markdown, manifest, page-markdown file, and available staged review assets.

## Findings

- The assigned chunk records entry `172` as the Pulgar/Arriagada row: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`.
- The current converted Markdown and page-markdown file record entry `172` as a different Burgos/de la Cruz row: child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at about 10 p.m. at `En esta`.
- The manifest points to `raw/codex-conversion-jobs/.../page-images/page-0001.png`, but that page image is not present in this checkout.
- The raw source PNG named in the manifest/source packet is not present under `raw/sources` in this checkout.
- Existing cropped review assets show a Pulgar/Arriagada parent/informant section and support a father field beginning `Jose del Carmen Pulgar`, but the crop does not include enough full-page context to certify row number/control by itself.

## QA Conclusion

This pass cannot certify which physical row controls entry `172` from the original image. It can only preserve the disagreement and stage dependent evidence at `hold_for_conversion_qa`.

The father field should not be promoted as `Jose del Carmen Pulgar S.` in this pass. Preserve it as `Jose del Carmen Pulgar [?]` or "at least Jose del Carmen Pulgar, suffix unresolved" until full-image QA certifies the visible suffix.

## Required Next Step

Restore or locate the original source image or full page image for SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, then rerun targeted conversion QA to certify row control and father-field suffix before proof review or canonical promotion.
