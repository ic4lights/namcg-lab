# Proposal 069-f-nonderivative-sector, round 1

## Result

The adversary collision F7 is upheld, and it is material. The package therefore delivers a correction and a bounded no-go for the cubic (and mass) branch of the L2793 paragraph, plus one exact piece of the t non-derivative sector. It does not deliver the full second-order non-derivative sector of t; that stays open, and the reason is identified.

1. **Cubic Hessian (exact).** With the cubic term of `eq:Smatrix` read on the three directions of K = S^2_N, `C_ijk = i c eps_ijk / g^2`, the background-Feynman-gauge operator of the three vector components along K is
   `H_V^K = chi^2 (L^2 - kappa S.L)`, `kappa = 2 - c/chi`.
   The merged operators (L2674, and the spectrum quoted at L2824) are the case `kappa = 2`. Ghosts, spinors and the other seven vector components are unchanged. At the tree stationary point `chi = c/2` the operator is `chi^2 L^2` and `v^K = 0` identically.
2. **Loss of the second-order cancellation (exact).** `sum w lambda^2 (v^K - tau^K) = (kappa^2 - 4) chi^4 N^2 (N^2-1) = (c^2 chi^2 - 4 c chi^3) N^2 (N^2-1)`. So on the cubic branch `Uhat` is logarithmically divergent at small proper time; the divergence has the form of a cubic term and of a mass term on K (absent from `eq:Smatrix`), and both carry `sqrt|g|`, not `rho_M`. The regulated term is O(N^4), against O(N^2) at c = 0.
3. **V != T on the cubic branch (exact spectra, large N).** `V/T -> kappa^2/4 = (1 - c/2chi)^2`, `W_R = V - T -> -T r_c(2 - r_c)`, with `r_c = c/2chi`. `V = T` only at `c = 0` or `c = 4 chi`, and the latter has a negative vector mode.
4. **Correction (M3 candidate).** The merged L2810 forms of `beta_K` "adding a tree cubic term" / "adding a tree mass term", and the L2824 example (`x = 3/10`, quartic 7.935, cubic -12.36, `beta_K = 1` "at a local minimum with Uhat > 0"), use loop terms from operators without the stabiliser's Hessian. The scope sentence at L2848 does not say so. At that example `c/chi = 2.336`, `kappa = -0.336`, `V/T = 0.028`, and the omitted loop term is at least 3.5 times the tree quartic already at N = 16. The merged L2844 statement that V = T "does not need a tuned K" holds only for the unstabilised operators.
5. **Exact relations on the quartic + cubic tree curve.** `1 - r_c = -L'/4Utilde`, `beta_K = 2(r_c - 1)/(4 - 3 r_c + delta)`, and hence `V/T = (L'/4Utilde)^2`. So V = T requires a one-loop slope as large as the tree quartic slope. This is the Dine-Seiberg statement (F6) in exact form for this class. At weak coupling the minimum sits at `r_c -> 1` (it exists at tree level, unlike the quartic alone), where `beta_K -> 0` (S2) and `V -> 0`. Bounded no-go: within one loop on S^2_N with this cubic term, no point has `beta_K = 1`, `V = T` and no negative mode.
6. **t sector, the part that is exact.** Eliminating `ln chi` gives `q_*^2|_chi = -beta_K L' L / 8 m^4 = (beta_K L'/4U_4) q_b^2`, non-positive at any local minimum. At the merged example (merged operators) it is `-14.8 q_b^2`: the chi exchange exceeds the vacuum term and has the tachyonic sign.
7. **F6 ratios at the merged point (merged operators):** slope: one-loop/tree = -1 (stationarity; one-loop slope is 0.168 of the quartic slope). `U_chichi`: -5.04/15.72 = -0.32. `q_*^2|_chi`: no tree part; it is `2L'^2/U_chichi` built from the one-loop slope. `V_00`, `V_01`: no tree part among the computed forms; on helicity +-2 they are `(1/15) V_0 m^-6 (m^2 q_0^2 + l^2 k^2) c.c`, fixed moments of the one-loop `V_0`. With the cubic Hessian included, the one-loop/tree ratio of the potential itself is >= 3.5 at N = 16 and grows as N^2. No "decides" statement is made.

