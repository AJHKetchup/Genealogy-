---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530015802989
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526134239386.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526134239386.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526095657171.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-evidence-extraction-20260526095657171.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Conversion Conflict

## Blockers First

1. Do not promote any child identity, birth fact, parent-child relationship, parent merge, or Dario-line bridge from this staged draft. The referenced converted Markdown and referenced chunk disagree on the entire entry-172 row.
2. The source image path recorded by the manifest and staging files was not available in this workspace checkout, and the rendered page image path under the conversion job was also absent. This review could not independently certify the visible handwriting.
3. The current converted Markdown and conversion job page Markdown identify entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. The chunk and source packet identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` with a disputed trailing mark, mother `Juana Arriagada de Pulgar`, born 8 March 1888.
4. The father field remains unresolved. The chunk reads `Jose del Carmen Pulgar S.`, while the source packet certifies only `Jose del Carmen Pulgar` and explicitly leaves the final mark unresolved.
5. No reviewed source text in this task names any Dario person or states a relationship to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada.

## Evidence Strengths

- The staged identity analysis accurately preserves the row-level conflict instead of treating it as a spelling or identity variant.
- The source packet and conflict draft both record prior image review supporting the Pulgar/Arriagada row, while still recommending `hold_for_conversion_qa`.
- The assigned chunk gives a detailed Pulgar/Arriagada transcription for entry 172, including child, sex, birth date/time, birth place, father, mother, informant, and residence fields.
- The converted file gives a detailed but incompatible Burgos/de la Cruz transcription for entry 172, confirming that the blocker is material and not limited to one field.
- The staged draft's anti-conflation treatment of Dario-line identities is supported: this evidence set contains no direct Dario naming or lineage bridge.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for the civil birth-register source type in principle; 5/10 usable in this review because the source/page image was unavailable locally |
| conversion_confidence_score | 3/10 overall; 6/10 for the chunk/source-packet Pulgar reading as a staged lead; 2/10 for the converted-file Burgos reading as controlling evidence |
| evidence_quantity_score | 4/10 |
| agreement_score | 3/10 overall because the main derivatives disagree; 7/10 between chunk, source packet, and conflict draft for the Pulgar/Arriagada lead |
| identity_confidence_score | 7/10 that the staged issue is a real conversion-row conflict; 5/10 for the Pulgar/Arriagada identity facts pending image QA; 1/10 for any Dario bridge |
| claim_probability | 0.90 that the staged draft should remain a hold-for-QA conflict note; 0.65 that entry 172 is the Pulgar/Arriagada row pending direct image QA; 0.10 that the Burgos/de la Cruz row should control this family-relevant claim set; 0.01 for a Dario identity bridge |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged identity analysis is supported as a proof-review hold. It correctly identifies a derivative row conflict and correctly blocks promotion of dependent identities, relationships, parent merges, and Dario-line connections.

The Pulgar/Arriagada reading has meaningful local support from the chunk, source packet, and prior image-review note, but this reviewer could not inspect the source image or page image because both referenced image paths were unavailable. The converted Markdown remains materially contradictory, so the claim probability is not high enough for canonical use.

The Burgos/de la Cruz reading is relevant only as the competing derivative transcript unless targeted conversion QA proves that it is the correct row or that the chunk/source packet are attached to the wrong image/version.

## Next Action

Keep this staged draft and all dependent claims at `hold_for_conversion_qa`.

Run targeted conversion QA against the original page image or regenerated page image, the current converted Markdown, the current chunk, and the source packet. QA should explicitly decide the controlling entry-172 row and certify whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before any claim or relationship promotion. Do not attach this evidence to any Dario canonical page without a separate reviewed source that directly supports the identity or lineage bridge.
