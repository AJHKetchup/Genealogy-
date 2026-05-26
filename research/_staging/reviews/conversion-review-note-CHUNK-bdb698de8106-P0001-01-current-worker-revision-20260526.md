---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
worker: postconv-evidence-extraction-20260526095546978
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_sha256: 05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
page_reference: page 1; register page 172; entries 513-515
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Current Worker Revision 2026-05-26

## Scope

This revision addresses the proof-review follow-up for `CHUNK-bdb698de8106-P0001-01`. No raw source, converted Markdown, chunk Markdown, page Markdown, or canonical wiki page was edited.

## Person-First Family Evidence

The family-relevant evidence is entry 513, where the derivative transcript places `José del Carmen Pulgar` / `José del C. Pulgar` in the father/declarant context with domicile `Calle Colon`. This is a useful Pulgar-family lead for identity, residence, occupation, and a possible parent-child relationship, but the child identity and mother surname are not stable enough for canonical use.

Literal derivative support for the family-relevant portion:

```text
Nombre del padre.
José del Carmen Pulgar
Nac. Chileno Prof. Agricultor
Domicilio. Calle Colon
Nombre de la madre.
Juana de Dios Amador de Pulgar
...
José del C. Pulgar
Padre
Edad. Cuarenta i siete Años
Prof. Agricultor
Dom. Calle Colon
```

## Current Staged Outputs

Existing staged drafts for this chunk already provide the needed source packet, atomic claims, relationship candidates, conflict candidates, identity analysis, and conversion-QA research tasks under `research/_staging/`. They consistently cite the bdb chunk path and preserve the derivative/image disagreement.

The key family-linked drafts remain:

- `research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md`
- `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-name-sex.md`
- `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place.md`
- `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-father.md`
- `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-mother.md`
- `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant.md`
- `research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md`
- `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-bdb698de8106-P0001-01-qa-candidates.md`
- `research/_staging/research-tasks/task-chunk-bdb698de8106-p0001-01-entry-513-514-targeted-conversion-qa.md`
- `research/_staging/tasks/task-chunk-bdb698de8106-p0001-01-conversion-qa-followup-revision-20260526.md`

## QA Blocker

Promotion remains blocked by material conversion conflict:

- Entry 513 child name/sex conflicts between the derivative transcript and image-reviewed evidence.
- Entry 513 mother surname remains unresolved, including the derivative `Amador` reading and image-sensitive `Amagada` or related alternatives.
- Entry 513 declarant/father evidence is stronger than the rest of the row, but it should stay staged until conversion QA confirms the row-level transcription.
- Entry 515 remains partial and should not be used to infer a full identity or relationship from the derivative transcript.

## Promotion Recommendation

Keep the source packet, entry 513 family-linked claims, entry 513 relationship candidate, entry 515 drafts, and related identity/conflict notes on `hold_for_conversion_qa` or `do_not_promote` as already staged. Do not promote, merge, rename, or attach any Dario/Pulgar/Pulgar-Smith/Arriagada identity from this chunk until targeted conversion QA resolves entries 513-515 and a later proof-review pass evaluates the corrected transcription.
