# Proposal 075-g-edge-frameavg, round 1

Target: frontier edge G.edge-frameavg (chain-2 rank 1): frame-averaged evaluation
at fixed saddle, i.e. the avenue (3) of the 072 review and the ranked avenue (a)
of the 074 review, inside the 072 (H1)-(H4) hypothesis class on the product
fuzzy-sphere testbed.

## Result

Within the (H1)-(H4) class extended by cap frames, the frame average acts
benignly and controllably on the fixed-frame vacuum-term excess of the
integrated 072/073/074 paragraphs:

1. The frame dependence of the saddle data is exact: deforming a factor by a
   real matrix with Gram matrix B and taking the cap projector for a unit axis
   n, the squared edge length is s^2(n) = (1/4) M(N-M)(tr B - n^T B n), i.e.
   the manuscript's sigma_1^2 + sigma_2^2 is exactly the trace of B on the
   plane orthogonal to n (065 edge-datum formula, general axis; verified here
   by direct block computation at N <= 14 for general A and general n, relative
   deviations <= 1.4e-15, s1). Consequently the saddle rows and the continuum
   defect depend on the frame only through the two edge-length fractions
   u_f(n) = t sqrt(m_f(1-m_f) rho_f(n)), rho_f = s^2(n)/s^2(round frame).

2. The continuum defect is additive across the two arguments,
   Lambda(u1,u2) = R(m1,m1+m2,u1) + R(m2,m1+m2,u2), and each per-factor profile
   is strictly increasing and strictly concave (R_u = log((a+u)/(m+u)) > 0,
   R_uu = 1/(a+u) - 1/(m+u) < 0, sympy-checked closed forms, s2 section 2).
   Hence, on the mean-preserving axial family (E_n rho = 1, tr B = 3), the
   Jensen chain gives, for the sphere-averaged axes:
   Lambda(u1^-,u2^-) <= Lambda_bar <= Lambda(1/2,1/2) = log(27/16) =
   0.523248144, with the upper bound strict for any non-round mean-preserving
   deformation and the lower bound attained at the frame whose axes are the
   largest-eigenvalue axes. So the frame average strictly LOWERS the excess
   relative to the round-frame value, and the frame minimum stays strictly
   positive and extensive (Theta(N)) for every non-degenerate deformation; the
   lower bound can tend to 0 only as the transverse edge data of a factor
   degenerate (B -> rank 1).

3. Numerically (exact closed forms, s2): mean-preserving family
   B = diag((3-g)/2,(3-g)/2,g), averaged limit / frame minimum:
   g=0.6: 0.522691 / 0.502218; g=1.4: 0.522655 / 0.479485;
   g=2.0: 0.519217 / 0.396700; g=2.6: 0.511350 / 0.268892;
   all <= 0.523248144 (= g=1 value, the integrated saddle constant).
   Finite N (N=400,1600,3200, GL64 frames): frame-averaged Delta/N converges to
   the averaged limit with per-frame residual at most 7.70 (e.g. g=2.6, N=3200:
   bar/N=0.509033, min-frame/N=0.267304), so the limit exchange is uniform over
   frames at the tested scale; every frame value is positive.

4. Stacked rows (074 class): the frame-averaged stacked defect has limit
   q * Lambda_bar (s2/s3: g=1.6: 0.521881, min 0.454690; g=2.2: 0.517216,
   min 0.361662), finite-N tables at q<=3, N<=3200 with residuals <= 59.80;
   the round-frame sequence reproduces the integrated 074 values
   0.520906/1.037902/1.551490 (N=3200, q=1,2,3) exactly (diff <= 4.3e-07).

5. The auxiliary selection-data statements of the integrated paragraphs are
   frame-uniform at the tested scale: the corner-mode fraction N*delta_2/Tr E^2
   (m=(1/2,1/3), N=3200) reproduces 2.4396 at the round frame and stays in
   [0.9423, 2.4484] for axial parameters up to 2.6; the saddle rank ratio
   reproduces 0.8111 at the round frame and stays in [0.7858, 0.9023].

6. The large-perturbation breakdown of the 073 paragraph (box minimum vanishing
   at c=1/2, trivial diagram) is untouched: the frame average acts on the
   diagrams at fixed saddle data and never moves the saddle rows outside the
   box interior at any tested frame.

Nothing is derived for Problem G; every statement is conditional on (H1)-(H4)
plus the cap-frame class below. Problem G's missing steps (i)-(iv), the frame
average and minimisation of the leading reference, the two-sided diagrams and
the minimised block entropy all remain OPEN.

