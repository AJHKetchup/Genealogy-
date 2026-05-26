---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260525234847240
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
canonical_readiness: hold
---

# Identity Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The staged conflict draft reports a material row-control conflict for entry 172. The assigned chunk/source-image reading identifies a Pulgar/Arriagada birth row, while the current converted Markdown identifies a different Burgos/de la Cruz family.
- The father field for the Pulgar/Arriagada row remains unresolved. The local evidence supports that it begins `Jose del Carmen Pulgar`, but the exact trailing form must be certified as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- No child identity, birth fact, parent-child relationship, parent identity merge, or Pulgar-to-Dario comparison should be promoted until targeted conversion QA decides which entry-172 row controls the source and certifies the father-field reading.
- The requested `$genealogy-proof-review` skill file is not installed in this session. This note follows the dispatched evidence contract directly: literal readings are kept separate from interpretation, hypotheses remain separate, scores are explicit, and canonical promotion is held.

## Evidence Boundary

Reviewed local evidence only:

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md`.
- Referenced source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md`.
- Referenced chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing canonical context: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/jose-del-carmen-pulgar.md`, and related search hits for `Juana de Dios Amagada de Pulgar`.

No external research was performed.

## Literal Source Readings

### Assigned Chunk And Source-Packet Reading

The assigned chunk and source packet preserve entry 172 as:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: 8 March 1888 at 3 p.m.
- Birth place: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the chunk transcription; source-packet visual note says the line begins `Jose del Carmen Pulgar` and the trailing element is not certified.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employee, resident at Calle de Valdivia.

### Current Converted Markdown Reading

The current converted Markdown records entry 172 as:

- Child: `Jose Miguel`.
- Sex: `Varon`.
- Birth: 6 April 1888 at 10 p.m.
- Birth place: `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

## Interpretation

The two readings cannot describe the same birth-registration row. The conflict is not a minor name variant. It changes the child, both parents, birth date, birth place, informant, and family cluster.

The strongest local explanation is a conversion-control or row-control problem in the converted Markdown, because the referenced source packet states that visual review found page 58 row 172 to be the Pulgar/Arriagada row. However, identity analysis should not correct the conversion silently. The controlling next step is targeted conversion QA, not promotion.

## Hypotheses And Scores