**Not established:** the second-order response of `U_2` and of the first term (the named `(P_+ - 2)(P_- - 2)` computation), the constant of the first-term logarithm, hence the sign of `q_*^2 - q_b^2`; any long-range-force statement; any value or sign of `G_eff`. I did not compute those: with the corrected operators the non-derivative density is regulator-dependent at O(N^4), so a second-order coefficient computed on the merged operators would repeat the omission.

## Target and status

- **Problem F** (appH `sec:status-F`, L1669-1672, verbatim): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating \(G_{\mathrm{eff}}\) as an input leaves F OPEN and does not satisfy the matrix-derived criterion." Missing step (L1678-1685): specify the gauge-fixed fluctuation, Goldstone and ghost operators and weights, proper-time limits, thresholds, continuation, counterterm scheme; evaluate weighted `a_1` and curvature-linear `a_2`.
- **ch17 F item** (L403-411): "CRITICAL PATH; OPEN. The conditional heat-kernel identity does not compute the physical coupling."
- **C and N** are carried by the closing sentence of L2848 ("Problems C, F and N remain open and PROGRAMME-CONDITIONAL"). Their labels were not re-read in full this round beyond the digest status lines (C: L435-436; N: L3243-3244, both OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL).
- **Edge:** `F.t-nonderivative-sector` (frontier.yaml L274), 049 review-r4 avenue 1.
- **Dependencies:** IKKT content (supplied), product background, K supplied, cubic term on K supplied (`def:matrix-coords-ext`: "the cubic term is not extended here"), Assumptions `ass:lorentzian`, `ass:gap-psi` retained.
- **Classification of this package:** PROGRAMME-CONDITIONAL. Nothing is DERIVED.
- **Discrepancy noted, not resolved:** `eq:Smatrix` does not state the reality of `C`. For Hermitian matrices `eps_ijk Tr X_i X_j X_k` is imaginary, so a real action needs imaginary `C_ijk` on K. The insert states this as part of the supplied input.

## Source reading

Digest + targeted reads. `make_digest.py --check` printed DIGEST CURRENT (head 54a2dcb, dirty-chapters: no).

- Read in full: appH L1660-1700 (F ledger, missing step), L2672-2720, L2762-2850; ch03 L120-200 (`eq:Smatrix`, `def:matrix-coords-ext`); ch17 L396-420; `proposals/049-k-scale-dilaton-response/review-r4.md`; `reports/adversary/adversary-P-20261114-1705.md`; frontier.yaml F edges (L268-300).
- Not read: appH L2722-2761 (the Lichnerowicz/torsion closed-forms paragraph); the insert does not use it. SME scout `sme-scout-20261114-1206.md` was only searched for F-relevant routes (cubic, Myers, polarised, dilaton): none found; its ranked routes concern other chains.
- No file unreadable.

## Research and reasoning

### F7 re-derivation (first, as instructed)

The K part of the tree action with the cubic term is `g^-2 [ -1/4 tr[X_i,X_j]^2 + (i c/3) eps_ijk tr X_i X_j X_k ]`. On `X = chi J`: `eps_ijk J_i J_j J_k = i J^2`, so the cubic term is `-(2c/3) abar chi^3` with `abar = N(N^2-1)/8`, real for real c.

Second variation of the cubic term: `(ic/3) * 3 * eps_ijk tr(a_i a_j X_k) = (ic/2) eps_ijk tr(X_k [a_i,a_j])`. It is linear in `ad X_k` and acts on the K vector index only. The Yang-Mills flux term on S^2 is `[X_i,X_j] = i chi^2 eps_ijk J_k`, also proportional to `eps_ijk ad J_k`. So the cubic Hessian rescales the flux term of the K vector block: `2 chi^2 -> 2 chi^2 - c chi`.

Independent fix of the coefficient: for an on-shell background the gauge-fixed operator on a gauge mode `a_i = [X_i, lambda]` must equal the ghost operator, `chi^2 l(l+1)`. Gauge modes are the `j = l` tower, where `S.L = -1`, so `L^2 - kappa S.L = l(l+1) + kappa` requires `kappa = 0` at the tree solution `c = 2 chi`. Linearity in c with `kappa = 2` at c = 0 gives `kappa = 2 - c/chi`.

Script `s1` builds the Hessian from the matrix action itself (exact quartic finite differences, no formula input) for N = 2..5 and six (chi, c) pairs and matches the predicted spectrum with multiplicities to 8e-14. It also confirms stationarity at `chi = c/2`, the tree value, and that the unfixed Hessian annihilates gauge directions there but not at c = 0.

