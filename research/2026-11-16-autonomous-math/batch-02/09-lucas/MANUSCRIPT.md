# Lucas’s theorem — source report text

**Classification: CANDIDATE PROOF** (not externally or formally verified). Original report: `MathWise_Cycle_03_Lucas_Theorem_Report.pdf`. Source ZIP SHA-256: `23d8b991b3a13bc26c5759b3dbf8682a5371686b598cada2d212ecb5936d2835`.

**Publication transformation:** text extracted from the entire source PDF; selected private operator/header labels omitted; text typography and layout do not reproduce the PDF exactly. This is not the original ZIP proof manuscript byte stream. See [Batch 02 index](../README.md) for verification and limitations.

---

<PARSED TEXT FOR PAGE: 1 / 6>
                MathWise Research Cycle 003
                       Lucas’s Theorem for Binomial Coefficients Modulo a Prime


     Cycle                          003

     Mission class                  Established theorem with independently checkable proof

                                    CANDIDATE PROOF — rigorous written proof supplied; not
     Classification
                                    proof-assistant or externally independently verified

     Computation                    PASS — 392,504 exact finite checks

     Timestamp                      2026-11-16 10:07:07 EST

     Research integrity notice
     This report does not claim novelty. Lucas’s theorem is an established theorem. The executable
     checks are finite exact arithmetic checks and do not replace the general proof.

MathWise Cycle 003 · Lucas Theorem · Grounded DI LLC                                                 Page 1
<PARSED TEXT FOR PAGE: 2 / 6>
  1. Problem Statement
  Let p be a prime. For nonnegative integers n and k, write their base-p expansions as finite digit
  strings n = n_0 + n_1 p + ... + n_r p^r and k = k_0 + k_1 p + ... + k_r p^r, padding with trailing zero
  digits as needed. Each digit satisfies 0 <= n_i, k_i < p. Define C(a,b) = 0 when b > a.
   Theorem (Lucas).
   For every prime p and all nonnegative integers n,k,

        C(n,k) ≡ Π_i C(n_i,k_i)         (mod p),

   where n_i and k_i are the base-p digits of n and k, padded to a common length.


  2. Method Classification
    Stage                   Method                                         Evidence type

                            Freshman’s dream in F_p[x] and coefficient     Human-checkable written
    Algebraic proof
                            extraction                                     proof

    Boundary                Digit comparison for k > n and convention
                                                                           Logical case analysis
    handling                C(a,b)=0

    Executable              Exact Python integer arithmetic over
                                                                           Builder-executed finite check
    verification            exhaustive finite ranges

                            Search for invalid assumptions, circularity,   Self-audit; not independent
    Critical review
                            and boundary failures                          external review


  3. Proof Attempt
  Lemma 1. In the polynomial ring F_p[x], (1+x)^p = 1 + x^p.

  Proof. Expanding by the binomial theorem gives (1+x)^p = 1 + x^p + Σ_{j=1}^{p-1} C(p,j)x^j. For
  1 <= j <= p-1, the prime p divides C(p,j), because C(p,j)=p!/(j!(p-j)!) and neither j! nor (p-j)! is
  divisible by p. Hence each middle coefficient is zero in F_p.

  Lemma 2. For each integer i >= 0, (1+x)^(p^i) = 1 + x^(p^i) in F_p[x].

  Proof. Apply Lemma 1 repeatedly through the Frobenius map f(x) -> f(x)^p in characteristic p.
  Equivalently, raise (1+x) to p, then p again, and continue i times.

  Main proof.
  Let n = Σ_i n_i p^i. In F_p[x], factor (1+x)^n according to the base-p digits of n:
   (1+x)^n
     = Π_i ((1+x)^(p^i))^(n_i)
     ≡ Π_i (1 + x^(p^i))^(n_i)                    (mod p).

  Expand each factor on the right:
   Π_i (1 + x^(p^i))^(n_i)
     = Π_i Σ_{b=0}^{n_i} C(n_i,b) x^(b p^i).

  The coefficient of x^k is obtained by selecting one term from each digit factor. Because base-p
  representation is unique, the only possible way to make exponent k = Σ_i k_i p^i is to choose b = k_i


MathWise Cycle 003 · Lucas Theorem · Grounded DI LLC                                                     Page 2
<PARSED TEXT FOR PAGE: 3 / 6>
  from the i-th factor for every i. If any k_i > n_i, the needed choice is unavailable and the coefficient is
  0. Otherwise the coefficient is exactly Π_i C(n_i,k_i).

  The coefficient of x^k in (1+x)^n is C(n,k). Since the two polynomials are congruent coefficientwise
  modulo p, C(n,k) is congruent to Π_i C(n_i,k_i) modulo p. This proves Lucas’s theorem.

  Boundary Case: k > n
  When k > n, C(n,k)=0 by convention. In base p, comparing the most significant digit at which n and k
  differ gives k_j > n_j for some j, so the Lucas product contains C(n_j,k_j)=0. Thus the congruence also
  holds for k > n.

