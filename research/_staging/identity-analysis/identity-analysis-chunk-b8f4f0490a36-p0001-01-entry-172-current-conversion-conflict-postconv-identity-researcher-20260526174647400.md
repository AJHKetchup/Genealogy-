---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526174647400
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526171029823.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
subject: "Entry 172, Los Angeles birth register, 1888"
conflict_type: row_level_conversion_conflict
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Entry 172 Current Conversion Conflict

## Blockers First

1. The controlling entry-172 row is not proof-ready. The assigned chunk and source packet read entry 172 as a Pulgar/Arriagada birth registration, while the current converted Markdown reads entry 172 as a Burgos/de la Cruz birth registration.
2. The father field is not proof-ready at the suffix level. The chunk reads `Jose del Carmen Pulgar S.`; the source packet says the image supports `Jose del Carmen Pulgar` with a trailing mark compatible with `S.`, but requires targeted QA certification.
3. No identity, parent-child relationship, duplicate-person merge, or canonical Pulgar-line attachment should be promoted until conversion QA resolves the row conflict and a later proof review accepts the corrected source reading.
4. The staged draft does not itself name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Darío Pulgar Arriagada. Those candidates are relevant only because existing wiki/staged Pulgar context requires anti-conflation review before using Jose/Juana parent candidates as a bridge.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526171029823.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Canonical wiki pages checked: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, and `wiki/people/dario-pulgar-adult-passenger-age-64.md`.
- Related staged Pulgar-line context checked for anti-conflation: ICRC `Dario Jose Pulgar-Arriagada` source packet, 1918 `Darío J. Pulgar Arriagada` medical-title source packet, and `Dr Dario Pulgar A.`/Fundo Los Cuartos source packet.

## Literal Source Readings

The assigned chunk reads page 58, entry 172 as:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`, male.
- Registration: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about 3 p.m., `Calle de Valdivia`.
- Father field: `Jose del Carmen Pulgar S.`, Chilean, employee, resident at `Calle de Colipí`.
- Mother field: `Juana Arriagada de Pulgar`, Chilean, `Su sexo`, resident at `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, present at birth, age 26, employee, resident at `Calle de Valdivia`.

The current converted Markdown reads entry 172 as:

- Child: `José Miguel`, male.
- Registration: 7 April 1888.
- Birth: 6 April 1888, 10 p.m., `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

The source packet states that direct image review supports the Pulgar/Arriagada row, not the Burgos/de la Cruz row, but still holds promotion pending targeted conversion QA.

## Hypotheses

### Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

Interpretation: Most likely from the assigned chunk and source packet, but not promotion-ready because the current converted Markdown materially disagrees.

Supporting evidence:

- The assigned chunk gives a coherent row for register page 58, entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- The source packet says the source image shows entry 172 as the Pulgar/Arriagada row.
- Existing canonical stubs already contain staged evidence snapshots for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`, but those snapshots appear dependent on this same row and do not independently resolve the current conversion conflict.

Conflicts:

- The current converted Markdown gives a different child, parents, birth date/time/place, and informant for the same entry number.
- Father suffix `S.` remains uncertain at proof level.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.64 | Strong local support from chunk/source packet, blocked by current converted Markdown disagreement. |
| conflict_severity | 0.95 | Wrong-row promotion would create wrong child, parents, and birth facts. |
| evidence_quality | 0.72 | Civil register evidence is high value, but current derivative artifacts conflict. |
| conversion_confidence | 0.58 | Source packet reports image support, but conversion QA has not certified the controlling row/father field. |
| claim_probability | 0.68 | Pulgar row is more probable than converted Markdown from reviewed local notes, but still on hold. |
| relevance | 0.90 | Directly relevant to Pulgar/Arriagada family reconstruction. |
| canonical_readiness | 0.12 | Not ready until conversion QA and proof review. |

### Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Birth Row

Interpretation: Possible only because the current converted Markdown says so. The assigned chunk and source packet directly contradict it for this staged task.

Supporting evidence:

- Current converted Markdown records entry 172 as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.

Conflicts:

- The assigned chunk and source packet both identify entry 172 as the Pulgar/Arriagada row.
- The source packet explicitly says direct image review supports the Pulgar/Arriagada row rather than the Burgos/de la Cruz row.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.24 | Supported by one current derivative file, contradicted by the staged conflict packet and chunk. |
| conflict_severity | 0.95 | If wrong, every dependent entry-172 identity and relationship claim changes. |
| evidence_quality | 0.38 | The converted Markdown is internally readable but appears to reflect a different row/image state. |
| conversion_confidence | 0.25 | Current conversion is the artifact under challenge. |
| claim_probability | 0.22 | Lower probability after staged image-review/source-packet evidence. |
| relevance | 0.65 | Relevant as the conflicting row, not as a Pulgar-line relationship candidate. |
| canonical_readiness | 0.05 | Do not promote without QA proving this row controls. |

### Hypothesis 3: `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` Is The Father Candidate For The Pulgar Row

Interpretation: Likely father candidate if Hypothesis 1 survives QA. The suffix must remain literal/uncertain until certified.

Supporting evidence:

- Assigned chunk father field reads `Jose del Carmen Pulgar S.`.
- Source packet says the image visibly supports at least `Jose del Carmen Pulgar`, with a trailing mark compatible with `S.`.
- Canonical `wiki/people/jose-del-carmen-pulgar.md` exists as a stub and has a separate staged/draft child link to `Tulio Cesar Luis Jose`, but no reviewed evidence here proves this is the same father as other Jose del Carmen Pulgar candidates.

Conflicts:

- The converted Markdown father field is `Oswaldo Burgos`.
- The `S.` suffix could represent a real name element, abbreviation, mark, or conversion artifact; it is not ready for normalization.
- Existing Jose del Carmen Pulgar context must not be merged by name alone.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.55 | Good row-level candidate if Pulgar row is confirmed; lower for exact suffix/canonical person identity. |
| conflict_severity | 0.88 | Father misidentification would create or reinforce wrong parent-child links. |
| evidence_quality | 0.66 | Register row is valuable, but suffix and row control are unresolved. |
| conversion_confidence | 0.50 | Needs targeted father-field QA. |
| claim_probability | 0.60 | Probable father reading at least as `Jose del Carmen Pulgar` if Pulgar row controls. |
| relevance | 0.92 | Direct parent candidate for the child in the Pulgar row. |
| canonical_readiness | 0.10 | Hold; no merge or promotion. |

### Hypothesis 4: `Juana Arriagada de Pulgar` Is The Mother Candidate For The Pulgar Row

Interpretation: Stronger than the father suffix question if the Pulgar row is accepted, but still blocked by row-level conflict.

Supporting evidence:

- Assigned chunk and source packet both read the mother as `Juana Arriagada de Pulgar`.
- Canonical `wiki/people/juana-arriagada-de-pulgar.md` exists and already has a probable staged child link to `Jose del Carmen Segundo Pulgar Arriagada`, apparently dependent on this same entry-172 evidence.

Conflicts:

- Current converted Markdown reads mother as `Concepcion de la Cruz`.
- No independent source in this review proves that this Juana should be merged with any other Juana or used as a bridge to Dario-line candidates.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Clear in the Pulgar row reading, still dependent on row QA. |
| conflict_severity | 0.88 | Mother misidentification would corrupt parent-child evidence. |
| evidence_quality | 0.70 | Mother field is coherent in chunk/source packet. |
| conversion_confidence | 0.58 | Blocked by conflicting converted Markdown. |
| claim_probability | 0.66 | Probable if the Pulgar row controls. |
| relevance | 0.92 | Direct mother candidate for the child in the Pulgar row. |
| canonical_readiness | 0.12 | Hold for QA and proof review. |

### Hypothesis 5: This Entry Bridges To Dario Arturo Pulgar-Smith / Dario Arturo Pulgar

Interpretation: Not supported by this entry. At most, the Pulgar/Arriagada row is family-context evidence that may later be compared after proof-reviewed parent-child chains exist.

Supporting evidence:

- Canonical `Dario Arturo Pulgar-Smith` is a family-supplied maternal-grandfather profile and explicitly warns not to automatically merge records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith.
- Existing staged CV materials discuss a document-level `Dario Arturo Pulgar`, but this entry-172 source does not name Dario or Arturo.

Conflicts:

- Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`; it does not name `Dario Arturo Pulgar-Smith` or `Dario Arturo Pulgar`.
- Name/family context alone is insufficient for a same-person, ancestor, or duplicate-person bridge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | No direct Dario Arturo/Pulgar-Smith evidence in this entry. |
| conflict_severity | 0.80 | Premature attachment would conflate Pulgar-line clusters. |
| evidence_quality | 0.20 | Only indirect family-context relevance. |
| conversion_confidence | 0.58 | Same row QA blocker applies, but Dario bridge is unsupported regardless. |
| claim_probability | 0.07 | Very low from this exact staged evidence. |
| relevance | 0.45 | Relevant only as anti-conflation/future chain context. |
| canonical_readiness | 0.00 | Not ready. |

### Hypothesis 6: This Entry Bridges To Dario Jose Pulgar-Arriagada, Darío J. Pulgar Arriagada, Dario/Darío Pulgar Arriagada, Or Dario Pulgar A.

Interpretation: Not supported by this entry. Preserve these as separate or unresolved candidates unless later proof-reviewed sources supply a direct bridge.

Supporting evidence:

- Local staged context includes `Dario Jose Pulgar-Arriagada` from ICRC photograph metadata, but the converted photograph page has no visible identifying text.
- A 1918 source packet names `Darío J. Pulgar Arriagada` as a `Médico-Cirujano`; it does not expand `J.` or state parents, birth, spouse, or a same-person bridge.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` records a narrow 2000 expropriation-event claim for `Darío Pulgar Arriagada`.
- The `Dr Dario Pulgar A.`/Fundo Los Cuartos packet supports a physician/property/inheritance context but does not name parents or expand the `A.`.

Conflicts:

- Entry 172 does not name any Dario candidate.
- The child in entry 172 is `Jose del Carmen Segundo`, not Dario.
- Existing Dario/Pulgar-Arriagada clusters vary by middle name or initial, date, source type, and context; merging by surname or maternal surname alone would violate the evidence contract.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | No direct Dario evidence in entry 172. |
| conflict_severity | 0.82 | High risk of conflating separate Pulgar-Arriagada clusters. |
| evidence_quality | 0.22 | Related context exists but does not bridge to this birth row. |
| conversion_confidence | 0.58 | Entry row still requires QA; Dario bridge unsupported in either row. |
| claim_probability | 0.05 | Very low from reviewed materials. |
| relevance | 0.40 | Anti-conflation relevance only. |
| canonical_readiness | 0.00 | Not ready. |

## Conflict Summary

- Same-person conflict: unresolved; this entry does not prove any same-person bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Darío J. Pulgar Arriagada, Dario Pulgar A., or canonical Darío Pulgar Arriagada.
- Duplicate-person risk: high if `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` is merged with existing Jose del Carmen Pulgar candidates by name alone; high if this family context is used to merge Dario clusters.
- Name-variant conflict: `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` must be held as a source-reading issue, not silently normalized.
- Relationship conflict: current converted Markdown gives Burgos/de la Cruz parents; chunk/source packet give Pulgar/Arriagada parents.
- Chronology conflict: current converted Markdown gives birth 6 April 1888 at 10 p.m.; chunk/source packet give birth 8 March 1888 at about 3 p.m.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.68 | Hold for targeted conversion QA, then proof review. |
| 2 | `Juana Arriagada de Pulgar` is the mother in the Pulgar row. | 0.66 | Hold with the row; no canonical promotion yet. |
| 3 | `Jose del Carmen Pulgar` is the father in the Pulgar row. | 0.60 | Hold; certify exact father field and suffix before any relationship claim. |
| 4 | Entry 172 is the Burgos/de la Cruz row in the current converted Markdown. | 0.22 | Preserve only as the conflicting derivative reading unless QA validates it. |
| 5 | Entry 172 bridges to Dario Arturo Pulgar-Smith or Dario Arturo Pulgar. | 0.07 | Do not attach; require a separate proof-reviewed identity bridge. |
| 6 | Entry 172 bridges to Dario Jose Pulgar-Arriagada, Darío J. Pulgar Arriagada, Dario/Darío Pulgar Arriagada, or Dario Pulgar A. | 0.05 | Preserve separate/unresolved; do not merge by name alone. |

## Recommended Next Action

Run targeted conversion QA on the exact source image, assigned chunk, source packet, and current converted Markdown. The QA decision must:

1. Decide whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row.
2. If the Pulgar/Arriagada row controls, certify the father field as exactly one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. After QA, rerun proof review for the child identity, birth facts, mother claim, father claim, and parent-child relationships.
4. Run a separate Pulgar-line identity-bridge proof review before connecting this evidence to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Darío J. Pulgar Arriagada, Dario/Darío Pulgar Arriagada, Dario Pulgar A., or any Jose/Juana parent candidate outside the specific row.

