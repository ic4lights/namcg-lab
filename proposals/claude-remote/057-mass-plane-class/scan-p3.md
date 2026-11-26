## Scan note, pass 3 of 5 (ordinal-55 full scan, CLAUDE.md 3(a))

**Working file confirmed.** `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex` is 561466 bytes and 3255 lines, with sha256 `ea5c753b0f01a3a92e426435f747fa464521980f609ab330f4a432868daba1f5`. The hash matches.

**What I read.**
- `C:\Users\redgi\Projects\namcg-lab\proposals\057-mass-plane-class\appH_insert.tex`, in full (11 lines).
- appH lines 2201–3255, every line, in consecutive ranges: 2201–2260, 2261–2350, 2351–2420, 2421–2480, 2481–2530, 2531–2580, 2581–2630, 2631–2670, 2671–2710, 2711–2750, 2751–2790, 2791–2940, 2941–3100 and 3101–3255.
- For the status comparison, ch17-agenda.tex lines 470–604, plus grep of its priority lines.

**Content of the range.** It covers the Problem F Poisson-limit and conjugate-coordinate (CP^{1,2}) paragraphs (2201–2750) and the Problem G, H, I, J and N sections plus "What this appendix does not do" (2752–3255).

**Mechanical checks.**
- **Labels.** The range defines six labels: `sec:status-G`, `-H`, `-I`, `-J`, `-N` and `-not`. Each appears exactly once across `chapters/*.tex`; the second grep hit was the `.aux` file.
- **Refs.** All 34 distinct `\ref`/`\eqref` targets in the range resolve to exactly one label.
- **Citations.** All 15 cite keys exist once in `bib/`.
- **Process language.** A grep for "as proposed", "the researcher", "proposal" and similar found none.
- **Spot re-derivations.** These all check out:
  - the 2m=2 counterexample K=−4g_L^{-1} (L2304);
  - e^Te=I iff ω̂²=−I (L2286);
  - the negative-mode counts 49 and 154 (L2412);
  - the f_rat expansion (L3052);
  - the maximally symmetric relation k−8αk³=Λ/3 (L3078);
  - the Bose occupation identity (L2803–2814);
  - the deviation range (1, 4/3] for β_K∈[−1,0) (L2748).

## Findings

1. **L2349, note.** The line says the sign of the level-one tree form "depends on the convention for the weight, which \eqref{eq:Smatrix} does not fix". This stays true of eq:Smatrix itself. It does not conflict with the Problem E Definitions (A)/(B)/(C), which are separate regulated-integral definitions for a different model setting. No action.

2. **L2414, L2443, L2460, L2495, L2607, L2622, L2662, L2693, L2750, note.** These say Euclidean-to-Lorentzian passage is "a Wick-rotation hypothesis tied to Problem E", or that the result "leaves/does not bear on Assumption~\ref{ass:lorentzian}". This agrees with the 057 closing sentence that the positive mass does not discharge `ass:lorentzian`, and with the 053–056 E blocks.

3. **L2669 and L3146, note.** L2669 uses the "formal continuation S_L=−S_E" (tree form). L3146 uses "S_E=−iS_L as in Appendix~\ref{app:seeley-dewitt}" (heat-kernel effective action, flagged as an added convention). These are two different, explicitly labelled conventions in different settings. Neither asserts a derived contour or real-time reading, so neither conflicts with the 057 limit statements, which leave open whether the γ>0 limit exists and give Euclidean values at phases for γ→0 first.

4. **L2313 and L2526, note.** Θ is used locally for the Poisson bivector (F section) and for the heat-trace function Θ(s) (L2526). The 057 insert uses Θ(E) for a plane-angle branch of arg det. All three are defined locally in separate sections, so there is no clash that affects the insert. There are no occurrences in the range of `\mathfrak C`, `M_\gamma`, `F_{\mathrm E}` or `\mathcal R_u`.

5. **L2777 vs ch17 L521, minor (pre-existing).** The qualifiers on Problem H's priority differ. appH has "OPTIONAL within the phenomenological scope"; ch17 has "OPTIONAL research within the theory". Both say OPTIONAL and OPEN, so there is no status conflict, only qualifier wording. This is not touched by 057.

6. **L2277, note (pre-existing).** "Problems~B, C, D and~F remain open" uses the undifferentiated "D". It is consistent with ch17, where D (and D1) stays OPEN and CRITICAL PATH. No status disagreement.

7. **Status lines.**
   - **G (L2756–2771):** OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL, mechanism CLOSED CONDITIONALLY, derivation OPEN, and G-model/G-external limited to a scope-limited model. This matches ch17 L475–495.
   - **H, I, J (L2777, L2864, L2995):** OPTIONAL, matching ch17 L685.
   - **N (L3120):** CRITICAL PATH for the matrix-derived label, OPEN, matching ch17 L498.
   - **F closing lines across 2201–2750:** "Problem F remains open", sometimes "and PROGRAMME-CONDITIONAL", with no label changes.
   - No status, priority or completion line in the range disagrees with ch17 or with another line.

8. **PRIOR-CLAIM-ERROR: none found.** The F paragraphs scope themselves carefully: Poisson limit, leading symbol, sampled points, and "numerical, not proved" where applicable. L2557 and L2566 contain a self-correction of the sign of a logarithmic term in earlier Fin values, and L2544 supersedes the earlier Landau model. Both are already recorded in the merged text.

## Does anything block the 057 insert?

**No.** Nothing in lines 2201–3255 blocks integrating the 057 insert. The range does not reference the Problem E insertion anchor (L1564), any 057 symbol, or Definitions (A)/(B)/(C). All Lorentzian and Wick statements in the range defer to `ass:lorentzian` and Problem E, consistently with the insert. There are no blocking or major findings, only one minor and several notes.
