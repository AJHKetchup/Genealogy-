---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526195436658
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526172507192.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526172507192.md
reviewed_sources:
  - research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526171029823.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
source_quality_score: 0.86
conversion_confidence_score: 0.48
evidence_quantity_score: 0.62
agreement_score: 0.42
identity_confidence_score: 0.60
claim_probability: 0.64
relevance_level: high
relevance_confidence: 0.93
canonical_readiness: hold
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- Canonical readiness remains `hold`. The staged identity analysis correctly identifies a material row-level conflict: the referenced chunk, source packet, and source image support entry 172 as a Pulgar/Arriagada birth row, while the current converted Markdown gives a different Burgos/de la Cruz row for the same entry number.
- The current converted file cannot safely support claims for entry 172. It names child `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and a 6 April 1888 birth, which conflicts with the source image and chunk for the visible entry 172 row.
- The father field for the Pulgar/Arriagada row is not proof-ready beyond a cautious reading. The chunk reads `Jose del Carmen Pulgar S.`, and the image appears compatible with a trailing mark after `Pulgar`, but targeted conversion QA should certify whether the field is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- No relationship or same-person merge should be promoted from this staged draft. The evidence supports a probable birth row for `Jose del Carmen Segundo Pulgar Arriagada`, but the unresolved conversion conflict blocks child identity, parent-child relationships, parent identity merges, and any Dario-line comparison.

## Evidence Strengths

- The civil birth register image is an original/near-original record image and is strong source material for a birth registration once the row transcription is certified.
- The assigned chunk transcribes entry 172 on page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. on Calle de Valdivia, with parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The source packet independently flags the same Pulgar/Arriagada row and explicitly recommends `hold_for_conversion_qa`, matching the staged draft's caution.
- Direct image review supports the row-level conclusion that visible entry 172 on page 58 is the Pulgar/Arriagada entry, not the Burgos/de la Cruz entry in the current converted Markdown.

## Scored Judgment

| Factor | Score / Value | Rationale |
| --- | ---: | --- |
| `source_quality_score` | 0.86 | Civil birth register image is strong primary evidence, though the handwriting still needs targeted certification for the father suffix. |
| `conversion_confidence_score` | 0.48 | The assigned chunk aligns with the image at row level, but the canonical converted Markdown is materially wrong for this entry number. |
| `evidence_quantity_score` | 0.62 | One original image plus derivative chunk/source-packet/conflict notes are enough to detect the conflict, not enough to promote dependent identity claims. |
| `agreement_score` | 0.42 | Chunk, packet, and image agree against the current converted file; derivative agreement is strong but the conversion set is internally inconsistent. |
| `identity_confidence_score` | 0.60 | Probable that the visible row names a Pulgar/Arriagada child, but identity use remains limited until QA resolves the conversion conflict. |
| `claim_probability` | 0.64 | The staged claim that this is a conversion conflict is well supported; promotion of the underlying genealogical claims is not yet supported. |
| `relevance_level` | high | The Pulgar/Arriagada names are directly relevant to the family cluster under review. |
| `relevance_confidence` | 0.93 | The visible row and chunk contain the target family surnames and parent-child structure. |
| `canonical_readiness` | hold | Requires targeted conversion QA before any canonical claim or relationship update. |

## Claim-Level Assessment

| Claim / Hypothesis | Probability | Review Decision | Notes |
| --- | ---: | --- | --- |
| Staged draft's core assertion that entry 172 has a row-level conversion conflict | 0.90 | hold, conflict confirmed | The current converted Markdown is incompatible with the image-supported chunk. |
| Entry 172 visible row names `Jose del Carmen Segundo Pulgar Arriagada` | 0.72 | hold for QA | Supported by chunk and image review, but blocked by the conflicting converted file. |
| Father should be promoted as `Jose del Carmen Pulgar S.` | 0.55 | hold/revise | Plausible but not certified; do not silently normalize the trailing mark. |
| Mother should be promoted as `Juana Arriagada de Pulgar` | 0.68 | hold | Supported by chunk and image review, but promotion waits on conversion QA. |
| Entry 172 supports Burgos/de la Cruz family claims | 0.12 | reject for this visible page image pending QA | The current converted file appears to describe a different row/page set than the referenced image. |
| Entry 172 bridges to any Dario Pulgar identity | 0.02 | blocked | No Dario, Arturo, Smith, spouse, descendant, or explicit bridge appears in the reviewed entry. |

## Next Action

Run targeted conversion QA on the referenced image, current converted Markdown, assigned chunk, and source packet. The QA note should decide the controlling row for page 58 entry 172 and certify the father field only to the extent visible. After QA, rerun proof review for the child identity, birth facts, parent names, and parent-child relationships before any canonical promotion.
