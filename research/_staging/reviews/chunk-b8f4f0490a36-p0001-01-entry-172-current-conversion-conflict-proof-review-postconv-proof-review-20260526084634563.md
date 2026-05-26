---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526084634563
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045206977.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045206977.md
reviewed_source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md
reviewed_conflict_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md
reviewed_converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
reviewed_chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
reviewed_page_image: raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png
created: 2026-05-26
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- The staged identity analysis is correctly held. The assigned chunk and source packet read entry `172` as a Pulgar/Arriagada birth registration, while the current converted Markdown for the same converted file and entry number reads a Burgos/de la Cruz birth registration for `Jose Miguel`.
- This is a row-level derivative conflict, not a spelling, accent, or name-variant issue. The competing readings disagree on child identity, sex wording, birth date/time, birth place, father, mother, informant, and residence fields.
- The visible page image broadly favors the assigned chunk's Pulgar/Arriagada row for entry `172`, but this proof review is not a conversion-QA correction pass and must not rewrite the converted Markdown or certify a corrected transcript.
- The father field remains unresolved for canonical use. Preserve the alternatives `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted conversion QA certifies the visible reading.
- No Dario-line identity bridge is supported by this record. The reviewed evidence does not name `Dario`, `Arturo`, `Smith`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.

## Evidence Reviewed

- Staged identity analysis: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045206977.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md`.
- Conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Current chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced page image: `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png`.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration is a strong direct source class for birth and parent-name claims; the page image is usable for row-level review. |
| conversion_confidence_score | 0.34 | The conversion derivatives materially disagree for the same source and entry number, so canonical conversion confidence is low despite the image and chunk alignment. |
| evidence_quantity_score | 0.64 | There is one direct page image plus two conflicting derivative transcriptions and staged analysis; quantity is enough to diagnose conflict, not enough to promote. |
| agreement_score | 0.42 | Source packet, conflict draft, staged identity analysis, chunk, and visible image broadly agree with the Pulgar/Arriagada row, but the current converted Markdown gives a different entry. |
| identity_confidence_score | 0.62 | `Jose del Carmen Segundo Pulgar Arriagada` is plausible as the entry-172 child if the chunk controls; identity confidence is capped by the unresolved derivative conflict. |
| claim_probability | 0.68 | It is more likely than not that entry `172` is the Pulgar/Arriagada row shown in the chunk/image, but the proof standard is not met until conversion QA reconciles the derivatives. |
| relevance_level | high | If confirmed, the row directly concerns Pulgar/Arriagada family identity and parent-child relationships. |
| relevance_confidence | 0.86 | The Pulgar and Arriagada terms are explicit in the chunk and visible enough in the image; relevance drops only if the converted Markdown is later found to be controlling. |
| canonical_readiness | hold_for_conversion_qa | Do not promote claims, relationships, merges, or wiki edits until targeted conversion QA resolves the row and father-field reading. |

## Evidence Strengths

- The assigned chunk gives a coherent entry-172 row naming `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The source packet and conflict draft accurately describe the derivative mismatch and correctly recommend `hold_for_conversion_qa`.
- The page image broadly matches the assigned chunk's row structure for entry `172`, including the Pulgar/Arriagada names, making the staged hold conclusion well supported.
- The staged identity analysis appropriately avoids a Dario-line merge or bridge and treats existing canonical stubs as derivative context, not independent confirmation.

## Relationship And Identity Risk

- Parent-child relationships from this row are probable but blocked. Do not promote `Jose del Carmen Pulgar S.` or `Juana Arriagada de Pulgar` as parents of `Jose del Carmen Segundo Pulgar Arriagada` until conversion QA resolves the row.
- Do not normalize the father to `Jose del Carmen Pulgar` or create a suffix-free canonical attachment from this review. The visible source must control the final father-field form.
- Do not attach this entry to any Dario identity. The record lacks direct name, chronology, relationship, occupation, spouse, descendant, or place-bridge evidence for such a jump.

## Next Action

Keep the staged identity analysis at `hold_for_conversion_qa`. The next worker should run targeted conversion QA against `CHUNK-b8f4f0490a36-P0001-01`, comparing the page image, current converted Markdown, current chunk, and source packet, then certify whether entry `172` is the Pulgar/Arriagada row or the Burgos/de la Cruz row and preserve/correct the father-field reading. After QA, rerun proof review before any canonical claim, relationship, merge, or wiki-page update.
