# Weighted spanning trees and correlation — source report text

**Classification: CANDIDATE PROOF** (not externally or formally verified). Original report: `MWPRO-20261116-8H_Cycle03_Research.pdf`. Source ZIP SHA-256: `77427fbab0900b84258060b8537fd8b5e37a663be88bdfc30a92b5db95a942b9`.

**Publication transformation:** text extracted from the entire source PDF; selected private operator/header labels omitted; text typography and layout do not reproduce the PDF exactly. This is not the original ZIP proof manuscript byte stream. See [Batch 02 index](../README.md) for verification and limitations.

---

<PARSED TEXT FOR PAGE: 1 / 12>

 MATHEMATICAL RESEARCH / ROUND 003 OF 008

 A determinant
 counts trees.
 Edges compete.
 The weighted matrix-tree theorem, reconstructed from incidence
 minors, with an exact formula for pairwise negative correlation.

     Cycle classification
     CANDIDATE PROOF (not independently verified)
     Complete model-written reasoning, separate AI review, exact finite checks and one observed
     replay. The underlying theorems are established mathematics.

   EXHAUSTIVE GRAPHS                      EXACT COFACTORS                        WEIGHTED FIXTURES


   33,867 labeled graphs                  202,013 principal minors               43 rational cases
   Every graph on 1-6 vertices            Every choice of root                   Bridges, parallel edges and zero
                                                                                 weights


 The general proof yields an exact covariance formula. A weighted triangle illustrates strict
 negativity; opposite edges of K₄ show why equality must remain allowed. Neither the proof
 nor the finite results are presented as a new theorem.

 2026, 08:18:11 Eastern / 13:18:11 UTC. Manual continuation of series MWPRO-20261116-8H.

<PARSED TEXT FOR PAGE: 2 / 12>

 CYCLE 03 / 02

 Statements and assumptions
 Finite undirected multigraphs; edges have distinct identities even when endpoints coincide.

 Let G have n ≥ 1 labeled vertices and m indexed edges. Loops are excluded; parallel edges
 are allowed. A spanning tree connects every vertex without a cycle, including a two-edge
 cycle formed by parallel edges. Give edge e weight we ≥ 0, and give a tree the product of its
 edge weights.

 Orient each edge e = (u,v) arbitrarily. Its incidence column ce has +1 at u, -1 at v and zero
 elsewhere. Delete a chosen root coordinate to obtain be. The weighted Laplacian and its
 reduced principal minor are:

     Theorem A. For every graph, nonnegative weight assignment and root above, det Ar
     = τ(G,w). For n = 1, the empty determinant and the empty tree weight are both 1. A
     disconnected graph with n ≥ 2 has zero tree sum and zero reduced determinants.


 Theorem B. Assume additionally n ≥ 2, connectedness and strictly positive weights. Sample
 a tree with probability W(T)/τ. The reduced matrix A is invertible. Put Kef = beTA-1bf. Then:

 Here pe is the probability of including edge e, and pef is the probability of including both
 distinct edges. Subtracting pepf gives the nonpositive covariance on the cover. The
 same-edge case is a variance and is excluded from that formula.

 The classical matrix-tree identity is documented in [S1]. The weighted law and transfer-current consequence
 appear in [S2]; [S3] supplies original determinantal-marginal attribution. This report proves the needed finite
 results directly.

