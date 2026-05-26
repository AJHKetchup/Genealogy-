---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: "postconv-identity-analysis-20260526013246594"
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
promotion_recommendation: hold_for_conversion_qa
created: 2026-05-26
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Row-control blocker: the staged conflict draft reports the assigned chunk/source packet as a Pulgar/Arriagada birth row for entry 172, while the current converted Markdown records a Burgos/de la Cruz birth row for the same entry number. These are mutually exclusive identity, parentage, birth-date, birthplace, and informant readings.
- Father-field blocker: even if the Pulgar/Arriagada row controls, the father line must be certified only to the visible extent: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Canonical promotion blocker: no child identity, parent-child relationship, Jose/Juana parent merge, Dario-line comparison, or canonical wiki attachment should be promoted from this record until targeted conversion QA resolves the row-control conflict and proof review is rerun.
- Anti-conflation blocker: the entry does not name Dario, Arturo, Smith, Dario Jose, Dario J., or Dario Pulgar Arriagada. Pulgar-family context can justify a later double-check, but it cannot silently bridge this birth entry to any Dario-line person.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing wiki context reviewed for relevant candidates: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/dario-arturo-pulgar-smith.md`, and `wiki/people/dar-o-pulgar-arriagada.md`.

## Literal Readings Kept Separate

Pulgar/Arriagada reading from staged draft, source packet, and assigned chunk:

- Entry 172, registered 7 April 1888.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: 8 March 1888, about 3 p.m., Calle de Valdivia.
- Father: `Jose del Carmen Pulgar S.` in the assigned chunk/source packet, with certification still required.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth.

Burgos/de la Cruz reading from current converted Markdown:

- Entry 172, registered 7 April 1888.
- Child: `Jose Miguel`.
- Sex: `Varon`.
- Birth: 6 April 1888, about 10 p.m., `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

## Hypotheses And Evidence

### 1. Entry 172 Controls As The Pulgar/Arriagada Birth Row

Supporting evidence:

- The staged conflict draft and source packet both state that the assigned chunk supports entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- The assigned chunk transcribes a complete Pulgar/Arriagada row for entry 172 on page 58.
- Existing canonical wiki pages already contain Pulgar/Arriagada evidence snapshots tied to this chunk family, but those snapshots should be treated as at-risk until the row-control conflict is resolved.

Conflicts:

- The current converted Markdown gives a completely different entry 172 person and family: `Jose Miguel`, `Oswaldo Burgos`, and `Concepcion de la Cruz`.
- Father name precision remains unresolved between no suffix, `S.`, or uncertain trailing text.

Interpretation:

- This is the strongest identity hypothesis if the assigned chunk is the controlling row, but it is not canonically ready because the derivative conversion record conflicts at the row level.

### 2. Entry 172 Controls As The Burgos/de la Cruz Birth Row

Supporting evidence:

- The current converted Markdown explicitly records entry 172 as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`.

Conflicts:

- The staged conflict draft, source packet, and assigned chunk all present entry 172 as Pulgar/Arriagada, not Burgos/de la Cruz.
- This reading would invalidate or require withdrawal/revision of any existing wiki evidence snapshots that attach this chunk to Jose del Carmen Segundo Pulgar Arriagada or Juana Arriagada de Pulgar.

Interpretation:

- This hypothesis remains possible only because the current converted Markdown is an accepted local derivative under review. It is weaker than the chunk/source-packet reading for this staged task, but cannot be dismissed without targeted conversion QA.

### 3. Same Person Or Parent Candidate: Jose del Carmen Pulgar / Jose del Carmen Pulgar S.

Supporting evidence:

- Under the Pulgar/Arriagada hypothesis, the father is read as `Jose del Carmen Pulgar S.` in the assigned chunk/source packet.
- The existing wiki page `wiki/people/jose-del-carmen-pulgar.md` contains a separate draft child link to `Tulio Cesar Luis Jose`, showing that a Jose del Carmen Pulgar candidate already exists in canonical context.

Conflicts:

- The entry 172 father field is not certified to exact visible form.
- The current converted Markdown names `Oswaldo Burgos`, not Jose del Carmen Pulgar.
- The existing Jose del Carmen Pulgar page does not by itself prove that the entry 172 father is the same person as any other Jose del Carmen Pulgar candidate.

Interpretation:

- Treat as an unresolved parent candidate. Do not merge the entry 172 father with any existing Jose del Carmen Pulgar profile until row-control QA and a parent-identity proof review are complete.

### 4. Same Person Or Parent Candidate: Juana Arriagada de Pulgar

Supporting evidence:

- Under the Pulgar/Arriagada hypothesis, the mother is read as `Juana Arriagada de Pulgar`.
- The existing wiki page `wiki/people/juana-arriagada-de-pulgar.md` contains a probable child link to Jose del Carmen Segundo Pulgar Arriagada based on this chunk family.

Conflicts:

- The current converted Markdown names `Concepcion de la Cruz`, not Juana Arriagada de Pulgar.
- Existing wiki evidence is dependent on the disputed row and should remain provisional.

Interpretation:

- Treat as an unresolved parent candidate tied to the Pulgar/Arriagada row. Do not strengthen or merge the mother relationship until row-control QA and proof review are complete.

### 5. Same Person As Dario Arturo Pulgar-Smith

Supporting evidence:

- Existing wiki context has a family-supplied canonical person `Dario Arturo Pulgar-Smith`, maternal grandfather of Alexander John Heinz.
- The Pulgar surname and family line make this entry relevant enough for later Pulgar-line review if the Pulgar/Arriagada row is certified.

Conflicts:

- Entry 172 does not name Dario, Arturo, Smith, Alexander John Heinz, a grandchild, spouse, or any direct bridge to the canonical Pulgar-Smith person.
- The child name in the Pulgar/Arriagada reading is `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Arturo Pulgar-Smith.

Interpretation:

- Do not merge or attach this record to Dario Arturo Pulgar-Smith. A later identity-bridge proof review would need a direct local source connecting the certified entry 172 child or parents to Dario Arturo Pulgar-Smith.

### 6. Same Person As Dario Arturo Pulgar

Supporting evidence:

- Existing staged context contains a document-level `Dario Arturo Pulgar` CV cluster, and separate notes repeatedly warn that `Dario Arturo Pulgar` requires a bridge before attachment to `Dario Arturo Pulgar-Smith`.

Conflicts:

- Entry 172 does not name Dario Arturo Pulgar.
- No chronology bridge, parent statement, or name-variant bridge connects `Jose del Carmen Segundo Pulgar Arriagada` or the Jose/Juana parents to the CV subject.

Interpretation:

- Preserve separately. This birth entry can only be used for Dario Arturo Pulgar after row-control QA plus a separate identity-bridge proof review that supplies direct genealogical linkage.

### 7. Same Person As Dario Jose Pulgar-Arriagada / Dario J. Pulgar Arriagada / Dario Or Dario Pulgar Arriagada

Supporting evidence:

- Existing staged context contains unresolved Dario Jose / Dario J. / Dario Pulgar Arriagada material, including image-identity and medical-title cautions.
- Existing canonical context has a separate `Dario Pulgar Arriagada` page with a 2000 legal/administrative-style event.

Conflicts:

- Entry 172 does not name Dario, Dario Jose, Dario J., or Dario Pulgar Arriagada.
- The Pulgar/Arriagada child in entry 172 is named `Jose del Carmen Segundo Pulgar Arriagada`, and the row is for an 1888 birth.
- The Dario Pulgar Arriagada canonical/legal-notice cluster and Dario Jose/Dario J. staged clusters require their own proof chains; name overlap alone is not enough.

Interpretation:

- Very weak same-person hypothesis. Preserve as separate/unresolved unless a later proof-reviewed source explicitly connects entry 172's child or parents to one of the Dario Arriagada candidates.

## Conflict Summary

- Same-person conflict: unresolved only at a broad Pulgar-line level; entry 172 itself does not support a same-person claim with any Dario candidate.
- Duplicate-person risk: high if `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, or any Dario Pulgar variant is merged by surname/family context before row-control QA.
- Name-variant conflict: `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` is an unresolved literal father-field issue, not a proven variant.
- Relationship conflict: Pulgar/Arriagada parent-child claims directly conflict with Burgos/de la Cruz parent-child claims for the same entry number.
- Chronology conflict: Pulgar/Arriagada reading gives birth on 8 March 1888; Burgos/de la Cruz reading gives birth on 6 April 1888.
- Place conflict: Pulgar/Arriagada reading gives Calle de Valdivia; Burgos/de la Cruz reading gives `En esta`.

## Scores

| Category | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.42 | Moderate only for recognizing two competing entry-172 identity readings; low for any canonical person attachment. |
| conflict_severity | 0.95 | The row conflict changes the child, parents, birth date, place, and informant for the same entry number. |
| evidence_quality | 0.72 | Local staged source packet and chunk give detailed support, but derivative conversion disagreement prevents acceptance. |
| conversion_confidence | 0.38 | The assigned chunk is detailed, but current converted Markdown materially disagrees; targeted QA is required. |
| claim_probability_pulgar_row | 0.66 | More local staged materials support Pulgar/Arriagada, but not enough for promotion while conversion conflict remains. |
| claim_probability_burgos_row | 0.34 | Supported by current converted Markdown, but contradicted by staged conflict/source packet/assigned chunk. |
| relevance | 0.90 | Highly relevant to Pulgar/Arriagada parent candidates and possible later Pulgar-line review. |
| canonical_readiness | 0.05 | Not ready for canonical promotion, relationship promotion, merge, or Dario-line attachment. |

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.66 | Targeted conversion QA comparing source image, converted Markdown, assigned chunk, and source packet; then rerun proof review on child identity and birth facts. |
| 2 | Entry 172 is the Burgos/de la Cruz row for `Jose Miguel`. | 0.34 | Same targeted conversion QA; if accepted, revise/withdraw dependent Pulgar/Arriagada staged and canonical-derived evidence. |
| 3 | Entry 172 father is an existing or mergeable `Jose del Carmen Pulgar` candidate. | 0.28 | After row-control QA, certify father field and run parent-identity proof review against existing Jose del Carmen Pulgar context. |
| 4 | Entry 172 mother is the canonical/staged `Juana Arriagada de Pulgar` candidate. | 0.40 | After row-control QA, run mother/child relationship proof review and keep evidence labeled provisional until accepted. |
| 5 | Entry 172 connects to `Dario Arturo Pulgar-Smith`. | 0.08 | Require a separate proof-reviewed bridge source connecting the certified entry 172 child/parents to Dario Arturo Pulgar-Smith. |
| 6 | Entry 172 connects to document-level `Dario Arturo Pulgar`. | 0.07 | Require a separate identity bridge between the entry 172 family and the CV/document-level Dario Arturo Pulgar cluster. |
| 7 | Entry 172 connects to `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Dario Pulgar Arriagada`. | 0.04 | Preserve separately; require direct vital, parentage, chronology, or property-chain evidence before any merge. |

## Recommended Next Action

Keep this staged conflict at `hold_for_conversion_qa`. The exact next step is targeted conversion QA on entry 172 using the original source image, current converted Markdown, assigned chunk, and source packet to certify the controlling row and father field. After QA, rerun proof review before any claim promotion, relationship promotion, Jose/Juana parent merge, or Dario-line comparison. If the Pulgar/Arriagada row is certified, the next promotion path should be child identity and birth-fact proof review first, then separate father/mother relationship reviews, and only then any broader Pulgar-line identity bridge.
