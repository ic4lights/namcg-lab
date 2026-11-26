# Proposal 069-f-nonderivative-sector, round 2

## Result

This is a correction of text now in the tree that is false as written (M3, PRIOR-CLAIM-ERROR, scope-omission type), plus a supplementing paragraph with the exact cubic Hessian. Every review-r1 finding (F1-F8) is addressed. The r1 numbers that came from the truncated formula are replaced by values of the exact integral.

1. **What is false in the tree.** In the paragraph "Conjugate-coordinate class times a fuzzy factor: response of the scale of K to the frame ..." (appH L2949-3004, sha 6a72a326...), six sentences present one-loop statements for an action with a tree cubic or mass stabiliser on K. Those statements use `U_4`, `U_2` and `Y` of operators that omit that stabiliser's Hessian (`c_3 = mu = 0`), and the scope sentence (L3004) does not say so. They are corrected in place by six qualifiers, E1-E6 (quoted below), and the new paragraph E7 supplies the exact content.
2. **Exact (unchanged from r1, re-derived).** The K-vector operator is `H_V^K = chi^2 (L^2 - kappa_3 S.L)`, with `kappa_3 = 2 - c_3/chi`. The moment `sum w lambda^2 = (kappa_3^2 - 4) chi^4 N^2 (N^2-1)` is exact, so the s^-3 integral diverges logarithmically. At large N, `V/T = (1 - r_3)^2`.
3. **New this round (F1).** `mathcal U = s_Lambda^-2 sum w E_3(s_Lambda lambda)` holds exactly. The r1 truncated values were wrong at `s_Lambda chi^2 N^2 ~ 1`: the zero at 0.926 is an artefact. The exact integral is negative at every sampled limit `1e-4 <= s_Lambda chi^2 N^2 <= 30` for every sampled `kappa_3 <= 1.9` (N = 16, 64, 512). It is positive at some limits at N = 16 for `kappa_3 >= 1.95`. At the example the replacing term is 41.1 (N = 16) and 659 (N = 64) at limit 1/2, against the tree quartic 7.935.
4. **New this round (F3), the regulator-independent part.** At large N and `vartheta = 1`, `U_2` with the Hessian is `(2 - 5 kappa_3^2/4) x = +0.56`, not -0.9. Its slope is +1.70, not -1.8. With Y = 7.5 unchanged, the one-loop slope without the `mathcal U` term is already 9.2 > 5.34 = |tree slope|. The slope of the `mathcal U` term is positive at every sampled limit. So the example is not stationary for the sampled limits without counterterms. With counterterms, or with a regulator derived from the matrices of M, this is not determined.
5. **Conditional (F2).** On the cubic branch, `beta_K = -2 d(rho V_t/g^2)/U_chichi` and the derived `beta_K` relations are conditional on the uncomputed response of the `W_R` term of `U_2`. `1 - r_3 = -U'_loop/4Utilde` and `V/T = (U'_loop/4Utilde)^2` are not conditional.
6. **Bounded no-go (F5 wording).** On `S^2_N` with this cubic term at `c_3 != 0` and large N, no point has V = T and no negative mode, so none has `beta_K = 1` with V = T.

**Not established:** the original edge target (the second-order `U_2` and first-term response, the first-term constant, the sign of `q_*^2 - q_b^2`); any `G_eff` value or sign; any long-range statement.

## Target and status

- **Problem F** (appH L1824-1828, verbatim): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating \(G_{\mathrm{eff}}\) as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- **Missing step** (L1834-1842): the gauge-fixed operators and weights, proper-time limits, thresholds, continuation and finite-counterterm scheme; then the weighted `a_1` and the curvature-linear `a_2`.
- **ch17 F** (L403-412): "CRITICAL PATH; OPEN. The conditional heat-kernel identity does not compute the physical coupling." The target is the weighted `a_1` and curvature-linear `a_2` on the locked block, with a scheme stated.
- **C** (appH L552) and **N** (L3452) are carried by the closing sentences. Both are OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
- **Edge:** `F.t-nonderivative-sector`.
- **Gating** (pathfinder plan 2026-11-21, pointer only): D1 gates F.
- **Dependencies:** IKKT content (supplied), product background, `K = S^2_N` supplied, cubic term on K supplied (`def:matrix-coords-ext`: "the cubic term is not extended here"), Assumptions `ass:gap-psi` and `ass:lorentzian` retained.
- **Classification:** PROGRAMME-CONDITIONAL. Nothing is DERIVED.
- **Discrepancy (recorded, not resolved):** `eq:Smatrix` (ch03 L141-153) does not state the reality of `C`. The insert states the choice `C = i c_3 eps/g^2` as part of the supplied input.

