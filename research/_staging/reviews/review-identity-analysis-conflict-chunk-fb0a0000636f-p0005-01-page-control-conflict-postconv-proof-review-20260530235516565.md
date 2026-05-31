---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530235516565
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530232549577.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530232549577.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530224457988.md
reviewed_conflict_candidate: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530224457988.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
page_reference: page 5
review_status: hold
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: CV Page 5 Control Conflict

## Blockers

1. The reviewed staged draft is `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530232549577.md`.
2. Page control is not resolved. The assigned chunk transcribes page 5 as a 1979-1970 career sequence beginning with HABITAT in Nairobi, while the conversion-job page Markdown transcribes page 5 as a 1999-1997 sequence beginning with PROFONANPE in Peru.
3. The aggregate converted file currently contains both incompatible sequences: the 1999-1997 section under page 5 and the 1979-1970 chunk text later in the same aggregate. This confirms internal derivative disagreement, not a stable source reading.
4. The conversion job manifest references `page-images/page-0005.jpg`, but that image file was not present when checked. I did not regenerate images, rerun conversion, or edit derivative outputs.
5. Hash control is unstable. The chunk manifest records `fb0a0000636f...` for the converted file, while the observed converted-file hash is `da9ec0c3...`; the observed chunk hash is `d6ea4f61...`, differing from manifest entries.
6. Page 5, in the reviewed derivatives, does not independently state `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, parent names, spouse names, child names, or any family relationship.

## Evidence Scoring

| category | score | rationale |
|---|---:|---|
| source_quality_score | 0.56 | A CV is a useful self/administrative career source, but this review relied on conflicted local derivatives because the rendered page image is absent. |
| conversion_confidence_score | 0.16 | Page-markdown, aggregate converted text, chunk content, and manifest/hash state disagree materially. |
| evidence_quantity_score | 0.62 | There is enough derivative evidence to prove a page-control conflict, but not enough stable evidence to prove either career sequence. |
| agreement_score | 0.14 | The controlling page-5 text is contradicted across local derivatives. |
| identity_confidence_score | 0.58 | Document-level title supports a Dario Arturo Pulgar attribution, but the page body is not independently identity-bearing. |
| claim_probability | 0.94 | The claim that page-5 facts must remain held for conversion QA is strongly supported. |
| relevance_level | high | The conflict directly controls whether page-5 career facts can be used at all. |
| relevance_confidence | 0.98 | All reviewed local files point to this same page-control issue. |
| canonical_readiness | hold_for_conversion_qa | No canonical claim, relationship, or identity merge should be promoted from this page until source-page QA resolves the controlling transcription. |

## Claim Judgments

| reviewed claim or hypothesis | probability | judgment |
|---|---:|---|
| Page-5 claims must remain held until conversion QA selects the controlling text. | 0.94 | Supported. This is the only review-ready conclusion. |
| The page belongs to document-level CV subject `Dario Arturo Pulgar`. | 0.68 | Plausible at document level from the source title and conversion title, but not page-local proof. |
| `Dario Arturo Pulgar` is the same person as `Dario Arturo Pulgar-Smith`. | 0.42 | Not proven in the reviewed page-control evidence. Requires a separate identity bridge. |
| Same person as `Dario Jose Pulgar-Arriagada` or `Dario/Dario Pulgar Arriagada`. | 0.08 | Not supported by this page. Treat as anti-conflation only. |
| Relationship to Jose/Juana parent candidates. | 0.03 | Not supported by this page. No relationship language appears in the reviewed derivatives. |

## Evidence Strengths

- The staged draft accurately identifies the controlling problem: the assigned chunk and the conversion-job page Markdown are mutually incompatible for page 5.
- The reviewed source packet explicitly documents the same conflict and recommends `hold_for_conversion_qa`.
- The reviewed conflict candidate is conservatively scoped and does not attempt to promote either work-history sequence.
- The staged draft correctly separates document-level attribution from page-local identity proof and relationship proof.

## Review Notes

- Literal support is adequate for a conflict/hold note, not for extracted career facts.
- Uncertainty is high because the absent rendered page image prevents direct visual verification in this task.
- Source reliability cannot overcome conversion-control failure; even if the PDF is likely a useful CV source, the current derivative layer is unstable.
- Relationship jumps are blocked: no parent, spouse, child, grandchild, or Alexander John Heinz relationship is stated in the reviewed page-5 derivatives.
- Identity risk is material because attaching an unresolved page-5 chronology to a canonical person could merge career evidence across distinct Pulgar name forms without page-local proof.

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. The next worker should restore or recheck the physical source page/page image for page 5, determine whether the 1999-1997 text or the 1979-1970 text is the controlling transcription, and repair the manifest/hash drift before any canonical claim, relationship, identity merge, or wiki update is considered.
