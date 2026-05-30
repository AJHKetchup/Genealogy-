---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530042938381
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205831848.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205831848.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_prior_review: "research/_staging/reviews/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-proof-review-postconv-proof-review-20260525204415696.md"
source_image_status: "referenced_source_image_not_found_at_recorded_path"
source_quality_score: 0.72
conversion_confidence_score: 0.30
evidence_quantity_score: 0.55
agreement_score: 0.40
identity_confidence_score: 0.56
claim_probability: 0.62
relevance_level: high
relevance_confidence: 0.96
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row Conflict Identity Analysis

This review covers only the staged draft `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205831848.md`.

## Blockers First

1. Canonical readiness remains `hold_for_conversion_qa`. The staged draft is correct to block promotion because the assigned chunk/source packet and the current converted Markdown disagree on the controlling row for entry 172.
2. The source image recorded in the packet and manifest was not available at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, and no page image was present under the conversion job directory during this review. I therefore cannot newly certify the handwriting or father-field ending from the visible source.
3. The assigned chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
4. The current converted Markdown reads entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
5. These are row-level conflicts, not spelling variants. Child identity, parents, birth date, birth place, and informant context all change.
6. The father field must not be normalized beyond the reviewed derivative text. Keep it unresolved pending visual QA as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
7. No Dario-line identity bridge is supported by the reviewed materials. The draft properly treats Dario comparisons as anti-conflation guidance only.

## Evidence Strengths

- The staged draft accurately identifies the controlling proof problem: competing derivative readings for the same entry number and page context.
- The source packet and assigned chunk are internally consistent for the Pulgar/Arriagada row, including child name, sex, registration date, birth date/time/place, parents, residences, and informant.
- The converted Markdown is directly inconsistent with that packet/chunk, which supports the draft's conclusion that the issue is conversion or assignment control rather than a person-merge question.
- The prior proof review also held the item for conversion QA and independently noted that no Dario candidate is named in the reviewed entry context.

## Evidence And Probability Scoring

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.72 | Civil birth registration is high-quality source type, but the source image was unavailable at the recorded path during this review, so visual certification is not refreshed here. |
| conversion_confidence_score | 0.30 | The assigned chunk/source packet and current converted Markdown materially disagree for entry 172. |
| evidence_quantity_score | 0.55 | One source packet, one assigned chunk, one current converted file, and one prior review were checked; no independent corroborating identity source was reviewed. |
| agreement_score | 0.40 | Packet and chunk agree with each other, but the converted Markdown gives a different row identity. |
| identity_confidence_score | 0.56 | The Pulgar/Arriagada reading is plausible within the assigned chunk/packet chain, but identity confidence is capped by the row conflict and missing source image. |
| claim_probability | 0.62 | The staged draft's probability is reasonable for the Pulgar/Arriagada hypothesis, but it remains a scored judgment, not promotion-ready proof. |
| relevance_level | high | Directly relevant to the staged identity-conflict draft and Pulgar/Arriagada parent-candidate analysis. |
| relevance_confidence | 0.96 | All reviewed files point to the same chunk id and entry-172 task even though they disagree on row content. |
| canonical_readiness | hold_for_conversion_qa | Do not promote child identity, parent claims, relationships, merges, or Dario-line attachments from this review. |

## Claim-Specific Assessment

| Claim Or Hypothesis | Probability | Review Judgment |
| --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.62 | Supported by the assigned chunk and source packet; blocked by converted Markdown conflict and unavailable source image. |
| Entry 172 is the Burgos/de la Cruz row for `José Miguel`. | 0.28 | Supported by the current converted Markdown only; conflicts with the assigned chunk and source packet. |
| `Jose del Carmen Pulgar S.` is the father as a certified literal reading. | 0.42 | Derivative chunk support exists, but the ending requires targeted visual QA before canonical use. |
| `Juana Arriagada de Pulgar` is the mother if the Pulgar row controls. | 0.58 | Supported within the Pulgar/Arriagada derivative chain; still held pending row control. |
| This source supports a Dario identity bridge. | 0.02 | No Dario name or linking relationship appears in the reviewed materials. |

## Next Action

Keep the staged draft and all dependent claims on `hold_for_conversion_qa`.

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the actual source/page image, the assigned chunk, the current converted Markdown, and the source packet. The QA note should decide the controlling entry-172 row and certify the father field only to the extent visible. After QA, rerun proof review before any canonical claim, relationship, identity merge, parent merge, or Dario-line comparison is promoted.
