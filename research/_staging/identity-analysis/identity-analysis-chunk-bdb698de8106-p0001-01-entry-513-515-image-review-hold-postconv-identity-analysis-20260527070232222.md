---
type: identity_conflict_analysis
status: hold
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-image-review-hold-postconv-evidence-extraction-20260527045039396.md"
worker: postconv-identity-analysis-20260527070232222
staged_draft: research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-image-review-hold-postconv-evidence-extraction-20260527045039396.md
source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260527045039396.md
relationship_draft: research/_staging/relationships/chunk-bdb698de8106-p0001-01-513-child-parents-image-review-hold-postconv-evidence-extraction-20260527045039396.md
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
page_reference: page 1; register page 172; entries 513-515
canonical_readiness: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Entry 513-515 Image-Review Hold

## Blockers

1. The exact staged draft under review is `research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-image-review-hold-postconv-evidence-extraction-20260527045039396.md`.
2. Entry 513 is not conversion-stable. The derivative transcript reads child `Isolina del Carmen / Jose`, sex `Masculino`, mother `Juana de Dios Amador de Pulgar`, and birth time `a las cuatro de la mañana`; image-review notes instead see a child-name field beginning with `Pulgar`, uncertain `Rosa Da[?]` or similar, a line `Jose`, mother `Juana de Dios Ama[?]gar` or `Ama[?]gada de Pulgar`, and birth time closer to `a las cuatro i media de tarde`.
3. The child identity endpoint is unresolved. Do not create, merge, or attach a child identity from this draft.
4. The mother surname is unresolved among at least derivative `Amador`, image-reviewed `Ama[?]gar` / `Ama[?]gada`, and the broader local risk of incorrectly normalizing to `Arriagada`.
5. Entry 515 is boundary-control only. It is a separate lower row and provides no Pulgar-family identity evidence for this task.
6. Existing canonical pages already contain draft/probable context for `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Tulio Cesar Luis Jose`, `Jose del Carmen Segundo Pulgar Arriagada`, and `Juana Arriagada de Pulgar`; this draft does not authorize a new merge or promotion against those pages.
7. This source does not name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Darío Pulgar Arriagada`. Pulgar-line family context justifies an anti-conflation check only.

## Literal Evidence

- The staged conflict draft preserves the derivative reading `513 converted: Nombre. Isolina del Carmen / Jose ... Sexo. Masculino` and the image-reviewed alternative `child name appears to begin Pulgar Rosa ...; Sexo. Masculino`.
- The staged conflict draft preserves derivative mother `Juana de Dios Amador de Pulgar` and image-reviewed mother `Juana de Dios Ama[?]gar / Ama[?]gada de Pulgar`.
- The source packet states entry 513 is relevant because father/declarant fields identify `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, but it says the child identity, birth details, and mother surname are not stable enough for promotion.
- The related relationship draft names the child as unresolved and parents as `Jose del Carmen Pulgar` and `Juana de Dios Ama[?]gar or Ama[?]gada de Pulgar; converted transcript reads Juana de Dios Amador de Pulgar`, with confidence `0.35` and `hold_for_conversion_qa`.
- Local conversion-review notes for the same source/page also report father `Jose del Carmen Pulgar`, declarant `Jose del C. Pulgar`, mother close to `Juana de Dios Ama[?]gada de Pulgar`, and a child field beginning with `Pulgar`; they continue to require targeted QA.
- Canonical `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, and `Tulio Cesar Luis Jose` pages contain draft family links from reviewed evidence, but those pages do not settle this newer bdb698de image-review hold.
- Canonical `Dario Arturo Pulgar-Smith` is family-supplied and explicitly warns not to merge similarly named Pulgar records without identity review. Canonical `Darío Pulgar Arriagada` is a separate 2000 expropriation-event stub.

## Interpretation Boundary

Entry 513 likely concerns a Pulgar-family birth-register row, and the father/declarant reading is the strongest same-row identity evidence. The draft does not settle the child name, mother surname, parent-child relationship endpoint, or any Dario-line bridge. Existing family or wiki context cannot silently correct the literal uncertainty in this row.

## Hypotheses

### 1. Entry 513 Father And Declarant Are The Same Page-Local Man

Hypothesis: `Jose del Carmen Pulgar` in the father field and `Jose del C. Pulgar` in the declarant field identify the same page-local person.

Supporting evidence:

- Both names occur in entry 513.
- The declarant is identified as `Padre`.
- The father/declarant context shares residence `Calle Colon` and profession `Agricultor` in the reviewed notes.

Conflicts and cautions:

- The row remains low-confidence for conversion overall.
- Do not promote age, occupation, residence, or parent relationship until QA certifies the row.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.84 | Same-row full-name/abbreviated-name pattern plus `Padre` is strong. |
| conflict_severity | 0.40 | Identity is likely, but promotion risk remains because adjacent fields are unstable. |
| evidence_quality | 0.66 | Direct register evidence, supported by multiple local notes. |
| conversion_confidence | 0.56 | Father/declarant is comparatively strong inside a low-confidence row. |
| claim_probability | 0.86 | Likely same person within entry 513. |
| relevance | 0.98 | Directly controls the Pulgar parent/declarant candidate. |
| canonical_readiness | 0.20 | Hold for conversion QA and proof review. |

### 2. Entry 513 Is The Same Underlying Row As The Existing `Tulio Cesar Luis Jose` Cluster

Hypothesis: The current bdb698de entry 513 conflict and existing canonical/staged `Tulio Cesar Luis Jose` with parents `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` refer to the same register row under conflicting transcriptions.

Supporting evidence:

- Both contexts concern entry 513 on register page 172 of the 1889 Los Angeles birth register source image.
- Both include father `Jose del Carmen Pulgar`.
- Existing canonical pages show draft links among `Tulio Cesar Luis Jose`, `Jose del Carmen Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Image-review notes are closer to a `Pulgar ... / Jose` child-name structure and an `Ama[?]gada` mother reading than to the derivative `Isolina del Carmen / Jose` and `Amador` reading.

