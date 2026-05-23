---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/conflict-chunk-a4cd3c3e5c16-p0001-01-source-image-missing-qc-reread.md
worker: postconv-identity-analysis-20260523063533913
staged_draft: research/_staging/conflicts/conflict-chunk-a4cd3c3e5c16-p0001-01-source-image-missing-qc-reread.md
source_path: raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png
source_packet: research/_staging/source-packets/sp-chunk-a4cd3c3e5c16-p0001-01-andes-pulgar-passenger-list.md
converted_file: raw/converted/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953.codex.md
chunk: raw/chunks/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953-codex/page-0001-chunk-01.md
chunk_id: CHUNK-a4cd3c3e5c16-P0001-01
page_reference: image page 1; passenger list page P.M. 25
analysis_status: hold
canonical_readiness: hold
---

# Identity/Conflict Analysis: Child Dario Pulgar Address QA

## Blockers

- Exact staged draft reviewed: `research/_staging/conflicts/conflict-chunk-a4cd3c3e5c16-p0001-01-source-image-missing-qc-reread.md`.
- The conflict is a conversion-QA blocker for one field only: the child Dario Pulgar row's column 6 last-UK-address cell.
- The converted table renders a ditto mark in the child row address column, but the staged conflict and source packet say local image review does not clearly show that column 6 ditto mark.
- Do not promote `Bedford Corner Hotel, London.` as the child Dario row's last United Kingdom address until targeted page-image reread resolves column 6.
- The passenger list does not explicitly state parentage, spouse relationships, birth date, middle name, surname `Smith`, or a lineage bridge to any canonical Pulgar profile.
- The source contains two separate Dario Pulgar rows: an adult male aged 64 and a male child aged 11. They must not be merged by name.
- No external research was performed. No raw sources, converted Markdown, chunks, staged drafts outside this note, or canonical wiki pages were edited.

## Hypothesis 1: Child Dario Has A Held Address Ditto To Bedford Corner Hotel

Hypothesis: The child `Dario Pulgar` row repeats the adult Pulgar address `Bedford Corner Hotel, London.` by ditto mark.

Literal evidence:

- The converted table row for the child reads `" Dario`, age `11`, occupation `Student`, with a ditto mark rendered in column 6.
- The adult Dario row above gives `Bedford Corner Hotel, London.` in column 6.
- The Dorothy row between them also uses a ditto mark in column 6 in the converted table.

Interpretation:

- Row grouping makes the ditto plausible, but the source-packet reread and conflict draft both say the image is not clear enough for promotion.
- This is a conversion-confidence conflict, not a proved identity conflict.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.82 | The child row is a distinct `Dario Pulgar` entry; the field issue does not disturb the row identity. |
| conflict_severity | 0.46 | A wrong address would overstate residence evidence but would not by itself merge people. |
| evidence_quality | 0.58 | Table structure supports the reading, while image review weakens this one cell. |
| conversion_confidence | 0.38 | The specific address ditto is not visually clear enough. |
| claim_probability | 0.55 | Plausible but held. |
| relevance | 0.96 | This is the exact claim blocked by the staged draft. |
| canonical_readiness | 0.05 | Do not promote this address claim. |

## Hypothesis 2: Child Dario Is A Separate Passenger From Adult Dario

Hypothesis: The passenger list records two separate same-name passengers: `Dario Pulgar (adult passenger, age 64)` and `Dario Pulgar (child passenger, age 11)`.

Literal evidence:

- The converted Pulgar rows include `PULGAR Dario` with age `64` and occupation `Medical`.
- A later row reads `" Dario` with age `11` in the child male age column and occupation `Student`.
- The staged identity candidate `research/_staging/identity/id-chunk-a4cd3c3e5c16-p0001-01-two-dario-pulgar-entries.md` states that local image review confirms two separate Dario Pulgar entries.

Interpretation:

- This is the strongest identity conclusion from the page.
- The address-cell uncertainty does not erase the adult/child distinction.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.91 | Separate age columns and separate rows strongly distinguish the two entries. |
| conflict_severity | 0.72 | Merging the two Dario rows would create a serious chronology/person error. |
| evidence_quality | 0.78 | Converted table, source packet, and identity draft align on the distinction. |
| conversion_confidence | 0.74 | Main row identity fields are stronger than the address cell. |
| claim_probability | 0.92 | Very likely two different passengers. |
| relevance | 0.90 | Needed to prevent name-only conflation. |
| canonical_readiness | 0.70 | Ready as an anti-conflation note after proof review, not as a merge. |

## Hypothesis 3: Child Dario Is The Child Of Adult Dario And Dorothy Pulgar

Hypothesis: The child passenger aged 11 is the child of the adjacent adult passengers `Dario Pulgar (adult passenger, age 64)` and `Dorothy Pulgar`.

Literal evidence:

- The three Pulgar rows are consecutive.
- Dorothy and the younger Dario use surname ditto marks under the preceding Pulgar surname.
- Adult ages are entered in columns labelled for adults accompanied by husband or wife.

Interpretation:

- This is a family-context clue only. The table has no relationship-to-head, parent, spouse, or child column.
- The staged relationship drafts correctly mark the spouse and parent-child hypotheses as low confidence and `do_not_promote`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.50 | The grouping is suggestive but not relationship-proof. |
| conflict_severity | 0.55 | A promoted parent relationship without direct evidence would materially affect the tree. |
| evidence_quality | 0.44 | Evidence is structural and inferential. |
| conversion_confidence | 0.62 | Row grouping is readable, but relationship meaning is not stated. |
| claim_probability | 0.48 | Possible, not proven. |
| relevance | 0.82 | Relevant to interpreting the repeated name and address clue. |
| canonical_readiness | 0.03 | Do not promote as a family relationship. |

## Hypothesis 4: Child Dario Is Dario Arturo Pulgar Or Canonical Dario Arturo Pulgar-Smith

Hypothesis: The child passenger `Dario Pulgar`, aged 11 on 1953-08-07, is the same person as staged CV subject `Dario Arturo Pulgar` and possibly canonical `Dario Arturo Pulgar-Smith`.

Literal evidence:

- The child passenger stub records a Chilean `Dario Pulgar`, age 11, student, with last permanent residence England and intended future residence/citizenship Chile.
- Staged CV packets identify a document-level subject `Dario Arturo Pulgar`; CV page 9 records schooling at `Liceo Enrique Molina. Concepción, Chile` in 1954-1959.
- The canonical page `wiki/people/dario-arturo-pulgar-smith.md` names `Dario Arturo Pulgar-Smith` from family-supplied knowledge and warns against automatic merging with similarly named Pulgar records.

Interpretation:

- Chronology is compatible: a child aged 11 in August 1953 could plausibly be in secondary school in Chile from 1954.
- The passenger list does not provide `Arturo`, `Smith`, birth date, parents, or any direct bridge to the CV or canonical page.
- Family context justifies targeted comparison, not silent correction from `Dario Pulgar` to `Dario Arturo Pulgar-Smith`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.48 | Compatible age/name context but no direct identity bridge. |
| conflict_severity | 0.64 | Premature attachment would affect the canonical maternal-line profile. |
| evidence_quality | 0.52 | Evidence is circumstantial across staged clusters. |
| conversion_confidence | 0.66 | Main child row facts are usable; the address and CV-to-canonical bridge remain held. |
| claim_probability | 0.46 | Possible but not promotion-ready. |
| relevance | 0.88 | Required Pulgar-line comparison and likely future proof-review target. |
| canonical_readiness | 0.10 | Hold; no merge or canonical attachment. |

## Hypothesis 5: Adult Dario Is Dario Jose Pulgar-Arriagada / Dario J. Pulgar Arriagada / Dario Pulgar A.

Hypothesis: The adult passenger `Dario Pulgar`, age 64 and occupation `Medical`, is the same person as older Pulgar-Arriagada clusters such as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or 1928 passenger `Dario Pulgar A.`.

Literal evidence:

- The 1953 adult passenger row gives `PULGAR Dario`, age `64`, occupation `Medical`, citizenship and intended residence Chile.
- The 1928 staged identity candidate for `Dario Pulgar A.` gives age `39`, occupation `Medical Surgeon`, Chile residence/citizenship, and intended future residence France.
- A 1918 staged identity candidate names `Dario J. Pulgar Arriagada` under `Medicos-Cirujanos`.
- Staged Geneva photograph candidates use `Dario Jose Pulgar-Arriagada` from source title/file context, but the photograph pages do not provide independent visible text, birth data, parents, spouse, or residence.

Interpretation:

- The older medical/professional chronology is plausible for the 1953 adult passenger but remains unproved.
- This hypothesis is separate from the child-address QA issue and must not be used to infer the child row's address or parentage.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.56 | Age/profession chronology aligns with older medical clusters, but names are incomplete or metadata-driven. |
| conflict_severity | 0.68 | Wrong merger could collapse 1918/1928/1929/1953 clusters. |
| evidence_quality | 0.50 | Several supporting clusters are held for conversion QA or source-context review. |
| conversion_confidence | 0.48 | Older Pulgar-Arriagada materials have reread or missing-image caveats. |
| claim_probability | 0.52 | Plausible but not established. |
| relevance | 0.76 | Required anti-conflation comparison. |
| canonical_readiness | 0.08 | Hold pending anti-conflation proof review. |

## Hypothesis 6: Same As Darío Pulgar Arriagada In The 2000 Expropriation Notice

Hypothesis: One of the 1953 Dario Pulgar passengers is the same person as `Darío Pulgar Arriagada` named in a 2000 Serviu Región del Bío Bío expropriation resolution.

