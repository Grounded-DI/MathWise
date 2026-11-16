# Three-rank chain repair — source report text

**Classification: CANDIDATE PROOF** (not externally or formally verified). Original report: `MWR-20261116-24H_Cycle08_Chain_Repair_Report.pdf`. Source ZIP SHA-256: `87355278cbe6a75b04d8fe80331d678d16cdaf50b89230b9bcfc197cfee34dd2`.

**Publication transformation:** text extracted from the entire source PDF; selected private operator/header labels omitted; text typography and layout do not reproduce the PDF exactly. This is not the original ZIP proof manuscript byte stream. See [Batch 02 index](../README.md) for verification and limitations.

---

<PARSED TEXT FOR PAGE: 1 / 6>

CYCLE 08 / 01


Repairing symmetric chains
Newly formulated repair investigation | Complete model-written candidate proof

Precise conjecture
For every finite pure graded poset P with three nonempty ranks A,B,C of sizes (a,b,a), where 1 ≤ a
≤ b, a symmetric saturated chain decomposition exists if and only if the largest union of two
antichains has size a+b. Connectivity is not required. “Pure graded” means every maximal chain
has one element in each of ranks 0,1,2.

A chain is saturated if consecutive elements are covers. It is symmetric if its endpoint ranks sum
to 2. The only allowed symmetric blocks are full rank-0–1–2 chains and singleton middle elements.
Antichains consist of pairwise incomparable elements. Equalities concern actual element counts,
not probabilities.

A quantitative candidate identity
Let n = 2a+b, U₂(P) be the largest union of two antichains, and F(P) the maximum number of
vertex-disjoint full chains. The argument below establishes the stronger identity U₂(P) = n −
F(P). Consequently U₂(P) − (a+b) = a − F(P), giving both the criterion and an exact packing
deficit.

Two recomputed controls with ranks (3,6,3). Cycle06’s failed weak criterion has F=2 and U₂=10. The complete
three-rank control has F=3 and U₂=9. The present repair excludes the first and accepts the second.

Status: CANDIDATE PROOF. Complete human-checkable reasoning and exhaustive finite checks are provided.
No formal checker or external reviewer verified the proof. This is a new formulation within the experiment, derived
using classical min-max ideas; no global novelty is claimed.

<PARSED TEXT FOR PAGE: 2 / 6>

CYCLE 08 / 02


From antichains to separators
The first identity requires no flow theorem

Define the hitting number
Let K(P) be the smallest size of a vertex set D meeting every full chain x < y < z with
x∈A,y∈B,z∈C. Such a set always exists: D=A works, so K ≤ a. We will first prove U₂ = n−K, then
prove K=F constructively.

A union of two antichains contains no full chain
Any three-element chain has at most one element in each of two antichains, so their union cannot
contain a full chain. Therefore the complement of any union T of two antichains meets every full
chain. This gives K ≤ n−|T| and hence U₂ ≤ n−K.

Every full-chain-free subset is a union of two antichains
Let D be a minimum hitting set and S=P∖D. It contains no three-element chain: any such chain in
this three-rank poset necessarily has ranks 0,1,2 and would be a full chain missed by D. Partition S
into its minimal elements L and the remaining elements R. Here “minimal” is in the induced order
on S, not merely rank 0 in P.

L is an antichain by minimality. R is also an antichain: if x < y were in R, then x is nonminimal in S,
so some z∈S satisfies z < x. The three distinct elements z < x < y would form a forbidden
three-element chain. Thus S=L∪R is a union of two antichains, with size n−K. This gives U₂ ≥ n−K
and proves the identity.

Why this repairs Cycle06’s question
The ordinary Sperner property controls only one antichain, and Cycle06 showed it can miss a
full-chain obstruction. The present condition controls a union of two antichains. Since A∪B is
already such a union, U₂ ≥ a+b always. The proposed threshold says that no larger union occurs,
equivalently that every full-chain hitting set has at least a elements.

The partition argument above is the height-two case of a classical chain/antichain duality, but it is proved directly
here. It does not rely on the separate Cycle05 proof of Dilworth’s theorem, nor on its validation status.

<PARSED TEXT FOR PAGE: 3 / 6>

CYCLE 08 / 03


A complete flow argument
Integral augmentations turn a separator bound into disjoint full chains

