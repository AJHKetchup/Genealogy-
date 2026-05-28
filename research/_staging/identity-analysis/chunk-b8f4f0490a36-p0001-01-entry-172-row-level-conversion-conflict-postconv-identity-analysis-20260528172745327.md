---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260528172745327
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260528170150642.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260528170150642.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528170150642.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528170150642.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
canonical_readiness: hold_for_proof_review
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. The current converted Markdown and the assigned chunk do not describe the same entry 172. The converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; the assigned chunk, source packet, and targeted row-control QA record physical row entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
2. The father-name suffix is not promotion-ready. The chunk reads `Jose del Carmen Pulgar S.`, but the 20260528170150642 source packet and conversion-review note explicitly bound the certified father reading to `Jose del Carmen Pulgar`.
3. This source does not name Dario, Arturo, Smith, Dario Jose, or Dario/Dario Pulgar Arriagada. It cannot bridge the entry-172 child or parents to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, the adult passenger `Dario Pulgar`, or the child passenger `Dario Pulgar`.
4. Existing canonical pages already contain low-confidence/probable entry-172 evidence for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`. Do not use this staged conflict note to overwrite canonical pages or raise confidence; a proof-review acceptance step is still required.
5. `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` remain separate parent candidates in the current wiki context. This entry supports only the source-named `Juana Arriagada de Pulgar`; it does not prove that she is the same person as `Juana de Dios Amagada de Pulgar`.

## Literal Source Readings Kept Separate

The assigned chunk literal row for page 58, entry `172`, reads the child as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`, with father field `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.

The targeted conversion-review note for this task reports direct source-image review and narrows the image-controlled father reading to `Jose del Carmen Pulgar`. It also records the mother as `Juana Arriagada de Pulgar`, the parents' residence as `Calle de Colipi`, and informant `Ernesto Herrera L.`.

The current converted Markdown literal derivative text for entry `172` instead gives `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and a 6 April 1888 birth. That text must be preserved as a conversion conflict, not normalized into the Pulgar/Arriagada row.

## Hypotheses And Scores

| Rank | Hypothesis | Supporting evidence | Conflicts and limits | Identity confidence | Claim probability | Canonical readiness |
| ---: | --- | --- | --- | ---: | ---: | --- |
| 1 | Physical row entry `172` is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | Assigned chunk, source packet, and targeted row-control QA all support the Pulgar/Arriagada row for physical entry `172`. | Current converted Markdown gives a different Burgos/de la Cruz family for entry `172`; proof review must accept row-control QA before promotion. | 0.88 | 0.90 | hold_for_proof_review |
| 2 | `Jose del Carmen Pulgar` is the source-named father of the child in the image-controlled row. | Source packet and conversion-review note certify father only as `Jose del Carmen Pulgar`; chunk contains same base name. | The trailing `S.` in the chunk is not certified and must not be promoted from this task. | 0.78 | 0.82 | hold_for_proof_review |
| 3 | `Juana Arriagada de Pulgar` is the source-named mother of the child in the image-controlled row. | Chunk, source packet, and conversion-review note consistently name `Juana Arriagada de Pulgar`. Existing canonical page has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`. | No proof here that she is identical with `Juana de Dios Amagada de Pulgar`; spelling/name similarity is not enough. | 0.84 | 0.86 | hold_for_proof_review |
| 4 | The Burgos/de la Cruz entry-172 text and the Pulgar/Arriagada row are duplicate-person or name-variant evidence for the same child. | Only shared feature is the entry number in conflicting derivative layers. | Names, parents, birth date, and row identity disagree materially. Treat as conversion conflict, not duplicate identity. | 0.01 | 0.02 | reject_for_identity_merge |
| 5 | Entry 172 is direct evidence for `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. | Pulgar/Arriagada surname context may justify later family-line comparison. | The entry names no Dario candidate and gives no chronology bridge to the 1918, 1929, 1953, 1959, 2000, or family-supplied Dario clusters. | 0.02 | 0.03 | not_ready |

## Dario-Line Comparison

- `Dario Arturo Pulgar-Smith`: Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns not to merge similarly named source clusters without identity review. Entry 172 provides no `Dario Arturo`, no `Smith`, and no relationship to Alexander John Heinz.
- `Dario Arturo Pulgar`: Staged CV evidence elsewhere is document-level occupational evidence for a CV subject, with repeated notes requiring identity-bridge review before linking to `Dario Arturo Pulgar-Smith`. Entry 172 does not name that CV subject.
- `Dario Jose Pulgar-Arriagada`: Staged Geneva/medical-title evidence elsewhere names Dario Jose or Dario J. Pulgar Arriagada in 1918/1929 contexts. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, born in 1888, and does not supply a Dario name or a later identity bridge.
- `Dario/Dario Pulgar Arriagada`: The canonical `Darío Pulgar Arriagada` page currently has a 2000 expropriation event, while passenger pages carry separate 1953 adult/child `Dario Pulgar` clusters. Entry 172 does not resolve whether any of those are the same person as each other or as a family-supplied Pulgar-Smith person.
- Jose/Juana parent candidates: This entry supports source-named parents `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` for the entry-172 child only. It does not prove that `Jose del Carmen Pulgar` is the same father candidate appearing in other staged/canonical relationships, and it does not merge `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar`.

## Conflict Assessment

- Conflict severity: 0.92, high. The conversion conflict changes the whole family group, not a spelling detail.
- Evidence quality: 0.80. The assigned chunk and image-reviewed row-control note agree, but the derivative converted Markdown remains materially inconsistent.
- Conversion confidence: 0.78 overall; 0.90 for row-control after targeted image review; 0.55 for the exact father suffix after `Pulgar`.
- Relationship-conflict risk: 0.86 if parent-child links are promoted before proof review accepts the row-control and father-boundary notes.
- Chronology-conflict risk: 0.70 for any attempted Dario bridge, because this is an 1888 birth entry with no later-life identifiers.
- Relevance: 0.88 to the Pulgar/Arriagada parent-child cluster; 0.10 to Dario-line identity bridging.

## Recommended Next Action

Run proof review on this identity analysis together with the exact staged draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260528170150642.md`, the 20260528170150642 source packet, and the targeted row-control QA note. If proof review accepts the conflict analysis, the promotion step should promote only bounded row-control facts and parent-child candidates for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`, while preserving the Burgos/de la Cruz text as a derivative conversion conflict and leaving all Dario and Juana duplicate-person questions unresolved.
