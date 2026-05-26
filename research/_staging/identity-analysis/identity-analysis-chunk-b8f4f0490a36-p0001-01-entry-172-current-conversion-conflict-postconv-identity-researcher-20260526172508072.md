---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526172508072
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
conflict_type: row_level_conversion_conflict
promotion_recommendation: hold_for_conversion_qa
created: 2026-05-26
---

# Identity Analysis: Entry 172 Current Conversion Conflict

## Blockers First

1. The current converted Markdown and the assigned chunk give materially different people for the same entry number `172`. This is a row-control conflict, not a same-person, duplicate-person, or spelling-variant issue.
2. The father field in the Pulgar/Arriagada row is not fully certified. The chunk reads `Jose del Carmen Pulgar S.`, while the source packet preserves the father as `Jose del Carmen Pulgar` with a trailing letter or mark unresolved.
3. No Dario identity bridge is present in this staged draft, source packet, converted file, or chunk. This entry does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario Pulgar Arriagada, or Dario Pulgar-Arriagada.
4. The entry-172 mother candidate `Juana Arriagada de Pulgar` must not be silently merged with the separate existing wiki/staged candidate `Juana de Dios Amagada de Pulgar`; those names may deserve comparison later, but this draft does not prove same-person identity.
5. Existing canonical pages already contain some derivative evidence snapshots for this entry, but this controller task owns only this staged analysis note. No canonical update, merge, or fact promotion is ready.

## Literal Source Readings Preserved

From the assigned chunk for `CHUNK-b8f4f0490a36-P0001-01`, entry `172` reads as a Pulgar/Arriagada birth registration:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Registration date: 7 April 1888.
- Birth: 8 March 1888, about 3 p.m., `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the chunk; source packet/image-review caution leaves the final `S.` or mark unresolved.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.

From the current converted Markdown, entry `172` instead reads as a Burgos/de la Cruz birth registration:

- Child: `Jose Miguel`; sex `Varon`.
- Birth: 6 April 1888, about 10 p.m., `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

## Hypotheses Ranked

### H1: Entry 172 is the Pulgar/Arriagada row, and the current converted Markdown has a row-level conversion error