## Source reading

**Digest + targeted reads + corpus-wide grep. A full scan was not done.**

- `make_digest.py --check` printed `DIGEST CURRENT` (head 4b7db5f, `dirty-chapters: yes`). The dirty diff is the 068 integration in sec:status-D (appH L1581, L1607-1628) and does not touch sec:status-F.
- appH sha256 is `6a72a326...b39a7c` (3587 lines, CRLF 3587/3587, no BOM).
- **Read in full:**
  - appH L1821-1842 (F ledger and missing step);
  - L2829-2851 (product backgrounds: factorisation, `W_R`, `W_X`, `c_T`, scope);
  - L2949-3006 (the whole paragraph edited here, every sentence E1-E6 touches, and the anchor);
  - the definitions of `vartheta = coth^2 tau` and `R/6+E_0 = 2 - 3vartheta/4` in L2863-2917 (read via targeted grep);
  - the L2918 paragraph for `A+B = V/8`, `c^TT = 8A/(1+varrho)`, `varrho` and the weight `kappa` (targeted grep);
  - ch17 L403-412;
  - ch03 L138-186 (`eq:Smatrix`, `def:matrix-coords-ext`);
  - every ledger status line (A L16, B L158, C L552, D L717, E L1633, F L1825, G L3010, H L3095, I L3182, J L3327, N L3452).
- **Corpus-wide grep** of all 30 `chapters/*.tex` for: cubic term, tree cubic, `beta_K`, `beta_K=1`, `S^2_N`, fuzzy sphere, stabiliser, tuned, Chern--Simons, Myers, `V=T`. The only hits outside L2949-3004 are ch03 L161/181 (cubic term; consistent), appH L1014 (a generic "cubic term" item in another problem), L2933/L2939 (`V=T` used as a hypothesis in the fibre-point paragraph, correctly scoped there) and unrelated "stabiliser" (group-theory) uses. None is made stale.
- **Protocol 3(c)/(d):** this package changes a scope sentence (E6), and the digest shows `dirty-chapters: yes`, so a full scan is mandatory. I did not read all 30 files in full: appH alone is 720 KB and the manifest is about 1.16 MB. What I did is the reads and grep listed above. The gatekeeper's full scan at the ACCEPT round remains required, as review-r1 already noted for 3(b).
- No file was unreadable.

## Research and reasoning

### Re-derivations relied on (repeated this round)

- **Cubic normalisation.** `(1/3!) Tr(C_ijk [X^i,X^j] X^k)` with `C = i c_3 eps/g^2` gives `(i c_3/3g^2) eps tr X^iX^jX^k`. On `X = chi J`, `eps_ijk J_iJ_jJ_k = i J^2` and `tr J^2 = nbar = 2abar`, so the term is `-(2c_3/3) abar chi^3`. Hence `V_t = abar(chi^4 - (2/3)c_3 chi^3)`, stationary at `chi = c_3/2`.
- **Hessian, `kappa_3 = 2 - c_3/chi`.**
  - The Yang-Mills flux term on the three K components is `-i chi^2 eps tr(J_k[a_i,a_j])`; the cubic second variation is `+(i c_3 chi/2) eps tr(J_k[a_i,a_j])`. So `2chi^2 -> 2chi^2 - c_3 chi`.
  - Gauge-mode check: on the `j = l` tower `S.L = -1`, and on-shell (`c_3 = 2chi`) the operator must equal the ghost operator `chi^2 l(l+1)`. That forces `kappa_3 = 0` there, which agrees.
  - `s1` checks this against the matrix action itself.
- **Second moment.** `tr(S.L) = 0` and `tr(S.L)^2 = N^2(N^2-1)` give `sum w lambda^2 = (kappa_3^2-4) chi^4 N^2(N^2-1)` (`s2` C).
- **Exact regulated integral (F1).**
  - `int_eps^inf ds s^-3 e^{-s lambda} = eps^-2 E_3(eps lambda)`.
  - `E_3(z) = 1/2 - z + (z^2/2)(-ln z + 3/2 - gamma) + sum_{k>=3} -(-z)^k/((k-2)k!)`.
  - With `sum w = sum w lambda = 0`, the first two terms cancel exactly. The r1 closed form is the `z^2` term, and its remainder is `O(eps lambda_max) = O(eps chi^2 N^2)`.
  - `s5` evaluates the exact form without cancellation (series for z < 1/2) and checks it against 40-digit quadrature (agreement to 1e-12). It reproduces the review-r1 table: -1.0515, -1.7891, -4.4519 exact against -0.0547, -1.1970, -4.3247 truncated.
