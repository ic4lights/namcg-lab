VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2

## Verdict
The central results hold: the closed form of g (checked independently), the growth law and asymptotics of the Zeeman-dressed character, the "model, not the leaf" scoping of the Landau paragraph, and the fact that the vector-Zeeman part qualifies rather than falsifies merged text. Two statements in the block must be corrected before integration:
- The claim that real-mass phases leave the growth exponent unchanged is false off the real axis.
- The "up to 40%" frame variation of the Maxwell part understates the quoted data.

## Source reading
- Digest and targeted reads. The digest is STALE (dirty working tree, as expected). Under 3(d) I read the affected passages directly: appH lines 2113-2173 in full (the 027, 028 and 030 blocks), the Problem E and F ledger labels, and the anchor region. I grepped all chapters for Landau/nilpotent usage and found no conflicting text.
- Not a full scan.
- Ordinal assumption: 033 lands first, so 032 is integrated item 31 and 3(a) does not apply. If 032 lands first it is item 30 and a full scan is owed. I did not do one, and I rely on 033's gatekeeper scan for that case. Because the block is append-only and changes no definition or status, I do not expect it to find a contradiction.
- 3(c) is not triggered: no existing text is made false, and no definition, assumption, status or scope passage is changed.

## Claim under review
- **Claim.** A bounded no-go for background-flux (Landau/nilpotent) resummation as an infrared cutoff, in the CP^{1,2} four-matrix class (Poisson limit, one loop, leading nilpotent symbol, Lorentzian iε, 028 content), plus an exact g(a,b) and a Landau-model Einstein–Hilbert sector.
- **Problem F** (appH label, verbatim): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- **Problem E** (appH label, verbatim): "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
- No label is touched.

## Checks performed
1. **g(a,b), my own code** (mpmath, ray integral with the 1/s² tail added back, versus the closed form): agreement to about 1e-6 at (0.83, 1.21, θ=0.4) and (2.1, 0.37, θ=1.1). That is the limit set by my lower cutoff 1e-6, not by the formula. At (1,1, θ=0.7) it agrees to about 1e-18. Different rays give the same value.
   - I re-ran `s2`: 1e-24 agreement, homogeneity, and Re g, Im g < 0 for all r, with the limits −a ln 2 and −b ln 2.
   - S(r) < 0 because the alternating series has a decreasing first term.
   - g is finite and ray independent in the open fourth quadrant. The poles lie on the boundary axes, and the decay rate a cosθ + b sinθ ≥ min(a,b) > 0.
2. **Θ.** The normalisation −i/(16π²s²) is re-derived by hand from the free Gaussian integral. I re-ran `s1`: KMS, d ln Θ/ds, and the Landau-level sum all agree.
3. **Character.** I re-derived the asymptotic by hand: Θχ_str → (ab/π²) sinh²[s(a−ib)/2], whose constant term is −ab/(2π²). On θ* = arctan(a/b) the cosh part is purely oscillatory.
   - The ray growth rate |a cosθ − b sinθ| is confirmed.
   - The log slope −0.032 per doubling follows from ab·ln2/(2π²) at (0.7, 1.3).
   - The same rate holds for Θ(χ_V − 4).
4. **Mass-phase claim (new check, my own code).** The measured slope on a ray equals |a cosθ − b sinθ| − m sinθ. At θ=0.8 and m=+1 the slope is −0.27 (convergent). At m=−3 it is +2.6. The block's "unchanged by real-mass phases" therefore holds only on the real axis (see finding 1).
5. **Re-run:** `s3`, `s5` (checks A–E pass), and `s7` output files. I did not re-run one `s7` frame (about 80 s) myself; I read its saved output.
6. **Numbers.** The Fin/c real parts are 7.57, 8.09, 6.79 and 7.61, 5.90, 7.33, as quoted. The spreads are about 17%, 22% and 10%, so "10–20%" is acceptable. The imaginary parts are not quoted (finding 3). The Hessian residuals are 0.987, 0.822 (f_e/f_m = 0.36) and 0.742, 0.399 (0.735), so "0.4–1.0" is correct. Both signs of the eigenvalues occur, though the one positive Re eigenvalue is small (0.02–0.04).
7. **Block identity and compile.** `block-r1.tex` is identical to the block in the proposal. It contains no TAB, no non-ASCII characters and no CR (the integrator must convert to CRLF). The compile check passes: 295 pages, 0 undefined, 0 multiply-defined. The "double subscripts: 1" hit is a false positive (`\sum_iw_im_i`).
8. **Anchor.** `\section{Problem G: HBEV}` occurs once (line 2174), immediately after the 030 block, which ends "…Problem~F remains open." The label `ch:vierbein-emergence` exists in ch04. No new labels or cites.
9. **Literature.** No citations in the block. The Bastianelli–Davila–Schubert pointer is not used and not verified.

## Findings