<PARSED TEXT FOR PAGE: 3 / 12>

 CYCLE 03 / 03

 Why only trees survive
 Every selected incidence minor has determinant zero or magnitude one.

  TREE: |det B_F| = 1                                     DISCONNECTED: det B_F = 0


                        1                                         0


      0                                2                                                              3


                                                           1                  2
                                              3

  Three indexed edges on four vertices.                   A triangle leaves vertex 3 isolated.


 Let B be the incidence matrix with the root row removed. For an edge set F of size n-1, write
 BF for its square column submatrix. We establish the tree criterion without using a
 determinant counting theorem.

 Graph facts
 A connected graph contains a tree of n-1 edges: start from one vertex and repeatedly add an
 edge to an unreached vertex. Each step adds exactly one vertex and cannot make a cycle.
 Therefore a connected graph with precisely n-1 edges is itself a tree. A tree with at least two
 vertices has two leaves, because the endpoints of a longest simple path cannot have
 additional neighbors without extending the path or forming a cycle.

 If F is not a spanning tree
 It is disconnected by the edge-count fact. Choose a component not containing the deleted
 root. Summing its rows in BF gives zero: each internal edge contributes +1 and -1, and no
 selected edge leaves that component. This nonempty row relation forces det BF = 0.

 If F is a spanning tree
 Use induction, starting with the empty determinant 1 at n = 1. Choose a leaf different from
 the root. Its row has exactly one nonzero entry, ±1. Expanding along that row removes the
 leaf and its edge, leaving the reduced incidence matrix of the smaller tree. Induction gives
 determinant magnitude 1. Its sign disappears when squared.

<PARSED TEXT FOR PAGE: 4 / 12>

 CYCLE 03 / 04

 A complete determinant count
 Cauchy-Binet is derived here, rather than imported as an unproved counting step.

 Let X have k rows and m columns, and let Y have m rows and k columns. Write Xj for column
 j of X. Column ℓ of XY is the sum of YjℓXj over j. Multilinearity expands its determinant into
 terms indexed by k-tuples:

 Terms with repeated indices have repeated columns and vanish. Fix a distinct set F = {f₁ <
 … < fk}. Its orderings are jℓ = fσ(ℓ). Each column permutation contributes sign(σ) det XF.
 Summing the signed coefficient products over σ is exactly the determinant of the selected
 rows YF. Hence:

 If m < k, no distinct tuple exists and both sides are zero. If k = 0, the single empty term is 1.
 Thus the identity covers the boundary cases needed here.

 Apply it to the weighted incidence factorization

 Choose X = B and Y = diag(w)BT. Selecting a row of Y contributes its edge weight. Its
 remaining determinant is that of BFT, equal to det BF. Therefore:

 The preceding page proves that non-tree terms vanish and tree terms have squared
 determinant 1. The surviving sum is precisely τ(G,w). This proves Theorem A for every stated
 graph and nonnegative weight assignment, including zero weights, disconnected graphs and
 n = 1.


     Root independence is a consequence. Deleting any vertex produces the same tree
     sum. No matrix inverse, division by τ, or probabilistic formula was used in the proof.

<PARSED TEXT FOR PAGE: 5 / 12>

 CYCLE 03 / 05

 The inverse is justified
 Connectedness and positive weights enter before any probability or inverse is used.

 A connected graph has a spanning tree, and strictly positive edge weights give that tree
 positive weight. Thus τ > 0 and W(T)/τ defines a probability distribution.

 For a vector x on the non-root vertices, extend it by root value zero to a vector x̃. The
 reduced Laplacian satisfies the energy identity:

 If the sum is zero, strict positivity forces equal endpoint values along every edge.
 Connectedness forces a constant vector, and the zero root value makes it zero. Thus A is
 symmetric positive definite and invertible. In particular, Kef = Kfe.

 Prove the rank-two update
 For any two-column matrix U and diagonal 2 × 2 matrix D, form the block matrix M with
 blocks A,U in the top row and -DUT,I₂ in the bottom row. Two block row operations, each
 represented by a determinant-one triangular matrix, evaluate its determinant in different
 ways.

   Row operation                                                Resulting determinant


   Add DUᵀA⁻¹ times the top block row to the bottom             det A · det(I₂ + DUᵀA⁻¹U)


   Subtract U times the bottom block row from the top           det(A + UDUᵀ)

 The first operation makes M block upper triangular; the second makes it block lower
 triangular. Only the original A must be invertible. The same argument with one column and a
 scalar lower-right block proves the one-edge update.

 The manuscript writes both multiplying block matrices explicitly. This identity follows from ordinary determinant
 rules and does not assume a spanning-tree probability theorem.

