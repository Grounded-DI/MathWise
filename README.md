# MathWise

MathWise is a Grounded DI mathematical archive for formula proposals, replay receipts, visualizations, and cross-domain planning demonstrations.

**Published by:** Grounded DI LLC · **Creator / operator:** Mark S. Weinstein · **Public repository established:** July 29, 2025

## Overview

This repository preserves ten public artifacts spanning partition-function estimation, prime-number visualization, an entropy-linked toroidal-fluid specification, a replayable polygon-cascade record, and a preeclampsia delivery-timing planning framework.

The archive separates three different kinds of material: mathematical or scientific proposals, artifact-recorded execution results, and exploratory or safety-bounded demonstrations. “Deterministic” is used here in the narrow sense of fixed or reproducible processing under stated inputs and rules; it does not mean that a formula is proven, that a model is universally correct, or that a clinical decision is automated.

No executable solver, runtime package, dependency manifest, test suite, or CI workflow is included in the current repository. The files are therefore suitable for review and controlled evaluation, not direct deployment.

## Why It Matters

The strongest record in this repository is the explicit separation of mathematical content from replay identity. The polygon-cascade receipts preserve a canonical payload hash, mathematical-data hash, SVG hash, ZIP hash, run number, and verification result. That gives a reviewer a concrete basis for checking whether a later artifact is byte-identical to the recorded output, while leaving mathematical correctness to separate analysis.

The other records show how the same rule-oriented approach is expressed across number theory, applied mathematics, and a safety-gated research planning example. They are useful starting points for formula review, provenance packaging, and a scoped proof of concept.

## Key Records

| Artifact | What the repository records | Boundary |
|---|---|---|
| `run_receipt_1_of_5.json`, `run_receipt_5_of_5.json`, and `Five_Independent_Runs_Polygon_Cascade_PASS_re_run_receipts.jpeg` | Five-run polygon-cascade replay record; the two included JSON receipts carry matching hashes and `verification_result: PASS`. The companion capture reports zero coordinate mismatches and maximum coordinate error `0.0`. | The repository contains receipts 1 and 5 plus the capture, not an executable harness or all five JSON receipts. |
| `Partition_Function_Estimate.md` and `Partition_function_plot.pdf` | A proposed finite correction to the Hardy–Ramanujan partition estimate and a plotted comparison for `1 ≤ n ≤ 20`. | This is a proposal and visualization. No proof, error analysis, or claim of improved accuracy is established here. |
| `Prime_Echo_Lattice_Demo.md` | Ulam-spiral visualization concepts using diagonal band compression (`Dθ`) and a local prime-phase entropy filter (`E_local`). | The “Prime Echo Lattice” is presented as an exploratory conjecture; novelty and mathematical validity are not independently established. |
| `Toroidal_Entropy_Cascade.md` | A coupled PDE specification, initial and boundary conditions, sample input, and illustrative sample output for an entropy-linked charge cascade. | No solver, numerical method, or run artifact is included; the sample output is not presented as computed validation. |
| `Preeclampsia Delivery-Timing Optimizer (Deterministic)` | A research/IRB planning framework with an objective function, biomarker inputs, entropy metrics, hard safety gates, pseudocode, and audit notes. | It is not medical advice or a clinical system. Institutional protocols and maternal–fetal medicine judgment control any real decision. |

## What the Record Demonstrates

### Replay identity

The two JSON receipts identify the same canonical payload, mathematical data, SVG, and ZIP bytes across runs 1 and 5:

| Field | Recorded value |
|---|---|
| `canonical_payload_sha256` | `87f40ead722efaf0d0334d38ff4acd4f74e1eceb594af8df99f84f79fa211513` |
| `mathematical_data_sha256` | `44b635f9c6841740bd089f7c619957b2b7c73fc8ef51ce40b49ef79bd16a590e` |
| `svg_sha256` | `9cf49bf3527c5fa8b6eb104bc08d657df83041cac674afec71f323c036bccf23` |
| `zip_sha256` | `0ca1239ede5bac427e5e7b4a4e38bc0ace930d8cf3d0b3644ec97f6da9bb1729` |
| `total_runs` | `5` |
| `verification_result` | `PASS` |

