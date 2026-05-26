---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260526220737422
task_id: "proof-review:research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916.md"
staged_draft: "research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916.md"
reviewed:
  - "research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916.md"
  - "research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526193717806.md"
  - "research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526193717806.md"
  - "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md"
  - "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
source_quality_score: 0.78
conversion_confidence_score: 0.28
evidence_quantity_score: 0.55
agreement_score: 0.34
identity_confidence_score: 0.36
claim_probability: 0.52
relevance_level: high
relevance_confidence: 0.96
canonical_readiness: hold
created: 2026-05-26
---

# Proof Review: Entry 513-515 Identity Conflict Analysis

## Blockers First

1. The staged draft is correctly held. The reviewed source packet and conflict draft both state `hold_for_conversion_qa`, and the converted/chunk transcript is materially challenged by prior image-review concerns summarized in those staging files.
2. Entry 513 has strong family relevance but unstable endpoints. The derivative transcript supports `Jose del Carmen Pulgar` as father and `Jose del C. Pulgar` as father/declarant, but the child-name field and mother surname remain unresolved.
3. Entry 515 is not ready for identity or relationship claims. The converted/chunk transcript reads `Rosa Elvira del Carmen` and `Pedro Pablo Leiva`, but the staging materials flag bottom-crop/partial-image concern and possible disagreement with the converted child/father readings.
4. No reviewed material directly names or bridges `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or related Dario/Pulgar-Arriagada candidates. Those comparisons are relevant only as anti-conflation guardrails.
5. Do not promote, merge, rename, or attach parent-child relationships from these rows before targeted conversion QA resolves the visible-source readings.

## Evidence Strengths

- The source itself is a civil birth register page for Los Angeles, La Laja, Chile, 1889, page 172, entries 513-515. As a record class, it is high-value direct evidence for births and parent/declarant statements.
- The converted file and chunk agree with each other on the derivative readings for entry 513: child field `Isolina del Carmen` / `Jose`, sex `Masculino`, father `Jose del Carmen Pulgar`, mother `Juana de Dios Amador de Pulgar`, and declarant `Jose del C. Pulgar`, role `Padre`, age forty-seven.
- The converted file and chunk also agree with each other on the derivative entry 515 readings: child `Rosa Elvira del Carmen` and father/declarant `Pedro Pablo Leiva`.
- The staged identity analysis preserves uncertainty rather than converting the derivative transcript into canonical identity claims. That treatment is supported by the source packet and conflict draft.

## Score Table

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil birth register is a strong source type, but this review used the converted/chunk text and staging notes rather than resolving the image directly. |
| conversion_confidence_score | 0.28 | Low because entry 513 child/mother fields and entry 515 child/father fields are explicitly challenged in staging QA notes. |
| evidence_quantity_score | 0.55 | One page, one converted file, one chunk, one source packet, and one conflict draft are available; no independent corroborating record is reviewed here. |
| agreement_score | 0.34 | Converted file and chunk agree with each other, but staging review materials disagree with material row-level fields. |
| identity_confidence_score | 0.36 | Moderate only for entry 513 being Pulgar-relevant; low for exact child, mother, entry 515, and any cross-record identity. |
| claim_probability | 0.52 | Probable that entry 513 contains Pulgar-family evidence; not probable enough for exact identity or relationship promotion. |
| relevance_level | high | The draft directly addresses the assigned entry 513-515 conflict and Pulgar-line identity risk. |
| relevance_confidence | 0.96 | Reviewed paths match the assigned staged draft and its referenced source materials. |
| canonical_readiness | hold | No canonical promotion is justified. |

## Claim Judgments

| Claim or hypothesis | Review judgment | Probability | Canonical readiness |
| --- | --- | ---: | --- |
| Entry 513 is Pulgar-family relevant. | Supported as a cautious staging claim by the derivative father/declarant readings and matched family term. | 0.70 | hold |
| Entry 513 child is exactly `Isolina del Carmen Jose`. | Derivative transcript support exists, but source packet flags child-name conflict. | 0.32 | hold |
| Entry 513 father/declarant is `Jose del Carmen Pulgar` / `Jose del C. Pulgar`. | Best-supported row detail in the reviewed materials, still not enough for a same-person merge with any existing page. | 0.66 | hold |
| Entry 513 mother is `Juana de Dios Amador de Pulgar`. | Supported by converted/chunk text, challenged by staging note that mother surname may not be `Amador`. | 0.36 | hold |
| Entry 515 child/father are `Rosa Elvira del Carmen` and `Pedro Pablo Leiva`. | Derivative transcript support only; partial/bottom-crop concern blocks promotion. | 0.25 | hold |
| Either entry establishes a Dario/Pulgar-Smith or Dario/Pulgar-Arriagada bridge. | Unsupported by the reviewed materials. | 0.03 | not_ready |

## Next Action

Run targeted conversion QA against the source image for entry 513 child name/sex, mother surname, father/declarant profession, and entry 515 child-name/father-declarant fields. After QA, rerun proof review on atomic claims and relationship candidates before any canonical edit.