Conflicts and cautions:

- The current draft does not literally certify `Tulio Cesar Luis Jose`.
- The child field remains materially conflicted, including `Isolina del Carmen / Jose`, `Pulgar Rosa ...`, and other older local readings.
- Treat this as row-control conflict context, not as a completed identity merge.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Same source/page/entry and father are strong, but child text is unresolved. |
| conflict_severity | 0.88 | Wrong child endpoint would corrupt person and relationship pages. |
| evidence_quality | 0.58 | Local evidence is relevant but internally inconsistent. |
| conversion_confidence | 0.34 | The draft explicitly labels conversion confidence low. |
| claim_probability | 0.58 | Plausible same row, not proof-ready. |
| relevance | 1.00 | Central conflict for entry 513. |
| canonical_readiness | 0.08 | No new canonical action from this draft. |

### 3. Mother Candidate Is `Juana de Dios Ama[?]gada de Pulgar` / Existing `Juana de Dios Amagada de Pulgar`

Hypothesis: The mother in entry 513 is the same person represented by the existing canonical stub `Juana de Dios Amagada de Pulgar`.

Supporting evidence:

- Image-review notes repeatedly favor `Ama[?]gada de Pulgar` or similar over derivative `Amador`.
- Existing canonical context has `Juana de Dios Amagada de Pulgar` as a draft parent of `Tulio Cesar Luis Jose`.
- The current relationship draft preserves `Ama[?]gar or Ama[?]gada` rather than promoting `Amador`.

Conflicts and cautions:

- The exact letters remain unresolved; `Ama[?]gada` is not a certified reading in this assignment.
- Do not infer `Arriagada` from the broader Pulgar-line context.
- Married form `de Pulgar` is not enough to prove duplicate identity.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.55 | Locally favored but still image-sensitive. |
| conflict_severity | 0.86 | A mistaken surname would create a false mother identity or duplicate merge. |
| evidence_quality | 0.54 | Direct row evidence plus existing context, but no final QA. |
| conversion_confidence | 0.30 | Mother surname is a named blocker. |
| claim_probability | 0.56 | Slightly favored over `Amador`, still uncertain. |
| relevance | 0.98 | Controls mother identity and relationship handling. |
| canonical_readiness | 0.00 | Hold; do not update the canonical page. |

### 4. Mother Candidate Is Derivative `Juana de Dios Amador de Pulgar`

Hypothesis: The derivative transcript reading `Juana de Dios Amador de Pulgar` is correct and represents a separate or differently named mother candidate.

Supporting evidence:

- The converted/chunk-derived text and staged conflict preserve `Amador`.
- This reading must remain in the evidence file as a literal alternative.

Conflicts and cautions:

- The source packet and conversion-review notes state `Amador` is not visually secure.
- No reviewed canonical page for `Juana de Dios Amador de Pulgar` was identified in the checked context.
- Do not create a new person or merge with `Amagada` from this draft.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.32 | Supported mainly by derivative text now under challenge. |
| conflict_severity | 0.82 | Promotion could create a false duplicate or wrong mother. |
| evidence_quality | 0.40 | Direct but derivative and contradicted by image review. |
| conversion_confidence | 0.26 | Exact surname is explicitly unstable. |
| claim_probability | 0.28 | Possible but currently not favored. |
| relevance | 0.94 | Must be preserved as an unresolved reading. |
| canonical_readiness | 0.00 | No promotion. |

### 5. Entry 513 Connects To `Jose del Carmen Segundo Pulgar Arriagada` / `Juana Arriagada de Pulgar`

Hypothesis: Entry 513 is related to the separate entry-172 Pulgar/Arriagada cluster involving child `Jose del Carmen Segundo Pulgar Arriagada` and mother `Juana Arriagada de Pulgar`.

Supporting evidence:

- Both are Pulgar-line birth-register contexts from Los Angeles/La Laja.
- Existing canonical pages for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` preserve separate reviewed evidence.
- Entry 513's mother uncertainty includes a risk of mistaken normalization toward an Arriagada-like surname.

Conflicts and cautions:

- Entry 513 does not certify `Arriagada`.
- The known `Jose del Carmen Segundo Pulgar Arriagada` cluster is tied to another entry/page context and birth date, not this entry 513 hold.
- Similar father and surname context is not enough for a duplicate-person or parent merge.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Broad Pulgar/Jose/Juana overlap only. |
| conflict_severity | 0.78 | High risk of conflating nearby Pulgar-line register rows. |
| evidence_quality | 0.42 | Existing local records are real but not a bridge for this row. |
| conversion_confidence | 0.30 | Entry 513 surname field remains unresolved. |
| claim_probability | 0.14 | No direct bridge from this draft. |
| relevance | 0.76 | Required anti-conflation comparison. |
| canonical_readiness | 0.00 | Do not merge or attach. |

### 6. Entry 515 Is A Separate Non-Pulgar Boundary Row

Hypothesis: Entry 515 should be used only to prevent row spillover and should not affect Pulgar-family identity analysis.

Supporting evidence:

- The source packet says entry 515 is retained only as row-boundary control.
- The staged conflict says entry 515 is a separate lower row.
- Image review reports entry 515 father/declarant appears to be `Pedro Pablo Neira`, not a Pulgar candidate.

Conflicts and cautions:

- Entry 515 also has derivative/read conflicts, including `Leiva` versus `Neira`.
- No entry 515 person or relationship claim should be promoted from this task.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.34 | Enough to treat as separate boundary control, not enough for identity work. |
| conflict_severity | 0.56 | Spillover could contaminate entry 513, but it is not central Pulgar evidence. |
| evidence_quality | 0.38 | Partial/boundary evidence only. |
| conversion_confidence | 0.24 | Entry 515 fields also conflict. |
| claim_probability | 0.70 | Probable separate non-Pulgar row for this task's purpose. |
| relevance | 0.50 | Relevant mainly as row-control evidence. |
| canonical_readiness | 0.00 | No promotion. |

### 7. Bridge To `Dario Arturo Pulgar-Smith` Or `Dario Arturo Pulgar`

Hypothesis: Entry 513 provides evidence for the identity of `Dario Arturo Pulgar-Smith` or the staged CV subject `Dario Arturo Pulgar`.

Supporting evidence:

- The row likely belongs somewhere in a broad Pulgar family context if QA confirms it.
- Canonical `Dario Arturo Pulgar-Smith` and staged CV materials are existing Pulgar-line comparison targets.

Conflicts and cautions:

- Entry 513 does not name Dario, Arturo, Smith, Pulgar-Smith, Alexander John Heinz, a spouse, child, grandchild, CV, or migration/work-history context.
- Surname overlap alone is not identity evidence.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.04 | No direct Dario evidence. |
| conflict_severity | 0.80 | High false-attachment risk to family-supplied canonical Dario. |
| evidence_quality | 0.20 | Only broad surname context. |
| conversion_confidence | 0.30 | Base row is not QA-stable. |
| claim_probability | 0.03 | Unsupported by this source. |
| relevance | 0.74 | Required Pulgar-line anti-conflation check. |
| canonical_readiness | 0.00 | No attachment. |

### 8. Bridge To `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, Or `Darío Pulgar Arriagada`

