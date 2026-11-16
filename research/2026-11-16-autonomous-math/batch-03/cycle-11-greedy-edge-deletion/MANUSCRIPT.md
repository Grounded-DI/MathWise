# Cycle11 — Two-step greedy edge deletion need not maximize spanning trees

Grounded DI LLC · Mark S. Weinstein · Series MWR-20261116-24H

## Precise conjecture

For every connected finite simple undirected graph G on vertices {0,…,n−1}, n≥1, with m≥n+1 edges, delete exactly two edges while retaining connectivity and all vertices. Write τ(H) for the number of spanning trees, with τ(H)=0 when disconnected. At each step greedy chooses an edge e maximizing τ(H−e); ties use lexicographic order on ordered endpoint pairs (u,v), u<v. The conjecture says this always attains the maximum over all two-edge deletion sets. A connected deletion exists at both stages because the graph still has a surplus edge.

## Explicit witness

Let V={0,1,2,3,4} and

E={02,03,04,12,13,14,23}, where uv denotes the undirected edge {u,v}.

This is K₂,₃ with bipartition {0,1}|{2,3,4}, plus edge23. It is simple, connected, and has seven edges, satisfying m≥n+1.

A theta graph with three internally disjoint paths of lengths a,b,c has ab+ac+bc spanning trees: a tree deletes exactly two edges, one on each of two different paths. Each such deletion connects all vertices without a cycle; deleting both on one path leaves the other two paths forming a cycle.

| First deleted edge | Remaining structure | τ |
|---|---|---:|
| 23 | Theta lengths 2,2,2 | 12 |
| 02,03,12,13 | Theta lengths 1,2,3 | 11 each |
| 04,14 | Forced leaf edge and theta lengths 1,2,2 | 8 each |

For example, after deleting02 the theta endpoints are1 and3 and the paths are 1–3, 1–2–3 and 1–4–0–3. After deleting04, vertex4 is a leaf and the theta endpoints are2 and3. The remaining cases follow by swapping0↔1 and2↔3. Thus23 is the unique best first deletion.

Deleting23 leaves K₂,₃. Deleting any further edge gives a four-cycle with one pendant edge, hence exactly four spanning trees. The lexicographically chosen second deletion is02; every alternative tie also gives four.

Instead delete02 and13. The surviving graph is the five-cycle 0–3–2–1–4–0, with five spanning trees. Therefore greedy is strictly suboptimal.

## Exact global optimum

Any two deletions leave five edges on five vertices. A connected such graph is unicyclic: a spanning tree has four edges and the extra edge creates exactly one cycle. All noncycle edges are bridges, so its spanning trees correspond to deleting one cycle edge. The cycle length is at most five; therefore τ≤5. The displayed five-cycle attains five, proving OPT=5 and greedy/OPT=4/5.

The original graph has24 spanning trees, checked by subset enumeration, parent assignments and a reduced Laplacian determinant. This initial count is not needed for the elementary refutation.

## Extension and critique

Attaching k≥0 pendant vertices to vertex0 preserves every core tree count: all pendant edges are forced. Greedy never deletes a pendant bridge while a connected core deletion remains; any admissible optimal pair likewise avoids them. Thus the same obstruction exists for all n=5+k with ratio4/5. This is a written general argument; the executable search checks the five-vertex core rather than every extension.

The attempted exchange proof would need an optimal pair containing the uniquely best first edge23. Every pair containing23 yields four, whereas an optimum yields five, defeating that exchange. No worst-case approximation ratio, weighted extension or classification of failing graphs is established.

The original first parent-checker attempt failed because list and tuple endpoints were compared. The corrected checker uses tuple endpoints; the failed attempt remains in the private source archive. The public edition publishes the corrected mathematical checker and its fresh outputs. It enumerates tree subsets, independently counts parent assignments, and checks all29 reduced Laplacian cofactors (original, seven single deletions and21 pairs).

## Reference

David G. Wagner, [Combinatorics of Electrical Networks](https://www.math.uwaterloo.ca/~dgwagner/Networks.pdf), 2009, Theorem1, supplies the Matrix-Tree background for the determinant cross-check. The elementary theta/unicyclic proof above is self-contained. The original investigation also consulted the abstract of Li et al., [arXiv:1804.02785](https://arxiv.org/abs/1804.02785), which studies adding edges; it does not establish this deletion conjecture or its refutation.

## Status and reproduction

**COUNTEREXAMPLE FOUND.** This refutes the precisely stated experiment conjecture. No historical novelty, minimality, external certification or formal proof-assistant validation is claimed. The proof text is model-written; the finite certificates and exact program runs are separate supporting evidence. All implementations share authorship and execution environment.

The public `verify.py` is byte-identical to the corresponding original source checker. It uses only Python's standard library. Run from this directory:

```bash
python3 verify.py fresh_results
```

The checked-in `results/` directory contains actual output from the publication run. `PROVENANCE.json` identifies source reports, archives, original SHA-256 values and corrected/legacy numbering. This manuscript is a new mathematical edition; the original mixed archive is not published.