- **Sign of the exact `mathcal U`** (`s5` C). The maximum of `mathcal U/N^4` over 99 limits in `[1e-4, 30]` is negative for every sampled `kappa_3 in {-0.99, ..., 1.9}` at N = 16, 64, 512. At N = 16 it is positive for `kappa_3 = 1.95` and 1.99, where the finite `c_3 = 0` part (`Uhat > 0`, O(N^2)) competes with the `(kappa_3^2-4)` O(N^4) part. The review-r1 statement "negative for every sampled `-1 < kappa < 2`" is therefore narrowed to `kappa_3 <= 1.9`, with the exception stated.
- **Example values (F1).** Units are `F sqrt|g| N^2 vartheta^2/32pi^2`, and `x = 3/10`. The value `c_3/chi = 2r_3 = 2.33648` comes from tree cubic/quartic = `-(4/3) r_3`. `P = -chi^4 mathcal U/N^2`, at fixed physical `s_Lambda`, is 41.09 (N = 16) and 659.39 (N = 64) at `s_Lambda chi^2 N^2 = 1/2`, matching the gatekeeper's (GK) 41.1 and 659. P is independent of `vartheta` at fixed x and `s_Lambda chi^2 N^2`.
- **Regulator-independent slope (F3).**
  - The merged `U_2 = -(F/32pi^2) sqrt|g| [2(Vhat-That) - (3/4) vartheta (Vhat - 2That)] chi^2`, with `Vhat -> kappa_3^2 N^2` and `That -> 4N^2`, gives `U_2 = [2(4-kappa_3^2)/vartheta - (3/4)(8-kappa_3^2)] x` in these units.
  - At `vartheta = 1` (the large-tau value, `vartheta = coth^2 tau`) this is `(2 - 5kappa_3^2/4)x = +0.5575`. It reproduces -3x = -0.9 at `kappa_3 = 2`, and it agrees with the exact spectra at N = 64 and 512 (`s5` E).
  - At fixed `c_3`, `d kappa_3/d ln chi = c_3/chi`, so `dU_2/dln chi = +1.705`.
  - `Y = (15F/64pi^2) vartheta^2 sqrt|g| N_K` comes from `s_0^K` (the scalar trace) and is unchanged: 7.5.
  - So `dU_2 + Y = 9.20 > 5.34`, and it stays above 5.34 for the sampled `1 <= vartheta <= 2` (8.27, 7.34, 6.40).
  - The `mathcal U` slope is positive at every sampled limit; its minimum over `[1e-4, 30]` is +0.016 (N = 16), +0.318 (N = 64) and +20.6 (N = 512).
  - Hence there is no stationary point at the example for those limits without counterterms. This replaces the r1 unqualified sentence and the gatekeeper's "at least 56", which held only for limits at or below about 1.
- **Tree curve.** `V_t' = 4abar chi^4 (1-r_3)` and `V_t'' = 4abar chi^4 (4-3r_3)` (`s3` B). Stationarity gives `1 - r_3 = -U'_loop/4Utilde`; with `V/T = (1-r_3)^2` this gives `V/T = (U'_loop/4Utilde)^2`, which needs no response assumption. Under the F2 condition, `beta_K = 2(r_3-1)/(4-3r_3+delta)`.
- **`q_*^2|_chi`.** Elimination gives `(U_4 - beta_K U'_loop/4) sigma_1^2` (`s3` B). The `U_4` part alone reproduces `-q_b^2` with the merged `L = 32pi^2 m^6/A` (GK verified). This uses the first-order responses of the preceding paragraph, which the insert now states.

### Fork: hypotheses and relaxations (ranked derivation-first)

