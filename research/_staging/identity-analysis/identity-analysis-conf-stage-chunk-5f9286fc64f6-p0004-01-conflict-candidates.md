---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/CONF-STAGE-CHUNK-5f9286fc64f6-P0004-01-conflict-candidates.md
worker: postconv-identity-analysis-20260523075138684
staged_draft: research/_staging/conflicts/CONF-STAGE-CHUNK-5f9286fc64f6-P0004-01-conflict-candidates.md
source_path: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-5f9286fc64f6-P0004-01-cv-dario-pulgar-page-4.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md
chunk_id: CHUNK-5f9286fc64f6-P0004-01
page_reference: page 4
analysis_status: hold
canonical_readiness: hold_for_conversion_qa_and_identity_bridge
---

# Identity/Conflict Analysis: CONF-STAGE-CHUNK-5f9286fc64f6-P0004-01

## Blockers

- The exact staged conflict draft reviewed here is `research/_staging/conflicts/CONF-STAGE-CHUNK-5f9286fc64f6-P0004-01-conflict-candidates.md`.
- The staged conflict draft reports no direct evidence conflict inside page 4, but it flags identity attribution because page 4 is a continuation page and does not repeat the CV subject's full name.
- Page 4's literal text does not independently name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`.
- Subject attribution comes from the source path, converted-file title/context, and source packet, not from a page-body name.
- The source packet has `promotion_recommendation: hold_for_conversion_qa` and reports medium reading confidence, missing rendered page image, and visible text issues such as `Indian Sates` and `aassessing`.
- The referenced chunk path aligns with page 4, but its front matter reports `chunk_id: CHUNK-56be215c030b-P0004-01` and converted SHA `56be215c030b...`, while this staged conflict/source-packet family uses `CHUNK-5f9286fc64f6-P0004-01` and converted SHA `5f9286fc64f6...`. Reconcile this before promotion.
- The canonical candidate `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns against attaching similarly named Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records without identity review.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, reviewed notes, or canonical wiki pages were edited.

## Hypothesis 1: No Direct Conflict Within Page 4

Hypothesis: The staged conflict draft is correct that page 4 contains no direct internal identity, relationship, or chronology conflict.

Literal evidence:

- The staged draft says, `No direct evidence conflict was identified within this chunk`.
- The page-4 literal support cited in the staged draft records `2000`, `International Bank for Reconstruction and Development (IBRD)`, `Bolivia, Peru`, and `Senior Consultant`.
- The page-4 literal support also records `1999 - 2000`, `Antamina Mining Company`, `Huarmey, Peru`, and `Head Community Relations`.
- The source packet and chunk contain no competing personal name, parent, spouse, child, birth event, death event, or relationship statement.

Interpretation:

- This is the leading finding. Page 4 should be treated as a conversion/identity-attribution hold, not as a substantive conflict record.
- The absence of an internal conflict does not make the occupational claims canonically ready.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.80 | Page belongs to a locally titled CV, but the page body is unnamed. |
| conflict_severity | 0.18 | No internal contradiction appears; the risk is provenance and over-attribution. |
| evidence_quality | 0.70 | Staged draft, source packet, converted file, and chunk generally align on page content. |
| conversion_confidence | 0.62 | Typed text is readable, but page-image QA and chunk/hash reconciliation are pending. |
| claim_probability | 0.86 | High probability the correct conflict finding is "no direct conflict, hold for QA." |
| relevance | 1.00 | Directly answers the assigned staged conflict draft. |
| canonical_readiness | 0.26 | Hold pending conversion QA and identity bridge review. |

## Hypothesis 2: Page 4 Belongs To Document-Level CV Subject Dario Arturo Pulgar

Hypothesis: The occupational entries on page 4 belong to the document-level CV subject identified locally as `Dario Arturo Pulgar`.

Literal evidence:

- The source path is `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- The converted file title is `CV of Dario Arturo Pulgar pages 4-9`.
- The source packet title is `Source Packet: CV of Dario Arturo Pulgar, Page 4`.
- Page 4 literally contains IBRD and Antamina occupational entries for 1999-2000 and 2000.
- Page 4 does not name another person.

