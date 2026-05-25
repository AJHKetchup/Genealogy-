---
type: identity_conflict_analysis
status: draft
task_id: identity-analysis:research/_staging/conflicts/chunk-dceaf19e5117-p0008-01-metadata-and-identity-hold.md
worker: postconv-identity-analysis-20260525004316060
role: identity_researcher
staged_draft: research/_staging/conflicts/chunk-dceaf19e5117-p0008-01-metadata-and-identity-hold.md
source_packet: research/_staging/source-packets/chunk-dceaf19e5117-p0008-01-cv-dario-arturo-pulgar-work-history.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
referenced_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0008-chunk-01.md
canonical_candidate: wiki/people/dario-arturo-pulgar-smith.md
canonical_readiness: hold_for_conversion_qa_and_identity_bridge
---

# Identity And Conflict Analysis: CV Page 8 Metadata And Identity Hold

## Blockers First

1. The staged draft under review is `research/_staging/conflicts/chunk-dceaf19e5117-p0008-01-metadata-and-identity-hold.md`. It references chunk id `CHUNK-dceaf19e5117-P0008-01` and chunk path `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0008-chunk-01.md`, but that page-8 chunk file is currently absent from `raw/chunks`.
2. The current chunk manifest does not list a page-8 chunk. It lists pages 4, 5, 6, 7, another page 5 entry, and page 9; no `P0008` entry is present.
3. Provenance hashes disagree across the staged draft/source packet, current manifest, and live file state. The staged draft/source packet cite converted SHA `dceaf19e511728a6cacce6d03293232ed56641d0485aa2eabf44020e36edc942`; the current chunk manifest cites `b2e036516c17cf6c253a84554ca9fccd71944e51ff46121a8549b9ec6904a7a3`; a live SHA256 check of the converted file on 2026-05-25 returns `4CA8AFB8A1237D8C8955315996E4B5B25EC20EF3A7F99E38F6D43B09F3064CDE`.
4. Page 8 itself, as represented in the converted file, does not print `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Pulgar-Smith`, `Dario Jose`, `Pulgar-Arriagada`, `Jose`, `Juana`, a parent, spouse, child, grandchild, birth, death, or other family relationship.
5. The canonical page `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns not to automatically attach records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith without identity review.

## Literal Source Readings

From the assembled converted file for page 8, the literal work-history sequence includes:

- `1979 - 1982`, `United Nations Centre for Human Settlements (HABITAT)`, `Nairobi, Kenya`, `Development Support Communications Officer`.
- `1974 - 1978`, `National Film Board of Canada (NFB)`, `Montreal, Canada`, `Audio Visual Consultant`.
- `1972 - 1973`, `Chile Films`, `Santiago, Chile`, `General Manager Distribution and Exhibition, Head of International Department`.
- `1970 - 1972`, `Cine, Televisión y Comunicaciones (CITELCO)`, `Santiago, Chile`, `Producer`.

The converted file's document heading and page metadata identify the source as `CV of Dario Arturo Pulgar` / `raw/sources/CV of Dario Arturo Pulgar.pdf`. That is document-level context, not a page-body name reading.

## Interpretation Kept Separate

The best interpretation is narrow: page 8 probably belongs to a locally titled CV for `Dario Arturo Pulgar` and reports work-history entries for the CV subject. This is not the same as proof that the page body names him, and it is not proof that `Dario Arturo Pulgar` is the canonical `Dario Arturo Pulgar-Smith`.

Because the page-8 chunk is missing from the current chunk set and the derivative hashes disagree, canonical promotion should remain blocked even before the surname/identity bridge question is reached.

## Hypothesis 1: Page 8 Belongs To The Document-Level CV Subject `Dario Arturo Pulgar`

Evidence supporting:

- The source packet title, source path, converted file title, and converted-file page metadata all identify the larger source as `CV of Dario Arturo Pulgar`.
- The page-8 content is a continuous CV work-history page consistent with adjacent CV pages in the same converted file.
- The work-history sequence is internally coherent from 1970 through 1982 and contains no page-local contradiction.

Evidence against or limiting:

- Page 8 does not independently name the subject in body text.
- The currently referenced page-8 chunk is absent, and the current manifest does not include a page-8 chunk entry.
- Hash/id disagreement prevents treating the staged derivative as clean provenance.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.68 | Probable document-level attribution to `Dario Arturo Pulgar`, weakened by missing current chunk and no page-local name. |
| evidence_quality | 0.62 | Converted page text is coherent, but provenance is not clean. |
| conversion_confidence | 0.35 | Current page-8 chunk is absent and hashes disagree; the assembled converted file still has page-8 text. |
| claim_probability | 0.72 | Page 8 probably reports the CV subject's work history, but promotion must wait. |
| relevance | 0.88 | High relevance to the Pulgar CV/career cluster. |
| conflict_severity | 0.72 | High enough to block promotion because the issue is provenance plus identity bridge. |
| canonical_readiness | 0.20 | Hold for conversion QA and identity bridge. |

## Hypothesis 2: `Dario Arturo Pulgar` Is The Same Person As Canonical `Dario Arturo Pulgar-Smith`

Evidence supporting:

- The name `Dario Arturo Pulgar` overlaps strongly with canonical `Dario Arturo Pulgar-Smith`.
- The canonical page represents a family-supplied person whose preferred name includes all three document-level elements plus `Smith`.
- Local CV and Habitat-related staged work suggests a modern professional Dario Pulgar cluster, but page 8 alone does not prove that bridge.

Evidence against or limiting:

- Page 8 does not print `Smith` or any relationship to Alexander John Heinz.
- The canonical page is family-supplied and warns against automatic attachment of Dario/Pulgar records.
- No reviewed identity-bearing CV title page, biographical page, family source, or accepted bridge is cited in this staged draft.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Plausible but unproved surname/identity bridge. |
| evidence_quality | 0.42 | Relies on name overlap and family-supplied canonical context, not page-8 direct evidence. |
| conversion_confidence | 0.35 | Same provenance blocker applies. |
| claim_probability | 0.45 | Possible same person; not promotion-ready. |
| relevance | 0.82 | Directly relevant to the intended canonical candidate. |
| conflict_severity | 0.65 | Moderate-high duplicate-person/name-variant risk if promoted prematurely. |
| canonical_readiness | 0.15 | Do not attach page-8 facts to the canonical page yet. |

## Hypothesis 3: Same Person As `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, Or Canonical `Darío Pulgar Arriagada`

