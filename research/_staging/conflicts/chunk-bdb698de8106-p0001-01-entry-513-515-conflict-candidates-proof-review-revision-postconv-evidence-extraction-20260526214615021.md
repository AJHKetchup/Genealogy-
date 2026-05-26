---
type: conflict_candidates
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
worker: postconv-evidence-extraction-20260526214615021
source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526214615021.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
page_reference: page 1; register page 172; entries 513-515
promotion_recommendation: hold_for_conversion_qa
---

# Conflict Candidates: Entries 513 And 515

## Conflicts To Preserve

1. Entry 513 child-name/sex: converted transcript supports `Isolina del Carmen Jose`, `Masculino`; proof-review context reports unresolved image-reviewed disagreement.
2. Entry 513 mother name: converted transcript supports `Juana de Dios Amador de Pulgar`; proof-review context reports unresolved surname disagreement.
3. Entry 515 child name: converted transcript supports `Rosa Elvira del Carmen`; proof review says the partial row does not securely support the full name.

## Literal Support

```text
513 ... Nombre. Isolina del Carmen Jose ... Sexo. Masculino
513 ... Nombre del padre. Jose del Carmen Pulgar
513 ... Nombre de la madre. Juana de Dios Amador de Pulgar
515 ... Nombre. Rosa Elvira del Carmen
```

## Conversion Confidence / QA Concern

Low. The conflict is between derivative conversion text and prior image-reviewed evidence, so evidence extraction should not resolve it by inference.

## Uncertainty

Entry 513 remains unresolved for child identity and mother surname. Entry 515 remains unresolved because the visible row is partial in proof-review context.

## Handling

These conflicts should be resolved by conversion QA, not by evidence extraction inference. Existing derivative transcripts and image-reviewed notes should remain distinguishable until a corrected transcription is issued.

## Promotion Recommendation

`hold_for_conversion_qa`.