**Ruling on F7:** upheld. (a) and (b) are a scope tension the merged text handles by "supplied"; (c) is a real omission. The adversary's p3 observation (nonzero cubic second variation) is confirmed and sharpened to an exact operator.

### Consequences

- The factorisation identity of L2678 is algebraic and survives with the new `v^K`. The sentence "the index parts of the vector and of the spinors agree at second order in the flux" fails on K: the vector flux coefficient is `kappa`, the spinor one stays 2. Moments in `s2` part C.
- `Uhat = int ds s^-3 (v - tau)` then diverges logarithmically. Closed form with a lower limit in `s2` part A (checked against quadrature; the residual 0.08 at eps = 1e-4 is the stated O(eps) term). Sign of the regulated value: negative once the cutoff lies above K's spectrum (`s2` part E; zero at `s_Lambda chi^2 N^2 = 0.926`).
- `Vhat = int ds s^-2 v -> kappa^2 N^2`, `That -> 4N^2` (`s2` part D). Calibration at kappa = 2 reproduces the merged values (`That/N^2 -> 4`, `Vhat - That - 4 ln N -> 1.016`, `Uhat/N^2 -> 1`) (`s2` part B).
- At `r_c = 1`: `W_R = -T` exactly. With the merged `c_T = W_R/6 - 4 W_X`, `W_X = -T/8` this is `T/3 > 0`. This fixes the sign of `W_R` at this K, which L2694 left open ("do not ... fix the sign of W_R"). It is not a sign of `G_eff`: K, the content, the replica and the metric identification remain supplied, and the merged all-harmonics forms degenerate there (`A + B = V/8 -> 0`).
- Mass term: Hessian `mu^2` on the three components; `sum w lambda = 3 mu^2 N^2` (`s3` part D), so `W_R` is itself log divergent.

### Tree curve

`beta_K = -2 d_lnchi(rho_M V_t/g^2)/U_chichi` (merged, 049) does not depend on the form of the loop term. For `V_t = abar(chi^4 - (2c/3) chi^3)`: `V_t' = 4 abar chi^4 (1 - r_c)`, `V_t'' = 4 abar chi^4 (4 - 3 r_c)` (`s3` part B). The merged point is reproduced from the merged numbers: `r_c = (6 + delta)/5 = 1.168` with `delta = -5.04/(4*7.935)`.

### t sector

Second-order non-derivative form in `(delta ln chi, sigma_1)`, `sigma_1 = delta ln sqrt|g| = -t/2m^2`: the mixed coefficient is `L'` (first-order responses, merged), the `sigma_1^2` coefficient of `U_4` is `U_4` (from `sqrt|g_n| = m^-4 (1+x_n)^-1`, merged vacuum term). Elimination: `(U_4 - L'^2/2U_chichi) sigma_1^2 = (U_4 - beta_K L'/4) sigma_1^2` (`s3` part B). Normalisation check: the `U_4` part alone gives `2 M L = U_4 L / 2m^4 = -q_b^2` with the merged `q_b^2 = 12 Uhat chi^2 / m^2 (Vhat + 2 That)`, so the conventions agree with L2838. The merged text integrates chi out in the matter coupling (L2826) but its reduced t form has no t-chi-t term; this supplies it. chi is taken fibre-constant, so this term sits in the `q_*^2` slot (fibre-averaged t), not in the fibre-pointwise `q_b^2` slot.

The helicity +-2 moment of the vacuum term is checked symbolically in `s4`.

### Fork: hypotheses of the no-go and relaxations

| Hypothesis | Relaxation | Explored here | Outcome |
|---|---|---|---|
| Stabiliser = bosonic cubic on K | none (c = 0) | merged O4b | no weak-coupling minimum |
| Stabiliser = bosonic cubic on K | tree mass instead | moments only | `sum w lambda != 0`: `W_R` log divergent; V = T lost too |
| No fermion bilinear | supersymmetric completion (fermion bilinear in `S_matter`, boson masses; the class of arXiv:2409.18706) | not computed | open, rank 1 |
| Poisson limit on M (regulator) | finite matrices on M fix `s_Lambda` | sign only | regulated `U < 0` for cutoff above K's spectrum, value open |
| K = S^2_N | other K, cubic on other index sets | no | open |
| Static K with tree stabiliser | rotating K (stabilised kinetically, no tree Hessian) | no | open; this route avoids the present no-go |
| One loop | higher loops | no | open |
| Merged operators for second-order `U_2`, first term | recompute with corrected operators | no | open |

