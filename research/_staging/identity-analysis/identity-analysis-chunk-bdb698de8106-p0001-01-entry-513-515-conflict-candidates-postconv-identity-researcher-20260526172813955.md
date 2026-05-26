---
type: identity_conflict_analysis
status: hold
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526171453486.md"
worker: postconv-identity-analysis-20260526172813955
staged_draft: research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526171453486.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
chunk_id: CHUNK-bdb698de8106-P0001-01
canonical_readiness: hold_for_conversion_qa
---

# Identity/Conflict Analysis: 1889 Los Angeles Birth Register Page 172 Entries 513 And 515

## Blockers

1. The exact staged draft is `research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526171453486.md`.
2. Entry 513 is not row-control stable. The current converted file and chunk read child `Isolina del Carmen / José`, sex `Masculino`, father `José del Carmen Pulgar`, mother `Juana de Dios Amador de Pulgar`, and declarant `José del C. Pulgar`; other staged/image-reviewed page-172 work reads the child and mother differently.
3. Entry 513 mother surname is unresolved between at least `Amador`, `Amagada`, and possibly an `Arriagada`-style reading. Do not normalize or substitute a family-context surname.
4. Entry 513 child endpoint is unresolved. The current draft cannot safely create or attach a child identity from `Isolina del Carmen / José`.
5. Entry 515 is bottom-cropped/partial in reviewed evidence and conflicts with converted child/father readings. It provides no Pulgar-line support in this task.
6. Existing wiki context already contains draft/probable links for `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` as parents of `Tulio Cesar Luis Jose`, but the current draft raises enough row-level conversion conflict that no additional canonical action should be taken from this bdb698de draft.
7. This source does not name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`; any Dario-line bridge remains unsupported here.

## Literal Evidence

- Current staged conflict literal support: entry 513 converted transcript gives `José del Carmen Pulgar`, `Juana de Dios Amador de Pulgar`, and `José del C. Pulgar`; entry 515 converted transcript gives `Rosa Elvira del Carmen` and `Pedro Pablo Leiva`.
- Current source packet says entry 513 is family-relevant because it contains `Pulgar` in the father and declarant fields, but it must be held because child name, birth details, and mother surname conflict with image-reviewed evidence.
- Current source packet says entry 515 is included only because proof review requested continued hold/reconciliation; it is not used to support the Pulgar family narrative.
- Current converted file and chunk for `CHUNK-bdb698de8106-P0001-01` transcribe entry 513 as `Isolina del Carmen / José`, male, born at `Calle Colon`, with father `José del Carmen Pulgar`, mother `Juana de Dios Amador de Pulgar`, and declarant `José del C. Pulgar`, father, age forty-seven, farmer, domiciled `Calle Colon`.
- Existing staged atomic claims for the same source page preserve a conflicting image-reviewed direction: entry 513 child field begins with a `Pulgar Ama...` surname line and a `José ...` given-name line; father `Jose del Carmen Pulgar`; mother most likely `Juana de Dios Amagada de Pulgar`, while still held for targeted QA.
- Existing canonical/wiki context has `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, and `Tulio Cesar Luis Jose` pages with draft/probable relationship evidence from older reviewed page-172 entry-513 material. It also has separate pages for `Juana Arriagada de Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Dario Arturo Pulgar-Smith`, and `Darío Pulgar Arriagada`.

## Interpretation Boundary

The current bdb698de draft supports only a held conflict finding: entry 513 likely concerns a Pulgar-family row, and the father/declarant field is the strongest part of the derivative reading. It does not settle the child identity, the mother's exact surname, the child-parent relationship endpoint, or any Dario-line connection. The older promoted/reviewed entry-513 context is relevant conflict context, not permission to silently correct this draft.

## Hypotheses

### 1. Entry 513 Father And Declarant Are The Same Page-Local Man, `Jose del Carmen Pulgar` / `Jose del C. Pulgar`

Supporting evidence:

- The same row names father `José del Carmen Pulgar`.
- The declarant field reads `José del C. Pulgar`, identifies him as `Padre`, gives age forty-seven, occupation farmer, and domicile `Calle Colon`.
- The father field and declarant field share name, role, occupation, and residence context.

Conflicts and cautions:

- Same-row father/declarant identity is strong, but the row itself is not conversion-stable.
- Do not promote father attributes or approximate birth year until entry 513 is QA-certified.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.82 | Same-row abbreviation plus role/residence strongly supports same page-local person. |
| conflict_severity | 0.42 | Main risk is premature promotion while row fields are conflicted. |
| evidence_quality | 0.62 | Civil register derivative evidence is direct, but current draft is low-confidence. |
| conversion_confidence | 0.55 | Father/declarant reading is comparatively stable, but the row is not. |
| claim_probability | 0.84 | Likely same person within entry 513. |
| relevance | 0.95 | Directly controls Pulgar-line father/declarant handling. |
| canonical_readiness | 0.20 | Hold until targeted conversion QA and proof review. |

### 2. Current Entry 513 Is The Same Underlying Row As The Older `Tulio Cesar Luis Jose` / `Juana de Dios Amagada de Pulgar` Cluster

Supporting evidence:

- Both contexts point to the same source image, register page 172, entry 513, Los Angeles/La Laja birth register, 1889.
- Older staged/reviewed relationship material reports `Tulio Cesar Luis Jose` with father `Jose del Carmen Pulgar` and mother `Juana de Dios Amagada de Pulgar`.
- Current later staged claims for the same page say image review appears closer to a `Pulgar Ama...` child surname line and an `Amagada` mother reading than to the current converted `Isolina del Carmen / José` and `Amador`.

Conflicts and cautions:

- The current assigned converted file/chunk read `Isolina del Carmen / José` and `Juana de Dios Amador de Pulgar`.
- Existing wiki relationship pages report older proof review as high confidence, but later staged tasks explicitly call for targeted conversion QA on this same source and row.
- Treat this as a row-control conflict, not a completed correction.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.64 | Same source/page/entry strongly links the clusters, but literal row fields disagree. |
| conflict_severity | 0.86 | Child endpoint and mother surname control person/relationship promotion. |
| evidence_quality | 0.58 | Multiple local staged files exist, but they disagree and include derivative readings. |
| conversion_confidence | 0.38 | Current draft labels confidence low and asks for conversion QA. |
| claim_probability | 0.60 | Plausible that this is the same row under conflicting transcriptions. |
| relevance | 1.00 | This is the central identity conflict for entry 513. |
| canonical_readiness | 0.10 | No new canonical action from this draft. |

### 3. Mother Candidate Is `Juana de Dios Amagada de Pulgar`, Not Current Converted `Amador`

Supporting evidence:

- Existing wiki/staged relationship context preserves `Juana de Dios Amagada de Pulgar`.
- Later staged atomic claims for the same source say image review appears closer to `Juana de Dios Amagada de Pulgar` than `Amador`, while still requiring targeted crop QA.
- The child surname line in image-review notes appears to begin `Pulgar Ama...`, which is compatible with an `Amagada` maternal surname hypothesis.

Conflicts and cautions:

- The current converted file and current bdb698de source packet quote `Juana de Dios Amador de Pulgar`.
- `Amagada`, `Amador`, and any `Arriagada`-style reading must remain literal-reading alternatives until QA certifies the handwriting.
- Married form `de Pulgar` does not establish birth surname or same-person identity beyond this row.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.52 | Local context favors `Amagada`, but current assigned derivative text conflicts. |
| conflict_severity | 0.88 | Wrong surname would create a false mother identity or merge. |
| evidence_quality | 0.50 | Evidence is local and direct but not transcription-stable. |
| conversion_confidence | 0.32 | The exact surname is the key unresolved conversion issue. |
| claim_probability | 0.56 | Slightly favored by image-review notes, not proof-ready. |
| relevance | 0.98 | Controls mother identity and child surname interpretation. |
| canonical_readiness | 0.00 | Hold for targeted crop/field QA. |

