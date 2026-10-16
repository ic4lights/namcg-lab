VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
All of F1–F5 are applied as required, and r2 changes nothing else in the LaTeX. The package is a bounded no-go with sharpening. It closes nothing and changes no label.

## Source reading
Digest plus targeted reads in this round. The scope is an r2 diff against my r1 FULL SCAN of all 30 files. `chapters/` is clean (`git status` on chapters and bib shows nothing), so the r1 scan still covers it. Integration ordinal 15 is therefore covered, and I make no new full-scan claim.

## Claim under review
The claim is a bounded no-go on the G_T ≠ G_A gap of integrated proposal 015. This is the normalisation half of B1/B2 in `sec:status-B`. The no-go covers:
- the 't Hooft gauge parameter α;
- an EOM term in the gauge function;
- Dirac content, with the gap depending on the replica gluing.

Current Appendix H labels, quoted verbatim:
- **Problem B:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- **Problem F:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL."
- **Problem A:** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

Chapter 17 `sec:ch17-done` lists A, B, C, D1, E, F, G-derived and N, unchanged. No label change is proposed.

## Checks performed
**Diff of the LaTeX block, r1 against r2.** I extracted both blocks and compared them sentence by sentence. The changes are exactly these:
- **F1.** The tip-domain justification ("a different choice of domain changes it by an α-independent amount, because a finite set of angular modes has a scale-free transverse trace") is deleted. It is replaced by "This depends on that choice of domain; other choices are not examined." ✓
- **F2.**
  - "numerical second-order evaluation" and "values, matched by the rational forms" are in.
  - "rational fits to 2×10⁻³, not derived; α = 1/3,…,3 only" is in.
  - The gap 2Λ²/π is stated for the tested range 1/3 ≤ α ≤ 3.
  - "for every α>0" appears only for J=0 backgrounds under the stated conditions.
  - The sentence that the TT value agrees with the exact lemma is kept. ✓
- **F3.**
  - The antiperiodic prescription is now named as the polar-frame / spinor-transported one, "not the unrotated pull-back gluing used above for a^μ".
  - The periodic result is reported: c_A(Dirac) = −2/3, gap 4−2n_D, zero at n_D = 2 with c_T = c_A = 0. It is labelled "an equality of vanishing Λ² coefficients, not a derivation".
  - "The gluing selected by the matrix state is not determined here."
  - The closing statement reads "2 for antiperiodic and 0 for periodic gluing".
  - Problem A and the modular flow are named in the scope sentence.
  - "Numerology" is dropped and the r1 claim "not the replica of a state" is withdrawn. ✓
- **F4.** `\mathcal G` becomes `\mathrm{Gr}` and E_ν becomes `\mathfrak J_\nu`, consistently, including in the gauge-function sentence. E_f stays the endomorphism, and the unrenamed E in the "E=0" phrases is now `\mathfrak J=0`. Neither macro occurs anywhere in `chapters/`. ✓
- **F5.** The clause "the Yukawa couplings Γ^i[X̂_i,Ψ] to the N_s transverse matrices vanish on the background and are dropped" is added. ✓
- **F6.** No edit, as I stated in r1.
- **No other changes.** The diff shows nothing beyond the items above: the dropped "not the value −2/3 of periodic gluing" clause and the rewording of the nearby sentences are covered by F3.

**Insert file and anchor.**
- `appH_insert.tex` is identical to the r2 proposal block (script comparison with CRLF normalised: True).
- The anchor sentence ("they give no value or sign of \(G_{\mathrm{eff}}\). Problems~B, C, D, F and~G remain open.") occurs once, at appH line 179 (`grep -cF` gives 1).
- `\section{Problem C: conformal mode and Cassini}` occurs once, at line 181.
- The insert goes between them and replaces nothing.

**Labels and macros.**
- `rem:ch3-trace-quadratic` is defined in ch03.
- `eq:O-eta` is defined in ch08.
- `ass:EE` is defined in ch06.
- Each is defined once; no label is added.
- `\LUV` is defined in the preamble, and the bib keys IKKT1997 and Solodukhin2011 exist (checked in r1).
- The block has no process language and no consecutive repeated status lines. One scoped closing sentence ends paragraph 3 only.

**Re-run of `gap_periodic.py`** (with `python -I`). Output matches the stored `gap_periodic.out.txt`:
- antiperiodic gap 4−n_D;
- periodic gap 4−2n_D;
- D=10 content: c_T = 0, c_A = 2 (antiperiodic) and 0 (periodic);
- ρ²X coefficient 1−n_D/2, which is 0 at n_D = 2.

