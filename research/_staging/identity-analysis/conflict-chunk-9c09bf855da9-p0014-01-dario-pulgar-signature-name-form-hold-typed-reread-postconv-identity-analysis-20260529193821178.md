---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260529193821178
task_id: "identity-analysis:research/_staging/conflicts/conflict-chunk-9c09bf855da9-p0014-01-dario-pulgar-signature-name-form-hold-typed-reread-20260529185214597.md"
staged_conflict_draft: "research/_staging/conflicts/conflict-chunk-9c09bf855da9-p0014-01-dario-pulgar-signature-name-form-hold-typed-reread-20260529185214597.md"
source_packet: "research/_staging/source-packets/chunk-9c09bf855da9-p0014-01-el-aguila-fundo-los-cuartos-dario-pulgar-typed-reread-postconv-evidence-extraction-20260529185214597.md"
source: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0014-chunk-01.md"
chunk_id: CHUNK-9c09bf855da9-P0014-01
page_reference: page 14
analysis_status: hold_for_signature_qa_and_identity_bridge
canonical_readiness: hold
---

# Identity/Conflict Analysis: Dr Dario Pulgar A Signature Name-Form Hold

## Blockers First

- Exact staged conflict draft analyzed: `research/_staging/conflicts/conflict-chunk-9c09bf855da9-p0014-01-dario-pulgar-signature-name-form-hold-typed-reread-20260529185214597.md`.
- The literal typed article line is stronger than the footer signature and reads `AL DR DARIO PULGAR A,`. The red-pencil footer signature remains unresolved as to spacing and final form.
- The assigned page does not expand `A` to `Arriagada`, `Arturo`, or any other name. It does not print `Jose`, `J.`, or `Smith`.
- The assigned page mentions inheritance from `sus padres` only. It does not name Jose or Juana parent candidates.
- The existing canonical `wiki/people/dario-arturo-pulgar-smith.md` is family supplied and warns that Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records need identity review before attachment.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, reviewed notes, or canonical wiki pages were edited.

## Literal Source Readings

From the staged conflict draft:

```text
Typed article line: AL DR DARIO PULGAR A,
```

```text
Converted chunk signature note: [Handwritten signature: DR. DARIO PULGARA]
```

