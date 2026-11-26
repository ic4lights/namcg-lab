VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M5 | FLAGS: none | PROGRESS: first | OPEN: 0/3

## Verdict
The central algebra and rank computations are correct and reproducible. The package is not integrable as drafted. Its headline no-go is already in the merged 008 paragraph. The N_tot sentence is unsupported. The literature sentence attributes more than the abstracts support. The new definition also needs repairs.

## Source reading
FULL SCAN, as CLAUDE.md 3(c) requires. I read all 30 current chapter files: ch01-ch18 and appA-appL, with appH read in full (lines 1-2330). The digest was CURRENT at the start.

After I finished, proposal 010 was integrated (commit ab0fa84). It changed ch09 (one Stelle clause) and appK (one paragraph). I did not re-read those two files whole. I read the git diff 20715b7..ab0fa84 for `chapters/`. The edits only add scope qualifiers. They do not touch ch03 or appH, and they contradict nothing in 009.
- After the 010 integration the digest is CURRENT.
- The ch03 anchor ("analysis with a \(c\)-number \(\Theta^{\mu\nu}\)." before `\end{definition}`) still occurs once.
- The appH anchor ("Problem~F, and Problems~A, B, C and~D, remain open.", followed by a blank line and `\section{Problem G: HBEV}`) still occurs once.
- Every label listed below occurs once.

## Claim under review
The proposal adds the ch03 definition `def:matrix-coords-ext` (D matrix coordinates, Poisson limit, 4-dimensional symplectic leaf, fixed η_IJ). It adds one appH paragraph (a-d below). It adds two BibTeX entries.
- **a)** G = (θᵀgθ)⁻¹ ≠ c·g for any D ≥ 4 when g is real Lorentzian.
- **b)** The linear Einstein-operator rank is 3 about a flat brane for every D. About a generic curved brane it is min(6, D-1).
- **c)** The N_tot = D-2 bookkeeping.
- **d)** Literature context.

Target: `ass:emergent-op` (Problem F), with A, D1 and E by dependency. Current Appendix H labels, quoted verbatim:
- F: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- A: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
- D: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2 ... supports only a scope-limited Presentation-B model; D remains OPEN ..."
- E: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

The Chapter 17 `sec:ch17-done` criterion lists A, B, C, D1, E, F, G-derived and N. No discrepancy with Appendix H or CLAUDE.md. The original target is not met by this package. No label change is proposed, and the proposal states none.

## Checks performed
**Direct verification**
- **(a) Algebra.** I re-derived it by hand. G = ωg⁻¹ωᵀ with ω = θ⁻¹ and ωᵀ = -ω, so G = -gM² with M = g⁻¹ω. Then det M = Pf(ω)²/det g < 0 for Lorentzian g.
  - G = cg forces M² = -c.
  - c > 0 because G is congruent to g⁻¹, so its signature is (-+++), and cg has that signature only for c > 0.
  - A real 4×4 M with M² = -c has eigenvalues ±i√c in conjugate pairs, so det M = c² > 0. This contradicts det M < 0.
  - My own numpy run confirmed det M = Pf²/det g (negative) and G = -gM². Their `check_conformal_nogo.py` reproduced the same results (min relative residual 0.22-0.42 for D = 4..11).
