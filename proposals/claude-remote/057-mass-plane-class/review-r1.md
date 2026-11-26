VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/0

## Verdict
I re-derived the core mathematics of 057 and it holds: the plane-class invariant, its conservation, the endpoint classes, the isotropic-P extension and the ε→0 rank-one/non-integrability statement. Four minor wording and scope corrections are still required. The main one is that one sentence of (iii) claims more than is proved when γ_j is unbounded. Because of that, this is not yet a plain ACCEPT.

## Source reading
- **Mode:** digest + targeted reads. **No full scan was done.** Following the orchestrator's ruling, the CLAUDE.md 3(a) full scan for ordinal 55 is to be run separately, in split passes, before any plain ACCEPT is integrated.
- **Digest status:**
  - `make_digest.py --check` printed DIGEST CURRENT.
  - `dirty-chapters: yes`. `git status` and `git diff --stat` show only `chapters/appH-microscopic-proofs.tex` modified: one hunk, +35 lines at L1529, which is the 055+056 blocks.
  - The working appH is 561466 bytes, sha256 ea5c753b…a1f5, which matches the stated baseline.
- **Read in full:**
  - appH `sec:status-E`, L1482–1566: ledger label, 053 (including the "admissible u closes like ε/γ" sentence at L1506), 054, 055 (L1529–1549), 056 (L1551–1562), and the Status anchor L1564–1565.
  - ch17 L394–399 and L712–725.
  - ch04 L318–327 (`ass:lorentzian`).
  - The `reports/ledger.md` tail for 055–056, and MILESTONE.md.
  - Unreadable files: none.

## Claim under review
- **Claims:** for Definition (A) with the mass term, γ>0, linear colour-blind contours A=ΛX, and paths with Λ(0) real, Re M_γ>0 and Re iS_b≤0 throughout:
  - (i) the plane-class dichotomy;
  - (ii) the class is conserved, the Hermitian contour is upper and every admissible −𝔆₀ contour is lower, so none is reached at any N. This includes 056's e^{iπ/8}/e^{−3πi/8} contour and isotropic P. For γ≤0 the lower set is empty;
  - (iii) as ε→0 with γ/ε→∞ and convergent end points, Im h_∞=−κvvᵀ; S_b and the mass term are real on v·X=0; at N=2 the ε=0 integrand on Λ_∞ is not absolutely integrable.
- **Original target:** derive Lorentzian signature rather than retain `ass:lorentzian`.
- **Appendix H, verbatim:** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
- **ch17, verbatim:** "OPEN; CRITICAL PATH for the matrix-derived label." The full-GR criterion item reads "Problem~E: Lorentzian signature is derived rather than retained (Assumption~\ref{ass:lorentzian})".
- The two sources are consistent. The current critical-path set is A, B, C, D1, E, F, G-derived and N.

## Checks performed

