---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/identity/ID-STAGE-CHUNK-a485f4030ce7-P0005-01-dario-cv-subject.md
worker: postconv-identity-analysis-20260524105955751
staged_draft: research/_staging/identity/ID-STAGE-CHUNK-a485f4030ce7-P0005-01-dario-cv-subject.md
source_path: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-a485f4030ce7-p0005-01-cv-dario-arturo-pulgar-work-history.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-a485f4030ce7-P0005-01
page_reference: page 5
canonical_candidate: wiki/people/dario-arturo-pulgar-smith.md
analysis_status: hold
canonical_readiness: hold
---

# Identity/Conflict Analysis: ID-STAGE-CHUNK-a485f4030ce7-P0005-01

## Blockers

- The exact staged draft reviewed here is `research/_staging/identity/ID-STAGE-CHUNK-a485f4030ce7-P0005-01-dario-cv-subject.md`.
- Page 5 is not independently identity-bearing. It does not print `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Smith`, `Arriagada`, `Jose`, `Juana`, or any family relationship.
- Attribution to `Dario Arturo Pulgar` is document-level context from the source title/path, staged draft, source packet, and chunk metadata, not a literal page-body reading.
- A provenance/content mismatch blocks canonical readiness: the assigned staged draft and source packet cite `CHUNK-a485f4030ce7-P0005-01`, and the current referenced chunk file contains 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries. The referenced converted file's page-5 section instead begins with 1999 PROFONANPE/TVE/Arca/Klohn/SNC Lavalin Agriculture entries.
- The chunk manifest for this converted file contains duplicate `CHUNK-a485f4030ce7-P0005-01` entries, both pointing to the same page-0005 chunk path but with different character counts and hashes. That must be audited before promotion.
- Existing parallel staged material for `CHUNK-3661a25ff4f5-P0005-01` supports the 1999 page-5 consulting sequence, while several page-8 analyses support the 1979-1982 HABITAT/NFB/Chile Films/CITELCO sequence. The assigned `a485f4030ce7` draft appears to mix page-5 identity metadata with page-8-like work-history content.
- The possible canonical page is `wiki/people/dario-arturo-pulgar-smith.md`, but this staged draft supports only the shorter document-level form `Dario Arturo Pulgar`. It does not prove that `Pulgar` and `Pulgar-Smith` are the same person or controlled variants.
- The canonical `Dario Arturo Pulgar-Smith` page explicitly warns that records mentioning `Dario`, `Pulgar`, `Pulgar-Arriagada`, or `Pulgar-Smith` should be attached only after identity review.
- No external research was performed. No raw source, converted Markdown, chunk, reviewed note, or canonical wiki page was edited.

## Hypothesis 1: Assigned Chunk Belongs To Document-Level CV Subject Dario Arturo Pulgar

Hypothesis: Despite the page/content mismatch, the assigned staged identity draft concerns a CV locally identified as `Dario Arturo Pulgar`.

Literal evidence:

- The staged draft names `candidate_identity: Dario Arturo Pulgar` and cites `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- The source packet records `source_identity: Dario Arturo Pulgar, from source title/file identity rather than page-body text`.
- The converted file title is `CV of Dario Arturo Pulgar pages 4-9`.
- The current referenced chunk file contains no competing personal name.

Interpretation:

- The narrow document-level identity is plausible because all local metadata points to a CV of Dario Arturo Pulgar.
- The claim must remain held because the assigned page/chunk evidence is internally unstable. It is not ready for proof promotion or canonical attachment.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.70 | Metadata consistently names the CV subject, but page-local identity is absent and provenance is conflicted. |
| conflict_severity | 0.62 | Content/page mismatch could attach the wrong occupational sequence to the wrong page reference. |
| evidence_quality | 0.50 | Useful local metadata exists, but the converted-file/chunk disagreement lowers reliability. |
| conversion_confidence | 0.45 | Text is legible, but the assigned chunk provenance and duplicate manifest entries require QA. |
| claim_probability | 0.72 | Probable that the broader document is Dario Arturo Pulgar's CV; not proved that this page content is correctly staged. |
| relevance | 0.96 | Directly relevant to the assigned staged draft. |
| canonical_readiness | 0.08 | Hold pending provenance audit, page-image QA, and identity bridge review. |

## Hypothesis 2: Page-5 Content Is The 1999 Consulting Sequence

Hypothesis: The authoritative page-5 content for the converted file is the 1999 consulting sequence shown in the converted page-5 section and in parallel `CHUNK-3661a25ff4f5-P0005-01` staging.

Literal evidence:

- The referenced converted file's page-5 section lists 1999 PROFONANPE, TVE in London, 1998-1999 Arca Consulting/European Commission in Lesotho, 1997-1998 Klohn Crippen Consultants in Huaraz, and SNC Lavalin Agriculture in Maracaibo.
- Parallel source packet `SP-STAGE-CHUNK-3661a25ff4f5-P0005-01-cv-dario-pulgar-page-5.md` describes the same 1999 page-5 sequence and says the final SNC Lavalin Agriculture entry continues beyond the page.
- The assigned staged draft says page 5 contains occupational entries but does not print the subject's name.

Interpretation:

- This hypothesis better fits the converted file's visible page-5 section and parallel page-5 staging.
- It does not resolve the assigned `a485f4030ce7` chunk conflict, so no fact should be promoted from this analysis alone.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.66 | The content remains document-level CV evidence, not page-local identity proof. |
| conflict_severity | 0.70 | Competing page-5 content creates a high citation/provenance risk. |
| evidence_quality | 0.58 | Converted file and parallel staging agree, but this task owns the `a485f4030ce7` draft. |
| conversion_confidence | 0.60 | The converted text reports no illegible words, but page-image proof review is still needed. |
| claim_probability | 0.64 | Plausible page-5 content, pending manifest/chunk audit. |
| relevance | 0.88 | Directly affects what the assigned page-5 identity draft can support. |
| canonical_readiness | 0.06 | Not ready. |

## Hypothesis 3: Assigned Chunk Content Is Actually Page-8-Like Work-History Evidence

Hypothesis: The assigned `a485f4030ce7` page-5 source packet/chunk is carrying the 1979-1982 HABITAT/NFB/Chile Films/CITELCO sequence that other local analyses treat as page-8 work-history evidence.

Literal evidence:

- The assigned source packet quotes 1979-1982 United Nations Centre for Human Settlements (HABITAT), 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries.
- The current referenced chunk file contains the same 1979-1982 through 1970-1972 sequence and ends with `EDUCATION`.
- Existing reviewed/staged page-8 context elsewhere in the workspace treats this same sequence as the visible page supporting HABITAT, NFB, Chile Films, and CITELCO work-history evidence.
- The assigned draft does not itself cite page 8; it labels the evidence as page 5.

Interpretation:

- The occupational sequence is highly relevant to Dario Pulgar identity research because it overlaps Habitat/NFB/Chile Films context.
- For this exact staged draft, it is a blocker rather than a promotable claim, because the page reference and chunk provenance are not stable.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.72 | The work-history sequence fits the broader Dario Arturo Pulgar CV cluster, but not the assigned page reference. |
| conflict_severity | 0.78 | Misnumbered page/chunk evidence could corrupt downstream citations. |
| evidence_quality | 0.54 | Strong internal text, weak provenance control for this assigned draft. |
| conversion_confidence | 0.50 | Other reviews support the sequence visually, but this task did not perform image reread and the assigned page conflicts. |
| claim_probability | 0.68 | Probable that the sequence is real CV content; uncertain as `P0005-01` evidence. |
| relevance | 0.92 | Relevant to both Dario identity and the required conflict analysis. |
| canonical_readiness | 0.05 | Do not promote from this staged draft. |

## Hypothesis 4: Same Person As Canonical Dario Arturo Pulgar-Smith

Hypothesis: The document-level CV subject `Dario Arturo Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith`, with the CV using a shortened surname form.

Literal evidence:

- The staged draft lists `wiki/people/dario-arturo-pulgar-smith.md` as the possible canonical match.
- The canonical page's preferred name is `Dario Arturo Pulgar-Smith`, based on family-supplied knowledge.
- The name elements `Dario Arturo` and `Pulgar` align between the CV source title and the canonical page.
- The assigned page does not state `Smith`, `Pulgar-Smith`, Alexander John Heinz, parentage, spouse, children, or any family relationship.

Interpretation:

- Same-person identity is plausible but unproved from this staged draft.
- Family context justifies a targeted proof-review step. It does not justify silently normalizing `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.60 | Meaningful name overlap, but no page-local or relationship bridge. |
| conflict_severity | 0.46 | Incorrect attachment would misattribute CV work-history claims to the canonical person. |
| evidence_quality | 0.52 | Evidence is name overlap plus family-supplied canonical context. |
| conversion_confidence | 0.45 | Conversion/provenance problems do not resolve the name-variant question. |
| claim_probability | 0.58 | Plausible but not demonstrated here. |
| relevance | 0.96 | This is the nominated canonical match. |
| canonical_readiness | 0.04 | Not ready for attachment, merge, rename, or fact promotion. |

## Hypothesis 5: Same Broader Work-History Cluster As Staged Dario Pulgar Evidence

Hypothesis: The CV subject belongs to the same broader staged work-history cluster as local records naming `Dario Pulgar` in Habitat, Chile Films, NFB, and communications/media contexts.

