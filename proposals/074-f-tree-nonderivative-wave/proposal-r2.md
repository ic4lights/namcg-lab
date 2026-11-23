# Proposal 074-f-tree-nonderivative-wave, round 2

## Result

This round applies the review-r1 replacement texts verbatim, plus m1-m6. The mathematics of r1 is unchanged: s1 and s3 re-run with byte-identical output. The established content, restated without the r1 overclaims (m6):

1. **Localisation identity (established, exact).** For a wave A = eps(y) w, with w a fixed leaf function, the tree form is the leading symbol plus the single non-derivative term eps^2 <w.L(w)>. It has no first-derivative term and no tadpole.
2. **Rescaling realisation of the y^mu y^nu channel (exact in that realisation).**
   - T_tree = C_tree = 0 here.
   - Only T_tree = 0 holds in every realisation, because the background is stationary. So the tree terms cancel the tadpole of U_4 in no channel.
   - C_tree = 0 is a property of this realisation only. The other entries of the identity were obtained with the background torsion held and are not computed on it.
   - r1 Result 2 said the tree terms "cannot make the first pole Yukawa in this channel". That is withdrawn: it was shown for this realisation only, not for the identity's profile.
3. **Level-one realisation (conditional: frozen point, recorded normalisation).** Per sigma_1^2 the tree form is (3 rho_M/2g^2)(k^-2 - m^2). Normalised by the identity's constant L/2m^4, this is -3 varpi/m^2 from the leading symbol plus +3 varpi/(m^4 k^2) from the non-derivative term.
   - r1 Result 3 said the tree "supplies no positive q=0 constant in the recorded channel by either realisation". It is narrowed in two ways:
     - (i) The +3 varpi/(m^4 k^2) term is positive and dominates at small k. Its effect on the static response, where the frozen point is not controlled, is not determined.
     - (ii) The -3 varpi/m^2 term is not among the terms of the identity's displays L3051/L3055/L3111, which are the phase average of the induced density alone (M3).
   - The claim is now: "no positive constant at q=0 on these two realisations".
4. **Singlet sector (conditional).** At fixed sigma_1 the stationary value over the sigma_1-neutral singlet is C_tree = (1/4)(rho_M/g^2)(l^2+m^2). That is +vartheta varpi/2m^2 in the identity's normalisation.
   - r1 Result 4 presented this as "the Yukawa sign at tree strength" without qualification. It is now qualified: the value comes from extremising over the direction (P_perp - 3P)T, whose own non-derivative term is negative (eigenvalue -2 of L; curvature -4 of the form at fixed sigma_1). It is a maximum, not a positive-definite contribution.
   - Whether the static channel selects it is open.
5. **The identity's own profile.** This is the equal-weight elimination of all fibre harmonics. It is not computed in the r2 insert. A candidate computation is reported separately below (not for integration this round).

Nothing closes C, F or N. No status label changes.

## Target and status

Unchanged from r1:
- **F**: OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
- **C**: OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
- **N**: OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
- **Critical-path set** (ch17 and appH): A, B, C, D1, E, F, G-derived, N, all OPEN. No discrepancy found.
- **Package classification:** PROGRAMME-CONDITIONAL. It is a derivation-grade partial computation that shows the tree form depends on the realisation.

## Source reading

Digest + targeted reads:
- `make_digest.py --check` printed DIGEST CURRENT. The header has dirty-chapters: yes.
- appH L2977-3122 was re-read in full: the equal-weight elimination, the static response, the scale-of-K paragraph and the identity paragraph.
- E_a occurrences in appH were checked (L1610ff, L2685) for the m1 rename.

**No full scan was done.** The review states that the full scan is owed under 3(c) and 3(d) before integration.

## Research and reasoning

r1 sections (a)-(e) stand unchanged; see proposal-r1.md. The r2 changes are textual, so no new mathematics enters the insert.

### Finding by finding

