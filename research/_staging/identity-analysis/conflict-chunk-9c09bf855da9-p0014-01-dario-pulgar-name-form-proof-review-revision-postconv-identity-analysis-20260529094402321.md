---
type: identity_conflict_analysis
status: hold
role: identity_researcher
worker: postconv-identity-analysis-20260529094402321
task_id: "identity-analysis:research/_staging/conflicts/conflict-chunk-9c09bf855da9-p0014-01-dario-pulgar-name-form-proof-review-revision-postconv-evidence-extraction-20260529090029107.md"
staged_draft: "research/_staging/conflicts/conflict-chunk-9c09bf855da9-p0014-01-dario-pulgar-name-form-proof-review-revision-postconv-evidence-extraction-20260529090029107.md"
subject: "Dr Dario Pulgar A. / DR. DARIO PULGARA"
source_packet: "research/_staging/source-packets/chunk-9c09bf855da9-p0014-01-el-aguila-fundo-los-cuartos-dario-pulgar-proof-review-revision-postconv-evidence-extraction-20260529090029107.md"
source: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0014-chunk-01.md"
chunk_id: CHUNK-9c09bf855da9-P0014-01
page_reference: page 14
promotion_recommendation: hold_for_conversion_qa_and_identity_bridge_review
canonical_readiness: low
tags: [identity-analysis, conflict-review, pulgar, el-aguila]
---

# Identity/Conflict Analysis: Dr Dario Pulgar A. Name Form

## Blockers First

1. Exact staged draft analyzed: `research/_staging/conflicts/conflict-chunk-9c09bf855da9-p0014-01-dario-pulgar-name-form-proof-review-revision-postconv-evidence-extraction-20260529090029107.md`.
2. The controlling evidence is derivative only. `raw/sources/El Aguila Nombre Grande Scan.pdf` and the expected page image `raw/codex-conversion-jobs/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18/page-images/page-0014.jpg` are absent locally.
3. The exact name form is unresolved: the typed article line is transcribed as `DR DARIO PULGAR A`, while the handwritten signature note is transcribed as `DR. DARIO PULGARA`.
4. The article says the person inherited Fundo Los Cuartos from `sus padres` around 1917, but names no parent. No Jose or Juana candidate can be promoted from this page.
5. Do not expand `A`, normalize `PULGARA`, merge people, rename canonical pages, attach this to `Dario Arturo Pulgar-Smith`, or promote named-parent relationships until page-image QA and identity-bridge proof review are complete.

## Literal Evidence

