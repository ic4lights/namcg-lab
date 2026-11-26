
**Stale passages elsewhere:** none. The 068 paragraph's (R1)/(R2) statements are scoped to vanishing connection and stay correct. ch17 and ch10 are unaffected. The frontier edge text ("no source read supplies one") is a report-side pointer, not manuscript text.

## Verification scripts

All scripts are in `proposals/071-d1-curved-torsion-backgrounds/` and are run with `python -I` from any cwd. Each script adds its own folder to `sys.path`.

**Modules**

| File | Role |
|---|---|
| `bg.py` | constant section-value geometry and brackets (independent re-implementation; agrees with `core068.brackets` to 1e-15) |
| `symgeom.py` | exact sympy version of the same |
| `opcheck.py` | operator-level bundle check |
| `invariants.py` | invariants of the Lie algebra, the torsion and the curvature |
| `lin.py` | backgrounds; gauge vectors with the `xi R` term; `Q` with connection |
| `core068.py`, `tools068.py` | verbatim copies of the 068 `core.py`/`tools.py`; the only change is the import line in `tools068` |

**Reproduction pack**

| Command | Expected invariant output |
|---|---|
| `python -I s1_backgrounds.py` (about 3 min) | `B1 == 0 identically: True ; B2 == 0 identically: True` for F_tau and for H; general-m ansatz `B1 ∝ m1**2 - 2*m1*s - m3**2`, `B2` empty; trace `s*(tau**2+4*tau+1)/(2*tau)`; `T_abc T^abc = 0` (F), `2*kappa**2` (H); `R_abcd R^abcd = 0` for both; scalar `-s**2*(tau+1)**2/tau` (F), 0 (H); R rank 1; trace-free point `m = [0, -s, 0, sqrt(3)*s]`, trace `[0,0,0,0]` |
| `python -I s0_operator_check.py` (about 4 min) | for F and H, all entries ≤ 5e-14 and `matrix_eq_max` ≤ 1.4e-14; control `matrix_eq_max` ~ 1e2 |
| `python -I s2_linearised.py` (about 6 min) | (a) rank 30, `|MG|` ~ 1e-15, kernel = span G True, `|MG0|` O(1-10); (b) `|dB2/dh|` O(1-10); (c) `≤ 3e-15`; (d) alpha sets `{±1.73, ±1.73±1j, ±1.73+2j}` (trace-free) and `{-0.5j, -1.5j, -2.5j}` (tau=1), Q `{±1.73}` and `{-1.5j}`; converse at tau=1 ~ 1e-16 vs control ~ 1e-3; (e) `≤ 1e-15`; (f) `|dB2'/df| ≤ 1e-14`, rank Y = 18 |
| `python -I s3_survey.py` (about 6 min) | flat `eta`: `59 converged, 56 with R != 0`, `max |RR| ~ 3e-15`; flat Euclidean: `0 converged`; stored solvable solutions: residuals ≤ 4e-11, RR `-7.1e-04, 8.9e-04, -3.7e-03, ~1e-12`, `dim[g,g] 2`, derived series `[2, 0]` |
| `python -I x1_isotropic.py`, `python -I x1b_flrw.py` | isotropic flat: `B1_00 = 3 beta**2 s`; FLRW brackets as recorded |
| `python -I apply_and_build_r1.py --build` | pre `d8d8b678fa0ceabe03f3f9c2f56cc60dbe140aa845658beddb0c206ba26c9180`; post `a73760f2181d68d04e99915aac756907a2ef753f746e4920d388c37bfc0e13c0`; block sha256 `9ccda7041a51984b22994e2cdecba1967786c485673d2be3316caaf82c7e02f3`; `BUILD CLEAN`, 0 undefined/multiply-defined, 414 pages, temp copy removed |

## Decisions Taken

- **Background class.** I took left-invariant data with a constant nonzero connection. This is the minimal relaxation of the 068 hypothesis "vanishing connection", and it keeps exact harmonic analysis available.
  - Rejected first: isotropic and FLRW torsion. The static and flat isotropic cases have no solution (x1). The time-dependent case is singular and not homogeneous in time.
  - Rejected second: non-constant connections, which lose the polynomial reduction.
