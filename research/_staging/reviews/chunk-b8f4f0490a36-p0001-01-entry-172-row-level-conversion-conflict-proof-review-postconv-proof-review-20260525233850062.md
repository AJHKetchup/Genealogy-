---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260525233850062"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230105907.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230105907.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Canonical readiness: hold. The staged draft correctly treats this as a row-level conversion conflict, not as a resolved identity claim.
- The referenced converted file and the referenced chunk do not describe the same entry 172. The chunk/source-packet reading gives `Jose del Carmen Segundo Pulgar Arriagada`; the converted Markdown gives `José Miguel`, with different parents, birth facts, and informant.
- The source image visually supports the need for targeted conversion QA: entry 172 on page 58 appears to be the Pulgar/Arriagada row, while the converted Markdown's Burgos/de la Cruz reading is unsupported by the visible entry 172 in the referenced image.
- Do not promote child identity, birth fact, father claim, mother claim, parent-child relationships, parent identity merges, or Dario/Pulgar-line comparisons from this staged draft until conversion QA certifies the controlling row and the father-name suffix.
- The visible/source-packet father field should remain uncertified at suffix level. This proof review does not authorize changing the transcription to any exact suffix form beyond a QA-limited reading.

## Scored Judgment

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration is a strong source type, and the referenced image is available. The score is reduced because the derivative conversion set is internally inconsistent. |
| conversion_confidence_score | 0.34 | Low for canonical use. The converted Markdown conflicts materially with the chunk/source packet and visible image for entry 172. |
| evidence_quantity_score | 0.62 | One source image, one chunk, one source packet, one conflict draft, and one converted file were available. Quantity is enough to identify the blocker but not enough to resolve it as proof. |
| agreement_score | 0.46 | Chunk, source packet, conflict draft, staged analysis, and visible image broadly agree on the Pulgar/Arriagada row; the converted file sharply disagrees. |
| identity_confidence_score | 0.41 | The Pulgar/Arriagada identity is plausible for entry 172, but the active conversion conflict prevents identity certification. |
| claim_probability | 0.70 | The staged draft's central claim, that entry 172 has a row-control conversion conflict requiring hold/QA, is well supported. The exact genealogical identity claim is not ready. |
| relevance_level | 0.99 | Directly relevant to the assigned staged draft and its claimed conversion conflict. |
| relevance_confidence | 0.98 | The reviewed files all reference the same chunk id, page/register context, source image, and entry number. |
| canonical_readiness | 0.04 | Hold for targeted conversion QA; not ready for canonical claims or relationships. |

## Evidence Strengths

- The staged draft accurately identifies the core conflict: two incompatible entry-172 readings exist in the local materials.
- The local chunk and source packet give a full Pulgar/Arriagada row with child, sex, registration date, birth date/time/place, parents, and informant.
- The current converted Markdown gives a different family for entry 172: `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth on 6 April 1888 at 10 p.m., place `En esta`, informant `Oswaldo Burgos`.
- The visible source image is consistent with the staged draft's caution that the converted Markdown is not reliable for this row.
- The staged draft correctly avoids merging the Pulgar/Arriagada child with Dario-line candidates and frames those comparisons as anti-conflation only.

## Relationship And Identity Risk

- Identity risk is high if `Jose del Carmen Segundo Pulgar Arriagada` is treated as the same person as `José Miguel`; the names, parents, and birth details differ.
- Relationship risk is high if parent-child links to `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar` are promoted before row-control QA.
- Dario-line relevance is indirect only. This entry does not name Dario, Arturo, Smith, Pulgar-Smith, or any descendant bridge.

## Next Action

Run targeted conversion QA against the referenced source image, converted Markdown, chunk, and source packet. The QA note should identify the controlling entry-172 row, explain why the converted file diverges from the chunk/source packet, and certify only the visible extent of the father field. After that, rerun proof review for the child identity, birth facts, parent names, and parent-child relationship claims.
