---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_sha256: 05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
page_reference: page 1; register page 172; entries 513-515
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Proof-Review Revision 2026-05-26

## Revision Scope

This evidence-extraction revision preserves the disagreement between the current derivative transcript and direct image-reviewed evidence. No raw source, converted Markdown, chunk Markdown, page Markdown, or canonical wiki page was edited.

## Current Staged State

The bdb source packet and entry 513 atomic drafts already cite the restored chunk path and use `promotion_recommendation: hold_for_conversion_qa`. That recommendation remains correct. The relevant staged claim set includes child name/sex, birth date/place, registration date, father, mother, declarant, and the child-parent relationship candidate for entry 513.

## Family-Relevant Evidence

Entry 513 is family-relevant because the row contains `Pulgar` in the father/declarant evidence. The current derivative transcript gives:

```text
Nombre del padre. José del Carmen Pulgar
Nombre de la madre. Juana de Dios Amador de Pulgar
José del C. Pulgar
Padre
Edad. Cuarenta i siete Años
Prof. Agricultor
Dom. Calle Colon
```

Direct image reread supports a Pulgar father/declarant appearance in entry 513, but it does not make the row promotion-ready. The child-name field visibly conflicts with converted `Isolina del Carmen José`, and the mother's surname remains unresolved between the converted `Amador` reading and image-sensitive `Amagada`/`Arriagada`-style alternatives.

## Blocking QA Issues

- Entry 513 child identity is not settled, so no canonical child page, name variant, birth event, or parent-child relationship should be promoted.
- Entry 513 mother identity is not settled because the surname is image-sensitive and may not match the converted `Amador` reading.
- Entry 513 father/declarant is comparatively stronger evidence for a `José del Carmen Pulgar` / `José del C. Pulgar` appearance, but the complete claim remains blocked until conversion QA confirms the row fields.
- Entry 515 remains partial in the source image and conflicts with converted `Rosa Elvira del Carmen` / `Pedro Pablo Leiva`; it should not be promoted and should not be used to infer context for entry 513.

## Required Next Step

Use `research/_staging/tasks/task-chunk-bdb698de8106-p0001-01-conversion-qa-followup-revision-20260526.md` for targeted conversion QA. After QA certifies the corrected row-level transcription, rerun proof review on the separate atomic claims before any canonical promotion, merge, rename, or tree attachment.

## Promotion Recommendation

Keep all bdb entry 513 and entry 515 staged drafts on `hold_for_conversion_qa`.
