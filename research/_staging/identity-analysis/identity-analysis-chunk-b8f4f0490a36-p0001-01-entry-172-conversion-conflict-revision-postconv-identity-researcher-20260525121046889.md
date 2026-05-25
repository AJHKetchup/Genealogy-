---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525121046889
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
conflict_type: row_level_conversion_conflict
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conflict

This note analyzes the exact staged draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md`.

## Blockers First

1. The assigned converted Markdown and the current chunk/source-packet reading are mutually exclusive for entry 172. The current chunk/source-packet reading identifies `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`; the assigned converted Markdown identifies `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`.
2. This is not a spelling, accent, or name-variant conflict. It is a row-level conversion or assignment conflict for the same entry number.
3. The father-field ending after `Jose del Carmen Pulgar` remains unresolved. Preserve the readings `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted image/conversion QA certifies the visible form.
4. Existing canonical wiki pages already contain low-confidence or draft Pulgar/Juana evidence derived from this chunk lineage. Do not use those pages to bootstrap promotion while this conversion conflict is unresolved.
5. No Dario-line merge is supported by this staged draft. `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, and `Dario Pulgar A.` remain separate or unresolved comparison clusters unless a later proof-reviewed bridge supplies full-name/date/relationship continuity.

## Literal Evidence Layers

Current chunk/source-packet reading:

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the chunk; final `S.` requires QA.
- Mother: `Juana Arriagada de Pulgar`.
- Parent residence: `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, recorded as present at the birth.

Assigned converted Markdown reading:

- Entry number: `172`.
- Child: `José Francisco`.
- Birth date/time: `El veinte i seis de Marzo de mil ochocientos ochenta i ocho, a las diez de la noche`.
- Birth place: `En esta`.
- Father: `Oswaldo Gomez`.
- Mother: `Emilia de la Cruz`.
- Informant: `Oswaldo Gomez`.

Existing canonical/local context checked:

- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` has a stub with evidence snapshot claims from the same entry-172 lineage, including probable mother `Juana Arriagada de Pulgar`.
- `wiki/people/juana-arriagada-de-pulgar.md` has a stub with a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.
- `wiki/people/jose-del-carmen-pulgar.md` is a separate stub with a draft child link to `Tulio Cesar Luis Jose`, not a certified entry-172 father bridge.
- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns against automatic merge with similarly named Pulgar clusters.
- `wiki/people/dar-o-pulgar-arriagada.md` has a separate 2000 expropriation-notice context for `Darío Pulgar Arriagada`.
- Local staged context also preserves separate leads for `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dario Pulgar A.`, `Juana de Dios Amagada de Pulgar`, and other Jose/Juana candidates.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

Hypothesis: the controlling source row for entry 172 is the Pulgar/Arriagada row naming `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`.

Evidence supporting:

- The current chunk and assigned source packet agree on the Pulgar/Arriagada row.
- The chunk includes internally coherent page layout for page 58 entries 171-173 and places the Pulgar/Arriagada row at entry 172.
- The staged conflict draft was created specifically because the image-reviewed/current chunk evidence supports this row.
- Existing canonical stubs for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` already reflect this lineage, but those should be treated as downstream context, not independent proof.

Evidence against or limiting:

- The assigned converted Markdown for the same converted file records a completely different entry 172.
- The father-field suffix is not certified.
- The current source packet remains staged and recommends `hold_for_conversion_qa`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | Strong within the current chunk/source-packet layer, reduced by direct converted-file contradiction. |
| conflict_severity | 0.95 | Competing child, parents, birth date, place, and informant. |
| evidence_quality | 0.62 | Civil birth register is high-value, but the derivative readings conflict. |
| conversion_confidence | 0.45 | Mixed because the current chunk and assigned converted Markdown disagree. |
| claim_probability | 0.68 | Plausible controlling row, not promotable until QA certifies it. |
| relevance | 0.85 | Direct Pulgar/Arriagada family relevance if certified. |
| canonical_readiness | 0.10 | Hold for conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is The Gomez/de la Cruz Birth Row

Hypothesis: the controlling source row for entry 172 is the assigned converted Markdown row naming `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`.

Evidence supporting:

- The assigned converted Markdown explicitly records entry 172 with this child and parent set.
- The converted file is the file referenced by the staged draft metadata.