| Hypothesis of the bounded no-go | Relaxation | Status |
|---|---|---|
| Static K with a tree stabiliser (Hessian present) | rotating K, stabilised kinetically, with no tree Hessian | open, rank 1: the only route on which `beta_K = 1` with V = T can still arise in this class |
| Bosonic cubic, no fermion bilinear | supersymmetric completion (mass-deformed IKKT class) | open, rank 2: test `sum w lambda^2 = 0` and V vs T |
| Proper-time cutoff in the Poisson limit, no counterterms | regulator from the matrices of M; cubic and mass counterterms | open, rank 3: decides stationarity, since the bounded statement here is only for the sampled limits |
| `W_R` response not computed | compute the first-order response of the `W_R` term of `U_2` | open, rank 4: lifts the F2 condition |
| `K = S^2_N` | other K (`S^2 x S^2`, flux stacks at `f_1 = f_2 + f_3`) | open, rank 5 |
| One loop | higher loops at `r_3 = 1` | open, rank 6 |

Ranks 1-4 can each give positive data for `beta_K` or for the t non-derivative sector. Gating: D1 gates F. None of these findings transfers to D1.

### Literature

- **Iso, Kimura, Tanaka, Wakatsuki**, hep-th/0101102, Nucl. Phys. B 604 (2001) 121-147, DOI 10.1016/S0550-3213(01)00173-0.
  - The INSPIRE record was fetched this round and gives the full author names Satoshi Iso, Yusuke Kimura, Kanji Tanaka and Kazunori Wakatsuki (this addresses the F8 initials point). The title, journal, volume, pages and DOI match.
  - It is cited only for "a Chern-Simons term is added to make the fuzzy sphere a classical solution". That statement is in the abstract (verified in r1 by the GK).
- **Not cited and not verified:** Hartnoll-Liu 2409.18706, Imai et al., Dine-Seiberg.

## Claim classification

