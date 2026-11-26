VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/2

## Verdict
The central mathematics holds up when I re-derive it, and the citations check out against their sources. Two wording problems block a plain ACCEPT. First, the symbol γ is used both for the mass parameter and for the kinetic tensor. Second, the finite-N "only for N→∞" sentence gives an so(4,2) argument for a statement about a whole so(p,q) family, and as worded that statement is false. Seven minor corrections are also needed. Exact replacement text is given below.

## Source reading
- **Mode:** digest + targeted reads. No full scan is claimed.
- **Digest:** `make_digest.py --check` printed DIGEST CURRENT (head 92aa29e, dirty-chapters: yes).
- **Baselines match the working tree:**
  - appH: 579751 B, sha256 b6c505ad…5a8a;
  - bib: 26627 B, acbee1ce…738f.
- **Read in full:**
  - appH L596–612, the Problem D header and ledger label;
  - appH L1394–1454 (blocks 050–051, including S₂ = (1/2g²)η^{ab}Tr(A_a(ℰA)_b), background gauge, and the weight w);
  - appH L1482–1521 (Problem E label, 053, start of 054);
  - appH L1573 (058 closing), L1586 (059 closing, P1/P2) and L1588–1589 (anchor);
  - appH L1378 (ℓ, m notation), L2426 (orbit relation, y·y = −ℓ² over A = 0..4, K = (y⁴)²η), L2625 (E^{aμ} = ±mη^{aμ}, "exact in the Lie–Poisson algebra") and L2636 (η_{ab}M^{aμ}M^{bν} = c_θη + yy − tt);
  - ch17 L329–346 (D/D1), L393–398 (E) and L700–740 (completion criterion);
  - ch03 L136–150 (eq:Smatrix), L170–200 (def:matrix-coords-ext) and L260–272 (ass:frame-lock);
  - ch04 L166–180 (ass:nondeg) and L316–332 (ass:lorentzian).
- **Read only partly:** appH L1522–1572 and L1574–1585, the long lines of 054–059, truncated at about 500 characters per line. No conclusion below depends on the truncated parts.
- **Not read this round:** block 052 (L1455–1480) and the dirty 058 files (ch13, ch16, appE, appI). The 059 reviewers found the 058 files unrelated to Problem E. The insert does not rely on 052.
- **Scan ruling:**
  - 3(a): not triggered. This is ordinal 58, and the next 5th-item scan is due at 60.
  - 3(c): not triggered. The insert is a new conditional paragraph. It changes no definition, assumption, scope statement or status. It does make D1 statements: the flat point of the first-order class, frame non-degeneracy on m≠0, and frame-lock/nondeg not discharged. These are conditional and scoped. Placing them in Problem E with a pointer to Section D follows the precedent of 050–052, which sit in D and name F and N. I judge it acceptable.
  - 3(b): not triggered. By the precedent of 059 r2, M2 does not stop the loop.
  - 3(d): addressed by reading the affected Problem E passages directly, with the partial reads noted above.
- **Unreadable files:** none.

## Claim under review
- **The claim.**
  - The semi-classical criterion of arXiv:2605.13294 v2 fails at the flat point of the first-order class. With states of width σ, the ratio of its two sides is g/2σ² (Euclidean) or 2^{−3/4}g/σ² (η, Definition A).
  - Three signature lemmas: Gram, Sylvester, and fibre averaging.
  - On the conjugate-coordinate class:
    - the equation of motion holds iff H = Lᵀh₀L = cη, with γ = 3cη^{c₀c₀};
    - under (9,1), c > 0 and the kinetic tensor is Lorentzian on m≠0;
    - the so(6) twin is Euclidean at the same γ > 0, so there is no selection;
    - there is no finite-N Lorentzian member.
  - The base-presentation average is diag(m², (2ℓ²−m²)/3 ×3).
  - Coupling: ρ_M ∝ 1/|m|, giving g² ∝ |m|⁻³ (conjugate) and |2ℓ²−m²|^{−3/2} (base).
