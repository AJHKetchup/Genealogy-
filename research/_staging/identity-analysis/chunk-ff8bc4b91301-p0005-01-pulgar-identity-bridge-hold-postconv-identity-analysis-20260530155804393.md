---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260530155804393
task_id: "identity-analysis:research/_staging/conflicts/chunk-ff8bc4b91301-p0005-01-pulgar-identity-bridge-hold-postconv-evidence-extraction-20260530154508254.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-ff8bc4b91301-p0005-01-pulgar-identity-bridge-hold-postconv-evidence-extraction-20260530154508254.md"
subject: "Pulgar (source-local surname-only Habitat page 5 person)"
source_packet: "research/_staging/source-packets/chunk-ff8bc4b91301-p0005-01-habitat-revisited-pulgar-vancouver-hold-postconv-evidence-extraction-20260530154508254.md"
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/page-0005-chunk-01.md"
chunk_id: "CHUNK-ff8bc4b91301-P0005-01"
page_reference: "page 5"
analysis_status: hold_for_conversion_qa_and_identity_bridge
canonical_readiness: hold
---

# Identity/Conflict Analysis: Habitat Page-5 Pulgar

## Blockers First

1. Exact staged conflict draft analyzed: `research/_staging/conflicts/chunk-ff8bc4b91301-p0005-01-pulgar-identity-bridge-hold-postconv-evidence-extraction-20260530154508254.md`.
2. Conversion/provenance QA blocks promotion. The staged source packet records expected converted SHA `ff8bc4b9130169ba6f4ecc103ba089ba6bf26c7162f5dfebbf3bae9ebd3a7271`, observed live converted SHA `97c8a1cbf4db9e4e39f2044e3260d5938381e2a89583f8e49e6777c77d13444c`, expected chunk SHA `78154f079280b003dbe9fc57c0427a7cb0b00df991dc9c77fd098328072a8584`, and observed live chunk SHA `0c06f927fe30653e7aba9f1a8dc3f2c491b6669abacb42caa3f9c9db76b6504c`.
3. The referenced page image `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0005.jpg` was missing during the evidence-extraction revision, so the page-5 `Pulgar` line is not visually proofed in the current staged review chain.
4. The literal page-5 reading names only `Pulgar`. It does not state `Dario`, `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Jose`, `Juana`, birth, death, parentage, spouse, child, or any family relationship.
5. Same-source pages 7-8 provide useful context for a later bridge to `Dario Pulgar`, but page 5 alone remains surname-only and cannot support a silent correction or merge.
6. No external research was performed. No raw sources, converted Markdown, chunks, source packets, reviewed notes, or canonical wiki pages were edited.

## Literal Evidence Reviewed

From the staged source packet and prepared page-5 chunk:

```text
By the late spring of 1976 it was decided a small group of us, including Pulgar ,
Gyborg, Jane Weiner, and Barbara Janes ... and myself, would go to Vancouver
to help get the show ... "on the air".
```

The page later says:

```text
We arrived in Vancouver on May 19. The Conference was to begin on May 31.
```

Literal reading: page 5 records a surname-only person `Pulgar` in a small audiovisual-program group going to Vancouver in 1976. The later `We arrived` and `our makeshift offices` wording is group/pronoun-chain context, not a repeated named-person assertion.

Interpretation kept separate: the nearby Habitat narrative may make this `Pulgar` the same source-local person as page-7 `Dario Pulgar`, but that requires conversion QA and a separate cross-page identity-bridge proof review.

## Hypothesis 1: Page-Local Surname-Only `Pulgar`

Supporting evidence:

- The staged conflict draft, staged source packet, and prepared chunk all identify the page-5 name as `Pulgar`.
- The sentence directly places `Pulgar` in a small group selected in late spring 1976 for Vancouver Habitat audiovisual work.
- No competing `Pulgar` person appears in the page-5 excerpt.

