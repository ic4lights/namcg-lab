# Proposal 071-d1-curved-torsion-backgrounds, round 3

## Result

Round 3 is a minimal revision that addresses the four findings of `review-r2.md` (AWRR, minor/informational only). No mathematics changed. All r2 results, scripts and outputs stand as recorded in `proposal-r2.md`, which is kept with every r2 file.

- **Finding 1 (minor):** "For a != 0 ... R^2 != 0" is false at kappa = 0. Snippet H was applied verbatim, with the condition `\(\chi\kappa\neq0\)`.
- **Finding 2 (minor):** the parameter `a` clashed with the frame index `a`. It is renamed `\chi` in the insert, through snippet H (whole sentence) and snippet SC2, both verbatim.
- **Finding 3 (informational, proposal only):** the "first exact solution with `R^2 != 0`" wording now carries the qualifier "among left-invariant, constant-connection backgrounds with T != 0". The true statement is narrower, because appH L1527 already has Schwarzschild, Kasner and dS at `T = 0`.
- **Finding 4 (informational):** "a gap is not excluded by symmetry" is now labelled as an avenue rationale, not a result. This is in the proposal only; the insert makes no gap claim.

Everything else is unchanged from r2.
- **Established:** families (i) and (ii); the wider Heisenberg family `w = k(chi B + zeta N + x N')`, which solves all three brackets; the invariants; the sign map; the 068 correction (edit E).
- **Bounded no-go:** no mass shell on family (i), and only there.
- **Not closed:** D, F and N remain OPEN and PROGRAMME-CONDITIONAL.

## Target and status

Unchanged from r2. Problem D (D1 route) is OPEN, CRITICAL PATH and PROGRAMME-CONDITIONAL, and the item attacked is "torsion or propagating modes". D1 supplies operators to F, and F gates N. At full-GR scope the critical-path OPEN set is A, B, C, D, E, F, G and N; H, I and J are optional. No discrepancy was found.

## Source reading

