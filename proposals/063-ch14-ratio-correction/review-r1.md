VERDICT: ACCEPT | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: first | OPEN: 0/0

## Verdict
The merged claim at ch14:243–258 is false. With the chapter's own eq:Fdiss, Assumption ass:drag (η constant on a given inspiral), eq:Pent and eq:Peters on a circular Newtonian orbit, P_ent/P_GW = (5/32)η/(G³M²μ), which does not depend on d. I re-derived the replacement text and the edited exercise independently and they are correct. The text is scoped to the reduced Newtonian/quadrupole model, the anchors are unique, the LaTeX builds, and no label or status changes.

## Source reading
Digest + targeted reads. This is not a full scan.
- `python scripts/make_digest.py --check` printed `DIGEST CURRENT` (head 4eb4b3a, tree-hash c47cd614ceaf8d55). `dirty-chapters: yes` comes from the uncommitted appH and bib changes (061/062). Those are accepted integrations and are expected under the 2026-10-15 directive. I read the affected appH passage (sec:status-I) in the working tree. ch14 in the working tree equals HEAD, sha256 d6883ca3…2d36, which matches the baseline.
- Read in full: `chapters/ch14-dissipation.tex` (all 398 lines); appH sec:status-I (lines 2929–3059); ch17:578–597 and 738–751; ch16:205–330 (this covers 220–222, 258 and 286–313); ch15:160–300 (this covers 169 and 289–292); ch13:398–410; ch11:200–224 and 355–374; ch01:106–115 and 258–271; MILESTONE.md triggers; ledger line 537.
- Greps over all `chapters/*.tex`: `eq:Pent`, `eq:ratio`, `P_{\mathrm{ent}}`, "wide separation", `chirp`, `Peters`, `drag|dissipat|quadrupole|sec:ch14-quad|eq:Fdiss|ass:drag` (154 hits in 16 files), and `\mathcal M`. Every hit that bears on the GW comparison or on separation scaling was read in context, as listed above. The remaining hits are generic "phenomenological drag, not derived" statements (appB, appC, appF, appJ, ch02, ch06, ch10, ch18) and make no claim about the ratio.
- **Scan ruling (CLAUDE.md 3(c)).** No full scan is required.
  - Block 1 replaces a derived physics statement; the assumption it rests on (ass:drag) is untouched. Block 2 edits an exercise. Neither block changes a definition, an assumption, a scope statement or a status passage, so 3(c) does not fire.
  - 3(a) does not apply: this is ordinal 61 and the next 5th-item scan is at 65.
  - 3(d) does not apply: the digest is current, and the dirty files are unrelated to this edit and were read where relevant.
  - The ordinal-60 full scan read ch14 at these exact bytes. No file was unreadable.

## Claim under review
- **Claim.**
  - ch14:243–258 states that P_ent/P_GW carries "a positive power of d" and grows toward wide separations at fixed η. That statement is false.
  - The correct result is the d-independent ratio (5/32)η/(G³M²μ). For a drag falling as d^{-n} the ratio scales as d^{4−n}.
  - The extra loss is degenerate, in the leading-order frequency evolution of the reduced model, with the chirp-mass rescaling 𝓜 → (1+R)^{3/5}𝓜.
  - The exercise "Energy identity" is corrected to match: P_ent/|dU_N/dt| = (5/64)η/(G³M²μ).
- **Original target.** Problem I is untouched by this package: derive Γ_ij(r; ℓ_A, ℓ_B) from microscopic dynamics. Appendix H sec:status-I, verbatim: "Status: OPEN. Priority: OPTIONAL falsifiable phenomenological extension; prerequisite only if drag is claimed as derived or predicted. Completion: PROGRAMME-CONDITIONAL."
- **Chapter 17 agreement.** ch17:582: "OPEN; OPTIONAL falsifiable phenomenological extension." ch17:744–747 keeps H, I and J optional. There is no discrepancy between appH and ch17. No critical-path problem is affected.

## Checks performed
1. **Ratio, derived by hand.**
   - P_ent = ημv²/d⁴ = ημGM/d⁵.
   - P_GW = (32/5)Gμ²d⁴Ω⁶ = (32/5)Gμ²d⁴(GM)³d⁻⁹ = (32/5)G⁴μ²M³/d⁵.
   - Ratio = (5/32)η/(G³M²μ), so ∂_d(ratio) = 0.
   - Dimensions with c restored: [η] = L⁴/T, and G³M²μ/c⁵ = (GM/c²)³ · c also has units L⁴/T. The ratio is dimensionless (it is ηc⁵/(G³M²μ) in SI form), so the old prefactor was right and only the factor (d/GM)^k was wrong, with k = 0.