<PARSED TEXT FOR PAGE: 6 / 12>

 CYCLE 03 / 06

 Extract the edge probabilities
 Perturbing two weights produces a bilinear polynomial whose coefficients are probabilities.

 Fix distinct edges e,f. Multiply their positive weights by 1+s and 1+t, with s,t ≥ 0. A tree
 either uses each indexed edge once or omits it. Dividing the perturbed tree sum by the
 original sum gives:

                                                     T            T
 The new reduced Laplacian is A + swebebe + twfbfbf . Put U = (be,bf) and D = diag(swe,twf)
 in the proved update. The 2 × 2 determinant expands to:

 Theorem A identifies these two expressions. Their bilinear coefficients agree; evaluations at
 (0,0), (1,0), (0,1) and (1,1) already determine every coefficient. Consequently:

 A graph with only one edge uses the one-column update to obtain its marginal. The
 single-edge formula therefore does not assume that a second edge exists.

 Root and orientation invariance
 Reversing an orientation changes an incidence column’s sign. A and diagonal K entries stay
 fixed; off-diagonal entries change only by sign, which disappears on squaring. To compare
 roots, solve Ax = bf and extend x by root value zero. The full equation Lv = cf holds,
 including the root row because both sides sum to zero. Two such solutions differ by a
 constant, by the energy argument. Since ce sums to zero, ceTv = Kef is unaffected.

<PARSED TEXT FOR PAGE: 7 / 12>

 CYCLE 03 / 07

 A triangle, calculated exactly
 Weights 2, 3 and 5 turn the abstract identity into a complete three-tree calculation.

                                         1
                                                                      THREE POSSIBLE TREES

                  e: 2                           f: 3                 {e,f}: weight 6

                                                                      {e,g}: weight 10

                                                                      {f,g}: weight 15
              0                                         2
                                    g: 5
                                                                      Total tree weight: 31

 Use orientations 0→1, 1→2 and 0→2, and delete root 2. Direct calculation gives:


           A=                7     -2                        A⁻¹ = (1/31)            5        2
                             -2    5                                                 2        7

   Quantity                       Tree enumeration                           Matrix formula


   Partition τ                    6 + 10 + 15 = 31                           det A = 35 - 4 = 31


   P(e)                           (6 + 10)/31 = 16/31                        2 × (8/31)


   P(f)                           (6 + 15)/31 = 21/31                        3 × (7/31)


   P(e and f)                     6/31                                       6 × (56 - 25)/31²

 Conditioning on f reduces the chance of e from 16/31 to (6/31)/(21/31) = 2/7. This is a complete exact calculation,
 not a frequency estimate from simulated trees.

<PARSED TEXT FOR PAGE: 8 / 12>

 CYCLE 03 / 08

 Equality matters
 Pairwise negative correlation permits independence; strict negativity needs a nonzero cross term.

 Because the edge weights are positive, covariance is zero exactly when Kef = 0. For two
 indicator variables, pef = pepf implies independence: the other three joint probabilities follow
 from the marginals and their sum.

 A counterexample to a strict strengthening


          0                      1             UNIFORM K₄ / OPPOSITE EDGES

                                               16 spanning trees

                                               P(e) = P(f) = 1/2

                                               P(e and f) = 1/4; covariance = 0
          2                      3


 Of the 20 three-edge subsets of K₄, four are triangles and 16 are trees. A fixed edge lies in 10
 three-edge subsets, of which two are triangles, so its marginal is 8/16. With the two
 highlighted disjoint edges fixed, any of the four edges joining their components completes a
 tree. Their joint probability is 4/16. Neither is a bridge, yet the events are independent.

 How another edge’s weight changes a probability
 Differentiating the finite product-weight tree sums gives wf∂pe/∂wf = pef - pepf for e ≠ f:
 differentiating each tree weight multiplies it by its f-indicator, and the quotient rule supplies
 the product term.

 For the triangle, replace the weight 3 by x > 0. Then pe(x) = (2x+10)/(7x+10), with
 derivative -50/(7x+10)². At x = 3 the log-weight derivative is -150/961, exactly the
 covariance. Increasing another edge’s weight cannot increase pe.

 For e = f, the log-weight derivative is pe(1-pe) ≥ 0. Pairwise identities alone are not used here to assert negative
 association for arbitrary increasing events.

