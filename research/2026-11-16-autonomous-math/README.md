# MathWise Autonomous Research — November 16, 2026

**Grounded DI LLC | Public mathematical research register**

This is a curated index of independently labeled mathematical investigations from multiple overnight research threads. It is NOT a claim that one eight-cycle unattended run executed all items. Results retain their original evidence classifications.

## Release 1: Four finite counterexample investigations

### 1. Spanning-tree degree bound — COUNTEREXAMPLE FOUND
The conjecture was that for every finite connected simple bridgeless graph of minimum degree delta >= 3, every edge appears in at most 2/delta of spanning trees. Construct two disjoint K5 cliques, joined only by e=(a1,b1) and f=(a2,b2). The graph has 10 vertices, 22 edges and minimum degree 4, and no bridges. Exact count: 43,750 spanning trees, of which 28,125 contain e. Thus 9/14 > 1/2. Original: MathWise_Cycle_02_Degree_Bottleneck_Report.pdf. Separate exact enumeration, determinant and rational-current checks were reported. The finite witness refutes the formulated conjecture; no global novelty claim.

### 2. Symmetric-chain converse — COUNTEREXAMPLE FOUND
The formulated converse asserted that every connected rank-0/1/2 poset with symmetric unimodal rank sizes, full maximal chains and the Sperner property has a symmetric saturated-chain decomposition. The original 12-element poset has ranks (3,6,3), width 6 and no such decomposition: each full chain uses one of two designated middle elements, so at most two vertex-disjoint full chains are available when three are required. Original: MWR-20261116-24H_Cycle06_Symmetric_Chains_Report.pdf. The report records exhaustive 4,096 subset checks, 816 full-chain triples and exact-cover verification. The full original cover relation and verifier have not yet been mirrored in this release; do not treat this synopsis as a standalone replay package.

### 3. Quadratic zero-sum count — COUNTEREXAMPLE FOUND
For n=4, indexed residues (0,0,0,1,2,2,3) satisfy the multiplicity cap <=3 but have exactly 7 four-index subsets summing to 0 mod 4, below the proposed (n-1)^2 = 9. There are only 35 four-index subsets; direct counting gives three (0,0,2,2), three (0,0,1,3), one (1,2,2,3). Original: MWPRO-20261116-8H_Cycle02_Research.pdf. Its separate n>=5 conjecture remained UNRESOLVED in this investigation.

### 4. Independence-polynomial log-concavity — COUNTEREXAMPLE FOUND
The cycle conjecture asserted that independence-polynomial coefficients are log-concave for every finite simple graph. Its explicit 10-vertex graph has coefficients (1,10,17,4,1). Therefore 4^2 = 16 < 17*1 = 17. The original 28-edge list is encoded in the accompanying publication checker. Original: MathWise_Cycle_02_Independence_LogConcavity_Counterexample_Report.pdf. This is a counterexample to the cycle conjecture, not a historical novelty claim.

**Publication verifier:** [verify_three_witnesses.py](verify_three_witnesses.py) independently enumerates three explicit finite witnesses above. This is new release code, not an original sealed execution script or an assertion of independent external certification. The symmetric-chain case is omitted pending publication of the complete original cover relation.

## Other investigations — preserve candidate statuses
- Cayley/Pruefer — CANDIDATE PROOF (classical theorem reconstruction).
- Dilworth — CANDIDATE PROOF.
- Erdos-Ginzburg-Ziv — CANDIDATE PROOF; duplicate threads require provenance-preserving consolidation.
- Three-rank chain repair — CANDIDATE PROOF, independent review pending.
- Birkhoff-von Neumann — CANDIDATE PROOF (established theorem).
- Generalized Sperner / k-LYM — CANDIDATE PROOF (established theorem).
- Weighted spanning-tree correlation — CANDIDATE PROOF (established mathematics).
- Lucas — CANDIDATE PROOF (established theorem).
- Powers-of-3/4/7 MathWise Lab — UNRESOLVED infinite-tail certificate/replay question.

## Evidence and boundaries
The original research PDFs, frozen ZIPs, source ledgers, checksums and original execution outputs are NOT all mirrored by publishing this index. Public publication of this first register must not be confused with complete archival release. A hash verifies specified bytes, not mathematical truth, novelty or cross-runtime replay. Finite checks cannot prove arbitrary universal statements. No peer review or formal proof-assistant validation is claimed. Keep proprietary DI2/DIP architecture, patent documents, internal controls and unrelated private archives out of this repository.

**Research date:** November 16, 2026. **Publisher:** Grounded DI LLC. **Operator:** Mark S. Weinstein.


## Batch 03: Three additional exact counterexamples

[Batch 03 — manuscripts, executable original checkers and fresh verification results](batch-03/README.md) publishes three additional actual investigations from MWR-20261116-24H:

- **Current Cycle09 (historical Cycle12):** the specified lexicographic greedy Birkhoff decomposition uses nine terms while the certified optimum is four, refuting its proposed factor-two bound.
- **Current Cycle11:** two-step greedy edge deletion preserves four spanning trees while the global optimum preserves five.
- **Current Cycle13:** vertex-disjoint nonroot arcs of a bidirected five-cycle have positive covariance 2/25, refuting the formulated directed negative-correlation conjecture.

All three retain **COUNTEREXAMPLE FOUND** classification. Fresh publication runs reproduced the original exact JSON outputs. This batch includes mathematical verification code and finite certificates; the original mixed operational ZIPs are not mirrored. No global novelty, formal verification or external certification is claimed. Corrected actual-investigation numbers and historical source aliases are recorded separately.
