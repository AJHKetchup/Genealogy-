---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260527203121681
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-control-held-postconv-evidence-extraction-20260526172400000.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-control-held-postconv-evidence-extraction-20260526172400000.md"
reviewed_at: "2026-05-27"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers

- The referenced source image path in the staged draft and manifest does not resolve in this workspace: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.
- The manifest page image path also does not resolve: `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png`.
- The converted Markdown and assigned chunk materially disagree for entry 172. The converted file records a Burgos/de la Cruz row; the chunk records a Pulgar/Arriagada row. Because the image is unavailable for this review, the Pulgar/Arriagada reading cannot be independently certified here.
- Do not promote the child identity, birth facts, parent-child relationships, parent identity links, or any Dario-line comparison from this draft until targeted conversion QA resolves the row-control conflict against the visible source image.

## Evidence Strengths

- The staged draft accurately reports the conflict between the converted Markdown and the assigned chunk.
- The assigned chunk and source packet are internally consistent: both identify entry 172 as Jose del Carmen Segundo Pulgar Arriagada, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at Calle de Valdivia, with father Jose del Carmen Pulgar S. and mother Juana Arriagada de Pulgar.
- The current converted Markdown and page-level conversion job Markdown are internally consistent with each other but conflict with the chunk/source packet: both record entry 172 as Jose Miguel, born 6 April 1888 at about 10 p.m., child of Oswaldo Burgos and Concepcion de la Cruz.
- The staged draft properly avoids using this birth entry as proof that Jose del Carmen Segundo Pulgar Arriagada is Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Dario Pulgar Arriagada.

## Scored Judgment

- source_quality_score: 0.88
  - Civil birth registration is a strong original-source class, but the source image was unavailable to this reviewer.
- conversion_confidence_score: 0.20
  - The conversion/chunk conflict is severe and affects the controlling row for entry 172.
- evidence_quantity_score: 0.45
  - There are multiple derivative workspace artifacts, but only one underlying source page and no accessible image for independent verification.
- agreement_score: 0.25
  - The assigned chunk agrees with the source packet, while the converted file agrees with the page-level conversion Markdown; the two artifact sets disagree on every core identity fact for entry 172.
- identity_confidence_score: 0.30
  - Confidence that this draft identifies a real row-control conflict is high, but confidence in the Pulgar/Arriagada identity as the canonical entry 172 reading remains limited without the image.
- claim_probability: 0.60
  - It is more likely than not that a conversion conflict exists because the referenced workspace artifacts directly disagree. The probability that the Pulgar/Arriagada row is the correct source reading is not certified in this review.
- relevance_level: high
  - If certified, the Pulgar/Arriagada row would be directly relevant to the Pulgar/Arriagada family and birth/parentage claims.
- relevance_confidence: 0.80
  - Relevance is clear from the names and relationship fields in the chunk/source packet, subject to row-control resolution.
- canonical_readiness: hold_for_conversion_qa

## Review Decision

Hold. The staged draft's cautious recommendation is supported: this should remain a conversion-QA item, not a canonical claim or relationship source. The current review verifies the existence of a material internal conflict but cannot certify the visible-source reading because the source image and manifest page image are unavailable in the expected locations.

## Next Action

Targeted conversion QA should restore or locate the source/page image matching SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, compare the visible entry 172 row against the converted Markdown and assigned chunk, and then issue a corrected conversion or explicit QA note. The father field should be recorded only as far as the image supports, such as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
