---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527234712207
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-row-control-postconv-evidence-extraction-20260527222756266.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-row-control-postconv-evidence-extraction-20260527222756266.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260527222756266.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
canonical_readiness: hold
---

# Identity/Conflict Analysis: Entry 172 Row-Control Conflict

## Blockers First

1. The staged conflict draft reports a material row-control conflict: the image-reviewed/assigned chunk row for entry `172` is the Pulgar/Arriagada row, while the current converted Markdown records entry `172` as a Burgos/de la Cruz row.
2. The father field must stay bounded to the certified reading `Jose del Carmen Pulgar`. The assigned chunk includes a possible trailing `S.`, but the staged draft and source packet do not certify that suffix for promotion.
3. The Burgos/de la Cruz child and parents must not be merged into the Pulgar/Arriagada row. These are different children, parent sets, birth dates, and birth places under the same entry number in conflicting derivatives.
4. No Dario-line attachment is ready. Entry `172` names `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.
5. Jose/Juana parent candidates remain unresolved across local Pulgar-line context. `Juana Arriagada de Pulgar` in this entry should not be silently normalized to `Juana de Dios Amagada de Pulgar`, and the `Jose del Carmen Pulgar` father candidate requires a separate same-person review before merging with other Jose parent clusters.

## Evidence Reviewed

- Exact staged draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-row-control-postconv-evidence-extraction-20260527222756266.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260527222756266.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Canonical wiki context reviewed: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/juana-de-dios-amagada-de-pulgar.md`, and `wiki/people/tulio-cesar-luis-jose.md`.
- Staged/review context searched for `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, `Darío Pulgar Arriagada`, Jose/Juana Pulgar parent candidates, and Pulgar-Smith identity bridge notes.

## Literal Source Readings

### Image-Reviewed/Assigned Chunk Reading

The staged conflict draft and source packet report physical row `172` as:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: 7 April 1888.
- Birth: 8 March 1888, about 3 p.m., `Calle de Valdivia`.
- Father, certified boundary: `Jose del Carmen Pulgar`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.

The assigned chunk has the fuller father-field text `Jose del Carmen Pulgar S.`, but the source packet explicitly limits the staged father reading to `Jose del Carmen Pulgar` because the trailing `S.` is unresolved.

### Conflicting Converted Markdown Reading

The current converted Markdown records entry `172` as:

- Child: `Jose Miguel`.
- Birth: 6 April 1888, about 10 p.m., `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Declarant: `Oswaldo Burgos`.

## Interpretation Kept Separate

The source packet states `conversion_confidence: image_reviewed_row_control` and treats the original image/assigned chunk as controlling for the Pulgar/Arriagada row. This analysis accepts that as staged reviewed evidence for prioritizing proof review, but it does not edit conversion output or promote any canonical facts.

The Burgos/de la Cruz text remains a derivative conflict. It may be stale, row-shifted, or drawn from a different page/image set, but that explanation is an interpretation. The literal conflict is simply that two local derivatives assign incompatible identities to entry `172`.

## Ranked Hypotheses

### H1: Entry 172 Controls As Jose del Carmen Segundo Pulgar Arriagada

Probability: 0.86.

Supporting evidence:

- The staged conflict draft says the original image and assigned chunk support the Pulgar/Arriagada row for entry `172`.
- The source packet records image-reviewed row control and family relevance for `Pulgar` and `Arriagada`.
- The assigned chunk gives a coherent row with a child, father, mother, birth date/time/place, registration date, and informant.
- Existing canonical `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` already carries low-confidence/probable staged evidence from this entry cluster.

Conflicts and limits:

- The current converted Markdown materially disagrees.
- The father suffix is unresolved and should not be promoted.
- Canonical parent-child relationship promotion still requires proof review.

Scores: identity confidence 0.86; evidence quality 0.78; conversion confidence 0.72; claim probability 0.86; relevance 0.88; canonical readiness 0.35.

### H2: Converted Markdown Entry 172 Controls As Jose Miguel, Child Of Oswaldo Burgos And Concepcion de la Cruz

Probability: 0.08.

Supporting evidence:

- The current converted Markdown explicitly labels the Burgos/de la Cruz row as entry `172`.

Conflicts and limits:

- The staged draft and source packet reject this as the controlling row for the assigned source identity.
- The assigned chunk and image-reviewed row-control evidence point to the Pulgar/Arriagada row instead.

