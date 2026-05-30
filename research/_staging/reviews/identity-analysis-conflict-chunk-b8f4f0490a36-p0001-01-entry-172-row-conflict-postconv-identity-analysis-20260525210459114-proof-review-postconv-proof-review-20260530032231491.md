---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530032231491
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-postconv-identity-analysis-20260525210459114.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-postconv-identity-analysis-20260525210459114.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
page_image_checked: unavailable_at_referenced_path
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conflict

## Blockers First

1. The exact referenced source image path was unavailable during this review: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`. A narrow file search found related derivative and review-asset files, but not the referenced source PNG. I did not use unreferenced assets to substitute for the source image.
2. The assigned converted Markdown and assigned chunk materially disagree about entry 172. This is not a spelling, accent, or abbreviation issue; it changes the child, parents, birth details, residence, informant, and family line.
3. The assigned chunk supports a Pulgar/Arriagada row for entry 172: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
4. The assigned converted Markdown supports a different entry 172: `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
5. No reviewed material supports treating this entry as evidence for Dario, Arturo, Smith, `Dario Jose Pulgar-Arriagada`, or any Dario-line same-person bridge. Shared Pulgar/Arriagada surname context is not enough for an identity or relationship claim.
6. The father-field reading remains unresolved. The reviewed staged materials correctly require targeted QA to decide among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Evidence Strengths

- The staged identity analysis accurately identifies the controlling issue as a row-level conversion conflict, not a resolved identity conflict.
- The source packet and conflict draft consistently preserve the literal chunk reading and explicitly mark promotion as `hold_for_conversion_qa`.
- The source type, if the source image can be verified, is a civil birth registration, which is a strong source class for a child identity and parent-child relationship. That strength is not currently usable for canonical promotion because the derivatives conflict and the referenced image was unavailable.
- The staged analysis appropriately avoids forcing the record into a Dario identity cluster and keeps same-person, parent-candidate, and relationship conclusions staged.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for the stated civil birth register source class; 4/10 for this review's usable source access because the referenced source image was unavailable |
| conversion_confidence_score | 3/10 |
| evidence_quantity_score | 4/10 |
| agreement_score | 2/10 across assigned chunk and converted Markdown; 7/10 among the staged analysis, source packet, and conflict draft as hold signals |
| identity_confidence_score | 6/10 for the Pulgar/Arriagada row as a plausible staged reading; 2/10 for the Burgos/de la Cruz reading as controlling this staged family-relevant claim; 0.5/10 for any Dario same-person bridge |
| claim_probability | 0.65 that entry 172 may be the Pulgar/Arriagada row described in the chunk/source packet; 0.20 that the converted Markdown's Burgos/de la Cruz row is controlling for this assignment; 0.02 that this entry supports a Dario-line identity bridge |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged identity analysis is supported as a hold/review signal. It should not be promoted as a canonical child identity, parent-child relationship, parent merge, or Dario-line bridge.

Literal support exists only at the derivative level and is split between incompatible readings. The chunk/source-packet side supports the Pulgar/Arriagada hypothesis; the converted Markdown side supports a Burgos/de la Cruz row. Because the referenced source image was unavailable at the recorded path, this proof review cannot certify the controlling row or the exact father-field reading.

## Next Action

Keep the item on `hold_for_conversion_qa`. The next action is targeted conversion QA against the actual page image for page 58, entry 172, specifically to decide the controlling row and certify the father field. After QA, rerun proof review before any canonical claim, relationship, merge, or Dario-line comparison is promoted.
