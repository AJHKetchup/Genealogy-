---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260525221149889
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-analysis-20260525211334388.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-analysis-20260525211334388.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
canonical_readiness: not_ready
---

# Proof Review: Entry 172 Row Conflict Identity Analysis

## Blockers First

- The staged draft correctly identifies a row-level conflict: the assigned chunk and source packet read page 58, entry 172 as a Pulgar/Arriagada birth, while the assigned converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- The visible source image supports the presence of a Pulgar/Arriagada row at page 58, entry 172 at a high level, but this proof review should not rewrite the conversion. The derivative conversion conflict must be resolved by targeted conversion QA.
- The father-name field remains uncertified. The staged materials propose `Jose del Carmen Pulgar S.`, while the visible image is not sufficient in this review pass to certify whether the final reading should include `S.`, omit it, or mark it uncertain.
- No Dario candidate is literally named in entry 172. Any proposed Dario-line bridge from this row is unsupported and should remain an anti-conflation check only.
- Canonical pages or prior generated evidence cannot resolve the conversion conflict. They should not be used to promote a child identity, parent relationship, same-person merge, or Dario-line attachment from this staged draft.

## Evidence Checked

- Staged draft under review: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-analysis-20260525211334388.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Assigned converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source type is a civil birth register, which is highly relevant and normally strong evidence for birth identity and parent-child relationships.
- The chunk and source packet agree on the core family-relevant reading: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, registration on 7 April 1888, birth on 8 March 1888 at Calle de Valdivia.
- The source image visually aligns with the chunk/source-packet family of entries for pages 58-59, including a page 58 entry 172 with Pulgar/Arriagada content rather than the converted Markdown's Burgos/de la Cruz reading.
- The staged identity analysis is appropriately conservative: it treats the issue as a conversion conflict and blocks canonical promotion.

## Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration is a strong primary source for birth and parent fields, subject here to image readability and derivative conflict. |
| conversion_confidence_score | 0.30 | The chunk/source packet and source image favor Pulgar/Arriagada, but the assigned converted Markdown is incompatible. |
| evidence_quantity_score | 0.58 | There is one controlling source image plus derivative artifacts; quantity is limited and internally conflicted. |
| agreement_score | 0.42 | The chunk and source packet agree, and the image broadly supports them, but the assigned converted Markdown disagrees on child, parents, birth date, and page context. |
| identity_confidence_score | 0.56 | Pulgar/Arriagada is the better-supported reading, but the conflict blocks identity certainty and same-person conclusions. |
| claim_probability | 0.68 | It is more likely than not that page 58 entry 172 is the Pulgar/Arriagada birth, but this remains below promotion standard until conversion QA certifies the row. |
| relevance_level | high | The row is directly relevant to Pulgar/Arriagada identity sorting and to preventing Dario-line overreach. |
| relevance_confidence | 0.86 | Relevance is clear if the Pulgar/Arriagada row controls; relevance to Dario remains low and indirect. |
| canonical_readiness | 0.10 | Not ready for canonical claims, relationships, merges, or Dario-line use. |

## Claim Judgment

The staged identity analysis is supported as a hold note. Its central claim is not that the Pulgar/Arriagada identity is proven, but that the row conflict prevents canonical use. That conclusion is well supported by the checked artifacts.

The draft should remain `hold_for_conversion_qa`. It should not be promoted, and no canonical relationship or same-person merge should be made from it.

## Next Action

Run targeted conversion QA against the source image, assigned converted Markdown, assigned chunk, and source packet. QA should certify the controlling row for page 58 entry 172 and explicitly resolve the father-name field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain reading. After QA, rerun proof review before any canonical child identity, parent relationship, Jose/Juana identity merge, or Dario-line comparison is promoted.