| Finding | How addressed |
|---|---|
| M1 | Channel paragraph replaced verbatim. The added passage is placed after "...do not have the same tree form." E1-E3 replaced verbatim. The insert now says that the identity's own profile (equal weights, pointwise elimination) is not computed, and that the two realisations give different tree forms. |
| M2 | Consequence paragraph replaced verbatim. It claims "no positive constant at q=0" only on the two computed realisations, and states that the effect of the k^-2 term is undetermined. |
| M3 | Added passage, verbatim, last sentence: the -3 varpi/m^2 of the leading symbol is not among the terms of the displays of the two preceding paragraphs. |
| m1 | `\(E_a=0\)` becomes `\(\mathsf E_a=0\)`, and `\langle E\cdot A\rangle` becomes `\langle\mathsf E\cdot A\rangle`. The frame E in "(1+\epsilon\mathsf P)E" is kept. The first "In the normalisation of the identity" now reads "In the normalisation of the identity, that is after multiplication by its constant \(L/2m^4\), which is not the operator \(L\), ...". The later occurrence (singlet) refers back to it. |
| m2 | Covered by the channel replacement: T_tree = 0 in every realisation, from E = 0. |
| m3 | Scope sentence: "with the supplied bilinear term and the matter fields at their vanishing background" (verbatim). The same qualification is added at the degree argument, where it is load-bearing: "with the matter fields at their vanishing background every term of the quartic term ..., of the supplied bilinear term ...". The setting sentence now says "whose supplied bilinear term". |
| m4 | E3 keeps the item, qualified: "the tree non-derivative terms on the profile of the equal-weight elimination" (verbatim). |
| m5 | A sentence is added after "...the Yukawa sign at tree strength.": "This positive value is obtained by extremising over the \(\sigma_1\)-neutral direction \((\mathsf P_\perp-3\mathsf P)T\), whose own non-derivative term is negative, with the eigenvalue \(-2\) of \(L\) and the curvature \(-4\) of the form at fixed \(\sigma_1\)." The direction is verified: sigma_1 = -(4eps_1 + eps_y) = 0 gives eps_y = -4 eps_1, so w is proportional to T - 4PT = (P_perp - 3P)T, the -2 eigenvector (s2 (d)). The curvature -4 is the s3 (iii) output. |
| m6 | Results 2-4 are corrected above. |

### Candidate result (avenue 1; NOT in the r2 insert; for a later round)

**Script and profile.** Script: `s4_equal_weight_profile_candidate.py`, output saved. Setting: V = T, coupling (S1), dust at rest with constant u = yhat at the base point, static q = k e_3 with q.y = 0. The equal-weight elimination with the tree term gives alpha(n) = X v/(v.v + varpi), with X = uu + (1/2) eta and v^mu = M^{mu rho} q_rho (appH L3051-3055 structure). For m^2 k^2 << varpi:

alpha = X v/varpi + O(k^3).

Up to 1/varpi this is the polynomial leaf function w = u(u.Mq) + (1/2) Mq. Since u and X are constant, this is the literal profile, not an extension choice.

**Exact results (Lie-Poisson algebra, both signs s).**
- Mq = -s{q.T, T} is a gauge direction, so L(Mq) = 0. Hence L(w) = L(w1), with w1 = u(u.Mq).
- Pointwise, w.L(w) = (k^2/2)(2(M^03)^2 - (M^13)^2 - (M^23)^2).
- q.w = 0.
- The algebraic trace eta_{a mu}{w^a, y^mu} is proportional to y^3, so it vanishes on the base fibre. sigma_1 is therefore purely from derivatives.

**Fibre averages.** These follow from (M^03)^2 = (m^2/|y|^2) T_3^2 and sum_{i<j}(M^ij)^2 = l^2 (from M.M = 2l^2 - 2m^2). They are checked numerically to under 0.6% at two orbit points:
- <w.L(w)> = k^2 (m^2 - l^2)/3;
- <w.w> = k^2 (2l^2 - m^2)/12;
- <w.v> = k^2 (m^2 + 2l^2)/6.

