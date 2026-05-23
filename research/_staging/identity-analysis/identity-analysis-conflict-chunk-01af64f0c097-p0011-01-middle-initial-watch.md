---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-01af64f0c097-p0011-01-middle-initial-watch.md"
worker: postconv-identity-analysis-20260523074233748
staged_conflict_draft: "research/_staging/conflicts/chunk-01af64f0c097-p0011-01-middle-initial-watch.md"
subject: "Dario J. Pulgar Arriagada"
source_packet: "research/_staging/source-packets/chunk-01af64f0c097-p0011-01-dario-j-pulgar-arriagada-medico-cirujano.md"
chunk_id: "CHUNK-01af64f0c097-P0011-01"
promotion_recommendation: hold_for_conversion_qa_and_identity_proof_review
tags: [identity-analysis, conflict-review, pulgar, middle-initial-watch]
---

# Identity And Conflict Analysis: Dario J. Pulgar Arriagada

## Blockers First

- The exact staged conflict draft reviewed here is `research/_staging/conflicts/chunk-01af64f0c097-p0011-01-middle-initial-watch.md`.
- The 1918 source packet and staged claim are on `hold_for_conversion_qa`: the converted text is medium confidence, the controller requested `qc:reread-page`, and the referenced rendered page image was missing from the conversion job directory.
- The literal source reading supplies a name and professional-title context only. It gives no birth date, age, parents, spouse, child, residence, signature, death date, or explicit family relationship.
- The middle initial `J.` is not expanded in this source. It cannot be silently normalized to `Jose`, `José`, `Juana`, `Arturo`, `A.`, `Arriagada`, or `Pulgar-Smith`.
- Existing local Pulgar context contains multiple near-name candidates: `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar A.`, `Darío/Dario Pulgar Arriagada`, adult and child `Dario Pulgar` passenger stubs, and Jose/Juana parent candidates. This draft does not prove a merge with any of them.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, staged drafts, or canonical wiki pages were edited.

## Literal Source Reading

The referenced converted chunk gives this source context:

```text
Sesion de 2 de Setiembre de 1918
```

```text
Previas las formalidades reglamentarias i el juramento requerido el señor Rector confirió los siguientes títulos i grados:
```

```text
Médicos-Cirujanos:
```

```text
» Darío J. Pulgar Arriagada
```

Literal reading: a person rendered in the conversion as `Darío J. Pulgar Arriagada` appears in a `Médicos-Cirujanos` list in the 2 September 1918 Council of Public Instruction session minutes.

Interpretation kept separate: if page reread confirms the line, this can support a narrow professional-title/education credential claim for a named person. It does not itself prove identity with any other Dario Pulgar or Pulgar-Arriagada person.

## Hypothesis 1: Separate 1918 Named-Person Cluster `Dario J. Pulgar Arriagada`

Supporting evidence:

- The staged identity candidate records `Dario J. Pulgar Arriagada` as a named person mention.
- The staged claim says the Rector conferred titles and degrees and then lists `Dario J. Pulgar Arriagada` under `Medico-Cirujano`.
- The relationship candidate explicitly records that no family relationship is stated in this chunk.

Conflicts and limits:

- The line still needs page-image or PDF reread to confirm exact diacritics, spacing, and the middle initial.
- This source does not supply age, vital dates, parentage, spouse, residence, or later-life identifiers.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.82 | Strong for a local named-person mention if the conversion line is confirmed. |
| conflict_severity | 0.30 | Low if kept as its own held cluster; higher only if merged prematurely. |
| evidence_quality | 0.66 | Official printed session minutes are useful, but current extraction is conversion-dependent. |
| conversion_confidence | 0.55 | Medium conversion confidence with missing page-image reread. |
| claim_probability | 0.72 | Probable that the page names this person in a medical-title list, pending reread. |
| relevance | 1.00 | Directly addresses the assigned middle-initial watch. |
| canonical_readiness | 0.18 | Hold until conversion QA and proof review. |

