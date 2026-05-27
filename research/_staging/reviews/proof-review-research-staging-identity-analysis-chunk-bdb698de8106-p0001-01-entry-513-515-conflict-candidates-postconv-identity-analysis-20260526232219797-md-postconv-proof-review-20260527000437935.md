---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527000437935
task_id: proof-review:research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526232219797.md
staged_draft: research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526232219797.md
source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526232219797.md
conflict_candidates: research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526232219797.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
reviewed: 2026-05-27
source_quality_score: 0.86
conversion_confidence_score: 0.38
evidence_quantity_score: 0.46
agreement_score: 0.44
identity_confidence_score: 0.40
claim_probability: 0.55
relevance_level: high
relevance_confidence: 0.78
canonical_readiness: hold
---

# Proof Review: Entry 513-515 Identity Conflict Analysis

## Blockers

1. Canonical readiness remains `hold`. The staged draft depends on a derivative conversion that is internally consistent with the chunk, but the source packet and conflict-candidate note explicitly preserve low conversion confidence for identity-controlling fields.
2. Entry 513 child identity is not promotion-ready. The converted text gives `Isolina del Carmen` / `Jose` with `Sexo. Masculino`; the page image appears to support a Pulgar/Isolina-style reading, but the name and sex presentation remain too unstable for a child identity or child-parent relationship.
3. Entry 513 mother surname is unresolved. The converted file reads `Juana de Dios Amador de Pulgar`, while the review context preserves an `Amagada`-style concern; visual inspection did not make the surname stable enough to replace or promote either reading.
4. Entry 513 father/declarant profession is not material to the identity guardrail, but it is still a conversion-QA issue because the staged context asks for targeted verification.
5. Entry 515 is only a row-boundary/control item. It is not Pulgar-relevant on the reviewed evidence and should not be used for family inference.

## Evidence Strengths

- The source is a civil birth register page image, a strong source class for birth-row facts when transcription is stable.
- The converted file and chunk agree that entry 513 names `Jose del Carmen Pulgar` as father and `Jose del C. Pulgar` as father/declarant. The page image visibly supports a Pulgar father/declarant lead, though not a canonical same-person merge from abbreviation alone.
- The converted file and chunk agree that entry 513 names a mother as `Juana de Dios ... de Pulgar`, supporting the draft's choice to preserve a mother-identity lead while holding surname resolution.
- The draft's Dario/Pulgar guardrail is supported: the reviewed source, chunk, and conversion do not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, Alexander John Heinz, or any direct identity bridge to those people.
- Entry 515 is separated from the Pulgar row in the conversion and image context; its converted father/declarant is Pedro Pablo Leiva, so the draft correctly limits it to boundary/QA control.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil register page image is a strong source type, but this review did not create a corrected transcription. |
| conversion_confidence_score | 0.38 | Conversion/chunk agree with each other, but multiple identity-controlling fields remain under conversion-QA hold. |
| evidence_quantity_score | 0.46 | One register page plus derivative chunk/packet; no independent corroborating evidence. |
| agreement_score | 0.44 | Derivative texts agree, but prior image-review concerns and current visual ambiguity prevent high agreement. |
| identity_confidence_score | 0.40 | Jose del Carmen Pulgar is a credible lead, but child, mother surname, and abbreviation handling remain unresolved. |
| claim_probability | 0.55 | The draft's limited "hold and preserve conflict" analysis is more likely than not, but no identity claim is promotion-ready. |
| relevance_level | high | Entry 513 contains Pulgar names and is plausibly family-relevant after QA. |
| relevance_confidence | 0.78 | Relevance is stronger than identity proof because the Pulgar surname is visible and repeated. |
| canonical_readiness | hold | Targeted conversion QA is required before any canonical claim, relationship, or person-page edit. |

## Review Decision

The staged draft is supported as a conservative conflict-analysis note. It should remain on hold and should not be promoted to canonical claims, relationships, person pages, or family pages.

## Next Action

Run targeted conversion QA on entry 513 child name/sex, mother surname, birth row fields, and father/declarant profession, and on entry 515 only as needed to confirm row boundaries. After QA produces a stable transcription or explicit uncertainty markers, rerun proof review on any atomic claims and relationship candidates.
