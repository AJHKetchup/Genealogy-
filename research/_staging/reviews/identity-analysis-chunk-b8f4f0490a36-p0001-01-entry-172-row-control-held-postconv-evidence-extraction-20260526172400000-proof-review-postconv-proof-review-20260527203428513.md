---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527203428513
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-control-held-postconv-evidence-extraction-20260526172400000.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-control-held-postconv-evidence-extraction-20260526172400000.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526172400000.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers First

1. The referenced primary source image is not present at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, and the manifest's page image path is also unavailable in this checkout. I could not independently verify the visible row from the image.
2. The converted Markdown and job page Markdown record entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. The assigned chunk records entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, born 8 March 1888. This is a material row-control conflict.
3. Do not promote child identity, birth facts, parent-child relationships, parent identity merges, or Dario-line comparisons from this staged draft until targeted conversion QA restores or locates the source image and certifies the controlling row.
4. The father suffix after `Pulgar` is not review-certifiable here because the visible source could not be opened. It should remain no stronger than the staged alternatives: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Evidence Strengths

- The staged draft accurately reports the derivative conflict between Candidate A, the Pulgar/Arriagada row in the assigned chunk/source packet, and Candidate B, the Burgos/de la Cruz row in the converted Markdown.
- The source packet correctly treats the item as `hold_for_conversion_qa` and does not ask for canonical promotion while row control remains unresolved.
- The anti-conflation note is appropriate. No reviewed artifact supports merging `Jose del Carmen Segundo Pulgar Arriagada` with any Dario/Dario Arturo/Dario Jose Pulgar identity.
- The underlying source type, if restored and verified, would be a strong civil birth registration source for birth and parentage facts; the current blocker is access and derivative disagreement, not source class.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for the cited civil birth register as a source class; 4/10 usable in this review because the referenced image is unavailable |
| conversion_confidence_score | 2/10 because the converted Markdown/job page Markdown and assigned chunk disagree on the entire row for entry `172` |
| evidence_quantity_score | 3/10: one cited source event, but only conflicting derivative transcriptions were available for review |
| agreement_score | 2/10: chunk/source packet agree with each other, converted/job Markdown agree with each other, but the two derivative sets materially conflict |
| identity_confidence_score | 3/10 for certifying the Pulgar/Arriagada child from this review context; 1/10 for any Dario-line identity bridge |
| claim_probability | 0.95 that the item should remain held for conversion QA; 0.55 that entry `172` controls as the Pulgar/Arriagada row based on derivative evidence only; 0.10 or lower for any Dario identity merge |
| relevance_level | high |
| relevance_confidence | 0.85 |
| canonical_readiness | hold |

## Review Finding

The staged draft is supported as a hold/conflict analysis, not as proof of the Pulgar/Arriagada birth facts. The review could verify that the converted Markdown and chunk conflict materially, but could not verify the physical row because the referenced source image is missing from `raw/sources` and the manifest page image is not present under the conversion job.

The safest proof judgment is to keep this item out of canonical claim, relationship, and person/family pages. The row-control issue must be resolved from the source image before any facts or relationships are promoted.

## Next Action

Restore or locate the source image with SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, then run targeted conversion QA comparing the image against the converted Markdown, job page Markdown, chunk, and source packet. After row control is certified, rerun proof review before canonical promotion.
