# Proposal 070-b-content-class, round 1

## Result

1. **Adversary finding F9 is upheld as arithmetic, and it is not a manuscript error.** Re-derived from the operators (not from the quoted formulas): the fixed-state gap is `c_A - c_T = 4 kappa_X + n_D`, so "gap = 4 kappa_X", "c_A - 1 = c_W(-1)" and "3 kappa_X remains" hold only at `n_D = 0`. At the IKKT content `(N_s, n_D) = (6, 2)`, `N_tot = kappa_X = 0` and the question "what supplies the remaining 3 kappa_X" is `0 = 0`. The appH paragraphs that use these relations (L400-429) each say "n_D = 0" in their setting and scope sentence, so no prior manuscript statement is materially wrong. The defect is in the frontier edge wording, which drops that scope.
2. **The ledger at (6,2), order Lambda^2, one-loop Poisson-limit class.** The tensor side is zero in every presentation (`c_T = c_T^ext = c_W(r) = 0` for all `r`). The `r`-family, the presentation dependence of the Noether coefficient, the frame non-invariance of `rho^2 X` and the `-4 kappa_X` asked of the modular Hamiltonian are all absent. The only nonzero entry is the fixed-state area coefficient `c_A = n_D = 2`, which is the Dirac antiperiodic excess alone (1 on `n<1` or 3 on `n>1` with the vector holonomy contact). So at this content the comparison is either `0 = 0` (periodic, smooth) or `2 != 0` (trace of `rho^n`: `1/G_A = Lambda^2/pi`, `1/G_T = 0`). Neither determines a Newton constant.
3. **Which B route stays open at (6,2).** A non-vacuous comparison needs a class with a scale. For formal constant sector masses both sides are weighted by the same `f(m^2)`, and the comparison reduces to two spectral sums: `c_T = S_n/6 - 4 S_kappa`, `c_A^per = S_n/6`. Periodic-gluing equality holds iff `S_kappa = 0`. For one bosonic and one fermionic mass, `c_A^per = -(1/2) c_T`, of opposite sign.

This is a bounded result. It closes nothing, and Problem B stays OPEN.

## Target and status

- **Problem B**, `sec:status-B` (appH L72-429 at the baseline hash below). Ledger label, verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- **ch17 (L121-137)**: "CRITICAL PATH; OPEN. ... Closure requires fixed-volume variations of the tensor (non-conformal) block from the microscopic action, a specified map g^(0) -> g, and no use of an already-existing metric."
- **Original target**: derive `delta S_D = 0` at fixed volume for the tensor block from the microscopic action, with the area term related to the emergent metric. The sub-question here is the necessary condition `G_A = G_T` of the normalisation paragraph (L205-210).
- **Dependencies**: A (state, modular Hamiltonian, gluing), F (induced coefficient), D (local frame rotations).
- **Classification of this package**: PROGRAMME-CONDITIONAL.
- **Discrepancies**: none between ch17 and appH for B. The frontier edge `B.matrix-state-edge-sector` (reports/graph/frontier.yaml L89-90) states the `3 kappa_X` question without the `n_D = 0` scope that appH L416 and L429 carry.

## Source reading

Digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST CURRENT`; all chapter files unchanged, `dirty-chapters: no`. No full scan: no definition, assumption, scope statement or status passage is changed.

Read in full:
- appH `sec:status-B` L72-431;
- ch17 L118-142;
- reports/adversary/adversary-P-20261114-1705.md F8-F10, the Survived, Scripts and "What this is not" sections, and scratch/adversary/p1_content_gap.py with its output;
- reports/graph/frontier.yaml, the B edges and the chain table.

Read by grep only: reports/sme-scout-20261114-1206.md (it has no B route; its routes are A and G-derived) and reports/ledger.md.

No file was unreadable. Baseline appH: 624232 bytes, sha256 `c2dac013...8b5c`.

## Research and reasoning

**Class and order of limits (F8).** Four matrix coordinates; the Poisson limit is taken first, then the proper-time limit `s_min = Lambda^-2`, common to all sectors; Euclidean section; `alpha = 1`; one loop; Yukawa couplings dropped. No matrix state is used. The replicas are gluing prescriptions for the Poisson-limit operators on the cover of the chart, and no `N -> infinity` or block-rank `M -> infinity` limit is taken. The insert says this explicitly.

**Sector data, re-derived (s1).** Operators, with `D_mu = Theta^{mu nu} d_nu`:
- `O_s = -D^2`;
- `(O_v a)_mu = -D^2 a_mu - 2{Theta_{mu nu}, a_nu}`, the form fixed by the intertwining `O_v Gr = Gr O_s - {J, .}` of L215, which I re-derived by hand from `[D_mu, D_nu] = {Theta_{mu nu}, .}`;
- `O_f = -(gamma.D)^2 = O_s - (1/2) gamma^{mu nu}{Theta_{mu nu}, .}`.

Each is Laplace-type for `G^{nu rho} = Theta^{mu nu} Theta^{mu rho}` (`sqrt G = rho^2`). The endomorphism follows from the standard formula (Vassilevich, hep-th/0306138, eqs. 2.2-2.4, quoted from memory and not re-fetched; the script checks it against the manuscript's closed form for `E_s`). At four random two-jets of closed `omega`, in exact arithmetic:
- `E_s = e = -(1/2) Box ln rho + (1/4)|d ln rho|^2`;
- `tr E_v = 4e - X`;
- `tr E_f = 4e - X/2`, with `X = sum (d Theta)^2 = -tr(b_s b^s) > 0`.

With the conformal identity `rho R[g_rho] = rho^2 (R_G + 3 Box ln rho - (3/2)|d ln rho|^2)` (standard, analytic), `sqrt G (R_G/6 - e) = (1/6) rho R[g_rho]` pointwise. So each sector has `(n/6) rho R[g_rho] + kappa rho^2 X` with `(n, kappa)` = (1,0) scalar and ghost, (4,1) connection, (4,1/2) Dirac. The weighted sum is `(N_tot/6) rho R + (1 - n_D/2) rho^2 X`, identically zero at (6,2).

**Tensor rule (s2).** On plane-wave modes with `delta rho = 0` about constant `Theta-bar`, the second-order averages obey `<rho R[g_rho]> = -(1/4) <rho^2 X>` (four random modes, exact; two generic modes with `delta rho != 0` give other ratios). Hence `c_T = c_R - 4 kappa_X`.

**Area side (s3).**
- A scalar component gives `(1 - n d_n)[(1/12)(1/n - n)] = 1/6`.
- A Dirac block with twists `a_k = k/n` gives `sum a_k^2 = (n^2-1)/(12n)`, hence `-1/6` per block and `+1/3` per Dirac field at weight -1 (against `-2/3` for periodic gluing).
- The vector holonomy `a = 1 - n` on two components shifts `c` by `-1`.

These reproduce the manuscript's values. The Dirac domain choice (less singular extension) and the statement "antiperiodic = trace of rho^n" are inherited from L225, conditional on the quasi-free state with rotational modular flow. They are not re-derived.

**F9.** `c_A^fs - c_T = 4 kappa_X + n_D` and `(c_A^fs - 1) - c_W(-1) = n_D/2`. So the adversary's table is confirmed: (6,0) gives `c_T = -8/3`, gaps 4 and 4; (6,2) gives `c_T = 0`, gaps 2 (antiperiodic) and 0 (periodic). One refinement the adversary did not state: the fixed-state gap splits into two parts of different origin. The `rho^2 X` index weight sits on the tensor side only, and the Dirac excess sits on the area side only. At (6,2) only the second survives.

**Consequence at (6,2).** The weighted `a_1` vanishes pointwise, so the induced density at order Lambda^2 is zero. Everything built on it (the charges of `L_r`, the `r` ambiguity, `T_eta`) is then zero too. The requirement of L414, that the edge term contribute `-4 kappa_X`, is void. What remains is `c_A = 2` for the trace of `rho^n`, with no tensor counterpart.

At logarithmic order the manuscript's own formulas, evaluated at `n_D = 2` and not re-verified here, give gaps 0, 2, 0 (L298) and `kappa_C^T = 0`. `S_4` is quartic in `b` (L259-263), so the logarithmic coefficient has no quadratic form about constant `Theta-bar`.

**Sectors with a scale (s3).** A constant mass multiplies every heat trace, on the chart and on the cover, by `e^{-s m^2}` exactly. Both sides then carry the same `f(m^2) = int_{Lambda^-2}^inf ds s^-2 e^{-s m^2} = Lambda^2 - m^2 ln(Lambda^2/m^2) - (1 - gamma_E) m^2 + ...`; mpmath gives residuals 5e-7 and 4.5e-8 against this expansion. This gives the `S_n`, `S_kappa` formulas of the Result. The mass is the formal shift of L265, with no gauge-invariant mass term.

**No-go fork.** The obstruction: at (6,2) no nontrivial `G_A = G_T` is available in this class. It depends on the following hypotheses.

| # | Hypothesis | Relaxation | What was found here |
|---|---|---|---|
| H1 | Four coordinates, no scale | Ten matrices on `M x K` with a Kaluza-Klein tower | Explored formally: mass-weighted sums. The comparison becomes non-vacuous and reduces to `S_kappa = 0`. The actual towers are not computed. |
| H2 | One loop, Lambda^2 and log orders only | Finite terms; two loops | Not explored. |
| H3 | Poisson limit first | Moyal corrections at the cutoff, which break the `N_tot = 0` cancellation scale by scale | Not explored. |
| H4 | Gluing is the trace of `rho^n` with the less singular extension | A Dirac contact of `-1` per field, or a state whose replica is the periodic or smooth one | The manuscript's Dirac holonomy contact is 0 at first order, so none is supplied. The state belongs to Problem A. |
| H5 | Yukawa couplings dropped | Keeping them changes `E_f` off the background only | Not explored. |
| H6 | Proper-time regulator, one common limit | Sector-dependent limits are an input | L208 gives the split-cutoff form at `n_D = 0`; not pursued. |

Avenues still open, ranked:
1. `S_n` and `S_kappa` on an actual product background with IKKT content (H1). This must be serialized with the F chain, since it reads the product class.
2. The Dirac tip domain and gluing selected by a matrix state (H4; this is A intersect B and waits on A).
3. Finite and Moyal terms at (6,2) (H2, H3).
4. Yukawa terms (H5).

**Literature.** No new source. `DonnellyWall2016` and `Steinacker2023` are existing bib keys, used exactly as appH L235 and L265 already use them. Their content was not re-fetched in this package and is not independently verified here.

## Claim classification

- Sector endomorphism traces `(n, kappa)`: established identity at sampled jets (exact arithmetic at four jets; not a general proof).
- `<rho R> = -(1/4)<rho^2 X>` on `delta rho = 0` modes: established at four sampled modes (exact).
- General-content identities, the table, and the collapse of `c_W(r)` at `kappa_X = 0`: established algebra, given the above.
- `c_A` values per gluing: conditional (inherited replica prescriptions, tip domain, quasi-free state).
- "`1/G_A = Lambda^2/pi` against `1/G_T = 0` for the trace of `rho^n`": conditional (same hypotheses; regulator dependent).
- Log-order pattern at (6,2): conditional, inherited from L259-300 and not re-verified.
- Mass-weighted formulas: conditional (formal mass).
- Relevance of `S_n`, `S_kappa` to Kaluza-Klein towers: unresolved.
- State, gluing, modular Hamiltonian: unresolved (Problem A).

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex`, inside `sec:status-B`, at its end. Nothing is removed or replaced.

