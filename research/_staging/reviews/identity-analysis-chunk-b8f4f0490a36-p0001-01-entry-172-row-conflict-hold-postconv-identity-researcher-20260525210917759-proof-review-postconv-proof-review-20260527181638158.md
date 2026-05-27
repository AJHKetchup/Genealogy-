---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527181638158
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525210917759.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525210917759.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_control_and_narrow_claim_review
---

# Proof Review: Entry 172 Row Conflict Hold

## Blockers First

1. Do not promote identity, parent-child relationship, parent merge, or Dario-line bridge claims from this staged identity analysis. The assigned converted Markdown and assigned chunk still disagree at the whole-row level for entry `172`.
2. The current converted Markdown reads entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`; the assigned chunk and source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
3. I could not directly open the named source image from `raw/sources/...Entry No. 172;.png` in this workspace. A prior targeted row-control QA note reports image review supporting the Pulgar/Arriagada row and father `Jose del Carmen Pulgar`, but this proof review should not upgrade the father suffix `S.` to canonical fact.
4. The staged draft correctly blocks any bridge to `Dario`, `Arturo`, `Smith`, `Dario Jose`, or `Darío/Dario Pulgar Arriagada`; none of the checked derivative text names those persons.
5. Canonical readiness remains `hold_for_conversion_control_and_narrow_claim_review` until the conflicting converted Markdown is superseded/corrected or a downstream workflow explicitly accepts the prior image-reviewed QA note as controlling.

## Evidence Strengths

- The staged draft accurately reports the material conflict between the converted file and chunk/source packet.
- The source packet and assigned chunk agree on a Pulgar/Arriagada entry `172` with registration date `Siete de Abril de mil ochocientos ochenta i ocho`, child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The civil birth register is a strong source type for birth event, parent names, date, and place when the row transcription is controlled.
- The prior targeted row-control QA note `research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260527151911781.md` reports image-reviewed support for the Pulgar/Arriagada physical row and limits the father reading to `Jose del Carmen Pulgar`.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for a civil birth registration as a source type; 6/10 for this review because the source image path was unavailable for direct inspection |
| conversion_confidence_score | 5/10 overall because the converted file and chunk conflict; 7/10 only if the prior image-reviewed row-control QA note is accepted as controlling |
| evidence_quantity_score | 4/10: one directly relevant birth-register row plus derivative QA context |
| agreement_score | 4/10 across all derivatives; 8/10 between source packet, chunk, and prior row-control QA note for the Pulgar/Arriagada reading |
| identity_confidence_score | 6.5/10 for the narrow Pulgar/Arriagada child identity if the QA note is accepted; 2/10 or lower for any broader Dario-line identity bridge |
| claim_probability | 0.82 for the narrow claim that entry `172` is the Pulgar/Arriagada birth row if the prior image-reviewed QA note is controlling; 0.20 for the Burgos/de la Cruz reading under the current converted Markdown alone; 0.25 for promoting father suffix `Pulgar S.`; 0.02 for a Dario-line bridge |
| relevance_level | high for Pulgar/Arriagada research; low for Dario-line linkage |
| relevance_confidence | 0.85 for Pulgar/Arriagada relevance; 0.20 for Dario-line relevance |
| canonical_readiness | hold_for_conversion_control_and_narrow_claim_review |

## Review Finding

The staged identity analysis is supported as a hold. It is not promotion-ready because the assigned derivative materials still contain an unresolved row-level contradiction. The prior image-reviewed QA note is useful verification context and supports preferring the Pulgar/Arriagada row over the Burgos/de la Cruz row, but this review does not independently inspect the source image and does not certify the father suffix after `Pulgar`.

The only potentially supportable downstream claims are narrow entry-172 facts for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`, and only after the row-control QA note is accepted by the claim workflow or the conflicting converted Markdown is corrected/superseded. No checked text supports a same-person merge or relationship jump to Dario/Arturo/Smith identities.

## Next Action

Keep this staged identity analysis on hold. Next, either make the source image available for direct proof review or use the existing image-reviewed row-control QA note to stage revised, narrow claims that explicitly avoid `Pulgar S.` unless separately certified. Rerun proof review before any canonical wiki, claim, relationship, or merge update.
