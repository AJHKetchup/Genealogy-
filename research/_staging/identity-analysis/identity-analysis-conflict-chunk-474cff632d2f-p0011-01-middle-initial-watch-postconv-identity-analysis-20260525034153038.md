---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-474cff632d2f-p0011-01-middle-initial-watch.md"
worker: postconv-identity-analysis-20260525034153038
staged_conflict_draft: "research/_staging/conflicts/chunk-474cff632d2f-p0011-01-middle-initial-watch.md"
subject: "Darío J. Pulgar Arriagada"
source_packet: "research/_staging/source-packets/chunk-474cff632d2f-p0011-01-dario-j-pulgar-arriagada-medico-cirujano.md"
chunk: "raw/chunks/ca753b8b14-anales-de-la-universidad-p0004-0023-anales-de-la-universidad-de-chile-sess-af33a57786/page-0011-chunk-01.md"
chunk_id: "CHUNK-474cff632d2f-P0011-01"
promotion_recommendation: do_not_promote_identity_merge
tags: [identity-analysis, conflict-review, pulgar, middle-initial-watch]
---

# Identity And Conflict Analysis: Darío J. Pulgar Arriagada

## Blockers First

- Exact staged draft reviewed: `research/_staging/conflicts/chunk-474cff632d2f-p0011-01-middle-initial-watch.md`.
- The staged draft and source packet use `CHUNK-474cff632d2f-P0011-01`, but the referenced chunk front matter currently reads `CHUNK-55285fb49aba-P0011-01` and has a different `converted_sha256`. Resolve this metadata/hash mismatch before promotion.
- The source supports only the printed name line and medical-title list context. It does not state age, birth date, parents, spouse, child, residence, signature, death date, or any family relationship.
- The middle initial `J.` is unexpanded. It must not be silently treated as `Jose`, `José`, `Juana`, `Arturo`, `A.`, `Arriagada`, or `Pulgar-Smith`.
- Existing local context contains multiple Pulgar candidates: `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar A.`, `Darío/Dario Pulgar Arriagada`, adult and child `Dario Pulgar` passenger stubs, and Jose/Juana parent candidates. This draft does not prove a merge with any of them.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, staged drafts, or canonical wiki pages were edited.

## Literal Source Reading

From the staged source packet and referenced page chunk, the page is the `Sesion de 2 de Setiembre de 1918` of the `Consejo de Instruccion Publica`. It says the Rector conferred titles and degrees and, under `Médicos-Cirujanos:`, lists:

```text
» Darío J. Pulgar Arriagada
```

Interpretation kept separate: this supports a narrow claim that a person printed as `Darío J. Pulgar Arriagada` appears in a 1918 University of Chile public-instruction session list under medical-surgeon title conferrals. It does not prove a full middle name, alternate surname form, duplicate identity, or relationship.

## Hypotheses And Evidence

### 1. Separate 1918 named-person cluster: `Darío J. Pulgar Arriagada`

Supporting evidence:

- The staged conflict draft preserves the literal reading `» Darío J. Pulgar Arriagada`.
- The source packet reports high conversion confidence after local page-image reread on 2026-05-25 for the session date, `Médicos-Cirujanos:` heading, and name line.
- The page context is an official printed title/degree conferral list.

Conflicts and limits:

- Chunk/hash metadata is not aligned between the staged packet and the referenced chunk.
- No family or later-life identifiers are present.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.86 | Strong for a distinct local named-person mention. |
| conflict_severity | 0.28 | Low if held separately; risk rises if merged by name. |
| evidence_quality | 0.78 | Official printed list plus page-image reread, but narrow. |
| conversion_confidence | 0.88 | High for the name line; metadata mismatch remains. |
| claim_probability | 0.84 | Probable as a narrow title-conferral/name-list claim. |
| relevance | 1.00 | Directly responsive to the staged middle-initial watch. |
| canonical_readiness | 0.30 | Only potentially ready for a narrow claim after proof review and metadata reconciliation; not ready for merge. |

### 2. Same person as `Dario Pulgar A.` older medical/property/passenger candidate

Supporting evidence:

- Other staged/canonical local context includes `Dario Pulgar A.` and medical-surgeon/physician context.
- A medical title in 1918 is chronologically plausible for some older Dario Pulgar medical-cluster evidence.
- `Pulgar A.` could be an abbreviated maternal-surname form in some contexts, but this requires proof.

Conflicts and limits:

- `J.` is not `A.`.
- The 1918 line does not give an age, residence, signature, property, or full identity bridge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.56 | Medical context is meaningful; initials conflict. |
| conflict_severity | 0.60 | Moderate risk if `J.` and `A.` are treated as interchangeable. |
| evidence_quality | 0.62 | Relevant local hints, but no direct bridge in this draft. |
| conversion_confidence | 0.66 | 1918 line is high; compared records have separate cautions. |
| claim_probability | 0.52 | Plausible but unproved. |
| relevance | 0.90 | Important Pulgar medical-cluster comparison. |
| canonical_readiness | 0.14 | Hold for targeted bridge review. |

### 3. Same person as `Dario Jose Pulgar-Arriagada`

Supporting evidence:

- The initial `J.` could stand for `Jose`.
- Name structure overlaps: `Dario` plus `Pulgar Arriagada` / `Pulgar-Arriagada`.

Conflicts and limits:

- The 1918 source does not expand `J.`.
- Local `Dario Jose Pulgar-Arriagada` context must be treated as separate unless a reviewed source supplies an explicit bridge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.44 | Possible by initial and surname pattern. |
| conflict_severity | 0.64 | Premature expansion of `J.` could collapse distinct clusters. |
| evidence_quality | 0.50 | Indirect name overlap only. |
| conversion_confidence | 0.60 | 1918 reading is strong; expansion is unsupported. |
| claim_probability | 0.36 | Possible, not proved. |
| relevance | 0.94 | Direct middle-initial comparison. |
| canonical_readiness | 0.08 | Not ready for variant promotion or merge. |

### 4. Same person as canonical `Darío Pulgar Arriagada`

Supporting evidence:

- Existing `wiki/people/dar-o-pulgar-arriagada.md` records a `Darío Pulgar Arriagada` event in 2000.
- The name overlaps except for the 1918 middle initial.

Conflicts and limits:

- The 2000 canonical event is 82 years after the 1918 title-conferral list.
- The canonical snapshot does not give age, occupation, middle initial, parents, spouse, birth, or death data that would bridge the two mentions.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.30 | Strong name overlap but weak chronology bridge. |
| conflict_severity | 0.72 | High chronology risk without vital evidence. |
| evidence_quality | 0.54 | Both sources are useful only for their narrow events. |
| conversion_confidence | 0.74 | 1918 line is reread; canonical event is not identity-rich. |
| claim_probability | 0.26 | Possible but not persuasive. |
| relevance | 0.88 | Required Pulgar-Arriagada comparison. |
| canonical_readiness | 0.06 | Do not attach the 1918 title to the 2000 stub. |

### 5. Same person as `Dario Arturo Pulgar` or canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- The names share `Dario` and `Pulgar`.
- Canonical `Dario Arturo Pulgar-Smith` is family supplied as Alexander John Heinz's maternal grandfather.
- Local CV material uses the document-level name `Dario Arturo Pulgar`, but previous local reviews hold that evidence pending a bridge to `Pulgar-Smith`.

Conflicts and limits:

- The 1918 source says `Darío J. Pulgar Arriagada`, not `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or `Pulgar-Smith`.
- No reviewed local source connects `J.` or `Arriagada` to `Arturo` or `Pulgar-Smith`.
- This source states no family relationship to Alexander John Heinz.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | Shared given name and paternal surname only. |
| conflict_severity | 0.80 | High risk of collapsing distinct surname lines or generations. |
| evidence_quality | 0.46 | Family/CV context is anti-conflation context, not a bridge. |
| conversion_confidence | 0.68 | 1918 line is strong; CV-to-Smith bridge is separately unresolved. |
| claim_probability | 0.10 | Low from this staged draft. |
| relevance | 0.82 | Required Pulgar-line comparison. |
| canonical_readiness | 0.02 | No attachment to Pulgar-Smith or CV subject. |

### 6. Same person as 1953 adult or child `Dario Pulgar` passenger stubs

Supporting evidence:

- `wiki/people/dario-pulgar-adult-passenger-age-64.md` records an adult `Dario Pulgar`, age 64, traveling on 1953-08-07. That age is chronologically possible for a 1918 medical-title recipient.
- `wiki/people/dario-pulgar-child-passenger-age-11.md` records a separate child `Dario Pulgar` on the same passenger-list context.

Conflicts and limits:

- Neither passenger stub states `J.`, `Jose`, `Arriagada`, `A.`, or `Pulgar-Smith`.
- The child passenger, age 11 in 1953, is chronologically incompatible with receiving a medical title in 1918.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.46 | Adult passenger is possible by age; child passenger is effectively excluded. |
| conflict_severity | 0.68 | Passenger-list conflation could collapse adult/child and medical clusters. |
| evidence_quality | 0.56 | Useful age context but no full-name bridge. |
| conversion_confidence | 0.72 | Canonical snapshots support narrow passenger claims. |
| claim_probability | 0.42 | Possible for adult passenger, near-zero for child passenger. |
| relevance | 0.78 | Relevant duplicate-person check. |
| canonical_readiness | 0.10 | No merge without direct bridge. |

### 7. Connected to Jose/Juana parent candidates

Supporting evidence:

- Existing local context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- `Jose del Carmen Segundo Pulgar Arriagada` shares the `Pulgar Arriagada` surname combination and a recorded 1888 birth, which is chronologically compatible with a 1918 professional title only if future evidence proves a name bridge.
- The unexpanded `J.` justifies a targeted check for a `Jose` expansion.

Conflicts and limits:

- The 1918 source names no parent, mother, father, spouse, child, or household.
- A middle initial is not evidence of parentage.
- Jose/Juana register and relationship clusters have separate confidence and conversion cautions.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Chronologically interesting for Jose del Carmen Segundo, but no bridge exists. |
| conflict_severity | 0.62 | Unsupported lineage attachment would create relationship conflicts. |
| evidence_quality | 0.42 | Compared evidence is separate and relationship-sensitive. |
| conversion_confidence | 0.50 | 1918 line is strong; parent-candidate readings have separate QA limits. |
| claim_probability | 0.14 | Future-check hypothesis only. |
| relevance | 0.70 | Required parent-candidate checklist. |
| canonical_readiness | 0.01 | No relationship action supported. |

## Conflict Summary

- Same-person conflict: unresolved. The strongest comparison is the older medical `Dario Pulgar A.` cluster, but the `J.`/`A.` initial conflict blocks identity merger.
- Duplicate-person risk: high if `Darío J. Pulgar Arriagada` is merged by name alone with `Dario Jose Pulgar-Arriagada`, `Darío/Dario Pulgar Arriagada`, `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, passenger stubs, or Jose/Juana lineage clusters.
- Name-variant conflict: this source supports only `Darío J. Pulgar Arriagada`. It does not prove `Jose`, `Arturo`, `Pulgar-Smith`, or `Pulgar A.` variants.
- Relationship conflict: no relationship is stated. Do not promote parent, spouse, child, sibling, grandparent, maternal-line, or Jose/Juana relationship claims from this source.
- Chronology conflict: 1918 is compatible with some older medical/adult-passenger hypotheses, incompatible with the 1953 child passenger, and risky across the 82-year gap to the 2000 `Darío Pulgar Arriagada` canonical stub without vital evidence.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Separate 1918 named-person cluster `Darío J. Pulgar Arriagada` with medical-title list evidence | 0.86 | Reconcile chunk/hash metadata, then proof-review only the narrow 1918 name/title list claim. |
| 2 | Same as `Dario Pulgar A.` older medical/property/passenger cluster | 0.52 | Hold; run targeted bridge review comparing initials, age, occupation, signatures/property, and full-name evidence. |
| 3 | Same as 1953 adult `Dario Pulgar`, age 64 | 0.42 | Hold; require a source connecting the adult passenger to `J.` or `Arriagada`. |
| 4 | Same as `Dario Jose Pulgar-Arriagada` | 0.36 | Hold; proof-review direct evidence that expands `J.` to `Jose`. |
| 5 | Same as canonical `Darío Pulgar Arriagada` in 2000 expropriation context | 0.26 | Preserve as unresolved; do not merge across 82 years without vital-date evidence. |
| 6 | Connected to Jose/Juana parent candidates, especially `Jose del Carmen Segundo Pulgar Arriagada` | 0.14 | No relationship action; use only as future checklist after bridge evidence appears. |
| 7 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.10 | Do not attach; require explicit reviewed evidence bridging `J. Pulgar Arriagada` to `Arturo` or `Pulgar-Smith`. |

## Recommended Next Action

First proof-review step: resolve the `CHUNK-474cff632d2f-P0011-01` versus `CHUNK-55285fb49aba-P0011-01` metadata/hash mismatch, then review the narrow claim that the 2 September 1918 session list includes `Darío J. Pulgar Arriagada` under `Médicos-Cirujanos`.

Separate identity proof-review step: create or use a targeted Pulgar medical-cluster bridge review comparing the confirmed 1918 line against `Dario Pulgar A.` evidence, the 1953 adult `Dario Pulgar` stub, and any direct `Dario Jose Pulgar-Arriagada` identity-bearing source. Keep `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Darío/Dario Pulgar Arriagada`, the 1953 child passenger, and Jose/Juana parent candidates separate unless a reviewed local source supplies explicit identity or relationship evidence.
