---
type: proof_review
status: completed
role: claim_reviewer
worker: "postconv-proof-review-20260528221347347"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526000554848.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526000554848.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
recommendation: hold
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

1. The draft correctly identifies a controlling row-level conversion conflict: the chunk, source packet, conflict draft, and visible source image identify entry 172 as the Pulgar/Arriagada row, while the current converted Markdown identifies entry 172 as a Burgos/de la Cruz row.
2. The current converted Markdown is not reliable for promoting any entry-172 identity or relationship claim until the conversion-control conflict is resolved.
3. The father-field suffix after `Jose del Carmen Pulgar` remains uncertain. The chunk reads `Jose del Carmen Pulgar S.`, but the source packet explicitly leaves the trailing element uncertified.
4. No Dario, Arturo, Smith, Pulgar-Smith, grandparent, descendant, or later-life bridge appears in the visible entry. Any Dario-line attachment would be a relationship jump.
5. Canonical promotion should remain blocked for child identity, birth facts, parent names, parent-child relationships, and parent identity merges until targeted conversion QA certifies the controlling row and father-field reading.

## Evidence Strengths

- The source type is a civil birth register, a strong direct source for a birth entry when the correct row is established.
- The visible page image supports the row-number finding that entry 172 on page 58 is the Pulgar/Arriagada row, not the Burgos/de la Cruz row currently in the converted Markdown.
- The chunk and source packet agree on the central Pulgar/Arriagada elements: child `Jose del Carmen Segundo Pulgar Arriagada`, male; birth on 8 March 1888 at 3 p.m.; birthplace `Calle de Valdivia`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- The staged identity-analysis draft uses the conflict conservatively. It recommends hold, not promotion, and treats Dario comparisons as anti-conflation checkpoints.
- The draft preserves uncertainty on the father field and does not force `Jose del Carmen Pulgar S.` into a canonical identity.

## Scores

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Direct civil-registration image; high source value, though handwriting and row-control disagreement require QA. |
| conversion_confidence_score | 0.42 | The chunk is visually supported, but the current converted Markdown materially disagrees with the image and chunk. |
| evidence_quantity_score | 0.64 | One direct source image plus chunk/source-packet/conflict-draft support; only one original event source is in scope. |
| agreement_score | 0.54 | Source image, chunk, source packet, and conflict draft agree against the current converted Markdown. Agreement is mixed because the canonical converted file is contradictory. |
| identity_confidence_score | 0.72 | The visible row likely supports the Pulgar/Arriagada entry-172 identity, but not enough for canonical promotion while the conversion file conflicts. |
| claim_probability | 0.82 | High probability that the staged draft's hold-for-QA conflict judgment is correct. Probability of any promoted identity claim from this draft is low until QA. |
| relevance_level | direct | The reviewed evidence directly concerns entry 172 and the staged conflict. |
| relevance_confidence | 0.99 | The draft, chunk, source packet, source image, and converted file all identify the same assigned entry-number problem. |
| canonical_readiness | 0.05 | Hold. The evidence is important but not promotion-ready because row control and father-field certification are unresolved. |

## Literal Support Check

The staged draft's key claim is supported: there is a real conflict between the Pulgar/Arriagada reading and the Burgos/de la Cruz reading for entry 172.

The current converted file records entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. The chunk records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. The source image view supports the chunk's row placement for entry 172.

The father suffix is not independently certified in this review. It should remain as an uncertainty target, not a promoted normalized name.

## Risk Review

- Identity risk: high if the converted-file Burgos/de la Cruz row is used for Pulgar claims, or if the Pulgar row is used before conversion QA resolves row control.
- Relationship risk: high for parent-child promotion before QA; very high for connecting this row to Dario/Pulgar-Smith identities by surname pattern alone.
- Conflict risk: severe, because two incompatible families are assigned to the same entry number in local artifacts.
- Reliability risk: moderate to high for the current converted Markdown; lower for the chunk/source-packet reading after visual inspection, but still staged.

## Next Action

Run targeted conversion QA against `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, page 58, row 172. The QA note should decide whether entry 172 is controlled by the Pulgar/Arriagada row and should separately certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

Until that QA note exists, keep this draft on hold and do not promote any claims or relationships to canonical folders.
