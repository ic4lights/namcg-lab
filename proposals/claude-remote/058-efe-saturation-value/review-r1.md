VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: first | OPEN: 0/0

## Verdict
I verified the core correction independently. The value "ν_√(g_gal) ≈ 1.1" is false under eq:nu-sqrt at the manuscript's own inputs; the correct value is 1.348. The eq:nu-efe bracket sign is reversed relative to the 1D QUMOND law (FM12 Eq. 60, which I checked against the arXiv text), and the claims built on both errors are unsupported or false. Two small wording defects in the new text must still be fixed before integration: the appE sentence that labels the assumption's own baryonic reading as the alternative, and the missing link between the anisotropy sentence and eq:efe-sat.

## Source reading
- **Mode.** Digest + targeted reads + the ordinal-55 full-scan record. I did not do a new full scan in this review.
- **Digest.** `make_digest.py --check` printed `DIGEST CURRENT`, head 13647fa, `dirty-chapters: yes`. The dirty file is appH only (055–057).
- **Target files.** The digest file-hash prefixes match the baselines in apply_check for all four targets: ch13 aafba1b0c80e, ch16 8ce01e1d5c4f, appE 695dd9c29321, appI 91daa222e510. `git diff --quiet HEAD` is clean for them.
- **Read in full:**
  - ch13 L190–319: ass:track, ass:efe, eq:nu-efe, eq:efe-sat, the commentary paragraph, eq:nu-sqrt, and the SPARC paragraph.
  - ch16 L95–279 and L300–361: the table, the coefficient list, the observational checklist, "not made", and the bridge.
  - appE L20–69 and L190–309.
  - All of appI (L1–84).
  - appH sec:status-H, L2784–2869.
  - ch17 L518–579 (Problem H) and L676–695.
  - ch18 L38–56.
- **Dependency sweep.** I grepped every `chapters/*.tex` for: ass:efe, nu-efe, efe-sat, appE-efe, saturat, wide binar, g_ext, g_gal, QUMOND, AQUAL, Chae, Banik, FamaeyMcGaugh, "1.1", "1.35", "1.4", "external field" and Gaia. I read every hit in context. The appH hits at L2463, L2524 and L2631 are unrelated; L2803 and L2866–2868 are neutral and remain accurate. Labels ass:efe, eq:nu-efe, eq:efe-sat, eq:appE-RAR, sec:gaia-show and app:empirical are each defined exactly once. Both bib keys exist (namcg.bib L248, L330); this is their first use in chapters.
- **Ruling on the scan requirement (CLAUDE.md 3(c)).** The package edits an equation inside an assumption and a Status-section sentence, so 3(c) applies. I rule it satisfied in substance, though not by a new full scan:
  - The ordinal-55 gatekeeper full scan (proposals/057-mass-plane-class/scan-p1..p5.md) read all 30 files at f2d005f. Its pass 5 independently flagged exactly this "1.1" error and the eq:nu-efe sign (reports/ledger.md).
  - `git diff --stat f2d005f -- chapters/` shows only appH changed since then (+46 lines). I read that diff: it is Lorentzian-contour material (057) with no EFE content.
  - The four target files are byte-identical to the scanned versions.
  - My grep sweep covers every dependent token.
  - I state honestly that in this session I did not read every manifest file. The claim of coverage rests on the prior scan record plus the unchanged hashes plus the sweep.

## Claim under review
- **Claims:**
  1. "ν_√(g_gal) ≈ 1.1" (ch13 L255, ch16 L208, appE L48, appE L221) is false; the value is ≈1.35.
  2. The dependent claims are unsupported or false: "γ≈1.4 not explained", "compatible with ass:efe", appI "null result … expected", and appI Status "compatible … with the modest residual".
  3. appI's 20% is a velocity excess; only the units are clarified.
  4. The eq:nu-efe bracket sign is reversed; eq:efe-sat is unchanged.
  5. A sentence on the anisotropy of the saturated boost is added.
