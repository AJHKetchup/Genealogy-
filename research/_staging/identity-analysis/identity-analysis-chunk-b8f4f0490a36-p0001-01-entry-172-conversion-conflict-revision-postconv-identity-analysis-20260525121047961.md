---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260525121047961
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115123585.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115123585.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
canonical_readiness: hold
---

# Identity/Conflict Analysis: Entry 172 Pulgar/Arriagada Conversion Conflict

## Blockers First

1. Row-level conversion conflict blocks promotion. The staged draft and source packet say the current chunk records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, while the assigned converted Markdown records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`. This is not a spelling or name-variant issue.
2. The father-name ending remains unresolved. The current chunk reads `Jose del Carmen Pulgar S.`, while reviewed local cautions require preserving `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted QA certifies the image-visible form.
3. Canonical pages already contain low-confidence/probable Pulgar/Arriagada relationships derived from this chunk family, but this analysis cannot promote, rename, merge, or correct canonical pages.
4. This entry does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, or an Alexander John Heinz relationship. Those Pulgar-line identities must remain separate or unresolved from this entry unless a later proof-review bridge supplies direct evidence.

## Literal Source Readings Kept Separate

Current chunk/source-packet reading:

- Entry: `172`, page 58, Los Angeles civil birth register, 1888.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father line: `Jose del Carmen Pulgar S.` in the chunk; final suffix unresolved for canonical use.
- Mother line: `Juana Arriagada de Pulgar`.
- Parent residence: `Calle de Colipi`.
- Informant: `Ernesto Herrera L.`, present at the birth.

Assigned converted Markdown reading:

- Entry: `172`.
- Child: `Jose Francisco`.
- Birth: `El veinte i seis de Marzo de mil ochocientos ochenta i ocho, a las diez de la noche`.
- Birth place/residence: `En esta`.
- Father: `Oswaldo Gomez`.
- Mother: `Emilia de la Cruz`.
- Informant/father: `Oswaldo Gomez`.

Interpretation: these are competing row/file-assignment readings for entry 172. The Pulgar/Arriagada reading is family-relevant and supported by the current chunk/source packet, but the derivative transcript conflict keeps all dependent identities and relationships on hold.

## Hypotheses And Evidence

