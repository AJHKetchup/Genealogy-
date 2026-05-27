---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527000231135
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526232323475.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526232323475.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
canonical_readiness: hold_for_proof_review_and_conversion_reconciliation
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. The referenced converted Markdown still identifies entry `172` as a Burgos/de la Cruz birth entry for `Jose Miguel`, while the staged conflict draft, source packet, assigned chunk, and targeted conversion QA note identify physical entry `172` on register page 58 as the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`.
2. The father field is not promotion-ready beyond `Jose del Carmen Pulgar`. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the targeted QA note certifies only `Jose del Carmen Pulgar` and says the visible suffix is not clear enough to promote.
3. This staged draft does not support a Dario-line merge or lineage bridge. Entry 172 does not name `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, or `Darío/Dario Pulgar Arriagada`.
4. `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` remain separate Jose/Juana parent candidates. This entry names only `Juana Arriagada de Pulgar`; existing wiki context separately records `Juana de Dios Amagada de Pulgar` as a parent candidate for `Tulio Cesar Luis Jose`.
5. Canonical promotion should wait for proof review acceptance of the targeted row-control QA and a conversion-control decision about retaining or correcting the stale Burgos/de la Cruz converted Markdown.

## Literal Source Readings

The certified physical-row reading from the staged source packet and targeted QA note is:

- Registration number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar`.
- Mother: `Juana Arriagada de Pulgar`.
- Declarant: `Ernesto Herrera L.`, present at birth.

The assigned chunk agrees with the Pulgar/Arriagada row but reads the father as `Jose del Carmen Pulgar S.`. The current converted Markdown instead gives entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`.

## Hypotheses And Evidence

### H1: Physical Entry 172 Is The Pulgar/Arriagada Birth Row

Evidence supporting: the staged conflict draft, source packet, assigned chunk, and targeted conversion QA note all identify physical entry `172` on register page 58 as the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.

Evidence against or limiting: the derivative converted Markdown for the same source path gives a different entry `172` family. This is a row-control/conversion conflict, not a name variant.

Scores: identity confidence 0.86; conflict severity 0.95; evidence quality 0.88; conversion confidence 0.72 because of the stale converted Markdown; claim probability 0.84; relevance 0.95; canonical readiness hold pending proof review.

### H2: Converted Markdown's Burgos/de la Cruz Row Controls Entry 172

Evidence supporting: the converted Markdown explicitly records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.

Evidence against or limiting: the targeted QA note directly rejects that row as controlling for the physical source image and says staged evidence from this task should use the Pulgar/Arriagada row.

Scores: identity confidence 0.18; conflict severity 0.95; evidence quality 0.35; conversion confidence 0.20; claim probability 0.16; relevance 0.10 for Pulgar-line work; canonical readiness not ready.

### H3: `Jose del Carmen Segundo Pulgar Arriagada` Matches The Existing Canonical Stub Of That Name

Evidence supporting: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` already carries Entry 172 evidence snapshots for the same child name, birth date/time, birthplace, sex, and probable mother `Juana Arriagada de Pulgar`.

Evidence against or limiting: those wiki facts derive from the same Entry 172 cluster and therefore do not independently resolve the conversion mismatch. They support same-cluster alignment, not independent corroboration.

Scores: identity confidence 0.82; conflict severity 0.50; evidence quality 0.76; conversion confidence 0.72; claim probability 0.80; relevance 0.94; canonical readiness hold for row-control proof review.

### H4: `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` Is The Father Candidate For This Entry

Evidence supporting: the targeted QA certifies father `Jose del Carmen Pulgar`; the assigned chunk reads `Jose del Carmen Pulgar S.`. The existing wiki page `wiki/people/jose-del-carmen-pulgar.md` is a local parent-candidate page, but its visible evidence snapshot concerns a separate child, `Tulio Cesar Luis Jose`.

Evidence against or limiting: the suffix/initial is unresolved. This entry should not merge `Jose del Carmen Pulgar S.` into `Jose del Carmen Pulgar` as a full identity decision, and it should not attach other children or relationships by name alone.

Scores: identity confidence 0.66 for the bounded father reading; conflict severity 0.60; evidence quality 0.78; conversion confidence 0.70; claim probability 0.74 for `Jose del Carmen Pulgar` as recorded father; relevance 0.88; canonical readiness hold for father-field proof review.

### H5: `Juana Arriagada de Pulgar` Is The Mother Candidate For This Entry

Evidence supporting: the staged source packet, assigned chunk, targeted QA note, and existing canonical page `wiki/people/juana-arriagada-de-pulgar.md` align on `Juana Arriagada de Pulgar` as mother of `Jose del Carmen Segundo Pulgar Arriagada`.

Evidence against or limiting: this is a married-style recorded name. It should not be silently normalized to another Juana identity. The similar local candidate `Juana de Dios Amagada de Pulgar` appears in existing wiki context for a different child and remains separate.

Scores: identity confidence 0.84; conflict severity 0.35; evidence quality 0.84; conversion confidence 0.76; claim probability 0.86; relevance 0.92; canonical readiness scoped hold until row-control proof review accepts the QA note.

### H6: `Juana Arriagada de Pulgar` And `Juana de Dios Amagada de Pulgar` Are The Same Person

Evidence supporting: both are Jose/Juana Pulgar-line parent candidates in existing wiki context.

Evidence against or limiting: the names are materially different readings, the associated children differ, and this staged entry gives no direct identity bridge between them. Family-context similarity is only a double-check prompt.

Scores: identity confidence 0.20; conflict severity 0.70 if merged prematurely; evidence quality 0.25; conversion confidence 0.60 for this entry only; claim probability 0.18; relevance 0.55; canonical readiness not ready.

### H7: Entry 172 Bridges To `Dario Arturo Pulgar-Smith` Or Document-Level `Dario Arturo Pulgar`

Evidence supporting: existing wiki context has canonical `Dario Arturo Pulgar-Smith` as a family-supplied maternal-grandfather profile, and staged CV materials elsewhere use document-level `Dario Arturo Pulgar`. The Pulgar surname makes this entry a possible future lineage lead.

Evidence against or limiting: this birth entry names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario, Arturo, Smith, Pulgar-Smith, Alexander John Heinz, a spouse, child, or descendant of a Dario candidate. Existing CV proof-review notes require a separate identity bridge before attaching document-level `Dario Arturo Pulgar` facts to canonical `Dario Arturo Pulgar-Smith`.

Scores: identity confidence 0.08; conflict severity 0.88 if attached prematurely; evidence quality 0.20 for Dario comparison; conversion confidence 0.72 for the row only; claim probability 0.06; relevance 0.35 as a future lead; canonical readiness not ready.

### H8: Entry 172 Bridges To `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, Or `Darío/Dario Pulgar Arriagada`

