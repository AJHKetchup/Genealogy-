---
type: identity_conflict_analysis
status: completed
role: identity_researcher
task_id: identity-analysis:research/_staging/identity/id-stage-chunk-3f469b56e502-p0002-01-administrative-names.md
worker: postconv-identity-analysis-20260523102908766
staged_identity_draft: research/_staging/identity/id-stage-chunk-3f469b56e502-p0002-01-administrative-names.md
source_packet: research/_staging/source-packets/sp-stage-chunk-3f469b56e502-p0002-01-league-of-nations-routing-slip.md
chunk: raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0002-chunk-01.md
chunk_id: CHUNK-3f469b56e502-P0002-01
page_reference: "page 2"
canonical_readiness: do_not_promote_identity
---

# Identity And Conflict Analysis: Administrative Name Mentions Only

## Blockers First

- Do not promote `research/_staging/identity/id-stage-chunk-3f469b56e502-p0002-01-administrative-names.md` to a canonical person identity, duplicate-person finding, relationship finding, or chronology finding.
- The assigned page is a League of Nations file cover/routing slip. It states an administrative file subject and circulation log, not a genealogical person, vital event, household, residence, lineage, or kinship claim.
- The literal names `M. Schwartz`, `M. Walters`, `Marquis Paulucci`, `M. Paulucci`, and `M. Avenol` are administrative routing recipients only in this draft.
- Repeated `M. Paulucci` / `Marquis Paulucci` and repeated `M. Schwartz` / `XIX M. Schwartz` / `XXI M. Schwartz` entries may represent the same administrative recipients within the routing table, but this page lacks identity controls needed to merge or profile them.
- There is a metadata QA blocker for source-context promotion: the referenced chunk file front matter reads `chunk_id: CHUNK-649ea7df3134-P0002-01`, while the staged draft and source packet use `CHUNK-3f469b56e502-P0002-01`.
- There is a conversion/source-packet QA blocker for the following dossier number: the chunk transcription reads `Dossier suivant | No. 1801`, while the source packet interpretation/excerpt records `7801`.
- Pulgar-line comparison is negative for this draft. No Dario, Pulgar, Smith, Arriagada, Jose, or Juana identity evidence appears in the assigned staged identity draft or page 2.

## Evidence Reviewed

- Staged identity draft: `research/_staging/identity/id-stage-chunk-3f469b56e502-p0002-01-administrative-names.md`.
- Source packet: `research/_staging/source-packets/sp-stage-chunk-3f469b56e502-p0002-01-league-of-nations-routing-slip.md`.
- Relationship negative-evidence draft: `research/_staging/relationships/rel-stage-chunk-3f469b56e502-p0002-01-negative-evidence.md`.
- Conflict negative-evidence draft: `research/_staging/conflicts/conflict-stage-chunk-3f469b56e502-p0002-01-no-direct-conflict.md`.
- Referenced chunk: `raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0002-chunk-01.md`.
- Referenced converted file: `raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md`.
- Existing same-page conflict analysis note: `research/_staging/identity-analysis/identity-analysis-conflict-stage-chunk-3f469b56e502-p0002-01-no-direct-conflict.md`.
- Existing canonical Pulgar context checked only for anti-conflation: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/dario-pulgar-adult-passenger-age-64.md`, `wiki/people/dario-pulgar-child-passenger-age-11.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.

## Literal Source Reading

The staged identity draft quotes routing-table entries:

```text
| m. Schwartz<br>Legal Dept | 26.5.31 | Marquis Paulucci | 7.10.31 ✓ | <s>M. Paulucci</s> | <s>9.7.31</s> |
| m. Walters by | 29.5.31 | XIX M. Schwartz<br>Legal Dept | 19.10.31 ✓ | Disarmament | 1.4.32 ✓ |
```

```text
| Marquis Paulucci | 30.5.31. ✓ |
| m. Schwartz<br>Legal Dept | 12.6.31. ✓ |
| XI m. Walters by | 1.7.31. ✓ |
```

The referenced chunk transcribes the page as a `GENERAL AND MISCELLANEOUS` file cover with a French subject line concerning the July 1929 diplomatic conference to revise the 1906 Geneva Convention and develop a prisoner-of-war code. Its table headings are `Transmis a / Referred to` and `Date`, with entries for routing recipients and offices including Schwartz, Walters, Paulucci, Avenol, Legal, and Disarmament.

Interpretation kept separate: these names are visible administrative circulation entries. They are not proof of family identity, residence, occupation in a genealogical sense, birth, death, parentage, marriage, or a canonical person profile.

## Hypothesis 1: Administrative Routing Mentions Only

Hypothesis: the staged identity draft is correctly classified as `administrative_name_mentions`; the named people should not be promoted from this page.

Supporting evidence:

- The page structure is a file cover/routing slip, not a biographical, civil, church, household, or family record.
- The source packet classifies the page as source-context evidence only and says it does not state vital events, kinship, household membership, or other family relationships.
- The relationship draft explicitly finds no spouse, parent, child, sibling, household, or other family relationship in the assigned chunk.
- The conflict draft explicitly finds no direct genealogical conflict in the assigned chunk.
- The staged identity draft itself recommends `do_not_promote`.

Conflicts and cautions:

- The routing-table names are literal source readings and should remain available as source-context names.
- Several routing entries are struck through, abbreviated, or flagged as uncertain; they need proof review before detailed circulation chronology is promoted.
- The chunk-id mismatch and `Dossier suivant` number disagreement block clean source-context promotion until reconciled.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.07 | High confidence that names are present; very low confidence that they identify genealogical persons. |
| conflict_severity | 0.10 | Low; risk is mainly over-promotion or duplicate-person creation from administrative names. |
| evidence_quality | 0.76 | Direct local evidence supports administrative context, but no identity controls are present. |
| conversion_confidence | 0.68 | Main form and subject are readable; routing entries, struck-through text, chunk id, and following-dossier number need QA. |
| claim_probability | 0.93 | The `administrative mentions only` interpretation is strongly supported by the staged draft and context. |
| relevance | 0.14 | Low genealogical relevance; useful mainly for archival file provenance. |
| canonical_readiness | 0.03 | Not ready for person identity, relationship, chronology, merge, or conflict promotion. |

## Hypothesis 2: Schwartz, Walters, Paulucci, And Avenol Are Identity Candidates

Hypothesis: the draft could support person profiles, same-person findings, or name-variant findings for named routing recipients.

Supporting evidence:

- The page literally includes name strings such as `M. Schwartz`, `M. Walters`, `Marquis Paulucci`, `M. Paulucci`, and `M. Avenol`.
- `Legal Dept` or `Legal` appears with several Schwartz entries, which may be administrative role context.
- `M. Paulucci` and `Marquis Paulucci` may refer to the same routing recipient within this file's circulation history.

Conflicts and cautions:

- The page gives no forenames, birth/death data, nationality, residence, family role, biographical detail, or external identity bridge for Schwartz, Walters, Paulucci, or Avenol.
- `M.` is a title or abbreviation, not an identity control. Ordinal-like marks such as `XI`, `XIX`, `XXI`, or `XXIV` may be routing annotations, not name elements.
- Same-person treatment for Paulucci variants is plausible but unproved; it should remain a routing-table hypothesis, not a canonical merge.
- Same-person treatment for repeated Schwartz or Walters entries is plausible within the circulation table, but supports only repeated administrative handling in this file.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.22 | Names are readable, but identity controls are minimal. |
| conflict_severity | 0.18 | Moderate only if a worker creates or merges person pages from these names. |
| evidence_quality | 0.40 | Direct name evidence, weak biographical specificity, and some uncertain/struck-through entries. |
| conversion_confidence | 0.62 | Names mostly appear readable, but detailed routing-table proofing is still needed. |
| claim_probability | 0.24 | Possible administrative persons, not proved genealogical identities. |
| relevance | 0.09 | Very limited family-history relevance. |
| canonical_readiness | 0.02 | Do not create, merge, rename, or attach canonical people from this page. |

## Required Pulgar-Line Comparison

The assigned staged identity draft does not mention Pulgar-line names. Existing wiki context contains Pulgar candidate pages, so the comparison is an anti-conflation check only.

| Candidate cluster | Evidence in this staged identity draft/page | Ranking for this page |
| --- | --- | ---: |
| Dario Arturo Pulgar-Smith | No `Dario`, `Arturo`, `Pulgar`, `Smith`, family-supplied relationship, or biographical bridge appears. | 0.00 |
| Dario Arturo Pulgar | No CV title/path, occupational CV context, or `Dario Arturo Pulgar` name appears. | 0.00 |
| Dario Jose Pulgar-Arriagada | No `Dario Jose`, `Pulgar-Arriagada`, medical-officer context, parentage, or chronology appears. | 0.00 |
| Dario/Dario Pulgar Arriagada | No `Dario Pulgar Arriagada`, `Dario Pulgar A.`, Chiguayante, passenger-list, or expropriation context appears. | 0.00 |
| Jose/Jose parent candidates | No Jose/Jose Pulgar, parent, father, declarant, child, or register wording appears. | 0.00 |
| Juana parent candidates | No Juana, mother, spouse, parent, household, or married-name wording appears. | 0.00 |

Ranked Pulgar conclusion: no Pulgar-line identity hypothesis is supported by this page. The exact proof-review or promotion step needed next for this staged identity draft is none for Pulgar identities. Any Pulgar proof review belongs to a different staged draft that actually contains a Pulgar name or relationship bridge.

## Conflict Summary

- Same-person evidence: none for genealogical identities. Repeated Schwartz, Walters, and Paulucci routing entries may represent repeated administrative handling, not a canonical person merge.
- Duplicate-person evidence: none.
- Name-variant evidence: weak administrative variation only, especially `M. Paulucci` versus `Marquis Paulucci` and repeated abbreviated Schwartz/Walters entries.
- Relationship-conflict evidence: none; no family relationships are stated.
- Chronology-conflict evidence: none for people; dates are routing dates from 1931 to 1932.
- Conversion/confidence issues: routing entries include struck-through or uncertain readings; the staged chunk id and referenced chunk front matter disagree; the `Dossier suivant` number differs between chunk transcription and source-packet interpretation.

## Recommended Next Action

Keep `research/_staging/identity/id-stage-chunk-3f469b56e502-p0002-01-administrative-names.md` on hold as a negative identity-candidate note and do not promote it to canonical identity pages.

If this page is used, route only source-context metadata through proof review: file subject, routing names/dates, struck-through entries, and following-dossier number. Reconcile the `CHUNK-3f469b56e502-P0002-01` versus `CHUNK-649ea7df3134-P0002-01` mismatch and the `1801` versus `7801` dossier-number disagreement before any source-context promotion. No person merge, name normalization, relationship promotion, canonical rename, or Pulgar-line action is supported by this staged identity draft.
