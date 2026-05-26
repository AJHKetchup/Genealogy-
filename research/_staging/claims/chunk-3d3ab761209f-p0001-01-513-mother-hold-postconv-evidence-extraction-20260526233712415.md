---
type: claim
status: draft
claim_type: parent_context
subject: "Juana de Dios Ama[...] de Pulgar"
predicate: "is_named_as_mother_for"
object: "entry 513 Pulgar child (identity unresolved)"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_packet: "research/_staging/source-packets/chunk-3d3ab761209f-p0001-01-entry-513-pulgar-hold-postconv-evidence-extraction-20260526233712415.md"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
page_reference: "image page 1; register page 172; entry 513"
confidence: 0.35
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Atomic Claim: Entry 513 Mother Hold

## Literal Support

The chunk reads:

```text
Nombre de la madre.
Juana de Dios Amagada de Pulgar
Nac. Chilena Prof. Labores de su sexo
Domicilio. Calle Colon
```

The converted file conflicts:

```text
Nombre de la madre.
Juana de Dios Amador de Pulgar
Nac. Chilena Prof. Labores de su sexo
Domicilio. Calle Colon
```

Image review supports `Juana de Dios Ama[...] de Pulgar`, but the exact surname remains conversion-sensitive.

## Conversion Confidence / QA Concern

Low. This claim preserves the mother field as a held parent-context reading. The `Amagada` / `Amador` / possible `Arriagada` issue must not be silently normalized.

## Uncertainty

Do not promote this as a canonical mother identity or merge it with `Juana Arriagada de Pulgar` or `Juana de Dios Amagada de Pulgar` until targeted QA and identity proof review are complete.
