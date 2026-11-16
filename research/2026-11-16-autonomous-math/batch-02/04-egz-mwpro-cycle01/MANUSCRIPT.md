# EGZ (MWPRO Cycle 01) — source report text

**Classification: CANDIDATE PROOF** (not externally or formally verified). Original report: `MWPRO-20261116-8H_Cycle01_Research.pdf`. Source ZIP SHA-256: `ac2bfaf6f76091243794dfe40b7f6de2b1d8d2e3a7a40195514b709b95340db4`.

**Publication transformation:** text extracted from the entire source PDF; selected private operator/header labels omitted; text typography and layout do not reproduce the PDF exactly. This is not the original ZIP proof manuscript byte stream. See [Batch 02 index](../README.md) for verification and limitations.

---

<PARSED TEXT FOR PAGE: 1 / 10>

 OVERNIGHT MATHEMATICAL RESEARCH / 01 OF 08

 A sharp threshold
 for zero sums
 The Erdos-Ginzburg-Ziv theorem, reconstructed through
 polynomial counting and a composite-modulus lift.

     Cycle classification
     CANDIDATE PROOF (not independently verified)
     The produced proof has separate AI review and exact finite checks. No local formal proof checker
     or external mathematical referee was used.

 Research finding
 The argument establishes the classical threshold for every positive integer modulus, explains
 why the threshold is optimal, and derives a stronger prime-case counting congruence. The
 proof review found no unresolved logical gap. The classification above describes the
 verification of this manuscript; it does not suggest that the classical theorem is open.

   DEDUCTIVE WORK                         EXACT ENUMERATION                    CONSTRUCTIVE CHECK


   All positive integers n                202,905 multisets                    700 specified cases
                                          n = 1 through 8                      35 moduli, up to 210


 research for Mark S. Weinstein / Grounded DI LLC.

 This is Cycle 01 of series MWPRO-20261116-8H. No novelty claim. Finite computation and general deduction are
 recorded separately.

<PARSED TEXT FOR PAGE: 2 / 10>

 CYCLE 01 / 02

 Statement and foundations
 Repeated values are allowed. The selected indices must be distinct.

 Theorem. For every integer n ≥ 1 and every indexed sequence a1, …, a2n-1 of integers, there
 is a subset I of {1, …, 2n-1} having exactly n indices for which n divides the sum of the
 selected values. For n ≥ 2, 2n-1 is the smallest universal length. The singleton case n = 1 is
 immediate.

 The result is the Erdos-Ginzburg-Ziv theorem [S1]. The prime proof uses the established
 Chevalley-Warning route [S2-S4], whose needed divisibility statement is proved on the next
 page. All arithmetic in the field argument is in Fp, where p is prime; all final divisibility
 statements concern ordinary integers.

 Finite-field indicator
 For u ≠ 0 in Fp, multiplication by u permutes all p-1 nonzero field elements. Multiplying the
 elements before and after this permutation and cancelling their nonzero product gives up-1 =
 1. At u = 0 the same power is 0, since p-1 ≥ 1. Thus this power detects nonzero coordinates.

 Small-exponent power sums

 For k = 0, the monomial is the constant polynomial 1, including at t = 0; the sum is p = 0 in
 the field. For 1 ≤ k < p-1, the polynomial Xk-1 has at most k roots, so some nonzero u
 satisfies uk ≠ 1. The root bound follows by repeatedly factoring X-r at a root r; a nonzero
 polynomial cannot have more roots than its degree over a field.

 Writing S for the power sum, multiplication by u permutes the field and gives S = ukS.
 Cancellation of the nonzero factor uk-1 yields S = 0. When p = 2, the required range contains
 only k = 0, already covered.

