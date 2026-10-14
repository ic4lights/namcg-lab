# Proposal 003-auto-target, round 1

Working title: *Which metric the condensate heat kernel induces: a scaffold no-go for the induced Einstein–Hilbert and Fierz–Pauli structures of the composite metric (Problem F, with consequences for C, B, D1).*

## Result

For the displayed Presentation-B action `eq:Smicro` + `eq:V` on the fixed scaffold `g^(0)` (Assumption `ass:aux-metric`), I establish three things and correct two merged claims.

1. **Lemma 1 (Λ-structure of the scaffold one-loop action; established, conditional on the regularization of `eq:W-again` with the operator built from `g^(0)` and with `A_μ` held at a background value).** The kinetic term is bilinear in Φ, so the fluctuation operator is `-g^(0)μν D̄_μ D̄_ν + E(Φ̄)` with `E` = ½ Hess V, which contains no derivative of Φ̄. The Λ-dependence of `W_E^(1)` is fixed by `a_0, a_1, a_2` (eqs `eq:appA-a0`–`eq:appA-a2`) up to terms vanishing as Λ→∞. Hence **no Λ⁴, Λ² or ln Λ term contains a derivative of Φ̄** (outside total derivatives). The Λ² curvature term is the Sakharov term `eq:universal-R` (with 𝒩₀ = 32) **for the scaffold metric g^(0)**, which is held fixed; for the composite metric `g[Φ̄]` its coefficient is zero. Explicit counterexample: for Φ̄ = (v+σ)𝕀 the Λ² term is (Λ²/32π²)∫ tr E(σ) with tr E = 16λ(v²+4vσ+2σ²) and no (∂σ)², whereas the emergent-background operator of `prop:scaffold` gives −𝒩₀Λ²(∂σ)²/(32π²v²), exactly the induced ghost-sign term used in `eq:Z-sigma`.
2. **Finite conformal-mode coefficient (established at one loop, A_μ = 0 fixed).** The (∂σ)² term of the scaffold one-loop action is UV finite: the Hermitian block gives `W_E ⊃ (3λ/8π²) e^{-λv²/Λ²} ∫(∂σ)²`, i.e. Z = 2N + 3λ/(4π²) + O(λv²/Λ²) (healthy sign); the massless anti-Hermitian block gives only a term non-analytic in p² with no Λ-dependent (∂σ)² coefficient.
3. **Lemma 2 (scaffold Lorentz invariance excludes linearised diffeomorphism invariance; established, all loop orders, flat scaffold, regulator and gauge fixing preserving scaffold rotations).** The components of Φ^I_A are scaffold scalars; hence the full quadratic effective action in Φ (connections A_μ, ω_μ set to zero or eliminated) is Σ φ̃_a(−p) F_ab(p²) φ̃_b(p). For any fixed linear map to a symmetric h_μν (e.g. the composite-metric fluctuation of `eq:g-from-e` with `eq:vev-is-frame`), the resulting form is invariant under h → h + p⊗ξ + ξ⊗p only if it vanishes (same on the traceless block with `eq:FP-gauge`). So the linearised Einstein–Hilbert and massless Fierz–Pauli structures (`eq:FP`, hypothesis 5 of `thm:mT`) **cannot be generated** for the composite metric by the displayed action or its quantum corrections on the flat scaffold. A p²-only form can coincide with a *gauge-fixed* EH operator (Feynman–de Donder), but without the gauge symmetry and its ghosts all its directions, including opposite-sign ones, propagate.
4. **Corrections of merged text (PRIOR-CLAIM-ERROR).** (a) `prop:scaffold` (ch08) concludes "Self-consistently substituting the emergent metric is therefore valid through the order of this conditional truncated identity." By Lemma 1 the replacement creates the entire Λ² emergent-metric coefficient (scaffold value zero), so the inference is invalid; the emergent-background operator is a premise, not a derivative-expansion consequence. The sentence introducing it ("The justification is the derivative expansion:") and `appB` L110–112 inherit the error. (b) ch05 L249–251 states that the quadratic expansion of S_micro produces ψ∂∂T and A∂T mixings; at tree level the expansion of `eq:Smicro` contains neither (derivatives contract only through g^(0)μν; A_μ mixes only with the anti-Hermitian block), and by Lemma 2 no symmetric loop correction produces ψ∂∂T.

**What is not established:** no value or sign of physical G_eff; nothing about the auxiliary-A_μ-integrated theory in Lemma 1; nothing about Θ-dependent (Lorentz-breaking) regulators, curved scaffolds in Lemma 2, or Presentation A; the emergent-background operator is not shown to be wrong as a modelling premise — only shown to be not supplied by the displayed action. No problem is closed; all labels unchanged.

## Target and status

Re-derived from the current sources (ch17 §`sec:ch17-done` and Appendix H ledger labels; full scan, no discrepancy found between them):

| Problem | Ch.17 | App H ledger label | Role here |
|---|---|---|---|
| F | "CRITICAL PATH; OPEN" (L404) | Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL (L1107–1110) | primary target |
| C | "CRITICAL PATH; OPEN" (L140) | OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL (L145–148) | Z_σ consequence |
| B | "CRITICAL PATH; OPEN" (L123) | OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL (L45–47) | provenance of thm:mT hyp. 5 |
| D (D1 required) | "CRITICAL PATH; OPEN" (L330) | OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL (L310–313) | structural ingredient |
| A, E, G-derived, N | critical path, OPEN | OPEN, PROGRAMME-CONDITIONAL | not targeted |

