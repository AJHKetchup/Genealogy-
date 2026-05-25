---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260525211125251
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525203741061.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525203741061.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
conflict_type: row_level_conversion_conflict
canonical_readiness: not_ready
---

# Identity Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The staged draft and staged source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the assigned converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- This is a row-level conflict between incompatible family clusters, not a name-variant issue.
- The father field in the Pulgar/Arriagada reading still needs field-level QA: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Existing canonical pages already contain low/probable generated evidence for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` from this chunk family. Do not treat those generated snippets as promotion-ready until the controlling row is certified.
- Entry 172 does not literally name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Darío J. Pulgar Arriagada, or Darío Pulgar Arriagada. Any Dario-line comparison is an anti-conflation check only.

## Literal Evidence Boundary

The assigned chunk transcribes entry 172 on page 58 as a birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at Calle de Valdivia. The same row gives father `Jose del Carmen Pulgar S.`, Chilean, employee, resident Calle de Colipi, and mother `Juana Arriagada de Pulgar`, Chilean, resident Calle de Colipi.

The staged source packet repeats that Pulgar/Arriagada reading and states that direct image inspection during extraction supported the Pulgar/Arriagada row on register page 58, entry 172. It also preserves the father-suffix uncertainty.

The assigned converted Markdown instead transcribes entry 172 as `Jose Miguel`, male, born 6 April 1888, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, with no Pulgar or Arriagada names in that entry.

## Hypotheses

| Rank | Hypothesis | Supporting evidence | Conflicts and limits | Claim probability |
| ---: | --- | --- | --- | ---: |
| 1 | The controlling entry 172 row is the Pulgar/Arriagada birth for `Jose del Carmen Segundo Pulgar Arriagada`. | Assigned chunk and staged source packet agree; staged packet says image context supports the Pulgar/Arriagada row. Existing canonical stubs for the child and Juana reflect this same chunk family, though not promotion-ready. | Assigned converted Markdown gives a different entry 172 family. Father suffix remains unresolved. | 0.72 |
| 2 | The controlling entry 172 row is the Burgos/de la Cruz birth for `Jose Miguel`. | Assigned converted Markdown gives a complete Burgos/de la Cruz row. | Assigned chunk and staged image-reviewed packet contradict it; no Pulgar/Arriagada bridge exists if this row controls. | 0.22 |
| 3 | Both rows are real register rows but one derivative has been assigned to the wrong row/page/image boundary. | The two transcripts are internally coherent but mutually incompatible; this pattern fits row/file-assignment drift. | Requires targeted conversion QA against the source image and job artifacts; identity analysis cannot resolve it alone. | 0.60 |
| 4 | `Jose del Carmen Pulgar S.` is the same person as canonical/stub `Jose del Carmen Pulgar`. | Same name core appears in the staged row and an existing canonical stub. | The suffix `S.` is unresolved; the existing stub has separate evidence involving Tulio Cesar Luis Jose and does not itself prove this 1888 father is the same person. | 0.48 |
| 5 | `Juana Arriagada de Pulgar` in entry 172 is the same person as canonical/stub `Juana Arriagada de Pulgar`. | Exact name match and existing generated evidence point to the same entry-172 child-mother relationship. | The underlying row conflict blocks canonical readiness. This does not resolve whether other Juana variants, including Juana de Dios/Amagada/Amador candidates in other staged context, are the same person. | 0.62 |
| 6 | Entry 172 provides a lineage bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Darío J. Pulgar Arriagada, or Darío Pulgar Arriagada. | Pulgar surname is present if the Pulgar/Arriagada row controls; existing local context contains several Dario/Pulgar candidates. | Entry 172 names no Dario, Arturo, Smith, Dario Jose, Darío J., or Darío Pulgar. Name overlap is insufficient for a bridge. | 0.05 |

## Conflict Assessment

- Same-person conflict: unresolved for `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar`; severity moderate because a parent identity could be duplicated or wrongly merged.
- Duplicate-person conflict: moderate for `Juana Arriagada de Pulgar` if generated canonical evidence is treated as accepted before QA; low for Dario-line people because entry 172 does not name them.
- Name-variant conflict: father suffix `S.` is unresolved; `Jose Miguel` versus `Jose del Carmen Segundo Pulgar Arriagada` is not a variant.
- Relationship conflict: high. The two readings assign different parents to different children in the same entry number.
- Chronology conflict: high for the child event because the Pulgar/Arriagada row gives birth 8 March 1888 while the converted Burgos/de la Cruz row gives birth 6 April 1888.

## Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | The Pulgar/Arriagada identity is better supported by the chunk and staged image-reviewed packet, but the assigned converted Markdown directly conflicts. |
| conflict_severity | 0.92 | Different child, parents, dates, and family cluster under the same entry number. |
| evidence_quality | 0.74 | Civil birth registration evidence would be strong if the row controlled; current evidence is derivative plus staged image-review statement, pending targeted QA. |
| conversion_confidence | 0.30 | The assigned converted Markdown and assigned chunk disagree at row level. |
| claim_probability | 0.72 | Best narrow claim is that the Pulgar/Arriagada row probably controls, but not enough for promotion. |
| relevance | 0.88 | Highly relevant to Pulgar/Arriagada identity sorting and parent-child relationships. |
| canonical_readiness | 0.10 | Not ready; all dependent claims and relationships should remain held. |

## Dario-Line Anti-Conflation Ranking

| Candidate | Ranking for this entry | Reason |
| --- | ---: | --- |
| Dario Arturo Pulgar-Smith | 5 | Existing canonical family-supplied person; entry 172 has no Dario/Arturo/Smith or grandchild evidence. |
| Dario Arturo Pulgar | 5 | Existing CV/document-level candidate elsewhere; entry 172 has no Dario Arturo wording. |
| Dario Jose Pulgar-Arriagada / Darío J. Pulgar Arriagada | 4 | Arriagada surname appears only if the Pulgar/Arriagada row controls, but the child is `Jose del Carmen Segundo`, not Dario Jose or Darío J. |
| Darío Pulgar Arriagada / Dario Pulgar Arriagada | 4 | Existing canonical stub has a 2000 expropriation event; entry 172 is an 1888 birth row and gives no direct same-person bridge. |
| Jose/Juana parent candidates | 1 | These are the only local identity candidates directly relevant to entry 172, but they remain blocked by row QA and father-field QA. |

## Recommended Next Action

Keep the staged conflict at `hold_for_conversion_qa`. The exact next proof-review/promotion step is targeted conversion QA against the source image, assigned converted Markdown, assigned chunk, and staged source packet to certify the controlling row for entry 172 and the father-name field. After that QA, rerun proof review before promoting any child identity, parent relationship, same-person merge, or Dario-line bridge. Do not merge `Jose del Carmen Pulgar S.` into `Jose del Carmen Pulgar`, do not merge Juana variants, and do not attach this entry to any Dario candidate from name overlap alone.
