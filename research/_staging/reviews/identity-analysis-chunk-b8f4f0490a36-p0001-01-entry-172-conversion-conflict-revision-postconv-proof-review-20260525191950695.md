---
type: proof_review
status: draft
role: claim_reviewer
worker: postconv-proof-review-20260525191950695
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525121046889.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525121046889.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
reviewed_conflict_note: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_quality_score: 0.88
conversion_confidence_score: 0.42
evidence_quantity_score: 0.55
agreement_score: 0.35
identity_confidence_score: 0.60
claim_probability: 0.62
relevance_level: high_if_pulgar_row_certified
relevance_confidence: 0.82
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Conflict

This review covers the exact staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525121046889.md`.

## Blockers First

1. Canonical readiness remains blocked by a row-level derivative conflict. The chunk and source packet identify entry 172 as the Pulgar/Arriagada birth row; the referenced converted Markdown in this checkout identifies entry 172 as a different non-Pulgar row.
2. The staged identity-analysis draft says the assigned converted Markdown reads `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`. The converted file now available in this checkout reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`. This secondary mismatch should be corrected or documented by conversion QA before any promotion.
3. The father field in the Pulgar/Arriagada row remains uncertain at the suffix/ending level. The chunk reads `Jose del Carmen Pulgar S.`, while source-image review supports the broader father name `Jose del Carmen Pulgar` but does not remove the need for targeted QA of the final mark after `Pulgar`.
4. No Dario-line identity or relationship claim is supported by this entry. The entry does not name Dario and does not provide a bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or `Dario Pulgar A.`.
5. Existing canonical wiki context must not be used as independent proof for this entry. The reviewed staged draft correctly treats downstream Pulgar/Juana pages as context only while the conversion conflict is unresolved.

## Evidence Strengths

- The source type is strong: an 1888 civil birth register page for Los Angeles, Chile.
- The source image visibly places entry 172 on page 58 and supports the Pulgar/Arriagada row as the row at that entry number: child `Jose del Carmen Segundo Pulgar Arriagada`, male, birth on 8 March 1888 at 3 p.m., place `Calle de Valdivia`, father `Jose del Carmen Pulgar ...`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The chunk and source packet agree with each other on the Pulgar/Arriagada row and preserve the needed uncertainty about the father's final suffix.
- The staged identity-analysis draft appropriately recommends `hold_for_conversion_qa` and does not promote same-person, parent-child, or Dario-line conclusions.

## Scored Judgment

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration is a high-quality source class, and the page image is available for direct verification. |
| conversion_confidence_score | 0.42 | Low-to-mixed because the converted file and chunk disagree, and the draft's summary of the converted-file conflict does not match the current converted text exactly. |
| evidence_quantity_score | 0.55 | There is one direct register entry plus derivative readings; quantity is adequate for row-local review but not enough for identity bridging. |
| agreement_score | 0.35 | The chunk/source packet agree with the image-reviewed Pulgar row, but the converted Markdown conflicts on the same entry number. |
| identity_confidence_score | 0.60 | Moderate for the row-local Pulgar/Arriagada identity; low for any canonical merge or broader Dario-line identity. |
| claim_probability | 0.62 | The Pulgar/Arriagada row is probable as the controlling image-visible row for entry 172, but the derivative conflict prevents promotion. |
| relevance_level | high_if_pulgar_row_certified | High for Pulgar/Arriagada family work only after conversion QA certifies the row. |
| relevance_confidence | 0.82 | The names Pulgar and Arriagada are plainly relevant if the row is certified. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until the conversion/assignment conflict and father suffix are resolved. |

## Claim-Level Findings

| Claim or hypothesis | Review disposition | Probability | Notes |
| --- | --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth row | Hold for conversion QA | 0.72 | Supported by the source image, chunk, and source packet; contradicted by the referenced converted Markdown layer. |
| Child is `Jose del Carmen Segundo Pulgar Arriagada` | Hold for conversion QA | 0.70 | Literal support is visible in the image and chunk, but row-level derivative conflict remains. |
| Father is `Jose del Carmen Pulgar S.` | Hold/revise wording | 0.58 | Father name is supported as `Jose del Carmen Pulgar`; suffix `S.` needs targeted image QA. |
| Mother is `Juana Arriagada de Pulgar` | Hold for conversion QA | 0.70 | Supported by the image-visible row and chunk; contradicted by the converted-file layer. |
| Entry proves any Dario-line identity or relationship | Do not promote | 0.05 | No Dario is named and no relationship bridge appears in the source. |
| The staged draft is ready for canonical promotion | Hold | 0.10 | The draft's hold recommendation is correct; its converted-file detail should be corrected or documented before downstream use. |

## Next Action

Keep the staged identity analysis at `hold_for_conversion_qa`. The next worker should perform targeted conversion QA against entry 172 on page 58, reconcile why the converted file and chunk describe different rows for the same entry number, and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, a separate proof review can reconsider narrow birth and parent claims for canonical promotion.
