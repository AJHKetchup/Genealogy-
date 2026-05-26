---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
worker: postconv-evidence-extraction-20260526234347596
source_id: ca05d0627a-los-angeles-birth-register-1889-page-172-entry-513-515
title: "Los Angeles, Chile civil birth register, 1889, register page 172, entries 513-515"
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_sha256: "05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
page_reference: "image page 1; register page 172; entries 513-515"
family_relevance: high
matched_family_terms:
  - Pulgar
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Revision: Register Page 172, Entries 513-515

## Person-First Relevance

Entry 513 is the family-relevant row because it names a Pulgar household. The page may eventually support claims about a child in the Pulgar family, father/declarant Jose del Carmen Pulgar, and mother Juana de Dios ... de Pulgar, but the child name and maternal surname are still conversion-sensitive.

## Source And Derivative References

- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Converted file: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md`
- Chunk id: `CHUNK-3d3ab761209f-P0001-01`
- Chunk manifest: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/manifest.json`

## Literal Support

- Page heading visible in the image: `1889.- Rejistro de NACIMIENTOS en la Circunscripcion de Los Anjeles, num. 1o de La Laja`.
- Register page: `Paj. 172`.
- Entry 513 registration number is visible.
- Entry 513 registration date is visible as July 22, 1889 in Spanish wording.
- Entry 513 child surname line begins `Pulgar Ama...`; the following given-name line is not safely read as the derivative `Jose Luis` and appears closer to `Rosa Da...` or similar on image review. The sex field reads `Masculino`.
- Entry 513 birth field supports June 1889 wording, time `a las cuatro i media de tarde`, and place `Calle Colon`; the exact day remains a QA target because derivative layers disagree.
- Entry 513 father field supports `Jose del Carmen Pulgar`; the declarant field supports `Jose del C. Pulgar`, `Padre`, age about 47, agriculturist, domicile `Calle Colon`.
- Entry 513 mother field supports `Juana de Dios ... de Pulgar`; the surname between `Dios` and `de Pulgar` remains image-sensitive and should not be normalized to Amagada, Amador, or Arriagada without targeted QA.
- Entry 514 is visible as a separate non-Pulgar row. The image supports father field `Se ignora`, mother/declarant `Mercedes Riquelme`, and child `Riquelme / Juan Bautista`; this is useful as a conflict-control row only.
- Entry 515 is partly visible and appears to support `Neira Ulloa / Laura de la Cruz`, father/declarant `Pedro Pablo Neira`, and the marginal correction `Neira=emendado= / vale=`, but lower-row completeness remains a blocker for its mother field.

## Conversion Confidence And QA Concern

Promotion remains blocked. The chunk transcription reads entry 513 child as `Pulgar Amagada / Jose Luis`, mother as `Juana de Dios Amagada de Pulgar`, and birth as June 26 at 4:30 p.m. Image review supports a Pulgar row and the Jose del Carmen/Juana de Dios parental context, but does not securely confirm the child given name, maternal surname, or exact birth day. The image also contradicts earlier derivative conflicts for entry 514 that named a father rather than `Se ignora`.

## Uncertainty

This packet should be used as a correction map, not as a canonical source packet. Do not attach entry 513 to Dario/Pulgar identity clusters, do not infer `Amagada` as `Arriagada`, and do not promote entry 515 mother claims until targeted row-level conversion QA records a certified reading.

## Promotion Recommendation

`hold_for_conversion_qa`: rerun proof review only after a targeted image QA note resolves or explicitly preserves uncertainty for entry 513 child full name, entry 513 birth day/time, entry 513 mother surname, and entry 515 lower-row mother field.
