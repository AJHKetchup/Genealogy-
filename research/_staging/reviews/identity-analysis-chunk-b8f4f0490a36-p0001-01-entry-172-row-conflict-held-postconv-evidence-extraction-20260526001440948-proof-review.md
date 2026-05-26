---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260526231446918"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-held-postconv-evidence-extraction-20260526001440948.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-held-postconv-evidence-extraction-20260526001440948.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
reviewed: 2026-05-26
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers

- The staged draft is correct to treat this as a conversion row-control problem, not as promotable identity evidence. The referenced converted Markdown assigns entry 172 to Jose Miguel, son of Oswaldo Burgos and Concepcion de la Cruz, while the referenced chunk and visible page image support a different entry 172 row for Jose del Carmen Segundo Pulgar Arriagada.
- Because the controlling transcription is internally conflicted, no canonical child identity, birth date, birthplace, parent-child relationship, parent identity merge, or Dario-line comparison should be promoted from this staged draft.
- The father field should remain uncertified beyond the clearly supported start of the name until targeted conversion QA resolves whether the trailing mark is `S.`, another suffix, or uncertain.

## Evidence Strengths

- The source is a contemporaneous civil birth register image, which is a strong source type for a birth registration once row control is resolved.
- The referenced chunk, source packet, conflict candidate, and page image agree that the visible row numbered 172 is a Pulgar/Arriagada row.
- The staged draft preserves the anti-conflation boundary: it does not assert that this record directly names Dario, Arturo, Smith, Dario Jose, or a later Dario Pulgar-Arriagada identity.

## Scores

- source_quality_score: 0.90
- conversion_confidence_score: 0.35
- evidence_quantity_score: 0.55
- agreement_score: 0.40
- identity_confidence_score: 0.45
- claim_probability: 0.60 for the limited claim that the staged draft identifies a real row-control conflict; 0.30 for any dependent canonical Pulgar/Arriagada identity or relationship claim before QA.
- relevance_level: high
- relevance_confidence: 0.85
- canonical_readiness: hold_for_conversion_qa

## Judgment

The draft is literally supported as a conflict analysis. It accurately reports that the converted Markdown and the assigned chunk disagree materially for entry 172, and the page image supports the concern that the converted Markdown is not controlling for this row.

This review does not certify a corrected transcription. It only supports holding the evidence and routing the source image, converted Markdown, chunk, source packet, and conflict note to targeted conversion QA.

## Next Action

Run targeted conversion QA for entry 172 and certify row control against the page image. After QA, rerun proof review before promoting any child identity, birth fact, parent-child relationship, parent identity merge, or Dario-line comparison.
