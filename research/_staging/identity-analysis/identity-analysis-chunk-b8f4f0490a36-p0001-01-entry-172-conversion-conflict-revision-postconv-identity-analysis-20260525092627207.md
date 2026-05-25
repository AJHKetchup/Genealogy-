---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525081514407.md
worker: postconv-identity-analysis-20260525092627207
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525081514407.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525081514407.md
source_path: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: page 1; register page 58; entry 172
analysis_status: hold
canonical_readiness: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Entry 172 Conversion Conflict

## Blockers

- The exact staged draft analyzed here is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525081514407.md`.
- The controlling blocker is a material row-level conflict. The assigned converted Markdown records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`; the current chunk and source packet record entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- This is not a spelling variant or ordinary name-form issue. It is a conversion, row alignment, or file-assignment conflict that must be resolved before any identity, relationship, or canonical promotion.
- The father-name ending remains unresolved even under the Pulgar/Arriagada reading. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as possible QA outcomes until the source image is rechecked.
- Existing canonical pages already show generated evidence for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` from this chunk, but this analysis treats those as not ready for further promotion while the conversion conflict remains open.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, or canonical wiki pages were edited.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Hypothesis: The correct row for entry 172 is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`.

Literal evidence:

- The staged conflict draft states that the current chunk supports entry 172 as the birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The source packet records the same child, sex `Hombre`, registration date 7 April 1888, birth date 8 March 1888 at 3 p.m., birth place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, parents resident at `Calle de Colipi`, and informant `Ernesto Herrera L.`.
- The current chunk transcription also lists entry 172 with those Pulgar/Arriagada details.
- Canonical stubs exist for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`, and their generated snapshots cite the same chunk/source-packet family.

Interpretation:

- This is the strongest family-relevant reading if the current chunk is confirmed against the source image.
- It is still not canonically ready because the assigned converted Markdown attached to the same source/hash gives a different row. Treat the Pulgar/Arriagada reading as a held hypothesis, not a promoted fact.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.62 | The chunk and source packet align, but the assigned converted Markdown directly conflicts. |
| conflict_severity | 0.96 | The conflict changes the child and both parents. |
| evidence_quality | 0.58 | Local staged evidence is specific, but derivative artifacts disagree on the controlling row. |
| conversion_confidence | 0.35 | Conversion state is mixed until source-image QA resolves row alignment. |
| claim_probability | 0.61 | Plausible from current chunk/source packet; below promotion threshold. |
| relevance | 1.00 | Directly addresses the assigned staged draft. |
| canonical_readiness | 0.05 | Hold for targeted conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is The Gomez/de la Cruz Birth Registration

Hypothesis: The assigned converted Markdown is controlling, and entry 172 belongs to `Jose Francisco`, child of `Oswaldo Gomez` and `Emilia de la Cruz`.

Literal evidence:

- The converted Markdown records entry 172 as `Jose Francisco`, sex `Varon`, born 26 March 1888 at 10 p.m. in `En esta`.
- The same converted row names father `Oswaldo Gomez`, mother `Emilia de la Cruz`, and informant `Oswaldo Gomez`.
- The staged conflict draft explicitly identifies this converted-file reading as conflicting with the current chunk.

Interpretation:

- This hypothesis is possible only if the current chunk/source-packet Pulgar row is misassigned, stale, or drawn from a different page image than the converted Markdown.
- It would eliminate the Pulgar/Arriagada identity and relationship claims from this entry, but that conclusion cannot be adopted without targeted QA because the source packet and chunk currently disagree with the converted text.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.42 | Supported by one converted artifact, contradicted by current chunk and staged packet. |
| conflict_severity | 0.96 | Controls whether any Pulgar-line person is present in this entry. |
| evidence_quality | 0.43 | The converted text is concrete but appears misaligned against the current chunk. |
| conversion_confidence | 0.35 | Same mixed conversion state as hypothesis 1. |
| claim_probability | 0.39 | Possible, but not the best family-context reading without QA. |
| relevance | 1.00 | This is the other side of the row-level conflict. |
| canonical_readiness | 0.03 | Do not create or promote Gomez/de la Cruz claims from this task. |

## Hypothesis 3: Father Candidate Is Jose del Carmen Pulgar / Jose del Carmen Pulgar S.

Hypothesis: If the Pulgar/Arriagada row is confirmed, the father is a Jose del Carmen Pulgar candidate, with the final `S.` or suffix unresolved.

Literal evidence:

- The current chunk reads father as `Jose del Carmen Pulgar S.`, Chilean, employed, resident at `Calle de Colipi`.
- The source packet explicitly warns not to promote an exact father-name form until QA certifies `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- The canonical `wiki/people/jose-del-carmen-pulgar.md` page exists, but its current generated evidence snapshot links him to `Tulio Cesar Luis Jose` from a separate staged relationship, not to this entry's child.

