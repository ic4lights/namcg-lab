VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
F1–F4 are applied correctly and nothing else changed, so the block is accepted for integration.

## Source reading
Digest + targeted reads. I did not run a full scan, and none is claimed. appH is dirty with the expected uncommitted integrations, so I read the anchor region of `chapters/appH-microscopic-proofs.tex` directly. I did not re-read Chapter 17 or Appendix H this round. The F and E statuses are taken from the r1 review and the 028 block, and this package changes no label.

## Claim under review
- **Claim:** a bounded no-go, with a conditional Einstein–Hilbert-form limit, for the next-to-leading symbol of the mass-supertrace term at order ε². It is stated for the 028 class.
- **Statuses:** Problem F, `OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL`. Problem E, `OPEN, CRITICAL PATH for the matrix-derived label`. Neither changes.
- **Not claimed:** no finite coefficient, no sign of G_eff, no identification with the emergent metric.

## Checks performed
- **Diff of proposal r1 against r2.**
  - Header and changelog.
  - Body wording for F1–F4, with the class sentence matching the block.
  - The ranked avenues list.
  - Nothing else changed.
- **Diff of block-r1.tex against block-r2.tex.** Only lines 6 and 10 differ. These are exactly the F1–F4 edits:
  - (i) "10^-8 or better".
  - (i) "expected ... non-uniform ... (a mass insertion into the massless non-kernel propagator; not computed)".
  - (iii) the phase-averaged FP form plus the dilaton term.
  - (iv) c_θ, "a scalar function of the orbit point" and "machine precision".
- **FP algebra.** (1/24)[v²((q·a)²−q²a²)+q²(a·v)²] − (1/8)q²(a·v)² = (1/24)[v²((q·a)²−q²a²) − 2q²(a·v)²] = A. This is correct, and the decomposition is now gauge invariant.
- **Re-run of `check_fp_r2.py`.** Residuals are at most 1.8e-15, so the sum equals A. This is a numerical check of the algebra, not a proof. I confirmed the algebra by hand.
- **Block identity.** The latex block in proposal-r2.md equals `block-r2.tex` (CR-insensitive comparison), and the file has 0 TAB characters.
- **Anchor.**
  - `\section{Problem G: HBEV}` occurs exactly once.
  - It is immediately preceded by the 028 block, ending "...Problem~F remains open.\r\n\r\n".
  - The new paragraph heading is not yet present in appH.
- **Labels.** The block uses only `ch:vierbein-emergence`, which exists once, in ch04. There are no new labels, no citations and no bib changes.
- **Compile check.** I did not re-run it. I read the researcher's `compile_check_r2.out.txt` claim (0 errors, 0 undefined, 0 multiply defined). The integrator must run `scripts/build_check.py`.

## Findings
None. F1–F4 from r1 are closed.

## Scope of what is established
- **Class of the no-go.** Poisson limit, one loop, CP^{1,2} four-matrix class, μ²=−3, supplied IKKT content with no bilinear fermion mass, one species-independent Gaussian window of Δ_{3/4}, formal expansion, frozen first jet and constant window symbol, first-order mass term.
- **Established or checked.**
  - The symbol recursion, validated three ways. These checks were verified in r1, and the scripts are unchanged.
  - c0 equals the Maxwell coefficient to 1e-8 or better. This is a sampled numerical result.
  - The linear s-divergence of c0. The non-uniformity of the derivative expansion is only expected and not computed.
  - c1 is non-invariant and non-covariant for the actual window. This is numerical and sampled.
- **Conditional.** The f→0 limit of c1 equals λ1·A, with A the Fierz–Pauli plus dilaton second variation. This is numerical, with error O(f).
- **Numerical, one base point.** Fibre-average non-covariance.
- **Conjecture or unresolved.** Pauli–Sakharov completion, the sign of G_eff, and the map to the emergent metric.
- **Labels.** F and E remain OPEN and PROGRAMME-CONDITIONAL. No label change. Spacetime remains emergent.
- **Open avenues, ranked.** These are as in the proposal and I endorse them.
  1. Background-flux (Landau/nilpotent) resummation as an infrared cutoff of the c0 divergence. This relaxes the first-order mass expansion and the frozen background.
  2. A gauge/diffeo-covariant window.
  3. Non-perturbative masses and the Pauli–Sakharov completion.
  4. Fermion mass patterns, including the M_str=0 plane.
  5. The exact non-expanded Hessian.
  6. Relaxing the frozen jet and constant window symbol.
  7. Transverse flux K.

## Recommended disposition
Integrate as-is. This is ordinal 28 or 29, depending on whether 031 lands first. Accepted exactly:
- The single `\paragraph{Conjugate-coordinate class: ...}` block with `\emph{...}` sub-parts in `block-r2.tex`.
- Insertion immediately before `\section{Problem G: HBEV}`, after the 028 block.
- No other file and no label change.
- CRLF line endings preserved. The block has no tabs.

## Corrected snippet
None needed.
