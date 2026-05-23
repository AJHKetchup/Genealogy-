---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260523101249876
task_id: identity-analysis:research/_staging/conflicts/CONFLICT-STAGE-CHUNK-b986d37e685d-P0002-01-conversion-qa.md
staged_draft: research/_staging/conflicts/CONFLICT-STAGE-CHUNK-b986d37e685d-P0002-01-conversion-qa.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-b986d37e685d-P0002-01-league-of-nations-file-cover-routing-slip.md
source: raw/sources/R3578-50-5569-5569-Jacket5.pdf
converted_file: raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md
chunk: raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0002-chunk-01.md
referenced_chunk_id: CHUNK-b986d37e685d-P0002-01
current_chunk_frontmatter_id: CHUNK-649ea7df3134-P0002-01
promotion_recommendation: hold_for_conversion_qa
tags: [identity-analysis, conflict-analysis, conversion-qa, routing-slip, staging]
---

# Identity/Conflict Analysis: CONFLICT-STAGE-CHUNK-b986d37e685d-P0002-01 Conversion QA

## Blockers First

- Provenance mismatch blocks promotion: the staged conflict draft references `CHUNK-b986d37e685d-P0002-01`, but the current referenced chunk file front matter reads `CHUNK-649ea7df3134-P0002-01`.
- Hash reconciliation remains blocked: the source packet records converted SHA-256 `b986d37e685d7788568baf82b8d1c6d9c92b30eda4a02450e64a28471dc92196`, current converted SHA-256 `88e402458471c1e4f84a77cd3c8143e25bc52f7b7a5ea897a1c02fef66089a78`, current chunk SHA-256 `3c0874f5be388c569246e2582a5919a5fd7dc975dafaeb86d5119c7f28fe132c`, and manifest chunk SHA-256 `bb0d4e7230c65a332f676aec0dd2294c5e8fa6d977c8633abdefe0e3b16f0530`.
- The staged conflict draft and companion identity draft are about handwritten administrative routing names only. They do not state a family identity, relationship, vital event, residence, or uniquely identifying biographical claim.
- Handwritten name/date readings remain conversion-sensitive. The staged conflict draft flags `M. Schurnik[?]` and `I.C.V`; the current chunk instead reads the relevant uncertain routing entries as `M. Schwartz (upl)` and `M. Avenol (by L.C.V)`.
- Do not promote any person, relationship, chronology, or name-variant fact from this staged draft until a page-image reread and metadata reconciliation are complete.

## Literal Source Readings

From the staged conflict draft:

```text
M. Schurnik[?]
```

```text
I.C.V
```

From the companion staged identity draft:

```text
| [Handwritten] Marquis Paulucci | [Handwritten] 30.5.31 |
```

```text
| [Handwritten] M. Schwartz<br>legal dept | [Handwritten] 12.6.31 |
```

```text
| [Handwritten] M. Schurnik[?] (legal) | [Handwritten] 12.11.31 |
```

From the current referenced chunk file:

```text
| <s>M. Schwartz</s><br>Legal Dept | 26.5.31 | <s>XIX M. Schwartz</s><br>Legal | 19.10.31 | <s>Disarmament</s> | 1.4.32 ✓ |
```

```text
| <s>Marquis Paulucci</s> | 30.5.31 | <s>XX M. Avenol (by L.C.V)</s> | | <s>XXJ M. Schwartz</s><br>Legal | 17.5.32 ✓ |
```

```text
| <s>XI M. Walters</s><br>by | 1.7.31 | <s>M. Schwartz (upl)</s> | 12.11.31 | <s>Disarmament</s> | 21.5.32 ✓ |
```

Interpretation kept separate: these are circulation-table entries on a League of Nations archival file cover or routing slip. They are not evidence of kinship or family identity.

## Hypothesis 1: Administrative Routing Names Only

