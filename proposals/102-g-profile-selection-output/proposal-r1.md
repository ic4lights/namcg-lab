PROPOSAL 102 r1 | G (entropy/stationarity) - G.moments-derivedprofile edge | flat-Dirichlet exact statistics of rho_p | write-up r1

## TARGET

Upgrade the integrated D=3 flat-Dirichlet numerical confirmation in the G-block of
`chapters/appH-microscopic-proofs.tex` (eigenvalue-reduction paragraph, line 3195 at PRE bytes
798457, sha256-prefix cfb6af516017367f) - the integrated sentence

> "its normalised squared entries are exactly flat on the simplex at \(D=2\), with the flat
> Dirichlet moments confirmed numerically at \(D=3\)"

to exact closed-form statistics of the moment-map obstruction factor rho_p on the profile simplex
at general D. G-block context: rho_p = p! h_p(p) is the moment-map obstruction factor
(rho_2 - 1 = 1/D_eff, exact partition form; third-paragraph-above region of the G-block, the
"Charge-to-edge moment identification" and "Uniform minimiser" paragraphs), the uniform profile
attains the floor prod_{k=1}^{p-1}(1+k/D), and the flat Dirichlet(1,...,1) member is the member of
the named fixed-trace Dirichlet-beta family at a = 1, beta = 0 identified in the fixed-trace beta
deformation paragraph as "the flat Haar frame weight, and the slot pushforward at uniform profile"
(grep-verified, count 1) and as the Haar-frame pushforward ("the Haar measure pushes forward ...
to the flat exchangeable weight on the simplex", count 1).

What this package is NOT (no-closure scope, rule 3; governing integrated sentences, each
grep-verified count 1 in the live appH bytes):
- it does not touch the Problem G missing steps (i)-(iv): the insert's own status sentence records
  they are "unchanged";
- it selects no profile and supplies no state. The variational-rigidity paragraph: "No functional
  on profile space is produced for this role by the core action ... the remaining demand is a
  weight on profile space produced by the core and non-degenerate along the kernel directions";
- it evaluates no matrix integral. The pushforward-weights paragraph: "the fibre-integration route
  yields no weight on profile space beyond the profile data already supplied; the matrix integral
  itself is not evaluated here, these statements supply no state and no selection mechanism";
- the fixed-trace beta deformation paragraph: "it supplies no state, its origin in the matrix
  integral is not established";
- it closes nothing in Problem G. The content is an exact-statistics supplement to the measure
  characterizations of the named flat member, upgrading the D=3 numerics of the eigenvalue-reduction
  paragraph to closed symbolic forms (findings.md, OPEN item 3).

## DERIVATION SUMMARY

Route (findings.md "Route statement", deliverable `s4_dirichlet_rho_direct.py` /
`s4_dirichlet_rho_direct.out`, 41 lines, live sha8 7b293544, exit 0, final line ALL CHECKS PASS):
rho_p evaluated via the exact partition (Newton) form with the unit-trace substitution x_1 = s_1 = 1
imposed before averaging; E[prod_k s_k^{m_k}] obtained by grouping the multi-indices of the
power-sum factors into equality patterns (set partitions of the factor list into b equal-index
blocks), each pattern contributing the falling factorial D!/(D-b)! of slot assignments times the
standard Dirichlet(1^D) monomial moment E prod_i p_i^{a_i} = (D-1)!(prod_i a_i!)/(D+A-1)!,
A = sum_i a_i (moment function reused verbatim from s3b's correct `dirichlet_monomial_moment`).

Closed forms (s4 .out sections A, D symbolic):
- E[rho_2] = (D+3)/(D+1)   [CHECK True: == 1 + 2/(D+1)]
- E[rho_3] = (D^2 + 9D + 26)/((D+1)(D+2))   [CHECK True: == 1 + 6/(D+1) + 12/((D+1)(D+2))]
- E[rho_4] = (D^3 + 18D^2 + 131D + 426)/((D+1)(D+2)(D+3))
- rho_1 = 1 exactly on the unit-trace simplex; rho_2 = 1 + s_2 and rho_3 = 1 + 3 s_2 + 2 s_3
  verified from the partition form.

Floor gaps, all strictly positive with factor (D-1) and positive numerator (s4 .out lines 9-11,
matching the insert text verbatim in factored form):
- E[rho_2] - floor(2,D) = (D-1)/(D(D+1))   [CHECK True]
- E[rho_3] - floor(3,D) = (D-1)(3D^2 + 16D + 4)/(D^2 (D+1)(D+2))
- E[rho_4] - floor(4,D) = (D-1)(6D^4 + 79D^3 + 361D^2 + 168D + 36)/(D^3 (D+1)(D+2)(D+3))

Sigma = s_2 = 1/D_eff moments (s4 .out section B): E[sigma] = 2/(D+1);
E[sigma^2] = 4(D+5)/((D+1)(D+2)(D+3));
Var[sigma] = 4(D-1)/((D+1)^2 (D+2)(D+3)) - numerator 4(D-1), numerator(D+2) = 4D+4 all-positive,
denominator > 0 for D >= 1, Var(1) = 0; hence Var[sigma] > 0 for every D >= 2 (the buggy s3b path
had printed a variance negative at small D, impossible; see EVIDENCE).
Rates: D E[sigma] -> 2; D^3 Var[sigma] -> 4 (Var[sigma] ~ 4/D^3); sigma -> 0 in L2 at rate
D^{-3/2}; E[rho_p] -> 1 at fixed p by the pointwise pin.

Pointwise pin (s4 .out section D): 1 <= rho_p <= 1 + (p!-1) s_2 on the simplex, with equality
rho_2 - 1 = s_2 at p = 2 (40 random rational profiles, p = 2..5); in mean the pin is sharp at
p = 2 (E[rho_2] equals the upper bound at D = 3, 6, 24) and strict at p = 3 and p = 4 there.

Monte Carlo corroboration (s4 .out section C, seed 102, 400000 normalized exponential rows;
corroboration, not proof): all 9 sampled means within relative 10^-2 of the closed values,
worst relative deviation 8.19e-04 (D=6 sigma); values as printed in the .out and findings.md.

## RULE-6 CLASSIFICATION TABLE (from findings.md)

| claim | class |
|---|---|
| rho_p definition, partition form, D_eff, rho_2 - 1 = 1/D_eff; uniform floor and equality case; flat simplex measure as Haar-frame pushforward and a=1,beta=0 family member | established-in-repo (appH; floor equality reproduced exactly in `s2_uniform_rho_r2.out`, "ALL EXACT CHECKS PASS", floor rho_p = prod_{k=1}^{p-1}(1+k/D), D=2..5 p=1..6) |
| four E[rho_p] closed forms, three sigma moments, Var factorization/positivity, limits and 4/D^3 rate, E[rho_2] - floor = (D-1)/(D(D+1)), mean-pin relations | in-folder exact (sympy, D symbolic, CHECKED lines in s4 .out; consumed Dirichlet monomial moment is the standard one, stated in the script) |
| 9 MC means within 1% (worst 8.19e-04) | MC corroboration, not proof |
| that the flat Dirichlet statistics select a profile, or that the flat measure is produced by the core matrix integral | NOT CLAIMED (appH: deformation origin "is not established"; frame side "supplies no state and no selection mechanism") |

## EVIDENCE FILES

- `s4_dirichlet_rho_direct.py` (9452 B, sha8 69a04377) / `.out` (41 lines, live sha8 **7b293544**,
  exit 0, final line ALL CHECKS PASS): the deliverable; all quoted numbers trace to it.
- `s2_uniform_rho_r2.py` / `.out`: floor equality (`ALL EXACT CHECKS PASS`) used for the
  established-in-repo row above.
- `s1_frame_identities.py` / `.out`: cited ONLY as frame-identity corroboration (Parseval/
  row-level/iid errors ~1e-15, truncated-frame rho_2 vs floor at N=6,8,12); NO Dirichlet content
  taken from it. Caveat when citing: at lc=8, N=32 the truncated-frame rows print
  `offdiag/minDiag inf  profile spread inf` (slot variance underflow; RuntimeWarning at s1
  lines 76-77, .out lines 39, 49).
- Superseded, never cited: `s2_uniform_rho.py`/`.out` (superseded by r2);
  `s3_dirichlet_rho_stats.py` (crashed, no .out); `s3b_dirichlet_rho_stats.out` Check-I/Check-II
  numbers - defects identified in findings.md ("What s3b's buggy path actually returned": wrong
  falling factorial (D-1)!/(D-b)! and missing unit-trace substitution; its Var[sigma] line
  evaluates negative at small D). s3b's pin block and MC block were sound and its in-file FIX 2
  note records the identification. Its numbers are not used anywhere in this package.
- `hygiene_102.py` / `hygiene_102.out`: HYGIENE PASS, exit 0 - ASCII-only, CRLF-only, no BOM,
  balanced braces, no \ref/\label/\eqref, every macro used present elsewhere in appH, exactly one
  closing scoped status sentence. The file documents two orchestrator plumbing fixes applied after
  tool-echo death #37: FIX H102 (macro loop mapped `\\(` and `\\)` both to `\\)`; keys iterated as
  written) and FIX H102b (appH contains a non-ASCII byte 0xe2 at offset 711159 from an integrated
  character; appH read with lenient UTF-8 decode, the ASCII-only assertion is on the insert).
- `findings.md`: authoritative route/results/classification/OPEN list; persisted by the orchestrator
  verbatim from the FIX-102 dispatch handback (provenance note at the head of the file; the
  handback's "sha8 17544b9f" for the s4 .out was a pipe/EOL artifact - live bytes 7b293544 govern).
- `insert-r1.tex`: the manuscript text, 3155 B, sha8 654284b4, one CRLF-terminated line.
- `simulate_apply_102.py` / `simulate_apply_102.out`: byte contract for the splice (next section).

## MANUSCRIPT CHANGE

One paragraph (`insert-r1.tex`), pure insertion, `chapters/appH-microscopic-proofs.tex` G-block,
immediately AFTER the "Eigenvalue reduction of the edge Gram and the Jacobian origin of the beta
factor." paragraph (the insert refers back to it: "confirmed numerically at \(D=3\) in the
eigenvalue-reduction paragraph above") and BEFORE the "Transport of the profile coordinate along
the pushforward family and its moment coordinates." paragraph. No existing text is modified,
moved, or deleted; no \ref/\label/\eqref (hygiene: none found); regional idiom preserved
(paragraphs separated by exactly one blank CRLF line).

Byte contract, simulated by `python -I proposals/102-g-profile-selection-output/simulate_apply_102.py`
from the repo root, exit 0 (real output `simulate_apply_102.out`, sha8 f66cb326):
- PRE: bytes 798457, sha256-16 cfb6af516017367f, CRLF 3866, bareLF 0, no BOM;
- PIN (asserted to occur exactly once, count printed = 1): the complete full text of the
  eigenvalue-reduction paragraph line + its CRLF + the following blank-CRLF separator line,
  quoted in full in the .out;
- payload: insert-r1.tex (3155 B, sha8 654284b4, CRLF-terminated) + one blank-CRLF separator = 3157 B;
- POST: bytes 801614 (= PRE + 3157, asserted), sha256-16 ad41acde1e45c887, CRLF 3868, bareLF 0,
  PIN still count 1; `SIMULATION PASS`;
- simulated POST written only to `scratch/102_sim_post.tex` (git-ignored); the live file is
  untouched by the simulation (in-memory copy only).

## SUGGESTED VERDICT CRITERIA + REPRO PACK

ACCEPT criteria: (1) the insert's statements match the s4 .out lines quoted here (grep the
factorizations, the Var formula, the MC table, the pin rows); (2) the splice anchor is the
eigenvalue-reduction paragraph boundary as above and the change is pure insertion; (3) the insert
asserts nothing beyond "exact statistics of a named measure on the profile simplex" and carries the
single closing scoped status sentence; (4) no status/priority/completion-classification text is
touched. REJECT/flag if any s3b or s3 number appears in the insert or this proposal as a result.

Reproduction pack (run from repo root):
- `python -I proposals/102-g-profile-selection-output/s4_dirichlet_rho_direct.py`
  - expected: exit 0; final line `ALL CHECKS PASS`; four `CHECK ... : True` lines;
    `Var[sigma] = 4*(D - 1)/((D + 1)**2*(D + 2)*(D + 3))`; `D^3 * Var[sigma] -> 4`; all 9 MC
    rel.devs <= 1e-2 (worst 8.19e-04). sympy + numpy; seeds fixed (default_rng(102),
    random.seed(102)).
- `python -I proposals/102-g-profile-selection-output/simulate_apply_102.py`
  - expected: PRE pins above; `PIN count in appH bytes = 1`; `payload bytes ... = 3157`;
    `POST bytes = 801614`; `POST == PRE + payload bytes = True`; final line `SIMULATION PASS`, exit 0.
- `python -I proposals/102-g-profile-selection-output/hygiene_102.py`
  - expected: `insert-r1.tex bytes = 3155`, `insert-r1.tex sha8 = 654284b4`, final line
    `HYGIENE PASS`, exit 0.

Status-label recommendation: none (routine write-up round; no status, priority or
completion-classification change proposed - Appendix H Problem G and its missing steps (i)-(iv)
unchanged). Milestone: routine.

No status, priority or completion-classification change is proposed or implied.
