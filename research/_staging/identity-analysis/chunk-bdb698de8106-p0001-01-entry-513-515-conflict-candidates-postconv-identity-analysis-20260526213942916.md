---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260526213942916
task_id: "identity-analysis:research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526193717806.md"
staged_draft: "research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526193717806.md"
source_packet: "research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526193717806.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
created: 2026-05-26
canonical_readiness: hold
promotion_recommendation: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entries 513 And 515

## Blockers First

1. The staged conflict draft is explicitly `hold_for_conversion_qa`. It reports unresolved row-level conflicts for entry 513 and entry 515, so no child identity, parent-child relationship, duplicate-person conclusion, name normalization, or canonical promotion is ready.
2. Entry 513 has family-relevant Pulgar evidence, but the child-name field and mother surname are not conversion-stable. The converted/chunk text reads `Isolina del Carmen Jose` and `Juana de Dios Amador de Pulgar`; prior proof review and image-review notes preserve a possible Pulgar/Jose child-name reading and a possible `Juana de Dios Amagada de Pulgar` mother reading.
3. Entry 515 is bottom-cropped or partial in reviewed image evidence. The converted/chunk reading `Rosa Elvira del Carmen` with father/declarant `Pedro Pablo Leiva` conflicts with proof-review concerns that the father/declarant surname may be closer to `Neira` and that the child-name lines may not support the converted text.
4. The evidence in this staged draft does not directly name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Dario Pulgar Arriagada`. Those identities remain comparison guardrails only.
5. Existing wiki context contains separate Jose/Juana/Pulgar candidates, including `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, `Tulio Cesar Luis Jose`, and `Jose del Carmen Segundo Pulgar Arriagada`. This draft cannot merge or reconcile those candidates because the controlling entry 513 text is still unsettled.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526193717806.md`.
- Staged source packet: `research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526193717806.md`.
- Staged relationship candidate: `research/_staging/relationships/chunk-bdb698de8106-p0001-01-513-child-parents-proof-review-revision-postconv-evidence-extraction-20260526193717806.md`.
- Converted file and chunk for `CHUNK-bdb698de8106-P0001-01`.
- Prior local conflict/proof-review notes for `CONFLICT-STAGE-CHUNK-bdb698de8106-P0001-01-qa-candidates`, entry 513 child-parents review, and entry 515 child-father review.
- Existing canonical wiki pages for `Dario Arturo Pulgar-Smith`, `Dario/Dario Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, and `Tulio Cesar Luis Jose`.

## Literal Readings Kept Separate

### Converted/Chunk Reading For Entry 513

- Entry number: `513`.
- Registration date: `Julio veintidos de mil ochocientos ochenta i nueve`.
- Child field: `Isolina del Carmen` / `Jose`.
- Sex: `Masculino`.
- Birth: same 22 July 1889, about 4 a.m.
- Place: `Calle Colon`.
- Father: `Jose del Carmen Pulgar`, Chilean, agriculturist, domiciled at `Calle Colon`.
- Mother: `Juana de Dios Amador de Pulgar`, Chilean, labores de su sexo, domiciled at `Calle Colon`.
- Declarant: `Jose del C. Pulgar`, role `Padre`, age 47, agriculturist, domiciled at `Calle Colon`.

### Image-Review / Proof-Review Concerns For Entry 513

- The father and declarant readings are comparatively strong: `Jose del Carmen Pulgar` and `Jose del C. Pulgar` are repeatedly preserved as family-relevant support.
- The child name is not stable. Prior review states that the visible child-name area appears closer to a Pulgar/Jose reading than to the converted `Isolina del Carmen Jose`.
- The mother surname is not stable. Local notes preserve a conflict between `Amador` and an `Amagada`-style reading.
- The declarant profession may require reconciliation between `Agricultor` and `Jornalero` in older review context.

### Converted/Chunk Reading For Entry 515

- Entry number: `515`.
- Child field: `Rosa Elvira del Carmen`.
- Registration date: `Julio veintitres de mil ochocientos ochenta i nueve`.
- Father: `Pedro Pablo Leiva`, Chilean, `Jornalero`.
- Declarant: `Pedro Pablo Leiva`, role `Padre`.

