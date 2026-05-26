---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260526174903677
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md
subject: "Entry 172, Los Angeles birth register, 1888"
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
created: 2026-05-26
---

# Identity And Conflict Analysis: Entry 172 Current Conversion Conflict

## Blockers First

1. The controlling row for entry `172` is not certified across the local evidence set. The assigned chunk and staged source packet read entry `172` as the Pulgar/Arriagada row, while the current converted Markdown reads entry `172` as a Burgos/de la Cruz row.
2. This is a material row-level conversion conflict, not a spelling variant. It changes child identity, birth date/time/place, father, mother, informant, residence context, and all relationship candidates.
3. The father field in the Pulgar/Arriagada row remains uncertified at the final element: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
4. Existing canonical pages already contain promoted or draft context for `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Pulgar`, but this new staged draft specifically flags the current converted Markdown disagreement. No additional promotion or merge should proceed from this draft until targeted conversion QA reconciles that disagreement.
5. No evidence in this staged draft directly names `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. Those names appear only through existing wiki/staged Pulgar-line context and must remain comparison guardrails, not identity bridges.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md`.
- Staged source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing canonical or promoted context: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/juana-de-dios-amagada-de-pulgar.md`, and promoted/staged relationship/source-packet files for the same local clusters.

## Literal Readings Kept Separate

### Assigned Chunk / Staged Packet Reading

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about `tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father field: `Jose del Carmen Pulgar S.` in the assigned chunk; staged packet notes the trailing mark is unresolved.
- Mother field: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age 26, employed, resident at `Calle de Valdivia`.

### Current Converted Markdown Reading

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose Miguel`.
- Sex: `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho`, about `diez de la noche`.
- Birthplace: `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

## Hypotheses Ranked

### H1: Entry 172 Is The Pulgar/Arriagada Row

The assigned chunk and staged source packet support this hypothesis. Existing promoted local context also contains a source packet for birth registration entry 172 naming `Jose del Carmen Segundo Pulgar Arriagada`, with an image-reread note stating that the child, mother, informant, birth date/time, and birthplace agree with the Pulgar/Arriagada row while the father's suffix remains uncertain.

Interpretation: This is the stronger local hypothesis for the staged conflict draft, but the current converted Markdown still blocks canonical readiness because it records a different row under the same entry number.

- Identity confidence: 0.78
- Conflict severity: 0.95
- Evidence quality: 0.82
- Conversion confidence: 0.45
- Claim probability: 0.74
- Relevance: 0.99
- Canonical readiness: 0.20, blocked pending conversion QA

### H2: Entry 172 Is The Burgos/de la Cruz Row

The current converted Markdown supports this hypothesis. It gives a complete internally coherent entry for `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`.

Interpretation: This remains a live conversion-control hypothesis only because it appears in the current converted file. It conflicts with the assigned chunk, the staged source packet, and existing Pulgar/Arriagada canonical context.

- Identity confidence: 0.30
- Conflict severity: 0.95
- Evidence quality: 0.45
- Conversion confidence: 0.35
- Claim probability: 0.26
- Relevance: 0.95
- Canonical readiness: 0.05, blocked pending conversion QA

### H3: The Two Readings Are Same-Person, Duplicate-Person, Or Name Variants

This hypothesis is not supported. The readings disagree across child name, parents, birth date, birth time, birthplace, and informant. There is no plausible name-variant path from `Jose del Carmen Segundo Pulgar Arriagada` to `Jose Miguel`, nor from `Jose del Carmen Pulgar` / `Juana Arriagada de Pulgar` to `Oswaldo Burgos` / `Concepcion de la Cruz`.

- Identity confidence: 0.03
- Conflict severity: 0.95
- Evidence quality: 0.80 for rejecting the merge
- Conversion confidence: 0.45
- Claim probability: 0.02
- Relevance: 0.99
- Canonical readiness: 0.00, do not merge

### H4: The Pulgar/Arriagada Child Connects To A Later Dario Pulgar Identity

