---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260527015353808"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526235734395.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526235734395.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md"
reviewed_conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: "hold_for_conversion_reconciliation"
created: 2026-05-27
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- The staged draft is supported as a conflict and identity-risk analysis, but it is not promotion-ready as a canonical claim set. The current converted Markdown still records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the source image, assigned chunk, source packet, and targeted QA note support physical entry `172` as the Pulgar/Arriagada row.
- The derivative conversion conflict is material. It changes the child, parents, birth date, birth place, residence details, and declarant, so canonical promotion should wait until the converted Markdown mismatch is retained as a known derivative error or reconciled through the conversion-control process.
- The father field should remain bounded to `Jose del Carmen Pulgar` for promotion purposes. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the targeted QA note certifies only `Jose del Carmen Pulgar`; the visible image does not make the suffix safe enough to promote here.
- No same-person, lineage, or relationship bridge to any Dario-line person is supported by this entry. Any attachment to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, or `Darío/Dario Pulgar Arriagada` would be an unsupported identity jump.
- `Juana Arriagada de Pulgar` should not be merged with `Juana de Dios Amagada de Pulgar` from this evidence. This entry supports the recorded mother name only for this child and does not resolve the separate Juana candidate.

## Scores

- source_quality_score: 0.88
- conversion_confidence_score: 0.62
- evidence_quantity_score: 0.68
- agreement_score: 0.72
- identity_confidence_score: 0.84 for the bounded Pulgar/Arriagada row-control conclusion; 0.10 for any Dario identity bridge.
- claim_probability: 0.87 that physical entry `172` is the Pulgar/Arriagada row; 0.76 that the father can be cited as `Jose del Carmen Pulgar`; 0.06 that this entry identifies or bridges to a Dario-line person.
- relevance_level: high for Pulgar/Arriagada row-control and anti-conflation; low-to-moderate for Dario-line research lead value only.
- relevance_confidence: 0.91
- canonical_readiness: hold_for_conversion_reconciliation

## Evidence Strengths

- The original image is a primary civil birth register page. Physical entry `172` on page 58 visibly aligns with the chunk and targeted QA note: `Jose del Carmen Segundo Pulgar Arriagada`, male, born on 8 March 1888 at 3 p.m. at Calle de Valdivia, with parents recorded as `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
- The targeted QA note directly addresses the row-control problem and appropriately downgrades the father suffix from the chunk's `Pulgar S.` reading to the certified `Jose del Carmen Pulgar`.
- The staged identity analysis correctly frames the Burgos/de la Cruz material as a derivative conversion mismatch rather than as a name variant or duplicate-person problem.
- The staged draft's anti-conflation conclusions are well supported: this source does not name Dario, Arturo, Smith, spouse, child, later residence, public office, or any other bridging evidence to the Dario clusters.

## Next Action

Hold canonical promotion until conversion reconciliation records how the Burgos/de la Cruz converted Markdown conflict will be handled. After that, promote only narrowly scoped Entry 172 facts supported by the image-reviewed row and the QA-certified father reading `Jose del Carmen Pulgar`; do not promote the `S.` suffix, merge Juana candidates, or attach any Dario-line identity without a separate direct bridge.
