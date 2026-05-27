---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527195112545
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527180532740.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register pages 58-59; entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity And Conflict Analysis: Entry 172 Derivative Row Conflict

## Blockers First

- The staged draft reports a material row-control conflict for entry `172`: the assigned chunk reads a Pulgar/Arriagada birth row, while the current converted Markdown reads a Burgos/de la Cruz birth row.
- This analysis did not inspect the original image. The assigned staged draft and held source packet state that the raw source image and job page image were absent for that worker, so this note cannot independently certify physical row control.
- The conflict is not a name variant or same-person issue. The competing readings name different children, different parents, different birth dates and times, different places, and different informants.
- Under the Pulgar/Arriagada reading, the father's terminal suffix is not promotion-ready. The safe held reading is `Jose del Carmen Pulgar`; the final `S.` or other mark requires targeted image QA.
- No evidence reviewed for this exact task directly bridges entry 172 to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.

## Literal Source Readings

Assigned chunk and held source-packet reading:

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Father field in the assigned chunk: `Jose del Carmen Pulgar S.`
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at Calle de Valdivia.

Current converted Markdown reading:

- Entry number: `172`.
- Child: `Jose Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant/declarant: `Oswaldo Burgos`.

Interpretation kept separate: these two readings most likely describe two different register rows or a source/row alignment problem, not alternate readings of one person's name.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Row

Evidence supporting:

- The assigned chunk and held source packet agree on the core Pulgar/Arriagada reading: child `Jose del Carmen Segundo Pulgar Arriagada`, father field beginning `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`.
- Existing canonical wiki stubs include `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`, with low-confidence or draft evidence connected to this entry-172 cluster. Those pages are context only, not independent proof of row control.
- Multiple reviewed local notes found during repository search treat the Pulgar/Arriagada row as the family-relevant reading, while still holding promotion for conversion QA.

Conflicts and limits:

- The current converted Markdown for the same converted file labels entry `172` as a Burgos/de la Cruz row.
- This worker did not visually review the source image.
- The father suffix after `Pulgar` remains unresolved.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.70 | Probable as the intended staged Pulgar/Arriagada row, but not proof-ready. |
| conflict_severity | 0.95 | The alternate reading changes all core identities and event details. |
| evidence_quality | 0.62 | Useful staged derivative evidence, blocked by row-control uncertainty. |
| conversion_confidence | 0.35 | The conversion artifacts materially disagree. |
| claim_probability | 0.76 | Plausible to probable if prior image-reviewed staging is accepted. |
| relevance | 0.95 | Directly relevant to Pulgar/Arriagada parent-child research. |
| canonical_readiness | 0.20 | Hold for conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Row

Evidence supporting:

- The current converted Markdown explicitly labels `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, as entry `172`.
- The converted file is the file referenced by the staged draft and chunk metadata.

Conflicts and limits:

- This reading conflicts with the assigned chunk and held source packet.
- It has no Pulgar-line relevance unless targeted QA proves the Pulgar/Arriagada row belongs to a different entry, page, or source.
- It should not control Pulgar claims without source-image row certification.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.20 | Weak as controlling evidence for this Pulgar-line staging task. |
| conflict_severity | 0.95 | Direct row-level contradiction. |
| evidence_quality | 0.40 | Derivative transcript contradicted by other staged artifacts. |
| conversion_confidence | 0.35 | Not reliable enough for promotion. |
| claim_probability | 0.20 | Low without image-based QA. |
| relevance | 0.10 | Low for the Pulgar-line question. |
| canonical_readiness | 0.10 | Do not promote from this task. |

## Hypothesis 3: Source/Row Alignment Conflict, Not A Person Merge

Evidence supporting:

- `Jose del Carmen Segundo Pulgar Arriagada` is not a plausible variant of `Jose Miguel`.
- `Jose del Carmen Pulgar` is not a plausible variant of `Oswaldo Burgos`.
- `Juana Arriagada de Pulgar` is not a plausible variant of `Concepcion de la Cruz`.
- The dates, places, and informants also differ, supporting a row/source alignment problem rather than a duplicate-person or spelling problem.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.90 | Strong that the immediate issue is conversion QA, not identity merging. |
| conflict_severity | 0.95 | High downstream impact. |
| evidence_quality | 0.75 | The conflict classification is clear from staged texts. |
| conversion_confidence | 0.35 | Source-to-derivative control remains unsettled. |
| claim_probability | 0.88 | Most likely workflow result is hold for conversion QA. |
| relevance | 0.95 | Directly controls all entry-172 claims. |
| canonical_readiness | 0.15 | Not ready until row control is settled. |

