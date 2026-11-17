# Cycle14 — Cauchy–Davenport through a coefficient identity

Grounded DI LLC · Mark S. Weinstein · Series MWR-20261116-24H

**CANDIDATE PROOF — classical theorem reconstruction.** This is a new public mathematical edition derived from the original report and proof text, not the original PDF or a claim of a new theorem.

## Precise theorem and definitions

For every prime p and every pair of nonempty subsets A,B of the field Fₚ of residues modulo p, define A+B={a+b mod p : a∈A, b∈B}. Then the Cauchy–Davenport theorem asserts:

$$|A+B|\geq\min\{p,|A|+|B|-1\}.$$

The sets contain distinct residues, not multisets. The conclusion counts distinct sums, not representations. The bound is sharp for every permitted size pair. This is a classical theorem reconstruction, not a novelty claim.

## Why this investigation matters

The theorem converts the sizes of two sets into a guaranteed amount of additive expansion. It is a useful test of the polynomial method: a hypothetical small sumset creates a polynomial that vanishes on a grid, while one coefficient forces a nonzero grid value. The critical details are the total-degree bound, nonzero interpolation denominators and arithmetic in a field.

## A worked sharp example

Take p=7, A={0,1,2}, B={0,1,2,3}. Their sumset is {0,1,2,3,4,5}, with six distinct residues, exactly |A|+|B|−1=6.

## Proof architecture

First derive a coefficient identity from one-variable Lagrange interpolation. Then apply it to the polynomial ∏(X+Y−c) over a hypothetical small container C for the sumset. The large-set case follows separately by intersection counting. This separation avoids factorials divisible by p.

Executed checks:17,148 exhaustive ordered nonempty pairs for p=2,3,5,7;210 seeded pairs for seven larger primes;11,610 monomial coefficient identities;377 interval sharpness cases. The original investigation recorded passing checks in two same-host processes; the fresh publication run also passed. These finite checks do not prove the arbitrary-prime statement.

## A self-contained lemma over any field

## One-variable extraction

Let S be a nonempty finite subset of a field F, with |S|=s. For x∈S put Dₛ(x)=∏_(u∈S, u≠x)(x−u). All factors are nonzero, hence Dₛ(x) is invertible. Empty products equal 1. The polynomials Lₓ(Z)=∏_(u∈S,u≠x)(Z−u)/Dₛ(x) have degree s−1 and satisfy Lₓ(u)=1 if u=x and 0 otherwise.

For every polynomial g of degree at most s−1, g(Z)=∑_(x∈S)g(x)Lₓ(Z): their difference has degree at most s−1 and vanishes at all s distinct elements of S, so it is zero. Comparing the coefficient of Z^(s−1) gives ∑g(x)/Dₛ(x)=[Z^(s−1)]g.

In particular, for integer k with 0≤k≤s−1, ∑x^(k)/Dₛ(x) equals 0 if k<s−1 and 1 if k=s−1. This includes s=1 and k=0; as polynomial evaluation, x⁰=1 also at x=0.

## Two-variable coefficient formula

Let |A|=m≥1 and |B|=n≥1, and let f(X,Y) have total degree at most m+n−2. Then

$$[X^{m-1}Y^{n-1}]f=\sum_{x\in A,\ y\in B}\frac{f(x,y)}{D_A(x)D_B(y)}.$$

Proof: both sides are linear in f, so it suffices to consider a monomial XⁱYʲ with i+j≤m+n−2. The sum on the right factors as (∑xⁱ/Dₐ(x))(∑yʲ/Dᵦ(y)). If (i,j)=(m−1,n−1), both factors are1. Otherwise at least one exponent is smaller than its target: if neither were smaller, their total-degree bound would force equality of both. The smaller-exponent factor is 0 by the one-variable identity. Thus the right side selects exactly the target monomial coefficient.

## The nonvanishing consequence

If the target coefficient is nonzero, f cannot vanish at every point of A×B, because the displayed sum would then be zero. Crucially, we never apply the one-variable interpolation identity to a power above s−1: in every other monomial, a factor with exponent below its target already vanishes. This closes a common gap in attempts to justify the formula.

## The complete argument separates saturation from the polynomial case

## Case 1: |A|+|B| exceeds p

Write m=|A| and n=|B|. If m+n>p, fix any t∈Fₚ. The sets A and t−B have sizes m and n, so they intersect: otherwise their union would contain m+n>p elements of Fₚ. Choose x=t−y in the intersection with x∈A,y∈B. Then t=x+y belongs to A+B. Since t was arbitrary, A+B=Fₚ.

