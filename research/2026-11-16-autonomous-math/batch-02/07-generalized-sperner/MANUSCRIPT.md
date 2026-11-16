# Generalized Sperner / k-LYM — source report text

**Classification: CANDIDATE PROOF** (not externally or formally verified). Original report: `MWR-20261116-24H_Cycle11_Sperner_Report.pdf`. Source ZIP SHA-256: `e2171142800c0b0006dd1b7faad04035ac5adc745541f4cf83bfd78203f2f8a3`.

**Publication transformation:** text extracted from the entire source PDF; selected private operator/header labels omitted; text typography and layout do not reproduce the PDF exactly. This is not the original ZIP proof manuscript byte stream. See [Batch 02 index](../README.md) for verification and limitations.

---

<PARSED TEXT FOR PAGE: 1 / 5>

CYCLE 11 / 01


How large can a chain-free family be?
Established theorem investigation | Generalized Sperner theorem and k-LYM

Precise statement
For every integer n≥0, let Bₙ be the set of all subsets of [n]={1,…,n}, ordered by inclusion. A
family F is a subset of Bₙ, so its members are distinct sets. Its height is the greatest number of
members in a strictly increasing inclusion chain; the empty family has height0. For every integer
k≥0, determine the largest |F| subject to height(F)≤k, equivalently no chain of k+1 distinct
members.

The claimed maximum is the sum of the min(k,n+1) largest numbers among C(n,0),…,C(n,n). Ties
can be resolved by any fixed rank order. The accompanying weighted inequality is
∑S∈F1/C(n,|S|)≤k. For k=1, the size bound is the classical Sperner antichain bound C(n,⌊n/2⌋).

An explicit attaining family for n=8,k=3: all sets of sizes3,4,5. Its cardinality is56+70+56=182. Its height is3, and
its weighted LYM sum is exactly3. The bars show exact binomial coefficients; the selected ranks are highlighted.

Finding and status
CANDIDATE PROOF. A complete chain-incidence proof, sharp rank optimization and attainment
construction are provided. Exhaustive finite checks cover65,814 families through n=4. No formal
checker or external reviewer verified this written proof. This reconstructs classical mathematics;
no novelty or full equality-classification claim is made.

<PARSED TEXT FOR PAGE: 2 / 5>

CYCLE 11 / 02


Count chains with exact weights
The generalized LYM inequality and the sharp cardinality bound

Maximal chains and incidences
Every permutation π of [n] gives the maximal chain ∅⊂{π₁}⊂{π₁,π₂}⊂⋯⊂[n]. Conversely each
such maximal chain determines its permutation by the order in which elements are added. There
are n! maximal chains, including one chain when n=0. A fixed r-element set S lies on exactly
r!(n−r)! of them: first order its elements, then order the remaining elements.

If height(F)≤k, any maximal chain contains at most k members of F. Count pairs (S,C), with S∈F
and C a maximal chain containing S. Counting first by chains gives at most k n! pairs; counting
first by sets gives ∑S∈F|S|!(n−|S|)!. Divide by n! to obtain ∑S∈F1/C(n,|S|)≤k. This is a finite double
count, requiring no asymptotic or independence assumption.

Convert the weighted bound to the best size bound
Write fᵣ for the number of r-element members of F, bᵣ=C(n,r) and qᵣ=fᵣ/bᵣ. Then 0≤qᵣ≤1, ∑qᵣ≤k,
and |F|=∑bᵣqᵣ. Reorder ranks so b₁≥⋯≥bₘ>0, where m=n+1; indices here denote that reordered
list, not original set cardinalities.

For 1≤k<m, coefficients beyond position k are at most bₖ. Therefore ∑bᵢqᵢ≤∑i≤kbᵢqᵢ+bₖ∑i>kqᵢ. The
bound ∑qᵢ≤k gives ∑i>kqᵢ≤∑i≤k(1−qᵢ). Substitution bounds the total by ∑i≤k[bᵢqᵢ+bₖ(1−qᵢ)]≤∑i≤kbᵢ,
using qᵢ≤1 and bᵢ≥bₖ.

For k=0, the weighted inequality forces all qᵣ=0 and F is empty. For k≥m, the trivial total-family
bound |F|≤2ⁿ equals the sum of all m rank sizes. This proves the claimed upper bound for all n,k in
the stated domain.

The weighted constraints are a relaxation, not a characterization of chain-free families. For example, {{1},{1,2}}
in B₄ has LYM sum1/4+1/6=5/12≤1 but height2. The proof uses only the necessary implication; the next page
constructs actual families attaining the upper bound.

<PARSED TEXT FOR PAGE: 3 / 5>

CYCLE 11 / 03


Attainment and boundary checks
The upper bound is achieved by concrete rank unions

Choose the largest rank levels
Select min(k,n+1) distinct ranks having the largest binomial coefficients, and let F consist of every
set in those ranks. A strictly increasing chain has strictly increasing set cardinalities, so it can
contain at most one set from each selected rank. Hence height(F)≤k. Its cardinality is exactly the
sum in the upper bound, proving that the maximum is attained.

When 0≤k≤n+1, one maximal chain contains a set in every selected rank, giving height exactly k.
Each selected full rank contributes C(n,r)/C(n,r)=1 to the LYM sum, so the weighted inequality is
also attained. If k≥n+1, take all of Bₙ, whose size is2ⁿ and height n+1.