- **(b) Rank, scripts.** I re-ran `check_brane_rank.py`. The table reproduces exactly: flat brane 3 for all D = 4..11; generic II 3,4,5,6,6,6,6,6; K-traceless II identical. The Hamiltonian-gauge check is True in every run.
- **(b) Rank, independent check.** My own numpy script uses different random draws and SVD ranks. It gave flat [3,3,3,3,3,3,3,3] and generic [3,4,5,6,6,6,6,6]. It also confirmed that ξ = θᵀp gives δG = p∘(Gξ).
- **(b) Formulas.** I checked the hand-coded linearized Ricci and Einstein symbol against the standard δR_ab. I checked δg = L_ξ g - 2φ_iII^i by direct differentiation: the normal part drops out of the tangent term and ∂n·∂x = -II. The Hamiltonian vector field of e^{ip·y} is ξ ∝ θᵀp.
- **(b) Rank logic.**
  - The upper bounds are exact. The image contains the gauge direction, and Einstein is annihilated by Diff_G (4-dim), so the rank is ≤ D-1. The image also lies in the 6-dim space of conserved tensors, so the rank is ≤ 6.
  - The flat value 3 is exact for all D, not only for the tested D. Normal modes do not enter δg at first order, so the image is the D = 4 image. A constant g maps to η by a linear change of y.
  - The lower bounds come from rank samples in exact rationals. The rank is lower semicontinuous in polynomial data, so one full-rank draw proves generic full rank. The upper bounds are trivial. So one draw per entry is adequate, provided the text states this logic.
  - The frozen-coefficient (WKB) treatment is consistent once the normal amplitudes are rescaled φ ~ p·ξ, so that both mode types enter δG at order p. Corrections are then suppressed by 1/(pL).
  - The Gauss-Codazzi caveat and the "kinematic only" caveat are correctly stated. I confirm "D ≥ 8 including the density scalar is a necessary count only".
- **Anchors and labels.** I ran `verify_anchors_labels.py`: all existing labels count 1, `def:matrix-coords-ext` counts 0 (new), `app:status`, `ch:vierbein-emergence` and `eq:Geff-structure` exist. The bib key `Steinacker2023` exists, and `KumarSteinacker2023` and `Steinacker2026` are absent (new).

**Literature (fetched)**
- **arXiv:2303.08012.** H. C. Steinacker, "One-loop effective action and emergent gravity on quantum spaces in the IKKT matrix model" (Mar 2023). The abstract says the brane sits alongside compact fuzzy extra dimensions, with the Newton constant set by the Kaluza-Klein scale. The existing `Steinacker2023` entry (JHEP 05, 129, 2023) matches Crossref. **BibTeX record: VERIFIED.**
- **arXiv:2312.01317.** K. Kumar and H. C. Steinacker, "Modified Einstein equations from the 1-loop effective action of the IKKT model" (v1, 3 Dec 2023). It covers dilaton/axion terms and an "anharmonicity tensor" C_μν, with no journal reference. The proposed `KumarSteinacker2023` entry (authors, title, year 2023, eprint) matches. **BibTeX record: VERIFIED.**
- **arXiv:2601.08031.** H. C. Steinacker, "Modified gravity at large scales on quantum spacetime in the IKKT model" (v1, 12 Jan 2026), sole author. It covers an extra geometric tensor ("mirage matter") and non-Ricci-flat modes. The proposed `Steinacker2026` entry matches. **BibTeX record: VERIFIED.**
- **arXiv:1606.00769.** It is already in the repository as `Steinacker2016Gravity`. I did not re-fetch it.
- These are abstract-level checks only. Full texts were not read, so the result content is not independently verified.

**Not verified:** the content of the three papers beyond their abstracts; the quantum spaces' leaf dimension in 2312.01317 and 2601.08031.

## Findings
1. **Major. Location: appH paragraph, "Operator metric versus induced metric", and proposal item 1.**
   - **Finding.** The no-go G ≠ c·g for real Lorentzian g and D ≥ 4 is already in the integrated 008 paragraph (appH "Metric seen by the operators", about line 1822). That paragraph says: "pointwise for any real Lorentzian g, the operator metric G = K⁻¹ is not g; this extends Remark rem:ch3-moyal-check". The "correction to 008" concerns only the 008 proposal's "Decisions Taken" ranking. That is not manuscript text, and the merged manuscript text is correct. The paragraph would therefore restate a merged result as new, and it is not an M2.
   - **Required action.** Delete the proof paragraph. Keep at most one sentence that cites the 008 statement and adds the genuinely new part: the statement is independent of D, and G = cg is possible only for a Euclidean induced g.