Interpretation:

- This is probable document-level attribution, but it is not page-local proof of the subject's identity.
- Promote only after page-image QA confirms the headings/body and an identity-bearing CV page or accepted local bridge supports the subject assignment.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.82 | Multiple metadata layers identify the CV as Dario Arturo Pulgar's; page body is unnamed. |
| conflict_severity | 0.24 | Wrong assignment would misattribute work history, but no competing page name appears. |
| evidence_quality | 0.72 | Source packet and converted context are coherent, with metadata caveats. |
| conversion_confidence | 0.62 | Medium confidence and missing rendered page image keep it below promotion level. |
| claim_probability | 0.84 | Probable as held CV-subject evidence. |
| relevance | 0.98 | Central to interpreting the conflict draft. |
| canonical_readiness | 0.30 | Hold. |

## Hypothesis 3: Same Person As Canonical Dario Arturo Pulgar-Smith

Hypothesis: The CV subject `Dario Arturo Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith`, with the CV using a shortened surname form.

Literal evidence:

- The canonical page preferred name is `Dario Arturo Pulgar-Smith`.
- The canonical page states that Dario Arturo Pulgar-Smith is Alexander John Heinz's maternal grandfather, based on family-supplied knowledge.
- The document-level CV name `Dario Arturo Pulgar` shares the given names `Dario Arturo` and the `Pulgar` surname element.
- Page 4 does not state `Smith`, `Pulgar-Smith`, Alexander John Heinz, a parent, spouse, child, birth date, or other direct family bridge.

Interpretation:

- Same-person identity is plausible, but page 4 cannot prove the surname variant or canonical family placement.
- Family context justifies a targeted proof-review step; it does not justify silently correcting `Pulgar` to `Pulgar-Smith`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.60 | Strong name overlap, no direct `Pulgar-Smith` bridge. |
| conflict_severity | 0.44 | Incorrect attachment would place occupational chronology on the wrong canonical person. |
| evidence_quality | 0.56 | Evidence is name overlap plus family-supplied canonical context. |
| conversion_confidence | 0.62 | Conversion does not resolve the surname-form issue. |
| claim_probability | 0.58 | Plausible but unproved in this draft. |
| relevance | 0.94 | Main canonical comparison. |
| canonical_readiness | 0.18 | Do not merge, rename, or promote from this page. |

## Hypothesis 4: Same Person As Dario Jose Pulgar-Arriagada / Dario Pulgar Arriagada

Hypothesis: The page-4 CV subject is the same person as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`.

Literal evidence:

- Existing local context includes a canonical `Darío Pulgar Arriagada` page with a narrow 5 December 2000 expropriation event.
- Other staged local materials refer to `Dario Jose Pulgar-Arriagada` or related Pulgar-Arriagada forms in separate source clusters.
- Page 4's document-level name is `Dario Arturo Pulgar`.
- Page 4 does not state `Jose`, `Arriagada`, `Pulgar-Arriagada`, `Pulgar A.`, medical/Geneva context, property context, parents, or lineage.

Interpretation:

- Name overlap alone is insufficient. The Pulgar-Arriagada clusters must remain separate or unresolved until a reviewed source bridges full names, dates, relationships, and life context.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.12 | Only broad Dario/Pulgar overlap appears. |
| conflict_severity | 0.78 | Name-only merging could collapse distinct surname forms and source clusters. |
| evidence_quality | 0.46 | Comparison evidence is outside this page and partly held elsewhere. |
| conversion_confidence | 0.50 | Separate source clusters have their own QA caveats. |
| claim_probability | 0.10 | Low from this staged draft. |
| relevance | 0.88 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.02 | Do not attach or merge. |

## Hypothesis 5: Relationship To Jose/Juana Parent Candidates

Hypothesis: Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, or Juana de Dios Amagada de Pulgar may belong somewhere in the broader Pulgar line, but page 4 does not connect them to the CV subject.

Literal evidence:

- Existing wiki context includes Jose/Juana Pulgar-line candidates, including `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Those candidates come from separate birth/register clusters with unresolved or image-sensitive readings.
- Page 4 contains no Jose, Juana, parent, spouse, child, household, birth-register, or lineage statement.

