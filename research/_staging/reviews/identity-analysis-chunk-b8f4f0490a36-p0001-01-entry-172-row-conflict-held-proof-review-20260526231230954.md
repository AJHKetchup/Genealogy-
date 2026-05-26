---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260526231230954"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-held-postconv-evidence-extraction-20260526002943637.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-held-postconv-evidence-extraction-20260526002943637.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: 2026-05-26
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers

- The staged draft is correct to hold the item: the converted Markdown and assigned chunk give incompatible readings for entry 172. The converted Markdown identifies a Burgos/de la Cruz child, while the chunk identifies a Pulgar/Arriagada child.
- The disagreement is row-level and affects child identity, birth date, birth time, birthplace, father, mother, parent residence, informant, and relationship evidence.
- The source image visible in this review appears more consistent with the assigned chunk's Pulgar/Arriagada row than with the converted Markdown's Burgos/de la Cruz row, but this review should not be treated as a corrected transcription. Targeted conversion QA still needs to certify the controlling row.
- The father field should remain bounded to the visible-source question already stated in staging: whether the field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- No Dario, Arturo, Smith, Dario Jose, or later Dario Pulgar-Arriagada identity is named in the checked evidence. Any Dario-line comparison would be a relationship or identity jump.

## Scores

- source_quality_score: 0.86
- conversion_confidence_score: 0.32
- evidence_quantity_score: 0.55
- agreement_score: 0.22
- identity_confidence_score: 0.38
- claim_probability: 0.82 for the staged draft's hold recommendation; 0.30 for promoting any Pulgar/Arriagada child or parent-child claim before QA
- relevance_level: high for Pulgar/Arriagada family research if row control is confirmed; low for any direct Dario identity claim
- relevance_confidence: 0.78 for Pulgar/Arriagada relevance; 0.90 that direct Dario relevance is not shown
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The source is a civil birth registration image with an identified source path and SHA-256 in the source packet and chunk metadata.
- The assigned chunk, source packet, and conflict note consistently describe the same Pulgar/Arriagada candidate row for entry 172.
- The staged draft accurately frames the issue as a conversion row-control conflict before identity linking.
- The anti-conflation warning is appropriate: surname and parent-name similarity are not enough to merge persons or connect the record to a later Dario-line identity.

## Next Action

Route the source image, converted Markdown, assigned chunk, source packet, and conflict note to targeted conversion QA. QA should certify the controlling row for entry 172 and the father-field reading only to the visible extent. After QA, rerun proof review before promoting any claim, relationship, identity merge, or Dario-line comparison.
