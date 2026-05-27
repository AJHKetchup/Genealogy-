---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260527073906517
task_id: proof-review:research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-identity-analysis-20260527001502207.md
staged_draft: research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-identity-analysis-20260527001502207.md
source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526232219797.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
review_status: hold
canonical_readiness: hold_for_conversion_qa
created: 2026-05-27
---

# Proof Review: Entries 513 And 515 Conflict Candidates

## Blockers

- Canonical readiness is `hold_for_conversion_qa`; no claim, relationship, person merge, family link, or canonical wiki edit is supported from this draft.
- The converted file and chunk agree with each other, but the source packet marks `conversion_confidence: low` and `promotion_recommendation: hold_for_conversion_qa`.
- Entry 513 has unresolved identity-controlling fields: child name, sex, mother surname, and row-level birth details. These fields control any parent-child claim and cannot be promoted while held.
- The visible source image supports the need for targeted QA in the child-name and mother-surname areas. This review does not substitute a new transcription for those cells.
- Entry 515 is only relevant as a row-boundary/control issue. It does not provide Pulgar-family support and should not be used to build a separate Leiva claim from this draft.
- Dario-line comparisons remain anti-conflation context only. This source does not name Dario, Arturo, Smith, or a direct bridge to an existing Dario Pulgar identity.

## Scored Judgment

| score | value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register page is a high-quality source type for birth and parentage once the row transcription is stable. |
| conversion_confidence_score | 0.32 | Converted file and chunk are internally consistent, but the packet and image inspection show unresolved transcription risk in identity fields. |
| evidence_quantity_score | 0.46 | One page and one row cluster provide useful evidence, but the key claims depend on a single disputed entry. |
| agreement_score | 0.38 | Derivative files agree with each other; staged review context and visible image concerns disagree with parts of the derivative reading. |
| identity_confidence_score | 0.40 | The Pulgar father/declarant lead is plausible, but child and mother identity are not settled. |
| claim_probability | 0.44 | Probable that entry 513 is Pulgar-relevant; not probable enough for a specific child, mother, or relationship claim. |
| relevance_level | high | The draft directly concerns the assigned page, entries 513 and 515, and the Pulgar conflict candidates. |
| relevance_confidence | 0.96 | All reviewed materials point to the same source packet, converted file, chunk, and page image. |
| canonical_readiness | hold_for_conversion_qa | Stable transcription or explicit uncertainty markers are required before proof promotion. |

## Evidence Strengths

- The staged draft accurately preserves the hard boundary between derivative text and unresolved image-review concerns.
- The source packet gives clear provenance: page 172, entries 513-515, civil birth register, and matching source/converted/chunk identifiers.
- Literal derivative support exists for a source-level father/declarant lead: `Jose del Carmen Pulgar` and `Jose del C. Pulgar`.
- Literal derivative support exists for the held mother-name candidate: `Juana de Dios Amador de Pulgar`, but this is explicitly not settled.
- The draft correctly treats Entry 515 as boundary protection rather than Pulgar evidence.

## Claim Review

| reviewed item | support judgment | probability | canonical action |
| --- | --- | ---: | --- |
| Entry 513 is Pulgar-relevant | Supported as a lead, not as a final claim | 0.68 | Hold pending QA |
| Entry 513 father/declarant is Jose del Carmen Pulgar | Plausible derivative support with remaining row risk | 0.62 | Hold pending QA |
| Entry 513 mother is Juana de Dios Amador/Amagada/Arriagada candidate | Unresolved surname conflict | 0.42 | Hold, do not normalize variants |
| Entry 513 proves a parent-child relationship | Not proof-ready because child identity and mother surname are unstable | 0.28 | Do not promote |
| Entry 515 supports a Pulgar claim | Not supported; boundary context only | 0.05 | Do not promote |
| Any person is same as a Dario Pulgar identity | Unsupported in this draft | 0.02 | Anti-conflation only |

## Reliability And Risk

- Source reliability is strong in principle because this is a contemporary civil register page.
- Conversion reliability is low for canonical use because the disputed fields are not peripheral; they are the fields needed to identify the child and mother.
- Identity risk is high if `Amador`, `Amagada`, and `Arriagada` are collapsed by context instead of source-level QA.
- Relationship risk is high if the father/declarant lead is attached before the child-name and mother-surname readings are settled.
- Relevance is high for conflict review and low for promotion.

## Next Action

Keep the staged identity analysis on `hold_for_conversion_qa`.

The next required step is targeted conversion QA against the source image for entry 513 child name, sex, birth details, father/declarant role and profession, and mother surname; and for entry 515 row-boundary fields. After QA produces stable literal readings or explicit uncertainty markers, rerun proof review on atomic claims before any canonical promotion or Dario-line comparison.
