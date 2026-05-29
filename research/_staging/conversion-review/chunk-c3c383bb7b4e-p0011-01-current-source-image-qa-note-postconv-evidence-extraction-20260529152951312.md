---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-c3c383bb7b4e-P0011-01"
worker: "postconv-evidence-extraction-20260529152951312"
subject: "Current source/image QA status for Darío J. Pulgar Arriagada Médico-Cirujano listing"
source: "raw/sources/Anales de la Universidad de Chile, Session of the Council of Public Instruction, September 1918..pdf"
source_sha256: "753b8b140d94a0c3927cace4e9083609cfd845260d89f8068122337b7498171d"
converted_file: "raw/converted/ca753b8b14-anales-de-la-universidad-p0004-0023-anales-de-la-universidad-de-chile-session-of-the-council-of-public-instruction-september-1918-pages-4-23.codex.md"
converted_sha256: "c3c383bb7b4e241409abc58f697dfbdd88784c617e8f90a0241848564f52cae4"
chunk: "raw/chunks/ca753b8b14-anales-de-la-universidad-p0004-0023-anales-de-la-universidad-de-chile-sess-af33a57786/page-0011-chunk-01.md"
chunk_id: "CHUNK-c3c383bb7b4e-P0011-01"
page_reference: "source page 11"
conversion_confidence: "medium_derivative_text_only"
promotion_recommendation: "hold_for_conversion_qa"
---

# Current Conversion QA Note: Page 11

The current workspace supports only derivative-text extraction for this page. The assigned chunk and conversion page Markdown agree that page 11 contains a `Sesion de 2 de Setiembre de 1918`, states that the Rector `confirió los siguientes títulos i grados`, and lists `Darío J. Pulgar Arriagada` under `Médicos-Cirujanos:`.

The requested `reread-page` cannot be completed from the current files because the task source PDF is absent at `raw/sources/Anales de la Universidad de Chile, Session of the Council of Public Instruction, September 1918..pdf`, and no rendered page images are present under the conversion job. This supersedes any staged note that treats a local page-0011 image reread as currently verified.

## Literal Support To Verify

```text
Sesion de 2 de Setiembre de 1918
```

```text
Previas las formalidades reglamentarias i el juramento requerido el señor Rector confirió los siguientes títulos i grados:
```

```text
Médicos-Cirujanos:
```

```text
» Darío J. Pulgar Arriagada
```

## Promotion Guidance

Keep canonical promotion on hold for conversion/source QA. After the source PDF or page image is restored, verify the date, the `Médicos-Cirujanos` heading, the middle initial `J.`, and the full name `Darío J. Pulgar Arriagada`. This page should not be used for a same-person bridge, middle-name expansion, or family relationship.