Literal evidence:

- The assigned source packet/chunk content, if accepted after provenance QA, gives a sequence including HABITAT, National Film Board of Canada, Chile Films, and CITELCO.
- Existing staged Habitat/memoir task context names `Dario Pulgar` in Chilean/Canadian and communications/media settings, with page-reference and identity holds.
- Existing page-8 analyses rank the HABITAT/NFB/Chile Films/CITELCO sequence as a strong work-history overlap but still require an identity-bearing CV page and proof-reviewed bridge.
- The assigned staged draft does not itself include a page-body name or family bridge.

Interpretation:

- The broader cluster comparison is promising, especially if page provenance is corrected.
- It is not a canonical identity proof. The current `a485f4030ce7` page-5 conflict makes it unsuitable as the next bridge source.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.62 | Work-history overlap is useful but depends on resolving the page/chunk mismatch. |
| conflict_severity | 0.54 | Overusing held cluster evidence could collapse separate Dario Pulgar references. |
| evidence_quality | 0.50 | Relies on staged and reviewed local context with outstanding QA. |
| conversion_confidence | 0.46 | Assigned chunk provenance is conflicted. |
| claim_probability | 0.60 | Plausible as a broader work-history cluster, held. |
| relevance | 0.84 | Useful for later identity resolution. |
| canonical_readiness | 0.05 | Hold. |

## Hypothesis 6: Same Person As Child Passenger Dario Pulgar, Age 11 In 1953

Hypothesis: The CV subject may be the same person as canonical stub `Dario Pulgar (child passenger, age 11)`.

Literal evidence:

- `wiki/people/dario-pulgar-child-passenger-age-11.md` records a `Dario Pulgar` child passenger aged 11 on 1953-08-07, listed as a student, citizen or subject of Chile by ditto mark, with last permanent residence England and intended future permanent residence Chile.
- The CV source title uses `Dario Arturo Pulgar`.
- This assigned staged draft gives no age, birth date, parents, passenger-list data, school linkage, or `Smith` surname.

Interpretation:

- The comparison remains possible on name and chronology only.
- It is not a bridge. The passenger stub does not provide `Arturo`, `Smith`, parentage, or direct CV linkage.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.44 | Compatible same-name/chronology context only. |
| conflict_severity | 0.42 | A premature merge would collapse passenger and CV identities without proof. |
| evidence_quality | 0.48 | Useful local anti-conflation context, but indirect. |
| conversion_confidence | 0.50 | Both clusters have separate limitations; this assigned draft is provenance-held. |
| claim_probability | 0.42 | Possible, not ready. |
| relevance | 0.66 | Relevant same-name comparison. |
| canonical_readiness | 0.02 | No merge or attachment supported. |

## Hypothesis 7: Same Person As Dario Jose Pulgar-Arriagada / Dario J. Pulgar Arriagada / Dario Pulgar Arriagada / Dario Pulgar A.

Hypothesis: The CV subject `Dario Arturo Pulgar` is the same person as older or separate Pulgar-Arriagada clusters, including `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`.

Literal evidence:

- Existing Pulgar-line context contains separate or unresolved candidates using `Dario`, `Pulgar`, and `Arriagada` name forms, including `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, canonical `Dario Pulgar Arriagada`, and `Dario Pulgar A.`.
- `wiki/people/dar-o-pulgar-arriagada.md` records a narrow 2000-12-05 expropriation event naming `Dario Pulgar Arriagada`.
- Existing passenger-list context elsewhere distinguishes an adult `Dario Pulgar` aged 64 in 1953 from a child `Dario Pulgar` aged 11.
- The assigned page does not state `Jose`, `J.`, `Arriagada`, `Pulgar A.`, physician/surgeon, Health Service captain, Geneva, passenger data, expropriation, property, or parentage.

Interpretation:

- Name overlap alone is insufficient and potentially misleading.
- Older medical/Geneva/adult passenger/Arriagada contexts appear to be separate or unresolved clusters, not proved variants of the CV subject.
- The 2000 `Dario Pulgar Arriagada` expropriation notice remains a weak possible name-variant question only.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.12 | Only broad Dario/Pulgar overlap appears. |
| conflict_severity | 0.78 | Name-only merging could collapse distinct generations, professions, and source clusters. |
| evidence_quality | 0.44 | Compared Pulgar-Arriagada evidence is sparse or metadata-dependent. |
| conversion_confidence | 0.42 | Several compared clusters have unresolved image/provenance QA. |
| claim_probability | 0.10 | Low probability from this staged draft. |
| relevance | 0.90 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.01 | Do not attach or merge. |

## Hypothesis 8: Relationship To Jose/Juana Parent Candidates

Hypothesis: Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, Juana de Dios Amagada de Pulgar, or related Jose/Juana candidates may connect the CV subject to the broader Pulgar line.

Literal evidence:

- Existing canonical stubs include `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` are tied to a separate register-derived parent/child cluster.
- `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` are tied to a separate child-parent cluster for `Tulio Cesar Luis Jose`.
- The assigned page names no Jose or Juana candidate and gives no parent, child, spouse, household, birth-register, or lineage statement.

Interpretation:

- Jose/Juana candidates are checklist context only. This page supports no relationship, descent, parentage, or household claim.
- No kinship should be inferred from surname context or from the existence of Pulgar-line canonical stubs.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.06 | No direct identity or relationship bridge appears here. |
| conflict_severity | 0.62 | Premature lineage attachment could create unsupported relationships. |
| evidence_quality | 0.40 | Related register clusters are separate and not cited by this draft. |
| conversion_confidence | 0.38 | Jose/Juana readings have separate QA concerns; this page does not use them. |
| claim_probability | 0.06 | No Jose/Juana relationship is supported here. |
| relevance | 0.62 | Relevant only as required Pulgar-line context. |
| canonical_readiness | 0.01 | No relationship action supported. |

## Conflicts

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: moderate for CV `Dario Arturo Pulgar` versus canonical `Dario Arturo Pulgar-Smith`; high if merged by name alone with `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, `Dario Pulgar Arriagada`, `Dario Pulgar A.`, adult/child `Dario Pulgar` passenger clusters, or Jose/Juana candidates.
- Name-variant conflict: this staged draft supports only document-level `Dario Arturo Pulgar`; it does not prove `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, `Dario J.`, or `Dario Pulgar A.` as variants.
- Relationship-conflict evidence: none in the assigned staged draft. It does not state parents, spouse, child, grandchild, or relationship to Alexander John Heinz.
- Chronology-conflict evidence: no chronology conflict is proved within the CV subject hypothesis. Cross-cluster chronology cautions against merging the CV subject with older medical/Geneva/1953 adult passenger/Arriagada clusters by name alone.
- Conversion/provenance conflict: the assigned `a485f4030ce7` page-5 draft has an unresolved content mismatch between the source packet/chunk and the referenced converted file page-5 section, plus duplicate `P0005-01` manifest entries.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | Assigned evidence belongs somewhere in the document-level CV for `Dario Arturo Pulgar` | 0.72 | Hold as document-level context only; audit provenance before claim review. |
| 2 | Assigned chunk content is page-8-like HABITAT/NFB/Chile Films/CITELCO evidence | 0.68 | Reconcile page/chunk metadata against rendered page images and existing page-8 reviews. |
| 3 | Page-5 content is the 1999 consulting sequence | 0.64 | Compare converted page-5 section, parallel `3661a25ff4f5` staging, chunk manifest, and page image. |
| 4 | Same broader CV/Habitat work-history cluster as staged `Dario Pulgar` evidence | 0.60 | Revisit after page provenance and proof-reviewed Habitat/CV bridge evidence. |
| 5 | Same person as canonical `Dario Arturo Pulgar-Smith` | 0.58 | Require explicit proof-reviewed bridge from `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`. |
| 6 | Same person as child passenger `Dario Pulgar`, age 11 in 1953 | 0.42 | Require passenger-to-CV bridge evidence, not chronology alone. |
| 7 | Same as `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada` / `Dario/Dario Pulgar Arriagada` / `Dario Pulgar Arriagada` / `Dario Pulgar A.` | 0.10 | Preserve separately or unresolved; do not merge by name alone. |
| 8 | Connected to Jose/Juana parent candidates | 0.06 | No action from this page; revisit only if lineage evidence appears in a proof-reviewed source. |

## Recommended Next Action

Keep `research/_staging/identity/ID-STAGE-CHUNK-a485f4030ce7-P0005-01-dario-cv-subject.md` on hold. Do not merge people, rename canonical pages, promote page-5 facts, or attach these claims to `wiki/people/dario-arturo-pulgar-smith.md`.

Exact next proof-review step: perform a provenance-first CV review for `CHUNK-a485f4030ce7-P0005-01`. Compare the rendered page image, converted file page-5 section, current chunk file, chunk manifest duplicate entries, and parallel page-5/page-8 staged notes to decide whether this staged draft is a true page-5 identity draft, a duplicate/misnumbered page-8 work-history draft, or a stale chunk artifact. Only after the page/chunk conflict is resolved should a targeted CV identity review attempt to bridge document-level `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`. Preserve separate anti-conflation checks for `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, `Dario Pulgar Arriagada`, `Dario Pulgar A.`, adult/child Dario passenger clusters, and Jose/Juana parent candidates.
