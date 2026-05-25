---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525194809618
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525122915316.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525122915316.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115123585.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers First

1. Canonical readiness is `hold`. The staged draft correctly treats entry 172 as blocked by a material row-level conversion/file-assignment conflict.
2. The staged draft's literal description of the converted Markdown side is not supported by the current converted file reviewed for this task. The staged draft says the converted Markdown records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`; the current converted file records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
3. The conflict remains material even with that correction. The current chunk and source packet identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at Calle de Valdivia.
4. The father-name ending after `Jose del Carmen Pulgar` is not proof-ready. It must remain one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until targeted conversion QA certifies the visible reading.
5. No Dario-line identity or relationship jump is supported by this entry. The reviewed entry does not name Dario, Arturo, Smith, Dario Jose, or any later Dario identity cluster.

## Evidence Strengths

- The source packet and current chunk are internally coherent for the Pulgar/Arriagada row at entry 172.
- Visual inspection of the source image supports the presence of a Pulgar/Arriagada family cluster in row 172 on page 58.
- The staged draft correctly rejects canonical promotion, parent merge, Dario bridging, and silent normalization of `Juana Arriagada de Pulgar` into other Juana-name variants.
- The draft's anti-conflation reasoning is appropriate: surname overlap alone does not connect this birth registration to any Dario candidate.

## Scoring

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is a strong source type, and the page image is available for row-level inspection. |
| conversion_confidence_score | 0.42 | The image-backed chunk/source packet and the current converted Markdown disagree on entry 172's child-parent cluster. |
| evidence_quantity_score | 0.55 | There is one primary page image plus derivative chunk/packet/conversion text, but no independent corroborating record for the identity claims. |
| agreement_score | 0.38 | Chunk and source packet agree with each other; converted Markdown disagrees materially; staged draft also misstates the current converted-file reading. |
| identity_confidence_score | 0.70 for the Pulgar/Arriagada entry-172 row; 0.03 for any Dario bridge | Pulgar/Arriagada is probable from the chunk and image, but unresolved conversion conflict prevents proof-ready identity use; no Dario appears. |
| claim_probability | 0.68 for "entry 172 is the Pulgar/Arriagada birth registration"; 0.94 for "canonical action should hold"; 0.03 for Dario-line linkage | The hold decision is strongly supported. The positive Pulgar claim remains probable but not promotable. |
| relevance_level | high | The staged draft directly concerns entry 172 and the Pulgar/Arriagada conversion conflict. |
| relevance_confidence | 0.98 | All reviewed materials reference the same chunk id, source image, page 58, and entry 172 conflict context. |
| canonical_readiness | hold | Requires targeted conversion QA before any claim, relationship, identity merge, or canonical page update. |

## Claim-Level Judgment

The staged draft is acceptable as a hold-level conflict analysis, but it should be treated as requiring revision or QA annotation before reuse because its exact description of the converted Markdown conflict is stale or unsupported by the current converted file. The controlling conclusion remains valid: no child identity, birth fact, parent relationship, parent-identity merge, Juana variant merge, or Dario bridge should be promoted from this draft.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, current chunk, source packet, conflict draft, and converted Markdown. The QA note should identify the controlling entry-172 row, explain why the current converted file gives `Jose Miguel` / `Oswaldo Burgos` / `Concepcion de la Cruz` while the chunk/source packet give the Pulgar/Arriagada row, and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Rerun proof review after QA before any canonical promotion.
