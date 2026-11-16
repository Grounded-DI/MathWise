# Birkhoff–von Neumann — source report text

**Classification: CANDIDATE PROOF** (not externally or formally verified). Original report: `MWR-20261116-24H_Cycle09_Birkhoff_Report.pdf`. Source ZIP SHA-256: `fbab5eae38f011df2b8fa81bbcf1d8a9befa1808e54a4d8024eca51cb604a19f`.

**Publication transformation:** text extracted from the entire source PDF; selected private operator/header labels omitted; text typography and layout do not reproduce the PDF exactly. This is not the original ZIP proof manuscript byte stream. See [Batch 02 index](../README.md) for verification and limitations.

---

<PARSED TEXT FOR PAGE: 1 / 6>

CYCLE 09 / 01


Exact mixtures of permutations
Established theorem investigation | Birkhoff–von Neumann and its term bound

Precise statement
For every integer n ≥ 1 and every real n-by-n matrix A with nonnegative entries and every row
and column sum equal to 1, prove A = ∑k=1m λₖPₖ, where λₖ > 0, ∑λₖ = 1 and each Pₖ is a
permutation matrix. Show m ≤ (n−1)²+1 and that the extreme points of the doubly stochastic
matrix set are exactly permutation matrices.

A permutation matrix has one entry 1 in each row and column and all others 0. An extreme point
is not a nontrivial convex combination of two distinct points of the set. The written proof applies
directly to real matrices; the executable audit uses scaled integers and exact rational fractions.

An executed 3-by-3 example decomposed into five weighted permutation matrices. Dark cells are 1, light cells are
0 in the permutation panels. Input entries and weights are exact fractions; color intensity is visual context only.

Finding and classification
CANDIDATE PROOF. A complete support-matching argument, constructive decomposition,
dimension bound and extreme-point proof are supplied. Exact checks cover 2,792 integer-grid
inputs and 120 known-positive rational stress inputs. The argument has not received formal or
external verification. The theorem and bound are classical; no novelty is claimed.

<PARSED TEXT FOR PAGE: 2 / 6>

CYCLE 09 / 02


Why the peeling step exists
A self-contained matching argument and a finite decomposition

Positive support satisfies Hall’s condition
Form a bipartite graph of n rows and n columns, joining row i to column j exactly when Aᵢⱼ > 0. For
any row set S, its total mass |S| lies in its neighboring columns N(S). Each such column has total
mass 1, so |S| ≤ |N(S)|.

To prove that this condition gives a perfect matching, choose a maximum-cardinality matching M,
which exists because the graph is finite. If it leaves a row r unmatched, start at r and follow
unmatched edges from rows to columns and matched edges back to rows. Let S,T be the reached
rows and columns. No reached column is unmatched: a shortest alternating path to one could be
flipped to increase M. Every reached row except r is the matched partner of a reached column, so
|S|=|T|+1. Every neighbor of S lies in T: unmatched edges are traversed forward, and the matched
neighbor of a reached matched row is already its predecessor. This contradicts Hall’s condition.
Hence M is perfect, defining a permutation matrix P supported on positive entries of A.

Subtract and normalize
Set ε = miniAi,π(i), where P selects column π(i) in row i. Then 0 < ε ≤ 1. If ε=1, row sums force A=P
and the process ends. Otherwise B=(A−εP)/(1−ε) is nonnegative and has every row and column
sum equal to 1. Thus A=εP+(1−ε)B. At least one positive matched entry becomes zero; existing
zeros stay zero.

Repeat on B. Each nonterminal step strictly reduces the number of positive entries, and a doubly
stochastic matrix has at least n positive entries. With exactly n it is a permutation matrix. Hence
the process terminates after finitely many steps, and substitution gives positive convex weights
summing to 1. A crude bound is k−n+1 terms when the initial matrix has k positive entries. The
stronger bound follows on page 3.

This proves existence directly for all real inputs under the hypotheses. It does not rely on an unproved step of
approximating a real doubly stochastic matrix by rational doubly stochastic matrices. The positive-support peeling
mechanism is classical [1,2].

<PARSED TEXT FOR PAGE: 3 / 6>

CYCLE 09 / 03


Dimension and extreme points
The sharper term bound follows from strict affine-dimension descent

