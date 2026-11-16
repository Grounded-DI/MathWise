# Dilworth — source report text

**Classification: CANDIDATE PROOF** (not externally or formally verified). Original report: `MWR-20261116-24H_Cycle05_Dilworth_Report.pdf`. Source ZIP SHA-256: `05b5c100997b2941a6023c155e6a5dd2272571834ed1b2abc992a6c14b5fabf5`.

**Publication transformation:** text extracted from the entire source PDF; selected private operator/header labels omitted; text typography and layout do not reproduce the PDF exactly. This is not the original ZIP proof manuscript byte stream. See [Batch 02 index](../README.md) for verification and limitations.

---

<PARSED TEXT FOR PAGE: 1 / 6>

CYCLE 05 / 01


Order from two directions
Established theorem investigation | Dilworth’s finite chain decomposition theorem

The result under investigation
For every finite partially ordered set P, the largest number of pairwise incomparable elements
equals the smallest number of disjoint chains needed to partition P. This cycle reconstructs a
complete proof through bipartite matching and gives explicit finite certificates for both sides of
the equality.

maximum antichain = minimum chain partition

Boolean lattice B₃: subsets of {1,2,3} ordered by inclusion. Colored paths form three chains; the ringed
singletons form a three-element antichain. Labels list subset elements. Dashed links, if present, skip a level but
remain comparable.

Finding and classification
CANDIDATE PROOF. The written argument is complete and human-checkable. Exact finite
tests agree across antichain enumeration, chain-partition dynamic programming, matching
dynamic programming and an augmenting-path construction. This cycle does not claim a
formally checked or externally reviewed proof. The theorem is classical; no mathematical
novelty is claimed.

<PARSED TEXT FOR PAGE: 2 / 6>

CYCLE 05 / 02


The reduction to matching
Definitions, quantifiers and the first exact identity

Definitions and boundary cases
A finite poset is a finite set P with a reflexive, antisymmetric, transitive relation ≤. Write x < y
for x ≤ y and x ≠ y. A chain is a subset whose elements are pairwise comparable. An antichain
has no two distinct comparable elements. A chain partition consists of pairwise disjoint
nonempty chains whose union is P. Let n = |P|, width w(P) be the maximum antichain size, and
c(P) the minimum number of chains. For the empty poset both are 0.

Every antichain meets each chain in at most one element, so w(P) ≤ c(P). The substantive task
is the reverse inequality. Finiteness guarantees that all extrema used below exist.

A bipartite graph with two copies of P
Let L = {x : x∈P} and R = {x : x∈P}. Put an edge x y exactly when x < y. Use the full strict
            L                       R                    L R
order, not merely cover relations in a Hasse diagram. A matching is a set of edges with no
shared endpoints. Let ν be the largest matching size.

A chain partition yields a matching
Given a partition into k chains, list each chain increasingly and match consecutive elements x
                                                                                                   L
to y . No left or right copy is used twice. A chain of t elements contributes t - 1 matching edges,
    R
so the matching has n - k edges. Consequently k ≥ n - ν, and c(P) ≥ n - ν.

A matching yields a chain partition
For each matched pair x y , draw the directed link x→y on P. Every vertex has at most one
                              L R
incoming and one outgoing link. A directed cycle is impossible because each link is strictly
increasing. A finite directed graph with these degree bounds and no cycles is a disjoint union of
directed paths, including isolated vertices. Transitivity makes each path a chain. With ν links
there are n - ν paths. Hence c(P) ≤ n - ν.

Identity 1: c(P) = n - ν. This argument uses only strict-order properties; it does not invoke
Dilworth’s theorem or a vertex-cover theorem.

<PARSED TEXT FOR PAGE: 3 / 6>

CYCLE 05 / 03


A cover from alternating paths
A self-contained proof of the matching–cover equality needed here