**Anchor (occurs once; checked by `apply_check.py`):** the closing sentence of the paragraph on the matrix gauge realisation, followed by the Problem C header:

> the Dirac sector or the measure of the matrix integral, and derive no local Lorentz symmetry. Problems~B and~D remain open and PROGRAMME-CONDITIONAL.
>
> \section{Problem C: conformal mode and Cassini}

Insert the block below immediately before `\section{Problem C: conformal mode and Cassini}`. The block ends with a blank line, and the existing blank line after the anchor sentence is kept. The exact bytes are in `proposals/070-b-content-class/appH_insert.tex`; the integrator normalizes to CRLF.

The block adds no `\ref` and no `\label`. It uses the cite keys `DonnellyWall2016` and `Steinacker2023` (one bib entry each) and the macro `\LUV`. The symbols `c_T^{ext}`, `kappa_C^T`, `c_W(r)`, `L_r` and `\mathcal S_4` are those of the preceding paragraphs; `\mathsf S_n` and `\mathsf S_\kappa` are new and defined in the block.

```latex
\paragraph{Content class of the order-\(\LUV^2\) comparison: the ledger at \(N_s=6\), \(n_D=2\) and the scope of the edge-term question (conditional; not closure).}
Keep the setting of the paragraphs on the normalisation of the tensor kinetic term, on fermionic content, on the order \(\Lambda^2\) and on covariant variables: four matrix coordinates, the Poisson limit taken before the proper-time limit, the Euclidean section, \(\alpha=1\), one loop, the \(\LUV^2\) term with one common proper-time limit, \(N_s\) scalar components, the connection with its ghosts and \(n_D\) Dirac fields with the Yukawa couplings dropped, and the two modes with \(\delta\rho=0\) about a constant \(\bar\Theta\). No state of the matrix model enters: the replicas below are gluing prescriptions for the Poisson-limit operators on the cover of the matrix chart, and no limit of finite matrices or of the rank of a block is taken.

\emph{Sector data.} For each sector \(\sqrt{|G|}\operatorname{tr}(\tfrac16R_G-E)=\tfrac n6\,\rho R[g_\rho]+\kappa\,\rho^2X\) pointwise, with \((n,\kappa)=(1,0)\) for a scalar component and for a ghost, \((4,1)\) for the connection and \((4,\tfrac12)\) for a Dirac field (endomorphisms computed from the operators \(\mathcal O_s\), \(\mathcal O_v\), \(\mathcal O_f\) at four random two-jets of a closed \(\omega\), exact arithmetic), and on the modes with \(\delta\rho=0\) the second-order averages obey \(\langle\rho R[g_\rho]\rangle=-\tfrac14\langle\rho^2X\rangle\) (four random modes, exact arithmetic). With the weights \(1,1,-2,-1\) this gives \(c_R=N_{\mathrm{tot}}/6\), \(\kappa_X=1-\tfrac12n_D\) and \(c_T=c_R-4\kappa_X\). The area coefficients of the preceding paragraphs are \(c_A^{\mathrm{per}}=c_R\) for the unrotated periodic gluing, \(c_A=c_R+n_D\) for the fixed-state replica and \(c_A^{\mathrm{sm}}=-c_R/2\) for the first-order smooth replica, and the Noether coefficient is \(c_W(r)=c_R+\kappa_Xr\). Hence, for every \(N_s\) and \(n_D\),
\[
  c_A-c_T=4\kappa_X+n_D,\qquad c_A^{\mathrm{per}}-c_T=4\kappa_X,\qquad c_W(r)-c_T=\kappa_X(r+4),\qquad (c_A-1)-c_W(-1)=\tfrac12n_D .
\]
The gap of the fixed-state replica has two parts of different origin: the index-weighted coefficient of \(\rho^2X\), which enters the tensor side only, and the excess \(+1\) per Dirac field of the antiperiodic cone value, which enters the area side only. The identification of that gap with \(4\kappa_X\), the relation \(c_A-1=c_W(-1)\) and the remainder \(3\kappa_X\) of the paragraphs on covariant variables and on the matrix gauge realisation hold at \(n_D=0\), as stated there, and at no other \(n_D\).
\begin{center}
\begin{tabular}{@{}lccc@{}}
\toprule
coefficient & general & \((N_s,n_D)=(6,0)\) & \((6,2)\)\\
\midrule
\(c_R=N_{\mathrm{tot}}/6\) & \(\tfrac16(N_s+2-4n_D)\) & \(\tfrac43\) & \(0\)\\
\(\kappa_X\) & \(1-\tfrac12n_D\) & \(1\) & \(0\)\\
\(c_T\) & \(c_R-4\kappa_X\) & \(-\tfrac83\) & \(0\)\\
\(c_T^{\mathrm{ext}}\) & \(c_R-2\kappa_X\) & \(-\tfrac23\) & \(0\)\\
\(c_W(r)\) & \(c_R+\kappa_Xr\) & \(\tfrac43+r\) & \(0\)\\
\(c_A^{\mathrm{per}}\) & \(c_R\) & \(\tfrac43\) & \(0\)\\
\(c_A\), fixed-state & \(c_R+n_D\) & \(\tfrac43\) & \(2\)\\
\(c_A\), fixed-state and vector holonomy, \(n<1\) & \(c_R+n_D-1\) & \(\tfrac13\) & \(1\)\\
\(c_A^{\mathrm{sm}}\) & \(-\tfrac12c_R\) & \(-\tfrac23\) & \(0\)\\
\bottomrule
\end{tabular}
\end{center}

\emph{At \(N_s=6\), \(n_D=2\).} Here \(c_R=\kappa_X=0\), the weighted \(a_1\) density vanishes pointwise for every Poisson bivector, and the induced density of order \(\LUV^2\) is zero. The tensor side then vanishes in every presentation, \(c_T=c_T^{\mathrm{ext}}=c_W(r)=0\) for every \(r\): the family \(L_r\) of the paragraph on covariant variables has a single member, and the dependence of the Noether coefficient on the presentation, the non-invariance of \(\rho^2X\) under local rotations of the frame and the term \(-4\kappa_X\) required there of the modular Hamiltonian are all absent, the remainder \(3\kappa_X\) being zero. The uniform contact \(-N_{\mathrm{tot}}/4\) is zero, and the periodic and smooth replicas give \(0=0\). The one nonvanishing entry is the fixed-state area coefficient \(c_A=n_D=2\), which is the Dirac excess alone; the vector holonomy contact of modulus \(1\), the edge-mode value of~\cite{DonnellyWall2016} for a Maxwell field if the state carries that sector, changes it to \(1\) on \(n<1\) and \(3\) on \(n>1\), and the Dirac holonomy contact vanishes at first order, so no contact of the paragraph on the order \(\Lambda^2\) removes it. The coefficient of \(W\) at logarithmic order has the same pattern, with gaps \(0\), \(2\), \(0\) for the periodic, fixed-state and completed replicas and \(\kappa_C^T=0\); and since \(\mathcal S_4\) is quartic in \(b_\sigma\), the logarithmic coefficient of the induced action stated in the paragraph on the next order has no quadratic form about a constant \(\bar\Theta\). At this content the requirement \(G_A=G_T\) of the paragraph on the normalisation is therefore, at order \(\LUV^2\), the single condition \(c_A=0\) on the area side, with \(1/G_T=0\): for the trace of \(\rho^n\) of the paragraph on fermion replica gluing \(1/G_A=\LUV^2/\pi\) while \(1/G_T=0\), and for the periodic and smooth replicas both vanish. In this class the comparison at this content is either an equality of vanishing coefficients or the inequality \(2\neq0\), and in neither case does it determine a Newton constant.

\emph{Sectors with a scale.} Let each sector carry a constant mass, \(\mathcal O_i\to\mathcal O_i+m_i^2\), the formal shift of the paragraph on the next order, with the ghosts at the mass of the connection. The heat trace of the sector is multiplied by \(e^{-sm_i^2}\) on the chart and on the cover alike, so the sector data above are weighted on both sides by the same function, \(f(m^2)=\int_{\LUV^{-2}}^\infty\mathrm ds\,s^{-2}e^{-sm^2}=\LUV^2-m^2\ln(\LUV^2/m^2)-(1-\gamma_{\mathrm E})m^2+O(m^4/\LUV^2)\), with \(\gamma_{\mathrm E}\) the Euler constant. With \(\mathsf S_n=\sum_iw_in_if(m_i^2)\) and \(\mathsf S_\kappa=\sum_iw_i\kappa_if(m_i^2)\), in units in which the massless value of \(f\) is \(1\),
\[
  c_T=\tfrac16\mathsf S_n-4\mathsf S_\kappa,\qquad c_A^{\mathrm{per}}=\tfrac16\mathsf S_n,\qquad c_A=\tfrac16\mathsf S_n+\sum_{\text{Dirac}}f(m_D^2),\qquad c_A^{\mathrm{per}}-c_T=4\mathsf S_\kappa .
\]
At \(N_s=6\), \(n_D=2\) the \(\LUV^2\) parts of \(\mathsf S_n\) and \(\mathsf S_\kappa\) cancel and both sums are of order \(m^2\ln\LUV\). The tensor coefficient is nonzero only if \(\mathsf S_n\neq24\,\mathsf S_\kappa\), and for the periodic gluing it equals the area coefficient if and only if \(\mathsf S_\kappa=0\), a condition on the connection and Dirac spectra alone; the fixed-state replica keeps in addition the Dirac term, of order \(\LUV^2\). For one bosonic mass and one fermionic mass \(c_T=-\tfrac83(f_b-f_f)\) and \(c_A^{\mathrm{per}}=\tfrac43(f_b-f_f)\), of opposite sign. At this content the comparison of \(G_A\) with \(G_T\) is thus not vacuous only in a class with a split spectrum, where it reduces to the two sums \(\mathsf S_n\) and \(\mathsf S_\kappa\). Whether the Kaluza--Klein towers of fuzzy extra dimensions, for which~\cite{Steinacker2023} attributes the Einstein--Hilbert term to a mixed quartic term and not to a mass shift of \(a_1\), give sums of this form is not examined.

These statements are for the Poisson limit taken first, four matrix coordinates, the Euclidean section, one loop, \(\alpha=1\), the proper-time regulator with one common limit, the contents stated with the Yukawa couplings dropped, the replicas and contacts of the preceding paragraphs with their hypotheses, the two modes with \(\delta\rho=0\), and formal constant masses without a gauge-invariant mass term. They supply no state, modular Hamiltonian or gluing of the matrix model, do not derive the content, do not treat finite terms, Moyal corrections, more than four matrix coordinates or a Kaluza--Klein tower, use the stated properties of \(\mathcal S_4\) and of the coefficient of \(W\) from the preceding paragraphs without a new check, and give no value or sign of \(G_{\mathrm{eff}}\). Problem~B remains open and PROGRAMME-CONDITIONAL.
```

