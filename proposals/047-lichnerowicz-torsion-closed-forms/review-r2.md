VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
The full scan is complete, (a)-(m) were applied verbatim and every changed claim re-derives, but three minor replacements are required: two define weights used in printed inequalities, and one fixes a power of `mq` against the scale of K. Do not integrate on this review. This verdict is not merge approval; only the author merges.

## Source reading
**Method: full scan. All 30 files in the manifest were read in the working tree.**

- **Digest:** `--check` printed DIGEST CURRENT. Head b9c8b10, chapters-hash 1416784d1e1634a9, tree-hash 339cd7f99f895f0d. dirty-chapters: yes, and `git status` shows only appH modified, as the task states. I read the working-tree files directly.
- **Read in full:**
  - ch01 to ch18;
  - appA, B, C, D, E, F, G, I, J, K, L;
  - appH in consecutive ranges L1-180, 181-255, 256-300, 301-346, 347-846, 847-1406, 1407-2026, 2027-2176, 2177-2236, 2237-2286, 2287-2336, 2337-2386, 2387-2422, 2422-2923.
- **Long lines:** appH has 30 lines over 2000 characters (maximum 3816). I saw no truncated line in the output.
- **Also read:**
  - MILESTONE.md and review-r1.md;
  - appH_insert.tex and proposal-r2.md in full;
  - compile_check.py in full, and part of s6_insert_mechanics.py;
  - arXiv:2411.02598 as extracted text: keyword search across the whole text, plus the introduction (part), Sec. 3.3 opening and Discussion (part).
- **Not read:** `reports/ledger.md`. The rulings and the 044-046 standard were taken from review-r1.
- **Reuse of this scan:** it covers ordinal 45 for chapters-hash 1416784d1e1634a9. If that hash is unchanged next round, the next gatekeeper can rely on it and need not repeat it. The revisions below touch only the proposal folder.
- **Process slips, all read-only in effect:**
  - Three times I issued two read-only calls in one batch, against the sequential rule.
  - I ran `apply_r2_replacements.py --help`, which ran its default mode. It refused to write because the file no longer holds the r1 bytes. The sha256 and mtime of the insert are unchanged, and nothing in the repo changed.

**Scan results**
- **Chapter 17 against Appendix H:** no discrepancy.
  - The critical-path set is A, B, C, D1, E, F, G-derived and N. H, I and J are optional.
  - G reads "mechanism CLOSED CONDITIONALLY, derivation OPEN" in ch17 L475 and appH L2434, and "OPEN ... PROGRAMME-CONDITIONAL" in appH L2423. These are compatible.
- **Labels:** no duplicate or undefined labels (mechanical pass; the build agrees).
- **Stale after 046/047:** nothing requires an edit. These merged passages are refined by the insert and stay true as scoped: L2413 ("first background-torsion correction"), L2415 (M*, isolated data, the range M ~ coth^2 tau), L2387 and L2398 (equality "not derived").
- **Contradicting the insert:** nothing. L2385 and L2391 say W_R has no fixed sign and no value or sign of G_eff follows. The insert keeps both. L2391's clause "do not ... fix the sign of W_R, so no value or sign of G_eff follows" has a weaker reason after the insert, but its conclusion stands.
- **Pre-existing items, not from 046/047, not math errors and not blocking (for the author):**
  - **Hard-coded references** (269 by regex). Examples: ch16 L214 and L275 "Theorem 7.3", appE L219, appE L283 "Assumption E.1", ch16 L267 "Appendix D". The insert adds none.
  - **ch01 L322 and ch07 L421** say Chapter 17 lists falsifiers. Chapter 16 does.
  - **ch03 L904-916, ch01 L52-56, ch02 L118-124** present the frame as the gradient `<dPhi>`. ch04 L100-114 keeps only Repair II.
  - **appJ L103-104** places the signature assumption in Chapter 3. It is in Chapter 4.
  - **ch16 inventory** omits `ass:sqrt-mod`, which belongs to optional Problem H.

