---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527233759480
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-row-control-postconv-evidence-extraction-20260527222756266.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-row-control-postconv-evidence-extraction-20260527222756266.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260527222756266.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
canonical_readiness: hold_for_proof_review
---

# Identity Analysis: Entry 172 Row-Control Conflict

## Blockers First

1. The current converted Markdown and the row-controlled chunk/source packet disagree on the identity of entry `172`. The converted Markdown says entry `172` is `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at about 10 p.m. at `En esta`. The image-reviewed staged draft and assigned chunk say physical row `172` is `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`.
2. Do not merge the Burgos/de la Cruz child and parent set with the Pulgar/Arriagada child and parent set. They are incompatible row identities for the same entry number in derivative materials.
3. The father field boundary must remain narrow. The assigned chunk includes `Jose del Carmen Pulgar S.`, but the staged source packet certifies only `Jose del Carmen Pulgar` and treats any trailing suffix or mark after `Pulgar` as unresolved.
4. The record does not name `Dario`, `Arturo`, `Smith`, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`. Any Dario-line relevance is family-context or cluster-context only and cannot support a same-person merge from this entry.
5. Existing canonical pages already contain probable/draft evidence snapshots for some entry-172 facts. This analysis does not promote, rename, merge, or edit canonical pages.

## Literal Evidence

- Staged draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-row-control-postconv-evidence-extraction-20260527222756266.md` identifies the conflict as a row-control derivative conversion conflict.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260527222756266.md` states that the original image controls and that physical row `172` is the Pulgar/Arriagada row.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md` transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, father field `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` instead gives entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. at `En esta`.
- Canonical context: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` exists as a stub with generated entry-172 birth facts and a probable mother link to `Juana Arriagada de Pulgar`.
- Canonical context: `wiki/people/juana-arriagada-de-pulgar.md` exists as a stub with a generated probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.
- Canonical context: `wiki/people/jose-del-carmen-pulgar.md` exists as a stub but does not contain a promoted entry-172 parent link in the reviewed snapshot read for this task.
- Canonical context: `wiki/people/dario-arturo-pulgar-smith.md` is family supplied and explicitly says similarly named Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records should be attached only after identity review.
- Canonical context: `wiki/people/dar-o-pulgar-arriagada.md` is a separate stub currently supported by a 2000 expropriation event naming `Darío Pulgar Arriagada`, not by this 1888 birth record.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

Hypothesis: The controlling physical row for entry `172` is the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`, with father field certified narrowly as `Jose del Carmen Pulgar` and mother field `Juana Arriagada de Pulgar`.

Evidence supporting:

- The staged draft explicitly reports image-reviewed row control for physical row `172`.
- The source packet says the original image controls and describes the converted Burgos/de la Cruz text as derivative conflict material.
- The assigned chunk transcribes a coherent row with entry number `172`, registration date 7 April 1888, child `Jose del Carmen Segundo Pulgar Arriagada`, birth date/time/place 8 March 1888 at 3 p.m. at `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- Existing canonical stubs already preserve this child and mother as probable/draft context, which is consistent with the Pulgar/Arriagada row but does not independently resolve the conversion conflict.

Conflicts and limits:

- The current converted Markdown assigns the same entry number to a completely different child and parent set.
- The father's possible final `S.` is not certified by the staged source packet and should not be promoted.
- This row supports a child-parent evidence candidate, not a same-person merge with any later Dario/Pulgar identity.

Scores:

| Measure | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.86 | Strong row-controlled support for the narrow child identity, capped by the unreconciled converted Markdown conflict. |
| conflict_severity | 0.92 | The derivative text changes child, parents, birth date/time/place, and row family identity. |
| evidence_quality | 0.84 | Civil birth register row plus staged image-reviewed packet; derivative conversion conflict remains. |
| conversion_confidence | 0.80 | High for row control after image-reviewed staging; lower for exact father suffix. |
| claim_probability | 0.88 | The narrow Pulgar/Arriagada row reading is more probable than the derivative Burgos/de la Cruz reading for this source identity. |
| relevance | 0.95 | Directly relevant to Pulgar-line parent-child evidence and anti-conflation. |
| canonical_readiness | 0.58 | Ready only for proof review, not direct canonical promotion, because the converted file conflict and father-field boundary must be preserved. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Birth Row

Hypothesis: Entry `172` in this source should be treated as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, as stated in the current converted Markdown.

Evidence supporting:

- The current converted Markdown contains a complete derivative transcription for entry `172` under this identity.

Conflicts and limits:

- The staged draft and source packet say the original image and assigned chunk control against this reading.
- The Burgos/de la Cruz details do not match the row-controlled page context: different child name, different parents, different birth date/time/place, and different apparent locality wording.
- No local evidence read for this task bridges Burgos/de la Cruz to Pulgar/Arriagada or indicates these are duplicate people.

Scores:

| Measure | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Supported only by the stale/conflicting derivative conversion. |
| conflict_severity | 0.92 | Directly conflicts with the row-controlled Pulgar/Arriagada identity. |
| evidence_quality | 0.22 | Single derivative text contradicted by image-reviewed staging. |
| conversion_confidence | 0.16 | Current conversion appears stale, row-shifted, or from another page/image set. |
| claim_probability | 0.12 | Low for this exact source identity and entry row. |
| relevance | 0.34 | Relevant mainly as a conversion-control warning, not Pulgar identity evidence. |
| canonical_readiness | 0.05 | Not ready; should not be promoted from this source packet. |

## Hypothesis 3: Father Is Jose del Carmen Pulgar, Not Yet A Resolved Canonical Merge

Hypothesis: The father field in the row-controlled entry names `Jose del Carmen Pulgar`, but this source alone does not prove whether he is identical with any other same-named or similarly named Pulgar father candidate.

Evidence supporting:

- The staged source packet certifies the father field only as `Jose del Carmen Pulgar`.
- The assigned chunk's longer `Jose del Carmen Pulgar S.` still contains the certified base name `Jose del Carmen Pulgar`.
- Existing canonical `wiki/people/jose-del-carmen-pulgar.md` exists, but the page snapshot read for this task does not itself resolve all same-name candidates or all parent-child links.

Conflicts and limits:

- The trailing `S.` or mark after `Pulgar` is unresolved and cannot be expanded.
- Other local staged/reviewed Pulgar material references `Jose del Carmen Pulgar` in other entries, but this task's source supports only the entry-172 father field and does not merge all same-named men.

Scores:

| Measure | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.76 | Good confidence for the literal father-name field; lower for canonical same-person linkage. |
| conflict_severity | 0.60 | The main risk is suffix/merge overreach rather than a competing father within the row-controlled reading. |
| evidence_quality | 0.78 | Direct birth-register parent field, with a stated boundary around the suffix. |
| conversion_confidence | 0.74 | Certified to `Jose del Carmen Pulgar`; not certified to `Jose del Carmen Pulgar S.` |
| claim_probability | 0.82 | High for the narrow field value, not for broader identity equivalence. |
| relevance | 0.90 | Directly relevant to parent-child staging and Pulgar-line grouping. |
| canonical_readiness | 0.50 | Needs proof review to decide whether to attach to the existing canonical stub and how to word the suffix caveat. |

## Hypothesis 4: Mother Is Juana Arriagada de Pulgar, Not Juana de Dios Amagada de Pulgar

Hypothesis: The mother field for row-controlled entry `172` names `Juana Arriagada de Pulgar`; this source does not support changing that reading to `Juana de Dios Amagada de Pulgar` or merging those candidates.

Evidence supporting:

- The staged draft and source packet both give `Juana Arriagada de Pulgar`.
- The assigned chunk transcribes the mother field as `Juana Arriagada de Pulgar`.
- Existing canonical `wiki/people/juana-arriagada-de-pulgar.md` preserves a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.

Conflicts and limits:

- Local Pulgar-line context includes a separate `wiki/people/juana-de-dios-amagada-de-pulgar.md` candidate, but this entry-172 staged draft does not name `Juana de Dios` or `Amagada`.
- Similarity between `Arriagada` and `Amagada` is a double-check cue only; it is not a basis for silent correction or merge.

Scores:

| Measure | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.82 | Strong for the literal mother field in entry 172. |
| conflict_severity | 0.46 | Main conflict is broader candidate conflation risk, not this row's mother reading. |
| evidence_quality | 0.80 | Direct civil-register parent field with staging support. |
| conversion_confidence | 0.78 | Image-reviewed staging and chunk agree on the mother name. |
| claim_probability | 0.86 | High for the narrow row-controlled mother field. |
| relevance | 0.92 | Directly relevant to the Pulgar/Arriagada child-parent claim. |
| canonical_readiness | 0.60 | Candidate is proof-reviewable, but should preserve probable status until accepted. |

## Hypothesis 5: Same Person As Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Hypothesis: `Jose del Carmen Segundo Pulgar Arriagada` or a parent in entry `172` is directly the same person as, or a proven ancestor/identity bridge for, `Dario Arturo Pulgar-Smith` or document-level `Dario Arturo Pulgar`.

Evidence supporting:

- Only broad Pulgar-line relevance exists: the row names Pulgar/Arriagada people, and canonical `Dario Arturo Pulgar-Smith` is a family-supplied Pulgar-Smith line person.
- Existing identity-analysis context in the workspace repeatedly treats `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith` as an unresolved bridge requiring proof review.

Conflicts and limits:

- Entry `172` does not name `Dario`, `Arturo`, `Smith`, a spouse, descendant, grandchild, later residence, profession as adult, or any bridge to the family-supplied Dario Arturo Pulgar-Smith page.
- Name overlap through `Pulgar` is insufficient for same-person, duplicate-person, or relationship promotion.
- `Dario Arturo Pulgar-Smith` remains a separate family-supplied canonical person; `Dario Arturo Pulgar` remains a document-level/CV-name cluster unless an identity-bearing local source bridges it.

Scores:

| Measure | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | No direct name or biographical bridge in entry 172. |
| conflict_severity | 0.70 | High risk if a later Dario identity is merged into an 1888 child/parent record by surname alone. |
| evidence_quality | 0.18 | Only indirect family-context relevance. |
| conversion_confidence | 0.80 | Row control is useful for Pulgar-line evidence, but not for Dario identity bridging. |
| claim_probability | 0.06 | Very low for any direct same-person conclusion. |
| relevance | 0.42 | Relevant as an anti-conflation checkpoint. |
| canonical_readiness | 0.00 | Not ready for any Dario Arturo or Pulgar-Smith attachment. |

## Hypothesis 6: Same Person As Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, Or Dario/Darío Pulgar Arriagada

Hypothesis: The entry-172 child or family row is the same identity cluster as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Darío Pulgar Arriagada`.

Evidence supporting:

- The row-controlled child surname form `Pulgar Arriagada` overlaps with later Pulgar-Arriagada name clusters.
- Existing canonical `wiki/people/dar-o-pulgar-arriagada.md` and reviewed staging show separate local evidence for a `Darío Pulgar Arriagada` name form in later records.

Conflicts and limits:

- Entry `172` names the child `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario`, `Dario Jose`, `Dario J.`, or `Darío`.
- Existing reviewed Pulgar-Arriagada/Dario directory and expropriation materials are later, separate clusters and do not provide a birth date, parents, or bridge to this 1888 child in the evidence read for this task.
- A possible Dario/Jose name-order issue in other staged entry-513 materials cannot be imported into this row-controlled entry 172 as correction evidence.

Scores:

| Measure | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | Surname overlap only; given names and source contexts differ. |
| conflict_severity | 0.78 | High conflation risk across Pulgar-Arriagada candidates. |
| evidence_quality | 0.24 | Useful for cluster awareness, not identity proof. |
| conversion_confidence | 0.80 | Entry-172 row control is strong but does not name Dario. |
| claim_probability | 0.10 | Low for same-person linkage. |
| relevance | 0.55 | Relevant for anti-conflation and future bridge review. |
| canonical_readiness | 0.00 | No same-person or relationship promotion from this entry. |

## Ranked Conclusions

| Rank | Hypothesis | Probability | Readiness |
| ---: | --- | ---: | --- |
| 1 | Physical row `172` is `Jose del Carmen Segundo Pulgar Arriagada`, child of father field `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`. | 0.88 | Promote only after proof review accepts row control and father-field boundary. |
| 2 | `Jose del Carmen Pulgar` is the literal father field but not yet a resolved merge with all same-named Pulgar candidates. | 0.82 | Proof-reviewable as a narrow field/relationship candidate. |
| 3 | `Juana Arriagada de Pulgar` is the literal mother field and distinct from unsupported `Juana de Dios Amagada de Pulgar` unless separately bridged. | 0.86 | Proof-reviewable as a narrow field/relationship candidate. |
| 4 | Converted Markdown Burgos/de la Cruz text represents this exact source row. | 0.12 | Hold as derivative conflict only. |
| 5 | Entry 172 bridges to `Dario Arturo Pulgar-Smith` or document-level `Dario Arturo Pulgar`. | 0.06 | Not ready; preserve as separate hypothesis. |
| 6 | Entry 172 bridges to `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Darío Pulgar Arriagada`. | 0.10 | Not ready; preserve as separate hypothesis. |

## Conflict Types

- Same-person conflict: no same-person merge is supported between the Pulgar/Arriagada child, Burgos/de la Cruz child, Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, or Dario/Darío Pulgar Arriagada clusters.
- Duplicate-person risk: moderate for existing Jose/Juana Pulgar-line stubs if parent-child links are promoted without proof-review wording; high for any Dario merge by surname alone.
- Name-variant conflict: `Jose del Carmen Pulgar S.` must not be normalized beyond certified `Jose del Carmen Pulgar`; `Juana Arriagada` must not be silently corrected to `Juana de Dios Amagada`.
- Relationship conflict: the source can support only candidate parents for the entry-172 child after proof review. It does not support Dario-line descendant/ancestor bridges.
- Chronology conflict: Burgos/de la Cruz derivative row gives birth on 6 April 1888, while the row-controlled Pulgar/Arriagada evidence gives birth on 8 March 1888. These should remain separate row hypotheses, not reconciled as one person.

## Recommended Next Action

Run proof review on the staged conflict draft and source packet for row-control acceptance. The exact proof-review decision needed next is:

1. Accept or reject that the original image and assigned chunk control entry `172` as the Pulgar/Arriagada physical row rather than the converted Burgos/de la Cruz derivative text.
2. If accepted, promote only narrow row-controlled claims for `Jose del Carmen Segundo Pulgar Arriagada`, birth date/time/place, mother `Juana Arriagada de Pulgar`, and father field `Jose del Carmen Pulgar`.
3. Preserve the father suffix as unresolved; do not promote `Jose del Carmen Pulgar S.` unless a targeted image reread certifies it.
4. Keep all Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, Dario/Darío Pulgar Arriagada, and Jose/Juana parent-candidate mergers on hold until a separate identity-bridge proof review supplies direct full-name/date/relationship evidence.