- **Target.** Problem H, quoted from appH L2788–2790: "Status: OPEN. Priority: OPTIONAL within the phenomenological scope. Completion: PROGRAMME-CONDITIONAL." ch17 L521 says "OPEN; OPTIONAL research within the theory." There is no status conflict. This is not a critical-path problem of the current Chapter 17 matrix-derived criterion (A, B, C, D1, E, F, G-derived, N), and none of those entries is touched.
- **Labels.** No status, priority or completion label is changed anywhere. The appI Status edit alters a compatibility sentence only. "does not alter the open-problem ledger" is retained.

## Checks performed
- **ν by hand.** x = 2.2/1.20 = 1.8333, √x = 1.35401, e^(−√x) = 0.25822, so ν = 1/0.74178 = 1.3481.
  - At 1.5e-10: ν = 1.4857.
  - At 1e-11: ν = 3.988, which confirms the existing "γ≈4".
- **Alternative readings, checked by hand:**
  - Simple MOND: ν = (1+√(1+4/x))/2 = 1.392.
  - Standard MOND: solve y²/√(1+y²) = 1.8333. This gives y² = 4.168 and ν = 2.0415/1.8333 = 1.114. It is the only reading near 1.1, and the manuscript does not use that interpolator.
  - Velocity factor: √1.348 = 1.161.
  - RAR inversion: g_N = 1.474e-10 gives ν·g_N = 1.4928 × 1.474e-10 = 2.200e-10, so ν = 1.49.
  - Claim 1 is verified.
- **1D QUMOND sign.** The collinear total field is ν(|g_N+g_e|)(g_N+g_e). Subtracting the external solution ν(g_e)g_e gives g = ν(g_tot)g_N + [ν(g_tot) − ν(g_e)]g_e. This is the corrected bracket; the manuscript form differs by 2g_e[ν(g_tot) − ν(g_e)].
  - **Source check.** I downloaded arXiv:1112.3960v2 and extracted the text with pdftotext into the scratchpad. In Eq. (60), "g = g_N ν((g_N+g_Ne)/a0) + g_Ne [ν((g_N+g_Ne)/a0) − ν(g_Ne/a0)]", the ν glyphs are dropped but the minus sign stands before the g_Ne-only argument. That is unambiguous and matches the derivation.
  - FM12 g_Ne is the Newtonian external field, consistent with ass:efe's "baryonic field".
  - Verified.
- **Along-field values.** Linearising the vector form in g_N with g_ext ∥ ẑ, ν(g_tot) ≈ ν_e + ν_e′(g_N·ẑ):
  - corrected: transverse ν_e, along ν_e + g_eν_e′ = ν_e(1+L_e);
  - manuscript: along ν_e(1−L_e).
  - L_e = −(ν−1)√x/2 = −0.34811 × 0.67700 = −0.2357.
  - Along-field values: 1.348 × 0.7643 = 1.030 (corrected) and 1.348 × 1.2357 = 1.666 (manuscript). Verified.
- **3D anisotropy.** Linearised QUMOND gives ∇²φ = ν_e(∇²φ_N + L_e∂_z²φ_N). The solution is φ = ν_e(φ_N + L_e∂_z²ψ) with ψ = −Gmr/2, and ∂_z²r = sin²θ/r. Hence φ = −Gmν_e[1 + (L_e/2)sin²θ]/r.
  - Radial force on the axis: ν_e. In the transverse plane: ν_e(1+L_e/2) = 1.348 × 0.8822 = 1.189.
  - This agrees to first order with FM12 Eqs. (63)–(64) as extracted: r̃ = r/[1+(L_Ne/2)(x²+y²)/r²]. Verified.