<PARSED TEXT FOR PAGE: 9 / 12>

 CYCLE 03 / 09

 Every graph through six vertices
 An exhaustive finite check of the tree identity, independent of the general proof.


   n       All graphs                Connected                Cofactors               Direct checks


   1       1                         1                        1                       1


   2       2                         1                        4                       2


   3       8                         4                        24                      8


   4       64                        38                       256                     64


   5       1,024                     728                      5,120                   1,024


   6       32,768                    26,704                   196,608                 0


   All     33,867                    27,476                   202,013                 1,099


 A labeled simple graph is specified by a bit mask over the C(n,2) possible edges, in a fixed
 lexicographic edge order. The exact coverage is 2C(n,2) at each n. Every mask, tree count,
 root cofactor and available direct count is retained in the compressed CSV records.

 Separate computational routes
 Combinatorial count. Decode every Prüfer word of length n-2 into a labeled tree mask
 (with the singleton handled explicitly). A subset-zeta transform counts which tree masks are
 contained in each graph mask. No Laplacian determinant supplies those counts.

 Linear algebra. Build each graph’s integer Laplacian and use exact Bareiss elimination for
 every root’s reduced determinant. Compare all 202,013 cofactor values with the
 combinatorial counts. The program uses unbounded integers and checks the exact divisions
 in elimination.

 Direct enumeration. For every graph through n = 5, enumerate its edge subsets of size n-1
 and test connectivity and absence of cycles using union-find. All 1,099 direct counts agree
 with the other route.

 Disconnected graphs are included, with zero counts and cofactors. The one-vertex graph gives the empty
 determinant and empty-tree count 1. No exhaustive simple-graph check beyond six vertices was performed.

<PARSED TEXT FOR PAGE: 10 / 12>

 CYCLE 03 / 10

 Weighted cases and critical review
 Exact fractions; explicitly retained fixtures; no sampled frequencies.


   Check                                  Executed scope or result


   Weighted inputs                        43 specified cases; all inputs listed, including 30 generated rational
                                          multigraphs


   Reduced determinants                   474 comparisons across all roots and three orientation patterns


   Probability domain                     41 positive-partition cases; 2 zero-partition cases excluded from probability
                                          formulas


   Marginals and pairs                    2,889 marginal and 9,057 joint-formula comparisons


   Distinct case-edge pairs               669 pairs: 557 strict negative covariance, 112 zero covariance


   Separate review                        10 small cases; every root and orientation: 839 determinants, 4,408
   implementation                         marginals and 10,232 pairs


 Every main weighted fixture retains all its spanning-tree subsets and exact product weights. The main suite uses
 explicit edge-subset enumeration and exact fraction matrix calculations. Its three orientation patterns are as
 listed, all reversed and alternating. The reviewer used a separate implementation and broader orientation
 coverage on its own smaller fixtures. These scopes overlap and are not additive independent trials.


 Boundary findings
 Parallel edges: equal incidence columns up to sign make the two-edge determinant zero;
 both cannot occur in a tree. Bridges: every spanning tree contains them, giving marginal 1
 and zero covariance with other edges. Zero partition: the determinant identity remains
 meaningful, but probabilities and inverses are not used.

 Failed routes and rejected implications
 The full Laplacian has the all-ones vector in its kernel, so its determinant cannot replace a
 principal cofactor. Independent-edge reasoning fails on the weighted triangle. Strict
 negativity for every non-bridge pair fails on K₄. The proof avoids deriving the matrix-tree
 identity from a probability formula and then using that identity to justify the same formula.


     Review outcome: the separate AI reconstruction and manuscript audit found no
     required mathematical correction or unresolved gap. The review was unblinded and
     used the same model family and workspace. No formal checker or external human
     referee was used.