Evidence supporting:

- Local staged and wiki context contains multiple Dario/Pulgar-Arriagada clusters, including `Darío J. Pulgar Arriagada` as a 1918 medical-title recipient, `Dario Pulgar-Arriagada` as a Chilean health-service captain in convention-listing context, `Dario Jose Pulgar-Arriagada` in photo/source-title contexts, and canonical `Darío Pulgar Arriagada` in a 2000 expropriation notice.
- Shared given name and Pulgar surname justify a double-check in Pulgar-line review.

Evidence against or limiting:

- Page 8 says none of `Jose`, `J.`, `Arriagada`, `Pulgar-Arriagada`, `Dr`, `Médico-Cirujano`, medical title, health-service captain, Geneva Convention, expropriation, or property context.
- The page-8 CV work-history cluster is communications/film/Habitat work from 1970-1982, not medical/health-service evidence.
- Existing local notes repeatedly warn not to merge Pulgar-Arriagada clusters by name alone.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Name overlap only; no direct bridge from page 8. |
| evidence_quality | 0.30 | Compared context is local but from different source clusters and scopes. |
| conversion_confidence | 0.35 | Page-8 provenance remains unsettled. |
| claim_probability | 0.10 | Low probability from this evidence set. |
| relevance | 0.55 | Relevant as an anti-conflation check, not as a supported merge. |
| conflict_severity | 0.78 | High conflation risk if merged by name alone. |
| canonical_readiness | 0.05 | Preserve separately or unresolved. |

## Hypothesis 4: Same Person As Passenger-List `Dario Pulgar` Candidates

Evidence supporting:

- Existing canonical stubs include `Dario Pulgar (adult passenger, age 64)` and `Dario Pulgar (child passenger, age 11)`, both from a 7 August 1953 passenger-list cluster.
- The child passenger age 11 in 1953 could be chronologically plausible for a person in his twenties during early-1970s Chile Films/Habitat-related narratives, but page 8 does not state age, birth year, family, travel, or passenger-list details.