This agrees with my r1 hand arithmetic.

**Carried over from r1, not re-derived this round:** the gauge lemma (hand check plus independent exact-rational check), the decomposition algebra, the Dirac a_1, and the Solodukhin equations (126)–(127), (136) and (147).

**Not independently verified (unchanged):**
- The off-shell TT and third-mode closed forms are numerical fits (I re-ran one point in r1).
- The EOM-gauge-function shift was not re-run.
- `cone_twist_zeta.py` was cross-checked only against Solodukhin ratios.
- Steinacker arXiv:2303.08012 was not opened, and no number from it is used.
- The block does not cite it.

## Findings
None blocking or major. One non-blocking remark, no action required: the proposal's "Changelog" and "Decisions Taken" sections contain process language. They are not part of the LaTeX block, so this is not an issue.

## Scope of what is established
**Established identity:** O_v Gr = Gr O_s − {𝔍,·} and Gr†Gr = O_s, for any Poisson bivector.

**Conditional (J=0 backgrounds, stated tip domain, zero modes, one cutoff on O_κ):**
- the decomposition, with a_1 = ((3+α)/6)ρR + ρ²X and area coefficient (3+α)/6;
- hence α-independence of c_A − c_T = 4 for that domain.

**Numerical fits, 1/3 ≤ α ≤ 3 only:** the off-shell TT and third-mode eigenvalues, and the EOM-term shift.

**Established algebra plus numerics:** the Dirac a_1, the Dynkin ratio and the weights, giving b_total = 1 − n_D/2.

**Conditional on gluing:** the gap is 4−n_D (antiperiodic polar-frame), 4−2n_D (unrotated periodic; 0 = 0 at n_D = 2, not a derivation), or 3−n_D / 5−n_D (rotated vector, continuation-dependent).

**Input, not derived:** the identification n_D = 2, N_s = 6 with the 10D content.

**No-go class:** Poisson limit, Euclidean section, one loop, Λ² term, the two δρ=0 modes of a^μ, replica (I) with the stated gluing and tip domain, constant Θ̄, and linear gauge families D·a (+ c𝔍·a).
- Hypotheses relaxed: Feynman gauge, no fermions.
- Hypotheses not relaxed: Λ² order; tensor block = δρ=0 modes of a^μ; gluing and tip-domain choice; Moyal corrections; constant Θ̄.

**Problems B, F and A remain OPEN** with labels unchanged. B is OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. Nothing here derives ass:EE, stationarity, the map Θ → G, or a value or sign of G_eff. Spacetime stays emergent (G is built from Θ).

**Ranked open avenues (as r1; the proposal lists the same):**
1. Next-order coefficients (log / a_2, Moyal) in the D=10 content, per gluing. Most promising: at n_D = 2, N_s = 6, c_T = 0 for all gluings, and c_A = 0 or 2.
2. Replica gluing and internal-index rotation from the matrix modular flow (a Problem A sub-lemma; resolve the non-analyticity at n = 1).
3. Tensor-block identification (Φ–a mixing, torsion irreducible parts of ρ²X).
4. Explicit non-constant J=0 Poisson backgrounds.
5. Other gauge functions, α ≥ 4 with a better grid.
6. Tip domain and edge modes for the non-minimal operator.
7. The tree-level (014) class, Moyal and curved backgrounds.

BREAKTHROUGH: no. M2 is justified narrowly: two relaxations that the manuscript left open, the gauge parameter and the fermion content at Λ² order, do not close the gap within the stated class.

## Recommended disposition
Integrate as-is.

**Exactly what is accepted:**
- The two `\paragraph{...}` blocks and the closing paragraph of `proposals/017-GT-GA-gap/appH_insert.tex`. This is byte-identical to the r2 LaTeX block, modulo CRLF; the integrator must write CRLF.
- Target: `chapters/appH-microscopic-proofs.tex`, inserted after line 179 (end of the 015 block in `sec:status-B`) and before `\section{Problem C: conformal mode and Cassini}` at line 181.
- Nothing is replaced and no label is added.
- No other file is touched, and there is no ledger, Chapter 17 or label change.
- The proposal's research text, tables and claims beyond the LaTeX are not accepted as manuscript content; they are supporting evidence only.

## Corrected snippet
None needed.
