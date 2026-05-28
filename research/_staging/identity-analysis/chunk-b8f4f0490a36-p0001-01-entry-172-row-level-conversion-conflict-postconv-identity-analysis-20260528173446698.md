---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260528173446698
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260528165422297.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260528165422297.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528165422297.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528165422297.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_proof_review
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. The current converted Markdown and the image-reviewed row-control evidence disagree on entry `172`. The converted Markdown names `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; the image-reviewed row-control note and assigned chunk identify physical row `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
2. The father field is only certified here as `Jose del Carmen Pulgar`. The assigned chunk includes `Jose del Carmen Pulgar S.`, but the conversion review note explicitly withholds promotion of the trailing `S.`.
3. The row does not name Dario, Arturo, Smith, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. Any Dario-line attachment would be a relationship jump and is not ready.
4. Existing canonical pages are stubs or family-supplied pages with generated evidence snapshots. They can guide comparison, but this staged note must not merge people, rename pages, or promote facts.
5. The Burgos/de la Cruz text is a derivative transcript conflict, not a name variant or alternate identity for the Pulgar/Arriagada child.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260528165422297.md`.
- Source packet: `research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528165422297.md`.
- Conversion review note: `research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528165422297.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Conflicting converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing canonical wiki pages checked: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/tulio-cesar-luis-jose.md`, `wiki/people/dario-arturo-pulgar-smith.md`, and `wiki/people/dar-o-pulgar-arriagada.md`.

## Literal Source Readings Kept Separate

Image-reviewed row-control evidence says physical entry `172` on register page 58 records:

- Registration date: 7 April 1888.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: male.
- Birth: 8 March 1888, 3 p.m., `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar`.
- Mother: `Juana Arriagada de Pulgar`.
- Parents' residence: `Calle de Colipi`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employee, resident at `Calle de Valdivia`.

The assigned chunk agrees in substance but reads the father as `Jose del Carmen Pulgar S.`. That terminal suffix is not certified by the image-reviewed QA note.

The current converted Markdown reads entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth 6 April 1888 at `En esta`. This is preserved only as a derivative conversion conflict.

## Hypotheses And Evidence

### H1: Physical Row 172 Is A Pulgar/Arriagada Birth Registration

Evidence supporting:

- The source packet and conversion review note both identify physical row `172` as the Pulgar/Arriagada birth registration.
- The assigned chunk table names `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar S.`, and `Juana Arriagada de Pulgar` in row `172`.
- The row-control review explicitly states the Burgos/de la Cruz reading is not the row controlled by the image.

Conflicts:

- The converted Markdown has a materially different entry `172`.
- Father suffix handling remains unresolved.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity confidence | 0.90 | High for row-level identity of the child in the image-reviewed physical row. |
| conflict severity | 0.92 | Different child, parents, dates, and place appear in the derivative conversion. |
| evidence quality | 0.86 | Image-reviewed row-control note plus assigned chunk are stronger than derivative converted Markdown. |
| conversion confidence | 0.84 | High for row control; reduced by father suffix uncertainty and conflicting converted file. |
| claim probability | 0.90 | The Pulgar/Arriagada reading is the best-supported row-level claim. |
| relevance | 0.88 | Directly relevant to Pulgar/Arriagada parent-child evidence. |
| canonical readiness | 0.58 | Ready only for proof-review consideration, not direct promotion from this worker. |

### H2: The Burgos/de la Cruz Entry Is A Duplicate Or Variant Of The Pulgar/Arriagada Entry

Evidence supporting:

- None beyond both being labeled entry `172` in different derivative layers.

Conflicts:

- Names, parents, birth date, birth place wording, and row context all differ.
- The conflict draft and row-control review explicitly instruct that Burgos/de la Cruz not be merged into Pulgar/Arriagada evidence.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity confidence | 0.04 | Shared entry number in a conflicted derivative layer is not identity evidence. |
| conflict severity | 0.94 | Treating this as a variant would conflate two materially different records. |
| evidence quality | 0.20 | The Burgos/de la Cruz support is from the challenged converted Markdown. |
| conversion confidence | 0.18 | Current conversion is contradicted by row-control QA. |
| claim probability | 0.03 | Variant/duplicate hypothesis is not supported. |
| relevance | 0.60 | Relevant as a conversion conflict only. |
| canonical readiness | 0.00 | Not ready; preserve as conflict, not identity evidence. |

### H3: Father Candidate Is Existing Canonical `Jose del Carmen Pulgar`

Evidence supporting:

- Entry `172` image-reviewed row-control evidence names father `Jose del Carmen Pulgar`.
- Existing wiki page `wiki/people/jose-del-carmen-pulgar.md` has a stub for the same preferred name and a generated draft child link to `Tulio Cesar Luis Jose` from separate staged evidence.
- Other staged Pulgar work has treated `Jose del Carmen Pulgar` as a recurring father/declarant lead, but name recurrence alone is not a same-person proof.

Conflicts and limitations:

- This row does not state age, birth year, spouse marriage, parents, or other identifiers for the father beyond occupation/residence/nationality.
- The canonical page's existing generated relationship to `Tulio Cesar Luis Jose` comes from separate conflicted staged evidence and does not prove the same man.
- The `S.` suffix in the assigned chunk cannot be promoted here.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity confidence | 0.52 | Same name and father role are meaningful but insufficient for a same-person merge. |
| conflict severity | 0.55 | Risk is moderate if the row is attached to the existing stub without bridge evidence. |
| evidence quality | 0.70 | Father name is image-reviewed, but identity bridge evidence is thin. |
| conversion confidence | 0.78 | Father base name is certified; suffix is not. |
| claim probability | 0.57 | Probable father-name lead, not a proved canonical same-person match. |
| relevance | 0.86 | Direct Pulgar parent candidate. |
| canonical readiness | 0.35 | Hold pending proof-reviewed parent/identity comparison. |

### H4: Mother Candidate Is Existing Canonical `Juana Arriagada de Pulgar`

Evidence supporting:

- Entry `172` image-reviewed row-control evidence names mother `Juana Arriagada de Pulgar`.
- Existing wiki page `wiki/people/juana-arriagada-de-pulgar.md` has the same preferred name and generated evidence linking her as probable mother of `Jose del Carmen Segundo Pulgar Arriagada`.

Conflicts and limitations:

- The row does not provide age, birth year, parents, or marriage details for Juana.
- The name form `de Pulgar` is consistent with a married-style reference but is not enough to merge with other Juana variants.
- Separate local canonical/staged context includes `Juana de Dios Amagada de Pulgar` linked to a different conflicted child row; this row alone must not merge those Juana candidates.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity confidence | 0.66 | Stronger than the father-stub bridge because the existing stub already reflects this row's exact mother name. |
| conflict severity | 0.45 | Main risk is over-merging with other Juana/Arriagada/Amagada variants. |
| evidence quality | 0.76 | Mother name and attributes are row-controlled, but identity bridge remains narrow. |
| conversion confidence | 0.84 | No specific mother-name uncertainty was flagged in the review note. |
| claim probability | 0.72 | Good staged mother candidate for this child after proof review. |
| relevance | 0.90 | Direct parent evidence. |
| canonical readiness | 0.50 | Likely promotable only after proof review accepts row control and relationship scope. |

### H5: Child `Jose del Carmen Segundo Pulgar Arriagada` Is Same Person As `Dario Arturo Pulgar-Smith`

Evidence supporting:

- Both are Pulgar-line names in local context.
- Family context makes Dario/Pulgar records worth checking against the maternal line.

Conflicts and limitations:

- Entry `172` names `Jose del Carmen Segundo`, not Dario or Arturo.
- Canonical `Dario Arturo Pulgar-Smith` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic merging with similarly named Dario/Pulgar clusters.
- No Smith surname, grandchild, spouse, child, occupation, adult chronology, or intermediate bridge appears in entry `172`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity confidence | 0.02 | No direct identity bridge. |
| conflict severity | 0.80 | A merge would create a high-risk identity conflation. |
| evidence quality | 0.12 | Only broad family-name context exists. |
| conversion confidence | 0.84 | Row reading is good, but it does not support this identity bridge. |
| claim probability | 0.02 | Not supported by this staged draft. |
| relevance | 0.42 | Relevant only as an anti-conflation comparison. |
| canonical readiness | 0.00 | Do not attach to Dario Arturo Pulgar-Smith from this row. |

### H6: `Dario Arturo Pulgar` Is A Short-Name Variant Of `Dario Arturo Pulgar-Smith`

Evidence supporting:

- Local staged CV contexts identify a document-level subject `Dario Arturo Pulgar`.
- Canonical `Dario Arturo Pulgar-Smith` shares the leading name string.

Conflicts and limitations:

- Entry `172` does not name `Dario Arturo Pulgar`.
- Existing staged CV analyses and proof-review notes require a separate identity-bridge review before linking `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`.
- This birth row provides no new evidence on the Pulgar versus Pulgar-Smith surname question.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity confidence | 0.00 | This row contributes no direct evidence for the CV/canonical bridge. |
| conflict severity | 0.55 | Moderate broader Dario-line duplicate risk, but not caused by this row. |
| evidence quality | 0.05 | Out-of-scope context only. |
| conversion confidence | 0.84 | Row-controlled evidence is reliable but irrelevant to this hypothesis. |
| claim probability | 0.00 | No support from entry `172`. |
| relevance | 0.25 | Mentioned to satisfy Pulgar-line anti-conflation review. |
| canonical readiness | 0.00 | Requires separate CV identity-bridge proof review. |

### H7: Child `Jose del Carmen Segundo Pulgar Arriagada` Is Same Person As `Dario Jose Pulgar-Arriagada`

Evidence supporting:

- Both names include Pulgar-Arriagada components.
- Local staged photograph/Geneva contexts preserve `Dario Jose Pulgar-Arriagada` as a separate unresolved cluster.

Conflicts and limitations:

- Entry `172` does not name Dario Jose.
- The shared `Jose` element is not enough: the entry's given-name string is `Jose del Carmen Segundo`.
- No date, age, occupation, residence, parent, spouse, child, or source-provenance bridge connects the 1888 child to the Dario Jose cluster.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity confidence | 0.04 | Shared surname pattern and one given-name element are weak. |
| conflict severity | 0.78 | A merge by name pattern would be high-risk. |
| evidence quality | 0.18 | This row supplies no Dario evidence. |
| conversion confidence | 0.84 | Row reading is good but does not bridge identities. |
| claim probability | 0.04 | Preserve as unresolved or separate. |
| relevance | 0.48 | Relevant as an explicit anti-merge comparison. |
| canonical readiness | 0.00 | Not ready. |

### H8: Child `Jose del Carmen Segundo Pulgar Arriagada` Is Same Person As `Dario/Dario Pulgar Arriagada`

Evidence supporting:

- Both carry Pulgar/Arriagada name elements.
- Existing wiki page `wiki/people/dar-o-pulgar-arriagada.md` records a `Dario Pulgar Arriagada` expropriation event dated 5 December 2000.

Conflicts and limitations:

- Entry `172` does not name Dario.
- The 2000 expropriation event is 112 years after the 1888 birth. It is chronologically possible only for an extremely elderly person and has no supporting age, residence, parentage, property-chain, or family bridge in this row.
- Other staged materials preserve Dario/Dario Pulgar Arriagada variants separately or unresolved.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity confidence | 0.03 | Shared surnames only. |
| conflict severity | 0.82 | Chronology and name-form risks are high for an unsupported merge. |
| evidence quality | 0.16 | No direct bridge. |
| conversion confidence | 0.84 | Reliable row reading does not support this merge. |
| claim probability | 0.03 | Not supported. |
| relevance | 0.50 | Relevant to Pulgar-line conflict control. |
| canonical readiness | 0.00 | Not ready. |

## Conflict Summary

- Same-person conflict: unresolved only for whether source-named `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` should attach to existing canonical stubs. Entry `172` does not support any Dario same-person conclusion.
- Duplicate-person conflict: high risk if Burgos/de la Cruz is treated as a duplicate/variant of Pulgar/Arriagada; high risk if the 1888 child is merged into Dario-line clusters by surname.
- Name-variant conflict: `Jose del Carmen Pulgar S.` must remain separate from promoted `Jose del Carmen Pulgar` until proof review certifies the suffix. `Juana Arriagada de Pulgar` must not be silently normalized to other Juana/Amagada/Arriagada candidates.
- Relationship conflict: the source-controlled row supports staged parent candidates for Jose/Juana, but relationship promotion must wait for proof review because the converted Markdown row is materially wrong.
- Chronology conflict: no direct chronology conflict within the 1888 row; chronology risk becomes high only if attached to later Dario/Dario Pulgar Arriagada clusters without bridge evidence.

## Ranked Conclusions

| Rank | Conclusion | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Physical row `172` is the Pulgar/Arriagada birth registration, not the Burgos/de la Cruz derivative entry. | 0.90 | Proof review should accept or reject the row-control QA and decide how to preserve/supersede the conflicting converted Markdown. |
| 2 | The child in row `172` is source-named `Jose del Carmen Segundo Pulgar Arriagada`. | 0.90 | Promote only after proof review accepts row control. |
| 3 | The mother is source-named `Juana Arriagada de Pulgar` and is a strong staged parent candidate for this child. | 0.72 | Proof-review the child-mother relationship and compare against other Juana variants before promotion. |
| 4 | The father is source-named `Jose del Carmen Pulgar`, with any trailing `S.` held. | 0.57 | Proof-review the father field and decide whether `S.` is rejected, uncertain, or separately certified. |
| 5 | Existing canonical `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` stubs are the same people named in this row. | 0.52 / 0.66 | Run a scoped parent-candidate identity review using accepted local rows, residences, occupations, spouse/child links, and any reviewed notes. |
| 6 | Any attachment to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. | 0.00-0.04 | Open a separate Dario-line identity-bridge proof review using direct identifiers, not this row alone. |

## Recommended Next Action

Hold this staged identity analysis for proof review. The exact next proof-review step is to accept the targeted row-control QA for entry `172`, preserve the Burgos/de la Cruz text as a derivative conversion conflict, and certify the father field as `Jose del Carmen Pulgar` with the `S.` suffix unresolved unless independently readable.

If proof review accepts the row-control QA, promote only narrow row-level claims for `Jose del Carmen Segundo Pulgar Arriagada` and staged parent candidates `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada` without a separate identity-bridge review that supplies dates, parentage, spouse/children, occupation, residence, or source-provenance continuity.
