VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
The insert is exactly r2 plus (n), (o), (p). Every changed claim re-derives against the merged 046 text, and the chapters hash is unchanged. This is a review verdict, not merge approval; only the author merges.

## Source reading
**Method: digest + targeted reads, relying on the full scan recorded in review-r2.md.** I did not repeat the full scan this round.
- **Hash:** my own recomputation, by the `make_digest.py` definition over 30 working-tree files, gives chapters-hash 1416784d1e1634a9. That is the hash review-r2 scanned, so the ordinal-45 scan requirement is met by that record. `--check` printed DIGEST CURRENT (head 57d63ef).
- **Working tree:** dirty-chapters: yes. `git status` shows only appH modified. `git diff --stat` shows 15 insertions; I did not separately open that diff to attribute it to 046. The ledger records 046 as integrated and awaiting the author's commit.
- **Read in full:** review-r2.md; appH_insert.tex; apply_r3_replacements.py; s6 and compile_check; appH L2398-2417, including the whole merged 046 block.
- **Read in part:**
  - proposal-r3.md, through its word diff against r2 plus lines 74, 208, 236, 285, 320 and 382;
  - appH L45-47 and L1366-1369;
  - ledger entries 044-046;
  - 046's s2 weight code and saved output;
  - s5 lines 155-170.
- **Not read:** ch17 prose and MILESTONE.md this round. My grep of MILESTONE.md for M1-M5 returned no lines, so the milestone ruling carries forward from review-r2 with no new claim added.
- **Unreadable files:** none.
- **Process slip:** my first read issued three read-only calls in one batch, against the sequential rule. Nothing changed, and all later calls were serial. All my writes went to the scratchpad; the repo status and the insert sha256 are unchanged.

## Claim under review
Round-3 text of the conditional 047 paragraph on CP^{1,2} x K: closed forms, exclusion of isolated K data at first order in torsion, Lichnerowicz reduction, the range M ~ coth^2 tau, the helicity-two coefficient on the null cone, and the sign and replica gaps.

**Problem B (appH L45-47):** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."

**Problem F (appH L1366-1369):** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating \(G_{\mathrm{eff}}\) as an input leaves F OPEN and does not satisfy the matrix-derived criterion."

The insert changes no status, priority or completion label and claims no critical-path target closed. It closes with "Problems~B and~F remain open and PROGRAMME-CONDITIONAL." Emergence is kept: nothing makes the metric fundamental, and the insert disclaims identifying \(\bar h\) with the emergent metric.

## Checks performed
**Bytes (direct)**
- My script parsed (n), (o), (p) from review-r2.md and applied them to the blob `b9c8b10:appH_insert.tex` (13992 bytes, sha256 92464fa5...). Each old string occurs once.
- The rebuild equals the current file: 14281 bytes, sha256 d722bd481556f125bdd9974762c0f040e970eab24021f887c91889afd2d98d2b, ASCII, LF, no BOM.
- A character diff shows exactly three insertions and nothing else. The integrator restores CRLF.

**Scripts, on copies outside the repo**
- s6 output is identical to `s6_insert_mechanics.r3.out.txt`. The r3 output differs from r2 only in the byte count.
- compile_check output is identical to the saved r3 output: exit codes [0,0,0,0], 325 pages baseline and 329 with the insert, no undefined references or citations, no multiply defined labels.
- The anchor `\section{Problem G: HBEV}` occurs once, and the line before it is the 046 closing sentence. So "the preceding paragraph" means the 046 paragraph, as intended.
- s1-s5, s7 and 046's s2 were not re-run, because no computation changed. For L_2 and the F_1 assignment I relied on the saved s2 output and code. Rendered pages were not inspected.

