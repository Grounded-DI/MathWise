# Barei Evolution Algebra Audit Confirmation

**The principal mathematics survived this bounded audit under the stated hypotheses.** A source-informed, AI-assisted mathematical audit commissioned by Mark S. Weinstein reconstructed the counterexample and principal arguments in Andres Barei’s *On Solvable Evolution Algebras and a Conjecture by García-Martínez and Pérez-Rodríguez*. The paper credits Muse Spark and names Nicolás Jaramillo Torres as reviewer. This is a separate review of the public manuscript, with no endorsement implied by its authors or Meta.

Published to MathWise on 3 October 2026 at Mark S. Weinstein’s request, following preparation for review earlier that day. The authors have not been contacted. This companion leaves the earlier detailed audit intact and adds a dated rerun and proof review in the same assistant workflow. It is not blind replication, a second independent human expert review, or a proof-assistant formalization.

## What survived checking

The original conjecture of Xabier García-Martínez and Andrés Pérez-Rodríguez proposed an equivalence between solvability and absence of nonzero idempotents for finite-dimensional complex evolution algebras. Barei’s Example 2.1 disproves the reverse implication. Its derived dimensions are **3 → 2 → 2**, and zero is its only complex idempotent.

The manuscript’s standing field assumption is algebraic closure, with no characteristic exclusion for the abstract results. Example 2.1 itself is over the complex numbers. Multiplication is bilinear, generally nonassociative; distinct natural-basis vectors multiply to zero. Rows of the structure matrix encode basis squares. The derived term is formed from the span of **all products** in the preceding term.

Lemma 3.1, Theorems 3.2 and 3.3, Corollary 3.4, and Remark 3.6 remain supported by the reconstructions. The stable derived-series arguments hold for general finite-dimensional algebras with bilinear multiplication. Remark 3.5 is a search observation and is not treated as a theorem.

## What the audit added

**Exhaustive idempotent elimination.** From the published matrix the equations are x = −2x², y = y² − z², and z = 2x² − y² + z². Thus x is 0 or −1/2. Set s = y + z = 2x²; then (1 − 2s)y = −s². For x = 0 this forces y = z = 0. For x = −1/2 it forces 0 = −1/4. Every complex solution is covered by these two branches.

**A precise, shorter existence argument.** Yuri Lyubich and Alexander Tsukerman’s 2014 Theorem 2.1 provides the idempotent-or-square-zero existence result over every algebraically closed field. Applying it to a nonzero subalgebra with no nonzero square-zero element supplies the converse of Barei’s Theorem 3.3. Its proof and geometric dependency were reviewed separately from the code. Applying the same result directly to the stable term also shortens Corollary 3.4.

**An explicit strictness witness.** The audit independently constructed a four-dimensional complex evolution algebra whose stable term has no nonzero square-zero element but admits no natural basis. It therefore meets Barei’s sufficient condition while failing Hu–Wen’s sufficient hypothesis that the stable term itself be an evolution algebra. The detailed audit supplies the matrix, induced multiplication, exhaustive square-zero argument, and exact noncommuting-matrix obstruction. This construction is a supporting witness from this audit; historical novelty has not been established.

## Comparison and credit

The retrieved Hu–Wen example and Barei’s Example 2.1 are isomorphic through e₁ ↦ −h₂, e₂ ↦ h₃, e₃ ↦ −h₁. The nine basis-product identities and invertibility check pass exactly. This qualifies any claim of a distinct counterexample class relative to the acknowledged concurrent work. The explicit comparison makes no inference about copying, independence of discovery, or model training exposure.

Credit belongs to Andres Barei and the paper’s named reviewer, Nicolás Jaramillo Torres; Muse Spark’s role is attributed as reported by the authors. The original conjecture is due to Xabier García-Martínez and Andrés Pérez-Rodríguez. Xing-Yu Hu and Ran Wen supplied the acknowledged concurrent counterexamples and stable-term criterion. Yuri Lyubich and Alexander Tsukerman supplied the older general existence theorem used in the alternative proof. Ravi Vakil’s geometry notes support the properly qualified Bézout dependency.

The specific sufficient condition in Corollary 3.4 is strictly broader than Hu–Wen’s condition, as the witness confirms. Global priority for that exact formulation remains unresolved. The authors’ statements and margin labels document a reported AI collaboration; interaction logs, prompts, and version histories were not supplied. This audit does not independently reconstruct Muse Spark’s contribution or demonstrate a causal benefit from Grounded DI or Protocol A.

## The new rerun and its scope

The unchanged checking program ran under Python **3.12.14**, exited with code **0**, and returned **PASS for all 11 exact check groups**. The rerun is recorded at **2026-10-03 15:04:32 UTC**, or **11:04:32 a.m. EDT**. Its eleven check records match the archived results. Fresh downloads of five central primary PDFs also match their earlier recorded hashes. No material correction to the principal conclusions was found; this companion uses the exact Hu–Wen theorem locator, p. 3.