- **Original targets.**
  - E (ch17): "Lorentzian signature is derived rather than retained (Assumption~\ref{ass:lorentzian})".
  - D1 (ch17): SO(3,1) gauge symmetry derived, and "The locked frame and its non-degeneracy on the claimed domain are derived, not assumed".
- **Appendix H, verbatim.**
  - E: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
  - D: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."
- **Critical-path set** (ch17 L700–733): A, B, C, D1, E, F, G-derived, N. There is no discrepancy with appH.

## Checks performed
- **Gaussian ratios, by hand.**
  - The Hermitian kernel pair weight exp(−Q²|z|²/g²) gives ⟨|A_ij|²⟩ = g²/|Q|². Then ⟨|⟨ψ|A|ψ⟩|²⟩ = g²E[G(δ)] with δ ~ N(0, 2σ²·1₄).
  - Euclidean: E[1/|δ|²] = 1/(s²·E… ) with E[1/χ²₄] = 1/2, which gives 1/(4σ²). The ratio is g/(2σ²).
  - η, Definition A: the propagator is ±ig²/(Q·Q ± iε). The Schwinger representation gives (1/2s²)∫₀^∞(1+iu)^{−1/2}(1−iu)^{−3/2}du. The antiderivative is −i((1+iu)/(1−iu))^{1/2}, on the branch e^{i·arctan u}, so the integral is 1+i. The modulus is 1/(2√2σ²) and the ratio is 2^{−3/4}g/σ².
  - Dimensions check out: g² ~ L⁴, so the ratio is dimensionless.
  - The maximum at t′ = t (Euclidean) holds because the smoothed 4D Newtonian kernel is radial and superharmonic.
  - Verified.
- **2605 Eq. (64), side remark.** The imaginary part, π∫d⁴k e^{−|k|²/2}δ(k_η²), equals 2π². So the printed π²(1+i) is low by a factor of 2; the real part is from s1. No SME input is needed. The remark is not in the manuscript, but it affects one constant the insert quotes (finding m4).
- **Lemmas (i) and (ii).** The Gram argument is immediate.
  - Sylvester with a (9,1) form: n₋ ≤ 1. A timelike v ∈ W gives (3,1), because v^⊥ is positive definite.
  - A spacelike W gives (4,0). Otherwise W contains a null vector and the form is degenerate and semidefinite.
  - c = 0 is excluded because the maximal totally null subspace has dimension 1. Verified.
- **Lie identity and its sign.** I checked this independently in the scratchpad file C:/Users/redgi/AppData/Local/Temp/claude/3ba14ee056ac155d/15e6827c-2d5a-4852-be36-98ee14883700/scratchpad/gk_lie.py, using Hermitian-convention generators M = iE in the defining representation and a random symmetric H.
  - Residual ≤ 9e−16 for so(4,2) with c₀ = 4, so(4,2) with c₀ = 5, so(6) and so(4,1).
  - With H = η: γ = +3, −3, +3, +3 respectively.
  - Sign cross-check: Hermitian su(2) gives Σ_j[J_j,[J_j,J_i]] = +2J_i.
  - Sign check of the EOM from the manuscript's S_b + S_γ: [A^ν,[A_ν,A_μ]] = γA_μ.
  - Agreement with merged 051, "{T_a,{T^a,T^b}} = −3T^b" in the real bracket, which is +3 for Hermitian generators.
  - With rank L = 4 this gives EOM ⇔ (tr P)1 − P ∝ 1 ⇔ P = c1, and γ = 3cη^{c₀c₀}. Verified.
  - **New fact:** the four T^a = M^{a4} and their commutators close on a 10-dimensional algebra. That algebra is so(4,1) on the indices {0..4}, not so(4,2). This drives finding M2.
