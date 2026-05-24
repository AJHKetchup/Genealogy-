---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
source_packet: "research/_staging/source-packets/sp-chunk-3d3ab761209f-p0001-01-proof-review-revision-20260524.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_sha256: "05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
page_reference: "image page 1; register page 172; entries 513-515"
confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Proof Review Revision

## Entry 513

Image review supports entry 513 as a Pulgar family birth registration. The child-name field begins with a surname line `Pulgar Ama...`; the given-name line appears to begin `Jose D...`; sex reads `Masculino`. Father/declarant is `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, and mother is `Juana de Dios ... de Pulgar`.

Blocked readings:

- Child full name: assigned chunk `Pulgar Amagada / Jose Luis`; assembled converted Markdown `Isolina del Carmen / Jose`; image supports a Pulgar surname line but needs a crop for the full given-name line.
- Birth date/time: assigned chunk `Junio veinte i seis ... cuatro i media de la tarde`; assembled converted Markdown `El mismo veinte dos ... cuatro de la manana`; image appears closer to `Junio veinte i dos ... cuatro i media ... tarde`, but exact day/time remains crop-sensitive.
- Mother surname: assigned chunk `Amagada`; assembled converted Markdown `Amador`; image favors `Amagada`, but surname should not be promoted without crop QA.
- Officer signature: derivative readings disagree and should not be normalized from this extraction task.

## Entry 514

Entry 514 is not a Pulgar family entry, but it explains the derivative conflict on the same page. Image review supports `Riquelme / Juan Bautista`, sex `Masculino`, father field `Se ignora`, mother/declarant `Mercedes Riquelme`, and a note that appears to say she asked that her name be recorded. It does not support promoting a father named Belisario Riquelme or a spouse/father inference from `Juan Soler` in the assembled converted Markdown.

Blocked readings include street name, witness surnames, and whether the child surname line includes any second surname.

## Entry 515

Entry 515 is not a Pulgar family entry. The visible image supports `Neira Ulloa / Laura de la Cruz` and father/declarant `Pedro Pablo Neira`; the right column includes `Neira=emendado= / vale=`. The lower mother field is not sufficiently secure for promotion from this task.

## Recommendation

Keep the revised entry-513 Pulgar claims and relationship candidate on `hold_for_conversion_qa`. The next action is a targeted crop QA pass for entry 513 child full name, birth date/time, and mother surname, plus entry 514 and lower entry 515 fields if this page is being corrected as a whole.
