---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
source_packet: "research/_staging/source-packets/sp-chunk-3d3ab761209f-p0001-01-los-angeles-birth-register-page-172.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_sha256: "05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
page_reference: "image page 1; register page 172; entries 513-515"
conversion_confidence: mixed
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review Revision Note: Register Page 172

## Revision Scope

This note responds to the proof-review holds for staged entry 513 and 514 claims. It does not alter the raw source image, assembled converted Markdown, assigned chunk, or page Markdown.

## Literal Support And Current Reading

- Page heading visible in the image: `1889.-Rejistro de NACIMIENTOS en la Circunscripcion de Los Anjeles, num. 1o de La Laja`.
- Entry 513: the image supports the Pulgar family row, father `Jose del Carmen Pulgar`, domicile `Calle Colon`, male sex, and mother line beginning `Juana de Dios ... de Pulgar`; the child given-name line and maternal surname remain image-sensitive.
- Entry 513 birth field: image review appears closer to `Junio veinte i dos` than the assigned chunk's `Junio veinte i seis`; the time phrase appears closer to `a las cuatro i media ... tarde` than the assembled converted file's `a las cuatro de la manana`, but it should still be checked from a targeted crop.
- Entry 514: the image supports father field `Se ignora`, mother/declarant `Mercedes Riquelme`, and a male child in the Riquelme row; the child surname suffix, witness surname, and `Lugar` spelling remain QA-sensitive.
- Entry 515: the visible upper row supports `Neira Ulloa / Laura de la Cruz`, father/declarant `Pedro Pablo Neira`, and right-column note `Neira=emendado= / vale=`, but the lower mother field is not sufficiently visible in the available image.

## Conversion Confidence And QA Concern

The assigned chunk and assembled converted Markdown remain materially inconsistent:

- Entry 513 child: assigned chunk `Pulgar Amagada / Jose Luis`; converted Markdown `Isolina del Carmen / Jose`.
- Entry 513 birth date/time: assigned chunk `Junio veinte i seis ... a las cuatro i media de la tarde`; converted Markdown `El mismo veinte dos ... a las cuatro de la manana`; image review currently favors `Junio veinte i dos` and likely `cuatro i media ... tarde`, but does not settle the time enough for promotion.
- Entry 513 mother: assigned chunk `Juana de Dios Amagada de Pulgar`; converted Markdown `Juana de Dios Amador de Pulgar`; image review does not fully settle the surname.
- Entry 514 child/place/witness: assigned chunk `Riquelme Aviles / Juan Bautista`, `Calle Sanegueso`, `Benjamin Utiera`; converted Markdown `Riquelme Juan Teodoro`, `Calle Saneguin`, `Benjamin Utrosa`.
- Entry 514 father: image and assigned chunk support `Se ignora`; converted Markdown reads `Belisario Riquelme` in the father field and should not be used as a father-child relationship from this evidence packet.
- Entry 515 mother: assigned chunk `Carmen Ulloa`; converted Markdown `Carmen Leiva`; image crop does not visibly confirm the full lower mother field.

## Staging Decision

All staged claims and relationship candidates for this chunk should remain at `hold_for_conversion_qa`, except the entry 514 father-negative relationship candidate, which remains `do_not_promote` as a tree relationship. The grouped atomic-claims overview has been revised so it no longer contains stale `Promote after review` recommendations.

## Uncertainty

Do not normalize names, surname order, street names, time of birth, or officer signatures from this packet until a targeted conversion-QA pass reconciles the source image with both derivative transcripts. Entry 514 `Se ignora` is negative evidence for this registration only, not proof that no father was ever identified.