Ambient affine dimension
In the affine space of matrices whose row and column sums are 1, the upper-left (n−1)-by-(n−1)
entries determine all remaining entries. Row and column total sums make the final corner
consistent. Thus the dimension is d=(n−1)². Nonnegativity and additional prescribed zeros can
only reduce affine dimension.

Every nonterminal peel drops dimension
For a zero pattern Z, let DZ be the doubly stochastic matrices zero at all positions in Z. At a current
nonterminal step, both A and the selected permutation P lie in DZ. For an entry e attaining ε,
Aₑ=ε<1 while Pₑ=1, so coordinate e is nonconstant on the affine hull of DZ. The next matrix B has
Bₑ=0 and retains all zeros Z. Its new zero-pattern set is therefore contained in the intersection of
that affine hull with the hyperplane Xₑ=0. This nonempty intersection has dimension at least one
less.

Starting from dimension at most d, there are at most d nonterminal peels before dimension 0. At
dimension 0, the current matrix and its supported permutation must coincide, so the last step is
terminal. The total number of permutation terms is at most d+1=(n−1)²+1. More precisely it is at
most one plus the initial zero-pattern affine dimension. This is a bound on a valid decomposition,
not a claim that the returned decomposition minimizes the number of terms.

Characterize the extreme points
Suppose a permutation matrix P equals θB+(1−θ)C with 0<θ<1 and doubly stochastic B,C.
Nonnegativity forces B,C to be zero wherever P is zero. Each row then has only P’s selected
position available, and row sum 1 forces B=C=P. Hence P is extreme.

If A is not a permutation matrix, its finite decomposition from page 2 contains at least two distinct
permutation matrices with positive weights. Separate one term λP from the normalized convex
mixture Q of the remaining terms: A=λP+(1−λ)Q, with 0<λ<1. If Q=P then A=P, a contradiction.
Thus A is a nontrivial convex combination and is not extreme. This proves that the permutation
matrices are exactly the extreme points.

<PARSED TEXT FOR PAGE: 4 / 6>

CYCLE 09 / 04


An exact worked certificate
Rational reconstruction and a support-sensitive dimension check

The preserved worked input is A=M/D with D=71 and integer matrix M below. Indices in permutation tuples are
zero-based: tuple π means Pi,π(i)=1.

 Row           Integer entries of M

 0             [29, 18, 24]

 1             [34, 19, 18]

 2             [8, 34, 29]


 Term          Exact weight                         Permutation columns

 1             19/71                                [0, 1, 2]

 2             10/71                                [0, 2, 1]

 3             10/71                                [1, 0, 2]

 4             8/71                                 [1, 2, 0]

 5             24/71                                [2, 0, 1]


The coefficients sum to 1 and entrywise reconstruction agrees exactly with every fraction Mᵢⱼ/D.
Support dimensions before successive peels are [4, 3, 2, 1, 0]. Every nonterminal step strictly
decreases the dimension. The five-term output meets the general bound for n=3, but this does
not establish that five is the minimum for this particular input.

How the dimension is computed exactly
Let k be the number of positive entries and c the number of connected components of the
bipartite support graph. There are no isolated vertices. On the allowed k coordinates, row/column
equations have rank 2n−c: a dependence of their coefficients has the form αᵢ+βⱼ=0 on every
support edge, giving one free parameter per connected component and no others. Therefore their
solution space has dimension k−2n+c.

The current matrix is strictly positive on every allowed coordinate. Any sufficiently small
perturbation in a homogeneous row/column-sum direction remains positive there, so the
zero-pattern set has exactly that affine dimension. The audit computes k and c by counting entries
and graph traversal, and checks descent at every iteration. No floating-point rank threshold is
used.

For n=1 the dimension is 0 and the only doubly stochastic matrix is [1]. A support consisting of n isolated matched
edges also has dimension 0 and gives a single permutation matrix. These boundaries are included in the
executable checks.

<PARSED TEXT FOR PAGE: 5 / 6>

CYCLE 09 / 05


Executed exact verification
Independent input generation, rational reconstruction and bounded scope

 n        Integer row/column mass D                     Grid inputs                Largest observed terms

 1        1                                             1                          1

 2        1,…,8                                         44                         2

 3        1,…,5                                         433                        5

 4        1,…,3                                         2,314                      3


