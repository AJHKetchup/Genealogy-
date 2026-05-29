---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260529092815100
task_id: "identity-analysis:research/_staging/conflicts/conflict-chunk-9c09bf855da9-p0014-01-dario-pulgar-name-form-proof-review-revision-postconv-evidence-extraction-20260529090740365.md"
staged_draft: "research/_staging/conflicts/conflict-chunk-9c09bf855da9-p0014-01-dario-pulgar-name-form-proof-review-revision-postconv-evidence-extraction-20260529090740365.md"
subject: "Dr Dario Pulgar A. / DR. DARIO PULGARA"
source_packet: "research/_staging/source-packets/chunk-9c09bf855da9-p0014-01-el-aguila-fundo-los-cuartos-dario-pulgar-proof-review-revision-postconv-evidence-extraction-20260529090740365.md"
source: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0014-chunk-01.md"
chunk_id: CHUNK-9c09bf855da9-P0014-01
page_reference: page 14
analysis_status: hold_for_conversion_qa
canonical_readiness: not_ready
---

# Identity/Conflict Analysis: Dr Dario Pulgar A. Page-14 Name Form

## Blockers First

- Exact staged draft analyzed: `research/_staging/conflicts/conflict-chunk-9c09bf855da9-p0014-01-dario-pulgar-name-form-proof-review-revision-postconv-evidence-extraction-20260529090740365.md`.
- The raw source PDF `raw/sources/El Aguila Nombre Grande Scan.pdf` is absent in this workspace, and the expected page-14 image was not present under the conversion job path checked. This blocks visual reread of the typed name line and handwritten signature.
- The available evidence is derivative text only: typed article line `DR DARIO PULGAR A` and handwritten-signature note `DR. DARIO PULGARA`.
- The source packet rates conversion confidence `low_to_medium` and recommends `hold_for_conversion_qa`.
- The page says the subject inherited Fundo Los Cuartos from `sus padres` around 1917, but names no parent. No Jose, Juana, Arriagada, Amagada, Smith, Arturo, spouse, child, birth, or death identifier appears in the page-local text.
- No external research was performed. No raw sources, converted Markdown, chunks, canonical wiki pages, source packets, or staged conflict drafts were edited.

## Literal Evidence

