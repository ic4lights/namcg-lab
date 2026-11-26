# Proposal 059-d1-lorentz-local-frame, round 1

Target: **D1.lorentz** (Problem D, local Lorentz invariance from Presentation A).
Problem D ledger status, `chapters/appH-microscopic-proofs.tex` L648-649 (VERBATIM):

> Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet.

Chapter 17 criterion, `chapters/ch17-agenda.tex` L329-361 (VERBATIM, the Problem D paragraph):

> \paragraph{Problem D: local Lorentz invariance from Presentation~A.}
> \emph{CRITICAL PATH; OPEN.} Generator counting is closed
> conditionally, while local Lorentz symmetry is imposed.
> Assumption~\ref{ass:local-lorentz} puts
> \(\mathrm{SO}(3,1)\) into Presentation~B by hand. Either derive a
> local Lorentz gauge symmetry from the matrix algebra and condensate
> (D1), or state that NAMCG is a theory of a condensate field on an
> auxiliary spacetime and stop calling Presentation~A ontologically
> prior (D2). D1 closure requires the \(\omega\), \(A_\mu\), \(B\), and
> ghost operators and the resulting field content to be specified.
> D1 closure also requires that the locked frame exist and be
> non-degenerate on the claimed domain, derived from the same
> microscopic data rather than taken from
> Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg}.
> Under D2, even with these operators specified, the result is only a
> scope-limited Presentation-B model: D remains OPEN and CRITICAL PATH,
> and a full matrix-derived spectrum is not established. [...]
> Problem~D is unresolved.

**Problem D stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. Nothing in this proposal changes any status label.**

## Result

Two labelled, scoped insertions into the Problem D ledger of Appendix H:

1. A **conditional sub-lemma**: the first-order equivariant class relations of Appendix H are *realizable at finite N by matrices* on a compact toy (unit S^2 base, circle structure group, Levi-Civita connection). The toy shows *why* the class has the form it has: the commutator of two first-order horizontal lifts is not first-order when the curvature is nonzero (vertical part −csc²θ·ξ ≠ 0), so the zeroth-order slot ½R^{cd}_{ab}𝒮_{cd} is forced, not optional; and the finite-N fuzzy-sphere (Berezin-Toeplitz-type) model reproduces, exactly at every N, the derivation part (Leibniz rule, rotation-algebra closure 𝓛_a = ħ_eff⁻¹ ad_{X_a}, action on coordinates), with the coefficient-function and frame-redundancy errors at O(ħ_eff) = O(1/N), and the ghost operator Σ ad²_{X_i}/ħ_eff² has the Laplace–Beltrami spectrum {l(l+1), mult 2l+1} of S² *exactly*, truncated only at l > N−1. This is the mechanism of Hattori–Seko–Tsuchiya (PTEP 2026 083B01) read on the class object of the section.
2. A **mechanism paragraph**: an Elitzur-compliant reading of the locked frame as a gauge-invariant bilocal composite (parallel-transported two-point object), replacing the gauge-variant expectation ⟨Φ⟩ = v𝕀 of eq:VEV as the order-parameter-like statement, with Assumption ass:nondeg re-read as non-degeneracy of the composite. Classified as mechanism/conjecture, not a derivation; it presupposes the connection content that D1 closure requires.

What is NOT claimed: closure of D or D1, derivation of local SO(3,1), the (7,3) kinetic signature, class selection by the matrix equation, existence/non-degeneracy of the locked frame from microscopic data, or any change of any status.

## Target and status

