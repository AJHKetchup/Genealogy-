---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
source_packet: "research/_staging/source-packets/CHUNK-3d3ab761209f-P0001-01-source-packet.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_sha256: "05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
page_reference: "image page 1; register page 172; entries 513-515"
conversion_confidence: mixed
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Register Page 172, Entries 513-515

## Literal Support

Limited image review supports the page heading as `Los Anjeles, num. 1o de La Laja`, entry 514 father field as `Se ignora`, and the entry 515 marginal/emendation note as `Neira=emendado= / vale=`.

For entry 513, the image supports the Pulgar family row and male sex, but the child given-name line, maternal surname, and birth time remain difficult enough to keep all related person and relationship drafts on hold.

## Conversion Confidence And QA Concern

The assigned chunk and assembled converted Markdown are derivative transcripts of the same image, but they materially disagree:

- Entry 513 child: assigned chunk `Pulgar Amagada / Jose Luis`; assembled converted Markdown `Isidoro del Carmen Diaz`.
- Entry 513 birth date/time: assigned chunk `Junio veinte i seis ... a las cuatro i media de la tarde`; assembled converted Markdown `veinte i dos ... a las cuatro i veinte de la tarde`; image review appears closer to `Junio veinte i dos` and likely `cuatro i media de la tarde`, while the time phrase still needs targeted review.
- Entry 513 mother: assigned chunk `Juana de Dios Amagada de Pulgar`; assembled converted Markdown `Juana de Dios Amador de Pulgar`.
- Entry 514 father: assigned chunk and image `Se ignora`; assembled converted Markdown places `Mercedes Riquelme` in the father field.
- Entry 514 witness/place: assigned chunk `Benjamin Utiera` and `Calle Sanegueso`; assembled converted Markdown `Benjamin Utrosa`, `Ignacio Jara`, and `Calle Panquehue`.
- Entry 515 child/father/mother: assigned chunk `Neira Ulloa / Laura de la Cruz`, `Pedro Pablo Neira`, `Carmen Ulloa`; assembled converted Markdown `Rosa Elvira del Carmen`, `Pedro Pablo Leiva`, `Carmen Leiva`; available image does not fully confirm the lower mother field.

## Uncertainty

This note does not correct the raw source, converted Markdown, chunk Markdown, or page Markdown. It records the current disagreement for follow-up QA. Do not promote the entry 513 child identity, entry 513 parent-child links, entry 514 witness/place readings, or entry 515 mother relationship until targeted conversion QA resolves the image-sensitive fields.

## Promotion Recommendation

`hold_for_conversion_qa`: use this note as a staging blocker and correction map for proof review. The only high-value negative evidence supported in this pass is entry 514's father field `Se ignora`, and it should be handled as negative evidence rather than a tree relationship.
