---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526063001716
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044220967.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044220967.md"
reviewed_sources:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_quality_score: 0.78
conversion_confidence_score: 0.30
evidence_quantity_score: 0.45
agreement_score: 0.35
identity_confidence_score: 0.58
claim_probability: 0.62
relevance_level: high
relevance_confidence: 0.88
canonical_readiness: hold
canonical_readiness_score: 0.10
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

1. The staged identity analysis is not proof-ready for canonical promotion because the referenced converted Markdown and referenced chunk assign entry 172 to different children, different parents, different birth dates, different birth places, and different informants.
2. The converted Markdown records entry 172 as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 1888-04-06 at 10 p.m. The chunk and source packet record entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, born 1888-03-08 at 3 p.m.
3. The source image appears broadly consistent with the Pulgar/Arriagada row on page 58, entry 172, but this review is not a targeted transcription QA pass and should not silently replace the existing converted Markdown.
4. The father field remains a specific conversion-risk point. Do not normalize or promote `Jose del Carmen Pulgar S.` as `Jose del Carmen Pulgar` until QA certifies the visible reading.
5. No Dario-line bridge is supported by this evidence. The staged draft correctly treats Dario comparison as anti-conflation context only.

## Evidence Strengths

- The staged draft accurately reports the material conflict between the chunk/source packet and the current converted Markdown.
- The chunk, source packet, conflict note, and visible source image all support treating the Pulgar/Arriagada reading as plausible and highly relevant.
- The staged draft appropriately avoids claiming a canonical identity merge, parent-child promotion, or Dario-line bridge from the disputed row.
- The recommendation to hold for conversion QA is supported by the evidence reviewed.

## Scored Judgment

| Category | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil birth registration image is a strong source type, but the working evidence is affected by competing derivative transcriptions. |
| conversion_confidence_score | 0.30 | The conversion layer is internally conflicted; the chunk and converted file cannot both be correct for the same entry row. |
| evidence_quantity_score | 0.45 | One source image and two derivative readings are available; there is no independent corroborating source in this review packet. |
| agreement_score | 0.35 | Chunk/source packet agree with each other and broadly with the image; converted Markdown sharply disagrees. |
| identity_confidence_score | 0.58 | Pulgar/Arriagada identity is the stronger current hypothesis, but not proof-ready while the conversion conflict remains unresolved. |
| claim_probability | 0.62 | More likely than not that the staged draft's hold-and-QA conclusion is correct; the underlying child/parent claim itself remains provisional. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parent-child claims. |
| relevance_confidence | 0.88 | The disputed row contains the target surnames and direct family terms if the chunk reading is certified. |
| canonical_readiness | hold | Do not promote to canonical claims, relationships, or wiki pages until targeted conversion QA resolves the row. |

## Claim Probability And Readiness

- Pulgar/Arriagada row as controlling entry 172: probability 0.62; canonical readiness `hold`.
- Burgos/de la Cruz row as controlling entry 172: probability 0.28; canonical readiness `hold`.
- Father claim `Jose del Carmen Pulgar S.` for the Pulgar/Arriagada child: probability 0.54; canonical readiness `hold`.
- Mother claim `Juana Arriagada de Pulgar` for the Pulgar/Arriagada child: probability 0.60; canonical readiness `hold`.
- Any Dario-line relationship or identity bridge from this row: probability 0.03; canonical readiness `blocked`.

## Next Action

Run targeted conversion QA against `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, the current converted Markdown, and the chunk. QA should decide the controlling entry-172 row and explicitly certify the father-field reading. After QA, rerun proof review before any canonical promotion.