Hypothesis: Schwartz, Walters, Marquis Paulucci, M. Paulucci, M. Avenol, and the uncertain `M. Schurnik[?]`/`M. Schwartz (upl)` reading are administrative routing recipients or departments, not genealogy identities to merge or promote.

Evidence supporting:

- The source packet identifies the page as an archival file cover or routing slip.
- The literal text is a circulation table headed `Transmis à / Referred to` with dates.
- The source packet states the named entries appear to be administrative routing recipients or departments, not family members.
- No birth, death, parent, spouse, child, household, residence, or family-event language appears in the assigned draft or referenced page text.

Evidence against or limits:

- Individual names are handwritten and at least one name/initial reading differs between staged drafts and the current chunk.
- Some entries are personal names, so they may represent real officials or staff, but this page supplies no identity-disambiguating data.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | The page names routing recipients but does not identify them genealogically. |
| conflict_severity | 0.20 | Low genealogy conflict severity; high only if someone tried to promote routing names as family identities. |
| evidence_quality | 0.58 | The source scope is clear, but handwritten name details are unstable. |
| conversion_confidence | 0.55 | Medium for page purpose, lower for exact handwritten names and initials. |
| claim_probability | 0.90 | Very likely these are administrative routing entries only. |
| relevance | 0.74 | Directly answers the staged conversion QA conflict. |
| canonical_readiness | 0.05 | Not ready for canonical person or relationship pages. |

## Hypothesis 2: A Genealogical Same-Person Or Duplicate-Person Conflict Exists On This Page

Hypothesis: The page contains evidence for a same-person, duplicate-person, name-variant, relationship, or chronology conflict.

Evidence supporting:

- None in the assigned staged draft, companion identity draft, source packet, current chunk, or current converted-page text reviewed here.

Evidence against or limits:

- The staged conflict draft explicitly says no genealogical conflict is stated in this chunk.
- The companion identity draft says these names should be treated as administrative routing recipients only and should not be promoted.
- The source packet says no vital event, residence, kinship, household, or family identity claim is stated.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | No identity-bearing genealogy evidence. |
| conflict_severity | 0.08 | No direct genealogy conflict; the practical risk is false promotion. |
| evidence_quality | 0.50 | Good enough to reject genealogy promotion, not good enough for exact name assertions. |
| conversion_confidence | 0.55 | Conversion issues affect names, not the non-genealogical scope. |
| claim_probability | 0.03 | A genealogical conflict is very unlikely from this page alone. |
| relevance | 0.80 | This is the negative-control conclusion for the assigned conflict draft. |
| canonical_readiness | 0.00 | No canonical update should be made. |

## Required Pulgar-Line Comparison

This staged draft does not mention Dario, Pulgar, Pulgar-Smith, Pulgar-Arriagada, Jose Pulgar, or Juana candidates. Existing wiki context does contain Pulgar-line pages, so the comparison below is an anti-conflation check only.

### Dario Arturo Pulgar-Smith

Canonical context: `wiki/people/dario-arturo-pulgar-smith.md` represents Dario Arturo Pulgar-Smith from family-supplied knowledge as Alexander John Heinz's maternal grandfather and explicitly warns not to merge similarly named records automatically.

Comparison to this routing-slip page:

- No `Dario`, `Arturo`, `Pulgar`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, grandparent relationship, or family-line reference appears in the assigned staged draft.
- This page contributes no evidence for or against Dario Arturo Pulgar-Smith.

Scores: identity_confidence 0.00; conflict_severity 0.04; evidence_quality 0.00; conversion_confidence 0.55; claim_probability 0.00; relevance 0.18; canonical_readiness 0.00.

### Dario Arturo Pulgar

Local staged CV materials elsewhere treat `Dario Arturo Pulgar` as a document-level CV subject pending identity review. This routing-slip page is unrelated.

Comparison:

- No `Dario Arturo Pulgar` reading appears.
- No CV, occupation, chronology, or biographical bridge appears.

