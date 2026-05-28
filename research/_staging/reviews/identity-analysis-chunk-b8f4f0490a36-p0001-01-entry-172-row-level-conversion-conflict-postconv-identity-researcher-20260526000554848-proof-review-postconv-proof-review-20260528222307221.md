---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528222307221
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526000554848.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526000554848.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote identity, birth, parent, parent-child, parent-merge, or Dario-line claims from this staged draft while the converted Markdown and chunk/source-image reading still disagree.
2. The current converted Markdown is not reliable for entry 172. It assigns entry 172 to `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`, but the assigned chunk and visible page image show entry 172 as a Pulgar/Arriagada row.
3. The father field remains a narrow transcription uncertainty. The visible row supports `Jose del Carmen Pulgar` at minimum, but this proof review should not certify the trailing mark or abbreviation as `S.` without targeted conversion QA.
4. No relationship bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Darío Pulgar Arriagada` is supported by this source. The entry names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario.
5. Existing canonical Jose/Juana/Pulgar pages contain probable, draft, or family-supplied material that must remain downstream context only. This review does not make those canonical items stronger.

## Evidence Strengths

- The staged draft accurately identifies the controlling conflict: the assigned chunk/source-packet row and the current converted Markdown are not the same entry-172 family.
- The source packet states that visual review of page 58 row 172 supports the Pulgar/Arriagada row; direct review of the local page image in this proof review agrees.
- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with mother `Juana Arriagada de Pulgar`.
- The visible page image supports the broad Pulgar/Arriagada row identity and contradicts the Burgos/de la Cruz reading in the converted Markdown.
- The staged draft correctly treats Dario/Pulgar surname overlap as anti-conflation context, not relationship proof.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 4/10 overall because the current converted file is materially wrong for the assigned row; 8/10 for the chunk's broad Pulgar/Arriagada row identity after image check; 5/10 for the exact father suffix |
| evidence_quantity_score | 5/10 |
| agreement_score | 7/10 between staged draft, conflict draft, source packet, chunk, and source image; 2/10 when the current converted Markdown is included |
| identity_confidence_score | 8/10 that the visible entry 172 is the Pulgar/Arriagada row; 5/10 for exact father-name suffix; 1/10 for any Dario bridge |
| claim_probability | 0.86 that entry 172 is the Pulgar/Arriagada row; 0.10 that the converted-file Burgos/de la Cruz row controls this source image; 0.04 for a Dario identity bridge from this row alone |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged identity analysis is supported. Its main recommendation, `hold_for_conversion_qa`, is the correct handling because the repository contains a severe row-control conflict between the assigned chunk and the current converted Markdown.

The proof balance favors the Pulgar/Arriagada row for page 58 entry 172. The page image visibly aligns with the chunk/source-packet reading and not with the converted Markdown's Burgos/de la Cruz row. Even so, this review should not be used as a silent conversion repair: the source transcription boundary requires a targeted conversion QA note to certify the controlling row and exact father-field reading.

The draft's anti-conflation treatment is also supported. This row is relevant to a Pulgar/Arriagada surname cluster, but it contains no literal Dario name, no Pulgar-Smith form, no descendant chain, and no relationship bridge to the existing Dario pages.

## Next Action

Run targeted conversion QA against the source image for page 58, entry 172. The QA should explicitly decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz and should separately certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain reading. After that, run a separate claim review before promoting any child identity, birth fact, parent claim, or parent-child relationship.
