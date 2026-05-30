---
type: proof_review
status: completed
role: claim_reviewer
worker: "postconv-proof-review-20260530140038847"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124454140.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124454140.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-source-image-missing-conflict-qa-postconv-evidence-extraction-20260530115033211.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: not_ready
review_decision: hold_for_conversion_qa
source_quality_score: 0.45
conversion_confidence_score: 0.30
evidence_quantity_score: 0.42
agreement_score: 0.18
identity_confidence_score: 0.40
claim_probability: 0.36
relevance_level: conditional_high
relevance_confidence: 0.55
---

# Proof Review: Entry 172 Derivative Transcript Conflict

This review covers the exact staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124454140.md`.

## Blockers First

- The source image is unavailable at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.
- The conversion-job page image is unavailable at `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png`.
- Row control cannot be certified from the visible source. The assigned chunk and source packet identify entry `172` as a Pulgar/Arriagada birth registration; the current converted Markdown identifies entry `172` as a Burgos/de la Cruz birth registration.
- The conflict is material, not a spelling or name-variant issue. The two derivative readings disagree on child, parents, birth date, birth place, informant, and surrounding page content.
- No canonical claim, parent-child relationship, identity merge, Dario-line attachment, page rename, or wiki update is ready from this staged draft.
- The father reading `Jose del Carmen Pulgar S.` is derivative-only in this review. The `S.` suffix or terminal mark requires source-image QA before canonical use.

## Evidence Strengths

- The staged draft accurately reports the main derivative conflict found in the verification files.
- The assigned chunk and source packet agree internally that entry `172` is for `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at Calle de Valdivia, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The current converted Markdown clearly conflicts by giving entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at about 10 p.m. in `En esta`.
- The conversion review note already preserves the dispute and recommends `hold_for_conversion_qa`; this review agrees with that handling.
- The staged draft appropriately avoids changing the reading to any Dario identity. It only allows later double-checking of possible Pulgar-line relevance.

## Scored Judgment

| Field | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.45 | Civil birth registration would normally be strong, but this worker could not inspect the image and only derivative text layers are available. |
| conversion_confidence_score | 0.30 | The chunk and converted Markdown are incompatible for the same entry number, and no source/page image is present to resolve the conflict. |
| evidence_quantity_score | 0.42 | Multiple derivative files were available, but they collapse into two conflicting transcript lines rather than independent source confirmations. |
| agreement_score | 0.18 | Agreement is internal within the Pulgar/Arriagada packet and chunk only; the converted Markdown materially disagrees. |
| identity_confidence_score | 0.40 | The Pulgar/Arriagada identity is plausible within the assigned chunk, but row control and physical-source support are not certified. |
| claim_probability | 0.36 | Probability that the staged identity analysis is canonically usable now is low because the controlling row remains unresolved. |
| relevance_level | conditional_high | If the Pulgar/Arriagada row is certified, the entry is relevant to the Pulgar/Arriagada family line; if the Burgos/de la Cruz row controls, relevance drops sharply. |
| relevance_confidence | 0.55 | Family relevance depends on unresolved row control, so confidence is moderate at best. |
| canonical_readiness | not_ready | Hold for image-controlled conversion QA before any promotion or relationship work. |

## Claim Probability Detail

| Claim or hypothesis | Probability | Review judgment |
| --- | ---: | --- |
| Entry `172` physically corresponds to the Pulgar/Arriagada row in the assigned chunk. | 0.58 | Plausible from the chunk and source packet, but not proven without image control. |
| Entry `172` physically corresponds to the Burgos/de la Cruz row in the converted Markdown. | 0.30 | Plausible from the converted file, but contradicted by the assigned chunk and packet. |
| The staged draft is safe for canonical promotion as written. | 0.08 | Not safe because the source image is missing and derivative transcripts conflict. |
| This record supports attaching any Dario Pulgar identity. | 0.02 | No Dario name appears in the checked draft, chunk, packet, QA note, or converted entry. |
| The parents can be canonically asserted as `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`. | 0.25 | Possible only if the Pulgar/Arriagada row is later certified. |

## Review Finding

The staged draft is supportable as a conflict-analysis hold note, but not as canonical evidence. Its core conclusion should remain `hold_for_conversion_qa` / `not_ready`. The draft should not be promoted or used to strengthen parent-child links until the missing source image or certified page image is available and row control is resolved.

## Next Action

Restore or locate the original source image or certified page image, then run targeted conversion QA on physical entry `172`. That QA should decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz and should specifically bound the father-name reading before any later proof review promotes claims or relationships.
