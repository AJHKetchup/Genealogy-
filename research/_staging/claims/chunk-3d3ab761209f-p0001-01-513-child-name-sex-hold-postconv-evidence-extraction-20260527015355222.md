---
type: claim
status: draft
claim_type: identity
subject: "Entry 513 child"
predicate: "was recorded with name and sex"
object: "surname line beginning Pulgar A[...] with given-name line unresolved; sex Masculino"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_packet: "research/_staging/source-packets/chunk-3d3ab761209f-p0001-01-entry-513-pulgar-hold-postconv-evidence-extraction-20260527015355222.md"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
page_reference: "image page 1; register page 172; entry 513; Nombre i sexo column"
confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Atomic Claim Draft: Entry 513 Child Name And Sex

Literal support: the chunk reads `Pulgar Amagada / Jose Luis` and `Masculino`; the converted file reads `Isolina del Carmen / Jose` and `Masculino`. The source image supports a Pulgar surname line and `Masculino`, but the full name is not safely settled in this extraction pass.

Conversion confidence / QA concern: child full name is a blocking conflict. The disagreement must be preserved rather than collapsed into one normalized child identity.

Uncertainty: targeted conversion QA should reread the child surname line, given-name line, and sex field together before any identity claim is promoted.