- **so(4,2) has no nontrivial finite-dimensional Hermitian representation.** This is correct. The algebra is simple, so a representation is zero or injective. An injective image in u(N) carries the invariant form −tr(XY), so it is compact with a negative definite Killing form, whereas the Killing form of so(4,2) has inertia (8,7) (s2). The statement is standard, but it is not the statement the EOM needs (M2).
- **Base-presentation average, by hand, from η_CD M^{AC}M^{BD} = ℓ²η^{AB}.** Taking AB = 45, 44 and 55 gives t·y = 0, t·t = ℓ² + m² and y·y = −ℓ² − m².
  - In the rest frame of y the eigenvalues are m² (time), ℓ², ℓ² and −m² (along t).
  - The S² average is ℓ² − |t|²/3 = (2ℓ² − m²)/3.
  - The signature table follows for c > 0. Verified.
  - Here ℓ is the orbit constant, with y_Ay^A = −ℓ² over A = 0..4 (L2426). See m1.
- **Coupling.** The invariant measure of {y_Ay^A = −ℓ²} in the chart y^μ is d⁴y/(2|m|).
  - Conjugate: |det(m²cη)|^{1/2} ∝ m⁴, so ρ² ∝ |m|³. This matches 2605 Eq. (89) with m = ℓ sinh τ (L2480).
  - Base: |det|^{1/2} ∝ |m||2ℓ²−m²|^{3/2}, so ρ² ∝ |2ℓ²−m²|^{3/2}. Verified.
- **Scripts.** I re-ran s1–s4 with output to the scratchpad; the outputs are byte-identical to the committed `.out.txt` files. apply_check reports nothing in the repository; its output is identical to apply_check.txt.
  - The anchor `\paragraph{Status.}␍␊Remains Assumption~\ref{ass:lorentzian}.` occurs exactly once (L1588).
  - Result appH: 590057 B, c0e28e02…b45f, CRLF 3300, bare LF 0.
  - Result bib: 27535 B, 1a27efb3…be37, CRLF 922.
  - The proposal's bib_entries.bib is LF, 877 B; apply_check converts it to 906 B CRLF.
  - All seven refs and three cites resolve, there are no new labels and no duplicate keys.
  - I did not re-run the LaTeX build, which writes to the repository. bibtex must be run at integration.
- **Literature, fetched.**
  - **2605.13294 v2.** Fetched the arXiv abstract and HTML; extracted the PDF text in an isolated scratchpad directory.
    - The PDF prints Eqs. (13), (16), (17), (64), (88), (89) and (100) as the proposal states.
    - The HTML numbering differs ((76), (103), (104), (115)), which explains the scouts' numbers.
    - "we propose", the absolute value, the window |t′−t| < Δ_T (printed "|t′−t′|"), "fails for commutative backgrounds (except for the diagonal elements)" and the Lorentz gauge with Feynman parameter are all confirmed.
  - **1709.10480 v3.** Read the source, section "Lorentzian fuzzy hyperboloids".
    - Confirmed: g = diag(−κ²,1,1,1,1); 4r² + m̃₀² = 0 = (3+κ²)r² + m²; γ̃ = 3P_H for κ² = 1; cosh 2η₀ = (κ²+5)/(κ²−1) "provided κ²>1"; and m² < m₀² < 0.
    - The abstract says "Euclidean 'before' the BB". The DOI 10.1007/JHEP02(2018)033 is listed on the arXiv page.
  - **2512.03161 v2.** Abstract and HTML. Confirmed: the title and authors; "only exists in N→∞ limit"; "four-dimensional Euclidean spacetime with SU(2) isometry"; and no journal reference.
  - **No journal reference is invented.**
- **Wording.**
  - Nothing claims a derived signature.
  - "Nothing here selects the real form…" is present.
  - The dependence on (9,1) is stated as "for h₀ of signature (9,1)". It does not name P1∧P2, but the preceding paragraph does, and that is adequate.
  - The order of limits is stated in the closing paragraph.
  - There is no process language, and there is one scoped closing sentence, distinct from 053–059.
  - There is no label change.