C01–C03 cover the counterexample’s products, derived term, and analytically forced idempotent branches. C04 checks the Hu–Wen isomorphism. C05–C06 check the four-dimensional embedding, multiplication identities, nonzero commutator, and an idempotent. C07–C11 probe field, characteristic, necessity, coefficient sensitivity, and multiplication-closure limits.

The square-zero-free property of the four-dimensional witness and the implication from a natural basis to commuting operators are mathematical arguments. C06 checks their finite matrix data; it does not machine-prove their universally quantified conclusions. Similarly, the code does not prove the general derived-series or geometric existence theorem.


To reproduce the finite checks from this directory, use Python 3.8 or newer with the standard library, without `-O`:

```bash
python3 verify_audit.py --output my_results.json
```

An additional prepublication run returned the same eleven check records; its [actual results](evidence/results_publication_run.json) are separate from the preserved earlier rerun.

Correctness rests on the disclosed calculations and proof dependencies. Reproducibility means the program and actual outputs are available for rerun. SHA-256 records identify exact file bytes for comparison with a trusted copy; they do not prove mathematical correctness or authorship. The original archive’s seven listed file hashes and its ZIP integrity check passed. The saved standalone PDF and the PDF inside that archive have distinct byte hashes but matching extracted page text and decoded page-content streams; the input record identifies both variants.

## Inspect the evidence

- [Complete original review package](artifacts/Barei_Public_Audit_Review_Package.zip) and [supplied ZIP SHA-256 record](artifacts/Barei_Public_Audit_Review_Package.zip.sha256.txt)
- [Four-page public companion](artifacts/Barei_Public_Audit_Companion.pdf)
- [Claim-to-evidence table](CLAIM_EVIDENCE.csv), with exact primary-source and detailed-audit locations
- [Unchanged checker](verify_audit.py) and [actual rerun results](evidence/results_rechecked.json)
- [Actual run log](evidence/run_log_rechecked.txt) and [dated recheck record](evidence/RECHECK_RECORD.json)
- [Earlier detailed audit](input_record/Barei_Evolution_Algebra_Audit.pdf) and [earlier checks archive](input_record/Barei_Audit_Checks.zip)
- [Source manifest](evidence/source_manifest_original.json) and [fresh source checks](evidence/sources_rechecked.json)
- [Publication provenance](PUBLICATION_RECORD.json) and [published-file SHA-256 inventory](SHA256SUMS.txt)

The complete review ZIP and earlier audit records are preserved byte-for-byte. Their internal draft-status language records the preparation stage. This repository note updates the publication status and evidence links. The separately attached companion PDF has a different byte hash from the version inside the ZIP, but all four pages’ extracted text and decoded content streams match. Both hashes are disclosed in the publication record.

Remaining limits include the exact Harris fixed-point locator, direct checking of Hu–Wen’s older 2017 classification identification, submission-history chronology, global novelty, and AI interaction provenance. The needed existence conclusion is supported through Lyubich–Tsukerman and its disclosed argument. The review package includes public source links and preserves these unresolved records.

## Primary sources

1. [Barei and the official Meta publication](https://ai.meta.com/research/publications/on-solvable-evolution-algebras-and-a-conjecture-by-garcia-martinez-and-perez-rodriguez/): §2 and Example 2.1, pp. 2–3; Lemma 3.1 and Theorems 3.2–3.3, p. 3; Corollary 3.4, pp. 3–4; Remarks 3.5–3.6, p. 4; attribution statement and reviewer, p. 1.
2. [García-Martínez and Pérez-Rodríguez](https://doi.org/10.1007/s00013-026-02251-0), *A note on complete evolution algebras*: Conjecture 3.6, printed p. 602 / PDF p. 6; finite-dimensional complex scope begins in §3, printed p. 600 / PDF p. 4.
3. [Hu and Wen](https://arxiv.org/pdf/2609.25023), *Idempotent-free non-solvable evolution algebras over C*: Theorem 2.1 and Corollary 2.2, p. 3; displayed exceptional matrix, Remark 2.5, p. 4; Proposition 2.8, p. 6.
4. [Lyubich and Tsukerman](https://arxiv.org/pdf/1403.4623), *Idempotents in nonassociative algebras and eigenvectors of quadratic operators*: Theorem 2.1, p. 2; Lemma 3.2, pp. 4–5; proof, p. 5. The algebraically closed-field result has no characteristic exclusion.
5. [Vakil, class 31 geometry notes](https://math.stanford.edu/~vakil/0506-216/216class31.pdf): Bézout exercise 1.8, p. 4; complete-intersection degree, §1.10, p. 6.
6. [Meta’s official announcement](https://research.meta.ai/blog/solving-open-research-problems-together), 2 October 2026, sixth-paper section: public description of the author-reported Muse Spark collaboration and named review.