## Case 2: |A|+|B| is at most p

Suppose instead m+n≤p and, for contradiction, |A+B|≤m+n−2. Put d=m+n−2. Since0≤d≤p−2, extend A+B to a subset C of Fₚ with exactly d elements. Define f(X,Y)=∏_(c∈C)(X+Y−c). This polynomial has total degree d and vanishes on A×B.

Its degree-d homogeneous part is (X+Y)^(d), so the coefficient of X^(m−1)Y^(n−1) is binomial(d,m−1)=d!/((m−1)!(n−1)!). Every factorial here is a product of integers strictly below p, hence is nonzero in Fₚ. The coefficient is therefore nonzero. The lemma above forces a nonzero value on A×B, contradicting vanishing. This proves |A+B|≥m+n−1.

If d=0, the empty product is 1. The same contradiction is valid; equivalently, two nonempty sets cannot have an empty sumset. The two cases cover all possible m,n, including singletons, full-field sets and p=2.

## Sharpness for every size pair

For any1≤m,n≤p, choose A={0,…,m−1} and B={0,…,n−1}. Their integer sums cover every integer from0 to m+n−2. Indeed t can be represented using a=min(t,m−1), b=t−a, and 0≤b≤n−1 throughout that interval. Modulo p, this consecutive interval has min(p,m+n−1) distinct residues. Thus the bound is attained for every size pair; no claim that these are all equality cases is made.

## Why primality is essential

Modulo4, A=B={0,2} has A+B={0,2}, of size 2, below min(4,2+2−1)=3. This is a counterexample to the composite-modulus extension, not to Cauchy–Davenport. Differences such as2 are nonzero but not invertible modulo4, so the interpolation denominators cannot be inverted. Treating a ring as a field would invalidate the proof.


Direct enumeration collects all (x+y) mod p in a set. The other route ORs cyclic rotations of the B bitmask, one rotation per element of A, then compares exact masks. Coefficient tests evaluate every monomial of total degree≤m+n−2 on each bounded grid using modular inverses. Sample seed 2026111614 and every actual input are retained. The210 larger samples are30 per prime 11,13,17,19,23,29,31; they are not exhaustive.

## Distinct critique phase and rejected shortcuts

The initial shortcut of applying the polynomial argument at every size was rejected: d! can vanish modulo p once d≥p. The final proof handles m+n>p by intersection counting. A second risk was applying interpolation to arbitrarily high powers; the monomial argument explicitly uses only the low-exponent factor. Distinct residues guarantee invertible denominators. Empty products, singleton grids and characteristic2 are addressed. The composite control confirms that dropping primality changes the theorem.

No proof gap was identified in this review. The argument remains model-written, without external review or formal checking. Algorithms share an author and host; replay shows local reproducibility, not independent mathematical validation. No counterexample was found in the stated prime-field tests.

## Sources and attribution

Noga Alon, *Combinatorial Nullstellensatz*, Theorem1.2 and Section3, primary author-hosted paper: https://www.tau.ac.il/~nogaa/PDFS/null2.pdf. This verifies the polynomial-method framework and its classical Cauchy–Davenport application. The report supplies its own detailed two-variable coefficient derivation.

Simao Herdade, John Kim and Swastik Kopparty, *A Cauchy-Davenport theorem for linear maps*, arXiv:1508.02100 (2015), retrieved abstract. It confirms the classical sumset context and polynomial-method connection. No generalized linear-map result is asserted here. https://arxiv.org/abs/1508.02100

## Public reproduction and evidence

Python3 standard library only; assertions must remain enabled (do not use `-O`). From this investigation directory run:

```bash
python3 verify.py fresh_results
```

The public script is unchanged from the original mathematical verifier. Every exact input and certificate it emits is included in `results/`; actual publication stdout, stderr and commands are included with timestamps in the batch `VERIFICATION.json`. Run `python3 verify_all.py` from the parent batch directory to check the SHA-256 inventory and compare fresh outputs against all published result JSON files.

`PROVENANCE.json` retains source report/package identities, original archive digest, member hashes and corrected/legacy labels. The original mixed operational archive and report-building environment are not published. References above describe source checks recorded in the original investigation; publication replay does not represent a new literature review or external endorsement.

The complete model-written proof and finite computations remain distinct. Different implementations share authorship and execution environment; none is a formal proof assistant or an independent external referee. Classification remains CANDIDATE PROOF.
