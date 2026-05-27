---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527193648354
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527180532740.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity And Conflict Analysis: Entry 172 Derivative Row Conflict

## Blockers First

- Row control is not settled in the assigned conflict draft. The assigned chunk reads entry `172` as the Pulgar/Arriagada birth row, while the current converted Markdown reads entry `172` as a Burgos/de la Cruz row.
- This worker did not inspect the raw source image. The assigned conflict draft and source packet state that the raw source image and job page image were absent for that worker.
- The father field must not be promoted as `Jose del Carmen Pulgar S.` from this draft alone. Prior image-reviewed staging notes bound the father to `Jose del Carmen Pulgar` and leave any terminal suffix unresolved.
- Canonical pages already contain low-confidence or draft Pulgar-line evidence. This analysis does not merge people, rename pages, or promote facts.
- No evidence in the assigned entry-172 draft directly bridges `Jose del Carmen Segundo Pulgar Arriagada` to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.

## Literal Source Readings

Assigned chunk / held source-packet reading:

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Father field in the chunk: `Jose del Carmen Pulgar S.`.
- Mother field: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at Calle de Valdivia.

Current converted Markdown reading:

- Entry number: `172`.
- Child: `José Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

Prior staged image-QA context reviewed for comparison:

- `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md` reports direct image review and says the physical row numbered `172` is the Pulgar/Arriagada row.
- That same image-QA note certifies the father only as `Jose del Carmen Pulgar`, not the terminal `S.` suffix.
- `research/_staging/tasks/chunk-b8f4f0490a36-p0001-01-entry-172-proof-review-request-postconv-evidence-extraction-20260527025809657.md` requests proof review before any canonical claim, relationship, merge, or wiki update.

## Hypotheses

### H1: Physical entry 172 is the Pulgar/Arriagada birth row

Evidence supporting:

- The assigned chunk and the assigned held source packet agree on the child `Jose del Carmen Segundo Pulgar Arriagada`, father field beginning `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`.
- Multiple staged image-QA notes report that image review controls in favor of the Pulgar/Arriagada row, not the Burgos/de la Cruz row.
- Existing canonical stubs already reflect a held/probable low-confidence Pulgar/Arriagada cluster: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, and `wiki/people/juana-arriagada-de-pulgar.md`.

Conflicts / limits:

- The current converted Markdown for the same converted file and chunk id gives a different entry-172 family.
- The assigned conflict draft could not certify the image itself.
- The father suffix is unresolved; use `Jose del Carmen Pulgar` for proof-review boundary, not `Jose del Carmen Pulgar S.` as a promoted identity.

Scores:

- Identity confidence: 0.72 for the staged Pulgar/Arriagada row as the likely target of the assigned chunk; 0.45 for canonical use before proof-review acceptance.
- Conflict severity: 0.95, because the competing readings identify different children and parents.
- Evidence quality: 0.62 overall; direct image-QA notes raise support, but this assigned draft is derivative and blocked.
- Conversion confidence: 0.35 for the current converted Markdown as controlling row evidence.
- Claim probability: 0.78 that the physical row-control answer will favor Pulgar/Arriagada if prior image-QA is accepted.
- Relevance: 0.95 to the Pulgar/Arriagada family line.
- Canonical readiness: 0.20; hold until proof review accepts row control and father-field boundary.

### H2: Current converted Markdown is the controlling entry-172 transcript

Evidence supporting:

- The current converted Markdown explicitly labels the Burgos/de la Cruz row as entry `172`.
- It is the current conversion output for the referenced converted file.

Conflicts / limits:

- It conflicts with the assigned chunk, the held source packet, and prior image-QA notes.
- It names a different child, father, mother, birth date/time, place, informant, and official context from the assigned chunk.
- No Pulgar-line claim should be made from this reading.

Scores:

- Identity confidence: 0.20 as the controlling row for this Pulgar-line task.
- Conflict severity: 0.95.
- Evidence quality: 0.40 because it is a derivative transcript contradicted by staged image-QA context.
- Conversion confidence: 0.35.
- Claim probability: 0.20 for canonical control over entry `172`.
- Relevance: 0.10 to the Pulgar line unless conversion QA proves the Pulgar row belongs elsewhere.
- Canonical readiness: 0.10; do not promote Burgos/de la Cruz as entry `172` from this conflict draft.

### H3: The conflict is a row/source alignment problem, not a same-person conflict

Evidence supporting:

- The two readings are not plausible name variants: `Jose del Carmen Segundo Pulgar Arriagada` is not a variant of `Jose Miguel`; `Jose del Carmen Pulgar` is not a variant of `Oswaldo Burgos`; `Juana Arriagada de Pulgar` is not a variant of `Concepcion de la Cruz`.
- The spread-level entry numbers overlap while the row contents diverge. This fits stale conversion output, row shift, wrong image association, or conversion-control drift.

Conflicts / limits:

- Without image access in the assigned draft, this analysis cannot decide the exact cause of the derivative mismatch.

Scores:

- Identity confidence: 0.90 that this is not a duplicate-person or name-variant issue.
- Conflict severity: 0.95.
- Evidence quality: 0.75 for classifying the conflict type from staged text.
- Conversion confidence: 0.35.
- Claim probability: 0.85 that conversion QA, not identity merging, is the correct next workflow.
- Relevance: 0.95.
- Canonical readiness: 0.15 until conversion/proof review resolves the row.

## Pulgar-Line Identity Comparison

- `Dario Arturo Pulgar-Smith`: Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather. No direct evidence in this entry-172 draft links him to `Jose del Carmen Segundo Pulgar Arriagada` or to either parent. Probability of same person with the 1888 child: 0.01; they are different name clusters and the chronology would require evidence not present here.
- `Dario Arturo Pulgar`: Staged CV evidence elsewhere uses this name and repeatedly requires a separate identity-bridge review before attachment to `Dario Arturo Pulgar-Smith` or another Pulgar identity. This entry-172 draft contains no `Dario Arturo Pulgar` evidence. Probability of direct identity bridge from this draft: 0.02.
- `Dario Jose Pulgar-Arriagada`: Existing staged relationship context for a Geneva Convention photograph names this person but states no family relationship. This entry-172 draft gives no Dario Jose evidence. Probability of direct bridge from this draft: 0.02.
- `Dario/Darío Pulgar Arriagada`: Existing wiki context includes `Darío Pulgar Arriagada` in a 2000 expropriation event, and other staged notes mention delegate/institutional contexts. This entry-172 draft gives no evidence that the 1888 child is this person or that the people should be merged. Probability of direct bridge from this draft: 0.03.
- `Jose del Carmen Pulgar`: The assigned chunk and prior image-QA notes support this as the father field for the Pulgar/Arriagada row. Existing wiki context also has a `Jose del Carmen Pulgar` page with another draft child-parent link to `Tulio Cesar Luis Jose`; that could be the same father, but the current entry-172 draft alone cannot merge those family groups. Probability this is the entry-172 father if H1 controls: 0.80; probability the terminal `S.` suffix is promotion-ready: 0.25.
- `Juana Arriagada de Pulgar`: The assigned chunk supports this mother field for entry 172. Existing wiki context already has a low-confidence child link to `Jose del Carmen Segundo Pulgar Arriagada`. Probability this is the entry-172 mother if H1 controls: 0.82.
- `Juana de Dios Amagada de Pulgar` / related Juana parent candidates: Existing wiki/staging context has this separate mother candidate for `Tulio Cesar Luis Jose`. This may be a related or variant Pulgar-family mother cluster, but entry 172's assigned draft reads `Juana Arriagada de Pulgar`, not `Juana de Dios Amagada de Pulgar`. Do not merge these Juana candidates by name or spouse context alone. Probability of same person from this draft alone: 0.25.

## Relationship And Chronology Conflicts

- Parent-child: If H1 is accepted, entry 172 supports `Jose del Carmen Segundo Pulgar Arriagada` as child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`; if H2 controls, none of those relationships belong to entry 172.
- Duplicate-person / name-variant: The Pulgar/Arriagada and Burgos/de la Cruz rows are separate identity clusters, not variants.
- Chronology: The Pulgar/Arriagada row gives birth on 8 March 1888 and registration on 7 April 1888. The Burgos/de la Cruz row gives birth on 6 April 1888. The dates reinforce that the rows are different registrations.
- Canonical collision: Existing canonical pages contain probable/draft evidence generated from entry 172. Because this conflict remains staged, those pages should remain low-confidence and not be expanded from the current draft.

