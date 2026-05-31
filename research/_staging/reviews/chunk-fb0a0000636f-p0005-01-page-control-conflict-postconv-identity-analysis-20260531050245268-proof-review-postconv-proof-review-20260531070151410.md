---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531070151410
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531050245268.md"
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531050245268.md
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260531040158454.md
conflict_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531040158454.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
source_quality_score: 0.25
conversion_confidence_score: 0.15
evidence_quantity_score: 0.35
agreement_score: 0.20
identity_confidence_score: 0.30
claim_probability: 0.90 for page-control conflict; 0.20 for promotion-ready page-5 work-history attachment; 0.10 for same-person or relationship claims
relevance_level: high
relevance_confidence: 0.80
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

This review covers staged draft `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531050245268.md`.

## Blockers First

1. Page control is unresolved. The assigned chunk transcribes a 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO sequence ending with `EDUCATION`. The conversion-job `page-markdown/page-0005.md` transcribes a different 1999 PROFONANPE/TVE, 1998-1999 Arca Consulting/European Commission, and 1997-1998 Klohn Crippen/SNC Lavalin sequence.
2. The controlling physical source could not be checked in this workspace. `raw/sources/CV of Dario Arturo Pulgar.pdf`, the manifest's local staged source PDF, and `page-images/page-0005.jpg` are absent at the expected paths.
3. Provenance metadata is unstable. The source packet records a mismatch between the converted SHA recorded in the chunk and the observed converted-file SHA, and the chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` with conflicting metadata.
4. The reviewed page-local text does not name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar`. Subject attachment relies only on source title/document continuity.
5. No same-person merge, name-variant normalization, family relationship, education claim, or occupational chronology claim is ready for canonical promotion from this page-5 evidence.

## Evidence Strengths

- The staged draft is well supported as a hold recommendation. Direct inspection confirms that the assigned chunk and conversion-job page Markdown contain materially different page-5 derivative transcriptions.
- The source packet and conflict draft consistently identify the same dispute: missing controlling page image/source, duplicate chunk manifest entries, hash drift, and a page-control conflict.
- Both derivative readings are internally plausible CV work-history text from a document titled as the CV of `Dario Arturo Pulgar`; this supports relevance to a Pulgar biography review, but not canonical attachment.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.25 | CV source context is potentially useful, but the source PDF and page image are unavailable for this review. |
| conversion_confidence_score | 0.15 | Two page-5 derivative readings conflict and the manifest/hash state is unstable. |
| evidence_quantity_score | 0.35 | Enough derivative evidence exists to prove a conflict; not enough controlled evidence exists to prove the page's occupational facts. |
| agreement_score | 0.20 | Source packet, conflict draft, and staged identity analysis agree on hold status, but the underlying transcriptions disagree. |
| identity_confidence_score | 0.30 | Document title supports possible CV-subject continuity; page-local text does not name the person. |
| claim_probability | 0.90 conflict; 0.20 occupational attachment; 0.10 merge/relationship | The page-control conflict is highly probable. Specific page-5 work-history and identity/relationship claims are not proof-ready. |
| relevance_level | high | A CV of Dario Arturo Pulgar is relevant to Pulgar identity work if page control is repaired. |
| relevance_confidence | 0.80 | Relevance follows from the document title and CV context, with reduced confidence because page control is unresolved. |
| canonical_readiness | blocked | Conversion QA and identity-bridge review are required before canonical use. |

## Claim Probability Notes

- `0.90`: The staged draft's claim that a serious page-control/provenance conflict exists is supported.
- `0.35`: The broad hypothesis that the disputed page belongs somewhere in the `CV of Dario Arturo Pulgar` conversion context is plausible from document title/path continuity.
- `0.20`: Any specific page-5 work-history claim is currently too unstable for canonical promotion because the controlling physical page is not certified.
- `0.10`: Same-person claims linking `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or `Darío/Dario Pulgar Arriagada` are unsupported by this page-local evidence.
- `0.02`: Relationship claims involving `Jose del Carmen Pulgar` or `Juana Arriagada de Pulgar` are unsupported by this page-local evidence.

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. Restore or regenerate the source PDF/page image, reconcile the duplicate chunk manifest entries and hash drift, and certify the controlling page-5 transcription. After that, rerun proof review on any surviving work-history claim and run a separate identity-bridge proof review before attaching CV claims to any canonical person page.