Exact finite example: n=4

 Allowed height k               Largest possible family                   One set of attaining ranks

 0                              0                                         []

 1                              6                                         [2]

 2                              10                                        [2, 1]

 3                              14                                        [2, 1, 3]

 4                              15                                        [2, 1, 3, 0]

 5                              16                                        [2, 1, 3, 0, 4]


For k=2, a coarse estimate2·C(4,2)=12 is not sharp: the correct answer is
C(4,2)+C(4,1)=6+4=10. Weighted rank allocation supplies the sharper value. For k=3 the middle
three levels contain4+6+4=14 sets. These maxima are also recovered by exhaustive
enumeration, not just by evaluating the formula.

Domain and logical boundaries
For n=0, B₀={∅}: the maximum is0 at k=0 and1 at k≥1. The empty family is the unique height0
family. Factorials at0 are1. All binomial denominators C(n,r), 0≤r≤n, are positive. Rank ties do not
affect the sum or validity of the construction. The proof shows that rank unions are extremizers; it
does not assert that they are the only extremizers.

Unlike general poset statements, this argument uses the exact uniform chain-incidence structure of the Boolean
lattice. No analogous coefficient bound for arbitrary graded posets is inferred. The result is independent of the
validation status of earlier cycle proofs.

<PARSED TEXT FOR PAGE: 4 / 5>

CYCLE 11 / 04


Executed exact verification
Every Boolean family through n=4; larger inputs explicitly bounded

 n                Families checked                                   Maximal chains per family

 0                2                                                  1

 1                4                                                  1

 2                16                                                 2

 3                256                                                6

 4                65,536                                             24


Exhaustive total:65,814 families. A family is encoded by a bitmask F whose bit at position S
records whether subset-bitmask S is a member. Every possible mask is examined. Unlike sampling
isomorphism types, this enumerates all labeled subset families for each stated n.

Different exact checking routes
First compute height by subset dynamic programming: the best family chain inside S is the best
inside a one-element deletion of S, plus1 if S belongs to the family. Independently enumerate
every permutation maximal chain and count family hits. Their maximum must equal the DP
height; any family chain can be extended to a maximal Boolean chain by adding the missing
elements between its successive sets.

The audit compares the sum of all maximal-chain hit counts with the independent incidence
numerator ∑S∈F|S|!(n−|S|)!. This checks the weighted identity using integers, with denominator
n!, and verifies that the numerator is at most height(F)·n!. It also checks the cardinality bound. For
each k=0,…,n+1, the largest observed size among all families of height≤k must equal the stated
theorem value, and an explicit rank-union mask must attain it.

Additional checks and execution scope
Eighty fixed-seed random families,20 each for n=5,…,8, passed the same height, chain-incidence
and bound checks. Fifty-four explicit rank-union controls for n=0,…,8 verify attainment and
equality of the weighted sum. Some controls overlap the exhaustive domain; these are not
claimed as independent or distinct trials. The larger Boolean lattices were not exhaustively
enumerated.

One Python verifier process exited0 with empty stderr. Mathematical arithmetic was integer-only; weighted sums
are stored as numerator/n!. The two algorithms share an author and runtime. There was no formal checker,
external reviewer or cross-runtime replay. Exact family masks, certificates, sample inputs, commands, timestamps
and environment are retained. Finite checks do not establish the arbitrary-n theorem.

<PARSED TEXT FOR PAGE: 5 / 5>

CYCLE 11 / 05


Critique, sources and handoff
Classical theorem reconstructed with transparent verification boundaries

Attempted route and revisions
A size estimate k times the largest rank is valid but generally too coarse; the n=4,k=2 calculation
exposes the loss. The argument was sharpened by counting exact rank-dependent chain weights
and solving the resulting allocation bound. This is a reasoning-level refinement, not a failed
numerical run. The recorded exact audit passed on its first run.

Chain length: count members, not inclusion steps. Distinctness: families contain distinct
subsets; repeated copies are not allowed. Incidences: every r-set occurs r!(n−r)! times, including
r=0,n. Optimization: qᵣ≤1 is essential; the weighted sum alone would give only the coarse k·max
C(n,r) bound. Converse: LYM≤k does not imply height≤k. Attainment: actual rank unions, not
just fractional allocations, close the proof. Scope: arbitrary graded posets and classification of
every extremizer are not asserted.

Sources checked
[1] Mykhaylo Tyomkyn, NDMI113–Extremal Combinatorics, Lecture2, “LYM inequality, set shifting,” teaching
notes2025, p.1. Author’s course notes. Consulted for the standard LYM statement and maximal-chain method. The
report supplies the generalized count and full size optimization.

[2] Matthias Beck, Xueqin Wang and Thomas Zaslavsky, “A unifying generalization of Sperner’s theorem,”
arXiv:math/0112067v1, submitted December7,2001. Author preprint abstract and metadata. Consulted for the
classical generalized-Sperner/LYM context. The full paper was not reviewed. No substantive novelty review was
attempted and no novelty is claimed.

Conclusion and strongest independent-check target
CANDIDATE PROOF. The exact k-LYM inequality, sharp cardinality bound and an attaining construction are
reconstructed for every n,k in the stated domain. The highest-value independent check is the rank-allocation
inequality and its boundary cases, together with the factorial chain count. The written proof remains externally and
formally unverified.

Recompute with python3 verify.py fresh_results; rebuild with python3 build.py. The ZIP contains the
complete proof text, exact verifier and inputs, exhaustive CSV certificates, controls, run logs, source evidence,
environment and SHA-256 manifest. The manifest covers all ZIP members except itself; archive digest and later
save receipts remain external. Rendered QA images are intermediates. Earlier cycle artifacts and snapshots are
preserved.


