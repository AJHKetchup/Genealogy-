---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
worker: postconv-evidence-extraction-20260527045039396
source_title: Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1889, page 172
source_type: civil_birth_register
record_type: birth_register_page
jurisdiction: Los Angeles, La Laja, Chile
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_sha256: 05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
converted_sha256: bdb698de810680fda5a8207dc19746550a2bfbba789d92ab01a18646d925b060
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
chunk_manifest: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/manifest.json
page_reference: page 1; register page 172; entries 513-515
page_start: 1
page_end: 1
family_relevance: high
matched_family_terms: [Pulgar]
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Revision: Entry 513 Pulgar Birth Row

## Person-First Focus

Entry 513 is relevant to the Pulgar family because the father and declarant fields identify `Jose del Carmen Pulgar` / `Jose del C. Pulgar`. The row may eventually support a birth event and parent-child relationship, but the child identity, birth date/time, and mother surname are still not stable enough for canonical promotion.

Entry 515 is retained only as a row-boundary check. It appears below the Pulgar row and should not be used for Pulgar-family inference except to prevent spillover from adjacent rows.

## Literal Support From Converted Chunk

```text
513 ... Nombre. Isolina del Carmen / Jose ... Sexo. Masculino
Fecha. El mismo veinte dos de mil ochocientos ochenta i nueve, a las cuatro de la mañana. Lugar. Calle Colon
Nombre del padre. Jose del Carmen Pulgar ... Prof. Agricultor ... Domicilio. Calle Colon
Nombre de la madre. Juana de Dios Amador de Pulgar ...
Jose del C. Pulgar ... Padre ... Edad. Cuarenta i siete Años ... Prof. Agricultor ... Dom. Calle Colon
```

## Targeted Image Review Notes

```text
513 child name appears to begin Pulgar Rosa ... with following given-name lines uncertain; the converted Isolina del Carmen reading is not supported by this image review. Sex reads Masculino.
513 birth field appears to read Junio veinte i dos ... de mil ochocientos ochenta i nueve, a las cuatro i media de tarde. Place reads Calle Colon.
513 father reads Jose del Carmen Pulgar; father nationality/profession/domicile read Chileno, Agricultor, Calle Colon.
513 declarant reads Jose del C. Pulgar, Padre, Edad Cuarenta i siete Anos, Prof. Agricultor, Dom. Calle Colon.
513 mother reads Juana de Dios Ama[?]gar or Ama[?]gada de Pulgar; the converted Amador reading is not secure.
515 lower row confirms a separate non-Pulgar entry boundary; no Pulgar-family claim should be inferred from entry 515.
```

## Conversion Confidence / QA Concern

Low. The image-reviewed evidence materially disagrees with the converted transcript in identity-controlling fields. Father/declarant Pulgar, Agricultor, Calle Colon, and sex Masculino are comparatively legible, but the child name, mother surname, and birth month/time require a formal conversion-review correction or uncertainty-marked transcription before proof review can promote claims.

## Uncertainty

Do not normalize the child name or the mother surname from this packet. Preserve the mother surname as `Ama[?]gar` / `Ama[?]gada` until conversion QA settles the letters. Do not promote `Amador`, `Amagada`, or `Arriagada` from this packet alone.

## Promotion Recommendation

`hold_for_conversion_qa`. Rerun proof review after conversion QA creates a stable corrected transcription or explicit uncertainty markers for entry 513.
