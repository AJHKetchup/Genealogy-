---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527194226695
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

- Row control is unresolved for entry `172`. The staged conflict draft and source packet preserve a Pulgar/Arriagada row, while the current converted Markdown for the same referenced source records a Burgos/de la Cruz row as entry `172`.
- The raw source image and job page image are absent in this checkout, matching the blocker reported by the staged conflict draft. I did not run conversion or edit any conversion output.
- The conflict changes the child, both parents, birth date/time/place, and informant. This is not a name-variant or duplicate-person issue.
- The father field under the Pulgar/Arriagada hypothesis is not promotion-ready as `Jose del Carmen Pulgar S.`. Prior local review context supports the father name beginning `Jose del Carmen Pulgar`, with the terminal suffix requiring targeted source-image QA.
- No evidence in this staged draft supports a same-person bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.

## Literal Readings Kept Separate

Staged chunk/source-packet reading:

- Entry `172`; registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Father field in the current chunk: `Jose del Carmen Pulgar S.`
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at Calle de Valdivia.

Current converted Markdown reading:

- Entry `172`; child `José Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant/declarant: `Oswaldo Burgos`.

## Hypotheses And Scores

### H1: Physical entry 172 is the Pulgar/Arriagada row

Evidence supporting:

- The assigned chunk and source packet agree on `Jose del Carmen Segundo Pulgar Arriagada`, father field beginning `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`.
- Local staged proof-review and conversion-review notes for this source repeatedly treat the Pulgar/Arriagada row as the family-relevant reading while holding canonical promotion for conversion QA.
- Existing canonical stubs already carry low-confidence or draft Pulgar/Arriagada evidence for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`; those pages are context only, not promotion authority.

Conflicts / limits:

- The current converted Markdown for the same referenced source contradicts this row assignment.
- The source image is unavailable in this worker's checkout.
- The father's terminal suffix remains unresolved.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.70 | Probable as the intended Pulgar/Arriagada row in staging; not enough for canonical promotion. |
| conflict_severity | 0.95 | Competing readings identify different children and parents. |
| evidence_quality | 0.62 | Useful local staged evidence, but derivative and blocked by missing image access. |
| conversion_confidence | 0.35 | Conversion artifacts materially disagree. |
| claim_probability | 0.76 | Pulgar/Arriagada row is plausible to probable if prior local image-QA context is accepted. |
| relevance | 0.95 | Directly relevant to Pulgar/Arriagada parent-child research. |
| canonical_readiness | 0.20 | Hold for targeted conversion QA and proof review. |

### H2: Current converted Markdown is the controlling entry-172 transcript

Evidence supporting:

- The converted Markdown explicitly labels the Burgos/de la Cruz child as entry `172`.
- It is the current converted Markdown file referenced by the staged draft.

Conflicts / limits:

- It conflicts with the assigned chunk and held source packet.
- It has no Pulgar-line relevance unless conversion QA proves the Pulgar row belongs to a different entry or source.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.20 | Weak as controlling evidence for this Pulgar-line task. |
| conflict_severity | 0.95 | Direct row-level contradiction. |
| evidence_quality | 0.40 | Derivative transcript contradicted by local staged context. |
| conversion_confidence | 0.35 | Current conversion exists but is not reliable enough for promotion. |
| claim_probability | 0.20 | Low probability it should control the Pulgar/Arriagada staging without QA. |
| relevance | 0.10 | Low for Pulgar-line identity analysis. |
| canonical_readiness | 0.10 | Do not promote Burgos/de la Cruz as controlling entry 172 from this task. |

### H3: This is a row/source alignment conflict, not an identity merge

Evidence supporting:

- `Jose del Carmen Segundo Pulgar Arriagada` is not a plausible variant of `José Miguel`.
- `Jose del Carmen Pulgar` is not a plausible variant of `Oswaldo Burgos`.
- `Juana Arriagada de Pulgar` is not a plausible variant of `Concepcion de la Cruz`.
- The competing dates and places describe separate registrations, not one person with spelling variation.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.90 | Strong that the correct workflow is conversion QA, not person merging. |
| conflict_severity | 0.95 | High impact on all downstream claims. |
| evidence_quality | 0.75 | The conflict classification is clear from the staged texts. |
| conversion_confidence | 0.35 | Source-to-derivative control is unsettled. |
| claim_probability | 0.88 | Most likely conclusion is hold-for-conversion-QA. |
| relevance | 0.95 | Directly controls whether entry 172 can support Pulgar claims. |
| canonical_readiness | 0.15 | Not ready until conversion-control decision is recorded. |

## Pulgar-Line Comparison

- `Dario Arturo Pulgar-Smith`: Canonical page is family-supplied as Alexander John Heinz's maternal grandfather and warns against automatic Dario/Pulgar merges. This entry-172 draft gives no `Dario`, `Arturo`, `Smith`, grandchild, spouse, or descendant bridge. Same-person probability with the 1888 child: 0.01.
- `Dario Arturo Pulgar`: Staged CV context elsewhere identifies a document-level `Dario Arturo Pulgar`, but this entry-172 draft has no CV evidence and no bridge to `Pulgar-Smith`. Direct bridge probability: 0.02.
- `Dario Jose Pulgar-Arriagada`: Local staged portrait/name-form context elsewhere names this cluster, but entry 172 does not name `Dario Jose`. Direct bridge probability: 0.02.
- `Dario/Darío Pulgar Arriagada`: Existing wiki/staged context includes later `Darío Pulgar Arriagada` references. Entry 172's child is `Jose del Carmen Segundo Pulgar Arriagada`, not Dario. Direct bridge probability: 0.03.
- `Jose del Carmen Pulgar`: If H1 controls, this is probably the entry-172 father field. Probability as father under H1: 0.80. Probability that the terminal `S.` is ready for canonical use: 0.25.
- `Juana Arriagada de Pulgar`: If H1 controls, this is probably the entry-172 mother field. Probability as mother under H1: 0.82.
- `Juana de Dios Amagada de Pulgar` and related Juana parent candidates: Existing local context treats this as a separate mother candidate in other Pulgar work. Entry 172 reads `Juana Arriagada de Pulgar`, not `Juana de Dios Amagada de Pulgar`; do not merge by name/spouse-family context alone. Same-person probability from this draft alone: 0.25.

## Relationship And Chronology Conflicts

- Parent-child conflict: Under H1, entry 172 supports a held parent-child cluster for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`; under H2, none of those claims belong to entry 172.
- Chronology conflict: H1 gives birth on 8 March 1888; H2 gives birth on 6 April 1888. The divergent dates reinforce that the rows are separate registrations.
- Relationship conflict: Existing `Jose del Carmen Pulgar` and Juana pages may reflect related Pulgar family work, but this draft cannot merge the entry-172 parents with other Jose/Juana candidates.

## Ranked Conclusion

1. Most likely workflow conclusion: hold for conversion QA because entry 172 has a row-level derivative conflict.
2. Most likely identity conclusion if row control is accepted: the Pulgar/Arriagada row concerns `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
3. Most likely father-name boundary: use `Jose del Carmen Pulgar` until targeted image review certifies or rejects the terminal suffix.
4. Least supported action: any merge or identity bridge involving Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Darío Pulgar Arriagada.

## Recommended Next Action

Run targeted conversion QA/proof review against the source image, current converted Markdown, current chunk, and held source packet. The exact next proof-review decision needed is:

1. Decide whether physical entry `172` on register page 58 is the Pulgar/Arriagada row or the Burgos/de la Cruz row.
2. If Pulgar/Arriagada is accepted, certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. Reconcile or supersede the converted Markdown so downstream workers do not treat the Burgos/de la Cruz row as controlling entry `172`.
4. Only after row control is resolved, rerun proof review for the child-name, birth event, residence, and parent-child claims. A separate identity-bridge proof review is required before linking this family to any Dario Pulgar identity.