From the referenced source packet:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL AÑO 1917
```

Interpretation kept separate: the page supports a page-local person named `Dr Dario Pulgar A`, described as a distinguished physician of Concepcion, associated with Fundo Los Cuartos, and said to have inherited that fundo from unnamed parents around 1917. The signature should not be used to assert `PULGARA`, to normalize the name as `Pulgar A.`, or to bridge identities until targeted visual QA resolves the signature.

## Hypothesis 1: Page-Local Dr Dario Pulgar A

Supporting evidence:

- The staged conflict draft and source packet both preserve the typed article reading `DR DARIO PULGAR A`.
- The same sentence supplies the physician, Concepcion, Fundo Los Cuartos, and unnamed-parent inheritance context.
- The source packet gives medium-high confidence for the typed article line after local page-image reread.

Conflicts and limits:

- The final `A` is not expanded.
- The signature is lower confidence than the typed article line.
- No spouse, child, named parents, birth/death details, or canonical family bridge is stated.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.84 | Strong for the page-local article subject only. |
| conflict_severity | 0.42 | Moderate name-form risk, not a direct kinship contradiction. |
| evidence_quality | 0.74 | Direct typed article text with reread support. |
| conversion_confidence | 0.70 | Medium-high for typed text; low for footer signature spacing. |
| claim_probability | 0.84 | The article very likely names a local `Dr Dario Pulgar A`. |
| relevance | 0.96 | Direct Pulgar-line property and physician lead. |
| canonical_readiness | 0.45 | Narrow page-local claims may proceed to proof review; identity bridge is not ready. |

## Hypothesis 2: Footer Signature Is A `Pulgar A` Or `Pulgara` Name Variant

Supporting evidence:

- The footer signature is on the same page as the typed article naming `DR DARIO PULGAR A`.
- The conflict draft specifically identifies the signature as ambiguous between a spaced final initial and an unspaced `PULGARA` form.

Conflicts and limits:

- The staged draft explicitly says not to use the footer to assert `PULGARA` or a clean `PULGAR A.` signature without sharper targeted visual review.
- The footer cannot expand `A` to `Arriagada`, `Arturo`, or any other name.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Plausible same-page variant, unresolved. |
| conflict_severity | 0.52 | Material name-normalization risk if promoted. |
| evidence_quality | 0.42 | Signature reading is visually ambiguous. |
| conversion_confidence | 0.35 | Low for signature spacing/final form. |
| claim_probability | 0.55 | Possible but not promotable. |
| relevance | 0.92 | Directly controls the staged conflict. |
| canonical_readiness | 0.05 | Hold for targeted signature QA. |

## Hypothesis 3: Same As Dario/Darío Pulgar Arriagada Or Darío J. Pulgar Arriagada

Supporting evidence:

- Staged Anales evidence names `Darío J. Pulgar Arriagada` under `Médicos-Cirujanos` at a 2 September 1918 title-conferral session.
- Other staged Pulgar-Arriagada materials name `Dario Pulgar-Arriagada` or `Darío Pulgar Arriagada` in medical, Red Cross, hospital, or later legal contexts.
- The El Aguila article describes the page-local subject as `Dr` and `facultativo de Concepcion`, making a medical-professional comparison relevant.
- The final `A` in `Dario Pulgar A` is a legitimate proof-review target for possible `Arriagada`, but only as a hypothesis.

Conflicts and limits:

- The assigned page does not print `Arriagada` or `J.`.
- Existing Pulgar-Arriagada sources are separate staged/canonical contexts and do not state Fundo Los Cuartos, inheritance around 1917, or this signature.
- Same name family plus profession is not enough for a same-person merge.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.46 | Medical context is suggestive; bridge terms are absent. |
| conflict_severity | 0.64 | Risky if merged by final initial or profession alone. |
| evidence_quality | 0.55 | Useful comparison evidence exists locally but not on this page. |
| conversion_confidence | 0.62 | Assigned typed line is usable; bridge evidence is separate. |
| claim_probability | 0.40 | Plausible research lead, not proved. |
| relevance | 0.90 | Required Pulgar-line comparison. |
| canonical_readiness | 0.10 | Not ready. |

## Hypothesis 4: Same As Dario Jose Pulgar-Arriagada

Supporting evidence:

- Local staged ICRC/Geneva materials include the form `Dario Jose Pulgar-Arriagada`.
- If future proof review expands `Darío J. Pulgar Arriagada` to `Dario Jose Pulgar-Arriagada`, that would become relevant to the medical-professional comparison.

Conflicts and limits:

- The assigned page does not state `Jose`, `J.`, or `Arriagada`.
- The ICRC group-photograph packet depends on source title/file metadata and reports no visible text or image-region identity basis.
- No reviewed local source ties `Dario Jose Pulgar-Arriagada` to Fundo Los Cuartos or the page 14 signature.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.30 | Name-cluster relevance only. |
| conflict_severity | 0.56 | Medium risk if imported without a proof chain. |
| evidence_quality | 0.45 | No direct bridge from assigned page. |
| conversion_confidence | 0.60 | Assigned typed line is clearer than the proposed bridge. |
| claim_probability | 0.25 | Possible only through future `J.`/Jose bridge evidence. |
| relevance | 0.82 | Required Pulgar-Arriagada anti-conflation check. |
| canonical_readiness | 0.05 | Not ready. |

## Hypothesis 5: Same As Dario Arturo Pulgar

Supporting evidence:

- Staged CV material identifies a document-level subject named `Dario Arturo Pulgar`.
- The 1959 I-94 staged packet identifies `DARIO A PULGAR`, showing that an `A` initial appears in a separate Dario Pulgar context.

Conflicts and limits:

- The assigned page does not state `Arturo`.
- The 1959 I-94 packet gives birthdate `1 JUN 1942`, which is chronologically incompatible with an adult physician who inherited property around 1917.
- CV/Habitat/communications evidence does not bridge to the earlier doctor/property-owner identity.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Chronology argues strongly against same-person identity with the 1942-born cluster. |
| conflict_severity | 0.78 | High generation-conflation risk if merged by name or initial. |
| evidence_quality | 0.56 | Separate Dario Arturo evidence exists, but not as a bridge. |
| conversion_confidence | 0.55 | Several Dario Arturo/I-94 items remain held for QA. |
| claim_probability | 0.08 | Name overlap only. |
| relevance | 0.85 | Required anti-conflation comparison. |
| canonical_readiness | 0.00 | Do not merge or attach. |

## Hypothesis 6: Same As Canonical Dario Arturo Pulgar-Smith

Supporting evidence:

- Canonical `wiki/people/dario-arturo-pulgar-smith.md` records `Dario Arturo Pulgar-Smith` as Alexander John Heinz's maternal grandfather from family-supplied knowledge.
- Broad `Dario` plus `Pulgar` overlap makes the page a family-context double-check target.

Conflicts and limits:

- The assigned page does not state `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, or a descendant relationship.
- The canonical page explicitly warns against attaching similarly named Pulgar records without identity review.
- The El Aguila page alone is not a canonical identity bridge.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | Family-context watch only. |
| conflict_severity | 0.76 | High risk of false canonical attachment by name overlap. |
| evidence_quality | 0.42 | Canonical identity is family supplied; this page lacks bridge facts. |
| conversion_confidence | 0.70 | Typed line is usable but does not support this bridge. |
| claim_probability | 0.10 | Not supported from this page alone. |
| relevance | 0.90 | Required canonical anti-conflation check. |
| canonical_readiness | 0.00 | Do not attach. |