## Claim under review
Round-2 text of five conditional results in the 045/046 class on CP^{1,2} x K, targeting Chapter 17 `sec:ch17-done` items 2 and 6 and the sub-target G_T = G_A:
1. closed forms;
2. exclusion of isolated K data at first order in torsion;
3. Lichnerowicz reduction;
4. frozen resummation and scale argument;
5. helicity-two coefficient on the null cone, with sign and replica gaps.

**Problem B (appH L45-47):** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."

**Problem F (appH L1366-1369):** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating \(G_{\mathrm{eff}}\) as an input leaves F OPEN and does not satisfy the matrix-derived criterion."

No status, priority or completion label changes. The closing sentence is the merged form. Emergence is kept: g and G are composites of the frame, and nothing makes the metric fundamental.

## Checks performed
**Bytes**
- My own script parsed (a)-(m) from review-r1.md and applied them to the r1 blob from c930d87. Each old string occurs once, and the result is byte-identical to the current insert.
- 13992 bytes, sha256 92464fa5ef88d23f589d2ea203a78cc518050d0faa8c6b65d69ae5aed1c5c9be, ASCII, LF, no BOM. The integrator restores CRLF.
- The (f) old string with `\)` was used, as r1 specified.

**Scripts, run on copies outside the repo**
- s6 output is identical to the saved r2 output.
- compile_check gave exit codes [0,0,0,0] for baseline (325 pages) and with insert (329 pages), with no undefined references or citations and no multiply defined labels.
- s1-s5 and s7 were not re-run. Their text and numbers are unchanged from r1, which re-ran them byte-identically. Rendered pages were not inspected.

**My own code (gk6.py)**
- **Geometry:** R = 26, Riem^2 = 4292/27, e = -1/12, complete 1783/648, frozen 3125/648 at (5,3). Also an off-axis point with R = 46 = 18 x (35/9) - 24.
- **Coefficient algebra (symbolic):** c_T^TT, its V/T form, and all three replica gaps are exact as printed. The helicity-1 deviation from linear interpolation in phi is exactly W_R^(1)(x-1)^2/(20x).
- **Printed inequalities, numeric:**
  - F(M) > 0 on a grid, with F M_t^2 >= 1/5 (minimum 0.2).
  - B_0 >= B_1 for positive and negative x.
  - Peierls-Bogoliubov: 60 random Hermitian draws with so(6) vector and spinor generators, all positive. Minimum relative index part 0.185 and 0.183.

**By hand, each changed claim**
- **(c) projected coefficients:** matches L2409. Transitions to J' = 2 are carried by B_i.
- **(d) connection:** Gilkey's form gives omega = d phi - B/2 and E = E_0 - B.B/4, because W = (1/2) rho^-1 d(rho B) = 0. This is the -(D^2+E) convention of L248, and rho/sqrt|g| = m^3 reproduces the merged density (5m^2 - 3l^2)/(4m^6).
- **(e) index density:** from Z = -i Sigma T, (1/4) g tr_D ZZ = X/2. Then L335's X = 2T + (3/2)S^2 + 2V.V with V = -2 d phi gives the displayed identity, including the sign flip of A^2 between eta and delta.
- **(f) normalisation:** the Gaussian moment gives order s = (s/4) g tr ZZ, hence -sqrt|g| R and -EH for a phase-averaged wave. Q_1 = m^4 IX_1 holds at unit amplitude, consistent with the merged L2413 and with the order s of the frozen second variation.
- **(g) frozen value:** 4(1-xi)e^{-xi/2} gives (5/8)theta^2 = 3125/648.
- **(h) Dirac weights:** tr(R/6 + E_D) = -R/3, independent of phi. So the Dirac weight minus four scalars gives (pi/9)R - (8pi/3)e, and the spin term gives -(pi/3)R_ijij. The 4 pi ratio is 1/(4 pi) against 1/(4 pi)^2. The deltas of L248 reproduce the printed surface density.
- **(i) literature:** see below.
- **(j) scale argument:** it stays labelled as a scale argument. The squared-component comparison is correct.
- **(k) pole:** follows from the printed finite limits, which are at the leading symbol.
- **(l) TT coefficient:** IX2 = -(6/5)(4 + 1/x) at phi = 0 confirms the equality at fixed q is only the rotation. Limits are -24/5 and 2/5. The coefficient 7/30, -14/5 is exact.
- **(m) scope:** the sign claim is restricted to zeroth order in the background torsion, with no sign for M <~ coth^2 tau.
- **Frozen integrals:** brute Gaussian moments by hand give 4(1-xi)e^{-xi/2} and 2 + 2(1-4xi)e^{-2xi}. F(M) follows from the phi part of the second variation. F(0) = 3.2/theta^2.