**Per sigma_1^2, in r1 conventions.** The conventions reproduce the level-one value (3 rho/2g^2)(k^-2 - m^2) in the same script. After multiplication by L/2m^4:
- non-derivative term: +12 (m^2 - l^2) varpi / (m^2 k^2 (m^2 + 2l^2)^2), which tends to +12 varpi/(m^4 k^2) as l/m -> 0, four times the level-one value;
- leading symbol: -3 (m^2 - 2l^2) varpi/(m^2 + 2l^2)^2, which tends to -3 varpi/m^2, the same as at level one.

**Reading.** On the (small-k) profile of the identity, the tree non-derivative term is again positive and of order k^-2, not a constant at q=0. The reason is structural: the profile is of order k and has no algebraic trace, so sigma_1 is of order k^2 while <wLw> is of order k^2.

So a tree constant at q=0 per sigma_1^2 needs a profile component with k-independent algebraic trace, that is, the singlet directions T or PT. This points to avenue 2 (singlet kinetic matrix plus matter coupling) as the place where a positive q=0 constant could arise.

**Caveats (why it is a candidate only).**
- (i) At small k, <wLw>, of order |alpha|^2, dominates the loop form, of order k^4 |alpha|^2, and the tree leading symbol, of order k^2 |alpha|^2. A self-consistent elimination would have to include L, which is not a fibre multiplication operator. So this is the evaluation of <wLw> on the recorded profile, not a self-consistent elimination.
- (ii) The frozen base point is not controlled at small k.
- (iii) Only (S1), V = T and l/m arbitrary at y^i = 0 are covered.

Classification: conditional.

## Claim classification

- **Established (exact):**
  - localisation identity;
  - L(kappa T);
  - L(PT) = 2 P_perp T;
  - eigenvalues {6, -2};
  - one-component flatness at finite N, with the supplied bilinear term and the matter fields at their vanishing background;
  - T_tree = 0 in every realisation.
- **Conditional:**
  - C_tree = 0 on the rescaling;
  - the level-one values;
  - the singlet stationary value (a maximum over a negative direction);
  - the s4 candidate values.
- **Unresolved:**
  - a self-consistent tree term on the identity's profile;
  - which channel or singlet is selected;
  - the loop items of L3113;
  - the sign of the static scalar pole.

## Proposed changes

Everything is in `chapters/appH-microscopic-proofs.tex`.
- Pre sha256 (verified live): `29ac2a634bb819df7ecb29e138f97ae014656d4c0bb812b86f3573759a872046`.
- **Post sha256: `b704e29e5c8af4e5c779150cbfb074430f255e64e9dac98ce8b64e009d416efb`** (776980 bytes, 3721 lines, 0 bare LF).

**E1** (pre L3057, occurs 1x, inside the "response of the scale of K" paragraph). Old:
`The tree non-derivative terms, the terms that cancel the tadpole of \(U_4\) at \(q=0\), and any term with the same fibre dependence are not computed, and a long-range form needs them or \(\hat U\to0\);`
New:
```latex
The terms that cancel the tadpole of \(U_4\) at \(q=0\), any term with the same fibre dependence and the tree non-derivative terms on the profile of the equal-weight elimination are not computed (for two other realisations of this channel see the paragraph on the tree non-derivative terms below), and a long-range form needs them or \(\hat U\to0\);
```

**E2** (pre L3113, occurs 1x, inside the tadpole paragraph). Old:
`the part of the first term with the fibre flux, at first and at second order, and the tree non-derivative terms of the wave, which the leading symbol of the tree form drops, none of which is computed.`
New:
```latex
the part of the first term with the fibre flux, at first and at second order, and the tree non-derivative terms of the wave on the profile of the equal-weight elimination, which the leading symbol of the tree form drops, none of which is computed (on two other realisations of this channel the tree terms supply no positive constant; paragraph on the tree non-derivative terms below).
```