## Hypothesis 2: Same Person As `Dario Jose Pulgar-Arriagada`

Supporting evidence:

- The `J.` initial could stand for `Jose`, and staged ICRC/Geneva materials contain the form `Dario Jose Pulgar-Arriagada`.
- The name structure overlaps: `Dario` plus `Pulgar Arriagada` / `Pulgar-Arriagada`.

Conflicts and limits:

- The 1918 source does not expand `J.` to `Jose`.
- The staged ICRC/Geneva photograph packets rely on title/file or collection context for identity and do not independently identify him in visible page text in the reviewed notes.
- No reviewed source here bridges the 1918 medical-title person to a Geneva photograph, a table seat, a date range, a birth date, or a family relationship.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.46 | Plausible middle-initial expansion, but no direct bridge. |
| conflict_severity | 0.62 | Expanding `J.` without proof could collapse separate metadata-dependent clusters. |
| evidence_quality | 0.48 | Compared evidence is staged and partly metadata/title dependent. |
| conversion_confidence | 0.50 | Both sides have unresolved QA or identity-basis limits. |
| claim_probability | 0.38 | Possible, not proved. |
| relevance | 0.92 | Direct middle-initial and Pulgar-Arriagada comparison. |
| canonical_readiness | 0.08 | Not ready for merge, variant control, or promotion. |

## Hypothesis 3: Same Person As `Dario Pulgar A.` Passenger Candidate

Supporting evidence:

- The 1928 passenger list names `Dario Pulgar A.`, age 39, occupation `Medical Surgeon`, citizen and last permanent resident of Chile.
- Age 39 in July 1928 is chronologically compatible with receiving a medical-surgeon title in September 1918 if the same person was a young adult in 1918.
- The occupation/title overlap is meaningful: `Medical Surgeon` aligns with `Médico-Cirujano`.

Conflicts and limits:

- The 1928 row uses `A.`, not `J.` or full `Arriagada`; the initial is not expanded in that row.
- The 1928 passenger source has its own image/QA cautions in staged analysis.
- No proof-reviewed source directly states that `Dario Pulgar A.` and `Dario J. Pulgar Arriagada` are the same person.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.61 | Chronology and medical occupation are stronger than name alone, but initials differ and no bridge exists. |
| conflict_severity | 0.54 | Moderate conflation risk if `A.` and `J.` are treated as interchangeable. |
| evidence_quality | 0.60 | Passenger row and title list are relevant but both need targeted QA before merging. |
| conversion_confidence | 0.58 | 1918 is medium; 1928 row is useful but locally staged with image-review cautions. |
| claim_probability | 0.56 | Plausible same-person hypothesis, not proof. |
| relevance | 0.88 | Important Pulgar-line comparison because of medical context. |
| canonical_readiness | 0.14 | Hold; requires identity bridge and image rereads. |

## Hypothesis 4: Same Person As 1953 Adult `Dario Pulgar`

Supporting evidence:

- Existing canonical context preserves a `Dario Pulgar (adult passenger, age 64)` stub for the 7 August 1953 passenger list.
- Prior staged analysis notes the adult row lists age 64 and occupation/calling `Medical`.
- If age 64 in 1953 is accurate, this implies birth about 1888-1889, which is compatible with being conferred a medical-surgeon title in 1918.

Conflicts and limits:

- The 1953 adult row gives only `Dario Pulgar`; it does not state `J.`, `Jose`, `Arriagada`, `A.`, or full name.
- The 1953 row does not contain birth date, parentage, spouse relationship, or a direct reference to the 1918 title.
- The 1953 list also contains a separate child `Dario Pulgar`, so name-only attachment is especially risky.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.54 | Age and medical occupation fit, but full identity markers are absent. |
| conflict_severity | 0.66 | Wrong merge could collapse the 1918 medical-title person, 1928 passenger, and 1953 adult cluster. |
| evidence_quality | 0.56 | Useful but indirect cross-source comparison. |
| conversion_confidence | 0.62 | 1953 adult row appears usable in prior review; 1918 still needs reread. |
| claim_probability | 0.50 | Possible, not proved. |
| relevance | 0.84 | Required because adult 1953 Dario may be part of the older medical Pulgar cluster. |
| canonical_readiness | 0.12 | Do not merge without a proof-reviewed bridge. |