## Findings
1. **Severity: major.**
   - *Location:* the paragraphs "Signature of the kinetic tensor", "Conjugate coordinates" and "Coupling".
   - *Finding:* γ denotes both the kinetic tensor γ^{μν} (2605's notation) and the mass parameter γ of S_γ (053–059). Inside one paragraph, "γ = 0 where m = 0" (the tensor) is followed by "γ = 3cη^{c₀c₀}" and "γ > 0" (the mass). The scope sentence "at fixed γ of the sign stated" is then ambiguous.
   - *Reason:* the clash makes a load-bearing scope statement ambiguous. The manuscript already writes the kinetic tensor as K (def:matrix-coords-ext) and as 𝖪 = θᵀgθ (appH L2618).
   - *Required action:* write the kinetic tensor as \(\mathsf K\) (replacement R1).
2. **Severity: major.**
   - *Location:* the conjugate-coordinates paragraph, its last two sentences.
   - *Finding:* the reason given is that an so(4,2) representation by Hermitian matrices is trivial. But the four T^a and their commutators span only the subalgebra on the indices {a, c₀}, which is so(4,1) for this class (checked numerically). So the EOM never needs all of so(4,2). For the general so(p,q) family that the identity sentence introduces, "the non-zero solutions at finite N are those of compact forms" is false as worded. For example, so(5,1) with four spacelike indices and c₀ spacelike gives a non-zero finite-N solution through the compact subalgebra so(5), and so(5,1) is a non-compact real form.
   - *Reason:* the conclusion (no finite-N Lorentzian member) is true, but it needs the subalgebra argument. This is no-go (c) of the M2 claim.
   - *Required action:* replacement R2.
3. **Severity: minor (m1).**
   - *Location:* conjugate coordinates, "\(\ell^2=-y_ay^a\)".
   - *Finding:* in the insert, a runs over the four T-indices, so this reads ℓ² = −y_μy^μ. But the formulas that follow, |t|² = ℓ² + m² and the average (2ℓ² − m²)/3, and the Coupling paragraph's y_Ay^A = −ℓ², all need ℓ to be the orbit constant, so that y_μy^μ = −ℓ² − m² (L1378, L2426).
   - *Required action:* R3.
4. **Severity: minor (m2).**
   - *Location:* the flat-point paragraph.
   - *Finding:* "so that Δ_T = σ" treats a Gaussian state as if it were quasi-coherent; none exists. Also, at finite N the Minkowski window |t′−t| < Δ_T = 0 contains no t′ ≠ t. The eigenvector argument therefore establishes the failure of (16), not of (17). For η, failure follows from the Gaussian scaling, as Δ_T^{−2}.
   - *Required action:* R4.
5. **Severity: minor (m3).**
   - *Location:* the flat-point paragraph, "the weight w … supplies such a width".
   - *Finding:* w is a weight on p used to truncate the labels. Δ_T measures the spread in p̃ = up, and under the non-compact fibre that spread is not w's width.
   - *Required action:* R5.
6. **Severity: minor (m4).**
   - *Location:* the Coupling paragraph, "as \(g_{\mathrm{YM}}/\sqrt2\) … (its Eq.~(100))".
   - *Finding:* the factor-2 error in Eq. (64), which I confirmed by the δ-function imaginary part, changes this constant to g_YM. The attribution is literal, but quoting a constant we have checked to be wrong should be avoided.
   - *Required action:* R6.
7. **Severity: minor (m5).**
   - *Location:* the base-coordinates paragraph.
   - *Finding:* the signature statements need c > 0, which holds for (9,1) by the argument in the preceding paragraph, but the paragraph does not say so.
   - *Required action:* R7.
8. **Severity: minor (m6).**
   - *Location:* the closing paragraph, "do not apply to these backgrounds".
   - *Finding:* the finite-N results of 053–059 do apply to commuting N×N matrices. The intended referent is the conjugate-coordinate backgrounds.
   - *Required action:* R8.
9. **Severity: minor (m7).**
   - *Location:* bib entry Steinacker2026Weak.
   - *Finding:* the equation numbers are those of the v2 PDF. v1 has different content, and the HTML numbering also differs.
   - *Required action:* R9. Regenerate the apply_check hashes after the change.
10. **Optional, not required.**
    - Replace "It is the mechanism of~\cite{Steinacker2018BB}, where," with "The same mechanism, averaging over the fibre, gives the signature change of~\cite{Steinacker2018BB}, where,". This avoids implying that the four-matrix result appears in that paper.
    - Relating the identity at γ = 0 to the h-form equation of~\cite{Liao2026} (already cited at appH L1464) would place it in the literature. I have checked only that paper's abstract, so I propose no text.
    - A one-line pointer from Section D is not needed.
    - The proposal's word "new" for the identity stays out of the manuscript, as it should.

## Scope of what is established
- **Established (exact or tree-level, within hypotheses):**
  - At the flat point of the first-order class, in background Feynman gauge at tree level, no quasi-coherent state exists. The Euclidean criterion fails, and width-σ Gaussian states give ratios g/2σ² and 2^{−3/4}g/σ². A semi-classical window needs a supplied σ ≫ g^{1/2}.
  - The Gram and Sylvester lemmas.
  - The Lie identity and the equivalence EOM ⇔ H = cη, with γ = 3cη^{c₀c₀}.
  - The so(6) twin solves the same equation at the same sign of γ.
  - The base-presentation average and its signature table.
  - ρ_M ∝ 1/|m| and the two exponents of g².
- **Conditional:**
  - Lorentzian kinetic tensor on m≠0, with c > 0 and W timelike. This holds only for h₀ of signature (9,1), which 059 fixes only under the imposed P1∧P2, and only for the supplied class.
  - The semi-classical domain lies inside the Lorentzian one. This rests on 2605's late-time estimate.
- **Bounded no-gos, and their exact classes:**
  - (a) H1–H5: a commuting background, tree level, background Feynman gauge, quasi-coherent states as in (13), and the proposed criterion (16)/(17).
  - (b) and (c) G1–G4: four generators T = L·M^{ac₀} with exact Lie relations, an isotropic h₀-contracted mass, the tree-level EOM, and a simple real form.
  - (c), corrected per M2: no finite-N Hermitian solution has a Lorentzian kinetic tensor.
- **Not established:**
  - the criterion near m = 0;
  - the criterion for the transverse modes and the factor K, for the curved first-order members, or at one loop;
  - any selection of the real form, of W or of the background;
  - any derived signature or frame.
- **Labels.** E and D (D1) remain OPEN, CRITICAL PATH and PROGRAMME-CONDITIONAL. Nothing here is DERIVED for either target.
- **Relaxations that could still favour the IR or full-GR derivation, ranked:**
  1. A one-loop (IKKT-content) comparison of the so(4,2) and so(6) members at N→∞ and fixed γ > 0. This is the only relaxation here that could make the integral, rather than the author, select the real form.
  2. N→∞ first in Definition (A) at fixed γ > 0, and whether the conjugate background is a saddle of the regulated integral. This relaxes the order of limits used in 053–059.
  3. Curved first-order members, where Δ_T comes from curvature-induced noncommutativity (½𝖱𝒮). This relaxes H1.
  4. Approximate finite-N truncations of so(4,1) or so(4,2) that solve the EOM to controlled error. This relaxes the exact Lie relations of G1.
  5. A fluctuation estimate valid near the bounce, and in the base presentation's Euclidean domain.
  6. Anisotropic or non-Lie backgrounds (relaxing G2 or G4). The 1709 κ-route needs a supplied second mass.
  - The criterion (H5) is itself proposed, not derived. A different semi-classical criterion is a further, lower-ranked relaxation.

## Recommended disposition
Revise. Apply R1–R9 verbatim, regenerate the apply_check hashes for appH and the bib, and resubmit as r2. Integration requires a plain ACCEPT. bibtex must be run once at integration.

## Corrected snippet
None of these needs new physics or assumptions. All edits are to `appH_insert.tex` unless stated.

**R1 (major 1).** Make these substitutions:
- "the kinetic tensor is \(\gamma^{\mu\nu}=(h_0)_{ab}E^{a\mu}E^{b\nu}\)" → "the kinetic tensor is \(\mathsf K^{\mu\nu}=(h_0)_{ab}E^{a\mu}E^{b\nu}\), that of Definition~\ref{def:matrix-coords-ext} with \(h_0\) in place of \(\eta_{IJ}\)"
- "then \(\gamma\) is a Gram matrix" → "then \(\mathsf K\) is a Gram matrix"
- "four, \(\gamma\) has, by Sylvester's" → "four, \(\mathsf K\) has, by Sylvester's"
- "then \(\gamma=m^2\eta^{-1}H\eta^{-1}\)" → "then \(\mathsf K=m^2\eta^{-1}H\eta^{-1}\)"
- "and \(\gamma=0\) where \(m=0\)" → "and \(\mathsf K=0\) where \(m=0\)"
- "\(\rho^2=\rho_M|\det\gamma^{\mu\nu}|^{1/2}\)" → "\(\rho^2=\rho_M|\det\mathsf K^{\mu\nu}|^{1/2}\), with \(\mathsf K\) the tensor written \(\gamma^{\mu\nu}\) there,"

Every remaining γ is then the mass parameter.

**R2 (major 2).** Replace the last two sentences of the conjugate-coordinates paragraph, from "A representation of \(\mathfrak{so}(4,2)\) by Hermitian" to "exists only for \(N\to\infty\).", with:
"The \(T^a\) and their commutators span the subalgebra on the five indices \(a\) and \(c_0\), which is \(\mathfrak{so}(4,1)\) for the class above. A representation of a non-compact simple Lie algebra by Hermitian \(N\times N\) matrices is trivial, since its image would be a compact Lie algebra isomorphic to it, with negative definite Killing form, whereas the Killing form of a non-compact simple Lie algebra is indefinite; \(\mathfrak{so}(5)\subset\mathfrak{so}(6)\) has such representations. Within this family, a non-zero solution at finite \(N\) therefore has \(\eta\) definite on these five indices and a positive definite kinetic tensor, and the Lorentzian member exists only for \(N\to\infty\)."

**R3.** "\(m=M^{45}\) and \(\ell^2=-y_ay^a\)" → "\(m=M^{45}\) and \(y_\mu y^\mu=-\ell^2-m^2\)"

**R4.** Make two changes in the flat-point paragraph:
- Replace "The criterion therefore fails, as stated in~\cite{Steinacker2026Weak} for commutative backgrounds." with "The Euclidean criterion therefore fails, as stated in~\cite{Steinacker2026Weak} for commutative backgrounds; for \(\eta\) the window \(|t'-t|<\Delta_T\) then contains no \(t'\neq t\), and the states below give a ratio that grows like \(\sigma^{-2}\) as their width \(\sigma\to0\)."
- Replace ", so that \(\Delta_T=\sigma\)," with ", with its uncertainty \(\sigma\) in place of \(\Delta_T\), since no quasi-coherent state exists,"

**R5.** "; the weight \(w\) used for this class in Section~\ref{sec:status-D} supplies such a width and is not derived." → "; the weight \(w\) used for this class in Section~\ref{sec:status-D} is likewise a supplied momentum scale, and no width is derived."

**R6.** "the criterion as \(g_{\mathrm{YM}}/\sqrt2\) at late \(\tau\)" → "the criterion as of order \(g_{\mathrm{YM}}\) at late \(\tau\)"

**R7.** "the identity with \(c_0=5\) gives \(\gamma=-3c\)," → "the identity with \(c_0=5\) gives \(\gamma=-3c\), with \(c>0\) for \(h_0\) of signature \((9,1)\) as above,"

**R8.** "therefore do not apply to these backgrounds" → "therefore do not apply to the conjugate-coordinate backgrounds"

**R9.** In `bib_entries.bib`, entry Steinacker2026Weak, add the line `  note    = {Version 2; the equation numbers cited refer to it},` after the `year` line.

**Files referenced:**
- C:\Users\redgi\Projects\namcg-lab\proposals\060-semiclassical-signature-domains\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\proposals\060-semiclassical-signature-domains\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\proposals\060-semiclassical-signature-domains\bib_entries.bib
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (anchor L1588)
- Gatekeeper check: C:/Users/redgi/AppData/Local/Temp/claude/3ba14ee056ac155d/15e6827c-2d5a-4852-be36-98ee14883700/scratchpad/gk_lie.py

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/2
