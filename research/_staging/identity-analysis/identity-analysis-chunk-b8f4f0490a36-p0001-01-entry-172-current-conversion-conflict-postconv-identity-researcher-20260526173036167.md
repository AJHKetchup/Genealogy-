---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260526173036167
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
created: 2026-05-26
---

# Identity Analysis: Entry 172 Current Conversion Conflict

## Blockers First

- The controlling row for entry `172` is not conversion-stable. The assigned chunk and staged source packet read entry 172 as a Pulgar/Arriagada birth registration, while the current converted Markdown reads entry 172 as a Burgos/de la Cruz birth registration.
- This is a material row-level conversion conflict, not a same-person, duplicate-person, or spelling-variant conflict. It changes the child, birth date/time/place, father, mother, informant, residences, and relationship candidates.
- The father field in the Pulgar/Arriagada row is not exact-name ready. The chunk reads `Jose del Carmen Pulgar S.`, while the staged source packet preserves the visible reading only as at least `Jose del Carmen Pulgar` with an unresolved trailing letter or mark.
- The named `$genealogy-proof-review` skill file was not available in this session's listed skills. This note follows the local proof-review contract visible in staged reviews: literal readings first, interpretation separate, uncertainty retained, scored confidence supplied, and no promotion without conversion/source fit.
- No external research was performed. This analysis uses only the assigned staged conflict draft, referenced staged source packet, converted Markdown, chunk Markdown, reviewed local notes visible in the staging area, and existing canonical wiki pages.

## Literal Evidence

The assigned staged conflict draft says the Pulgar/Arriagada reading for entry `172` is:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`, male.
- Birth: 8 March 1888, about 3 p.m., `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar`; assigned chunk reads `Jose del Carmen Pulgar S.`, with trailing mark unresolved.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth.

The referenced staged source packet repeats the same row and says direct image review supports the Pulgar/Arriagada row on register page 58, entry 172, but holds all dependent claims because the current converted Markdown gives a different entry.

The assigned chunk currently transcribes entry `172` as:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`, male.
- Registered: 7 April 1888.
- Birth: 8 March 1888 at 3 p.m., `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.`, Chilean, employee, resident `Calle de Colipi`.
- Mother: `Juana Arriagada de Pulgar`, Chilean, `Su sexo`, resident `Calle de Colipi`.
- Informant: `Ernesto Herrera L.`, age 26, employee, resident `Calle de Valdivia`, present at the birth.

The current converted Markdown currently transcribes entry `172` as a different family:

- Child: `Jose Miguel`, male.
- Birth: 6 April 1888 at 10 p.m., `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

## Interpretation

The Pulgar/Arriagada row and the Burgos/de la Cruz row cannot both be treated as the same entry-172 event. They describe different children, different parents, different date/place details, and different informants. The likely issue is conversion row-control or source-image/converted-file mismatch, not identity ambiguity among the named people.

If targeted conversion QA accepts the source packet and assigned chunk as controlling, the record is probable evidence for a birth registration of `Jose del Carmen Segundo Pulgar Arriagada` and a mother-child relationship to `Juana Arriagada de Pulgar`. The father-child relationship should remain slightly lower confidence until the father suffix after `Pulgar` is certified.

If targeted conversion QA accepts the current converted Markdown as controlling, the Pulgar/Arriagada claims from this staged packet must not be promoted from this source path, and any existing staged/canonical Pulgar evidence tied to this conversion should be flagged for revision.

## Hypotheses

| rank | hypothesis | probability | evidence and limits |
| ---: | --- | ---: | --- |
| 1 | Entry 172 on the source image/chunk is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.72 | Supported by the assigned chunk and staged source packet with image-reviewed comments. Capped by direct conflict with the current converted Markdown and father-suffix uncertainty. |
| 2 | Entry 172 in the current converted Markdown is the Burgos/de la Cruz birth registration for `Jose Miguel`. | 0.20 | Supported by the assembled converted Markdown currently on disk. Lower probability because the staged source packet and assigned chunk both identify a coherent Pulgar/Arriagada row and explicitly describe the converted Markdown as conflicting. |
| 3 | The two readings are name variants or duplicate identities for the same child/family. | 0.02 | Not supported. Names, parents, birth details, and informant differ too much for a same-person explanation. |
| 4 | The Pulgar/Arriagada row belongs to a neighboring entry rather than entry 172. | 0.06 | Possible only as a row alignment/control problem. Requires targeted page-image QA; cannot be resolved by identity analysis alone. |

## Person And Relationship Comparisons

### Jose del Carmen Segundo Pulgar Arriagada

Existing wiki page `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` already has probable/draft evidence generated from the same `CHUNK-b8f4f0490a36-P0001-01` family of staged materials. This current task does not add independent identity evidence; it confirms that all such claims remain dependent on resolving the row-level conversion conflict.

Identity confidence for this source-local child if Pulgar row controls: 0.70.

Canonical readiness for new or stronger facts now: 0.10.

### Jose del Carmen Pulgar Father Candidate

Existing wiki page `wiki/people/jose-del-carmen-pulgar.md` has separate draft evidence as parent of `Tulio Cesar Luis Jose` from entry 513 material. This staged entry 172 can support only a row-local father candidate named at least `Jose del Carmen Pulgar`; it does not prove the entry-172 father is the same person as the entry-513 father. The possible suffix `S.` after `Pulgar` must not be normalized away or expanded without targeted QA.

Identity confidence for base father-name reading if Pulgar row controls: 0.62.

Same-person confidence with the entry-513 `Jose del Carmen Pulgar` candidate: 0.35.

Canonical readiness for a father merge or added cross-record identity: 0.05.

### Juana Arriagada de Pulgar And Juana Parent Candidates

Existing wiki page `wiki/people/juana-arriagada-de-pulgar.md` is already tied to this entry-172 evidence as probable mother of `Jose del Carmen Segundo Pulgar Arriagada`. Existing wiki page `wiki/people/juana-de-dios-amagada-de-pulgar.md` is a separate candidate tied to entry 513 material as mother of `Tulio Cesar Luis Jose`.

The entry-172 mother reading `Juana Arriagada de Pulgar` is not the same literal name as `Juana de Dios Amagada de Pulgar`. The shared married-name form `de Pulgar` is not enough to merge them. The `Arriagada` / `Amagada` similarity is a double-check clue only, especially because entry 513 materials elsewhere have their own conversion instability around `Amagada` / `Amador`.

Identity confidence for entry-172 mother reading if Pulgar row controls: 0.68.

Same-person confidence between `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar`: 0.18.

Canonical readiness for any Juana merge: 0.03.

### Dario Arturo Pulgar-Smith

Existing wiki page `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatically merging similarly named source clusters. This entry-172 draft does not name Dario Arturo Pulgar-Smith, does not name Dario Arturo Pulgar, and does not supply a later-life bridge.

Same-person or direct-relationship confidence from this draft alone: 0.01.

Canonical readiness for attaching this birth-register evidence to Dario Arturo Pulgar-Smith: 0.00.

### Dario Arturo Pulgar

Local staged CV/Habitat materials use document-level `Dario Arturo Pulgar` contexts, but this entry-172 staged draft does not name that person. No identity bridge exists here from `Jose del Carmen Segundo Pulgar Arriagada` or his parents to the CV subject.

Same-person or direct-relationship confidence from this draft alone: 0.01.

Canonical readiness for attachment: 0.00.

### Dario Jose Pulgar-Arriagada

No source-local evidence in this entry names `Dario Jose Pulgar-Arriagada`. The only Pulgar-Arriagada child in the Pulgar-row hypothesis is `Jose del Carmen Segundo Pulgar Arriagada`.

