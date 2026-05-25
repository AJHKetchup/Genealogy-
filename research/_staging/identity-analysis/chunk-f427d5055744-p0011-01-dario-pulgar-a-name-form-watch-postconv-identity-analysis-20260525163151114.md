---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525163151114
task_id: "identity-analysis:research/_staging/conflicts/chunk-f427d5055744-p0011-01-dario-pulgar-a-name-form-watch.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-f427d5055744-p0011-01-dario-pulgar-a-name-form-watch.md"
source_packet: "research/_staging/source-packets/chunk-f427d5055744-p0011-01-el-aguila-fundo-los-cuartos-dario-pulgar-a.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0011-chunk-01.md"
chunk_id: "CHUNK-f427d5055744-P0011-01"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity/Conflict Analysis: Dr. Dario Pulgar A. Name Form Watch

## Blockers First

1. The assigned staged draft is `research/_staging/conflicts/chunk-f427d5055744-p0011-01-dario-pulgar-a-name-form-watch.md`. It is a name-form and conversion-QA watch, not a proved canonical identity conflict.
2. The same El Aguila page has two converted name forms: typed article `DR DARIO PULGAR A` and footer signature `[signature] DR. DARIO PULGARA [/signature]`. A page-image reread is required before treating `A` as a middle initial, maternal-surname abbreviation, joined surname, or conversion artifact.
3. The article says Dr. Dario Pulgar A. inherited Fundo Los Cuartos from `sus padres` around 1917, but it does not name the parents. No Jose/Juana candidate can be attached from this source.
4. The canonical `wiki/people/dario-arturo-pulgar-smith.md` page is family-supplied and explicitly warns not to merge similarly named Dario/Pulgar records without identity review.
5. Do not merge or rename Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Darío/Dario Pulgar Arriagada, or Jose/Juana parent candidates from this note.

## Literal Source Readings

- Staged conflict draft: `research/_staging/conflicts/chunk-f427d5055744-p0011-01-dario-pulgar-a-name-form-watch.md`.
- El Aguila source packet: `research/_staging/source-packets/chunk-f427d5055744-p0011-01-el-aguila-fundo-los-cuartos-dario-pulgar-a.md`.
- El Aguila chunk: `raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0011-chunk-01.md`.
- Literal body support: `EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,` and `DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDÓ DE SUS PADRES ESTE FUNDO ALLA POR EL AÑO 1917`.
- Literal signature transcription: `[signature] DR. DARIO PULGARA [/signature]`.
- Relevant comparison packet: `research/_staging/source-packets/SP-STAGE-CHUNK-c136e7acf00f-P0001-01-highland-loch-pulgar-passenger-list.md` reports row 55 as `Dario Pulgar A.`, occupation `Medical Surgeon`, age `39`, Chile citizenship/residence, but is held for image/row QA.
- Relevant comparison packet: `research/_staging/source-packets/chunk-c3c383bb7b4e-p0011-01-dario-j-pulgar-arriagada-medico-cirujano.md` reports `Darío J. Pulgar Arriagada` under `Médicos-Cirujanos` in the 2 September 1918 Anales session.
- Relevant comparison packet: `research/_staging/source-packets/SP-STAGE-CHUNK-cda8daf3a341-P0001-01-icrc-group-photo-dario-jose-pulgar-arriagada.md` uses title/file metadata for `Dario Jose Pulgar-Arriagada`; the image page itself has no identifying caption text.
- Relevant comparison packet: `research/_staging/source-packets/SP-STAGE-CHUNK-f128f4a0ac0d-P0001-01-dario-a-pulgar-i94-transit-1959.md` reports `DARIO A PULGAR`, birthdate `1 JUN 1942`, and permanent address `Box 1244 CONCEPCION CHILE`, held for source-image QA.

## Hypotheses

### H1: El Aguila Dr. Dario Pulgar A. is the 1928 Highland Loch `Dario Pulgar A.`

Evidence supporting:

- Exact source-level name overlap: El Aguila article has `Dario Pulgar A`; the 1928 passenger-list packet has `Dario Pulgar A.`.
- Occupation aligns: El Aguila says `DR` and `facultativo de Concepcion`; the passenger row says `Medical Surgeon`.
- Chronology is plausible: age 39 in July 1928 implies birth about 1888-1889, old enough to be a physician and property heir by 1917.
- Chile context aligns broadly: El Aguila ties him to Concepcion/Bio-Bio; the passenger row has Chile citizenship/residence and a Chile departure context.

Conflicts and limits:

