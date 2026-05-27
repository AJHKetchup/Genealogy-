---
type: identity_conflict_analysis
status: draft
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-postconv-evidence-extraction-20260527221218880.md"
worker: "postconv-identity-analysis-20260527223141315"
role: identity_researcher
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-postconv-evidence-extraction-20260527221218880.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-rowcert-postconv-evidence-extraction-20260527221218880.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
page_reference: "page 1; register page 58; physical row entry 172"
canonical_readiness: hold_for_proof_review
---

# Identity And Conflict Analysis: Entry 172 Derivative Row Conflict

This note analyzes the exact staged conflict draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-postconv-evidence-extraction-20260527221218880.md`.

## Blockers First

1. Row control is not promotion-ready. The staged conflict draft and source packet say the original image/assigned chunk control physical row `172` as a Pulgar/Arriagada birth registration, while the current converted Markdown labels entry `172` as a Burgos/de la Cruz registration.
2. The father field must remain bounded to `Jose del Carmen Pulgar` for promotion review. The assigned chunk contains `Jose del Carmen Pulgar S.`, but the staged packet and image-reread notes do not certify the terminal `S.` or mark.
3. Existing canonical pages already contain low-confidence/probable Pulgar/Arriagada evidence generated from this row. Do not expand or strengthen those pages until row-control proof review accepts the controlling reading.
4. No evidence in this staged draft directly names or bridges `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`. Those names are Pulgar-line comparison points only.
5. The named `$genealogy-proof-review` skill was not available in this session's skill list, so this note applies the local evidence-contract constraints from the task prompt and uses only staged drafts, referenced converted/chunk/source files, reviewed notes, and existing wiki pages.

## Literal Source Readings

- Assigned chunk reading: entry `172`; registration `Siete de Abril de mil ochocientos ochenta i ocho`; child `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; born `Ocho de Marzo de mil ochocientos ochenta i ocho`, 3 p.m., `Calle de Valdivia`; father line `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- Staged source-packet/image-control reading: physical row `172` on register page 58 is the Pulgar/Arriagada row, not the Burgos/de la Cruz row; father certified only as `Jose del Carmen Pulgar`.
- Current converted Markdown reading: entry `172`; child `José Miguel`; born 6 April 1888 at 10 p.m.; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.

## Hypotheses And Scores

| Rank | Hypothesis | Supporting Evidence | Conflicting Evidence / Limits | Identity Confidence | Conflict Severity | Evidence Quality | Conversion Confidence | Claim Probability | Relevance | Canonical Readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Physical row `172` is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | The assigned chunk, source packet, and image-reviewed row-control statement all identify row `172` as Pulgar/Arriagada. Existing wiki pages for the child and `Juana Arriagada de Pulgar` already preserve probable/low-confidence evidence from this packet. | Current converted Markdown assigns entry `172` to an unrelated Burgos/de la Cruz row; father suffix remains unresolved. | 0.91 | 0.88 | 0.86 | 0.90 for row-control packet; 0.58 overall while derivative conversion conflicts | 0.90 | 0.99 | hold_for_proof_review |
| 2 | Current converted Markdown's Burgos/de la Cruz row controls entry `172`. | The converted Markdown explicitly labels `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, as entry `172`. | It conflicts with the assigned chunk and staged image-reviewed row-control packet. The names, dates, parents, domicile, and informant are a separate identity cluster, not variants of the Pulgar/Arriagada row. | 0.10 | 0.88 | 0.36 | 0.20 | 0.08 | 0.95 | blocked_for_canonical_use |
| 3 | The entry-172 father `Jose del Carmen Pulgar` is the same person as the existing wiki `Jose del Carmen Pulgar` parent candidate. | Same literal father name appears in the staged row, and the wiki has a `Jose del Carmen Pulgar` page with a draft child-parent link to `Tulio Cesar Luis Jose`. | This draft gives no independent spouse, age, signature, or cross-record bridge proving the same man across child records. The terminal `S.` is not proof-ready. | 0.54 | 0.52 | 0.68 | 0.70 | 0.50 | 0.88 | not_ready |
| 4 | The entry-172 mother `Juana Arriagada de Pulgar` is the same person as existing `Juana Arriagada de Pulgar`. | The literal mother reading matches the canonical page display name, and the wiki already has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`. | Confidence on the canonical page is low/probable and depends on the same row-control issue. | 0.74 | 0.46 | 0.74 | 0.76 | 0.72 | 0.95 | hold_for_proof_review |
| 5 | `Juana Arriagada de Pulgar` is a variant/duplicate of `Juana de Dios Amagada de Pulgar`. | Both are Pulgar-line Juana parent candidates in existing wiki context. | The literal names differ: `Arriagada` vs `Amagada`, and entry 172 does not state `de Dios` or a connection to `Tulio Cesar Luis Jose`. Do not merge by spouse/family context alone. | 0.26 | 0.62 | 0.55 | 0.70 for entry-172 mother name only | 0.22 | 0.82 | not_ready |
| 6 | Entry 172 bridges to Dario-line identities. | Broad Pulgar/Arriagada surname context makes the row relevant to later Pulgar-line review. | This staged draft does not name Dario or Smith and contains no chronology, parentage, occupation, or relationship bridge to Dario candidates. | 0.03 | 0.68 | 0.42 | 0.55 | 0.02 | 0.70 | blocked_for_identity_merge |

## Pulgar-Line Anti-Conflation Comparison

| Candidate | Assessment From This Draft | Required Next Step |
| --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather. Entry 172 does not name him and does not prove a relationship to `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar`. Same-person probability with the 1888 child: 0.01. | Separate reviewed bridge from family-supplied `Dario Arturo Pulgar-Smith` to a source-bearing `Dario Arturo Pulgar` or Pulgar/Arriagada family record. |
| `Dario Arturo Pulgar` | Existing staged CV context may support a document-level `Dario Arturo Pulgar`, but entry 172 supplies no `Dario Arturo` name or CV/occupation continuity. Same-person probability with any entry-172 person: 0.02. | Identity-bearing CV/front-matter proof review plus a separate lineage bridge before connecting to this 1888 birth row. |
| `Dario Jose Pulgar-Arriagada` | Existing staged portrait/photo contexts name `Dario Jose Pulgar-Arriagada`, but entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. Same-person probability from this draft alone: 0.03. | Source-control and identity-bridge proof review for the Dario Jose material before comparing to Pulgar/Arriagada birth-register families. |
| `Dario/Darío Pulgar Arriagada` | Existing wiki/staged context has a separate `Darío Pulgar Arriagada` page and mentions in non-entry-172 sources. Entry 172 does not identify him. Same-person probability with the 1888 child: 0.02. | Compare dates, occupations, property/medical contexts, and parentage in a dedicated Dario Pulgar Arriagada proof review. |
| `Jose del Carmen Pulgar` | Literal father candidate if H1 controls; plausible overlap with existing wiki parent stub but not proven across all Jose parent records. | After row-control proof review, run focused Jose parent review across entry 172 and the Tulio Cesar Luis Jose parent evidence, comparing residence, occupation, spouse/mother forms, dates, and source quality. |
| `Juana Arriagada de Pulgar` | Literal mother candidate if H1 controls; current canonical page already carries a probable child link from this entry cluster. | If row-control proof review accepts H1, promote only the literal mother reading with source boundary intact. |
| `Juana de Dios Amagada de Pulgar` and other Juana parent candidates | Separate candidate cluster in existing wiki context; not proven same as `Juana Arriagada de Pulgar`. | Run targeted Juana-variant proof review; keep `Arriagada`, `Amagada`, and `de Dios` as separate readings until a reviewed source reconciles them. |

## Conflicts

- Same-person conflict: unresolved for `Jose del Carmen Pulgar` across parent contexts; unresolved and weaker for Juana variants.
- Duplicate-person conflict: low between the Pulgar/Arriagada child and any Dario candidate; moderate risk if `Jose del Carmen Pulgar` or Juana candidates are merged by name/family context alone.
- Name-variant conflict: `Jose del Carmen Pulgar` vs uncertified `Jose del Carmen Pulgar S.`; `Juana Arriagada de Pulgar` vs `Juana de Dios Amagada de Pulgar`.
- Relationship conflict: high. The converted Burgos/de la Cruz child-parent set conflicts with the image-reviewed Pulgar/Arriagada child-parent set for the same entry number.
- Chronology conflict: high for row identity. Pulgar/Arriagada row has birth 8 March 1888 and registration 7 April 1888; Burgos/de la Cruz row has birth 6 April 1888 and registration 7 April 1888.
- Canonical collision: existing canonical stubs contain evidence derived from entry 172; they should remain low-confidence/probable until row-control proof review resolves the derivative conflict.

## Recommended Next Action

Exact next proof-review step: run targeted row-control proof review for register page 58, physical row `172`, comparing the original source image, assigned chunk, source packet, current converted Markdown, and any conversion-review note. Decide whether entry `172` is controlled by the Pulgar/Arriagada row or the Burgos/de la Cruz row, then either reconcile/supersede the converted Markdown or mark it as a non-controlling derivative. If H1 is accepted, promote only bounded claims: child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, and father `Jose del Carmen Pulgar` without the terminal suffix unless the image is explicitly certified.