**(o) B_0**
- Merged L2409 reads: "The torsion vertex is already of order q^2, so its weight is \(\int_0^1e^{-s\Delta a}\,\mathrm da\)". The insert's wording matches it.
- From the merged definitions, B_i(s) = sum_{J,J'} (2J+1) c(J,J') e^{-s mu_J} w_i(s Delta).
- With this B_0, my closed-form evaluation for tau^K proportional to s^2 e^{-sM} gives beta_X = 0.065, 0.400, 0.859, 0.964 at n = 30, M = 0.01, 0.1, 1, 8. The merged table prints 0.065, 0.40, 0.86, 0.96, so this reading is the one that produced the merged numbers.
- W_X^(2) = -(1/8) int s^-2 tau^K B_0 then follows from merged L2383 and the second-harmonic split.

**(p) B_1**
- The merged F_1 weight is a(1-a), and int_0^1 a(1-a) da = 1/6. So 6 int a(1-a) e^{-s Delta a} da is the normalisation with B_1 = D for degenerate levels.
- The merged calibration (1/4)(F_1/6 + F_2/3) agrees: the F_1 part carries 1/6 and the F_2 part 1/3.
- In 046's s2, L1 is the F_1 part. Its saved output shows (1/6)L_F1 + (1/3)L_F2 = SC2 - SC1 exactly, and the F_2 leak is zero in the eigenvalues I inspected (truncated output lines at three of the seven points). That matches the merged "L_2 vanishes on the five". Hence the coefficient of L_1 is W_R^(1) = V_1 - T_1 with weight B_1.
- Index labelling is consistent: T_1 uses B_1 and T_2 uses B_0, so W_X^(2) = -T_2/8.

