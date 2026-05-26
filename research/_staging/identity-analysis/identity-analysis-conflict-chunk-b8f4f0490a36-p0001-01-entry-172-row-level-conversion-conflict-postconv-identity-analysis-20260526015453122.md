---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526015453122
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
analysis_status: hold
canonical_readiness: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Do not promote child identity, birth facts, parent-child relationships, parent merges, duplicate-person merges, name-variant conclusions, or Dario-line comparisons from the staged conflict draft.
- The controlling blocker is a row-level conversion conflict: the assigned chunk and source packet describe entry 172 as a Pulgar/Arriagada row, while the current converted Markdown describes entry 172 as a Burgos/de la Cruz row.
- The father's exact name ending in the Pulgar/Arriagada row remains unresolved. Hold the father field as one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until targeted conversion QA certifies the visible source reading.
- The entry does not name `Dario`, `Arturo`, `Smith`, `Dario Jose`, or `Dario Pulgar Arriagada`. Any Dario-line relevance is family-context only and cannot bridge identities.
- Existing canonical pages already contain provisional or family-supplied Pulgar-line context, including `Dario Arturo Pulgar-Smith`, `Darío Pulgar Arriagada`, `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`. This analysis does not alter those pages and does not resolve those identities.

## Literal Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Reviewed proof note: `research/_staging/reviews/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-proof-review-postconv-proof-review-20260526015110115.md`.
- Canonical context pages read only: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/juana-de-dios-amagada-de-pulgar.md`, `wiki/people/birth-registration-entry-172-for-jose-del-carmen-segundo-pulgar-arriagada.md`, and `wiki/relationships/dario-arturo-pulgar-smith-maternal-grandfather-of-alexander-john-heinz.md`.

## Hypotheses And Evidence

### Hypothesis 1: Entry 172 is the Pulgar/Arriagada birth row

The assigned chunk transcribes page 58, entry 172 as child `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`. The source packet says image review supports a Pulgar/Arriagada row and says the father field visibly begins `Jose del Carmen Pulgar`.

This hypothesis is strongest for the broad row identity, but not ready for canonical use because the converted Markdown for the same file/entry does not match it. It also cannot establish any Dario identity or later Pulgar-line relationship.

Probability: 0.72. Identity confidence: 0.66. Evidence quality: 0.82. Conversion confidence: 0.38. Relevance: 0.90. Canonical readiness: 0.10, hold for conversion QA.

### Hypothesis 2: Entry 172 is the Burgos/de la Cruz birth row in the converted Markdown

The current converted Markdown transcribes entry 172 as child `Jose Miguel`, male, born 6 April 1888 at about 10 p.m. at `En esta`, with father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.

This hypothesis is supported by the current conversion output only. It conflicts materially with the assigned chunk and source packet on child name, parents, birth date, birth place, and informant. It is not a name variant of the Pulgar/Arriagada row.

Probability: 0.28 as the controlling row for this assigned source packet. Identity confidence: 0.25. Evidence quality: 0.45. Conversion confidence: 0.38 because the conversion layer is internally disputed. Relevance: 0.05 to the Pulgar line. Canonical readiness: 0.05, hold.

### Hypothesis 3: The Pulgar/Arriagada child is a duplicate or name variant of a Dario Pulgar candidate

No reviewed entry-172 evidence names Dario. The child in the chunk is `Jose del Carmen Segundo Pulgar Arriagada`; the Dario canonical/context pages involve `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, and `Dario/Darío Pulgar Arriagada` clusters from other staged records and family-supplied context.

The exact surname overlap justifies later comparison after conversion QA, but it does not support a merge, duplicate-person conclusion, or name-variant conclusion. `Jose del Carmen Segundo` and `Dario Arturo` / `Dario Jose` are not interchangeable on this evidence.

Probability: 0.04. Identity confidence: 0.08. Evidence quality for this bridge: 0.10. Conversion confidence: 0.38. Relevance: 0.25 as a future Pulgar-line double-check only. Canonical readiness: 0.00.

### Hypothesis 4: Jose del Carmen Pulgar in entry 172 is the same father candidate as other Jose del Carmen Pulgar context