Evidence against or limiting:

- Page 8 gives no passenger event, age, ship, residence, citizenship, family group, or travel clue.
- The adult age-64 candidate is chronologically and occupationally unlikely to be the CV subject if the CV subject held early-career film roles in 1970-1973.
- No identity bridge connects either passenger candidate to `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or the page-8 CV work history.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Child-passenger chronology is worth later review, but page 8 supplies no bridge. |
| evidence_quality | 0.38 | Passenger stubs are local canonical context; no direct page-8 relationship. |
| conversion_confidence | 0.35 | Page-8 provenance remains unsettled. |
| claim_probability | 0.16 | Low from this evidence set. |
| relevance | 0.45 | Useful duplicate-person check only. |
| conflict_severity | 0.60 | Moderate risk if a name-only merge is made. |
| canonical_readiness | 0.05 | Do not merge or attach. |

## Hypothesis 5: Page 8 Supports Jose/Juana Parent Candidate Or Relationship Claims

Evidence supporting:

- Local canonical context includes `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar` parent/child or candidate-family clusters.
- The Pulgar-line surname overlap makes these relevant to anti-conflation review.

Evidence against or limiting:

- Page 8 contains no `Jose`, `Juana`, parent, spouse, child, grandchild, birth, household, or civil-registration language.
- The Jose/Juana contexts are separate birth-registration or family-link clusters and cannot be inferred from a CV employment page.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | No page-8 identity support for these candidates. |
| evidence_quality | 0.25 | Local context exists but is unrelated to the page-8 work-history evidence. |
| conversion_confidence | 0.35 | Page-8 provenance remains unsettled. |
| claim_probability | 0.02 | Relationship claim unsupported. |
| relevance | 0.35 | Relevant only as a required Pulgar-line exclusion check. |
| conflict_severity | 0.70 | High risk if relationship claims were inferred silently. |
| canonical_readiness | 0.00 | No canonical relationship promotion. |

## Conflicts

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person conflict: moderate risk for the CV subject versus canonical Pulgar-Smith; high risk if merged with Pulgar-Arriagada, passenger-list, or Jose/Juana clusters by name alone.
- Name-variant conflict: page 8 supports only document-level `Dario Arturo Pulgar`; it does not prove `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, `Darío J.`, `Dario Pulgar A.`, or any Jose/Juana form as variants.
- Relationship conflict: no relationship evidence appears on page 8.
- Chronology conflict: no internal page-8 chronology conflict; chronology argues against merging the CV subject with older-generation Pulgar-Arriagada or adult-passenger candidates without a direct bridge.
- Conversion/provenance conflict: current page-8 chunk absence, current manifest omission of page 8, manifest duplicate page-5 entry, and hash mismatch block promotion.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | Page 8 belongs to the locally titled CV subject `Dario Arturo Pulgar`. | 0.72 | Hold until conversion QA restores/reconciles page-8 chunk and hashes. |
| 2 | `Dario Arturo Pulgar` is canonical `Dario Arturo Pulgar-Smith`. | 0.45 | Require reviewed identity-bearing CV page or accepted local bridge before attachment. |
| 3 | CV subject is the 1953 child-passenger `Dario Pulgar`. | 0.16 | Preserve as a later chronology/identity question; not supported by page 8. |
| 4 | CV subject is `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`. | 0.10 | Preserve separately/unresolved; do not merge by name alone. |
| 5 | Page 8 supports Jose/Juana parent-candidate relationships. | 0.02 | Exclude from page-8 promotion; no relationship claim. |

## Recommended Next Action

Keep the staged conflict draft on hold. The next proof-review step should be conversion QA/provenance reconciliation for page 8: restore or regenerate the current `page-0008-chunk-01.md`, correct the chunk manifest so it includes page 8 once and does not duplicate page 5, and align the converted-file and chunk hashes. After that, run a targeted identity-bridge proof review using an identity-bearing CV page, title page, or accepted local source that explicitly connects document-level `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`. Until that bridge is reviewed, do not promote page-8 work-history claims to any canonical person and do not merge with Pulgar-Arriagada, passenger-list, or Jose/Juana candidates.
