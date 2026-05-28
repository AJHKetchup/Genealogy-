---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528202044475
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173924316.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173924316.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528165422297.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528165422297.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
canonical_readiness: hold_identity_merges_accept_row_control
---

# Proof Review: Entry 172 Row-Level Conversion Conflict Identity Analysis

## Blockers First

1. The converted Markdown is materially inconsistent with the image, chunk, source packet, and targeted QA note. It records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; the image-controlled row and assigned chunk support entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
2. The father-name suffix remains bounded. The chunk reads `Jose del Carmen Pulgar S.`, but the targeted QA certifies only `Jose del Carmen Pulgar`; this review does not promote the trailing `S.`.
3. The staged identity analysis includes same-person and Dario-line hypotheses that are not directly supported by this birth row. No merge, bridge, or attachment to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada` is ready from this evidence.
4. Relationship evidence is source-level only. The row supports that the child was recorded with named father and mother fields, but it does not independently prove same-person identity for existing canonical parent stubs or resolve Juana name variants.
5. Canonical readiness is limited to proof-reviewed row-control acceptance. No canonical claim, relationship, identity merge, or wiki page update should occur from this review note alone.

## Verification Context

- Staged draft reviewed: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173924316.md`.
- Source packet reviewed: `research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528165422297.md`.
- Conversion QA note reviewed: `research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528165422297.md`.
- Assigned chunk reviewed: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Conflicting converted Markdown reviewed: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Page image visually checked: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Scored Judgment

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong direct source for the row-level event; image quality is usable but not ideal for every terminal mark. |
| conversion_confidence_score | 0.82 | Row-control QA and chunk agree on the Pulgar/Arriagada row; the converted Markdown is unreliable for this entry and the father suffix remains uncertain. |
| evidence_quantity_score | 0.74 | One direct source image, one assigned chunk, one source packet, and one targeted QA note support the narrow row-control finding. |
| agreement_score | 0.78 | Image, chunk, packet, and QA agree on the main row identity; converted Markdown conflicts completely. |
| identity_confidence_score | 0.84 | High confidence for the recorded child name and named parent fields in physical row `172`; lower for any same-person merge beyond the row. |
| claim_probability | 0.86 | The staged draft's central claim that physical row `172` is the Pulgar/Arriagada birth row is strongly supported. |
| relevance_level | high | Directly relevant to the staged identity-analysis conflict and Pulgar/Arriagada row-control question. |
| relevance_confidence | 0.96 | The reviewed evidence is the exact source set referenced by the staged draft. |
| canonical_readiness | hold_identity_merges_accept_row_control | Accept the row-control conclusion for downstream proof work; hold merges, Dario bridges, and father suffix promotion. |

## Evidence Strengths

- The page image shows the middle entry on page 58 numbered `172`; the visible row corresponds to the Pulgar/Arriagada entry summarized in the targeted QA note.
- The assigned chunk transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The conversion QA note independently bounds the father field to `Jose del Carmen Pulgar` and warns that the terminal mark after `Pulgar` is not certified.
- The converted Markdown's Burgos/de la Cruz entry has different child, parents, birth date, place language, and declarant context, so it should be treated as a derivative conversion conflict rather than a name variant or duplicate-person hypothesis.
- The staged draft correctly warns against Dario-line attachment from this row alone; no visible source text names Dario, Arturo, Smith, Alexander John Heinz, or a later-life identifier.

## Review Decision

The staged identity analysis is accepted only as a proof-reviewed row-level conflict analysis. The best-supported conclusion is that physical row `172` on register page 58 is the birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, with named parent fields `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`. The current converted Markdown is not reliable for entry `172` and must remain flagged as a derivative conversion conflict.

The staged draft is not ready for canonical identity merges, parent-stub merges, Juana variant normalization, father suffix promotion, or Dario-line attachment. Those require separate proof review using direct bridge evidence.

## Next Action

Hold for scoped downstream proof work. Use the image-controlled row and targeted QA as the controlling evidence for entry `172`; preserve the Burgos/de la Cruz transcript as a conversion conflict; promote no canonical facts until a separate promotion task accepts the row-level evidence and keeps identity bridges explicitly bounded.
