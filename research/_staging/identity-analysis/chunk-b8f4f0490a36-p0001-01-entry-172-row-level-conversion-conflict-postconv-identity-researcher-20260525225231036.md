---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260525225231036
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
canonical_readiness: hold
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Row-level conversion conflict blocks canonical promotion. The assigned staged draft says the assigned chunk/source-image-supported row for entry 172 is `Jose del Carmen Segundo Pulgar Arriagada`, while the current converted Markdown gives entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
2. The exact father-field reading is not yet certified. The source packet/chunk use `Jose del Carmen Pulgar S.`, while the staged draft requires targeted QA to decide between `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. Existing canonical pages already include separate Pulgar-line stubs and Dario-line candidates. This entry cannot be used to merge `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Darío Pulgar Arriagada` by name or surname pattern alone.
4. The named proof-review contract skill was not available locally as a readable skill file in this worker session, so this note applies the task's stated evidence rules: literal readings are separated from interpretation; only staged drafts, referenced local files, reviewed notes, and existing wiki pages are used.

## Literal Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing wiki context: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.

## Hypotheses And Evidence

### Hypothesis 1: Entry 172 is the Pulgar/Arriagada birth row

The assigned chunk and source packet transcribe page 58, entry 172 as a male child named `Jose del Carmen Segundo Pulgar Arriagada`, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`. Existing wiki pages for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` already reflect this cluster as probable or low-confidence staged evidence.

Interpretation: this is the best local row-control hypothesis, but it is not canonical-ready because the converted file still contains a different entry-172 family and the father suffix remains unresolved.

Scores: identity confidence 0.78; conflict severity 0.95; evidence quality 0.72; conversion confidence 0.48; claim probability 0.78; relevance 1.00; canonical readiness 0.20.

### Hypothesis 2: Entry 172 is the Burgos/de la Cruz row from current converted Markdown

The current converted Markdown reads entry 172 as `José Miguel`, male, born 6 April 1888 at 10 p.m. in `En esta`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.

Interpretation: this is a real local conversion reading but is contradicted by the assigned chunk and source packet for the same entry/page assignment. It may represent a wrong row, wrong source spread, earlier conversion error, or stale converted output. It should not be promoted as entry 172 without targeted QA.

Scores: identity confidence 0.25; conflict severity 0.95; evidence quality 0.45; conversion confidence 0.30; claim probability 0.25; relevance 1.00; canonical readiness 0.05.

### Hypothesis 3: The entry-172 Jose/Juana parents are same-person candidates with other Jose/Juana Pulgar-line pages

Existing wiki context has `Jose del Carmen Pulgar` with a draft child link to `Tulio Cesar Luis Jose`, `Juana de Dios Amagada de Pulgar` with a draft child link to the same Tulio page, and `Juana Arriagada de Pulgar` with a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`. The entry-172 staging names a father broadly as `Jose del Carmen Pulgar...` and a mother as `Juana Arriagada de Pulgar`.

Interpretation: `Jose del Carmen Pulgar` is a plausible same-name parent candidate across local Pulgar-line evidence, but the entry-172 father suffix and record linkage are not settled. `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are not the same literal name and must remain separate hypotheses unless a later proof review explains the name forms through source-level evidence.

Scores: identity confidence 0.35; conflict severity 0.70; evidence quality 0.50; conversion confidence 0.48; claim probability 0.35; relevance 0.85; canonical readiness 0.10.

### Hypothesis 4: This entry bridges to Dario Arturo Pulgar-Smith or Dario Arturo Pulgar

The canonical `Dario Arturo Pulgar-Smith` page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly says similarly named Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records should be attached only after identity review. Local staged CV material for `Dario Arturo Pulgar` is document-level occupational evidence and does not provide a parent, child, birth, or direct bridge to this 1888 entry.

Interpretation: no direct bridge exists in this assigned draft or reviewed entry-172 files from `Jose del Carmen Segundo Pulgar Arriagada` or his parents to `Dario Arturo Pulgar-Smith` or `Dario Arturo Pulgar`.

Scores: identity confidence 0.10; conflict severity 0.60; evidence quality 0.30; conversion confidence 0.48; claim probability 0.10; relevance 0.55; canonical readiness 0.00.

### Hypothesis 5: This entry bridges to Dario Jose Pulgar-Arriagada or Darío Pulgar Arriagada

Existing local context includes a separate `Darío Pulgar Arriagada` canonical stub with a 5 December 2000 expropriation event, and staged references elsewhere to `Dario Pulgar-Arriagada`, `Dario Jose Pulgar-Arriagada`, and `Dario/Darío Pulgar Arriagada` as unresolved Pulgar-line clusters. The assigned entry-172 files do not name Dario, Arturo, Jose-as-Dario, Pulgar-Smith, a spouse, a descendant, or any 20th-century identifying event.

Interpretation: this entry can be family-context material after QA, but it cannot attach to any Dario/Darío Pulgar Arriagada identity from the current evidence alone.

Scores: identity confidence 0.08; conflict severity 0.60; evidence quality 0.30; conversion confidence 0.48; claim probability 0.08; relevance 0.50; canonical readiness 0.00.

## Conflicts

- Same entry, different family: Pulgar/Arriagada row versus Burgos/de la Cruz row.
- Name-form uncertainty: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` remain unresolved literal possibilities.
- Parent-candidate conflict: `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are separate local candidates, not merge-ready variants.
- Dario-line overreach risk: matching `Pulgar` and `Arriagada` surname elements are insufficient to merge or attach this 1888 entry to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Darío Pulgar Arriagada.

## Ranked Conclusion

1. Most probable: entry 172 should be treated as a held Pulgar/Arriagada row-control candidate pending targeted conversion QA.
2. Secondary: the Burgos/de la Cruz reading is a conflicting converted-output candidate that must be reconciled or retired for this entry before any promotion.
3. Possible but unproved: the entry-172 father/mother may connect to other Jose/Juana Pulgar-line candidates, but not until source-level QA and separate parent-candidate proof review.
4. Unsupported now: any Dario-line same-person, duplicate-person, name-variant, or relationship claim from this entry.

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, current converted Markdown, assigned chunk, and source packet. The QA note must explicitly state which row controls entry 172 and must certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review for the child identity, birth date/time/place, registration date, sex, father, mother, informant, child-parent relationships, and any parental-pair clue. Then run a separate Jose/Juana parent-candidate identity review before merging or linking parent pages. Do not promote any Dario-line attachment unless a later identity-bearing source directly bridges the relevant Dario candidate to this Jose/Juana/Pulgar-Arriagada evidence.
