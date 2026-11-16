# EGZ (MWR Cycle 07) — source report text

**Classification: CANDIDATE PROOF** (not externally or formally verified). Original report: `MWR-20261116-24H_Cycle07_EGZ_Report.pdf`. Source ZIP SHA-256: `e1cc30ef8a46c5fb37d2bdb41ea62b84a7d54d7343cacfb54aaefbd5ef73e129`.

**Publication transformation:** text extracted from the entire source PDF; selected private operator/header labels omitted; text typography and layout do not reproduce the PDF exactly. This is not the original ZIP proof manuscript byte stream. See [Batch 02 index](../README.md) for verification and limitations.

---

<PARSED TEXT FOR PAGE: 1 / 7>

CYCLE 07 / 01


An exact zero-sum guarantee
Established theorem investigation | Erdős–Ginzburg–Ziv, with sharpness

Precise problem
For every positive integer n and every indexed sequence of integers a₁,…,a2n−1, prove that some
set I of exactly n distinct indices satisfies ∑i∈I aᵢ ≡ 0 (mod n). Values may repeat; equal values at
different indices remain distinct choices. For n ≥ 2, show that replacing 2n−1 by 2n−2 makes the
guarantee false.

Proof route
The argument first proves the needed prime-field Chevalley–Warning lemma, then obtains a
congruence for the number of zero-sum p-element index sets when p is prime. A disjoint-block
construction transfers the existence theorem from factors a and b to their product ab. Strong
induction completes all positive moduli.

Worked n = 6 construction: five disjoint pairs with even sums produce five integer quotients. The highlighted
three quotient blocks sum to a multiple of 3; their six original entries sum to a multiple of 6. The exact input and
trace appear on page 4.

Result and status
CANDIDATE PROOF. A complete human-checkable argument and sharpness construction are
supplied. The computation checks all residue multisets through n = 6, along with additional
integer inputs and polynomial-root counts. No formal checker or external reviewer verified this
written proof. This is a reconstruction of classical mathematics, with no novelty claim.

<PARSED TEXT FOR PAGE: 2 / 7>

CYCLE 07 / 02


The prime-field counting lemma
A self-contained Chevalley–Warning argument over Fₚ

Lemma and hypotheses
Let p be prime. Let f₁,…,fs be polynomials in m variables over the field Fₚ, with the sum of their
total degrees strictly smaller than m. Constant or zero polynomials are permitted, with degree
bounded by 0. Then the number N of common zeros in Fₚm is divisible by p. The case needed
later has two polynomials and m = 2p−1.

Elementary field facts
For nonzero t∈Fₚ, multiplication by t permutes the p−1 nonzero field elements. Multiplying those
elements before and after the permutation, and cancelling their nonzero product, gives tp−1 = 1.
Thus 1−up−1 is 1 when u = 0 and 0 otherwise.

For 0 ≤ k < p−1, the field sum Sk = ∑x∈Fₚ xk is zero. When k = 0, the constant monomial is 1
even at x = 0, so S₀ = p = 0 in the field. When 1 ≤ k < p−1, the polynomial Tk−1 has at most k
roots, hence some nonzero t satisfies tk ≠ 1. The substitution x↦tx gives Sk = tkSk, forcing Sk = 0.
The root bound follows by repeatedly factoring T−r at a root, reducing the degree.

Sum an indicator polynomial
Define H(x) = ∏j=1s(1−fⱼ(x)p−1). Its value is the indicator of being a common zero, so ∑x∈Fₚᵐ H(x)
equals N as a field element. Its total degree is at most (p−1)∑deg fⱼ < m(p−1). Every monomial of
H therefore has some variable with exponent k < p−1; otherwise its total degree would be at
least m(p−1).

Summing a monomial over all m-tuples factors as the product of its m one-variable sums. The
low-exponent factor is zero by the previous paragraph. Every monomial sum is therefore zero,
and linearity gives ∑H = 0 in Fₚ. The natural integer map to Fₚ has kernel pZ, so p divides N. This
proves the lemma without requiring a primitive root or any estimate on the number of solutions.

The standard indicator/power-sum route is documented in [1]. A separate formal development of the theorem
exists in Mathlib [3]; that development was not run here and does not certify this reconstruction.

<PARSED TEXT FOR PAGE: 3 / 7>

CYCLE 07 / 03


Prime moduli: existence by counting
A stronger congruence for indexed zero-sum subsets

Fix a prime p and any 2p−1 integers a₁,…,a2p−1. Reduce their values modulo p. Let Z be the
number of p-element index sets I satisfying ∑i∈Iaᵢ = 0 in Fₚ. We show that Z ≡ 1 (mod p), which in
particular makes Z nonzero.

Encode support size and support sum
                                                                      p−1                 p−1
Use variables x₁,…,x2p−1 over Fₚ and polynomials f(x) = ∑ xᵢ , g(x) = ∑ aᵢxᵢ . Their degree
sum is at most 2(p−1) = 2p−2 < 2p−1, the number of variables. The lemma on page 2 implies
that their common-zero count N is divisible by p.

