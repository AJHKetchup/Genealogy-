---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260527090815308
task_id: proof-review:research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-identity-researcher-20260526235735222.md
staged_draft: research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-identity-researcher-20260526235735222.md
reviewed_source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526232219797.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
canonical_readiness: hold
---

# Proof Review: Entry 513 And 515 Identity Conflict Analysis

## Blockers First

- Hold for targeted conversion QA. The staged draft is correctly marked `hold_for_conversion_qa`; the source packet also gives `conversion_confidence: low` and says the identity-controlling fields require row-level QA before promotion.
- Entry 513 child identity is not proof-ready. The converted Markdown and chunk read `Isolina del Carmen` / `Jose` with sex `Masculino`, but the page image and prior review context leave the child-name field visibly contested. I cannot replace the transcription with a new name in this review note.
- Entry 513 mother surname is not proof-ready. The converted Markdown and chunk read `Juana de Dios Amador de Pulgar`; the staged draft preserves an `Amagada`-style concern. This review cannot normalize `Amador`, `Amagada`, or `Arriagada` as variants without a QA-certified reading.
- Entry 513 father/declarant is relevant but not enough for canonical identity resolution. `Jose del Carmen Pulgar` and `Jose del C. Pulgar` are supported by the derivative layer and are comparatively legible in the page image, but name agreement alone does not attach the row to any existing person page or parent-child relationship.
- Entry 515 is a boundary/control row, not Pulgar identity evidence. Its converted `Rosa Elvira del Carmen` and `Pedro Pablo Leiva` readings may help prevent row spillover, but they do not support a Pulgar-family claim in this staged draft.
- No Dario/Pulgar-Smith/Pulgar-Arriagada bridge is supported. The reviewed materials do not name Dario or Smith and do not provide a relationship chain to any Dario candidate.

## Evidence Strengths

- The source type is strong: an 1889 Los Angeles, La Laja civil birth register page with entries 513-515.
- The cited converted file and cited chunk are present and internally aligned with each other for the derivative transcription.
- Entry 513 is probably family-relevant in a narrow sense because the derivative text and visible row context both place `Jose del Carmen Pulgar` / `Jose del C. Pulgar` in father/declarant context.
- The staged draft appropriately separates literal transcription, interpretation, hypothesis scoring, conflict severity, and canonical readiness instead of promoting a binary identity conclusion.

## Scored Judgment

| dimension | score / value | review judgment |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil register page image is a strong source type, but the usable row evidence is limited by legibility and conversion dispute. |
| conversion_confidence_score | 0.24 | Converted file and chunk agree with each other, but the assigned packet and staged draft both preserve low-confidence QA concerns. |
| evidence_quantity_score | 0.50 | One register row is directly relevant, with entry 515 only as a boundary control. |
| agreement_score | 0.36 | Derivative files agree, but derivative text conflicts with image-review concerns in child name, mother surname, and row-level fields. |
| identity_confidence_score | 0.22 | Exact child, mother, same-person, and relationship identities remain unresolved. |
| claim_probability | 0.70 | The narrow claim that entry 513 is Pulgar-family relevant is probable; exact identity and relationship claims are much lower. |
| relevance_level | high | Entry 513 directly concerns a Pulgar father/declarant candidate. |
| relevance_confidence | 0.86 | Relevance is stronger than identity readiness because the Pulgar father/declarant context is the most stable element. |
| canonical_readiness | hold | No canonical promotion, merge, page rename, or relationship attachment is ready. |
| canonical_readiness_score | 0.10 | Further targeted conversion QA is required before proof review can evaluate promotable atomic claims. |

## Claim-Level Probability

| reviewed claim or hypothesis | probability | readiness |
| --- | ---: | --- |
| Entry 513 is a Pulgar-family birth row through father/declarant context. | 0.70 | hold_for_conversion_qa |
| Entry 513 father/declarant may correspond to an existing `Jose del Carmen Pulgar` person stub. | 0.42 | not_ready |
| Entry 513 mother is the converted `Juana de Dios Amador de Pulgar`. | 0.34 | not_ready |
| Entry 513 mother is an `Amagada`-style reading. | 0.46 | hold_for_targeted_crop_review |
| Entry 513 mother is `Juana Arriagada de Pulgar` or the same person as an Arriagada candidate. | 0.10 | not_ready |
| Entry 513 child is an existing `Tulio Cesar Luis Jose` or any other specific canonical child identity. | 0.18 | not_ready |
| Entry 513 bridges to any Dario/Pulgar-Smith/Pulgar-Arriagada identity. | 0.02 | not_ready |
| Entry 515 is secure Pulgar-line evidence. | 0.00 | not_relevant |

## Review Determination

The staged draft should remain on `hold_for_conversion_qa`. Its main conclusion is supported: entry 513 is relevant enough to preserve for Pulgar-family review, but it is not reliable enough for canonical identity work because the child name, mother surname, and relationship-bearing fields remain contested.

No raw source, converted Markdown, chunk, staged source packet, staged identity draft, canonical wiki page, claim, or relationship file was edited.

## Next Action

Run targeted row-level conversion QA for page 172, entries 513 and 515. QA should certify or explicitly leave uncertain the entry 513 child-name/sex field, birth date/time/place, father/declarant name and occupation, mother surname, and the entry 515 boundary fields needed to prevent spillover. After that, rerun proof review on atomic claims before any canonical promotion.
