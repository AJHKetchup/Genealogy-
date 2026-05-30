---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530103923737
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530092229282.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530092229282.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530072501797.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530072501797.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530072501797.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Keep the staged identity analysis on hold. The original full-page source PNG is unavailable in this checkout, so this review cannot certify physical row control for entry `172`.
2. The derivative materials conflict materially. The converted Markdown reads entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888; the chunk reads entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888.
3. Do not promote a same-person, parent-child, Dario-line, or Jose/Juana canonical attachment from this draft. The proof context supports a row-control problem, not a resolved identity bridge.
4. Do not promote the father suffix after `Pulgar`. The crop-level evidence supports `Jose del Carmen Pulgar` as visible, but the possible trailing mark or suffix is not proof-ready.

## Evidence Strengths

- Civil birth registration is a strong source type for a birth event and parent names when row control is certified.
- The assigned chunk, source packet, conversion review note, and two staged crop assets agree on the local Pulgar/Arriagada parent and informant field area.
- The crop assets visibly support a Pulgar/Arriagada field sequence including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.` at crop level.
- The staged identity analysis correctly rejects treating the Burgos/de la Cruz reading as a name variant or same-person evidence for the Pulgar/Arriagada row.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for the civil registration source type; 4/10 for this review instance because the original full-page image is unavailable |
| conversion_confidence_score | 4/10 overall; 6.5/10 for the local cropped Pulgar/Arriagada parent/informant fields; 2/10 for full entry row control |
| evidence_quantity_score | 4/10 |
| agreement_score | 5/10 overall; high agreement among chunk, packet, review note, and crops, but direct conflict with the current converted Markdown |
| identity_confidence_score | 6/10 for the local Pulgar/Arriagada row hypothesis; 1/10 for any Dario identity bridge; 1/10 for Burgos/de la Cruz same-person treatment |
| claim_probability | 0.68 that the available crop/chunk evidence reflects a Pulgar/Arriagada entry `172`; 0.25 that the converted Burgos/de la Cruz row controls; 0.02 for a Dario identity bridge; 0.01 for Pulgar/Arriagada and Burgos/de la Cruz being the same family event |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold; not ready for canonical claims, relationships, merges, or wiki updates |

## Review Finding

The staged identity analysis is supported as a hold note. Its main conclusion is properly scoped: this is a conversion row-control conflict, not a resolved identity or relationship claim.

Literal support is present for the existence of a Pulgar/Arriagada parent/informant field in the available crop evidence, and the chunk preserves a coherent Pulgar/Arriagada entry. Literal support is also present that the current converted Markdown records a different Burgos/de la Cruz entry for the same entry number. Because the full-page source image is absent, this review cannot determine which derivative row is the controlling transcription for entry `172`.

The staged draft should not be used to attach any claim to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or any Jose/Juana parent candidate beyond the literal row hypothesis. The source materials reviewed here do not provide a direct Dario name, adult identity bridge, spouse, child, descendant, or later-life continuity evidence.

## Next Action

Keep `promotion_recommendation: hold_for_conversion_qa`. The next action is full-page original-image row-control review against source SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, with special attention to whether entry `172` is the Pulgar/Arriagada row, the Burgos/de la Cruz row, or a shifted derivative alignment. After row control is certified, separately review the father-name suffix and then any narrow birth, parent-name, and parent-child claims.