MathWise Cycle 003 · Lucas Theorem · Grounded DI LLC                                                     Page 3
<PARSED TEXT FOR PAGE: 4 / 6>
  4. Exact Computational Verification
  The evidence script verified Lucas’s congruence for primes [2, 3, 5, 7, 11, 13, 17, 19], all n from 0 to
  300, and all k satisfying 0 <= k <= n + 12. Total exact cases checked: 392,504. All computations
  used Python’s exact integer arithmetic and direct binomial evaluation.

    Metric                                      Value

    Script return code                          0

    Status                                      PASS

    Mismatches recorded                         0

    Total cases checked                         392,504

    Output JSON                                 evidence/outputs/verification_results.json

  Selected exact cases:
    p     n       k       n digits LSF                  k digits LSF            C(n,k) mod p   Lucas RHS   match

    5     42      17      [2, 3, 1]                     [2, 3]                  1              1           True

    7     100     38      [2, 0, 2]                     [3, 5]                  0              0           True

    11    284     133     [9, 3, 2]                     [1, 1, 1]               10             10          True

    13    300     91      [1, 10, 1]                    [0, 7]                  3              3           True

    2     255     127     [1, 1, 1, 1, 1, 1, 1, 1]      [1, 1, 1, 1, 1, 1, 1]   1              1           True

    19    299     301     [14, 15]                      [16, 15]                0              0           True

  5. Visual Check: Pascal Triangle Modulo 5

MathWise Cycle 003 · Lucas Theorem · Grounded DI LLC                                                               Page 4
<PARSED TEXT FOR PAGE: 5 / 6>
  Figure: residues of C(n,k) modulo 5 for rows 0–63. The block structure is consistent with Lucas’s digitwise factorization,
  but this visualization is illustrative only and is not itself a proof.

MathWise Cycle 003 · Lucas Theorem · Grounded DI LLC                                                                      Page 5
<PARSED TEXT FOR PAGE: 6 / 6>
  6. Independent Critical Review
    Risk checked                Finding

                                Essential. The proof uses characteristic p and divisibility of middle
    Prime assumption            binomial coefficients. The statement is not valid as written for arbitrary
                                composite moduli.

    Coefficient                 Valid because polynomial congruence over F_p gives coefficientwise
    extraction                  congruence and all products are finite.

    Uniqueness of digit         Valid by uniqueness of base-p expansion after padding with trailing zero
    selection                   digits.

                                Handled by binomial convention and digit comparison; RHS has a zero
    Boundary k > n
                                digit factor.

                                No use of Lucas’s theorem appears in the proof. The proof uses only
    Circularity
                                binomial theorem, primality, and base representation.

    Computational               Finite exact checks support implementation correctness and examples
    scope                       only. They do not establish the infinite theorem.

    Novelty                     No novelty claim. This is a reconstruction of a classical theorem.


  7. Revision and Conclusion
  The proof survived the internal critique after explicitly adding the k > n boundary case and
  sharpening the dependence on p being prime. The strongest unchecked component is not
  mathematical but formal: the proof has not been entered into a proof assistant or externally
  reviewed. Accordingly, this cycle is classified conservatively as CANDIDATE PROOF rather than
  PROVEN.

     Cycle 003 conclusion
     Lucas’s theorem is supported by a complete written proof and 392,504 exact finite checks.
     Classification: CANDIDATE PROOF. Recommended next step: formalize in Lean, Coq, Isabelle, or
     another proof assistant if independent formal verification is required.

  8. Evidence Package Contents
  The ZIP package preserves the verification script, inputs, outputs, figure data, manifest, and this
  report. The SHA-256 manifest is generated after artifact creation.
   evidence/inputs/config.json
   evidence/scripts/verify_lucas.py
   evidence/outputs/verification_results.json
   evidence/outputs/execution_stdout.txt
   evidence/outputs/execution_stderr.txt
   evidence/outputs/execution_returncode.txt
   evidence/outputs/pascal_triangle_mod5_matrix.csv
   pascal_mod5_rows_0_63.png
   MathWise_Cycle_03_Lucas_Theorem_Report.pdf
   evidence/sha256_manifest.json

MathWise Cycle 003 · Lucas Theorem · Grounded DI LLC                                                         Page 6