Interpretation:

- Jose/Juana candidates are an anti-conflation checklist only for this page. Page 4 supports no family-placement claim.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.06 | No direct identity or kinship bridge appears. |
| conflict_severity | 0.62 | Unsupported lineage attachment would create relationship errors. |
| evidence_quality | 0.40 | Parent-candidate evidence is external and unresolved in places. |
| conversion_confidence | 0.42 | Jose/Juana readings have separate conversion concerns. |
| claim_probability | 0.05 | Page 4 does not support a Jose/Juana relationship claim. |
| relevance | 0.62 | Relevant only as required Pulgar-line context. |
| canonical_readiness | 0.01 | No relationship action supported. |

## Conflicts

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: moderate for CV `Dario Arturo Pulgar` versus canonical `Dario Arturo Pulgar-Smith`; high if merged by name alone with `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, `Darío Pulgar Arriagada`, or other Dario Pulgar stubs.
- Name-variant conflict: page 4 supports only the document-title form `Dario Arturo Pulgar`; it does not resolve `Pulgar` versus `Pulgar-Smith`, `Pulgar-Arriagada`, or `Pulgar Arriagada`.
- Relationship-conflict evidence: none in the literal page-4 text. Page 4 does not state parents, spouse, child, grandchild, relationship to Alexander John Heinz, or Jose/Juana parentage.
- Chronology-conflict evidence: none within the IBRD 2000 and Antamina 1999-2000 entries. Cross-cluster chronology should still be checked before any merge with older passenger, medical, or property clusters.
- Conversion/provenance conflict: page 4 is readable, but the source packet holds for rendered page-image QA, and the referenced chunk file's chunk id/hash differs from the staged conflict/source-packet identifiers.

## Ranked Hypotheses

| rank | hypothesis | probability | next step |
|---:|---|---:|---|
| 1 | No direct conflict within page 4; hold for QA | 0.86 | Reconcile conversion/page-image/chunk metadata before any promotion. |
| 2 | Page 4 belongs to document-level CV subject `Dario Arturo Pulgar` | 0.84 | Verify source image and identity-bearing CV context. |
| 3 | Same person as canonical `Dario Arturo Pulgar-Smith` | 0.58 | Require explicit reviewed bridge from `Dario Arturo Pulgar` to `Pulgar-Smith`. |
| 4 | Same as `Dario Jose Pulgar-Arriagada` / `Dario/Dario Pulgar Arriagada` | 0.10 | Preserve separately or unresolved; do not merge by name alone. |
| 5 | Connected to Jose/Juana parent candidates | 0.05 | No action from page 4; revisit only if lineage evidence appears. |

## Recommended Next Action

Keep `research/_staging/conflicts/CONF-STAGE-CHUNK-5f9286fc64f6-P0004-01-conflict-candidates.md` as a held no-direct-conflict / identity-attribution caution. Do not merge people, rename canonical pages, promote occupational facts, or attach page-4 claims to `wiki/people/dario-arturo-pulgar-smith.md` from this staged draft alone.

The exact next proof-review step is targeted CV conversion and identity QA: restore or generate the page-4 rendered image, compare the IBRD and Antamina headings and body text against the page image, reconcile the `5f9286fc64f6` versus `56be215c030b` chunk/hash metadata, and locate a reviewed identity-bearing CV page or accepted local source that explicitly connects `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`. Before any Pulgar-line canonical attachment, run anti-conflation comparison against `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, `Darío Pulgar Arriagada`, other Dario Pulgar stubs, and Jose/Juana parent-candidate pages.
