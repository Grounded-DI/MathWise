# Cycle13 — Vertex-disjoint directed tree arcs can be positively correlated

Grounded DI LLC · Mark S. Weinstein · Series MWR-20261116-24H

## Precise conjecture

For every finite strongly connected simple digraph G=(V,E), assume every vertex has equal indegree and outdegree, each at least two. Simple means no loops or repeated ordered pairs; opposite arcs are allowed. Fix a root r and select uniformly a spanning in-arborescence T toward r: each nonroot has exactly one outgoing arc, the root has none, and every chosen path reaches r.

For every pair e=(a,b), f=(c,d) whose four endpoints are distinct and avoid r, the conjecture asserts P(e,f∈T)≤P(e∈T)P(f∈T). If N counts all trees and A,B,C count e,f,both, respectively, this is CN≤AB.

## Five-vertex witness and complete certificate

Use V={0,1,2,3,4}, root0, and both directions of each edge of the cycle0–1–2–3–4–0. Mark e=1→2 and f=3→4. Every vertex has indegree=outdegree=2; the digraph is simple and strongly connected. All four marked endpoints are distinct and avoid the root.

Forgetting directions in any in-arborescence gives four distinct connected underlying edges: both directions of one edge would form a forbidden directed two-cycle. Hence it is a spanning tree of C₅, obtained by deleting one edge. Conversely any such path has exactly one orientation toward0. These maps are inverse.

| Deleted cycle edge | Rootward arcs | e present | f present |
|---|---|---|---|
| 01 | 1→2, 2→3, 3→4, 4→0 | yes | yes |
| 12 | 1→0, 2→3, 3→4, 4→0 | no | yes |
| 23 | 1→0, 2→1, 3→4, 4→0 | no | yes |
| 34 | 1→0, 2→1, 3→2, 4→0 | no | no |
| 40 | 1→0, 2→1, 3→2, 4→3 | no | no |

Thus N=5,A=1,B=3,C=1 and CN=5>3=AB. The covariance is1/5−(1/5)(3/5)=2/25>0. In fact e's presence implies f's presence.

The two underlying undirected edges each appear in four of the five trees, and jointly in three; their covariance is3/5−16/25=−1/25. Directed membership specifies rootward orientation as well as presence. It is a global path property, so transferring undirected negative dependence to these directed events is invalid.

## General cycle family

For n≥5 take the bidirected cycle on0,…,n−1 rooted0. Index undirected edges by k for {k,k+1}, modulo n. Each of its n rooted trees deletes exactly one edge k, uniformly. For integers1≤i<j≤n−2 with j≥i+2, choose e=i→i+1 and f=j→j+1. Their endpoints are disjoint and avoid0.

Arc i→i+1 occurs exactly when k<i: then the route to0 runs forward through n−1. If k=i its edge is absent; if k>i the route runs backward. Accordingly P(e)=i/n, P(f)=j/n and P(e,f)=i/n, giving covariance i(n−j)/n²>0. The five-vertex certificate alone refutes the universal conjecture; this written family argument is not a finite-check extrapolation.

## Verification and critique

The public original checker enumerates all outgoing parent assignments for n=5,…,10 and rejects directed cycles or paths not reaching0. A different route enumerates underlying spanning-edge subsets and orients them by breadth-first traversal from0; the complete tree sets agree. Exact rational reduced out-Laplacian cofactors cross-check all tree and forced-arc counts. Forcing an arc retains only that outgoing option at its tail; the marked tails are distinct and nonroot.

The scope is six cycle graphs,1008 parent assignments,45 underlying subsets,56 separated arc pairs and174 determinants. It is not an exhaustive search over arbitrary digraphs. The attempted undirected transfer fails because orientation events depend on the remainder of the tree. No smallest-order or global novelty claim is made.

## Reference

G. R. Grimmett and S. N. Winkler, [Negative association in uniform forests and connected graphs](https://arxiv.org/abs/math/0302185), v3 (2003). The original investigation consulted its abstract for undirected spanning-tree background only. That source is not attributed the directed conjecture, and does not externally validate this counterexample. The explicit five-tree proof above is self-contained.

## Status and reproduction

**COUNTEREXAMPLE FOUND.** This refutes the precisely stated experiment conjecture. No historical novelty, minimality, external certification or formal proof-assistant validation is claimed. The proof text is model-written; the finite certificates and exact program runs are separate supporting evidence. All implementations share authorship and execution environment.

The public `verify.py` is byte-identical to the corresponding original source checker. It uses only Python's standard library. Run from this directory:

```bash
python3 verify.py fresh_results
```

The checked-in `results/` directory contains actual output from the publication run. `PROVENANCE.json` identifies source reports, archives, original SHA-256 values and corrected/legacy numbering. This manuscript is a new mathematical edition; the original mixed archive is not published.