2. **Exponent n.** F = −ημv/d^n gives P_ent = ημGM/d^{n+1}, so the ratio is ∝ d^{5−(n+1)} = d^{4−n}. It grows outward only for n < 4. This agrees with ch11 eq:airrev, which keeps n general.
3. **Exercise ratio along a Peters inspiral.**
   - E = −GMμ/(2d) and U_N = −GMμ/d = 2E, so dU_N/dt = 2 dE/dt = −2P_GW. The sign is negative and the factor is 2.
   - Hence P_ent/|dU_N/dt| = (5/64)η/(G³M²μ), and the powers are comparable at η = (64/5)G³M²μ.
   - ḋ_Peters = −(64/5)G³M²μ/d³, the standard Peters result.
4. **Chirp-mass degeneracy.**
   - Ω² = GM/d³ gives E(Ω) = −½μ(GM)^{2/3}Ω^{2/3}, and P_GW = (32/5)Gμ²(GM)^{4/3}Ω^{10/3}.
   - Ω̇ = (1+R)P_GW/|dE/dΩ| = (1+R)(96/5)(G𝓜)^{5/3}Ω^{11/3}, with 𝓜^{5/3} = μM^{2/3}.
   - So ḟ is multiplied by the constant 1+R, and R is constant because η is constant (ass:drag) and the masses are fixed. A rescaling 𝓜 → λ𝓜 multiplies ḟ by λ^{5/3}, so λ = (1+R)^{3/5}. This is correct.
   - The text scopes it with "leading-order quadrupole frequency evolution … At that order". It makes no waveform-amplitude or parameter-estimation claim.
   - Aside, not in the text: at Newtonian order the amplitude mismatch would in addition be absorbed into a distance rescaling, so the statement does not overstate distinguishability. It understates it, if anything.
5. **Can any reading of ch14 save the original claim?**
   - The sentence itself says "if η is held fixed", and ass:drag fixes η on a given inspiral. With η fixed, k = 0 exactly.
   - eq:force-PN does allow η^μ(d, ḋ). But the sentence is explicitly the fixed-η case, and "an artefact of treating η as constant" refers to a growth that does not exist under that hypothesis.
   - The orbit is stated to be circular. eq:Peters scales as d⁴Ω⁶ ∝ d⁻⁵. The inclination factors carry no d-dependence.
   - No reading makes the original claim true, so the PRIOR-CLAIM-ERROR is confirmed.
6. **Overclaim check.**
   - The new text says the working law singles out no crossover separation and that the comparison is fixed by η and the masses. Both are correct for constant η.
   - It says that this book does not calculate whether η differs between regimes. That matches ch17:591–592 ("estimate η at tidal radii and at LIGO-band separations") and ch15:279–281.
   - It makes no observability claim beyond the scoped degeneracy. The retained Solar-System sentence is pre-existing and qualitative.
7. **Dependent passages.**
   - ch14:262–275 (intended domain list and LIGO paragraph): still true.
   - ch15:169 (laboratory image of P_ent): unaffected. ch15:291–292 ("regime in which quadrupole losses dominate"): still a valid pointer, now to a parameter regime in η and the masses.
   - ch16:220–222: compatible (see minor finding 2). ch16:258 ("only a bound on η"): still true, and weaker if anything. ch16:289 and 305: unaffected.
   - ch13:404–410, ch11:362–368, ch01:110–113 and 261–271: unaffected.
   - appH and ch17 Problem I contain no ratio claim.
   - No other chapter relies on the removed growth claim.
8. **Scripts.**
   - `verify_ratio.py` was re-run, with output to the scratchpad. The output is byte-identical to `verify_ratio_output.txt` and agrees with all my hand results above. The script checks the scaling, the coefficients, the factor −2, the comparable-η values, ḋ_ent = −2η/d³ and the ḟ factor (1+R). Its dimension line is bookkeeping only.
   - `apply_check.py` was re-run, writing its output to `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\ch14-new.tex`.
     - The baseline is 16520 bytes, sha256 d6883ca3…2d36, and matches the working tree.
     - Each OLD string occurs once and each NEW string 0→1.
     - The result is 17336 bytes, sha256 b1fefa68…dd2, with 411 CRLF, no bare LF/CR, no BOM and no trailing whitespace.
     - The output is identical to `apply_check_output.txt` apart from the "wrote" path line.
   - Diffing the result against the baseline shows only the two declared hunks, all CRLF.
