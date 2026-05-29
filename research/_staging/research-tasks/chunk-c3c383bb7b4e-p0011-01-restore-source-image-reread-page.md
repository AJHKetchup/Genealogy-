---
type: research_task
status: draft
task_type: conversion_source_image_qa
task_id: "evidence-extraction:CHUNK-c3c383bb7b4e-P0011-01"
worker: "postconv-evidence-extraction-20260529152951312"
subject: "Restore source/page image and reread Darío J. Pulgar Arriagada listing"
source_packet: "research/_staging/source-packets/chunk-c3c383bb7b4e-p0011-01-dario-j-pulgar-arriagada-medico-cirujano.md"
source: "raw/sources/Anales de la Universidad de Chile, Session of the Council of Public Instruction, September 1918..pdf"
converted_file: "raw/converted/ca753b8b14-anales-de-la-universidad-p0004-0023-anales-de-la-universidad-de-chile-session-of-the-council-of-public-instruction-september-1918-pages-4-23.codex.md"
chunk: "raw/chunks/ca753b8b14-anales-de-la-universidad-p0004-0023-anales-de-la-universidad-de-chile-sess-af33a57786/page-0011-chunk-01.md"
chunk_id: "CHUNK-c3c383bb7b4e-P0011-01"
page_reference: "source page 11"
priority: high
confidence: medium
promotion_recommendation: "hold_for_conversion_qa"
---

# Research Task: Restore Source/Page Image For Reread

Objective: restore the source PDF or rendered page image for page 11 and complete the controller-requested `reread-page` check before any canonical claim is promoted.

Derivative support to verify:

```text
Sesion de 2 de Setiembre de 1918
```

```text
Médicos-Cirujanos:
```

```text
» Darío J. Pulgar Arriagada
```

Conversion confidence/QA concern: medium. The assigned chunk and conversion page Markdown agree, but the current workspace lacks both the task source PDF and any local page image. This task should specifically verify the full name, the middle initial `J.`, the title heading, and the session/title-conferral context.

Uncertainty: the derivative text does not expand `J.` and does not state parents, spouse, children, age, residence, or a same-person bridge to other Pulgar candidates.

Promotion recommendation: keep the source packet and professional-title claim at `hold_for_conversion_qa` until this reread is completed. Do not promote a relationship or identity merge from this page.