From the staged conflict draft, source packet, and assigned chunk:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL AÑO 1917
```

```text
[Handwritten signature: DR. DARIO PULGARA]
```

Interpretation kept separate: the source currently supports only a held page-local person named in derivative text as `Dr Dario Pulgar A.` or possibly `Dr. Dario Pulgara`, associated with Fundo Los Cuartos and described as a Concepcion medical professional. The final `A` may be an initial, a separated surname abbreviation, a collapsed `Pulgara` reading, or a conversion artifact.

## Hypothesis 1: One Page-Local Dr Dario Pulgar A. / Pulgara

Supporting evidence:

- The typed article and signature note occur on the same derivative page.
- The body gives coherent page-local attributes: owner of Fundo Los Cuartos, distinguished physician/facultativo of Concepcion, heir from unnamed parents around 1917.
- The conflict is a final-letter or spacing boundary, not a different forename or incompatible event.

Conflicts and limits:

- The PDF/page image is unavailable, so the typed spacing, final `A`, and signature cannot be checked.
- No full name, age, birth date, spouse, child, death date, or named parents are stated.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | Strong for one page-local subject, weak for fuller identity. |
| conflict_severity | 0.50 | Material name-form issue, but no competing relationship fact yet. |
| evidence_quality | 0.58 | Direct derivative transcription, blocked by absent visual control. |
| conversion_confidence | 0.40 | Source packet rates low-to-medium and reports missing PDF/page image. |
| claim_probability | 0.70 | Probable as a narrow page-local claim only. |
| relevance | 1.00 | Directly addresses the staged conflict draft. |
| canonical_readiness | 0.08 | Hold for conversion QA and identity bridge. |

## Hypothesis 2: Same Older Medical Person As Dario Jose Pulgar-Arriagada / Dario J. Pulgar Arriagada

Supporting evidence:

- Page 14 uses `Dr` and `facultativo de Concepcion`, making medical Pulgar candidates the most relevant comparison group.
- Local staged context includes `Dario J. Pulgar Arriagada` under `Medicos-Cirujanos` in a 2 September 1918 title-conferral context.
- Other staged Geneva/ICRC materials preserve `Dario Jose Pulgar-Arriagada`, `D. Pulgar`, and Pulgar-Arriagada convention contexts as possible comparison evidence.
- If page-image QA later confirms `Pulgar A.`, `A` could be tested as a possible abbreviation for `Arriagada`; that is a hypothesis, not a reading.

Conflicts and limits:

- Page 14 does not spell `Jose`, `J.`, `Arriagada`, or `Pulgar-Arriagada`.
- The `A` after `Pulgar` cannot be expanded from this source alone.
- The comparison sources do not name Fundo Los Cuartos or the page-14 unnamed parents in the reviewed context.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.44 | Profession and chronology are suggestive, but no direct bridge exists. |
| conflict_severity | 0.72 | High risk if `A` is silently expanded to `Arriagada`. |
| evidence_quality | 0.56 | Relevant local staged evidence, but indirect. |
| conversion_confidence | 0.48 | Page 14 remains visually unverified; comparison items have separate holds. |
| claim_probability | 0.38 | Plausible older-medical hypothesis, not proved. |
| relevance | 0.98 | Required Pulgar-Arriagada comparison. |
| canonical_readiness | 0.05 | No merge or attachment. |

## Hypothesis 3: Same As Adult Passenger Dario Pulgar, Age 64

Supporting evidence:

- Canonical `Dario Pulgar (adult passenger, age 64)` has a 7 August 1953 travel fact. Age 64 implies a birth around 1888/1889, which could fit an adult who inherited property around 1917.
- Same broad name `Dario Pulgar`; prior local notes treat adult medical/passenger clusters as comparison leads.

Conflicts and limits:

- The canonical adult passenger stub does not state `A`, `Arriagada`, `Arturo`, `Smith`, Fundo Los Cuartos, Concepcion physician status, or named parents.
- The passenger event is a travel cluster, not an identity bridge to the page-14 property article.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Chronology is possible, but direct identifiers are absent. |
| conflict_severity | 0.64 | Moderate-to-high duplicate-person risk if linked by name only. |
| evidence_quality | 0.52 | Canonical passenger evidence is narrow and not a bridge. |
| conversion_confidence | 0.58 | Passenger evidence appears more stable than page 14, but indirect. |
| claim_probability | 0.14 | Possible lead only. |
| relevance | 0.74 | Useful same-name/chronology comparison. |
| canonical_readiness | 0.02 | Do not attach. |

## Hypothesis 4: Same As Dario Arturo Pulgar / Dario Arturo Pulgar-Smith

Supporting evidence:

- Canonical `wiki/people/dario-arturo-pulgar-smith.md` identifies Dario Arturo Pulgar-Smith as Alexander John Heinz's maternal grandfather from family-supplied knowledge.
- Staged CV materials use the document-level subject `Dario Arturo Pulgar`.
- The broad `Dario Pulgar` overlap and final `A` justify a double-check.

Conflicts and limits:

- Page 14 does not say `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, CV, Habitat, spouse, child, or grandchild.
- `Pulgar A` is not evidence that `A` means `Arturo`.
- The canonical Pulgar-Smith page explicitly warns against attaching similarly named records without identity review.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | Name overlap only. |
| conflict_severity | 0.84 | Wrong attachment would conflate family-supplied Pulgar-Smith/CV context with an older doctor/property-owner candidate. |
| evidence_quality | 0.40 | Canonical and CV contexts exist but do not bridge to page 14. |
| conversion_confidence | 0.42 | Page-14 name evidence controls and is held. |
| claim_probability | 0.09 | Unsupported by the assigned draft. |
| relevance | 0.95 | Required family-line anti-conflation comparison. |
| canonical_readiness | 0.01 | Do not attach. |

## Hypothesis 5: Same As Canonical Dario/Dario Pulgar Arriagada Property-Notice Cluster

Supporting evidence:

- Canonical `wiki/people/dar-o-pulgar-arriagada.md` exists for `Dario/Darío Pulgar Arriagada`.
- Its evidence snapshot records a 5 December 2000 Serviu Region del Bio Bio expropriation event.
- If later verified, `Pulgar A.` could theoretically abbreviate `Pulgar Arriagada`.

Conflicts and limits:

- Page 14 does not spell `Arriagada`.
- The 2000 notice does not state `Dr`, Concepcion medical status, Fundo Los Cuartos, inheritance around 1917, parent names, or age.
- The 1917-to-2000 chronology is hazardous without vital, estate, property-chain, or same-person bridge evidence.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | Initial/surname compatibility only. |
| conflict_severity | 0.80 | High duplicate-person and chronology-conflict risk. |
| evidence_quality | 0.48 | Legal-notice evidence supports its own stub, not this bridge. |
| conversion_confidence | 0.52 | The 2000 item is more stable than the page-14 signature, but comparison is indirect. |
| claim_probability | 0.08 | Weak without direct bridge evidence. |
| relevance | 0.88 | Required Pulgar-Arriagada comparison. |
| canonical_readiness | 0.01 | Do not merge. |

## Hypothesis 6: Child Passenger Dario Pulgar, Age 11