- **Original target (F):** "evaluate the weighted a_1 and the curvature-linear part of a_2 on the locked block, including diffeomorphism and local-Lorentz ghosts and the radial-mode threshold, with a scheme stated" and (ch17 item 6) "A,B,C and the sign/scheme dependence of G_eff computed from the specified operators; G_eff is not an input." G_eff is the coupling of the **emergent** metric (`eq:W-EH`).
- **Dependencies:** D1 (operators for ω, A_μ, B, ghosts), A (dictionary), E (signature); C depends on F through G_eff (`eq:Z-sigma`).
- **Classification of this package:** PROGRAMME-CONDITIONAL. It is a no-go / dependency resolution for F, not a derivation of F.

## Source reading

**Full scan.** `python scripts/make_digest.py --check` → `DIGEST CURRENT` (hash d3558e44b583da45, dirty-chapters: no). I read `scratch/digest.md`, then every one of the 30 manifest files in `chapters/` in full (ch01–ch18, appA–appL; appH all 1869 lines; ch17 all 788 lines). A full scan was required because the proposal changes a proposition's conclusion (scope statement). No unreadable files. Also read `MILESTONE.md`, `reports/ledger.md`, `reports/run-20261014-1216.md`, `proposals/001-full-gr-scope/proposal-r2.md` (unrelated scope text, no review) and the 002 ledger entry. Not re-proposing 002 content or the withdrawn fixed-L route.

## Research and reasoning

### R1. Why this is the exact missing step

Problem F's missing step (ch17 L457–471; App H L1116–1123) asks for "the gauge-fixed quadratic Hessian for every locked-block field" and then the weighted a_1. The manuscript already supplies the Φ–Φ Hessian of `eq:Smicro` on the scaffold (App H "Quadratic Hessian…", L1125–1151) and then, in the one-block bookkeeping paragraphs (L1190–1288, 1359–1432), *assumes* the operator lives on the emergent background (`eq:O-eta`, "Integrate η at one loop on a slowly varying emergent background g", ch08 L50–52), justified by `prop:scaffold`. The consequential question is therefore: **does the displayed action, computed on its own scaffold, induce an Einstein–Hilbert term for the composite metric at all?** If not, the emergent-background operator is not a technical replacement but the entire source of G_eff, and F's missing step must include deriving it.

### R2. Lemma 1 (derivation)

Setup: Euclidean `S_E = ∫√g0 Tr(g0^{μν}(D_μΦ)†D_νΦ + V)`, locked 4×4 complex block, A_μ = Ā_μ fixed. Real components: Φ = Φ̄ + Σ_a(h_a + i k_a)T_a with Hermitian T_a, Tr T_aT_b = δ_ab (check 1(i): Tr(δ†δ) = Σh²+Σk²). S_E is quadratic in Φ in its kinetic term, so δ²S_E/δΦδΦ = 2(−g0^{μν}D̄_μD̄_ν + E(Φ̄)), E = ½ Hess V(Φ̄), with no Φ̄-derivatives. One loop: W_E = ½ Tr ln O (ln 2 constant dropped), regulated as in `eq:W-again`, s_min = Λ^{-2}, using the scaffold operator.

Λ-dependence: with I(Λ) = ∫_{Λ^{-2}}^{μ^{-2}} ds s^{-1} f(s), f(s) = Tr e^{-sO} ~ (4πs)^{-2} Σ_k s^k ∫a_k, one has ∂_Λ I = 2Λ^{-1} f(Λ^{-2}) = (2/Λ)(Λ⁴/16π²)Σ_k Λ^{-2k}∫a_k. Terms with k ≥ 3 give ∂_Λ I = O(Λ^{3-2k}), whose integral vanishes as Λ→∞. So the Λ-dependent part of W_E is
−∫√g0 [ a0Λ⁴/(64π²) + a1Λ²/(32π²) + a2 ln(Λ²/μ²)/(32π²) ] with a0 = 32, a1 = tr(R0/6 − E), a2 = tr(R0²-terms/180 + E²/2 − R0E/6 + F̄²/12 + D²R0/30 − D²E/6) (manuscript `eq:appA-a2`). The only Φ̄-derivative is in D²E, a total derivative. ∎

Interpretation: the Λ² curvature term is −(32/192π²)Λ²∫√g0 R[g0], i.e. the standard Sakharov-induced term **for g^(0)**. Assumption `ass:aux-metric` holds g^(0) fixed, so this term does not act on the emergent g.

Counterexample to `prop:scaffold`'s conclusion (flat scaffold, Ā = 0, Φ̄ = (v+σ)𝕀): Repair II gives g = Ω²δ with Ω = 1+σ/v (`eq:repairII-trace`); in 4D Euclidean, √g R = −6Ω□Ω = 6(∂Ω)² − 6∂(Ω∂Ω) (check 1(iv), sign fixed by R = +12 on unit S⁴). Scaffold computation: Λ² term = (Λ²/32π²)∫tr E(σ), tr E = 16λ(v² + 4vσ + 2σ²) (check 1(ii)) — no (∂σ)². Emergent-operator computation: −(32/192π²)Λ²∫√g R = −(Λ²/π²v²)∫(∂σ)² = −𝒩₀Λ²(∂σ)²/(32π²v²). Consistency with `eq:Z-sigma`: with 1/(16πG) = 𝒩₀Λ²/(192π²), the Lorentzian induced term +3(∂σ)²/(8πGv²) corresponds to Euclidean −6·𝒩₀Λ²/(192π²v²) = −𝒩₀Λ²/(32π²v²). ✓ So the replacement in `prop:scaffold` changes the Λ²(∂σ)² coefficient from 0 to the full induced value; the proposition's own text concedes the change consists of "the same operators already kept", so the inference "therefore valid through the order of this identity" does not follow and is false for the displayed action.

### R3. Finite (∂σ)² coefficient