- **20% arithmetic.** √1.3481 − 1 = 0.161 and √1.4857 − 1 = 0.219. The isolated map gives a velocity factor of √3.988 = 1.997, so the "∼4" is an acceleration factor. Verified.
- **Scripts.** I re-ran nu_check.py and apply_check.py with output to the scratchpad (`C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\nu_out.txt`, `...\apply_out.txt`, `...\out058r\`).
  - nu_out.txt is identical to nu_check.txt.
  - apply_out.txt differs from apply_check.txt only by the "wrote" lines, because I passed an output directory.
  - All OLD strings occur exactly once and all NEW strings occur zero times in the baseline. Baseline and result hashes and CRLF counts match the proposal. There are no bare LFs.
  - The repository is unchanged afterwards (`git status` still shows appH only).
- **Literature:**
  - Chae (arXiv:2305.04613): the abstract was fetched. It gives g_obs/g_pred = 1.43 ± 0.06 at g_N ≈ 10^−10.15, and says the deviation "agrees with the boost factor that the AQUAL theory predicts" under the Galactic external field. Characterised accurately.
  - Banik et al. (arXiv:2311.03436, MNRAS 527, 4573): the abstract was fetched. MOND with the EFE predicts velocities ≈20% above Newtonian asymptotically; MOND is excluded at 16σ (MCMC), with Newton preferred at 19σ. Characterised accurately, and the package adds no citation key for it.
  - Pittordis et al. 2025 and the "quality-framework study 2026" (appI L45–46): not independently verified, but not relied on or changed.
- **Build.** I did not rebuild, because that would write in the repository. The researcher reports a scratch build of 365 pages with 0 undefined references and both citations resolved. The integrator's build_check must confirm this.
- **Text hygiene.** No process language. No new labels.

## Findings
1. **Severity: minor (required).** Location: appE Edit 1 NEW (after L48).
   - **Finding.** "If g_ext is *instead* read as the baryonic Newtonian field …" presents the baryonic reading as the alternative.
   - **Reason.** Assumption ass:efe (ch13 L223, "a baryonic field g_ext") and appE L36–37 ("external Newtonian field") already define g_ext as baryonic. It is v²/R0, used for the headline 1.35, that is the observed field. As worded, the new sentence implies the main reading takes g_ext as non-baryonic, which contradicts the assumption. The proposal's own D2 recognises this clash.
   - **Required action.** Use the replacement text in the Corrected snippet below. It adds the explicit condition that the RAR holds at the Sun, which the proposal already classifies as conditional.
2. **Severity: minor (required).** Location: ch13 Edit 2 NEW.
   - **Finding.** The anisotropy sentence shows that eq:efe-sat ("γ → ν(g_ext)", unqualified inside ass:efe) holds for the corrected eq:nu-efe only transverse to g_ext; along the field it gives ≈1.03. The new sentence does not tie this back to eq:efe-sat.
   - **Reason.** Without that link, the assumption displays an isotropic limit and the next paragraph gives contradicting along-field numbers. The mismatch is pre-existing (with the old sign the along-field value was 1.67), but the package now records the numbers, so it should name the equation they qualify.
   - **Required action.** Change "The saturated boost\nis anisotropic at order" to "The saturated boost~\eqref{eq:efe-sat}\nis anisotropic at order". The sentence's own content then states the direction in which eq:efe-sat is exact for each form. No change to the assumption is needed.
3. **Severity: minor (not required).** Location: ch16 Edit and appE Edit 2, "of the size of that saturated value".
   - **Finding.** This is acceptable as an order-of-size statement under a conditional "would be".
   - **Note.** Chae's 1.43 is measured at g_N/g_ext ≈ 0.3, outside the strict g_N ≪ g_ext limit, where the ν_√ quadrature-sum prediction is at most 1.35. The orbit-averaged anisotropic value lies between 1.03/1.19 and 1.35.
   - **Action.** Optional: "comparable to" would be slightly more conservative. Not required. Nothing here turns Problem H into a success: "coefficient-level agreement, not a derivation" is correctly scoped.
4. **Severity: minor (out of scope, pre-existing).** Location: ch16 L214 and L267, appE L219 and L283.
   - **Finding.** These lines hard-code "Theorems~7.3--12.4", "Appendix~D", "Theorem~7.3" and "Assumption~E.1"; the inputs g_gal = 2.2e-10 and (1.5–2.2)e-10 have no source in the repository.
   - **Action.** Leave as is in this package, and record them for a later bookkeeping item.

No blocking or major findings remain.

## Scope of what is established
**Established (arithmetic and derivation on the manuscript's inputs):**
- ν_√(2.2e-10; g_s = 1.20e-10) = 1.348. "1.1" is false under every reading the manuscript supports.
- The eq:nu-efe bracket sign was reversed relative to the 1D QUMOND law (FM12 Eq. 60).
- The corrected algebraic form gives ν_e transverse and ν_e(1+L_e) ≈ 1.03 along g_ext. 3D QUMOND (point mass, linearised) gives ν_e along and ν_e(1+L_e/2) ≈ 1.19 transverse.
- appI's 20% is a velocity excess (0.16–0.22).

**False implications removed:**
- "γ≈1.4 not explained by saturation";
- "Newtonian null compatible with/expected under ass:efe";
- appI Status "compatible with the modest residual", which also contradicted appI L44–46.

**Conditional:**
- The baryonic g_ext ≈ 1.5e-10 (requires the RAR at the Sun).
- "ass:efe as written is disfavoured by the controlled analyses" (requires those analyses and premises (i)–(vi) of the proposal). The manuscript text says only "disfavour" and "constrains", which is appropriately weak.

**Problem H.** Unchanged: OPEN, OPTIONAL, PROGRAMME-CONDITIONAL. The package is neither DERIVED nor PROGRAMME-CONDITIONAL progress on H. It is not a breakthrough.

**Bounded negative.** The corrected record makes ass:efe's saturated value look disfavoured by the cited Gaia analyses. That holds only within the premises below; avenues that could still favour the programme are listed in the next block.
- (i) ν_√ is the embedded-subsystem boost;
- (ii) the external field enters only through the argument of the same ν (a QUMOND-type premise);
- (iii) the unsourced g_ext at the Sun;
- (iv) no orbit-averaged anisotropic computation;
- (v) wide binaries are not deep in g_N ≪ g_ext;
- (vi) the data analyses (Chae versus Banik and others) disagree.

**Open avenues, ranked (none bears on the infrared/full-GR critical path):**
1. Compute the external-field dependence of the modular response directly, i.e. U_ent[I(A:B)] with an external Newtonian source. This replaces premise (ii) and is the only avenue that is Problem-H content.
2. Compute an orbit-averaged, projected 3D boost for the corrected eq:nu-efe or full QUMOND with ν_√, to replace the isotropic 1.35.
3. Source g_ext at the Sun, baryonic and observed, from a cited Milky Way mass model.

## Recommended disposition
Revise. Apply the two required wording changes (Findings 1–2) in r2. The ch13 sign fix (Edit 1) and all other edits may stay as submitted. Re-run apply_check and the build in r2.

Milestone: M3 (PRIOR-CLAIM-ERROR) applies. A false numerical claim with false falsifier-list implications, and a sign error in a displayed equation inside an assumption, sit in merged text. Their scope is optional phenomenology.

## Corrected snippet
No new physics is needed. The only added assumption is "the RAR holds at the Sun", stated explicitly.

appE Edit 1, replacement NEW:
```latex
\approx 1.8\,g_{\dagger}\), so \(\nu_{\sqrt{}}(g_{\mathrm{gal}})\approx 1.35\).
Assumption~\ref{ass:efe} takes \(g_{\mathrm{ext}}\) to be baryonic,
whereas \(v_{\odot}^{2}/R_{0}\) is the observed field. If~\eqref{eq:appE-RAR}
holds at the Sun, inverting it at \(g_{\mathrm{obs}}=v_{\odot}^{2}/R_{0}\) gives
\(g_{\mathrm{ext}}\approx 1.5\times 10^{-10}\,\mathrm{m\,s^{-2}}\) and
\(\nu_{\sqrt{}}(g_{\mathrm{ext}})\approx 1.5\).
```

ch13 Edit 2, NEW, second and third lines only (the rest unchanged):
```latex
\(\nu_{\sqrt{}}(g_{\mathrm{gal}})\approx 1.35\). The saturated boost~\eqref{eq:efe-sat}
is anisotropic at order
```

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: first | OPEN: 0/0