For each x, let S = {i: xᵢ ≠ 0}. Since xᵢp−1 is the nonzero indicator, f(x) = 0 says that |S| is
divisible by p. The only possibilities in 0 ≤ |S| ≤ 2p−1 are |S| = 0 and |S| = p. The first contributes
the unique all-zero tuple.

When |S| = p, the second equation becomes ∑i∈Saᵢ = 0. Each qualifying support has (p−1)p
assignments of nonzero values to its coordinates, independently. Consequently the exact integer
identity is:

N = 1 + (p−1)pZ.
Modulo an odd prime p, (p−1)p ≡ (−1)p = −1. For p = 2, the coefficient is 1, which is also −1 in
F₂. Thus 0 ≡ N ≡ 1−Z (mod p), proving Z ≡ 1 (mod p). Since Z counts actual index sets, it is a
nonnegative integer; this congruence excludes Z = 0.

Why the hypotheses matter
This step depends on a field and on primality; no polynomial-zero theorem over Z/nZ for
composite n is assumed. The resulting count congruence does not generally hold modulo
composite n. For n = 4 and seven zeros, Z = C(7,4) = 35 ≡ 3 (mod 4), even though the existence
theorem remains true. The computational audit retains this boundary control.

No enumeration over all primes could establish this argument. The finite checks are support for the explicit
calculation and implementation, while the general prime case rests on the written lemma and the exact
support-count identity.

<PARSED TEXT FOR PAGE: 4 / 7>

CYCLE 07 / 04


From factors to all moduli
Disjoint blocks make the composite step constructive

Let E(n) denote the claimed zero-sum existence theorem. Suppose a,b ≥ 2 and E(a), E(b) hold.
Begin with 2ab−1 integers. Repeatedly select disjoint a-element blocks B₁,…,B2b−1, each with
sum divisible by a. Before selecting block j (1 ≤ j ≤ 2b−1), at least 2ab−1−(j−1)a ≥ 2a−1
elements remain. Apply E(a) to any 2a−1 remaining entries to obtain the next block.

Set qⱼ = (∑i∈Bⱼaᵢ)/a, an actual integer. There are 2b−1 quotients. Applying E(b), select b of them
whose sum is divisible by b. The union of the corresponding disjoint blocks has exactly ab indices
and total sum a times a multiple of b, hence is divisible by ab. Thus E(a) and E(b) imply E(ab).

E(1) holds trivially: every integer is 0 modulo 1. The prime cases were proved on page 3. By
strong induction, if n is composite write n = ab with 2 ≤ a,b < n; both factor cases are already
available, so E(n) follows. This proves the theorem for every positive n.

Executed n = 6 example, with zero-based indices
Input: [5, 1, 0, 2, 3, 4, 4, 3, 2, 1, 0]. Here a = 2 and b = 3. The implementation selects each pair from the current
three-entry window, preserving its original indices.

 Block         Original indices                     Values                                         Sum / 2

 0             [0, 1]                               [5, 1]                                         3

 1             [2, 3]                               [0, 2]                                         1

 2             [5, 6]                               [4, 4]                                         4

 3             [4, 7]                               [3, 3]                                         3

 4             [8, 10]                              [2, 0]                                         1


Selected block indices: [1, 2, 4]. Selected original indices: [2, 3, 5, 6, 8, 10]. Their values [0, 2, 4, 4, 2, 0] sum to
12, a multiple of 6.

The induction proves existence without requiring an efficient prime-case search. The supplied constructor uses
exhaustive search for each prime base and recursion for composite moduli. Performance claims beyond the
bounded executed inputs are not made.

<PARSED TEXT FOR PAGE: 5 / 7>

CYCLE 07 / 05


Sharpness and critical review
The threshold is exact; the proof boundaries are explicit

Why one fewer integer is insufficient
For any n ≥ 2, take n−1 zeros and n−1 ones. This sequence has 2n−2 entries. Every n-element
index set contains k ones for some 1 ≤ k ≤ n−1: neither value occurs n times. Its sum is k, which
is not divisible by n. Hence no n-element zero-sum selection exists. The bound 2n−1 is sharp. For
n = 1, a single entry suffices; an empty sequence contains no one-element selection.

Attempted route and revision
A direct pigeonhole argument on all n-element subset sums was considered, but equality of two
subset sums generally produces a difference of selections, not a new zero-sum selection with
exactly n distinct indices. That implication was not used. The proof route was revised to encode
cardinality and value-sum simultaneously over a prime field, then preserve cardinality with
disjoint composite blocks. This is a reasoning-level discarded approach, not a failed executable
experiment.