At Φ̄ = φ₀𝕀: E_H = (λ/2)(3φ₀² − v²) on 16 Hermitian components, E_K = (λ/2)(φ₀² − v²) on 16 anti-Hermitian components, no off-diagonal entries (check 1(ii)). With φ₀ = v+σ: E_H(0) = λv², E_H' = 3λv, E_K(0) = 0, E_K' = λv. Second order of ½Tr ln(O₀ + δE): −¼ Tr(GδE GδE) = −¼ Σ_b n_b E_b'² ∫ σ̃(p)σ̃(−p) B_b(p), with B(p) = (1/16π²)∫₀¹dx E₁((m² + x(1−x)p²)/Λ²) (proper-time/Feynman-parameter representation; checked numerically against direct quadrature, check 2). Exactly, ∂_{p²}B|₀ = −e^{−m²/Λ²}/(96π²m²) (check 2, closed form and finite differences at Λ/m = 10, 100, 1000). Hence W_E ⊃ (16·9λ²v²)/(4·96π²λv²) e^{−λv²/Λ²}∫(∂σ)² = (3λ/8π²)e^{−λv²/Λ²}∫(∂σ)². Tree: Tr(∂Φ̄†∂Φ̄) = 4(∂σ)² = ½(2N)(∂σ)², N = 4. So Z = 2N + 3λ/(4π²) + O(λv²/Λ²), relative correction 3λ/(32π²). The K block: m = 0, B₀(p) = (1/16π²)[ln(Λ²/p²) + 2 − γ_E + O(p²/Λ²)]: a λ²v² ln Λ mass renormalization and a non-analytic λ²v² ln p² term; its analytic p² coefficient is (1/96π²)/Λ² → 0 (check 2). This agrees with the textbook fact that one-loop λφ⁴-type theories have no field-strength renormalization; the result is UV finite and regulator independent at leading order.

### R4. Lemma 2 (derivation)

Premise check from the manuscript: App H D (L742–757) states "In `eq:Smicro` the field Φ^I_A carries no coordinate index: it is a set of scalar fields on the scaffold"; ch02 L36–41 keeps coordinate, tangent and internal alphabets separate; the identification A↔μ (`eq:vev-is-frame`) is interpretive, not a symmetry. On flat Euclidean scaffold, x → Rx (R ∈ SO(4)) with Φ_a(x) → Φ_a(R⁻¹x), A_μ, ω_μ transforming as vectors in μ only, is a symmetry of `eq:Smicro` and of its D2 completion `eq:D-both` (scaffold index only on ∂_μ, A_μ, ω_μ, contracted with g^(0)μν). The background Φ̄ = v𝕀, Ā = ω̄ = 0 is invariant.

Assume an SO(4)-preserving regulator (the scaffold proper-time regulator is) and gauge fixing (Lorenz/background-field/unitary gauges are). The effective action Γ is then SO(4)-invariant, so Γ^(2)_ab(Rp) = Γ^(2)_ab(p) for the scalar components; an SO(4)-invariant function of one vector depends only on |p|. Mixed kernels Γ_{a,μ}(p) are vectors, = p_μ f_a(p²); connection kernels are α(p²)δ_μν + β(p²)p_μp_ν; their Schur complement on the Φ block again depends only on p². So the quadratic form on Φ, with connections zero or eliminated, is F(p²).

Invariance step: let Q_p be the form on h_μν (a fixed linear image of the Φ components, restricted or reduced). Q(h+δh) = Q(h) ∀h, with δh = p⊗ξ + ξ⊗p, iff Q_p δh = 0 ∀ξ. Since Q_p depends only on p², it annihilates p'⊗ξ + ξ⊗p' for every p' on the same SO(4)-orbit; for p ≠ 0 these span Sym²(ℝ⁴) (take p' = |p|e_i, ξ = e_j). So Q_p = 0. Script check 3 solves the 160 linear equations for a general 10×10 symmetric form: forced to zero for Euclidean |p|²=1 and for Lorentzian p² = +1, −1 (future sheet), 0 (future null), and on the 9-dim traceless block with δT = pξ + ξp − ½η(p·ξ) (`eq:FP-gauge`) for δ and η. Script also confirms Q_FP is invariant and direction dependent (value 0 vs 2 for h₀₁ = 1 at p = e₀ vs e₂), so Q_p ≠ c·Q_FP + (p²-only form) unless c = 0; and confirms Q_FP + 2(p^μh_μν − ½p_νh)² = p²(h·h − ½h²) (Feynman–de Donder), which is why the p²-only statement must be phrased via gauge invariance, not via the form alone.

Relation to existing text: App H D L765–791 proves the tree-level classification for ≤2 derivatives and says FP structures "are not excluded" for terms "that tie the derivative index to the tangent index through the vacuum identification"; App H D L948–966 restricts to "diagonal-invariant forms without derivative–tangent mixing". Lemma 2 shows such mixing is never *generated* from `eq:Smicro` on a flat scaffold with a symmetric regulator, at any loop order; it must be put in by a new ingredient. This is consistent with, and strictly extends, those paragraphs; it does not contradict them.

### R5. Consequences

- **F:** the Φ–Φ Hessian of the displayed action on the scaffold contributes no Einstein–Hilbert term for the composite metric (A = B = C = 0 from this route); the emergent-background operator (`eq:O-eta` + `prop:scaffold`) is the sole source of the induced coupling in `thm:Geff` and is a premise. F's missing step thus includes deriving that operator, or another derivative–tangent mixing ingredient, from the microscopic theory.
- **C:** in the scaffold one-loop calculation, Z_σ = 2N + 3λ/(4π²) > 0; the ghost/tachyon branch of `eq:Z-sigma` (Z < 0 for Nv² < 3M_P²) is a property of the assumed emergent operator. This neither closes C nor removes `ass:gap-psi`.
- **B:** hypothesis 5 of `thm:mT` (FP tensor block) cannot be supplied by the displayed action or its symmetric quantum corrections on the flat scaffold; it is an input requiring the same new ingredient. (App H F L1145–1147 already says it is "an additional input"; Lemma 2 shows loops cannot supply it.)
- **D1:** an admissible ingredient must provide a tensor with one scaffold and one tangent index (or a composite-metric operator/regulator, or a Presentation-A mechanism). Sketch only; see Author decision.

