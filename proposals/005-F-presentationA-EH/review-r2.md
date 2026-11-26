VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
The new cubic-order test is sound and reproducible, all four r1 findings are closed, the LaTeX is worded as a conditional computation, and there are no required corrections. Two minor wording suggestions are optional.

## Source reading
**Full scan.** This is the 5th integrated item. I read all 30 files in `chapters/*.tex` in full:
- Appendices A, B, C, D, E, F, G, H, I, J, K, L.
- Chapters 01 to 18.

Digest status:
- The orchestrator reports the digest as CURRENT (chapters-hash f3d857ee3e3830f5).
- My own `--check` printed STALE, because the 007 integration (commit 6e5f56a) landed mid-review.
- The full scan makes the digest irrelevant.
- `git status` showed no modified chapters.

appH was read before the 007 change. I confirmed from the diff that 007 touched only one `\cite{BarvinskyVilkovisky1990}` in sec:status-N, far from the 005 anchor. The anchor-area lines (1646–1650) are unchanged. No unreadable files.

## Claim under review
**Claim.** The proposal adds one conditional paragraph to appH after the "What the two preceding results imply for Problem F" paragraph. It records a Presentation-A Poisson-limit computation:
- The scalar-sector identity √|G|(R_G/6 − E) = ρR[g_ρ]/6.
- The Θ-built metric G = η_AB e^A e^B.
- The connection-sector trace (4/6)ρR + ρ²X.
- The quadratic eigenvalues +1, −¼, −¾.
- New in r2: the cubic-order test showing ρ²X is not αρR[g_ρ] + βρ|∇lnρ|² modulo total derivatives.

**Original target.** The F original target is untouched by this proposal.

**Problem F, verbatim from appH L1106–1110.** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."

**Chapter 17.** The current criterion lists A, B, C, D1, E, F, G-derived and N. F is "CRITICAL PATH; OPEN". The proposal does not change this.

## Checks performed
**Scripts re-run.**
- `check_X_covariant_rewrite.py 40` gives:
  - Quadratic order: α = β = −4, residual 1.3e-15.
  - Cubic order: best fit (−3.55, −3.19), residual 0.316. These match the proposal.
- `check_X_covariant_sanity.py` gives:
  - Eigenvalues of x⁻¹h = (−¾, −¼, −¼) in both signatures.
  - Eigenvalues of x⁻¹r = (0, 0, ½).
  - B q = 0 exactly.
  - Residual 0.317 at fixed (−4, −4).

**My own check.** I wrote a scratch script at `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\4d0177a0-6b3d-45ad-bb6d-645d2be99f00\scratchpad\flat.py`.
- It reuses the researcher's jet algebra class, matrix inverse and Riemann code on a metric g = ψ*(constant η), which is flat. It runs on three random cubic samples.
- All Ricci-scalar coefficients vanish to 1e-12 or better, including the cubic mask 7. The relevant scale is about 1e4–1e5 for the Lagrangian coefficients.
- This is the key independent check. The quadratic order never tests the ΓΓ terms, the nilpotent inverse series (three terms) or the three-term log. A bug there could have faked the 0.32 residual, but the flat-metric test shows these are correct at cubic order.
- It does not independently test X or r. X is a direct contraction of ∂Θ. The sanity script's quadratic eigenvalues cross-check r and X.

**Is the cubic test sound?** Yes, as a counterexample within its class.
- ψ*ω̄ is closed and nondegenerate, so Θ is Poisson for any w.
- The ε₁ε₂ε₃ coefficient at Σp = 0 has an x-independent exponential factor of 1. Any ∂_a V^a with V built from the jets has coefficient i·P_total·V = 0. So the identity "X = αh + βr + ∂V" for any V, covariant or not, would force C_X = αC_h + βC_r for every sample.
- A global least-squares fit across 40 samples, in both signatures, with residual 0.32 versus 1e-15 at quadratic order, is far outside rounding error.
- The td column being zero is a trivial consistency check, as the proposal itself states.

**Is the candidate basis complete?** Adequate for the claim, with one caveat.
- g_ρ^{μν} = ρK is a tensor density with √|g_ρ| = 1, so its covariance is under unimodular diffeomorphisms.
- Under those, ρ is a scalar and the volume form is √g. The two-derivative scalar densities are f(ρ)R, f(ρ)|∇ρ|² and f(ρ)□ρ.
- □ρ is reducible by parts to |∇ρ|² modulo total derivatives.
- The scaling Θ → λΘ leaves g_ρ invariant, sends ρ → λ⁻²ρ, and sends ρ²X → λ⁻²ρ²X. This fixes f ∝ ρ for R and f ∝ ρ⁻¹ for |∇ρ|². Since the identity must hold for all λ, mixed-degree pieces separate.
- The manuscript sentence asserts this completeness without stating the group or the scaling argument (see finding m1).

**Total derivatives.** Handled correctly. At the cubic order used, they contribute exactly zero. The r2 note that the "td" entry is zero by construction is accurate.

**Is the scope statement accurate?** Yes.
- The block says rewritings using further structure, "such as the constant η, are not tested".
- It says "on this sample". It does not claim non-covariance in general, and it does not say "obstruction".
- It also does not claim non-existence of rewritings that use η, or of other sector contents.