Conflicts and limits:

- Page image is missing and derivative SHA values conflict.
- `Pulgar` is surname-only and cannot establish a full identity or family connection.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | Good for a source-local surname-only person; not for full identity. |
| conflict_severity | 0.20 | Low if kept local; risk rises with a full-name bridge. |
| evidence_quality | 0.56 | Direct derivative text, but blocked by missing image and SHA mismatch. |
| conversion_confidence | 0.20 | Conversion/provenance QA is explicitly blocked. |
| claim_probability | 0.68 | Probable narrow surname-only mention after QA. |
| relevance | 1.00 | Directly addresses the assigned staged conflict draft. |
| canonical_readiness | 0.02 | Hold; no canonical action. |

## Hypothesis 2: Same Source-Local Person As Habitat Page-7 `Dario Pulgar`

Supporting evidence:

- Same source, same Habitat/Vancouver/UN Habitat Secretariat narrative sequence.
- Page 7 separately names `Dario Pulgar` as a UN Habitat Secretariat confrere and Chilean participant in the Vision Habitat context.
- Page 8 continues with first-name-only `Dario` in the same work-group narrative.

Conflicts and limits:

- Page 5 itself does not give the forename `Dario`.
- Page 7 and page 8 also carry derivative hash or proof-review holds; page 5 has the stronger blocker because the page image is missing.
- Cross-page narrative continuity is a bridge lead, not standalone proof.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.54 | Plausible same-source bridge, still unproofed. |
| conflict_severity | 0.38 | Moderate if only staged; higher if promoted without QA. |
| evidence_quality | 0.50 | Useful same-source context, but all relevant Habitat pieces are held. |
| conversion_confidence | 0.26 | Page 5 is blocked; page 7-8 have derivative-hash cautions. |
| claim_probability | 0.52 | Possible to probable after page-image and cross-page review. |
| relevance | 0.96 | This is the exact suggested follow-up in the staged draft. |
| canonical_readiness | 0.04 | Do not attach canonically yet. |

## Hypothesis 3: Same As Document-Level `Dario Arturo Pulgar` CV Subject

Supporting evidence:

- Staged CV material identifies a document-level `Dario Arturo Pulgar`.
- CV page-9 education/language analysis preserves a possible broader CV/Habitat cluster, and Habitat page 7 describes a Chilean film-distribution background compatible with work-history comparison.

Conflicts and limits:

- Page 5 says only `Pulgar`; it does not state `Dario` or `Arturo`.
- CV page-9 itself does not repeat the subject name and remains held for identity-bridge proof review before canonical attachment.
- No reviewed local source currently links this page-5 surname-only mention to the CV title identity.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.30 | Contextually possible only through other held Habitat/CV material. |
| conflict_severity | 0.56 | Premature attachment could move page-5 group facts to the wrong Dario. |
| evidence_quality | 0.44 | Indirect staged context, not a direct identity statement. |
| conversion_confidence | 0.34 | Both page-5 and CV bridge chains have QA holds. |
| claim_probability | 0.26 | Possible, not proved. |
| relevance | 0.88 | Required Pulgar-line comparison. |
| canonical_readiness | 0.03 | No CV fact promotion from page 5. |

## Hypothesis 4: Same As Canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- Existing canonical `wiki/people/dario-arturo-pulgar-smith.md` is the family-supplied Pulgar-line anchor and names Alexander John Heinz's maternal grandfather.
- The canonical page explicitly warns that records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith should be attached only after identity review.

Conflicts and limits:

- Page 5 says neither `Dario Arturo` nor `Pulgar-Smith`.
- The canonical page is family-supplied context, not proof that every `Pulgar` or `Dario Pulgar` record belongs there.
- Page 5 supplies no grandchild, child, spouse, parent, residence, date of birth, or surname-variant bridge.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Broad surname/context overlap only. |
| conflict_severity | 0.78 | High duplicate-person and family-attachment risk. |
| evidence_quality | 0.38 | Canonical family context is real but not bridging. |
| conversion_confidence | 0.20 | Page-5 provenance is blocked. |
| claim_probability | 0.12 | Not supported by page 5 alone. |
| relevance | 0.90 | Required anti-conflation comparison. |
| canonical_readiness | 0.00 | Do not attach to Pulgar-Smith. |

## Hypothesis 5: Same As `Dario Jose Pulgar-Arriagada` Or `Dario/Dario Pulgar Arriagada`

Supporting evidence:

- Existing staged identity analyses preserve Pulgar-Arriagada clusters, including `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar-Arriagada`, and legal-notice `Dario/Dario Pulgar Arriagada` leads.
- Some Pulgar-Arriagada material has medical or official-listing context and is useful for future family-line review.

Conflicts and limits:

- Page 5 does not state `Arriagada`, `Jose`, `J.`, a medical title, a legal notice, property, parents, or age.
- Existing Pulgar-Arriagada analyses themselves hold those clusters separate unless a bridge source proves continuity.
- Name overlap with `Pulgar` alone is insufficient and risks cross-generation conflation.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | Surname overlap only from this page. |
| conflict_severity | 0.80 | High if a surname-only 1976 Habitat mention is merged into older Pulgar-Arriagada clusters. |
| evidence_quality | 0.36 | Compared evidence is separate and partly held. |
| conversion_confidence | 0.28 | Page-5 QA is blocked; compared clusters have their own QA limits. |
| claim_probability | 0.06 | Not supported from page 5. |
| relevance | 0.84 | Required Pulgar-line comparison. |
| canonical_readiness | 0.00 | No merge or name-variant promotion. |

## Hypothesis 6: Same As Adult Or Child Passenger-List `Dario Pulgar`

Supporting evidence:

- Existing canonical stubs preserve a 1953 adult `Dario Pulgar` passenger aged 64 and a 1953 child `Dario Pulgar` passenger aged 11.
- The child passenger chronology has been treated elsewhere as a possible comparison point for the CV subject, not for page 5 directly.

Conflicts and limits:

- Page 5 gives no age, travel-party, passenger-list context, residence, education chronology, or family relationship.
- The adult passenger aged 64 in 1953 is chronologically unlikely to be the same active Habitat/Vancouver participant in 1976 without strong proof.
- The child passenger remains a possible broader Dario Pulgar lead only if later CV/Habitat identity-bearing sources bridge the names and chronology.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.16 adult; 0.28 child | Child chronology is less implausible, but page 5 gives no direct bridge. |
| conflict_severity | 0.70 | Passenger merges carry substantial duplicate-person and chronology risk. |
| evidence_quality | 0.40 | Passenger evidence is separate and does not identify page-5 `Pulgar`. |
| conversion_confidence | 0.34 | Page-5 QA is blocked; passenger evidence remains scoped separately. |
| claim_probability | 0.08 adult; 0.22 child | Adult weak; child possible only through later bridge evidence. |
| relevance | 0.72 | Useful anti-conflation check. |
| canonical_readiness | 0.00 | No attachment supported. |

## Hypothesis 7: Jose/Juana Parent Candidates Explain This `Pulgar`

Supporting evidence:

- Existing canonical/staged context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- These names matter for future Pulgar-line reconciliation because they may belong to civil-registration clusters involving Pulgar/Arriagada surname patterns.

Conflicts and limits:

- Page 5 names no `Jose`, no `Juana`, and no parent, spouse, child, household, informant, birth, or lineage relationship.
- Jose/Juana materials carry separate row-control, child-name, mother-surname, and conversion-sensitive cautions.
- Family-context hints justify a later double-check only; they do not support parentage or a family merge here.