## Target and status

Problem: G (edge/entropy derivation of the boundary term), Appendix H ledger
section of the 065 block; ch17 completion criterion read live (L474-497):
"CRITICAL PATH; mechanism CLOSED CONDITIONALLY, derivation OPEN"; G DERIVED only
when the entropy density and stationarity are derived from matrix theory.
Current labels (quoted, not touched): Status OPEN, Priority CRITICAL PATH,
Completion PROGRAMME-CONDITIONAL.

Original target of G.edge-frameavg (frontier.yaml): the frame-averaged value of
the excess, since the integrated 072 result and its closing sentence are
explicitly fixed-frame ("not a minimisation over frames"). This package computes
the frame average over CAP frames at fixed saddle class. It does not close the
edge: the full frame average (conjugacy-class average over rank-M projectors)
and the minimisation of FlissFrenkelHartnollSoni2025 remain outside the computed
class. Classification of the package: bounded conditional computation with exact
structural components. DERIVED not claimed.

Dependencies: integrated 065 block (edge datum, 065 no-go), 072 (H1)-(H4) and
dominant-rep excess, 073 uniform row-perturbation description, 074 stacked-row
extension. No new bibliography.

## Source reading

Digest (compact, head eb8fc7d, appH hash 50f12c813181 matches live,
dirty-chapters: yes) + targeted reads, per dispatch: appH L3022-3170 read IN
FULL (entire Problem G entry and 065 block including the three integrated
paragraphs L3153-3159, L3161, L3163, the Vacuum-term paragraph L3165 and the
block closer L3167 - re-read this round to fix the "preceding paragraph"
references in the insert); ch17-agenda L474-497; 072 proposal-r1.md and
review-r1.md; 073 review files and shipped scripts; 074 review-r1.md and shipped
scripts; frontier.yaml G.edge-frameavg entry; reports/sme-scout-20261115-1409.md
head. The appH file (700,825 B) was never read whole (dispatch instruction);
make_digest.py --full not used (known defect, 074 review finding 1). Live pins
re-verified this round: appH 700,825 B / sha256 50f12c8131819f513ff37d5149529ba
616063578b04510891a6b7f1d43b8f25e / CRLF 3814 / bareLF 0; bib 37,463 B / sha256
4d6d7b2a...de6 / CRLF 1239 / bareLF 0. Anchor counts live: short `\emph{Vacuum
term.}` 2, long form 1, line-start long form 1, new header 0.

## Research and reasoning

(H1)-(H4), restated from the 072 package as recorded in the integrated
paragraphs (appH L3153-3163): (H1) the product fuzzy-sphere testbed
X^I = (A_1 J)^a (x) 1, 1 (x) (A_2 J)^a with interval projectors of ranks
M_f = m_f N, block of the union of rank M = M1+M2; (H2) leading semiclassical
order at the leading-order entropy of FlissFrenkelHartnollSoni2025, one dominant
U(M)-representation selected from the moments of the U(M1+M2)-invariant edge
data by Frenkel's rule (Frenkel2023EdgeModes), the transposition of the rule
from the diagonal cut to the block cut being a supplied transplant (the
manuscript records it as a transplant, conditional); (H3) saddle class rows
l_i = t s_i with fixed t (t = 2 sqrt(W), <l^2> = 4 s^2 W); (H4) two-row
diagrams, and their stacked (equal-depth) extension of 074.

Frame class added here (declared, and the honest limitation of the package):
a CAP frame on a factor is the rank-M spectral projector Theta(n) of n.J on its
M largest eigenvalues for a unit axis n in S^2; the frame average is the product
of the uniform measures on the two axes. This is the only frame family for which
the 065 edge-datum formula is available in closed form within the class; the
full U(N) conjugacy-class average over all rank-M projectors, and the
simultaneous frame-and-diagram minimisation of the leading reference, are NOT
computed and remain open. Deformations enter only through the Gram matrix
B = A^T A; the mean-preserving family B = diag((3-g)/2,(3-g)/2,g) (tr B = 3) is
chosen so that the sphere mean of rho is exactly 1 and the g=1 line reproduces
the integrated numbers (anchor discipline).

