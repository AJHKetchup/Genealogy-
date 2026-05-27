---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527000641674
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526232323475.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526232323475.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
canonical_readiness: hold_for_proof_review
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. The exact staged draft under review is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526232323475.md`. It reports a material row-control conflict: the current converted Markdown records entry `172` as a Burgos/de la Cruz birth for `Jose Miguel`, while the source packet, assigned chunk, and targeted conversion QA identify physical entry `172` as the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`.
2. Canonical promotion remains blocked until proof review accepts the targeted conversion QA row-control decision. The QA note is strong staged evidence, but it is still a staging gate, not a canonical merge or promotion.
3. The father field is bounded to `Jose del Carmen Pulgar` for this analysis. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the targeted QA note certifies only `Jose del Carmen Pulgar` and says the suffix/terminal mark is not clear enough to promote.
4. This entry does not name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, or `Darío/Dario Pulgar Arriagada`. Do not attach this entry to any Dario-line person by surname or family context alone.
5. `Juana Arriagada de Pulgar` and separate wiki/staged parent candidates such as `Juana de Dios Amagada de Pulgar` remain distinct hypotheses. This entry can justify a double-check of Juana variants, but it cannot silently merge them.

## Literal Source Readings

Staged source packet and targeted QA certify the controlling physical-row reading as:

- Registration: `172`, registered `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Place: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar`.
- Mother: `Juana Arriagada de Pulgar`.
- Declarant: `Ernesto Herrera L.`, present at the birth.

The assigned chunk agrees with the Pulgar/Arriagada row but reads the father as `Jose del Carmen Pulgar S.`. The current converted Markdown instead reads entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born on 6 April 1888 at 10 p.m. This is a row-level conversion mismatch, not a name variant.

## Hypotheses

### H1: Physical Entry 172 Is The Pulgar/Arriagada Birth Row

Supporting evidence: the staged conflict draft, source packet, assigned chunk, and targeted conversion QA all identify the physical row for entry `172` on register page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, with parents `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.

Conflicting evidence: the derivative converted Markdown points to a different child and parents for the same entry number and source identity. The QA note directly explains that converted Markdown as stale, row-shifted, or sourced from a different image/page set.

Scores: identity confidence 0.87; conflict severity 0.95; evidence quality 0.88; conversion confidence 0.72; claim probability 0.85; relevance 0.96; canonical readiness `hold_for_proof_review`.

### H2: The Converted Burgos/de la Cruz Row Controls Entry 172

Supporting evidence: the converted Markdown explicitly records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.

Conflicting evidence: the assigned chunk, source packet, and targeted QA reject that row as the controlling physical row for this staged task. The names, parents, birth date/time, and row family differ materially from the Pulgar/Arriagada evidence.

Scores: identity confidence 0.16; conflict severity 0.95; evidence quality 0.34; conversion confidence 0.20; claim probability 0.14; relevance 0.10; canonical readiness `not_ready`.

### H3: The Child Matches The Existing Canonical Stub `Jose del Carmen Segundo Pulgar Arriagada`

Supporting evidence: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` already contains Entry 172 evidence snapshots for the same birth-name cluster, sex, birth date/time, birth place, and probable mother `Juana Arriagada de Pulgar`.

Conflicting evidence: the canonical snapshot appears to derive from the same Entry 172 evidence cluster, so it is not independent corroboration. It should not be used to bypass proof review of the row-control conflict.

Scores: identity confidence 0.82; conflict severity 0.50; evidence quality 0.76; conversion confidence 0.72; claim probability 0.80; relevance 0.94; canonical readiness `hold_for_proof_review`.

### H4: `Jose del Carmen Pulgar` / Possible `Jose del Carmen Pulgar S.` Is The Father Candidate

Supporting evidence: targeted QA certifies `Jose del Carmen Pulgar`; the assigned chunk reads `Jose del Carmen Pulgar S.`. Existing wiki context has a local `Jose del Carmen Pulgar` stub, but its visible evidence snapshot concerns a separate child, `Tulio Cesar Luis Jose`.

