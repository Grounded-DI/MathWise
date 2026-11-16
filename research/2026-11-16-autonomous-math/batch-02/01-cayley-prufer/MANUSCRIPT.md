# Cayley / Prüfer — source report text

**Classification: CANDIDATE PROOF** (not externally or formally verified). Original report: `MathWise_Cycle_01_Cayley_Prufer_Report.pdf`. Source ZIP SHA-256: `64caf548a515098809f738016e0bcfb74776f14d8b9cde45b33d6e00db3b9d7f`.

**Publication transformation:** text extracted from the entire source PDF; selected private operator/header labels omitted; text typography and layout do not reproduce the PDF exactly. This is not the original ZIP proof manuscript byte stream. See [Batch 02 index](../README.md) for verification and limitations.

---

<PARSED TEXT FOR PAGE: 1 / 3>
   MathWise Autonomous Research Mission — Cycle
                       01
Timestamp UTC: 2026-11-16T05:57:15.461759+00:00

Classification: CANDIDATE PROOF. The proof is a complete human-checkable mathematical argument and is
supported by exact finite computational checks, but it is not machine-formally verified and not externally independently
verified.

Problem type: Established theorem with independently checkable solution.

Artifact status: Report generated with evidence scripts and SHA-256 manifest.


1. Precise Problem Statement
For every integer n ≥ 2, determine the number of labeled trees on vertex set {1,2,...,n}. A labeled tree is a simple
connected acyclic graph whose vertices are exactly the labels 1 through n. The theorem to prove is Cayley’s formula:

Theorem. The number of labeled trees on {1,2,...,n} is nn−2.


2. Definitions
Tree. A simple graph is a tree if it is connected and acyclic.

Leaf. A vertex of degree 1.

Prüfer sequence. A sequence (a1,...,an−2) with each ai ∈ {1,...,n}. For n=2, the Prüfer sequence is the unique empty
sequence.

Encoding map. Given a labeled tree T on {1,...,n}, repeatedly remove the smallest-labeled leaf and record the label of its
unique neighbor. After n−2 removals, two vertices remain. The recorded list is the Prüfer code P(T).

Decoding map. Given a sequence S=(a1,...,an−2), initialize degrees d(v)=1+number of occurrences of v in S. For
i=1,...,n−2, let ■ be the smallest label with d(■)=1, add edge {■,ai}, and decrement d(■), d(ai). At the end, connect the
two remaining degree-1 labels.


3. Proof Attempt
Claim 1: The encoding procedure is well-defined. Every tree with at least two vertices has a leaf, and after removing a
leaf from a tree, the remaining graph is again a tree. Therefore the repeated deletion process is valid until exactly two
vertices remain. The removed leaf has exactly one neighbor, so each recorded symbol is a label in {1,...,n}.

Claim 2: The decoding procedure is well-defined. At any decoding stage, the multiset of current degrees has total
sum equal to twice the number of remaining edges to be produced. Initially, Σ d(v)=n+(n−2)=2n−2. Each step removes
one leaf-degree and one incidence from a recorded symbol, reducing the sum by 2. A recorded symbol ai cannot be
chosen as the smallest available leaf at that same stage if it still appears in the unprocessed suffix; its degree then
exceeds 1. Hence the chosen leaf is outside the unprocessed symbols and can be safely connected to ai. At the end,
exactly two labels have degree 1 and are connected.

Claim 3: Decoding produces a tree. The procedure adds exactly n−1 edges. Each of the first n−2 edges attaches the
currently chosen leaf ■ and then removes ■ from future consideration. Thus no cycle can be created at that step: ■ has
not previously been attached to the still-active graph as a nonremoved vertex. The final edge connects the two remaining
components. Equivalently, reversing the construction gives a valid leaf-deletion order, so the graph is connected and
acyclic. Hence it is a labeled tree.
<PARSED TEXT FOR PAGE: 2 / 3>
Claim 4: Decoding inverts encoding. Let S be any Prüfer sequence. In the decoded tree, the first leaf removed by the
encoding rule is the smallest label with degree 1 under the initial degree assignment. This is exactly the first leaf chosen
by the decoding rule, and its neighbor is a1. After deleting it, the remaining degrees and remaining sequence are
precisely the decoding state for (a2,...,an−2). Induction over the n−2 stages shows that encoding the decoded tree returns
S.

Claim 5: Encoding inverts decoding. Let T be any labeled tree and let P(T)=S. The degree of a vertex v in T equals 1
plus the number of times v appears in S: each time v is recorded, one adjacent leaf is deleted while v remains; after all
such incidents are removed, v is eventually deleted as a leaf or is one of the final two vertices. Therefore the first leaf
selected by decoding S is the same smallest leaf selected in the first encoding step of T, and it is connected to the same
recorded neighbor. Inducting after removing that leaf, decoding P(T) reconstructs T.

Conclusion. Encoding and decoding are inverse maps between labeled trees on {1,...,n} and sequences of length n−2
over an n-symbol alphabet. There are n choices for each of n−2 positions, hence exactly nn−2 labeled trees.


4. Exact Computational Verification
The evidence package includes a Python script that implements the decoding and encoding maps using exact integer
labels. It checks all Prüfer sequences for n=2 through n=7. For each n it verifies: (i) the number of sequences equals
nn−2; (ii) decoded edge sets are trees; (iii) encode(decode(S)) = S for every sequence; and (iv) the number of unique
decoded trees equals nn−2.

 n    sequences checked         expected n^(n-2)       unique decoded trees        roundtrip failures       tree failures

 2                         1                      1                           1                         0              0

 3                         3                      3                           3                         0              0

 4                        16                     16                          16                         0              0

 5                       125                   125                          125                         0              0

 6                      1296                  1296                        1296                          0              0

 7                    16807                  16807                       16807                          0              0


This computation is a finite audit check only. It does not replace the general proof for arbitrary n.


5. Independent Critique
Boundary n=2. The theorem gives 20=1 and the empty Prüfer sequence represents the single edge {1,2}; the proof
handles this as a base boundary.

Potential proof gap: decoding acyclicity. The main risk is asserting that edges added during decoding cannot create a
cycle. This was addressed by noting that the chosen leaf is removed from future active consideration immediately after
attachment; the construction admits a reverse leaf-deletion order, which certifies treeness.

Potential proof gap: degree formula. The equality degT(v)=1+occurrences of v in P(T) is essential. The proof explains
it operationally but is not formalized in a proof assistant.

Circularity check. The proof does not use Cayley’s formula to prove the bijection. The counting conclusion follows only
after the inverse-map argument.

Novelty check. Cayley’s formula and Prüfer codes are classical. No novelty is claimed.


6. Revision After Critique
The proof was revised to explicitly state the inverse-map structure, the n=2 boundary, and the finite/evidentiary
distinction. The cycle remains classified as CANDIDATE PROOF rather than PROVEN because the proof is not
<PARSED TEXT FOR PAGE: 3 / 3>
independently verified by an external checker or formal proof assistant.


7. Conclusion
Cycle 01 successfully produced a rigorous candidate proof of Cayley’s formula via Prüfer sequences, plus exact finite
verification for n=2 through n=7. The strongest mathematical content is the explicit bijection between labeled trees and
n-ary sequences of length n−2.


8. Evidence Package Contents
Files preserved: verify_cayley_prufer.py, verification_stdout.txt, verification_stderr.txt, verification_returncode.txt,
verification_results.json, manifest_sha256.json, cycle_01_metadata.json. The stderr file contains environment startup
noise from an unrelated spreadsheet warmup path, while the verification script itself exited with return code 0 and
produced the JSON results shown above.