<PARSED TEXT FOR PAGE: 3 / 10>

 CYCLE 01 / 03

 Counting common zeroes
 Prime-field Chevalley-Warning divisibility, proved explicitly.

 Lemma. Let P1, …, Pr be polynomials over Fp in m ≥ 1 variables. Give them nonnegative
 total-degree upper bounds dj with Σdj < m. The zero polynomial may receive bound 0. If N is
 the ordinary integer number of common zeroes in Fpm, then p divides N.

 At a field point, each factor equals 1 when its polynomial vanishes and 0 otherwise. Hence H
 is the common-zero indicator as a field-valued function. Summing H over every field point
 gives N modulo p.

 Every monomial c x1e₁ xmeₘ appearing in H therefore has at least one exponent ei < p-1.
 Otherwise its total degree would be at least m(p-1). The sum of this monomial over all field
 points factors as follows:

 At least one factor vanishes by the small-exponent power-sum lemma, including the
 zero-exponent case. Every monomial consequently sums to zero, and their finite sum H does
 too. This gives N = 0 in Fp, equivalent to the ordinary divisibility p | N.


     What the argument needs. A field of prime order; the strict total-degree inequality;
     and the constant-monomial case. The rearrangements involve finite sums and
     products only.


 The general finite-field version is documented in Mathlib [S3]. This report needs only the prime-field statement
 just derived.

<PARSED TEXT FOR PAGE: 4 / 10>

 CYCLE 01 / 04

 Prime moduli
 A nonzero common root forces the exact cardinality.

 Fix a prime p and reduce the 2p-1 input values modulo p. In m = 2p-1 variables, define:

 The degree bounds sum to 2(p-1) < 2p-1. The counting lemma therefore makes the
 common-zero count N divisible by p. The all-zero vector is a common zero. It cannot be the
 only one, because N = 1 would violate that divisibility. Choose a nonzero common zero x.

 Let I be the set of its nonzero coordinates. The equation P(x) = 0 gives |I| ≡ 0 modulo p.
 Since x is nonzero and there are 2p-1 coordinates, 1 ≤ |I| ≤ 2p-1. The only possible positive
 multiple of p is p itself.

 This proves the prime case, including p = 2. Repetition among the input values is harmless
 because I selects indices.

 An additional counting identity
 Let Zp count the p-index subsets whose sum is zero modulo p. A common root has empty
 support or exactly p supported coordinates. Each qualifying p-index support allows (p-1)p
 choices of nonzero coordinate values. Thus:

 For odd p, (p-1)p ≡ -1; for p = 2, 1 and -1 are the same residue. Together with p | N this gives
 the congruence. It is stronger than mere existence, but remains an established consequence
 of the same proof route, with no novelty claim.

<PARSED TEXT FOR PAGE: 5 / 10>

 CYCLE 01 / 05

 Lifting to every modulus
 The block sums are divided in the integers, not in a composite residue ring.

 Write E(k) for the EGZ assertion at modulus k. Assume E(a) and E(b) for a, b ≥ 2. Start with
 2ab-1 indexed integers. Repeatedly remove a selected block of exactly a entries whose sum
 is divisible by a, forming 2b-1 pairwise disjoint blocks B1, …, B2b-1.

 This procedure has enough entries at every step. Before block j, the remaining count is
 2ab-1-(j-1)a. For 1 ≤ j ≤ 2b-1, that count is at least 2a-1; equality holds just before the final
 extraction. Apply E(a) to any 2a-1 remaining entries, then remove only the a indices it
 selects. Exactly a-1 entries remain unused at the end.

 By E(b), some b of these integer quotients, indexed by J, have sum divisible by b. The
 corresponding blocks are disjoint, so their union I contains exactly ab indices. Their total
 sum is:

 Therefore E(a) and E(b) imply E(ab). Coprimality is unnecessary: the quotient is an integer
 before the second theorem is applied.

 Strong induction
 The base E(1) is immediate. Every prime case was proved on the preceding page. If n is
 composite, write n = ab with 2 ≤ a,b < n. Strong induction supplies both E(a) and E(b), and
 the product lemma supplies E(n). This includes prime powers and all other positive integers.


     Resource invariant. Final extraction begins with 2a-1 entries; all 2b-1 blocks use
     a(2b-1) entries; a-1 remain. The construction never reuses an index.