Scores: identity confidence 0.08; evidence quality 0.30; conversion confidence 0.20; claim probability 0.08; relevance 0.10; canonical readiness 0.05.

### H3: Jose del Carmen Pulgar In Entry 172 Is The Same Person As Jose del Carmen Pulgar In The Entry 513/Tulio Context

Probability: 0.42.

Supporting evidence:

- Entry `172` names father `Jose del Carmen Pulgar`.
- Canonical `wiki/people/jose-del-carmen-pulgar.md` has a draft child link to `Tulio Cesar Luis Jose` from a separate entry 513 staging context.
- The repeated Jose del Carmen Pulgar name in Los Angeles/La Laja Pulgar register context makes a same-person comparison plausible.

Conflicts and limits:

- Entry `172` mother is `Juana Arriagada de Pulgar`; the Tulio/entry 513 context names `Juana de Dios Amagada de Pulgar`.
- No age, spouse-continuity, residence-continuity, or direct cross-reference in the evidence reviewed here proves the fathers are the same person.
- The entry `172` father field remains certified only as `Jose del Carmen Pulgar`.

Scores: identity confidence 0.42; evidence quality 0.55; conversion confidence 0.60 for the comparison evidence; claim probability 0.42; relevance 0.75; canonical readiness 0.20.

### H4: Juana Arriagada de Pulgar In Entry 172 Is The Same Person As Juana de Dios Amagada de Pulgar In The Entry 513/Tulio Context

Probability: 0.28.

Supporting evidence:

- Both are Juana + Pulgar-associated mother candidates in local Pulgar-line birth-register context.
- Both appear near a `Jose del Carmen Pulgar` father candidate in staged/canonical context.

Conflicts and limits:

- The literal surnames differ: `Arriagada` versus `Amagada`.
- The entry `172` source packet certifies `Juana Arriagada de Pulgar`.
- No local evidence reviewed here proves that `Amagada` is an error for `Arriagada` or that both names refer to the same woman.

Scores: identity confidence 0.28; evidence quality 0.50; conversion confidence 0.55 for comparison evidence; claim probability 0.28; relevance 0.70; canonical readiness 0.10.

### H5: Jose del Carmen Segundo Pulgar Arriagada Is The Same Person As Dario Arturo Pulgar-Smith

Probability: 0.02.

Supporting evidence:

- Only broad Pulgar-line relevance.
- Canonical `Dario Arturo Pulgar-Smith` is the family-supplied maternal-grandfather profile, and the wiki explicitly flags Pulgar records for identity review.

Conflicts and limits:

- Entry `172` names `Jose del Carmen Segundo`, not `Dario Arturo`.
- The entry does not state `Smith`, `Pulgar-Smith`, Alexander John Heinz, a spouse, child, grandchild, occupation, or any direct bridge to the canonical family-supplied person.
- A same-person claim would require more than surname-family context.

Scores: identity confidence 0.02; evidence quality 0.20 for this bridge; conversion confidence 0.70 for row reading but 0.00 for Dario bridge; claim probability 0.02; relevance 0.40; canonical readiness 0.00.

### H6: Dario Arturo Pulgar Is A Short-Name Variant Of Dario Arturo Pulgar-Smith

Probability in this entry: 0.00; broader local-context bridge probability: 0.60.

Supporting evidence:

- Local staged CV tasks repeatedly identify a document-level subject `Dario Arturo Pulgar`.
- Canonical `Dario Arturo Pulgar-Smith` shares `Dario Arturo Pulgar` as the leading name string and is family-supplied as Alexander John Heinz's maternal grandfather.

Conflicts and limits:

- Entry `172` does not name Dario Arturo Pulgar.
- Existing staged CV notes require a separate identity-bridge proof review before attaching `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`.
- The canonical page warns against automatic merging of similarly named Dario/Pulgar records.

Scores for this entry: identity confidence 0.00; evidence quality 0.00; conversion confidence 0.00; claim probability 0.00; relevance 0.20; canonical readiness 0.00.

### H7: Jose del Carmen Segundo Pulgar Arriagada Is The Same Person As Dario Jose Pulgar-Arriagada

Probability: 0.05.

Supporting evidence:

- Both names use a Pulgar-Arriagada surname pattern or Pulgar-Arriagada source-title context.
- Local staged materials contain a `Dario Jose Pulgar-Arriagada` portrait/source-title cluster.