A hash establishes identity of the hashed bytes. It does not, by itself, establish that the underlying mathematics is correct.

### Formula and specification records

The partition-function document defines the Hardy–Ramanujan estimate and proposes an entropy-based damping term. The prime-lattice document defines the prime phase function, diagonal projection, and local second-difference filter. The toroidal-cascade document defines a coupled PDE and the quantities it proposes to track. These are reviewable formulas and specifications, not packaged implementations.

### Safety-gated planning example

The preeclampsia document evaluates candidate horizons `h ∈ {0,…,14}` with an objective balancing maternal hazard, fetal-flow hazard, and prematurity penalty. Gates such as eclampsia, uncontrolled severe hypertension, thrombocytopenia, renal deterioration, and non-reassuring fetal testing override optimization. The document explicitly limits the work to research/IRB planning; it does not provide an individualized recommendation or clinical validation.

## Technical Model

The repository’s common evidence pattern can be read as:

`fixed inputs → mathematical transformation or rule specification → canonical output → receipt / manifest hashes → replay comparison`

Where a record is only a proposal or sample, the chain stops at the specification or illustration. Where receipts exist, they preserve the identity of the recorded bytes and the stated verification result.

## Recorded Checks

| Check | Result | Evidence |
|---|---|---|
| Polygon-cascade replay record | `PASS`; `total_runs: 5` | `run_receipt_1_of_5.json`, `run_receipt_5_of_5.json`, and the companion capture |
| Receipt hash comparison | Matching canonical-payload, mathematical-data, SVG, and ZIP hashes in the two included receipts | The two JSON files listed above |
| Coordinate comparison | `0` mismatches; maximum error `0.0` | Companion JPEG record |
| Repository review during this update | Ten tracked artifacts inspected; no executable runtime, dependency manifest, tests, or CI found | Current `main` tree and Git history |

The replay and coordinate results above are artifact-recorded results. No original execution harness was available to rerun them from this repository during this review.

## How to Review

```bash
git clone https://github.com/Grounded-DI/MathWise.git
cd MathWise
```

Recommended order:

1. Read the two JSON receipts and the polygon-cascade capture.
2. Review `Partition_Function_Estimate.md` alongside [`Partition_function_plot.pdf`](Partition_function_plot.pdf).
3. Read `Prime_Echo_Lattice_Demo.md` and `Toroidal_Entropy_Cascade.md` as exploratory specifications.
4. Read `Preeclampsia Delivery-Timing Optimizer (Deterministic)` with its research/IRB and clinical-safety boundary in view.

## Evaluation and Integration Context

The archive can support a scoped proof of concept around canonical serialization, replay receipts, hash-based artifact identity, or human-reviewed formula workflows. A technical evaluator can use the public records to define the required inputs, gates, outputs, and evidence package before requesting private implementation access.

Potential integration scenarios are limited to evaluation until executable components and validation plans are supplied. The preeclampsia material requires institutional review and qualified clinical oversight; it is not a deployable medical product. Commercial licensing and integration inquiries: **[CONTACT PLACEHOLDER]**.

## Authorship and Provenance

Git history records Grounded DI LLC and Mark S. Weinstein as the repository’s originating authorship identity, beginning July 29, 2025. The public artifacts retain their dates, filenames, formulas, receipts, and hashes. These records support technical history and authorship traceability; repository metadata and hashes do not by themselves establish legal ownership or patent priority.

No open-source license is present in the repository. Public availability should not be read as a grant of reuse rights. Add or review a deliberate license, `AUTHORS`, `NOTICE`, `CITATION.cff`, release tags, and signed manifests separately with legal counsel if broader distribution is intended.

## Scope and Status

**Status:** Active public mathematical and demonstration archive. It contains formula proposals, visualizations, a receipt-backed replay record, and a safety-bounded research planning document. It is not a certified proof, production solver, clinical decision system, or independently validated benchmark package.

The repository’s strongest demonstrated result is the recorded polygon-cascade replay identity and its receipt structure. The mathematical proposals and cross-domain specifications remain open to independent review.

## Discovery

#MathWise #DeterministicAI #MathematicalModeling #Replayability #AuditTrail #Provenance #ResponsibleAI
