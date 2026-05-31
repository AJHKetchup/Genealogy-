---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530235954179
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530232549577.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530232549577.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530224457988.md
reviewed_conflict_candidate: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530224457988.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
reviewed_conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
page_reference: page 5
source_quality_score: 0.54
conversion_confidence_score: 0.15
evidence_quantity_score: 0.61
agreement_score: 0.14
identity_confidence_score: 0.56
claim_probability: 0.94
relevance_level: high
relevance_confidence: 0.98
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: CV Page 5 Control Conflict

Reviewed staged draft: `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530232549577.md`

## Blockers

1. Page control is unresolved. The assigned chunk for `CHUNK-fb0a0000636f-P0005-01` gives a 1979-1970 work-history sequence beginning with HABITAT in Nairobi; the conversion-job `page-markdown/page-0005.md` gives a different 1999-1997 sequence beginning with PROFONANPE in Peru.
2. The aggregate converted file contains both incompatible page-5 derivative texts in different positions, so it cannot be treated as a stable controlling transcription.
3. The source manifest references `page-images/page-0005.jpg`, but that image file was not present when checked. This review did not regenerate images, rerun conversion, or edit derivative outputs.
4. Provenance control is unstable. The chunk metadata records converted SHA-256 `fb0a0000636f...`, while the observed converted-file hash is `DA9EC0C3A0F604B4C0E827A2A733A0BA013DD60D86ABEA2B46490D9F8820D288`; the observed chunk hash is `D6EA4F611EE03000C11CBBA63246E95B55F8A421FCBC87D0D667E91F5C8D0B8D`, which differs from manifest entries.
5. The reviewed page-5 derivatives do not independently state `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, Jose/Juana parent candidates, Alexander John Heinz, or any parent/spouse/child/grandchild relationship.

## Evidence Scoring

| metric | score / value | rationale |
|---|---:|---|
| source_quality_score | 0.54 | A CV can be a useful career and identity-context source, but this review could only inspect conflicted derivatives because the rendered page image is absent. |
| conversion_confidence_score | 0.15 | Competing page-5 transcriptions, duplicate/conflicting manifest data, hash drift, and a missing page image block reliance on the current conversion layer. |
| evidence_quantity_score | 0.61 | The local artifacts are sufficient to prove a page-control conflict, but insufficient to prove either work-history sequence as the physical page-5 text. |
| agreement_score | 0.14 | The assigned chunk, page-markdown, aggregate converted file, and manifest/hash state materially disagree. |
| identity_confidence_score | 0.56 | The source title supports document-level relevance to Dario Arturo Pulgar, but the reviewed page body lacks independent identity or relationship anchors. |
| claim_probability | 0.94 | The staged draft's hold/page-control-conflict conclusion is strongly supported. Any promoted career or relationship claim from page 5 remains low probability. |
| relevance_level | high | The issue directly controls whether page-5 CV facts can be used in later identity or career analysis. |
| relevance_confidence | 0.98 | The staged draft, source packet, conflict candidate, chunk, and page-markdown all point to the same control problem. |
| canonical_readiness | hold_for_conversion_qa | No canonical claim, relationship, merge, or wiki edit is ready from this evidence. |

## Claim Judgments

| reviewed claim or hypothesis | probability | judgment |
|---|---:|---|
| Page-5 claims must remain held until conversion QA selects the controlling transcription. | 0.94 | Supported. This is the only review-ready conclusion. |
| The assigned 1979-1970 chunk is the controlling physical page-5 transcription. | 0.31 | Hold. It is explicit and legible as a derivative, but conflicts with page-markdown and aggregate text. |
| The 1999-1997 page-markdown text is the controlling physical page-5 transcription. | 0.33 | Hold. It is explicit and legible as a derivative, but conflicts with the assigned chunk and aggregate duplication. |
| The page belongs to document-level CV subject `Dario Arturo Pulgar`. | 0.68 | Plausible from source title and conversion title, but not page-local identity proof. |
| `Dario Arturo Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith`. | 0.40 | Not proven here. Requires separate identity-bridge proof after conversion QA. |
| Same person as `Dario Jose Pulgar-Arriagada` or `Darío/Dario Pulgar Arriagada`. | 0.08 | Not supported by this page-control evidence; treat only as anti-conflation context. |
| Relationship to Jose/Juana parent candidates or Alexander John Heinz. | 0.02 | Unsupported. No relationship language appears in the reviewed page-5 derivatives. |

## Evidence Strengths

- The staged draft accurately identifies the controlling conflict and does not choose between the incompatible derivative transcriptions.
- The reviewed source packet and conflict candidate independently recommend `hold_for_conversion_qa`.
- Both competing derivative texts are substantial, coherent CV work-history text, making the conflict a provenance/page-control issue rather than a simple isolated typo.
- The draft correctly separates document-title attribution from page-local identity proof and from family relationship proof.

## Next Action

Keep this staged draft on `hold_for_conversion_qa`. The next action is conversion QA: restore or recheck the physical page-5 rendering/PDF page, determine whether the 1999-1997 text or the 1979-1970 text is the controlling transcription, and repair the manifest/hash drift before any career claim, identity bridge, relationship claim, or canonical wiki update is considered.
