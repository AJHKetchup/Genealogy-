---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260525174615713
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170607416.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170607416.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170607416.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
created: 2026-05-25
---

# Identity And Conflict Analysis: Entry 172 Pulgar/Arriagada Conversion Conflict

## Blockers First

- The controlling row for entry `172` is unresolved. The assigned chunk and staged source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, but the assigned converted Markdown reads entry `172` as `Jose Francisco`, child of `Oswaldo Gomez` and `Rosario de la Cruz de la Maza`.
- This is a row-level or file-assignment conflict, not a name variant. No child identity, parent-child relationship, or parent candidate should be promoted until targeted conversion QA decides which row controls entry `172`.
- The father-name ending after `Jose del Carmen Pulgar` is unresolved. Proof review must preserve and decide among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- The record does not name Dario. It cannot bridge or merge `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, adult/child `Dario Pulgar` passenger stubs, or any Dario CV/Habitat clusters.
- Existing canonical wiki context already contains stubs for `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Pulgar`, but this staged revision should keep dependent facts at hold because the current converted Markdown contradicts the Pulgar/Arriagada row.

## Literal Source Readings Kept Separate

### Chunk And Source Packet Reading

- Entry: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Father: chunk reads `Jose del Carmen Pulgar S.`; staged review leaves final suffix or mark unresolved after `Pulgar`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age `Veintiseis años`, profession `Empleado`, residence `Calle de Valdivia`.

### Assigned Converted Markdown Reading

- Entry: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose Francisco`; sex `Hombre`.
- Birth: `En veinte de Febrero de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En Pellin`.
- Father: `Oswaldo Gomez`.
- Mother: `Rosario de la Cruz de la Maza`.
- Informant: `Oswaldo Gomez`; age `Veinte i seis años`; profession `Empleado`; residence `Pellin`.

## Hypotheses

### Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

The child in entry `172` is `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar` plus unresolved suffix/mark and mother `Juana Arriagada de Pulgar`.

Evidence supporting:

- The assigned chunk explicitly transcribes entry `172` with the Pulgar/Arriagada child and parents.
- The staged source packet reports an image-visible row review supporting the Pulgar/Arriagada reading.
- The page reference, source path, chunk id, and source packet all point to the same staged assignment for entry `172`.
- Existing canonical stubs contain Pulgar/Arriagada facts sourced to earlier staging for this same chunk, showing the same local evidence cluster has been recognized before.

Conflicts and limits:

- The converted Markdown gives a completely different child-parent-place cluster for entry `172`.
- The father field cannot yet be normalized because the final mark after `Pulgar` remains unresolved.
- No Dario name or Dario relationship appears in this record.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.68 | Strong within the chunk/source-packet reading, reduced by direct converted-file contradiction. |
| conflict_severity | 0.95 | Different child, parents, birth date, place, informant, and residence for the same entry number. |
| evidence_quality | 0.62 | Staged image review and chunk are useful, but derivative conversion disagreement blocks promotion. |
| conversion_confidence | 0.42 | Mixed; the source packet itself marks conversion confidence as mixed. |
| claim_probability | 0.66 | Probable if the chunk/image row is controlling; not promotion-ready. |
| relevance | 0.90 | Directly relevant to Pulgar/Arriagada parent candidates. |
| canonical_readiness | 0.15 | Hold until targeted conversion QA and proof review rerun. |

### Hypothesis 2: Entry 172 Is The Gomez/de la Cruz de la Maza Birth Row

The child in entry `172` is `Jose Francisco`, son of `Oswaldo Gomez` and `Rosario de la Cruz de la Maza`.

Evidence supporting:

- The assigned converted Markdown transcribes entry `172` as the Gomez/de la Cruz de la Maza row.
- The converted Markdown claims complete transcription and no uncertainty for the document.

Conflicts and limits:

- The chunk and source packet for this same assignment read entry `172` as the Pulgar/Arriagada row.
- The staged conflict draft treats the disagreement as high-confidence row-level or file-assignment conflict.
- The Gomez/de la Cruz de la Maza reading has no apparent Pulgar-line identity relevance unless QA determines that it is actually the controlling row.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Supported by the converted file, but contradicted by the assigned chunk and staged image review. |
| conflict_severity | 0.95 | Mutually exclusive with the Pulgar/Arriagada identity for the same entry number. |
| evidence_quality | 0.45 | Single derivative conversion layer against chunk/source-packet review. |
| conversion_confidence | 0.35 | Converted file is internally confident but externally contradicted. |
| claim_probability | 0.34 | Possible, pending row-control QA. |
| relevance | 0.20 | Low Pulgar-line relevance unless QA rejects the Pulgar/Arriagada row. |
| canonical_readiness | 0.05 | Do not promote from this conflict state. |

### Hypothesis 3: `Jose del Carmen Pulgar` Is A Parent Candidate For This Child

If the Pulgar/Arriagada row controls, `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S./[?]` is the father of `Jose del Carmen Segundo Pulgar Arriagada`.

Evidence supporting:

- The chunk reads father as `Jose del Carmen Pulgar S.`.
- The source packet confirms the father field begins `Jose del Carmen Pulgar` and isolates only the final suffix or mark as unresolved.
- Existing canonical `wiki/people/jose-del-carmen-pulgar.md` has a separate draft child link to `Tulio Cesar Luis Jose`, showing a same-name parent candidate exists in the local wiki.

Conflicts and limits:

- The final father suffix may be meaningful and must not be silently dropped.
- The same-name canonical parent candidate cannot be merged with this father field by name alone.
- If the converted Markdown controls, this father candidate is not in entry `172`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.55 | Father name is reasonably read, but suffix and row control are unresolved. |
| conflict_severity | 0.80 | Wrong row control would create a false parent-child relationship. |
| evidence_quality | 0.58 | Chunk/source-packet support exists; final mark unresolved. |
| conversion_confidence | 0.40 | Father field depends on disputed row. |
| claim_probability | 0.56 | Plausible parent candidate only under Hypothesis 1. |
| relevance | 0.85 | Direct parent-candidate relevance. |
| canonical_readiness | 0.10 | Needs targeted QA plus proof-review comparison to existing Jose candidate(s). |

### Hypothesis 4: `Juana Arriagada de Pulgar` Is A Parent Candidate For This Child

If the Pulgar/Arriagada row controls, `Juana Arriagada de Pulgar` is the mother of `Jose del Carmen Segundo Pulgar Arriagada`.

Evidence supporting:

- The chunk reads the mother as `Juana Arriagada de Pulgar`.
- The source packet repeats that mother reading without the father-field suffix uncertainty.
- Existing canonical `wiki/people/juana-arriagada-de-pulgar.md` has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada` from earlier staging for this chunk.

Conflicts and limits:

- The mother relationship still depends on the unresolved controlling row for entry `172`.
- The name form `de Pulgar` suggests marital context, but it does not by itself prove spouse identity or broader lineage placement.
- If the converted Markdown controls, the mother in entry `172` is `Rosario de la Cruz de la Maza`, not Juana.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Mother reading is clear within the Pulgar/Arriagada row. |
| conflict_severity | 0.80 | Wrong row control would create a false parent-child relationship. |
| evidence_quality | 0.64 | Less internally uncertain than the father field, but still blocked by row conflict. |
| conversion_confidence | 0.42 | Depends on disputed row. |
| claim_probability | 0.64 | Probable if Hypothesis 1 controls. |
| relevance | 0.88 | Direct parent-candidate relevance. |
| canonical_readiness | 0.15 | Keep held until conversion QA. |

### Hypothesis 5: This Record Bridges A Dario-Line Person

The entry might connect to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.

Evidence supporting:

- The Pulgar/Arriagada row, if confirmed, shares the surnames `Pulgar` and `Arriagada` with some unresolved Dario-line clusters.
- Existing wiki context includes a family-supplied `Dario Arturo Pulgar-Smith` and a separate `Darío Pulgar Arriagada` stub.

Conflicts and limits:

- The staged draft and referenced entry do not name Dario.
- No birth, parent, spouse, child, residence continuity, chronology bridge, or identity-bearing Dario source connects this 1888 child or parents to any Dario person.
- `Dario Arturo Pulgar-Smith` is currently family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic merges with similar source clusters.
- `Dario Arturo Pulgar` CV/Habitat clusters, `Dario Jose Pulgar-Arriagada`, and `Dario/Dario Pulgar Arriagada` remain separate or unresolved identity clusters unless a reviewed bridge supplies stronger identity facts.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | Surname-context hint only; no named Dario in this record. |
| conflict_severity | 0.90 | Merging by surname would risk major cross-generation conflation. |
| evidence_quality | 0.20 | No direct Dario evidence in the assigned draft. |
| conversion_confidence | 0.42 | Even the underlying Pulgar/Arriagada row is not QA-resolved. |
| claim_probability | 0.05 | Not supported for same-person or relationship attachment. |
| relevance | 0.40 | Useful only as a future double-check if a bridge source names this family. |
| canonical_readiness | 0.00 | No Dario canonical action. |

## Dario-Line Anti-Conflation Comparison

| Candidate | Current local evidence context | Comparison result for this staged draft |
| --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | Canonical family-supplied maternal grandfather of Alexander John Heinz; warns against automatic merges. | No bridge. This entry does not name Dario or Smith. |
| `Dario Arturo Pulgar` | Staged CV/document-level subject in other local drafts. | No bridge. This birth entry does not identify a CV subject or work-history person. |
| `Dario Jose Pulgar-Arriagada` | Unresolved Dario/Pulgar-Arriagada name cluster in staging context. | No bridge. Shared surname pattern only. |
| `Dario/Dario Pulgar Arriagada` / `Darío Pulgar Arriagada` | Canonical stub has a 2000 expropriation event. | No bridge. 1888 Jose child and parents cannot be merged with 2000 Dario stub by surname. |
| Adult `Dario Pulgar`, age 64 in 1953 | Separate canonical passenger stub. | No bridge; chronology and identity facts absent here. |
| Child `Dario Pulgar`, age 11 in 1953 | Separate canonical passenger stub. | No bridge; chronology and identity facts absent here. |

## Conflict Findings

- Same-person conflict: unresolved only for the entry `172` child identity because two mutually exclusive row readings exist.
- Duplicate-person risk: high if `Jose del Carmen Pulgar` from this record is merged with an existing Jose candidate before suffix and row QA; high if `Juana Arriagada de Pulgar` is treated as fully canonical before row QA.
- Name-variant conflict: father may be `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`; this must remain unresolved.
- Relationship conflict: Pulgar/Arriagada parent-child claims conflict with the converted-file Gomez/de la Cruz de la Maza parent-child cluster for the same entry number.
- Chronology conflict: none internal to the Pulgar/Arriagada reading; no Dario chronology can be inferred.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Entry `172` is the Pulgar/Arriagada birth row. | 0.66 | Targeted conversion QA against source image, converted Markdown, chunk, and source packet. |
| 2 | `Juana Arriagada de Pulgar` is the mother of the Pulgar/Arriagada child. | 0.64 | Only after row-control QA confirms the Pulgar/Arriagada row. |
| 3 | `Jose del Carmen Pulgar` / `Pulgar S.` / `Pulgar [?]` is the father of the Pulgar/Arriagada child. | 0.56 | Father-field proof review must certify the final suffix or mark. |
| 4 | Entry `172` is the Gomez/de la Cruz de la Maza row. | 0.34 | Test during the same row-control QA; reject Pulgar claims if this controls. |
| 5 | This record bridges any Dario-line person. | 0.05 | No action except future anti-conflation review if a direct bridge source appears. |

## Recommended Next Action

Keep all dependent identity, relationship, claim, parent-candidate, and Dario-line comparison work at `hold_for_conversion_qa`. The exact next proof-review step is targeted row-control QA for entry `172`: compare the source image, assigned converted Markdown, assigned chunk, and source packet; identify whether entry `172` is the Pulgar/Arriagada row or the Gomez/de la Cruz de la Maza row; then certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After that QA, rerun proof review before any canonical promotion or merge. If the Pulgar/Arriagada row is confirmed, separately compare `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` against existing canonical parent-candidate pages. Do not attach this record to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada` without a later reviewed source that explicitly bridges names, dates, relationships, and life context.