**r1 findings and rulings**
- Findings 1-8 are closed by (a)-(m).
- Finding 9 is closed: proposal-r2 withdraws "the only route" at section 5 and in "Remaining open step". The phrase survives only in negated form (L192, L377, L407).
- All six rulings are adopted and the avenue list follows r1. Proposal Result items, sections 2, 4, 7, 8, 9, 10, 11 and the claim table match the rulings.

**Literature: arXiv:2411.02598, fetched PDF**
- A whole-text search for polarization, polarisation and related terms finds no statement of one coefficient across polarisations.
- (3.32) says "the Einstein Hilbert action is part of the one-loop effective action". (3.33) identifies G_N. That is a decomposition, not a polarisation statement.
- The Discussion leaves the hs-mass hierarchy open.
- Final insert wording: "The sections compared make no statement of one coefficient on the five polarisations: that is a criterion of this ledger, which is neither established in that work nor contradicted by it." It implies neither reading, and the whole-text search supports the broader phrase "in that work". The JHEP version and 2601.08031 are not independently verified, and PDF extraction garbles symbols.

## Findings
**1. Minor. Location: closing paragraph, "which on the null cone requires the components of \(mq\)".**
- *Finding:* the insert compares `mq` with the scale of K at a different power from its own "The range" part.
- *Reason:* L2405 measures the scale of K by M, in units of Box. "The range" part, as corrected by (j), uses "squared components". Proposal section 11 says "below sqrt M". The cross term has singular values of order m|q|J. Its relative effect, of order (m|q|J)^2/(M + mu_J)^2, peaks at J ~ sqrt M at (mq)^2/M. So the squared form is the actual condition when n reaches sqrt M. The printed sentence is not false as a necessary condition for M > 1, but it understates the hypothesis and is dimensionally inconsistent with the same paragraph.
- *Action:* replacement (n).

**2. Minor. Location: "Dependence on the wave vector" and "Sign and replicas", B_0 and B_1.**
- *Finding:* the labels B_0 and B_1 are not defined anywhere in the manuscript.
- *Reason:* the merged L2409 has only "the corresponding sums B_i(s)", with no assignment of indices. The printed inequalities B_0 >= B_1 > 0 and T_2 >= T_1 depend on the normalisation 6a(1-a), which matches s5 `m0`, `m1n` and 046 s2. A reader cannot check them literally as written.
- *Action:* replacements (o), (p).

No other finding. Every other printed inequality I tested holds literally.

**Rulings on the job's questions**
- No PRIOR-CLAIM-ERROR. The merged L2413 and L2415 are true as scoped.
- Milestone: none. M1-M5 are not met, by the same reasoning as ruling 5. This is a narrowing within a class already bounded by frozen symbol, J = 0 and first-order torsion.
- Not a breakthrough. SME consultation is not needed.

## Scope of what is established
- **Exact or established:**
  - closed forms in the frozen setting;
  - background Casimir and spin-connection identities;
  - W = 0;
  - the index identity;
  - frozen integrals and F(M);
  - c_T^TT algebra;
  - Peierls-Bogoliubov positivity, assuming V_i, T_i finite.
