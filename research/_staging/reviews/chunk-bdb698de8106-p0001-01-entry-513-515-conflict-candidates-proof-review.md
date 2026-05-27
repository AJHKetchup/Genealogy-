---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260527073013726
task_id: proof-review:research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-identity-analysis-20260527001502207.md
staged_draft: research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-identity-analysis-20260527001502207.md
source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526232219797.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
review_status: hold
canonical_readiness: hold
created: 2026-05-27
---

# Proof Review: Entries 513 And 515 Conflict Candidates

## Blockers

- Canonical readiness is `hold`. The staged draft correctly treats this as a conversion-QA problem, not as a promotable identity, relationship, merge, or canonical-page update.
- Entry 513 has a material source-vs-conversion conflict in the child-name field. The converted file and chunk read `Isolina del Carmen / Jose`, but the visible source image appears to show a Pulgar child name beginning with `Pulgar Ana Rosa...`, with the remaining text not fully secure from this review view. This controls the identity of the child and blocks any parent-child claim.
- Entry 513 mother surname is not settled. The converted/chunk text reads `Juana de Dios Amador de Pulgar`; the visible source is at least compatible with an `Amagada`-style reading rather than a stable `Amador` reading. This blocks mother identity and any merge/variant decision.
- Entry 513 father/declarant is a useful lead, but not independently promotable from this draft because it is embedded in a row with unresolved child and mother fields. The visible source supports a `Jose del Carmen Pulgar` / `Jose del C. Pulgar`-style father/declarant reading, but that does not cure the row-level identity risk.
- Entry 515 is relevant only as a row-boundary control. The visible source and conversion both place `Pedro Pablo Leiva` in entry 515, but entry 515 does not supply Pulgar-family proof and should not be used to reconcile entry 513.
- No Dario, Arturo, Smith, or Arriagada identity bridge is directly supported by this source. Any Dario-line connection remains an anti-conflation checkpoint only.

## Evidence Strengths

- The source type is strong: a civil birth-register page for Los Angeles/La Laja, Chile, 1889, page 172, entries 513-515.
- The source packet, converted file, chunk, and source image are present and refer to the same source and chunk identifiers.
- The staged draft's main conclusion is supported: the page is family-relevant because entry 513 contains a Pulgar father/declarant lead, but identity-controlling fields require targeted conversion QA before proof promotion.
- The draft respects the transcription boundary by preserving competing readings as uncertainty rather than silently replacing the converted text.

## Scored Judgment

| field | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil register source is high-value, contemporary evidence for births once read correctly. |
| conversion_confidence_score | 0.24 | Converted/chunk text conflicts with the visible source in the child-name field and likely in the mother-surname field. |
| evidence_quantity_score | 0.54 | One direct register page plus derivative chunk and packet; enough to identify a QA target, not enough to settle identities. |
| agreement_score | 0.32 | Converted file and chunk agree with each other, but the source image materially disagrees with them in identity-controlling fields. |
| identity_confidence_score | 0.30 | Page-level Pulgar relevance is credible; exact child and mother identities are unresolved. |
| claim_probability | 0.66 | Probable that entry 513 is a Pulgar-relevant birth-register row requiring QA; low probability for any exact identity/relationship promotion. |
| relevance_level | high | The reviewed materials directly match the assigned staged draft and task. |
| relevance_confidence | 0.98 | The source packet, converted file, chunk, and image all match the staged draft metadata. |
| canonical_readiness | 0.05 | Hold for conversion QA; no canonical action. |

## Claim Review

| claim or hypothesis | probability | review |
| --- | ---: | --- |
| Registration-scoped conflict hold for entries 513 and 515 | 0.82 | Supported. The source image confirms that conversion QA is needed before any claim extraction or canonical promotion. |
| Entry 513 father/declarant is Jose del Carmen Pulgar / Jose del C. Pulgar | 0.70 | Plausible source-level lead. Hold as unpromoted because the row's child and mother fields are unstable. |
| Entry 513 child is the converted `Isolina del Carmen / Jose` | 0.10 | Not supported by visible source review; hold/revise through conversion QA. |
| Entry 513 mother is exactly `Juana de Dios Amador de Pulgar` | 0.25 | Not proof-ready; visible source appears more consistent with an alternate surname concern, but this review does not substitute a final transcription. |
| Entry 515 supplies Pulgar-family evidence | 0.02 | Unsupported. It is a row-boundary/control issue only. |
| Same-person or lineage bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario Pulgar Arriagada | 0.01 | Unsupported in this source. Preserve only as anti-conflation context. |

## Next Action

Keep the staged draft on `hold_for_conversion_qa`.

Run targeted conversion QA against the source image for entry 513 child full name, sex, birth date/place, father/declarant fields, and mother surname; and for entry 515 row-boundary separation. After QA produces a stable transcription or explicit uncertainty markers, rerun proof review on atomic claims before any canonical claim, relationship, page merge, or lineage bridge is promoted.
