---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md"
worker: postconv-identity-analysis-20260524175425360
staged_conflict_draft: "research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md"
subject: "Dr. Dario Pulgar A."
source_packet: "research/_staging/source-packets/chunk-63c2ae38e2fe-p0014-01-dario-pulgar-los-cuartos.md"
source: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0014-chunk-01.md"
chunk_id: "CHUNK-63c2ae38e2fe-P0014-01"
page_reference: "source page 14"
analysis_status: hold_for_conversion_qa_and_identity_bridge
canonical_readiness: do_not_promote
---

# Identity And Conflict Analysis: Pulgar A. Signature Watch

## Blockers First

- This note analyzes the exact staged conflict draft `research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md`.
- The requested `$genealogy-proof-review` contract is not installed as a readable skill in this session; this note follows the local evidence contract already present in the staged Pulgar proof-review notes: preserve literal readings, separate interpretation, and do not merge by name alone.
- Do not promote the signature reading. The staged draft and source packet say page 14 was flagged for `reread-page`, and no page image for page 14 was found in the conversion job directory during extraction.
- Resolve the provenance mismatch before promotion: the staged draft/source packet cite `CHUNK-63c2ae38e2fe-P0014-01`, while the current referenced chunk frontmatter reads `CHUNK-dfc1ae4668c1-P0014-01`.
- The typed article line reads `DR DARIO PULGAR A`; the visual note transcribes the handwritten signature as `DR. DARIO PULGARA`. This is a name-form/conversion conflict, not proof of a separate surname or duplicate person.
- The article says the subject inherited Fundo Los Cuartos from unnamed parents around 1917. It does not name Jose, Juana, Arturo, Smith, Arriagada, spouse, child, or grandchild.
- Existing wiki and staged context keep `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Darío Pulgar Arriagada`, adult/child `Dario Pulgar` passenger candidates, and Jose/Juana parent candidates as separate or unresolved clusters.
- No external research was performed. No raw sources, converted Markdown, chunks, staged source packets, or canonical wiki pages were edited.

## Literal Source Reading

