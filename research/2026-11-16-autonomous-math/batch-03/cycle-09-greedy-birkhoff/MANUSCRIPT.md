# Cycle09 — Lexicographic greedy Birkhoff decomposition exceeds twice optimum

Grounded DI LLC · Mark S. Weinstein · Series MWR-20261116-24H  
Historical source alias: Cycle12. Publication classification: **COUNTEREXAMPLE FOUND**.

## Conjecture and exact algorithm

For every integer n≥1 and every n×n doubly stochastic matrix A (nonnegative entries; every row and column sum one), let OPT(A) be the minimum number of permutation matrices in an exact convex decomposition with positive real weights. Let G(A) count terms produced by repeatedly choosing the lexicographically first supported permutation, subtracting the minimum entry along it, and continuing until zero. Permutations are tuples of zero-based column indices, ordered by row 0, then row 1, etc. The conjecture asserts G(A)≤2OPT(A).

For A=M/D, subtracting integer masses from M gives exactly the same support choices as normalizing after each step: if current row mass is r and removed mass is t, normalization gives local coefficient t/r and global coefficient t/D. Thus normalization cannot change the exhibited greedy trace.

## Witness and optimum

Take D=15 and

$$M=\begin{pmatrix}8&1&2&4\\1&2&4&8\\4&8&1&2\\2&4&8&1\end{pmatrix}.$$

Every entry is positive; each row and column sums to 15. For a tuple π let Pπ have entry one at (i,π(i)) and zero elsewhere. An exact decomposition is:

| Weight | Permutation tuple |
|---|---|
| 1/15 | [1, 0, 2, 3] |
| 2/15 | [2, 1, 3, 0] |
| 4/15 | [3, 2, 0, 1] |
| 8/15 | [0, 3, 1, 2] |

These four positive weights sum to one and reconstruct A entrywise. Every permutation contributes at most one positive position in a given row. A combination of k permutations therefore has at most k positive positions per row. Each row of A has four, so k≥4 even for arbitrary positive real weights. Consequently OPT(A)=4.

## Greedy trace

| Step | Removed integer mass (weight = mass/15) | Permutation tuple |
|---|---|---|
| 1 | 1 | [0, 1, 2, 3] |
| 2 | 1 | [0, 1, 3, 2] |
| 3 | 1 | [0, 2, 3, 1] |
| 4 | 5 | [0, 3, 1, 2] |
| 5 | 1 | [1, 3, 0, 2] |
| 6 | 2 | [2, 3, 0, 1] |
| 7 | 1 | [3, 0, 1, 2] |
| 8 | 1 | [3, 2, 0, 1] |
| 9 | 2 | [3, 2, 1, 0] |

The masses sum to 15 and the residual is zero after step nine. The accompanying complete trace certificate records every residual and a zero blocking each lexicographically earlier permutation. The selected tuple is supported and its removed mass is exactly the minimum selected entry. Thus this is the prescribed algorithm, giving G(A)=9>8=2OPT(A).

`verify.py` checks permutation enumeration against increasing-column recursive backtracking, exact reconstructions and row support. `verify_trace.py` checks all ordering blockers and nine minima against the supplied certificate:

```bash
python3 verify_trace.py
```

## Attempt and critique

The tempting absolute Birkhoff term bound gives no factor-two bound relative to OPT; that attempted inference was discarded. Showing an arbitrary nine-term decomposition would also be insufficient: the complete ordering certificate establishes the algorithm's actual choices. One structured seeded input was tested before finding this witness. No exhaustive matrix search or smallest-dimension claim follows. The result concerns this lexicographic algorithm, not every greedy heuristic.

## Reference

F. Dufossé, K. Kaya, I. Panagiotas and B. Uçar, “Further notes on Birkhoff–von Neumann decomposition of doubly stochastic matrices,” Linear Algebra and Its Applications 554 (2018), 68–78, DOI [10.1016/j.laa.2018.05.017](https://doi.org/10.1016/j.laa.2018.05.017). The original investigation inspected the institutional abstract for background on greedy versus minimum-size decompositions; the full article was not reviewed. The factor-two conjecture is this experiment's formulation and is not attributed to those authors. The finite refutation above is self-contained.

## Status and reproduction

**COUNTEREXAMPLE FOUND.** This refutes the precisely stated experiment conjecture. No historical novelty, minimality, external certification or formal proof-assistant validation is claimed. The proof text is model-written; the finite certificates and exact program runs are separate supporting evidence. All implementations share authorship and execution environment.

The public `verify.py` is byte-identical to the corresponding original source checker. It uses only Python's standard library. Run from this directory:

```bash
python3 verify.py fresh_results
```

The checked-in `results/` directory contains actual output from the publication run. `PROVENANCE.json` identifies source reports, archives, original SHA-256 values and corrected/legacy numbering. This manuscript is a new mathematical edition; the original mixed archive is not published.