In a bipartite graph (L,R,E), a vertex cover is a set of vertices meeting every edge. Any cover has
at least as many vertices as any matching: the disjoint matching edges require distinct covering
vertices. We now construct a cover of size ν from a maximum matching M.

Reachability rules
Start at all unmatched left vertices U. Traverse nonmatching edges from L to R, and matching
edges from R to L. Let ZL and ZR be the reached vertices on the two sides. If an unmatched right
vertex were reached, a shortest directed path from U to it would be a simple alternating path,
starting and ending with nonmatching edges. Flipping membership in M along that path would
increase the matching size by one, a contradiction. Thus every reached right vertex is matched.

The proposed cover
Set C = (L ∖ ZL) ∪ ZR. To show C covers all edges, take xLyR. If xL is not reached, it lies in C. If xL
is reached and the edge is unmatched, the traversal rule reaches yR. If the edge is matched and
x is reached, then x cannot be a starting vertex, since starting vertices are unmatched. Its
 L                      L
incoming traversal is its unique matched edge, so its matched partner y is reached. Therefore
                                                                                   R
every edge meets C.

Count the cover without double counting
For each matched pair, its right endpoint is reached if and only if its left endpoint is reached.
One implication is the matching traversal rule; the converse was established in the previous
paragraph. If both endpoints are reached, the right endpoint alone is in C. If neither is reached,
the left endpoint alone is in C. Thus exactly one endpoint of each matched edge belongs to C.

No unmatched vertex belongs to C: every unmatched left vertex starts the search and is
reached; no unmatched right vertex is reached. It follows that |C| = |M| = ν. Together with the
lower bound, this proves that a minimum vertex cover has size ν. The argument is constructive
and includes the case M empty.

Dependency audit
The only optimality implication used was that a maximum matching cannot have an augmenting path, proved
directly by flipping the path. The converse augmenting-path theorem is unnecessary for this written proof. The
executable solver’s optimality is checked separately against exact subset dynamic programming.

<PARSED TEXT FOR PAGE: 4 / 6>

CYCLE 05 / 04


Extracting the antichain
Completing the proof and inspecting a concrete certificate

Return to the bipartite graph of the poset. Let C be the size-ν cover constructed on page 3.
Define A to consist of the elements x∈P for which neither xL nor xR lies in C. At most |C| different
labels are excluded, since each excluded label has at least one copy in C. Therefore |A| ≥ n - ν.

The set A is an antichain. If x < y held for x,y∈A, then xLyR would be an edge with neither
endpoint in C, contradicting the cover property. Thus w(P) ≥ |A| ≥ n - ν. Combining this with
pages 2 and the elementary lower bound yields:

w(P) ≤ c(P) = n - ν ≤ |A| ≤ w(P).
All inequalities must be equalities. This proves w(P) = c(P) for every finite poset, including the
empty one. It also constructs both an optimal chain partition and an optimal antichain from a
maximum matching.

The eight-element Boolean lattice example
For P = 2{1,2,3} ordered by inclusion, the exact audit gives ν = 5 and n - ν = 3. The diagram on
page 1 displays the constructed chain partition and a maximum antichain. Integer labels in the
JSON certificate are bitmasks: bit i represents membership of i + 1.

 Certificate                                 Exact preserved value

 Matching links                              [[0, 1], [1, 3], [2, 6], [3, 7], [4, 5]]

 Chain partition (bitmasks)                  [[0, 1, 3, 7], [2, 6], [4, 5]]

 Maximum antichain (bitmasks)                [1, 2, 4]

 Cover left / right                          [0, 1, 2, 4] / [7]


The independent chain-partition DP may return a different optimal partition from the matching construction;
equality of optimal values is required, not equality of arbitrary witness choices. Every returned witness is
checked against the original relation.

<PARSED TEXT FOR PAGE: 5 / 6>

CYCLE 05 / 05


The finite audit
Exact computation supports the argument without replacing the general proof

