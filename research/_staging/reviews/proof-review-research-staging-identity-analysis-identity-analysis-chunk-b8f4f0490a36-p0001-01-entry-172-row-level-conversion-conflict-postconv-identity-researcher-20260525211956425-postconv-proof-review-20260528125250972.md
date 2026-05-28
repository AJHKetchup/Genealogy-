---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260528125250972
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525211956425.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525211956425.md"
reviewed_files:
  - "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525211956425.md"
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525203741061.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_quality_score: 0.86
conversion_confidence_score: 0.35
evidence_quantity_score: 0.62
agreement_score: 0.32
identity_confidence_score: 0.64
claim_probability: 0.70
relevance_level: high
relevance_confidence: 0.94
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- The staged draft is held correctly: the assigned converted Markdown and assigned chunk describe incompatible row-172 families.
- The converted Markdown reads entry 172 as child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- The assigned chunk and source packet read entry 172 as child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- Direct source-image review supports the Pulgar/Arriagada row as the visible row 172 on page 58, but this review does not rewrite the converted Markdown or certify a corrected transcription.
- The father field suffix remains uncertain. The review cannot safely choose among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- No canonical claim, relationship, identity merge, parent merge, or Dario-line comparison is ready while row-control and father-field QA remain unresolved.

## Evidence Strengths

- The source is a civil birth registration image for Los Angeles, Chile, 1888, page 58, entry 172; source quality is strong for a birth, parent, residence, and informant claim if the row transcription is settled.
- The chunk and source packet agree on the Pulgar/Arriagada child, registration date, birth date and time, birth place, parents, parental residences, and informant.
- The visible page image aligns with the chunk/source-packet family cluster rather than the Burgos/de la Cruz converted Markdown row.
- The staged identity analysis correctly treats this as a row-level conversion conflict, not a name variant, duplicate-person merge, or promoted parent-child proof.
- The draft correctly rejects Dario/Dario Arturo/Dario Jose bridging: the source row does not name Dario, Arturo, Smith, or any literal Dario-line identifier.

## Scored Judgment

| factor | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth registration image is a strong source type, though legibility and row alignment require care. |
| conversion_confidence_score | 0.35 | Low, because derivative transcripts disagree at the whole-row level. |
| evidence_quantity_score | 0.62 | One source image plus multiple derivative notes; quantity is enough to identify the issue, not enough to promote. |
| agreement_score | 0.32 | Chunk/source packet agree with each other, but the converted Markdown conflicts materially. |
| identity_confidence_score | 0.64 | Moderate for a Pulgar/Arriagada entry-172 candidate after image review; not final because conversion QA is unresolved. |
| claim_probability | 0.70 | Probability that visible entry 172 is the Pulgar/Arriagada row, subject to targeted QA. |
| relevance_level | high | The row is directly relevant to Pulgar/Arriagada identity and parent-child claims if verified. |
| relevance_confidence | 0.94 | Relevance is high because the chunk/source packet name Pulgar and Arriagada directly. |
| canonical_readiness | hold_for_conversion_qa | Not ready for canonical use until row-control and father-field QA are complete. |

## Claim-Level Assessment

- Pulgar/Arriagada child identity claim: probable but held. Literal support exists in the chunk/source packet and visible image, but the converted Markdown conflict prevents promotion.
- Burgos/de la Cruz child identity claim: unsupported by the chunk/source packet and not supported by my source-image check for row 172; keep as the conflicting converted-text reading until QA resolves the derivative mismatch.
- Parent-child relationship to `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`: direct under the Pulgar row hypothesis, but held because row control and father suffix are unresolved.
- Same-person or parent merge for `Jose del Carmen Pulgar`: not supported by this review. Name overlap alone is insufficient.
- Dario-line relevance: no literal support for a Dario identity. Any Dario comparison should remain a negative/guardrail note, not a claim.

## Next Action

Run targeted conversion QA for page 58, entry 172 against the source image, converted Markdown, chunk, and source packet. The QA note should explicitly decide the controlling row for entry 172 and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical promotion.
