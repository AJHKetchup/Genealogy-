---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260530104409513
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530092229282.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530092229282.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530072501797.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530072501797.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
page_reference: "page 1; register page 58; physical row entry 172"
decision: hold
canonical_readiness: not_ready
source_quality_score: 0.82
conversion_confidence_score: 0.48
evidence_quantity_score: 0.62
agreement_score: 0.36
identity_confidence_score: 0.60
claim_probability: 0.86
relevance_level: direct
relevance_confidence: 0.97
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

This review covers the exact staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530092229282.md`.

## Blockers First

- Canonical readiness blocker: keep this staged draft at `hold`; it is not ready for promotion, merge, relationship attachment, or wiki work.
- Full-page image blocker: the referenced original source PNG and conversion-job page image are absent in this checkout, so I cannot independently certify the physical row alignment from the full page.
- Conversion conflict blocker: the referenced chunk records entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, while the referenced converted Markdown/page Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Source-path blocker: the source packet's unaccented `raw/sources/...Circunscripcion de Los Angeles...png` path and the manifest/chunk accented `raw/sources/...Circunscripción de Los Ángeles...png` path are both missing.
- Relationship/identity blocker: this draft does not supply direct evidence for any Dario/Dario/Dario Arturo/Dario Jose identity bridge. Surname-context leads must not be promoted.
- Father-name blocker: the available crop support is enough to keep `Jose del Carmen Pulgar` as a local reading lead, but not enough to certify the trailing `S.` or a normalized father identity.

## Evidence Strengths

- The staged identity analysis accurately frames the issue as a row-control/conversion conflict, not as a name variant or same-person conflict between the Pulgar/Arriagada and Burgos/de la Cruz readings.
- The referenced chunk directly supports the Pulgar/Arriagada row text for entry `172`: child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, registration date 7 April 1888, birth 8 March 1888 at 3 p.m. at `Calle de Valdivia`, father field `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The referenced converted Markdown directly supports the conflicting Burgos/de la Cruz derivative reading for entry `172`: child `Jose Miguel`, birth 6 April 1888 at 10 p.m., father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and place `En esta`.
- The two staged crop assets under `research/_staging/conversion-review-assets/` are present and visibly support the Pulgar/Arriagada parent/informant field area at crop level, including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`
- Civil birth registration is a strong source class for a birth row when the row is certified, but the present review has only derivative text plus crops, not the full source image.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil registration is high-quality, but the full-page source image is unavailable here. |
| conversion_confidence_score | 0.48 | Chunk and crop evidence favor Pulgar/Arriagada locally, while the converted Markdown materially disagrees. |
| evidence_quantity_score | 0.62 | One chunk, one converted Markdown file, one source packet, one QA note, manifest context, and two crop assets were available. |
| agreement_score | 0.36 | Agreement is good among the staged packet, QA note, chunk, and crops, but poor against the current converted Markdown. |
| identity_confidence_score | 0.60 | Moderate for a local Pulgar/Arriagada row hypothesis; very low for any wider Dario-line identity bridge. |
| claim_probability | 0.86 | High probability that the staged draft correctly identifies a real derivative row-control conflict requiring hold. |
| Pulgar row controls entry 172 probability | 0.70 | Leading local hypothesis from chunk and crops, still below promotion threshold without full-page row-control proof. |
| Burgos/de la Cruz row controls entry 172 probability | 0.20 | Supported by the converted Markdown, but contradicted by the chunk and staged crop-supported packet. |
| same-person/name-variant probability | 0.01 | Different child, parent set, birth date/time, and place; entry-number overlap alone is not identity evidence. |
| relevance_level | direct | The staged draft directly reviews the assigned row-control conflict. |
| relevance_confidence | 0.97 | All bounded evidence concerns the same entry number and conversion conflict. |
| canonical_readiness | not_ready | Hold for conversion QA and row-control certification. |

## Review Decision

Decision: `hold`.

The staged draft is literally supported as a conflict analysis: it correctly preserves the contradiction between the assigned chunk/crop-supported Pulgar-Arriagada reading and the current converted Burgos-de la Cruz reading. It should not be revised into a promoted claim because full-page original-image row control is unavailable in this checkout.

The draft's caution around Dario-line candidates is also supported. No bounded source text names Dario, Arturo, Smith, Dario Jose, an adult identity bridge, a spouse, a descendant, or a later-life connection.

## Next Action

Perform targeted full-page original-image row-control review when the source image or page image is available. That review should decide which physical row controls entry `172` and should separately decide whether the father field is only `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Until then, do not promote claims, relationships, identity merges, Dario-line attachments, or canonical wiki updates from this staged draft.
