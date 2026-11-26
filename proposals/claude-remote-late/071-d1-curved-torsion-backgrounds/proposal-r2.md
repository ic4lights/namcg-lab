# Proposal 071-d1-curved-torsion-backgrounds, round 2

## Result

Round 2 addresses all seven findings of `review-r1.md` (AWRR, two major, five minor). It also fixes one error in r1 that the review did not flag (the scalar `R_ab^{ab}`, see S below) and adds one fully verified exact family (finding 7).

**Established (unchanged from r1 unless stated):**
1. **Exact backgrounds with `R != 0` and `T != 0`** in the first-order equivariant class, on left-invariant data with constant connection.
   - Family (i): flat frame, `w = s k B + m N`, on the hyperbola `(m_1-s)^2 - m_3^2 = s^2`.
   - Family (ii): time x Heisenberg, `w = k(zeta N + x N')`, `(zeta,x) != 0`.
   - All three brackets hold, including the order-zero part.
2. **New in r2 (finding 7): the wider Heisenberg family.** On `[E_3,E_1] = kappa E_2`, the connection `w = k(aB + zeta N + x N')` solves all three brackets for all real `kappa, a, zeta, x`. The data are:
   - `T_ac^c = a k_a` and `F_13 = a kappa/2` (the only pair of F);
   - `R_13^{cd} = kappa(aB + zeta N + x N')` (the only pair of R);
   - `R_abcd R^abcd = -4 a^2 kappa^2`, `R_ab^{ab} = 0` and `T^2 = 2 kappa^2`.

   For `a != 0` this is the **first exact solution in the class with `R_abcd R^abcd != 0`**, on a unimodular algebra, with a background scale `kappa`. The survey solutions with R² ≠ 0 are numerical only. The gatekeeper's control `w = ±kB` (κ = 1) is the slice `a = ±1`, `zeta = x = 0`.
3. **Linearised equations on (i)** are unchanged: the label reduction to `Q`, the block-triangular form, and the gauge kernel with `xi R`.
4. **Converse cone test, now clean at both points (finding 2).** It drops rank on each cone at both points: `sigma_30/sigma_1 <= 1.3e-16`, against controls of `2.8e-5` to `3.0e-2`. The r1 "weak converse at the trace-free point" was an s2 artefact: alpha had been rounded to 2 decimals. **The r1 Jordan/defective-roots reading is withdrawn.**
5. **No isolated mass shell and no invariant scale on family (i).** This bounded no-go is unchanged and rests on the boost-dilation symmetry.

**Not established:** none of this closes D1. Selection of the class, of `A`, of the backgrounds and of the frame is not shown. There is no norm and no regulated trace, and everything is tree level. The wider family (ii) is not linearised. D, F and N remain OPEN and PROGRAMME-CONDITIONAL.

## Target and status

Unchanged from r1. The appH sha was re-checked at the start of r2: `d8d8b678...9180`, the live tree.
- Problem D (D1 route): OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. The item attacked is "torsion or propagating modes".
- Dependencies (ch17): D1 supplies operators to F; F gates N.
- The critical-path OPEN set at full-GR scope is A, B, C, D, E, F, G, N. H, I and J are optional. No discrepancy was found.

## Source reading

- **Mode:** digest + targeted reads. `DIGEST CURRENT`; `dirty-chapters: yes`, from the uncommitted 068/069 integrations.
- **Re-read for r2:**
  - appH L1513-1519, the coordinate form `D_a = u e(∂ - u ω ∂_u) + t - iA` and the fluctuation sign `+½ω S`;
  - appH L1619-1629, the 068 paragraph including L1623.
- **No full scan by this package.** It changes no definition, assumption, scope or status passage. Edit E corrects one sign in a merged results sentence. The review notes that the gatekeeper's full scan is still owed.

## Research and reasoning

### Finding 1 (sign convention): A applied; every sign-sensitive value checked

At `u = 1`, ½w^{cd}S_cd acts on u as `w^c_f ∂/∂u_f^c`, while L1519 has `-ω^c_f ∂/∂u_f^c`. So the code normalisation (`bg.py`, `symgeom.py`, `core068.py`: first-order part `E + ½ w S`) is `w = -e·ω`. Snippet A defines w by exactly this normalisation, so every value in the insert is stated for this w. I confirmed each value with the literal-L1519 operator script `gk071_op.py` (re-run with `python -I`), using `ω = -w`:

| value in insert (w normalisation) | gk071_op input (L1519 ω) | gk071_op output | check |
|---|---|---|---|
| `T_ac^c = (s+m_1)k_a` | ω = kB + 2N, i.e. w with s=-1, m_1=-2 | trace `[-3,0,-3,0]` | `(s+m_1)k = -3k` ✓ |
| trace-free at `m = (0,-s,0,±√3 s)` | ω = kB + (0,-1,0,√3)N, i.e. w with s=-1, m=(0,1,0,-√3) | trace 0 | ✓ (also a member of the family under w → -w) |
| `R_13 = κ(ζN + xN')` | ω = k(N + ½N'), i.e. w with ζ=-1, x=-½ | R_13: (01) -1, (12) -1, (03) -½, (23) +½ | ✓ |
| wider (ii): `T = a k`, `R_13^{02} = aκ` | ω = kB, i.e. w with a=-1 | trace `[-1,0,-1,0]`, R_13^{02} = -1 | ✓ |
| `F = -c·t`, third bracket | all four runs | order-zero part `0.0e+00` | ✓ |

**alpha sets.** These are sign-sensitive. New check `s2_linearised_r2.py (g)`: the dilation `D → -D` maps solutions to solutions, sending `w → -w` and `q → -q`, so `alpha(-w) = -alpha(w)` numerically:
- `{±√3, ±√3±i, ±√3+2i} → {±√3, ±√3±i, ±√3-2i}`;
- `{-i/2, -3i/2, -5i/2} → {+i/2, +3i/2, +5i/2}`.

So these sets hold as written for `s = 1` in the w normalisation of snippet A. In L1519 terms at `s_ω = 1` they would be the negatives. I kept the w statement, which is correct under A.

**Convention-independent statements:**
- the solution sets (each family is closed under `w → -w` with `(s,m) → (-s,-m)`);
- the invariants;
- the boost-dilation argument;
- "β real".

### Finding 2: s2 rounding fixed; B applied with the re-run numbers

The fix is a new script, `s2_linearised_r2.py`; `s2_linearised.py` is kept as the r1 record. In part (d):
- the raw alpha of all roots are clustered (tolerance 5e-3; roots with `|k·q| < 1e-3|q|` and `|alpha| < 1e-3` are dropped as k·q≈0 artefacts);
- each cluster median is matched to a closed form `±√n + i b/2`, accepted only within 1e-4;
- the converse is then tested at **both** the unrounded median and the closed form.

Results:
- trace-free point: all 8 cones `<= 1.3e-16`, both at the medians (`<= 5.1e-16`) and at the closed forms; medians agree with closed forms to `<= 3e-14`;
- `tau = 1`: all 3 cones `<= 1.0e-16`;
- controls: `1.2e-4 ... 3.0e-2` and `2.8e-5 ... 8.6e-3` respectively.

Snippet B was applied with "against `3·10^{-5}` to `3·10^{-2}`" in place of the template's "at least `10^{-4}`", because the re-run minimum control is 2.8e-5. **The Jordan/defective-roots reading is withdrawn.** The trace-free point's weak separation in r1 came entirely from testing at alpha = 1.73 instead of √3.

### Findings 3, 4, 6

- C and D were applied verbatim.
- s1 print label fixed: `m = (0,-s,0,sqrt3 s)`. The value was already +√3 s; s1 was re-run.
- `gk071_surv.py`, re-run: stored solution 2 has `tr ad = (-0.12, -0.06, -0.08, 0.01)` (not unimodular), and solution 4 has trace T 0.26. C now says "not all unimodular" and that t and the third bracket are not examined.

### Finding 5: edit E (merged 068, appH L1623)

The 068 sentence "the gauge with constant frame and `ω_a^{12} = ϑ k_a` ... has the same torsion for `ϑ = -½`" was computed in the 068 code normalisation, `w = ϑk`. Under `w = -ω` the value is `ϑ = +½`. Re-verification is in `v4s_068_signmap.py`, an adapted copy of 068 `v4_null_rotation_vartheta_r2.py` that imports 068 core/tools read-only with bytecode writing disabled. It checks three things:
1. **Torsion.** ω-ϑ = +½ (code w = -½) gives `max|T - T_left-inv| = 0`. ω-ϑ = -½ gives 1.0. `T^2 = 0` in both cases.
2. **Cones and multiplicities, at every ω-ϑ the text names (-½, ½, 1, 2) and at -1 and -2.** All 40 roots lie on `(q + jϑk)^2 = 0` with `max|x-j| <= 2.7e-10`, multiplicities `{0:4, ±1:6, ±2:2}` per crossing, and `ALL ROOTS ON CONES ... True`.
3. **Chains and exact ranks at ω-ϑ = 1 (code w = -1)**, the value at which the text states them:
   - partial multiplicities `[2,2,2,2]`, `[4,5,6,6]`, `[4,4,4,4]`, `[4,5,6,6]`, `[2,2,2,2]` for j = -2..2, so chains are at most three;
   - exact ranks are 28/26/26/26/28 and generic rank 30, the same as the 068 record at code w = +1.

So the 068 statements on cones, multiplicities, chains and ranks are unchanged under the sign map; only the torsion-matching value changes sign. The cone set is symmetric in j, and `D → -D` maps the spectrum at ϑ to that at -ϑ. Edit E is the single replacement `\(\vartheta=-\tfrac12\)` → `\(\vartheta=\tfrac12\)` inside "has the same torsion for ..., with". That string occurs once, at L1623.

### Correction found in r2 (not in the review): the scalar `R_ab^{ab}`

r1 stated `R_ab^{ab} = -2 s m_1` on family (i). That number came from `symgeom.py`/`invariants.py`, which computed `Σ_b Ric_b^b η_bb`; this is not a Lorentz scalar. The scalar is `Ric_b^b`.

By hand: on (i), `R_ab^{cd} = ρ_ab N^{cd}` (rank one), with `ρ_01 = -ρ_12` (s1 output), and N has nonzero components only at (01) and (12), both equal to 1. So `R_ab^{ab} = 2(ρ_01 + ρ_12) = 0`. The same holds on gk071_op's operator read-off: at `tau = 1`, `R_01^{01} = 2` and `R_12^{12} = -2`.

Changes:
- `symgeom.py`: `scal` is now `Ric_b^b`, and the r1 quantity is kept as `scal_weighted`;
- `invariants.py`: `scal = trace(Ric)`;
- s1 and s3 were re-run;
- insert replacement S: `R_abcd R^abcd = R_ab^{ab} = 0`.

Family (ii) and its wider form also have `R_ab^{ab} = 0`. The survey "scalar" column changed, but it is not used in the insert.

### Finding 7: Heisenberg with `aB` (verified fully and added to the insert)

**Section values** (`x2_heisenberg_kB.py`, exact sympy, all four parameters symbolic):
- B1 and B2 have no nonzero entry for any `kappa, a, zeta, x`;
- `trace T = a k` and `T^2 = 2κ²`;
- `R_13` as stated, rank one, with `R^2 = -4a²κ²` and scalar 0;
- Ricci depends only on `(zeta, x)`, so for `zeta = x = 0` the Ricci tensor vanishes while `R^2 != 0`;
- `F = -c·t`, whose only pair is `F_13 = aκ/2`, and the third bracket `∇^a F_ab - T_ab^c F^a_c = 0` identically.

**Operator level** (`x3_op_heisenberg.py`, an adapted copy of `gk071_op.py`; literal L1519 vector fields on (y,u) at a random Lorentz u, ω = -w), at four parameter points (κ, a, ζ, x) = (1,1,0,0), (1,-1,0,0), (1,½,1,-⅓), (2,-3/2,½,1):
- first relation `0`, vector part `<= 3.5e-16`, order-zero part `0`;
- trace `a k`, `R_13` as predicted, and `F_13 = (multiplication part) + T_13^c t_c = aκ/2`.

This meets the review's bar ("all three brackets plus the order-zero part"). One sentence was added after the itemize. Snippet D's text for (ii) is kept verbatim as the `a = 0` slice.

**Bearing on the target.** It is a background with a dimensionful invariant (`R^2/T^2 = -2a²` in units where `T^2 = 2κ²`, and `κ` itself). The boost in the 0-2 plane does not preserve `[E_3,E_1] = κE_2`, because it mixes the central E_2 with E_0. So the boost-dilation argument that excludes a mass shell on (i) is not available here. This is the first exact solution on which an isolated mass shell or gap is not excluded by symmetry, which makes it the top avenue below.

## Claim classification

| claim | class |
|---|---|
| (i), (ii) solve all three brackets | established (exact; operator check) |
| wider (ii), `w = k(aB+ζN+xN')`, solves all three brackets; invariants as stated | established (exact symbolic section values; operator check at 4 points) |
| `R_ab^{ab} = 0` on all families | established (by hand + exact) |
| sign map `w = -e·ω`; values valid in w normalisation | established (by hand + gk071_op) |
| `alpha(-w) = -alpha(w)` | established (D → -D symmetry), numerical check |
| alpha sets, converse clean at both points | numerical |
| no isolated mass shell / invariant scale on (i) | established, given the exact symmetry (bounded no-go: flat-frame null family (i), tree level, linear order) |
| 068 L1623 value is `ϑ = +½` under L1519; cones/multiplicities/chains unchanged | established (numerical roots, exact ranks) |
| survey solutions with c free | numerical, not classified; t and the third bracket not examined |
| Jordan/defective roots at the trace-free point | **withdrawn** |

## Proposed changes

**File `chapters/appH-microscopic-proofs.tex` only.** The pre-hash is `d8d8b678fa0ceabe03f3f9c2f56cc60dbe140aa845658beddb0c206ba26c9180` (live tree, verified).

1. **Insert** `appH_insert_r2.tex` (CRLF, 9280 bytes, sha256 `169d1239...fff8d`) plus one blank CRLF line, immediately before the unique line `\section{Problem E: signature}` (L1631), i.e. after the 068 paragraph ending "Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL."
2. **Edit E**, appH L1623. In the paragraph beginning "The null-rotation algebra solves the equation for \(\eta\)", the unique string
   `has the same torsion for \(\vartheta=-\tfrac12\), with`
   becomes
   `has the same torsion for \(\vartheta=\tfrac12\), with`.
   Nothing else in the 068 paragraph changes.

The post-hash is `c1a880e53a5eb0d70751f4ea4dfeec65d6acf66a8c498ed82e72b4a581e3e891` (753073 bytes, no bare LF). The added `\ref`s were each verified to be defined once: `eq:Smatrix`, `ass:frame-lock`, `ass:nondeg`, `ass:lorentzian`, `ass:local-lorentz`, `ass:EFT-a2`, `ch:vierbein-emergence`. No new labels, no citations, no bib change. There is one status sentence, in the last paragraph.

### Exact diffs from r1 (applied by `make_insert_r2.py`, each asserted to occur once in `appH_insert_r1.tex`)

- **A**: `but give the connection constant components \(\omega_a{}^{cd}=w_a{}^{cd}\) in this frame.` → `but give the connection constant components \(w_a{}^{cd}\) in this frame, normalised so that the first-order part of \(\mathbb D_a\) at \(u=1\) is \(E_a+\tfrac12w_a{}^{cd}\mathcal S_{cd}\), the sign of the fluctuation \(\tfrac12\omega_a{}^{cd}\mathcal S_{cd}\) below; in the coordinate form of the paragraph on local \(\mathrm{SO}(3,1)\) inside the unitary group this is \(e_a{}^\mu\omega_\mu{}^{cd}=-w_a{}^{cd}\).` (snippet A verbatim)
- **S** (new, scalar correction): `\(\mathsf R_{abcd}\mathsf R^{abcd}=0\), \(\mathsf T_{abc}\mathsf T^{abc}=0\), \(\mathsf R_{ab}{}^{ab}=-2sm_1\), and` → `\(\mathsf R_{abcd}\mathsf R^{abcd}=\mathsf R_{ab}{}^{ab}=0\), \(\mathsf T_{abc}\mathsf T^{abc}=0\), and`
- **D**: snippet D verbatim.
- **H** (new, finding 7), appended after `is cancelled in the first bracket by the torsion terms. `:
  ```latex
  On the algebra of (ii) the wider ansatz \(w_a{}^{cd}=k_a(aB^{cd}+\zeta N^{cd}+xN'^{cd})\) solves all three brackets for all real \(\kappa,a,\zeta,x\): \(\mathsf T_{ac}{}^c=a\,k_a\), the only nonzero pair of \(\mathsf F\) is \(\mathsf F_{13}=\tfrac12a\kappa\), the only nonzero pair of \(\mathsf R\) is \(\mathsf R_{13}{}^{cd}=\kappa(aB^{cd}+\zeta N^{cd}+xN'^{cd})\), and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4a^2\kappa^2\), \(\mathsf R_{ab}{}^{ab}=0\), \(\mathsf T_{abc}\mathsf T^{abc}=2\kappa^2\) (exact for the section values; for the operators on the bundle at random Lorentz \(u\), including the order-zero part, residual below \(10^{-15}\)). For \(a\neq0\) it is an exact solution with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\) on a unimodular algebra.
  ```
- **C**: snippet C verbatim.
- **B**: the r1 converse sentence → `Conversely the forty equations drop rank at random complex points of each of these cones (numerical; the relative smallest singular value is about \(10^{-16}\) at both points, against \(3\cdot10^{-5}\) to \(3\cdot10^{-2}\) at random points off the cones).`
- **SC1**: `the two families named,` → `the families named,`
- **SC2**: `Family (ii) and the survey solutions` → `Family (ii), its extension with \(a\neq0\) and the survey solutions` (rest of the sentence unchanged).

The full insert text is in `appH_insert_r2.tex`; `appH_insert_r1.tex` is kept.

## Verification scripts

| command (from this folder) | checks | expected invariant output |
|---|---|---|
| `python -I gk071_op.py` (about 30 s) | literal L1519 operators, sign map | (i) trace-free: trace 0; tau=1: trace `[-3,0,-3,0]`; (ii): R_13 `(01) -1, (12) -1, (03) -0.5, (23) 0.5`; control: trace `[-1,0,-1,0]`, R_13^{02} = -1; all order-zero parts `0.0e+00` |
| `python -I x3_op_heisenberg.py` (about 22 s) | wider (ii) at operator level | 4 runs: first relation 0, vector part ≤ 3.5e-16, order-zero 0; `F_13 = 0.5, -0.5, 0.25, -1.5`; R_13 = κ(aB+ζN+xN') |
| `python -I x2_heisenberg_kB.py` | wider (ii) exact; scalar | `so the first two brackets hold for all kappa, a, zeta, x`; `R_abcd R^abcd = -4*a**2*kappa**2 ; scalar R_ab^ab = 0`; third bracket `[0, 0, 0, 0]`; family (i): `true scalar ... = 0`, weighted `= -2 s m_1` |
| `python -I s1_backgrounds.py` | (i), (ii) exact | `B1 == 0 ... True ; B2 == 0 ... True` twice; `scalar R_ab^ab = 0` for F and H; label `m = (0,-s,0,sqrt3 s)` |
| `python -I s2_linearised_r2.py` (about 10 s) | linearisation; unrounded converse; sign map | `SUMMARY F (... trace-free): max over cones at closed forms 1.3e-16 ; min over controls 1.2e-04`; `SUMMARY F (s=1, tau=1): ... 1.0e-16 ; ... 2.8e-05`; (g) `alpha(-w) = -alpha(w)` |
| `python -I s3_survey.py` (about 80 s) | survey | 56 of 60 with R≠0 for η, max R² 3.4e-15; 0 for Euclidean |
| `python -I v4s_068_signmap.py` (about 5 s) | edit E | `omega-vartheta = +0.5 ...: max|T - T_left-invariant| = 0.0e+00`; `ALL ROOTS ON CONES ... True`; chains `[4,5,6,6]` for j = ±1; exact ranks 28/26/26/26/28, generic 30 |
| `python -I gk071_roots.py`, `gk071_068.py`, `gk071_surv.py` | gatekeeper scripts | unchanged outputs (ϑ = -0.5 gives 0.0 in code w) |
| `python -I make_insert_r2.py` | builds the insert | 8 replacements applied once; sha `169d1239...` |
| `python -I apply_and_build_r2.py --build` | apply on a temp copy outside the repo + build | pre `d8d8b678…` True; E anchor line 1623; post `c1a880e5…`; pdflatex 414 pages; `undefined/multiply-defined warnings: 0`; `BUILD CLEAN`; temp copy removed |

All outputs are saved as `*_output.txt` (s2 as `s2_linearised_r2_output.txt`).

## Decisions Taken

- **Sign convention: keep the w normalisation (A) rather than restating values in L1519 ω.** A is the gatekeeper's text, it ties w to the fluctuation sign already in use, and it makes every scripted value directly checkable. The rejected alternative was to flip every value to ω terms, which needs more text and carries a risk of partial flips.
- **Converse controls: give the actual range instead of the template's "at least 10^{-4}".** The re-run minimum is 2.8e-5, and inventing a bound would be an unsourced number.
- **Added the wider Heisenberg family to the insert** (one sentence) after full verification. It is positive, derivation-grade input: an exact R² ≠ 0 background with a scale and no boost-dilation symmetry, which is what avenue 1 consumes. The rejected alternative was to record it only in the proposal; that would leave the manuscript claiming that the only R² ≠ 0 solutions are numerical survey points.
- **Corrected `R_ab^{ab}`** within the same insert rather than in a separate package. It is a materially false number in text not yet merged.
- **Edit E is the minimal one-token change**, with full re-verification of the dependent 068 statements.

## Milestone assessment

Routine. The wider family is an exact existence result inside an assumed class. It derives no critical-path step from the matrix theory. Not a breakthrough.

## Status-label recommendation

None. D, F and N remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. No label is touched, and edit E changes a number, not a status.

## Author decision needed

None.

## Remaining open step

To close D1, the following are still needed (unchanged):
- derive the class, `A`, the backgrounds, the frame and its non-degeneracy from the matrix integral;
- specify the operators with a norm and a regulated trace.

Avenues on the torsion/propagating-modes item, re-ranked derivation-first:
1. **Linearise the wider Heisenberg family `w = k(aB+ζN+xN')`, `a != 0`,** in the oscillator sectors `p != 0`, using the 068 Schrödinger modes (`heisenberg_modes`) with `wbar != 0`. It is exact, unimodular and has `R² = -4a²κ² != 0`. No boost-dilation symmetry removes its scale, and it has a nonzero background `F_13 = aκ/2`. This is the first place where an isolated mass shell / gap for the Lorentz or torsion modes is not excluded by symmetry. Questions to answer: does `a` shift the 068 Landau levels `q_0² = p² + κp(2n+1∓2)`, and does it lift or deepen the Nielsen–Olesen-type growth `Γ ≤ κ/2`?
2. **The c-free survey solutions** (non-unimodular). First examine `t` and the third bracket, then harmonic analysis on solvable groups.
3. **A form/norm for the imaginary cone shifts** on (i) (ties to `D1.krein-finiteN-dS`; not an E package).
4. Nonlinear evolution and one loop on these backgrounds (feeds F).
5. Non-constant connections.
6. **(Bottom)** Further null families with a boost-dilation symmetry. The expected output is the same no-gap result.

**Transfer to F (gated on D1):** the operator content on (i) (`Q` with connection, block `Y`, gauge kernel with `xi R`) and, once avenue 1 is done, on the wider (ii).

## Special instructions for the gatekeeper

- Re-run `x3_op_heisenberg.py` and `x2_heisenberg_kB.py` for sentence H. The F_13 readout adds `T_13^c t_c` to the multiplication part of `[D_1,D_3]`, because `[D_a,D_b] = -T D + ½RS + F` with `D_c` containing `t_c`.
- Check the R_ab^{ab} correction by hand: rank-one `R = ρ ⊗ N` with `ρ_01 = -ρ_12`.
- Do not let H be read as a gap or mass result. It is existence plus invariants only, and it is not linearised (SC2 says so).
- Edit E: confirm that only the torsion-matching value changes. The cones, multiplicities, chains and ranks were re-verified at the ω values named in the text (`v4s_068_signmap.py`).
- The full scan noted as owed in review-r1 is still outstanding on the gatekeeper side.
- No files outside this folder were changed. 068 modules were imported read-only, with bytecode writing disabled, and the 068 `__pycache__` timestamps are unchanged.