- The 1928 table is held for source-image/row-column QA.
- The passenger list does not mention Fundo Los Cuartos, parents, Concepcion, or Arriagada.
- The El Aguila `PULGAR A`/`PULGARA` discrepancy remains unresolved.

Scores:

| Metric | Score | Note |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong name and occupation bridge, pending QA. |
| conflict_severity | 0.50 | Mainly a normalization and row-proof risk. |
| evidence_quality | 0.72 | Two local staged sources; one dense table held for reread. |
| conversion_confidence | 0.68 | El Aguila medium-high with signature concern; passenger list medium. |
| claim_probability | 0.76 | Probable same source person if both readings survive proof review. |
| relevance | 0.95 | Direct comparison for the staged draft. |
| canonical_readiness | 0.35 | Hold until proof review. |

### H2: El Aguila Dr. Dario Pulgar A. is `Darío J. Pulgar Arriagada`

Evidence supporting:

- The 1918 Anales packet has high-confidence support for `Darío J. Pulgar Arriagada` under `Médicos-Cirujanos`.
- The 1918 medical-title date is close to the article's statement that the doctor inherited the fundo around 1917.
- The terminal `A.` in `Dario Pulgar A.` could be an abbreviation for `Arriagada`.

Conflicts and limits:

- El Aguila does not print `J.` or `Arriagada`; Anales does not print `Fundo Los Cuartos`, Concepcion, parents, age, or property.
- The `J.` initial is not expanded in the reviewed local evidence.
- This hypothesis becomes stronger only after the El Aguila and 1928 `Dario Pulgar A.` readings are proof-reviewed.

Scores:

| Metric | Score | Note |
| --- | ---: | --- |
| identity_confidence | 0.66 | Plausible occupational/chronology bridge; no direct identity bridge. |
| conflict_severity | 0.55 | Risk of silently expanding initials. |
| evidence_quality | 0.74 | Anales name/title evidence is strong, but comparative bridge is circumstantial. |
| conversion_confidence | 0.76 | Anales reread is high; El Aguila still has signature QA. |
| claim_probability | 0.62 | Plausible if `A.` is proved as Arriagada. |
| relevance | 0.90 | Direct Pulgar-Arriagada comparison. |
| canonical_readiness | 0.30 | Hold for bridge review. |

### H3: El Aguila Dr. Dario Pulgar A. is `Dario Jose Pulgar-Arriagada`

Evidence supporting:

- The ICRC group-photo packet contains title/file metadata naming `Dario Jose Pulgar-Arriagada`.
- If later proof expands `Darío J. Pulgar Arriagada` to `Dario Jose Pulgar-Arriagada`, it may become part of the same candidate cluster.

Conflicts and limits:

- No source in this task expands `J.` to `Jose`.
- The ICRC image page has no visible caption or person label; identity is metadata-based.
- El Aguila does not print `Jose` or `Arriagada`.

Scores:

| Metric | Score | Note |
| --- | ---: | --- |
| identity_confidence | 0.48 | Possible through an unproved name expansion. |
| conflict_severity | 0.45 | Bridge gap, not a direct contradiction. |
| evidence_quality | 0.52 | Metadata identity is weak for proof. |
| conversion_confidence | 0.58 | Mixed QA status. |
| claim_probability | 0.43 | Contingent on future proof. |
| relevance | 0.78 | Required comparison. |
| canonical_readiness | 0.15 | Not ready. |

### H4: El Aguila Dr. Dario Pulgar A. is Dario Arturo Pulgar or Dario Arturo Pulgar-Smith

Evidence supporting:

- The canonical page records `Dario Arturo Pulgar-Smith` as Alexander John Heinz's maternal grandfather from family-supplied knowledge.
- Staged later records include a `DARIO A PULGAR` I-94 with Concepcion, Chile context, and the `A` initial.

Conflicts and limits:

- The I-94 packet reports birthdate `1 JUN 1942`; that person cannot be the adult doctor who inherited a fundo around 1917 or the age-39 medical surgeon in 1928.
- The CV/I-94 style later `Dario Arturo` cluster is not bridged to the El Aguila doctor/fundo owner.
- The canonical Pulgar-Smith page itself warns against same-name merges without identity review.

Scores:

| Metric | Score | Note |
| --- | ---: | --- |
| identity_confidence | 0.06 | Chronology strongly disfavors same-person identity with the 1942-born cluster. |
| conflict_severity | 0.80 | High risk if merged by name or initial alone. |
| evidence_quality | 0.65 | Relevant for anti-conflation, not for same-person proof. |
| conversion_confidence | 0.55 | Later records still include QA holds. |
| claim_probability | 0.08 | Name overlap only. |
| relevance | 0.85 | Required Pulgar-Smith comparison. |
| canonical_readiness | 0.05 | Do not attach to Pulgar-Smith now. |

### H5: El Aguila Dr. Dario Pulgar A. is later canonical `Darío Pulgar Arriagada`

Evidence supporting:

- `wiki/people/dar-o-pulgar-arriagada.md` has a reviewed 2000 legal-notice fact for `Darío Pulgar Arriagada`.
- The `Pulgar Arriagada` name form is relevant to evaluating whether El Aguila's `A.` could stand for `Arriagada`.

Conflicts and limits:

- The 2000 legal notice has no birth year, medical occupation, parents, or direct bridge to the 1917-1928 doctor/fundo-owner evidence.
- A same-name or same-surname form across decades is not enough for a merge.

Scores:

| Metric | Score | Note |
| --- | ---: | --- |
| identity_confidence | 0.20 | Name-form context only. |
| conflict_severity | 0.35 | Watch-level risk. |
| evidence_quality | 0.60 | Narrow canonical fact, sparse identity data. |
| conversion_confidence | 0.70 | Stable for the 2000 claim, not for this identity bridge. |
| claim_probability | 0.18 | No bridge. |
| relevance | 0.55 | Useful comparison, not a same-person proof. |
| canonical_readiness | 0.05 | No merge or attachment. |

### H6: Jose/Juana candidates are parents of El Aguila Dr. Dario Pulgar A.

Evidence supporting:

- El Aguila states that Dr. Dario Pulgar A. inherited Fundo Los Cuartos from `sus padres`.
- Existing wiki context includes Pulgar-line Jose/Juana candidates: `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Conflicts and limits:

- El Aguila names no parents.
- `Jose del Carmen Segundo Pulgar Arriagada` is a separate child identity, not a parent candidate for Dario by this evidence.
- The Jose/Juana records belong to separate staged/canonical clusters and must not be imported by surname proximity.

Scores:

| Metric | Score | Note |
| --- | ---: | --- |
| identity_confidence | 0.10 | Parent identity is not stated. |
| conflict_severity | 0.70 | High false-relationship risk. |
| evidence_quality | 0.45 | Parent-candidate evidence exists elsewhere but is not linked here. |
| conversion_confidence | 0.45 | Some related clusters have review caveats. |
| claim_probability | 0.08 | Generic parent language only. |
| relevance | 0.65 | Important because the article mentions unnamed parents. |
| canonical_readiness | 0.00 | No parent relationship ready. |

## Ranked Conclusion

1. Most plausible same-person hypothesis: El Aguila `Dr. Dario Pulgar A.` is the 1928 Highland Loch `Dario Pulgar A.`, age 39, `Medical Surgeon`.
2. Plausible but unproved: El Aguila `Dr. Dario Pulgar A.` is `Darío J. Pulgar Arriagada`, if `A.` is later proved as `Arriagada` or a bridge source joins the doctor/fundo-owner to the 1918 medical-title person.
3. Possible name expansion only: `Dario Jose Pulgar-Arriagada`, contingent on proof that `Darío J.` expands to Jose and belongs to the same identity.
4. Low-confidence contextual match: later canonical `Darío Pulgar Arriagada` legal-notice person.
5. Unlikely same person: later `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` cluster, especially where the 1959 I-94 reports birthdate `1 JUN 1942`.
6. Unsupported: any Jose/Juana parent candidate as parent of El Aguila Dr. Dario Pulgar A.

## Recommended Next Action

1. Proof-review the El Aguila page image for the exact typed name and signature: decide whether the signature reads `DARIO PULGARA`, `DARIO PULGAR A`, or another form.
2. Proof-review the 1928 Highland Loch row 55 for row/column alignment: `Dario Pulgar A.`, age `39`, `Medical Surgeon`, Chile citizenship/residence, and intended future residence.
3. If both pass, run a targeted identity-bridge proof review comparing only the proof-reviewed El Aguila doctor/fundo-owner and 1928 medical-surgeon evidence first; then compare that result to the 1918 `Darío J. Pulgar Arriagada` medical-title packet.

Canonical action remains blocked. Do not promote parent relationships, attach El Aguila claims to Dario Arturo Pulgar-Smith, or merge Pulgar-Arriagada pages until the proof-review steps above produce a direct bridge.