### 4. Mother Candidate Is Literal Current Converted `Juana de Dios Amador de Pulgar`

Supporting evidence:

- The current converted file, chunk, and bdb698de source packet literally quote `Juana de Dios Amador de Pulgar`.
- The staged conflict correctly preserves this derivative reading rather than silently replacing it.

Conflicts and cautions:

- Multiple later staged notes say image review appears closer to an `Amagada` or related reading.
- No existing wiki page for `Juana de Dios Amador de Pulgar` was found in the reviewed context.
- This should remain a transcription alternative, not a new canonical mother page.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.34 | Supported by current derivative text only. |
| conflict_severity | 0.82 | Promotion would conflict with existing Juana candidate handling. |
| evidence_quality | 0.42 | Direct but derivative and contradicted by image-review notes. |
| conversion_confidence | 0.28 | Exact surname is explicitly low-confidence. |
| claim_probability | 0.30 | Possible, but not currently favored. |
| relevance | 0.94 | Must be preserved as an unresolved reading. |
| canonical_readiness | 0.00 | Do not promote or create a new identity. |

### 5. Entry 515 Converted `Rosa Elvira del Carmen` / `Pedro Pablo Leiva` Is A Separate Non-Pulgar Row

Supporting evidence:

- Current converted file and staged conflict quote entry 515 as `Rosa Elvira del Carmen` with father/declarant `Pedro Pablo Leiva`.
- The source packet says entry 515 is not used to support the Pulgar family narrative.

Conflicts and cautions:

- Other staged/image-reviewed evidence reads the entry 515 child/father differently, including `Neira` alternatives and bottom-crop limitations.
- Entry 515 should not be used as negative or positive evidence for Pulgar-line identity.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.26 | Derivative entry-515 reading is materially conflicted. |
| conflict_severity | 0.60 | Non-Pulgar row, but row spillover could contaminate entry 513. |
| evidence_quality | 0.36 | Bottom-cropped/partial support. |
| conversion_confidence | 0.20 | Staged draft flags unresolved derivative reading. |
| claim_probability | 0.24 | Current literal reading only, not proof-ready. |
| relevance | 0.45 | Relevant mainly for row-boundary control. |
| canonical_readiness | 0.00 | No promotion. |

### 6. Same Person Or Lineage Bridge To `Dario Arturo Pulgar-Smith` / `Dario Arturo Pulgar`

Supporting evidence:

- Existing wiki context has `Dario Arturo Pulgar-Smith` as Alexander John Heinz's maternal grandfather from family-supplied knowledge.
- Existing staged CV context uses document-level `Dario Arturo Pulgar`.
- Entry 513 has a Pulgar father candidate, so it may later be useful Pulgar-line context if QA confirms the row.

Conflicts and cautions:

- This source does not name `Dario`, `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, spouse, child, grandchild, or any CV bridge.
- Name overlap through `Pulgar` is not identity evidence.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.04 | No direct Dario evidence in this row. |
| conflict_severity | 0.78 | High false-merge risk to family-supplied canonical Dario. |
| evidence_quality | 0.20 | Only broad surname context. |
| conversion_confidence | 0.38 | Base row is not QA-stable. |
| claim_probability | 0.03 | Unsupported by this source. |
| relevance | 0.76 | Required anti-conflation check. |
| canonical_readiness | 0.00 | No attachment to Pulgar-Smith or CV subject. |

### 7. Same Person Or Variant Bridge To `Dario Jose Pulgar-Arriagada` Or `Dario/Darío Pulgar Arriagada`

Supporting evidence:

- Existing wiki/staging context preserves separate Dario/Pulgar-Arriagada candidates.
- Existing Jose/Juana Pulgar-line records may eventually help build lineage, if independently bridged.

Conflicts and cautions:

- Entry 513 does not name any Dario candidate.
- Entry 513 mother surname uncertainty cannot be used to infer `Arriagada` or bridge to Pulgar-Arriagada Dario candidates.
- Existing `Darío Pulgar Arriagada` legal-notice context is chronologically and evidentially separate.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | No Dario name or bridge in the current source. |
| conflict_severity | 0.80 | High risk of conflating generations and surname variants. |
| evidence_quality | 0.18 | Only external wiki context and broad surname overlap. |
| conversion_confidence | 0.38 | Underlying entry remains conflicted. |
| claim_probability | 0.02 | Unsupported here. |
| relevance | 0.74 | Required Pulgar-line comparison. |
| canonical_readiness | 0.00 | Do not merge, variant-link, or attach. |

## Ranked Conclusion

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Entry 513 father and declarant are the same page-local `Jose del Carmen Pulgar` / `Jose del C. Pulgar`. | 0.84 | Targeted conversion QA must certify the row and then proof review the father/declarant claim. |
| 2 | Current bdb698de entry 513 and older `Tulio Cesar Luis Jose` / `Juana de Dios Amagada de Pulgar` materials refer to the same underlying register row under conflicting transcriptions. | 0.60 | Conversion QA must reconcile current converted/chunk files, image-review notes, and older staged relationship material for entry 513. |
| 3 | Mother surname is best held as unresolved, with `Juana de Dios Amagada de Pulgar` slightly favored over `Amador` by local image-review context. | 0.56 | Targeted crop/field QA must decide `Amador`, `Amagada`, `Arriagada`, or `[...] [?]`. |
| 4 | Literal current converted mother reading `Juana de Dios Amador de Pulgar` is correct. | 0.30 | Preserve as an alternative until QA; do not create or merge a person. |
| 5 | Entry 515 current `Rosa Elvira del Carmen` / `Pedro Pablo Leiva` reading is stable. | 0.24 | Reconcile entry 515 row only enough to prevent spillover; no Pulgar promotion. |
| 6 | Entry 513 bridges to `Dario Arturo Pulgar-Smith` or `Dario Arturo Pulgar`. | 0.03 | Require a separate source naming the Dario relationship or a proof-reviewed lineage bridge after entry-513 QA. |
| 7 | Entry 513 bridges to `Dario Jose Pulgar-Arriagada` or `Dario/Darío Pulgar Arriagada`. | 0.02 | Require independent proof linking the Jose/Juana candidate cluster to a named Dario candidate. |

## Conflict Summary

- Same-person conflict: `Jose del Carmen Pulgar` and `Jose del C. Pulgar` are likely the same page-local person, but not proof-ready for canonical action from this draft.
- Duplicate-person conflict: do not create a separate `Juana de Dios Amador de Pulgar` or merge it with `Juana de Dios Amagada de Pulgar` before QA.
- Name-variant conflict: active for `Amador` / `Amagada` / possible `Arriagada`; also active for child readings `Isolina del Carmen / José` versus `Tulio Cesar Luis Jose` or `Pulgar Ama... / José ...`.
- Relationship conflict: current bdb698de draft conflicts with older promoted/reviewed `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` parent links to `Tulio Cesar Luis Jose`; hold any new parent-child promotion until the row-control conflict is resolved.
- Chronology conflict: no internal chronology conflict in entry 513; cross-source Dario attachments would create unsupported lineage/chronology risk.

## Recommended Next Action

Keep this staged draft on `hold_for_conversion_qa`. The exact next step is targeted conversion QA for `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`, focused on entry 513 child full name, sex, birth date/time, father/declarant form, father age/profession/residence, and mother full name/surname. The QA result must explicitly decide or preserve uncertainty among `Amador`, `Amagada`, `Arriagada`, and an uncertain form, and must reconcile the current bdb698de transcript with older page-172 entry-513 staged/proof-reviewed materials before any proof-review rerun or canonical promotion.
