---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260530015327868
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526134239386.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526134239386.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526095657171.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_image_available: false
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.78
conversion_confidence_score: 0.24
evidence_quantity_score: 0.44
agreement_score: 0.22
identity_confidence_score: 0.40
claim_probability: 0.52
relevance_level: high
relevance_confidence: 0.88
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`. The staged draft identifies a real row-level derivative conflict, but the referenced source image is not present at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, and the manifest page image `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png` is also unavailable.
- The referenced converted Markdown and referenced chunk cannot both be literal transcriptions of the same physical entry `172`. The converted Markdown gives a Burgos/de la Cruz row; the chunk gives a Pulgar/Arriagada row.
- The father field in the Pulgar/Arriagada reading remains uncertified from visible source review in this proof step. Preserve the source-packet boundary: `Jose del Carmen Pulgar` is certified there only to that extent, with any final `S.` or mark unresolved.
- The staged draft's references to existing canonical pages and broader Jose/Juana/Dario comparison context were not re-verified in this review because they are outside the allowed verification set for this task. They should remain anti-conflation context only, not proof support.
- No Dario identity, relationship, or lineage bridge is supported by the reviewed staged draft, source packet, chunk, or converted Markdown.

## Evidence Strengths

- The staged draft's central conflict finding is supported by the referenced files: this is a material identity-controlling conflict, not a spelling variant.
- The referenced chunk and source packet agree on a Pulgar/Arriagada reading for entry `172`: child `Jose del Carmen Segundo Pulgar Arriagada`, male, born `Ocho de Marzo de mil ochocientos ochenta i ocho` at `Calle de Valdivia`, father read in the chunk as `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The referenced converted Markdown consistently gives a different entry `172`: child `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril de mil ochocientos ochenta i ocho` at `En esta`, with `Oswaldo Burgos` as compareciente.
- The source class is strong if the image is recovered and verified: a civil birth registration can directly support child identity, birth details, parent names, and informant context.
- The staged draft correctly recommends holding dependent identity, relationship, merge, and Dario-line conclusions until targeted conversion QA resolves row control.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil birth registration is a high-quality source class, but the source image was unavailable for this review. |
| conversion_confidence_score | 0.24 | Chunk/source packet agree with each other, but the assigned converted Markdown materially disagrees on identity-controlling fields. |
| evidence_quantity_score | 0.44 | There are three local derivatives to compare, but no available page image to arbitrate the conflict. |
| agreement_score | 0.22 | Agreement exists within the chunk/source-packet pair; agreement fails between those files and the converted Markdown. |
| identity_confidence_score | 0.40 | The Pulgar/Arriagada identity cluster is internally coherent in derivative evidence, but row control and father suffix are unresolved. |
| claim_probability | 0.52 | The Pulgar/Arriagada row may be the correct controlling row, but proof cannot rise above tentative without source-image QA. |
| relevance_level | high | The conflict directly affects whether this source can support Pulgar/Arriagada child and parent claims. |
| relevance_confidence | 0.88 | The reviewed files directly concern the assigned staged draft and its promotion risk. |
| canonical_readiness | hold_for_conversion_qa | Do not promote any child identity, birth fact, parent relationship, parent merge, or Dario comparison from this draft until QA resolves the row-level conflict. |

## Review Decision

Hold. The staged draft is broadly supported as a conflict analysis, but it is not canonical-ready and should not be used as proof for any promoted identity or relationship claim. Treat the Burgos/de la Cruz reading as a competing derivative artifact and the Pulgar/Arriagada reading as a plausible but still QA-blocked row.

## Next Action

Recover or regenerate the original page image for SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, then run targeted visual conversion QA for register page `58`, entry `172`. The QA note should decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz and, if Pulgar/Arriagada controls, certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an explicitly uncertain reading.
