---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527233542846
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-postconv-identity-analysis-20260527222753668.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-postconv-identity-analysis-20260527222753668.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-rowcert-postconv-evidence-extraction-20260527221218880.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-postconv-evidence-extraction-20260527221218880.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Derivative Row Conflict

## Blockers First

- Canonical readiness remains `hold`. The visible source image, assigned chunk, source packet, and conflict draft support physical entry `172` as the Pulgar/Arriagada birth registration, but the current converted Markdown for the same source path still labels entry `172` as a Burgos/de la Cruz row.
- The converted Markdown is therefore not safe as the controlling derivative for this entry until conversion-control reconciles, supersedes, or explicitly annotates the row-control conflict.
- The father should remain bounded as `Jose del Carmen Pulgar` in any downstream claim review. The visible/chunk reading may include a trailing mark or `S.`, but this proof review does not certify a suffix.
- The staged identity analysis correctly refuses a direct bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. No Dario/Smith identity evidence is visible in this entry.
- No Jose/Juana parent merge is ready. This review verifies row control and literal support for this entry only; it does not prove cross-record identity for existing Jose or Juana candidates.

## Evidence Strengths

- The referenced page image is a civil birth register image and is the strongest source for row control. On page 58, physical row `172` visibly contains the Pulgar/Arriagada child entry, not the Burgos/de la Cruz row shown in the current converted Markdown.
- The assigned chunk transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered `Siete de Abril de mil ochocientos ochenta i ocho`, born `Ocho de Marzo de mil ochocientos ochenta i ocho` at about three in the afternoon, place `Calle de Valdivia`.
- The assigned chunk and source packet agree on the core parent readings: father `Jose del Carmen Pulgar` with unresolved possible trailing mark, and mother `Juana Arriagada de Pulgar`.
- The conflict draft accurately preserves the competing derivative reading: converted Markdown entry `172` gives `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- The staged identity analysis keeps interpretation separate from transcription and treats Dario-related comparisons as unsupported identity-bridge hypotheses.

## Scored Judgment

| Review dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.91 | Civil registration image is direct evidence for the birth-registration row; image quality is sufficient for row control and core names, though handwriting and crop scale limit suffix certainty. |
| conversion_confidence_score | 0.72 | High confidence in the assigned chunk/source-packet row control, reduced by the unreconciled converted Markdown conflict and unresolved father suffix. |
| evidence_quantity_score | 0.70 | One direct source image plus one assigned chunk, one source packet, one conflict draft, and one conflicting converted derivative. Adequate for row-control review, not enough for broader identity merging. |
| agreement_score | 0.64 | Image, chunk, source packet, and conflict draft agree with each other; current converted Markdown materially disagrees. |
| identity_confidence_score | 0.90 | High confidence that physical entry 172 concerns `Jose del Carmen Segundo Pulgar Arriagada`; low confidence for any bridge beyond this child-parent row. |
| claim_probability | 0.92 | The claim that physical entry 172 is the Pulgar/Arriagada birth row is strongly probable from visible row control. |
| relevance_level | high | The row is directly relevant to Pulgar/Arriagada family evidence and to preventing a wrong Burgos/de la Cruz attachment. |
| relevance_confidence | 0.98 | Pulgar and Arriagada are visible/transcribed in the relevant row and match the staged family-relevance terms. |
| canonical_readiness | hold | Core row-control claim is review-supported, but canonical use should wait for conversion-control reconciliation or an explicit superseding note. |

## Claim-Level Findings

| Claim or hypothesis | Probability | Review result |
| --- | ---: | --- |
| Physical entry `172` is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.92 | Supported for review purposes; hold pending derivative reconciliation. |
| Converted Markdown entry `172` Burgos/de la Cruz row controls this task. | 0.07 | Not supported by the visible page image for this staged task; preserve only as the conflicting derivative. |
| Father is safely staged as `Jose del Carmen Pulgar`. | 0.88 | Supported with boundary. Do not promote a suffix or trailing initial from this review. |
| Mother is `Juana Arriagada de Pulgar` in this entry. | 0.88 | Supported by image/chunk/source packet for this row. Do not normalize to other Juana variants here. |
| This entry directly bridges to Dario Arturo/Dario Jose/Dario Pulgar candidates. | 0.03 | Unsupported. The staged draft is correct to block such a bridge. |
| This row proves existing Jose/Juana wiki candidates are duplicates or the same people. | 0.35 | Plausible future comparison context only; not proved by this row-control review. |

## Reliability And Risk

- Source reliability is strong because the page image is a contemporaneous civil birth register page, not a later compiled index.
- Conversion reliability is mixed: the assigned chunk appears aligned to the visible page image, while the current converted Markdown is materially misaligned for entry numbers and family rows.
- Identity risk is high if the converted Markdown is used uncritically, because it would attach Burgos/de la Cruz parents to the wrong task entry.
- Relationship risk is high for any promoted child-parent relationship until the derivative conflict is carried forward or resolved.
- Claim confidence is high for the physical row being Pulgar/Arriagada and low for any broader Dario or Jose/Juana merge inference.

## Next Action

1. Keep this staged identity analysis on `hold`, not promoted, until conversion-control reconciles or supersedes the conflicting converted Markdown.
2. If conversion-control accepts the image-reviewed row control, proceed to proof-review atomic claims for child name, sex, birth date/time/place, registration date, father name bounded to `Jose del Carmen Pulgar`, mother name, and informant.
3. Run separate targeted identity reviews for Jose/Juana parent candidates only after the row-control conflict is settled.
4. Keep all Dario candidates separate unless a later direct bridge source supplies explicit identity or lineage evidence.
