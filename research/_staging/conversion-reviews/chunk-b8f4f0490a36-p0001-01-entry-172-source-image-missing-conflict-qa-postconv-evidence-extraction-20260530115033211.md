---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530114928256"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
conversion_confidence: "derivative_conflict_unresolved_source_image_missing"
conversion_qa_concern: "The assigned chunk records entry 172 as the Pulgar/Arriagada row, but the current converted Markdown records entry 172 as a Burgos/de la Cruz row. The expected original/page image was not available at the source path or conversion-job page-images path in this worker run, so this worker cannot independently certify physical row control."
promotion_recommendation: hold_for_conversion_qa
---

# Targeted Conversion QA Note: Entry 172

This revision preserves the disagreement between derivative transcripts and does not certify row control from the image.

## Files Checked

- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Chunk manifest: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json`
- Conversion-job manifest: `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/manifest.json`

The manifest points to `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png`, but that file is not present in the current workspace. The expected `raw/sources/...Entry No. 172;.png` file is also not locatable by this worker run.

## Derivative Transcript Conflict

The assigned chunk's row for entry `172` reads as a Pulgar/Arriagada birth registration:

```text
172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. ... Nombre de la madre Juana Arriagada de Pulgar ... | Ernesto Herrera L. Presente al nacimiento ...
```

The current converted Markdown's entry `172` reads as a different birth registration:

```text
Nombres. Jose Miguel; father Oswaldo Burgos; mother Concepcion de la Cruz; born seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche, En esta.
```

These are not variant readings of the same row. They are materially different children, parents, dates, places, and informants.

## QA Result

Row control remains unresolved in this worker run because the source image was unavailable for direct reread. The family-relevant Pulgar/Arriagada evidence should remain staged only as derivative chunk-supported evidence, with the converted Markdown conflict attached and with `promotion_recommendation: hold_for_conversion_qa`.

Do not promote canonical claims, parent-child relationships, identity merges, Dario-line attachments, or wiki updates until a later worker restores or locates the source image and proof review accepts a targeted row-control QA.
