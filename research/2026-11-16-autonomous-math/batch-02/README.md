# MathWise research — Batch 02 (November 16, 2026)

**Grounded DI LLC | Publication classification: CANDIDATE PROOF**

This batch publishes **nine distinct source-investigation records across eight mathematical subjects**, including two separate Erdős–Ginzburg–Ziv reconstructions. All nine retain **CANDIDATE PROOF** status. No mathematical novelty, external refereeing, or formal proof-assistant verification is claimed.

This is the public *mathematical report-text edition*, not a dump of the original ZIP research environments. Each linked `MANUSCRIPT.md` is a text extraction of the entire original report, with internal operator/footer labels removed. Extracted mathematical typography may differ from the original PDF; where necessary, use the stated formulas and source records. It is not byte-identical to the source report or to the original ZIP's `proof.txt` / `proof.md` file.

| # | Subject / original investigation | Fresh original check in this publication run |
|---|---|---|
| 1 | [Cayley / Prüfer](01-cayley-prufer/MANUSCRIPT.md) | PASS 1.10 s, fresh finite checker; no general formal proof |
| 2 | [Dilworth](02-dilworth/MANUSCRIPT.md) | PASS 1.77 s, fresh original verify.py |
| 3 | [EGZ (MWR Cycle 07)](03-egz-mwr-cycle07/MANUSCRIPT.md) | PASS 1.61 s, fresh original verify.py |
| 4 | [EGZ (MWPRO Cycle 01)](04-egz-mwpro-cycle01/MANUSCRIPT.md) | Archive ZIP CRC only in this publication run; historical replay described in manuscript, not rerun |
| 5 | [Three-rank chain repair](05-three-rank-chain-repair/MANUSCRIPT.md) | INCOMPLETE: original verify.py exceeded 12 s fresh-run budget; prior reported checks not promoted |
| 6 | [Birkhoff–von Neumann](06-birkhoff-von-neumann/MANUSCRIPT.md) | PASS 1.22 s, fresh original verify.py |
| 7 | [Generalized Sperner / k-LYM](07-generalized-sperner/MANUSCRIPT.md) | PASS 1.71 s, fresh original verify.py |
| 8 | [Weighted spanning trees and correlation](08-weighted-spanning-tree-correlation/MANUSCRIPT.md) | Archive ZIP CRC only in this publication run; original full replay not rerun |
| 9 | [Lucas’s theorem](09-lucas/MANUSCRIPT.md) | PASS 1.40 s, fresh original verify_lucas.py (392,504 checks reported) |

## Exact provenance and source ZIP hashes

- **Cayley / Prüfer**: original report `MathWise_Cycle_01_Cayley_Prufer_Report.pdf`; source archive `MathWise_Cycle_01_Evidence_Package.zip`; archive SHA-256 `64caf548a515098809f738016e0bcfb74776f14d8b9cde45b33d6e00db3b9d7f`.
- **Dilworth**: original report `MWR-20261116-24H_Cycle05_Dilworth_Report.pdf`; source archive `MWR-20261116-24H_Cycle05_Research_Package.zip`; archive SHA-256 `05b5c100997b2941a6023c155e6a5dd2272571834ed1b2abc992a6c14b5fabf5`.
- **EGZ (MWR Cycle 07)**: original report `MWR-20261116-24H_Cycle07_EGZ_Report.pdf`; source archive `MWR-20261116-24H_Cycle07_Research_Package.zip`; archive SHA-256 `e1cc30ef8a46c5fb37d2bdb41ea62b84a7d54d7343cacfb54aaefbd5ef73e129`.
- **EGZ (MWPRO Cycle 01)**: original report `MWPRO-20261116-8H_Cycle01_Research.pdf`; source archive `MWPRO-20261116-8H_Cycle01_Research_Package.zip`; archive SHA-256 `ac2bfaf6f76091243794dfe40b7f6de2b1d8d2e3a7a40195514b709b95340db4`.
- **Three-rank chain repair**: original report `MWR-20261116-24H_Cycle08_Chain_Repair_Report.pdf`; source archive `MWR-20261116-24H_Cycle08_Research_Package.zip`; archive SHA-256 `87355278cbe6a75b04d8fe80331d678d16cdaf50b89230b9bcfc197cfee34dd2`.
- **Birkhoff–von Neumann**: original report `MWR-20261116-24H_Cycle09_Birkhoff_Report.pdf`; source archive `MWR-20261116-24H_Cycle09_Research_Package.zip`; archive SHA-256 `fbab5eae38f011df2b8fa81bbcf1d8a9befa1808e54a4d8024eca51cb604a19f`.
- **Generalized Sperner / k-LYM**: original report `MWR-20261116-24H_Cycle11_Sperner_Report.pdf`; source archive `MWR-20261116-24H_Cycle11_Research_Package.zip`; archive SHA-256 `e2171142800c0b0006dd1b7faad04035ac5adc745541f4cf83bfd78203f2f8a3`.
- **Weighted spanning trees and correlation**: original report `MWPRO-20261116-8H_Cycle03_Research.pdf`; source archive `MWPRO-20261116-8H_Cycle03_Research_Package.zip`; archive SHA-256 `77427fbab0900b84258060b8537fd8b5e37a663be88bdfc30a92b5db95a942b9`.
- **Lucas’s theorem**: original report `MathWise_Cycle_03_Lucas_Theorem_Report.pdf`; source archive `MathWise_Cycle_03_Evidence_Package.zip`; archive SHA-256 `23d8b991b3a13bc26c5759b3dbf8682a5371686b598cada2d212ecb5936d2835`.

All nine source archives passed ZIP CRC/membership readability (`ZipFile.testzip() == None`) locally. These hash values were calculated on retrieved archive bytes. **The original ZIP archives are not posted in this batch**: they contain mixed materials, including private operator/runtime records. No inference of full original-script replay follows from a readable archive.

## Verification performed during this publication session

- Seven original verification scripts were attempted from separately extracted sources. Six returned status **PASS** (Cayley, Dilworth, MWR EGZ, Birkhoff, Sperner, Lucas); one was **TIMEOUT** (three-rank chain repair; 12-second per-run budget). The two larger MWPRO EGZ and weighted-tree scripts were not freshly invoked.
- Executions used fresh temporary output directories and Python standard-library code. Output is a local replay check, **not external certification**. The timeout is not a mathematical failure, and a previously recorded PASS does not replace an uncompleted fresh run.
- [verify_public.py](verify_public.py) provides a new, limited public smoke-check suite covering selected small exact examples. **This is not a replacement for the original full verification scripts or their frozen manifests**. It checks only the finite domains indicated in its source.

## Scope, reproducibility and omissions

The PDF-extracted manuscripts below include theorem statements, proof arguments, examples, limitations and prior execution descriptions. The preserved original `verify.py`, `proof.txt`, source ledgers, raw exhaustive certificate tables, full ZIP packages, and original SHA-256 member manifests have **not** been published here; the public smoke script is a new implementation. Full source-package replication is therefore **not yet established from this GitHub release alone**. This limitation applies even though the original local packages and their integrity hashes were inspected and six original verifiers were rerun.

For the two EGZ treatments, retain both independent provenance chains: MWR Cycle 07 and MWPRO Cycle 01. They are the same classical theorem investigated in distinct task series, not two novel results. The three-rank repair is a new-to-experiment conjecture; historical novelty is unestablished.

Private governance instructions, patent materials, internal operational artifacts, and unrelated research archives were excluded. Batch 01 was preserved unchanged.

**Research operator:** Mark S. Weinstein. **Publisher:** Grounded DI LLC. **Publication date:** November 16, 2026.