## Pulgar-Line Anti-Conflation Review

| Candidate | Evidence in this task | Same-person / bridge probability | Required next step |
| --- | --- | ---: | --- |
| `Dario Arturo Pulgar-Smith` | Canonical page is family-supplied as Alexander John Heinz's maternal grandfather. Entry 172 does not name Dario, Arturo, Smith, Alexander, a spouse, or a descendant. | 0.01 | Do not attach this entry by surname context alone; require a separate identity-bridge proof review after row control. |
| `Dario Arturo Pulgar` | Local staged CV context elsewhere identifies a document-level `Dario Arturo Pulgar`. Entry 172 does not cite the CV or name Dario Arturo. | 0.02 | Compare only after entry-172 row control and a reviewed bridge to the CV subject. |
| `Dario Jose Pulgar-Arriagada` | Local portrait/photo context elsewhere names this cluster. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose`. | 0.02 | Preserve separately pending direct identity-bearing evidence. |
| `Dario/Dario Pulgar Arriagada` | Existing wiki/staged context includes later `Dario Pulgar Arriagada` references. Entry 172 does not name Dario. | 0.03 | Do not merge; require a proof-reviewed identity bridge. |
| `Jose del Carmen Pulgar` | Under the Pulgar/Arriagada hypothesis, this is the father field, with unresolved terminal suffix. | 0.80 as father under H1; 0.25 for suffix readiness | Targeted image QA must certify `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. |
| `Juana Arriagada de Pulgar` | Under the Pulgar/Arriagada hypothesis, this is the mother field. | 0.82 as mother under H1 | Promote only after row control and proof review. |
| `Juana de Dios Amagada de Pulgar` | Existing canonical/staged context treats this as a separate Juana candidate in other Pulgar work. Entry 172 reads `Juana Arriagada de Pulgar` in the Pulgar/Arriagada reading. | 0.25 same-person from this task alone | Do not merge; compare only through separate proof-reviewed records. |

## Relationship And Chronology Conflicts

- Parent-child conflict: H1 supports a held cluster for child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`; H2 assigns entry `172` to unrelated Burgos/de la Cruz people.
- Chronology conflict: H1 gives birth on 8 March 1888 at about 3 p.m.; H2 gives birth on 6 April 1888 at about 10 p.m.
- Place conflict: H1 gives `Calle de Valdivia`; H2 gives `En esta`.
- Parent-candidate conflict: this task cannot merge `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar`, or attach `Jose del Carmen Pulgar` to other Jose/Pulgar candidates, until row control and identity proof review are complete.

## Ranked Conclusion

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | The task should remain held for conversion QA because row control is unresolved. | 0.88 | Hold all dependent claims, relationships, and identity attachments. |
| 2 | If source-image QA accepts the assigned chunk, entry 172 concerns `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`. | 0.76 | Rerun proof review, then promote only the certified row fields. |
| 3 | The father field should be limited to `Jose del Carmen Pulgar` until the suffix is certified. | 0.80 | Do not promote `S.` without targeted image review. |
| 4 | Any bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada is unsupported by this task alone. | 0.02 | Preserve separate hypotheses; require a separate identity-bridge proof review. |

## Recommended Next Action

Run targeted conversion QA / proof review against the original source image, current converted Markdown, current chunk, and held source packet. The exact next proof-review decisions are:

1. Certify whether physical entry `172` on register page 58 is the Pulgar/Arriagada row or the Burgos/de la Cruz row.
2. If Pulgar/Arriagada controls, certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. Record a correction or supersession note for the conflicting converted Markdown before downstream promotion.
4. Rerun proof review for child identity, birth event, residence context, and parent-child relationships.
5. Require a separate identity-bridge proof review before connecting this family cluster to any Dario Pulgar identity.
