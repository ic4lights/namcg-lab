VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: PRIOR-CLAIM-ERROR, AUTHOR-DECISION | PROGRESS: first | OPEN: 0/1

## Verdict
The central algebra is correct and I re-derived it independently: the basis change, the induced coefficients, the spin projections, the pole masses, Υ, the Lambert-W zeros and Υ_*(0)=π/2. But the proposed LaTeX states the fixed-L pole location ("ghost below Λ_UV once Λ_UV/μ>e^5") as a result. That pole always lies where, by the package's own argument, the fixed-L form does not apply. This needs one major wording revision before integration.

## Source reading
**Full scan.** It was required because the package edits the Problem N Status passage (CLAUDE.md rule 3(c)).
- Digest: `python scripts/make_digest.py --check` printed DIGEST CURRENT. chapters-hash d3558e44b583da45, dirty-chapters: no.
- I read all 30 current chapter files in full: ch01–ch18 and appA–appL. appH was read in four ranges covering lines 1–1869.
- No file was unreadable.
- Also read: bib/namcg.bib (Vassilevich2003, Stelle1977), MILESTONE.md, reports/ledger.md (empty), and the proposal folder.

## Claim under review
**Claim.** Inside the truncated identity of Thm `thm:Geff` with common limits and the stated continuation:
- The induced Weyl coefficient is c_W = W_C·L/(32π²).
- The extra spin-2 pole is at m_2² = −Υ·Λ_UV²/L, with Υ = π/(G_eff·W_C·Λ_UV²). It is a tachyonic ghost if G_eff·W_C > 0.
- If G comes from a_1 alone, Υ = A_1/(2W_C). This equals 10 for minimal real scalars.
- In a leading-log form-factor model F(x) = 1 − (x/Υ)(ln(1/x)+δ_W), there is no zero in |x|<1 iff Υ > Υ_*(δ_W), with Υ_*(0) = π/2.
- N is not claimed closed.

**Original target** (Ch.17 lines 497–513; criterion item lines 724–728). Derive from the matrix path integral that the graviton two-point function has no propagating Ostrogradsky ghost for p<Λ_UV, for the Problem-F values of α and G_eff, and state the region where this holds.

**Appendix H ledger label, quoted verbatim:**
- Problem N: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL." Ch.17 agrees: "CRITICAL PATH for the matrix-derived label; OPEN."
- Problem F (dependency): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."

The current critical-path set is A, B, C, D1, E, F, G-derived, N. I found no discrepancy between Ch.17 and Appendix H. No label change is proposed.

## Checks performed
**Algebra re-derived by hand or with sympy in my scratchpad:**
- Basis change: Riem²−Ric² = (3/2)C² − (1/2)E_GB + 0·R². So (Riem²−Ric²)/180 = C²/120 − E_GB/360.
- The R² coefficient for E=E_0+QR is (1/2)(1/6−Q)², consistent with eq:appA-a2 (+E²/2 − RE/6).
- Continuation: S_E = −∫L_L applied to curvature scalars gives 1/(16πG) = A_1·Λ_UV²/(32π²). This reproduces appH "Sector sum" (1/G = N_0·Λ_UV²/(12π)) and the appA vacuum sign. It also gives c_W = W_C·L/(32π²) > 0. The relative sign of the R and C² coefficients does not depend on the overall continuation sign (confirmed).

**Spin projections:**
- TT: ∫C² → (1/2)k⁴ h·h, and the EH term gives −k²/(64πG). The spin-2 coefficient is −(k²/64πG)(1 − 32πG·c_W·k²).
- Spin-0: R^(1) = k²θ·h gives 3c_R·k⁴·hP0h. The spin-0 coefficient is (k²/32πG)(1 + 96πG·c_R·k²).
- Residue signs agree with the proposal. The Stelle check gives m² = 1/(16πGα).
- Υ = 10 and m_0² = 2Λ_UV²/L for minimal scalars.

**Form factor and disc criterion:**
- ∫ds/s∫dτ e^{−τ(1−τ)sk²} − ln(Λ_UV²/k²) → −γ − ∫ln(τ(1−τ)) = 2−γ_E exactly (analytic).
- Lambert inversion: x = −Υ/W_j(−Υe^{−δ}) (verified).
- On |x|=1 the zero condition is (δ−iθ)e^{iθ} = Υ. For δ≥1 its only solution is θ=0, Υ=δ. For δ=0 it is θ=±π/2, Υ=π/2.
- F ≠ 0 on both sides of the branch cut, F → 1 at x=0, and F has no zeros in the slit disc for large Υ. So "Υ>Υ_* ⇒ no zero in the disc" is in fact provable. The converse remains numerical.
- My crossing computation gives Υ_*(−9.58458) = 10.000, Υ_*(−10) = 10.40, Υ_*(−1) = 2.26, Υ_*(0.9) = 1.05. These confirm the LaTeX window −9.58 < δ_W < 10 and |x| ≈ 3.935.

