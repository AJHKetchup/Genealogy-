---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260526020941456"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014144513.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014144513.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: "2026-05-26"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

1. The current converted Markdown and the assigned chunk do not agree on the controlling row for entry 172. The converted Markdown gives a Burgos/de la Cruz child, while the chunk and visible source image give a Pulgar/Arriagada child.
2. Because the row-control conflict changes the child, parents, birth date, birth time, residence, and informant, no child identity, parent-child relationship, residence, or informant claim should be promoted from this draft.
3. The father field remains only partly certified. The image and packet support a name beginning `Jose del Carmen Pulgar`, but the trailing mark or suffix should remain unresolved pending targeted conversion QA.
4. The draft does not supply identity-bearing evidence connecting the entry-172 child to any Dario candidate. Any Dario comparison should remain an anti-conflation note only.
5. Existing Jose/Juana wiki clusters are relevant as identity-risk context, but this draft does not prove that any Jose or Juana candidate pages are duplicates or variants.

## Evidence Strengths

- The source type is strong: a civil birth registration image for Los Angeles, Chile, dated in the register context to April 1888.
- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at about 3 p.m. on Calle de Valdivia, with parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- The source packet explicitly reports image-reviewed support for the Pulgar/Arriagada row and recommends `hold_for_conversion_qa`.
- Direct image review in this proof review confirms that page 58, entry 172 is visibly a Pulgar/Arriagada row, not the Burgos/de la Cruz row currently present in the converted Markdown.
- The draft handles uncertainty conservatively by recommending hold rather than promotion, and by separating Dario-line anti-conflation from identity proof.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil birth register image is a strong original-record source for the event if the correct row is certified. |
| conversion_confidence_score | 0.42 | The chunk and image align, but the canonical converted Markdown materially conflicts with them. |
| evidence_quantity_score | 0.68 | There is one direct register image plus a chunk and source packet; there is not yet an independent corroborating record. |
| agreement_score | 0.45 | Source image, chunk, and source packet agree with each other, but the converted Markdown disagrees on the entire row. |
| identity_confidence_score | 0.70 | The entry-172 Pulgar/Arriagada child is likely supported by the visible row, reduced by unresolved conversion governance. |
| claim_probability | 0.72 | Probable that the source image row is Pulgar/Arriagada, but not ready for canonical use until conversion QA resolves the converted-file conflict. |
| relevance_level | 0.90 | Directly relevant to Pulgar/Arriagada birth and parentage research if certified. |
| relevance_confidence | 0.86 | The visible names and family terms align with the Pulgar/Arriagada research target. |
| canonical_readiness | 0.10 | Hold. The record is promising but blocked by row-control and father-field certification issues. |

## Claim-Level Review

| Claim or hypothesis | Probability | Review disposition |
| --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.72 | Hold for targeted conversion QA; probable on image and chunk evidence. |
| Entry 172 is the Burgos/de la Cruz row from the converted Markdown. | 0.12 | Treat as conversion-conflict evidence, not as controlling for this draft. |
| `Jose del Carmen Pulgar S.` is the fully certified father reading. | 0.55 | Revise/hold; visible source supports `Jose del Carmen Pulgar` but suffix requires targeted review. |
| `Juana Arriagada de Pulgar` is the mother named in the Pulgar row. | 0.78 | Hold for row QA; visually and chunk-supported, but affected by row-control governance. |
| Entry-172 child is the same person as any Dario candidate. | 0.04 | Reject for promotion; no identity-bearing bridge in this draft. |
| Existing Jose/Juana parent candidates are duplicates or variants. | 0.25 | Hold as identity-risk context only; this draft does not prove merges. |

## Reliability And Risk Notes

- Literal support: the staged draft accurately reports the major conflict between the current converted Markdown and the chunk/source-packet evidence.
- Source reliability: high for event facts once the correct row is certified.
- Conversion reliability: currently mixed because two local derived texts disagree completely.
- Identity risk: high if promoted prematurely, because the conflict would attach a different child and parent set to the same entry number.
- Relationship risk: high for parent-child claims and moderate-to-high for Jose/Juana duplicate or variant hypotheses.
- Relevance risk: low for Pulgar/Arriagada research if the row is certified; high for Dario attachment because this source does not name Dario.

## Next Action

Run targeted conversion QA on the source image, converted Markdown, and assigned chunk to certify the controlling row for entry 172 and the father-field reading. After that QA, rerun proof review before promoting any child identity, birth fact, parent-child relationship, residence, informant, parent merge, or Dario-line comparison.