- **Linearised example.** I linearised family (i) rather than (ii), because (i) has constant coefficients and a full translation commutant, so the spectrum is exact in characters. I report two points: the trace-free point, which avoids the `t` subtlety, and `tau = 1`, which has rational data and the cleanest numerics.
- **Meaning of "mass".** "Mass/gap" means an isolated value of `q^2` on the characteristic variety, which is gauge-invariant because the translation labels are commutant eigenvalues. Cone shifts along `k` are not counted as masses (hazard F3).
- **What goes into the insert.** The isotropic no-go and the FLRW reduction stay out of the insert (smallest text). The survey stays in as one sentence, because it locates the next avenue (non-null solutions).
- **Converse root test at the trace-free point.** The converse test there is numerically weak. I recorded it with its numbers and qualified it ("clean only for m=(0,2,0,0)"), rather than dropping the point.

## Milestone assessment

**Routine.** This is a conditional sub-lemma. It supplies the named missing input (R != 0, T != 0 solutions), generalises the 068 reduction and gives a bounded no-gap statement for one null family. No critical-path step is derived from the matrix theory, so no milestone trigger applies.

## Status-label recommendation

- **Critical-path list:** A, B, C, D (D1), E, F, G-derived and N, all OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. This is derived from ch17 L330-343 and L645-716 and from the appH ledger lines L16, L158, L552, L719, L1635, L1827, L3070 and L3512.
- **Optional:** H, I and J are OPEN and OPTIONAL.
- **Recommendation:** no label change.

## Author decision needed

None.

## Remaining open step

To close D1, the following are still needed:
- derive local SO(3,1) and the locked frame with its non-degeneracy from the matrix integral (selection of the class, of `A`, and of the backgrounds);
- specify `omega, A, B` and the ghost operators with a norm and a regulated trace.

On the narrower torsion/propagating-modes item, the ranked open avenues are (derivation-first):
1. **Linearise the non-null survey solutions** (`R_abcd R^abcd != 0`, solvable groups with a 2-dim abelian derived algebra). No scaling symmetry is shown for them, so they are the first place where an invariant scale, and hence a genuine gap, could appear. This needs the harmonic analysis of non-unimodular solvable groups (characters only on `q ⊥ [g,g]`, plus the infinite-dimensional representations).
2. **Linearise family (ii)** in the oscillator sectors `p != 0`. The Heisenberg structure constant `kappa` is not boost-covariant along `k`, so (ii) can carry an invariant scale. Test whether `R != 0` modifies the 068 Landau-level/Nielsen–Olesen growth `Gamma <= kappa/2`.
3. **Interpret the imaginary cone shifts** (`e^{beta k.y}` growth of section values) with a form. This ties to `D1.krein-finiteN-dS` and must not become an E package.
4. **(Bottom)** Further null families with `R_abcd R^abcd = 0` and a boost-dilation symmetry. The scaling argument already excludes an isolated mass shell for them, so their expected output is the same no-gap result.

**What transfers to F (gated on D1, ch17 L650-653):** on these backgrounds the operator content (`Q` with connection, the block `Y`, and the gauge kernel with the `xi R` term) is the tree-level `omega`/frame quadratic operator that a one-loop F computation would consume.

## Special instructions for the gatekeeper

- **Re-derive by hand:**
  1. `F = -c t` for constant section values;
  2. `∂_I = D_I - 1/2 w_I S` at `u = 1`, and the resulting label section values `(h, omega) = (-f δ_I, -f w_I)`; check the sign against s2 (c);
  3. the diffeomorphism gauge direction with `xi^c R_ca^{de}`;
  4. the boost-dilation argument, i.e. `[B,N] = -N` and `k -> e^{-theta} k` with the stated conventions, and the inference from it.
- **Must not be asserted:**
  - that the torsion modes are massless "in general";
  - that the backgrounds are selected;
  - that the imaginary shifts are or are not instabilities;
  - that (ii) or the survey solutions have no gap;
  - any norm statement.
- **The roots are numerical.** The converse test is clean only at `tau = 1`, and the insert says this.
- **The survey statement** ("56 of 60", "none for Euclidean") is numerical and not a classification.
- **Anchor:** insert before the unique `\section{Problem E: signature}`, after the 068 paragraph's status sentence. The pre-hash is the live appH (dirty tree from the 068/069 integrations). The block has exactly one status sentence, which is in its last paragraph. No new labels or citations are added.
