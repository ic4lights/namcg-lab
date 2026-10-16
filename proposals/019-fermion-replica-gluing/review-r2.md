VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
The r2 text applies F1–F5 exactly. I re-checked the algebra, scripts, anchors and BibTeX records and read the full chapter manifest. The conditional resolution of the fermion gluing and the Q10 character identification are sound, correctly scoped, and change no label.

## Source reading
**Full scan, done this round.** The digest is stale (`DIGEST STALE`, dirty chapters, as announced), so CLAUDE.md 3(c)/(d) applies. I read in full all 30 files of `chapters/*.tex`:
- ch01–ch18.
- appA, appB, appC, appD, appE, appF, appG, appH (all 2485 lines, read in chunks), appI, appJ, appK, appL.

`frontmatter/` is outside `chapters/**` and was not read. It is not a named insertion surface.

Findings from the scan:
- The only fermion/gluing/replica-of-spinor text is the 017 block in appH (lines 188–191).
- ch02:499–501 defers spinor bundles and says NAMCG is bosonic at the microscopic level. This is a pre-existing scope note and is compatible with the conditional fermion paragraph.
- ch03:120–139 and ch15/ch16 contain nothing that conflicts.
- ch17 and appH labels are unchanged and consistent. No stale statement is created by the insert.

I also re-ran all six scripts, `curl`ed Crossref for both bib records, and diffed r1 against r2 programmatically.

## Claim under review
Problem B (`sec:status-B`) sub-gap `G_T` vs `G_A`, with the Problem A input (replica gluing from the modular flow). The package claims:
1. The `Tr rho^n` fermion gluing is fixed under stated hypotheses, and the D=10 `Lambda^2` mismatch (`c_A-c_T = 4-n_D`) stands.
2. 017's "periodic" branch and the rotated vector branches are not continuations of `Tr rho^n`.
3. `N_tot` and `b` are the orders `alpha^0` and `alpha^2` of the MST character `Q_10`, and the first survivor is `alpha^4`.

Current labels quoted verbatim from appH:
- **Problem B:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- **Problem A:** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
- **Chapter 17 `sec:ch17-done` (line 691):** the matrix-derived label needs A, B, C, D1, E, F, G-derived and N all DERIVED. H, I and J are optional within their scopes.

I checked ch17 `sec:ch17-bearing`/`coeff` and the appH headers for A, B, C, D, E, F, G, N and found no discrepancy.

## Checks performed
**r1 vs r2 diff (programmatic, LaTeX block).**
- **F1 applied.** "as in the replica of the preceding paragraphs" is deleted. "(for integer spin, the identity at integer \(n\))" is added.
- **F2 applied.** The text now reads "the less singular self-adjoint extension of the first-order operator". It adds that this extension is the one giving an analytic continuation. It also adds that the componentwise-regular domain gives `Sum|a_k| = n/4` or `(n^2-1)/(4n)` by parity of `n`, which is non-analytic. The sentence "Hence \(\sum a_k^2\)…" became "With the less singular extension, …".
- **F3 applied.** The list now reads "the choice of self-adjoint extension, the uniqueness of the continuation from integer \(n\), the domain of the first-order operator, …". The phrase "for the stated extension" qualifies the exclusion of `-2/3` and `4-2n_D`.
- **Extra conditional wording on the rotated branches.** The text reads "if the continuation from integer \(n\) is unique, the rotated branches … are not continuations of Tr rho^n". This is the same content as the F3 snippet, made visibly conditional. It is stronger on scoping, not weaker, and I accept it.
- **F4 applied.** The first paragraph is split in two. The block is now three paragraphs.
- **F5 applied.** `number = {50}` is added to `CasiniHuerta2009`.
- **No other change.**

**appH_insert.tex equals the r2 block.** The string comparison is True (4633 characters). The file has LF endings. The integrator must write it with CRLF per CLAUDE.md. Braces balance (0) and `\(`/`\)` count 88/88.

**Anchors, re-counted in the working tree.**
- "The gluing selected by the matrix state is not determined here." occurs once (line 189, inside the 017 fermion paragraph).
- "…or the Kaluza--Klein sector. Problems~B, C, D, F and~G remain open." occurs once (line 191). It is immediately followed by `\section{Problem C: conformal mode and Cassini}` (line 193, once).
- "Fermion replica gluing" is not yet in appH (count 0).

**LaTeX scope grep.**
- No `a_2`/`W_4`/`f_1`/`f1` occurs outside the sentence "not the \(a_2\) coefficient of the operators".
- The only `\alpha^4` statement is "the order α^4 is (x²−y²)²/16, which vanishes for self-dual or anti-self-dual flux".
- There is no link of this locus to 018's `f1=f2`.
- No `\ref` is added.
- Cites used: `CasiniHuerta2009`, `FursaevMiele1997` (both absent from `bib/namcg.bib`, count 0; to be added by the integrator) and `MantaSteinackerTran2024` (exists).
- `\LUV` is defined at `namcg-book7.tex:54`.
- No label or status text is added.