**Scripts:** I re-ran all three researcher scripts into my scratchpad. Their output is byte-identical to the saved `*.out.txt` files (CRLF stripped).

**Anchors:** "and no stronger." (appH:1857), "No computation is recorded" (appH:1860) and "undetermined here." (ch09:126) each occur exactly once. The proposed labels exist. The new symbols do not clash with existing chapter symbols. Both target files are ASCII with CRLF.

**Citation:** Crossref confirms Barvinsky & Vilkovisky, NPB 333(2) 471–511 (1990), DOI 10.1016/0550-3213(90)90047-H, title "Covariant perturbation theory (II). Second order in the curvature. General algorithms". The attributed general claim (second-order curvature terms are nonlocal form factors) is consistent with the title. The decay property is not independently verified; the text correctly states it as an assumption.

**Not verified:** no LaTeX build was run by me or by the researcher.

## Findings
1. **Major — appH block, first paragraph ("the ghost lies below Λ_UV once Λ_UV/μ>e^5" and "compositeness ... does not by itself place the extra spin-two pole above Λ_UV: its position ... fixed by ... L").**
   - Finding: |m_2|²/μ² = Υ·e^L/L ≫ 1 always. The fixed-L pole therefore always sits at |k| ≫ μ, which is exactly where the block's second paragraph says the fixed-L form "is not the one-loop result". Within the same package, the refined model with Υ=10 has no zero in the disc for −9.58 < δ_W < 10, the opposite conclusion.
   - Reason: as written, the first paragraph presents an artefact of an inconsistently applied truncation as a consequence. Read next to Ch.16 lines 139–143 (a ghost below Λ_UV is a killer), it overstates. The proposal's suggested "no-go" (M2) rests on this.
   - Required action: say explicitly that the fixed-L pole is a property of that form, not a one-loop prediction. Restrict the (L/Υ)k²/Λ_UV² statement to |k| ≲ μ. Support "not implied by compositeness" only through the form-factor model (zeros inside the disc for Υ < Υ_*(δ_W)). See the corrected snippet.
2. **Minor — closing sentence of the block ("Within this truncation, absence of a ghost pole below Λ_UV is a numerical condition...").** At |x| ~ 1 the neglected O(k²/Λ_UV²) form-factor terms are the same order as δ_W. The condition belongs to the leading-log model F, not to the truncation. Required: say "within the leading-logarithmic model F".
3. **Minor — "on a flat background".** Flat space solves the equations only if the vacuum term ρ_Λ (nonzero for massless sectors) is cancelled or neglected. Required: state this, as Ch.9 ECG item 2 does.
4. **Minor — continuation attribution.** Appendix A fixes only S_E = −iS_L and the vacuum term. Continuing curvature invariants without a sign change is an added convention (the appH Sector-sum paragraph calls it "a convention to be checked"). Required: phrase it as an added convention, not as "the continuation of Appendix A".
5. **Minor — consecutive status lines.** The block ends "Problems F and N remain open." and is immediately followed by the rewritten Status paragraph. Smallest fix: delete the stale sentence "No computation is recorded." rather than replace it, so Status reads "Remains Assumption~\ref{ass:EFT-a2}."
6. **Minor — "not k²/Λ_UV²".** This overstates. Write "k²/Λ_UV² multiplied by L/Υ".
7. **Minor (record only, not in the LaTeX).** The Υ_* table in proposal R4 has grid overshoots: −1 → 2.26 (not 2.27), −10 → 10.40, 0.9 → 1.05.
8. **Minor — process.** `\cite{Barvinsky1990}` needs an edit to bib/namcg.bib, which is outside `chapters/`. The author must authorise that edit, or the citation must be dropped. Use DOI-free style (`pages = {471}`) to match existing entries if wanted.
9. **PRIOR-CLAIM-ERROR (minor, non-load-bearing) — chapters/appK-endomorphism.tex line 17.** It gives a_1 = tr(E) − (1/6)R·dim for Δ = −D²+E. That is the opposite overall sign to eq:appA-a1 and eq:a0a1 (a_1 = tr(R/6 − E)), which is the standard value for this operator convention. The merged equation is wrong in sign. Its conclusion δa_1 = 0 is unaffected. Under MILESTONE.md, sign corrections to non-load-bearing text are routine, so I do not classify this as M3. The author should be told; it needs a separate one-line correction item.
10. **AUTHOR-DECISION — notation.** α is overloaded in more places than the three the researcher lists: eq:W-again-9 / eq:W-through-2; eq:stelle; the ECG coupling (ch09:236, appH Problem J); the Fierz–Pauli mass parameter (ch07:79, 423); ν_exp (appE:98); and the per-galaxy fit parameter (ch17:572, 626). The N target text "values of α ... computed in Problem F" is ambiguous. This is not an error. Whether to restate N in terms of c_W/c_R or Υ, and whether to qualify the "(p/Λ_UV)²" wording of `ass:EFT-a2`, are author wording choices.

