# Four dimensions are minimal for the strictness witness

Published 3 October 2026 at the request of Mark S. Weinstein. This is a source-informed, AI-assisted mathematical follow-up to the [Barei audit](../README.md), in the same assistant workflow. The earlier audit and its evidence remain intact.

**The minimum ambient dimension is exactly four over the complex numbers.** The target is a finite-dimensional evolution algebra E whose stable derived term D has no nonzero square-zero element but is not itself an evolution algebra. The existing four-dimensional witness supplies the upper bound; the argument below supplies the lower bound.

This establishes where the two sufficient hypotheses first differ: in ambient dimensions at most three, Barei’s square-zero-free stable-term condition and Hu–Wen’s evolution-algebra stable-term condition coincide. The witness separates them in dimension four. Historical novelty has not been established.

## Definitions and the lower bound

Multiplication is bilinear and commutative, generally nonassociative. A natural basis has zero products between distinct basis vectors. The zero algebra has its empty natural basis. Write V² for the **span** of all products in V, and N(V) = {v : v² = 0}. This set need not be a subspace. The derived sequence starts at E and repeatedly squares the preceding subspace.

The sequence descends: E² ⊆ E, and U ⊆ V implies U² ⊆ V². Finite dimensionality forces stabilization, giving D² = D. Thus D is a commutative subalgebra, although it need not have a natural basis.

**Low-dimensional lemma.** Every commutative complex algebra A of dimension at most two with N(A) = {0} admits a natural basis.

Dimensions zero and one are immediate. In dimension two choose a basis a,b and let L_u(v) = uv. If L_a is singular, take u = a. Otherwise det(L_b + tL_a) is a quadratic with nonzero leading coefficient det(L_a), so it has a complex root t₀. Take u = b + t₀a, which is nonzero and has singular L_u. In either case choose nonzero v in ker L_u. Since u² ≠ 0, v cannot be a multiple of u. Therefore u,v form a basis with uv = vu = 0: a natural basis.

This proof covers singular and degenerate multiplication without assuming A² = A or associativity. Algebraic closure enters only in the quadratic-root step. It imports no classification or idempotent-existence theorem.

Consequently the target properties require dim D ≥ 3. Also D ≠ E, because E already has a natural basis. Hence dim E ≥ dim D + 1 ≥ 4.

| Possible dimension of D when dim E ≤ 3 | Exclusion |
|---|---|
| 0 | Empty natural basis |
| 1 | Any one-vector basis is natural |
| 2 | Low-dimensional lemma applies |
| 3 | Necessarily D = E, which is an evolution algebra |

For the stated comparison, the other direction also holds: a stable term that is an evolution algebra has D² = D. Its natural-basis squares span D and, being dim D vectors, form a basis. If ∑xᵢfᵢ has square zero, independence of the fᵢ² forces every xᵢ² = 0, hence every xᵢ = 0.

## The four-dimensional upper bound

Rows of the structure matrix encode basis squares, and distinct natural-basis vectors multiply to zero:

```text
W = [[1,0,-1,0],
     [1,1, 0,1],
     [0,1,-1,-1],
     [0,0, 1,1]].
```

The stable term is D = {(x,y,z,x+z)}, with basis f₁ = e₁+e₄, f₂ = e₂, f₃ = e₃+e₄. In these coordinates multiplication is

(x,y,z)(u,v,w) = (xu+yv, yv+zw, xw+zu).

The basis products include f₁² = f₁, f₂² = f₁+f₂, f₃² = f₂ and f₁f₃ = f₃; the other mixed products are zero. They show E² = D and D² = D, giving derived dimensions 4 → 3 → 3.

The square map is (x²+y², y²+z², 2xz). A zero square forces xz = 0. If x = 0, the first equation gives y = 0 and the second gives z = 0. If z = 0, the second gives y = 0 and the first gives x = 0. These branches exhaust all complex solutions.

To exclude a natural basis, the three coordinate multiplication forms have symmetric matrices

```text
B₁ = diag(1,1,0),   B₂ = diag(0,1,1),
B₃ = [[0,0,1],[0,0,0],[1,0,0]].
```

Set B₀ = B₁+B₂ = diag(1,2,1). It is invertible. A natural basis with change matrix P would make every PᵀBⱼP diagonal. The identity

P⁻¹(B₀⁻¹Bⱼ)P = (PᵀB₀P)⁻¹(PᵀBⱼP)

would then make the operators B₀⁻¹Bⱼ simultaneously diagonal, so they would commute. But

