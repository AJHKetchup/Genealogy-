---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527195324397
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211124639.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211124639.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
page_markdown: "raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-markdown/page-0001.md"
source_image_status: "missing at referenced source and page-image paths"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row Conflict

## Blockers First

1. Do not promote any child identity, birth-event, parent-name, residence, informant, parent-child relationship, parent merge, or Dario-line bridge from this staged draft. The derivative evidence disagrees at the row level for entry 172.
2. The source image recorded in the staged materials was not available at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, and the conversion-job page image was not available at `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png`. Because the visible source could not be checked, the review cannot certify either row as controlling.
3. The assigned chunk and source packet identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`. The converted file and page-markdown identify entry 172 as `José Miguel`, with father `Oswaldo Burgos` and mother `Concepcion de la Cruz`. This is not a spelling variant.
4. The father field for the Pulgar hypothesis remains uncertified. It must not be normalized to `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until targeted conversion QA checks the visible source.
5. The checked materials do not literally name Dario, Darío, Arturo, Smith, Dario Jose, or any Dario/Darío Pulgar Arriagada variant. Shared Pulgar/Arriagada surname context is not sufficient for an identity or relationship bridge.

## Evidence Strengths

- The staged identity analysis accurately preserves the row conflict rather than treating it as a promoted claim.
- The conflict draft and source packet both explicitly warn that all dependent claims are blocked pending targeted conversion QA.
- The assigned chunk is internally coherent for a Pulgar/Arriagada row on page 58, entry 172, including child, parents, birth date/place, residences, and informant.
- The converted file and page-markdown are internally coherent for a different Burgos/de la Cruz row on page 58, entry 172.
- The staged draft correctly treats the possible Jose/Juana parent candidates and all Dario-line comparisons as unresolved.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for a civil birth register as a source type; 3/10 for this review because the source image/page image was unavailable for visual verification |
| conversion_confidence_score | 2/10 overall due to direct contradiction between assigned chunk/source packet and converted file/page-markdown |
| evidence_quantity_score | 3/10; there are multiple derivative witnesses, but they appear to depend on the same unavailable source image and disagree on the core row |
| agreement_score | 2/10 overall; 8/10 within the Pulgar derivative pair and 8/10 within the Burgos derivative pair, but 0/10 between the two row readings |
| identity_confidence_score | 0.35 for `Jose del Carmen Segundo Pulgar Arriagada` as the entry-172 child; 0.15 for `José Miguel` as the entry-172 child; 0.05 or lower for any Dario/Darío Pulgar bridge |
| claim_probability | 0.50 that the staged draft's hold recommendation is correct; 0.35 for the Pulgar/Arriagada row as controlling; 0.15 for the Burgos/de la Cruz row as controlling; 0.02 for a direct Dario-line claim |
| relevance_level | high for Pulgar/Arriagada research triage; low for direct Dario/Darío identity proof |
| relevance_confidence | 0.90 for relevance as a row-conflict blocker; 0.25 for relevance to any Dario-line bridge |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is supported as a hold/QA item. It should not be revised into a promoted identity or relationship claim because the controlling source row cannot be certified from the materials available in this review.

The literal support is split: the chunk/source packet support a Pulgar/Arriagada reading, while the converted file/page-markdown support a Burgos/de la Cruz reading. Without the missing source or page image, proof review cannot choose between them, cannot certify the Pulgar father field, and cannot attach this entry to any canonical person or family.

## Next Action

Run targeted conversion QA for page 58, entry 172 using the actual source image or restored page image. The QA note should decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz and should certify the Pulgar father field only to the extent visible. After that, rerun proof review before any canonical claim, relationship, identity merge, parent merge, or Dario-line comparison is promoted.
