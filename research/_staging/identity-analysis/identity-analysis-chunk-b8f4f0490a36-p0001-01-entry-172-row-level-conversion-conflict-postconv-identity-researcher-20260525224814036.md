---
type: identity_conflict_analysis
status: hold
role: identity_researcher
worker: postconv-identity-analysis-20260525224814036
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: not_ready
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

This note analyzes the exact staged conflict draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md`.

## Blockers First

- Row-control blocker: the current converted Markdown reads entry 172 as a Burgos/de la Cruz birth, while the assigned chunk and source packet read entry 172 as a Pulgar/Arriagada birth. These are separate family rows, not name variants.
- Conversion-certification blocker: no identity, relationship, duplicate-person, or chronology claim from this entry is promotion-ready until targeted conversion QA compares the source image, converted Markdown, chunk, and source packet.
- Father-field blocker: if the Pulgar/Arriagada row is controlling, the father field must remain literal until QA certifies `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Canonical-dependency blocker: existing wiki snapshots for `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Pulgar` are context only here. This task does not edit or promote canonical pages.
- Pulgar-line bridge blocker: this entry does not name Dario, Arturo, Smith, Dario Jose, Dario J., or Darío/Dario Pulgar Arriagada. Shared Pulgar/Arriagada wording is a double-check prompt, not proof of identity.

## Evidence Reviewed

- Staged conflict draft named above.
- Staged source packet `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md`.
- Assigned chunk `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing wiki context: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, and `wiki/people/juana-arriagada-de-pulgar.md`.
- Local staged/reviewed Dario context was checked only for anti-conflation: staged references to `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar-Arriagada`, and `Dario Pulgar A.` do not supply a bridge from this 1888 row.

## Literal Source Readings

### Reading A: Pulgar/Arriagada Row

The assigned chunk and source packet read register page 58, entry 172 as:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the current chunk/source-packet reading, with the final suffix still requiring targeted QA.
- Mother: `Juana Arriagada de Pulgar`.
- Parents' residence: `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, present at birth, age 26, employee, resident at `Calle de Valdivia`.

### Reading B: Burgos/de la Cruz Row

The current converted Markdown reads entry 172 as:

- Child: `José Miguel`; sex `Varon`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`.
- Birthplace: `En esta`.
- Father and informant: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.

## Interpretation

Reading A and Reading B conflict on the child, parents, birth date, birthplace, and informant. The best classification is row-level conversion conflict. The evidence does not support treating `Jose del Carmen Segundo Pulgar Arriagada` and `José Miguel` as the same person, duplicates, or variants.

If Reading A is certified, it can proceed to proof review for a narrow birth-registration identity and parent-candidate claims. If Reading B is certified, the Pulgar/Arriagada claim set must not be promoted from this source. This identity analysis cannot choose the controlling row because the next required step is conversion QA, not interpretation.

## Hypotheses And Scores

| Rank | Hypothesis | Supporting evidence | Conflicts / limits | Probability | Identity confidence | Claim probability | Canonical readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`. | Assigned chunk and source packet agree on child, parents, birth details, and informant. | Current converted Markdown reads a different family; father suffix unresolved. | 0.64 | 0.52 | 0.56 | 0.10 |
| 2 | Entry 172 is the Burgos/de la Cruz row for `José Miguel`. | Current converted Markdown gives an internally coherent entry-172 reading. | It conflicts with assigned chunk/source packet and has no Pulgar relevance. | 0.30 | 0.42 | 0.44 | 0.05 |
| 3 | The Pulgar-reading father is the same person as canonical `Jose del Carmen Pulgar`. | Reading A gives father as `Jose del Carmen Pulgar S.` or a close literal variant; canonical stub exists. | Name overlap alone is insufficient; suffix, spouse context, residence, and separate child claims need proof review. | 0.35 | 0.30 | 0.32 | 0.05 |
| 4 | `Juana Arriagada de Pulgar` is the mother in Reading A. | Reading A directly names her as mother; canonical stub contains related staged context. | Fully dependent on row-control QA; do not merge with other Juana candidates by similarity. | 0.60 | 0.50 | 0.54 | 0.10 |
| 5 | This row supports a same-person or family bridge to a Dario Pulgar candidate. | The surnames Pulgar/Arriagada are family-context hints. | No Dario/Arturo/Smith/Jose/Dario J. bridge, no relationship statement, and no chronology bridge. | 0.04 | 0.03 | 0.03 | 0.00 |

