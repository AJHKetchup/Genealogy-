---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260523170911048
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-id-stage-chunk-bdb698de8106-p0001-01-identity-candidates.md
staged_draft: research/_staging/identity-analysis/identity-analysis-id-stage-chunk-bdb698de8106-p0001-01-identity-candidates.md
review_status: hold
canonical_readiness: hold
---

# Proof Review: identity-analysis-id-stage-chunk-bdb698de8106-p0001-01

## Blockers

- The assigned staged draft is `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-bdb698de8106-p0001-01-identity-candidates.md`, but its front matter and first blocker refer to `research/_staging/identity/ID-STAGE-CHUNK-bdb698de8106-P0001-01-identity-candidates.md`. That path mismatch should be cleaned up before any downstream proof use.
- The staged draft reports that the cited bdb chunk path is missing. In this review, `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md` was present and matched the bdb converted transcription. The draft's blocker is therefore stale or was created against a different workspace state.
- The bdb converted file and bdb chunk read entry 513 as child `Isolina del Carmen José`, mother `Juana de Dios Amador de Pulgar`, and birth date `El mismo veinte dos... a las cuatro de la mañana`; the page image visibly supports a different or at least unresolved child-name/maternal-surname/date reading. The staged draft correctly treats this as a conversion conflict, but the exact replacement reading is not proof-ready from this review.
- A parallel chunk for the same source, `CHUNK-3d3ab761209f-P0001-01`, reads entry 513 as `Pulgar Amagada / José Luis`, mother `Juana de Dios Amagada de Pulgar`, and birth date `Junio veinte i seis... a las cuatro i media de la tarde`. That conflicts materially with the bdb chunk and confirms the need for targeted conversion QA.
- Entry 514 and entry 515 identity and relationship fields also conflict across the bdb transcript, source packet image-QA summary, and the visible image. These rows should not be used to support promoted identities or parent-child relationships from this draft.
- The staged draft compares the entry to Dario/Pulgar canonical and staged identities. The assigned source image and bdb derivative files contain no visible `Dario`, `Arturo`, `Smith`, or confirmed `Arriagada` identity bridge, so those comparisons remain contextual guardrails only.

## Evidence Strengths

- Source identity is strong: the source packet, converted file, bdb chunk, and image all point to the same civil birth-register page, page 172, for Los Angeles/La Laja, Chile, 1889, with registrations 513, 514, and 515.
- The draft's main recommendation to hold rather than promote is supported. The page image and derivative layers disagree on core identity fields, including child names, mother surname, birth dates, father fields, street/place readings, witnesses, and page completeness.
- Some broad literals are supported by the available evidence: entry numbers 513-515, the register page context, a father/declarant reading for entry 513 close to `José del Carmen Pulgar` / `José del C. Pulgar`, male sex for entry 513, and Calle Colon context. These are not enough to resolve a canonical identity.

## Scores

| score | value | rationale |
|---|---:|---|
| source_quality_score | 0.86 | Civil birth-register image is a strong original source type for births, parentage, and registration data. |
| conversion_confidence_score | 0.30 | The bdb conversion conflicts with the visible image and with a parallel chunk for the same source. |
| evidence_quantity_score | 0.58 | There is one source image plus multiple derivative layers, but quantity does not overcome contradictory readings. |
| agreement_score | 0.34 | Agreement is good for source/page identity and weak for the identity-bearing fields. |
| identity_confidence_score | 0.28 | No exact person identity or same-person match is ready; only broad registration-scoped candidates are supportable. |
| claim_probability | 0.24 | Probability is low for the staged draft's specific identity comparisons and moderate only for the general hold/conflict conclusion. |
| relevance_level | high | The reviewed evidence directly concerns the assigned staged identity-analysis draft and its cited page. |
| relevance_confidence | 0.94 | Source packet, converted file, chunk, and image all reference the same assigned bdb source family. |
| canonical_readiness | hold | Do not promote, merge, rename, or attach to canonical people/families until conversion QA resolves the conflicts. |

## Claim-Level Judgment

| reviewed claim area | judgment | claim_probability | notes |
|---|---|---:|---|
| The source is an 1889 Los Angeles/La Laja birth-register page containing entries 513-515 | supported | 0.92 | Supported by source packet, bdb converted file, bdb chunk, and image. |
| Entry 513 can be promoted as `Isolina del Carmen José` child of José del Carmen Pulgar and Juana de Dios Amador de Pulgar | hold/revise | 0.18 | The bdb derivative says this, but the page image and parallel chunk do not agree on the child name, maternal surname, or date. |
| Entry 513 may involve José del Carmen Pulgar / José del C. Pulgar as father/declarant | limited support | 0.72 | This reading is consistent across the bdb derivative and visible image enough to treat as a lead, not a canonical relationship. |
| Entry 514 supports Belisario Riquelme as father | hold/revise | 0.10 | The bdb derivative says this, but the visible image and source packet conflict summary support an unknown father reading. |
| Entry 515 supports Pedro Pablo Leiva and Rosa Elvira del Carmen | hold/revise | 0.14 | The bdb derivative says this, but visible evidence and packet notes point toward Neira/Ulloa readings. |
| The page should be attached to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Darío Pulgar Arriagada | not supported | 0.03 | No Dario or direct lineage bridge appears in the assigned evidence. |

## Next Action

Keep the staged draft on hold. The next action is targeted conversion QA against the page image for entries 513-515, with special attention to entry 513 child name, birth date/time, mother surname, father/declarant field, and citation path consistency. After that QA note exists, run a fresh proof review before any canonical promotion or Pulgar-line identity comparison.