**B_0 >= B_1 > 0 pointwise (proved by hand, term by term)**
- With K(a) = 1 - 6a + 6a^2 and f = e^{-ua}, two integrations by parts give int K f = (1/2) int a^2(1-a)^2 f'' da >= 0 for every real u. So J -> J-2 is covered, with equality only at u = 0.
- w_1 > 0 because a(1-a) > 0.
- (2J+1)c(J,J') >= 0 and is symmetric (checked exactly for J up to 7). Sum_{J'} c(J,J') = 1 for J >= 1, and c(1,1) = 2/5.
- So B_0 >= B_1 > 0 for all s at n >= 1. The inequality is an equality at n = 1, where only Delta = 0 survives.
- Numeric check in stable form: no violations for n = 1, 2, 3, 5, 30, 300 and s from 1e-4 to 100.
- For n = 0 the sums vanish, but no J = 1 level exists, so the level-one setting already requires n >= 1. No text change is needed.

**(n) squared components**
- Merged singular values are of order 2m|q|J. The relative effect at level J is (2m|q|J)^2/(M + mu_J)^2.
- At large M, J^2/(M + J^2)^2 has maximum 1/(4M) at J^2 = M, so the peak is (mq)^2/M. Squared components below M is the correct condition where the paragraph uses it (M >> coth^2 tau >= 1), and it matches the insert's own "The range" part.

**Downstream algebra (symbolic, residual exactly zero)**
- (1/6)W_R - 2W_X = V_0/6 + T_0/12.
- c_T^TT = V_0/6 + T_0/12 + (7/30)(V_1 - T_1) + (7/20)T_2. Positivity follows from T_2 >= T_1: the mixed part is at least (7/30)V_1 + (7/60)T_1.
- Periodic and smooth gaps as printed, taken against merged L2398.
- The fixed-state mixed gap reduces by hand to the same two mixed terms and is negative.
- Limits: -24/5, 2/5, 7/30, -14/5.
- By hand: the helicity-1 term (x-1)^2/(20x).

**r2 findings and proposal-r3**
- Findings 1 and 2 are closed.
- proposal-r3 lines 208, 236, 285 and 320 match. Its line 236 states the any-real-x form, which I re-derived.
- Its researcher decision to keep "below sqrt M" as an equivalent form in the section 11 table row is correct.
- The r3 diff adds no new claim.

**Literature:** no literature wording changed. The r2 record stands, including its "not independently verified" items. No SME consultation is needed.

## Findings
None blocking, major or minor. No byte must change.

One observation, for the record only: "requires" in (n) is a scale statement for M > 1 with n reaching sqrt M.
- For M << 1 the peak is at J = 1, with relative effect of order (mq)^2. For n << sqrt M the peak is at J = n, and the condition is weaker.
- In both cases the printed condition is stronger than necessary, so it narrows the scope and claims nothing extra.
- The M << 1 regime lies inside M <~ coth^2 tau, where the insert defines no two-derivative coefficient and claims no sign.
- A later computation that keeps the cross term should use the J-resolved form.

No PRIOR-CLAIM-ERROR. Milestone: none, carried forward from review-r2 because round 3 adds no claim. Not a breakthrough.

## Scope of what is established
- **Exact or established:**
  - closed forms in the frozen setting;
  - background Casimir and spin-connection identities;
  - W = 0;
  - the index identity;
  - frozen integrals and F(M);
  - c_T^TT algebra;
  - B_0 >= B_1 > 0 at n >= 1;
  - Peierls-Bogoliubov positivity, assuming V_i and T_i finite.
- **Conditional:**
  - the mixed term as a (g, phi) functional (J = 0, projected coefficients, axial torsion and d phi zero at first order);
  - the cone cross term;
  - the replica gaps (merged cone values, no contacts, zeroth order in the background torsion);
  - the first-term cone shift (L not computed).
- **Mechanism only:** the scale argument for M >> coth^2 tau.
- **Open:** B and F stay OPEN and PROGRAMME-CONDITIONAL. Nothing is DERIVED.
- **No-go class, exact hypotheses:** rank-6 CP^{1,2} x K; level-one graviton; IKKT content supplied; frozen leading symbol; inert amplitudes zero; product background without mixed flux; cross term dropped; first-order torsion on J = 0 modes; one coefficient on all five traceless polarisations for all q at a base point. It closes no direction outside this class.

**Open avenues, ranked as in review-r2 (each keeps spacetime emergent; none is the only route):**
1. All-harmonic and inert elimination including the tree form. The obstructing 1/x term is not polynomial in (q, h-bar, y) at fixed h-bar, so it comes from restricting to level one.
2. Torsion on J >= 1 loop modes (relaxes first order on J = 0).
3. The on-shell TT sector: Newtonian coupling, trace polarisation, whether the first-term cone part or contacts can supply the negative mixed gap, and replica selection (Problem A).
4. Second variation of the complete J = 0 order-s^2 density. A cheap lemma to test: a local density gives only forms polynomial in q, so it may be unable to cancel 1/x.
5. S^2-M fibre-flux part with the cross term kept, using the J-resolved cross-term estimate above.
6. Equivariant K or mixed M-K flux.
7. A J = 2 or hs-mode graviton; other presentations (M^{A5}, non-product).
8. Construction of a K with f_1 = f_2 + f_3 on every mode (W_R = 0; existence not shown).

## Recommended disposition
Integrate as-is: appH_insert.tex at sha256 d722bd48..., immediately before `\section{Problem G: HBEV}`, with CRLF restored, and run the build check. The author commits and merges.

## Corrected snippet
None.

## Files
- Proposal: `C:\Users\redgi\Projects\namcg-lab\proposals\047-lichnerowicz-torsion-closed-forms\proposal-r3.md`
- Insert: `C:\Users\redgi\Projects\namcg-lab\proposals\047-lichnerowicz-torsion-closed-forms\appH_insert.tex`
- Previous review: `C:\Users\redgi\Projects\namcg-lab\proposals\047-lichnerowicz-torsion-closed-forms\review-r2.md`
- Byte check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g47r3\chk.py`
- Hash, weights, beta_X and algebra check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g47r3\w.py`. Its naive B evaluation overflowed at n = 30, large s, and misreported the n = 1 equality through roundoff; b.py below supersedes that part.
- Stable inequality check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g47r3\b.py`