Conflicts and limits:

- Given names differ materially: `Jose del Carmen Segundo` versus `Dario Jose`.
- Existing proof-review context for the Dario Jose portrait notes that available identity support is title/file metadata, not a visible text label.
- Entry `172` supplies no Dario identity bridge.

Scores: identity confidence 0.05; evidence quality 0.25; conversion confidence 0.70 for entry row but 0.00 for this bridge; claim probability 0.05; relevance 0.45; canonical readiness 0.00.

### H8: Jose del Carmen Segundo Pulgar Arriagada Is The Same Person As Dario/Darío Pulgar Arriagada

Probability: 0.04.

Supporting evidence:

- Same broad Pulgar Arriagada surname pattern.
- Canonical `Darío Pulgar Arriagada` has a reviewed 2000-12-05 event in the wiki.
- Staged source packets also mention Dario/Darío Pulgar Arriagada name forms in separate contexts.

Conflicts and limits:

- Entry `172` names `Jose del Carmen Segundo`, not Dario or Darío.
- No reviewed local source connects the 1888 child to the 2000 public-event person.
- If literally the same person, the 2000 event would occur at about age 112, which is not impossible but is too unlikely to infer without direct proof.

Scores: identity confidence 0.04; evidence quality 0.30; conversion confidence 0.70 for entry row but 0.00 for this bridge; claim probability 0.04; relevance 0.45; canonical readiness 0.00.

## Conflict Assessment

- Same-person conflict severity: 9/10 for row `172` because the competing local readings identify different people and parents.
- Duplicate-person risk: 7/10 for Jose/Juana parent candidates across entry `172` and entry 513 because similar names and nearby context could invite premature merges.
- Name-variant risk: 8/10 for treating `Pulgar`, `Pulgar S.`, `Pulgar-Smith`, and `Pulgar Arriagada` as interchangeable without bridge evidence.
- Relationship conflict severity: 9/10 because Burgos/de la Cruz parentage and Pulgar/Arriagada parentage cannot both describe the same child in the same source row.
- Chronology conflict severity: 6/10 for any attempted merge between the 1888 Jose child and later Dario/Darío Pulgar candidates, especially the 2000 Darío Pulgar Arriagada event.

## Overall Scores

| Category | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 8.6/10 for `Jose del Carmen Segundo Pulgar Arriagada`; 0.2/10 for Dario bridge | Staged image-reviewed row control supports the Jose child, but no Dario identity bridge appears in this entry. |
| conflict_severity | 9.0/10 | The same entry number has incompatible children, parent sets, birth dates, and places. |
| evidence_quality | 7.8/10 | The source packet and assigned chunk are strong staged evidence, while the current converted Markdown remains contradictory. |
| conversion_confidence | 7.2/10 for staged row-control; 2.0/10 for current converted Markdown row assignment | Image-reviewed row-control evidence is stronger than the derivative converted entry assignment. |
| claim_probability | 0.86 for Pulgar/Arriagada row; 0.08 for Burgos/de la Cruz as controlling this source | The staged draft/source packet favor Pulgar/Arriagada but still require proof review before promotion. |
| relevance | 8.8/10 | The row is directly Pulgar-line relevant and names possible parent candidates, but it does not itself name Dario. |
| canonical_readiness | 3.0/10 | Ready for proof-review queueing; not ready for canonical merge, parent promotion, or Dario-line attachment. |

## Recommended Next Action

Run proof review on this row-control extraction set before any promotion. The exact proof-review decision needed next is:

1. Confirm whether entry `172` controls as the Pulgar/Arriagada row despite the current converted Markdown conflict.
2. Confirm whether the father field should be promoted only as `Jose del Carmen Pulgar` or whether any suffix can be certified from the image.
3. Decide whether the parent-child candidates `Jose del Carmen Segundo Pulgar Arriagada` -> `Jose del Carmen Pulgar` and `Jose del Carmen Segundo Pulgar Arriagada` -> `Juana Arriagada de Pulgar` may be promoted as probable, while preserving row-control caveats.
4. Open a separate Jose/Juana same-person review before merging `Jose del Carmen Pulgar` or `Juana Arriagada de Pulgar` with entry 513/Tulio parent candidates.
5. Open a separate Dario-line identity-bridge proof review before any attachment to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`. That bridge must use direct identifiers such as dates, places, parents, spouse/children, occupation, or source provenance beyond surname similarity.
