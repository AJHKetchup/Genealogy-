---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260528194621126
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528172745327.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528172745327.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528170150642.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528170150642.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_quality_score: 0.86
conversion_confidence_score: 0.74
evidence_quantity_score: 0.72
agreement_score: 0.62
identity_confidence_score: 0.82
claim_probability: 0.84
relevance_level: high_for_pulgar_arriagada_row_low_for_dario_identity
relevance_confidence: 0.88
canonical_readiness: hold_for_conversion_conflict_resolution
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. The staged draft is supported as a conflict analysis, but it is not canonically ready because the current converted Markdown still assigns entry `172` to `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`, while the chunk, source packet, targeted QA note, and visible image support the physical row `172` as the Pulgar/Arriagada birth entry.
2. The father field must stay bounded to `Jose del Carmen Pulgar`. The chunk includes a trailing `S.` after `Pulgar`, but the targeted row-control QA explicitly does not certify that suffix for promotion.
3. The entry does not name Dario, Arturo, Smith, Dario Jose, or any later-life identifier. It is not evidence for merging this child or either parent with any Dario-line person.
4. The source supports source-named parentage in this birth row only. It does not prove that `Juana Arriagada de Pulgar` is the same person as `Juana de Dios Amagada de Pulgar`, and it does not resolve other parent-candidate merges.

## Evidence Strengths

- The source is a civil birth register image, which is a strong source type for the recorded birth, registration date, sex, named parents, residence fields, and informant statement.
- The page image visibly places entry `172` on page 58 in the Pulgar/Arriagada row. This agrees with the assigned chunk, the source packet, and the targeted row-control QA note.
- The staged draft accurately preserves the converted Markdown as conflicting derivative text instead of treating the Burgos/de la Cruz record as a name variant or duplicate identity.
- The staged draft correctly keeps the Dario-line comparison negative: the row has Pulgar/Arriagada relevance but no direct Dario identity bridge.

## Scored Judgment

| Factor | Score | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil registration image is strong for this event, though handwriting and image quality leave some field-level caution. |
| conversion_confidence_score | 0.74 | High for row control after image review; reduced because the current converted Markdown is materially wrong for entry `172` and the father suffix remains uncertified. |
| evidence_quantity_score | 0.72 | One source image plus chunk, source packet, and targeted QA are enough for bounded row facts, but not enough for identity merges beyond the row. |
| agreement_score | 0.62 | Chunk, packet, QA, and image agree on the Pulgar/Arriagada row; the converted Markdown strongly disagrees. |
| identity_confidence_score | 0.82 | Strong that the physical row names `Jose del Carmen Segundo Pulgar Arriagada` with parents `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`; weak for any external identity attachment. |
| claim_probability | 0.84 | The bounded claim that physical entry `172` is the Pulgar/Arriagada birth registration is probable. Dario-merge claims remain near unsupported. |
| relevance_level | high_for_pulgar_arriagada_row_low_for_dario_identity | Relevant to the Pulgar/Arriagada birth and parentage cluster; not relevant as direct Dario proof. |
| relevance_confidence | 0.88 | Relevance boundary is clear from names, dates, and absence of Dario identifiers. |
| canonical_readiness | hold_for_conversion_conflict_resolution | Do not promote from this identity analysis until the conversion conflict is explicitly handled in the promotion workflow. |

## Claim-Level Findings

| Reviewed claim or hypothesis | Probability | Finding |
| --- | ---: | --- |
| Physical entry `172` is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.90 | Supported by image, chunk, source packet, and QA; held only because the converted file conflicts. |
| `Jose del Carmen Pulgar` is the source-named father in the controlled row. | 0.84 | Supported as a bounded father reading; do not include the trailing `S.` unless separately certified. |
| `Juana Arriagada de Pulgar` is the source-named mother in the controlled row. | 0.88 | Supported by the controlled row materials. |
| Burgos/de la Cruz and Pulgar/Arriagada entry-172 text are duplicate-person evidence. | 0.02 | Not supported; the disagreement is a conversion/row-control conflict. |
| Entry 172 supports a Dario Arturo, Dario Jose, Dario Pulgar Arriagada, or Pulgar-Smith identity bridge. | 0.03 | Not supported by this source. |

## Next Action

Hold for conversion-conflict resolution before canonical promotion. If promoted later, promote only bounded row-control facts for `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`; preserve the Burgos/de la Cruz text as conflicting derivative conversion output, and leave all Dario-line and Juana duplicate-person questions unresolved.
