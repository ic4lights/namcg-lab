VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2

## Verdict
The n_D-scope arithmetic and the (6,2) ledger are correct and all scripts reproduce, but the "Sectors with a scale" sub-paragraph says the Kaluza-Klein comparison "is not examined" when integrated text in `sec:status-F` (appH L2673-2694) already computes it, and the "trace of rho^n" sentence drops the state hypotheses it rests on.

## Source reading
Digest + targeted reads. **The every-5th-item full scan was NOT completed in this round, and I do not claim it.**

- Digest: `DIGEST CURRENT` at HEAD 20741cb, `dirty-chapters: no`, all 30 files unchanged, no duplicate labels.
- Read in full:
  - `chapters/ch17-agenda.tex` (whole file);
  - `chapters/appH-microscopic-proofs.tex` L1-1001 (Problems A, B, C and D to L1001), L2377-2410 and L2673-2720.
- Grep only: all other chapters for `n_D`, `kappa_X`, `c_A`, `G_A`, `IKKT`, `Kaluza`, `Steinacker2023`, `DonnellyWall2016`. Outside appH only ch03 L158, L883 and ch09 L192 mention IKKT, and none touches the insert. Within appH outside `sec:status-B` the B quantities appear at L2690, L2701, L2718 and L2758.
- Not read: appH L1002-2376, L2411-2672, L2721-3378, and the other 28 chapter files.
- Why deferred: the verdict is not ACCEPT, and 067 (ordinal 64) will change appH before this item can be integrated. The ordinal-65 full scan must be done on the post-064 tree in the round that would issue a plain ACCEPT. Even this partial scan produced major finding M1.
- No file was unreadable.

## Claim under review
- **Claim (i).** For every content, `c_A - c_T = 4 kappa_X + n_D` and `(c_A - 1) - c_W(-1) = n_D/2`. So "gap = 4 kappa_X", "c_A - 1 = c_W(-1)" and "3 kappa_X remains" (appH L414, L425, L427) hold at `n_D = 0` only.
- **Claim (ii).** At `(N_s, n_D) = (6,2)`, order Lambda^2, the tensor side vanishes in every presentation and the only nonzero entry is the fixed-state `c_A = 2`.
- **Claim (iii).** For formal constant masses the comparison reduces to `S_n`, `S_kappa`, and whether Kaluza-Klein towers give such sums "is not examined".
- **Target: Problem B.** appH L76-78 verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived." ch17 L123: "*CRITICAL PATH; OPEN.*" The original target is `delta S_D = 0` at fixed volume for the tensor block from the microscopic action, with the map `g^(0) -> g`.
- No label change is proposed, and none is warranted.

## Checks performed
**Reproduction pack (all re-run).**
- `s1_weighted_a1.py`: 88 s, all residuals 0, `S1 PASS`, matches the working-tree output.
- `s2_mode_ratio.py`, `s3_content_ledger.py`, `apply_check.py`: output byte-identical to the saved files.
- Apply check: anchor occurs once, CRLF only, both cite keys have one bib entry, balance 0/0/0/0, insert lies inside `sec:status-B`, no `Status:` or `Priority:` line. Result 632476 bytes, sha256 ee3a885f...
- `\LUV` is defined at `namcg-book7.tex` L54, and `booktabs` is loaded.
- The committed (HEAD) copy of `s1_weighted_a1_output.txt` ends in `S1 FAIL`: trial 0, residual (c), contained a surd in an exact-rational computation. The working tree replaces `nsimplify` by `simplify`/`expand` and sorts the monomials, and now passes. The proposal does not mention this (finding m5).