## Pulgar-Line Candidate Comparison

- `Dario Arturo Pulgar-Smith`: canonical context is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic attachment of similarly named records. This entry does not state `Dario`, `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, or any descendant relationship. Probability this row alone supports attachment: 0.03.
- `Dario Arturo Pulgar`: staged CV contexts use document-level `Dario Arturo Pulgar`, but this row contains no `Dario Arturo`, CV, occupation sequence, residence, spouse, child, or identity bridge to that subject. Probability this row alone supports attachment: 0.04.
- `Dario Jose Pulgar-Arriagada`: staged portrait/Geneva contexts use this name largely from source title/path or photograph context. This row reads either `Jose del Carmen Segundo Pulgar Arriagada` or `José Miguel`, not `Dario Jose`. Probability this row alone supports attachment: 0.04.
- `Dario/Darío Pulgar Arriagada`: local context includes a canonical `Darío Pulgar Arriagada` 2000 expropriation mention and staged official-list/medical-title contexts for similar names. This 1888 row does not link the child or parents to those later public-role/legal-notice identities. Probability this row alone supports attachment: 0.05.
- Jose/Juana parent candidates: within Reading A only, `Jose del Carmen Pulgar [S./?]` and `Juana Arriagada de Pulgar` are candidate parents of `Jose del Carmen Segundo Pulgar Arriagada`. They should remain staged until row-control QA and parent-child proof review. Do not use them as a bridge to Dario candidates without a separate proof-reviewed relationship chain.

## Conflicts

- Same-person conflict: Reading A child `Jose del Carmen Segundo Pulgar Arriagada` and Reading B child `José Miguel` are not supported as the same person.
- Duplicate-person conflict: no duplicate conclusion is ready for `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Juana Arriagada de Pulgar`; existing wiki entries are not independent resolution of this row-control issue.
- Name-variant conflict: father `Jose del Carmen Pulgar S.` is a literal-reading uncertainty, not a normalized name variant to collapse.
- Relationship conflict: Reading A parent-child relationships and Reading B parent-child relationships are mutually incompatible for entry 172 until QA resolves the row.
- Chronology conflict: Reading A gives birth on 8 March 1888 at 3 p.m.; Reading B gives birth on 6 April 1888 at 10 p.m. These cannot both be facts for the same entry-172 child.
- Dario-line conflation risk: high if Pulgar/Arriagada surname overlap is used to merge with Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Darío Pulgar Arriagada, or Dario Pulgar A.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| Identity confidence | 0.52 | Moderate for distinguishing competing row candidates; low for canonical attachment. |
| Conflict severity | 0.95 | The conflict changes child, parents, date, place, and informant. |
| Evidence quality | 0.62 | Chunk/source packet are detailed, but the current converted Markdown materially contradicts them. |
| Conversion confidence | 0.35 | Derivatives disagree; targeted conversion QA is required. |
| Claim probability | 0.56 | Pulgar/Arriagada claims are plausible from chunk/packet but not promotable. |
| Relevance | 0.90 | Highly relevant to Pulgar/Arriagada review if the row is confirmed. |
| Canonical readiness | 0.10 | Not ready for promotion, merge, rename, or relationship update. |

## Recommended Next Action

Keep this draft on `hold_for_conversion_qa`. The exact next proof-review/promotion step is targeted conversion QA for page 1 / register page 58 / entry 172: compare the source image, current converted Markdown, assigned chunk, and staged source packet; decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz; and, if Pulgar/Arriagada controls, certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, run a narrow proof review for the certified row's child identity, birth facts, father claim, mother claim, informant claim, and parent-child relationships. A separate identity-bridge proof review is required before connecting this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Pulgar A.`, or any Jose/Juana parent-candidate chain.
