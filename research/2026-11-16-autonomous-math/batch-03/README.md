# MathWise Batch 03 — Three exact counterexamples

Grounded DI LLC · Research operator: Mark S. Weinstein · November 16, 2026

Three previously unpublished investigations from series MWR-20261116-24H, each classified **COUNTEREXAMPLE FOUND**. Numbers count actual investigations; historical source aliases remain in the provenance records. These are experiment conjectures, not assertions attributed to the cited authors. No global novelty claim is made.

| Corrected cycle | Manuscript | Exact conclusion | Fresh verification |
|---|---|---|---|
| 09 (historical12) | [Greedy Birkhoff decomposition](cycle-09-greedy-birkhoff/MANUSCRIPT.md) | Lexicographic greedy9 terms, certified OPT4;9/4>2 | Permutation/backtracking agreement, reconstruction and all nine ordering/minimum certificates PASS |
| 11 | [Greedy edge deletion](cycle-11-greedy-edge-deletion/MANUSCRIPT.md) | Unique first greedy choice leads to4 trees, global optimum5 | Subset enumeration, rooted-parent count and29 exact cofactors PASS |
| 13 | [Directed arc correlation](cycle-13-directed-arc-correlation/MANUSCRIPT.md) | Bidirected C5 covariance2/25>0 | Complete oriented-tree set agreement and exact determinants; six graphs n5..10,56 marked pairs PASS |

## Reproduce

Use Python3 with its standard library; no external packages. Run from this batch directory, with assertions enabled (do not use `python -O`):

```bash
python3 verify_all.py
```

This validates the SHA-256 inventory, runs each original checker into fresh temporary output directories, compares every generated JSON with the published results, and checks the lexicographic trace. Individual commands appear in each manuscript and in [VERIFICATION.json](VERIFICATION.json). Actual stdout/stderr files and exact inputs/certificates are included beside each manuscript. Cycle09's explicit input is in `checks/counterexample.json`; Cycle11's is in `results/witness.json`; Cycle13's complete arcs and accepted trees are in `results/inputs_certificates.json`.

The Cycle11 script reproduces the original bounded search before checking its witness:319 graph masks,42 eligible connected graphs and780 candidate tree subsets. Those are search bounds, not a general exhaustive graph classification. Cycle09 examines one structured seeded input. Cycle13 checks only the specified cycle family, not arbitrary digraphs.

## Evidence and provenance

All three original source ZIPs passed CRC, unique/safe membership and all declared member hashes. Their original whole-archive SHA-256 values and source report/package identities are retained in each `PROVENANCE.json`. Source reports, proof text and checkers were inspected. Public `verify.py` scripts are unchanged from their original source bytes; manuscripts are newly edited mathematical editions. The Cycle09 trace checker and mathematical trace/input certificates are also preserved unchanged.

The original mixed ZIPs are deliberately omitted because they contain operator/runtime records. This public edition includes the mathematical scripts, complete finite certificates, actual publication outputs and instructions needed to replay the disclosed checks. It does not reproduce the original report-build environment or claim byte-for-byte reconstruction of private PDFs/ZIPs. Prior batches remain intact.

These exact witnesses refute the stated universal assertions. Finite family checks do not replace the separate written general-family arguments. Different algorithms share authorship and execution environment; no independent external referee or formal proof checker is claimed. The references are background sources consulted in the original investigations, not endorsements or a substantive novelty review.

`SHA256SUMS.txt` covers every file in this batch except itself, using paths relative to this directory. The parent index and future Git metadata are outside its coverage. Hash identity and mathematical correctness are separate conclusions.