Same-person or direct-relationship confidence from this draft alone: 0.01.

Canonical readiness for attachment: 0.00.

### Dario/Dario Pulgar Arriagada

Existing wiki page `wiki/people/dar-o-pulgar-arriagada.md` is tied to a 2000 expropriation event for `Dario Pulgar Arriagada`. This entry-172 draft does not name Dario and does not establish a relationship bridge from the 1888 child, father, or mother to the 2000 expropriation person.

Same-person or direct-relationship confidence from this draft alone: 0.01.

Canonical readiness for attachment: 0.00.

### Dario Pulgar Passenger Candidates

Existing wiki pages `wiki/people/dario-pulgar-adult-passenger-age-64.md` and `wiki/people/dario-pulgar-child-passenger-age-11.md` remain separate passenger-list candidates. This entry-172 draft supplies no passenger evidence, age match, occupation bridge, residence continuity, or family relationship bridge to either passenger candidate.

Same-person or direct-relationship confidence from this draft alone: 0.01 for each candidate.

Canonical readiness for attachment: 0.00.

## Conflict Assessment

- Same-person conflict: high risk if anyone merges the Pulgar/Arriagada row with the Burgos/de la Cruz converted row. These are distinct identity clusters unless QA proves one is not the controlling entry.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` and `Juana...de Pulgar` candidates across entry 172 and entry 513; current evidence does not support merge.
- Name-variant risk: low for Burgos/de la Cruz versus Pulgar/Arriagada; high enough for `Arriagada` / `Amagada` to justify double-check only, not correction.
- Relationship conflict: severe. The child-parent set changes completely depending on row control.
- Chronology conflict: severe for entry 172 if both readings are treated as claims from the same record; birth date differs by nearly a month and the place/time differ.

## Scores

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | Probable for the source-local Pulgar child if the assigned chunk/source packet controls, but capped by converted-file conflict. |
| conflict_severity | 0.95 | The conflict changes the entire family row and all dependent claims. |
| evidence_quality | 0.68 | Strong local derivative agreement between chunk and source packet, but current converted Markdown directly conflicts. |
| conversion_confidence | 0.35 | The source packet explicitly labels conversion confidence low and calls for targeted QA. |
| claim_probability | 0.62 | Pulgar-row claims are more likely than the current conversion reading from the staged evidence, but not promotion-grade. |
| relevance | 0.90 | High family relevance because Pulgar and Arriagada are matched family terms and existing wiki pages already reference this cluster. |
| canonical_readiness | 0.08 | Hold for conversion QA and rerun proof review before any canonical update, merge, or relationship promotion. |

## Ranked Next Steps

| rank | required step | exact action |
| ---: | --- | --- |
| 1 | Targeted conversion QA | Compare the original source image, current converted Markdown, assigned chunk, and staged source packet for page 58 entry 172. Decide whether the controlling row is Pulgar/Arriagada, Burgos/de la Cruz, or a row-alignment variant. |
| 2 | Father-field certification | If the Pulgar/Arriagada row controls, record the father field only to the visible extent as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. |
| 3 | Rerun proof review | After QA, proof-review the child identity, birth date/time/place, father claim, mother claim, informant fact, child-parent relationships, and parent-pair clue. |
| 4 | Identity bridge review | Only after proof review, compare `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` against entry-513 Jose/Juana candidates. Preserve separate hypotheses unless direct bridge evidence is accepted. |
| 5 | Dario-line protection | Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or passenger Dario candidates without a separate, proof-reviewed identity bridge. |

## Recommendation

Keep the assigned conflict draft and all dependent claims at `hold_for_conversion_qa`. Do not merge people, rename canonical pages, promote facts, or attach this evidence to Dario-line profiles. The exact next proof-review or promotion step is not promotion; it is targeted conversion QA for entry 172 followed by a fresh proof review of the reconciled row and father-field reading.