### 1. Real-mass phases (major)
- **Location:** Order-F⁴ paragraph, "the exponent is unchanged by the phases e^{-ism_i} of real masses, and it vanishes only on the single ray θ*"; also "No ray gives a convergent integral". The same claim is in Result item 4 and `s3_character.py` line 7. `s3` never tests it.
- **Finding:** On the ray s = |s|e^{-iθ}, |e^{-ism}| = e^{-m|s| sinθ}, so a mass m shifts the rate by −m sinθ. This is false for θ > 0; it holds only on the real axis. A positive mass-squared would open a window of convergent rays around θ*. For the vector with μ² = −3 the shift is +3 sinθ, so the rate |a cosθ − b sinθ| + 3 sinθ is positive on every ray and the no-go survives for the actual content.
- **Required action:** Correct the sentence, and restrict "no ray gives a convergent integral" to the massless character term and the rays of the closed fourth quadrant. Snippet (no new physics beyond the one-line shift derived above):
  "…the exponent is unchanged by the phases \(\mathrm e^{-\mathrm ism_i}\) of real masses on the real axis; on a ray of angle \(\vartheta\) a mass \(m\) shifts it by \(-m\sin\vartheta\), so for the vector with \(\mu^2=-3\) the rate is \(|a\cos\vartheta-b\sin\vartheta|+3\sin\vartheta>0\) on every ray, whereas a positive mass-squared would open a window of convergent rays about \(\vartheta_*\) for the massless term treated here."
- Add "of the closed fourth quadrant" to "No ray gives a convergent integral". Rays of the first quadrant correspond to the opposite iε prescription, and in this block they are neither claimed nor excluded.

### 2. "Up to 40%" frame variation (major)
- **Location:** Landau EH paragraph, "the Maxwell part of the same sector changes by up to 40% between frames".
- **Finding:** `s7` gives int T2_Maxwell (pair 1, frames 0, 1, 2): −1.36e-3−1.7e-4i, −9.7e-4−1.8e-4i, −1.375e-3−5e-6i. The largest relative change is about 32–45%. Pair 2 (1.919, 1.0): −1.3e-4−9.3e-4i, −1.20e-3−5.7e-4i, −3.2e-4−8.4e-4i. The largest relative change is about 85–120%. The quoted bound is wrong for the second pair.
- **Required action:** Replace the bound with "by about 30–45% at the first pair and by order unity at the second (complex values)", or quote the values.

### 3. Fin/c presentation (minor)
- **Location:** Landau EH paragraph, the Fin/c values.
- **Finding:** Fin/c is complex, with imaginary parts up to 1.3 at (1.92, 1.0), which the block omits. Only the real parts are quoted.
- **Required action:** Quote the real parts as real parts and note the imaginary parts.
- **Finding:** "Of the size of the logarithm" is unit dependent, since Fin/c shifts by ln λ under rescaling.
- **Required action:** Say that the frame variation at fixed (a, b), with A fixed, is the meaningful statement.

### 4. Provenance and scope of the "Dependence on A" paragraph (minor)
- **Location:** "Dependence on A" paragraph.
- **Finding:** The Hessian result concerns the M_str coefficient only, since the vector-Zeeman part has no contour. The paragraph does not say so.
- **Finding:** The statement that central Y leaves the frame determinant unchanged depends on the frozen nilpotent frame, in which Y commutes with W. The block gives the Jacobi-fixed non-commutation only in the Landau paragraph, without saying that it applies equally to 030's "ζ commuting with everything".
- **Finding:** "Neither covariant nor sign-definite" is loose. The Hessian of g(F) is built covariantly from F, κ and α. What is shown is that it is not of the covariant Maxwell form (the residual of the fit to G is 0.4–1.0), and the leaf average is noncovariant.
- **Required action:** Add "of the \(M_{\mathrm{str}}\) term", add "the same omission is made in the preceding paragraph" to the Landau sentence, and replace "neither covariant" by "not of the covariant Maxwell form".

### 5. Naming (minor)
- **Finding:** "Order-F⁴ term" names what is the whole massless resummed character term, which starts at order F⁴.
- **Required action:** Rename accordingly.

### 6. Statement in Research, not in the block (minor)
- **Finding:** Research says "in the upper half plane Θ itself grows". That is wrong: the closed form decays there. The first quadrant is simply the opposite iε prescription (s+i0), not admissible. The block does not repeat this.
- **Required action:** Do not carry it into the manuscript.

### 7. 030 sentence "which cuts off large s in the full leaf" (minor)
- **Finding:** The sentence is true for the M_str term and is only qualified by the new completeness paragraph.
- **Required action:** None, provided the "Completeness" paragraph stays. The proposal's "stale passages: none" is accurate in substance.