Split every poset vertex
Replace each v∈P by vin→vout of capacity 1. For every cover u<v, add uout→vin of capacity
M=n+1. Add a source s with capacity-M arcs to all xin for x∈A, and capacity-M arcs from all zout,
z∈C, to a sink t. These are finite integer capacities. Rank-0 and rank-2 vertices also have capacity
1; endpoint disjointness must be enforced.

The original network is acyclic. Each s–t path corresponds to exactly one full chain, and disjoint full
chains give a feasible integral flow of the same value. Conversely, an integral flow decomposes
into unit s–t paths: follow positive-flow arcs from s; conservation prevents a dead end, acyclicity
forces arrival at t, and subtracting one unit permits repetition. Vertex capacities ensure that the
resulting chains are vertex-disjoint.

Construct a maximum integral flow and equal cut
Start with zero flow. A residual forward arc has unused capacity; a residual backward arc permits
cancellation of existing flow. Whenever a residual s–t path exists, augment by the smallest
residual capacity on it. Capacities and flows stay integral, and the flow value increases by at least
1. The split arcs of A bound every flow value by a, so this process terminates after at most a
augmentations.

At termination, let R be all vertices reachable from s in the residual network. Then s∈R and t∉R.
Every original arc from R to its complement is saturated. Every original arc into R from outside has
zero flow, since positive flow would give a backward residual arc leaving R. Summing conservation
over R shows that the flow value equals the total capacity of this cut. Any feasible flow has value
at most any cut capacity by the same conservation identity, so the terminal flow is maximum.

The cut consists only of split-vertex arcs
Its capacity equals the terminal value, at most a. Since M=n+1>a, none of the cut’s forward arcs
can have capacity M. Each is therefore a capacity-1 split arc v →v . The corresponding set D of
                                                               in  out
original vertices has size equal to the flow value and meets every full chain, because every
associated s–t path must cross the cut.

If f is this flow value, unit-path decomposition gives f≤F; sending one unit along every maximum chain packing
gives F≤f. The cut gives K≤f=F, while any hitting set must meet each of F disjoint chains at distinct vertices, giving
K≥F. Hence K=F. This is the required classical vertex-path min-max argument [1], with its needed proof included.

<PARSED TEXT FOR PAGE: 4 / 6>

CYCLE 08 / 04


Resolve the repair conjecture
The equivalence and defect formula follow exactly

Combine the two identities
Pages 2 and 3 give U₂ = n−K = n−F = 2a+b−F. Since every full chain uses a distinct rank-0
element, F≤a. Thus U₂≥a+b, and the conjectured equality U₂=a+b holds exactly when F=a.

Full packing is equivalent to symmetric decomposition
An SCD must place each rank-0 element in a chain ending at rank 2. Saturation forces one middle
element, so it contains exactly a disjoint full chains. Therefore an SCD implies F=a. Conversely, if
F=a, these chains cover all a bottom and a top elements, and a distinct middle elements. The
remaining b−a vertices are all in the middle rank. Taking them as singleton chains yields an SCD.
This proves the claimed equivalence.

A precise deficit, not an edit-distance claim
The identity also gives U₂−(a+b)=a−F. The left side is how far the two-antichain union exceeds
the target; the right side is the number of full chains missing from a perfect bottom-to-top
packing. This does not claim that this many vertex or edge edits can repair the poset. That is a
different problem and was not investigated.

Controls and boundary cases

 Control, ranks (3,6,3)                                     F          K         U₂              SCD

 Cycle06 obstruction                                        2          2         10              no

 Complete cover matrices                                    3          3         9               yes


The first control has the same two-vertex separator {a0,c0} as Cycle06; it satisfies the ordinary
Sperner property but fails the repaired antecedent. The second connects every bottom vertex to
every middle vertex and every middle vertex to every top vertex. Both were recomputed in this
cycle, not accepted merely from prior prose.

When a=1, one full chain plus middle singletons is forced by purity. When b=a, there are no singleton leftovers.
The proof also allows a disconnected Hasse diagram; connectivity is unnecessary. Empty ranks and heights other
than two lie outside the precise statement. The result concerns three ranks, with highest rank 2, not
arbitrary-height strongly Sperner posets.

<PARSED TEXT FOR PAGE: 5 / 6>

CYCLE 08 / 05


