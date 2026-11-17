# Cycle10 — Weighted Matrix-Tree theorem for real edge weights

Grounded DI LLC · Mark S. Weinstein · Series MWR-20261116-24H

Historical source label: Cycle13; corrected actual investigation: Cycle10.

**CANDIDATE PROOF — classical theorem reconstruction.** This is a new public mathematical edition derived from the original report and proof text, not the original PDF or a claim of a new theorem.

## Precise theorem and conventions

For every integer n≥1, every finite simple undirected graph G=(V,E) on V={0,…,n−1}, every assignment of real weights w:E→ℝ, and every root r∈V, let L have off-diagonal entry Lᵢⱼ=−w({i,j}) when {i,j}∈E and 0 otherwise, and diagonal entry Lᵢᵢ=∑e incident to i w(e). Write Lʳ for L with row and column r deleted. Then

$$\det L^{(r)}=\sum_{T\text{ spanning tree of }G}\prod_{e\in T}w(e).$$

A spanning tree uses every vertex, is connected, and has no cycle. A disconnected graph has no spanning tree, so its sum is 0. For n=1 the empty edge set is the unique spanning tree, its product is 1, and the empty determinant is 1. Edge weights may vanish or be negative; in that case the sum can cancel and is not a probability normalization.

## Why investigate this theorem?

This identity replaces exponential tree enumeration with a determinant and explains why Laplacian calculations can verify combinatorial counts. This investigation reconstructs the general counting identity.

Triangle example: three spanning trees have products 2·3, 2·5 and 3·5. The total is 31. These are edge weights, not probabilities.

**CANDIDATE PROOF.** Complete model-written reasoning and bounded exact checks are supplied. No formal proof assistant or external reviewer checked this proof. This is classical mathematics; no novelty claim is made.

## Cauchy-Binet is derived here, rather than assumed as an unexplained gate

## Step 1: factor the weighted Laplacian

Orient every edge arbitrarily. Let B be the n-by-m signed incidence matrix: column e has −1 at its tail, +1 at its head and 0 elsewhere, where m=|E|. Let W=diag(w(e)). Entrywise multiplication gives L=BWBᵀ: each edge adds w(e) to its two diagonal entries and −w(e) to their two off-diagonal entries. Reversing an edge negates its incidence column twice in this product and changes nothing.

Delete row r from B to obtain Q. Deleting row and column r from L gives Lʳ=QWQᵀ. No square root of a weight is used, so the argument permits negative weights.

## Step 2: a determinant product expansion

For a k-by-m matrix X and an m-by-k matrix Y over ℝ, expand det(XY) by multilinearity in its rows. Row i of XY is ∑j Xᵢⱼ Yⱼ,*, so the expansion is the sum over all functions f:{1,…,k}→{1,…,m} of (∏i Xᵢ,f(i)) times the determinant whose row i is row f(i) of Y. A repeated f-value gives equal rows and determinant 0.

For each injective f, let S={s₁<…<sₖ} be its image and write f(i)=sσ(i) for a unique permutation σ. Its Y determinant is sign(σ)det(Y[S,:]). Summing ∏i Xᵢ,sσ(i) sign(σ) over σ is det(X[:,S]). Therefore

$$\det(XY)=\sum_{\substack{S\subseteq\{1,\ldots,m\}\\|S|=k}}\det(X[:,S])\det(Y[S,:]).$$

If m<k every function repeats a value, so both sides are 0. If k=0 the unique empty subset contributes 1. Thus the formula includes the small and sparse boundary cases.

## Step 3: apply the expansion

Take k=n−1, X=QW and Y=Qᵀ. Multiplying selected columns by their weights and using det(Mᵀ)=det(M) yields

$$\det L^{(r)}=\sum_{\substack{S\subseteq E\\|S|=n-1}}\det(Q[:,S])^2\prod_{e\in S}w(e).$$

It remains to identify the squared incidence minors. The following argument proves that they are exactly the indicators of spanning trees. The coefficient identity, rather than numerical interpolation, supplies the all-real conclusion.

## A complete combinatorial certificate for every incidence minor

## Step 4: a cycle forces a zero minor

Fix S⊆E with |S|=n−1. If (V,S) contains a cycle, traverse that cycle once. Multiply each corresponding incidence column by +1 or −1 according as its orientation agrees or disagrees with the traversal. Their sum is zero, since every cycle vertex has one incoming and one outgoing contribution. The columns are dependent even before deleting row r, and remain dependent afterward. Thus det(Q[:,S])=0.

## Step 5: an acyclic selection is a spanning tree

