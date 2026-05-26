---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526044010734
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526015109623.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526015109623.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: blocked
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Row-control blocker: the staged draft's central hold recommendation is supported. The assigned chunk and source packet read entry 172 as a Pulgar/Arriagada birth row, while the referenced converted Markdown reads entry 172 as a different Burgos/de la Cruz row. This prevents canonical promotion from the converted file family until targeted conversion QA reconciles the row.
- Father-field blocker: the source packet and staged draft correctly preserve uncertainty around the father field after `Jose del Carmen Pulgar`. The chunk transcribes `Jose del Carmen Pulgar S.`, but the review should not treat that suffix as certified from the visible source without targeted QA.
- Relationship blocker: the conditional parent-child claim for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.`, and `Juana Arriagada de Pulgar` is plausible but remains dependent on row-control QA and father-field certification.
- Identity-bridge blocker: the staged draft is correct that this evidence does not support a same-person, ancestor, parent, child, or bridge claim to any Dario/Dario Arturo/Dario Jose/Dario J./Darío Pulgar identity.

## Evidence Checked

- Staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526015109623.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted file: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source page image visibly supports the assigned chunk/source packet at row level: entry 172 on page 58 is a Pulgar/Arriagada row, not the Burgos/de la Cruz row currently present in the converted Markdown.
- The assigned chunk gives a coherent civil birth registration for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, sex male, birth date 8 March 1888, place Calle de Valdivia, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The source type is a civil birth register, which is a strong source class for birth identity and parent-child relationships once transcription control is resolved.
- The staged draft appropriately treats the Dario-line possibilities as anti-conflation/research-context cautions, not as supported identity claims.

## Scored Judgment

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth registration image is a strong original/near-original source for birth and parent fields. |
| conversion_confidence_score | 0.38 | The assigned chunk matches the visible row better than the converted Markdown, but the conversion family is internally inconsistent and the father suffix is not certified. |
| evidence_quantity_score | 0.62 | One source image plus two derivative readings are available; no independent corroborating records were reviewed for identity bridge or parent merges. |
| agreement_score | 0.52 | Chunk, source packet, and image agree on Pulgar/Arriagada row control, but the current converted Markdown materially disagrees. |
| identity_confidence_score | 0.68 | The child and mother identities are probable for the visible entry 172 row; father-name precision remains lower due to suffix uncertainty. |
| claim_probability | 0.70 | Probable that entry 172 is the Pulgar/Arriagada birth row; only conditional support for parent-child claims until QA. |
| relevance_level | 0.92 | Directly relevant to Pulgar/Arriagada research and to preventing false Dario-line merges. |
| relevance_confidence | 0.88 | The surname and row content make the relevance clear, while broader Dario relevance remains only contextual. |
| canonical_readiness | 0.10 | Blocked; do not promote until row-control QA and father-field certification are complete. |

## Claim-Level Review

| Claim | Review result | Probability | Canonical readiness |
| --- | --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada row in the source image. | Supported as probable by image, chunk, and source packet; contradicted by converted Markdown. | 0.78 | blocked |
| Current converted Markdown entry 172 is Burgos/de la Cruz. | Literally present in the converted file, but likely a row/image mismatch for this source packet. | 0.20 | blocked |
| Child is `Jose del Carmen Segundo Pulgar Arriagada`. | Supported by chunk, source packet, and visible image review at a practical level, but should await QA because canonical conversion control conflicts. | 0.74 | hold |
| Father is `Jose del Carmen Pulgar S.`. | Supported by the chunk transcription, but suffix is uncertain in source packet/image review. | 0.56 | hold |
| Mother is `Juana Arriagada de Pulgar`. | Supported by chunk/source packet and visually plausible in the row. | 0.72 | hold |
| Entry 172 proves a Dario-line bridge. | Not supported by this source or staged draft. | 0.04 | blocked |

## Next Action

Keep the staged draft's recommendation: `hold_for_conversion_qa`. The next action is targeted conversion QA comparing the source image, converted Markdown, assigned chunk, and source packet for entry 172, with explicit certification of the row control and the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review for any child identity, parent-child relationship, parent merge, or Dario-line comparison.
