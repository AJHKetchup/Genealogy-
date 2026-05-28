---
type: claim
status: draft
claim_type: relationship_attribute
subject: "Jose del Carmen Segundo Pulgar Arriagada"
predicate: "father_named_in_birth_registration"
object: "Jose del Carmen Pulgar; Chilean; employed; domiciled at Calle de Colipi"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-image-qa-postconv-evidence-extraction-20260527235532560.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
confidence: 0.80
promotion_recommendation: promote_after_review
---

# Atomic Claim: Entry 172 Father

## Literal Support

```text
Nombre del padre Jose del Carmen Pulgar S.
Nac Chileno
Prof Empleado
Dom Calle de Colipi
```

## Conversion Confidence / QA Concern

Image review certifies the father field only as `Jose del Carmen Pulgar`. The assigned chunk's terminal `S.` is not promoted by this claim because the final mark after `Pulgar` remains uncertain.

## Uncertainty

Do not promote the suffix `S.` from this extraction. The current converted Markdown names `Oswaldo Burgos` as father, but that row is not the image-controlled entry `172`.