An acyclic graph on n vertices with c components has n−c edges. To justify the count, each component with at least two vertices has a leaf: an endpoint of a longest simple path has no additional neighbor, since that would extend the path or create a cycle. Removing a leaf removes one vertex and one edge; induction gives v−1 edges for each nonempty component, including the one-vertex base. Summing over components gives n−c.

Since S has n−1 edges, acyclicity implies c=1. Hence every non-tree selection of this size has a cycle and was already eliminated. This avoids assuming that every n−1-edge selection is connected.

## Step 6: a tree minor is +1 or −1

Induct on n. For n=1, the minor is empty and has determinant 1. For n≥2, a tree has at least two leaves: both endpoints of a longest path have degree one. Choose a leaf v distinct from the deleted root r. Its row is still in Q[:,S] and has exactly one nonzero entry, equal to +1 or −1, in the column of its unique incident edge.

Expanding along row v gives the determinant, up to sign, of the analogous reduced incidence matrix of the tree obtained by removing v and its edge. The root r remains. Induction gives absolute determinant 1. Therefore det(Q[:,S])²=1 for every spanning tree and 0 for every other S of size n−1.

## Step 7: conclude the identity

Insert this indicator into the expansion above. Precisely the spanning-tree products remain. This proves the stated identity in the model-written argument for every root and every real weight assignment, including disconnected graphs and signed or zero weights. Root independence follows because the right side does not refer to r.

## Finite execution checks support the argument; they do not replace it

## Worked triangle

For edges01,02,12 with weights2,3,5, the Laplacian is

$$L=\begin{pmatrix}5&-2&-3\\-2&7&-5\\-3&-5&8\end{pmatrix}.$$

Deleting row/column0 gives determinant7·8−25=31. The three products are6,10,15.

## Executed verification scope

The original finite scope is every labeled simple graph on n=1,…,5 (1099 graphs),5405 rooted cofactors with two determinant methods,100 signed rational inputs of orders 1,…,6,19160 rooted incidence minors on complete graphs of orders 1,…,6, and 30 Cauchy–Binet controls. This is one deterministic positive weighting per enumerated graph, not all weights.

The exhaustive graph test enumerates masks of every unordered vertex pair. Present edge number j in the complete graph receives weight 1+(j mod 5), so the positive weights are a single deterministic assignment per graph, not every assignment. Candidate trees are all edge subsets of size n−1, tested by union-find for cycles and connectivity. Each accepted tree contributes its exact product.

The determinant routes differ: one uses Gaussian elimination over fractions.Fraction with row swaps; the other sums all signed permutation products directly. The signed sample uses seed 2026111613 and exact rational weights. Separate complete-graph incidence checks exercise zero and unit minors and simultaneous orientation reversal. All input matrices, graph masks, weights and exact outputs are included.

These programs share an author, host, Python runtime and input representation. Agreement is an algorithmic cross-check, not external mathematical validation. The real-weight conclusion comes from the written polynomial argument, not from the number of passing tests.


## Distinct adversarial review and revisions

An initial shortcut would infer the minor lemma from the rank of the full incidence matrix. That alone neither proves every selected tree minor is unimodular nor deals with each selected column set. The final argument uses cycle dependence and leaf expansion explicitly. This is a discarded reasoning shortcut; no failed external computation or reviewer is implied.

## Source verification and limits

David G. Wagner, *Combinatorics of Electrical Networks*, University of Waterloo lecture notes, June/July 2009. Theorem 5 on PDF pages 8–9 gives the weighted identity; Proposition 3 gives the incidence-minor criterion. These specific source sections were retrieved in the original investigation. URL: https://www.math.uwaterloo.ca/~dgwagner/Networks.pdf

The theorem and proof method are classical. No novelty review, formal checker or external proof reviewer was used. The source corroborates the mathematical background; it does not certify this report or its code. Classification remains **CANDIDATE PROOF (not independently verified)**.

## Public reproduction and evidence

Python3 standard library only; assertions must remain enabled (do not use `-O`). From this investigation directory run:

```bash
python3 verify.py fresh_results
```

The public script is unchanged from the original mathematical verifier. Every exact input and certificate it emits is included in `results/`; actual publication stdout, stderr and commands are included with timestamps in the batch `VERIFICATION.json`. Run `python3 verify_all.py` from the parent batch directory to check the SHA-256 inventory and compare fresh outputs against all published result JSON files.

`PROVENANCE.json` retains source report/package identities, original archive digest, member hashes and corrected/legacy labels. The original mixed operational archive and report-building environment are not published. References above describe source checks recorded in the original investigation; publication replay does not represent a new literature review or external endorsement.

The complete model-written proof and finite computations remain distinct. Different implementations share authorship and execution environment; none is a formal proof assistant or an independent external referee. Classification remains CANDIDATE PROOF.