For each n = 0,…,6, enumerate every subset of the ordered pairs (i,j) with 0 ≤ i < j < n. Retain
exactly those satisfying transitivity. These are all strict posets compatible with the chosen
natural linear extension. Any finite poset can be relabeled along a linear extension: repeatedly
remove a minimal element, which exists in every nonempty finite poset because a descending
chain cannot continue forever. Thus every isomorphism type through six elements occurs;
arbitrary labelings are not all separately enumerated.

 n             Relation subsets                             Transitive orders checked

 0             1                                            1

 1             1                                            1

 2             2                                            2

 3             8                                            7

 4             64                                           40

 5             1024                                         357

 6             32768                                        4824


Four exact methods and certificate checks
For every retained order, enumerate all subsets to find a maximum antichain; enumerate chain
subsets and use a subset DP to minimize the number of disjoint chains; use a separate
left-vertex/right-subset DP to maximize matching size; then construct a matching with
augmenting paths and derive its cover, paths and antichain. Assertions require agreement of
the four optimal values and verify coverage, chain comparability, antichain incomparability,
matching size and the exact label partition.

Executed: 5,232 orders plus B₃, all passing. Arithmetic uses integers only. The run exited 0 with
empty stderr. Full per-order certificates, input relation masks, result summaries, command,
timestamps and environment are retained. There was one computational run, not an asserted
cross-runtime replay. Distinct methods share the same assistant, Python process and relation
representation.

What this establishes
The finite computation found no discrepancy within its declared exhaustive scope. It verifies the explicit
certificates and catches many reduction errors, but does not establish the theorem for arbitrary n, prove the
implementation correct in all cases, or certify the written proof. Those limits are why the cycle remains
CANDIDATE PROOF.

<PARSED TEXT FOR PAGE: 6 / 6>

CYCLE 05 / 06


Adversarial review and handoff
Critical review, attempted routes, sources and evidence boundaries

Potential gaps tested in the reasoning
Circularity: the proof establishes the matching–cover equality rather than citing Dilworth to
obtain it. Missing transitive edges: the bipartite graph uses every strict comparison. Using
only Hasse edges is not justified here. Matched-edge reachability: this case is treated
separately; traversing only unmatched edges forward would otherwise leave a gap in cover
correctness. Duplicate labels in a cover: the extraction initially gives |A| ≥ n - |C|, not
equality by assumption. The closing inequality chain proves equality. Cycles: path
reconstruction uses strict order, not merely the degree bounds. Empty input: all extrema and
constructions return zero.

Attempts and revisions
A direct greedy chain-removal proof was considered and abandoned as an unproved approach:
removing an arbitrary long chain need not visibly decrease width by exactly one. This was a
reasoning-level dead end, not an executed search. The matching route was chosen to expose
checkable primal and dual certificates. During critique, the proof was expanded to include the
matched-edge reachability case and the label-count inequality. No failed numerical result was
suppressed; none occurred in the executed audit.

Sources and source-access limits
The classical statement and the existence of a separate formal development were checked against the primary
Archive of Formal Proofs entry, “Formal Proof of Dilworth’s Theorem”, by Vivek Soorya Maadoori and coauthors,
dated March 25, 2025. That development describes a Perles-based proof. This cycle instead supplies a
matching-based reconstruction; the AFP development was not executed and does not certify this argument.

R. P. Dilworth, “A Decomposition Theorem for Partially Ordered Sets,” Annals of Mathematics 51(1), 1950, pp.
161-166, was identified through search metadata. Two university-hosted PDF endpoints failed (502 and timeout);
their full text was not reviewed. The retained source record preserves those failures. No novelty review was
attempted, and no novelty is claimed.

What to review next
The most valuable independent check is the complete alternating-path cover proof and the conversion of a
two-copy cover into an antichain. The evidence ZIP contains this proof text, exact verifier, all 5,232 certificates,
the B₃ certificate and graphic, executed logs, source-access record and a SHA-256 manifest. This is
consequential mathematical work preserved for inspection, not a formal certification claim.