<PARSED TEXT FOR PAGE: 11 / 12>

 CYCLE 03 / 11

 Execution and replay
 Actual UTC on November 16, 2026; Eastern time is UTC minus five hours.


   Activity                               Actual UTC                           Observed outcome


   Round start                            13:18:11                             Manual Round 003 authorization


   Separate reviewer checks               13:20:15.279-13:20:16.101            Exit 0; exact fixture checks


   Main exact suite                       13:20:48.740-13:20:51.400            Exit 0; every specified
                                                                               comparison passed


   Fresh main-suite replay                13:21:57.067-13:21:59.736            Exit 0; 28/28 mathematical files
                                                                               identical

 The replay contract
 The retained checker was run once more into a fresh destination with unchanged bounds
 and fixtures. Every one of the 28 mathematical output files matched both direct bytes and
 SHA-256. All 32 protected original files remained unchanged. Actual timestamps, elapsed
 times and execution paths are kept separately from mathematical outputs and were not
 rewritten to force a match.

 The compressed streams retain all simple-graph inputs and counts and all weighted inputs,
 trees and matrix calculations. Replay agreement is an observed result for these fixed
 computations on this host. It does not certify cross-environment reproducibility, universal
 determinism or the general mathematical proof.

 What the package preserves
 The frozen problem specification, complete manuscript, separate reconstruction and final
 review, source ledger, executable checkers, exact inputs and outputs, execution logs, actual
 timestamps, replay contract, PDF source and SHA-256 manifest are included. The manifest
 covers all archive payloads except itself. The external cumulative index records the ZIP hash
 and saved artifact identities.

 Reproduction
 python3 verify_manifest.py --package-dir /path/to/extracted/package
 python3 verification/replay_checks.py --help

 The mathematics checkers and replay require only the Python standard library. Use new output/evidence
 destinations as documented in the package README. Rebuilding the report also requires ReportLab, Matplotlib,
 Pillow and the recorded DejaVu fonts.

 The original Round 001 and Round 002 reports and packages were hash-checked against the preserved index
 before this work; the new round does not modify them.

<PARSED TEXT FOR PAGE: 12 / 12>

 CYCLE 03 / 12

 Attribution and continuation
 Established results reconstructed; mathematical novelty is not asserted.

 [S1] R. Kenyon. The Laplacian on planar graphs and graphs on surfaces. arXiv:1203.1256v1 (2012). Theorem 4.2
 and its incidence/Cauchy-Binet proof, pages 14-15. Inspected proof route; the manuscript separately proves its
 boundary conventions.

 https://arxiv.org/pdf/1203.1256

 [S2] R. Lyons and Y. Peres. Probability on Trees and Networks. Author-hosted text; selected indexed passages
 inspected. Chapter 4: product-conductance law, transfer-current equation (4.5) and pairwise covariance, and
 matrix-tree statement; printed pages 97, 108-109 and 121. The exact PDF edition was not established.

 https://rdlyons.pages.iu.edu/prbtree/book.pdf

 [S3] R. Burton and R. Pemantle. Local Characteristics, Entropy and Limit Theorems for Spanning Trees and
 Domino Tilings Via Transfer-Impedances. Original paper (1993); arXiv author version math/0404048. Theorem 1.1,
 PDF page 4. The inspected simplified finite statement uses uniform trees.

 https://arxiv.org/pdf/math/0404048

 The source ledger retains five inspected records, exact read scopes and failed access attempts. A direct fetch of
 the large Lyons-Peres PDF exceeded the service size limit; its indexed content was subsequently opened and
 inspected. Source statements establish attribution, not external validation of this manuscript.


 Cumulative checkpoint

   Cycle            Investigation                                      Classification


   001              EGZ theorem and prime counting identity            CANDIDATE PROOF


   002              Quadratic zero-sum count conjecture                COUNTEREXAMPLE FOUND


   003              Weighted trees and edge correlation                CANDIDATE PROOF


   004–008          Five investigations remain                         Not executed in this series


 For Cycles 001 and 003, the full status is CANDIDATE PROOF (not independently verified). Cycle 002’s distinct n ≥
 5 conjecture remains unresolved; this graph-theory investigation does not settle it.

 Round 003 began on the present manual authorization at 08:18 Eastern. The earlier nominal 04:00 slot remains
 historical; no missed execution is simulated. No series timer was created. The full eight-cycle executive
 comparison remains pending actual completion of the remaining investigations.


