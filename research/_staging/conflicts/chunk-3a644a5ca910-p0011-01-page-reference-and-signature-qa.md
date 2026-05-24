---
type: conflict_candidate
status: draft
conflict_type: conversion_page_reference_and_signature_reading
subject: "El Fundo Los Cuartos page for Dr. Dario Pulgar A."
source_packet: "research/_staging/source-packets/chunk-3a644a5ca910-p0011-01-dario-pulgar-a-fundo-los-cuartos.md"
source: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0011-chunk-01.md"
chunk_id: CHUNK-3a644a5ca910-P0011-01
page_reference: "assigned source page 11; chunk metadata says printed page 14"
confidence: medium
promotion_recommendation: hold_for_conversion_qa
---

# Conflict Candidate: Page Reference And Signature QA

- Issue: The controller assignment and chunk filename point to page 11, while the chunk metadata and matching conversion-job markdown identify the article as printed page 14.
- Issue: The signature is transcribed as `DR. DARIO PULGARA`; this may represent `Dr. Dario Pulgar A.` and should not be promoted without image review.
- Evidence checked: the assigned chunk and the aggregate converted file contain the same article text; `page-markdown/page-0014.md` also contains the same article, while `page-markdown/page-0011.md` contains a different article about electricity and milk processing.
- Conversion confidence/QA concern: medium; the local page-images directory only contains `page-0004.jpg` despite the manifest listing page images through page 18.
- Promotion recommendation: hold related claims for conversion QA.
