---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260523182924292
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-id-stage-chunk-bdb698de8106-p0001-01-identity-candidates.md
staged_draft: research/_staging/identity-analysis/identity-analysis-id-stage-chunk-bdb698de8106-p0001-01-identity-candidates.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
prior_review: research/_staging/reviews/proof-review-research-staging-identity-analysis-identity-analysis-id-stage-chunk-bdb698de8106-p0001-01-identity-candidates-postconv-proof-review-20260523170911048.md
review_status: hold
canonical_readiness: hold
created_at: 2026-05-23T18:29:24Z
---

# Proof Review: bdb698de8106 Identity Candidates

## Blockers

- Hold for conversion QA. The restored bdb chunk path now exists and matches `CHUNK-bdb698de8106-P0001-01`, so the older missing-path blocker is no longer current. The decisive blocker is now the unresolved conflict between the bdb converted/chunk transcript and the visible source image.
- Entry 513 is not proof-ready for a child identity. The bdb converted/chunk text reads the child as `Isolina del Carmen Jose`, but the visible image and local image-reconciliation note point to a Pulgar-surname child field with an unresolved middle-line reading and a final `Jose` line. Do not normalize this into either reading.
- Entry 513 mother surname is unresolved. The bdb converted/chunk text reads `Juana de Dios Amador de Pulgar`; the image-reviewed note and alternate chunk support `Juana de Dios Amagada de Pulgar` as a likely but still uncertain reading. Do not silently normalize to `Arriagada`.
- Entry 514 and entry 515 reinforce that this page has material derivative-vs-image conflicts beyond entry 513. The visible image better supports entry 514 father as `Se ignora` and entry 515 father as `Pedro Pablo Neira`, conflicting with the bdb converted/chunk readings `Belisario Riquelme` and `Pedro Pablo Leiva`.
- No Dario identity is named on this page. The staged analysis correctly treats Dario/Pulgar comparisons as guardrails only; no same-person, ancestor-line, or relationship claim to any Dario Pulgar page is supported by this source alone.

## Evidence Strengths

- Source type is strong: a civil birth-register page is a direct, contemporary source for registrations, parent names, declarants, date/place fields, and sex when the row can be read confidently.
- Source identity is well supported: the image, source packet, converted file, and restored bdb chunk all point to page 172 of the 1889 Los Angeles/La Laja birth register, with entries 513, 514, and 515 visible.
- Entry 513 has relatively strong support for the father/declarant cluster: `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, role as father, age forty-seven, agriculturist, and Calle Colon domicile. This supports later targeted QA but not canonical parent-child promotion while the child and mother fields remain unsettled.
- The staged draft's overall hold posture is supported. Its older missing-chunk statement should be revised in a later draft, but the core conclusion remains correct: this is a conflict container, not a proof-ready identity packet.

## Scored Judgment

| score | value | rationale |
|---|---:|---|
| source_quality_score | 0.86 | Civil register image is a high-quality source type for birth-registration facts, though the page image is cropped/low contrast in places. |
| conversion_confidence_score | 0.32 | The bdb converted/chunk transcript materially conflicts with image review on names, dates/times, parent fields, and completeness. |
| evidence_quantity_score | 0.58 | One direct source image plus derivative transcription and local QA notes; enough to identify the conflict, not enough to settle identities. |
| agreement_score | 0.34 | Strong agreement on source/page and some father/declarant context; weak agreement on child names, mother surname, and entries 514-515. |
| identity_confidence_score | 0.28 | Page-level registration identity is clear, but exact person identities and same-person links are not reliable yet. |
| claim_probability | 0.30 | Probability is low for any exact identity-candidate claim beyond "page contains relevant Pulgar/Riquelme/Neira registration candidates." |
| relevance_level | high | The reviewed materials directly address the assigned staged identity-analysis draft and its cited source packet. |
| relevance_confidence | 0.96 | The task id, chunk id, source packet, converted file, chunk, and image all match the assignment. |
| canonical_readiness | hold | Do not promote to claims, relationships, wiki people, wiki families, or any Dario/Pulgar canonical identity. |

## Identity Risk And Relationship Review

- Identity risk is high for entry 513 because the child field and mother surname are exactly the fields needed to determine whether the row belongs to an existing Pulgar/Amagada/Arriagada cluster.
- Relationship risk is high for parent-child promotion. `Jose del Carmen Pulgar` is likely present as father/declarant, but the child identity is unstable and the mother reading is unresolved.
- Relationship jumps to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada are unsupported. Surname and locality context are only research leads.
- Conflict severity is high because promoting the bdb derivative text would likely create wrong or premature names for at least entry 513 and possibly entries 514-515.

## Next Action

Revise the staged identity-analysis draft before any canonical action: remove or update the stale missing-chunk blocker, keep `canonical_readiness: hold`, and request targeted conversion QA from the visible source image for entry 513 child name, birth date/time, mother surname, and official signature; entry 514 father/child/witness/street fields; and entry 515 child/father/mother/witness fields. After QA produces a stable literal transcription, rerun identity proof review before comparing against existing Pulgar, Amagada, Arriagada, or Dario identity pages.