Hypothesis: Entry 513 supports a same-person, name-variant, or lineage bridge to a Dario Pulgar-Arriagada candidate.

Supporting evidence:

- Existing local context contains separate `Dario Jose Pulgar-Arriagada` / `Darío Pulgar Arriagada` candidates.
- The entry 513 mother-name uncertainty makes Arriagada normalization a known risk to check.

Conflicts and cautions:

- Entry 513 does not name any Dario candidate.
- `Ama[?]gada` must not be silently corrected to `Arriagada`.
- Canonical `Darío Pulgar Arriagada` currently rests on a separate 5 December 2000 expropriation event, not this 1889 birth row.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | No Dario or Arriagada bridge in this source. |
| conflict_severity | 0.82 | High risk of conflating surname variants and generations. |
| evidence_quality | 0.18 | Comparison is contextual only. |
| conversion_confidence | 0.30 | Base surname reading is unresolved. |
| claim_probability | 0.02 | Unsupported here. |
| relevance | 0.74 | Required Pulgar-line anti-conflation check. |
| canonical_readiness | 0.00 | Do not merge, variant-link, or attach. |

## Conflict Summary

- Same-person conflict: `Jose del Carmen Pulgar` and `Jose del C. Pulgar` are likely the same page-local person, but the row still needs conversion QA before canonical promotion.
- Duplicate-person conflict: do not create or merge `Juana de Dios Amador de Pulgar`, `Juana de Dios Ama[?]gada de Pulgar`, `Juana de Dios Amagada de Pulgar`, or `Juana Arriagada de Pulgar` from this draft.
- Name-variant conflict: active for `Amador` / `Ama[?]gar` / `Ama[?]gada` / possible but unproven `Amagada` or `Arriagada`; active for child-name alternatives including `Isolina del Carmen / Jose`, `Pulgar Rosa ...`, and older `Tulio Cesar Luis Jose` context.
- Relationship conflict: the father/declarant evidence is stronger than the mother and child evidence, but the child-parent relationship draft correctly remains held at confidence `0.35`.
- Chronology conflict: no internal chronology conflict can be evaluated while the child identity and birth details are unsettled. Any Dario-line attachment would create unsupported lineage/chronology risk.

## Ranked Conclusion

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Entry 513 father and declarant are the same page-local `Jose del Carmen Pulgar` / `Jose del C. Pulgar`. | 0.86 | Targeted conversion QA must certify entry 513 row fields, then proof review the father/declarant claim. |
| 2 | Current entry 513 is the same underlying row as the existing `Tulio Cesar Luis Jose` cluster, under conflicting transcriptions. | 0.58 | Reconcile current bdb698de draft, image-review notes, and older entry-513 materials before any relationship promotion. |
| 3 | Mother is `Juana de Dios Ama[?]gada de Pulgar` / existing `Juana de Dios Amagada de Pulgar`. | 0.56 | Crop/field QA must certify or uncertainty-mark the mother surname. |
| 4 | Derivative `Juana de Dios Amador de Pulgar` is correct. | 0.28 | Preserve as an alternative until QA; do not create or merge a person. |
| 5 | Entry 515 is separate non-Pulgar boundary evidence. | 0.70 for boundary only | Use only for row-control; no identity promotion. |
| 6 | Entry 513 connects to `Jose del Carmen Segundo Pulgar Arriagada` / `Juana Arriagada de Pulgar`. | 0.14 | Require independent proof; do not normalize `Ama[?]gada` to `Arriagada`. |
| 7 | Entry 513 bridges to `Dario Arturo Pulgar-Smith` or `Dario Arturo Pulgar`. | 0.03 | Require a separate reviewed lineage or identity bridge naming Dario. |
| 8 | Entry 513 bridges to `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Darío Pulgar Arriagada`. | 0.02 | Require independent proof linking the Jose/Juana cluster to a named Dario candidate. |

## Recommended Next Action

Keep the staged draft on `hold_for_conversion_qa`. The exact next proof-review gate is targeted conversion QA for entry 513 in `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`, focused on the child full name, sex, birth date/time, father/declarant name and role, father age/profession/residence, and mother full name/surname. The QA result must explicitly decide or preserve uncertainty among `Amador`, `Ama[?]gar`, `Ama[?]gada`, `Amagada`, and `Arriagada` before proof review reruns atomic claims or any canonical page receives new evidence.
