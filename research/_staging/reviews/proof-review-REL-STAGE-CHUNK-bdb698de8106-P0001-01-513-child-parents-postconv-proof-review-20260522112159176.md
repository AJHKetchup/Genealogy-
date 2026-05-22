---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260522112159176
task_id: proof-review:research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
staged_draft: research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
reviewed_at: 2026-05-22T11:21:59Z
decision: hold
canonical_readiness: not_ready
source_quality_score: 0.86
conversion_confidence_score: 0.35
evidence_quantity_score: 0.55
agreement_score: 0.25
identity_confidence_score: 0.30
claim_probability: 0.20
relevance_level: direct_but_conflicted
relevance_confidence: 0.88
next_action: conversion_qa_reconcile_entry_513_child_identity_and_parent_readings
---

# Proof Review: REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents

## Blockers

- The exact staged relationship is not ready for canonical promotion because the child in the draft, `Isolina del Carmen Jose`, is not supported by the restored page image or by the available chunk lineage.
- The staged draft references `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`, but that file is unavailable. The same directory currently contains `page-0172-chunk-01.md` with chunk id `CHUNK-4127185dc97c-P0172-01`, not `CHUNK-bdb698de8106-P0001-01`.
- The cited converted file and available chunks conflict materially. The converted file currently reads entry 513 child as `Isidoro del Carmen Diaz`; the available `CHUNK-3d3ab761209f-P0001-01` reads `Pulgar Amagada / Jose Luis`; the source packet's image QA also reports the child name appears closer to `Pulgar ... / Jose Luis` and male, not the staged `Isolina del Carmen Jose`.
- Because the child identity is the subject of the relationship, the parent names cannot be linked to the staged child without conversion QA. Do not promote this relationship to `research/relationships`, `wiki/people`, or `wiki/families`.

## Evidence Strengths

- Source type is strong: a Chilean civil birth register page, page 172, entry 513, with a visible original page image and official register format.
- The restored page image directly shows entry 513 and visibly places `Jose del Carmen Pulgar` in the father field and a mother field reading close to `Juana de Dios Amador/Amagada de Pulgar`.
- The declarant column also visibly names `Jose del C. Pulgar` as father, adding internal support that the father field refers to the same entry.
- The page image, source packet, converted file, and available chunks all concern the same source image and entry set, so the evidence is relevant even though the transcription layer is unstable.

## Scored Judgment

| Factor | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Original civil register image is a strong primary source for birth and parentage, though handwriting and image contrast create reading risk. |
| conversion_confidence_score | 0.35 | Multiple derivative readings disagree on the child name, page/chunk id, and some register details. |
| evidence_quantity_score | 0.55 | One direct source page is present, but no independent corroborating source is used for this staged relationship. |
| agreement_score | 0.25 | Staged draft, converted file, available chunks, source packet QA, and visible image do not agree on the child identity. |
| identity_confidence_score | 0.30 | Parent fields are plausible for entry 513, but the staged child identity is not supported. |
| claim_probability | 0.20 | The exact relationship `Isolina del Carmen Jose` child of `Jose del Carmen Pulgar` and `Juana de Dios Amador de Pulgar` is unlikely as staged because the child name conflicts with visible and derivative evidence. |
| relevance_level | direct_but_conflicted | Entry 513 is directly relevant to a child-parent relationship, but not reliably to the staged child. |
| relevance_confidence | 0.88 | The reviewed materials are the correct source family for entry 513 despite the chunk/path conflict. |
| canonical_readiness | not_ready | Hold for conversion QA and staged relationship revision before any canonical use. |

## Next Action

Hold this staged relationship and run conversion QA against the restored page image for entry 513. Reconcile the child name, sex, surname sequence, father field, and mother field from the visible source; then revise or replace this staged relationship from the corrected transcription. Preserve the boundary between verification and transcription: do not change the child to a different reading unless the visible source supports that reading.
