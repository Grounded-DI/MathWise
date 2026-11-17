# MathWise Batch 04 — Three classical theorem reconstructions

Grounded DI LLC · Mark S. Weinstein · Series MWR-20261116-24H

This batch publishes corrected actual Cycles10,12,14 as **CANDIDATE PROOF**. These reconstruct established mathematics; no new theorem, external refereeing or formal proof-assistant verification is claimed.

| Investigation | Public manuscript | Fresh exact verification |
|---|---|---|
| Cycle10 (historical13) | [Weighted Matrix-Tree theorem](cycle-10-weighted-matrix-tree/MANUSCRIPT.md) | 1099 graphs,5405 rooted cofactors,100 signed rational inputs,19160 incidence minors and30 Cauchy–Binet controls: PASS |
| Cycle12 | [BEST theorem](cycle-12-best-theorem/MANUSCRIPT.md) | 125 eligible simple digraphs plus8 multigraph controls;515 cofactors,876 fixed-first-arc cases and15024 tour/inverse tests: PASS |
| Cycle14 | [Cauchy–Davenport](cycle-14-cauchy-davenport/MANUSCRIPT.md) | 17148 exhaustive pairs over primes2,3,5,7;210 larger samples;11610 coefficient tests;377 sharpness examples: PASS |

All three unchanged original mathematical checkers completed fresh publication runs. Every generated JSON file agrees with the original mathematical output after JSON parsing. Actual commands, UTC times, exit codes and Python version are in [VERIFICATION.json](VERIFICATION.json); each investigation includes stdout, stderr, exact input records and certificates under `results/`.

## Reproduce all finite checks

Use Python3 with its standard library and assertions enabled; do not pass `-O`. From this directory:

```bash
python3 verify_all.py
```

The batch runner verifies the inventory, runs each original checker in a fresh temporary output directory and compares every resulting JSON file with the published certificates. It imposes no short per-script timeout. Individual runs use `python3 verify.py fresh_results` from an investigation directory.

The graph and input bounds are documented precisely in the manuscripts and original scripts. Matrix-Tree's exhaustive graph set has one deterministic positive weighting per graph, with a separate bounded signed-rational sample; it does not test every real assignment. BEST enumerates all simple loopless masks of orders2–4 before selecting balanced strongly connected graphs; multigraph controls are examples rather than exhaustive. Cauchy–Davenport's larger prime inputs are seeded samples, not exhaustive.

## Mathematical status and review

The manuscripts include complete written arguments, definitions, boundary cases, examples, critique and references. Matrix-Tree derives Cauchy–Binet and the incidence-minor lemma. BEST includes the last-exit bijection, the no-premature-stop argument and a directed determinant proof. Cauchy–Davenport derives its coefficient identity, handles saturation separately and gives sharpness and a composite-modulus control.

Publication review found no mathematical gap requiring a status downgrade. The proofs remain model-written candidate proofs. The finite checkers use different methods where described but share authorship and execution environment. Passing computations and matching hashes are not formal verification of the general proofs. References describe targeted source consultation in the original investigations, not a substantive new literature review or endorsement.

## Provenance and coverage

Each `PROVENANCE.json` preserves corrected numbering, historical aliases, original report/package identities, archive hashes and mathematical member hashes. All three original mixed archives passed CRC, unique/safe-path membership and every declared member hash. Their operational records, report-build environment and original private PDFs/ZIPs are excluded. Public manuscripts are edited mathematical editions; verification scripts are byte-identical to original sources.

The public inputs, complete finite certificates and mathematical checkers reproduce the disclosed tests; they do not reproduce the private report-build environment. Prior batches remain intact. No investigation was omitted.

`SHA256SUMS.txt` covers every file in this batch except itself, with paths relative to this directory. The parent research index and Git metadata are outside coverage.