## Ranked Conclusions

1. Most likely workflow conclusion: derivative row-control conflict requiring proof review, not an identity merge.
2. Most likely identity conclusion if row control is accepted: entry 172 concerns `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
3. Most likely father-name boundary: `Jose del Carmen Pulgar`; suffix after `Pulgar` remains unresolved.
4. Least supported action: attaching this entry-172 evidence to any Dario Pulgar identity or using it to merge `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Darío Pulgar Arriagada`.

## Recommended Next Action

Run proof review on the staged image-reviewed row-control packet and conversion-review note, especially:

- `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md`
- `research/_staging/tasks/chunk-b8f4f0490a36-p0001-01-entry-172-proof-review-request-postconv-evidence-extraction-20260527025809657.md`

The exact proof-review decision needed next is:

1. Accept or reject that physical entry `172` on register page 58 is the Pulgar/Arriagada row.
2. If accepted, set the father field boundary to `Jose del Carmen Pulgar` unless the image visibly certifies a terminal suffix.
3. Reconcile or supersede the current converted Markdown so the conversion output no longer promotes the Burgos/de la Cruz row as controlling entry `172`.
4. Only after those steps, consider promoting low-confidence canonical claims for the child-parent group. A separate identity-bridge proof review is required before connecting this group to any Dario Pulgar identity.