## Hypothesis 5: Same Person As 2000/2001 `Darío Pulgar Arriagada`

Supporting evidence:

- Existing canonical `wiki/people/dar-o-pulgar-arriagada.md` records `Darío Pulgar Arriagada` in a 2000-12-05 expropriation event.
- The name overlaps strongly except for the missing middle initial in the legal notice.

Conflicts and limits:

- The expropriation notice gives no age, occupation, middle initial, parentage, spouse, or birth/death details.
- If the 1918 medical-title candidate were the same as the 2000 legal-notice person, the event span is 82 years. That is possible only with a long-lived individual and must not be assumed without vital-date evidence.
- Prior analysis of the 2000/2001 notice already treats same-person identity with `Dario J. Pulgar Arriagada` as unproved.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.34 | Strong name overlap, but no age, occupation, or middle-initial bridge. |
| conflict_severity | 0.72 | Major chronology caution from 1918 to 2000/2001. |
| evidence_quality | 0.52 | Both sources are useful for their own narrow events, not for identity bridging. |
| conversion_confidence | 0.60 | 1918 is held for reread; 2000 notice has its own proof-review/QA cautions. |
| claim_probability | 0.28 | Possible but not currently persuasive. |
| relevance | 0.86 | Direct Pulgar-Arriagada name comparison. |
| canonical_readiness | 0.06 | Do not merge or attach the 1918 title to the 2000/2001 stub. |

## Hypothesis 6: Same Person As `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith`

Supporting evidence:

- All forms share `Dario` and `Pulgar`.
- Canonical `Dario Arturo Pulgar-Smith` is family supplied as Alexander John Heinz's maternal grandfather.
- Prior staged CV notes identify document-level `Dario Arturo Pulgar` and warn that attachment to `Dario Arturo Pulgar-Smith` requires an explicit identity bridge.

Conflicts and limits:

- The 1918 source says `Dario J. Pulgar Arriagada`, not `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or `Pulgar-Smith`.
- The CV/Pulgar-Smith cluster is chronologically and contextually closer to the 1953 child passenger and later CV evidence, not to a 1918 medical-title person, unless a source proves otherwise.
- No source reviewed here connects `J.` or `Arriagada` to `Arturo` or `Pulgar-Smith`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | Shared given name and paternal surname only. |
| conflict_severity | 0.78 | High risk of collapsing distinct generations or surname lines. |
| evidence_quality | 0.44 | Family-supplied canonical context is relevant, but not a bridge to this source. |
| conversion_confidence | 0.58 | 1918 conversion is held; CV page identity is separately held in prior analysis. |
| claim_probability | 0.10 | Low from this draft. |
| relevance | 0.80 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.02 | No attachment to Pulgar-Smith or CV subject. |

## Hypothesis 7: Connected To Jose/Juana Parent Candidates

Supporting evidence:

- Existing canonical stubs include `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- `Jose del Carmen Segundo Pulgar Arriagada` shares the `Pulgar Arriagada` surname combination and a birth entry dated 1888-03-08 in local canonical evidence snapshots.
- A `Jose` name in the broader Pulgar line makes the `J.` initial worth targeted checking.

Conflicts and limits:

- The 1918 medical-title source names no Jose or Juana parent, no mother, no father, no spouse, no child, and no relationship.
- A `J.` initial in a person's own name is not evidence of a Jose/Juana parent.
- The Jose/Juana register-derived clusters have separate conversion and relationship-review cautions.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.07 | No direct same-person or kinship bridge. |
| conflict_severity | 0.60 | Unsupported lineage attachment would create relationship conflicts. |
| evidence_quality | 0.36 | Compared parent-candidate evidence is separate and conversion-sensitive. |
| conversion_confidence | 0.42 | Parent-candidate readings have unresolved QA; 1918 source does not mention them. |
| claim_probability | 0.06 | This draft supports no parent or family relationship claim. |
| relevance | 0.62 | Useful only as required Pulgar-line checklist context. |
| canonical_readiness | 0.01 | No relationship action supported. |

## Conflict Summary

- Same-person conflict: unresolved between `Dario J. Pulgar Arriagada` and every compared Pulgar candidate. The strongest possible same-person comparison is with older medical clusters, especially `Dario Pulgar A.` and the 1953 adult `Dario Pulgar`, but neither is proven.
- Duplicate-person risk: high if `Dario J. Pulgar Arriagada` is merged by name alone with `Dario Jose Pulgar-Arriagada`, `Darío/Dario Pulgar Arriagada`, `Dario Arturo Pulgar`, or `Dario Arturo Pulgar-Smith`.
- Name-variant conflict: this source can support only the literal converted form `Darío/Dario J. Pulgar Arriagada` after reread. It does not prove `Jose`, `Arturo`, `Pulgar-Smith`, or `Pulgar A.` variants.
- Relationship conflict: no family relationship is stated. Do not promote parent, spouse, child, sibling, household, grandparent, or maternal-line claims from this source.
- Chronology conflict: 1918 title evidence is compatible with the 1928 age-39 medical passenger and 1953 age-64 medical adult if later identity bridges exist; it creates a serious caution if attached to the 2000/2001 legal-notice person without vital-date evidence; it is chronologically weak for the later `Dario Arturo Pulgar-Smith`/CV cluster.
- Conversion-confidence conflict: the principal literal line remains held because the page image is missing and `qc:reread-page` is unresolved.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | Separate 1918 named-person cluster `Dario J. Pulgar Arriagada` with medical-title evidence | 0.72 | Reread page 11, then send the narrow title claim to proof review if confirmed. |
| 2 | Same as 1928 `Dario Pulgar A.` medical-surgeon passenger | 0.56 | Hold; compare initials, age, occupation, and full-name evidence in a targeted identity bridge review. |
| 3 | Same as 1953 adult `Dario Pulgar`, age 64, occupation `Medical` | 0.50 | Hold; require a source connecting the adult passenger to `J.` or `Arriagada`. |
| 4 | Same as `Dario Jose Pulgar-Arriagada` | 0.38 | Hold; verify whether `J.` expands to Jose in a source with direct identity basis. |
| 5 | Same as 2000/2001 `Darío Pulgar Arriagada` | 0.28 | Preserve as unresolved; do not merge across the 82-year span without vital-date evidence. |
| 6 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.10 | Do not attach; requires a source explicitly bridging `J. Pulgar Arriagada` to `Arturo` or `Pulgar-Smith`. |
| 7 | Directly connected to Jose/Juana parent candidates | 0.06 | No relationship action; use only as a future checklist after source reread. |

## Recommended Next Action

Complete the existing `research/_staging/research-tasks/chunk-01af64f0c097-p0011-01-reread-page.md` task first: locate or regenerate the page image for source page 11, compare the original page against the converted line `» Darío J. Pulgar Arriagada`, and verify exact diacritics, spacing, middle initial, and whether the 2 September 1918 session date should be treated as the title-conferral event date.

If the reread confirms the line, send only the narrow `Médico-Cirujano` title claim for proof review. The next identity proof-review step should be a targeted Pulgar medical-cluster bridge review comparing the confirmed 1918 name against the 1928 `Dario Pulgar A.` medical-surgeon passenger and the 1953 adult `Dario Pulgar` medical passenger. Do not merge with `Dario Jose Pulgar-Arriagada`, `Darío/Dario Pulgar Arriagada`, `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or Jose/Juana parent candidates unless a reviewed local source supplies explicit identity or relationship evidence.