The entry-172 chunk/source packet identify a father beginning `Jose del Carmen Pulgar`, possibly with suffix `S.`. The canonical `Jose del Carmen Pulgar` page currently has a draft child link to `Tulio Cesar Luis Jose` from a separate entry, and another review note for entry 513 names father `Jose del Carmen Pulgar` and mother `Juana de Dios Amagada de Pulgar` with unresolved surname reading.

This is a plausible same-name parent-candidate cluster, but the entry-172 row conflict and the uncertain father suffix block a same-person merge. The different mother names, `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar`, require separate proof review rather than silent correction.

Probability: 0.42. Identity confidence: 0.35. Evidence quality: 0.50. Conversion confidence: 0.38. Relevance: 0.80. Canonical readiness: 0.10.

### Hypothesis 5: Juana Arriagada de Pulgar is the same person as another Juana parent candidate

Entry 172's chunk/source packet name the mother as `Juana Arriagada de Pulgar`. Existing canonical context also has `Juana de Dios Amagada de Pulgar` as a separate page tied to a different draft child relationship. The names are similar enough to justify a future side-by-side review, especially because `Arriagada` and `Amagada` may be conversion-sensitive readings.

This analysis does not merge them. On current evidence, `Juana Arriagada de Pulgar` remains the entry-172 mother candidate and `Juana de Dios Amagada de Pulgar` remains a separate candidate from another record.

Probability: 0.30. Identity confidence: 0.25. Evidence quality: 0.45. Conversion confidence: 0.38. Relevance: 0.80. Canonical readiness: 0.05.

## Dario-Line Comparison Required By Task

Ranked from most to least supported by this specific staged conflict draft:

1. No Dario bridge from entry 172: strongest conclusion. The entry-172 evidence does not identify `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.
2. Future family-context relevance only: if conversion QA certifies the Pulgar/Arriagada row, the resulting Jose/Juana parent cluster may become context for later Pulgar-line proof review.
3. Same-person or duplicate-person Dario hypothesis: unsupported. No merge or name-variant conclusion should be made from this entry.

Exact next proof-review step needed: after targeted conversion QA certifies the controlling row and father-name reading, rerun proof review on the entry-172 child identity, parent-child relationships, Jose/Juana parent candidates, and only then open a separate Dario-line bridge review if another identity-bearing source connects these parents or child to a Dario candidate.

## Conflict Summary

| Conflict | Severity | Analysis |
| --- | ---: | --- |
| Pulgar/Arriagada row versus Burgos/de la Cruz converted row | 0.92 | Direct contradiction across child, parents, birth date, place, and informant for the same entry number. |
| Father field `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` versus uncertain ending | 0.55 | Affects parent identity and later same-person comparison; does not change the broad Pulgar row hypothesis. |
| `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar` parent candidates | 0.50 | Similar names in Pulgar context, but from separate evidence; hold as separate candidates. |
| Entry-172 Pulgar child versus Dario-name clusters | 0.20 | No direct contradiction; the issue is lack of bridge evidence. |

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.66 | Moderate for a discrete Pulgar/Arriagada child in the assigned chunk/source packet; low for broader identity linkage. |
| conflict_severity | 0.92 | The row-level contradiction blocks the entire evidence cluster. |
| evidence_quality | 0.82 | Civil birth registration image and chunk are strong in type, but derivative disagreement limits current use. |
| conversion_confidence | 0.38 | Chunk/source-packet evidence and current converted Markdown materially disagree. |
| claim_probability | 0.72 | Pulgar/Arriagada row is more probable than the Burgos/de la Cruz row for this staged source packet, pending QA. |
| relevance | 0.90 | Highly relevant to Pulgar/Arriagada parent-child reconstruction if certified. |
| canonical_readiness | 0.10 | Not ready for canonical promotion; `hold_for_conversion_qa`. |

## Recommended Next Action

Run targeted conversion QA against the visible source image, current converted Markdown, assigned chunk, and source packet. The QA note must identify the controlling row for entry 172, explain the Burgos/de la Cruz versus Pulgar/Arriagada mismatch, and certify the father field only to the visible extent. After QA, revise or supersede the affected source packet and rerun proof review before any canonical claim, relationship, merge, name-variant conclusion, or Dario-line comparison is promoted.
