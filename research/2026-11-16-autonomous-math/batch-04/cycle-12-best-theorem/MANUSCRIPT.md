# Cycle12 — BEST theorem with a fixed first labeled arc

Grounded DI LLC · Mark S. Weinstein · Series MWR-20261116-24H

**CANDIDATE PROOF — classical theorem reconstruction.** This is a new public mathematical edition derived from the original report and proof text, not the original PDF or a claim of a new theorem.

## The BEST theorem - precise scope

For every finite directed multigraph G=(V,E) with |V|≥2, assume that G is strongly connected, has no loops, and has equal positive indegree and outdegree d(v) at every vertex v. Parallel arcs are allowed and individually labeled. Fix an arc e with tail r. Let ECₑ(G) count ordered lists of all arcs, starting with e, following their directions, using every labeled arc exactly once, and returning to r.

An in-arborescence rooted at r chooses one outgoing arc at each v≠r, none at r, such that repeatedly following chosen arcs reaches r from every vertex. Let tᵣ(G) count these choices. The assertion is:

$$\operatorname{EC}_e(G)=t_r(G)\prod_{v\in V}(d(v)-1)!.$$

Tours are linear arc lists with the first labeled arc fixed. Neither reversal nor a relabeling of parallel arcs is identified. The classical theorem is reconstructed here; no mathematical novelty is claimed.

## Why this investigation is worthwhile

A global traversal problem factors into a spanning-tree choice and local permutations. The subtle step is proving that local instructions cannot finish a small closed trail while leaving arcs unused. That step makes a useful target for both adversarial proof review and exhaustive inverse-map tests.

Example tour: 0→1→0→2→1→2→0. The arcs 1→2 and 2→0 are the final departures from the nonroot vertices; they point toward root 0. For this bidirected triangle, t₀=3 and EC₍₀→₁₎=3.

## A complete model-written combinatorial proof within the stated scope

## 1. Extract a rooted tree from a tour

Take an Euler tour starting with e at r. For each v≠r, select its last outgoing arc, and write ℓ(v) for that departure’s position in the arc list. If the selected arc goes from v to w≠r, then after arriving at w the tour must depart w again: its terminal vertex is r. Consequently ℓ(w)>ℓ(v). A directed cycle of selected arcs would give a cyclic chain of strict inequalities, which is impossible.

Every nonroot has one selected outgoing arc and the root has none. A path following selected arcs either reaches r or eventually repeats a vertex. Repetition would create a directed cycle, already excluded. Thus these arcs form an in-arborescence. The tour also gives a linear order of outgoing arcs at each vertex, with the tree arc last at every nonroot and e first at r.

## 2. Reconstruct the tour from local orders

Conversely, choose any in-arborescence T toward r. At each nonroot v, order all outgoing arcs with the chosen tree arc last. At r, order all outgoing arcs with e first. Start at r and repeatedly traverse the next unused arc in the current vertex’s order. Stop only when the current vertex has no unused outgoing arc. Each step uses a new arc, so the process terminates after at most |E| steps.

It cannot stop at w≠r. At the end of a trail from r to w≠r, the number of arrivals at w exceeds departures by one. If all d(w) outgoing arcs had been used, there would be d(w)+1 used incoming arcs, contradicting indegree d(w). The maximal trail therefore ends at r and is closed.

## 3. Rule out a premature closed trail

For a closed trail, used arrivals and departures agree at every vertex. Since full indegrees and outdegrees also agree, unused arrivals and departures agree at each vertex. Suppose some outgoing arc remains unused at v. The stopping condition excludes v=r. At a nonroot, any unused outgoing arc implies that its last-in-order tree arc is unused.

Follow this unused tree arc to w. Vertex w now has an unused incoming arc, hence an unused outgoing arc. Repeat along the unique tree path toward r. Eventually r has an unused outgoing arc, contradicting the stopping condition. This argument includes vertices that the partial trail never visited. Therefore every arc was traversed, and the resulting list is an Euler tour starting with e.

## 4. The maps are inverses

The reconstructed tour uses each vertex’s outgoing arcs in exactly the prescribed order. Its extracted last exits are exactly T. Conversely, following the orders extracted from a given tour recovers that tour step by step. Thus no two distinct tree/order data produce the same arc list, and no arc list is omitted.

## The factorial factors and the directed determinant both have explicit proofs

## Counting the local choices

For each fixed tree, the last outgoing arc at a nonroot v is prescribed, leaving (d(v)−1)! orders. At r the first arc e is prescribed, also leaving (d(r)−1)! orders. These choices are independent across vertices. Multiplying, then summing over the tᵣ trees, proves the formula. Strong connectivity ensures tᵣ>0: for each v≠r choose the first arc on a shortest directed path from v to r; distance to r strictly decreases.

## A self-contained directed Matrix-Tree argument