9. **LaTeX.**
   - `eq:ratio` is kept (one occurrence, no references); `eq:Peters` and `ass:drag` each occur once. No new labels.
   - `\Geff` is already in local use. `\mathcal M` is defined inline as the chirp mass.
   - No process language. A single scoped closing sentence, with no repeated status lines.
   - The researcher's scratch build (`build_output.txt`): two pdflatex passes, exit 0, 376 pages, 0 undefined or multiply defined. I read this record but did not re-run the build.
10. **Literature.** No citations are added. The SME-scout ppE/Will pointers are not used in the text and were not verified by me.

## Findings
1. **Minor (no action required).**
   - **Location:** new Block 1, "At that order it is degenerate with a rescaling of the chirp mass".
   - **Finding:** the antecedent of "it" (the extra loss) and of "that order" (the leading-order frequency evolution) is clear from the preceding sentence.
   - **Reason:** a reader skimming might take it as a full-waveform degeneracy. As written it is correct and scoped.
   - **Optional tightening:** "In that leading-order frequency evolution the extra loss is degenerate with …". This is not a condition of acceptance.
2. **Minor (no action required).**
   - **Location:** ch16:221, "Expected if η is negligible at those separations".
   - **Finding:** with η constant per inspiral and a d-independent ratio, "at those separations" now has to be read as "in that regime/system".
   - **Reason:** the new ch14 sentence "This book does not calculate whether η differs between regimes" licenses this reading, and the retained ch14:270–275 LIGO paragraph is what "already said so" refers to. Not false.
   - **Possible later action:** a future tidy-up may replace "at those separations" with "in that regime".
3. **Minor (no action required).**
   - **Location:** `\mathcal M`.
   - **Finding:** `\mathcal M` is used elsewhere for a kinetic matrix (ch03:535–558, appH).
   - **Reason:** the ch14 use is local and defined inline, and chirp-mass notation is standard. No conflict in context.

No blocking or major findings.

## Scope of what is established
- **Established derivation, within the reduced Newtonian/quadrupole two-body model of ch14 (eq:Fdiss, constant η per ass:drag, eq:Peters, circular adiabatic orbits):**
  - P_ent/P_GW = (5/32)η/(G³M²μ), independent of d;
  - for a d^{-n} drag the ratio scales as d^{4−n};
  - dU_N/dt = −2P_GW, so P_ent/|dU_N/dt| = (5/64)η/(G³M²μ);
  - at leading order the frequency evolution changes by ḟ → (1+R)ḟ, equivalent to 𝓜 → (1+R)^{3/5}𝓜.
- **Correction of a merged claim (PRIOR-CLAIM-ERROR):** the old "positive power of d / grows toward wide separations / artefact" passage was false under its own stated hypothesis.
- **Not established, and not claimed:** the value of η, the drag exponent, whether η differs between regimes, any waveform or parameter-estimation statement, and any PN-order classification.
- **Problem I** remains OPEN / OPTIONAL / PROGRAMME-CONDITIONAL, and its original target is untouched. No label change.
- **Relevance to the infrared / full-GR derivation:** none on the critical path. This is a phenomenology consistency correction.
- **Open avenues the correction exposes (for the optional Problem I only):**
  1. The microscopic Γ_ij calculation alone decides n. Under the corrected text, n = 4 makes the drag a fixed fraction of the quadrupole loss, and n < 4 makes it grow outward.
  2. Γ_T (transverse) is the component that enters circular orbits, so a radial-only calculation (Γ_L) would not fix the ratio.

## Recommended disposition
Integrate as-is: the two blocks exactly as in `apply_check.py`, onto baseline sha256 d6883ca33d0cebd7e78162cdc0b49e0faffac9ac07bd986119ca4a09a3872d36, giving sha256 b1fefa684669f0315e705061a9efd84c732eca741e687b9f3a88977f2f976dd2. M3 fires because a merged claim was found wrong, so the loop stops for the author per MILESTONE.md. Not a breakthrough.

## Corrected snippet
None required. Relevant files:
- C:\Users\redgi\Projects\namcg-lab\proposals\063-ch14-ratio-correction\apply_check.py
- C:\Users\redgi\Projects\namcg-lab\chapters\ch14-dissipation.tex

VERDICT: ACCEPT | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: first | OPEN: 0/0
