---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260527072411423
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031956113.md"
reviewed_staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031956113.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260527020803650.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_quality_score: 0.88
conversion_confidence_score: 0.45
evidence_quantity_score: 0.68
agreement_score: 0.58
identity_confidence_score: 0.76
claim_probability: 0.82
relevance_level: critical
relevance_confidence: 0.96
canonical_readiness: hold_for_conversion_qa
canonical_readiness_score: 0.14
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

- Review task id: `proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031956113.md`
- Reviewed staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031956113.md`
- Role: claim_reviewer
- Review status: hold
- canonical_readiness: hold_for_conversion_qa

## Blockers

- The active converted Markdown materially conflicts with the image-reviewed and chunk-supported row control for entry `172`. The converted file gives `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and a 6 April 1888 birth; the source image, assigned chunk, source packet, QA note, and staged conflict draft support physical row `172` as a Pulgar/Arriagada registration.
- The conflict is identity-bearing. It changes the child, parent pair, birth date/time, place/residence context, informant, and apparent page/row context, so no canonical claim or relationship should be promoted from the derivative converted file until conversion-control reconciles it.
- The father field remains bounded to `Jose del Carmen Pulgar`. The assigned chunk reads a terminal `S.`, but the source packet and targeted QA note do not certify that suffix, and this proof review does not promote it.
- No Dario identity bridge is supported by this staged draft or by the reviewed source materials. The row names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada.
- The row does not prove broader same-person identity for existing Jose or Juana candidates. `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` remain row-local parent readings unless separately bridged by a focused identity review.

## Scoring

- source_quality_score: 0.88
- conversion_confidence_score: 0.45
- evidence_quantity_score: 0.68
- agreement_score: 0.58
- identity_confidence_score: 0.76
- claim_probability: 0.82
- relevance_level: critical
- relevance_confidence: 0.96
- canonical_readiness: hold_for_conversion_qa
- canonical_readiness_score: 0.14

## Evidence Strengths

- The referenced source image is available and shows page 58 with physical row `172` on the left page. Visual review supports the Pulgar/Arriagada row-control conclusion.
- The assigned chunk transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, sex male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at Calle de Valdivia, with parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The source packet and targeted QA note independently preserve the same row-control finding while explicitly limiting the father name to `Jose del Carmen Pulgar` and flagging the suffix as unresolved.
- The staged identity-analysis draft correctly treats the Burgos/de la Cruz text as a derivative conflict rather than merging it into the Pulgar/Arriagada family evidence.

## Review Judgment

The staged identity-analysis draft is supported as a conflict analysis. The most probable local finding is that physical entry `172` in the referenced page image is the Pulgar/Arriagada birth registration, and that the active converted Markdown is stale, row-shifted, or otherwise mismatched for this task.

Canonical readiness remains low. The image, chunk, source packet, QA note, and conflict draft agree on the Pulgar/Arriagada row, but the active converted Markdown still carries an incompatible Burgos/de la Cruz entry. This proof review accepts the row-control conflict finding and the hold recommendation; it does not promote child-birth claims, parent-child relationships, parent-pair claims, suffix readings, Dario attachments, or Jose/Juana same-person merges.

## Next Action

Send to conversion-control to repair, supersede, or quarantine `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` and reconcile downstream chunk/page derivatives against the source image for page 58, physical entry `172`.

After conversion reconciliation, rerun proof review for any proposed canonical child-birth, parent-child, parent-pair, suffix, or identity-merge claim. Carry the father as `Jose del Carmen Pulgar` with the terminal mark unresolved unless a focused crop or later proof review certifies the suffix.
