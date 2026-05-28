---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260528173704312
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260528170150642.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260528170150642.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528170150642.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528170150642.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
canonical_readiness: hold_for_proof_review
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. The exact staged draft under review reports a material row-level conversion conflict: the current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the image-reviewed row-control packet identifies physical row `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
2. The father field is bounded. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the targeted conversion review certifies only `Jose del Carmen Pulgar`; the trailing `S.` or mark is not ready for promotion.
3. The row does not name Dario, Arturo, Smith, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. Any Dario-line connection is only a future identity-bridge question.
4. Existing canonical pages already contain some generated Pulgar/Arriagada evidence snapshots, but this worker must not merge people, rename pages, promote facts, or edit canonical pages.
5. `Burgos/de la Cruz` must be preserved as a derivative transcript conflict, not treated as a duplicate person, name variant, or alternate family reading for the Pulgar/Arriagada row.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260528170150642.md`.
- Source packet: `research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528170150642.md`.
- Conversion review note: `research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528170150642.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Conflicting converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing canonical wiki pages checked: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/juana-de-dios-amagada-de-pulgar.md`, and `wiki/people/tulio-cesar-luis-jose.md`.

## Literal Source Readings

The image-reviewed row-control packet and conversion review identify physical entry `172` on register page 58 as:

- Registration date: 7 April 1888.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: male.
- Birth: 8 March 1888, about 3 p.m., at `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar`.
- Mother: `Juana Arriagada de Pulgar`.
- Parents' residence: `Calle de Colipi`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employee, resident at `Calle de Valdivia`.

The assigned chunk agrees in substance but transcribes the father field as `Jose del Carmen Pulgar S.`. Interpretation: only the base father name is certified here.

The current converted Markdown instead reads entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at about 10 p.m. in `En esta`. Interpretation: this is a derivative conversion conflict, not a source-controlled identity variant.

## Hypotheses

### H1: Physical Row 172 Is The Pulgar/Arriagada Birth Registration

Evidence supporting:

- The staged draft, source packet, and targeted conversion review all identify physical row `172` as the Pulgar/Arriagada birth row.
- The assigned chunk table gives entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, with father field `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The row-control review explicitly states that the Burgos/de la Cruz text is not the image-controlled row.

Conflicts:

- The current converted Markdown gives a different entry `172`.
- Father suffix handling remains unresolved.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.90 | High for source-row identity after image-reviewed row-control QA. |
| conflict_severity | 0.92 | The derivative conversion changes child, parents, date, and place. |
| evidence_quality | 0.86 | Image-reviewed QA plus assigned chunk outweigh the conflicting derivative conversion. |
| conversion_confidence | 0.84 | Row control is strong; father suffix remains bounded. |
| claim_probability | 0.90 | Best-supported conclusion for the physical row. |
| relevance | 0.95 | Directly answers this staged conflict draft. |
| canonical_readiness | 0.58 | Ready for proof review, not worker promotion. |

### H2: Burgos/de la Cruz Is A Duplicate Or Name Variant Of Pulgar/Arriagada

Evidence supporting:

- The only overlap is that both derivative layers label material as entry `172`.

Conflicts:

- The names, parent set, date, place, and informant/declarant context differ.
- The staged draft and conversion review both instruct that Burgos/de la Cruz not be merged into Pulgar/Arriagada evidence.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | Shared entry number in a conflicted derivative layer is not identity proof. |
| conflict_severity | 0.95 | Treating this as a variant would conflate two materially different records. |
| evidence_quality | 0.18 | Burgos/de la Cruz support comes from the challenged converted Markdown. |
| conversion_confidence | 0.18 | Current conversion is contradicted by row-control QA. |
| claim_probability | 0.03 | Duplicate/variant hypothesis is unsupported. |
| relevance | 0.70 | Relevant as a conversion conflict only. |
| canonical_readiness | 0.00 | Not ready; preserve as derivative conflict. |

### H3: Father Candidate Is `Jose del Carmen Pulgar`

Evidence supporting:

- The row-control review certifies the father field as `Jose del Carmen Pulgar`.
- Existing canonical `wiki/people/jose-del-carmen-pulgar.md` has the same preferred name and a generated draft child link to `Tulio Cesar Luis Jose` from separate staged evidence.
- The 1888 row gives useful local identifiers for the father field: Chilean, employee, resident at `Calle de Colipi`.

Conflicts and limits:

- The 1888 row does not give the father's age, birth date, parents, spouse marriage, or signature.
- The existing canonical page's `Tulio Cesar Luis Jose` link is from a separate draft source and does not prove that all `Jose del Carmen Pulgar` mentions are one man.
- `Jose del Carmen Pulgar S.` must not be promoted from this extraction.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.52 | Certified name field, but no resolved same-person bridge to all same-named candidates. |
| conflict_severity | 0.55 | Moderate risk if attached to a canonical stub without bridge review. |
| evidence_quality | 0.70 | Father base name is image-reviewed; identity depth is limited. |
| conversion_confidence | 0.78 | Base name certified; suffix not certified. |
| claim_probability | 0.57 | Good father-name lead, not a proved merge. |
| relevance | 0.88 | Direct Pulgar parent candidate. |
| canonical_readiness | 0.35 | Hold pending parent-candidate proof review. |

### H4: Mother Candidate Is `Juana Arriagada de Pulgar`

Evidence supporting:

- The row-control review and assigned chunk both name the mother as `Juana Arriagada de Pulgar`.
- Existing canonical `wiki/people/juana-arriagada-de-pulgar.md` has the same preferred name and an evidence snapshot tying her as probable mother of `Jose del Carmen Segundo Pulgar Arriagada`.
- No uncertainty was flagged for this mother-name reading in the 20260528170150642 review note.

Conflicts and limits:

- The row does not give age, birth date, parents, marriage record, or independent identity markers.
- A separate canonical/staged candidate, `Juana de Dios Amagada de Pulgar`, is linked to `Tulio Cesar Luis Jose`; entry `172` does not justify silently correcting `Arriagada` to `Amagada` or merging those women.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.66 | Exact source name and existing matching stub, but limited independent identity detail. |
| conflict_severity | 0.45 | Main risk is over-merging with other Juana variants. |
| evidence_quality | 0.76 | Row-controlled mother name and attributes are strong for a narrow claim. |
| conversion_confidence | 0.84 | No row-control uncertainty specific to the mother field. |
| claim_probability | 0.72 | Strong staged mother candidate after proof review. |
| relevance | 0.92 | Direct parent evidence. |
| canonical_readiness | 0.50 | Potentially promotable only after proof review accepts row control and relationship scope. |

### H5: `Juana Arriagada de Pulgar` Is Same Person As `Juana de Dios Amagada de Pulgar`

Evidence supporting:

- Both women appear in Pulgar-line parent contexts.
- Both are associated locally with a `Jose del Carmen Pulgar` father/husband-context candidate.

Conflicts and limits:

- Entry `172` reads `Juana Arriagada de Pulgar`; the separate Tulio context reads `Juana de Dios Amagada de Pulgar`.
- The names differ in given-name expansion and surname reading.
- No shared age, residence continuity, spouse proof, child set proof, or source-reviewed bridge is present in this staged draft.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.24 | Possible family-line lead only. |
| conflict_severity | 0.62 | Meaningful risk of merging distinct Juana candidates by context. |
| evidence_quality | 0.42 | Uses separate staged/canonical context, not direct evidence from entry `172`. |
| conversion_confidence | 0.55 | Mixed because the comparison depends on separate conversion-sensitive materials. |
| claim_probability | 0.20 | Not proven; preserve as separate hypothesis. |
| relevance | 0.72 | Required Jose/Juana parent-candidate comparison. |
| canonical_readiness | 0.05 | Not ready for merge or name normalization. |

### H6: Entry 172 Bridges To `Dario Arturo Pulgar-Smith`

Evidence supporting:

- `Dario Arturo Pulgar-Smith` is a canonical family-supplied maternal-line person.
- The entry is a Pulgar-line record, so it is relevant as a lead to double-check later.

Conflicts and limits:

- Entry `172` does not name Dario, Arturo, Smith, Alexander John Heinz, a spouse, a child, or a later-life identifier.
- The canonical Dario page explicitly warns against automatic merging with similarly named Dario/Pulgar/Pulgar-Arriagada records.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.02 | No direct identity bridge. |
| conflict_severity | 0.80 | High conflation risk if attached by surname context. |
| evidence_quality | 0.12 | Family-context hint only. |
| conversion_confidence | 0.84 | Row is readable, but irrelevant to this bridge. |
| claim_probability | 0.02 | Not supported by this draft. |
| relevance | 0.45 | Relevant as an anti-conflation check. |
| canonical_readiness | 0.00 | Do not attach to Pulgar-Smith from this row. |

### H7: Entry 172 Bridges To `Dario Arturo Pulgar`

Evidence supporting:

- Local staged CV contexts preserve a document-level `Dario Arturo Pulgar` identity cluster.
- The surname `Pulgar` overlaps.

Conflicts and limits:

- Entry `172` names `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Arturo Pulgar`.
- This row offers no CV, occupation-continuity, date, residence, family relationship, or source-provenance bridge to `Dario Arturo Pulgar`.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.01 | Surname-only overlap. |
| conflict_severity | 0.65 | Moderate-to-high duplicate risk if used as a bridge. |
| evidence_quality | 0.08 | No direct evidence. |
| conversion_confidence | 0.84 | Row-control quality does not help this hypothesis. |
| claim_probability | 0.01 | Unsupported here. |
| relevance | 0.35 | Anti-conflation only. |
| canonical_readiness | 0.00 | Requires separate CV identity-bridge proof review. |

### H8: Entry 172 Bridges To `Dario Jose Pulgar-Arriagada`

Evidence supporting:

- Both names include Pulgar/Arriagada elements, and `Jose` appears in the entry-172 child's given-name string.
- Local staged ICRC materials preserve `Dario Jose Pulgar-Arriagada` as a separate unresolved cluster.

Conflicts and limits:

- Entry `172` names `Jose del Carmen Segundo`, not `Dario Jose`.
- The staged ICRC identity is title/file-context dependent in local materials and is not visible text in this birth row.
- No age, occupation, family bridge, residence bridge, or source-chain bridge connects the 1888 child to the Dario Jose candidate.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.04 | Shared surname pattern and one given-name element are weak. |
| conflict_severity | 0.78 | High risk if merged by name elements alone. |
| evidence_quality | 0.18 | No direct Dario evidence in this row. |
| conversion_confidence | 0.84 | Row-control quality does not create an identity bridge. |
| claim_probability | 0.04 | Preserve separately or unresolved. |
| relevance | 0.55 | Required Pulgar-line comparison. |
| canonical_readiness | 0.00 | Not ready. |

### H9: Entry 172 Bridges To `Dario/Dario Pulgar Arriagada`

Evidence supporting:

- Both use Pulgar/Arriagada surname elements.
- Existing canonical `wiki/people/dar-o-pulgar-arriagada.md` preserves a `Darío Pulgar Arriagada` expropriation-event cluster dated 2000-12-05.

Conflicts and limits:

- Entry `172` does not name Dario/Darío.
- A direct same-person merge between an 1888 birth and a 2000 event would require strong vital-date or continuity evidence; this staged draft supplies none.
- Existing Pulgar-Arriagada legal-notice and Dario-line analyses keep these clusters separate pending bridge proof.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | Shared surnames only. |
| conflict_severity | 0.82 | Chronology and name-form risks are high without bridge evidence. |
| evidence_quality | 0.16 | No direct bridge. |
| conversion_confidence | 0.84 | Reliable row reading does not support this merge. |
| claim_probability | 0.03 | Not supported. |
| relevance | 0.55 | Required anti-conflation comparison. |
| canonical_readiness | 0.00 | Not ready. |

## Conflict Summary

- Same-person conflict: unresolved only for narrow attachment of source-named `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` to existing canonical stubs. Entry `172` does not resolve any Dario same-person question.
- Duplicate-person conflict: severe if Burgos/de la Cruz is treated as a duplicate or variant of Pulgar/Arriagada; severe if the 1888 child is merged into Dario-line clusters by surname.
- Name-variant conflict: `Jose del Carmen Pulgar S.` must remain separate from certified `Jose del Carmen Pulgar` until proof review certifies the terminal mark. `Juana Arriagada de Pulgar` must not be silently normalized to `Juana de Dios Amagada de Pulgar`.
- Relationship conflict: the row supports staged parent candidates for `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, but relationship promotion must wait for proof review because the converted Markdown row is materially inconsistent.
- Chronology conflict: no internal chronology conflict in the 1888 row; chronology risk becomes high only if attached to later Dario/Darío Pulgar Arriagada or Dario Arturo clusters without direct bridge evidence.

