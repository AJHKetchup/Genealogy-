---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527221429091
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-3d3ab761209f-p0001-01-entry-513-image-reviewed-conflict-note-postconv-evidence-extraction-20260527200921254.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-3d3ab761209f-p0001-01-entry-513-image-reviewed-conflict-note-postconv-evidence-extraction-20260527200921254.md"
source_packet: "research/_staging/source-packets/chunk-3d3ab761209f-p0001-01-entry-513-pulgar-image-reviewed-hold-postconv-evidence-extraction-20260527200921254.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
canonical_readiness: hold
---

# Proof Review: Entry 513 Pulgar Birth Register Conflict Note

## Blockers First

1. Do not promote an atomic child identity, birth event, or parent-child relationship from this staged draft yet. The referenced converted file and assigned chunk disagree on the child name, birth date/time, mother surname, and official signature.
2. The staged draft relies on an image-reviewed reading that appears plausible from the visible source image, but that row-level reading is not yet QA-certified and conflicts with both derivative transcriptions.
3. The visible page supports a Pulgar-family row for entry 513, but the exact child name should remain a conversion-QA question rather than be normalized into a canonical person record from this review alone.

## Evidence Strengths

- The original page image is a civil birth register page for Los Angeles, Chile, page 172, with entry 513 visibly occupying the first row.
- Entry 513 visibly names `Jose del Carmen Pulgar` as father and `Jose del C. Pulgar` as declarant/father, matching the draft's family relevance.
- The page image visibly supports a male child in the Pulgar entry, with birth and registration details in the same row and no obvious spillover from entries 514 or 515.
- The staged draft accurately flags the material conflicts between the converted Markdown, the assigned chunk, and the image-reviewed packet instead of promoting a single transcription as settled.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 3/10 for the existing converted/chunk text; 6/10 for the staged image-reviewed reading pending targeted QA |
| evidence_quantity_score | 4/10 |
| agreement_score | 2/10 across converted file, chunk, and image-reviewed packet for the disputed identity fields |
| identity_confidence_score | 5/10 for a distinct Pulgar child in entry 513; 4/10 for the exact identity `Dario Jose Pulgar Arriagada` until QA certification |
| claim_probability | 0.85 that entry 513 is a Pulgar-family birth record involving father/declarant Jose del Carmen Pulgar; 0.60 that the child is `Dario Jose Pulgar Arriagada` as image-reviewed; 0.25 or lower for the conflicting `Jose Luis`, `Isolina del Carmen`, `Amagada`, or `Amador` readings |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | hold |

## Review Finding

The staged conflict note is supported as a hold-for-conversion-QA item. The source image is relevant and appears to support a Pulgar birth registration in entry 513, but the existing derivative transcriptions are unreliable for the disputed fields. The draft's restraint is appropriate: this should not be attached to a canonical person, family cluster, or relationship until a conversion-review pass certifies the row-level transcription.

## Next Action

Send entry 513 to targeted conversion QA with the specific questions: child name and surname, birth date and time, mother surname, and official signature. After QA certification, rerun proof review on atomic identity, birth, and parent-child claims rather than promoting from this conflict note.
