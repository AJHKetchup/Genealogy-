---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-c3c383bb7b4e-P0011-01"
worker: "postconv-evidence-extraction-20260529152333626"
subject: "Page 11 source/image QA needed for Darío J. Pulgar Arriagada Médico-Cirujano listing"
source: "raw/sources/Anales de la Universidad de Chile, Session of the Council of Public Instruction, September 1918..pdf"
source_sha256: "753b8b140d94a0c3927cace4e9083609cfd845260d89f8068122337b7498171d"
converted_file: "raw/converted/ca753b8b14-anales-de-la-universidad-p0004-0023-anales-de-la-universidad-de-chile-session-of-the-council-of-public-instruction-september-1918-pages-4-23.codex.md"
chunk: "raw/chunks/ca753b8b14-anales-de-la-universidad-p0004-0023-anales-de-la-universidad-de-chile-sess-af33a57786/page-0011-chunk-01.md"
chunk_id: "CHUNK-c3c383bb7b4e-P0011-01"
page_reference: "source page 11"
conversion_confidence: "medium_derivative_text_only"
promotion_recommendation: "hold_for_conversion_qa"
---

# Targeted Conversion QA Note: Page 11

The assigned chunk and conversion page Markdown consistently transcribe a 2 September 1918 Council of Public Instruction session in which the Rector conferred titles and degrees. Under `Médicos-Cirujanos`, the derivative text lists `Darío J. Pulgar Arriagada`.

The extraction remains held because the task was flagged `reread-page`, but this workspace does not contain the task source PDF at `raw/sources/Anales de la Universidad de Chile, Session of the Council of Public Instruction, September 1918..pdf`. It also does not contain the rendered page image named in `raw/codex-conversion-jobs/.../page-markdown/page-0011.visuals.json`: `raw/codex-conversion-jobs/ca753b8b14-anales-de-la-universidad-p0004-0023-anales-de-la-universidad-de-chile-session-of-the-council-of-public-instruction-september-1918-pages-4-23/page-images/page-0011.jpg`.

Derivative support to verify against the page image:

- `Sesion de 2 de Setiembre de 1918`
- `Previas las formalidades reglamentarias i el juramento requerido el señor Rector confirió los siguientes títulos i grados:`
- `Médicos-Cirujanos:`
- `» Darío J. Pulgar Arriagada`

Do not promote canonical claims or identity bridges from this page until source/image QA confirms the name, the initial `J.`, and the title-conferral context. The page does not state parents, spouse, children, residence, birth date, or any same-person bridge to other Dario Pulgar or Pulgar-Arriagada candidates.