From the assigned source packet and chunk:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL AÑO 1917
```

The same derivative page description records:

```text
[Handwritten signature: DR. DARIO PULGARA]
```

Interpretation kept separate: `Pulgar A` may be a surname plus initial, an abbreviated maternal surname, a spacing/punctuation issue, or a conversion artifact. `PULGARA` may be a true signature reading or a collapsed `Pulgar A.` reading. Current evidence does not justify expanding `A.`, normalizing `PULGARA`, assigning parents, or attaching the mention to any canonical person.

## Hypothesis 1: Page-Local Dr Dario Pulgar A. Associated With Fundo Los Cuartos

Supporting evidence:

- The assigned conflict draft, source packet, converted file, and chunk all identify the relevant item as `CHUNK-9c09bf855da9-P0014-01`, page 14.
- The article body directly says Fundo Los Cuartos belonged to `DR DARIO PULGAR A`.
- The same sentence describes him as `DISTINGUIDO FACULTATIVO DE CONCEPCION`.
- It says he inherited the fundo from his parents around 1917, without naming those parents.

Conflicts and limits:

- The exact typed spacing and punctuation require visual QA.
- This is a page-local identity only, not a proved bridge to a family or canonical profile.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.76 | Strong for the narrow page-local derivative mention; not broader identity. |
| conflict_severity | 0.42 | Moderate because downstream name normalization or attachment could mislead. |
| evidence_quality | 0.60 | Direct derivative transcription, but source image/PDF is unavailable. |
| conversion_confidence | 0.46 | The packet itself rates low-to-medium and flags missing visual QA. |
| claim_probability | 0.72 | Probable as a held page-local claim after visual confirmation. |
| relevance | 1.00 | Directly addresses the assigned staged conflict. |
| canonical_readiness | 0.08 | Hold pending conversion QA and identity bridge. |

## Hypothesis 2: `PULGARA` Is A Misread Or Spacing Collapse Of `Pulgar A.`

Supporting evidence:

- The typed line on the same page reads `DR DARIO PULGAR A`.
- The signature note differs mainly by the spacing between `Pulgar` and `A`.
- Prior related local analyses and tasks frame this as a name-form/source-reading conflict before an identity conflict.

Conflicts and limits:

- No page image is available to inspect the handwriting.
- `PULGARA` cannot be promoted as a surname, and `Pulgar A.` cannot be silently imposed on the signature.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Same-page typed and signature forms probably concern the same page-local subject. |
| conflict_severity | 0.56 | Premature normalization could create a false surname or false initial. |
| evidence_quality | 0.44 | Derivative handwriting note only. |
| conversion_confidence | 0.30 | Handwritten spacing is the lowest-confidence part of the evidence. |
| claim_probability | 0.58 | Plausible but unproved. |
| relevance | 1.00 | This is the active name-form conflict. |
| canonical_readiness | 0.04 | Not ready for canonical use. |

## Hypothesis 3: Same Older Medical Person As Dario Pulgar A. / Dario J. Pulgar Arriagada / Dario Jose Pulgar-Arriagada

Supporting evidence:

- Page 14 calls the subject `Dr` and a Concepcion physician.
- A local staged medical-title task reports `Dario J. Pulgar Arriagada` under `Medicos-Cirujanos` in a 2 September 1918 title-conferral context.
- Local passenger-list staging distinguishes an adult `Dario Pulgar` aged 64 with occupation `Medical` from a child `Dario Pulgar` aged 11.
- Local metadata-derived staging preserves `Dario Jose Pulgar-Arriagada` as an identity candidate, with low confidence for image-level identification.

Conflicts and limits:

- Page 14 does not spell `J.`, `Jose`, or `Arriagada`.
- The `A.` after Pulgar cannot be expanded to Arriagada from this source alone.
- Metadata-derived Dario Jose evidence and medical/passenger clusters need their own proof-reviewed bridge before comparison can become promotion.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Profession, chronology, and initial shape are suggestive but indirect. |
| conflict_severity | 0.68 | High conflation risk across older Pulgar medical clusters. |
| evidence_quality | 0.50 | Relevant local staged evidence exists, but not as a direct bridge. |
| conversion_confidence | 0.46 | Page 14 remains visually unverified; comparison clusters carry their own limits. |
| claim_probability | 0.40 | Possible older-medical same-person hypothesis. |
| relevance | 0.94 | Required Pulgar-line comparison. |
| canonical_readiness | 0.06 | Do not merge; run identity-bridge proof review after page QA. |

## Hypothesis 4: Same Person As Dario Arturo Pulgar / Dario Arturo Pulgar-Smith

Supporting evidence:

- Existing canonical `wiki/people/dario-arturo-pulgar-smith.md` identifies Dario Arturo Pulgar-Smith as Alexander John Heinz's maternal grandfather from family-supplied knowledge.
- Staged CV packets identify a document-level subject `Dario Arturo Pulgar`, with page-level evidence held pending identity bridge.
- The broad name elements `Dario` and `Pulgar` overlap.

Conflicts and limits:

- Page 14 does not state `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, any family relationship, or any CV/Habitat context.
- `Pulgar A` is not evidence that `A` means Arturo.
- The canonical Pulgar-Smith page explicitly warns not to attach similarly named records without identity review.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | Broad name overlap only. |
| conflict_severity | 0.80 | Wrong attachment would conflate older medical/property evidence with the Pulgar-Smith/CV cluster. |
| evidence_quality | 0.40 | Family and CV context is real but not bridging here. |
| conversion_confidence | 0.44 | Page-14 and CV-to-canonical bridges remain held. |
| claim_probability | 0.09 | Low on current local evidence. |
| relevance | 0.95 | Required because Pulgar-Smith is the current family-supplied Dario anchor. |
| canonical_readiness | 0.01 | No canonical attachment supported. |

## Hypothesis 5: Same Person As Canonical Dario/Dario Pulgar Arriagada Legal-Notice Cluster

Supporting evidence:

- Canonical `wiki/people/dar-o-pulgar-arriagada.md` exists for a person named `Dario Pulgar Arriagada`.
- The local legal-notice candidate names `Dario Pulgar Arriagada` as apparent domain holder in a 5 December 2000 expropriation event.
- If later verified, `Pulgar A.` could theoretically abbreviate `Pulgar Arriagada`.

Conflicts and limits:

- Page 14 does not spell `Arriagada`.
- The 2000 legal-notice context does not state medical occupation, Fundo Los Cuartos, inheritance around 1917, parents, or age.
- The 1917 inheritance and medical title context require chronology controls before any link to a 2000 property notice.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Initial/surname compatibility only. |
| conflict_severity | 0.76 | Potential duplicate-person and chronology conflict if merged prematurely. |
| evidence_quality | 0.48 | The legal notice supports its own identity candidate, not this bridge. |
| conversion_confidence | 0.52 | Legal notice evidence is stronger than the page-14 signature, but comparison is indirect. |
| claim_probability | 0.14 | Possible but weak. |
| relevance | 0.86 | Required Pulgar-Arriagada anti-conflation comparison. |
| canonical_readiness | 0.03 | No merge or attachment supported. |

## Hypothesis 6: Jose/Juana Parent Candidates Are The Unnamed Parents

Supporting evidence:

- Page 14 says the subject inherited Fundo Los Cuartos from `sus padres`.
- Existing local context includes Jose/Juana Pulgar-line candidates, including `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Conflicts and limits:

- Page 14 names no parent.
- Existing Jose/Juana materials are separate and conversion-sensitive, including row-control issues in the Pulgar/Arriagada birth-registration cluster.
- Family-context hints justify a targeted double-check only; they do not justify assigning parents or merging identities.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.04 | No named parent or parent bridge appears on page 14. |
| conflict_severity | 0.72 | Unsupported parent assignment would create serious relationship conflicts. |
| evidence_quality | 0.32 | Parent-candidate evidence is separate and held. |
| conversion_confidence | 0.36 | Page 14 and parent-candidate clusters both have QA limits. |
| claim_probability | 0.03 | Current page supports unnamed parents only. |
| relevance | 0.70 | Required parent-candidate comparison. |
| canonical_readiness | 0.00 | No parent or lineage promotion supported. |

## Conflict Summary

- Name-variant conflict: active. Preserve `DR DARIO PULGAR A` and `DR. DARIO PULGARA` separately until page-image reread.
- Same-person conflict: unresolved. The strongest non-page hypothesis is an older medical `Dario Pulgar A.` / `Dario J. Pulgar Arriagada` / `Dario Jose Pulgar-Arriagada` cluster, but no bridge is proved.
- Duplicate-person risk: high if merged by name with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, canonical `Dario Pulgar Arriagada`, or the 1953 adult/child passenger candidates.
- Relationship conflict: page 14 gives unnamed parents only; no Jose/Juana candidate is supported.
- Chronology conflict: no contradiction inside page 14, but inherited-property timing around 1917 and physician status point toward older-generation controls before comparison with later CV/Habitat or 2000 legal-notice clusters.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Page-local `Dr Dario Pulgar A.` associated with Fundo Los Cuartos | 0.72 | Restore or locate the source PDF/page-14 image and visually reread the typed name, physician phrase, inheritance sentence, and page context. |
| 2 | Signature `PULGARA` is a misread or spacing collapse of `Pulgar A.` | 0.58 | Visual signature reread; do not normalize either form before that. |
| 3 | Same older medical person as `Dario Pulgar A.` / `Dario J. Pulgar Arriagada` / `Dario Jose Pulgar-Arriagada` | 0.40 | After page-14 QA, run targeted identity-bridge proof review comparing exact names, initials, profession, Concepcion context, age, and chronology. |
| 4 | Same as canonical `Dario Pulgar Arriagada` legal-notice cluster | 0.14 | Require direct bridge or vital/property-continuity proof; otherwise keep separate. |
| 5 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.09 | Require explicit reviewed bridge from the page-14 doctor/property owner to the CV/Pulgar-Smith identity. |
| 6 | Jose/Juana candidates are the unnamed parents | 0.03 | No parent promotion; require a separate source naming this Dario's parents. |

## Recommended Next Action

Keep this staged conflict on `hold_for_conversion_qa`. Do not merge people, rename pages, expand `A.`, normalize `PULGARA`, promote page-14 facts, or attach Jose/Juana parents.

The exact next proof-review step is targeted page-image QA for `CHUNK-9c09bf855da9-P0014-01`: restore or locate `raw/sources/El Aguila Nombre Grande Scan.pdf` or a page-14 image, then visually confirm the typed `DR DARIO PULGAR A` line, the handwritten signature, the Concepcion physician phrase, and the inherited-from-parents sentence. If confirmed, promote only narrow page-local claims first. A separate identity-bridge proof review should then compare the confirmed page-local subject to proof-reviewed older medical Pulgar-Arriagada records before considering any bridge to Dario Arturo Pulgar, Dario Arturo Pulgar-Smith, canonical Dario Pulgar Arriagada, or Jose/Juana parent candidates.
