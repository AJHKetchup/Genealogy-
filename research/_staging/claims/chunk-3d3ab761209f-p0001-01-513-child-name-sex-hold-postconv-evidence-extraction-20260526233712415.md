---
type: claim
status: draft
claim_type: identity_context
subject: "entry 513 Pulgar child (identity unresolved)"
predicate: "has_birth_registration_name_and_sex"
object: "child-name field begins with Pulgar Ama[...] and a Jose [...] given-name line; sex Masculino"
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

# Atomic Claim: Entry 513 Child Name And Sex Hold

## Literal Support

The chunk reads:

```text
Nombre. Pulgar Amagada
Jose Luis
Sexo.
Masculino
```

The converted file conflicts:

```text
Nombre.
Isolina del Carmen
Jose
Sexo.
Masculino
```

Image review supports a `Pulgar Ama[...]` surname line and a `Jose [...]` given-name line, with `Masculino` in the sex field, but does not settle the complete child name.

## Conversion Confidence / QA Concern

Low. This is a derivative-vs-image conflict on the child identity endpoint of the Pulgar relationship. Preserve this as a held identity-context claim only.

## Uncertainty

Do not promote a canonical child name or merge this child with any existing Pulgar, Arriagada, Amagada, or Dario identity from this draft.