| Claim | Class |
|---|---|
| `H_V^K`, spectra, stability range, gauge modes at `chi = c_3/2` | established |
| `sum w = sum w lambda = 0`, `sum w lambda^2` formula, mass moment `3mu^2N^2` | established |
| `mathcal U = s_Lambda^-2 sum w E_3(s_Lambda lambda)` and its expansion | established (identity) |
| Sign of exact `mathcal U` at sampled limits, `kappa_3 <= 1.9`; positivity near 2 at N = 16 | numerical (exact spectra, sampled grid) |
| `V/T -> kappa_3^2/4`; `U_2 = [2(4-kappa_3^2)/vartheta - (3/4)(8-kappa_3^2)] x` | numerical limit; conditional on the merged `U_2` form |
| Example: 41.1, 659; one-loop slope > tree slope at sampled limits, no counterterms | numerical, regulator-bounded |
| Not stationary with counterterms / matrix regulator | unresolved |
| `1 - r_3 = -U'_loop/4Utilde`, `V/T = (U'_loop/4Utilde)^2` | established (stationarity, large N) |
| `beta_K` relation on the cubic branch, `r_3 = (6+delta)/5`, `2/(delta-2)` | conditional (F2) |
| No V = T without a negative mode for `c_3 != 0` at large N | bounded no-go (class in the scope sentence) |
| `c_T = T/3` at `r_3 = 1` | conditional (merged forms, equal weights, supplied K); not a sign of `G_eff` |
| `q_*^2|_chi <= 0`; -14.8 `q_b^2` at the example (merged operators) | conditional |
| Original edge target; `G_eff` | unresolved |

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex` only. Pre-image sha256 is `6a72a3268302d46b9b5d3ede69f8b15e838a0a3c14bfddc2e1b4e8ab58b39a7c`; post-image sha256 is `120c8aba220c6a78277deaf4b98213ae84134cf141c198d1fcc1ea487db8439f` (733461 bytes, 3628 lines, CRLF throughout). Each old string occurs exactly once, inside the paragraph that begins at L2949, and is replaced by the new string. Nothing else in the paragraph changes. Status sentences: E1-E6 add none, and E7 has exactly one, at its end.

**E1 (L2966).** The sentence is false as a one-loop statement for the action with the cubic or mass term.

Old: "with \(\partial Y/\partial\ln\chi\) neglected in these three forms."

New:
```latex
with \(\partial Y/\partial\ln\chi\) neglected in these three forms; in the second and third, \(U_4\), \(U_2\) and \(Y\) are those of the operators without the Hessian of the tree cubic or mass term, so these are not the one-loop forms of the action with that term (next paragraph).
```

**E2 (L2966).** Old: "then \(\beta_K=1\) is attained in the cubic case"

New:
```latex
then, in these forms, \(\beta_K=1\) is attained in the cubic case
```

**E3 (L2980).** The sentence is false as written: with the Hessian, the example is not a stationary point at the sampled limits, and `V/T = 0.028` there.

Old: "With a tree cubic term \(\beta_K=1\) is attained at a local minimum with \(\hat U>0\):"

New:
```latex
With a tree cubic term, and the operators without its Hessian (next paragraph), \(\beta_K=1\) is attained at a local minimum with \(\hat U>0\):
```

**E4 (L3000; the r1 pointer L2970).** The sentence is false for any K stabilised by a tree cubic term: `V/T -> (1-r_3)^2`.

Old: "so \(V=T\) is approached at large \(N\) for this \(K\) and does not need a tuned \(K\);"

New:
```latex
so, for the operators without a tree stabiliser on \(K\), \(V=T\) is approached at large \(N\) for this \(K\) and does not need a tuned \(K\); with the Hessian of a tree cubic term it is not (next paragraph);
```

**E5 (L3002; review-r1 F7).** Old: "for \(\hat U<0\), where \(q_b^2<0\), it is available at negligible \(Y\)."

New:
```latex
for \(\hat U<0\), where \(q_b^2<0\), it is available at negligible \(Y\) in the forms with a tree stabiliser above, which omit its Hessian.
```

**E6 (L3004, scope sentence).** The pathfinder's point: the scope sentence did not state the `c = mu = 0` restriction.

Old: "with \(V=T\) where the index part alone enters \(U_2\) and with \(W_R\propto\hat V-\hat T\) neglected;"

New:
```latex
with \(V=T\) where the index part alone enters \(U_2\) and with \(W_R\propto\hat V-\hat T\) neglected; \(U_4\), \(U_2\) and \(Y\) of the operators without the Hessian of a tree stabiliser on \(K\), so that the forms with a tree cubic or mass term are one-loop forms only as its coefficient tends to zero;
```

**E7 (insert).**
- The block is `proposals/069-f-nonderivative-sector/appH_insert_r2.tex`: ASCII, LF, 12796 bytes, sha256(LF) `8f44109e6b86e1c7467ad8fcb3f6e2fb7cae06f92bebb0baf3cf8f8d29c7961c`. Convert it to CRLF.
- Insert it immediately before the unique line `\section{Problem G: HBEV}`, which comes after the scope sentence of the L2949 paragraph ("...Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL.") and its blank line. The block ends with a blank line.
- Its title is unchanged from r1 ("... (conditional; bounded no-go; correction of the cubic and mass branches of the preceding paragraph)").
- The text is not duplicated here, to avoid drift; it is the exact file.
- The phrase "next paragraph" in E1, E3 and E4 refers to E7.

**Labels referenced by E7** (each defined once, checked by the script): `eq:Smatrix`, `def:matrix-coords-ext`, `ch:vierbein-emergence`, `ass:gap-psi`, `ass:lorentzian`. E7 adds no label. E1-E6 add no reference.

**Bibliography:** `new_bib_entry.bib` (unchanged, LF; convert it to CRLF). The key `IsoKimuraTanakaWakatsuki2001` is absent from the current bib.
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

**Stale passages elsewhere:** none found by the corpus grep (Source reading).

**Build:** `apply_and_build_r2.py --build` copies the repository to a temporary directory outside the repo, applies E1-E7 and the bib entry, and runs pdflatex, bibtex, pdflatex and pdflatex. All exit with rc 0 (410 pages), with 0 undefined or multiply-defined warnings and no bibtex warning for the new key. The copy is then removed. The repository appH hash is unchanged (`6a72a326...`).

### Review-r1 findings and how each is addressed

| Finding | Action |
|---|---|
| **F1 (major)** truncated values | `s5` evaluates `mathcal U` exactly through `E_3`; the insert displays the exact identity and states that the remainder is O(1) at `s_Lambda chi^2 N^2 ~ 1`. 27.5/441 become 41.1/659 (reproduced). The 0.926 clause is deleted. The sign is stated for the exact integral, narrowed to the sampled `kappa_3 <= 1.9`, with the positive exception at N = 16 near `kappa_3 = 2` that my scan found (the gatekeeper's snippet "every sampled -1 < kappa < 2" was too broad). The proposal no longer uses "at least 3.5 times". |
| **F2 (major)** `beta_K` relation | The "Correction" ends with the gatekeeper's conditional sentence, verbatim apart from the symbol renaming. In "Tree curve" the `beta_K` relation, `r_3 = (6+delta)/5`, `(1+delta)^2/25`, `2/(delta-2)` and "beta_K -> 0" are marked "under the condition just stated". `1 - r_3` and `V/T` are kept unconditional. `q_*^2|_chi` now says "with the first-order responses of the preceding paragraph". The scope sentence lists "the response of the term of U_2 proportional to W_R" among the things not computed. |
| **F3 (major)** stationarity | The sentence is qualified, and strengthened by a regulator-independent part: `U_2` and `Y` alone give a one-loop slope of 9.2 > 5.34 at `vartheta = 1` (and for the sampled `vartheta <= 2`), and the `mathcal U` slope is positive at every sampled limit in `[1e-4, 30]`. Stationarity with counterterms or with a matrix regulator is stated as not determined. |
| **F4 (minor)** notation | `c -> c_3`, `r_c -> r_3`, `kappa -> kappa_3` (with a note that it is not the weight `kappa` of the fibre-point paragraph), `L' -> U'_loop`. The undefined `c\cdot c` (helicity +-2 vacuum moment) is removed together with that sentence, which carried no load. `s4` is kept but its result is no longer used in the text. `c_T` and `c^TT` keep their merged meanings. |
| **F5 (minor)** | Adopted: "at `c_3 != 0` and at large N, no point has V = T and no negative mode, so none has `beta_K = 1` with V = T". |
| **F6 (minor)** | "At large N the condition V = T holds only at `r_3 = 0` and at `r_3 = 2`, and at `r_3 = 2` the vector operator has the negative mode above." |
| **F7 (minor)** | L2966 "attained in the cubic case ... approached from below in the mass case" is qualified by E2 (via E1's "these forms"), and L3002 by E5. E7's first sentence of "The example of the preceding paragraph" names all of them. In-place qualifiers are used, at the orchestrator's instruction that the false sentences be corrected where they stand. |
| **F8 (minor)** | The digest head is refreshed (4b7db5f). CRLF conversion of the bib is noted. The full author names are now verified on INSPIRE (r1 had only initials). |

## Verification scripts

Run from any directory with `python -I`. Every command was re-run this round.

| Command | Expected invariant output |
|---|---|
| `python -I proposals/069-f-nonderivative-sector/s1_cubic_hessian.py` | identical to `s1_cubic_hessian_output.txt`: worst residual `7.82e-14`, final `PASS` |
| `python -I proposals/069-f-nonderivative-sector/s2_traces.py` | identical to saved; C: `m2 = (kappa^2-4)N^2(N^2-1)` exactly; D: `Vhat/That -> kappa^2/4`. (E is the truncated form and is superseded by s5.) |
| `python -I proposals/069-f-nonderivative-sector/s3_branch.py` | identical to saved; A: `r = 1.16824`, `kappa = -0.33648`, `V/T = 0.028305`, `-14.8333`; B: `beta_K = 2(r-1)/(delta-3r+4)`, check `0`. (Its part C is the truncated form and is superseded by s5 D. Its line "W_R term ... 1.4575" is the W_R part of U_2 alone; adding the T part -(3/4)vartheta That x = -0.9 gives the total +0.5575 of s5 D/E.) |
| `python -I proposals/069-f-nonderivative-sector/s4_vacuum_moment.py` | identical to saved (`True`, `0`, `0`); not used in the text |
| `python -I proposals/069-f-nonderivative-sector/s5_exact_regulated.py` | A: quad = E_3 form to 1e-12. B: `-1.0515 / -1.7891 / -4.4519` exact. C: `negative ... kappa <= 1.9 ...: True`, positive entries only at N=16, kappa 1.95/1.99; `kappa=2` gives `0.99998`. D: `P = 41.09` (N=16), `659.39` (N=64) at 0.5; `U_2 = +0.5575`, `dU_2/dlnchi = +1.7047`; `dU_2+Y > 5.34: True` for vartheta 1, 1.2, 1.5, 2; min slopes `+0.016 / +0.318 / +20.613`, each `all > 5.34: True`. E: `U_2 = +0.5572` (N=64), `+0.5575` (N=512) |
| `python -I proposals/069-f-nonderivative-sector/apply_and_build_r2.py --build` | pre-hash `True`; E1-E6 each `occurs 1x ... inside target paragraph True` at lines 2966, 2966, 2980, 3000, 3002, 3004; insert at line 3006; post sha `120c8aba...439f`, `post-hash matches expected: True`; 5 labels defined 1; cite in additions 1; `BUILD CLEAN`; `temp copy removed: True` |

Saved outputs: `s5_exact_regulated_output.txt`, `apply_and_build_r2_output.txt` (and the r1 outputs, re-checked as identical). `apply_check.py` and `appH_insert.tex` are r1 artefacts and are superseded.

## Decisions Taken

- **In-place qualifiers plus the supplementing paragraph** (E1-E6 + E7), rather than r1's insert-only. The orchestrator identified the in-tree sentences as false as written, and a supplement alone leaves them false where a reader meets them. Each qualifier is a phrase inserted into the existing sentence; no equation or number of the merged text is removed. Rejected alternatives: rewriting the `beta_K` forms (larger than needed), and insert-only (leaves false text).
- **Sign statement narrowed beyond the gatekeeper's snippet**, because my exact scan finds positive values at N = 16 for `kappa_3 >= 1.95`. Stating the narrower result is required by accuracy.
- **F3 strengthened with the regulator-independent slope**, rather than only qualifying it. This favours an accurate redirect: the example fails stationarity without counterterms whatever the sampled cutoff, which moves the open route to counterterms or a matrix-derived regulator (rank 3) and to the rotating class (rank 1).
- **Dropped the helicity +-2 vacuum-moment sentence**: its notation (`c\cdot c`) is undefined in the tree, and it bears on no conclusion.
- **`vartheta = 1` stated explicitly** for `U_2` at `kappa_3 != 2`, since the `W_R` part carries `1/vartheta` (the merged example value is `vartheta`-independent only at `kappa_3 = 2`). The robustness for sampled `vartheta <= 2` is recorded.

## Milestone assessment

- **M3 (prior-claim error): applies.** It was upheld in review-r1, and r2 now corrects the false sentences in place. Flag: PRIOR-CLAIM-ERROR. Per review-r1, this item goes to the author after an ACCEPT rather than to autonomous integration.
- **M2 is subsumed under M3.**
- Not a breakthrough; no critical-path step is derived.

## Status-label recommendation

The critical-path list, re-derived from ch17 and the appH ledger lines, is A, B, C, D (D1 in ch17), E, F, G (G-derived in ch17) and N. All eight are OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL (OPEN count on the critical path: 8 of 8). H, I and J are OPEN and OPTIONAL. The naming difference (appH section letters D and G against the ch17 items D1 and G-derived) is recorded, not resolved. Affected labels: none. No label edit is proposed or made.

## Author decision needed

None. (Information only: a supersymmetric completion of the cubic term, avenue rank 2, would add terms that `eq:Smatrix` does not display. Adopting it would be a core decision; computing it is not.)

## Remaining open step

- **For the edge `F.t-nonderivative-sector`:** the one-loop potential of chi with the stabiliser Hessian under a regulator derived from the matrices of M (or with stated counterterms); the response of the `W_R` term; then the second-order `U_2` and first-term response and the first-term constant; or the same on a rotating K.
- **For Problem F:** unchanged ledger missing step (operators, weights, scheme, `a_1`, `a_2`).
- **For C:** the scalar operator and coupling, with `ass:gap-psi` discharged.
- **For N:** control statement for the emergent metric.
- **Not addressed here:** the K selected by the theory is not constructed.

## Special instructions for the gatekeeper

1. Verify the in-tree falsity independently: E3 and E4 are the load-bearing corrections. Check that `V/T = (1 - r_3)^2` follows from `H_V^K` and that the example has `r_3 = 1.168`.
2. Re-run `s5` and confirm the exact-`E_3` values and the sign exception near `kappa_3 = 2` at N = 16. The text must not claim negativity for all `kappa_3 < 2`.
3. Check the `U_2` assembly `[2(4-kappa_3^2)/vartheta - (3/4)(8-kappa_3^2)] x` from the merged L2960 display, and that `Y` is unchanged by the K-vector Hessian. The F3 statement rests on these together with the sign of the `mathcal U` slope at the sampled limits.
4. "Not a stationary point" must stay bounded to the sampled limits without counterterms.
5. The `c_T = T/3` sentence is not a sign of `G_eff`.
6. The full scan (3(b)/(c)/(d)) is still owed at the ACCEPT round; I have not done it.
7. `s3` part C and `s2` part E are superseded truncated forms; the manuscript numbers come from `s5` only.