- **Mode:** digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST CURRENT`, and `scratch/digest.md` was read first.
- **Live appH sha256:** `d8d8b678fa0ceabe03f3f9c2f56cc60dbe140aa845658beddb0c206ba26c9180`, re-verified with `sha256sum` and by the apply script.
- **Problem D section:** lines L715 (`\section{Problem D: local Lorentz}`) to L1631 (`\section{Problem E: signature}`). This range was searched for `\chi`.
- **No full scan by this package.** The gatekeeper's full scan is still owed, per review-r2's disposition.

## Research and reasoning

### Check of the rename (task item 2)

- **The parameter `a` is gone from `appH_insert_r3.tex`.** `make_insert_r3.py` asserts that none of the old parameter patterns occur: `(aB^`, `kappa,a,`, `=a\,k_a`, `12a\kappa`, `4a^2`, `(a\neq0` and `(a)`. A regex pass over every standalone `a` token in the r3 insert leaves only three kinds of `a`: frame indices (`n^a`, `k^a`, `k_ay^a`, `\nabla^a`, `\mathsf F^a{}_c`), the English article "a", and the label `ass:EFT-a2`.
- **`\chi` is used 8 times in the insert**: 7 in sentence H and 1 in SC2.
- **`\chi` does not occur in the Problem D section.** `sed -n '715,1631p' chapters/appH-microscopic-proofs.tex | grep -F -c '\chi'` gives `0`. In appH, `\chi` appears only at L402 (Problem A) and L2689-2735 (Problem F, a test function `\chi(\lambda)`). Neither is in Section D, so there is no clash.

### Scripts (task item 6)

I re-ran `x2_heisenberg_kB.py` and `x3_op_heisenberg.py` with `python -I`. Both exit with rc 0, and each output is byte-identical to the stored `x2_heisenberg_kB_output.txt` and `x3_op_heisenberg_output.txt` (`diff -q`).

**Decision: the scripts keep the symbol `a`.** The rename is not cheap in `x3_op_heisenberg.py`, where `a` is also the frame-index loop variable in the operator code (lines 28-80). The mapping is `a` (scripts) = `chi` (insert); only the symbol name differs. For example, x2 prints `R_abcd R^abcd = -4*a**2*kappa**2`, which is `-4\chi^2\kappa^2` in the insert.

### Finding 3 wording

r2 said "first exact solution in the class with `R_abcd R^abcd != 0`". The corrected wording reads: "the first exact solution with `R_abcd R^abcd != 0` **among left-invariant, constant-connection backgrounds with T != 0** in the first-order equivariant class". Integrated appH L1527 records exact Schwarzschild, Kasner and dS solutions at `T = F = 0`, all with `R^2 != 0`, so the unqualified claim was false. The manuscript insert never made the unqualified claim. Sentence H says only "an exact solution with ... on a unimodular algebra".

## Claim classification

This table is unchanged from r2, except that the parameter is renamed:

| claim | class |
|---|---|
| (i) and (ii) solve all three brackets | established (exact; operator check) |
| the wider (ii), `w = k(chi B + zeta N + x N')`, solves all three brackets for all real `kappa, chi, zeta, x`; `R^2 = -4 chi^2 kappa^2`, which is nonzero iff `chi kappa != 0` | established (exact symbolic section values; operator check at 4 points) |
| first exact `R^2 != 0` solution among left-invariant, constant-connection, `T != 0` backgrounds | established (within that qualifier only) |
| no symmetry excludes a gap on the wider (ii) | avenue rationale (not a result) |
| `R_ab^{ab} = 0` on all families | established |
| sign map `w = -e·ω` | established |
| alpha sets; converse clean at both points | numerical |
| no isolated mass shell on (i) | bounded no-go (flat-frame null family (i), tree level, linear order) |
| L1623 value `ϑ = +½` | established (numerical roots, exact ranks) |
| survey solutions with `c` free | numerical; not classified |

## Proposed changes

**File `chapters/appH-microscopic-proofs.tex` only.** The anchors and edits are the same as in r2. The pre-hash is `d8d8b678fa0ceabe03f3f9c2f56cc60dbe140aa845658beddb0c206ba26c9180` (live, verified).

1. **Insert** `appH_insert_r3.tex` (CRLF, 9312 bytes, sha256 `c0ff0f791bfe4b19e4c37d29d70bfffc24f6311c0e78ef31818f17a3dc9a19dc`, no bare LF, no BOM), followed by one blank CRLF line, immediately before the unique line `\section{Problem E: signature}` (L1631). This places it after the 068 paragraph ending "Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL."
2. **Edit E, appH L1623 (unchanged from r2).** The unique string `has the same torsion for \(\vartheta=-\tfrac12\), with` becomes `has the same torsion for \(\vartheta=\tfrac12\), with`.

**Post-hash:** `36cb6f30fc7544ef15a6418b5d2bd5b2d8b8160b516c8be12eb4eecffe8a9dfe` (753105 bytes, no bare LF). This replaces the r2 post-hash `c1a880e5...`.

The `\ref`s are unchanged and each is defined once: `eq:Smatrix`, `ass:frame-lock`, `ass:nondeg`, `ass:lorentzian`, `ass:local-lorentz`, `ass:EFT-a2` and `ch:vierbein-emergence`. There are no new labels, no citations and no bib change. The insert has one status sentence, in its last paragraph.

### Exact diffs from r2

`make_insert_r3.py` applies these to `appH_insert_r2.tex`, and asserts that each old string occurs exactly once.

- **H**: the whole r2 sentence is replaced by snippet H of review-r2, verbatim. The script checks that the review's snippet line occurs once in the r3 insert.

  Old (r2):
  ```latex
  On the algebra of (ii) the wider ansatz \(w_a{}^{cd}=k_a(aB^{cd}+\zeta N^{cd}+xN'^{cd})\) solves all three brackets for all real \(\kappa,a,\zeta,x\): \(\mathsf T_{ac}{}^c=a\,k_a\), the only nonzero pair of \(\mathsf F\) is \(\mathsf F_{13}=\tfrac12a\kappa\), the only nonzero pair of \(\mathsf R\) is \(\mathsf R_{13}{}^{cd}=\kappa(aB^{cd}+\zeta N^{cd}+xN'^{cd})\), and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4a^2\kappa^2\), \(\mathsf R_{ab}{}^{ab}=0\), \(\mathsf T_{abc}\mathsf T^{abc}=2\kappa^2\) (exact for the section values; for the operators on the bundle at random Lorentz \(u\), including the order-zero part, residual below \(10^{-15}\)). For \(a\neq0\) it is an exact solution with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\) on a unimodular algebra.
  ```
  New (r3):
  ```latex
  On the algebra of (ii) the wider ansatz \(w_a{}^{cd}=k_a(\chi B^{cd}+\zeta N^{cd}+xN'^{cd})\) solves all three brackets for all real \(\kappa,\chi,\zeta,x\): \(\mathsf T_{ac}{}^c=\chi\,k_a\), the only nonzero pair of \(\mathsf F\) is \(\mathsf F_{13}=\tfrac12\chi\kappa\), the only nonzero pair of \(\mathsf R\) is \(\mathsf R_{13}{}^{cd}=\kappa(\chi B^{cd}+\zeta N^{cd}+xN'^{cd})\), and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4\chi^2\kappa^2\), \(\mathsf R_{ab}{}^{ab}=0\), \(\mathsf T_{abc}\mathsf T^{abc}=2\kappa^2\) (exact for the section values; for the operators on the bundle at random Lorentz \(u\), including the order-zero part, residual below \(10^{-15}\)). For \(\chi\kappa\neq0\) it is an exact solution with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\) on a unimodular algebra.
  ```
- **SC2**: `its extension with \(a\neq0\)` becomes `its extension with \(\chi\neq0\)`, verbatim per review-r2. The rest of the sentence is unchanged.

No other byte of the insert changes (character diff of `appH_insert_r2.tex` against `appH_insert_r3.tex`, `difflib`): 9280 to 9312 bytes, net +32. In H, two `aB` become `\chi B` (+4 each), four further `a` become `\chi` (+3 each), and `a\neq0` becomes `\chi\kappa\neq0` (+9), for +29. SC2 adds +3.

`appH_insert_r1.tex`, `appH_insert_r2.tex`, `make_insert_r2.py`, `apply_and_build_r2.py` and their outputs are kept.

### Changes to the proposal text from r2 (not in the manuscript)

- Result item 2 and the "Bearing on the target" paragraph are replaced as follows. The wider family `w = k(chi B + zeta N + x N')` is, for `chi kappa != 0`, the first exact solution with `R_abcd R^abcd != 0` among left-invariant, constant-connection backgrounds with T != 0 in the first-order equivariant class. Exact `R^2 != 0` solutions at `T = 0` (Schwarzschild, Kasner, dS; appH L1527) already exist. The absence of the 0-2 boost-dilation symmetry is an avenue rationale for linearising this family; no gap or mass result is claimed.
- Avenue 1 now uses `chi`: "Linearise the wider Heisenberg family at `chi kappa != 0`". The 068 Landau-level and growth-bound questions are unchanged.

## Verification scripts

| command (from this folder) | checks | expected invariant output |
|---|---|---|
| `python -I make_insert_r3.py` | builds the r3 insert from r2 | `replacement H applied once`; `replacement SC2 applied once`; `old parameter-a patterns remaining: 0`; `\chi occurrences in insert: 8`; `appH_insert_r3.tex bytes 9312 sha256 c0ff0f79...a19dc bare LF 0` (`make_insert_r3_output.txt`) |
| `python -I apply_and_build_r3.py --build` | applies the change on a temp copy outside the repo, then builds it | `pre-hash matches expected: True`; anchor line 1631; `E anchor unique: True; line 1623`; block sha `c0ff0f79...`; `appH post sha256 36cb6f30...a9dfe bytes 753105 bare LF 0`; 7 labels defined once; pdflatex 399 → bibtex → 414 → 414 pages; `undefined/multiply-defined warnings: 0`; `BUILD CLEAN`; `temp copy removed: True` (`apply_and_build_r3_output.txt`) |
| `python -I x2_heisenberg_kB.py` | the wider (ii), exact (symbol `a` = `chi`) | output byte-identical to the stored `x2_heisenberg_kB_output.txt`, e.g. `so the first two brackets hold for all kappa, a, zeta, x`; `R_abcd R^abcd = -4*a**2*kappa**2 ; scalar R_ab^ab = 0` |
| `python -I x3_op_heisenberg.py` | the wider (ii) at operator level | output byte-identical to the stored `x3_op_heisenberg_output.txt` |
| `sed -n '715,1631p' ../../chapters/appH-microscopic-proofs.tex \| grep -F -c '\chi'` | no `\chi` clash in Section D | `0` |

The other r2 scripts are unaffected and were not re-run, because r3 changes no computation: `gk071_op.py`, `s1`, `s2_linearised_r2.py`, `s3`, `v4s_068_signmap.py` and the gk071 scripts.

## Decisions Taken

- **Rename in the text only.** The parameter is `\chi` in the insert and the proposal prose. The scripts keep `a`, because `x3_op_heisenberg.py` uses `a` as a frame-index loop variable, so a rename there is not cheap or risk-free. The x2 and x3 outputs were confirmed byte-identical on re-run.
- **Finding 3** is handled in the proposal only, as instructed. The insert never made the unqualified claim.

## Milestone assessment

Routine. Not a breakthrough. The package gives an exact existence result inside an assumed class and derives no critical-path step from the matrix theory.

## Status-label recommendation

None. D, F and N remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

This is unchanged from r2. Closing D1 still requires deriving the class, `A`, the backgrounds, the frame and its non-degeneracy from the matrix integral, and operators with a norm and a regulated trace.

Avenues, ranked derivation-first:
1. Linearise the wider Heisenberg family at `chi kappa != 0` in the oscillator sectors. Does it shift the Landau levels, and does it change the growth bound?
2. The c-free survey: first `t` and the third bracket, then harmonic analysis.
3. A norm for the cone shifts on (i).
4. Nonlinear evolution and one loop (feeds F).
5. Non-constant connections.
6. (Bottom) Further boost-dilation-symmetric null families.

## Special instructions for the gatekeeper

- **Snippet H.** Confirm that it occurs verbatim; `make_insert_r3.py` asserts the H and SC2 replacements.
- **Hashes.** Pre `d8d8b678…9180`, post `36cb6f30…a9dfe`.
- **Rename check.** Confirm `\chi` is absent from appH L715-1631.
- **Script symbol.** The scripts keep the symbol `a` (= `chi`). The x2 and x3 outputs are unchanged.
- **No claims.** The insert claims no gap or mass on the wider family.
- **Scope of changes.** No files outside this folder were changed. The build ran in a temp directory outside the repository, which was removed afterwards.