## Scope of what is established
- **Established identities:** the C²/E_GB/R² decomposition; the spin-2 and spin-0 quadratic forms; m_2² = −1/(32πG·c_W) and m_0² = 1/(96πG·c_R); residue signs; the Lambert zero formula; Υ_*(0) = π/2; Υ_*(δ) = δ for δ ≥ 1, including uniqueness of the crossing; the 2−γ_E constant.
- **Conditional** (truncated identity, common limits, added continuation convention, flat vacuum): c_W, c_R, G_eff and Υ = A_1/(2W_C); Υ = 10 for minimal scalars.
- **Conditional / model:** the L → ln(Λ_UV²/k²) + δ_W replacement, where the decay of the Weyl form factor is assumed. The disc criterion is a property of the leading-log model F.
- **Numerical:** the Υ_*(δ) table and the necessity direction of the criterion.
- **Open:** W_C, A_1, G_eff and δ_W for the locked block; massive thresholds; control at |k| ~ Λ_UV; any derivation from the matrix path integral.
- The package is PROGRAMME-CONDITIONAL. Problem N stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL, and F stays OPEN.
- Significance: a useful sharpening of N's missing step into an explicit (Υ, δ_W) condition, plus the observation that Υ does not depend on Λ_UV for induced G. It is not a milestone. M1 does not apply (nothing is derived from the matrix theory). M2 does not apply: the "no-go" rests on the fixed-L artefact, and Ch.9 and appH already say the pole's position relative to Λ_UV depends on the Problem-F values. The bundled items (appH block, Status sentence, optional Ch.9 qualifier, bib entry) share one derivation and belong together.

## Recommended disposition
Revise, then integrate.
- Apply findings 1–6 (snippet below).
- Item 3 (the Ch.9 qualifier) is mathematically correct and may be integrated as proposed.
- Run `python scripts/build_check.py` at integration.
- Resolve the bib-edit permission (finding 8).
- Record the appK sign error (finding 9) for the author as a separate item.

## Corrected snippet
No new physics. One added explicit assumption: the vacuum term is cancelled or neglected.

In paragraph 1, change "Work in the truncated identity of Theorem~\ref{thm:Geff} on a flat background, ... with the continuation of Appendix~\ref{app:seeley-dewitt} (\(S_E=-iS_L\), curvature invariants continued without change of sign)" to:
```latex
Work in the truncated identity of Theorem~\ref{thm:Geff}, expanded about
a flat background with the vacuum term cancelled or neglected so that
flat space is a solution, with every included sector assigned the common
limits \(\LUV,\mu\), \(\mu\ll\LUV\), with \(S_E=-iS_L\) as in
Appendix~\ref{app:seeley-dewitt}, and with curvature invariants
continued without change of sign (an added convention).
```
Replace from "the ghost lies below \(\LUV\) once ..." to the end of paragraph 1 with:
```latex
\(|m_2|<\LUV\) in this fixed-\(L\) form once \(\LUV/\mu>e^{5}\), and
\(m_0^2=2\LUV^2/L\). Since \(|m_2|^2/\mu^2=\Upsilon e^{L}/L\gg1\), this
pole lies at momenta where the fixed-\(L\) form does not apply (see
below); it is a property of that form, not a one-loop prediction. For
\(|k|\lesssim\mu\), where the fixed-\(L\) form applies, the Weyl
correction relative to the Einstein term is
\(32\pi G_{\mathrm{eff}}c_Wk^2=(L/\Upsilon)\,k^2/\LUV^2\).
```
Replace the last two sentences of the block with:
```latex
Within the leading-logarithmic model \(F\), absence of a zero in
\(|k^2|<\LUV^2\) is a numerical condition on \(\Upsilon\) and
\(\delta_W\), which are outputs of Problem~F, and is not implied by the
metric being composite. Problems~F and~N remain open.
```
Status paragraph: delete only "No computation is recorded.", leaving "Remains Assumption~\ref{ass:EFT-a2}."

**Relevant files:**
- C:\Users\redgi\Projects\namcg-lab\proposals\002-auto-target\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (lines 1836–1860)
- C:\Users\redgi\Projects\namcg-lab\chapters\ch09-ultraviolet.tex (lines 108–145)
- C:\Users\redgi\Projects\namcg-lab\chapters\appK-endomorphism.tex (line 17)
- C:\Users\redgi\Projects\namcg-lab\chapters\ch16-falsifiers.tex (lines 139–143)
- My verification script: C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\4d0177a0-6b3d-45ad-bb6d-645d2be99f00\scratchpad\gk_check.py