2,792 integer-grid inputs passed. Rows are generated as all nonnegative integer compositions
of D with column residual capacities; the final row is forced. This enumerates every integer matrix
with the stated row/column masses, without generating inputs by assuming a permutation
decomposition. Dividing by D produces the rational input. Different denominators can represent
the same rational matrix; uniqueness of rational inputs is not claimed.

Checks on each input and each peel
The program validates nonnegativity, square shape and all row/column sums; checks Hall’s
inequality for every subset of rows; chooses a supported permutation by exhaustive permutation
search; subtracts the exact minimum positive mass; and verifies the residual invariants and strict
support-dimension descent. After termination, an independent entrywise sum using
fractions.Fraction reconstructs the input exactly. It checks positive weights, weight sum 1, distinct
permutation terms, both term bounds, and the one-term/permutation/dimension-zero boundaries.

Additional stress inputs and negative controls
A fixed seed 20261116 generates 40 known convex mixtures in each dimension n=3,4,5, for 120
additional algorithm stress inputs. Such inputs are known to be representable by construction and
are not independent evidence of the existence theorem. Maximum returned term counts were
5,10,17, respectively. They meet the general upper bounds for these dimensions; no
minimum-support optimality is asserted.

Four invalid-input controls were rejected: a merely row-stochastic matrix, a matrix with negative entries despite
row/column mass1, a zero matrix with requested positive mass, and an empty matrix. One Python verifier process
exited0 with empty stderr. All mathematical arithmetic used integers and exact fractions. Exact inputs,
decompositions, support dimensions, commands and UTC execution times are preserved.

The enumeration and direct reconstruction are different checking routes but share one author and runtime. No
formal checker, external mathematical reviewer or cross-runtime replay was used. Finite results support the
implementation and explicit certificates, not the arbitrary-real theorem.

<PARSED TEXT FOR PAGE: 6 / 6>

CYCLE 09 / 06


Critique and research handoff
Classical result reconstructed; no novelty or certification claim

Attempts and vulnerabilities
A rational-only construction followed by an informal approximation step was avoided because
approximations must preserve all row and column constraints, and a finite decomposition limit
would need justification. The direct real-valued peeling argument eliminates that gap. The initial
zero-count bound was strengthened by explicitly proving strict affine-dimension descent. These
are reasoning choices and revisions, not failed executable runs; the recorded audit passed on its
first run.

Matching: positive support, not arbitrary positions, must admit a perfect matching.
Normalization: ε=1 is terminal; division by1−ε is used only otherwise. Weights: substitution
preserves positivity and total1. Dimension: the newly zero coordinate is nonconstant because
Aₑ<1=Pₑ. Extremality: distinct terms are required for the nontrivial convex combination.
Optimality: attaining the universal bound in an algorithm run does not prove minimal term count
for that input. Scope: real inputs are handled by the written proof; only rational grids and samples
were executed.

Sources checked
[1] Stanford EE384X, Packet Switch Architectures I, handout H12, “Birkhoff–von Neumann Decomposition
Theorem,” especially printed slides2–3. Stanford course handout. Consulted for the classical theorem,
support-matching peeling mechanism, and the standard n²−2n+2 upper bound.

[2] Fanny Dufossé, Kamer Kaya, Ioannis Panagiotas and Bora Uçar, “Further notes on Birkhoff–von Neumann
decomposition of doubly stochastic matrices,” Linear Algebra and Its Applications554(2018),68–78,
DOI10.1016/j.laa.2018.05.017. Institutional publication record and abstract. Consulted for the distinction between
valid greedy decompositions and minimum-term decompositions. The full article was not reviewed.

Conclusion and next independent check
CANDIDATE PROOF. The theorem, term bound and extreme-point characterization are reconstructed completely.
Highest-value review targets are the support-matching proof and the proper-hyperplane dimension drop. No
novelty or independent mathematical validation is claimed. Recompute with python3 verify.py fresh_results;
rebuild with python3 build.py. The ZIP retains exact certificates, scripts, proof text, critique, execution logs,
environment, source evidence and SHA-256 manifest. Rendered QA images remain local intermediates; the archive
digest and later save receipts are external to avoid circular hashing.