No direct evidence in this staged draft supports this. The child is named `Jose del Carmen Segundo Pulgar Arriagada`, born in 1888. Existing Dario contexts are separate clusters: family-supplied `Dario Arturo Pulgar-Smith`; CV/source-title `Dario Arturo Pulgar`; photograph/source-context `Dario Jose Pulgar-Arriagada`; title-conferral `Dario J. Pulgar Arriagada`; legal-notice `Dario Pulgar Arriagada`; and passenger-list `Dario Pulgar` adult/child rows.

Interpretation: The surname and Pulgar/Arriagada family context justify future double-checking, but not a same-person or ancestry bridge. This staged draft should not be used to merge `Jose del Carmen Segundo Pulgar Arriagada` with any Dario identity.

- Identity confidence: 0.08
- Conflict severity: 0.70
- Evidence quality: 0.20 for the bridge
- Conversion confidence: 0.45
- Claim probability: 0.05
- Relevance: 0.60
- Canonical readiness: 0.00, no bridge

## Pulgar-Line Comparison Required By Task

| Candidate | Local evidence context | Relationship to this staged draft | Hypothesis rank |
| --- | --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | Canonical family-supplied maternal grandfather of Alexander John Heinz; page warns not to merge similarly named clusters automatically. | Not named in entry 172. No `Smith`, Arturo, spouse, child, birth, or parent bridge appears here. | Not connected from this draft. |
| `Dario Arturo Pulgar` | CV source-title/document-level cluster; multiple reviews hold attachment to `Dario Arturo Pulgar-Smith` pending identity bridge. | Not named in entry 172. No CV, occupation, or modern chronology appears here. | Not connected from this draft. |
| `Dario Jose Pulgar-Arriagada` | Photograph/source-context and portrait clusters; identification often depends on filenames or source context; not family relationship evidence. | Not named in entry 172. Similar Pulgar-Arriagada surname pattern only. | Not connected from this draft. |
| `Dario J. Pulgar Arriagada` / `Dario Pulgar Arriagada` | 1918 title-conferral and later legal-notice clusters; one source names `Dario J. Pulgar Arriagada` as a medico-cirujano, another names `Dario Pulgar Arriagada` in a 2000 expropriation notice. | Not named in entry 172. No age, parents, residence continuity, or chronology bridge. | Not connected from this draft. |
| `Jose del Carmen Pulgar` | Existing page has a draft child link to `Tulio Cesar Luis Jose` from an 1889 entry. Entry 172 assigned chunk/staged packet reads father as `Jose del Carmen Pulgar` with unresolved final mark. | Plausible same-name parent candidate, but father suffix and row control need QA before adding or linking father claims from this draft. | Highest parent-candidate lead, still held. |
| `Juana Arriagada de Pulgar` | Existing page has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada` from earlier reviewed context. | Direct mother reading in assigned chunk/staged packet, but current converted Markdown conflict requires holding new dependent claims. | Strong mother candidate if Pulgar row is certified. |
| `Juana de Dios Amagada de Pulgar` | Separate 1889 entry 513 mother candidate for `Tulio Cesar Luis Jose`. | Not named in entry 172. Similar married-style `de Pulgar` and possible family context, but no substitution is justified. | Separate Juana candidate. |

## Conflicts

- Same entry number conflict: `172` controls two incompatible rows in local derivative evidence.
- Relationship conflict: one reading implies parents `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`; the other implies parents `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Chronology conflict: one reading gives birth `1888-03-08 15:00`; the other gives `1888-04-06 22:00`.
- Place conflict: one reading gives `Calle de Valdivia`; the other gives `En esta`.
- Informant conflict: one reading gives `Ernesto Herrera L.` present at birth; the other gives `Oswaldo Burgos`.
- Canonical context conflict: existing local pages/source packets already carry Pulgar/Arriagada context, but the current converted Markdown still materially disagrees and must be reconciled before further promotion.

## Recommended Next Action

Run targeted conversion QA on the original image, assigned chunk, current converted Markdown, and staged source packet for entry `172`. The QA note should certify:

1. Which physical row controls entry `172`.
2. Whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. Whether the current converted Markdown is row-shifted, sourced from a different image/page, or otherwise stale against the assigned chunk.

After conversion QA, rerun proof review before any new canonical claim, relationship, merge, or wiki update. If the Pulgar/Arriagada row is certified, promote only scoped claims supported by the certified row; do not attach the child or parents to any Dario identity without a separate identity-bridge proof review.
