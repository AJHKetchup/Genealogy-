---
type: proof_review
status: complete
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124059453.md"
worker: "postconv-proof-review-20260530140733176"
role: claim_reviewer
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124059453.md"
reviewed_source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
reviewed_conversion_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-source-image-missing-conflict-qa-postconv-evidence-extraction-20260530115033211.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_quality_score: 0.54
conversion_confidence_score: 0.35
evidence_quantity_score: 0.42
agreement_score: 0.18
identity_confidence_score: 0.56
claim_probability: 0.62
relevance_level: conditional_high
relevance_confidence: 0.46
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Conflict

This review covers only the staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124059453.md`.

## Blockers First

- Row control is not certifiable. The expected source image `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` is absent, and the conversion-job page image `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png` is absent.
- The assigned chunk and source packet identify entry `172` as a Pulgar/Arriagada birth registration, while the current converted Markdown identifies entry `172` as a Burgos/de la Cruz birth registration.
- The conflict is material: child name, parents, birth date, birth time/place, and informant differ. This is not a spelling variant or translation issue.
- No canonical person, parent-child relationship, Dario-line attachment, same-person conclusion, merge, or page update is ready from this staged draft.
- The father-field reading `Jose del Carmen Pulgar S.` is derivative only. The terminal `S.` must remain unpromoted until image-controlled review confirms the visible text.

## Evidence Strengths

- The staged identity analysis accurately reports the disagreement between the assigned chunk/source packet and the current converted Markdown.
- The assigned chunk and source packet internally agree on the Pulgar/Arriagada reading: `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`
- The current converted Markdown internally supports the conflicting Burgos/de la Cruz reading: `Jose Miguel`, male, born 6 April 1888 at about 10 p.m. in `En esta`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, informant `Oswaldo Burgos`.
- The staged draft keeps the Dario comparison bounded. No reviewed derivative text literally names `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`

## Scored Judgment

| Dimension | Score / value | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.54 | A civil birth register would be strong evidence, but this review has no visible source image and must rely on conflicting derivative layers. |
| conversion_confidence_score | 0.35 | The assigned chunk and current converted Markdown disagree on the entire row identity. |
| evidence_quantity_score | 0.42 | There are multiple derivative files, but no independent image-controlled verification. |
| agreement_score | 0.18 | Agreement exists inside each derivative layer, but cross-layer agreement on entry `172` is poor. |
| identity_confidence_score | 0.56 | Conditional confidence that the staged Pulgar/Arriagada candidate is internally coherent; not enough for identity attachment. |
| claim_probability | 0.62 | Probability that the Pulgar/Arriagada row is the intended staged candidate, not probability that it is the certified physical entry. |
| relevance_level | conditional_high | Relevant to the Pulgar/Arriagada family only if row-control QA accepts the assigned chunk reading. |
| relevance_confidence | 0.46 | Relevance is sharply reduced by the unresolved row-control conflict. |
| canonical_readiness | not_ready | Hold for conversion QA; do not promote. |

## Claim Probability Notes

- Pulgar/Arriagada row controls physical entry `172`: 0.62. Supported by assigned chunk and source packet; blocked by absent image and conflicting converted Markdown.
- Burgos/de la Cruz row controls physical entry `172`: 0.26. Supported by current converted Markdown; contradicted by assigned chunk and source packet.
- Derivative row/page substitution or row-control mismatch exists: 0.88. The two readings describe different people and family groups under the same entry number.
- Any Dario attachment from this evidence: 0.02. No literal Dario name or identity bridge appears in the reviewed verification context.

## Review Decision

The staged draft is acceptable as a cautionary identity/conflict analysis, but not as support for canonical promotion. Its `hold_for_conversion_qa` recommendation is supported.

Canonical readiness remains `not_ready`.

## Next Action

Restore or locate the original source image or certified page image, then perform targeted row-control QA for physical entry `172`. After the visible source is checked, rerun proof review on the certified readings for child name, sex, registration date, birth date/time/place, father, mother, informant, and any parent-child relationship. Keep all Dario comparisons separate unless a later source literally supplies an identity bridge.