Adversarial checks

 Potential defect                           Resolution

 Wrong number of chosen entries             Support equation forces exactly p nonzero coordinates after
                                            excluding the empty support; composite blocks are disjoint.

 Equality in the degree bound               The sum is 2p−2 and variables number 2p−1: the required inequality
                                            is strict.

 All-zero tuple incorrectly treated as      It contributes the separate constant 1 in N = 1+(p−1)^p Z; the
 success                                    congruence forces an additional support.

 Prime p = 2 sign                           1 equals −1 in characteristic 2; the count argument still applies.

 Composite arithmetic mistaken for a        Prime fields are used only in the prime case; composite n uses
 field                                      integer quotients and induction.

 Insufficient entries during block          The last block starts with exactly 2a−1 entries; a−1 entries remain
 extraction                                 unused at the end.


These checks were performed by the same assistant as a separate critique phase. They do not constitute external
review. The classical theorem is not presented as a new discovery, and the model-written argument is not labeled
PROVEN.

<PARSED TEXT FOR PAGE: 6 / 7>

CYCLE 07 / 06


Executed verification
Exact counts, explicit witnesses and exhaustive-scope limits

 n       Canonical multisets        Index subsets checked             Minimum Z            Maximum Z

 2       4                          12                                1                    3

 3       21                         210                               1                    10

 4       120                        4,200                             1                    35

 5       715                        90,090                            1                    126

 6       4,368                      2,018,016                         1                    462


Totals: 5,228 multisets and 2,112,528 index subsets. For every canonical sequence, direct
combination enumeration agrees with a separate subset-size/residue dynamic program. The
recursive constructor returns n distinct indices with a sum divisible by n. For primes 2,3,5, every
count also satisfies Z ≡ 1 (mod p).

Canonical means nondecreasing residue sequences. Reducing arbitrary integers modulo n
preserves all divisibility conditions. Permuting entries bijects index subsets and preserves the
number of solutions. Thus the multiset enumeration covers every residue-sequence type for n ≤
6; it does not separately enumerate all ordered sequences.

Additional checks actually executed
For p = 2 and p = 3, all field assignments were enumerated for every canonical sequence: 25
systems and 5,135 assignment evaluations. Their common-zero counts equal 1+(p−1)pZ and are
divisible by p. Low-exponent power sums were checked for p = 2,3,5,7. These finite checks do
not prove the general polynomial lemma.

A fixed seed, 20261116, generated 120 additional integer inputs, 20 each for n = 7,…,12,
including negative values. Every constructed witness passed direct cardinality, distinctness and
divisibility checks; exact DP counts were positive. The sharpness construction returned zero
solutions for n = 2,…,12. The n = 1 case and the composite count-congruence counterexample
were separately checked.

Execution and independence
One Python process executed the audit, exited 0 and produced empty stderr. Arithmetic was integer-only.
Commands, UTC timestamps, environment, every canonical input and witness, root checks, sample inputs and
results are preserved. The DP, direct enumerator and constructor are different routes but share an author and
runtime. No cross-runtime replay, external reviewer or proof assistant was used.

<PARSED TEXT FOR PAGE: 7 / 7>

CYCLE 07 / 07


Research record and handoff
Sources, conclusion and strongest independent-verification target

Conclusion
CANDIDATE PROOF. The report supplies a full prime-field counting lemma, a prime zero-sum
congruence, the composite construction and the sharp threshold example. The strongest
independent-check target is the transition from polynomial common zeros to exact p-element
supports, followed by the last-block cardinality bound in the composite step. Finite tests support
these steps without proving the arbitrary-n theorem.

Sources checked
[1] Pete L. Clark, Tyler Genao and Frederick Saia, “Chevalley–Warning at the boundary,” Expositiones
Mathematicae39(2021),604–623, §1, especially Theorem1.1 and its indicator-polynomial proof, printed p.605.
Author-hosted paper. Consulted for the classical counting lemma; the report specializes and reconstructs the
required prime-field argument.

[2] Encyclopedia of Mathematics, “Erdös–Ginzburg–Ziv theorem.” Theorem and sharpness reference. Consulted
for the established statement and threshold example. Historical discussion on that page is not treated as current
research status.

[3] Mathlib documentation, Mathlib.FieldTheory.ChevalleyWarning, especially char_dvd_card_solutions_of_sum_lt
and sum_eval_eq_zero. Official project documentation. A formal development exists separately. Its source was not
compiled or used to certify the present written proof.

Evidence package and reproduction
Recompute with python3 verify.py fresh_results. Rebuild the report from the preserved checks with python3
build.py. The exact verifier uses the Python standard library. Report generation additionally uses ReportLab,
Matplotlib and recorded DejaVu fonts. The ZIP retains proof text, executable scripts, source evidence and retrieval
timestamp, exact inputs/outputs, the worked construction, critique, run logs, environment and SHA-256 manifest.
Rendered review pages remain local intermediates.

The manifest covers every research ZIP member except itself. The archive digest and later save receipts are
external, preventing circular self-hashing. Previous cycle artifacts and index snapshots remain intact. No global
novelty, smallest-counterexample, formal-verification or external-validation claim is made.