### R6. Literature

- Seeley–DeWitt a₀, a₁, a₂: used exactly as displayed in `eq:appA-a0`–`eq:appA-a2` (manuscript, standard; not re-derived). No a₃ coefficient is used in the proposed text; the finite (∂σ)² term is computed directly from the bubble.
- Sakharov-type induced gravity (positive 1/G from minimal scalars, coefficient N/(12π)Λ² in this proper-time convention) is consistent with the manuscript's own sector-sum paragraph (App H L1318–1333); no external citation is added.
- **Weinberg–Witten theorem** (S. Weinberg, E. Witten, "Limits on massless particles", Phys. Lett. B 96 (1980) 59–62): bibliographic record confirmed via the Princeton research portal and citing literature (e.g. Porrati, arXiv:0804.4672); the abstract states that theories with a Lorentz-covariant energy–momentum tensor forbid composite or elementary massless particles of spin > 1. DOI not independently verified. **Not used in the proposed LaTeX.** It is directly relevant to the structural question in "Author decision needed" (a flat-scaffold Presentation-B theory with exact scaffold Poincaré invariance and a covariant Hilbert stress tensor cannot have a massless helicity-±2 particle); its application to NAMCG has not been checked here and is left for a later package.
- Composite-metric pregeometry (Akama 1978; Amati–Veneziano 1981) is mentioned only as context in the author note; **not independently verified**, not cited in LaTeX.

### R7. Comparison with the original target