**E3** (pre L3121, occurs 1x, scope sentence of the tadpole paragraph). Old:
`the term of \(U_2\) proportional to \(W_R\), the tree non-derivative terms, higher loops or the fibre Laplacian`
New:
```latex
the term of \(U_2\) proportional to \(W_R\), the tree non-derivative terms on the profile of the equal-weight elimination, higher loops or the fibre Laplacian
```

**E4.** `appH_insert_r2.tex` is inserted immediately before the unique `\section{Problem G: HBEV}`, after the closing scope sentence of the tadpole paragraph and its blank line, exactly as in r1.
- File facts: LF in the folder, CRLF on apply; 9607 bytes; sha256(LF) `fd866a4ea38c9fa098eb57e8299cd5ce435ae2a12adc9e954f65d04e631605b9`; 6 blocks; one status sentence, at the end.
- r1's `appH_insert.tex` is kept unchanged.
- The insert is generated from r1 by `make_insert_r2.py`. Each old string occurs exactly once (`make_insert_r2_output.txt`).

Exact diffs of the insert, r1 to r2:
1. `the field equation \(E_a=0\)` becomes `the field equation \(\mathsf E_a=0\)`.
2. `\(\int\rho_M\langle E\cdot A\rangle\)` becomes `\(\int\rho_M\langle\mathsf E\cdot A\rangle\)`.
3. `whose bilinear term is that of the class` becomes `whose supplied bilinear term is that of the class`.
4. `every term of the quartic term with \(C_{\mu\nu\lambda}=0\), of the bilinear term and of the terms with the matrices of \(K\) is of degree two or zero in one component,` becomes `with the matter fields at their vanishing background every term of the quartic term with \(C_{\mu\nu\lambda}=0\), of the supplied bilinear term and of the terms with the matrices of \(K\) is of degree two or zero in one component,`.
5. Channel paragraph. `Hence \(T_{\mathrm{tree}}=C_{\mathrm{tree}}=0\) in this realisation: the tree non-derivative terms add nothing to ... do not cancel the tadpole of \(U_4\) in this channel.` becomes the review text: `Hence \(T_{\mathrm{tree}}=C_{\mathrm{tree}}=0\) in this realisation. That \(T_{\mathrm{tree}}=0\) holds in every realisation, since the background is stationary, so the tree terms do not cancel the tadpole of \(U_4\) in any channel; that \(C_{\mathrm{tree}}=0\) is a property of this realisation, on which the other entries of the identity of the preceding paragraph, obtained with the background torsion held, are not computed.`
6. `In the normalisation of the identity the leading symbol adds` becomes `In the normalisation of the identity, that is after multiplication by its constant \(L/2m^4\), which is not the operator \(L\), the leading symbol adds`.
7. After `the two realisations do not have the same tree form.` the review passage is appended: `These values are for the level-one profile \(\hat q\cdot T\). The identity of the preceding paragraph is stated at equal weights with all fibre harmonics eliminated at each fibre point; on that profile \(\langle\mathsf w\cdot L(\mathsf w)\rangle\) contains the fibre derivatives of \(L\) and is not computed. The reduced form of the paragraph on the response of the scale of \(K\) is the phase average of the induced density alone, so the term \(-3\varpi/m^2\) of the leading symbol of the tree form is not among the terms of the displays of the two preceding paragraphs.`
8. After `adds \(\vartheta\varpi/2m^2>0\) to its denominator, the Yukawa sign at tree strength.` this is appended: `This positive value is obtained by extremising over the \(\sigma_1\)-neutral direction \((\mathsf P_\perp-3\mathsf P)T\), whose own non-derivative term is negative, with the eigenvalue \(-2\) of \(L\) and the curvature \(-4\) of the form at fixed \(\sigma_1\).`
9. The Consequence paragraph is replaced in full by the review text (verbatim; see `make_insert_r2.py`, `new_cons`).
10. `They do not compute the loop profiles` becomes `They do not compute the tree non-derivative terms on the profile of the equal-weight elimination, the loop profiles`.
11. `the conjugate-coordinate class with the bilinear term and` becomes `the conjugate-coordinate class with the supplied bilinear term and the matter fields at their vanishing background and`.

