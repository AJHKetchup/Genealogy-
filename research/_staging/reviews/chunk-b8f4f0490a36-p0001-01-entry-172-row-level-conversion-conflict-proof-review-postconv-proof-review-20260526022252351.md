---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260526022252351"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014144513.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014144513.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: "2026-05-26"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

1. Row-control remains unresolved at the conversion-file level. The referenced chunk and source packet identify entry 172 on page 58 as the Pulgar/Arriagada row, and the source image visibly supports that row, but the referenced converted Markdown records entry 172 as a Burgos/de la Cruz row from a different apparent page/spread.
2. The converted Markdown cannot be treated as controlling evidence for any entry-172 Pulgar/Arriagada claim until targeted conversion QA reconciles or replaces it. This blocks canonical birth, parent, residence, informant, and relationship claims based on this draft.
3. The father-name suffix is not fully certified by this proof review. The row visibly supports the beginning `Jose del Carmen Pulgar`; the chunk reads `Jose del Carmen Pulgar S.`, but the trailing mark/suffix should remain uncertain pending targeted image QA.
4. Parent-identity and duplicate-person conclusions are not supported by this draft. `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, and possible `Juana de Dios Amagada de Pulgar` overlap require separate identity proof after row QA.
5. No Dario identity attachment is supported. The reviewed evidence names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario, Arturo, Smith, Pulgar-Smith, Dario Jose, or any kinship bridge to those clusters.

## Evidence Strengths

- The source type is a civil birth register, which is strong direct evidence for a birth-row claim when the row is correctly controlled.
- The referenced chunk gives a coherent transcription for page 58, entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 about 3 p.m. at Calle de Valdivia, father beginning `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The source packet explicitly reports image-reviewed support for the Pulgar/Arriagada row and correctly recommends `hold_for_conversion_qa`.
- Visual check of the referenced source image supports the staged draft's row-control concern: page 58 entry 172 appears to be the Pulgar/Arriagada row, not the Burgos/de la Cruz row in the current converted Markdown.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil birth registration image is a high-quality direct source for the event, assuming correct row control. |
| conversion_confidence_score | 0.42 | The chunk and image align, but the referenced converted Markdown materially contradicts them. |
| evidence_quantity_score | 0.70 | One direct source image, one chunk, one source packet, and one conflicting converted file were reviewed; no independent corroborating source was used. |
| agreement_score | 0.50 | Source packet, chunk, and visible image agree on Pulgar/Arriagada; converted Markdown disagrees completely. |
| identity_confidence_score | 0.72 | The row likely identifies a `Jose del Carmen Segundo Pulgar Arriagada` birth entry, reduced by unresolved conversion control and father suffix uncertainty. |
| claim_probability | 0.68 | Probable that page 58 entry 172 is Pulgar/Arriagada on current reviewed evidence, but not enough for canonical promotion. |
| relevance_level | 0.90 | Highly relevant to Pulgar/Arriagada parentage and anti-conflation review if certified. |
| relevance_confidence | 0.86 | Names and context are directly relevant, but final use depends on conversion QA. |
| canonical_readiness | 0.10 | Hold. The row-control conflict must be resolved before promotion or merge work. |

## Claim-Level Disposition

| Claim Or Hypothesis | Probability | Disposition |
| --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.68 | Hold for targeted conversion QA; likely but not canonical-ready. |
| Entry 172 is the Burgos/de la Cruz row in the current converted Markdown. | 0.12 | Treat as a conversion conflict, not controlling evidence for this staged draft. |
| `Jose del Carmen Pulgar S.` is the fully certified father reading. | 0.55 | Hold; visible start is supported, suffix needs targeted image QA. |
| Existing Jose/Juana parent candidates are duplicates or variants. | 0.25 | Hold; this draft supplies an identity watch issue, not a merge proof. |
| Entry-172 child is the same person as any Dario candidate. | 0.03 | Reject for promotion; only useful as an anti-conflation checkpoint. |

## Source Boundary Notes

- This review verifies that the Pulgar/Arriagada row is visibly present in the source image at page 58 entry 172, but it does not edit or correct the converted Markdown.
- The review does not promote facts to `research/claims`, `research/relationships`, `wiki/people`, `wiki/families`, or other canonical locations.
- The review treats `Jose del Carmen Pulgar S.` as an uncertain conversion reading, not as a corrected canonical name.

## Next Action

Run targeted conversion QA for the source image, referenced converted Markdown, and chunk `CHUNK-b8f4f0490a36-P0001-01`. The QA note should decide which row controls entry 172 and certify the father field only to the visible extent. After QA, rerun proof review for the child identity, birth details, parents, residence, informant, and any separate Jose/Juana parent-identity comparison.
