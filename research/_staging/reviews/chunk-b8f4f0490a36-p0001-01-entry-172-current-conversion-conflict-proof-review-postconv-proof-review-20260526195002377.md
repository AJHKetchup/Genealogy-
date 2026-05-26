---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526195002377
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526172507192.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526172507192.md
reviewed_conflict_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526171029823.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
source_quality_score: 0.88
conversion_confidence_score: 0.52
evidence_quantity_score: 0.72
agreement_score: 0.44
identity_confidence_score: 0.64
claim_probability: 0.70
relevance_level: high
relevance_confidence: 0.92
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- The staged draft should remain on hold. The assigned chunk, held source packet, and visible source image support page 58 entry 172 as the Pulgar/Arriagada row, while the current converted Markdown gives entry 172 as a Burgos/de la Cruz row. This is a row-level conversion conflict, not a spelling variant.
- The current converted Markdown cannot be used to support the Pulgar/Arriagada child, parent names, birth date, birth place, informant, or parent-child relationships because it records different people and a different birth event under the same entry number.
- The father field is still not promotion-ready. The chunk reads `Jose del Carmen Pulgar S.`, while the staged draft/source packet correctly limit certification to `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` pending targeted conversion QA.
- No reviewed evidence in this entry literally names Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario Pulgar Arriagada. Any Dario-line use remains an anti-conflation or later bridge-review question only.
- Canonical pages or generated context must not resolve this conflict. The review is limited to the staged draft and referenced verification files, and the conversion disagreement must be fixed before promotion.

## Evidence Strengths

- The source class is strong: a civil birth register image is direct evidence for a birth registration and declared parent fields when the row is correctly identified.
- The assigned chunk and held source packet agree that entry 172 on page 58 is for `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 about 3 p.m. at Calle de Valdivia, with father `Jose del Carmen Pulgar S.` or a similar father-field reading, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- Direct visual review of the referenced source image is consistent with the Pulgar/Arriagada row at page 58 entry 172 and inconsistent with the converted Markdown's Burgos/de la Cruz row for that same entry number.
- The staged identity-analysis draft properly identifies the problem as a conversion conflict and recommends hold rather than promotion.

## Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration image is a high-quality original source for birth and parent evidence, subject here to handwriting readability and row-certification risk. |
| conversion_confidence_score | 0.52 | The chunk and image review support the Pulgar/Arriagada row, but the canonical converted Markdown gives a materially different row. |
| evidence_quantity_score | 0.72 | There is one direct source image plus multiple derivative verification notes, enough to identify the conflict but not enough to promote dependent claims. |
| agreement_score | 0.44 | Chunk, source packet, and image align with each other, but the converted Markdown sharply disagrees on child, parents, birth date, place, and informant. |
| identity_confidence_score | 0.64 | The Pulgar/Arriagada child identity is more likely than the converted Burgos/de la Cruz reading for this image, but row QA is required before canonical use. |
| claim_probability | 0.70 | The staged draft's claim that this is a row-level conflict requiring hold is well supported; the underlying identity and relationship claims are not proof-ready. |
| relevance_level | high | If certified, the row is directly relevant to Pulgar/Arriagada identities and parent-child relationships. |
| relevance_confidence | 0.92 | The row contains family-relevant Pulgar and Arriagada terms, independent of later identity bridge questions. |
| canonical_readiness | hold_for_conversion_qa | Do not promote claims, relationships, merges, or Dario-line attachments until targeted conversion QA resolves the row and father field. |

## Reviewed Materials

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526172507192.md`
- Conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md`
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526171029823.md`
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`

## Next Action

Run targeted conversion QA against the source image, current converted Markdown, assigned chunk, and held source packet. QA should certify the controlling row for page 58 entry 172 and the exact father-field reading. After QA, rerun proof review before promoting any child identity, birth fact, parent name, parent-child relationship, parent merge, or Dario-line comparison.