**Stale passages elsewhere:** none in the manuscript. L414, L427 and L429 are correct as scoped. Outside the manuscript, and not mine to edit: frontier.yaml edge `B.matrix-state-edge-sector` should carry "(n_D = 0 only; 0 = 0 at the IKKT content)".

## Verification scripts

All in `C:\Users\redgi\Projects\namcg-lab\proposals\070-b-content-class\`. Run from the repository root with the repository Python.

| Command | Checks | Expected invariant output |
|---|---|---|
| `python proposals/070-b-content-class/s1_weighted_a1.py` (about 3 min; output `s1_weighted_a1_output.txt`) | `E_s = e`, `tr E_v = 4e - X`, `tr E_f = 4e - X/2` at four random two-jets, exact; Jacobi at the jet; weighted sum | every residual `0`; `weighted a_1 at (6,2): 0`; `S1 PASS` |
| `python proposals/070-b-content-class/s2_mode_ratio.py` (about 5 s; `s2_mode_ratio_output.txt`) | second-order averages on `delta rho = 0` modes | `ratio = -1/4` four times; generic modes differ; `S2 PASS` |
| `python proposals/070-b-content-class/s3_content_ledger.py` (`s3_content_ledger_output.txt`) | cone constants, general-content identities, table at (6,0) and (6,2), mass-weighted sums, `f(m^2)` expansion | `1/6`, `-1/6`, `1/3`, `-2/3`, holonomy shift `-1`; `(c_A^fs - 1) - c_W(-1) = n_D/2`; (6,2) column `0,0,0,0,0,0,2,1,0`; `ratio c_A^per/c_T = -1/2`; `f` residuals about `1e-7` |
| `python proposals/070-b-content-class/apply_check.py` (`apply_check_output.txt`) | baseline hash, unique anchor, CRLF, cites, balance, no process words, insert inside `sec:status-B` | `anchor occurrences: 1`; `result appH: 632476 ee3a885f...`; `APPLY CHECK PASS` |

No LaTeX build was run; the integrator builds. Symbolic output is a check, not a proof: s1 and s2 are exact at the sampled points only.

## Decisions Taken

1. **F9 is recorded as a scope statement, not as a correction of prior text.** Reason: L400-429 are correctly scoped to `n_D = 0`. Rejected: flagging a PRIOR-CLAIM-ERROR in appH, since no statement is false.
2. **One consolidated paragraph at the end of `sec:status-B`**, rather than edits to L414 or L427. This is the smallest text that records the result, and it leaves the accepted paragraphs untouched.
3. **The Frenkel-Hartnoll against Donnelly-Wall comparison was not attempted.** Per F8 it needs a state and an `N`, `M`, Poisson order of limits that nothing supplies. At (6,2) its target coefficient is `0 = 0` in any case.
4. **The mass-weighted extension is included** as the route that keeps the infrared and full-GR comparison alive at the actual content. It is formal and labelled as such. Rejected: computing actual towers on `M x K` here, because that reads the product class of `sec:status-F`, where another chain is active, and needs a derivation the product-class caveats do not yet supply.
5. **No reference to `sec:status-F` results is added**, which avoids conjoining configuration classes (F10).

## Milestone assessment

Routine. This is not a breakthrough and no critical-path step is derived. M3 (correction of a materially false prior statement) does not apply to the manuscript: no appH statement is false. The package is a bounded, reproducible obstruction that redirects the B edge: at the IKKT content the "3 kappa_X" target is void, and the open comparison moves to a class with a scale.

Suggested flag for the orchestrator: PLAN-CORRECTION for frontier edge `B.matrix-state-edge-sector`, and a new follow-up edge "B.kk-spectral-sums" serialized with the F chain.

## Status-label recommendation

The critical-path list from ch17 and appH at the full-GR / matrix-derived scope is A, B, C, D1, E, F, G-derived, N. Affected labels: none. B stays OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

For the original target, all of the following remain:
- `delta S_D = 0` at fixed volume for the tensor block from the microscopic action;
- the state, modular Hamiltonian and gluing (Problem A);
- the map from scaffold to emergent metric;
- a nonzero induced `G_T` at the actual content, which needs a class with a scale (Problem F);
- in that class, `S_kappa = 0` or an equivalent area-side contact, or else a derivation that the state's replica has `c_A` equal to the induced coefficient.

At (6,2) in the present class, the trace-of-`rho^n` area coefficient `2` has no tensor counterpart.

## Special instructions for the gatekeeper

- Evaluate every claim at (6,2) and at (6,0). The insert asserts nothing about `G_eff`, the state or the gluing.
- Re-derive `c_A - c_T = 4 kappa_X + n_D` and `(c_A - 1) - c_W(-1) = n_D/2` by hand from L208, L220 and L357. Re-run s1 and s2; they are independent of the adversary's script, which only substitutes into the quoted formulas.
- Please check the sentence "the logarithmic coefficient ... has no quadratic form about a constant Theta-bar". It rests on L259-263 (`a_2` weighted sum equal to `S_4/2` up to total derivatives; sampled jets). It was not re-verified here and the scope sentence says so. If you judge it too strong, deleting that clause leaves the rest intact.
- "`1/G_A = Lambda^2/pi`" uses `1/G = c Lambda^2/(2 pi)` of L338 with `c = 2`. It is regulator dependent and conditional on the gluing of L225. It must not be read as an entropy of a matrix state.
- The mass paragraph is formal (as L265). It must not be read as a statement about the product backgrounds of `sec:status-F`.
- The Vassilevich endomorphism formula in s1 is quoted from memory. Its correctness is tested only by residual (a), which reproduces the manuscript's `E_s`.
- No status, priority or completion label is changed. The insert lies wholly inside `sec:status-B`.