Scores: identity_confidence 0.00; conflict_severity 0.04; evidence_quality 0.00; conversion_confidence 0.55; claim_probability 0.00; relevance 0.16; canonical_readiness 0.00.

### Dario Jose Pulgar-Arriagada

Staged Geneva photograph identity drafts name `Dario Jose Pulgar-Arriagada` from source metadata/title context and hold promotion because image-level identification is weak or source images were missing locally.

Comparison:

- The routing slip concerns a League of Nations file cover about the 1929 diplomatic conference and routing names such as Schwartz, Walters, Paulucci, and Avenol.
- It does not name Dario Jose Pulgar-Arriagada and cannot bridge the metadata-derived photograph candidate to any canonical person.

Scores: identity_confidence 0.00; conflict_severity 0.06; evidence_quality 0.00; conversion_confidence 0.55; claim_probability 0.00; relevance 0.18; canonical_readiness 0.00.

### Dario/Darío Pulgar Arriagada

Canonical context: `wiki/people/dar-o-pulgar-arriagada.md` is a stub with a 2000-12-05 expropriation-event evidence snapshot.

Comparison:

- The routing slip does not name Dario/Darío Pulgar Arriagada.
- No chronology or relationship connection exists between this 1931-1932 routing table and the 2000 expropriation stub in the reviewed evidence.

Scores: identity_confidence 0.00; conflict_severity 0.05; evidence_quality 0.00; conversion_confidence 0.55; claim_probability 0.00; relevance 0.15; canonical_readiness 0.00.

### Jose/Juana Parent Candidates

Existing wiki context includes separate Jose/Juana candidates, including Jose del Carmen Segundo Pulgar Arriagada with probable mother Juana Arriagada de Pulgar, and Jose del Carmen Pulgar / Juana de Dios Amagada de Pulgar as draft parents of Tulio Cesar Luis Jose.

Comparison:

- The routing slip does not name Jose, Juana, Pulgar, Arriagada, Amagada, Tulio, or a parent-child relationship.
- It supplies no evidence to merge, reject, or rank Jose/Juana parent candidates.

Scores: identity_confidence 0.00; conflict_severity 0.05; evidence_quality 0.00; conversion_confidence 0.55; claim_probability 0.00; relevance 0.14; canonical_readiness 0.00.

## Conflicts

- Same-person conflict: none supported by this staged draft.
- Duplicate-person conflict: none supported by this staged draft.
- Name-variant conflict: only a conversion-level administrative-name conflict is present, especially `M. Schurnik[?]` versus current-chunk `M. Schwartz (upl)` and `I.C.V` versus current-chunk `L.C.V`.
- Relationship conflict: none supported.
- Chronology conflict: none genealogical. The routing dates are administrative circulation dates only and should not be used as life-event chronology for named persons.
- Provenance conflict: active blocker. The staged conflict's referenced chunk id/hash values do not align with the current chunk file and source-packet hash notes.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | This is a non-genealogical administrative routing-slip QA issue only. | 0.90 | Hold for conversion/provenance QA; do not promote names. |
| 2 | The page supports only low-level archival source-scope metadata after reread. | 0.70 | After QA, use only as file-cover/routing context if needed. |
| 3 | The page contains a genealogical identity, relationship, or chronology conflict. | 0.03 | Reject for now; reopen only if a reviewed page image reveals identity-bearing text not present in current staged materials. |
| 4 | The page connects to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Darío Pulgar Arriagada, or Jose/Juana parent candidates. | 0.00 | Preserve all Pulgar-line candidates separately; no Pulgar action from this staged draft. |

## Recommended Next Action

Run targeted conversion/provenance proof review for the referenced page: reconcile the staged `CHUNK-b986d37e685d-P0002-01` identifier and hash values against the current `page-0002-chunk-01.md` front matter, reread the page image for the disputed handwritten routing entries, and update only the appropriate conversion QA/staging artifacts through the normal proof-review path. Do not create, merge, rename, or promote any canonical person, relationship, or Pulgar-line fact from this staged conflict draft.