| rank | hypothesis | supporting evidence | conflicts or limits | probability | identity confidence | next proof-review or promotion step |
| ---: | --- | --- | --- | ---: | ---: | --- |
| 1 | Entry 172 should be treated as a held Pulgar/Arriagada birth-registration candidate for `Jose del Carmen Segundo Pulgar Arriagada`. | Assigned chunk and source packet both give this row-level reading, including Pulgar/Arriagada parents and 8 March 1888 birth details. Existing canonical page already has a low-confidence snapshot for this child and Juana Arriagada de Pulgar. | Current converted Markdown materially disagrees; father suffix remains unresolved. | 0.78 | 0.70 | Targeted conversion QA must certify row 172 and father field before proof review can accept claims or relationships. |
| 2 | Entry 172 should be treated as the Burgos/de la Cruz birth of `Jose Miguel`. | Current converted Markdown gives `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`. | Staged conflict draft and source packet say the visible source row is Pulgar/Arriagada, not Burgos/de la Cruz. No existing Pulgar canonical context supports this reading. | 0.18 | 0.20 | Keep as competing conversion reading only until targeted conversion QA resolves the source image against the conversion. |
| 3 | The Pulgar/Arriagada reading and Burgos/de la Cruz reading are duplicate identities or same-person variants. | None beyond both being labeled entry 172 in local derivatives. | Names, parents, birth date, place, and informant all differ. This is a row conflict, not a name variant. | 0.02 | 0.02 | Reject unless conversion QA finds a structural explanation tying both rows to the same source record. |
| 4 | The entry-172 child is the same person as `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. | Only surname/family-context overlap exists if the Pulgar/Arriagada row controls. | The row names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario, Arturo, Smith, or Jose as a Dario middle-name expansion. No chronology or relationship bridge appears in this draft. | 0.01 | 0.01 | Do not merge. Require a separate identity-bridge proof review using reviewed local evidence that explicitly connects this birth child to a Dario candidate. |

## Pulgar-Line Comparison

| candidate or cluster | local evidence compared | assessment |
| --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | Canonical page is family-supplied as Alexander John Heinz's maternal grandfather and warns not to attach Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records without identity review. | No same-person support from this entry-172 draft. The birth row, if accepted, names `Jose del Carmen Segundo Pulgar Arriagada`; it does not state Smith, Arturo, Dario, Alexander John Heinz, or a grandchild relationship. |
| `Dario Arturo Pulgar` | Local staged CV contexts use document-level attribution to `Dario Arturo Pulgar` and repeatedly require identity-bridge review before canonical attachment. | No support from this entry-172 draft. A Pulgar surname alone is insufficient. |
| `Dario Jose Pulgar-Arriagada` | Local staged photo/source-title contexts identify or flag `Dario Jose Pulgar-Arriagada`; other notes emphasize source-scope and image-identity limits. | No support from this row. The child name is `Jose del Carmen Segundo`, not `Dario Jose`; do not infer a Dario identity from the maternal surname pattern. |
| `Dario/Dario Pulgar Arriagada` | Canonical `Darío Pulgar Arriagada` page has a 2000 expropriation event. Other staged tasks mention `Darío J. Pulgar Arriagada` in a 1918 medical-title context with the initial unexpanded. | No support from this 1888 birth draft. The chronology and name do not bridge to the 1918 or 2000 contexts. |
| `Jose del Carmen Pulgar` father candidate | Entry-172 Pulgar reading names a father beginning `Jose del Carmen Pulgar`; existing `wiki/people/jose-del-carmen-pulgar.md` has a separate draft child link to Tulio Cesar Luis Jose. | Possible same-name parent cluster, but not enough for merge. Exact father suffix and row control must be certified first, then compared against the Tulio/entry-513 parent candidate in proof review. |
| `Juana Arriagada de Pulgar` mother candidate | Entry-172 Pulgar reading names the mother as `Juana Arriagada de Pulgar`; existing canonical stub links her to `Jose del Carmen Segundo Pulgar Arriagada` with low confidence. | Plausible mother candidate if the Pulgar row controls. Hold until conversion QA confirms row 172. |
| `Juana de Dios Amagada de Pulgar` / other Juana parent candidates | Existing canonical/search context shows a separate Juana parent candidate in the Tulio/entry-513 cluster. | Do not merge with `Juana Arriagada de Pulgar` by given name or married name alone. Requires a separate parent-candidate proof review comparing exact surname readings, child entries, residences, dates, and spouse/father context. |

## Conflict Assessment

- Same-person conflict: high risk if the converted Markdown reading is promoted as entry 172 while the Pulgar/Arriagada source-packet row is also promoted.
- Duplicate-person conflict: moderate risk around `Jose del Carmen Pulgar` because existing canonical context has another same-name parent candidate; current evidence does not prove duplication or sameness.
- Name-variant conflict: low for the child because `Jose Miguel` and `Jose del Carmen Segundo Pulgar Arriagada` are not credible variants of one another in this record context.
- Relationship conflict: high. The conflicting readings assign entirely different parents to entry 172.
- Chronology conflict: high. Birth 8 March 1888 at 3 p.m. conflicts with birth 6 April 1888 at 10 p.m.
- Conversion conflict: severe. The converted Markdown and assigned chunk/source-packet row disagree on the core row identity.

## Scores

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | The Pulgar/Arriagada row is supported by assigned chunk and source packet, but conversion QA is still required. |
| conflict_severity | 0.95 | Competing readings change all identity-bearing facts. |
| evidence_quality | 0.72 | Local evidence includes chunk text and a source-packet visual note, but this analysis did not perform image rereading and the current conversion disagrees. |
| conversion_confidence | 0.30 | The assigned chunk is internally strong, but the official converted Markdown is materially inconsistent. |
| claim_probability | 0.78 | Probable that the held Pulgar/Arriagada row is the relevant family candidate, subject to row-control QA. |
| relevance | 0.95 | The row directly concerns Pulgar/Arriagada birth and parent candidates. |
| canonical_readiness | 0.10 | Hold. No canonical promotion should occur before targeted conversion QA and proof review. |

## Recommended Next Action

Keep this analysis and all related claims on `hold_for_conversion_qa`.

Exact next step: targeted conversion QA must visually compare `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png` against entry 172 on page 58 and decide:

- whether row 172 controls as `Jose del Carmen Segundo Pulgar Arriagada` or as `Jose Miguel`;
- whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`;
- whether the existing converted Markdown should be corrected or superseded before any proof-review promotion.

After conversion QA, run proof review on the corrected/accepted row-level source packet before promoting child identity, birth facts, mother relationship, father relationship, or any comparison to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, `Jose del Carmen Pulgar`, or Juana parent candidates.