## Point-by-point answers to the task's points
1. **Landau-resummed mass-supertrace term.** The closed form of g is verified, finite and contour-robust within the open fourth quadrant (my own code), and Re g, Im g < 0. This is established for the stated integrand.
2. **Vector-Zeeman part.**
   - M_str is the zero-Z-insertion term only. The complete mass-linear term is i∫ds Θ[M_str + μ²(χ_V − 4)]. The growth is |a cosθ − b sinθ|, from Zeeman e^{2x} against orbital e^{-x}, verified.
   - 028 already lists the vector-mass constant Σ w_i m_i tr Σ_iΣ_i, and 027 already states that the Zeeman growth is not removed by a fibre bound.
   - 027's "weight-two coefficient = M_str × j(a), Re j > 0" is a statement at weight two, where the mass times Z² is weight four. It is scoped, not false.
   - So the new paragraph qualifies the 027/028 sentences and falsifies nothing. No PRIOR-CLAIM-ERROR, and the 3(c) full scan is not triggered by falsity.
3. **Zeeman-dressed character (the block's "order-F⁴" term).** The asymptotics and the constant −f_e f_m/(2π²) are verified. A bounded real-axis iε contour does not exist for the massless term (growth rate a). The correct statement about masses is finding 1.
4. **Leading symbol.**
   - The structural argument that A enters only through the centre-valued flux, with a Hessian of g, is acceptable as conditional on the frozen nilpotent frame (central Y).
   - On the leaf [W_a, Y] = −q_a Ham(y⁴) ≠ 0, which I confirmed from the so(4,2) bracket {M^{a4}, M^{μ5}} ∝ η^{aμ}M^{45}.
   - The leaf-average indefiniteness and non-Maxwell form are numerical at four points, with two points marginal; the proposal says so.
5. **Landau-model EH sector.** The block states "a model and not the leaf" explicitly, twice. The reproduction of 030's A at F=0 (c₁/A = i to 1e-8) is a consistency check of the engine against 030's own model, not an independent confirmation of A on the leaf. The coefficient A/16π² of ds/s is flux independent. This is automatic, because the flux enters at higher order in s, and the identification as the window-to-flux-scale logarithm is consistent.
   - The omission of [W_a, Y] makes 030's A model-scoped. 030 states "ζ commuting with everything" as the sector assumption and scopes its result to the frozen first jet. This is not materially false, but the new commutator is of order q¹ and so is not obviously suppressed by q-counting. It is open avenue 1, and finding 4 asks for a one-clause disclosure.
6. **Hedging.** No sign of G_eff is given and no Wick-rotation claim is made. The hypotheses and the class are explicit, and no induced form is identified with the emergent metric. Emergence is preserved.
7. **Anchor.** Unique and correct, and the characters are clean (see check 7).

## Scope of what is established
- **Proved or derived, for the stated integrand:** the closed form of g and its signs and homogeneity (numerically confirmed independently; not proved analytically); the Θ identity; the growth law and the asymptotic form of the character; the logarithmic divergence of the real part at θ*.
- **Conditional:**
  - The leading-symbol Hessian structure, conditional on the frozen nilpotent frame.
  - The Landau EH model (a scalar covariant 4D model with Y central), with the sampled Fin/c values.
  - The leaf-averaged non-Maxwell form at four points.
- **Class of the no-go:** Poisson limit, one loop, leading nilpotent symbol with constant flux at the centre variable, Lorentzian iε proper time, 028 content with μ² = −3, massless character term, sampled points.
- **Not covered by the no-go:** the next-to-leading symbol with the exact [W_a, Y]; spectral definitions; positive mass-squared stabilisation; non-perturbative masses; the transverse-flux 10D character, which was not computed; and Moyal terms.
- **Label status:** PROGRAMME-CONDITIONAL, F and E still OPEN.

**Open avenues, ranked by my judgement of promise:**
1. Next-to-leading symbol with the Jacobi-consistent [W_a, Y] and flux resummation. It is the true leaf analogue of the Landau model, and it tests whether A survives (the strongest lead).
2. Spectral, mode-by-mode definition of the vector sector with complex eigenvalues λ ± 2if_e, avoiding the proper-time contour.
3. A covariant window to remove the orientation dependence of Fin. Also a resummation of the mass-linear term with the vector mass kept positive or non-perturbative (note that the real-mass phase opens a convergent window only for positive m, whereas μ² = −3). Pauli–Sakharov completion belongs here.
4. Fermion mass patterns (M_str = 0 plane), which still leave the vector Zeeman part.
5. Transverse flux and fuzzy K.
6. Moyal and bilocal checks.

## Recommended disposition
Revise: apply findings 1 and 2 (required), findings 3–5 (minor wording), then integrate. The package is coherent (one class, one sequence of results). Its significance is a decisive bounded obstruction: the Lorentzian iε contour cannot define the resummed massless character term, and the IR-finite Landau-model Fin is frame dependent. It is not a breakthrough.

## Corrected snippet
Only for finding 1 (given above). For finding 2:
"…and the Maxwell part of the same sector changes between frames by about \(30\)–\(45\%\) at \((a,b)=(0.7,1.3)\) and by a factor of order one at \((1.92,1.0)\)…"

Files: `C:\Users\redgi\Projects\namcg-lab\proposals\032-landau-resummation\proposal-r1.md`, `block-r1.tex`. My scratch checks: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\4d0177a0-6b3d-45ad-bb6d-645d2be99f00\scratchpad\g.py`.
