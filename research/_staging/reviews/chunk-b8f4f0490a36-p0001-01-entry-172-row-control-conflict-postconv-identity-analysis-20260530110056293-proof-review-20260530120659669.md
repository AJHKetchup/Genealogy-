---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530120659669
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530102722394.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Control Conflict

This review checks the staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md`.

## Blockers First

1. Do not promote a child identity, birth event, parent-child relationship, same-person merge, or Dario-line attachment from this draft. The assigned chunk and current converted Markdown disagree materially for entry `172`.
2. Full-image row control is not certified in this checkout. The referenced raw source image path and the job page image path are absent, so the physical row cannot be rechecked from the original page image in this review.
3. The father-field suffix after `Jose del Carmen Pulgar` is not independently visible here. Preserve it as unresolved unless a later full-image QA pass certifies the suffix.
4. No checked file names Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada in entry `172`. Surname context alone is not an identity bridge.
5. The current converted Markdown supports a conflicting Burgos/de la Cruz reading for the same entry number; this is a conversion/row-control problem, not a normal spelling variation.

## Evidence Strengths

- The assigned chunk coherently transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The source packet accurately flags that the current converted Markdown instead identifies entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. at `En esta`.
- The staged identity analysis correctly treats the conflict as a hold for conversion QA and correctly rejects identity promotion to Dario candidates.
- The source type, if row control is later certified, is strong for birth, parent-name, registration-date, and informant claims because it is a civil birth registration.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for a civil birth register as a source type; 5/10 for this review pass because the original page image is unavailable |
| conversion_confidence_score | 4/10 because the assigned chunk and converted Markdown conflict on child, parents, birth date, time, place, and informant |
| evidence_quantity_score | 3/10: one conflicted source identity with derivative chunk, converted Markdown, and source packet, but no independent corroborating source |
| agreement_score | 3/10 overall; 8/10 between the staged draft, source packet, and assigned chunk for the Pulgar/Arriagada reading; 0/10 between that reading and the current converted Markdown for entry `172` |
| identity_confidence_score | 3/10 for attaching the Pulgar/Arriagada row to canonical people now; 1/10 or lower for any Dario same-person claim |
| claim_probability | 0.68 that the Pulgar/Arriagada row may be the intended entry `172`; 0.20 that the Burgos/de la Cruz conversion may control entry `172`; 0.82 that this is a row-control/conversion mismatch; 0.03 or lower for a Dario identity connection |
| relevance_level | high for Pulgar/Arriagada family-line triage if row control is certified; low for direct Dario identity proof |
| relevance_confidence | 0.85 for relevance to Pulgar/Arriagada review; 0.20 for relevance to Dario same-person analysis |
| canonical_readiness | hold_for_conversion_qa; not ready for canonical claim, relationship, merge, or wiki-page updates |

## Review Finding

The staged draft is supported as a hold recommendation. The local derivative evidence establishes a serious row-control conflict: the assigned chunk and current converted Markdown cannot both be correct for the same physical entry `172`.

The review cannot certify which row controls entry `172` because the referenced full source image and job page image are absent. Therefore, the Pulgar/Arriagada child, parent names, birth event, and relationships remain plausible leads only. The draft's caution against Dario identity attachment is fully supported by the checked evidence.

## Next Action

Keep the item on `hold_for_conversion_qa`. A conversion-QA worker should restore or locate the full page image, compare the physical row for entry `172` against both derivative readings, and bound the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` based only on visible source support.

After row control is certified, rerun proof review only for the narrow birth-name, birth-event, parent-name, and parent-child claims. Any connection to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada requires separate identity-bridge evidence.
