---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527194649697
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

- The controlling row for entry `172` is unresolved. The assigned chunk and held source packet read the entry as a Pulgar/Arriagada registration; the current converted Markdown reads entry `172` as a Burgos/de la Cruz registration.
- This worker did not inspect the original image. The staged draft reports that both the raw source image and job page image are absent from the checkout, so row control cannot be independently certified here.
- The conflict changes the child, both parents, birth date/time/place, and informant. It is not a same-person, duplicate-person, or spelling-variant conflict.
- The father field under the Pulgar/Arriagada reading is not ready as `Jose del Carmen Pulgar S.`. The safe held reading is only that the field begins `Jose del Carmen Pulgar`, with any terminal suffix requiring targeted image QA.
- No source in this task directly links the entry-172 child or parents to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.

## Literal Source Readings

Assigned chunk / held source-packet reading:

- Entry: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Father field in the assigned chunk: `Jose del Carmen Pulgar S.`
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at Calle de Valdivia.

Current converted Markdown reading:

- Entry: `172`.
- Child: `Jose Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant/declarant: `Oswaldo Burgos`.

## Hypotheses

### H1: Entry 172 Is The Pulgar/Arriagada Row

Evidence supporting:

- The assigned chunk and held source packet agree on `Jose del Carmen Segundo Pulgar Arriagada`, father field beginning `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`.
- Prior local staged context for this source repeatedly treats Pulgar/Arriagada as the family-relevant row while holding promotion for conversion QA.
- Existing canonical stubs contain low-confidence or draft evidence for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`; those pages are context only, not proof of row control.

Conflicts and limits:

- The current converted Markdown for the same source assigns entry `172` to a different Burgos/de la Cruz child.
- The original image is unavailable to this worker.
- The father's terminal suffix remains unresolved.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.70 | Probable as the intended staged Pulgar/Arriagada row, not promotion-ready. |
| conflict_severity | 0.95 | The competing readings identify different children and parents. |
| evidence_quality | 0.62 | Useful staged derivative evidence, blocked by missing image access. |
| conversion_confidence | 0.35 | Conversion artifacts materially disagree. |
| claim_probability | 0.76 | Plausible to probable if prior image-reviewed staging is accepted. |
| relevance | 0.95 | Directly relevant to Pulgar/Arriagada parent-child research. |
| canonical_readiness | 0.20 | Hold for targeted conversion QA and proof review. |

### H2: Entry 172 Is The Burgos/de la Cruz Row

Evidence supporting:

- The current converted Markdown explicitly labels the Burgos/de la Cruz child as entry `172`.
- The converted file is referenced by the staged draft and chunk metadata.

Conflicts and limits:

- This reading conflicts with the assigned chunk and held source packet.
- It has no Pulgar-line relevance unless targeted QA proves the Pulgar row belongs to another entry/source.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.20 | Weak as controlling evidence for this Pulgar-line staging task. |
| conflict_severity | 0.95 | Direct row-level contradiction. |
| evidence_quality | 0.40 | A derivative transcript contradicted by other local staged artifacts. |
| conversion_confidence | 0.35 | Existing conversion is not reliable enough for promotion. |
| claim_probability | 0.20 | Low without image-based QA. |
| relevance | 0.10 | Low for the Pulgar-line issue. |
| canonical_readiness | 0.10 | Do not promote from this task. |

### H3: The Problem Is Source/Row Alignment, Not A Person Merge

Evidence supporting:

- `Jose del Carmen Segundo Pulgar Arriagada` is not a plausible variant of `Jose Miguel`.
- `Jose del Carmen Pulgar` is not a plausible variant of `Oswaldo Burgos`.
- `Juana Arriagada de Pulgar` is not a plausible variant of `Concepcion de la Cruz`.
- The birth dates, birth places, and informants differ, indicating separate registrations rather than spelling variation.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.90 | Strong that the next step is conversion QA, not identity merging. |
| conflict_severity | 0.95 | High downstream impact. |
| evidence_quality | 0.75 | The conflict classification is clear from the staged texts. |
| conversion_confidence | 0.35 | Source-to-derivative control remains unsettled. |
| claim_probability | 0.88 | Most likely conclusion is hold-for-conversion-QA. |
| relevance | 0.95 | Directly controls all entry-172 Pulgar claims. |
| canonical_readiness | 0.15 | Not ready until row control is settled. |

## Pulgar-Line Anti-Conflation Review

| Candidate | Evidence in this task | Same-person / bridge probability | Required next step |
| --- | --- | ---: | --- |
| `Dario Arturo Pulgar-Smith` | Canonical page is family-supplied as Alexander John Heinz's maternal grandfather; entry 172 does not name Dario, Arturo, Smith, a spouse, descendant, or Alexander. | 0.01 | Separate identity-bridge proof review after row control; do not attach this entry by surname context alone. |
| `Dario Arturo Pulgar` | Local staged CV context elsewhere identifies a document-level `Dario Arturo Pulgar`; this entry does not cite the CV or name Dario. | 0.02 | Compare only after entry-172 row control and a reviewed bridge to the CV subject. |
| `Dario Jose Pulgar-Arriagada` | Local portrait/photo context elsewhere names this cluster; entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. | 0.02 | Preserve separately pending direct identity-bearing evidence. |
| `Dario/Dario Pulgar Arriagada` | Existing wiki/staged context includes later Dario Pulgar Arriagada references; entry 172 names a different child. | 0.03 | Do not merge; require a proof-reviewed identity bridge. |
| `Jose del Carmen Pulgar` | Under H1, this is likely the father field, but the terminal `S.` is unresolved. | 0.80 as father under H1; 0.25 for suffix readiness | Targeted image QA must certify `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. |
| `Juana Arriagada de Pulgar` | Under H1, this is likely the mother field. | 0.82 as mother under H1 | Promote only after row control and proof review. |
| `Juana de Dios Amagada de Pulgar` | Existing canonical/staged context treats this as a separate Juana candidate in other Pulgar work. Entry 172 reads `Juana Arriagada de Pulgar`. | 0.25 same-person from this task alone | Do not merge; compare only through separate proof-reviewed records. |

## Relationship And Chronology Conflicts

- Parent-child conflict: H1 supports a held cluster for child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`; H2 assigns entry `172` to unrelated Burgos/de la Cruz people.
- Chronology conflict: H1 gives birth on 8 March 1888 at about 3 p.m.; H2 gives birth on 6 April 1888 at about 10 p.m.
- Relationship conflict: Existing Jose/Juana Pulgar pages contain other draft or low-confidence relationships, but this task cannot merge the entry-172 parents with other Jose/Juana candidates.

## Ranked Conclusion

1. Most likely workflow conclusion: hold all entry-172 claims for targeted conversion QA.
2. Most likely identity conclusion if row control accepts H1: the row concerns `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
3. Most likely father-name boundary: use only `Jose del Carmen Pulgar` until the suffix is certified.
4. Least supported action: any canonical merge or bridge involving Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada.

## Recommended Next Action

Run targeted conversion QA / proof review against the original source image, current converted Markdown, current chunk, and held source packet. The exact next decisions needed are:

1. Certify whether physical entry `172` on register page 58 is the Pulgar/Arriagada row or the Burgos/de la Cruz row.
2. If Pulgar/Arriagada controls, certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. Record a correction or supersession note for the conflicting converted Markdown before downstream promotion.
4. Rerun proof review for child identity, birth event, residence context, and parent-child relationships.
5. Require a separate identity-bridge proof review before connecting this family cluster to any Dario Pulgar identity.
