---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
source_packet: "research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_sha256: "05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md"
chunk_id: "CHUNK-bdb698de8106-P0001-01"
page_reference: "image page 1; register page 172; entries 513-514"
confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entries 513 And 514

## Literal Support Basis

The assigned chunk is the bdb698de8106 page-1 chunk for a civil birth-register page headed `Páj. 172` and `1889.—Rejistro de NACIMIENTOS en la Circunscripcion de Los Anjeles, núm. 1º de La Laja`. The converted table includes entries 513, 514, and 515.

## Disagreement To Preserve

- Entry 513 child: the converted transcript reads `Isolina del Carmen / José` with `Sexo. Masculino`; image-review notes instead report a child-name field beginning `Pulgar Ama...` with a given-name line beginning `Jose ...`. Sex `Masculino` is supported, but the child identity is not resolved.
- Entry 513 birth event: the converted transcript reads `El mismo veinte dos ... a las cuatro de la mañana` and `Calle Colon`; proof-review revision asks QA to reconcile child identity, sex, birth date, birth time, and place directly against the image before retaining the place.
- Entry 513 parents/declarant: the converted transcript reads father `José del Carmen Pulgar`, mother `Juana de Dios Amador de Pulgar`, and declarant `José del C. Pulgar`, age 47, `Agricultor`, `Calle Colon`. Image-review notes support the father/declarant core but keep the mother surname and declarant profession in dispute.
- Entry 514 child: the converted transcript reads `Riquelme Juan Teodoro`; proof-review revision notes unresolved alternatives including `Rigoberto Juan Bautista` and `Riquelme / Juan Bautista`. Preserve `Sexo. Masculino` as supported, but do not create a canonical child identity.
- Entry 514 father/place: the converted transcript reads father `Belisario Riquelme` and `Calle Saneguin`; image review suggests the father field may read `Se ignora` and the street spelling remains uncertain.

## Recommendation

The revised staged claims and relationships should remain at `hold_for_conversion_qa` except the unsupported entry-514 father/two-parent assertions, which should remain `do_not_promote` as tree links. A corrected transcription or targeted crop QA is needed before proof review can promote any canonical child identity or parent-child relationship from entries 513-514.
