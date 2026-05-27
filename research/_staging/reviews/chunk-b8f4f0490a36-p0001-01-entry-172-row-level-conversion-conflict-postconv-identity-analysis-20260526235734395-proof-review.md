---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527021143834
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526235734395.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526235734395.md
reviewed_subject: "Entry 172, Los Angeles birth register, 1888"
reviewed_claim_type: identity_conflict_analysis
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
source_page_image_checked: true
source_quality_score: 0.88
conversion_confidence_score: 0.70
evidence_quantity_score: 0.78
agreement_score: 0.73
identity_confidence_score: 0.82
claim_probability: 0.86
relevance_level: high
relevance_confidence: 0.96
canonical_readiness: hold_for_conversion_reconciliation
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- Canonical readiness is `hold_for_conversion_reconciliation`. The source image, assigned chunk, source packet, and targeted QA note support the Pulgar/Arriagada row as physical entry `172`, but the referenced converted Markdown still records a different Burgos/de la Cruz row for entry `172`.
- The conflict is whole-row evidence, not a spelling variant. The child, parents, birth details, place, and declarant in the converted Markdown do not match the physical row visible on page 58.
- The father field is supported only as `Jose del Carmen Pulgar` for promotion purposes. The assigned chunk's trailing `S.` remains an unresolved mark or suffix unless a later paleographic review certifies it from the image.
- This entry does not support any same-person, duplicate-person, lineage, or relationship bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Dario Pulgar Arriagada. Any Dario attachment from this row would be a relationship jump.
- This review did not edit raw sources, converted Markdown, chunks, source packets, or canonical wiki pages. It verifies the staged conflict analysis only.

## Evidence Strengths

- The referenced source image was available and visually checked. Entry `172` on left page 58 visibly corresponds to the Pulgar/Arriagada row, not the Burgos/de la Cruz row in the converted Markdown.
- The assigned chunk transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, with birth on 8 March 1888 at about 3 p.m. at Calle de Valdivia, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and declarant `Ernesto Herrera L.`.
- The targeted conversion QA note independently records the same row structure and appropriately limits the father reading to `Jose del Carmen Pulgar`, preserving the suffix question.
- The staged identity analysis accurately treats the Burgos/de la Cruz reading as a derivative conversion conflict rather than a name variant or alternate identity for the Pulgar/Arriagada child.
- The anti-conflation findings are well supported: the entry names Jose del Carmen Segundo Pulgar Arriagada and his recorded parents, but it does not name or bridge any Dario-line person.

## Scored Judgment

- `source_quality_score: 0.88` - civil birth registration is a strong primary source class, and the source image is available; reduced slightly for image legibility and row-level paleography limits.
- `conversion_confidence_score: 0.70` - the assigned chunk and targeted QA note agree with the image, but the canonical converted Markdown remains materially mismatched.
- `evidence_quantity_score: 0.78` - one source image plus the referenced chunk, source packet, conversion QA note, converted file, and staged identity analysis were reviewed; sufficient for conflict judgment, not for broader identity linkage.
- `agreement_score: 0.73` - image, chunk, source packet, and QA note agree on the Pulgar/Arriagada row; the converted Markdown is the major opposing derivative.
- `identity_confidence_score: 0.82` - confidence is high that physical entry `172` is the Pulgar/Arriagada birth row, but father suffix and derivative-file reconciliation keep this below ready-for-canonical status.
- `claim_probability: 0.86` - the staged identity analysis's main claim, that the physical row controls as Pulgar/Arriagada while the converted Markdown conflicts, is probable.
- `relevance_level: high`; `relevance_confidence: 0.96` - the row directly affects Pulgar/Arriagada identity and parent-child evidence, and also functions as anti-conflation context for Dario-line work.
- `canonical_readiness: hold_for_conversion_reconciliation`.

## Review Judgment

The staged identity/conflict analysis is supported as a proof-reviewed hold note. Its main conclusion is sound: physical entry `172` on register page 58 should be treated in staging as the Pulgar/Arriagada row, while the Burgos/de la Cruz entry in the converted Markdown must remain a known derivative conflict until corrected or explicitly superseded by a conversion-control process.

The bounded claim `Jose del Carmen Pulgar` as recorded father is supported. The expanded reading `Jose del Carmen Pulgar S.` is not ready for promotion from this review. `Juana Arriagada de Pulgar` is supported as the recorded mother for this entry, but this does not prove identity with any separate Juana candidate.

## Next Action

Keep the staged analysis on hold for conversion reconciliation. A conversion-control worker should either correct or formally supersede the stale converted Markdown, preserve the derivative mismatch in audit history, and keep the father suffix unresolved unless a targeted image reread certifies it. After that, rerun promotion only for narrow Entry 172 facts and relationships; do not attach this row to Dario-line identities without separate direct bridge evidence.