Evidence supporting: local staged context contains Pulgar-Arriagada/Dario clusters, including canonical `wiki/people/dar-o-pulgar-arriagada.md` with a 2000 expropriation-event evidence snapshot and staged materials for `Dario Jose Pulgar-Arriagada` or `Darío J. Pulgar Arriagada`.

Evidence against or limiting: this entry names a different given-name cluster, `Jose del Carmen Segundo`, and supplies no medical, Geneva, public-office, residence, spouse, child, chronology, or parent bridge to any Dario candidate. A person born in 1888 as `Jose del Carmen Segundo Pulgar Arriagada` cannot be treated as a Dario identity by surname pattern alone.

Scores: identity confidence 0.07; conflict severity 0.90 if merged prematurely; evidence quality 0.18 for Dario comparison; conversion confidence 0.72 for the row only; claim probability 0.05; relevance 0.40 as anti-conflation context; canonical readiness not ready.

## Conflict Types

- Same-person conflict: high between the Pulgar/Arriagada and Burgos/de la Cruz readings if both are treated as the same entry/person. They describe different children, parents, birth dates, and places.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` until the suffix is resolved; moderate for Juana variants if family context is overused.
- Name-variant risk: high if `Pulgar S.` is normalized away without proof review; high if `Arriagada` and `Amagada` are treated as variants without image-level comparison.
- Relationship-conflict risk: high for promoting father or combined parent claims before row-control proof review; lower for the mother claim after QA, but still scoped to this entry.
- Chronology-conflict risk: high for any Dario attachment because this entry is an 1888 birth for `Jose del Carmen Segundo Pulgar Arriagada` and gives no Dario chronology bridge.

## Ranked Findings

1. Most likely: physical entry `172` is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`; proof review should accept or reject the targeted QA row-control resolution before promotion.
2. Probable but bounded: the mother field supports `Juana Arriagada de Pulgar` as recorded mother of this child, subject to the same row-control gate.
3. Probable but suffix-limited: the father field supports `Jose del Carmen Pulgar` as recorded father; `S.` must remain unpromoted unless proof review certifies it.
4. Not proved: `Juana Arriagada de Pulgar` equals `Juana de Dios Amagada de Pulgar`.
5. Not supported from this entry: any same-person or lineage bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, or `Darío/Dario Pulgar Arriagada`.

## Recommended Next Action

Send the targeted conversion QA note and this staged conflict analysis to proof review for a scoped decision: accept or reject physical-row control that entry `172` is the Pulgar/Arriagada row, preserve the converted Markdown Burgos/de la Cruz row as a derivative conversion mismatch unless conversion-control corrects it, and certify the father field only as `Jose del Carmen Pulgar` unless the proof reviewer can visibly accept the suffix. After that, rerun promotion only for narrowly scoped Entry 172 claims and relationships. Do not merge Jose/Juana candidates or attach any Dario-line identity without a separate identity-bridge proof review using direct bridging evidence.