| metric | score | rationale |
| --- | ---: | --- |
| identity_or_relationship_confidence | 0.03 | No relationship evidence on page 5. |
| conflict_severity | 0.76 | Unsupported parentage would create serious relationship conflicts. |
| evidence_quality | 0.32 | Parent-candidate evidence is separate and conversion-sensitive. |
| conversion_confidence | 0.28 | Page-5 and relevant Jose/Juana clusters have QA limitations. |
| claim_probability | 0.02 | No Jose/Juana claim is supported by this page. |
| relevance | 0.66 | Required Pulgar-line checklist item. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflict Summary

- Same-person evidence: sufficient only for a page-local surname-only `Pulgar` identity aid.
- Duplicate-person risk: high if page-5 `Pulgar` is merged with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, passenger-list `Dario Pulgar` stubs, or Jose/Juana parent candidates by name alone.
- Name-variant evidence: page 5 supports only `Pulgar`. It does not prove `Dario Pulgar`, `Dario Arturo`, `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, or `J.`.
- Relationship-conflict evidence: none on page 5. No parent, spouse, child, sibling, household, or Alexander John Heinz relationship is stated.
- Chronology-conflict evidence: no internal chronology conflict in page 5. Cross-cluster chronology risk appears only if the page-5 1976 Habitat mention is prematurely merged with older medical, passenger, civil-registration, or legal-notice clusters.
- Conversion-confidence conflict: promotion is blocked by the missing page image and live SHA mismatches for the converted file and chunk.

## Ranked Hypotheses

| rank | hypothesis | probability | required next step |
| ---: | --- | ---: | --- |
| 1 | Page-local surname-only `Pulgar` in the 1976 Habitat Vancouver group | 0.68 | Restore/regenerate page image, reconcile SHA mismatch, visually proof page 5. |
| 2 | Same source-local person as Habitat page-7 `Dario Pulgar` | 0.52 | After page-5 QA, run cross-page identity-bridge proof review against pages 7-8. |
| 3 | Same as document-level CV subject `Dario Arturo Pulgar` | 0.26 | Require accepted identity-bearing CV/Habitat bridge before attachment. |
| 4 | Same as child passenger `Dario Pulgar`, age 11 in 1953 | 0.22 | Compare only after CV/Habitat bridge proof; no action from page 5. |
| 5 | Same as canonical `Dario Arturo Pulgar-Smith` | 0.12 | Require explicit reviewed bridge from `Dario Arturo Pulgar` or `Dario Pulgar` to `Pulgar-Smith`. |
| 6 | Same as adult passenger `Dario Pulgar`, age 64 in 1953 | 0.08 | Treat as weak and chronology-risky; no merge. |
| 7 | Same as `Dario Jose Pulgar-Arriagada` or `Dario/Dario Pulgar Arriagada` | 0.06 | Preserve as separate hypotheses; require source naming Arriagada/Jose or a direct bridge. |
| 8 | Jose/Juana parent candidates explain page-5 `Pulgar` | 0.02 | No relationship action; revisit only with a relationship-bearing source. |

## Recommended Next Action

Keep the staged conflict draft at `hold_for_conversion_qa`. The exact next proof-review step is targeted conversion/provenance QA for `CHUNK-ff8bc4b91301-P0005-01`: reconcile the live converted-file and chunk SHA mismatches, restore or regenerate `page-0005.jpg`, and visually proof the page-5 `Pulgar` sentence.

Only after page-5 QA should a separate identity-bridge proof review compare the verified surname-only `Pulgar` against same-source page-7 `Dario Pulgar` and page-8 first-name-only `Dario`. If that cross-page bridge is accepted, a later and separate promotion review can compare the confirmed Habitat `Dario Pulgar` cluster against `Dario Arturo Pulgar`, canonical `Dario Arturo Pulgar-Smith`, the child/adult passenger stubs, Pulgar-Arriagada clusters, and Jose/Juana parent candidates. Do not promote a canonical fact, relationship, name variant, or merge from page 5 alone.