2. **Major. Location: appH "Content" paragraph, the N_tot sentence (and proposal item 4).**
   - **Finding.** "N_tot = (D-4) + N_other + 2 ... = D-2" rests on the 005 formula. The merged 005 text says N_s is "an input, not a derived count". The proposal's own item 3 says the healthiness of the normal scalars is not established. The operator O_s for the normal modes was checked only on a flat constant background. Mixing and the response of K to the fluctuation are not treated. The line adds no result and invites a reading as an induced-EH statement.
   - **Required action.** Drop the sentence. Keep the statement that the D-4 scalars are not covered by `ass:locked-block` and that they are extra infrared fields unless gapped. That statement is supported: `ass:locked-block` concerns internal directions of Φ.
3. **Major. Location: appH literature sentences and proposal item 4(b).**
   - **Finding.** "Their quantum spaces have a higher-dimensional leaf" is supported by the abstract only for 2303.08012 (fuzzy extra dimensions). The abstracts of 2312.01317 and 2601.08031, as fetched, say "3+1-dimensional quantum branes" and "covariant quantum spacetime". They do not state the leaf dimension. "Their Newton constant comes from the KK scale" is also attributable only to 2303.08012. "Not checked against our operators" is correct.
   - **Required action.** Attribute the extra-dimension and Newton-constant statements only to `Steinacker2023`. For the other two, say only that they "report modified Einstein equations with extra tensors". Phrase the leaf-dimension relaxation as a possible route in this package's hypothesis class, not as a property of those papers.
4. **Minor. Location: ch03 definition, three items.**
   - (i) ρ is introduced in "Tr → ∫d⁴y ρ" without definition. Add "ρ = 1/|Pf θ|" or the equivalent Liouville density.
   - (ii) "By Remark rem:ch3-moyal-check and Appendix app:status, the inverse of K is in general not proportional to g" is too weak and mis-cited. That remark covers D = 4, constant Θ and g = η only. For a 4-dimensional leaf and real Lorentzian g, K⁻¹ is nowhere proportional to g. The proof is in the 008 appH paragraph.
   - (iii) "read with I,J in place of μ,ν" covers the cubic C_{μνλ} term, whose D-index form is unspecified. Restrict it to the first (quartic) term and the matter term. "The case D = 4 is Definition ..." should read "reduces, for D = 4, to ...", because the new definition adds the semiclassical reading.
5. **Minor. Location: ch03 insertion point.** The definition sits before the paragraph defining Λ_UV and before eq:Smatrix, which it cites. A cleaner anchor is the end of the paragraph ending "The existence of such a map is enough for now.", just before `\section{Presentation B...}`. The integrator must verify that this anchor occurs exactly once.
6. **Minor. Location: appH, signature contrast.**
   - With η having a single negative sign, a pulled-back 4×4 g has at most one negative eigenvalue. A (2,2) induced g is therefore not realizable in this class; drop it.
   - A Euclidean induced g allows G ∝ g, but then G is Euclidean (G is congruent to g⁻¹), so there is no Lorentzian loophole.
   - The hypotheses of the no-go are: real 4-dimensional leaf, Poisson limit, real Lorentzian g. Relaxing the leaf dimension is the within-core route. The other relaxations are complex or Moyal-corrected structures and the E-related signature question.
7. **Minor. Location: appH "Linear response".**
   - State that a factor i is absorbed in ξ.
   - Say "ξ ∝ θᵀp".
   - Say "exactly three for every D" for the flat brane, because normal modes do not enter δg at first order.
   - State the generic-rank logic of (b): the upper bound is exact, and the lower bound is one exact-rational draw, generic by lower semicontinuity.
8. **Minor. Location: appH closing sentence.** It repeats 008's closing line on consecutive paragraphs and lists a fixed problem set ("Problem F, and Problems A, B, C, D and E, remain open."). CLAUDE.md asks to avoid repeating a fixed critical-problem list. Suggested closing: "This changes no ledger label; Problem~F remains open." Alternatively merge the paragraph into 008's as a continuation.