**r1 findings re-verified.**
- F1: the sign sentence is adopted. It states the Maxwell-kernel coefficient on the TT-type modes and that the EH piece always has that sign. Closed.
- F2: the text says "differs from this one expression" and calls the result a conditional computation. Closed.
- F3: N_tot = N_s + 2, defined as an input count. Closed.
- F4(a): "At the sample points tested" now covers both clauses. Closed.
- F4(b): the scaffold-rotation statement is cited by content. Closed.
- F4(c): the symbol clash is resolved. The block uses ϑ₁, ϑ₂ for the Θ components and a^μ for the gauge potential. Closed.
- F4(d): Euclidean is stated. Closed.

**Anchors and labels.**
- The anchor sentence "…Presentation~A in general. No value or sign of G_eff follows. Problems~B, C, D and~F remain open." occurs exactly once, at L1646–1648.
- `\section{Problem G: HBEV}` occurs once, at L1650.
- All 11 referenced labels exist in the sources. The "2" count from my grep came from `.aux` copies.
- Each source `\label{…}` occurs once. I explicitly confirmed `thm:Geff`, `eq:O-eta` and `ass:emergent-op`.
- `\LUV` is an existing macro.
- No new label is introduced.
- The paragraph introduces no process language.

**Emergence and labels.** Θ, η and G are matrix-model objects. The block explicitly does not identify G with the emergent metric. No emergence violation. No label change.

**Not independently verified.**
- The −¼ and −¾ eigenvalues rest on the researcher's brute-force and FP scripts. I re-ran them in r1 and the sanity script reproduces them here.
- Literature: the block cites none, so none was checked.

## Findings
- **m1 (minor).**
  - Location: LaTeX "Beyond quadratic order", sentence "Modulo total derivatives, the scalar densities of weight ρ with two derivatives built covariantly from g_ρ and ρ are the combinations of …".
  - Finding: This is asserted as a fact. The justification (unimodular covariance and scaling in Θ) is in the proposal but not in the block.
  - Optional action: Say "under unimodular diffeomorphisms and the scaling Θ → λΘ". Alternatively soften the sentence to "the covariant candidates considered are …". The conclusion is already scoped to "on this sample", so this is not blocking.
- **m2 (minor).**
  - Location: closing line of the new paragraph.
  - Finding: "Problems~B, C, D and~F remain open." is identical to the closing line of the immediately preceding paragraph.
  - Optional action: Vary the wording, for example "Problem~F, and Problems~B, C and~D, remain open", or accept the repetition, which is common in appH.
- **m3 (informational).**
  - The block says "forty random samples" and "relative residual about 0.3". Both are accurate.
  - The residual is a global fit over all samples. A single sample cannot fail a 2-parameter fit.

## Scope of what is established
**Established identities (hand-checked and numerically checked).**
- √|G|(R_G/6 − E) = ρR[g_ρ]/6 for the Poisson-limit scalar operator.
- G = η_AB e^A e^B for e = η⁻¹Θ⁻¹.
- The connection-sector trace formula, given the stated quadratic action.
- The quadratic eigenvalues +1, −¼, −¾.

**Computed counterexample (double precision, 40 random samples, both signatures).**
- ρ²X is not equal, modulo total derivatives, to any αρR[g_ρ] + βρ|∇lnρ|² at cubic order.
- The quadratic coincidence α = β = −4 is specific to quadratic order.
- This is a sampled counterexample, not a symbolic proof.
- It applies within the (g_ρ, ρ)-covariant class.
- It is untested for rewritings that use η or other structure.

**Conditional on:**
- The Poisson limit with Moyal terms dropped.
- Bosonic 4D content.
- Background gauge.
- A diagonal heat kernel with a local cutoff.
- Euclidean signs.
- N_tot as an input.

**Not established.**
- `ass:emergent-op` is not discharged, and ⟨Φ⟩/v = coframe is not derived.
- No value or sign of G_eff follows.
- The F locked-block target is not computed.
- This is not a no-go.

**Relaxable hypotheses within the core** (named, not researched here):
- Fermionic and extra-scalar content.
- Moyal corrections at the cutoff.
- Non-minimal gauges.
- Φ–a^μ mixing.
- A presentation-B frame coupling.
- Rewritings using η.

**Labels.** F, A, B, C, D1, E, G-derived and N all remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. No label change is proposed, so there is no LABEL-CHANGE-PROPOSED flag.

**Milestone and breakthrough.** Routine conditional sub-lemma with a bounded sharpening of what the quadratic form can say. It derives no critical-path step (not M1) and excludes no route class (not M2). It is not a BREAKTHROUGH. Milestone: none.

**Significance.** Consequential within its scope. It resolves the r1 ambiguity that α = −4 would reproduce X at quadratic order, and it identifies the fate of X as the sharpest sub-question for the net EH coefficient. The package is coherent: one computation, one insertion, no unrelated claims.

## Recommended disposition
Integrate as-is, as the single new paragraph in `chapters/appH-microscopic-proofs.tex` immediately before `\section{Problem G: HBEV}` (L1650). The optional m1 and m2 tweaks may be applied at the integrator's discretion if the text is re-submitted with them. Otherwise integrate the r2 block exactly.

## Corrected snippet
None required. Optional m1 wording, which adds no new physics: replace "Modulo total derivatives, the scalar densities of weight \(\rho\) with two derivatives built covariantly from \(g_\rho\) and \(\rho\) are" with "Modulo total derivatives, under unimodular diffeomorphisms and the scaling \(\Theta\to\lambda\Theta\), the scalar densities of weight \(\rho\) with two derivatives built from \(g_\rho\) and \(\rho\) are". If applied, it must be re-reviewed as exact text.
