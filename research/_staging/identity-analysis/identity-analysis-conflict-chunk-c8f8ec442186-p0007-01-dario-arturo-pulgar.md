---
type: identity_conflict_analysis
status: complete
role: identity_researcher
worker: postconv-identity-analysis-20260524020034290
task_id: "identity-analysis:research/_staging/conflicts/chunk-c8f8ec442186-p0007-01-no-conflict-candidate.md"
staged_draft: "research/_staging/conflicts/chunk-c8f8ec442186-p0007-01-no-conflict-candidate.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-c8f8ec442186-p0007-01-no-conflict-candidate.md"
source_packet: "research/_staging/source-packets/chunk-c8f8ec442186-p0007-01-cv-dario-arturo-pulgar.md"
source_path: "raw/sources/CV of Dario Arturo Pulgar.pdf"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0007-chunk-01.md"
chunk_id: "CHUNK-c8f8ec442186-P0007-01"
page_reference: "page 7"
canonical_candidate: "wiki/people/dario-arturo-pulgar-smith.md"
analysis_status: hold
canonical_readiness: hold_for_identity_bridge
---

# Identity/Conflict Analysis: CHUNK-c8f8ec442186-P0007-01

## Blockers

- The exact staged draft analyzed here is `research/_staging/conflicts/chunk-c8f8ec442186-p0007-01-no-conflict-candidate.md`.
- Page 7 does not repeat the subject's personal name in the page body. The `Dario Arturo Pulgar` attribution comes from source title/path, source-packet metadata, and document context.
- Page 7 contains occupational chronology only. It does not state `Pulgar-Smith`, `Smith`, `Dario Jose`, `Dario J.`, `Pulgar-Arriagada`, `Pulgar A.`, parentage, spouse, child, grandchild, or any relationship to Alexander John Heinz.
- The opening paragraph is a continuation from page 6. It should not be promoted as a standalone page-7 activity claim until the adjacent page is reviewed with it.
- The conflict draft correctly reports no internal page conflict, but that is narrower than canonical readiness. It does not resolve the identity bridge from `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`.
- Existing canonical `Dario Arturo Pulgar-Smith` is family-supplied and explicitly warns that Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records should be attached only after identity review.
- Pulgar-Arriagada, Pulgar A., adult passenger, child passenger, and Jose/Juana parent-candidate clusters remain separate unless a proof-reviewed source explicitly bridges them.

## Literal Source Reading

The page-7 chunk literally transcribes a continuation paragraph followed by employment entries:

```text
1988-1989
Food and Agriculture Organisation of the United Nations (FAO)
Ndola, Zambia
Training and Communication Advisor
```

```text
1988
Canadian International Development Agency (CIDA)
Ethiopia
Communication Consultant
```

```text
1986 - 1987
Worldview International Foundation (WIF)
Rome, Italy
Rural Communications and Extension Advisor
```

```text
1982-1985
Independent communications consultant
Canadian International Development Agency
```

Literal reading: page 7 is a typed CV page with employment chronology entries. The literal page body does not name a person or state a family relationship.

Interpretation kept separate: local source metadata identifies the document as `CV of Dario Arturo Pulgar`, so the entries are probably CV-reported occupational evidence for that document-level subject. The page itself does not prove that this subject is canonical `Dario Arturo Pulgar-Smith`.

## Hypothesis 1: Page 7 Belongs To Document-Level CV Subject Dario Arturo Pulgar

Supporting evidence:

- The staged conflict draft names the subject `Dario Arturo Pulgar`.
- The source packet records `extracted_subject: Dario Arturo Pulgar` and cites `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- The converted file and chunk both belong to the same CV page range for `CV of Dario Arturo Pulgar`.
- The page body has no competing personal name.
- The occupational sequence is internally coherent for 1982-1989, with only the opening page-continuation paragraph requiring page-6 context.

Conflicts and limits:

- The page body is unnamed.
- This source is a CV, so the evidence is self-reported or document-reported occupational history, not independent proof of identity or kinship.
- This hypothesis does not resolve surname variants.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.84 | Source title/path, source packet, conflict draft, and chunk context align on `Dario Arturo Pulgar`; page body is unnamed. |
| conflict_severity | 0.18 | No internal chronology or name conflict on page 7 if kept at document level. |
| evidence_quality | 0.72 | Direct staged/converted CV evidence, but identity comes from document context rather than page-local text. |
| conversion_confidence | 0.82 | Typed text is complete in the chunk and the page image/source PDF are present in this workspace; no new conversion was performed. |
| claim_probability | 0.86 | Probable that the entries belong to the CV's document-level subject. |
| relevance | 1.00 | Directly answers the assigned staged conflict draft. |
| canonical_readiness | 0.40 | Hold because canonical identity bridge and page-6 continuation review remain required. |

## Hypothesis 2: Same Person As Canonical Dario Arturo Pulgar-Smith

Supporting evidence:

- The canonical page is `wiki/people/dario-arturo-pulgar-smith.md`.
- The canonical preferred name `Dario Arturo Pulgar-Smith` shares the distinctive given-name pair `Dario Arturo` and surname element `Pulgar` with the CV title.
- The canonical page identifies this person, from family-supplied knowledge, as Alexander John Heinz's maternal grandfather.
- Existing local CV identity analyses treat the CV subject as a plausible but held candidate for this canonical person.

Conflicts and limits:

- Page 7 does not state `Smith` or `Pulgar-Smith`.
- Page 7 does not state a relationship to Alexander John Heinz or any other family member.
- Name overlap and family context are not enough to silently normalize `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.64 | Strong name overlap with the family-supplied canonical person, but no page-7 bridge to `Smith`. |
| conflict_severity | 0.44 | Incorrect attachment would place CV occupational history on the wrong canonical person. |
| evidence_quality | 0.58 | Evidence is document-level name overlap plus family-supplied canonical context. |
| conversion_confidence | 0.82 | Transcription confidence does not solve the surname-variant question. |
| claim_probability | 0.64 | Plausible, not proved by this page. |
| relevance | 0.96 | This is the main canonical candidate for the CV cluster. |
| canonical_readiness | 0.24 | Hold for targeted identity bridge proof review. |

## Hypothesis 3: Same Broader Person As The Staged CV/Habitat Dario Pulgar Cluster

Supporting evidence:

- Page 7 is part of the same CV work-history sequence as adjacent pages that include international development, communications, Canada, Chile, and Habitat-related occupational context.
- Other staged identity notes for nearby CV pages preserve the same document-level `Dario Arturo Pulgar` cluster while holding canonical attachment.
- Separate reviewed Habitat/memoir notes name `Dario Pulgar` in a Chile/Canada communications context, but those notes also keep identity linkage on review.

Conflicts and limits:

- Page 7 itself does not mention Habitat, Chile Films, National Film Board of Canada, exile, Canada residence, `Arturo`, or `Pulgar-Smith`.
- Cross-source cluster comparison should use proof-reviewed identity-bearing pages, not this unnamed page alone.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Compatible occupational context, but this page is not identity-bearing. |
| conflict_severity | 0.34 | Low internal conflict; moderate risk if held Habitat/CV evidence is overused. |
| evidence_quality | 0.56 | Local staged evidence is relevant but partly indirect. |
| conversion_confidence | 0.78 | Page text is usable; cross-source identity still needs proof review. |
| claim_probability | 0.62 | Plausible broader cluster membership. |
| relevance | 0.84 | Useful context for later CV identity resolution. |
| canonical_readiness | 0.20 | Hold. |

## Hypothesis 4: Same Person As Child Passenger Dario Pulgar, Age 11 In 1953

Supporting evidence:

- The canonical child-passenger stub records `Dario Pulgar`, age 11, traveling on 1953-08-07.
- Adjacent CV page-9 context in local staging records education beginning in 1954, which is chronologically compatible with an age-11 passenger in 1953.
- The shared name element is `Dario Pulgar`.

Conflicts and limits:

- Page 7 gives no age, birth date, school, passenger-list context, parents, or `Smith`.
- The child-passenger cluster does not by itself supply `Arturo`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Chronology is compatible, but the bridge is indirect and outside page 7. |
| conflict_severity | 0.42 | Premature merge could collapse passenger and CV identities. |
| evidence_quality | 0.52 | Local evidence is useful but not directly connected by this page. |
| conversion_confidence | 0.70 | Both clusters have readable staged evidence with separate proof-review limits. |
| claim_probability | 0.46 | Possible, not ready. |
| relevance | 0.68 | Relevant anti-conflation check. |
| canonical_readiness | 0.10 | No merge or attachment supported. |

## Hypothesis 5: Same Person As Dario Arturo Pulgar-Smith Versus Adult Passenger Dario Pulgar, Age 64

Supporting evidence:

- The adult passenger stub records a `Dario Pulgar`, age 64, in 1953.
- The name element `Dario Pulgar` overlaps with the CV title.

Conflicts and limits:

- Age 64 in 1953 would imply a birth around 1888-1889 and an age around 93-101 during the page-7 CV roles from 1982-1989, which is a serious chronology conflict for an active international communications career.
- The adult passenger cluster is more compatible with older medical/Pulgar A. candidates than with the later CV/Habitat Dario cluster.
- Page 7 does not state any medical occupation or passenger-list context.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Shared name only, with a severe age/career chronology conflict. |
| conflict_severity | 0.88 | A merge would likely create a major chronology error. |
| evidence_quality | 0.46 | Passenger and CV evidence each support their own narrow claims, not the bridge. |
| conversion_confidence | 0.70 | Conversion confidence does not overcome chronology. |
| claim_probability | 0.06 | Unlikely on current local evidence. |
| relevance | 0.66 | Relevant as an anti-conflation candidate. |
| canonical_readiness | 0.01 | Do not attach or merge. |

## Hypothesis 6: Same Person As Dario Jose Pulgar-Arriagada / Dario J. Pulgar Arriagada / Dario Pulgar-Arriagada / Dario Pulgar A.

Supporting evidence:

- Local staged context contains `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dario Pulgar-Arriagada`, and `Dario Pulgar A.` clusters.
- The forms share `Dario/Darío Pulgar`.
- Some older Pulgar-Arriagada/Pulgar A. materials include medical or public-role context.

Conflicts and limits:

- Page 7 supports `Dario Arturo Pulgar` only by document title and does not mention `Jose`, `J.`, `Arriagada`, `A.`, medical title, service captain, Geneva/ICRC context, property/expropriation context, age, or parents.
- `Dario Pulgar A.`, age 39 in 1928, is chronologically and occupationally a better candidate for older medical/Pulgar-Arriagada comparisons than for the later CV communications career.
- The ICRC/title-derived `Dario Jose Pulgar-Arriagada` materials and other Pulgar-Arriagada tasks require their own proof-review or identity-bridge work.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.13 | Only broad name overlap; middle names, surnames, occupations, and chronology are unbridged or adverse. |
| conflict_severity | 0.78 | Name-only merging could collapse distinct generations and professional clusters. |
| evidence_quality | 0.44 | Compared evidence is local but mostly separate, staged, or held. |
| conversion_confidence | 0.58 | Several compared clusters have conversion or metadata holds. |
| claim_probability | 0.10 | Low from this page. |
| relevance | 0.92 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.03 | Preserve separately; no merge. |

## Hypothesis 7: Relationship To Jose/Juana Parent Candidates

Supporting evidence:

- Existing local context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- These names are relevant Pulgar-line checklist candidates in other staged register and relationship materials.