This is the strongest working hypothesis. The staged conflict draft and source packet both report that the assigned chunk and image-reviewed evidence support a Pulgar/Arriagada row for entry `172`. The row identifies a child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` with an unresolved final element, and mother `Juana Arriagada de Pulgar`.

Supporting evidence:

- The assigned chunk gives a full row for entry `172` with Pulgar/Arriagada names, dates, residences, and informant.
- The source packet states that the original page image shows register page 58 with entry number `172` in the second row on the left page and that the row is visually consistent with the Pulgar/Arriagada reading.
- The staged draft correctly treats the Burgos/de la Cruz data as incompatible, not as a name variant.

Conflicts and limits:

- The converted Markdown still records a complete Burgos/de la Cruz row under entry `172`.
- The father suffix/mark remains unresolved and should not be normalized to either `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` for canonical use.

Score: identity confidence 0.78; claim probability 0.80 for the narrow Pulgar/Arriagada row identity; evidence quality 0.72; conversion confidence 0.35 because derivative artifacts conflict; relevance 0.95; canonical readiness 0.20.

### H2: Entry 172 is the Burgos/de la Cruz row in the converted Markdown

This is a weaker hypothesis for this staged analysis because it depends on the current converted Markdown despite the assigned chunk and source packet preserving a contradictory image-reviewed Pulgar row.

Supporting evidence:

- The current converted Markdown explicitly labels the Burgos/de la Cruz record as `Entry 172`.
- The converted Markdown provides internally coherent child, parent, birth, and informant details for a birth registration.

Conflicts and limits:

- The assigned chunk for the same chunk id gives a different complete row for entry `172`.
- The source packet reports direct image review supporting Pulgar/Arriagada for entry `172`.
- The staged conflict draft identifies the current conversion as the artifact needing QA, not as controlling evidence.

Score: identity confidence 0.22; claim probability 0.20; evidence quality 0.35; conversion confidence 0.25; relevance 0.80; canonical readiness 0.05.

### H3: `Jose del Carmen Pulgar S.` and `Jose del Carmen Pulgar` are the same father reading with an unresolved suffix/mark

This is plausible but not settled. The assigned chunk has `Jose del Carmen Pulgar S.`, while the source packet says the father field is visible to at least `Jose del Carmen Pulgar` and the trailing mark is uncertified.

Supporting evidence:

- Both forms share the same core name in the same father field of the same Pulgar/Arriagada row.
- Existing wiki context has a stub `Jose del Carmen Pulgar`, but the page does not itself settle the entry-172 suffix.

Conflicts and limits:

- The final `S.` may be a suffix, abbreviation, stray mark, or conversion artifact.
- Do not create a separate duplicate person for `Jose del Carmen Pulgar S.` and do not merge the suffix away until targeted QA certifies the field.

Score: identity confidence 0.68 for same father-field referent; conflict severity 0.55; evidence quality 0.62; conversion confidence 0.40; claim probability 0.65; relevance 0.90; canonical readiness 0.25.

### H4: `Juana Arriagada de Pulgar` is the mother in entry 172, but not proved identical to `Juana de Dios Amagada de Pulgar`

The entry-172 mother reading is relatively strong within the Pulgar-row hypothesis. A broader same-person comparison with `Juana de Dios Amagada de Pulgar` is not ready.

Supporting evidence:

- The assigned chunk and source packet both identify entry-172 mother as `Juana Arriagada de Pulgar`.
- Existing canonical wiki page `wiki/people/juana-arriagada-de-pulgar.md` already reflects an entry-172 child link as probable, though this analysis does not promote or revise it.

Conflicts and limits:

- Existing wiki context also has `Juana de Dios Amagada de Pulgar`, connected to a different 1889 entry and child `Tulio Cesar Luis Jose`.
- `Arriagada`, `Amagada`, and possible `Amador` variants appear in separate staged contexts. Similarity plus Pulgar household context is a reason for future double-checking, not a merge.

Score: identity confidence 0.82 for the entry-172 mother reading; 0.30 for same-person identity with `Juana de Dios Amagada de Pulgar`; conflict severity 0.50; evidence quality 0.70; conversion confidence 0.42; claim probability 0.78; relevance 0.90; canonical readiness 0.25.

### H5: This entry provides a lineage bridge to a Dario Pulgar candidate

This hypothesis is not supported by this evidence.

Comparison required by Pulgar-line handling:

- `Dario Arturo Pulgar-Smith`: Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic merges with similarly named source clusters. Entry 172 does not name Dario, Arturo, Smith, Alexander John Heinz, or a direct relationship to the canonical person.
- `Dario Arturo Pulgar`: Staged CV contexts use this name, but this birth-registration entry does not name Dario Arturo Pulgar or connect to the CV subject.
- `Dario Jose Pulgar-Arriagada`: Existing staged photo/ICRC contexts use this name, but this entry names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose.
- `Dario Pulgar Arriagada` / `Dario Pulgar-Arriagada` / `Darío J. Pulgar Arriagada`: Existing staged medical-title and international-listing contexts use these forms, but this entry does not name Dario and does not establish that `Jose del Carmen Segundo Pulgar Arriagada` is the same person, a parent, or an ancestor.
- Jose/Juana parent candidates: Entry 172 can support only a local parent cluster for `Jose del Carmen Segundo Pulgar Arriagada` with father `Jose del Carmen Pulgar...` and mother `Juana Arriagada de Pulgar`, after QA. It does not connect those parents to any Dario candidate yet.

Score: identity confidence 0.05 for any Dario same-person or lineage bridge from this entry alone; conflict severity 0.80 if promoted prematurely; evidence quality 0.20 for Dario linkage; conversion confidence 0.35; claim probability 0.05; relevance 0.65 because Pulgar-line context makes it worth tracking; canonical readiness 0.00.

## Conflict Assessment

The controlling conflict is row-level conversion conflict for entry `172`: Pulgar/Arriagada versus Burgos/de la Cruz. This conflict affects child identity, birth date/time/place, father, mother, informant, and all downstream relationship candidates. The conflict severity is high because accepting the wrong row would attach a complete unrelated family to the entry number.

The secondary conflict is father-field precision. The safe literal range is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until targeted QA certifies the visible final mark.

The Dario/Pulgar-line comparison produces a negative bridge result: no same-person, duplicate-person, parent-child, grandparent, or lineage claim to a Dario identity is supported by this entry alone.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Probable that the staged Pulgar/Arriagada row is the row under review, but row-control QA is still required. |
| conflict_severity | 0.92 | Two entirely different families are recorded for the same entry number across derivative artifacts. |
| evidence_quality | 0.72 | The chunk and source packet give detailed, internally coherent Pulgar evidence, but the converted Markdown conflict reduces proof readiness. |
| conversion_confidence | 0.35 | Current conversion artifacts disagree materially. |
| claim_probability | 0.80 | Probable for the narrow Pulgar/Arriagada row reading; low for canonical promotion before QA. |
| relevance | 0.95 | Directly relevant to Pulgar/Arriagada staged identity and relationship candidates. |
| canonical_readiness | 0.20 | Hold pending targeted conversion QA and proof review. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, current converted Markdown, assigned chunk, and source packet. The QA note must decide which row controls entry `172` and explicitly certify the father field as one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before promoting any child identity, birth fact, father relationship, mother relationship, or parent-attribute claim. A separate identity-bridge proof review is required before attaching this evidence to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, `Dario Pulgar-Arriagada`, or any Jose/Juana candidate outside the entry-172 parent cluster.