### Image-Review / Proof-Review Concerns For Entry 515

- Prior review says the entry is bottom-cropped or partial.
- The father/declarant surname may be closer to `Neira` than `Leiva`.
- The child-name field may not support the converted `Rosa Elvira del Carmen` reading.
- These are conflict indicators only, not replacement transcriptions.

## Hypotheses Ranked

### H1: Entry 513 Is A Pulgar Family Birth Row, But The Child Identity Is Unresolved

Supporting evidence:

- The source packet and relationship candidate identify entry 513 as the family-relevant row.
- The converted/chunk text names father `Jose del Carmen Pulgar` and declarant `Jose del C. Pulgar`, role `Padre`.
- The father/declarant details align internally by name, role, domicile, and age.

Conflicts and limits:

- The child identity is not stable; the converted `Isolina del Carmen Jose` conflicts with image-review concerns.
- A parent-child relationship needs a stable child endpoint, not only a strong father/declarant reading.
- The row cannot be used to create or attach a canonical child identity until conversion QA reconciles the child-name/sex field.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.38 | Strong for a Pulgar father/declarant within entry 513, low for the child endpoint. |
| conflict_severity | 0.88 | The conflict changes the child identity and therefore all dependent relationships. |
| evidence_quality | 0.66 | Direct civil register evidence and local proof review exist, but derivative readings disagree. |
| conversion_confidence | 0.30 | Entry 513 remains blocked by child-name and mother-surname conversion issues. |
| claim_probability | 0.55 | Likely that the row is Pulgar-relevant; not likely enough for the exact converted child identity. |
| relevance | 1.00 | Directly addresses the staged draft and Pulgar-line concern. |
| canonical_readiness | 0.08 | Hold for targeted conversion QA and proof review. |

### H2: Entry 513 Mother Is `Juana de Dios Amador de Pulgar`

Supporting evidence:

- The converted file and chunk both read `Juana de Dios Amador de Pulgar`.
- The row places this mother in the same domicile as the father, `Calle Colon`.

Conflicts and limits:

- Prior image-review notes preserve possible `Juana de Dios Amagada de Pulgar`.
- The difference is material because it affects identity matching with existing `Juana de Dios Amagada de Pulgar`.
- Do not silently normalize `Amador` to `Amagada`, `Arriagada`, or another Pulgar-line surname.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.34 | Supported by derivative text but directly challenged by proof-review/image concern. |
| conflict_severity | 0.76 | Wrong surname would create a bad mother identity and relationship link. |
| evidence_quality | 0.52 | One derivative reading plus conflict notes; no certified image resolution. |
| conversion_confidence | 0.26 | The surname is one of the declared blockers. |
| claim_probability | 0.36 | Possible, not ready. |
| relevance | 0.94 | Direct mother-candidate issue. |
| canonical_readiness | 0.05 | Hold. |

### H3: Entry 513 Mother Is `Juana de Dios Amagada de Pulgar`

Supporting evidence:

- Existing wiki context has a `Juana de Dios Amagada de Pulgar` page with a draft child link to `Tulio Cesar Luis Jose` from a related 1889 entry cluster.
- Prior review notes preserve an `Amagada`-style alternative for entry 513's mother surname.

Conflicts and limits:

- The current staged draft's literal converted reading is `Amador`, not `Amagada`.
- The exact child identity in entry 513 is not settled, so a cross-cluster link to `Tulio Cesar Luis Jose` or the existing Juana page is premature.
- This hypothesis must remain separate from `Juana Arriagada de Pulgar`, who belongs to a different entry-172 context unless later evidence bridges them.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.32 | Plausible image-review alternative and local context, but not certified in this draft. |
| conflict_severity | 0.76 | Same material mother-identity risk as H2. |
| evidence_quality | 0.48 | Local hints are useful but not conclusive. |
| conversion_confidence | 0.24 | Requires targeted paleographic QA. |
| claim_probability | 0.34 | Possible, not ready. |
| relevance | 0.92 | Directly relevant to entry 513 and Jose/Juana guardrails. |
| canonical_readiness | 0.05 | Hold. |