Executed finite verification
Four independent algorithmic routes within one author/runtime

 a      b      Matrices per side           Posets                  With SCD               Without SCD

 1      1      1                           1                       1                      0

 1      2      1                           1                       1                      0

 1      3      1                           1                       1                      0

 1      4      1                           1                       1                      0

 2      2      7                           49                      49                     0

 2      3      25                          625                     625                    0

 2      4      79                          6,241                   6,241                  0

 3      3      265                         70,225                  61,009                 9,216


Exhaustive total: 77,144 cover-matrix pairs. For each middle vertex, a nonzero bitmask
specifies its lower neighbors and another its upper neighbors. The OR of each side’s masks must
cover all outer-rank vertices. These conditions enumerate exactly all pure graded cover matrices
for the listed rank sizes with fixed labels. Isomorphic inputs and relabelings may recur; no count of
isomorphism classes or independent trials is asserted.

Methods checked against one another
For every input: enumerate all antichains and all pairs to compute U₂ directly; use subset-state
dynamic programming to maximize disjoint full chains; enumerate candidate hitting sets directly;
and independently execute a residual augmenting-path flow algorithm. Assertions require
agreement of the packing, separator and flow values, validate actual flow-chain witnesses and
separator coverage, and verify U₂=n−F and the SCD criterion. For accepted instances, full chains
plus middle singletons are explicitly checked to cover all vertices.

The verifier stores compact exact inputs (neighbor masks), objective values, antichain-pair
witnesses, disjoint-chain witnesses, flow separators and a minimum hitting-set mask for every
exhaustive case. In the (3,3,3) rank case, 61,009 inputs admit an SCD and 9,216 do not; all satisfy
the identity.

Sixty fixed-seed checks use a=3 and b=3,4,5. Twenty lie in an already exhaustive domain; these are additional
checks, not necessarily new distinct posets. Two named controls have ranks (3,6,3). One Python process exited 0
with empty stderr. Arithmetic is integer-only. Distinct algorithms share the same assistant, runtime and input
representation; no formal or external verification is implied.

<PARSED TEXT FOR PAGE: 6 / 6>

CYCLE 08 / 06


Critique and research handoff
A new repair question resolved using classical min-max ingredients

Attempts, vulnerabilities and revisions
The previous width-only conjecture was already false. Simply finding independent matchings on
the two adjacent rank pairs does not by itself establish compatible full chains. This route was
discarded in favor of a single vertex-capacitated flow network. This is a reasoning-level discarded
approach, not an unrecorded failed numerical run. The repaired statement and stronger identity
were registered before executable checks.

Definitions: saturation and endpoint symmetry are explicit; only full chains and middle
singletons are allowed. Induced order: the two-antichain partition uses minimal elements of the
remaining subset. Endpoints: all poset vertices, including the outer ranks, have capacity1. Finite
capacities: M=n+1 exceeds the cut bound a, excluding big arcs from the minimum cut.
Integrality: it follows from integer residual augmentations, not a fractional-flow assumption.
Circularity: the antichain identity and path min-max argument are proved separately before
combining them.

Sources and novelty boundary
[1] Yann Disser, Algorithmic Discrete Mathematics, summer2024 notes, July16,2024, §§6.1–6.3, especially
Theorems6.15–6.18, printed pp.50–52. Author’s lecture notes. Consulted for classical residual-flow, integral path
decomposition and vertex-splitting background. The report includes the needed specialized argument.

[2] Andrew Lin, notes for Alexander Postnikov’s MIT18.212, Lecture17, March15,2019, pp.1–2, definitions and
Lemma3. MIT lecture PDF. Consulted for standard symmetric-chain terminology and the necessary forward
implication. No substantive novelty review was conducted; this repair formulation and its classical consequences
are not claimed as globally new.

Conclusion and strongest next check
CANDIDATE PROOF. The argument resolves the registered repair conjecture for the entire stated three-rank class
and derives the defect formula. Finite checks support the proof and implementation; they do not establish the
arbitrary-size theorem. The highest-value independent review is the unit-capacity treatment of endpoints,
extraction of a vertex-only cut, and decomposition of the integral flow. There was no proof assistant or external
reviewer.

Recompute with python3 verify.py fresh_results; rebuild with python3 build.py after preserving checks/. The
ZIP contains the proof text, exact verifier and certificates, input bounds, controls, logs, UTC timestamps,
environment, source evidence and SHA-256 manifest. The manifest excludes only itself; the archive digest and
later save receipts are external. All earlier cycle artifacts and index snapshots remain preserved.