Conflicts and limits:

- Page 7 does not name Jose, Juana, a parent, spouse, child, household, grandchild, or any family relationship.
- Existing Jose/Juana candidates are themselves tied to separate draft or probable relationship clusters with conversion-sensitive readings.
- Surname context can justify future double-checking, but not a lineage claim.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | No direct relationship or same-person evidence appears on page 7. |
| conflict_severity | 0.62 | Unsupported lineage attachment would create relationship conflicts. |
| evidence_quality | 0.36 | Parent-candidate evidence is separate and not connected to this CV page. |
| conversion_confidence | 0.44 | Jose/Juana readings carry separate conversion cautions. |
| claim_probability | 0.04 | Page 7 supports no Jose/Juana relationship. |
| relevance | 0.60 | Relevant only as required anti-conflation context. |
| canonical_readiness | 0.01 | No relationship action supported. |

## Conflicts

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: moderate between CV `Dario Arturo Pulgar` and canonical Pulgar-Smith until a surname bridge is reviewed; high if the CV subject is merged by name alone with `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Pulgar A.`, or the 1953 adult passenger.
- Name-variant conflict: page 7 supports only document-level `Dario Arturo Pulgar`; it does not prove variants `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, `Dario J.`, or `Dario Pulgar A.`.
- Relationship-conflict evidence: none on page 7. No parent, spouse, child, grandchild, or Jose/Juana relationship is stated.
- Chronology-conflict evidence: none within the page-7 occupational sequence. Cross-cluster chronology argues strongly against merging this CV subject with the 1953 adult age-64 passenger or older medical/Pulgar A. clusters without a vital-date bridge.
- Conversion/provenance conflict: no internal transcription conflict was identified for the page-7 entries, but the opening continuation fragment requires page-6 context before promotion.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | Page 7 belongs to document-level CV subject `Dario Arturo Pulgar` | 0.86 | Keep as held CV occupational evidence; proof-review page text and page-6 continuation before promotion. |
| 2 | Same person as canonical `Dario Arturo Pulgar-Smith` | 0.64 | Hold for explicit identity bridge proving the `Pulgar`/`Pulgar-Smith` surname relationship. |
| 3 | Same broader staged CV/Habitat `Dario Pulgar` cluster | 0.62 | Compare against proof-reviewed identity-bearing CV and Habitat/Chile Films evidence. |
| 4 | Same person as child passenger `Dario Pulgar`, age 11 in 1953 | 0.46 | Possible chronology; requires targeted passenger/CV identity proof review. |
| 5 | Same as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar-Arriagada`, or `Dario Pulgar A.` | 0.10 | Preserve as separate hypotheses; do not merge by name alone. |
| 6 | Same as adult passenger `Dario Pulgar`, age 64 in 1953 | 0.06 | Treat as anti-conflation due to severe age/career chronology conflict. |
| 7 | Connected to Jose/Juana parent candidates | 0.04 | No relationship action from page 7. |

## Recommended Next Action

Keep `research/_staging/conflicts/chunk-c8f8ec442186-p0007-01-no-conflict-candidate.md` in hold/do-not-promote status for canonical purposes. Do not merge people, rename canonical pages, promote page-7 facts, or attach these occupational claims to `wiki/people/dario-arturo-pulgar-smith.md` yet.

The exact next proof-review step is a targeted CV identity bridge review: verify the CV identity-bearing pages/title and page-7 image against `raw/sources/CV of Dario Arturo Pulgar.pdf`, reconcile the page-7 opening continuation with page 6, and determine whether a proof-reviewed source explicitly links `Dario Arturo Pulgar` in this CV to canonical `Dario Arturo Pulgar-Smith`. Only after that bridge is accepted should page-7 occupational entries be promoted as CV-reported facts. Keep separate anti-conflation checks for `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Pulgar A.`, the 1953 adult and child passenger candidates, and Jose/Juana parent candidates.