## Ranked Conclusions

| Rank | Conclusion | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Physical row `172` is the Pulgar/Arriagada birth registration, not the Burgos/de la Cruz derivative entry. | 0.90 | Proof review should accept or reject the targeted row-control QA and preserve the derivative conflict. |
| 2 | The child in row `172` is source-named `Jose del Carmen Segundo Pulgar Arriagada`. | 0.90 | Promote only after proof review accepts row control. |
| 3 | The mother is source-named `Juana Arriagada de Pulgar`. | 0.72 | Proof-review the child-mother relationship and compare against Juana variants before promotion. |
| 4 | The father is source-named `Jose del Carmen Pulgar`, with any trailing `S.` held. | 0.57 | Proof-review the father field and decide whether the terminal mark is rejected, uncertain, or certified. |
| 5 | Existing canonical `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` stubs are the same people named in this row. | 0.52 / 0.66 | Run a scoped parent-candidate identity review using accepted local rows, residences, occupations, spouse/child links, and reviewed notes. |
| 6 | `Juana Arriagada de Pulgar` is the same person as `Juana de Dios Amagada de Pulgar`. | 0.20 | Hold for a separate Jose/Juana parent-candidate bridge review. |
| 7 | Any attachment to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. | 0.01-0.04 | Open a separate Dario-line identity-bridge proof review using direct identifiers, not this row alone. |

## Recommended Next Action

Hold this staged identity analysis for proof review. The exact next proof-review step is to accept the targeted row-control QA for entry `172`, preserve the Burgos/de la Cruz text as a derivative conversion conflict, and certify the father field only as `Jose del Carmen Pulgar` unless a targeted image reread certifies the trailing mark.

If proof review accepts row control, promote only narrow row-level claims for `Jose del Carmen Segundo Pulgar Arriagada` and staged parent candidates `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada` without a separate identity-bridge review that supplies direct name, date, relationship, occupation, residence, or source-provenance continuity.
