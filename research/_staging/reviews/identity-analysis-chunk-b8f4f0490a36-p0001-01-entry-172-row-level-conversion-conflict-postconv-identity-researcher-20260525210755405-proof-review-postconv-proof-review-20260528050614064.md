---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528050614064
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525210755405.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525210755405.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525203741061.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote child, birth, parent, or relationship claims from this staged draft while the assigned converted Markdown and assigned chunk disagree on entry 172.
2. The disagreement is a full family-cluster conflict, not a spelling variant. The converted Markdown gives entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`; the chunk and source packet give entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
3. Direct visual review of the referenced source image supports the Pulgar/Arriagada row as the visible entry 172 on page 58, but this proof review does not correct the converted Markdown. Targeted conversion QA still has to reconcile the official conversion record.
4. The father field remains field-level uncertain. The current chunk reads `Jose del Carmen Pulgar S.`, while the source packet correctly asks QA to certify whether the visible field should be treated as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
5. No reviewed evidence here names Dario, Arturo, Smith, a spouse, a child, or a later family bridge. Do not connect this entry to any Dario Pulgar identity cluster from this item alone.

## Evidence Strengths

- The source type is a civil birth register, which is high-value direct evidence for a birth and stated parents once the row is certified.
- The assigned chunk provides a complete row 172 reading with coherent date, place, child, parent, residence, informant, and official fields for the Pulgar/Arriagada family.
- The source packet documents prior direct image inspection and preserves the conversion conflict without silently editing the converted file.
- My direct visual check of the referenced page image agrees with the source packet on the narrow point that page 58 entry 172 visibly corresponds to the Pulgar/Arriagada row, not the Burgos/de la Cruz row shown in the assigned converted Markdown.
- The staged identity analysis correctly treats the Dario comparison as unsupported and correctly recommends hold-for-conversion-QA rather than promotion.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 3/10 overall because the canonical converted Markdown conflicts with the chunk; 7/10 for the narrow visual row identification in the page image |
| evidence_quantity_score | 4/10 |
| agreement_score | 5/10 overall: source image, chunk, source packet, and conflict draft agree on the Pulgar/Arriagada row, but the assigned converted Markdown materially disagrees |
| identity_confidence_score | 7/10 that the visible entry 172 row is the Pulgar/Arriagada row; 3/10 for any downstream parent-identity merge; 1/10 for any Dario identity bridge |
| claim_probability | 0.82 that visible entry 172 records the Pulgar/Arriagada birth row; 0.20 that the Burgos/de la Cruz converted row controls this source image; 0.05 or lower for any Dario merge or relationship claim |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold |

## Review Finding

The staged draft is supported as a hold. It accurately identifies a row-level conversion conflict and avoids promoting unsupported Pulgar-line or Dario-line identity conclusions.

For the narrow visible-source question, the page image supports the Pulgar/Arriagada row at entry 172. However, because the assigned converted Markdown still contains the incompatible Burgos/de la Cruz row, the proper action is conversion QA, not canonical promotion from this review.

The `Jose del Carmen Segundo Pulgar Arriagada` birth claim and the stated-parent claims for `Jose del Carmen Pulgar...` and `Juana Arriagada de Pulgar` are potentially strong after QA, but they are not canonical-ready yet. The father-name suffix and any parent-identity alignment with existing Jose/Juana pages require a separate proof step.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, converted Markdown, chunk, and source packet. The QA result should declare which entry 172 row controls and explicitly certify the father field. After that, rerun proof review for any child, birth, parent, relationship, or identity-bridge claim before promoting anything to canonical folders.