Evidence against or limiting:

- The current chunk and source packet disagree and identify a Pulgar/Arriagada row instead.
- The Gomez/de la Cruz row has no visible Pulgar-line relevance in the staged draft.
- Existing identity-analysis context treats the assigned conversion as the conflicting derivative layer, not as settled source truth.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.42 | Supported by one derivative layer only. |
| conflict_severity | 0.95 | Mutually exclusive with the Pulgar/Arriagada row. |
| evidence_quality | 0.45 | Derivative conversion without reconciliation against the conflicting chunk. |
| conversion_confidence | 0.35 | Low-to-mixed because the chunk/source packet contradicts it. |
| claim_probability | 0.32 | Possible assignment/conversion target, not safe for family work. |
| relevance | 0.05 | No Pulgar/Juana/Dario relevance if this row controls. |
| canonical_readiness | 0.05 | Not ready. |

## Hypothesis 3: Jose del Carmen Pulgar Is The Father Of Jose del Carmen Segundo Pulgar Arriagada

Hypothesis: if the Pulgar/Arriagada row is certified, the father candidate is `Jose del Carmen Pulgar`, possibly with suffix/initial `S.`.

Evidence supporting:

- The current chunk reads the father field as `Jose del Carmen Pulgar S.`.
- The mother is styled `Juana Arriagada de Pulgar`, consistent with a Pulgar spouse/household context, but this is interpretive context only.
- Existing `wiki/people/jose-del-carmen-pulgar.md` shows a separate draft Pulgar father candidate in the same broad local family context.

Evidence against or limiting:

- The father suffix is unresolved.
- The canonical Jose del Carmen Pulgar stub is tied to a separate draft child relationship for `Tulio Cesar Luis Jose`; this entry does not prove that the same Jose is involved.
- Do not merge father candidates by name alone.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.55 | Probable as row-local father if Hypothesis 1 is certified; weaker as canonical `Jose del Carmen Pulgar`. |
| conflict_severity | 0.70 | Father identity affects parent-child relationships and possible duplicate Jose candidates. |
| evidence_quality | 0.60 | Direct register field, but blocked by row conflict and suffix uncertainty. |
| conversion_confidence | 0.45 | Same row-level conversion conflict applies. |
| claim_probability | 0.58 | Reasonable row-local parent claim after QA, not currently promotable. |
| relevance | 0.80 | High for Pulgar-line parentage if certified. |
| canonical_readiness | 0.08 | Hold for conversion QA plus separate Jose identity review. |

## Hypothesis 4: Juana Arriagada de Pulgar Is The Mother Of Jose del Carmen Segundo Pulgar Arriagada

Hypothesis: if the Pulgar/Arriagada row is certified, the mother candidate is `Juana Arriagada de Pulgar`.

Evidence supporting:

- The current chunk/source packet directly reads the mother field as `Juana Arriagada de Pulgar`.
- Existing canonical stubs preserve `Juana Arriagada de Pulgar` and the probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.

Evidence against or limiting:

- The assigned converted Markdown gives a different mother, `Emilia de la Cruz`.
- Existing `Juana de Dios Amagada de Pulgar` context is a separate Jose/Juana line candidate and must not be silently corrected to `Juana Arriagada de Pulgar`.
- The source row must be certified before using this as canonical mother evidence.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Stronger row-local name than the father suffix, but still blocked by row conflict. |
| conflict_severity | 0.80 | Mother identity is mutually exclusive with `Emilia de la Cruz` in the assigned conversion. |
| evidence_quality | 0.62 | Direct register field in the current chunk/source-packet layer. |
| conversion_confidence | 0.45 | Mixed derivative state. |
| claim_probability | 0.64 | Probable if Hypothesis 1 is certified. |
| relevance | 0.85 | High for Pulgar/Arriagada lineage. |
| canonical_readiness | 0.08 | Hold for conversion QA and proof review. |

## Hypothesis 5: Entry 172 Child Or Parents Connect To Dario-Line Candidates