**Direct re-derivations**
- **Identity.** η=1−2e₀e₀ᵀ gives h=ΛᵀΛ−2ℓℓᵀ, so (ε+iγ')h=M_γ−2εℓℓᵀ.
  - For real x with aᵀx=bᵀx=0, ℓᵀx=0 and xᵀ(Re h_φ)x = Re(xᵀM_γx)/|ε+iγ'| > 0.
  - That subspace has codimension ≤2, so n₊(Re h_φ)≥8 by Sylvester. Verified.
- **Branch and dichotomy.**
  - With r>0, det(r+is)=det r·Π(1+iσ_j). The σ_j are real because r⁻¹s is similar to r^{−1/2}sr^{−1/2}.
  - A change of basis conjugates r⁻¹s and multiplies det by det(B)²>0, so Θ is well defined on planes.
  - At N=2 the damping condition is equivalent to Im det(h|_E)≥0 for all real planes: take x³=0 for one direction; summing the pair terms gives the other. For N≥3, embedding the upper-left 2×2 block gives the same traces.
  - det(h|_E)=e^{−2iφ}det(h_φ|_E) gives sin(Θ−2φ)≥0. Since Θ−2φ∈(−π−2φ, π−2φ)⊂(−2π,π), Θ∈[2φ,π)∪(−π,2φ−π]. The gap (2φ−π,2φ) has length π, and both sets are relatively closed in (−π,π). Verified.
- **Connectedness.**
  - For R|_E>0, E∩V_≤=0.
  - x↦x₊+t x_≤ is injective on E, and R(x₊+t x_≤)=R(x₊)+t²R(x_≤)≥R(x)>0 by R-orthogonality of the eigenspaces and R(x_≤)≤0.
  - Gr(2,V₊) is connected for dim V₊≥2.
  - Θ is continuous with values in two disjoint closed sets, so it is constant at each τ.
  - A positive plane stays positive for nearby τ, so the class is locally constant and therefore constant on [0,1]. φ is fixed along the path. Verified. Only continuity of the path is needed.
- **Endpoints.**
  - τ=0: Θ=2 arctan(tan φ)=2φ, upper.
  - −𝔆₀: 055 (ii) gives ≥8 β_μ∈(0,π/2). Sylvester gives ≥8 μ with cos(β_μ+φ)<0, so ≥6 indices satisfy both, and for those β_μ+φ∈(π/2,π).
  - On span(T⁻¹e_μ, T⁻¹e_ν), h_φ=diag(|d|e^{i(β+φ−π)}), with θ∈(−π/2,0). So Θ=β_μ+β_ν+2φ−2π, which is < 2φ−π because β_μ+β_ν<π. Lower. Verified.
  - 056 example: h_*=−e^{iπ/4}𝟙, and the minimum eigenvalue of Re M_γ is (γ'−ε)/√2. I computed the diagonal entries (ε+γ')/√2 and (γ'−ε)/√2. Θ=2φ−3π/2, and it lies in the lower set iff φ>π/4. Verified.
- **γ≤0.** φ∈[−π/2,0] gives 2φ−π≤−π, so the lower set is empty. Consistent with 056 (i).
- **Isotropic P.**
  - In a basis with P=1 and η diagonal, P⁻¹η has inertia (1,9). So the nine-fold eigenvalue 1/c has c>0 and P−cη=κwwᵀ with κ=1−cη₀>0.
  - (εc+iγ')h=M_γ^P−εκ(Λᵀw)(Λᵀw)ᵀ, and Steps (i)–(ii) go through with φ=arg(εc+iγ'). Verified.
- **(iii) limit.**
  - Re M/|ε+iγ'| = cos φ·Re ΛᵀΛ − sin φ·Im h → −Im h_∞, which is ≥0.
  - Suppose n₊(−Im h_∞)≥2. A plane positive for −Im h_∞=lim Re h_{φ_j} is positive for large j and upper, so Θ_j≥2φ_j→π. But Θ_j→Θ_∞∈(−π,π) by joint continuity. Contradiction. So Im h_∞=−κvvᵀ.
  - Every imaginary term of S_b and of the mass term carries v·X, which gives reality on v·X=0 at every N.
- **N=2 non-integrability.**
  - h_∞|_{v⊥} is real of rank ≥8 (restriction of a nondegenerate form to codimension one), so det 𝒢 is a nonzero real sextic in x_V and |det 𝒢|≥c'R⁶ on a cone.
  - Im S_b=O(R²|y|²).
  - The real part of the mass exponent is −γ'κ|y|²/2, bounded for |y|≤R⁻³ and for any real γ.
  - The change in det 𝒢 is O(R⁵·R⁻³)=O(R²).
  - |Pf|=|c_P||det 𝒢|⁴≥cR²⁴.
  - ∫R²⁶·R²⁴·R⁻⁹dR=∞. Verified.
- **Convergence hypotheses.** They are stated in (iii): γ_j/ε_j→∞, end points of admissible paths, Λ_j→Λ_∞ invertible. See F1 for the unbounded-γ case.

**Scripts**
- I re-ran `apply_check.py` in report mode, without an output path, so it wrote nothing. Results:
  - baseline 561466 bytes, ea5c753b…a1f5, matches;
  - anchor 61 bytes, a7c77412…26cc, occurs once, at L1564;
  - insert LF form 7714 bytes, f7fbbade…af82; CRLF form 7724 bytes, aa8fa08b…62a3;
  - result 569192 bytes, e97ec830…c07f0, CRLF 3266, bare LF 0;
  - all of these match the proposal.
- I wrote my own check at `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk057\gk.py`. It covers:
  - identity residual ≈1e−15;
  - Θ agrees with arg det mod 2π on 551 random positive planes, with 0 mismatches;
  - the −𝔆₀ lemma, with the exact Θ formula and the lower class, on 506/506 random admissible-necessary samples with real congruence;
  - the 056 example (min Re M_γ and Θ=2φ−3π/2 exact);
  - isotropic P=2LᵀL: P⁻¹η has eigenvalues (−0.5, 0.5×9) and P−cη has rank 1.
- Numerical output checks these statements; it does not prove them.
- I read `plane_class_checks.txt` and `limit_checks.txt` and did not re-run them. Their content agrees with my derivations above.

**LaTeX and wording**
- The only ref is `\ref{ass:lorentzian}`, defined once, in ch04. No new labels, no citations, and no Anagnostopoulos2026.
- No process language.
- Internal references resolve: "two preceding paragraphs" (055, 056), "(i) of the preceding paragraph" (056 φ, the example), "(ii) of the paragraph on linear contours that mix the indices" (055).
- The 053 citation "closing … like ε/γ" faithfully reflects L1506.
- No label change.

**Not verified**
- The researcher's scratch build (365 pages, 0 undefined) was not re-run. The integrator's `build_check.py` must confirm it.

## Findings

- **F1. Severity: minor (required).**
  - **Location:** insert (iii), the final sentence "So for fixed γ>0, and for γ/ε→∞, …", and "At N=2 this integrand of I[1] on the contour Λ_∞ …".
  - **Finding:** the hypotheses of (iii) allow γ_j→∞. Then the "ε=0 integrand on Λ_∞" has no defined mass. The failure of domination is inferred from non-integrability of a limit integrand, and that needs γ_j to converge to a finite limit. With γ_j→∞ the pointwise limit of the moduli is supported on y=0 only, so Fatou gives nothing.
  - **Reason:** the claim exceeds the proof in that regime. The step "a dominating function would dominate the limit integrand" is also left implicit.
  - **Required action:** restrict the conclusion to γ_j converging to a finite limit, and state the domination step. The rank-one statement and the reality statement need no change. Replacement text is below.

- **F2. Severity: minor (required).**
  - **Location:** (ii), "For γ≤0 the lower class is empty, and the inertia argument there applies instead."
  - **Finding:** "there" is ambiguous. The classes were defined only for 0<φ<π/2, under "let γ>0".
  - **Required action:** replacement text is below.

- **F3. Severity: minor (required).**
  - **Location:** the closing sentence.
  - **Finding:** "…so no signature is selected and Assumption~\ref{ass:lorentzian} is still required." repeats verbatim the final clause of 056's closing ("…so Assumption~\ref{ass:lorentzian} is still required."). The two paragraphs are consecutive, and the Status line follows directly. This is the same kind of repeated-closing issue as 056 r1 F5.
  - **Required action:** replacement text is below.

- **F4. Severity: minor (bookkeeping, required).**
  - **Finding:** after F1–F3 the insert hashes and the resulting appH hash change.
  - **Required action:** re-run `apply_check.py` and the scratch build, and report the new hashes and page count.

No blocking or major findings. No PRIOR-CLAIM-ERROR: 053's "nothing is stated" and 056's "no statement about fixed γ>0" remain true as scope statements of those paragraphs.

## Scope of what is established

**Proved (established, algebraic, every N)**
- For linear colour-blind contours, Definition (A) with the mass term (or isotropic P), fixed ε>0 and γ>0, and paths with Λ(0) real, Re M_γ>0 and Re iS_b≤0 throughout:
  - the plane class is an invariant;
  - the Hermitian contour is upper and every admissible −𝔆₀ contour is lower, so no such path joins them. This includes 056's example for every γ'>ε.
- So 056's avenue 1 is closed within this class.

**Proved with stated hypotheses**
- Im h_∞=−κvvᵀ for convergent end-point families with γ/ε→∞, at every N.
- At N=2, the ε=0 integrand on Λ_∞ is not absolutely integrable, for any real γ. So dominated convergence along such families is unavailable for γ_j converging to a finite limit (after F1).

**Not established / unresolved**
- Whether lim_{ε→0} I_{ε,γ} exists at fixed γ>0, and whether it is Euclidean.
- No signature is derived. The classes are those of the η put into S_b and the regulator, and `ass:lorentzian` is retained.

**Classification:** PROGRAMME-CONDITIONAL. Problem E stays OPEN, CRITICAL PATH for the matrix-derived label, PROGRAMME-CONDITIONAL. No label change.

**Hypothesis class of the no-go:** H1 linear colour-blind contours; H2 Re M_γ>0 along the path; H3 Definition (A) or isotropic P; H4 convergent end-point families (for (iii)); H5 dominated convergence; fixed N; γ a supplied deformation.

**Relaxations that could still favour the infrared / full-GR derivation, ranked:**
1. Direct oscillatory or conditionally convergent analysis of lim_{ε→0} I_{ε,γ} at N=2, fixed γ>0 (relaxes H5). This is the only finite-N route this package leaves open for fixed γ>0, so I rank it first, ahead of the researcher's ordering.
2. Lefschetz-thimble (non-linear) contours at fixed ε, γ>0 (relaxes H1). The linear plane class does not constrain them.
3. Colour-mixing linear maps (relaxes H1).
4. Anisotropic P of low rank (relaxes H3; the 8-dimensional bound degrades as n−2·rank).
5. Divergent or degenerate end-point families, possibly reduced by real-congruence normalisation (relaxes H4).
6. Positive semidefinite boundary passages (relaxes H2; at N=2 this is restricted by 056 (ii)).
7. N→∞ first; Definitions (B) and (C).

**Milestone:** M2 (a new bounded no-go closing a class the manuscript kept open: "about fixed γ>0" in 056). It does not stop the loop and is not a breakthrough.

## Recommended disposition
Revise: apply the three replacements below verbatim, then recompute the hashes and the build. After that the package is ready for a plain ACCEPT, subject to the separate ordinal-55 full scan before integration.

## Corrected snippet
No new physics; one added hypothesis (γ_j converges to a finite limit), stated explicitly in R2.

**R1 (F2).** Replace
`For \(\gamma\le0\) the lower class is empty, and the inertia argument there applies instead.`
with
`For \(\gamma\le0\), where \(-\pi/2\le\varphi\le0\), the interval \((-\pi,2\varphi-\pi]\) is empty, and the inertia argument of (i) of the preceding paragraph applies instead.`

**R2 (F1).** Replace
`At \(N=2\) this integrand of \(I[1]\) on the contour \(\Lambda_\infty\) is not absolutely integrable.`
with
`At \(N=2\) this integrand of \(I[1]\) on the contour \(\Lambda_\infty\), with any real \(\gamma\) in the mass term, is not absolutely integrable.`

and replace
`So for fixed \(\gamma>0\), and for \(\gamma/\epsilon\to\infty\), no linear contour reached from the Hermitian contour in this way, fixed or convergent as \(\epsilon\to0\), carries the dominated convergence used above for \(\gamma\le0\), in line with the closing of the admissible \(u\) on \(\mathcal R_u\) like \(\epsilon/\gamma\).`
with
`So for fixed \(\gamma>0\), and for \(\gamma/\epsilon\to\infty\) with \(\gamma\) converging to a finite limit, no linear contour reached from the Hermitian contour in this way, fixed or convergent as \(\epsilon\to0\), carries the dominated convergence used above for \(\gamma\le0\), since a dominating function would also dominate the integrand at \(\epsilon=0\) on \(\Lambda_\infty\) with that limit of \(\gamma\); this is in line with the closing of the admissible \(u\) on \(\mathcal R_u\) like \(\epsilon/\gamma\).`

**R3 (F3).** Replace
`The two classes are fixed by the \(\eta\) in \(S_{\mathrm b}\) and by the regulator, so no signature is selected and Assumption~\ref{ass:lorentzian} is still required.`
with
`The two classes are fixed by the \(\eta\) in \(S_{\mathrm b}\) and by the regulator, so they select no signature, and the positive mass does not discharge Assumption~\ref{ass:lorentzian}.`

**Relevant files**
- `C:\Users\redgi\Projects\namcg-lab\proposals\057-mass-plane-class\proposal-r1.md`
- `C:\Users\redgi\Projects\namcg-lab\proposals\057-mass-plane-class\appH_insert.tex`
- `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex` (L1495–1565)
- `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk057\gk.py`

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/0
