# A Lean countercheck of the Nielsen–Semita RH submission

**MathWise / Grounded DI LLC · November 12, 2026**

We were rooting for a proof. The next best thing is a clear result that the authors and other readers can reproduce.

## Result and scope

**Lean 4.16.0 accepted a derivation of `False` from assumptions in the submitted Version 2 archive.** The check imports the submitted modules and uses their own definitions and axioms. An inconsistent set of assumptions can support conclusions that do not establish the intended mathematical claim.

This result concerns the pinned Lean formalization identified below. It does **not** prove that the Riemann hypothesis is false, independently evaluate the whole written manuscript, or determine what later versions might contain. It does not assess the authors' intent. We welcome correction and independent reproduction.

## Exact submission and verification

- Authors: Jenny Lorraine Nielsen and Lu Semita.
- Repository: [Nielsen-and-Semita-Riemann-Proof-in-Lean4](https://github.com/startigerjln/Nielsen-and-Semita-Riemann-Proof-in-Lean4/tree/4532fb4410ffeed655a165cbb77032b8b4882e54).
- Commit: `4532fb4410ffeed655a165cbb77032b8b4882e54`.
- [Version 2 ZIP at that commit](https://github.com/startigerjln/Nielsen-and-Semita-Riemann-Proof-in-Lean4/blob/4532fb4410ffeed655a165cbb77032b8b4882e54/RiemannHypothesis-Lean4%20VERSION%202.zip), SHA-256 `6a7ffbc02f7fcfa9beeee133c00d0c544931fd3d5ea0573ac5834ed43af6d31d`.
- [GitHub Actions run and complete job log](https://github.com/Grounded-DI/MathWise/actions/runs/43162667905), with the [workflow source at its exact commit](https://github.com/Grounded-DI/MathWise/blob/19a060ce9a5e63dd6d6d5cf32c4d6f35606a9752/.github/workflows/nielsen-riemann-countercheck.yml).
- Runner: Ubuntu 26.04.1; `lean --version`: `Lean (version 4.16.0, x86_64-unknown-linux-gnu, commit 128a1e6b0a82, Release)`.
- The run fetched the Lean release from the official Lean GitHub release URL; it did not independently verify a release binary checksum.

**Build distinction:** the archive's unmodified `lake build` returned exit 1: `no such file or directory ... ./././RH/RH.lean`. The workflow deliberately allowed that step to fail so that it could continue with an independent module-by-module check. It compiled all eight original modules individually, in dependency order, and then `lean -DautoImplicit=false Countercheck.lean` returned exit 0. The overall workflow conclusion is `success` because the Lake step was marked `continue-on-error`; it is **not** evidence that the original Lake build passed.

## Why the assumptions conflict

In the ZIP's `RH/Defs.lean`, lines 68–70 define `LambdaSound.pres` to require that a sentence and its round-trip translation have the same truth value in every ZFC model. Lines 74–82 define an obstruction as those propositions being unequal and `LNonzero` as requiring such a model for every sound translation.

In `RH/Obstruction.lean`, line 12 assumes `linear_obstruction_RH : LNonzero RH_L`; line 24 assumes `exists_lambda_sound`. The first supplies a disagreement for any sound translation, while the second supplies a sound translation. Its soundness then supplies the equivalence that contradicts the disagreement.

The following file was accepted by Lean 4.16.0 after the submitted modules were compiled:

```lean
import RH.Main

theorem published_axioms_inconsistent : False := by
  obtain ⟨τ, hτ⟩ := exists_lambda_sound
  obtain ⟨M, hM, hobs⟩ := linear_obstruction_RH τ hτ
  have heq : msat modLin M RH_L = msat modLin M (τ.RL RH_L) :=
    propext (hτ.pres RH_L M hM)
  exact hobs heq

#print axioms published_axioms_inconsistent
#print axioms riemann_hypothesis_resolved
#check riemann_hypothesis_resolved
```

Lean printed these dependencies for the countercheck:

```text
'published_axioms_inconsistent' depends on axioms: [IsZFCModel,
 LCur, LLin, RH_L, exists_lambda_sound, linear_obstruction_RH,
 modLin, propext]
```

The abstract language and model declarations are also axioms in the submitted file; `propext` is Lean's proposition-extensionality principle. The check uses the submitted axioms: it is **not** a derivation of contradiction from Lean's standard foundations alone.

## What the final theorem states

Lean's actual output for the submitted endpoint was:

```text
riemann_hypothesis_resolved :
  (ZFCPi1Sound → TrueInN RH_L) ∧
    ZFCLCACProv RH_L ∧ (PhaseRigidityAxiom → ∀ (s : CritStripPoint), isXiZero s → realPart s)
```

Lean's `#print axioms riemann_hypothesis_resolved` output was:

```text
[CritStripPoint, IsPi1, IsZFCModel, LCur, LLin, RH_L, RH_is_pi1,
 RH_provable_in_LCAC, StdModel, ZFCLCACProv, ZFCProv,
 exists_lambda_sound, isXiZero, linear_obstruction_RH, modLin, negLin,
 neg_obstruction_RH, pi1_witness_reflection, propext, realPart, zfc_sound,
 Classical.choice, Quot.sound]
```

Among its dependencies are `exists_lambda_sound`, `linear_obstruction_RH` and `RH_provable_in_LCAC`. In `RH/ProofII.lean:24`, the last is declared as an axiom of the exact type used by the endpoint. In `RH/ProofIII.lean:33–40`, the phase-rigidity premise is defined as the same quantified proposition the theorem returns.

`RH_L`, the critical-strip type, and the zero and critical-line predicates are abstract declarations in the archive. The inspected project does not import Mathlib or establish an equivalence from these declarations to Mathlib's complex zeta function. The absence of `sorry` does not establish that the target is the intended classical statement or that nonstandard assumptions have been proved.

## Reproduce

Use Bash in a clean, isolated directory and Lean 4.16.0. Download the pinned ZIP, verify the SHA-256 above, and extract it into a fresh directory with no existing `.olean` files. The workflow linked above is the exact executed procedure. It tries the original `lake build`, then independently compiles the files below with `LEAN_PATH=.` and the project's `autoImplicit=false` option:

```sh
set -euo pipefail
export LEAN_PATH=.
for module in Defs Soundness Obstruction Independence TruthInN ProofII ProofIII Main; do
  lean -DautoImplicit=false -o "RH/$module.olean" "RH/$module.lean"
done
lean -DautoImplicit=false Countercheck.lean
```

Save the Lean block above as `Countercheck.lean` in the extracted root before the last command. Check both exit codes and the printed axiom lists. Do not treat the failed Lake build as a pass. No third-party source ZIP is redistributed in this note.

## Remaining limits

The public PhilArchive history lists newer manuscript versions; their full text was not retrieved for this audit. A revised manuscript or future code release needs its own version-specific review. The check is one execution using an official release binary on one hosted runner; it is not independent human mathematical peer review. The results above do not make claims about the correctness or originality of other work by either author.
