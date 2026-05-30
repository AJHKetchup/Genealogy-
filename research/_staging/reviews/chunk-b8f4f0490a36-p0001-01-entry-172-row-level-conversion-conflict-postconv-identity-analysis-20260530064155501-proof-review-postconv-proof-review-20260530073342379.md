---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530073342379
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064155501.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064155501.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers First

1. Canonical promotion is blocked. The referenced source PNG is not present in this checkout under the accented path in the chunk manifest or the unaccented path in the source packet, so I could not freshly certify the complete original page image.
2. The converted Markdown and assigned chunk materially disagree for entry `172`. The converted file records `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. The assigned chunk records `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888.
3. This is a row-control/conversion conflict, not a name-variant conflict. Do not attach Burgos/de la Cruz facts to the Pulgar/Arriagada child.
4. The suffix after `Jose del Carmen Pulgar` remains uncertain for promotion. The staged crop supports the base father name and the Pulgar/Arriagada row context, but does not make the trailing suffix independently promotion-ready.
5. No direct Dario-line identity claim is supported. The checked materials do not name Dario, Arturo, Smith, a spouse, child, descendant, or other bridge to a Dario Pulgar candidate.

## Evidence Strengths

- The staged draft accurately reports the conflict between the assigned chunk and the converted Markdown.
- The assigned chunk explicitly gives entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at three in the afternoon at Calle de Valdivia, with parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- The source packet and conversion review note consistently preserve the same Pulgar/Arriagada row reading while warning that original-image QA is still needed.
- The staged crop asset `research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-bottom-postconv-evidence-extraction-20260529000036877.png` visibly supports the lower parent/informant fields for the Pulgar/Arriagada row: base father name `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The staged draft correctly treats a same-person merge between the Pulgar/Arriagada and Burgos/de la Cruz readings as unsupported.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 6/10 |
| conversion_confidence_score | 5/10 overall; 7/10 for the assigned chunk and staged crop parent/informant fields; 3/10 for artifact-level agreement because the converted Markdown conflicts |
| evidence_quantity_score | 4/10 |
| agreement_score | 5/10 overall; high among staged Pulgar/Arriagada artifacts, low between chunk and converted Markdown |
| identity_confidence_score | 7/10 for treating Pulgar/Arriagada as the likely staged row reading; 1/10 for any same-person merge with Burgos/de la Cruz; 1/10 for any Dario identity bridge |
| claim_probability | 0.72 that the assigned row reading is Pulgar/Arriagada pending original-image QA; 0.28 that the converted Burgos/de la Cruz reading controls; 0.02 that the two readings describe the same person; 0.02 for a direct Dario bridge |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | hold |

## Review Finding

The staged identity analysis is supported as a hold and anti-conflation warning. The available local evidence favors the Pulgar/Arriagada reading for the assigned chunk, and the staged crop supports the base parent and informant fields. However, the original source PNG is unavailable in this checkout, and the current converted Markdown still records a different Burgos/de la Cruz entry for the same entry number.

The draft should not be promoted as a canonical identity, parent-child relationship, or Dario-line bridge. Its safest use is to block accidental conflation and to route the record back to targeted original-image row-control QA.

## Next Action

Run targeted original-image row-control certification for `CHUNK-b8f4f0490a36-P0001-01`, register page 58, physical row entry 172. The reviewer should certify the controlling row and separately decide whether the father field can be read as `Jose del Carmen Pulgar S.` or must remain bounded as `Jose del Carmen Pulgar [?]`. Keep all identity merges, relationships, and canonical wiki updates on hold until that certification is complete.