```text
[B₀⁻¹B₁, B₀⁻¹B₃] = [[0,0,1],[0,0,0],[-1,0,0]] ≠ 0.
```

Thus D has no natural basis. This is a necessary-condition obstruction, requiring no classification theorem. The witness attains the lower bound of four. Its three-dimensional stable term also shows that three is the least intrinsic dimension of a square-zero-free commutative complex algebra without a natural basis.

## Checks, evidence and limits

The [five-page proof report](Barei_Witness_Minimality_Followup.pdf) handles degenerate product images and provides real-field and square-zero-hypothesis controls. These deliberate changes to the hypotheses are not counterexamples to the complex lemma.

The unchanged original checker and the new [standard-library checker](verify_minimality.py) were rerun before publication. All **9 new supporting groups** and all **11 original groups** passed; their individual check records match the prepared results. See the [publication record](PUBLICATION_RECORD.json), [new actual results](results_minimality_publication.json), [original actual results](results_original_publication.json), and respective [new](run_log_minimality_publication.txt) and [original](run_log_original_publication.txt) logs.

M01–M04 check the witness’s embedding, products, derived dimensions, square-map coefficients and obstruction matrices. M05 checks the general formal determinant identity. M06–M09 check selected singular, nonreal-root, degenerate and hypothesis-control examples. These are finite exact supporting computations. They do not machine-prove complex root existence, all lower-dimensional exclusions, exhaustive square-zero elimination, or the natural-basis implication. The universal arguments appear above and in the report; this is not proof-assistant formal verification.

```bash
# From this directory:
python3 verify_minimality.py --output my_results.json
python3 ../verify_audit.py --output my_original_results.json
```

Both checkers use the Python standard library. Use ordinary Python without `-O` for the original checker.

The [attached review package](artifacts/Barei_Witness_Minimality_Checks.zip) is preserved byte for byte, including its original review status, earlier audit inputs, actual outputs and proposed addendum. Its [SHA-256 sidecar](artifacts/Barei_Witness_Minimality_Checks.zip.sha256.txt) records:

`4f410390393b2e8cb1d1426d25eb1a45e05b62c73856c2a259d6267cd0ef687c`

ZIP integrity and all 15 internally listed hashes passed. [SHA256SUMS.txt](SHA256SUMS.txt) identifies the browsable publication files; [SHA256SUMS_archived_package.txt](SHA256SUMS_archived_package.txt) preserves the original manifest, whose paths apply inside the archive. Hashes establish byte identity against a trusted copy, not correctness or authorship. The report remains the prepared review record; this note records its subsequent publication.

## Sources and credit

The [source-location table](SOURCE_LOCATIONS.csv) and [source record](SOURCES.json) pin the inspected prior commit `a52a1caf3c7e2f560eb9c3ee01f676153d299f83` and distinguish prior-audit material from this follow-up’s proof.

- [Barei’s official Meta publication](https://ai.meta.com/research/publications/on-solvable-evolution-algebras-and-a-conjecture-by-garcia-martinez-and-perez-rodriguez/): natural-basis definition, p. 1; derived-series conventions, §2, p. 2; Corollary 3.4, pp. 3–4; Remark 3.6, p. 4. The manuscript credits Muse Spark and names Nicolás Jaramillo Torres as reviewer.
- [Hu–Wen, *Idempotent-free non-solvable evolution algebras over C*](https://arxiv.org/pdf/2609.25023): natural-basis and matrix conventions, p. 1; stable-term sufficient criterion, Proposition 2.8, p. 6.
- [Earlier detailed audit](../input_record/Barei_Evolution_Algebra_Audit.pdf): stable-term argument, p. 4; independently constructed four-dimensional witness, p. 8. The [original checker](../verify_audit.py), lines 152–184, supplies C05–C06 matrix data.

Credit for the audited paper belongs to Andres Barei, with Muse Spark’s role attributed as reported by its authors and the named review by Nicolás Jaramillo Torres. The original conjecture is due to Xabier García-Martínez and Andrés Pérez-Rodríguez; Hu–Wen supplied the concurrent work compared in the audit. Older existence results used in the original audit remain credited there; they are not required for this minimality proof.

This follow-up was commissioned by Mark S. Weinstein. It is not blind replication or independent human expert review, and implies no endorsement by Meta or the authors. No historical novelty, independently reconstructed AI interaction provenance, or causal benefit from Grounded DI or Protocol A is claimed. No essential imported mathematical dependency remains unresolved for the elementary minimality argument. Historical priority remains unchecked. No authors were contacted.
