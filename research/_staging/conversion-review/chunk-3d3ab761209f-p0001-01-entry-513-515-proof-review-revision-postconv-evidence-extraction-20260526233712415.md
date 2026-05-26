---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
worker: postconv-evidence-extraction-20260526233712415
source_packet: "research/_staging/source-packets/chunk-3d3ab761209f-p0001-01-entry-513-pulgar-hold-postconv-evidence-extraction-20260526233712415.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_sha256: "05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
page_reference: "image page 1; register page 172; entries 513-515"
confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 513-515 Proof Review Revision

## Entry 513 Family-Relevant Row

The image supports entry 513 as a Pulgar family birth registration. The father/declarant is visible as `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, father, age forty-seven, agriculturist, domiciled Calle Colon. The child-name field appears to begin with a `Pulgar Ama[...]` surname line and a `Jose [...]` given-name line. Sex is `Masculino`.

The following remain blocked for conversion QA:

- Child full name: chunk reads `Pulgar Amagada / Jose Luis`; converted file reads `Isolina del Carmen / Jose`; image supports the Pulgar row but not a promotion-ready complete name.
- Birth date/time: chunk reads 26 June 1889 at 4:30 p.m.; converted file reads same-day 22 June 1889 at 4:00 a.m.; image appears closer to 22 June 1889 at 4:30 p.m., but this must be resolved by targeted QA.
- Mother surname: chunk reads `Amagada`; converted file reads `Amador`; image supports `Ama[...] de Pulgar` but should not be used here to force a normalized surname.
- Canonical identity: no Dario/Pulgar, Arriagada, Amagada, or existing Jose/Juana merge is supported until the literal row is corrected and proof reviewed.

## Entry 514 Row-Control Context

Entry 514 is not family-relevant except as row-control context. The image supports a Riquelme child row and a mother/declarant Mercedes Riquelme. Prior staged notes already report conflicts over child name, father field, place, and witness names. Do not promote non-family claims from this extraction task.

## Entry 515 Row-Control Context

Entry 515 is not a Pulgar row. It remains useful only to confirm that lower-row Neira/Leiva-style derivative conflicts do not spill into entry 513. The visible image supports a Neira-style row and an emendation note, but mother-field completeness remains limited.

## Recommendation

Keep all new entry 513 source packet, claims, and relationship candidate on `hold_for_conversion_qa`. The next action is targeted row-level conversion QA against the original image and derivative transcripts, followed by proof review of atomic claims only after QA issues stable corrected readings or explicit uncertainty markers.