**Re-derivations.**
- **Cone constant.** `B_2(|a|)+|a| = a^2-|a|+1/6+|a| = a^2+1/6`.
- **k-sum.** `Sum a_k^2 = (n^2-1)/(12n)`. Then `(1-n d_n)F|_{n=1} = -1/6`. For a Dirac field (two blocks, weight −1) `c_A = +1/3`, matching the 017/Solodukhin value.
- **Gap.** `c_A-c_T = 4-n_D`, and `(c_T,c_A) = (0,2)` at `(2,6,1)`.
- **`Sum|a_k|`.** `absk_check.py` reproduces the r1 observation for n=1..9. I spot-checked n=2 (1/2) and n=3 (2/3) by hand.
- **Odd-n ratio.** The regular-domain value is `Sum a^2 - Sum|a| = Sum a^2 - 3 Sum a^2 = -2 Sum a^2`, as stated.
- **Scripts.** `twist_ksum.py`, `q10_check.py` (orders 0–3 vanish, order 4 ratio −3/8 to V_4, closed forms `8−4n_D`, `(n_D−2)(x²+y²)/2`, `(x²−y²)²/16`), `gap_fixed.py`, `holonomy_check.py` and `w4_check.py` all run as claimed. These are checks, not proofs.
- **Tip-domain step.** It remains a mode-by-mode argument with cross-checks (CH 2D c=1, FM's continuation from β≤2π), not an operator-theoretic proof. The LaTeX presents it as conditional on the chosen extension.

**Literature.**
- **Casini–Huerta and Fursaev–Miele.** I confirmed both via PDF text in r1.
- **MST arXiv:2411.02598.** I confirmed eqs. (3.7)–(3.10) in r1. The statement that the expansion starts at `O(alpha^4)` as a result of maximal supersymmetry is the paper's own.

**BibTeX record: VERIFIED** for `CasiniHuerta2009`. Crossref gives Casini & Huerta, "Entanglement entropy in free quantum field theory", J. Phys. A (Math. Theor.) vol 42, issue/number 50, DOI 10.1088/1751-8113/42/50/504007, with eprint 0905.2562.

**BibTeX record: VERIFIED** for `FursaevMiele1997`. Crossref gives Fursaev & Miele, "Cones, spins and heat kernels", Nucl. Phys. B vol 484, pp 697–723, 1997, DOI 10.1016/S0550-3213(96)00631-1, with eprint hep-th/9605153.

**Not independently verified.**
- Steinacker 2303.08012 `V_4`; only the numerical −3/8 ratio is checked.
- The Carlson-type uniqueness of the continuation; it is assumed and the LaTeX says so.
- Nishioka–Yaakov.

## Findings
None blocking or major. All r1 findings are closed.

| r1 finding | Status |
|---|---|
| F1 (major) | closed |
| F2 (major) | closed |
| F3 (major) | closed |
| F4 (minor) | closed (paragraph split) |
| F5 (minor) | closed (`number={50}`) |

**Minor, non-blocking, no action required.**
- **Location:** insert para 1. Finding: "the first-order operator \(\gamma^\mu D_\mu\), whose square is \(\mathcal O_f\)" is sign-convention dependent. In the appH definition `O_f = -(γ·D)²`. Disposition: this is a harmless convention matter and I do not require a change. If the integrator wants it, "whose negative square" is the exact form. Accepting the text as submitted keeps it eligible for CLAUDE.md 4's "exactly that text" rule.
- **Location:** final conditional list. Finding: "the domain of the first-order operator" now partly duplicates "the choice of self-adjoint extension". Disposition: redundant but not wrong. It is kept deliberately and follows my r1 snippet.

**Cross-chapter consistency.**
- The 017 sentences giving "2 for antiperiodic and 0 for periodic" and the rotated-branch values `3−n_D`, `5−n_D` remain as reported alternatives. The new paragraph states they are not `Tr rho^n`. This is consistent and creates no contradiction.
- The replacement sentence "The gluing selected by a quasi-free state with rotational modular flow is stated below." is accurate. The material below is conditional on that state, and the matrix state itself remains underived.
- **No PRIOR-CLAIM-ERROR.** No merged sentence becomes materially false. 017 labelled the periodic branch an alternative and said the gluing was undetermined.
- **Emergence.** The wedge, rotation and cone are built on the emergent `G`, not a fundamental metric. No REJECT trigger.
- **Package coherence.** The gluing, the periodic/rotated exclusions, the gap arithmetic and the `Q_10` character identification share one setting (017's Poisson-limit D=10 content) and one source surface. Bundling is justified.
- **Significance.** This is a consequential bounded sharpening of a bounded no-go. It removes the `0 = 0` periodic coincidence as a replica result. It fixes the fermion gluing within H7. It identifies the `n_D = 2` cancellations as the standard supertrace orders `alpha^0` and `alpha^2`. It is not a derivation of a critical-path step, so no BREAKTHROUGH.

## Scope of what is established
**Established (algebra, verified).**
- The frame/phase relation. Polar antiperiodic under angle `2πn` equals Cartesian `−e^{2πinσ}`, which is `(−1)^{n+1}` at integer `n`.
- The twist sets and `Sum a^2 = (n²−1)/(12n)`.
- Periodic Cartesian equals the `Tr rho^n` set at odd `n` and the graded set at even `n`.
- The graded trace has twist `a = 1/2` at `n = 1`, so it is not normalised.
- `c_A − c_T = 4 − n_D`.
- `N_tot` and `b` are the `alpha^0` and `alpha^2` orders of `Q_10`, with first survivor `(x²−y²)²/16` at `n_D = 2`. This is a character statement only.

**Conditional (stated in the LaTeX).**
- Quasi-free state and rotational modular flow (Problem A).
- The less singular self-adjoint extension. This is a mode-by-mode derivation, not operator-theoretic.
- Uniqueness of the continuation from integer `n` (Carlson-type, assumed).
- The `Lambda^2` order, the content `n_D = 2`, `N_s = 6`, and the Poisson/Euclid/one-loop class (H1–H10).

**Not established.**
- The state, the flow, the vector/ghost/scalar tip domains, `ass:EE`, stationarity, and a value or sign of `G_eff`.
- The A-side next order.
- The `W_4` T-side structural survivor. It stays in the proposal only, as the proposal itself requests.

**Classification.** PROGRAMME-CONDITIONAL. Problem B stays OPEN. No label change and no `LABEL-CHANGE-PROPOSED`.

**No-go class.** The mismatch no-go holds within hypotheses H1–H10 of the proposal's fork list: Poisson limit; Euclidean section; one loop; `Lambda^2` order; tensor block = `delta rho = 0` modes; the fermion tip domain (now the less-singular extension); a quasi-free state with rotational flow; constant `Theta_bar`; content `n_D=2`, `N_s=6` with Yukawas dropped; and conical (not edge- or contact-augmented) area coefficient. It does not close the infrared derivation beyond those hypotheses.

**Open avenues after this no-go, ranked by promise.**
1. **Contact or edge terms of total weight `n_D = 2` at order `Lambda^2`** (units where a scalar is 1/6). The whole remaining gap is the spin term, +1 per Dirac field. Candidates are a Lichnerowicz-type `−R/4` endomorphism or fermion/ghost edge modes. This relaxes H10. Kabat's vector contact term (−1) cannot alone supply 2.
2. **A-side next order on a curved `J = 0` leaf**, compared with the T-side survivor. The T-side `W_4` is conjectural because E and Ω were not re-derived. This relaxes H4 and H8.
3. **Vector, ghost and scalar tip domains.** These fix the `alpha`-dependence and the R-holonomy kink. They relax H6.
4. **A non-rotational modular flow, a non-quasi-free state, or Moyal corrections (Problem A).** This relaxes H7.
5. **Non-flat `J = 0` backgrounds** to test the lemma and the tip conditions.

The proposal's "Lichnerowicz-type term" idea (its Section 4, item 6) belongs with avenue 1. The proposal's pointer to the (anti-)self-dual locus and 018's `f1=f2` BPS locus is correctly kept out of the LaTeX and is queued as separate work.

## Recommended disposition
Integrate as-is. Proposed integration ordinal: **17**.

**Accepted text, exactly:**
1. **Replacement sentence.** In `chapters/appH-microscopic-proofs.tex`, `sec:status-B`, replace the unique sentence "The gluing selected by the matrix state is not determined here." (line 189) with "The gluing selected by a quasi-free state with rotational modular flow is stated below."
2. **Insert.** The three-paragraph block in `proposals/019-fermion-replica-gluing/appH_insert.tex` (identical to the r2 block). The first paragraph is `\paragraph{Fermion replica gluing for \(\operatorname{Tr}\rho^n\) and the supertrace character (conditional; not closure).}`. Place it after the unique sentence ending "…or the Kaluza--Klein sector. Problems~B, C, D, F and~G remain open." (line 191) and before `\section{Problem C: conformal mode and Cassini}` (line 193). Preserve CRLF when writing.
3. **Bibliography.** Add `CasiniHuerta2009` (with `number = {50}`) and `FursaevMiele1997`, exactly as in proposal-r2's BibTeX block, to `bib/namcg.bib`. `MantaSteinackerTran2024` already exists. Do not alter the pending `BenArous1989` entry.

After integration, run `python scripts/build_check.py` to confirm no undefined or multiply-defined references. The proposal's own scratch compile used a stub `\cite`.

## Corrected snippet
None needed.

Relevant files:
- `C:\Users\redgi\Projects\namcg-lab\proposals\019-fermion-replica-gluing\proposal-r2.md`
- `C:\Users\redgi\Projects\namcg-lab\proposals\019-fermion-replica-gluing\appH_insert.tex`
- `C:\Users\redgi\Projects\namcg-lab\proposals\019-fermion-replica-gluing\review-r1.md`
- `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex` (lines 189, 191, 193)
- `C:\Users\redgi\Projects\namcg-lab\bib\namcg.bib`
