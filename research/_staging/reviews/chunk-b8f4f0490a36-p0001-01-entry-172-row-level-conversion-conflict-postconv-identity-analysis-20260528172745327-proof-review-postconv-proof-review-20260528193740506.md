---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528193740506
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528172745327.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528172745327.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528170150642.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528170150642.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote from the current converted Markdown entry-172 text. It gives `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`, while the assigned chunk, source packet, QA note, and visible page image support a different physical row for entry `172`.
2. Do not promote the father-name suffix after `Pulgar`. The chunk reads `Jose del Carmen Pulgar S.`, but the source packet and targeted QA note bound the promotable father reading to `Jose del Carmen Pulgar`; the page image does not make the trailing mark sufficiently clear for this review.
3. Do not use this entry for a Dario-line same-person merge or relationship bridge. The reviewed source names no `Dario`, `Arturo`, `Smith`, `Dario Jose`, or later-life identifier.
4. Do not merge `Juana Arriagada de Pulgar` with any separate Juana candidate from this evidence alone. This source supports only the source-named mother in entry `172`.
5. The staged draft's references to existing canonical pages were not independently checked in this proof-review scope. They should not be treated as proof support unless a separate review reads those pages.

## Evidence Strengths

- The assigned chunk transcribes physical entry `172` on register page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`, with parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- The source packet and targeted conversion-review note both identify the same physical row as the Pulgar/Arriagada birth registration and explicitly flag the Burgos/de la Cruz text as a derivative conversion conflict.
- Direct page-image inspection supports the row-control conclusion: the middle row on page 58 is entry `172` and visibly corresponds to a Pulgar/Arriagada birth registration, not the Burgos/de la Cruz family shown in the current converted Markdown.
- The staged identity analysis correctly keeps the conversion conflict separate from identity proof and correctly rejects use of this source as a Dario identity bridge.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 8/10 for physical row-control and child/mother reading; 6/10 for full literal detail; 4/10 for the uncertified father suffix after `Pulgar`; 2/10 for the conflicting current converted Markdown entry-172 text |
| evidence_quantity_score | 4/10 |
| agreement_score | 8/10 among the assigned chunk, source packet, targeted QA note, and page image for the Pulgar/Arriagada row; 2/10 when including the current converted Markdown |
| identity_confidence_score | 8/10 for the source-named child `Jose del Carmen Segundo Pulgar Arriagada`; 7.5/10 for the source-named father bounded as `Jose del Carmen Pulgar`; 8/10 for the source-named mother `Juana Arriagada de Pulgar`; 1/10 for any Dario-line identity bridge |
| claim_probability | 0.90 that physical entry `172` is the Pulgar/Arriagada birth row; 0.86 that `Jose del Carmen Segundo Pulgar Arriagada` is the recorded child; 0.82 that `Jose del Carmen Pulgar` is the recorded father; 0.86 that `Juana Arriagada de Pulgar` is the recorded mother; 0.02 for a Burgos/de la Cruz duplicate-person interpretation; 0.03 for any Dario-line identity claim |
| relevance_level | high for the Pulgar/Arriagada parent-child cluster; low for Dario-line identity bridging |
| relevance_confidence | 0.88 for Pulgar/Arriagada relevance; 0.10 for Dario-line relevance |
| canonical_readiness | hold |

## Review Finding

The staged identity analysis is supported as a conflict/hold note. The evidence supports a narrow image-controlled conclusion that physical entry `172` on register page 58 is the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`, with father bounded to `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`.

The broader conversion state is not ready for canonical promotion because the current converted Markdown still assigns entry `172` to an unrelated Burgos/de la Cruz family. That conflict is material, not a spelling variant. The source also provides no literal support for Dario-name expansion, a same-person merge, or a kinship bridge beyond the named child and named parents in this row.

## Next Action

Keep this item on hold for canonical use until downstream handling explicitly accepts the row-control QA and preserves the converted Markdown conflict. If advanced later, promote only bounded row facts and draft parent-child candidates for the source-named Pulgar/Arriagada people; keep father suffix expansion, Dario identity bridges, and Juana duplicate-person questions unresolved.
