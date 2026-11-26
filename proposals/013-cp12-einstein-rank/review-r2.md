VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
All six review-r1 snippets are applied verbatim, the major attribution finding is closed, and nothing else in the LaTeX or bib record changed. Accepted as a bounded kinematic sub-lemma. It is not a breakthrough and changes no label.

## Source reading
Digest + targeted reads. This is not a full scan and not a 5th-item scan.

I re-read in full:
- proposal-r2.md
- review-r1.md
- the word-level diff r1 to r2
- `verify_anchors_labels.r2.out.txt`

I grep-checked the anchor and the label definitions in `chapters/`.

I did not re-run `check_cp12_geometry.py`. The proposal folder has no uncommitted changes. `git diff HEAD~3 --stat -- chapters` is empty, so the manuscript is untouched.

The mathematics was verified in round 1 and r2 states that it did not change. That covers the independent rank re-derivation (image 9, rank 6, kernel 3), the Liouville identity and the gauge identification. I rely on that review and re-verify only the changes.

## Claim under review
The claim is the kinematic result for the CP^{1,2} conjugate-coordinate class (`H_CP`). It covers the first-order response of the fibre-integrated operator tensor, the linearised Einstein rank (9 and 6, kernel equal to the transverse diffeomorphisms), and a closure criterion for the base functions.

The target is Problem F (`ass:emergent-op`), with A, D1 and E by dependency. The Appendix H F status reads: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL." The Chapter 17 set at the full-GR / matrix-derived scope is A, B, C, D1, E, F, G-derived and N. All stay OPEN. The original target is not met.

## Checks performed
- **Snippet 1 (hedged tower sentence).** Verbatim in the first LaTeX paragraph. The sentence now reads "Fibre harmonics of the fluctuation matrices form the higher-spin tower described in~\cite{...}; the relation of the amplitudes ... is not examined here." The identification with a "lowest member" is gone, so the major attribution finding is resolved. The Literature note in the research section was also reworded to say that the text does not identify `b` with a member of the tower.
- **Snippet 2 (cross-reference opening).** Verbatim: "This paragraph supplements the preceding one, which left the rank ... uncomputed." The 011 text is unchanged.
- **Snippet 3 (surjectivity and divergence-free gauge group).** Verbatim, placed after "at most nine".
- **Snippet 4 (Yang--Mills-type analogy).** Applied as "A Yang--Mills-type tree-level quadratic action, analogous to that of Remark~\ref{rem:ch3-trace-quadratic} and built from first derivatives of \(A\), gives equations of second order in these amplitudes (no such action is computed in this class), whereas \(\mathcal E[h]\) is of third order ...". It is hedged and cited only as an analogy, as the review required.
- **Snippet 5 (base functions).** Verbatim:
  - "for \(\beta\neq0\) also \(\Box u^\mu\) ..." is stated.
  - "using these expressions" is added.
  - "for \(\alpha=\beta\) the \(u^\mu\) are not independent and the test does not apply" is added.
- **Snippet 6 (sheet).** "(the other sheet is not included)" is present.
- **No other change.** The word diff shows changes only in the changelog, the Source reading and Literature notes, Decisions Taken, and the six snippet sites. The Result, claim classification and scripts are unchanged.
- **Anchor.** `\section{Problem G: HBEV}` occurs exactly once (line 1857). The preceding line is the 011 torsion paragraph, which ends "This changes no ledger label; Problem~F remains open."
- **Labels.** Each of `rem:ch3-trace-quadratic` (ch03:450), `def:matrix-coords-ext` (ch03:173), `ch:vierbein-emergence` (ch04:2) and `ass:EE` (ch06:71) is defined once. `ass:emergent-op` occurs once in the r2 verification output. The proposal introduces no new labels.
- **Labels and status.** No label, status or priority text is changed.
- **Process language.** None appears in the LaTeX block.
- **Emergence.** The metric is built from the fibre average of K, so spacetime stays emergent.
- **BibTeX.** `SperlingSteinacker2019` is absent from `bib/namcg.bib`, so the integrator must add it. The entry is identical to r1 (the diff shows no change).
- **BibTeX record: VERIFIED.** Metadata only: title, authors, JHEP 2019 issue 7 article 10, DOI 10.1007/JHEP07(2019)010, arXiv 1901.03522. Content beyond the abstract is not independently verified, and the text does not rely on it.

## Findings
1. **Minor, not blocking, in the proposal file only.** The first line of Decisions Taken contains a literal "\n-" typo. It is outside the manuscript text. Do not carry it into any commit message or ledger entry.

No findings on the LaTeX.

## Scope of what is established
**Exact or derived in `H_CP`:**
- the δK first-order formula
- the fibre-integrated response and the constraint ∂∂(δ𝒦/m)=0
- that only the first harmonic contributes
- image dimension ≤9, and rank 6 on the image with kernel equal to the 3 transverse diffeomorphisms (exact-rational)
- the leading gauge image
- the Box eigenvalues and the closure criterion within the Lorentz-vector family

**Conditional:** the Poisson limit, linear order, frozen coefficients, leading order in 1/(|q|ℓ), and one fibre sheet. The inputs are η, T^a=M^{a4} and the orbit CP^{1,2}.

**Open or not established:**
- any field equation
- the second-order versus third-order mismatch
- masses, positivity and decoupling of the amplitudes
- subleading terms
- fibre-non-constant δK
- identification of G with the emergent metric
- G_eff
- the background as a solution
- that y^μ is the physical base

The no-go side result is exact only within the fibre-averaged, fixed-base-function, linear class. Relaxing any of those hypotheses is not excluded.

Status: PROGRAMME-CONDITIONAL. F and the other critical-path problems stay OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. No BREAKTHROUGH and no milestone trigger (M1 to M5) applies.

## Recommended disposition
Integrate as ordinal 13. Accepted are exactly:
1. Both `\paragraph{...}` blocks in the r2 LaTeX block ("Conjugate-coordinate class: first-order response and linearised Einstein rank" and "Why \(y^\mu=M^{\mu5}/R\) in this class"), inserted immediately before `\section{Problem G: HBEV}` in `chapters/appH-microscopic-proofs.tex`.
2. The BibTeX entry `SperlingSteinacker2019`, exactly as in r2, added to `bib/namcg.bib`.

Preserve CRLF line endings.

The integrator should run `build_check.py`. The new `\cite{SperlingSteinacker2019,MantaSteinacker2025}` needs the bib entry to resolve.

## Corrected snippet
None needed.