**Re-derived by hand from L208, L220, L227, L338, L357, L370.**
- `c_R = N_tot/6`, `kappa_X = 1 - n_D/2`, `c_T = c_R - 4 kappa_X = N_s/6 + 4n_D/3 - 11/3`.
- `c_A = c_R + n_D`, `c_A^per = c_R`, `c_A^sm = -c_R/2`, `c_T^ext = c_R - 2 kappa_X`, `c_W(r) = c_R + kappa_X r`.
- All four displayed identities, and every entry of the table at general content, (6,0) and (6,2).
- `1/G_A = Lambda^2/pi` from `1/G = c Lambda^2/(2 pi)` with `c = 2`.
- `f(m^2) = Lambda^2 E_2(m^2/Lambda^2) = Lambda^2 - m^2 ln(Lambda^2/m^2) - (1 - gamma_E) m^2 + O(m^4/Lambda^2)`.
- One bosonic and one fermionic mass: `S_n = 8(f_b - f_f)`, `S_kappa = f_b - f_f`, so `c_T = -8/3 (f_b - f_f)` and `c_A^per = +4/3 (f_b - f_f)`.

**Clause from L259-300 (the researcher's question).**
- The gaps 0, 2, 0 and `kappa_C^T = 0` follow from L296-298 at `n_D = 2`.
- The quadratic part of `int rho^2 S_4` about constant Theta-bar vanishes: `b_sigma = O(epsilon)`, so `S_4 = O(epsilon^4)`. This agrees with the independent L296 value `kappa_C^T = 0`.
- The clause is sound in substance but conditional on the sampled-jet identity "weighted a_2 = S_4/2" of L259, and the phrase "has no quadratic form" is imprecise (finding m2).

**F8.** The order of limits is named. The state is not named where "trace of rho^n" is used (finding M2).
**F10.** No other chain's passage is cited. That is the problem: the relevant one is ignored (finding M1).
**Citations.** The `DonnellyWall2016` and `Steinacker2023` bib entries exist. Their content was not re-fetched and is not independently verified here; both are used as in the already-integrated L235, L265 and L2680-2692, except as noted in m3.
**Not verified.** No LaTeX build. The sampled-jet identities of L259 and L296 were not re-run.

## Findings
**M1. Major. "Sectors with a scale", last two sentences; proposal Result 3, avenue 1, Decisions 4-5.**
- Finding: the insert says "Whether the Kaluza--Klein towers of fuzzy extra dimensions ... give sums of this form is not examined." Integrated text contradicts this.
- Reason: appH L2673-2694 (product backgrounds `M x K` at the maximally supersymmetric content) already computes the comparison in a class with a scale:
  - `c_T = W_R/6 - 4 W_X`, `c_A^per = W_R/6`, `c_A^sm = -W_R/12`, and a fixed-state value;
  - `W_X < 0` for nonzero flux of `K`, so the periodic gap `4 W_X` is nonzero;
  - the term that would carry `S_kappa`, namely `s_0^K (v^M - 2 sigma^M)`, "has no two-derivative part", because the scalar operator of `K` is common to all species;
  - the index weight enters through the mixed term.
  L2696-2848 then follow this up with bounded no-gos.
- Consequences:
  - "not examined" is false for the manuscript;
  - "not vacuous only in a class with a split spectrum, where it reduces to the two sums S_n and S_kappa" holds for the formal shift only, and is not the structure of the actual product class;
  - the proposal's top-ranked avenue and the suggested new frontier edge "B.kk-spectral-sums" duplicate integrated work.
- Required action: read L2673-2848. Replace the two closing sentences by a statement that matches L2682-2690 and quotes its caveats (see Corrected snippet), or delete the sub-paragraph and keep one pointer sentence. Correct the fork table row H1 and the avenue ranking.

**M2. Major. "At N_s=6, n_D=2", sentence "for the trace of rho^n of the paragraph on fermion replica gluing 1/G_A = LUV^2/pi".**
- Finding: the opening says "No state of the matrix model enters", yet this sentence gives a value "for the trace of rho^n" without its hypotheses.
- Reason: the identification of the fixed-state replica with `Tr rho^n` is conditional (L225-229) on a quasi-free state of the Poisson-limit fermions, rotational modular flow, the less singular extension and uniqueness of the continuation from integer `n`. L285 and L302 elsewhere describe the fixed-state replica as "not the trace of the n-th power of one state". The final scope sentence's "with their hypotheses" is too far from the claim to satisfy F8.
- Required action: name the hypotheses in that sentence (see Corrected snippet). Do not sharpen the L227 / L302 tension. That tension is pre-existing wording and not an error of this package; I do not flag PRIOR-CLAIM-ERROR, but the researcher should note it for a later package.

**m1. Minor (required). Same sub-paragraph, "the vector holonomy contact of modulus 1, the edge-mode value of [DonnellyWall2016] for a Maxwell field if the state carries that sector, changes it to 1 on n<1 and 3 on n>1".**
- Finding: the Donnelly-Wall / Kabat value is `-1` (L235, L242, L427). The `n > 1` value `+1` is the branch of the holonomy contact `-alpha_v sigma` (L340), not an edge-mode value.
- Required action: attach the apposition to the `n < 1` value only. L242's caveat (the contact "remains an input and is not a prescription of this class" in the variables `(G, rho, dTheta)`) should stay visible; "if the state carries that sector" covers L427 only.

**m2. Minor (required). Log-order clause.**
- Finding: "has no quadratic form about a constant Theta-bar" should say the coefficient vanishes at quadratic order, and should state its basis.
- Required action: reword to "vanishes at quadratic order about a constant Theta-bar, given the sampled-jet identity of that paragraph". Add "about a constant self-dual or anti-self-dual Theta-bar, on the n<1 branch" to the `W`-gap statement (L296, L304). "Has the same pattern" should allow for L300's remark that the completed gap has no Lambda^2 counterpart.

**m3. Minor (required). "for which [Steinacker2023] attributes the Einstein--Hilbert term to a mixed quartic term and not to a mass shift of a_1".**
- Finding: the negative half is the manuscript's comparison, not a statement of the cited paper.
- Required action: remove it. This is absorbed by the M1 rewrite.

**m4. Minor (recommended). "Sector data" and the sentence "The gap of the fixed-state replica has two parts of different origin ...".**
- Finding: this restates L227 ("the sum of the weight of rho^2 X and the excess +1 per Dirac field") and L231 ("it enters the area side only"). Most (6,2) entries are already at L220, L227, L235, L246, L353, L366, L370.
- Net new content of the package: the `n_D`-scope identities, the consolidated table, and the area side of the formal mass shift.
- Recommended action: replace the duplicated sentence by a back-reference, under the smallest-text rule. The proposal's "refinement the adversary did not state" is already in appH and should not be presented as new.

**m5. Minor (proposal file only).**
- Finding: the earlier `S1 FAIL` and the script change are not disclosed. The expected result hash will also be stale once 067 is integrated.
- Required action: state the earlier failure and its cause in the Verification section. Note that the integrator must re-run `apply_check.py` on the post-064 tree.

## Scope of what is established
**Proved (algebra, given the manuscript's sector values).** The four content identities and the table. The `n_D = 0` scope of "4 kappa_X", "c_A - 1 = c_W(-1)" and "3 kappa_X" is correct. L400-429 are scoped to `n_D = 0` (L400, L416, L419, L429), so there is no prior-claim error in appH. The defect is in the frontier edge `B.matrix-state-edge-sector`.

**Conditional.**
- Sector data: four sampled jets and four sampled modes.
- All `c_A` values: inherited replica prescriptions, tip domain, quasi-free state.
- The log-order pattern: sampled-jet identities of L259 and L296.
- The mass formulas: formal shift, no gauge-invariant mass term.

**No-go class (exact hypotheses).** Four matrix coordinates; Poisson limit first, then one common proper-time limit; Euclidean section; one loop; alpha = 1; content (6,2) with Yukawa couplings dropped; order Lambda^2 (and the `W` coefficient at log order on self-dual or anti-self-dual Theta-bar); the two `delta rho = 0` modes; replicas periodic, fixed-state and first-order smooth. Within this class the `G_A` against `G_T` comparison is `0 = 0` or `2 != 0` and fixes no Newton constant. It closes nothing beyond these hypotheses.

**Open avenues, ranked.**
1. Product and conjugate-coordinate classes with a scale. These are already begun at L2673-2848, not a new edge. The live sub-questions there are the first-term cutoff-dependent parts of the fixed-state `c_A`, the range `M ~ coth^2 tau`, and construction of `K`. Serialize with the F chain.
2. The replica and Dirac tip domain selected by a matrix state (A intersect B). A state whose replica is periodic or smooth leaves `0 = 0` at Lambda^2 and moves the test to (1).
3. Moyal corrections at the cutoff, which break the `N_tot = kappa_X = 0` cancellation scale by scale.
4. Finite terms and two loops at (6,2).
5. Yukawa couplings off the background.
6. Sector-dependent proper-time limits. This is an input unless derived.

**Classification.** PROGRAMME-CONDITIONAL. Problem B stays OPEN, CRITICAL PATH. Not a breakthrough.

## Recommended disposition
Revise (r2).

- Apply M1, M2 and m1-m3; consider m4; fix m5 in the proposal.
- Orchestrator: the frontier correction "(n_D = 0 only; 0 = 0 at the IKKT content)" for `B.matrix-state-edge-sector` is justified. Do **not** open "B.kk-spectral-sums" as a new edge; point it at appH L2673-2848.
- The ordinal-65 full scan is still owed and must precede a plain ACCEPT, on the tree after 067 is integrated.

## Corrected snippet
These quote existing appH text only and add no assumption. The researcher must check them against L225-229 and L2673-2694. The M1 replacement adds one `\ref` to the existing label `sec:status-F`.

**(M2)** Replace "for the trace of \(\rho^n\) of the paragraph on fermion replica gluing \(1/G_A=\LUV^2/\pi\) while \(1/G_T=0\)" by:
```latex
for the fixed-state replica, which is the trace of \(\rho^n\) only under the hypotheses of the paragraph on fermion replica gluing (a quasi-free state of the Poisson-limit fermions with rotational modular flow, the less singular extension and a unique continuation from integer \(n\)), \(1/G_A=\LUV^2/\pi\) while \(1/G_T=0\)
```

**(m1)** Replace "the vector holonomy contact of modulus \(1\), the edge-mode value of~\cite{DonnellyWall2016} for a Maxwell field if the state carries that sector, changes it to \(1\) on \(n<1\) and \(3\) on \(n>1\)" by:
```latex
the vector holonomy contact of modulus \(1\) changes it to \(1\) on \(n<1\), the value \(-1\) being that of the edge-mode term of~\cite{DonnellyWall2016} for a Maxwell field if the state carries that sector (an input, not a prescription of this class), and to \(3\) on \(n>1\)
```

**(m2)** Replace "has no quadratic form about a constant \(\bar\Theta\)" by:
```latex
vanishes at quadratic order about a constant \(\bar\Theta\), given the sampled-jet identity of that paragraph
```

**(M1, m3)** Replace the last two sentences of "Sectors with a scale" ("At this content the comparison ... is not examined.") by:
```latex
For this formal shift the comparison at this content is thus not vacuous only for a split spectrum, where it reduces to the two sums \(\mathsf S_n\) and \(\mathsf S_\kappa\). The product backgrounds \(M\times K\) of the paragraph on product backgrounds in Section~\ref{sec:status-F} are not of this form: there the scalar operator of \(K\) is common to all species, the term that would carry \(\mathsf S_\kappa\) has no two-derivative part, and the comparison is \(c_T=\tfrac16W_R-4W_X\) against \(c_A^{\mathrm{per}}=\tfrac16W_R\), with \(W_X\) from the mixed term of~\cite{Steinacker2023}, so that \(W_R\) and \(W_X\) take the places of \(\mathsf S_n\) and \(\mathsf S_\kappa\) and the periodic gap \(4W_X\) is nonzero for a nonzero flux of \(K\). Those statements are for the Poisson limit on \(M\), a fuzzy space \(K\) that is not constructed and not required to solve the equations of motion, product backgrounds without mixed flux, the orientation-even part of the mixed term and the replicas of this section, and they fix no sign of \(W_R\).
```

Files:
- C:\Users\redgi\Projects\namcg-lab\proposals\070-b-content-class\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\proposals\070-b-content-class\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\proposals\070-b-content-class\s1_weighted_a1.py
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (L205-229, L252-304, L337-429, L2673-2694)
- C:\Users\redgi\Projects\namcg-lab\chapters\ch17-agenda.tex (L121-137)
- C:\Users\redgi\Projects\namcg-lab\reports\graph\frontier.yaml (edge `B.matrix-state-edge-sector`)
