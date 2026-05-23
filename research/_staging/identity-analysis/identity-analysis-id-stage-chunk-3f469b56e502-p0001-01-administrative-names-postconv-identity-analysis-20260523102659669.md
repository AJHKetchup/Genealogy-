---
type: identity_conflict_analysis
status: completed
role: identity_researcher
task_id: identity-analysis:research/_staging/identity/id-stage-chunk-3f469b56e502-p0001-01-administrative-names.md
worker: postconv-identity-analysis-20260523102659669
staged_identity_draft: research/_staging/identity/id-stage-chunk-3f469b56e502-p0001-01-administrative-names.md
source_packet: research/_staging/source-packets/sp-stage-chunk-3f469b56e502-p0001-01-league-of-nations-file-jacket.md
chunk: raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0001-chunk-01.md
chunk_id: CHUNK-3f469b56e502-P0001-01
page_reference: "page 1"
canonical_readiness: do_not_promote_identity
---

# Identity And Conflict Analysis: Administrative Name Mentions Only

## Blockers First

- Do not promote `research/_staging/identity/id-stage-chunk-3f469b56e502-p0001-01-administrative-names.md` to a canonical person identity, duplicate-person finding, relationship finding, or chronology finding.
- The assigned page is a League of Nations file jacket and circulation table. It does not state a genealogical person, family relationship, vital event, household, residence, or lineage.
- The literal names `M. Schwartz`, `M. Paulucci`, `Marquis Paulucci`, and `Mr. Walker` are administrative routing recipients only in this draft.
- The repeated forms `M. Paulucci` and `Marquis Paulucci`, and the repeated forms `M. Schwartz` / `Mr. Schwartz (Legale)`, may be same-office or same-person administrative routing variants, but this page lacks identity controls needed to merge or profile them.
- There is a metadata QA blocker for any future source-context promotion: the staged identity draft and source packet use `CHUNK-3f469b56e502-P0001-01`, while the referenced chunk file front matter reads `chunk_id: CHUNK-649ea7df3134-P0001-01`.
- Pulgar-line comparison is negative for this draft. No Dario, Pulgar, Smith, Arriagada, Jose/Jose, or Juana identity evidence appears in the assigned staged identity draft or page 1.

## Evidence Reviewed

- Staged identity draft: `research/_staging/identity/id-stage-chunk-3f469b56e502-p0001-01-administrative-names.md`.
- Source packet: `research/_staging/source-packets/sp-stage-chunk-3f469b56e502-p0001-01-league-of-nations-file-jacket.md`.
- Relationship negative-evidence draft: `research/_staging/relationships/rel-stage-chunk-3f469b56e502-p0001-01-negative-evidence.md`.
- Conflict negative-evidence draft: `research/_staging/conflicts/conflict-stage-chunk-3f469b56e502-p0001-01-no-direct-conflict.md`.
- Referenced chunk: `raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0001-chunk-01.md`.
- Referenced converted file: `raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md`.
- Existing same-page identity/conflict note: `research/_staging/identity-analysis/identity-analysis-conflict-stage-chunk-3f469b56e502-p0001-01-no-direct-conflict.md`.
- Existing canonical Pulgar context checked only for anti-conflation: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/dario-pulgar-adult-passenger-age-64.md`, `wiki/people/dario-pulgar-child-passenger-age-11.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.

## Literal Source Reading

The staged identity draft quotes the circulation table:

```text
| M. Schwartz (Legale) | 8.7.32 | M. Schwartz (Legale) | 12.11.32 | | |
| M. Paulucci | 11.7.32 | Mr. Schwartz (Legale) | 22.11.32 | | |
```

```text
| Mr. Walker | 15.7.32 | | | | |
```

The referenced chunk additionally transcribes:

```text
| For previous circulation see within. | | M. Schwartz | 27.6.32 | | |
| Marquis Paulucci | 11.8.32 | | | | |
| Marquis Paulucci | 11.10.32 | | | | |
```

The page also identifies the file as League of Nations `JACKET N° 5`, registry/classification `R 3578` and `50 5569 5569`, with a subject concerning a July 1929 diplomatic conference on revision of the 1906 Geneva Convention and a prisoner-of-war code. The chunk reports `Uncertain Or Illegible: None` and a complete transcription.

Interpretation kept separate: the names are visible administrative circulation entries. They are not, in this page context, proof of family identity, residence, relationship, occupation, birth, death, or a canonical person profile.

## Hypothesis 1: Administrative Routing Mentions Only

Hypothesis: the staged identity draft is correctly classified as `administrative_name_mentions`; the named people should not be promoted from this page.

Supporting evidence:

- The page structure is a file jacket and routing table, not a biographical or genealogical record.
- The source packet states that names in the circulation table appear to be administrative routing recipients and are not sufficient for identity or relationship promotion.
- The relationship draft explicitly finds no spouse, parent, child, sibling, household, or other family relationship in the assigned chunk.
- The conflict draft finds no direct identity, date, place, or relationship conflict in the chunk.
- The staged identity draft itself recommends `do_not_promote`.

Conflicts and cautions:

- The routing-table names are literal and legible, so they should not be erased or silently ignored in source-context work.
- Repetition of Schwartz and Paulucci may matter for administrative file chronology, but only after proof review of the page image and metadata.
- The chunk-id mismatch blocks clean canonical source-context promotion until reconciled.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | High confidence that names are present; very low confidence that they identify genealogical persons. |
| conflict_severity | 0.12 | Low; risk is mainly over-promotion or duplicate-page creation. |
| evidence_quality | 0.78 | Direct local evidence supports administrative context, but no identity controls. |
| conversion_confidence | 0.88 | Conversion reports no uncertain text; metadata mismatch still needs QA. |
| claim_probability | 0.92 | The `administrative mentions only` interpretation is strongly supported. |
| relevance | 0.15 | Low genealogical relevance; useful mainly for file-provenance context. |
| canonical_readiness | 0.04 | Not ready for person identity, relationship, or conflict promotion. |

## Hypothesis 2: Schwartz, Paulucci, And Walker Are Canonical Identity Candidates

Hypothesis: the draft could support person profiles or same-person/variant findings for named recipients.

Supporting evidence:

- The page literally includes name strings: `M. Schwartz`, `M. Schwartz (Legale)`, `Mr. Schwartz (Legale)`, `M. Paulucci`, `Marquis Paulucci`, and `Mr. Walker`.
- `Legale` may indicate Schwartz was associated with a legal office or department.
- `M. Paulucci` and `Marquis Paulucci` may refer to the same administrative recipient.

Conflicts and cautions:

- The page gives no forenames, birth/death data, nationality, residence, kinship, personal role biography, or external identity bridge for Schwartz, Paulucci, or Walker.
- `M.` and `Mr.` are titles only; `Legale` is functional routing context, not a family-history identity control.
- Same-person treatment for `M. Paulucci` and `Marquis Paulucci` is plausible but unproved; it should remain a routing-table hypothesis, not a canonical merge.
- Same-person treatment for Schwartz entries is likely within the circulation table, but the evidence supports only repeated routing mentions in the same administrative file.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.24 | Names are readable, but identity controls are minimal. |
| conflict_severity | 0.20 | Moderate only if a worker creates or merges person pages from these names. |
| evidence_quality | 0.42 | Direct name evidence, weak biographical specificity. |
| conversion_confidence | 0.88 | Names appear cleanly converted, subject to image proofing. |
| claim_probability | 0.26 | Possible administrative persons, not proved genealogical identities. |
| relevance | 0.10 | Very limited family-history relevance. |
| canonical_readiness | 0.03 | Do not create, merge, rename, or attach canonical people from this page. |

## Required Pulgar-Line Comparison

The assigned staged identity draft does not mention Pulgar-line names. Existing wiki context contains Pulgar candidate pages, so the comparison is an anti-conflation check only.

| Candidate cluster | Evidence in this staged identity draft/page | Ranking for this page |
| --- | --- | ---: |
| Dario Arturo Pulgar-Smith | No `Dario`, `Arturo`, `Pulgar`, `Smith`, family-supplied relationship, or biographical bridge appears. | 0.00 |
| Dario Arturo Pulgar | No CV title/path, occupational CV context, or `Dario Arturo Pulgar` name appears. | 0.00 |
| Dario Jose Pulgar-Arriagada | No `Dario Jose`, `Pulgar-Arriagada`, medical-officer context, parentage, or chronology appears. | 0.00 |
| Dario/Darío Pulgar Arriagada | No `Darío Pulgar Arriagada`, `Dario Pulgar A.`, Chiguayante, passenger-list, or expropriation context appears. | 0.00 |
| Jose/Jose parent candidates | No Jose/Jose Pulgar, parent, father, declarant, child, or register wording appears. | 0.00 |
| Juana parent candidates | No Juana, mother, spouse, parent, household, or married-name wording appears. | 0.00 |

Ranked Pulgar conclusion: no Pulgar-line identity hypothesis is supported by this page. The exact proof-review or promotion step needed next for this staged identity draft is none for Pulgar identities. Any Pulgar proof review belongs to a different staged draft that actually contains a Pulgar name or relationship bridge.

## Conflict Summary

- Same-person evidence: none for genealogical identities. Repeated Schwartz and Paulucci routing entries may represent repeated administrative handling, not a canonical person merge.
- Duplicate-person evidence: none.
- Name-variant evidence: weak administrative variation only, especially `M. Paulucci` versus `Marquis Paulucci` and `M.` versus `Mr.` for Schwartz.
- Relationship-conflict evidence: none; no family relationships are stated.
- Chronology-conflict evidence: none for people; dates are routing dates.
- Conversion/confidence issue: text confidence is high, but the staged chunk id and referenced chunk front matter disagree.

## Recommended Next Action

Keep `research/_staging/identity/id-stage-chunk-3f469b56e502-p0001-01-administrative-names.md` on hold as a negative identity-candidate note and do not promote it to canonical identity pages.

If this page is used, route only source-context metadata through proof review: registry identifiers, file subject, routing entries, and continued-correspondence reference. Reconcile the `CHUNK-3f469b56e502-P0001-01` versus `CHUNK-649ea7df3134-P0001-01` mismatch before any source-context promotion. No person merge, name normalization, relationship promotion, canonical rename, or Pulgar-line action is supported by this staged identity draft.
