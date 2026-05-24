---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md"
worker: postconv-identity-analysis-20260524180723694
staged_conflict_draft: "research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md"
subject: "Dr. Dario Pulgar A."
source_packet: "research/_staging/source-packets/chunk-63c2ae38e2fe-p0014-01-dario-pulgar-los-cuartos.md"
source: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0014-chunk-01.md"
chunk_id: "CHUNK-63c2ae38e2fe-P0014-01"
page_reference: "source page 14"
analysis_status: hold_for_page_reread_and_identity_bridge
canonical_readiness: hold
---

# Identity And Conflict Analysis: Pulgar A. Signature Watch

## Blockers First

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md`.
- Do not promote the signature reading. The staged draft and source packet both say the page needs reread, and the source packet says no page image for source page 14 was found in the conversion job directory during extraction.
- Provenance/version blocker: the staged draft and source packet cite `CHUNK-63c2ae38e2fe-P0014-01`, but the referenced chunk frontmatter currently reads `CHUNK-dfc1ae4668c1-P0014-01` with converted SHA `dfc1ae4668c174a269b4b42e42ed66169bc0b7019e0fe6e9a38a9b5e7dfdeb3e`.
- Literal readings must stay separate: the typed article is transcribed as `DR DARIO PULGAR A,`; the visual note transcribes the handwritten signature as `DR. DARIO PULGARA`.
- Page 14 states that the subject inherited Fundo Los Cuartos from his parents around 1917, but it does not name Jose, Juana, or any other parent.
- Existing local context keeps `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, and Jose/Juana parent candidates unresolved or separate. This draft cannot merge them by name alone.

## Literal Source Reading