Hypothesis: `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar` may connect genealogically to one or more Dario-line candidates: `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or `Dario Pulgar A.`.

Evidence supporting:

- Names and surnames overlap with the broader Pulgar/Arriagada local research context.
- Existing local staged notes preserve many Pulgar-line comparison candidates, including older medical/professional Dario clusters and canonical `Dario Arturo Pulgar-Smith`.
- A family-context hint makes this row worth double-checking once the literal row is certified.

Evidence against or limiting:

- This staged draft does not name any Dario.
- This staged draft does not state a relationship between the entry-172 child/parents and `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or `Dario Pulgar A.`.
- The source is a 1888 birth entry; Dario-line attachment would require a later bridge through parentage, birth/death chronology, spouse/child evidence, or explicit source identity continuity.
- Existing `Dario Arturo Pulgar-Smith` canonical context is family-supplied and explicitly warns against automatic merge with same-name Pulgar clusters.

Ranked Dario/Pulgar comparison:

| Rank | Hypothesis | Probability | Required next proof step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is only a row-local Pulgar/Arriagada family record, not a Dario identity record. | 0.72 | Complete targeted conversion QA for entry 172 before any downstream identity bridge. |
| 2 | Entry 172 Jose/Juana candidates may be ancestral or collateral leads for a Dario-line person. | 0.30 | After QA, run a focused relationship proof review comparing certified Jose/Juana evidence against proof-reviewed Dario-line family records. |
| 3 | `Jose del Carmen Segundo Pulgar Arriagada` is directly the same person as a Dario candidate. | 0.03 | Require explicit same-person evidence explaining the different given names and chronology; none appears here. |
| 4 | `Jose del Carmen Pulgar` or `Juana Arriagada de Pulgar` should be merged with other Jose/Juana parent candidates now. | 0.12 | Require proof-reviewed parent/spouse/child continuity; do not merge with `Juana de Dios Amagada de Pulgar` or other candidates by surname similarity. |
| 5 | This entry proves a bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`. | 0.05 | Require an explicit bridge source; this draft supplies none. |

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.15 | No Dario is named in the entry. |
| conflict_severity | 0.65 | High duplicate-person risk if used to force Dario or Jose/Juana merges. |
| evidence_quality | 0.40 | Useful context only after the source row is certified. |
| conversion_confidence | 0.45 | Underlying row remains conflicted. |
| claim_probability | 0.12 | Plausible as a future lineage lead, not a current identity bridge. |
| relevance | 0.55 | Potentially relevant to Pulgar-line research, but indirect. |
| canonical_readiness | 0.03 | Not ready for Dario-line attachment. |

## Conflicts And Risks

- Same-person conflict: no same-person merge is supported. The child `Jose del Carmen Segundo Pulgar Arriagada` must remain separate from Dario candidates unless later evidence proves otherwise.
- Duplicate-person conflict: `Jose del Carmen Pulgar` may have multiple local candidate contexts. The entry-172 father field cannot be merged into the existing canonical Jose page until row QA and father suffix review are complete.
- Name-variant conflict: `Jose del Carmen Pulgar S.` is not yet proved to be the same form as `Jose del Carmen Pulgar`; `Juana Arriagada de Pulgar` is not interchangeable with `Juana de Dios Amagada de Pulgar`.
- Relationship conflict: Pulgar/Arriagada parent-child claims are directly contradicted by the converted Markdown's Gomez/de la Cruz parent-child claims for entry 172.
- Chronology conflict: the birth date differs between layers: `1888-03-08 15:00` in the Pulgar/Arriagada reading versus `1888-03-26 22:00` in the Gomez/de la Cruz reading.
- Canonical readiness conflict: existing canonical evidence snapshots appear to contain downstream entry-172 claims, but the current staged conflict requires those claims to remain held pending conversion QA.

## Recommended Next Action

Keep this staged identity analysis and all dependent claims at `hold_for_conversion_qa`.

Exact next proof-review step: targeted conversion QA against the source image and derivative files for `CHUNK-b8f4f0490a36-P0001-01`, specifically entry 172 on page 58. The reviewer must decide whether the controlling entry-172 row is the Pulgar/Arriagada row or the Gomez/de la Cruz row, and must certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

Only after that QA should a separate proof-review promotion step consider narrow claims for the certified child, birth date/place, and parents. A separate identity-bridge review is required before linking any certified Jose/Juana/child evidence to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Pulgar A.`, or other Jose/Juana parent candidates.
