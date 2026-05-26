---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260526225336792"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-held-postconv-evidence-extraction-20260526001440948.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-held-postconv-evidence-extraction-20260526001440948.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: 2026-05-26
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers

- The staged draft is supported as a conflict/hold note, but not as a promotable identity or relationship proof. The converted Markdown assigns entry 172 to a Burgos/de la Cruz birth row, while the chunk and visible source image show entry 172 as a Pulgar/Arriagada row.
- This row-control conflict affects the child name, parents, birth date, birth time, place, residence, and informant. Until conversion QA certifies the controlling transcription, no canonical claim or relationship should be promoted from this item.
- The father field should remain uncertified beyond the visible start "Jose del Carmen Pulgar" unless targeted QA confirms the trailing suffix or mark. The chunk's "Jose del Carmen Pulgar S." is plausible but should not be treated as final proof.
- The source does not directly support Dario, Arturo, Smith, Dario Jose, or a later Dario Pulgar-Arriagada identity. Any Dario-line comparison would be an identity-risk jump at this stage.

## Evidence Strengths

- The source is a civil birth register image, a strong source type for birth registration facts if row control is resolved.
- The assigned chunk and the source packet agree on a Pulgar/Arriagada entry 172: child Jose del Carmen Segundo Pulgar Arriagada, father beginning Jose del Carmen Pulgar, and mother Juana Arriagada de Pulgar.
- Visual inspection of the referenced source image supports the draft's basic row-control concern: entry 172 on page 58 appears to be a Pulgar/Arriagada row, not the Burgos/de la Cruz row found in the converted Markdown.
- The staged draft appropriately recommends `hold_for_conversion_qa` and warns against surname-based merging or Dario-line conflation.

## Scores

- `source_quality_score`: 0.85
- `conversion_confidence_score`: 0.35
- `evidence_quantity_score`: 0.45
- `agreement_score`: 0.40
- `identity_confidence_score`: 0.45
- `claim_probability`: 0.65 for the limited claim that entry 172 is probably a Pulgar/Arriagada row; 0.20 for any canonical child/parent relationship claim before QA.
- `relevance_level`: high
- `relevance_confidence`: 0.80
- `canonical_readiness`: hold_for_conversion_qa

## Review Judgment

The staged identity/conflict analysis is reviewable and should be retained as a hold note. It accurately treats the issue as a conversion row-control problem rather than an identity-merge proof. The visible source image and assigned chunk provide meaningful support for a Pulgar/Arriagada reading, but the derivative converted Markdown materially contradicts that reading for the same entry number.

Because the disagreement is at the row-control level, this item is not ready for canonical promotion. The only appropriate disposition is to keep dependent claims, relationships, merges, and Dario-line comparisons on hold until targeted conversion QA reconciles the image, converted Markdown, chunk, and source packet.

## Next Action

Route this item to targeted conversion QA. QA should certify the controlling row for entry 172 and transcribe the father field only to the visible extent, such as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA resolves the row conflict, rerun proof review before promoting any child identity, birth fact, parent-child relationship, parent merge, or Dario-line comparison.