**Ranked open avenues** (all keep spacetime emergent):
1. Rotating K (`F.rotating-K-fluctuation`): no tree stabiliser, so no stabiliser Hessian; check V = T and `beta_K` there. This rises above its previous rank because the static cubic and mass branches are now bounded.
2. Supersymmetric completion of the cubic term: K spectra of vector, spinor, ghost about S^2_N; test `sum w lambda^2 = 0`, V vs T, `beta_K`. Needs mass terms not in `eq:Smatrix`; adopting it would be an author decision, computing it is not.
3. Regulator from the matrices of M: value of the O(N^4) term, then the corrected potential of chi and the corrected `x_0` structure.
4. Second-order response of `U_2` and the first term with the corrected operators; first-term constant; then `q_*^2 - q_b^2`.
5. Other K (S^2 x S^2, flux stacks at `f_1 = f_2 + f_3`) with their own stabilisers.
6. Higher loops at the tree-stable point `r_c = 1`, where the loop expansion has a small parameter.

### Literature

- Iso, Kimura, Tanaka, Wakatsuki, hep-th/0101102, Nucl. Phys. B 604 (2001) 121: record fetched; the abstract states that a Chern-Simons term is added to make the fuzzy sphere a classical solution. Used only for that statement. The solution and the Hessian are derived here independently (`s1`).
- Hartnoll, Liu, arXiv:2409.18706: record fetched (title, authors, abstract summary: supersymmetric mass-deformed IKKT with SO(3) x SO(7), fuzzy-sphere saddle). Named as an avenue only; its action and any cancellation in it are **not independently verified** and not cited in the manuscript text.
- Imai, Kitazawa, Takayama, Tomino, hep-th/0303120: record fetched (non-vanishing corrections about the fuzzy sphere with a Myers term). Not used, not cited.
- Dine-Seiberg: not fetched; I rely on no statement from it. The exact relation `V/T = (L'/4Utilde)^2` is derived here.

### F10

No result from another chain's passage is cited. All merged statements used are from this chain's paragraphs (L2674-2848); their caveats apply: L2694 "a fuzzy space K that is not required to solve the equations of motion ... They do not construct K or fix the sign of W_R"; L2791 "a weight independent of the fibre orders of the external amplitudes, which is an assumption"; L2848 "with V = T where the index part alone enters U_2 and with W_R neglected". The present class violates the last one on the cubic branch, which is the point of the correction.

## Claim classification