The staged source packet quotes the typed article:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL AÑO 1917
```

The same packet separately records the signature:

```text
[Handwritten signature in blue ink:] DR. DARIO PULGARA
```

Literal reading: source page 14 identifies a page-local subject named `Dr Dario Pulgar A.`, describes him as a physician of Concepcion, says he owned Fundo Los Cuartos, and says he inherited that fundo from unnamed parents around 1917.

Interpretation kept separate: the final `A` in the signature may be a closely spaced initial after `Pulgar`, but the current local evidence does not prove `Pulgara` as a surname, does not expand `A.` to `Arriagada`, and does not identify the unnamed parents.

## Hypothesis 1: Signature Is `Pulgar A.` For The Same Page-Local Subject

Supporting evidence:

- The clearer typed article line gives the subject as `DR DARIO PULGAR A`.
- The staged conflict draft itself warns that the handwritten `PULGARA` may be `Pulgar A.` with a stylized or closely spaced final initial.
- The source packet describes one article subject and one signature location; no second Dario/Pulgar person is identified on the page.

Conflicts and limits:

- The derivative chunk and source packet still preserve the signature as `DR. DARIO PULGARA`.
- No page image was available during extraction, so the signature spacing and letters cannot be settled here.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.74 | Strong page-local alignment between typed subject and signature context; exact handwriting unresolved. |
| conflict_severity | 0.35 | Low if held as QA caution; material only if promoted as a separate name. |
| evidence_quality | 0.62 | Direct local transcription, but derivative and single-source. |
| conversion_confidence | 0.42 | Typed line is usable; signature and chunk-id mismatch reduce confidence. |
| claim_probability | 0.72 | Most likely current explanation for the `PULGARA` reading. |
| relevance | 1.00 | Directly addresses the assigned staged conflict. |
| canonical_readiness | 0.10 | Requires page-image proof review before promotion. |

## Hypothesis 2: Signature Literally Reads Distinct `Pulgara`

Supporting evidence:

- The referenced chunk and source packet both transcribe the handwritten signature as `DR. DARIO PULGARA`.
- The staged conflict draft correctly preserves this literal conversion reading instead of silently normalizing it.

Conflicts and limits:

- The typed article body supplies the stronger identity form `DR DARIO PULGAR A`.
- No local canonical page or reviewed note found for this task supports `Pulgara` as a separate surname or person.
- Promoting `Pulgara` would likely create a false name variant or duplicate-person conflict.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Rests on the lowest-confidence visual element. |
| conflict_severity | 0.70 | High risk if promoted as a distinct identity or surname. |
| evidence_quality | 0.30 | Needs direct page-image review. |
| conversion_confidence | 0.22 | Signature is the exact problem area. |
| claim_probability | 0.16 | Possible literal reading, but weaker than `Pulgar A.`. |
| relevance | 0.96 | Central to the staged conflict. |
| canonical_readiness | 0.00 | Do not promote. |

## Hypothesis 3: Same Older Medical/Property Candidate As `Dario Jose Pulgar-Arriagada` Or `Darío J. Pulgar Arriagada`

Supporting evidence:

- `Pulgar A.` could eventually prove to abbreviate `Pulgar Arriagada`, but that is only a hypothesis.
- Local staged context includes `Darío J. Pulgar Arriagada` as a medical-surgeon title candidate and `Dario Jose Pulgar-Arriagada` in a 1929 Health Service/Geneva photograph context.
- The page-14 article's `Dr.` and `facultativo de Concepcion` language is professionally compatible with an older medical cluster.
- Other local Pulgar analyses note a 1928 `Dario Pulgar A.` medical-surgeon passenger candidate and a 1953 adult `Dario Pulgar` medical passenger candidate as plausible but unmerged comparison points.

Conflicts and limits:

- Page 14 does not spell `Arriagada`, `Jose`, or `J.`.
- The photograph and passenger contexts have their own conversion/source-image holds or metadata limits.
- The current signature conflict cannot carry a full-name expansion or same-person bridge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.40 | Profession, place, and `A.` are suggestive, not conclusive. |
| conflict_severity | 0.68 | Expanding `A.` without proof would conflate clusters. |
| evidence_quality | 0.50 | Multiple local clues exist, but none bridges identity. |
| conversion_confidence | 0.46 | Mixed local evidence; page 14 and several comparison packets need QA. |
| claim_probability | 0.36 | Plausible older medical/property hypothesis. |
| relevance | 0.92 | Required Pulgar-line comparison. |
| canonical_readiness | 0.04 | No merge or name expansion. |

## Hypothesis 4: Same Person As Document-Level `Dario Arturo Pulgar` Or Canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- The names share `Dario` and `Pulgar`.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` records family-supplied knowledge that Dario Arturo Pulgar-Smith is Alexander John Heinz's maternal grandfather.
- Local CV staging preserves a document-level `Dario Arturo Pulgar` cluster requiring identity-bridge review before attachment to `Dario Arturo Pulgar-Smith`.

Conflicts and limits:

- Page 14 does not state `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, spouse, child, grandchild, CV education, or CV employment.
- The page-14 subject is an older Concepcion physician/property owner with inheritance around 1917; this is not a bridge to the CV/Pulgar-Smith cluster.
- The canonical Pulgar-Smith page explicitly cautions against automatic attachment of similarly named Pulgar records without identity review.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Shared name elements only. |
| conflict_severity | 0.78 | Wrong attachment would contaminate a central family-supplied profile. |
| evidence_quality | 0.42 | Family context is real but not source-linked to page 14. |
| conversion_confidence | 0.44 | Reread may settle `Pulgar A.`, not `Arturo` or `Smith`. |
| claim_probability | 0.12 | Low on present local evidence. |
| relevance | 0.92 | Required Pulgar-line anti-conflation check. |
| canonical_readiness | 0.01 | Do not attach to Pulgar-Smith or CV subject. |

## Hypothesis 5: Same As Later Canonical `Darío Pulgar Arriagada`

Supporting evidence:

- `Pulgar A.` might eventually expand to `Pulgar Arriagada`.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` holds a narrow 2000-12-05 expropriation event naming `Darío Pulgar Arriagada`.

Conflicts and limits:

- The 2000 expropriation page has no age, profession, Fundo Los Cuartos, parent, inheritance, or Concepcion physician bridge.
- Local prior analysis warns that older medical/passenger chronology compared to a 2000 event creates a serious chronology caution unless vital dates or property-continuity evidence resolve it.
- Page 14 does not spell `Arriagada`; the signature issue cannot support this merge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.16 | Only possible surname expansion/name overlap. |
| conflict_severity | 0.80 | High chronology and property-context conflation risk. |
| evidence_quality | 0.46 | Separate narrow claims exist, not an identity bridge. |
| conversion_confidence | 0.50 | Later canonical event is clearer than the page-14 signature, but no bridge exists. |
| claim_probability | 0.12 | Unlikely without vital-date/property-continuity proof. |
| relevance | 0.82 | Relevant because of possible `A.` expansion. |
| canonical_readiness | 0.02 | Do not merge. |

## Hypothesis 6: Jose/Juana Parent Candidates Explain The Unnamed Parents

Supporting evidence:

- The article literally says `Dr Dario Pulgar A.` inherited the fundo from `sus padres` around 1917.
- Existing wiki context includes separate Jose/Juana Pulgar-line candidates: `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Conflicts and limits:

- Page 14 names no parent.
- The Jose/Juana candidates belong to separate birth-register/relationship clusters with their own conversion and confidence issues.
- Family-context hints justify a targeted double-check only; they do not justify normalizing a name, assigning parents, or building a lineage bridge from this article.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | No named parent evidence on page 14. |
| conflict_severity | 0.66 | Parent assignment would be unsupported. |
| evidence_quality | 0.32 | Parent-candidate evidence is separate and conversion-sensitive. |
| conversion_confidence | 0.38 | Related register context remains separately qualified. |
| claim_probability | 0.04 | Only unnamed-parent inheritance is supported. |
| relevance | 0.72 | Relevant because the page mentions parents. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflict Summary

- Same-person conflict: unresolved. The safest subject label remains a held page-local `Dr Dario Pulgar A.`.
- Duplicate-person risk: high if `PULGARA` is promoted as a separate person or if page 14 is merged by name alone with Pulgar-Smith, Arturo, Jose/Arriagada, later Arriagada, passenger, medical, or parent clusters.
- Name-variant conflict: page 14 supports only a conflict between typed `Dario Pulgar A.` and converted signature `Dario Pulgara`; it does not prove `Arriagada`, `Arturo`, `Jose`, `Smith`, or `Pulgar-Smith` variants.
- Relationship conflict: the article supports only unnamed parents; no Jose/Juana parent relationship is promotable.
- Chronology conflict: the adult physician/property-owner context and inheritance around 1917 make an older medical/property candidate plausible, but they caution against unreviewed attachment to later CV/Pulgar-Smith or 2000 Arriagada contexts.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Exact next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Signature is `Pulgar A.` for the same page-local subject, not distinct `Pulgara` | 0.72 | Reread source page 14 image and verify signature spacing against the typed line. |
| 2 | Same older medical/property candidate as `Dario Jose Pulgar-Arriagada` / `Darío J. Pulgar Arriagada` / older `Dario Pulgar A.` medical cluster | 0.36 | After page-14 reread, run a separate identity-bridge proof review using full name, occupation, age chronology, Concepcion/hospital/property context, and dates. |
| 3 | Signature literally reads a distinct `Pulgara` name form | 0.16 | Hold only as a QA caution until visual proof review confirms the letters. |
| 4 | Same as later canonical `Darío Pulgar Arriagada` expropriation person | 0.12 | Require vital-date or property-continuity evidence before any merge. |
| 5 | Same as document-level `Dario Arturo Pulgar` or canonical `Dario Arturo Pulgar-Smith` | 0.12 | Require a reviewed identity bridge to `Arturo`/`Smith`; do not attach from this draft. |
| 6 | Jose/Juana candidates are the unnamed parents | 0.04 | Require a source naming this Dario's parents; do not infer from `sus padres`. |

## Recommended Next Action

Keep `research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md` on hold as a proof-review caution. The exact next step is a page-image reread of source page 14 from `raw/sources/El Aguila Nombre Grande Scan.pdf`, plus a provenance audit reconciling the staged `CHUNK-63c2ae38e2fe-P0014-01` reference with the current chunk frontmatter `CHUNK-dfc1ae4668c1-P0014-01`.

If that review confirms the reading, promote only narrow claims for the verified name form, physician of Concepcion description, Fundo Los Cuartos ownership, and inheritance from unnamed parents around 1917. Do not promote a canonical alternate name, `Pulgara` surname, person merge, `Arriagada` expansion, `Arturo`/`Smith` attachment, or Jose/Juana parent relationship from this staged conflict draft.