- **Conditional:**
  - the mixed term as a (g, phi) functional (J = 0 with projected coefficients, axial and d phi zero at first order);
  - the cone cross term (delta content as flagged at L254);
  - the replica gaps (merged cone values, no contacts, zeroth order in the background torsion);
  - the first-term cone shift (L not computed).
- **Mechanism only:** the scale argument for M >> coth^2 tau.
- **Open:** B and F stay OPEN and PROGRAMME-CONDITIONAL. Nothing is DERIVED.
- **No-go class, exact hypotheses:** rank-6 CP^{1,2} x K; level-one graviton; IKKT content supplied; frozen leading symbol; inert amplitudes zero; product background without mixed flux; cross term dropped; first-order torsion on J = 0 modes; one coefficient on all five traceless polarisations for all q at a base point. It closes no direction outside this class.

**Open avenues, ranked (each stays within emergence, none is the only route):**
1. All-harmonic and inert elimination including the tree form. The obstructing 1/x term is not polynomial in (q, h-bar, y) at fixed h-bar, so it comes from restricting to level one.
2. Torsion on J >= 1 loop modes (relaxes first order on J = 0).
3. The on-shell TT sector: Newtonian coupling, trace polarisation, whether the first-term cone part or contacts can supply the negative mixed gap, and replica selection (Problem A).
4. Second variation of the complete J = 0 order-s^2 density. Worth testing as a cheap lemma: a local density gives only forms polynomial in q, so it may be unable to cancel 1/x. That would extend the exclusion beyond the frozen symbol. Mind the unit-amplitude factor.
5. S^2-M fibre-flux part with the cross term kept (needed for the size of the cone shift).
6. Equivariant K or mixed M-K flux.
7. A J = 2 or hs-mode graviton; other presentations (M^{A5}, non-product).
8. Construction of a K with f_1 = f_2 + f_3 on every mode (W_R = 0; existence not shown).

## Recommended disposition
Revise. Apply (n), (o), (p) verbatim in r3 with no other byte changed, and re-run s6 and compile_check. A gatekeeper round then checks the bytes and, if chapters-hash is unchanged, relies on this scan. Do not integrate on this review.

## Corrected snippet
These add no new physics and no new assumptions. They name weights already used in the 046 and 047 scripts and align one power with the insert's own text. Each old string occurs exactly once in the current insert. Applied to a scratch copy, the result is 14281 bytes, sha256 d722bd481556f125bdd9974762c0f040e970eab24021f887c91889afd2d98d2b. s6 was re-run on it (first six output lines inspected, no problem). compile_check passed with exit codes [0,0,0,0], 329 pages, no undefined references or citations, and no multiply defined labels.

(n) `which on the null cone requires the components of \(mq\) to lie below the scale of \(K\).`
-> `which on the null cone requires the squared components of \(mq\) to lie below the scale of \(K\).`

(o) `with \(\tau^K\ge0\) and \(B_0>0\), this fails`
-> `with \(\tau^K\ge0\) and \(B_0>0\), \(B_0\) being the sum \(B_i\) of the preceding paragraph with the weight \(\int_0^1e^{-s\Delta a}\,\mathrm da\) of the torsion vertex, this fails`

(p) `and \(B_0\ge B_1>0\) pointwise.`
-> `and \(B_0\ge B_1>0\) pointwise, \(B_1\) being the sum \(B_i\) of the preceding paragraph with the weight \(6\int_0^1a(1-a)e^{-s\Delta a}\,\mathrm da\) of the term \(F_1\) there.`

## Files
- Proposal: `C:\Users\redgi\Projects\namcg-lab\proposals\047-lichnerowicz-torsion-closed-forms\proposal-r2.md`
- Insert: `C:\Users\redgi\Projects\namcg-lab\proposals\047-lichnerowicz-torsion-closed-forms\appH_insert.tex`
- Previous review: `C:\Users\redgi\Projects\namcg-lab\proposals\047-lichnerowicz-torsion-closed-forms\review-r1.md`
- My byte check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g47r2\chk.py`
- My mathematics check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g47r2\gk6.py`
- My replacement check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g47r2\app.py`