<PARSED TEXT FOR PAGE: 6 / 10>

 CYCLE 01 / 06

 Sharpness, made visible
 A constructive n = 6 example and a counterexample to the shorter threshold.

 For the input (0,0,1,1,2,2,3,3,4,4,5), take a = 2 and b = 3. The executed constructor forms
 five even-sum pairs. Dividing their sums by 2 yields (0,1,2,3,4). Choosing quotients 0,1,2
 gives a multiple of 3, hence the six selected original values sum to 6.

 FIVE DISJOINT BLOCKS / a = 2

     0 + 0                   1 + 1                  2 + 2                   3 + 3               4 + 4

       c1 = 0                  c2 = 1                  c3 = 2                   c4 = 3            c5 = 4


 Blue blocks selected: 0 + 0 + 1 + 1 + 2 + 2 = 6.
 The final input value 5 remains unused. Exact trace: worked_example_n6.json.

 Why 2n-2 cannot suffice

 For n ≥ 2, any selection of n entries must contain k ones with 1 ≤ k ≤ n-1: there are too few
 zeroes to choose none and too few ones to choose n. Its sum is k, which is never divisible by
 n. This family disproves the universal claim at length 2n-2 and proves the sharpness of 2n-1.

 For n = 1, length 1 is minimal because the empty sequence has no one-element selection. The sharpness family
 was also checked by exact computation for n = 2 through 50; the general counterexample follows from the
 argument above.

<PARSED TEXT FOR PAGE: 7 / 10>

 CYCLE 01 / 07

 What actually ran
 Exact arithmetic throughout. These finite checks do not replace the general proof.


   n          Multisets                        Valid witnesses                    Brute-force checks


   1          1                                1                                  1


   2          4                                4                                  4


   3          21                               21                                 21


   4          120                              120                                120


   5          715                              715                                715


   6          4,368                            4,368                              0


   7          27,132                           27,132                             0


   8          170,544                          170,544                            0


   TOTAL      202,905                          202,905                            861

 Enumeration and independent routes
 Every multiset of 2n-1 residues in {0,…,n-1} was enumerated for n = 1,…,8. A
 cardinality-indexed suffix bitset dynamic program found the first lexicographic witness. All
 exact input sequences and witnesses are retained. Order-invariance of the existence
 property justifies using multisets instead of enumerating every permutation.

 For all 861 multisets through n = 5, an explicit combinations enumerator returned the same
 first witness. The per-modulus total equals the stars-and-bars count shown below; this
 checks enumeration coverage, not the theorem itself.

 A separate implementation followed the prime-search/block-induction construction on 700
 specified inputs across 35 moduli, up to n = 210. Its prime bases use explicit combinations,
 not the bitset routine. These cases include large negative integers, constant sequences,
 extremal-family extensions and a fully specified linear-congruential input generator.

 Reviewer checks: all 740 residue multisets for p = 2,3,5 satisfy Zp ≡ 1 mod p; direct common-root enumeration
 verified the counting identity for all 25 multisets at p = 2,3. Overlapping tests are not added together as
 independent trials.

<PARSED TEXT FOR PAGE: 8 / 10>

 CYCLE 01 / 08

 Critique and revisions
 The review addressed the actual manuscript and retained its SHA-256 identity.


   Potential failure                      Resolution


   Zero exponent omitted                  The constant polynomial sums to p = 0 in Fₚ; the p = 2 edge case is
                                          included.


   Root count confused with               The zero vector gives N ≥ 1; p | N rules out N = 1.
   existence


   Support may have the wrong size        Its size is a positive multiple of p below 2p, hence exactly p.


   Composite step runs out of entries     Before the final extraction 2a-1 remain; only selected indices are
                                          removed.


   Illegal modular division               Each block sum is divisible by a in the integers before E(b) is applied.


   Repeated values collapse choices       The proof and programs work with distinct indices, not distinct numerical
                                          values.

 Approaches considered and rejected
 Prefix sums alone. Pigeonhole reasoning can produce a zero-sum contiguous segment, but
 not necessarily one of length n. An initial zero gives an immediate one-term collision; the
 exact-cardinality condition remains unproved.

 Composite-ring shortcut. The prime support indicator fails modulo 4: the nonzero residue
 2 has 2³ ≡ 0, not 1. The proof instead uses the valid product lemma.

 A shorter threshold. The n-1 zeroes/n-1 ones family is a verified counterexample to the
 strengthening with 2n-2 entries.


     Review outcome: no required corrections and no unresolved logical gap found in the
     final manuscript. Review was performed by a separate AI agent, unblinded to the
     proposed route, in the same model family and shared environment. Classification
     remains CANDIDATE PROOF.

