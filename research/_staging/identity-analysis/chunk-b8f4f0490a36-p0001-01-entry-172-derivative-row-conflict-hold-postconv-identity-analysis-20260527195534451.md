---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527195534451
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527180532740.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
canonical_readiness: hold_for_conversion_qa
promotion_recommendation: hold
---

# Identity And Conflict Analysis: Entry 172 Derivative Row Conflict

## Blockers First

- The exact staged conflict draft reports that the assigned chunk and current converted Markdown cannot both control entry `172`: the chunk gives a Pulgar/Arriagada birth row, while the converted Markdown gives a Burgos/de la Cruz birth row.
- I did not perform external research or run conversion. The referenced raw source image and job page image are absent in this checkout, so this note cannot newly certify the handwriting or physical row position.
- The conflict is material, not a spelling variant: the competing readings differ on child, parents, birth date/time, place, and informant.
- Existing proof-review context supports preserving the Pulgar/Arriagada reading as likely, but still holds conversion QA for the active converted-file conflict and for the father's possible terminal suffix after `Pulgar`.
- This entry does not itself name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario Pulgar Arriagada. No Dario-line merge or bridge is ready from this task.

## Literal Readings Kept Separate

Assigned chunk / held packet reading:

- Entry `172`, registered `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Father field in derivative text: `Jose del Carmen Pulgar S.`; reviewed image-reread context prefers `Jose del Carmen Pulgar` without certifying `S.`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age 26, employed, resident at Calle de Valdivia.

Current converted Markdown reading:

- Entry `172`, registered `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant/declarant: `Oswaldo Burgos`.

Interpretation: these are best treated as a source/row alignment or conversion-control conflict, not as duplicate persons or alternate name forms.

## Hypothesis 1: Entry 172 Controls The Pulgar/Arriagada Row

Evidence supporting:

- The assigned chunk and held source packet agree on the Pulgar/Arriagada row for entry `172`.
- A promoted source packet for this same source SHA records that image reread supported `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, and father read as `Jose del Carmen Pulgar`, while leaving the suffix unresolved.
- Proof reviews for the child birth name and child-father relationship hold promotion for conversion QA, but give high probabilities for the narrow Pulgar/Arriagada facts. The child-mother proof review marked the mother relationship ready only as a scoped relationship, with identity-normalization caution.
- Canonical wiki pages already exist for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`; these are context, not independent row proof.

Conflicts and limits:

- The active converted Markdown still describes a Burgos/de la Cruz entry as `172`.
- The raw source image is unavailable to this worker.
- The father-name suffix remains uncertain and must not be promoted as `S.` without targeted proof review.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.74 | Strong for the staged Pulgar child/mother cluster if prior image-reread context is accepted; weaker for the father suffix. |
| conflict_severity | 0.95 | A wrong row would attach the wrong child and parents. |
| evidence_quality | 0.74 | Civil-register evidence is high quality, but this task relies on derivative and reviewed local notes rather than a fresh image check. |
| conversion_confidence | 0.48 | Prior image-reviewed notes improve confidence, but the active converted Markdown remains contradictory. |
| claim_probability | 0.80 | Probable that the family-relevant row is Pulgar/Arriagada, pending conversion-control acceptance. |
| relevance | 0.97 | Directly relevant to Pulgar/Arriagada parent-child evidence. |
| canonical_readiness | 0.25 | Hold until row-control QA and proof-review acceptance. |

## Hypothesis 2: Entry 172 Controls The Burgos/de la Cruz Row

Evidence supporting:

- The current converted Markdown explicitly labels entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- That converted file is referenced by the staged conflict draft metadata.

Conflicts and limits:

- The assigned chunk, held packet, and prior image-reread/proof-review context contradict this as the family-relevant row.
- The Burgos/de la Cruz reading has no Pulgar-line relevance unless QA proves the Pulgar row belongs to another entry or source.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.22 | Low as controlling evidence for this Pulgar-line task. |
| conflict_severity | 0.95 | Direct contradiction of every core family field. |
| evidence_quality | 0.38 | A derivative conversion unsupported by the staged Pulgar packet. |
| conversion_confidence | 0.35 | The conversion set is internally inconsistent. |
| claim_probability | 0.20 | Possible only until row-control QA rejects or supersedes it. |
| relevance | 0.10 | Not relevant to Pulgar-line identity unless it proves the Pulgar packet is misassigned. |
| canonical_readiness | 0.05 | Do not promote from this task. |

## Hypothesis 3: Immediate Issue Is Conversion Control, Not Identity Merger

Evidence supporting:

- `Jose del Carmen Segundo Pulgar Arriagada` is not a plausible variant of `Jose Miguel`.
- `Jose del Carmen Pulgar` is not a plausible variant of `Oswaldo Burgos`.
- `Juana Arriagada de Pulgar` is not a plausible variant of `Concepcion de la Cruz`.
- The chronology and place fields also differ: 8 March 1888 at 3 p.m. on Calle de Valdivia versus 6 April 1888 at 10 p.m. in `En esta`.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.92 | High confidence that this is a row/source conflict rather than duplicate-person evidence. |
| conflict_severity | 0.95 | High downstream risk for all claims and relationships. |
| evidence_quality | 0.82 | The contradiction is clear from the staged and referenced texts. |
| conversion_confidence | 0.35 | The conversion artifacts cannot both be accepted. |
| claim_probability | 0.90 | Most likely disposition is hold for conversion QA. |
| relevance | 0.98 | Directly governs the staged draft. |
| canonical_readiness | 0.15 | Not ready until row control is reconciled. |

## Pulgar-Line Anti-Conflation Review

| Candidate | Evidence in this task and wiki context | Same-person / bridge probability | Required next step |
| --- | --- | ---: | --- |
| `Dario Arturo Pulgar-Smith` | Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather. Entry 172 does not name Dario, Arturo, Smith, Alexander, spouse, child, or descendant bridge. | 0.01 | No attachment from this task; require separate identity-bridge proof review after row-control QA. |
| `Dario Arturo Pulgar` | Existing staged CV/source context elsewhere names `Dario Arturo Pulgar`. Entry 172 does not cite the CV or name Dario Arturo. | 0.02 | Compare only through a reviewed bridge source, not surname context. |
| `Dario Jose Pulgar-Arriagada` | Existing local portrait/photo and Geneva-context staging elsewhere names this cluster. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose`. | 0.02 | Preserve as separate unless a proof-reviewed identity chain connects them. |
| `Dario/Dario Pulgar Arriagada` | Existing wiki has `Darío Pulgar Arriagada` for a 2000 expropriation event. Entry 172 does not name Dario. | 0.03 | Do not merge; require a chronological and relational bridge. |
| `Jose del Carmen Pulgar` | Under H1, entry 172 names this person as father, with unresolved suffix in the derivative transcript. Existing wiki also links this name to other Pulgar child candidates. | 0.78 as H1 father; 0.30 for broader canonical merge | Targeted image QA must certify the father field and a separate identity review must compare other Jose Pulgar records. |
| `Juana Arriagada de Pulgar` | Under H1, entry 172 names this person as mother. Existing wiki has a probable child link to Jose del Carmen Segundo Pulgar Arriagada. | 0.85 as H1 mother | Promote only with row-control acceptance and preserve married-style name handling. |
| `Juana de Dios Amagada de Pulgar` | Existing wiki/staged context names this as a separate Juana candidate in other Pulgar work. Entry 172's Pulgar reading says `Juana Arriagada de Pulgar`. | 0.22 same-person from this task alone | Do not merge; require side-by-side proof review of the Juana records and name forms. |

## Relationship And Chronology Conflicts

- Relationship conflict: H1 supports a held child-parent cluster for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`; H2 assigns entry `172` to unrelated Burgos/de la Cruz parents.
- Chronology conflict: H1 birth date/time is 1888-03-08 at 3 p.m.; H2 birth date/time is 1888-04-06 at 10 p.m.
- Place conflict: H1 gives `Calle de Valdivia`; H2 gives `En esta`.
- Name-variant conflict: none of the Burgos/de la Cruz names are reasonable variants of the Pulgar/Arriagada names.
- Parent-candidate caution: do not use this task to merge `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar`, or to merge `Jose del Carmen Pulgar` with other Jose/Juana parent candidates.

## Ranked Conclusion

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | This is a conversion/row-control conflict, not a same-person conflict. | 0.90 | Hold all dependent identity and relationship actions. |
| 2 | If prior image-reread context is accepted, entry 172 is the Pulgar/Arriagada row. | 0.80 | Proceed only through targeted conversion QA/proof review. |
| 3 | The father field should be handled as `Jose del Carmen Pulgar` pending suffix QA. | 0.78 | Do not promote `S.` or any father identity merge. |
| 4 | The Burgos/de la Cruz converted reading controls this Pulgar task. | 0.20 | Preserve only as the conflicting derivative reading until QA resolves it. |
| 5 | Entry 172 bridges directly to a Dario Pulgar identity. | 0.02 | Unsupported; require separate identity-bridge proof review. |

## Recommended Next Action

Run targeted conversion QA/proof review for the exact physical entry `172` against the original image, current converted Markdown, current chunk, held source packet, and prior row-certification notes. The next review must decide whether the converted Markdown should be corrected or superseded and must separately certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After row control is accepted, rerun scoped proof review for the child identity, birth event, child-mother relationship, child-father relationship, and any Jose/Juana parent-candidate comparison. Any bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario Pulgar Arriagada requires a separate proof-reviewed identity chain.
