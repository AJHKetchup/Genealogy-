---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527195959302
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211540757.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211540757.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
page_image_checked: unavailable
canonical_readiness: hold
---

# Proof Review: Entry 172 Row Conflict Revision

## Blockers First

1. Canonical readiness is `hold`. The staged draft correctly treats this as a row-level conversion conflict and does not support promotion of a child identity, birth fact, parent-child relationship, same-person merge, or Dario-line bridge.
2. The referenced source image path and the manifest page image path were unavailable in this workspace at review time. I could verify the derivative disagreement, but I could not resolve the controlling row from the visible source image.
3. The current converted Markdown file hash is `F768A72BF3B3547A9873D543306165F2622776665CA3DEBBDD6842524E8566D4`, which does not match the `converted_sha256` values recorded in the staged source packet or chunk metadata. This increases version-control risk for relying on any single derivative transcription.
4. The assigned chunk and source packet identify entry 172 as a Pulgar/Arriagada birth row, while the current converted Markdown identifies entry 172 as a Burgos/de la Cruz row. These are incompatible record readings, not name variants.
5. No reviewed artifact names `Dario`, `Darío`, `Arturo`, `Smith`, `Dario Jose`, or `Pulgar-Smith`. Any Dario-line identity or relationship use remains unsupported by this staged draft.

## Evidence Strengths

- The staged draft accurately quotes the assigned chunk/source-packet reading: entry 172, registered 7 April 1888, child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, birth on 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- The staged draft accurately quotes the conflicting converted Markdown reading: entry 172, registered 7 April 1888, child `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth on 6 April 1888 at 10 p.m. in `En esta`.
- The staged conflict candidate and source packet agree that all dependent claims should remain on `hold_for_conversion_qa`.
- The staged analysis is appropriately cautious about the father-name uncertainty and does not force `Jose del Carmen Pulgar S.` into a canonical person identity.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 6/10 for a civil birth register as a source class; 3/10 for this review because the source/page image was unavailable for direct visual verification |
| conversion_confidence_score | 2/10 for controlling entry-172 text; derivative transcripts directly conflict and the current converted file hash differs from staged metadata |
| evidence_quantity_score | 4/10; there are multiple derivative artifacts, but no available page image and only one disputed record event |
| agreement_score | 2/10 for the row content; 9/10 for the procedural conclusion that the conflict blocks promotion |
| identity_confidence_score | 2/10 for any promoted Pulgar/Arriagada identity claim from this row before QA; 0.5/10 for any Dario-line bridge |
| claim_probability | 0.95 that `hold_for_conversion_qa` is the correct disposition; 0.35 that the Pulgar/Arriagada row can be used as stated before image-based QA; 0.02 for a direct Dario identity bridge |
| relevance_level | high for Pulgar/Arriagada triage if the Pulgar row is confirmed; low for Dario-line proof at this stage |
| relevance_confidence | 0.85 for the hold/triage relevance; 0.20 for Dario-line relevance |
| canonical_readiness | hold |

## Review Finding

The staged draft is supported as a proof-control warning. It accurately represents the central conflict between the assigned chunk/source packet and the current converted Markdown, and its recommendation to keep the matter on `hold_for_conversion_qa` is justified.

The review cannot certify the Pulgar/Arriagada row, the Burgos/de la Cruz row, or the father suffix from the source image because the referenced image files were not available. The hash drift on the current converted Markdown is an additional reason to require targeted conversion QA before any canonical use.

## Next Action

Keep this staged draft on hold. Targeted conversion QA should restore or locate the page image with SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, reconcile the converted Markdown and chunk versions, decide the controlling row for entry 172, and certify the father field only to the extent visible. After that, rerun proof review before any canonical claim, relationship, same-person analysis, or Dario-line comparison is promoted.