Let Aᵥw count labeled arcs v→w, and let L=diag(d)−A be the row-outdegree Laplacian. Delete row and column r to obtain Lʳ. For each remaining vertex v let bᵥ be its coordinate unit row vector, and define bᵣ=0. Row v of Lʳ is the sum, over its outgoing labeled arcs v→w, of $b_v-b_w$.

Multilinearity of the determinant expands det Lʳ into a sum indexed by one chosen outgoing arc at each nonroot. If a choice contains a directed cycle, its cycle rows sum to zero, so its determinant contribution is zero. Otherwise every chosen path reaches r. Order the nonroot vertices by increasing distance to r in this chosen tree. With rows and columns reordered together, each row has diagonal entry 1 and its only possible other entry−1 in an earlier column. The matrix is triangular with determinant1. Simultaneous row/column permutation does not change the determinant.

Every choice either has a directed cycle or reaches r. Hence precisely the tᵣ in-arborescences contribute1, proving **det Lʳ=tᵣ**. Parallel arcs appear as separate summands, preserving multiplicity. This algebraic argument is included to avoid taking the determinant checker as an unexplained oracle.

## Convention controls

If only the starting vertex r is fixed, partition the tours by their first arc. There are d(r) possible first arcs and the formula gives the same count for each, so the count is d(r)ECₑ. For cyclic tours modulo rotation, each orbit contains exactly one list beginning with a specified labeled arc: that arc occurs once. Thus the fixed-arc convention also counts cyclic rotation classes. No extra |E| factor belongs in the stated formula.

## Bounded exact computation supports the reconstruction; it is not the general proof

The original scope is all 4164 loopless simple-digraph masks on n=2,…,4, of which125 are balanced and strongly connected, plus8 labeled-multigraph controls. Checks cover515 root cofactors,876 fixed-first-arc cases and 15024 tours, including complete set equality and inverse-map tests. The two-vertex parallel-arc and directed-cycle controls exercise multiplicity; one control exercises unequal vertex degrees.

Direct search extends unused incident arcs recursively and records only full closed tours. The construction route independently enumerates rooted parent choices and permitted local permutations. Both store complete tour sets, not just totals. A third calculation uses Fraction Gaussian elimination on the reduced Laplacian. Every input arc list, root count and tour certificate is saved.

## Distinct adversarial review

All checks were authored by the same model and run in the same environment. Distinct algorithms reduce shared-path mistakes but do not supply an independent external review. No counterexample was found in the precisely bounded test domain.


## Outcome and attempted approaches

The investigation produced a complete model-written proof of the fixed-first-arc BEST formula, plus a determinant proof for its rooted-tree factor. The initial tempting shortcut was “balanced degrees force the traversal to use every arc.” Balance only prevents stopping away from the root; it does not prevent an early return. The revised argument explicitly propagates unused arcs along reserved last exits to force a contradiction at the root.

The count was also reviewed against the wrong-root-factor alternative. The two-vertex, two-parallel-arcs control gives 2 tours with a fixed first arc but 4 when only the start vertex is fixed. These are different counting questions. The original investigation recorded two verifier runs with exit0 and empty stderr. Two attempts to open the Grinberg lecture PDF timed out; that unverified document is not used as a substantive source.

## Source grounding

[1] Matthew Farrell and Lionel Levine, *Multi-Eulerian tours of directed graphs*, arXiv:1509.06237v1 (2015), Theorem1. The retrieved primary research paper states BEST for a fixed first edge and trees oriented toward its tail, agreeing with the convention used here. https://arxiv.org/html/1509.06237v1

[2] Yang Ming-Tian, *BEST Theorem*, Nagoya University Special Mathematics Lecture (June5,2024), pp.1-3. This authored exposition discusses the last-exit construction and the distinction between tours with and without a fixed starting vertex. https://www.math.nagoya-u.ac.jp/~richard/teaching/s2024/SML_Yang_1.pdf

These targeted source checks establish classical attribution and counting conventions. They are not a substantive novelty review or an external validation of this newly written proof. Loops, one-vertex graphs, unbalanced graphs and unidentified parallel arcs are outside this report’s formal scope.

## Public reproduction and evidence

Python3 standard library only; assertions must remain enabled (do not use `-O`). From this investigation directory run:

```bash
python3 verify.py fresh_results
```

The public script is unchanged from the original mathematical verifier. Every exact input and certificate it emits is included in `results/`; actual publication stdout, stderr and commands are included with timestamps in the batch `VERIFICATION.json`. Run `python3 verify_all.py` from the parent batch directory to check the SHA-256 inventory and compare fresh outputs against all published result JSON files.

`PROVENANCE.json` retains source report/package identities, original archive digest, member hashes and corrected/legacy labels. The original mixed operational archive and report-building environment are not published. References above describe source checks recorded in the original investigation; publication replay does not represent a new literature review or external endorsement.

The complete model-written proof and finite computations remain distinct. Different implementations share authorship and execution environment; none is a formal proof assistant or an independent external referee. Classification remains CANDIDATE PROOF.