## Hypothesis 7: Jose/Juana Parent Candidates Are The Unnamed Parents

Supporting evidence:

- The assigned article says the page-local doctor inherited the fundo from `sus padres` around 1917.
- Existing wiki/staged context includes Pulgar-line Jose/Juana candidates, including `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Conflicts and limits:

- The assigned page names no Jose and no Juana.
- The Jose/Juana materials belong to separate birth-register and relationship contexts with their own conversion/name-form cautions.
- Generic parent wording can justify later parent-candidate review, not named parent promotion.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_or_relationship_confidence | 0.08 | No named parent evidence on this page. |
| conflict_severity | 0.80 | High if named parents are promoted from generic wording. |
| evidence_quality | 0.38 | Good only for unnamed-parent inheritance after proof review. |
| conversion_confidence | 0.70 | Typed inheritance sentence is medium-high; named-parent inference unsupported. |
| claim_probability | 0.78 unnamed parents; 0.05 Jose/Juana assignment | Literal wording supports only unnamed parents. |
| relevance | 0.84 | Important Pulgar-line reconstruction clue. |
| canonical_readiness | 0.00 | No named parent promotion. |

## Conflict Summary

- Same-person evidence: sufficient only for the page-local typed article subject.
- Duplicate-person evidence: no duplicate-person conclusion is supported.
- Name-variant evidence: active hold remains between typed `Pulgar A` and ambiguous footer `PULGARA`/`Pulgar A`.
- Relationship-conflict evidence: page supports unnamed parents only, not Jose/Juana named parents.
- Chronology-conflict evidence: no direct contradiction on page 14. The 1959 `DARIO A PULGAR`/Dario Arturo cluster is likely a different generation from the 1917 inheritance context.
- Conversion-confidence conflict: material only for the footer signature; the typed article line has medium-high reread confidence.

## Ranked Hypotheses

| Rank | Candidate or interpretation | Probability | Current disposition |
| ---: | --- | ---: | --- |
| 1 | Page-local `Dr Dario Pulgar A` from typed article | 0.84 | Proof-review eligible for narrow page-local claims only. |
| 2 | Footer signature as `Pulgara` / `Pulgar A` spacing variant | 0.55 | Hold for targeted visual signature QA. |
| 3 | Same as `Dario J. Pulgar Arriagada` / `Dario Pulgar Arriagada` | 0.40 | Plausible medical-context hypothesis; needs identity bridge. |
| 4 | Same as `Dario Jose Pulgar-Arriagada` | 0.25 | Possible only through future `J.`/Jose bridge. |
| 5 | Same as canonical `Dario Arturo Pulgar-Smith` | 0.10 | Family-context watch only; do not attach. |
| 6 | Same as `Dario Arturo Pulgar` / 1942-born `DARIO A PULGAR` cluster | 0.08 | Chronologically unlikely same person; do not merge. |
| 7 | Named Jose/Juana parent candidates | 0.05 | Unsupported by this page; do not promote. |

## Recommended Next Action

Proceed to proof review only for the narrow typed-article claims: page-local `Dr Dario Pulgar A`, association with Fundo Los Cuartos, description as a distinguished physician of Concepcion, and inheritance from unnamed parents around 1917.

Keep the red-pencil footer signature on conversion QA hold with this exact review question: does the local image support `DR. DARIO PULGARA`, `DR. DARIO PULGAR A`, or another uncertain form?

The next identity-proof step is a targeted Pulgar identity bridge review comparing proof-reviewed El Aguila facts against proof-reviewed `Dario Pulgar A` passenger/medical evidence, `Darío J. Pulgar Arriagada`, `Dario Jose Pulgar-Arriagada`, and only then `Dario Arturo Pulgar` / canonical `Dario Arturo Pulgar-Smith`. Do not assign Jose/Juana parents from this page.
