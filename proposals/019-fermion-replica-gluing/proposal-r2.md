# Proposal 019-fermion-replica-gluing, round 2

## Changelog r1 -> r2 (review-r1: ACCEPT WITH REQUIRED REVISIONS, M2, OPEN 0/3)

- **F1 (done).** Deleted "as in the replica of the preceding paragraphs"; added "(for integer spin, the identity at integer \(n\))" after "its representation of the rotation group".
- **F2 (done).** "the domain of the first-order operator" in the tip-domain sentence replaced by "the less singular self-adjoint extension of the first-order operator", with the statement that this is the extension giving an analytic continuation and that the componentwise-regular domain gives `sum_k |a_k| = n/4` (even `n`) or `(n^2-1)/(4n)` (odd `n`), parity-dependent and non-analytic. Checked exactly for `n = 1..9` in `absk_check.py` (the review's observation; I re-derived it: odd `n`, `m = (n-1)/2`, `sum|k| = m(m+1)`; even `n`, `sum|k| = n^2/4`).
- **F3 (done).** The conditional list now contains "the choice of self-adjoint extension, the uniqueness of the continuation from integer \(n\)". Exclusion of the periodic values phrased "for the stated extension its values ... do not apply". The rotated-branch exclusion is phrased "if the continuation from integer \(n\) is unique, ... are not continuations". (Wording slightly beyond the review's snippet; same content, makes the exclusion visibly conditional.) The old clause "the domain of the first-order operator" stays in the list after the new items, as the review's snippet specifies.
- **F4 (done, optional).** First insert paragraph split in two (second begins "The unrotated periodic gluing above ...").
- **F5 (done, optional).** `number = {50}` added to `CasiniHuerta2009`.
- The LaTeX makes no `a_2`/`W_4` claim and does not identify the `alpha^4` locus with 018's `f1 = f2` (the sentence only says the order vanishes for self-dual or anti-self-dual flux). The proposal text (R-b1 Step 1, avenue 2) still mentions the BPS locus in prose only, outside the LaTeX.
- Remaining-open-step section replaced by the five ranked avenues. No label change.
- Review note "complete the unread chapters": ch02 and ch16 hits (the only fermion mentions per the review) do not interact with the insert; I did not do a full scan, so this remains "digest + targeted reads" (inserting a paragraph under an existing Problem B passage does not change a definition, assumption, scope or status passage).
- `appH_insert.tex` now equals the r2 LaTeX block exactly (checked by script below). Anchors re-verified (`verify_anchors_r2.out.txt`): replaced sentence "The gluing selected by the matrix state is not determined here." count 1; insert anchor "...or the Kaluza--Klein sector. Problems~B, C, D, F and~G remain open." count 1, immediately followed by `\section{Problem C: conformal mode and Cassini}` (line 193, count 1). Scratch compile outside the repository (amsmath, amssymb, `\LUV`, stub `\cite`): no error, undefined or overfull message; scratch copy removed afterwards.

## Result

Targets: Problem B (`G_T` vs `G_A` gap, integrated 017 block, `sec:status-B`) with its Problem A input (replica gluing from the modular flow). Bounded sharpening of a bounded no-go. Nothing is closed.

1. **R-a1: the fermion gluing is fixed, not free** (conditional on: quasi-free state, modular flow = rotation by `2 pi t` acting through each field's rotation representation, tip domain of the first-order Dirac operator). `Tr rho^n` of the ungraded trace gives, in the polar frame, antiperiodicity under the angle `2 pi n`; for Cartesian components of transverse spin `sigma = +-1/2` the monodromy is `-exp(2 pi i n sigma)`, which is `(-1)^{n+1}` at integer `n` (Casini-Huerta) and `-e^{+-i beta/2}` at `beta = 2 pi n` (Fursaev-Miele eq. 4.6). The two statements are the same condition written in two frames (`twist_ksum.py`, section 1). The k-sum is `sum_k a_k^2 = (n^2-1)/(12 n)`, analytic in `n`; `(1 - n d_n)` at `n = 1` is `-1/6` per two-component block, so `c_A(Dirac) = +1/3`, `c_A - c_T = 4 - n_D`, and at `(n_D, N_s, alpha) = (2, 6, 1)`: `c_T = 0`, `c_A = 2`. **The D=10 Lambda^2 mismatch stands** for the `Tr rho^n` gluing.
2. **017's "unrotated periodic" branch is not `Tr rho^n`.** Cartesian phase `+1` for all `n` is `Tr rho^n` at odd `n` and the graded `Tr[(-1)^F rho^n]` at even `n` (`(-1)^{(n+1)F}`; `twist_ksum.py` section 2). It additionally uses the componentwise-regular domain, which for the same twists is `-2` times the Dirac-domain value (odd `n`, section 6), so it is not the heat trace of the square of the first-order operator either. The `0 = 0` coincidence at `n_D = 2` (gap `4 - 2 n_D`) is therefore not a replica result. (The scout's guess "periodic = graded trace" is only half right: neither; mixed by parity of `n`.) The graded `Tr[(-1)^F rho^n]` has `a = 1/2` at `n = 1`, `sum a^2 = 1/4 != 0`: not normalised, a fermion-parity defect, cannot give an entropy.
3. **The rotated-vector branches `3 - n_D`, `5 - n_D` are not continuations of `Tr rho^n`.** Rotation by `2 pi n` is the identity on an integer-spin index at integer `n`; the rotated `n<1` branch gives `13/24` against `1/24` per circular component at `n = 2` (section 7). Integer-`n` data fix the unrotated gluing for the vector. At `n_D = 2` the only surviving value of the gap is `2`; for the (excluded) rotated analytic branch it would be `1`; none vanishes.
4. **Structure of the surviving gap:** `c_A - c_T = 4 b + n_D` with `b = 1 - n_D/2`: the weight of the cone-blind `rho^2 X` plus a spin term `+1` per Dirac field (cone value `+1/3` minus its `rho R[g_rho]` coefficient `-2/3`). At `n_D = 2` the whole gap is the spin term.
5. **R-b1 Step 1 (verified in the paper, eqs. 3.7, 3.9, 3.10).** `N_tot` and `b` are exactly the orders `alpha^0` and `alpha^2` of the SO(1,9) character restricted to flux along the 4 Poisson directions: `alpha^0`: `8 - 4 n_D`; `alpha^2`: `(n_D - 2)(x^2+y^2)/2 = -b (x^2+y^2)`; so `c_T = N_tot/6 - 4 b` is zero at `(2,6)` because both cancel. The first surviving order is `alpha^4`: `(x^2-y^2)^2/16` at `n_D = 2`, proportional to `V_4 = -4 tr F^4 + (tr F^2)^2` with ratio `-3/8` on random 10D `F` (scripts), `>= 0`, vanishing exactly for (anti-)self-dual flux. This is a statement about the character, not about the `a_2` coefficient of the operators.
6. **R-a3 (bounded, only half confirmed):** an R-holonomy `mu = m(n-1)` does not move the `n -> 1` derivative of a Dirac-domain fermion block (`sum (a_k+mu)^2 = sum a_k^2 + n mu^2`), but scalar-like components with the componentwise-regular domain get `+-m` (kink). Nishioka-Yaakov's cancellation therefore depends on the scalar tip domain; not resolved.

Problem B stays OPEN. Nothing here derives the state, the modular flow, the tip domain of the vector, `ass:EE`, or a value/sign of `G_eff`.

## Target and status

Problem B (`sec:status-B`): Status OPEN, Priority CRITICAL PATH, Completion PROGRAMME-CONDITIONAL ("The first-law identity is established, but the stationarity condition for the tensor block is not derived", appH line 45). Problem A: OPEN, CRITICAL PATH (matrix-derived), PROGRAMME-CONDITIONAL. Chapter 17 `sec:ch17-done` (line 691): A, B, C, D1, E, F, G-derived, N required; H, I, J optional. No discrepancy found between appH, ch17 and the ledger. Original target of B: derive tensor-block stationarity from the microscopic action, `ass:EE` no longer an assumption. This package addresses only the gluing/normalisation sub-gap left by 017. Classification: PROGRAMME-CONDITIONAL (conditional result, hypotheses stated).

## Source reading

Digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST STALE` (dirty chapters, as announced); I read the sources directly. Read in full: `reports/sme-scout-gluing-fermions-20261015.md`; `proposals/017-GT-GA-gap/proposal-r2.md`, `review-r2.md`; the integrated 017 block in `chapters/appH-microscopic-proofs.tex` (lines ~179-191) and the `sec:status-B` header; `ch17` `sec:ch17-done` (head). Not read: other chapters (no full-scan claim).

Literature, opened by me this session (PDF text extracted):
- Casini-Huerta, arXiv:0905.2562 (J. Phys. A 42 (2009) 504007): Sec. 2.1, eq. (16) matrix `T` with last entry `(-1)^{n+1}`; eigenvalues `e^{i2 pi k/n}`, `k = -(n-1)/2..(n-1)/2` (roots of `(-1)^{n+1}`); eq. (27)-(28) fermion entropy `S = 2 int dlambda log Z/(lambda-1)^2`; footnote 2 (Rindler: `rho^n` = rotation by `2 pi n`, origin of the fermion signs). Verified.
- Fursaev-Miele, hep-th/9605153 (Nucl. Phys. B484 (1997) 697): eq. (4.4) antiperiodic in polar tetrad, (4.5)-(4.6) `-e^{i sigma_3 beta/2}`, (4.8)-(4.13) heat kernel; text after (4.11): `beta > 2 pi` "by analytical continuation" from `beta <= 2 pi`. Verified. (4.13): spin-1/2 coefficient is minus the scalar one.
- Manta-Steinacker-Tran, arXiv:2411.02598: eq. (3.7) `Q_10 = Tr_R(e^{i alpha Sigma^V dF} - (1/2) e^{i alpha Sigma^Psi dF} - 2)`; (3.8)-(3.9) 4+6 split `(Psi) = (2_- x 4_-) + (2_+ x 4_+)`; (3.10) `chi^(4) = 4 - 2 alpha^2 dF^2 + O(alpha^4)`, `chi^(2_pm) = 2 - (alpha^2/2) dF^2 + ...`; sentence "expansion of Q_10 starts at O(alpha^4) as a result of maximal supersymmetry". Verified from the PDF (page images 12-13).
- Not opened: Steinacker 2303.08012 eq. (4.21) (`V_4`; quoted by the scout; I only compare my numerics to the stated form), Nishioka-Yaakov, Huang-Zhou, Dowker, Solodukhin beyond 017's verified equations. Marked not independently verified.

## Research and reasoning

### 1. The gluing (R-a1)

(a) *Frames.* `psi_p = exp(-i theta Sigma_12) psi_c`, `Sigma_12 = sigma = +-1/2`. A smooth plane has `psi_c` periodic, hence `psi_p` antiperiodic (FM 4.4). `Tr rho^n` of the ungraded Fock trace: Grassmann-odd fields are antiperiodic around the modular circle `beta = 2 pi n` (one sign per `rho`, counted by rotation by `2 pi n`, plus the trace sign; CH footnote 2). So `psi_p(theta + 2 pi n) = -psi_p(theta)` and `psi_c(theta + 2 pi n) = -e^{2 pi i n sigma} psi_c`. At integer `n` this is `(-1)^{n+1}` for both `sigma`; at `n = 1` it is `+1` (smooth plane). Script section 1.

(b) *k-sum.* Diagonalising the cyclic matrix with last entry `(-1)^{n+1}` gives twists `a_k = k/n`, `k = -(n-1)/2..(n-1)/2` (CH). Periodic Cartesian (`+1`) gives `k/n`, `k = 0..n-1`: it coincides with the antiperiodic set for odd `n` and with the graded set `{1/2 + j/n}` for even `n` (asserted in the script). Graded at `n=1`: `a = 1/2`.

(c) *Tip domain (derivation, my own).* Per two-component block with flux `a`, `0 < a < 1/2`, the Dirac operator fixes the pair of Bessel orders `(upper, lower)` mode by mode: `(m+a, m+1+a)` for `m >= 0`, `(1-a, -a)` at `m = -1`, `(|m+a|, |m+a|-1)` for `m <= -2`. The lower component is the componentwise-regular spectrum except that the single `m' = 0` order is `-a` instead of `+a` (the less singular extension). With the Cheeger contribution `-nu/2` per order (analytic for `nu > -1`), the conical constant is `B_2(a) + a = a^2 + 1/6` per block (componentwise-regular: `B_2(|a|)`). Then `sum_k [C_D(a_k) - C_D(0)] = sum a_k^2 = (n^2-1)/(12 n)`. Cross-checks: (i) this is the 2D `c = 1` Dirac result (`(1/12)(1/n - n)` structure, CH); (ii) the polar-frame zeta value on the branch `n < 1` per component is `(n^2-1)/(24 n)`, exactly half; (iii) the componentwise-regular `n > 1` branch plus the sign-flipped mode (`+(n-1)/(2n)`) reproduces the `n < 1` form identically (script section 4) - so 017's two branches (`-1/12`, `5/12`) differ precisely by that mode, and the Dirac domain selects the analytic one, consistent with FM's continuation from `beta <= 2 pi`. At odd `n` the componentwise-regular periodic sum is `-2 sum a^2` (section 6).

(d) *n -> 1.* `F(n) = (n^2-1)/(12 n)`: `F(1) = 0`, `F'(1) = 1/6`, `(1 - n d_n)F|_1 = -1/6`; with weight `-1` and two blocks per 4D Dirac field: `c_A(Dirac) = +1/3` in units scalar `= 1/6`; equals the value of 017 and Solodukhin (126)-(127). The extension choice (`|a| < 1/2` less-singular) is the standard one and is conditional.

(e) *Vector.* For integer spin the rotation by `2 pi n` is trivial at integer `n`; the integer-`n` traces equal the unrotated k-sum (`B_2` multiplication theorem). The rotated cone function `B_2({n})/(2 n)` agrees at integers but its `n<1` analytic branch does not (`13/24` vs `1/24` at `n=2`): by uniqueness of the analytic continuation from integers (Carlson-type, assumed) only the unrotated one is the `Tr rho^n` continuation.

(f) *Gap with the gluing fixed* (`gap_fixed.py`): `c_A - c_T = 4 - n_D` (unrotated vector); `n_D = 2` gives `c_T = 0`, `c_A = 2`. The decomposition `4 b + n_D` is arithmetic: per Dirac, `c_A - (coefficient of rho R) = 1/3 - (-2/3) = 1`.

### 2. R-b1 Step 1

Scripts `q10_check.py` (explicit SO(10) gammas, random antisymmetric `F`): `Q_10` orders 0, 1, 2, 3 vanish identically (to `1e-15`), order 4 is `-3/8` times `V_4` for generic `F`, for 10D and 4D-supported `F`. Closed form for flux in the four Poisson directions (eigenvalues `+-i x`, `+-i y`; vector `2cos x + 2cos y`, Dirac `4 cos(x/2)cos(y/2)`, six inert scalars, ghosts `-2`, `n_D` Dirac): order 0 `= 8 - 4 n_D`, order 2 `= (n_D-2)(x^2+y^2)/2`, order 4 `= -(n_D(x^4+6x^2y^2+y^4) - 8(x^4+y^4))/96`; at `n_D = 2`: `(x^2-y^2)^2/16`. Match with 017: `N_tot = N_s + 2 - 4 n_D = 8 - 4 n_D` at `N_s = 6`; `b = 1 - n_D/2`; `T(Dirac)/T(vector) = 1/2` (also verified by `w4_check.py`, ratio `0.500000`). `c_T = N_tot/6 - 4b` (from 017's table: eigenvalue `= (N_tot/6)(-1/4) + b` on the TT modes). This identifies the two zeros as the standard supertrace cancellations (dimension count, Dynkin-index count) and shows `n_D = 2` is the unique zero of `alpha^2` for the `D = 10` count; it does not derive the content.

*T-side first survivor (structural, conditional).* Heat-kernel `a_2` for operators of Laplace type: bulk terms are `tr 1` (times `R^2, Ric^2, Riem^2`), `tr E`, `tr E^2`, `tr Omega^2`. If `E` and `Omega` are built from `beta_sigma`, `d beta`, `d ln rho` and the Levi-Civita rotation generator (as for the operators of 017; `E` of the connection sector at `alpha = 1` not re-derived), then `tr Omega^2` and every term quadratic in algebra elements is proportional to the weighted index (`w4_check.py`: weighted `tr[B_s,B_t]^2 = 0` at `n_D = 2`; weighted cubic `= 0`), and only `Sigma w tr(beta.beta)^2` survives: `W_4 = tr_V (B.B)^2 - n_D tr_D (B.B)^2 = (1/2)|l|^2|r|^2 + |K|^2 >= 0` (fit to `1e-12`; SU(2)xSU(2) decomposition `l, r` of the `N^sigma`, `K_ab = sum_sigma l_sigma^a r_sigma^b`; min over 2000 random draws `> 0`), zero iff every `N^sigma` is self-dual or anti-self-dual. So there is no `Lambda^2` or `Lambda^0 log Lambda R^2` term at `D=10` content; the first survivor is a sign-definite quartic in the torsion `N^sigma_{ab} = Theta^{rho sigma} d_rho Theta_{ab}`. Not in the LaTeX.

*A-side first survivor:* not computable from what is here. The conical constants depend on spin through twist-dependent functions (as `a^2` vs `-|a| + a^2` above), not only on `tr 1`, `tr E`, so there is no reduction to the weighted invariants; also the log coefficient needs a non-flat leaf (SME scout; on constant `Theta_bar` the leaf is flat). Stated as open.

### 3. R-a3

`holonomy_check.py`: for `mu = m(n-1)`, Dirac block `(1 - n d_n)[sum (a_k+mu)^2] = -1/6` independent of `m`; scalar-like complex component `1/3 +- m` on `n >/< 1` (kink). So the fermion first derivative is untouched; the scalar part depends on a tip domain that 017/015 do not fix. Not a general proof of Nishioka-Yaakov's statement in this setting.

### 4. No-go as a fork

Hypotheses of the (017 + this package) no-go: H1 Poisson limit; H2 Euclid section; H3 one loop; H4 `Lambda^2` order; H5 tensor block = `delta rho = 0` modes; H6 tip domain (fermion: now fixed by the first-order operator; vector/ghost/scalar: componentwise-regular, unexamined); H7 state quasi-free with rotational modular flow (Problem A); H8 constant `Theta_bar`; H9 content = `n_D = 2`, `N_s = 6`, Yukawas dropped; H10 conical (not edge-mode/contact-augmented) area coefficient.

What each relaxation gave: gluing (H7): fixed, mismatch stands; graded vs ungraded: eliminated (neither); continuation: eliminated rotated branches; R-holonomy: fermions inert, scalars domain-dependent; next order (H4): T-side survivor identified (`W_4`, sign-definite, BPS locus), A-side open.

Ranked open avenues:
1. **A-side next order on a curved leaf** with twisted fermion and unrotated vector cones, compared to `W_4`; note the T-side survivor vanishes exactly on (anti-)self-dual flux, which is the BPS / `f_1 = f_2` locus of 018 and R-f1 (queued separately).
2. **Contact/edge terms of total weight `n_D = 2` (units where a scalar is `1/6`)**: the remaining gap is entirely the spin term (+1 per Dirac); Kabat's vector contact term is `-1` (017 row 3b), so it cannot alone supply 2; vector tip domain, ghost/fermion edge modes (Donnelly-Wall, CHR) are the candidates.
3. **Tip domain of the vector, ghosts, scalars** (determines the `alpha`-dependence and the R-holonomy kink, hence R-a3).
4. **State/flow (Problem A):** a non-rotational modular flow, or a state not quasi-free, would change H7; also the Moyal corrections.
5. **Non-flat `J = 0` backgrounds** (017 avenue 4) to test the lemma and tip conditions.
6. Lichnerowicz-type term: the spin term `+1 per Dirac` equals what a Levi-Civita `-R/4` endomorphism would add to the `rho R` coefficient; whether the matrix Dirac operator (frame torsion) supplies it at another order is open.

## Claim classification

| Claim | Class |
|---|---|
| Polar-antiperiodic <-> Cartesian `-e^{2 pi i n sigma}`, `(-1)^{n+1}` at integer `n` | established (algebra; CH, FM verified) |
| `Tr rho^n` gluing for the matrix fermions | conditional (quasi-free, rotational modular flow; Problem A) |
| `C_D(a) = a^2 + 1/6`, `c_A(Dirac) = 1/3` via k-sum | conditional (less-singular extension; my derivation, agrees with CH 2D and 017) |
| Periodic branch = mixed `Tr rho^n`/graded, regular domain, not a Dirac trace | established (twist sets, script) / conditional on domain argument |
| Graded `Tr[(-1)^F rho^n]` not normalised at `n=1` | established (twist `a = 1/2`) |
| Rotated vector branches not continuations of `Tr rho^n` | conditional (Carlson-type uniqueness) |
| `gap = 4 - n_D`, `(c_T, c_A) = (0, 2)` at D=10 content | conditional |
| `N_tot`, `b` = orders `alpha^0, alpha^2` of `Q_10`; first survivor `alpha^4` `(x^2-y^2)^2/16` | established (script; paper eqs. verified) for the character; identification with 017's counts: algebra |
| T-side `a_2` survivor `W_4` | conjecture/structural (E, Omega form assumed) |
| A-side next order | unresolved |
| R-holonomy statement | conditional, half-confirmed |
| `n_D = 2`, `N_s = 6` content | input (identification) |
| `ass:EE`, stationarity, `G_eff` value/sign | unresolved |

## Proposed changes

File `chapters/appH-microscopic-proofs.tex`, `sec:status-B`, after the integrated 017 block. Nothing else is touched; no label added; one new bibliography key pair (below) for the integrator.

(1) Replace exactly the sentence (occurs once, line ~189): `The gluing selected by the matrix state is not determined here.` by `The gluing selected by a quasi-free state with rotational modular flow is stated below.`

(2) Insert the following paragraph after the sentence ending the 017 third paragraph, `... or the Kaluza--Klein sector. Problems~B, C, D, F and~G remain open.` (occurs once, line 191) and before `\section{Problem C: conformal mode and Cassini}` (once, line 193). Cites used: `CasiniHuerta2009`, `FursaevMiele1997` (new), `MantaSteinackerTran2024` (exists, `@misc`). Compiled in a scratch copy outside the repository (amsmath, amssymb, `\LUV`, stub `\cite`): no error, no undefined or overfull message. File: `proposals/019-fermion-replica-gluing/appH_insert.tex`. No `\ref` is added.

```latex
\paragraph{Fermion replica gluing for \(\operatorname{Tr}\rho^n\) and the supertrace character (conditional; not closure).}
Let the state of the Poisson-limit fermions on the wedge be quasi-free, and let its modular flow be the rotation by \(2\pi t\) of the transverse plane of \(\Sigma\), acting on every field through its representation of the rotation group (for integer spin, the identity at integer \(n\)). The ungraded trace \(\operatorname{Tr}\rho^n\) then glues a Grassmann-odd field with the rotation by \(2\pi n\) and one sign from the cyclicity of the trace: in the polar frame the spinor is antiperiodic under the angle \(2\pi n\), and the Cartesian components of transverse spin \(\sigma=\pm\tfrac12\) acquire the monodromy \(-e^{2\pi\mathrm in\sigma}\), which is \((-1)^{n+1}\) for integer \(n\)~\cite{CasiniHuerta2009,FursaevMiele1997}. Diagonalising the replica matrix gives the twist phases \(e^{2\pi\mathrm ik/n}\), \(k=-(n-1)/2,\dots,(n-1)/2\)~\cite{CasiniHuerta2009}. For a block of two components with twist \(a\), \(|a|<\tfrac12\), and the less singular self-adjoint extension of the first-order operator \(\gamma^\mu D_\mu\), whose square is \(\mathcal O_f\), the conical heat-trace constant is \(a^2+\tfrac16\): the componentwise-regular value \(B_2(|a|)\), \(B_2(x)=x^2-x+\tfrac16\), plus \(|a|\) from the reversed sign of the one Bessel order that the first-order operator fixes. This extension is the one giving an analytic continuation: the componentwise-regular domain gives \(\sum_k|a_k|\) equal to \(n/4\) or \((n^2-1)/(4n)\) for even or odd \(n\), a parity-dependent and non-analytic \(\operatorname{Tr}\rho^n\). With the less singular extension, \(\sum_ka_k^2=(n^2-1)/(12n)\), analytic in \(n\), equal to the zeta-function value of the polar-frame cone on the branch \(n<1\), with \((1-n\partial_n)\) equal to \(-\tfrac16\) per block at \(n=1\). The area coefficient of a Dirac field (two blocks, weight \(-1\)) is therefore \(+\tfrac13\), as used above for antiperiodic gluing.

The unrotated periodic gluing above has the phase \(+1\) for all \(n\): its twists are those of \(\operatorname{Tr}\rho^n\) for odd \(n\) and those of the graded trace \(\operatorname{Tr}[(-1)^F\rho^n]\) for even \(n\), and with the componentwise-regular domain it gives \(-2\) times the Dirac-domain value at odd \(n\). It is not \(\operatorname{Tr}\rho^n\), and for the stated extension its values \(-\tfrac23\) and \(4-2n_D\) do not apply to \(\operatorname{Tr}\rho^n\). The graded trace has the twist \(a=\tfrac12\) at \(n=1\) and is not normalised there. The rotation by \(2\pi n\) is the identity on the vector index for integer \(n\), so the integer-\(n\) traces of the connection sector are those of the unrotated gluing; if the continuation from integer \(n\) is unique, the rotated branches \(3-n_D\) and \(5-n_D\) above do not reproduce them and are not continuations of \(\operatorname{Tr}\rho^n\). With \(c_A=\tfrac{N_s+\alpha+1}6+\tfrac{n_D}3\) and \(c_T\) as above, \(c_A-c_T=4(1-\tfrac{n_D}2)+n_D\), the sum of the weight of \(\rho^2X\) and the excess \(+1\) per Dirac field of the cone value \(+\tfrac13\) over its coefficient \(-\tfrac23\) of \(\rho R[g_\rho]\). For \(n_D=2\), \(N_s=6\), \(\alpha=1\): \(c_T=0\), \(c_A=2\).

In the character \(\mathsf Q_{10}\) of~\cite{MantaSteinackerTran2024}, Eq.~(3.7), with the flux along the four Poisson directions, the vector, six inert scalars, the ghosts and \(n_D\) Dirac fields in place of the sixteen-component spinor, the coefficient of order \(\alpha^0\) is \(N_{\mathrm{tot}}=8-4n_D\) and that of order \(\alpha^2\) is \(-b\,(x^2+y^2)\) with \(b=1-n_D/2\), where \(\pm\mathrm ix,\pm\mathrm iy\) are the eigenvalues of the flux. These are the weighted component count and the weighted index of the preceding paragraphs, so that \(c_T=N_{\mathrm{tot}}/6-4b\) vanishes at \(n_D=2\), \(N_s=6\) because the orders \(\alpha^0\) and \(\alpha^2\) of the character vanish. At \(n_D=2\) the order \(\alpha^4\) is \((x^2-y^2)^2/16\), which vanishes for self-dual or anti-self-dual flux. This concerns the character only, not the \(a_2\) coefficient of the operators and not the area side. These statements are conditional on the quasi-free state, the rotational modular flow, the choice of self-adjoint extension, the uniqueness of the continuation from integer \(n\), the domain of the first-order operator, the \(\LUV^2\) order and the class of the preceding paragraphs; they do not derive the state, the flow, the content, or a value or sign of \(G_{\mathrm{eff}}\), and they do not compute the next order of either side. Problems~B, C, D, F and~G remain open.
```

Stale passages: the 017 sentences giving the periodic result and the rotated branches stay (they are reported as alternatives); the new paragraph states they are not `Tr rho^n`. ch17 and the ledger: unchanged.

Verified BibTeX (for the integrator; records opened and checked: CH via PDF and Crossref, FM via PDF and Crossref):

```bibtex
@article{CasiniHuerta2009,
  author  = {Casini, Horacio and Huerta, Marina},
  title   = {Entanglement entropy in free quantum field theory},
  journal = {J. Phys. A},
  volume  = {42},
  number  = {50},
  year    = {2009},
  doi     = {10.1088/1751-8113/42/50/504007},
  eprint  = {0905.2562},
  archivePrefix = {arXiv}
}
@article{FursaevMiele1997,
  author  = {Fursaev, Dmitri V. and Miele, Gennaro},
  title   = {Cones, spins and heat kernels},
  journal = {Nucl. Phys. B},
  volume  = {484},
  pages   = {697--723},
  year    = {1997},
  doi     = {10.1016/S0550-3213(96)00631-1},
  eprint  = {hep-th/9605153},
  archivePrefix = {arXiv}
}
```

## Verification scripts

All in `proposals/019-fermion-replica-gluing/`; run with `python -I`; outputs saved as `*.out.txt`.
- `twist_ksum.py`: frames to Cartesian phase; twist sets (anti/periodic/graded) and sums of `a^2` for `n = 1..7`; asserts `sum a^2 = (n^2-1)/(12 n)`, odd-`n` coincidence anti/periodic, even-`n` coincidence periodic/graded; `C_D(a)`; polar zeta `n < 1` vs k-sum; `n > 1` regular branch + flipped mode = analytic form; `(1 - n d_n)` derivative; ratio `-2` at odd `n`; rotated vs unrotated vector at integers.
- `q10_check.py`: SO(10) gamma matrices; `Q_10` orders 0-4; ratio `-3/8` to `V_4`; 4D closed form and general `n_D`.
- `w4_check.py`: index ratios, weighted index-type invariants vanish, `W_4 >= 0`, fit `(1/2)|l|^2|r|^2 + |K|^2`, zero on SD/ASD.
- `holonomy_check.py`: R-holonomy; `gap_fixed.py`: gap table; `verify_anchors.sh`: anchor and key counts.
- Scratch compile of `appH_insert.tex` outside the repository (no error). These are checks, not proofs; the tip-domain step (1c) is a mode-by-mode argument supported by cross-checks, not a rigorous operator-theoretic proof.

## Decisions Taken

1. Used the polar-frame k-sum as the only continuation (Carlson-type); reported the non-analytic branches only as excluded by integer-`n` data. Reason: the entropy is the `n -> 1` limit of the integer-`n` trace.
2. Domain: first-order operator (Dirac) domain for fermions because the action is first order; the vector/scalar domains left as in 017.
3. Kept the 017 text; added a paragraph and replaced one sentence rather than rewriting the periodic/rotated passages.
4. Put the `W_4` T-side structural claim in the proposal but not in the LaTeX (conjecture/structural; E and Omega form not re-derived).
5. R-a3 limited to the fermion/scalar holonomy derivative; not extended to a SUSY multiplet.

## Milestone assessment

M2 (bounded no-go, narrowly), no breakthrough. The package removes two escape routes of 017 (the periodic `0 = 0` and the rotated branches), fixes the fermion gluing under stated hypotheses, and identifies the cancellations as `alpha^0`, `alpha^2` of the SO(1,9) character. It derives no critical-path step from the matrix theory.

## Status-label recommendation

None. B: OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; A unchanged; critical-path set A, B, C, D1, E, F, G-derived, N unchanged. No label in the LaTeX.

## Author decision needed

None. Spacetime stays emergent: wedge, rotation and cone are built from the emergent `G(Theta)`; no background `eta`; the Q_10 comparison uses the matrix-model SO(1,9) representations, not a fundamental metric.

## Remaining open step

Not derived: the quasi-free state and rotational modular flow (Problem A), the vector/scalar tip domains, `ass:EE`, stationarity, the map `Theta -> G`, a value/sign of `G_eff`, uniqueness of the continuation from integer `n`. To close the `G_T = G_A` gap at the D=10 content one needs a mechanism for the `n_D = 2` spin term at order `Lambda^2`, or a matching of both sides at the first surviving next order. Ranked open avenues (the gatekeeper's list, review-r1):

1. **Contact/edge terms of total weight `n_D = 2` at order `Lambda^2`** (units scalar `= 1/6`). The whole remaining gap is the spin term, `+1` per Dirac (Lichnerowicz-type `-R/4` endomorphism or fermion/ghost edge modes). Relaxes H10 (conical-only area coefficient). Kabat's vector contact term is `-1` (017 row 3b) and cannot alone supply 2.
2. **A-side next order on a curved `J = 0` leaf**, compared with the T-side structural survivor (`W_4`, conjectural: E and Omega not re-derived; kept out of the LaTeX). Relaxes H4, H8.
3. **Vector, ghost and scalar tip domains** (fix the `alpha`-dependence and the R-holonomy kink). Relaxes H6.
4. **Non-rotational modular flow or non-quasi-free state, Moyal corrections** (Problem A). Relaxes H7.
5. **Non-flat `J = 0` backgrounds** to test the lemma and the tip conditions.

## Special instructions for the gatekeeper

- Do not read this as closing B or A: the `Lambda^2` mismatch is sharpened, not resolved, and the results are conditional on H7 (state, modular flow) and the first-order-operator domain.
- Re-check: (a) the mode-by-mode derivation `C_D(a) = a^2 + 1/6` (section 1c) and the cross-check `n > 1` regular + flipped mode = `n < 1` (script section 4); (b) CH eq. (16)/footnote 2 and FM (4.4), (4.6), (4.11) text; (c) MST eqs. (3.7), (3.9), (3.10); (d) that the LaTeX asserts only character-level statements for `Q_10` and no `a_2` claim.
- The `W_4` structural paragraph is not in the manuscript block and must stay out unless E, Omega are re-derived.
- Not independently verified: Steinacker 2303.08012 `V_4` form (only matched numerically); Carlson-type uniqueness is assumed, not proven.
