---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530093019479
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013245826.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013245826.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_image_present: false
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.62
conversion_confidence_score: 0.45
evidence_quantity_score: 0.56
agreement_score: 0.38
identity_confidence_score: 0.64
claim_probability: 0.66
relevance_level: direct
relevance_confidence: 0.96
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013245826.md`.
- The referenced original source image path was not present on disk during this review, so I could not independently certify the physical row, child-name field, or father suffix from the image.
- The assigned chunk and source packet identify entry `172` as a Pulgar/Arriagada birth row, while the current converted Markdown identifies entry `172` as a Burgos/de la Cruz birth row. This remains a material row-control conflict.
- The staged draft's strongest conclusion, that the Pulgar/Arriagada row is the better hypothesis, is plausible from the chunk and source packet but is not canonical-ready without image-backed row-control QA.
- The father field must remain bounded. The chunk reads `Jose del Carmen Pulgar S.`, but the staged draft itself says the suffix/mark is unresolved; this review cannot promote `S.` as a settled literal reading.
- No child identity, parent-child relationship, parent merge, Juana-name merge, or Dario-line bridge should be promoted from this draft.

## Evidence Strengths

- The staged draft accurately flags a real derivative conflict: the chunk/source packet and the converted file provide incompatible families, child names, birth details, and informants for entry `172`.
- The chunk is internally coherent for a Pulgar/Arriagada row: `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, birth on 8 March 1888 at 3 p.m. at Calle de Valdivia, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The source packet repeats the Pulgar/Arriagada row and explicitly treats the Burgos/de la Cruz converted-file text as a row-level conversion conflict.
- The converted file is explicit and internally coherent for a competing Burgos/de la Cruz row: child `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at about 10 p.m.
- The staged draft correctly avoids using this entry as a Dario identity bridge; no reviewed text names Dario, Arturo, Smith, or a later-life identity connector.

## Scored Judgment

| metric | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.62 | A civil birth register would be strong direct evidence, but the original image was unavailable to this reviewer and the review depends on conflicting derivatives. |
| conversion_confidence_score | 0.45 | The assigned chunk and source packet agree with each other, but the current converted Markdown materially disagrees for the same entry number. |
| evidence_quantity_score | 0.56 | There are multiple local derivative witnesses, but only one assigned chunk/source packet set supports the Pulgar/Arriagada row and the image could not be checked. |
| agreement_score | 0.38 | Agreement is high inside the Pulgar/Arriagada derivative set and low across the full reviewed record set because the converted file gives a different row. |
| identity_confidence_score | 0.64 | The Pulgar/Arriagada child identity is plausible if the chunk controls, but the row-control conflict and missing image prevent higher confidence. |
| claim_probability | 0.66 | Probability favors the staged draft's hold analysis over the converted-file reading, but not enough for canonical action. |
| relevance_level | direct | The evidence directly concerns the assigned staged identity/conflict analysis for entry `172`. |
| relevance_confidence | 0.96 | All reviewed files are tied to the same chunk id, source packet, converted file, and staged draft. |
| canonical_readiness | hold_for_conversion_qa | Keep staged only; do not promote to canonical folders. |

## Claim Review

- Entry `172` is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`: hold. Probability `0.66`; canonical_readiness `hold_for_conversion_qa`.
- Entry `172` is the Burgos/de la Cruz birth row for `José Miguel`: hold as a competing derivative reading. Probability `0.28`; canonical_readiness `hold_for_conversion_qa`.
- `Jose del Carmen Pulgar S.` is the settled literal father-name form: hold/revise. Probability `0.45` for a suffix being present from derivative text only; canonical_readiness `not_ready`.
- `Juana Arriagada de Pulgar` is the mother in the Pulgar/Arriagada row: hold pending row control. Probability `0.64`; canonical_readiness `hold_for_conversion_qa`.
- This source bridges any Dario Pulgar identity cluster: reject for promotion. Probability `0.02`; canonical_readiness `not_ready`.

## Identity And Relationship Risk

- Identity risk is high if Pulgar/Arriagada and Burgos/de la Cruz readings are treated as the same record without source-image row control.
- Relationship risk is high if parent-child claims are promoted before resolving whether the controlling row is the chunk row or the converted-file row.
- Name-variant risk remains for `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]`.
- The staged draft's broader Jose/Juana and Juana-name comparisons are useful cautions, but this entry alone does not prove merges or variant identities.

## Next Action

Keep this staged identity analysis at `hold_for_conversion_qa`. Restore or locate the original source image for source SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, then perform targeted row-control QA for page 58, entry `172`, including the child-name field, parent fields, informant field, and the mark or suffix after `Jose del Carmen Pulgar`. Rerun proof review before any canonical claim, relationship, identity merge, Dario-line attachment, or wiki update.
