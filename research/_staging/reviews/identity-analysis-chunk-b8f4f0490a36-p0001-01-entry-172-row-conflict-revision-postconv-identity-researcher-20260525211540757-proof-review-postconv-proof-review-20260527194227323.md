---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527194227323
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211540757.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211540757.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row Conflict Revision

## Blockers First

1. Do not promote child, birth, parent, residence, informant, same-person, or relationship claims from this staged draft. The derivative evidence is in direct row-level conflict for entry 172.
2. The cited source image path is not available in the workspace, and the conversion job's `page-images/page-0001.png` cache is also absent. This proof review could not verify either row against the visible source.
3. The assigned chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
4. The converted Markdown and conversion job page Markdown read entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. at `En esta`.
5. These are not name variants or ordinary uncertainty. They are incompatible row readings. The controlling entry-172 row and the Pulgar father field must be resolved by targeted conversion QA from the source image before canonical use.
6. No reviewed material in this task supports a direct Dario/Darío Pulgar identity bridge, a Pulgar-Smith bridge, or any parent-child relationship beyond the disputed row text.

## Evidence Strengths

- The staged draft correctly identifies the central conflict between the assigned chunk/source packet and the current converted Markdown.
- The source packet explicitly flags low conversion confidence and recommends `hold_for_conversion_qa`.
- The chunk and source packet are internally consistent for the Pulgar/Arriagada reading.
- The converted Markdown and conversion job page Markdown are internally consistent for the Burgos/de la Cruz reading.
- The record type, if the image is later verified, is a civil birth registration and would normally be strong direct evidence for a birth event and named parents.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 6/10 for the cited civil-registration source metadata; not higher because the source image was unavailable for this review |
| conversion_confidence_score | 2/10 overall because two derivative conversion streams give incompatible entry-172 rows |
| evidence_quantity_score | 3/10 for the identity claim; multiple derivative files were checked, but they are not independent visible-source confirmations |
| agreement_score | 2/10 overall; 8/10 within the Pulgar derivative pair, 8/10 within the Burgos derivative pair, but direct conflict between the pairs |
| identity_confidence_score | 3/10 for `Jose del Carmen Segundo Pulgar Arriagada` as the entry-172 child until image QA; 3/10 for `José Miguel` as the entry-172 child until image QA; 0.5/10 for any Dario-line identity bridge |
| claim_probability | 0.95 that a row-level conversion conflict exists; 0.40 that the Pulgar/Arriagada row controls; 0.45 that the Burgos/de la Cruz row controls; 0.05 or lower for Dario-line identity/relationship claims from this item |
| relevance_level | high for resolving a possible Pulgar/Arriagada birth registration; low for Dario-line proof unless separate bridge evidence is supplied |
| relevance_confidence | 0.85 for the conflict-review relevance; 0.20 for direct Dario-line relevance |
| canonical_readiness | hold; not ready for canonical claims, relationships, or wiki updates |

## Review Finding

The staged draft is supported as a hold, not as proof of either child identity. Its strongest claim is procedural: entry 172 has an unresolved conversion conflict requiring source-image QA. The review should not prefer the Pulgar/Arriagada row over the Burgos/de la Cruz row, or the reverse, without visual verification.

The Pulgar father reading must remain bounded to the derivative transcription: `Jose del Carmen Pulgar S.` or an explicitly uncertain alternative after QA. It should not be silently normalized to a canonical `Jose del Carmen Pulgar`.

## Next Action

Run targeted conversion QA using the actual source image or regenerated page image. The QA note should identify which row is visible for entry 172 and certify the father field only to the level supported by the image. After that, rerun proof review before any claim promotion, relationship creation, same-person merge, or Dario-line comparison.
