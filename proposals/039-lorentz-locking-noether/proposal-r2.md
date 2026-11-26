# Proposal 039-lorentz-locking-noether, round 2

Round 2 is a wording-only revision answering `review-r1.md` (ACCEPT WITH REQUIRED REVISIONS, six findings). No new
mathematics, no new scripts, no change to any computed number. Everything in `proposal-r1.md` stands except as
corrected below. The r1 block is saved as `appH_insert_r1.tex`; `appH_insert.tex` is the r2 block.

## Result (corrected summary)

Unchanged in substance: local frame rotations leave a first-order frame density invariant only on
span{calT, |d ln rho|^2}; with the Chapter 10 dressing taken as an input and Lambda at its own stationary point, the
density rho^2 X becomes 2 calT + 2 V^2 at the plane-wave stationary points and on the cone family; the joint flow then
selects r = -2, not -4; the residue c_A - c_T^ext is 2 for antiperiodic Dirac gluing at every N_s and n_D.

**Correction of the r1 summary (F1).** The r1 summary said the dressing "halves the 038 gap". That is false in general.
The reduction is by 2 kappa_X = 2 - n_D: it is half of the value 4 - n_D only at n_D = 0 (4 -> 2) and is nil at n_D = 2
(2 -> 2, kappa_X = 0). Where r1 text said "halves", read "lowers by 2 kappa_X". Likewise 1/G_A - 1/G_T^ext = Lambda_{UV,v}^2/pi
at n_D = 0 only. Status: B, A, D remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; no label change.

## Findings and how each was applied

All six substitutions are the verbatim strings of the review's "Corrected snippet"; each old string occurred exactly
once (confirmed by script `apply_r2.py` before replacing; assertion on count == 1). No other edit to the block.

| Finding | Action |
|---------|--------|
| F1 (major) "half of the value 4-n_D" | replaced by "smaller by 2 kappa_X than the value 4-n_D before the dressing, that is half of it at n_D=0 and unchanged at n_D=2"; summary above corrected |
| F2 (major) "whole non-invariance" | qualified: with V.V replaced by its class value |d ln rho|^2; the difference 2(V.V - |d ln rho|^2) vanishes on the class but is not invariant. Agreed: s1/s4 measure A[X], and A[X] != A[S^2] on generic class jets (10.2 vs 6.0). The classification (invariant span, extension ambiguity) is unaffected |
| F3 (major) "On the stationary set the density depends on e only through G and rho" | restricted to "At the stationary points above, where S=0 and V=d ln rho" |
| F4 (major) status of the dressing | block now states: Lambda acts on the coframe, density rho^2 X[Lambda e], an input of Assumption local-lorentz (\ref{ass:local-lorentz}), not derived; Lambda treated as a field fixed by stationarity at the Theta-built frame; in unitary gauge Lambda = 1 the density is the undressed one and r stays undetermined (consistent with the merged compensating-field paragraph and with H2 of r1) |
| F5 (minor) V notation | setting sentence now defines V_mu = G^{lambda nu} T_{lambda mu nu}, equal to d_mu ln rho on the Poisson class |
| F6 (minor) "six rotation amplitudes" | "twelve real rotation amplitudes" |

The review's remark that the two r = -2 routes (eigenvalue 1/2 and calT ~ -R) share the input <R> = -calT on the modes is
accepted: they are a consistency check, not independent derivations. The block does not claim otherwise.

## Mechanics of the r2 block

- `appH_insert.tex` (r2): **6406 bytes**; 0 TAB; 0 CR; 0 non-ASCII or control characters other than LF; braces balanced
  (net 0); `\(` and `\)` balanced (101 each).
- References: `eq:dressed-omega` (ch10, unique) and `ass:local-lorentz` (ch10 L56). `\label{ass:local-lorentz}` occurs exactly
  once in chapters/*.tex (the only other grep hit is a stale `.aux` file, not a source label).
- Anchor `\section{Problem C: conformal mode and Cassini}` unique (grep count 1); the block sits after the 038 block.
- Scratch compile outside the repository (block inserted in CRLF before the anchor): two pdflatex passes rc = 0, 0, undefined
  references 0, multiply defined labels 0 (80 pre-existing citation warnings because bibtex is not run in scratch);
  `compile_check_r2.out.txt`. Scratch copy deleted. Nothing in chapters/ or bib/ was touched.
- `apply_r2.py` in this folder performs and logs the substitutions and the byte/brace checks (its first line saves r1).

## Remaining items

Unchanged from r1: Decisions Taken, Milestone assessment (routine, no breakthrough claimed), Status-label recommendation
(none), Author decision needed (none), Remaining open step, and the ranked avenues (H1 covariant bundle connection; H5
contact of modulus 2; H2 loop-level or gauge-versus-field status of Lambda; H3 nonlinear stationary set; H4 fermion
X-term; H6 Lorentzian Goldstone signs).
