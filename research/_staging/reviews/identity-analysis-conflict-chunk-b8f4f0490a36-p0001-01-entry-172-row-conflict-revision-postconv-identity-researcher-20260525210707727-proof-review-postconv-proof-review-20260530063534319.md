---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530063534319
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210707727.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210707727.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Assignment Conflict

## Blockers First

1. The referenced source image is not available at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, and the manifest page image is not available at `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png`. I could not visually certify the controlling row or the father field.
2. The assigned chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
3. The converted file and page-level conversion Markdown read entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
4. This is a row-control or conversion-control conflict, not a spelling variant. No child identity, parent-child relationship, residence, informant, parent merge, or Dario-line bridge should be promoted from this draft.
5. The visible-source boundary must remain intact: the review may ask conversion QA to double-check whether the row is Pulgar/Arriagada, but it cannot change the reading to Pulgar/Arriagada or Burgos/de la Cruz without a source image or certified QA note.

## Evidence Strengths

- The staged draft accurately identifies the material conflict between the chunk/source-packet reading and the converted Markdown reading.
- The source packet explicitly preserves the conflicting derivative readings and recommends `hold_for_conversion_qa`.
- Both derivative readings agree that the document is a civil birth register for Los Angeles, Chile, with entry 172 dated 7 April 1888, which gives useful context once row control is resolved.
- Under the Pulgar/Arriagada derivative reading, the child, father, mother, birth details, residence, and informant are internally coherent within the chunk. This is useful as a QA target, but not sufficient for canonical use while the source image is unavailable and the converted file disagrees.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 6/10 for the described civil birth register as a source class; 2/10 for this review because the actual source image is unavailable in the workspace |
| conversion_confidence_score | 2/10 overall due to contradictory derivative conversions and missing image verification |
| evidence_quantity_score | 3/10: one intended civil birth entry, but no independent corroborating source and no available image check |
| agreement_score | 2/10: chunk/source packet agree with each other, converted/page Markdown agree with each other, but the two derivative groups materially disagree |
| identity_confidence_score | 2/10 for any canonical child or parent identity from this draft; 1/10 for any Dario-line connection |
| claim_probability | 0.55 that there is a real entry-172 row-control problem requiring QA; 0.45 for the Pulgar/Arriagada row as the controlling entry; 0.35 for the Burgos/de la Cruz row as the controlling entry; 0.05 or lower for any Dario identity or relationship bridge |
| relevance_level | high for Pulgar/Arriagada research if the chunk is certified; low for Dario-line claims until a separate bridge source exists |
| relevance_confidence | 0.80 for the row-conflict relevance; 0.20 for Dario-line relevance |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is supported as a hold. The proof review cannot certify the literal entry because the referenced source image is missing and the derivative transcriptions contradict each other at the row level. The safest scored judgment is to preserve the conflict, block all dependent claims, and require targeted conversion QA.

The Pulgar/Arriagada reading may be family-relevant, but it is not yet proof-ready. The Burgos/de la Cruz reading may be the actual converted row, but it is not enough to override the chunk without image-level QA. Neither reading supports a relationship to any Dario, Arturo, Smith, Dario Jose, or Dario Pulgar Arriagada identity.

## Next Action

Run targeted conversion QA for page 58, entry 172 using the actual source/page image. The QA note should identify the controlling row and certify the father field only to the extent visible: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical claim, relationship, identity merge, parent merge, wiki update, or Dario-line comparison.