Literal evidence:

- The canonical stub `wiki/people/dar-o-pulgar-arriagada.md` records a 2000-12-05 expropriation-notice naming of `Darío Pulgar Arriagada`.
- The 1953 passenger list names `Dario Pulgar` but not `Arriagada`.

Interpretation:

- Name overlap alone is insufficient. The 2000 notice gives no age, occupation, family relationship, or travel context that bridges to either 1953 passenger row.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.18 | Only broad name overlap. |
| conflict_severity | 0.50 | A false link would attach property/legal evidence to an unproved passenger identity. |
| evidence_quality | 0.54 | The legal-notice claim is narrow; the identity bridge is weak. |
| conversion_confidence | 0.62 | No specific conflict with this passenger page, but no bridge. |
| claim_probability | 0.16 | Low from current evidence. |
| relevance | 0.62 | Required Pulgar-line comparison. |
| canonical_readiness | 0.02 | Do not merge or attach. |

## Hypothesis 7: Jose/Juana Parent Candidates Connect This Passenger Group To A Lineage

Hypothesis: Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, or Juana de Dios Amagada de Pulgar may connect to the broader Pulgar line that includes the 1953 passenger rows.

Literal evidence:

- Existing wiki context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- The assigned passenger-list conflict draft does not name Jose or Juana and contains no parent, child, grandparent, or ancestor statement.
- Existing Jose/Juana register work has separate conversion and identity caveats, including unresolved surname and parent-link readings.

Interpretation:

- These are future lineage-check candidates only. They do not resolve the child Dario address cell and do not prove any relationship to the 1953 passengers.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.05 | No direct connection in the assigned source. |
| conflict_severity | 0.58 | Premature lineage attachment would create false family structure. |
| evidence_quality | 0.38 | Related register clusters remain image-sensitive. |
| conversion_confidence | 0.36 | Jose/Juana readings have separate QA conflicts. |
| claim_probability | 0.05 | Not supported by this draft. |
| relevance | 0.55 | Required parent-candidate comparison only. |
| canonical_readiness | 0.01 | No canonical action. |

## Conflicts

- Conversion-confidence conflict: converted child row shows an address ditto mark, but local image review does not clearly support that mark.
- Same-person conflict: none directly caused by the address cell. The page itself distinguishes adult and child Dario rows.
- Duplicate-person risk: high if adult and child `Dario Pulgar` rows are merged by name; moderate if the child row is attached to `Dario Arturo Pulgar` or `Dario Arturo Pulgar-Smith` before an identity bridge is proof-reviewed.
- Name-variant conflict: this page supports only `PULGAR Dario` and ditto-surname `" Dario`; it does not prove `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Darío Pulgar Arriagada`.
- Relationship-conflict evidence: the passenger list has no relationship column. Spouse and parent-child readings are possible clues only.
- Chronology-conflict evidence: the adult age 64 in 1953 is incompatible with being the child aged 11. The child age is chronologically compatible with, but does not prove, the staged CV education chronology.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | Adult and child Dario Pulgar are separate passengers | 0.92 | Promote only as anti-conflation after proof review. |
| 2 | Child address ditto to `Bedford Corner Hotel, London.` | 0.55 | Hold for targeted reread of column 6. |
| 3 | Adult Dario same as older medical/Pulgar-Arriagada cluster | 0.52 | Run anti-conflation proof review across 1918, 1928, 1929, and 1953 records. |
| 4 | Child Dario same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.46 | Compare with verified CV title/education evidence and a direct identity bridge. |
| 5 | Child Dario is child of adult Dario and Dorothy | 0.48 | Treat as research clue; require a source with explicit parentage. |
| 6 | Same as 2000 `Darío Pulgar Arriagada` | 0.16 | Preserve as separate unless a direct bridge appears. |
| 7 | Jose/Juana parent candidates connect the 1953 passengers to a lineage | 0.05 | No action from this passenger-list conflict. |

## Recommended Next Action

Keep `research/_staging/conflicts/conflict-chunk-a4cd3c3e5c16-p0001-01-source-image-missing-qc-reread.md` on hold for conversion QA of the child Dario row's column 6 address cell. The exact next proof-review step is a targeted page-image reread of column 6 for the child row only, followed by a narrow proof review deciding whether the child address claim can say `Bedford Corner Hotel, London.` by ditto mark.

Do not merge people, rename canonical pages, attach the child row to `Dario Arturo Pulgar-Smith`, infer parentage from row order, or promote the child last-UK-address claim. Separately, maintain an anti-conflation checklist comparing `Dario Arturo Pulgar-Smith`, staged CV `Dario Arturo Pulgar`, child passenger `Dario Pulgar` age 11, adult passenger `Dario Pulgar` age 64, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar A.`, `Darío Pulgar Arriagada`, and Jose/Juana parent candidates before any Pulgar-line canonical attachment.
