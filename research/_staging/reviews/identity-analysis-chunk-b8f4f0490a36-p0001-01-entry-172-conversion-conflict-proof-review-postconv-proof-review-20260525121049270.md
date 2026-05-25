---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525121049270
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525091830000.md"
reviewed_staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525091830000.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525081514407.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity-Analysis Conversion Conflict

## Blockers First

1. The staged identity-analysis draft is correct that there is a material row-level derivative conflict. The source image and current chunk support entry 172 as a Pulgar/Arriagada birth row, while the assigned converted Markdown gives a different Gomez/de la Cruz row for entry 172.
2. The converted Markdown cannot be used as the controlling transcription for Pulgar/Arriagada claims in its current state. It conflicts on child name, father, mother, birth date, birth place, informant, occupations, residences, and official signature.
3. The father-name ending after `Pulgar` remains a literal-reading uncertainty. The chunk reads `Jose del Carmen Pulgar S.`, and the image appears compatible with a short trailing mark or abbreviation, but this review should not normalize it beyond what targeted conversion QA certifies.
4. No Dario, Arturo, Smith, Geneva/ICRC, passenger, medical, Alexander John Heinz, or later expropriation identity bridge is supported by the reviewed source context. Any Dario-line attachment remains blocked.
5. Canonical readiness is `hold_for_conversion_qa`. Do not promote dependent claims or relationships until the converted derivative is corrected, superseded, or explicitly marked non-controlling for this entry.

## Evidence Strengths

- The page image visibly places entry 172 on register page 58 and supports a child name consistent with `Jose del Carmen Segundo Pulgar Arriagada`, not `Jose Francisco`.
- The current chunk and staged source packet agree on the Pulgar/Arriagada row: registration date 7 April 1888, birth date 8 March 1888 at 3 p.m., birth place Calle de Valdivia, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The source class is strong for the basic event and parent claims because it is a civil birth register. The limiting issue is not source type, but derivative inconsistency.
- The staged draft handles the conflict conservatively by keeping the row at `hold_for_conversion_qa` and rejecting unsupported Dario-line linkage.

## Literal Support Check

| Reviewed point | Support judgment | Notes |
| --- | --- | --- |
| Entry 172 as Pulgar/Arriagada row | Supported by image, chunk, and source packet | The image and chunk align against the assigned converted Markdown. |
| Child `Jose del Carmen Segundo Pulgar Arriagada` | Supported with normal transcription caution | Image is consistent; chunk/source packet provide the literal derivative text. |
| Father `Jose del Carmen Pulgar S.` | Partially supported, unresolved suffix | Keep exact father-name form under QA control. |
| Mother `Juana Arriagada de Pulgar` | Supported by chunk/source packet and visible-source context | No independent identity anchor beyond this row. |
| Birth facts for 8 March 1888, 3 p.m., Calle de Valdivia | Supported by chunk/source packet and visible-source context | Converted Markdown conflicts with different birth facts. |
| Gomez/de la Cruz converted row as controlling entry 172 | Not supported by source image inspected for this review | Treat as conversion or assignment error until QA resolves it. |
| Dario-line identity or relationship claim | Not supported | No direct name, relationship, or bridge appears in reviewed context. |

## Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration is a high-value source class for birth and parent facts; image is available for direct checking. |
| conversion_confidence_score | 0.42 | The current chunk is persuasive for the Pulgar row, but the assigned converted Markdown materially disagrees. |
| evidence_quantity_score | 0.62 | One direct register row plus image/chunk/source packet derivatives; no corroborating independent source. |
| agreement_score | 0.54 | Image, chunk, source packet, conflict note, and staged identity analysis agree, but the converted Markdown disagrees at row level. |
| identity_confidence_score | 0.68 | The local child-parent row is probable if the chunk/image reading controls; parent same-person conclusions remain weak. |
| claim_probability | 0.78 | The Pulgar/Arriagada birth-row claim is likely from the visible source context, pending conversion QA. |
| relevance_level | high_for_pulgar_arriagada_birth_row; low_for_dario_identity | Directly relevant to the 1888 Pulgar/Arriagada row, not to any Dario candidate. |
| relevance_confidence | 0.89 | The surnames and row content are clearly family-relevant if the Pulgar row is confirmed. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until the derivative conflict and father suffix are resolved. |

## Review Decision

The staged identity-analysis draft is substantially supported as a conflict analysis. Its central conclusion should stand: this is not a spelling variant, and not a promotion-ready identity or relationship proof. The most defensible handling is `hold_for_conversion_qa`, with an added emphasis that the source image inspected for this review favors the Pulgar/Arriagada row over the assigned converted Markdown.

## Next Action

Run targeted conversion QA against the source image, assigned converted Markdown, and current chunk for register page 58, entry 172. The QA note should decide whether the converted Markdown is wrong or misassigned, certify the child and parent row, and preserve the father field as one of: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical claim, relationship, or identity merge is promoted.