Conflicting evidence: the suffix is unresolved. This entry does not prove whether `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and other Jose del Carmen Pulgar appearances are the same person.

Scores: identity confidence 0.66 for the bounded father reading; conflict severity 0.62; evidence quality 0.78; conversion confidence 0.70; claim probability 0.74; relevance 0.88; canonical readiness `hold_for_father_field_review`.

### H5: `Juana Arriagada de Pulgar` Is The Mother Candidate For This Entry

Supporting evidence: the source packet, assigned chunk, targeted QA note, and existing `wiki/people/juana-arriagada-de-pulgar.md` page align on `Juana Arriagada de Pulgar` as mother of `Jose del Carmen Segundo Pulgar Arriagada`.

Conflicting evidence: this is still scoped to the same Entry 172 row-control cluster. It should not be normalized into a different Juana candidate without a separate comparison.

Scores: identity confidence 0.84; conflict severity 0.35; evidence quality 0.84; conversion confidence 0.76; claim probability 0.86; relevance 0.92; canonical readiness `hold_for_row_control_proof_review`.

### H6: `Juana Arriagada de Pulgar` Equals `Juana de Dios Amagada de Pulgar`

Supporting evidence: both names appear in existing Pulgar-line parent context, and both are associated with Jose/Juana parent-candidate work.

Conflicting evidence: the names and associated children differ. Entry 172 gives no direct bridge between `Arriagada` and `Amagada`, no independent spouse proof, and no chronology or residence chain sufficient for a same-person conclusion.

Scores: identity confidence 0.20; conflict severity 0.70 if merged prematurely; evidence quality 0.25; conversion confidence 0.60 for Entry 172 only; claim probability 0.18; relevance 0.55; canonical readiness `not_ready`.

### H7: Entry 172 Bridges To `Dario Arturo Pulgar-Smith` Or Document-Level `Dario Arturo Pulgar`

Supporting evidence: the surname `Pulgar` and local family context make Entry 172 a possible future lead. Existing wiki context treats `Dario Arturo Pulgar-Smith` as a family-supplied maternal-grandfather profile, and other staged CV files use document-level `Dario Arturo Pulgar`.

Conflicting evidence: Entry 172 names neither Dario nor Arturo nor Smith. It gives no spouse, child, descendant, occupation, residence chain, or identity statement bridging `Jose del Carmen Segundo Pulgar Arriagada` to `Dario Arturo Pulgar-Smith` or document-level `Dario Arturo Pulgar`.

Scores: identity confidence 0.08; conflict severity 0.88 if attached prematurely; evidence quality 0.20; conversion confidence 0.72 for the row only; claim probability 0.06; relevance 0.35 as a future lead; canonical readiness `not_ready`.

### H8: Entry 172 Bridges To `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, Or `Darío/Dario Pulgar Arriagada`

Supporting evidence: local staged and canonical context includes Pulgar-Arriagada/Dario clusters, including `wiki/people/dar-o-pulgar-arriagada.md` and staged references to `Darío J. Pulgar Arriagada`.

Conflicting evidence: this entry's named child is `Jose del Carmen Segundo Pulgar Arriagada`, not Dario. The entry supplies no medical-title, public-record, property, family, or chronology bridge to any Dario Pulgar Arriagada candidate.

Scores: identity confidence 0.07; conflict severity 0.90 if merged prematurely; evidence quality 0.18; conversion confidence 0.72 for the row only; claim probability 0.05; relevance 0.40 as anti-conflation context; canonical readiness `not_ready`.

## Conflict Summary

- Same-person conflict: severe between the Pulgar/Arriagada and Burgos/de la Cruz readings if both are treated as the same entry/person.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` versus possible `Jose del Carmen Pulgar S.` until proof review certifies the terminal mark.
- Name-variant risk: high if `Pulgar S.` is normalized away, or if `Arriagada` and `Amagada` are treated as variants without separate image-level proof.
- Relationship-conflict risk: high for promoting father, parent pair, or child-parent relationships before row-control proof review.
- Chronology-conflict risk: high for any Dario attachment because the 1888 birth row gives no direct Dario bridge.

## Ranked Findings

1. Most likely: physical entry `172` is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`.
2. Probable but bounded: `Juana Arriagada de Pulgar` is the mother recorded in this entry.
3. Probable but suffix-limited: `Jose del Carmen Pulgar` is the father reading certified for this entry; `S.` remains unresolved.
4. Not proved: `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are the same person.
5. Not supported: any same-person, duplicate-person, or lineage bridge from this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, or `Darío/Dario Pulgar Arriagada`.

## Recommended Next Action

Send the targeted conversion QA note and this identity/conflict analysis to proof review for a narrow decision: accept or reject that the controlling physical entry `172` is the Pulgar/Arriagada row, keep the current Burgos/de la Cruz converted Markdown as a derivative conversion conflict until conversion-control updates it, and certify the father field only as `Jose del Carmen Pulgar` unless proof review accepts the terminal suffix. After that, promote only narrow Entry 172 child and parent claims. Do not merge Jose/Juana candidates or attach Dario-line identities without a separate identity-bridge proof review using direct bridging evidence.
