# Gatekeeper review of the fused state at HEAD 817a621 — 2026-11-11

Scope: merge safety of the `origin/remote/claude` bring-in (see `reports/merge-remote-claude-20261111.md`).
One gatekeeper pass, digest + targeted reads, no full 30-file scan. The report below is the agent's
output, verbatim; orchestrator verification notes follow it.

---

  VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: PRIOR-CLAIM-ERROR, SME-CONSULT | PROGRESS: first | OPEN: 0/2

  ## Verdict
  The fused state at HEAD 817a621 is mathematically sound and safe to build on: every numerical/closed-form change I re-derived independently is correct, the two fused Problem E continuations are complementary (not contradictory), the Problem G blocks are non-competing, and no Rule-2 line or completion claim moved; but two relative cross-references broken by the fusion must be fixed and the unsourced `g_gal` numbers need provenance before the corrected phenomenological values are load-bearing.

  ## Source reading
  Digest + targeted reads. No full 30-file scan was performed (this is a merge-safety review, not a 5th-item/milestone/definition-change review; CLAUDE.md 3(a)-(d) not triggered). `scratch/digest.md` reported CURRENT, `dirty-chapters: no` (orchestrator-provided). Read in full: `/home/red/code/namcg-lab/reports/merge-remote-claude-20261111.md`; `/home/red/code/namcg-lab/MILESTONE.md`; `/home/red/code/namcg-lab/chapters/ch16-falsifiers.tex` (entire); `/home/red/code/namcg-lab/chapters/appE-rar-bridge.tex` (entire); `/home/red/code/namcg-lab/chapters/appI-gaia-wide.tex` (entire, re-read L40-91 this session); `/home/red/code/namcg-lab/chapters/ch14-dissipation.tex` L224-298; `/home/red/code/namcg-lab/chapters/appH-microscopic-proofs.tex` L1553-1805 (fused Problem E), L2995-3130 (Problem G), L3257-3296 (Problem I ledger), plus exact text at L1566-1595, 1650-1734, 1699, 1714, 1723, 1727; `/home/red/code/namcg-lab/chapters/ch17-agenda.tex` L655-765; bib entries for all 13 new keys; full `git diff 651b1d7..HEAD -- chapters` for all five whole-file chapters. All other chapters: greps and diffs only — not read in full.

  ## Claim under review
  The merged working-tree state (author commits `7eaca1b`, `817a621` of the three-way merge of `origin/remote/claude` text into `local/gpu`): (1) coherence of the fused Problem E section; (2) placement of the two Problem G blocks; (3) three numerical corrections (ch14 `eq:ratio`, `nu\sqrt{g_gal}` 1.1->1.35, appI "20%" as velocity excess); (4) evidence boundaries, Rule-7 numbers, 12 new bib keys, hard-coded refs; (5) Rule-2 compliance. Affected problems, ledger lines quoted verbatim: E — "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label." (appH L1556-1557); G — "Status: OPEN. Priority: CRITICAL PATH." (L3007-3008); H — "Status: OPEN. Priority: OPTIONAL within the phenomenological scope."; I — "Status: OPEN. Priority: OPTIONAL falsifiable phenomenological extension; prerequisite only if drag is claimed as derived or predicted. Completion: PROGRAMME-CONDITIONAL." All remain OPEN; ch17 criterion (A,B,C,D1,E,F,G-derived,N; H,I,J optional) re-read at L700-747 and unchanged by the merge.

  ## Checks performed
  Independently re-derived (my own sympy/algebra, earlier in this review; symbolic checks are checks, not proofs):
  - `eq:ratio`: P_ent = eta mu v^2/d^4 = eta mu G/d^5; Peters P_GW = (32/5) G^4 M^3 mu^2/d^5; ratio = (5/32)eta/(G^3 M^2 mu), d-independent OK; drag propto d^-n => ratio propto d^(4-n), growth needs n<4, and `ass:drag` has n=4 (constant ratio, no growth) OK; constant-factor power excess rescales chirp mass by (1+P_ent/P_GW)^(3/5) OK; rewritten exercise agrees OK.
  - nu_sqrt(g)=1/(1-e^{-sqrt(g/g_s)}) at g=2.2e-10, g_s=1.20e-10: sqrt(g/g_s)=1.354, nu=1.348 -> "1.35" OK; ratio "~1.8 g_dagger" =1.833 OK. appE inversion at g_obs: g_ext~1.474e-10, nu~1.49 -> printed 1.5e-10/~1.5 OK. appI: sqrt(nu)-1 = 0.161-0.219 -> "0.16-0.22" OK, consistent with the retained "of order 20% in relative velocity" at appI L83. L_e=-0.2356 variants OK. Doubleton kernel (1/3)n(n+4)(n^2+4n+7) with multiplicity -> 80/304 at n=1,2 OK.
  Verified textually: fused-E seam (preamble header "The regulated Lorentzian integral at finite N (conditional for N>=3)" once at L1566; "Take traceless Hermitian" once at L1567; closing L1581 correctly points to our continuation in fused order; single closing status "Status. Remains Assumption~\ref{ass:lorentzian}." at L1803; no repeated closing lines); no mathematical contradiction between the halves (our modulus obstruction is within R_u/polynomial classes; their pointwise limits are in the wider frak-c class; their item (ii) "not integrable at N=2" agrees with our failure claim); Problem G edge block's Bearing (L3124(i)) explicitly denies del_M of def:HBEV; closing "Problem~G remains open and PROGRAMME-CONDITIONAL" (L3128); Rule-2: `git diff 651b1d7..HEAD -- chapters` contains no Status/Priority/Completion line change; ass:lorentzian explicitly "not discharged" at L1714, L1727 and section close; all 13 bib keys exist exactly once and every new key is cited (appH L1719-1770, L3106-3128; Chae only at appE L226); Rule-7 grep: no printed v_sun or R_0 anywhere in `chapters/`.
  Literature (WebFetch today): arXiv 2605.13294 (Steinacker, "Quantum spacetime and quantum fluctuations in the IKKT model at weak coupling") exists and matches topic; 2512.03161 (Liao-Maeta, Euclidean IKKT saddle with so(1,3) solution) exists and matches; 2403.17180 (Fioresi-Yuncken, Plancherel formula for SL(2,C)) exists, theorem number not confirmable; 2408.05274 (Fliss-Frenkel-Hartnoll-Soni, "Minimal Areas from Entangled Matrices") exists and matches. Via arXiv API: Pittordis-Sutherland-Shepherd 2025 and the Cookson-Banik-El-Badry et al. 2026 "Quality Framework... No Evidence for MOND" exist and support the attributed Newtonian conclusions; "Banik et al. 2024" attested only secondhand — not independently verified. Equation/theorem-number-level attributions (Steinacker2026Weak Eqs. (13),(16),(17),(88),(89),(100); FioresiYuncken2024 Thm 7.1; Fliss et al. Eqs. (3.14),(4.4); MartinDussaud2019 Eq. (308); MantaSteinacker2025 Eqs. (11)-(12)) — not independently verified.

  ## Findings
  1. **major** — appH L1654 and L1671 (fusion artifact). "Keep the setting, Definition~(A) and the contours \(\mathcal R_u\) of the preceding paragraph" (L1654) and "the notation of the two preceding paragraphs" (L1671): post-fusion, the immediately preceding paragraphs are our reflection-positivity block, but Definition (A), \(\mathcal R_u\) and the \(\mathcal G_{ab}\)/flat-direction notation live in the preamble at L1566-1581. As written they mispoint the setup of a proved-at-N=2 derivation. Required action: named references in the style already used at L1699/L1714/L1723/L1727 ("the paragraph on the regulated Lorentzian integral"). Snippet below.
  2. **major** — Rule 7 (pre-existing, now load-bearing): `g_gal = 2.2e-10` (appE L47, ch13 L253) and appI's `(1.5-2.2)e-10` have no source in the repository; grep confirms no printed v_sun or R_0 exists anywhere in `chapters/`. The merge makes these numbers carry the corrected printed values 1.35/1.5/0.16-0.22. Required action: print the source values with provenance in appE/app:empirical (the numbers are physically plausible from standard external v_sun, R_0), or mark them explicitly as external estimates. Not a merge defect; flagged by the merge report itself.
  3. **minor** — hard-coded cross-refs (convention): new text introduces one at appE L225 ("not Theorem~7.3"); pre-existing at ch16 L215 ("Theorems~7.3--12.4"), ch16 L268 ("Appendix~D"), ch16 L276, appE L290 ("Assumption~E.1"). The new instance should be converted to `\ref`; a sweep of the pre-existing ones is advisable but not merge-blocking.
  4. **minor** — merge report inaccuracy: the report says ch16 cites `Chae2023WideBinaries`; the full diff shows ch16 gained no `\cite` (Chae is cited only at appE L226). Consequence: ch16 L212's "A surviving \(\gamma\approx 1.4\}" remains uncited. Correct the report; optionally add the citation at ch16 L212.
  5. **minor** — appI L47-48 cites in plain text ("Banik et al.\ 2024; Pittordis, Sutherland & Shepherd 2025; quality-framework study 2026"), not bibkeys; the new Status sentence L82-85 ("disfavour a residual enhancement") rests on them. I verified Pittordis et al. 2025 and the 2026 quality-framework paper (Cookson-Banik-El-Badry et al.) exist and support the attributed claim; "Banik et al. 2024" not independently verified. Convert to bibkeys. Also note the field is contested in both directions (Chae et al. 2025/26 vs Pittordis/Cookson); the appendix already hedges ("less filtered samples diminish", ch16 "not a derivation"), so the one-sidedness is within acceptable scope.
  6. **minor** — notation: \(\mathcal G\) now serves two roles in one section — 10x10 spacetime-index \(\mathcal G_{\mu\nu}\) (L1583) and 3x3 colour \(\mathcal G_{ab}\) (L1571, L1671). Subscripts distinguish them and each usage is pre-existing on its own line, but the fusion puts them ~100 lines apart; a one-word disambiguation at first reuse in each block would help.
  7. **minor** — ch16 L220-222 LIGO bullet ("Expected if \(\eta\) is negligible at those separations") vs rewritten ch14: not contradicted — ch14's rewritten paragraph (L282-287) still says the quadrupole remains default unless eta is constrained large, and retains the regime loophole; "at those separations" is merely loose since the ratio is d-independent for fixed eta. No action required.
  8. **minor** — pre-existing looseness (identical on the other line, not a fusion artifact): "the preceding paragraph" at L1666/L1695/L1697 refers across list-item paragraphs. No action required.

  ## Scope of what is established
  Established by this review (verified): all three corrected numbers and their supporting algebra are correct as printed; the fusion introduces no mathematical contradiction, no duplicate/contradictory closing status, and no Rule-2 violation; nothing in the merged text discharges ass:lorentzian or closes E, G or I (every new block closes with explicit non-discharge language); the four spot-checked 2025/26 citations exist and match their attributed topics. Conditional within the text: the fused Problem E results remain proved-at-N=2 / conditional-for-N>=3 statements with explicit class qualifiers — N=2 contour-class invariants, the regulator-inertia no-go, pointwise spacelike-momentum limits, causal-k unreachability, k<14 Pfaffian window, and the (P1)/(P2) signature-selection paragraph with both premises declared supplied. Not verified: equation/theorem-number attributions to the 2025/26 references (see SME request). Still OPEN: Problems E, G (CRITICAL PATH), H, I, exactly as the ledger states; the Chapter 17 criterion is unmoved. The ch14 correction removes previously printed errors (the false growing-ratio claim and nu~1.1) that were on this line since the fork — hence PRIOR-CLAIM-ERROR; the current text is correct.

  ## Recommended disposition
  Revise, then integrate: apply the two named-reference fixes (Finding 1), then a sourcing item for Findings 2 and 5 (add the printed v_sun/R_0 values with provenance; promote appI's plain-text citations to bibkeys), optionally the `\ref` conversion for appE L225. Do not integrate further material on top of appH L1650-1680 until Finding 1 is fixed. Build facts as given (398 pp, 0 undefined, 0 multiply-defined) are consistent with my static checks; the `build_check.py` FAIL is a script gap (no bibtex pass), not a manuscript defect.

  ## Corrected snippet
  No new physics; mechanical named-reference fixes in the existing in-file style:
  - L1654: "Keep the setting, Definition~(A) and the contours \(\mathcal R_u\) of the paragraph on the regulated Lorentzian integral, and let \(O\) be a product of..."
  - L1671: "Keep Definition~(A), \(\gamma=0\) and the notation of the paragraphs on the regulated Lorentzian integral and on Fourier observables, and take the contours \(A_\mu=\sum_\nu\Lambda_{\mu\nu}X_\nu\)..."

  ## SME consultation request
  1. Do Eqs. (13), (16), (17) of arXiv:2605.13294 state the quasi-coherent-state criterion max|<<t|A_a|t'><t'|A_a|t>>|^(1/2) << Delta_T and its stated failure for commutative backgrounds, and do Eqs. (88)-(89), (100) give g_YM = 1/rho^2, the 1/sinh^3 tau dependence, and the late-tau fluctuation estimate as the manuscript (appH L1732-1746) attributes?
  2. Is Theorem 7.1 of arXiv:2403.17180 the SL(2,C) Plancherel statement used at appH L1770 (support on principal series; counting measure in the discrete label times polynomial density times Lebesgue measure in the continuous one)?
  3. Are Eq. (3.14) and Eq. (4.4) of arXiv:2408.05274 (SciPost 18(6):171) the row-length expression and the classicalised charge used at appH L3120, and is the "2 log(eM/)" flat-diagram factor from that paper?
  4. Is "Banik et al. 2024" (cited plainly in appI L47) a real, identifiable paper claiming Newtonian wide-binary kinematics at high significance, and is it the right anchor or should appI cite Cookson-Banik-El-Badry et al. 2026 instead?

---

## Orchestrator verification notes

* **Finding 1 confirmed by direct read** (`chapters/appH-microscopic-proofs.tex:1654`, `:1671`). At
  L1654 the sentence is "Keep the setting, Definition~(A) and the contours \(\mathcal R_u\) of the
  preceding paragraph", but the paragraph immediately preceding is this line's reflection-positivity
  block (L1592-1652); Definition (A), \(\mathcal R_u\), \(\tilde A_\mu\) and the flat-direction
  notation are in the fused preamble L1566-1581. L1671 "the notation of the two preceding paragraphs"
  and "the matrix \(\mathcal G\) of the preceding paragraphs" have the same drift. This is the
  expected signature of splicing two independently accepted continuations onto one preamble, and it
  was not caught by the compile (relative prose pointers are not references).
* **Finding 4 corrected as to its premise, upheld as to its consequence.** `reports/merge-remote-claude-20261111.md`
  contains no mention of `Chae` (grep: no match), so it never claimed ch16 cites that key. The verified
  facts: exactly **12** bib keys arrived in the merge (`git diff 651b1d7..HEAD -- bib/namcg.bib`,
  12 added `@` entries), not 13 — `Chae2023WideBinaries` was already in this line's bib before the
  merge, and it is cited only at `chapters/appE-rar-bridge.tex:226`. The reviewer's live point stands:
  the `gamma ~ 1.4` statement at ch16:212 has no citation attached.
* **Finding 3 nuance.** `git diff 651b1d7..HEAD -- chapters/appE-rar-bridge.tex` shows the sentence was
  rewritten but the hard-coded reference is a carry-over, not an import: `-Newton constrains the
  isolated reading, not Theorem~7.3.` / `+\(\nu_{\sqrt{}}(g_{\mathrm{gal}})\approx 1.35\), not
  Theorem~7.3.` So `Theorem~7.3` at appE is pre-existing on this line, on the same list as ch16's.
* **Finding 4 consequence verified.** The merge added **0** `\cite` lines to `chapters/ch16-falsifiers.tex`,
  so the `gamma ~ 1.4` statement there is indeed uncited; the key exists and is cited only in appE.
* **Rule 2 and the build** were confirmed independently before this review: `git diff 651b1d7..HEAD
  -- chapters` moves no Status/Priority/Completion line; `pdflatex` + `bibtex` + two more passes give
  398 pages with 0 undefined citations, 0 undefined references and 0 multiply-defined labels.
* **No file outside `scratch/` was written by the reviewer**; the working tree afterwards held only
  `scripts/build_check.py` (orchestrator edit) and `.claude/hooks/guard.py` (author edit).
* **Not established by this pass:** any full-scan claim. 23 chapter files were not read in full.
* **Open items carried forward:** the two named-reference fixes (chapters/, needs an `auto/*` branch
  plus `.claude/state/allow_chapters`, so not applicable on `local/gpu`); Finding 2 sourcing for
  `g_gal = 2.2e-10`; Finding 5 bibkeys for appI's plain-text citations; the four SME questions above.