| Claim | Class |
|---|---|
| `H_V^K = chi^2(L^2 - kappa S.L)`, spectra, stationarity at chi = c/2, gauge modes | established (algebra + exact matrix check) |
| Moments `sum w = sum w lambda = 0`, `sum w lambda^2 = (kappa^2-4) chi^4 N^2(N^2-1)`; mass moments | established |
| Regulated `U` closed form | established; O(s_Lambda) remainder |
| `V/T -> kappa^2/4`, `Uhat_reg < 0` above K's spectrum | numerical (exact spectra, N <= 512) |
| `W_R = -T`, `c_T = T/3` at `r_c = 1` | conditional (merged forms, equal weights, supplied K and content) |
| Tree-curve relations, `V/T = (L'/4Utilde)^2` | established for quartic + cubic, large N for the last |
| No point with `beta_K = 1`, V = T, no negative mode | bounded no-go (class in the insert's scope sentence) |
| `q_*^2|_chi = (beta_K L'/4U_4) q_b^2` | conditional (first-order responses of L2806, fibre-constant chi, q^2 below m_chi^2) |
| Helicity +-2 vacuum moment | established (symbolic) for the merged vacuum form |
| Merged example not a one-loop stationary point | established given the Hessian; regulator enters only the size (>= 3.5 at N = 16 at the mildest cutoff sampled) |
| Sign of `q_*^2 - q_b^2`, long-range force, `G_eff` | unresolved |

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex`, in `sec:status-F`.

**Anchor:** insert the block immediately before the line `\section{Problem G: HBEV}` (occurs once; `apply_check.py`). The text before it is the closing sentence of the L2793 paragraph, "...Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL." followed by a blank line. Nothing is replaced or removed; the L2793 paragraph stays as it is and the new paragraph records the correction, as the L2707 paragraph does for L2696.

**Block:** `proposals/069-f-nonderivative-sector/appH_insert.tex` (11086 bytes LF, sha256 `5b4340bf6356a5fa3591ef7792c0b5d658a44f26487855ed6ce519ea1ce406ec`; convert LF to CRLF on insertion). It is the exact text; it is not duplicated here to avoid two copies drifting. Its paragraph title:

```latex
\paragraph{Conjugate-coordinate class times a fuzzy factor: the Hessian of a tree stabiliser on \(K\), the one-loop weights on the cubic branch and the exchange of the scale of \(K\) (conditional; bounded no-go; correction of the cubic and mass branches of the preceding paragraph).}
```

**Labels referenced (each verified to exist once):** `eq:Smatrix`, `def:matrix-coords-ext`, `ch:vierbein-emergence`, `ass:gap-psi`, `ass:lorentzian`. No new label.

**Bibliography:** one new entry, `new_bib_entry.bib`:

```bibtex
@article{IsoKimuraTanakaWakatsuki2001,
  author  = {Iso, Satoshi and Kimura, Yusuke and Tanaka, Kanji and Wakatsuki, Kazunori},
  title   = {Noncommutative Gauge Theory on Fuzzy Sphere from Matrix Model},
  journal = {Nucl. Phys. B},
  volume  = {604},
  pages   = {121--147},
  year    = {2001},
  doi     = {10.1016/S0550-3213(01)00173-0},
  eprint  = {hep-th/0101102},
  archivePrefix = {arXiv}
}
```

**Stale passages elsewhere:** L2810 (three `beta_K` forms), L2824 (example), L2844 ("does not need a tuned K"), L2846 ("for Uhat < 0 ... it is available at negligible Y"). I propose no in-place edit; the new paragraph names them and states their range of validity (`c = mu = 0` operators). If the gatekeeper prefers in-place qualifiers, that is a status-neutral wording choice for the next round.

**Not done:** no LaTeX compile was run (no build inside the repository; I did not make an outside copy). The gatekeeper should compile the block.

## Verification scripts

All in `proposals/069-f-nonderivative-sector/`, run with the repository Python from any directory.

| Command | Expected invariant output |
|---|---|
| `python proposals/069-f-nonderivative-sector/s1_cubic_hessian.py` | 24 rows, `worst residual: 7.82e-14`, `|dS|` ~1e-15 at chi = c/2, unfixed Hessian on gauge modes ~1e-15 (1.44 at c = 0), final line `PASS` |
| `python proposals/069-f-nonderivative-sector/s2_traces.py` | A: closed forms = quadrature (Vhat to 1e-5; U to the O(eps) term); B: `That/N^2` 3.99995, offset 1.016, `Uhat/N^2` 1.000 at N = 512; C: `m2 = (kappa^2-4)N^2(N^2-1)` exactly; D: `Vhat/That = kappa^2/4`, min eigenvalue -2 at kappa = -2; E: sign line `True`, zero at `eps*N^2 = 0.9257` |
| `python proposals/069-f-nonderivative-sector/s3_branch.py` | A: `L' = 5.34`, tree slope -5.34, `U_chichi` 15.72 / -5.04 / 10.68, `beta_K = 1.0`, `r = 1.16824`, `kappa = -0.33648`, `V/T = 0.028305`, `-14.83`; B: `beta_K = 2(r-1)/(delta-3r+4)`, check `0`; C: `27.526` (N = 16, 0.5), `441.207` (N = 64, 0.5), c = 0 check `-0.09003`; D: `m1 = 3 mu^2 N^2`; E: both `0.0283053...` |
| `python proposals/069-f-nonderivative-sector/s4_vacuum_moment.py` | `True`, `0`, `0` |
| `python proposals/069-f-nonderivative-sector/apply_check.py` | 17 PASS lines then `ALL PASS`, sha as above |

Saved outputs: `s1_cubic_hessian_output.txt`, `s2_traces_output.txt`, `s3_branch_output.txt`, `s4_vacuum_moment_output.txt`, `apply_check_output.txt`. `rename_r.py` is a one-off helper already applied (renamed `r` to `r_c` in the insert); it is idempotent and need not be run.

## Decisions Taken

- **Include the cubic Hessian rather than only restating scope** (F7 offered both). Reason: the Hessian is O(1) at the merged point and changes V/T, so a scope sentence alone would leave a misleading example in place. Rejected: scope-only note.
- **Record the correction as a new supplementing paragraph**, following the L2707 precedent, not as in-place edits of L2793-2848. Reason: smallest change that is accurate; keeps merged equations.
- **Normalise the cubic coupling as `C_ijk = i c eps_ijk/g^2`** so that the tree term is `abar(chi^4 - (2c/3)chi^3)` and the solution is `chi = c/2`. Rejected: a real C (imaginary action).
- **Do not compute second-order `U_2` / first-term responses on the merged operators.** Reason: they would inherit the omission; the corrected operators need a regulator first. This is recorded as avenues 3-4, not abandoned.
- **Keep the background Feynman gauge off the stationary point**, as the merged text does; note that at `r_c = 1` the background is on-shell on K.
- **Rank the rotating-K route first** among follow-ups, favouring the route that can still give `beta_K = 1` with V = T.
- No RESEARCHER-DECISION flags were pending (round 1).

## Milestone assessment

- **M3 (prior-claim error): I believe it applies; the gatekeeper decides.** The merged statements "With a tree cubic term beta_K = 1 is attained at a local minimum with Uhat > 0: ... at x = 3/10 ..." (L2824) and "V = T is approached at large N for this K and does not need a tuned K" (L2844), read together with the cubic/mass forms of L2810, are not one-loop statements for the action with that stabiliser. They are correct for the `c = mu = 0` operators only, and the scope sentence does not say so. Flag: PRIOR-CLAIM-ERROR (049), scope-omission type.
- M2 (no-go changing direction): partial. The static cubic branch on S^2_N is bounded; the direction moves to the rotating K or a completed stabiliser.
- Not a breakthrough. No critical-path step is derived.

## Status-label recommendation

Critical-path list re-derived from ch17 status lines and appH: A, B, C, D1, E, F, G-derived, N remain OPEN / CRITICAL PATH. Affected labels: none. F, C, N unchanged. No label edit is proposed or made.

## Author decision needed

None required for this package. For information only: avenue 2 (a supersymmetric completion of the cubic term) would add fermion-bilinear and mass terms that `eq:Smatrix` does not display; adopting it would be a core change for the author. It keeps spacetime emergent. It is not proposed here.

## Remaining open step

For the edge: the one-loop potential of chi and the second-order t terms (`U_2`, first term, first-term constant) with the stabiliser's Hessian included and a regulator derived from the matrices of M, or on a K whose stabilisation adds no tree Hessian (rotating class). For Problem F itself: unchanged from the ledger's missing step (operators, weights, scheme, `a_1`, `a_2`); for C: the scalar operator and coupling with `ass:gap-psi` discharged; for N: a ghost statement for the emergent metric. The K selected by the theory is still not constructed; `chi = c/2` is a tree stationary point of a supplied term, not a selection.

## Special instructions for the gatekeeper

1. Re-derive `kappa = 2 - c/chi` independently (the gauge-mode argument above is a two-line check) before relying on `s1`.
2. Check the normalisation of `q_*^2|_chi`: the phase-average factor and `L = 32 pi^2 m^6/A` are taken from L2836-2838; I verified only that the same convention reproduces `-q_b^2` from `U_4`.
3. The sentence on `c_T = T/3` at `r_c = 1` must not be read as a sign of `G_eff`; the insert says so. If it reads too strongly, cut it.
4. The numbers 27.5 and 441 depend on the cutoff choice `s_Lambda chi^2 N^2 = 1/2`; they are lower-end values (the term grows with the logarithm). Do not let the text imply a regulator-independent value.
5. "Within one loop ... no point has beta_K = 1, V = T and no negative mode" is for S^2_N with this cubic term only. It must not be extended to other K, to a completed stabiliser, or to the rotating class.
6. No "decides" wording appears; the F6 ratios are stated as one-loop values.
7. Compile the block on a copy; I did not.
8. Rule on M3. Nothing here touches labels, `def:matrix-coords-ext`, or any assumption.
9. `s1_cubic_hessian.py` and its output do not show as untracked in `git status` although I created them this session; I did not investigate. Check that the file on disk is the one described (its last line prints `PASS`).
