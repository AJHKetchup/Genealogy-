---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528132040150
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote from the current converted Markdown. It identifies entry 172 as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the assigned chunk, source packet, conflict draft, staged identity analysis, and visible page image support a different entry-172 row for `Jose del Carmen Segundo Pulgar Arriagada`.
2. Treat this as a derivative-control conflict until conversion QA updates or supersedes the converted Markdown. The source image supports the Pulgar/Arriagada row, but the workspace still contains a contradictory converted file attached to the same source/chunk chain.
3. Do not promote any Dario, Arturo, Smith, Dario Jose, or public-role Pulgar-Arriagada bridge. The checked row names only the child, parents, and informant for this birth registration.
4. Do not silently normalize the father's suffix. The row visibly supports `Jose del Carmen Pulgar` and appears consistent with a final `S.`, but the staged analysis is correct that the suffix should be certified by targeted conversion QA before being used as a canonical literal.

## Evidence Strengths

- The visible source image for page 58, entry 172 aligns with the assigned chunk's row, including `Jose del Carmen Segundo Pulgar Arriagada`, `Ocho de Marzo`, `Calle de Valdivia`, father `Jose del Carmen Pulgar ...`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The staged conflict draft and source packet accurately identify the contradiction between the current converted Markdown and the chunk/source-packet reading.
- The staged identity analysis correctly keeps row-control/conversion-control separate from same-person, duplicate-person, and name-variant conclusions.
- The source type is a civil birth registration and is strong direct evidence for a birth event and named parents once the transcription control issue is resolved.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 4/10 overall because the current converted Markdown conflicts with the chunk; 8/10 for the narrow visible-image support of the Pulgar/Arriagada entry-172 row |
| evidence_quantity_score | 4/10 |
| agreement_score | 7/10 among source image, chunk, source packet, conflict draft, and identity analysis; 3/10 if the current converted Markdown is included as controlling derivative text |
| identity_confidence_score | 7/10 for the narrow birth-registration identity `Jose del Carmen Segundo Pulgar Arriagada`; 6/10 for parent names within this row; 1/10 for any Dario-related identity bridge |
| claim_probability | 0.88 that the visible entry 172 is the Pulgar/Arriagada row; 0.82 for the child birth-registration claim after conversion QA; 0.75 for the parent-name claims pending father suffix certification; 0.03 for any Dario/Arturo/Smith identity or relationship bridge |
| relevance_level | high for Pulgar/Arriagada birth-registration review; low for Dario-bridge claims |
| relevance_confidence | 0.90 for the Pulgar/Arriagada family-line lead; 0.15 for Dario-bridge use |
| canonical_readiness | hold; revise/QA before canonical promotion |

## Review Finding

The staged identity analysis is substantially supported as a hold against canonical promotion, but its strongest reason is now narrower: visual review of the referenced page image supports the Pulgar/Arriagada row for entry 172, while the current converted Markdown appears to be the conflicting derivative. This does not authorize editing the converted file in this task and does not make the claims canonical-ready.

The claim set should be held or revised, not promoted. A later QA note may certify the row as a direct birth-registration source for `Jose del Carmen Segundo Pulgar Arriagada`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with mother `Juana Arriagada de Pulgar`, father `Jose del Carmen Pulgar [S./?]`, and informant `Ernesto Herrera L.`. Until then, all dependent parent-child relationships and identity merges remain blocked.

No checked evidence supports connecting this row to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or `Dario Pulgar A.`.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` and record that the visible source image supports the Pulgar/Arriagada entry-172 row unless QA finds a page-control reason not visible here. Certify the father's literal field to the visible level before any canonical birth or parent-child claim is promoted.