| Rank | Hypothesis | Evidence supporting | Evidence against / limits | Probability |
| ---: | --- | --- | --- | ---: |
| 1 | Current chunk correctly identifies entry 172 as the birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar [S.?]` and `Juana Arriagada de Pulgar`. | The current chunk and source packet agree on the Pulgar/Arriagada row, page 58, entry 172, with matching child, parents, birth date, place, and informant. Existing local review notes also repeatedly preserve this Pulgar row as the target requiring QA. | The assigned converted Markdown gives a wholly different row for entry 172; father suffix is unresolved. | 0.66 |
| 2 | The assigned converted Markdown is attached to the wrong row/source state or reflects a superseded conversion for the same source file. | Converted file and chunk share the same source path/hash context but disagree across multiple names, dates, parents, places, official names, and neighboring rows. The conflict pattern is larger than normal OCR variance. | Identity researcher cannot run conversion or inspect raw image for a new correction in this task. | 0.62 |
| 3 | `Jose del Carmen Pulgar S.` in the chunk is the same person as canonical/stub `Jose del Carmen Pulgar`. | Name core matches, father role matches the Pulgar/Arriagada family context, and canonical `jose-del-carmen-pulgar.md` already has a separate Pulgar-line child link from another register cluster. | Suffix/mark is unresolved; no birth, age, spouse, or cross-record identity bridge in this staged draft. Treat as a parent candidate, not a merge-ready same-person conclusion. | 0.52 |
| 4 | `Juana Arriagada de Pulgar` in entry 172 is the mother candidate already represented by canonical/stub `Juana Arriagada de Pulgar`. | Exact name match and same child relation appear in the current chunk/source packet and canonical evidence snapshot. | Dependent on the same row-level conversion conflict; no independent identity bridge beyond this entry. | 0.60 |
| 5 | Entry 172 supplies a direct bridge to Dario Arturo Pulgar-Smith or document-level Dario Arturo Pulgar. | Pulgar surname and Arriagada maternal surname are family-context hints for later double-checking. | The entry does not name Dario, Arturo, Smith, Pulgar-Smith, Alexander John Heinz, or a relationship to the known family-supplied grandfather. | 0.08 |
| 6 | Entry 172 supplies a direct bridge to Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, Darío Pulgar Arriagada, or Dario Pulgar A. | Arriagada/Pulgar surname pattern may be relevant to a future Pulgar-line proof review. | This entry names `Jose del Carmen Segundo`, not Dario. No `Jose`/`J.` as a Dario middle-name expansion, no medical, passenger, property, Geneva, or CV context. | 0.06 |

## Conflict Analysis

- Same-person conflict: unresolved for `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` because the final father-name mark is not certified.
- Duplicate-person risk: moderate for parent stubs if downstream work treats `Jose del Carmen Pulgar S.` as automatically identical with canonical `Jose del Carmen Pulgar`; high if this entry is used to merge any Dario/Pulgar-Arriagada cluster by surname alone.
- Name-variant conflict: `Pulgar S.` may be a literal suffix/initial, a stray mark, or an uncertain reading. Preserve all three literal outcomes until QA.
- Relationship conflict: the chunk supports a child-parent pair for `Jose del Carmen Segundo Pulgar Arriagada` with `Jose del Carmen Pulgar [S.?]` and `Juana Arriagada de Pulgar`; the converted Markdown supports a different family group entirely (`Jose Francisco`, `Oswaldo Gomez`, `Emilia de la Cruz`). Both cannot be promoted for the same entry 172.
- Chronology conflict: chunk birth date is 1888-03-08 15:00; converted Markdown birth date is 1888-03-26 22:00. This is material, not normalization.
- Canonical context conflict: canonical pages already expose probable/low-confidence evidence from the Pulgar entry family. This analysis should reinforce hold status until targeted conversion QA and proof review rerun.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.64 | Moderate confidence in the Pulgar/Arriagada row as the intended local target, reduced by the assigned converted Markdown conflict. |
| conflict_severity | 0.95 | Different child, parents, dates, places, and row context make this a material row-level/file-assignment conflict. |
| evidence_quality | 0.68 | Current chunk/source packet are detailed and internally coherent; derivative disagreement prevents higher quality. |
| conversion_confidence | 0.42 | Mixed: the chunk is coherent, but the assigned converted Markdown is incompatible with it. |
| claim_probability | 0.66 | Pulgar/Arriagada entry claim is more probable locally than the converted row for this task, but not promotion-ready. |
| relevance | 0.88 | High Pulgar-line relevance if QA confirms the row; direct Dario relevance remains low. |
| canonical_readiness | 0.15 | Hold for conversion QA and proof review; no canonical promotion or merge should proceed from this note. |

## Pulgar-Line Comparison

- Dario Arturo Pulgar-Smith: canonical page is family-supplied as Alexander John Heinz's maternal grandfather and warns against automatic attachment of Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records. Entry 172 does not name him or Smith.
- Dario Arturo Pulgar: CV/document-level subject appears in separate staged contexts. Entry 172 does not name Arturo or provide a CV/occupation bridge.
- Dario Jose Pulgar-Arriagada / Dario J. Pulgar Arriagada: separate medical/title and related local contexts exist, but this entry names `Jose del Carmen Segundo`, not Dario Jose or Dario J.
- Dario/Dario Pulgar Arriagada / Darío Pulgar Arriagada: canonical stub has a 2000 expropriation evidence item. Entry 172 is an 1888 birth-register conflict and does not bridge to that property/person context.
- Jose/Juana parent candidates: `Jose del Carmen Pulgar [S.?]` and `Juana Arriagada de Pulgar` are plausible parents of the entry-172 child only if the Pulgar row is QA-confirmed. They should not be used as Dario-line ancestors without a later lineage bridge.

## Recommended Next Action

Run targeted conversion QA for the exact source image, assigned converted Markdown, chunk, and manifest. The QA result must decide whether entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row, and must explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review on the child identity, birth facts, father claim, mother claim, child-parent relationships, and any parent-pair clue. Only after that should a separate Pulgar-line identity bridge compare the confirmed entry against Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, and Jose/Juana parent candidates.