Supporting evidence:

- Canonical `Dario Pulgar (child passenger, age 11)` shares the broad name `Dario Pulgar`.

Conflicts and limits:

- Age 11 on 7 August 1953 implies birth around 1941/1942, which is chronologically incompatible with inheriting Fundo Los Cuartos around 1917.
- The child row does not state a parent-child relationship to the page-14 doctor/owner and does not contain `A`, `Arriagada`, `Arturo`, `Smith`, or Concepcion physician evidence.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | Same broad name only; chronology conflicts. |
| conflict_severity | 0.78 | High risk of false same-name merge. |
| evidence_quality | 0.50 | Passenger facts are narrow and unrelated to page 14. |
| conversion_confidence | 0.58 | Passenger evidence is not the weak point; the bridge is absent. |
| claim_probability | 0.02 | Implausible as same person. |
| relevance | 0.40 | Anti-conflation only. |
| canonical_readiness | 0.00 | Do not attach. |

## Hypothesis 7: Jose/Juana Candidates Are The Unnamed Parents

Supporting evidence:

- Page 14 says the subject inherited Fundo Los Cuartos from `sus padres` around 1917.
- Existing local context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Entry-172 review context supports `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` only as row-specific parent candidates for `Jose del Carmen Segundo Pulgar Arriagada`; entry-513 context preserves a separate `Juana de Dios Amagada de Pulgar` candidate.

Conflicts and limits:

- Page 14 names no parent.
- `Jose del Carmen Segundo Pulgar Arriagada` is a separate child identity, not a Dario identity.
- `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` must not be merged or substituted as parents from an unnamed `sus padres` phrase.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.04 | No named-parent evidence on page 14. |
| conflict_severity | 0.76 | Unsupported parent assignment would create a false lineage. |
| evidence_quality | 0.34 | Parent-candidate evidence is separate and partly conversion-sensitive. |
| conversion_confidence | 0.36 | Page 14 and parent-candidate clusters have QA limits. |
| claim_probability | 0.03 | The page supports only unnamed parents. |
| relevance | 0.82 | Required Jose/Juana parent-candidate comparison. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflict Summary

- Same-person evidence: unresolved beyond the page-local subject.
- Duplicate-person risk: high if this is merged by name with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, passenger candidates, or Jose/Juana parent clusters.
- Name-variant conflict: active and controlling. Preserve `DR DARIO PULGAR A` and `DR. DARIO PULGARA` separately until page-image proof review.
- Relationship conflict: no parent relationship is supported. `sus padres` is an unnamed-parent inheritance clue only.
- Chronology conflict: no internal page-14 chronology conflict, but serious cross-cluster chronology risk arises if this older doctor/property-owner context is attached to later CV, child passenger, or 2000 property-notice clusters without bridge evidence.
- Conversion conflict: missing PDF/page image is the controlling blocker for typed name spacing, signature reading, and promotion readiness.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Page-local `Dr Dario Pulgar A.` associated with Fundo Los Cuartos; signature likely same article context but name form unverified | 0.70 | Restore or locate page 14 source image/PDF and visually reread the typed name, signature, physician phrase, and inheritance sentence. |
| 2 | Same older medical person as `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada` / `Dario Pulgar-Arriagada` | 0.38 | After page-14 QA, run targeted identity-bridge proof review comparing exact names, initials, profession, Concepcion context, age, Los Cuartos/property clues, and chronology. |
| 3 | Same as adult passenger `Dario Pulgar` age 64 | 0.14 | Treat only as a lead; require reviewed age/occupation/property/name bridge. |
| 4 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.09 | Require explicit reviewed bridge to `Arturo`, `Pulgar-Smith`, or the CV/family identity. |
| 5 | Same as canonical `Dario Pulgar Arriagada` property-notice cluster | 0.08 | Require direct vital/property-chain/person bridge. |
| 6 | Jose/Juana candidates are the unnamed parents | 0.03 | Require a source naming this Dario's parents or a reviewed property/probate/vital bridge tied to Fundo Los Cuartos. |
| 7 | Same as child passenger `Dario Pulgar` age 11 | 0.02 | Do not pursue unless contradictory age evidence appears; current chronology argues against identity. |

## Recommended Next Action

Keep the assigned staged conflict on `hold_for_conversion_qa`. The exact next proof-review step is targeted visual QA for `CHUNK-9c09bf855da9-P0014-01`: restore or locate `raw/sources/El Aguila Nombre Grande Scan.pdf` or a page-14 image, then compare the image against the typed `DR DARIO PULGAR A` line, the handwritten signature, the `DISTINGUIDO FACULTATIVO DE CONCEPCION` phrase, and the inherited-from-parents sentence.

If page QA confirms the text, promote only narrow page-local claims first. A separate identity-bridge proof review is required before attaching the evidence to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, passenger-list candidates, or Jose/Juana parent candidates.