The source packet quotes the article body as:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL AÑO 1917
```

It separately records the handwritten note as:

```text
[Handwritten signature in blue ink:] DR. DARIO PULGARA
```

Literal page-local claim: the article names `DR DARIO PULGAR A`, describes him as a physician of Concepcion, says he inherited Fundo Los Cuartos from unnamed parents around 1917, and has a bottom-right signature currently transcribed as `DR. DARIO PULGARA`.

Interpretation: `PULGARA` may be a compressed or stylized `Pulgar A.` signature. The current evidence does not prove a surname `Pulgara`, does not expand `A.` to `Arriagada`, does not identify `Arturo` or `Smith`, and does not name the parents.

## Hypothesis 1: Signature Is `Pulgar A.`, Same Page-Local Subject

Supporting evidence:

- The typed body gives the clearer page-local form `DR DARIO PULGAR A`.
- The staged draft explicitly warns that handwritten `PULGARA` may be `Pulgar A.` with a stylized or closely spaced final initial.
- The source packet treats the signature as a conversion QA issue and recommends holding promotion.

Conflicts and limits:

- No page image was available during extraction, so the handwriting cannot be settled here.
- The referenced chunk still preserves the visual note as `DR. DARIO PULGARA`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.74 | Clear typed body supports `Dario Pulgar A.` as the page subject; exact signature form remains unresolved. |
| conflict_severity | 0.34 | Low if retained as QA caution; higher only if promoted as a distinct name. |
| evidence_quality | 0.62 | Direct transcription, but derivative and pending page-image reread. |
| conversion_confidence | 0.42 | Typed line is usable; signature and chunk provenance mismatch lower confidence. |
| claim_probability | 0.72 | Most likely current explanation is same subject with compressed `A.`. |
| relevance | 1.00 | Directly addresses the staged draft. |
| canonical_readiness | 0.10 | Hold until page-image proof review. |

## Hypothesis 2: `PULGARA` Is A Distinct Literal Name Form

Supporting evidence:

- The source packet and chunk both transcribe the handwritten signature as `DR. DARIO PULGARA`.
- The conflict draft properly preserves the visual reading instead of silently normalizing it.

Conflicts and limits:

- The typed article's `PULGAR A` is stronger page-local identity evidence than the unresolved handwriting note.
- No canonical or reviewed local context found here supports `Pulgara` as a separate surname/person for this article.
- Promoting `PULGARA` would risk creating an unsupported duplicate-person or name-variant conflict.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Based only on unresolved handwriting transcription. |
| conflict_severity | 0.70 | Promotion could create a false alternate name or duplicate identity. |
| evidence_quality | 0.30 | Needs direct visual confirmation. |
| conversion_confidence | 0.22 | Signature is the exact low-confidence element. |
| claim_probability | 0.16 | Possible but weaker than `Pulgar A.`. |
| relevance | 0.96 | Central to the conflict draft. |
| canonical_readiness | 0.00 | Do not promote. |

## Hypothesis 3: Same Older Medical/Property Candidate As `Dario Jose Pulgar-Arriagada` Or `Dario J. Pulgar Arriagada`

Supporting evidence:

- `Pulgar A.` could eventually prove to abbreviate `Pulgar Arriagada`, but that is interpretation only.
- Local staged context includes `Dario J. Pulgar Arriagada` and `Dario Pulgar-Arriagada` in medical/service contexts.
- Page 14 describes a `Dr Dario Pulgar A.` who was a physician of Concepcion and property owner, which is compatible with an older medical/property candidate.

Conflicts and limits:

- Page 14 does not spell `Arriagada`, `Jose`, or `J.`.
- Page 14 gives no birth date, spouse, child, named parent, title grant, convention role, or other explicit bridge.
- The signature issue cannot carry a same-person merge or surname expansion.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.38 | Medical context and `A.` are suggestive only. |
| conflict_severity | 0.68 | High conflation risk if `A.` is expanded without proof. |
| evidence_quality | 0.48 | Useful local context, but bridge evidence is weak. |
| conversion_confidence | 0.46 | Page 14 has QA hold; related sources need their own reviews. |
| claim_probability | 0.34 | Plausible older professional hypothesis, not proved. |
| relevance | 0.90 | Required Pulgar-line comparison. |
| canonical_readiness | 0.04 | No merge or name expansion. |

## Hypothesis 4: Same Person As `Dario Arturo Pulgar` Or Canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- The names share `Dario` and `Pulgar`.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and warns not to attach Dario/Pulgar/Pulgar-Arriagada records without identity review.
- Existing CV staging preserves a document-level `Dario Arturo Pulgar` cluster as a possible but unproved bridge to `Dario Arturo Pulgar-Smith`.

Conflicts and limits:

- Page 14 does not state `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, spouse, child, grandchild, CV facts, or any family relationship.
- An older Concepcion physician/property-owner context with inheritance around 1917 does not bridge to the later CV/Pulgar-Smith cluster.
- Existing proof-review context keeps CV-to-Pulgar-Smith attachment on hold pending explicit identity-bearing evidence.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Shared name elements only. |
| conflict_severity | 0.78 | Wrong attachment would contaminate the central family-supplied profile. |
| evidence_quality | 0.42 | Family context is real but not source-linked to this page. |
| conversion_confidence | 0.44 | Reread can settle `Pulgar A.`, not `Arturo` or `Smith`. |
| claim_probability | 0.12 | Low without an identity bridge. |
| relevance | 0.92 | Required anti-conflation check. |
| canonical_readiness | 0.01 | Do not attach to Pulgar-Smith or CV subject. |

## Hypothesis 5: Same As Later `Dario/Dario Pulgar Arriagada` Legal-Notice Candidate

Supporting evidence:

- `Pulgar A.` might eventually be an abbreviated `Pulgar Arriagada`.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` has a narrow 2000-12-05 expropriation event naming `Dario Pulgar Arriagada`.

Conflicts and limits:

- The legal-notice candidate has no age, profession, Fundo Los Cuartos connection, or parent/inheritance bridge in the canonical page.
- Page 14's inheritance around 1917 and adult physician/property-owner context are a chronology caution against unreviewed attachment to a 2000 legal-notice candidate.
- Page 14 does not spell `Arriagada`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.16 | Only possible abbreviation/name overlap. |
| conflict_severity | 0.80 | Serious chronology and property-context conflation risk. |
| evidence_quality | 0.46 | Each source supports separate narrow claims, not same-person identity. |
| conversion_confidence | 0.50 | The 2000 notice is clearer than the page-14 signature, but no bridge exists. |
| claim_probability | 0.12 | Unlikely on present evidence. |
| relevance | 0.82 | Relevant because of possible `A.` expansion. |
| canonical_readiness | 0.02 | Do not merge. |

## Hypothesis 6: Jose/Juana Parent Candidates Explain `Sus Padres`

Supporting evidence:

- The article says `Dr Dario Pulgar A.` inherited the fundo from `sus padres` around 1917.
- Existing wiki context includes separate Jose/Juana Pulgar-line candidates: `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Conflicts and limits:

- Page 14 names no parent.
- The Jose/Juana materials are separate birth-register/relationship clusters with their own confidence and conversion issues.
- Family-context hints justify a targeted double-check, not a silent correction or parent assignment.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | No named parent evidence on this page. |
| conflict_severity | 0.66 | Assigning named parents would create unsupported relationship claims. |
| evidence_quality | 0.32 | Parent-candidate evidence is separate and conversion-sensitive. |
| conversion_confidence | 0.38 | Page 14 and related register contexts need separate QA. |
| claim_probability | 0.04 | Only unnamed-parent inheritance is supported. |
| relevance | 0.72 | Relevant because the article mentions parents. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflict Summary

- Same-person conflict: unresolved. The page supports only a held page-local subject, `Dr Dario Pulgar A.`, until reread.
- Duplicate-person risk: high if `PULGARA` is promoted as a separate person or if `Dario Pulgar A.` is merged with Pulgar-Smith, Arturo, Jose/Arriagada, later Arriagada, passenger, or parent clusters by name alone.
- Name-variant conflict: typed body supports `Dario Pulgar A.`; the signature is currently `Dario Pulgara` in the conversion. Do not treat `Pulgara`, `Arriagada`, `Arturo`, `Jose`, or `Smith` as proved variants from this draft.
- Relationship conflict: the source states only unnamed parents; no Jose/Juana parent relationship is promotable.
- Chronology conflict: page 14's inheritance around 1917 and adult physician/property-owner context may fit an older medical cluster, but it cautions against unreviewed attachment to later CV/Pulgar-Smith or 2000 Arriagada contexts.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Signature is `Pulgar A.` / same page-local subject, not distinct `Pulgara` identity | 0.72 | Reread source page 14 image and verify typed line plus signature spacing. |
| 2 | Same older medical/property candidate as `Dario Jose Pulgar-Arriagada` or `Dario J. Pulgar Arriagada` | 0.34 | Preserve as unresolved; require full-name or identity-bearing bridge. |
| 3 | Signature literally reads a distinct `Pulgara` name form | 0.16 | Hold only as QA caution until visual proof review. |
| 4 | Same as later `Dario/Dario Pulgar Arriagada` legal-notice candidate | 0.12 | Do not merge; require vital-date/property-continuity proof. |
| 5 | Same as `Dario Arturo Pulgar` or canonical `Dario Arturo Pulgar-Smith` | 0.12 | Do not attach; require a reviewed identity bridge to Arturo/Smith. |
| 6 | Jose/Juana parent candidates explain the unnamed parents | 0.04 | No relationship action; require a source naming Dario's parents. |

## Recommended Next Action

Keep `research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md` on hold as a proof-review caution. The exact next step is a page-image reread of source page 14 from `raw/sources/El Aguila Nombre Grande Scan.pdf`, plus a provenance audit reconciling staged `CHUNK-63c2ae38e2fe-P0014-01` against current chunk frontmatter `CHUNK-dfc1ae4668c1-P0014-01`.

During proof review, decide only the narrow source reading: whether the page supports `DR DARIO PULGAR A`, `DR. DARIO PULGARA`, a stylized `Pulgar A.`, or another literal form. If confirmed, promote only narrow claims for verified name form, Concepcion physician description, ownership of Fundo Los Cuartos, and inheritance from unnamed parents around 1917. Do not promote a canonical alternate name, same-person merge, `Arriagada` expansion, `Arturo`/`Smith` attachment, or Jose/Juana parent relationship from this staged conflict draft.