Step 1 (s1). From the exact 065 single-factor edge datum, s^2(n) computed by
direct block computation at N = 6..14: A = I gives s^2 = M(N-M)/2 (the
manuscript's sigma_1^2+sigma_2^2 = 2); general invertible A and general n give
s^2(n) = (1/4) M(N-M)(tr B - n^T B n) to <= 1.379e-15 relative over 8 trials
(seed 75001); the convention-free ratio form s^2(n)/s^2(e3) =
(tr B - n^T B n)/(tr B - B_33) holds to <= 5.4e-16; the sphere mean is
(1/4) M(N-M)(2 tr B/3) to machine precision; and the edge-datum identity
sum_a Tr(X_Sb X_bS) = (1/2) Tr(Theta Box Theta) holds at a general axis to
9.4e-16. The rho-normalisation rho(n) = (tr B - n^T B n)/tr(B) * (tr B /2)
normalised to rho(round) = 1 is therefore exact at finite N up to the k=1
convention of the 072 testbed; only the ratio enters the saddle rows.

Step 2 (s2). With u_f = t sqrt(m_f(1-m_f) rho_f), the 073 limit profile
Lambda(u1,u2) is separable, R(m,a,u) = G(a,u) - G(m,u); sympy confirms
R_u = log((a+u)/(m+u)) > 0 and R_uu = 1/(a+u) - 1/(m+u) < 0 for a > m > 0,
u > 0, and (sqrt)'' = -1/(4 u^{3/2}) < 0. Since rho(z) is affine in z^2, z ->
u(z) is concave, so z -> R(u(z)) is concave (increasing concave of concave);
numerically the second differences are negative (max -8.1e-07). Jensen on each
factor gives the chain quoted in Result 2; the lower bound is attained because
rho is minimised at the largest-eigenvalue axis of B (n^T B n maximised).
Numerical tables: s2.out (3).

Step 3 (s2, finite N). Frames on GL64 grids in z = cos(theta); rows
round(N u(z)); exact two-row closed form by prefix sums; every node positive;
the per-frame residual |Delta - N Lambda(u(z))| is at most 7.70 over all tested
(g,N), which together with the 073 uniform residual bound (constants uniform on
the compact range of fractions u in [u^-, u^+] reached by the tested family)
justifies exchanging average and limit at this scale; bar/N matches the
continuum averaged limit within 12/N at every tested point. g=1 reproduces the
shipped fixed-frame sequence 0.509694/0.518996/0.520906 (<= 4.3e-07), pinning
the machinery to the integrated numbers.

Step 4 (s2, asymmetric m=(1/2,1/3)). With independent frames the two row
lengths can cross; the exact finite-N defect is then the closed form of the
SORTED partition (074 verified it for sorted rows against the Weyl dimension
formula in exact rational arithmetic). Both continuum pairings are reported:
factor-pairing 0.492739 (= 0.187482 + 0.305257) and sorted-pairing 0.488857;
finite N=1200 tensor GL64xGL40: bar/N=0.486819, min/N=0.377697, max/N=0.536683;
the sorted lower pair 0.379756 bounds the frame minimum to within 12/N. Each
pairing is positive; the conclusion (positivity, Theta(N), frame-uniform bounds)
is insensitive to the pairing choice.

Step 5 (s3). Stacked rows reuse the 074 closed form; the limit is linear in the
depth so the frame average gives q * Lambda_bar with the same two-sided bounds;
round-frame anchors reproduce the integrated q-series.

Step 6. Corner-mode fraction and rank ratio: 072's quantities evaluated over
the frame grids; both stay bounded between positive constants uniform in the
frame (Result 5).

What is NOT touched: the diagram-selection input (H2) - the average is at fixed
saddle selection; the c=1/2 box breakdown (073) - it concerns linear
perturbations of the rows, a different variation; the block closer's sentence
that the frame average and minimisation of the leading reference are used for
its state and not re-derived - unchanged; the monotonicity gap recorded by 072;
items (i)-(iii).

Literature: no new citations. Frenkel2023EdgeModes and
FlissFrenkelHartnollSoni2025 are referenced in the manuscript already and are
relied on only in the integrated sense (records verified in the 072 round; the
sme scout of 2026-11-15 re-confirms Frenkel's selection rule is stated for the
diagonal cut with the block-cut case open, and that frame minimisation in
FlissFrenkelHartnollSoni2025 is a supplied input, not re-derived; I did not
re-fetch either paper this round - not independently re-verified beyond the
072/074 rounds' verification).

## Claim classification

- s^2(n) = (1/4) M(N-M)(tr B - n^T B n), ratio form, sphere mean, edge-datum
  identity at general axis: conditional (065 edge-datum class) + numerically
  verified at finite N (<= 1.4e-15, s1).
- Frame dependence factors through (u1,u2); separability of Lambda: established
  given the 073 limit (exact algebra).
- R_u > 0, R_uu < 0, sqrt concavity: established (closed form, sympy-checked).
- Jensen bounds (upper round-frame, lower most-contracted-frame): established
  within the class (concavity + monotonicity), including strictness for
  non-degenerate mean-preserving families; the "lower bound -> 0 only under
  transverse degeneracy" is the continuity statement in B, established.
- Frame-average / limit exchange: conditional; 073's uniform residual bound
  applies node-by-node with constants uniform on the tested fraction range;
  numerically witnessed (residuals <= 7.70 two-row, <= 59.80 depth 3).
- Numerical tables (continuum averages, finite-N bars/minima, asymmetric case,
  corner fraction, rank ratio, stacked averages): numerically verified finite
  samples (exact closed forms; deterministic grids).
- Stacked frame limit q*Lambda_bar: conditional (074 limit per frame) +
  numerical.
- Breakdown unchanged: argument + numerical observation at tested frames; not a
  proof.
- Whole package vs Problem G: PROGRAMME-CONDITIONAL evidence only; nothing
  derived, nothing closed.

## Proposed changes

File: chapters/appH-microscopic-proofs.tex (single insertion; no other file in
scope; bib unchanged - no new entry needed, zero-\cite insert).

Anchor: the unique line-start long-form paragraph header
`\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}`
(with its leading CRLF; verified count 1). The short form
`\emph{Vacuum term.}` occurs TWICE (L3006 and L3163) and must not be used.
The new paragraph is inserted immediately BEFORE the anchor as its own line
followed by one blank CRLF line, i.e. between the 074 stacked-row paragraph
(L3163) and the Vacuum-term paragraph (L3165). No existing text is replaced;
nothing is removed.

Insert file `insert-r1.tex` (3,175 B, sha256
e06aa9529f3530737daba961209b791bdf8be5ca284fc0bef15f79ad830e0f05, single ASCII
line + terminal CRLF, no `$`, no `\ref`/`\eqref`/`\label`/`\cite`, no square
brackets, no status vocabulary). Verbatim (single line in the file):

```latex
\emph{Frame average of the fixed-frame excess at the saddle.} Under the same hypotheses as the three preceding paragraphs, and within them, the fixed-frame excess extends to the average over cap frames: deforming a factor by a real matrix, with Gram matrix \(B\), the squared edge length of a cap with axis \(n\) is one quarter of \(M(N-M)\) times the trace of \(B\) restricted to the plane orthogonal to \(n\), a general-axis case of the edge-datum identity above, re-established here by direct block computation at small sizes to within roundoff, so the saddle rows and the continuum defect depend on the frame only through the two edge-length fractions, which enter the defect additively through a per-factor profile that is strictly increasing and strictly concave in the fraction. Averaging the two cap axes independently and uniformly over the sphere, the frame-averaged defect per \(N\) converges, with per-frame finite-\(N\) residuals bounded independently of the frame (at most \(7.7\) for the two-row defect and \(59.8\) at depth three, \(N\) up to \(3200\), against the uniform residual bound of the second preceding paragraph), to the sphere mean of the defect function, which by concavity is bounded above by the round-frame value \(0.523248144\), attained only when the edge data are of the round frame, and bounded below by the strictly positive value at the most contracted frame, attained at the axis of the largest eigenvalue of \(B\): for the mean-preserving axisymmetric family of axial parameter \(\gamma\), the averaged limit is \(0.522655,0.519217,0.511350\) and the frame minimum is \(0.479485,0.396700,0.268892\) at \(\gamma\) equal to \(1.4,2,2.6\), so that the average and the minimum of the defect over cap frames remain extensive and strictly positive at every tested non-degenerate deformation, the lower bound tending to zero only as the transverse edge data of a factor degenerate, while the round-frame value is an upper bound rather than the value of the average (numerical, via the exact closed form, \(N\) up to \(3200\)). The stacked-row excess obeys the same average, with limit equal to the depth times the averaged profile and residuals of the same order (numerical, depths up to \(3\), \(N\) up to \(3200\), reproducing the integrated isotropic values at the round frame); the corner-mode fraction of the selection data stays \(O(1/N)\) uniformly over the frames tested (between \(0.9423\) and \(2.4484\) for axial parameters up to \(2.6\)), the saddle rank ratio stays between \(0.7858\) and \(0.9023\), and the large-perturbation breakdown boundary of the second preceding paragraph is untouched by the frame average, which acts on the diagrams at fixed saddle data. These statements are for cap frames of the product testbed within the dominant-representation class of the three preceding paragraphs with the saddle parameter held fixed, rows in two stacks of equal length and depths held fixed; they are not the full frame average or the minimisation over frames of the leading reference, they leave the selection of the diagram, the monotonicity statement and the items (i)-(iii) unchanged, and they close nothing in Problem~G.
```

Stale passages elsewhere: none identified by this result. The 072 closing
sentence ("they are not a minimisation over frames") stays true and is not
modified; the block closer (L3167) and the Vacuum-term paragraph are unchanged;
the new header `\emph{Frame average` occurs zero times in the live tree
(pre-insert assert in simulate_apply.py).

Byte contract (simulate_apply.out, reproduced byte-identically by rerun):
PRE appH 700,825 B / sha256 50f12c8131819f513ff37d5149529ba616063578b04510891a
6b7f1d43b8f25e / CRLF 3814 / bareLF 0; PRE bib 37,463 B / sha256 4d6d7b2a668fda
a64663e624b3f296d833c3bbcaa06a74ec5012a7f494ce0de6 / CRLF 1239 / bareLF 0.
POST appH 704,002 B / sha256 4e94893c9f173b097b310ca9f8b6edba6949fde1c4b66f711
e1948396a4850e0 / CRLF 3816 / bareLF 0 (delta +3,177 B, +2 CRLF); bib unchanged.

## Verification scripts

All under proposals/075-g-edge-frameavg/, run as `python -I <path>` from the
repository root (Windows, CPython; numpy + sympy only, no randomness beyond the
fixed seed 75001 in s1, no wall-clock; every run is byte-identical - each `.out`
ships with a `.repro.out` that cmp-matches it).

| file | sha256 (first 12) | B | purpose / PASS line |
|---|---|---|---|
| s1_frame_edge_data.py | 9d3e55446604 | 5491 | exact finite-N s^2(n), ratio, sphere mean, edge-datum identity; PASS s1 |
| s2_frame_two_row.py | f69d579925cb | 12447 | anchors, structure (sympy), continuum table, finite-N symmetric/asymmetric, corner fraction, rank ratio; PASS s2 |
| s3_frame_stacked.py | a5c7c51a2026 | 5241 | stacked frame average, 074 anchors; PASS s3 |
| simulate_apply.py | a350ac0dd3c0 | 4235 | read-only integration simulation, byte contract |
| r1_moment_decomposition.py | 070a46521204 | 5866 | 073 s1 copy (byte-identical); PASS s1 |
| r2_hook_content.py | 748b5cf9c65a | 5538 | 073 s2 copy; PASS s2 |
| r3_saddle_residual.py | c3859b761a9f | 4455 | 073 s3 copy (corner + rank-ratio definitions reused in s2); PASS s3 |
| r4_uniform_rowshift.py | cd1aec5c0b4f | 8298 | 073 s4 copy (uniform residual bound); PASS s4 |
| r5_scaling_and_breakdown.py | c24c3de0fab4 | 9825 | 073 s5 copy (Lambda values, breakdown); PASS s5 |
| r6_uq_closedform.py | 10b8c4be35a3 | 5735 | 074 s1 copy (stacked exact identity); PASS s1 |
| r7_uq_scaling.py | d9fce04dc103 | 3774 | 074 s2 copy (q-series anchors); PASS s2 |
| r8_uq_boxmin.py | 7990ae853a03 | 6210 | 074 s3 copy (box minima); PASS s3 |

All r*.py/.out are byte-identical copies of the gatekeeper-reviewed 073/074
shipped files (verified by sha256 against the source folders, and re-run here:
each r*.repro.out matches its shipped .out). r8 inherits the cosmetic corner/N^2
print artifact disclosed in the 074 review (finding 3); no cited number uses it.

Reproduction-pack expected invariant outputs (mechanical checks before
re-deriving):
- s1: "worst rel dev over 8 trials: 1.379e-15"; "lhs=26.368931234466
  rhs=26.368931234466"; last line "PASS s1".
- s2: lines "N= 3200 prefix Delta/N=0.520906 shipped=0.520906";
  "g=1.4 ... 0.479485 ... 0.522655"; "g=(1,1): ... [2.4396, 2.4396]";
  "g=1.0: ratio=0.8111  shipped 0.8111"; last line "PASS s2".
- s3: "q=2 Delta_q/N=1.037902 shipped=1.037902"; last line "PASS s3".
- simulate_apply: "appH post bytes 704002 sha256 4e94893c9f173b09..."; all
  asserts pass (exit 0).

Every number cited in the insert and in this proposal appears verbatim in a
shipped `.out` file.

## Decisions Taken

1. Frame = independent uniform cap axes on S^2 (product measure). Reason: the
   065 exact s^2(n) formula exists only for cap projectors, so this is the
   largest frame family computable exactly within (H1)-(H4); it directly
   extends the "fixed frame" of the integrated paragraphs. Rejected: full U(N)
   conjugacy-class average (edge datum not available in closed form there
   within the class); simultaneous average+minimisation in the
   FlissFrenkelHartnollSoni2025 sense (would presuppose their framework's
   measure, supplied input).
2. Mean-preserving normalisation E rho = 1 (tr B = 3). Reason: anchors every
   line to the integrated 0.523248144 and separates "the average changes the
   value" from "the average changes the size of the data". Rejected: unnormalised
   family (would conflate scale).
3. Sorted-row pairing for the finite-N asymmetric case, both pairing limits
   reported. Reason: only the sorted closed form is verified against the Weyl
   formula (074); the conclusion is pairing-insensitive. Rejected: unsorted
   evaluation (log of a negative hook ratio - undefined).
4. Deterministic Gauss-Legendre grids, no sampling. Reason: byte-reproducibility.
5. Zero new citations (zero-\cite insert).

## Milestone assessment

Routine. No milestone trigger applies: this is conditional testbed evidence
inside the already-integrated 065 block; no critical-path step is derived.

## Status-label recommendation

Re-derived from ch17 L474-497 and the Appendix H ledger lines: current
critical-path set at the full-GR scope is A, B, C, D1, E, F, G-derived, N (H, I,
J optional). Problem G remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
Affected labels: none. This proposal changes no label and asserts no closure.

## Author decision needed

None. (The choice of cap frames over the full U(N) average is a routine
within-scope route choice, recorded in Decisions Taken; no core definition,
scope statement or label is touched.)

## Remaining open step

For the frontier edge (frame average of the excess): the frame average or
minimisation beyond cap frames - i.e. over general rank-M projectors (the
conjugacy class), and the interaction with the diagram choice (minimising frame
and diagram jointly). For Problem G itself, unchanged: the missing steps (i)
additivity-to-density mechanism, (ii) density functional form, (iii)
stationarity, (iv) relation to the IR entropy, plus the two-sided diagrams and
the minimised block entropy; the selection-rule transplant (H2) remains a
supplied input. The exact s^2(n) for cap frames established here is the
computable substrate for the next step: a minimisation over CAP frames, then
over projectors, of the full log d_mu (including the |mu| log M term), not just
of the excess.

## Special instructions for the gatekeeper

- Priority checks: (a) s^2(n) formula - re-derive at N=6 by hand for A=I, then
  run s1 and check the ratio-form invariance (it is convention-free);
  (b) the Jensen chain - R_u>0, R_uu<0, sqrt concavity, mean-preserving
  E rho = 1 at tr B = 3; (c) the frame-minimum attainment (n^T B n maximised at
  the largest-eigenvalue axis); (d) byte contract (PRE pins are the post-074
  live tree; POST independently reproducible).
- What must NOT be asserted: that the full frame average or the minimisation of
  FlissFrenkelHartnollSoni2025 was computed (only cap frames were); that any
  selection-rule question was advanced (selection is held fixed); that anything
  in Problem G or its items (i)-(iv) is closed, derived or improved in status;
  that the lower bound is nonzero uniformly over ALL deformations (it degenerates
  as B approaches rank 1 - stated).
- The insert calls 073 the "second preceding paragraph" from its own position
  (074 is the immediately preceding paragraph): verified against L3153-3165.
- The asymmetric-section sorted-pairing subtlety (frames can cross row lengths)
  is disclosed in the proposal and in the s2 comment; both pairings reported.
- r8's corner/N^2 cosmetic artifact is inherited and unused (074 review
  finding 3).
- Source reading was digest + targeted reads (never a full appH read, per
  dispatch); the 074 review's digest defect (finding 1) stands and is the
  orchestrator's, not this package's.
