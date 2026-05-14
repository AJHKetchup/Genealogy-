---
type: staged_source_packet
status: draft
source_path: raw/codex-conversion-jobs/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no/source/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no.codex.md
chunk_manifest: raw/chunks/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-codex/manifest.json
chunk_refs:
  - CHUNK-8276d0c44e96-P0001-01
page_refs:
  - Page 1, entry 172
source_reliability_class: original civil birth register
source_reliability_score: 9
source_reliability_rationale: Near-contemporary civil registration with named child, parents, informant, and official signature.
evidence_type: direct evidence of birth; source-stated evidence of parentage and residence
informant_proximity: Ernesto Monroy presented the birth registration; relationship to the child is not stated.
conversion_confidence: medium
qa_review:
  triage: research/_conversion-review/triage/2026-05-14-conversion-qa-batch-img-017-019-batch-pdf-042-044.md
  corrections: research/_conversion-review/corrections/2026-05-14-dario-pulgar-conversion-corrections.md
  page_queue: research/_conversion-review/page-queues/2026-05-14-batch-img-017-entry-172-reread.md
  qa_status: reread-region
promotion_recommendation: hold
tags: [staging, source-packet, chile, birth-record, pulgar, arriagada]
---

# Staged Source Packet

## Source Identity

- Source path: `raw/codex-conversion-jobs/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no/source/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`
- Converted file: `raw/converted/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no.codex.md`
- Chunk manifest: `raw/chunks/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-codex/manifest.json`
- Chunk/page reference: `CHUNK-8276d0c44e96-P0001-01`, page 1, entry 172.
- QA triage: dated review on 2026-05-14 downgraded the key extraction lines to `reread-region` for the child given name and the father's full name.

## Source Reliability

- Reliability class: original civil birth register.
- Reliability score: 9/10.
- Evidence type: direct evidence of the recorded birth event; source-stated evidence of parents, residences, and informant.
- Informant proximity: the presenting informant is Ernesto Monroy, but his relationship to the child is not stated.

## Literal Source Support

Focused entry 172 transcription from the converted source:

```text
172 de mil ochocientos ochenta i ocho
Siete de Abril [de mil ochocientos ochenta i ocho]
Nombre: Fidelmiro Segundo Pulgar Arriagada
Sexo: Hombre
Fecha: Ocho de Marzo [de mil ochocientos ochenta i ocho]; a las tres de la tarde
Lugar: Calle de Valdivia
Nombre del padre: Juan de Casanova Pulgar
Nac.: Chileno
Prof.: Jornalero
Domicilio: Calle de Colon
Nombre de la madre: Juana Arriagada de Pulgar
Nac.: Chilena
Domicilio: Calle de Colon
Ernesto Monroy
Presenta al nacimiento
Edad: veintiseis anos
Prof.: Empleado
Dom.: Calle de Valdivia
Emilio Quiroga, oficial R.C.
```

## Translation

```text
Registration no. 172 in the year 1888.
Inscription date: 7 April 1888.
Child: Fidelmiro Segundo Pulgar Arriagada, male.
Birth: 8 March 1888 at three in the afternoon, at Calle de Valdivia.
Father: Juan de Casanova Pulgar, Chilean, day laborer, resident of Calle de Colon.
Mother: Juana Arriagada de Pulgar, Chilean, resident of Calle de Colon.
Informant/presenter: Ernesto Monroy, age twenty-six, employee, resident of Calle de Valdivia.
Official: Emilio Quiroga, civil register official.
```

## Interpretation

This is a high-value Pulgar-Arriagada birth registration from Los Angeles, Chile. It clearly warrants staged extraction, but the most important name lines remain under a targeted reread queue, so downstream claims tied to those readings should not be promoted yet.

## Uncertainty Notes

- The child given name `Fidelmiro` is still under visual reread because a near variant remains possible.
- The father's full name `Juan de Casanova Pulgar` is also under visual reread because the compound phrase may be over-resolved.
- The mother's occupation field appears blank or unstated.
- Neighboring entries were not fully transcribed because entry 172 is the target record.

## Candidate Entities And Claims

- Person candidate: Fidelmiro Segundo Pulgar Arriagada.
- Person candidate: Juan de Casanova Pulgar.
- Person candidate: Juana Arriagada de Pulgar.
- Person candidate: Ernesto Monroy.
- Claim draft: `research/_staging/claims/batch-img-017-fidelmiro-segundo-pulgar-arriagada-birth.md`
- Claim draft: `research/_staging/claims/batch-img-017-fidelmiro-segundo-pulgar-arriagada-parentage.md`
- Claim draft: `research/_staging/claims/batch-img-017-fidelmiro-segundo-pulgar-arriagada-registration.md`

## Proposed Claim Status And Confidence

- Birth event claim: `possible`, confidence 6.8/10, pending reread of the child-name line.
- Parentage naming claim: `possible`, confidence 6.2/10, pending reread of the father-name line.
- Registration event claim: `probable`, confidence 8.4/10.

## Follow-Up Tasks

- Perform the queued local reread of the child given name and the father's full-name line using the original evidentiary crop.
- Compare the father's name against related Pulgar-Arriagada birth, marriage, or death entries from Los Angeles / La Laja.

## Promotion Recommendation

`hold` until the dated reread queue for entry 172 is cleared.