---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525203741061.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
worker: postconv-identity-analysis-20260525210708351
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525203741061.md
---

# Identity Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers

- The assigned staged conflict draft reports an unresolved row-level conversion conflict for the same entry number. The chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the assigned converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- This is a family-cluster conflict, not a name-variant conflict. No child, parent, birth, residence, or relationship claim from this entry should be promoted until targeted conversion QA certifies the controlling row.
- The father field in the Pulgar/Arriagada row remains field-level uncertain. The chunk reads `Jose del Carmen Pulgar S.`, while the source packet requires QA to decide between `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Existing canonical wiki pages already contain generated evidence snapshots for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` based on prior entry-172 staging. Because this exact assigned converted file contradicts the Pulgar/Arriagada row, those canonical items remain low-readiness and should not be strengthened from this task.
- Entry 172 does not name Dario. It cannot by itself bridge `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar` to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.

## Evidence Boundary

Literal source readings and derivative context are kept separate here.

- Literal/supportive staged chunk reading: entry 172, registered 7 April 1888, records `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`; father `Jose del Carmen Pulgar S.`, Chilean, employee, resident `Calle de Colipí`; mother `Juana Arriagada de Pulgar`, Chilean, `Su sexo`, resident `Calle de Colipí`; informant `Ernesto Herrera L.`
- Source-packet interpretation: direct image inspection during evidence extraction supports the Pulgar/Arriagada row on register page 58, entry 172, but explicitly routes the matter to conversion QA because the assigned converted Markdown has a different family.
- Conflicting assigned converted Markdown reading: entry 172 is `Jose Miguel`, male, born 6 April 1888 at 10 p.m. `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.
- Existing canonical context: `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and warns against automatic merging with similarly named Pulgar records. `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-de-dios-amagada-de-pulgar.md`, and `wiki/people/dar-o-pulgar-arriagada.md` exist as separate or low-readiness local contexts.

## Hypothesis 1: Pulgar/Arriagada Row Controls Entry 172

Hypothesis: The controlling source row for entry 172 is the birth of `Jose del Carmen Segundo Pulgar Arriagada`, child of a father read as `Jose del Carmen Pulgar...` and mother `Juana Arriagada de Pulgar`; the Burgos/de la Cruz converted text is a row or file-assignment conversion error.

Supporting evidence:

- The assigned chunk gives a coherent full row for entry 172 on page 58 with the Pulgar/Arriagada family, dates, residences, informant, and official.
- The source packet says direct image context supports the Pulgar/Arriagada row rather than the Burgos/de la Cruz row.
- Existing canonical stubs for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` contain generated evidence from prior entry-172 Pulgar/Arriagada staging, but those entries are not a substitute for this task's conversion QA.

Conflicts and limits:

- The current assigned converted Markdown materially contradicts this hypothesis for the same entry number.
- The exact father-name suffix is unresolved.
- This hypothesis supports only the entry-172 child and parents if QA certifies the row; it does not identify a Dario person.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong coherent chunk/source-packet support for this row, blocked by derivative conflict. |
| conflict_severity | 0.95 | Different child and different parent set for the same entry number. |
| evidence_quality | 0.76 | Civil birth register context is high-value, but current task relies on staged derivative readings plus source-packet image review. |
| conversion_confidence | 0.35 | Low until converted Markdown and chunk are reconciled. |
| claim_probability | 0.78 | Probable if the source-packet image review is accepted, not ready for canonical promotion. |
| relevance | 1.00 | Directly relevant to the staged conflict draft. |
| canonical_readiness | 0.15 | Hold for conversion QA and father-field certification. |

## Hypothesis 2: Burgos/de la Cruz Row Controls Entry 172

Hypothesis: The assigned converted Markdown is the controlling reading, and entry 172 is `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; the chunk/source-packet Pulgar row is a derivative or assignment error.

Supporting evidence:

- The assigned converted Markdown explicitly gives entry 172 as `Jose Miguel` with father `Oswaldo Burgos` and mother `Concepcion de la Cruz`.

Conflicts and limits:

- The assigned chunk for the same source file and chunk id gives a different full entry-172 row.
- The source packet reports direct image context supporting the Pulgar/Arriagada row.
- No existing Pulgar-line canonical identity should be updated from this hypothesis because it removes Pulgar relevance rather than resolving it.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.32 | Supported by one assigned converted derivative, contradicted by chunk and source-packet image review. |
| conflict_severity | 0.95 | Same-entry family-cluster contradiction. |
| evidence_quality | 0.48 | Converted Markdown is useful but currently isolated against stronger local review context. |
| conversion_confidence | 0.25 | Low because the converted file conflicts with the chunk and packet. |
| claim_probability | 0.24 | Possible but currently weaker than the Pulgar/Arriagada hypothesis. |
| relevance | 1.00 | Directly relevant as the competing row. |
| canonical_readiness | 0.05 | Not ready; requires row-level conversion QA. |

## Hypothesis 3: Same-Person Or Duplicate Across The Two Rows

Hypothesis: `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel`, or the listed parent sets, are variant readings of the same child/family.

Supporting evidence:

- Both readings are tied to the same entry number in derivative local materials.

Conflicts and limits:

- The child names, parent names, birth dates, places/residences, and informant context diverge materially.
- `Pulgar Arriagada` versus `Burgos / de la Cruz` is not a spelling or accent variant.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | No substantive same-person evidence beyond shared entry number. |
| conflict_severity | 0.95 | Treating them as variants would collapse incompatible families. |
| evidence_quality | 0.62 | The evidence is adequate to reject a simple name-variant explanation. |
| conversion_confidence | 0.20 | The conflict itself shows conversion instability. |
| claim_probability | 0.03 | Very unlikely that these are variants of one identity. |
| relevance | 1.00 | Directly answers duplicate/name-variant risk. |
| canonical_readiness | 0.00 | Do not merge. |

## Hypothesis 4: Jose/Juana Parent Candidate Alignment

Hypothesis: If the Pulgar/Arriagada row controls, the father and mother may connect to existing local parent candidates: `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and possibly separate `Juana de Dios Amagada de Pulgar` or other Jose/Juana Pulgar records.

Supporting evidence:

- The chunk names a father in the form `Jose del Carmen Pulgar S.` and a mother `Juana Arriagada de Pulgar`.
- `wiki/people/jose-del-carmen-pulgar.md` exists and has a generated draft child link to `Tulio Cesar Luis Jose`.
- `wiki/people/juana-arriagada-de-pulgar.md` exists and has a generated probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` exists separately and has a generated draft child link to `Tulio Cesar Luis Jose`.

Conflicts and limits:

- `Juana Arriagada de Pulgar` is not silently equivalent to `Juana de Dios Amagada de Pulgar`; the given-name and surname readings differ.
- The father suffix or mark after `Pulgar` remains unresolved.
- Shared Pulgar context and spouse-style naming are hints for review, not merge authority.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Plausible local alignment for Jose/Juana candidates if Pulgar row controls, but exact parent identities need proof review. |
| conflict_severity | 0.70 | Moderate risk of merging distinct Jose/Juana candidates. |
| evidence_quality | 0.58 | Useful local context, mostly generated/staged and derivative. |
| conversion_confidence | 0.35 | Parent alignment depends on row QA and father-field QA. |
| claim_probability | 0.55 | Plausible but unproved. |
| relevance | 0.85 | Relevant to parent candidates and downstream Pulgar-line checks. |
| canonical_readiness | 0.10 | Hold for conversion QA plus parent-identity proof review. |

## Required Pulgar-Line Comparison

- `Dario Arturo Pulgar-Smith`: Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather. Entry 172 does not name `Dario`, `Arturo`, `Smith`, or a grandchild relationship. Same-person or relationship attachment from this entry is not supported. Rank: no present merge basis; probability 0.05.
- `Dario Arturo Pulgar`: Existing staged CV context concerns a document-level `Dario Arturo Pulgar`. Entry 172 names a child `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Arturo Pulgar`. Rank: no present merge basis; probability 0.04.
- `Dario Jose Pulgar-Arriagada`: Existing local photograph/context material uses this name in a separate context. Entry 172 shares Pulgar/Arriagada surname elements but has a different given-name string and no Dario evidence. Rank: preserve as separate/unresolved; probability 0.08.
- `Dario/Darío Pulgar Arriagada`: Existing canonical/staged context includes a `Darío Pulgar Arriagada` page tied to a 2000 expropriation event. Entry 172 does not identify Darío and predates that event by more than a century. Rank: no merge from this entry; probability 0.07.
- Jose/Juana parent candidates: If the Pulgar row controls, `Jose del Carmen Pulgar...` and `Juana Arriagada de Pulgar` are directly relevant parent candidates. They still require targeted father-field QA and a parent-identity proof review before any merge with other Jose/Juana pages or downstream Dario-line inference. Rank: highest relevance, held; probability 0.55 to 0.78 depending on exact claim.

## Conflict Summary

- Same-person conflict: high between two derivative readings of the same entry number; the likely issue is row/file conversion assignment, not biological identity.
- Duplicate-person risk: high if `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` are merged by entry number alone; moderate for Jose/Juana parent candidates if name variants are normalized without field QA.
- Name-variant conflict: low for Pulgar row versus Burgos row because the names are incompatible; moderate for `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.`; moderate for `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar`.
- Relationship conflict: high until row QA, because the parent set is either Pulgar/Arriagada or Burgos/de la Cruz.
- Chronology conflict: material between the two rows: Pulgar/Arriagada birth date is 8 March 1888; Burgos/de la Cruz converted row gives 6 April 1888.

## Ranked Conclusions

| Rank | Hypothesis | Claim probability | Canonical action |
| ---: | --- | ---: | --- |
| 1 | Pulgar/Arriagada row controls entry 172 | 0.78 | Hold; run targeted conversion QA and father-field certification. |
| 2 | Jose/Juana parent candidates may align with existing local Jose/Juana pages | 0.55 | Hold; only review after row QA. |
| 3 | Burgos/de la Cruz row controls entry 172 | 0.24 | Hold; possible only if conversion QA rejects the chunk/source-packet reading. |
| 4 | Entry 172 bridges to any Dario identity cluster | 0.04-0.08 | Do not merge or promote; require separate explicit bridge evidence. |
| 5 | The two row readings are same-person/name variants | 0.03 | Reject as current working explanation. |

## Recommended Next Action

Perform targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` by reconciling the source image, assigned converted Markdown, assigned chunk, and source packet. The QA result must state which family row controls entry 172 and must explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After row QA, run a proof-review promotion step only for the certified entry-172 claims. If the Pulgar/Arriagada row controls, then run a separate parent-identity proof review before merging or strengthening `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, or any other Jose/Juana candidate. A separate explicit identity-bridge proof review is required before any connection to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.