<PARSED TEXT FOR PAGE: 9 / 10>

 CYCLE 01 / 09

 Execution and evidence
 Original runs are preserved; reproduction writes into a separate destination.


   Activity                          Actual UTC                           Observed outcome


   Cycle initiation                  07:01:50                             Operator-authorized immediate run


   Exhaustive checker                07:03:56.821 - 07:04:06.558          Exit 0; 202,905 cases; stderr empty


   Reviewer arithmetic               07:04:54.463 - 07:04:54.531          Exit 0; prime congruence and root checks


   Constructive checker              07:06:34.941 - 07:06:35.166          Exit 0; all 700 witnesses valid


   Final manuscript review           07:06:54.977                         8,199 reviewed bytes; no gap found

 Machine-readable package
 The research archive includes the complete proof, reviewer reconstruction and findings,
 scripts, exact test inputs and outputs, full compressed case records, source ledger,
 commands, timestamps, environment information and SHA-256 manifest. The manifest
 defines its coverage; the ZIP hash is retained outside the ZIP to avoid a self-reference.

 Replay contract
 The replay runner executes the exhaustive checker and constructive checker in fresh output
 directories. It compares ten deterministic data products byte-for-byte with the retained
 originals. Execution timestamps and environment records are provenance and are not
 required to match. The replay result is recorded in replay/run01/replay_results.json and its
 detailed execution log.

 The observed replay on November 16 ran from 07:07:46 to 07:07:55 UTC. Both programs exited 0; all ten
 designated products matched exactly, and all nineteen protected original verification files remained unchanged.

 A successful same-environment reproduction establishes only the observed agreement for
 these specified scripts and inputs. It does not establish cross-environment reproducibility,
 mathematical validity of arbitrary code, or universal model determinism.

 Minimal reproduction
 python3 replay/replay_all.py --help

 Use the runner’s documented package-root and fresh-output arguments. The mathematics checkers use only the
 Python standard library. Rendering the PDF also uses ReportLab, Matplotlib and Pillow; the recorded builder and
 dependency versions are included.

 No local Lean compilation was performed. The published Mathlib formalization is a source reference, separate
 from these execution results.

<PARSED TEXT FOR PAGE: 10 / 10>

 CYCLE 01 / 10

 References and continuation
 Targeted attribution and proof-route lookup; no global novelty claim.

 [S1] P. Erdos, A. Ginzburg and A. Ziv. Theorem in the additive number theory. Bulletin of the Research Council of
 Israel, August 1961. Original article.

 https://www.renyi.hu/~p_erdos/1961-25.pdf

 [S2] Mathlib contributors. Mathlib.Combinatorics.Additive.ErdosGinzburgZiv. Official theorem documentation;
 identifies the Chevalley-Warning proof route.

 https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/ErdosGinzburgZiv.html

 [S3] Mathlib contributors. Mathlib.FieldTheory.ChevalleyWarning. Official statement and formalization
 documentation for common-zero divisibility.

 https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/ChevalleyWarning.html

 [S4] Yael Dillies / Mathlib contributors. ErdosGinzburgZiv.lean. Pinned source, commit
 9bac2d0692944a775113f7c130fd5e5b4608a854; inspected, not locally compiled.

 https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Combinatoric
 s/Additive/ErdosGinzburgZiv.lean

 Source retrieval ledger timestamp: 07:04:22 UTC on November 16, 2026. The ledger retains precise scope, short
 excerpts and failed retrieval attempts. The original 1961 article uses a combinatorial prime argument; this cycle
 uses the later polynomial route.


 Series state at this checkpoint

   Cycles          Authorized time (Eastern)                           State


   01              02:01, Nov 16                                       Mathematical investigation completed


   02-08           03:00 through 09:00, Nov 16                         Not scheduled: active-task limit reached


 The scheduler rejected creation because all 10 available task slots were occupied. Mark subsequently authorized
 continuing mathematics with the timer conditional on feasibility. No other task was changed. No future
 investigation or unattended execution is claimed.

 Cycle 02, when authorized execution becomes available, is reserved for a newly formulated conjecture. Later
 cycles alternate known theorems and new-to-this-experiment conjectures. The final eight-cycle executive
 comparison remains pending actual completion of the series.