## Scope of what is established
- **Established (exact algebra).** G = -gM² and det M = Pf²/det g, so G ≠ cg pointwise. Hypothesis class: real 4-dimensional symplectic leaf, Poisson limit, real Lorentzian induced g, any D ≥ 4. It is already merged via 008. The Euclidean contrast is established but irrelevant to a Lorentzian emergent metric.
- **Established (kinematic, exact-rational samples with trivial upper bounds).**
  - Linearized Einstein rank is 3 about a flat brane for all D.
  - It is min(6, D-1) for generic frozen second fundamental forms, with and without K^{μν}II^i_{μν} = 0.
  - All six conserved sources are reachable from D = 7.
  - Including the density scalar, D-1 ≥ 7 is a necessary count only.
  - The hypothesis class is: Poisson limit, 4-dimensional leaf, leading-order WKB with frozen g, θ and II at a point, Gauss-Codazzi not imposed, generic p. This is a bounded sharpening, not a new route-closing no-go.
- **Not established.** Any Einstein-type field equation for G; whether the transverse scalars are gapped; the identification of Φ with a tangent frame; any G_eff; any extra conserved stress; and that the one-loop literature supplies the 008 extra stress.
- **Completion and status.** The package is PROGRAMME-CONDITIONAL. F, A, D and E remain OPEN with their labels unchanged. Emergence is preserved: η_IJ is a fixed contraction of matrix indices as in eq:Smatrix, no metric enters the action, and the operator metric G is built from θ and the configuration. `ass:lorentzian` is explicitly retained, not derived.
- **No BREAKTHROUGH.**
- **Milestone.** M5 only, and only if the definition is integrated. It is a pre-approved structural addition, with no label change and no AUTHOR-DECISION needed. I judge M2 not warranted, because the no-go is already merged. M1 and M3 do not apply, because no merged claim is wrong.

## Recommended disposition
Revise, then integrate the shortened package.
- **Definition: keep it, after repairs.** It gives the D > 4 hypothesis class a labelled home, which the unlabeled "Suppose..." sentence in 008 lacks. It is the setting that a leaf-dimension relaxation would need. It adds no new assumption and is flagged conditional. If the integrator wants the smallest change, the appH paragraph alone would suffice, but I recommend keeping both.
- **appH paragraph: shorten.** It should contain the linear-response ranks, the not-covered-by-`ass:locked-block` remark, the corrected literature sentence, and a brief cross-reference to the 008 no-go.
- **Bib entries.** The integrator may add `KumarSteinacker2023` and `Steinacker2026` as proposed. The records are verified, and no journal data are claimed. Optionally add `primaryClass`.

## Corrected snippet
Replace the whole "Operator metric versus induced metric" paragraph with:
```latex
\emph{Operator metric versus induced metric.} The relation \(G=c\,g\) is excluded for every \(D\ge4\) by the argument of the preceding paragraph, because only the real four-dimensional leaf and the real Lorentzian \(g\) enter it; for a Euclidean induced \(g\) an orthogonal complex structure gives \(G\propto g\), but then \(G\) is Euclidean.
```
Replace the literature sentence with:
```latex
One-loop IKKT calculations on a brane with compact fuzzy extra dimensions report an induced Einstein--Hilbert term with the Newton constant set by the Kaluza--Klein scale~\cite{Steinacker2023}, and modified Einstein equations with extra tensors are reported in~\cite{KumarSteinacker2023,Steinacker2026}. A leaf of dimension greater than four is the hypothesis of the first statement above that such a construction would relax. These results have not been checked against the present operators.
```
Remove the N_tot sentence. Insert "\(\rho=1/|\operatorname{Pf}\theta|\)" in the definition after "\(\operatorname{Tr}\to\int\mathrm{d}^4y\,\rho\)". Make the other minor edits as listed.

Extra assumption: none. Files: `C:\Users\redgi\Projects\namcg-lab\proposals\009-matrix-coords-N8\proposal-r1.md`; my independent check script `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\4d0177a0-6b3d-45ad-bb6d-645d2be99f00\scratchpad\gk_rank.py`.
