---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260524120432731
task_id: identity-analysis:research/_staging/identity/ID-STAGE-CHUNK-a485f4030ce7-P0009-01-dario-cv-subject.md
staged_draft: research/_staging/identity/ID-STAGE-CHUNK-a485f4030ce7-P0009-01-dario-cv-subject.md
source_packet: research/_staging/source-packets/chunk-a485f4030ce7-p0009-01-cv-dario-arturo-pulgar-education-languages.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0009-chunk-01.md
assigned_chunk_id: CHUNK-a485f4030ce7-P0009-01
referenced_chunk_frontmatter_id: CHUNK-c25ee050e822-P0009-01
analysis_status: hold
canonical_readiness: hold_for_identity_bridge_and_metadata_audit
---

# Identity/Conflict Analysis: ID-STAGE-CHUNK-a485f4030ce7-P0009-01

## Blockers

- Exact staged draft reviewed: `research/_staging/identity/ID-STAGE-CHUNK-a485f4030ce7-P0009-01-dario-cv-subject.md`.
- Page 9 is not independently identity-bearing. The literal page body lists education and languages, but does not print `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Smith`, `Pulgar-Arriagada`, `Dario Jose`, `Jose`, `Juana`, or any family relationship.
- The current attribution to `Dario Arturo Pulgar` is document-level context from the source title/path, converted-file title, source packet, and staged identity draft. It is not a page-local name statement.
- Metadata needs proof-review reconciliation. The staged draft and source packet use `CHUNK-a485f4030ce7-P0009-01`, while the referenced physical chunk front matter identifies the same page file as `CHUNK-c25ee050e822-P0009-01`.
- The possible canonical match is `wiki/people/dario-arturo-pulgar-smith.md`, but this page supplies no `Pulgar-Smith` surname bridge and no relationship to Alexander John Heinz.
- The source packet reports that the page image now exists locally and visually supports the page-9 entries, but identity linkage still requires fuller CV context before attaching claims to a canonical person.
- No external research was performed. No raw sources, converted Markdown, chunks, reviewed notes, or canonical wiki pages were edited.

## Literal Source Readings

- Page 9 lists `1967 - 1968 : Stanford University. Stanford, California` with `Fulbright Scholarship. M.A. Communications`.
- Page 9 lists `1963 - 1966 : Universidad de Concepcion, Escuela de Periodismo. Chile` with `Journalism`.
- Page 9 lists `1960 - 1963 : Universidad de Concepcion, Escuela de Derecho. Chile` with `Field of Study: Law`.
- Page 9 lists `1954 - 1959 : Liceo Enrique Molina. Concepcion, Chile` with `Humanities, Baccalaureate`.
- Page 9 lists spoken languages as Spanish, English, French, Italian, and Portuguese.
- Page 9 lists written languages as Spanish, English, and French.

Interpretation kept separate: these entries are likely part of the local CV source titled for `Dario Arturo Pulgar`, but the page body itself does not name the CV subject.

## Hypothesis 1: Page 9 Belongs To Document-Level `Dario Arturo Pulgar`

This is the strongest narrow conclusion. The page belongs to a locally staged CV identified as `Dario Arturo Pulgar`, but it is not standalone identity proof.

Supporting evidence:

- The staged draft names `candidate_identity: "Dario Arturo Pulgar"`.
- The source packet identifies `source_identity` as `Dario Arturo Pulgar`, from source title/file identity rather than page-body text.
- The source path and converted-file title both point to `CV of Dario Arturo Pulgar`.
- The source packet and chunk agree on the substantive education and language entries.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.82 | Multiple local metadata layers agree on the document-level subject; page body is unnamed and chunk-id drift remains. |
| conflict_severity | 0.24 | No internal content conflict; risk is over-attribution beyond document context. |
| evidence_quality | 0.74 | Staged draft, source packet, converted file, and chunk content agree on page-9 evidence. |
| conversion_confidence | 0.86 | Typed transcription is clear; source packet reports local visual QA, pending proof-review acceptance. |
| claim_probability | 0.86 | Probable that the education/language entries belong to the document-level CV subject. |
| relevance | 0.99 | Directly addresses the staged identity draft. |
| canonical_readiness | 0.38 | Hold until identity bridge and chunk/hash reconciliation are proof-reviewed. |

## Hypothesis 2: Same Person As Canonical `Dario Arturo Pulgar-Smith`

Plausible but unproved. `Dario Arturo Pulgar` and `Dario Arturo Pulgar-Smith` share distinctive name elements, but page 9 does not prove the surname variant or family relationship.

Supporting evidence:

- The staged draft nominates `wiki/people/dario-arturo-pulgar-smith.md` as a possible canonical match.
- The canonical page records a family-supplied person named `Dario Arturo Pulgar-Smith`.
- The canonical page explicitly warns that records mentioning Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith require identity review before attachment.

Conflicts and limits:

- Page 9 does not state `Smith`, `Pulgar-Smith`, Alexander John Heinz, parentage, spouse, child, birth, death, or any relationship.
- Family-supplied canonical context is useful for targeting review, but it cannot silently correct `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.60 | Strong name overlap, no page-9 surname or relationship bridge. |
| conflict_severity | 0.45 | Wrong attachment would place CV education/language facts on the wrong canonical person. |
| evidence_quality | 0.48 | Evidence is document title plus family-supplied canonical context. |
| conversion_confidence | 0.86 | Readability does not resolve the surname-variant question. |
| claim_probability | 0.58 | Possible/probable enough for targeted proof review, not promotion. |
| relevance | 0.97 | This is the nominated canonical match. |
| canonical_readiness | 0.20 | No merge, rename, or fact promotion yet. |

## Hypothesis 3: Same Broader CV/Habitat `Dario Pulgar` Cluster

Page 9 is consistent with adjacent CV work-history staging and local Habitat/Chile Films/NFB context, but this page itself only adds education/language context.

Supporting evidence:

- Other staged CV tasks and identity notes locally identify a document-level `Dario Arturo Pulgar` and repeatedly hold the bridge to canonical `Dario Arturo Pulgar-Smith` for separate proof review.
- Page 9's 1954-1968 education sequence is compatible with later employment chronology in the staged CV context.

Conflicts and limits:

- Page 9 does not mention Habitat, Chile Films, NFB, profession, exile, or family relationship.
- Adjacent staged context can guide comparison, but should not be promoted from this page alone.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.62 | Same converted CV context supports cluster continuity; page 9 does not name work-history details. |
| conflict_severity | 0.30 | Main risk is overusing held staged context. |
| evidence_quality | 0.56 | Adjacent-page context is useful but indirect for this page. |
| conversion_confidence | 0.84 | Page text is usable; promotion QA remains open. |
| claim_probability | 0.62 | Plausible as part of the same CV cluster. |
| relevance | 0.84 | Useful for later identity resolution. |
| canonical_readiness | 0.20 | Hold. |

## Hypothesis 4: Same Person As Child Passenger `Dario Pulgar`, Age 11 In 1953

Chronologically compatible but circumstantial. A child passenger aged 11 on 1953-08-07 could plausibly attend Liceo Enrique Molina during 1954-1959, but this page gives no passenger-list bridge.

Supporting evidence:

- Existing canonical/staged context includes a child passenger `Dario Pulgar` aged 11 in 1953.
- The page-9 school chronology begins in 1954, which is not inconsistent with that age.

Conflicts and limits:

- Page 9 gives no age, birth date, travel, parents, residence, `Arturo`, or `Smith`.
- It does not support merging the child passenger cluster with the CV subject.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.48 | Name and chronology are compatible only. |
| conflict_severity | 0.44 | Premature merge would collapse separate source clusters. |
| evidence_quality | 0.50 | Useful local chronology, indirect. |
| conversion_confidence | 0.74 | Both clusters have usable but separate evidence. |
| claim_probability | 0.46 | Possible, not proved. |
| relevance | 0.72 | Relevant same-name and chronology check. |
| canonical_readiness | 0.10 | No merge or attachment supported. |

## Hypothesis 5: Same As `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Darío J. Pulgar Arriagada`, Or `Dario Pulgar A.`

Preserve these as separate or unresolved hypotheses. Page 9 supports only document-level `Dario Arturo Pulgar`; it does not prove `Pulgar-Arriagada`, `Dario Jose`, `Dario J.`, or `Dario Pulgar A.` as variants.

Supporting evidence:

- Existing local context includes separate Pulgar-Arriagada and abbreviated `Dario Pulgar A.` mentions.
- The canonical `Darío Pulgar Arriagada` page currently supports only a narrow 2000 expropriation mention, not a CV identity bridge.

Conflicts and limits:

- Page 9 does not contain `Jose`, `J.`, `Arriagada`, `Pulgar-Arriagada`, `A.`, `Dr`, medical title, legal notice, passenger status, or property context.
- Merging by name alone risks conflating separate generations, professions, and source clusters.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.14 | Only broad Dario/Pulgar overlap exists for these clusters. |
| conflict_severity | 0.76 | Name-only merging could collapse distinct people and source contexts. |
| evidence_quality | 0.28 | Comparison context exists, but this page contributes no bridge. |
| conversion_confidence | 0.86 | Page 9 is readable; it lacks the needed variant-name evidence. |
| claim_probability | 0.12 | Low probability from this page. |
| relevance | 0.90 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.03 | Do not attach or merge. |

## Hypothesis 6: Relationship To Jose/Juana Parent Candidates

Jose/Juana candidates are checklist context only. Existing wiki context includes separate Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, and Juana de Dios Amagada de Pulgar clusters, but page 9 contains no Jose/Juana name or relationship statement.

Supporting evidence:

- The Pulgar-line instruction requires comparing Jose/Juana parent candidates when they appear in staged or existing context.
- Existing local pages contain Jose/Juana Pulgar-line candidates that may matter in a later lineage review.

Conflicts and limits:

- Page 9 names no Jose, Juana, parent, child, spouse, sibling, household, or birth-registration fact.
- Family-context hints justify only a targeted double-check, not a silent relationship correction or lineage attachment.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.06 | No direct identity or relationship bridge appears on page 9. |
| conflict_severity | 0.62 | Premature lineage attachment would create unsupported relationships. |
| evidence_quality | 0.20 | Related register clusters are separate and partly unresolved. |
| conversion_confidence | 0.42 | Jose/Juana readings have separate QA concerns; page 9 does not use them. |
| claim_probability | 0.05 | No Jose/Juana relationship claim is supported. |
| relevance | 0.64 | Relevant only because Pulgar-line comparison was requested. |
| canonical_readiness | 0.01 | No relationship action supported. |

## Conflicts

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`; evidence supports a possible match, not a merge.
- Duplicate-person risk: moderate for CV subject versus canonical Pulgar-Smith; high if merged by name alone with `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Darío J. Pulgar Arriagada`, `Dario Pulgar A.`, passenger clusters, or Jose/Juana line candidates.
- Name-variant conflict: page 9 supports only document-level `Dario Arturo Pulgar`; it does not prove `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, `Dario J.`, or `Dario Pulgar A.`.
- Relationship-conflict evidence: none on page 9. No Jose/Juana parent candidate, spouse, child, grandchild, or relationship to Alexander John Heinz is stated.
- Chronology-conflict evidence: none within page 9's 1954-1968 education sequence. The sequence is compatible with, but does not prove, the 1953 child passenger hypothesis. It does not fit the 1953 adult passenger as the same person without a major generational conflict.
- Conversion/provenance conflict: no page-content contradiction was observed for page 9, but staged id `a485f4030ce7` should be reconciled with the current chunk front matter id `c25ee050e822`.

## Ranked Hypotheses

| rank | hypothesis | probability | next proof-review or promotion step |
|---:|---|---:|---|
| 1 | Page 9 belongs to document-level CV subject `Dario Arturo Pulgar` | 0.86 | Keep as held CV-reported education/language evidence pending proof review. |
| 2 | Same broader person as staged CV/Habitat `Dario Pulgar` cluster | 0.62 | Compare only against proof-reviewed identity-bearing CV pages and stronger Habitat/Chile Films bridge evidence. |
| 3 | Same person as canonical `Dario Arturo Pulgar-Smith` | 0.58 | Require explicit identity bridge from `Pulgar` to `Pulgar-Smith`. |
| 4 | Same person as child passenger `Dario Pulgar`, age 11 in 1953 | 0.46 | Possible chronological fit; require passenger-to-CV bridge evidence. |
| 5 | Same as `Dario Jose Pulgar-Arriagada` / `Dario/Dario Pulgar Arriagada` / `Darío J. Pulgar Arriagada` / `Dario Pulgar A.` | 0.12 | Preserve separately or unresolved; do not merge by name alone. |
| 6 | Connected to Jose/Juana parent candidates | 0.05 | No relationship action from page 9; revisit only after lineage evidence appears. |

## Recommended Next Action

Keep `research/_staging/identity/ID-STAGE-CHUNK-a485f4030ce7-P0009-01-dario-cv-subject.md` on hold for canonical promotion. Do not merge people, rename canonical pages, promote page-9 facts, or attach page-9 education/language claims to `wiki/people/dario-arturo-pulgar-smith.md` yet.

Exact next proof-review step: run targeted CV identity proof review that reconciles the staged `CHUNK-a485f4030ce7-P0009-01` id with the current `CHUNK-c25ee050e822-P0009-01` chunk front matter, accepts or rejects the page-image/PDF QA closure for the education/language transcription, and reviews an identity-bearing CV title/cover/contact/signature page or other accepted local source that explicitly connects `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`. Only after that bridge is accepted should page-9 education and language entries be promoted as CV-reported facts. Keep separate anti-conflation checks for `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Darío J. Pulgar Arriagada`, `Dario Pulgar A.`, the 1953 adult/child Dario Pulgar passenger entries, and Jose/Juana parent candidates.
