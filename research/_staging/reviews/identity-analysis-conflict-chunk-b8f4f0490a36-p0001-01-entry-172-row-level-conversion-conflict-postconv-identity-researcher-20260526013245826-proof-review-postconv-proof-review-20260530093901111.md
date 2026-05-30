---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260530093809595
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013245826.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013245826.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image_path_checked: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- The exact staged draft under review is `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013245826.md`.
- The referenced source image path could not be opened from this workspace. `raw/sources` currently contains no matching `Registro de Nacimientos...Entry No. 172;.png`, and the referenced conversion-job directory contains page markdown and work orders but no extracted source image. I therefore cannot independently certify the visible handwritten row.
- The referenced converted Markdown and referenced chunk materially disagree for the same source path, same converted SHA, same chunk id, page 1, register page 58, entry 172. The converted Markdown gives a Burgos/de la Cruz entry for `Jose Miguel`; the chunk gives a Pulgar/Arriagada entry for `Jose del Carmen Segundo Pulgar Arriagada`.
- Because the original image is unavailable and the conversion artifacts conflict, no child identity, parent-child relationship, parent merge, birth fact, residence fact, or Dario-line bridge should be promoted from this review.
- The father field cannot be certified by this proof review. The staged draft's bounded uncertainty around `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` remains appropriate.

## Evidence Strengths

- The staged draft accurately identifies the controlling problem as a row-level conversion-control conflict, not an ordinary same-person or name-variant dispute.
- The source packet and conflict draft consistently report the Pulgar/Arriagada reading: child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`, and birth/registration details tied to March and April 1888.
- The converted Markdown consistently reports a different row for entry 172: child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth 6 April 1888, and informant `Oswaldo Burgos`.
- The staged draft properly warns against attaching this entry to Dario, Arturo, Smith, or Dario Pulgar Arriagada identities. None of the reviewed conversion text names those people or provides a lineage bridge.

## Scores

| category | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.62 | A civil birth register would be a strong source type, but the source image is unavailable for this review and the conversion chain is internally inconsistent. |
| conversion_confidence_score | 0.25 | Two referenced conversion artifacts for the same image/checksum give incompatible entry-172 rows. |
| evidence_quantity_score | 0.45 | There is one relevant source packet, one conflict note, one converted file, and one chunk, but they reduce to one disputed source instance. |
| agreement_score | 0.20 | The packet/conflict/chunk agree with each other, but the converted Markdown directly contradicts them on every identity-bearing field. |
| identity_confidence_score | 0.30 | Identity confidence is low until row control and the father field are certified from the visible source. |
| claim_probability | 0.78 | The claim that this staged item must remain on hold for conversion QA is strongly supported by the artifact conflict and missing image access. |
| relevance_level | high | If certified, this entry is highly relevant to Pulgar/Arriagada identity and parent-child claims. |
| relevance_confidence | 0.86 | Relevance is clear from the chunk/source-packet reading, but promotion relevance depends on resolving row control. |
| canonical_readiness | 0.00 | No canonical promotion is ready from this review. |

## Claim Judgment

The staged draft's hold recommendation is supported. The review can confirm a serious artifact-level conflict between the referenced converted Markdown and the referenced chunk/source packet, but cannot independently certify the visible source transcription because the source image is missing from the expected path.

Probability that entry 172 is ready for canonical Pulgar/Arriagada promotion: 0.00.

Probability that targeted conversion QA is required before any proof promotion: 0.95.

## Next Action

Keep `canonical_readiness: hold_for_conversion_qa`. The next worker should restore or locate the original source image for SHA `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, compare it against the converted Markdown and chunk, certify the controlling row for entry 172, and only then rerun proof review for any Pulgar/Arriagada child, parent, relationship, merge, or Dario-line claim.
