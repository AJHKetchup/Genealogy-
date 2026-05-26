---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526215839027
task_id: "proof-review:research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916.md"
staged_draft: "research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916.md"
source_packet: "research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526193717806.md"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
created: 2026-05-26
source_quality_score: 0.84
conversion_confidence_score: 0.26
evidence_quantity_score: 0.58
agreement_score: 0.31
identity_confidence_score: 0.35
claim_probability: 0.43
relevance_level: direct
relevance_confidence: 0.97
canonical_readiness: hold
---

# Proof Review: Entry 513-515 Identity Conflict Analysis

## Blockers First

1. Canonical readiness is `hold`. The staged draft correctly treats entries 513 and 515 as conversion-conflicted and does not provide stable endpoints for person creation, relationship attachment, identity merge, or name normalization.
2. Entry 513 is probably the family-relevant Pulgar row, but the relationship-bearing fields are not settled. The converted/chunk text reads child `Isolina del Carmen Jose` and mother `Juana de Dios Amador de Pulgar`; the page image and local QA notes support a serious competing reading in the child-name and mother-surname areas. I am treating those as source-reading conflicts, not corrected transcriptions.
3. Entry 515 is not usable for a promoted identity or relationship. The converted/chunk text reads `Rosa Elvira del Carmen` and `Pedro Pablo Leiva`, while image/review context indicates a partial bottom row with a competing `Neira`-style surname concern and an emendation note.
4. The staged draft contains no direct support for connecting this page to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario J. Pulgar Arriagada`. Those names remain anti-conflation guardrails only.

## Scores

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.84 | Civil birth-register page image is a strong original source type and page 172 / entries 513-515 are identifiable. |
| conversion_confidence_score | 0.26 | Key identity fields disagree between converted/chunk text and image-review notes, especially entry 513 child/mother and entry 515 child/father. |
| evidence_quantity_score | 0.58 | One page image, converted file, chunk, source packet, conflict draft, and prior local review context exist, but no independent source corroborates the disputed identities. |
| agreement_score | 0.31 | Agreement is adequate for page identity and broad entry-513 Pulgar father/declarant relevance; agreement is poor for disputed names. |
| identity_confidence_score | 0.35 | Entry 513 likely concerns a Pulgar family row, but exact child, mother, and cross-record identity conclusions remain unresolved. |
| claim_probability | 0.43 | The held identity-analysis judgment is more probable than promotion; exact identity claims are below proof threshold. |
| relevance_level | direct | The reviewed staged draft directly concerns this exact source packet, chunk, and entries 513-515. |
| relevance_confidence | 0.97 | All reviewed files point to the same source image, converted file, chunk id, and page/entry scope. |
| canonical_readiness | hold | Targeted conversion QA must come before any canonical claim, relationship, merge, or wiki edit. |

## Evidence Strengths

- The source packet, converted file, chunk, and source image all identify the source as the 1889 Los Anjeles / La Laja birth register, page 172, with entries 513-515.
- Entry 513 has strong family relevance because the father/declarant area supports a `Jose del Carmen Pulgar` / `Jose del C. Pulgar` reading at the same row level.
- The staged identity-analysis draft preserves uncertainty and keeps competing `Amador` / `Amagada` / `Arriagada` and `Leiva` / `Neira` readings separate instead of silently normalizing them.
- The draft correctly blocks any Dario/Pulgar-Smith or Pulgar-Arriagada bridge because none of those names or relationship bridges appear in the reviewed source evidence.

## Claim Judgment

| Claim Or Hypothesis | Judgment | Claim Probability | Canonical Readiness |
| --- | --- | ---: | --- |
| Entry 513 is Pulgar-family relevant | Supported as a held hypothesis; father/declarant evidence is the strongest part of the row. | 0.64 | hold |
| Entry 513 child is the converted `Isolina del Carmen Jose` | Not stable; derivative reading conflicts with image-review context. | 0.18 | hold |
| Entry 513 mother is converted `Juana de Dios Amador de Pulgar` | Possible derivative reading only; not safe to promote or merge. | 0.28 | hold |
| Entry 513 mother is `Juana de Dios Amagada de Pulgar` or related variant | Plausible competing image-review hypothesis only; not a certified replacement transcription. | 0.35 | hold |
| Entry 513 father/declarant is `Jose del Carmen Pulgar` / `Jose del C. Pulgar` | Strongest narrow row-level reading, but no cross-record merge is proved. | 0.68 | hold |
| Entry 515 child/father as converted `Rosa Elvira del Carmen` / `Pedro Pablo Leiva` | Weak derivative reading against row-level image conflict. | 0.20 | hold |
| Any Dario/Pulgar-Smith/Pulgar-Arriagada bridge | Unsupported by this staged draft. | 0.02 | do_not_promote |

## Next Action

Run targeted conversion QA against the original page image for entry 513 child full name, sex, birth date/time/place, father/declarant details, and mother full name. Also reconcile entry 515 child-name and father/declarant surname only enough to prevent row spillover. After QA produces a stable transcription or explicit uncertainty markers, rerun proof review on each atomic claim and relationship candidate before any canonical promotion.