### H4: Entry 515 Is `Rosa Elvira del Carmen`, Child Of `Pedro Pablo Leiva`

Supporting evidence:

- The converted file and chunk read `Rosa Elvira del Carmen` and father/declarant `Pedro Pablo Leiva`.
- The entry structure includes a father/declarant field, so the page may contain a child-father relationship if legibility is resolved.

Conflicts and limits:

- Prior proof review says the image is bottom-cropped/partial and that father/declarant may read closer to `Neira`.
- The child-name field may not visibly support the converted `Rosa Elvira del Carmen` reading.
- This entry does not contain Pulgar-line evidence and is relevant mainly as a conversion-QA control.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.24 | Derivative text supports the endpoints, but image review materially challenges them. |
| conflict_severity | 0.70 | Wrong endpoints would create a false child-father relationship. |
| evidence_quality | 0.46 | Direct register structure exists, but bottom crop and conflicting readings weaken it. |
| conversion_confidence | 0.22 | Entry 515 is explicitly partial/conflicted. |
| claim_probability | 0.25 | Possible derivative reading only. |
| relevance | 0.70 | Relevant to the staged conflict draft, low Pulgar-family relevance. |
| canonical_readiness | 0.03 | Hold. |

### H5: Entry 513 Father/Declarant Is Existing `Jose del Carmen Pulgar`

Supporting evidence:

- Converted/chunk text for entry 513 reads father `Jose del Carmen Pulgar`.
- Declarant is `Jose del C. Pulgar`, role `Padre`, age 47, with the same domicile.
- Existing `wiki/people/jose-del-carmen-pulgar.md` preserves a separate draft child link in the broader Pulgar/Juana context.

Conflicts and limits:

- Same-name evidence is not enough to merge the entry-513 father/declarant with the existing canonical stub.
- The child identity and mother surname are unresolved, so the parent cluster cannot be stabilized from this draft.
- Existing `Jose del Carmen Pulgar` context may be derivative of other held register work and is not independent proof of same person.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.44 | Good same-row father/declarant support, insufficient cross-record bridge. |
| conflict_severity | 0.68 | Premature merge would distort parent clusters across held register entries. |
| evidence_quality | 0.60 | Stronger than the child/mother endpoints but still conversion-scoped. |
| conversion_confidence | 0.42 | Father name is comparatively stable, but row-level issues remain. |
| claim_probability | 0.46 | Plausible same-name candidate, not a merge. |
| relevance | 0.94 | Direct Jose parent-candidate issue. |
| canonical_readiness | 0.12 | Hold for QA and identity-bridge proof review. |

### H6: Entry 513 Or 515 Bridges To Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Or Dario Jose/Pulgar-Arriagada Candidates

Supporting evidence:

- Entry 513 is Pulgar-family relevant if confirmed.
- Existing local context contains family-supplied `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, and several Dario/Pulgar-Arriagada staged clusters.

Conflicts and limits:

- The staged draft does not name Dario, Arturo, Smith, Dario Jose, Dario J., Pulgar-Arriagada as a Dario identity, Alexander John Heinz, a spouse, a grandchild, or any modern biography bridge.
- Canonical `Dario Arturo Pulgar-Smith` explicitly warns against automatic merges with similarly named Dario/Pulgar/Pulgar-Arriagada records.
- Entry 513's unresolved Jose/Juana parent evidence can justify later comparison only after QA; it cannot establish a Dario-line attachment.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.04 | Broad surname/family relevance only. |
| conflict_severity | 0.82 | Premature attachment would create a major lineage conflation. |
| evidence_quality | 0.22 | No direct bridge in this staged draft. |
| conversion_confidence | 0.30 | QA could certify entry 513 text but still would not prove a Dario bridge. |
| claim_probability | 0.03 | Unsupported as a same-person or relationship claim. |
| relevance | 0.72 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.00 | Do not attach or merge. |

## Pulgar-Line Comparison Required By Task

| Candidate | Local evidence context | Relationship to this staged draft | Rank |
| --- | --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | Canonical family-supplied maternal grandfather of Alexander John Heinz; page warns against automatic merges with similar Pulgar records. | Not named in entries 513 or 515. No Smith, Arturo, Alexander, or family bridge appears here. | Not connected. |
| `Dario Arturo Pulgar` | CV/document-level staged cluster, still requiring identity bridge to Pulgar-Smith in prior reviews. | Not named in this register page. No CV, occupation chronology, or direct identity bridge. | Not connected. |
| `Dario Jose Pulgar-Arriagada` | Separate local photograph/ICRC/source-context cluster. | Not named here. Surname-family context only after entry 513 QA. | Not connected. |
| `Dario J. Pulgar Arriagada` / `Dario Pulgar Arriagada` | Separate medical-title, institutional, or legal-notice clusters in local staging/wiki context. | Not named here. No age, parentage, residence continuity, or chronology bridge. | Not connected. |
| `Jose del Carmen Pulgar` | Entry 513 converted/chunk father and declarant; existing wiki stub has separate draft parent context. | Highest same-name parent lead, but no merge before row QA and identity bridge. | Parent-candidate lead. |
| `Juana de Dios Amador de Pulgar` | Converted/chunk entry 513 mother reading. | Live literal derivative reading; conflicts with image-review alternatives. | Held mother candidate. |
| `Juana de Dios Amagada de Pulgar` | Existing wiki stub and prior review alternative for entry 513 mother surname. | Live alternate mother-surname hypothesis; not certified by this draft. | Held mother candidate. |
| `Juana Arriagada de Pulgar` | Separate entry-172 mother candidate for `Jose del Carmen Segundo Pulgar Arriagada`. | Not named in entry 513/515. Do not substitute for Amador/Amagada by family context. | Separate Juana candidate. |

## Conflict Summary

- Same-person conflict: none resolvable. Entry 513 child, entry 515 child, Jose father/declarant, and Juana mother candidates must remain separate until conversion QA.
- Duplicate-person risk: high for merging `Jose del Carmen Pulgar` father/declarant into an existing same-name stub without cross-record proof; high for merging `Juana de Dios Amador`, `Juana de Dios Amagada`, and `Juana Arriagada` by name similarity.
- Name-variant conflict: `Amador` versus `Amagada` is an unresolved source-reading conflict, not a silent variant. `Leiva` versus `Neira` in entry 515 is also an unresolved source-reading conflict.
- Relationship conflict: entry 513 parent-child relationship is blocked because the child identity and mother surname are unstable. Entry 515 child-father relationship is blocked because the child and father/declarant readings are unstable.
- Chronology conflict: no independent chronology bridge to Dario-line candidates is present; the 1889 register date should not be connected to modern Dario clusters without separate evidence.
- Conversion conflict: severe enough to hold all dependent claims from entries 513 and 515.

## Overall Scores

| Category | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.38 | Highest only for entry 513 as a Pulgar-relevant row; exact endpoints remain unsettled. |
| conflict_severity | 0.88 | The conflicts affect child identity, parent identity, and relationship endpoints. |
| evidence_quality | 0.62 | Civil register source is strong, but conversion/proof-review layers disagree. |
| conversion_confidence | 0.28 | Targeted conversion QA is the blocker named by the staged draft. |
| claim_probability | 0.55 | Entry 513 is probably Pulgar-relevant, but exact identities are not ready. |
| relevance | 0.96 | Directly addresses the staged conflict draft and required Pulgar-line guardrails. |
| canonical_readiness | 0.06 | Hold; no canonical edits or promotion. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-bdb698de8106-P0001-01` against the source image, converted Markdown, chunk, source packet, and proof-review notes. The QA result should certify entry 513 child name/sex, mother surname, father/declarant profession, and entry 515 child-name/father-declarant surname/bottom-crop completeness.

After QA, rerun proof review on each atomic claim and relationship candidate before any promotion. If entry 513 remains Pulgar-relevant, the next identity proof-review step must compare the certified row only against `Jose del Carmen Pulgar`, `Juana de Dios Amador de Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, and `Dario/Dario Pulgar Arriagada`, preserving separate hypotheses unless a direct bridge is found.
