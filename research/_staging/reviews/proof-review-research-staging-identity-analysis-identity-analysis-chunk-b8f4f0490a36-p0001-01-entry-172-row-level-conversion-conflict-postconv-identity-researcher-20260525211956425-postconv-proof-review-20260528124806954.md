---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260528124806954
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525211956425.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525211956425.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
source_quality_score: 0.88
conversion_confidence_score: 0.35
evidence_quantity_score: 0.72
agreement_score: 0.30
identity_confidence_score: 0.62
claim_probability: 0.70
relevance_level: high
relevance_confidence: 0.96
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The staged draft is not ready for promotion to claims, relationships, people pages, family pages, or other canonical locations.
- The assigned converted Markdown and assigned chunk disagree on the complete entry-172 row. The converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`; the chunk reads entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- The source packet reports direct image inspection supporting the Pulgar/Arriagada row, and my limited image check also sees entry 172 on page 58 as a Pulgar/Arriagada row. This supports the draft's hold recommendation, but it does not authorize editing the converted Markdown in this review task.
- The father field remains a targeted QA issue. The visible row supports a `Jose del Carmen Pulgar...` reading, but the suffix or final mark is not settled enough here to certify `Jose del Carmen Pulgar S.` as canonical text.
- No visible or derivative evidence in the allowed context names Dario, Dario Jose, Dario Arturo, Darío, Smith, or Pulgar-Smith. Any Dario-line identity bridge remains unsupported.

## Evidence Strengths

- Source quality is strong: the underlying item is a civil birth registration image, and the staged draft, source packet, chunk, converted file, and source image are all locally available.
- The chunk and source packet agree on the Pulgar/Arriagada family cluster for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`, birth date `Ocho de Marzo de mil ochocientos ochenta i ocho`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and compareciente `Ernesto Herrera L.`.
- The page image gives independent support that entry 172 is not the Burgos/de la Cruz row represented in the converted Markdown. The conflict is therefore likely a row-control or conversion-file-assignment problem, not a same-person ambiguity or spelling variant.
- The staged draft correctly treats the Pulgar/Arriagada child and parent claims as probable but blocked, and correctly avoids promoting the Dario-line comparison.

## Scored Judgment

| item | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong primary source, though the review is constrained by derivative disagreement. |
| conversion_confidence_score | 0.35 | The assigned converted Markdown and assigned chunk disagree across the whole row. |
| evidence_quantity_score | 0.72 | There is one primary image plus two agreeing derivative contexts for the Pulgar reading, but only one event row is under review. |
| agreement_score | 0.30 | Agreement is high between chunk/source packet/image, but low across the assigned conversion set because the converted Markdown conflicts. |
| identity_confidence_score | 0.62 | The Pulgar child identity is plausible from the image-supported row, but row-control QA and father-field QA are still required. |
| claim_probability | 0.70 | The strongest current claim is that entry 172 is the Pulgar/Arriagada birth row, but it remains below promotion threshold because of conversion conflict. |
| relevance_level | high | If row-control QA confirms the Pulgar row, the evidence is directly relevant to Pulgar/Arriagada birth and parentage claims. |
| relevance_confidence | 0.96 | The Pulgar and Arriagada terms are literal in the chunk, packet, and visible row. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until targeted QA certifies the controlling row and father field. |

## Claim-Level Assessment

| claim or hypothesis | probability | identity risk | relationship risk | review disposition |
| --- | ---: | --- | --- | --- |
| Entry 172 is the birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.70 | medium | medium | hold for row-control QA |
| Entry 172 is the Burgos/de la Cruz row for `Jose Miguel`. | 0.10 | high | high | revise or reject after QA if image reread is certified |
| `Jose del Carmen Pulgar S.` is the father as transcribed in the chunk. | 0.62 | medium | high | hold; father suffix needs QA |
| `Juana Arriagada de Pulgar` is the mother in the Pulgar row. | 0.72 | medium | medium | hold for row-control QA |
| Entry 172 supports any Dario/Darío/Pulgar-Smith identity bridge. | 0.02 | high | high | unsupported; do not promote |

## Next Action

Run targeted conversion QA for page 58, entry 172, comparing the source image, assigned converted Markdown, assigned chunk, and source packet. The QA note should certify the controlling row and explicitly decide whether the father field is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any claim, relationship, identity merge, or canonical wiki update.