The original F target is not derived. This package shows that the route "specify the Hessian of the displayed action and compute its weighted a₁" cannot, on its own scaffold, yield the emergent-metric coupling at all, and isolates the structural input that F (and B's hypothesis 5) actually needs.

## Claim classification

| Claim | Class |
|---|---|
| Fluctuation operator of `eq:Smicro` at fixed Ā is −D̄² + E(Φ̄), E = ½Hess V, E derivative-free | established identity |
| Λ-dependence of W_E fixed by a₀–a₂ up to o(1) as Λ→∞ | established (given heat-trace asymptotics; regularization of `eq:W-again`) |
| No Λ-dependent term contains ∂Φ̄ (Ā fixed); Λ²R term is the scaffold's | established, conditional on scaffold-operator regularization and fixed Ā |
| tr E(σ) = 16λ(v²+4vσ+2σ²); E_H, E_K values | established (sympy, check 1) |
| √gR = 6(∂σ)²/v² + t.d. for g = (1+σ/v)²δ | established (sympy, check 1) |
| Emergent-operator value −𝒩₀Λ²(∂σ)²/(32π²v²) and its match to `eq:Z-sigma` | established algebra, conditional on emergent-operator premise |
| `prop:scaffold` final inference invalid for displayed action | established (counterexample) — PRIOR-CLAIM-ERROR |
| ΔZ = 3λ/(4π²)·e^{−λv²/Λ²} from H block; K block non-analytic, no Λ-dependent p² term | established one-loop result, conditional on Ā = 0 fixed, scaffold regulator |
| Lemma 2 (p²-only quadratic form; gauge invariance ⇒ zero; also traceless block) | established, conditional on flat scaffold, SO(4)-preserving regulator and gauge fixing, invariant vacuum |
| ch05 ψ∂∂T/A∂T sentence false for `eq:Smicro` at tree level | established (direct expansion) — PRIOR-CLAIM-ERROR (non-load-bearing, "schematic") |
| F needs a derived emergent-background operator or other derivative–tangent mixing ingredient | conditional consequence (dependency resolution) |
| Integrated auxiliary A_μ, Θ-dependent regulators, Presentation A | unresolved / not covered |
| Weinberg–Witten applicability | not checked; context only |

## Proposed changes

All `.tex` files are CRLF (checked with `file`). No new labels are introduced; every `\ref`/`\eqref` target below was verified to exist exactly once: `eq:Smicro`, `eq:V`, `ass:aux-metric`, `eq:W-again`, `eq:s-limits`, `eq:appA-a0`, `eq:appA-a2`, `eq:universal-R`, `eq:repairII-trace`, `prop:scaffold`, `eq:Z-sigma`, `lem:msigma`, `eq:D-both`, `eq:g-from-e`, `eq:vev-is-frame`, `eq:FP-gauge`, `eq:FP`, `thm:mT`, `sec:status-D`, `sec:status-F`, `eq:O-eta`, `thm:Geff`, `eq:Geff-structure`, `app:status`. `E_1` is already defined in App H L1267.

### Item 1 — `chapters/appH-microscopic-proofs.tex`, Problem F section (new conditional paragraphs)

Anchor: insert immediately **before** the line `\section{Problem G: HBEV}` (unique; 1 occurrence), i.e. after the paragraph ending "and does not provide the missing \(\mathrm{SO}(3,1)\)-compatible / sector sum. Problems~B, C, D, F and~G remain open." (L1468–1470). Nothing is removed. Leave one blank line before `\section{Problem G: HBEV}`.

```latex
\paragraph{Which metric the scaffold one-loop action induces (conditional; not closure).}
Consider the displayed action~\eqref{eq:Smicro} with
potential~\eqref{eq:V} on the square locked block, on the scaffold
\(g^{(0)}\) of Assumption~\ref{ass:aux-metric}, after Wick rotation,
with the internal connection held at a background value
\(\bar A_\mu\) and not integrated. Expand \(\Phi=\bar\Phi+\varphi\)
about a smooth background \(\bar\Phi\) and write \(\varphi\) in
thirty-two real components normalized so that the kinetic term is
\(\sum_a g^{(0)\mu\nu}\bar D_\mu\varphi_a\bar D_\nu\varphi_a\). The
kinetic term is bilinear in \(\Phi\), so its second variation does not
depend on \(\bar\Phi\), and the fluctuation operator is
\[
  \mathcal O_{\bar\Phi}
  =-g^{(0)\mu\nu}\bar D_\mu\bar D_\nu+E(\bar\Phi),
\]
where \(\bar D\) is built from \(g^{(0)}\) and \(\bar A_\mu\), and
\(E(\bar\Phi)\) is one half of the Hessian of \(V\) at \(\bar\Phi\);
\(E\) contains no derivative of \(\bar\Phi\). Use this operator
in~\eqref{eq:W-again} with the limits~\eqref{eq:s-limits}. For
\(I(\LUV)=\int_{\LUV^{-2}}^{\mu^{-2}}s^{-1}f(s)\,\mathrm{d}s\) one has
\(\partial_{\LUV}I=2\LUV^{-1}f(\LUV^{-2})\), so the
\(\LUV\)-dependence of \(W_E^{(1)}\) is fixed by the small-\(s\)
expansion of the heat trace through \(a_2\), up to terms that vanish as
\(\LUV\to\infty\). By~\eqref{eq:appA-a0}--\eqref{eq:appA-a2},
\[
  W_E^{(1)}\supset
  -\int\mathrm{d}^4x\,\sqrt{g^{(0)}}\left[
    \frac{32\,\LUV^4}{64\pi^2}
    +\frac{\LUV^2}{32\pi^2}
     \operatorname{tr}\Bigl(\tfrac16R[g^{(0)}]-E(\bar\Phi)\Bigr)
    +\frac{1}{32\pi^2}\ln\Bigl(\frac{\LUV^2}{\mu^2}\Bigr)a_2
  \right],
\]
where \(a_2\) contains \(E^2\), \(R[g^{(0)}]E\), curvature-squared
terms of \(g^{(0)}\), \(\bar F_{\mu\nu}\bar F^{\mu\nu}\) and total
derivatives. No \(\LUV\)-dependent term contains a derivative of
\(\bar\Phi\) outside a total derivative. The \(\LUV^2\) curvature term
is the term~\eqref{eq:universal-R}, with \(\mathcal N_0=32\), for the
scaffold metric \(g^{(0)}\), which Assumption~\ref{ass:aux-metric}
holds fixed.

For the composite metric the corresponding coefficient vanishes. On
the flat scaffold take \(\bar A_\mu=0\) and
\(\bar\Phi=(v+\sigma)\mathbb I\), so that
\(g=(1+\sigma/v)^2\eta\) by~\eqref{eq:repairII-trace}; in the
Euclidean section \(\sqrt g\,R[g]=6(\partial\sigma)^2/v^2\) up to a
total derivative. The \(\LUV^2\) term above is
\(\tfrac{\LUV^2}{32\pi^2}\int\mathrm{d}^4x\operatorname{tr}E(\sigma)\),
with \(\operatorname{tr}E(\sigma)=16\lambda(v^2+4v\sigma+2\sigma^2)\),
and contains no \((\partial\sigma)^2\). Building the operator on \(g\)
instead, as in Proposition~\ref{prop:scaffold}, gives
\(-\mathcal N_0\LUV^2(\partial\sigma)^2/(32\pi^2v^2)\) at the same
order, which is the induced term of~\eqref{eq:Z-sigma} with
\(1/(16\pi G_{\mathrm{eff}})=\mathcal N_0\LUV^2/(192\pi^2)\). The
replacement supplies the whole \(\LUV^2\) coefficient for the composite
metric; it does not correct a scaffold value.

The \((\partial\sigma)^2\) term of the scaffold one-loop action is
ultraviolet finite. At \(\bar A_\mu=0\) the sixteen Hermitian
components have \(E_H=\tfrac\lambda2\bigl(3(v+\sigma)^2-v^2\bigr)\)
and the sixteen anti-Hermitian components have
\(E_K=\tfrac\lambda2\bigl((v+\sigma)^2-v^2\bigr)\). At second order in
\(\sigma\) the Hermitian block gives
\[
  W_E^{(1)}\supset
  -4\,E_H'(0)^2\int\frac{\mathrm{d}^4p}{(2\pi)^4}\,
   \tilde\sigma(p)\tilde\sigma(-p)\,B(p),
  \qquad
  B(p)=\frac{1}{16\pi^2}\int_0^1\mathrm{d}x\,
   E_1\!\left(\frac{\lambda v^2+x(1-x)p^2}{\LUV^2}\right),
\]
with \(E_H'(0)=3\lambda v\) and
\(\partial_{p^2}B|_{p=0}=-e^{-\lambda v^2/\LUV^2}/(96\pi^2\lambda v^2)\).
The local term is therefore
\(W_E^{(1)}\supset\frac{3\lambda}{8\pi^2}e^{-\lambda v^2/\LUV^2}
\int\mathrm{d}^4x\,(\partial\sigma)^2\), which adds
\(3\lambda/(4\pi^2)\), up to \(O(\lambda v^2/\LUV^2)\), to the
microscopic value \(2N\) of \(Z\) in~\eqref{eq:Z-sigma}. The
anti-Hermitian block is massless at \(\sigma=0\) and contributes a term
non-analytic in \(p^2\) with no \(\LUV\)-dependent
\((\partial\sigma)^2\) coefficient. In this one-loop calculation the
conformal-mode kinetic term keeps the sign of Lemma~\ref{lem:msigma};
the opposite-sign term of~\eqref{eq:Z-sigma} enters only through the
operator built on the emergent metric.

\paragraph{Scaffold rotations exclude linearized diffeomorphism invariance (conditional; not closure).}
In~\eqref{eq:Smicro} the components of \(\Phi^I{}_A\) are scalars of
the scaffold: a scaffold index appears only on \(\partial_\mu\) and
\(A_\mu\), and on \(\omega_\mu\) in the completion~\eqref{eq:D-both}.
On the flat Euclidean scaffold, rotations \(x\mapsto Rx\),
\(R\in\mathrm{SO}(4)\), acting on scaffold indices alone are a
symmetry, and the background \(\bar\Phi=v\mathbb I\),
\(\bar A_\mu=\bar\omega_\mu=0\) is invariant. Assume that the regulator
and the gauge fixing preserve this symmetry, as the scaffold
proper-time regulator above does. Then, at any loop order, the
quadratic part of the effective action in the components of \(\Phi\),
with the connections set to zero or eliminated at quadratic order, has
the form
\(\sum_{a,b}\tilde\varphi_a(-p)F_{ab}(p^2)\tilde\varphi_b(p)\):
invariance gives \(F_{ab}(Rp)=F_{ab}(p)\), an
\(\mathrm{SO}(4)\)-invariant function of one vector depends only on
\(p^2\), and eliminating a connection, whose mixed and diagonal kernels
have the forms \(p_\mu f(p^2)\) and
\(\alpha(p^2)\delta_{\mu\nu}+\beta(p^2)p_\mu p_\nu\) with internal
labels suppressed, preserves this form. Let \(h_{\mu\nu}\) be any fixed
linear function of these components, for example the composite-metric
fluctuation obtained from~\eqref{eq:g-from-e} with the
identification~\eqref{eq:vev-is-frame}, and let \(Q_p\) be the
restricted or reduced form on \(h\). If \(Q_p\) is invariant under
\(h\mapsto h+p\otimes\xi+\xi\otimes p\) for all \(\xi\), then \(Q_p\)
annihilates \(p'\otimes\xi+\xi\otimes p'\) for every \(p'\) with
\(p'^2=p^2\); for \(p\neq0\) these tensors span all symmetric tensors,
so \(Q_p=0\). The same holds on the traceless block with the
transformation~\eqref{eq:FP-gauge}. The linearized Einstein--Hilbert
form and the massless Fierz--Pauli form~\eqref{eq:FP} are invariant
and nonzero, hence depend on the direction of \(p\); \(Q_p\) cannot
equal \(c\) times either of them plus a form depending on \(p\) only
through \(p^2\) unless \(c=0\). A form depending only on \(p^2\) can
coincide with a gauge-fixed linearized Einstein--Hilbert operator, for
example the Feynman--de~Donder form
\(p^2\bigl(h_{\mu\nu}h_{\mu\nu}-\tfrac12h^2\bigr)\), but without the
gauge symmetry and its ghosts each nondegenerate direction of such a
form, including directions of opposite sign, is a propagating
component.

\paragraph{What the two preceding results imply for Problem~F (conditional; not closure).}
On the flat scaffold, with a regulator and gauge fixing that preserve
scaffold rotations, neither the displayed action nor its quantum
corrections give the composite-metric fluctuation a linearized
diffeomorphism invariance, an induced Einstein--Hilbert term, or the
Fierz--Pauli block of hypothesis~5 of Theorem~\ref{thm:mT}; the
induced Fierz--Pauli term assumed in the quadratic tests of
Section~\ref{sec:status-D} is likewise not generated in this way.
These structures need an ingredient that ties derivative indices to
tangent indices, such as a background tensor carrying one scaffold and
one tangent index, an operator or regulator built from the composite
metric, or a mechanism derived from Presentation~A. The
operator~\eqref{eq:O-eta} on the emergent background, used in
Theorem~\ref{thm:Geff} through Proposition~\ref{prop:scaffold}, is
such an ingredient and is assumed, not derived. The
\(\Phi\)--\(\Phi\) Hessian of the displayed action on the scaffold
therefore contributes no Einstein--Hilbert term for the composite
metric, and nothing to \(A\), \(B\) or \(C\)
in~\eqref{eq:Geff-structure}; the missing step of Problem~F includes
deriving the emergent-background operator, or another such
ingredient, from the microscopic theory. Not covered here: integration
of the auxiliary \(A_\mu\) in the first result, curved scaffolds in the
second, regulators depending on \(\Theta^{\mu\nu}\), which break
scaffold rotation invariance, and Presentation~A. No value or sign of
\(G_{\mathrm{eff}}\) follows. Problems~B, C, D and~F remain open.
```

Notes for Item 1: the inline `h_{\mu\nu}h_{\mu\nu}` is the Euclidean contraction (stated "Euclidean scaffold" in the same paragraph). "linearized" follows the manuscript's dominant spelling in App H (both "linearized" and "linearised" occur; integrator may harmonize).

### Item 2 — `chapters/ch08-heat-kernel.tex`, Section `sec:ch8-which-g` (correction of `prop:scaffold`; PRIOR-CLAIM-ERROR)

(a) Replace exactly the sentence (L284–285)
`The justification is the derivative expansion:`
with
```latex
The derivative expansion bounds what this choice changes; it does not
justify it:
```
The preceding two sentences ("Assumption~\ref{ass:aux-metric} declared … written on \(g_{\mu\nu}\).") are kept.

(b) Inside `\begin{proposition}[Scaffold replacement]`, keep the first three sentences ("Let … higher." and "On the Minkowski scaffold … \eqref{eq:W-expand}.") and replace exactly the final sentence (L294–296)
`Self-consistently substituting the emergent metric is therefore valid through the order of this conditional truncated identity.`
with
```latex
  These are the operators whose coefficients the identity computes, so
  the replacement is not a controlled approximation at that order. For
  the displayed action~\eqref{eq:Smicro} with the operator built from
  \(g^{(0)}\), the \(\LUV^2\) curvature term is that of \(g^{(0)}\)
  and multiplies no derivative of the condensate
  (Appendix~\ref{app:status}, Section~\ref{sec:status-F}); the
  emergent-metric coefficient of the identity is produced by the
  replacement. Using \(g\) inside \(\mathcal O_\eta\) is therefore a
  premise of the identity, not a consequence of the derivative
  expansion.
```
The `\end{proposition}` and the following paragraph ("At higher order the replacement produces …") are kept.

### Item 3 — `chapters/appB-modular.tex`, Section `sec:appB-replica` (stale dependent sentence)

Replace exactly (L110–112)
`In Presentation~B the cover is a branched cover of the auxiliary manifold, later identified with the emergent spacetime by Proposition~\ref{prop:scaffold}.`
with
```latex
In Presentation~B the cover is a branched cover of the auxiliary
manifold. Identifying it with the emergent spacetime uses the
emergent-background premise recorded in
Proposition~\ref{prop:scaffold}, which the displayed action does not
supply.
```
The next sentence ("In Presentation~A the same construction requires Problem~A of Chapter~17.") is kept.

### Item 4 — `chapters/ch05-lorentz-decomposition.tex`, Section `sec:ch5-kinetic` (false statement about S_micro; PRIOR-CLAIM-ERROR, non-load-bearing)

Replace exactly (L249–251)
`On a Minkowski condensate the mixing terms that survive after gauge fixing are of the form \(\psi\,\partial\partial T\) and \(A\,\partial T\). They are the usual linearized scalar--tensor and vector--tensor mixings.`
with
```latex
Mixing terms of the form \(\psi\,\partial\partial T\) and
\(A\,\partial T\) would be the usual linearized scalar--tensor and
vector--tensor mixings. The quadratic expansion of
\(S_{\mathrm{micro}}\) on the flat scaffold contains neither: its
kinetic term contracts derivatives only through \(g^{(0)\mu\nu}\), and
\(A_\mu\) mixes only with the anti-Hermitian part of \(\delta\Phi\);
a \(\psi\,\partial\partial T\) structure requires an additional
ingredient (Appendix~\ref{app:status}, Section~\ref{sec:status-F}).
```
The following sentence "Two structural facts will be used later." and the enumerate are kept.

Derivation of the A_μ statement: at Φ̄ = v𝕀, (DΦ)†DΦ ⊃ −iv(∂δΦ)†A + ivA∂δΦ, whose trace is iv Tr(A ∂(δΦ − δΦ†)) = 2iv Tr(A∂K) with K the anti-Hermitian part; this is the Y–A mixing of App H's U(4) paragraph (L1365–1380).

### Stale passages elsewhere (not edited; listed for the author)

- ch08 "What has been computed" table row "truncated \(R\)-coefficient identity | conditional on specified sectors and scheme" — could add "and on the emergent-background operator" (optional).
- ch04 L270–272 "Chapters~8 and~11 compute pieces of it: the Einstein--Hilbert term from the heat kernel" — conditional reading now needed (optional).
- ch01 L59–60 "a heat-kernel expansion supplies an explicit formula for \(\Geff\)" — framed as "theorems inside the framework"; optional qualifier.
- ch17 F "Missing step" (L457–471): see Author decision 3 (ch17 defines the target; not edited here).
- Pre-existing, unrelated: ch01 `eq:composite-metric`/`eq:spine`, ch02 `eq:composite-vierbein`, ch03 `eq:vierbein-next` still display the Repair-I form e = ⟨∂Φ⟩ that ch04 abandons; not addressed.

## Verification scripts

All in `proposals/003-auto-target/`, run with `C:\Python312\python` (sympy 1.14, mpmath 1.3); outputs saved alongside.

- `check_scaffold_hessian.py` → `check_scaffold_hessian.out.txt`: (i) Tr(δ†δ) = Σh²+Σk² in the orthonormal Hermitian basis; (ii) Hessian of V at φ₀𝕀 is block diagonal with E_H = (λ/2)(3φ₀²−v²), E_K = (λ/2)(φ₀²−v²) (16 each), E_H'(0) = 3λv, E_K'(0) = λv, tr E(σ) = 16λ(v²+4vσ+2σ²), N = 4; (iv) √g R + 6Ω□Ω = 0 for g = Ω²δ in 4D and R = +12 on the stereographic unit S⁴ (sign convention); emergent-operator coefficient −𝒩₀Λ²/(32π²v²).
- `check_bubble_lambda.py` → `check_bubble_lambda.out.txt`: closed form ∂_{p²}B|₀ = −e^{−m²/Λ²}/(96π²m²) and its large-Λ series (Λ-independent leading term); E₁ representation of the proper-time integral (numeric); W_E (∂σ)² coefficient (3λ/8π²)e^{−λv²/Λ²}, ΔZ → 3λ/(4π²), relative 3λ/(32π²); massless-block analytic p² coefficient ∝ 1/Λ²; numerical cross-check of B(p) against direct 2D quadrature and of ∂_{p²}B by finite differences at Λ/m = 10, 100, 1000.
- `check_invariance_nogo.py` → `check_invariance_nogo.out.txt`: a general symmetric 10×10 form invariant under h → h + p⊗ξ + ξ⊗p for a spanning set of p with fixed p² is forced to 0 (Euclidean; Lorentzian p² = +1, −1 future sheet, 0 future null); same on the traceless block with δT = pξ + ξp − ½η(p·ξ) (δ and η); Q_FP gauge invariant and direction dependent; Q_FP + de Donder term = p²(h·h − ½h²).

Tool output is a check; the reasoning is in R2–R4.

## Milestone assessment

I believe **M3** applies: an already merged claim is wrong — the concluding inference of `prop:scaffold` ("Self-consistently substituting the emergent metric is therefore valid through the order of this conditional truncated identity") is false for the displayed action (explicit counterexample, R2); the dependent appB sentence and the ch05 mixing sentence are also incorrect as statements about `eq:Smicro`. The ch05 item alone would be non-load-bearing; `prop:scaffold` is load-bearing for applying `thm:Geff` to the emergent metric. I also believe **M2** applies: Lemma 2 is a new no-go ruling out the route, currently open in the F missing step, of obtaining the composite-metric Einstein–Hilbert/Fierz–Pauli structure from the Hessian of the displayed action and its symmetric quantum corrections on the flat scaffold. **M5** is flagged (not proposed): resolving F/B requires a structural ingredient (Author decision 2). No M1 (nothing on the critical path is derived) and no M4 (no label change proposed).

## Status-label recommendation

Critical-path set re-derived from ch17 §`sec:ch17-done` and App H: A, B, C, D1, E, F, G-derived, N (H, I, J optional). **No label change recommended.** F, C, B, D remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. The proposed text adds no status word and edits no "Ledger label" paragraph.

## Author decision needed

1. **Correction of `prop:scaffold` (Item 2).** Approve the replacement of its final sentence and of the lead-in sentence. Optionally, convert the emergent-background operator into a named assumption (e.g. "fluctuations propagate on the emergent metric") and add it to the ch16 inventory as load-bearing; that would change the assumption inventory and is not proposed in LaTeX here.
2. **Structural ingredient for F and for hypothesis 5 of `thm:mT` (M5 flag; sketch only).** Lemma 2 shows the displayed Presentation-B action on a flat scaffold cannot produce linearized diffeomorphism invariance for the composite metric. Candidate routes, none adopted: (a) promote the tangent index of Φ to a scaffold covector index, Φ^I_μ (a coframe one-form), so the vacuum δ^I_μ breaks scaffold × internal Lorentz to a diagonal and permits ∂^μΦ_μ-type invariants — this inherits the indefinite-kinetic and ghost issues already recorded for the η-contracted candidate in App H D, and any route keeping a fixed Poincaré-invariant scaffold with a covariant conserved stress tensor must also confront the Weinberg–Witten theorem (Phys. Lett. B 96 (1980) 59; applicability not checked here); (b) keep the emergent-background operator as an explicit premise (scope-limited Presentation-B model; F stays open); (c) derive the fluctuation metric from Presentation A, noting that in matrix models the metric seen by fluctuations is built from the background matrices/Θ (cf. Remark `rem:ch3-moyal-check`, `rem:ch3-varying-theta`), not from Φ. Falsifier/validator: any proposed ingredient must make the composite-metric quadratic action invariant under δh = ∂ξ off shell, by the criterion of App H D L765–791.
3. **Optional ch17 sentence** (ch17 defines the target; not edited here). If desired, append to ch17 F "Missing step" (after "…is an input to, not a specification of, these operators."): "On the flat scaffold, that Hessian and its symmetric quantum corrections induce no Einstein--Hilbert term for the composite metric (Appendix~\ref{app:status}, Section~\ref{sec:status-F}); the operator on the emergent background must itself be derived."
4. Optional BibTeX for a later package (not used in this proposal's LaTeX; DOI not verified):
```bibtex
@article{WeinbergWitten1980,
  author  = {Weinberg, Steven and Witten, Edward},
  title   = {Limits on massless particles},
  journal = {Phys. Lett. B},
  volume  = {96},
  number  = {1-2},
  pages   = {59--62},
  year    = {1980}
}
```

## Remaining open step

To close F as originally targeted: derive from the matrix theory (or a stated completion) an operator or structure that ties derivative and tangent indices so that the composite-metric quadratic action is linearized-diffeomorphism invariant; specify the resulting gauge-fixed operators, ghosts (diffeomorphism and local-Lorentz), weights, thresholds, continuation and counterterm scheme; then compute A, B, C and the sign of G_eff. Separately still open in this direction: the A_μ-integrated version of Lemma 1 (auxiliary gauge field, sigma-model-type derivative couplings), Θ-dependent regulators, curved scaffolds for Lemma 2, and whether the Weinberg–Witten theorem obstructs a massless helicity-2 composite graviton in any fixed-flat-scaffold Presentation-B completion (candidate next package; would need its premises checked against NAMCG's stress tensor and Hilbert space). For C: mixing with T, non-minimal and matter couplings, and the physical status of Z once a metric-producing ingredient is chosen. For B: deriving the Fierz–Pauli block (hypothesis 5) and stationarity.

## Special instructions for the gatekeeper

- Must not be asserted: that physical G_eff vanishes; that the emergent-background operator is wrong as a model; that F, B, C or D is closed or advanced to DERIVED; that Weinberg–Witten applies to NAMCG (it is context only, not in LaTeX).
- Re-check: (1) the Λ-dependence argument ∂_Λ I = 2Λ⁻¹f(Λ⁻²) and that `eq:appA-a2` has no Φ̄-derivative except D²E; (2) Euclidean sign and normalization chain −𝒩₀Λ²/(32π²v²) ↔ `eq:Z-sigma` with 1/(16πG) = 𝒩₀Λ²/(192π²); (3) the factor −¼·16·E_H'² and ∂_{p²}B, giving ΔZ = 3λ/(4π²); (4) that Lemma 2 needs only scaffold SO(4) with Φ components scalars, and that the Schur-complement step preserves p²-dependence; (5) the de Donder caveat is correctly phrased (p²-only forms are not excluded; gauge invariance is); (6) the ch05 A_μ-mixing claim (only anti-Hermitian part) at Φ̄ = v𝕀.
- Scope limits to enforce in the text: Lemma 1 with A_μ fixed (background, not integrated); Lemma 2 on flat scaffold with rotation-preserving regulator and gauge fixing; neither covers Θ-dependent regulators or Presentation A.
- Interplay with proposal 002 (not integrated): its Υ uses G_eff from the a₁ term on the emergent background; this package shows that input is the emergent-operator premise. 002's text is already conditional on `thm:Geff`; no change to 002 is proposed.
- Items 2 and 4 edit merged text (PRIOR-CLAIM-ERROR); please classify severity (I assess Item 2 as load-bearing, Item 4 as non-load-bearing).