- Problem D: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL (quoted verbatim above). ch17 L329-361 agrees with the appH ledger; **no discrepancy found** between the two sources for Problem D.
- The target for this package is the structural understanding of the first-order equivariant class (the D1 route's presentation of local rotations as matrix gauge transformations) plus the Elitzur-consistency of the locking assumption. The class object, its relations, the local-rotation formula, the ghost operator and the flat-point spectrum counts are already in appH L1444-1528; this proposal adds the finite-N matrix realization sub-lemma and the composite reading, both explicitly scoped.
- DERIVED-or-PROGRAMME-CONDITIONAL: PROGRAMME-CONDITIONAL throughout. Item 1 is a derived conditional result about a toy, not about the NAMCG class itself.

## Source reading

digest + targeted reads (NOT a full scan; digest records 30 files, `dirty-chapters: yes`). Files read in full at the relevant ranges: `chapters/ch17-agenda.tex` L329-370; `chapters/appH-microscopic-proofs.tex` L644-1530 (Problem D ledger; class relations L1444-1460 re-quoted this round); `chapters/ch03-matrix-action.tex` L245-289 (eq:VEV, ass:frame-lock, eq:Phi-transform); `chapters/ch04-vierbein-emergence.tex` L150-194 (def:composite-metric, eq:g-from-e, ass:nondeg); `chapters/ch10-lorentz-locking.tex` L36-80 (ass:local-lorentz, eq:D-both); `scratch/digest.md`; `reports/sme-scout-20261108-0702.md`; `bib/namcg.bib` (key check: HoKawaiSteinacker2025 present; Elitzur1975 / FradkinShenker1979 / HattoriSekoTsuchiya2026 absent).

## Research and reasoning

### Conventions pinned
- Lie bracket [ , ] of vector fields; [V,W]f = V(Wf) − W(Vf). Scripts implement this.
- Class-relation conventions are the manuscript's (appH L1444-1446): [𝒮_cd,𝔻_a] = η_ad 𝔻_c − η_ac 𝔻_d; [𝔻_a,𝔻_b] = −𝖳_ab^c 𝔻_c + ½𝖗_ab^{cd}𝒮_cd + 𝖥_ab. Signs of 𝖳 follow [e_a,e_b] = −𝖳_ab^c e_c (appH: "the 𝖳 of the opposite sign" in [FurutaHanadaKawaiKimura2007] confirms the manuscript sign is the opposite of FHK).
- Structure group in the toy is U(1) (SO(2)); the Lorentz index structure is not retained; the claim is about the *form* of the class relations (first + zeroth order mixing) and finite-N realizability.
- Finite N: spin j = (N−1)/2; J_i the (2j+1)-dim irrep, [J_i,J_j] = iε_ijk J_k; X_i = J_i/√(j(j+1)) (radius 1); ħ_eff = 1/√(j(j+1)); 𝓛_a = ħ_eff⁻¹ ad_{X_a}.

### (A) Toy class data (exact, verified in `d1_toy_class_symbolic.py`)
S², coframe θ¹ = dθ, θ² = sinθ dφ; e₁ = ∂_θ, e₂ = (sinθ)⁻¹∂_φ.
- [e₁,e₂] = −cotθ e₂ ⇒ 𝖳₁₂² = cotθ.
- Levi-Civita: ω¹² = −cosθ dφ (torsion-free check: dθ²(e₁,e₂) − ω¹²([e₁,e₂])·(−1) form computed in script; numerically cotθ − cotθ = 0).
- Curvature: 𝖱₁₂¹² = e₁(ω₂) − e₂(ω₁) − ω¹²([e₁,e₂]) = 1 (unit sphere). The structure-equation term −ω¹²([e₁,e₂]) = −(−cotθ)(−cotθ)·... enters via the α([e₁,e₂]) term of dα(e₁,e₂) = e₁α₂ − e₂α₁ − α([e₁,e₂]); without it the check fails (this was a bug caught in round-0 development).
- Horizontal lifts 𝔻_a = e_a − ω_a ξ (ξ = ∂_u fibre field): the **full operator identity** [𝔻₁,𝔻₂] = −cotθ 𝔻₂ − ξ holds exactly. Key step: the vertical component is −(ω₂ e₁ω₂-coeff) chain = −cot²θ−1 = −csc²θ ξ; combined with the horizontal commutator −cotθ e₂ − csc²θ ξ and the −cotθ·(−ω₂ ξ) inside −cotθ 𝔻₂ = −cotθ e₂ + cotθ ω₂ ξ = −cotθ e₂ − cot²θ ξ, the residual is −csc²θ + cot²θ = −1, i.e. exactly −ξ. So
  **[𝔻₁,𝔻₂] = −𝖳₁₂²𝔻₂ − ξ = −𝖳₁₂²𝔻₂ + ½𝖗₁₂^{12}𝒮₁₂ (with 𝒮₁₂ ↦ −ξ under the U(1) fundamental field convention as implemented)**.
  The vertical part −csc²θ ξ of the commutator is nonzero: **two first-order operators do not close**, the zeroth-order slot is forced. This is the toy form of the Rennie–Varilly obstruction to inner first-order fluctuations; we state only the elementary computation, we do not import any RV theorem.
- Local rotation U(1) shadow: [λξ, 𝔻_a] = −(𝔻_a λ)ξ for generic λ(θ,φ) = cos²θ sinφ + θ sinθ cosφ. This matches the manuscript's [½λ^{cd}𝒮_cd, 𝔻_a] = λ^c_a 𝔻_c − ½(𝔻_a λ^{cd})𝒮_cd (appH L1452) with the 𝔻-rotation slot zero in the Abelian case.
- Frame fields: the SO(3) fundamental fields ρ_i = −ε_ijk x_j ∂_k on S² satisfy [ρ_i,ρ_j] = −ε_ijk ρ_k and Σx_iρ_i = 0 exactly; L_± = ρ₁ ± iρ₂ give [L₊,L₋] = +2iL₃ (constant structure coefficients; sign established by the computation).

### (B) Finite-N matrix realization (verified in `d1_finiteN_class.py`)
- Leibniz rule of 𝓛_a: inner derivations; numerically exact (‖·‖ ≤ 2e-12 over N ≤ 31).
- Closure [𝓛_i,𝓛_j] = iε_ijk 𝓛_k exactly: this is the Jacobi identity [ad_A,ad_B] = ad_{[A,B]} together with [X_i,X_j] = iħ_eff ε_ijk X_k; the ħ_eff factors cancel identically. So the **rotation-algebra action part of the class relations is exact at every finite N** (no asymptotics needed).
- Action on coordinates 𝓛_i(X_j) = iε_ijk X_k exact (machine precision).
- Coefficient-function error: Moyal-vs-Poisson relative error on polynomial symbols (P = x₁²x₂, Q = x₃ with {x_i,x_j} = ε_ijk x_k) decays with log-log slope −1.065 ± in N ⇒ error ~ ħ_eff (0.314 at N=5 to 0.044 at N=31).
- Frame redundancy ΣX_i 𝓛_i violates the classical Σx_iρ_i = 0 at relative size with slope −1.010 ⇒ O(ħ_eff).
- Ghost: G = Σ ad²_{X_i}. End(C^N) = ⊕_{ℓ=0}^{2j} V_ℓ under the adjoint SO(3); the superoperator Casimir identity Σ(J⊗1 − 1⊗Jᵀ)² = 2j(j+1) − 2ΣJ⊗Jᵀ gives G|_{V_ℓ} = +ℓ(ℓ+1)/(j(j+1)) = +ℓ(ℓ+1)ħ_eff²; full eigvalsh multiset match to {+ℓ(ℓ+1)ħ_eff² × (2ℓ+1)} with max deviation ≤ 6e-12 for N ≤ 31. Hence **G/ħ_eff² has the sphere Laplace–Beltrami spectrum exactly, truncated only at ℓ > N−1** (the matrix algebra has no V_ℓ for ℓ > 2j = N−1). Convention note: G = Σ ad² is positive semidefinite here; the LB sign convention is absorbed in the displayed formula.
- Round-0 development errors caught and fixed (for gatekeeper transparency): spin-raising matrix element must be √(j(j+1) − m(m+1)); superoperators must use the row-major vec convention of numpy reshape (vec(Af) = (A⊗I)vec f); errors scale as ħ_eff ~ 1/N so log-log slope in N is −1. All final outputs are in the saved `.out` files.

### (C) Literature (verified personally)
- Hattori–Seko–Tsuchiya, "Description of curved spacetimes by finite-size matrices in the type IIB matrix model", arXiv 2606.24577 [hep-th], PTEP (2026) 083B01, DOI 10.1093/ptep/ptag120. Re-verified this round by fetching the arXiv abs page (title/authors/journal ref/DOI confirmed). What it supports: finite-N Berezin-Toeplitz regularization of curved-geometry matrix configurations (fuzzy tori and spheres) with covariant-derivative interpretation. What it does NOT support: SO(3,1) fibre, class selection by the matrix equation, Einstein dynamics (HKK-type higher-derivative caveat already in appH L1460+).
- Elitzur, Phys. Rev. D 12, 3978-3982 (1975), DOI 10.1103/PhysRevD.12.3978 ("Impossibility of spontaneously breaking local symmetries"). Verified pre-round; record confirmed to exist with that title/scope. Classified: established theorem, cited as motivation only; its hypotheses (lattice, compact gauge group, local gauge variant) are matched to the *assumption structure*, not asserted for the NAMCG continuum measure.
- Fradkin–Shenker, Phys. Rev. D 19, 3682-3697 (1979), DOI 10.1103/PhysRevD.19.3682. Verified pre-round. Used only for "no local order parameter; analytic complementarity" and to ban "breaking" language.
- Ho–Kawai–Steinacker 2509.06646 is already in the bib (`HoKawaiSteinacker2025`, cited in appH's Sources paragraph) and is cited for the bilocal-field spirit only.
- Manta–Steinacker (2411.02598, 2502.02498) were listed in the scout as an A_μ-as-matrix-operators recipe; **not imported and not cited** in this package (their precise content was not re-verified to the level required; see ranked avenues).

### (D) Comparison with the original target
The D1 target (ch17 quoted above) requires deriving local Lorentz symmetry, the ω/A/B/ghost operators' field content, and the locked frame's existence and non-degeneracy from microscopic data. This package derives none of these for NAMCG. It (i) establishes a toy sub-lemma that the class relations' mixed first+zeroth order structure is exactly what curvature forces and is finitely realizable with quantified O(1/N) errors — a consistency and *form-explanation* result for the class presentation that D1 uses; and (ii) records an Elitzur-compatible replacement for the locking assumption's order-parameter reading, as a conjecture. The gap named by ch17 (derivation from the same microscopic data) is unchanged.

## Claim classification

- Toy identity [𝔻₁,𝔻₂] = −cotθ 𝔻₂ − ξ, 𝖳₁₂² = cotθ, 𝖱₁₂¹² = 1, torsion-free check: **established derivation** (exact symbolic, script 1).
- [λξ,𝔻_a] = −(𝔻_a λ)ξ on the toy: **established derivation** (script 1).
- Non-closure of first-order operators at nonzero curvature (vertical part −csc²θ ξ ≠ 0): **established derivation** on the toy; **unresolved** as a claim that SO(3,1) class operators of NAMCG need exactly the manuscript slot content (the manuscript assumes the class form; the toy explains its necessity in one example).
- Finite-N exactness of Leibniz/closure/coordinate action: **established derivation** (Jacobi identity) + numeric check (script 2).
- O(ħ_eff) Moyal and redundancy errors: **conditional result** (measured slope ≈ −1 on two symbol choices; general BT calculus not proved).
- Ghost spectrum = {+ℓ(ℓ+1)} exact with mult 2ℓ+1, truncated at ℓ = N−1: **established derivation** (Casimir on End = ⊕V_ℓ) + numeric multiset match.
- Applicability of this finite-N picture to the NAMCG SO(3,1) class (noncompact fibre): **conjecture/mechanism**; no theorem transfers the compact fuzzy construction to the Lorentz-fibre class.
- Locked frame as gauge-invariant bilocal composite; ass:nondeg as composite non-degeneracy; complementarity reading of locking: **conjecture/mechanism** (explicitly labelled so in the LaTeX).
- Elitzur/Fradkin-Shenker applicability to NAMCG's measure: **conditional** — theorems are lattice results; used to constrain the *form* of any order-parameter statement, not to prove the lattice theory is NAMCG.

## Proposed changes

One file: `chapters/appH-microscopic-proofs.tex`. Insert the two-paragraph block **immediately after** the last line of the Problem D ledger and before `\section{Problem E: signature}`. No existing text is removed or replaced; everything currently in L1444-1528 and the Problem E section stays.

**Anchor (VERBATIM, occurs exactly once — verified count = 1 in current bytes):**
`Problems~D, E, F and~N remain open and PROGRAMME-CONDITIONAL.`
Byte offsets computed from the CURRENT file bytes (appH size 550641, CRLF file): anchor first byte at offset **239000**; its line's CRLF begins at offset **239061** (so the anchor line ends at 239063 exclusive); the following blank line is the CRLF pair at 239063-239064; `\section{Problem E: signature}` begins at offset **239065**.

**Insertion:** insert at offset 239065 the block below (as CRLF text) followed by a CRLF CRLF blank line, before `\section{Problem E: signature}`. Expected post-apply size: 550641 + 4417 (block, CRLF) + 2 (separating blank line) = **555060 bytes**. The block is stored verbatim at `proposals/059-d1-lorentz-local-frame/insertion-block.tex` (LF, 4412 bytes; CRLF form 4417 bytes) so the gatekeeper can byte-compare.

```latex
\paragraph{A finite-\(N\) matrix toy for the class relations.}
On the model space of the class above, take the base to be the unit two-sphere with coframe \(\theta^1=\mathrm d\theta\), \(\theta^2=\sin\theta\,\mathrm d\varphi\), orthonormal frame \(e_1=\partial_\theta\), \(e_2=(\sin\theta)^{-1}\partial_\varphi\), and the circle group as structure group, with the Levi-Civita connection \(\omega^{12}=-\cos\theta\,\mathrm d\varphi\). The class data of this connection are \(\mathsf T_{12}{}^2=\cot\theta\), from \([e_1,e_2]=-\cot\theta\,e_2\), and \(\mathsf R_{12}{}^{12}=1\), with \(\mathsf F=0\). With \(\xi\) the fundamental vertical field, the horizontal lifts \(\mathbb D_a=e_a-\omega_a\xi\) satisfy exactly \([\mathbb D_1,\mathbb D_2]=-\cot\theta\,\mathbb D_2-\xi\) and \([\lambda\xi,\mathbb D_a]=-(\mathbb D_a\lambda)\xi\) for every real \(\lambda\) on the base: the vertical part of \([\mathbb D_1,\mathbb D_2]\) alone is \(-\csc^2\theta\,\xi\neq0\), so the commutator of two first-order operators is not itself first-order when the curvature is nonzero, and the zeroth-order slot \(\tfrac12\mathsf R_{ab}{}^{cd}\mathcal S_{cd}\) of the class relation is not optional. At finite \(N\) the derivation part of the same structure is carried by matrices: with spin-\(j\) generators \(J_i\), \(N=2j+1\), radius-one coordinates \(X_i=J_i/\sqrt{j(j+1)}\), so that \([X_i,X_j]=\mathrm i\hbar_{\mathrm{eff}}\varepsilon_{ijk}X_k\) with \(\hbar_{\mathrm{eff}}=1/\sqrt{j(j+1)}\), the inner derivations \(\mathcal L_a=\hbar_{\mathrm{eff}}^{-1}\operatorname{ad}_{X_a}\) obey the Leibniz rule and close the rotation algebra exactly, \([\mathcal L_i,\mathcal L_j]=\mathrm i\varepsilon_{ijk}\mathcal L_k\) and \(\mathcal L_i(X_j)=\mathrm i\varepsilon_{ijk}X_k\), for every \(N\); moving coefficient functions across the noncommutative product errs from the Poisson bracket at order \(O(\hbar_{\mathrm{eff}})\), and the frame redundancy \(\sum_i x_i\rho_i=0\) of the sphere frame is violated at the same order. The ghost operator \(\sum_i\operatorname{ad}_{X_i}^2/\hbar_{\mathrm{eff}}^2\) has, on \(\operatorname{End}(\mathbb C^N)\), the spectrum \(\{l(l+1):0\le l\le N-1\}\) with multiplicity \(2l+1\) exactly, so it reproduces the Laplace--Beltrami spectrum of the sphere up to the removal of the modes \(l>N-1\). This is the finite-size regularization of curved-geometry matrix configurations of \cite{HattoriSekoTsuchiya2026}, read on the class of this section. The toy is compact in base and fibre, Abelian in fibre, torsion-free and two-dimensional: it retains neither \(\mathrm{SO}(3,1)\) nor the noncompact fibre nor the \((7,3)\) kinetic signature nor the selection of the class by the matrix equation, and it discharges neither Assumption~\ref{ass:frame-lock} nor Assumption~\ref{ass:nondeg} nor Assumption~\ref{ass:local-lorentz}. Against the criterion of Chapter~17 this is a conditional sub-lemma on a compact toy, and the status recorded for Problem~D above is unchanged.

\paragraph{The locked frame as a gauge-invariant composite.}
Elitzur's theorem \cite{Elitzur1975} rules out a nonzero expectation value of a gauge-variant local field for a compact structure group, and Fradkin and Shenker \cite{FradkinShenker1979} showed that the Higgs and confinement regimes of such theories are analytically connected without any local order parameter. The expectation value of Equation~\eqref{eq:VEV} is gauge-covariant under Equation~\eqref{eq:Phi-transform}, so on a gauge-invariant presentation the locking of Assumption~\ref{ass:frame-lock} is not the statement that it is nonzero: the locked frame is instead represented by composites that are bilocal in the base, in the spirit of the bilocal fields of \cite{HoKawaiSteinacker2025}, with parallel transporters built from the connection of the class above relating the two points, and the composite metric of Equation~\eqref{eq:g-from-e} is invariant under tangent-space rotations. On this reading Assumption~\ref{ass:nondeg} becomes a non-degeneracy statement about the two-point composite rather than a consequence of a broken symmetry, and the locking is a complementarity of regimes, not a breaking. The construction presupposes the connection content that the closure of Problem~D1 in Chapter~17 requires to be specified, and is recorded as a mechanism whose selection by the matrix dynamics is open; the status recorded for Problem~D above is unchanged.
```

Labels referenced and verified (exactly one `\label` each, no duplicates, digest confirms none): `ass:frame-lock`, `ass:nondeg`, `ass:local-lorentz`, `eq:VEV`, `eq:Phi-transform`, `eq:g-from-e`. No new labels are added. (No new `\label` at all in the block.)

New citations (bib keys verified absent today): `HattoriSekoTsuchiya2026`, `Elitzur1975`, `FradkinShenker1979`. Full BibTeX for the integrator (records verified as in section (C)):

```bibtex
@article{HattoriSekoTsuchiya2026,
  author  = {Hattori, Keiichiro and Seko, Tatsuya and Tsuchiya, Asato},
  title   = {Description of curved spacetimes by finite-size matrices in the type {IIB} matrix model},
  journal = {Prog. Theor. Exp. Phys.},
  year    = {2026},
  pages   = {083B01},
  doi     = {10.1093/ptep/ptag120},
  eprint  = {2606.24577},
  archivePrefix = {arXiv}
}
@article{Elitzur1975,
  author  = {Elitzur, Shmuel},
  title   = {Impossibility of spontaneously breaking local symmetries},
  journal = {Phys. Rev. D},
  volume  = {12},
  pages   = {3978--3982},
  year    = {1975},
  doi     = {10.1103/PhysRevD.12.3978}
}
@article{FradkinShenker1979,
  author  = {Fradkin, Eduardo and Shenker, Stephen H.},
  title   = {Phase diagrams of lattice gauge theories with Higgs fields},
  journal = {Phys. Rev. D},
  volume  = {19},
  pages   = {3682--3697},
  year    = {1979},
  doi     = {10.1103/PhysRevD.19.3682}
}
```

Stale passages elsewhere: none identified. ch10/ch03/ch04 wording on the VEV is not contradicted (the block states a reading, not a rewrite); if the author later wants ch10 to reference the composite reading, that is a separate item.

## Verification scripts

- `proposals/059-d1-lorentz-local-frame/d1_toy_class_symbolic.py` (sympy exact arithmetic) → saved output `d1_toy_class_symbolic.out`: sections 1-4 above; **ALL PASS** (13 checks).
- `proposals/059-d1-lorentz-local-frame/d1_finiteN_class.py` (numpy float64) → saved output `d1_finiteN_class.out`: checks 1-5 above over N = 5..31; **ALL PASS** (exactness at machine precision; slopes −1.065, −1.010; ghost multiset match ≤ 6e-12).
- Run with `python -I <script>` from the folder; outputs are byte-reproducible (fixed rng seeds).
- `insertion-block.tex`: the exact LaTeX block (LF form, 4412 bytes).

## Decisions Taken

- Chose the scout's Arm-1 (finite-N class-relation sub-lemma on a compact toy) as the package core and Arm-2 (Elitzur-compliant composite, as a labelled mechanism) as the paired consistency paragraph. Rejected alternatives: importing HST's or Manta-Steinacker's results as evidence about NAMCG without derivation (violates evidentiary rules); a spectral-triple/fluctuation reconstruction (postulates the continuum geometry — excluded by the emergence guardrail); Arm-3's local-λ bootstrap against TT/torsion counting (could not be derived to standard within this package; recorded as open instead of sketched).
- Kept the class relation's manuscript sign conventions verbatim; the toy realizes them, so no convention drift was introduced.
- Kept "supposes/recorded as mechanism" wording rather than strengthening the composite paragraph into a derivation, since no matrix computation supports it yet.

## Milestone assessment

Routine. The finite-N sub-lemma is a conditional toy result and a consistency/form-explanation step; it closes no critical-path target and discharges no assumption. No MILESTONE.md trigger is believed to apply.

## Status-label recommendation

Re-derived current critical-path set from ch17 (this session: Problem D paragraph read; digest ledger snapshot): A, B, C, D1, E, F, G-derived, N. **All affected labels unchanged: Problem D remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.** No label change proposed.

## Author decision needed

None.

## Remaining open step

To close D1 as ch17 states it: derive local SO(3,1) gauge symmetry, the ω/A/B/ghost field content, and existence + non-degeneracy of the locked frame from the matrix algebra and condensate. Concretely still needed after this package:
1. Extend the class-relation realization to the noncompact SO(3,1) fibre (fuzzy noncompact cosets or Lorentz-fibre matrix truncation) — the main technical barrier.
2. Class selection: show which class the matrix dynamics favors (HKK heat-kernel attractors give 𝖱² terms, not Einstein; appH already records this).
3. Non-degeneracy of the composite locked frame (the bilocal reading is a conjecture; a spectral/positivity criterion is missing).
4. The (7,3) kinetic-signature and ghost-sector questions (unchanged; appH internal obstructions stand).
5. Manta-Steinacker A_μ-as-matrix-operators recipe as a candidate for the order-zero content (not imported here).
6. Arm-3: the local-λ(𝔁) bootstrap vs TT/torsion mode counting, as a consistency test of the class's gauge-parameter count.

Ranked avenues for the next package: (1) noncompact-fibre class realization attempt (highest value, hardest); (2) composite-frame non-degeneracy criterion (Elitzur-safe, mid difficulty); (3) Manta-Steinacker A_μ recipe verification against the 22-label count at appH L1486; (4) Arm-3 bootstrap.

## Special instructions for the gatekeeper

- Verify the identity [𝔻₁,𝔻₂] = −cotθ 𝔻₂ − ξ by hand (the −cot²θ − 1 = −csc²θ step), and re-run both scripts (`python -I`), byte-comparing the `.out` files and the block against `insertion-block.tex`.
- Must NOT be asserted: closure or narrowing of D/D1; that the toy discharges ass:frame-lock / ass:nondeg / ass:local-lorentz / ass:lorentzian; that any literature result transfers to NAMCG; that the composite paragraph derives anything; the word "breaking" for the locking.
- Check that the block adds no `\label` and that each `\ref`/`\eqref` target exists exactly once (listed above; digest confirms no duplicate labels).
- Anchor must occur exactly once before integration; block inserted with CRLF at offset 239065; expected appH size after: 555060 bytes.
- Report (do not fix): no ch17-vs-appH discrepancy found for Problem D this round.