Interpretation:

- The father candidate should not be merged or expanded from this entry yet.
- If QA confirms the Pulgar row and the father reading, the next proof-review step should create or revise a held parent relationship between the confirmed child and the confirmed father-name form. It should also compare, but not automatically merge, the existing `Jose del Carmen Pulgar` page.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.47 | Name is specific, but father suffix and row alignment are unresolved. |
| conflict_severity | 0.82 | Premature father attachment could misstate parentage and conflate Jose candidates. |
| evidence_quality | 0.52 | Specific current chunk reading, blocked by conversion conflict. |
| conversion_confidence | 0.30 | Father-name ending requires image-level reread. |
| claim_probability | 0.48 | Possible/probable only after the Pulgar row is confirmed. |
| relevance | 0.96 | Direct parent-candidate question for the assigned draft. |
| canonical_readiness | 0.04 | Hold; no father relationship promotion. |

## Hypothesis 4: Mother Candidate Is Juana Arriagada de Pulgar

Hypothesis: If the Pulgar/Arriagada row is confirmed, the mother is `Juana Arriagada de Pulgar`.

Literal evidence:

- The current chunk and source packet both name the mother as `Juana Arriagada de Pulgar`, Chilean, occupation `Su sexo`, resident at `Calle de Colipi`.
- The canonical `wiki/people/juana-arriagada-de-pulgar.md` page has a generated probable child link to `Jose del Carmen Segundo Pulgar Arriagada` citing this chunk/source-packet family.

Interpretation:

- The mother reading is internally more stable than the father suffix because the staged draft does not flag a mother-name ambiguity under the Pulgar row.
- It remains held because the row-level conflict could mean this entry is not the Pulgar row at all.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.59 | Chunk and packet agree on the mother name, but row alignment is unresolved. |
| conflict_severity | 0.78 | Wrong row selection would fabricate a parent-child relationship. |
| evidence_quality | 0.57 | Clear staged reading, dependent on conversion QA. |
| conversion_confidence | 0.37 | Mother field is not the flagged subreading, but the row conflict controls. |
| claim_probability | 0.58 | Plausible if Pulgar row is confirmed. |
| relevance | 0.96 | Direct parent-candidate question for the assigned draft. |
| canonical_readiness | 0.06 | Hold; do not promote further. |

## Required Pulgar-Line Anti-Conflation Comparison

Literal evidence from existing local wiki/staging context:

- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns not to attach Dario/Pulgar/Pulgar-Arriagada records without identity review.
- Existing staged review context treats `Dario Arturo Pulgar` in CV materials as document-level evidence requiring a bridge before attachment to `Dario Arturo Pulgar-Smith`.
- `wiki/people/dar-o-pulgar-arriagada.md` records a 5 December 2000 expropriation mention of `Dario Pulgar Arriagada`.
- Existing staged context separately mentions `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar-Arriagada`, `Dario Pulgar A.`, and adult/child `Dario Pulgar` passenger candidates.
- The assigned Entry 172 conflict draft names `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar S.`, and `Juana Arriagada de Pulgar`; it does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada in the source row itself.

Interpretation:

- Entry 172, if confirmed, would be an 1888 birth registration for a Jose/Juana Pulgar-Arriagada family unit. It does not by itself prove any same-person, parent-child, grandparent, or surname-variant bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.
- The only relevant Dario action is a future double-check after conversion QA: compare confirmed names, dates, places, parentage, and chronology against proof-reviewed Dario-line evidence. Do not merge by the shared `Pulgar` or `Arriagada` name elements.

Scores:

| comparison | identity_confidence | conflict_severity | evidence_quality | claim_probability | canonical_readiness | finding |
|---|---:|---:|---:|---:|---:|---|
| Entry 172 child/family same as `Dario Arturo Pulgar-Smith` | 0.02 | 0.86 | 0.20 | 0.02 | 0.00 | Unsupported; different given names and no bridge. |
| Entry 172 child/family same as `Dario Arturo Pulgar` CV subject | 0.02 | 0.82 | 0.20 | 0.02 | 0.00 | Unsupported; no Dario or CV evidence in this entry. |
| Entry 172 child/family same as `Dario Jose Pulgar-Arriagada` | 0.12 | 0.78 | 0.28 | 0.10 | 0.01 | Only broad Pulgar-Arriagada overlap; no Dario/Jose bridge yet. |
| Entry 172 child/family same as `Dario/Dario Pulgar Arriagada` | 0.08 | 0.78 | 0.25 | 0.08 | 0.01 | Name-family overlap only; no same-person proof. |
| Entry 172 Jose/Juana candidates as ancestors/relatives of any Dario candidate | 0.15 | 0.72 | 0.30 | 0.14 | 0.01 | Possible family-line lead only after entry QA and separate lineage proof. |

## Conflicts

- Same-person conflict: unresolved at the row level; the artifacts do not yet establish whether entry 172 is `Jose del Carmen Segundo Pulgar Arriagada` or `Jose Francisco`.
- Duplicate-person risk: high if `Jose del Carmen Pulgar S.` is silently normalized to existing `Jose del Carmen Pulgar` without confirming the row and suffix.
- Name-variant conflict: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` must remain separate literal-reading possibilities until QA.
- Relationship conflict: the Pulgar/Arriagada reading supports possible child-parent relationships, but the converted Markdown supports an unrelated Gomez/de la Cruz family. No relationship should be promoted from either side until QA resolves the row.
- Chronology conflict: the Pulgar row gives birth 8 March 1888 and registration 7 April 1888; the converted row gives birth 26 March 1888 and the same registration date. This is a different event, not a date variant for one child.
- Canonical context conflict: generated snapshots in canonical pages cite this chunk/source-packet family, but the staged conflict draft explicitly requires holding dependent claims and relationships for conversion QA.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | Entry 172 is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.61 | Hold; targeted conversion QA must verify source image, row alignment, and father field. |
| 2 | Entry 172 is the Gomez/de la Cruz birth registration for `Jose Francisco`. | 0.39 | Hold as competing artifact reading; do not stage Pulgar claims if QA confirms this. |
| 3 | Confirmed Pulgar-row father is existing `Jose del Carmen Pulgar`. | 0.48 | Do not merge; proof-review exact father-name form and compare to existing canonical page after QA. |
| 4 | Confirmed Pulgar-row mother is `Juana Arriagada de Pulgar`. | 0.58 | Do not promote further; proof-review relationship after row QA. |
| 5 | Entry 172 creates a bridge to Dario Arturo Pulgar-Smith / Dario Arturo Pulgar / Dario Jose Pulgar-Arriagada / Dario Pulgar Arriagada. | 0.02-0.15 | No bridge from this draft; preserve separate hypotheses and require a later lineage proof step. |

## Recommended Next Action

Keep the staged draft and all dependent identity, claim, relationship, and parent-candidate material at `hold_for_conversion_qa`.

Exact next proof-review or promotion step: run targeted conversion QA against `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, the assigned converted Markdown, and the current chunk. The QA note must decide whether the controlling row for entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row, and must explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` if the Pulgar row is confirmed.

After that QA, rerun proof review before any canonical claim, parent relationship, same-person merge, name-variant normalization, or Dario-line comparison is promoted. Do not merge this entry with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or any Jose/Juana parent candidate by name alone.