**Other text.** L3006 and the C Missing step (L712) remain accurate and are not edited. No bibliography entries are added and no labels are added. The only `\ref` is `ch:vierbein-emergence`, which has one definition.

## Verification scripts

Run from `proposals/074-f-tree-nonderivative-wave/` with `python -I`.

| Command | Expected invariant |
|---|---|
| `python -I s1_matrix_flat_direction.py` | byte-identical to `s1_matrix_flat_direction_output.txt` (re-run r2: identical); "det = -16 a^2 < 0: OK" |
| `python -I s3_orbit_local_forms.py` | byte-identical to `s3_orbit_local_forms_output.txt` (re-run r2: identical); "value sigma**2/2", "curvature in d1: -4", "= -3 * varpi/m^2", "all checks passed" |
| `python -I s2_liepoisson_q0_hessian.py` | unchanged from r1 (not re-run in r2; the gatekeeper reproduced it in r1) |
| `python -I make_insert_r2.py` | 11 lines "old occurs 1x"; sha256(LF) `fd866a4e...05b9` |
| `python -I apply_and_build_r2.py --build` | pre-hash True; E1/E2/E3 "occurs 1x" at lines 3057/3113/3121, "inside intended paragraph True"; post sha256 `b704e29e...6efb`, "post-hash matches expected: True"; pdflatex rc 0, 422 pages; "undefined/multiply-defined warnings: 0"; "BUILD CLEAN"; "temp copy removed: True" (build in a `tempfile.mkdtemp` copy outside the repo) |
| `python -I s4_equal_weight_profile_candidate.py` (candidate only) | (a) "L(Mq) = 0 exactly: True" for s = ±1; (b) "L(w) = L(w1) exactly: True", w.L(w) = q3^2(2M03^2 - M13^2 - M23^2)/2; ratios ≈ 1 (within 0.6%); "level-one C = -3 rho (km-1)(km+1)/(2g^2k^2)"; "at ell -> 0: non-derivative 12/(k^2 m^4) * varpi ; leading symbol -3/m^2 * varpi" |

## Decisions Taken

- **Placement of m3.** The qualification goes both in the scope sentence (verbatim, as the review asked) and at the degree argument, where the hypothesis is used. Rejected alternative: the scope sentence only, which would leave the "to all orders ... also at finite matrix size" claim unqualified at the point where it is made.
- **Placement of m1's constant-L remark.** It goes at the first occurrence of "normalisation of the identity", where both L's appear in one paragraph.
- **Avenue 1 is kept out of the insert,** as directed, and reported as a candidate. Recommended next package: avenue 2 (the singlet kinetic matrix plus matter coupling). The s4 reading is that a q=0 tree constant per sigma_1^2 needs a profile with k-independent algebraic trace, which only the singlets have. This is ranked derivation-first.

## Milestone assessment

Routine.

## Status-label recommendation

None. C, F and N stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

- A self-consistent tree form on the identity's profile, including L in the elimination. s4 gives the evaluation only.
- The singlet kinetic matrix plus matter coupling (avenue 2).
- The one-loop profiles on the rescaling (avenue 3).
- The L3113 loop items (avenue 4).
- At the bottom of the list: other bilinear weights and a cubic on M (avenue 5).
- For the original targets, G_eff (F) and the full scalar operator (C). Both remain gated by D1.

## Special instructions for the gatekeeper

- **Full scan.** 3(c) and 3(d) apply, and the full scan is still owed.
- **Re-verify each r1 finding against the r2 insert:**
  - the verbatim replacement texts;
  - the m1 rename: `E_a` appears only as `\mathsf E_a`, and the frame E is untouched;
  - m5's identification of the sigma_1-neutral direction as (P_perp - 3P)T.
- **The s4 candidate is not for integration.** Assess it only as input to the next package. Do not assert that the identity's profile has been computed.
