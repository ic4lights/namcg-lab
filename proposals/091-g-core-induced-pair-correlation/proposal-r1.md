# Proposal 091-g-core-induced-pair-correlation, round 1

## Result

Route (A) delivered at sub-lemma level. The non-product pair-repulsion factor whose absence
089 and 090 recorded as the only route that can close the moment-map interaction edges is
**computed from a core-matrix coordinate**, not posed: for the edge block
\(A=\Theta\Pi\bar\Theta\) of a momentum in the gaussian state class of the Row length
paragraph, restricted to the subclass of constant variance on the block entries, the Gram
matrix \(G=AA^{\dagger}\) carries under the eigenvalue change of variables the Jacobian
\(\prod_{i<j}(\lambda_i-\lambda_j)^2\) (exact \(2\times2\) chart:
\(\det J=\tfrac12(y_1-y_2)^2\lvert\sin2\theta\rvert\); numerical \(D=3\) coincidence slopes
2.00 per pair, 6 at triple collision), and conditioning on \(\tau=\operatorname{Tr}G\)
separates exactly, so the normalised Gram spectrum \(p_i=\lambda_i/\tau\) carries **exactly**
the \((a,\beta)=(\lvert N-2M\rvert+1,\,2)\) member of the 090 fixed-trace family, the
exponents computed rather than posed (separation ratio constant \(2^{1-2a}\), checked). Exact
pair statistics discriminate it from the flat member: \(\operatorname{Var}(p_1)=3/(8a+12)\)
vs \(1/(4(2a+1))\), \(\mathbb P(u<\varepsilon)=\varepsilon^3\) vs \(\varepsilon\) at \(a=1\).
The repulsion exponent two is kinematic (change of variables, not the law): MC under
heterogeneous column variances preserves it (CDF exponent 3.09) while the prefactor deforms.
Two boundaries are established, not assumed: in the rank-one edge-datum class the slot-power
law is **exactly flat Dirichlet** (no repulsion at the slot-power level there), so the
repulsive weight lives on the Gram-spectrum coordinate, and the identification of that
coordinate with the profile coordinate of the moment map is not supplied by the repository.
Problem G, both edges (G.moments-interaction-nonconvex, G.moments-nonproduct-measures) and
every sub-target remain OPEN; nothing is closed here.

## Target and status

- Problem G, `chapters/appH-microscopic-proofs.tex` ledger block; completion criterion
  `chapters/ch17-agenda.tex` L488: "G is DERIVED only when the entropy density and
  stationarity relation are derived from the matrix theory and Λ_eff follows from them."
  Current status: OPEN, CRITICAL PATH at the full-GR / matrix-derived scope (re-read 2026-11-19).
- Dispatch target (chain 2 rank 1, edge G.moments-interaction-nonconvex; the same derivation
  serves edge G.moments-nonproduct-measures, REVIEW-089 exit (1)): derive from the matrix core
  a non-product slot measure / pair-correlation (repulsion-type) factor - the factor 089/090
  showed no symmetric postulated weight can produce - or produce a sharp bounded obstruction.
- Binding prior results respected: orbit rigidity (090), 089 bounded negative (fibre
  integration inside named product measures), 088 dichotomy, Hewitt-Savage/O(D)
  factorisation. None is re-litigated; none is invoked as if it derived NAMCG measure facts.
- This package: an important sub-lemma (the beta factor has a Jacobian origin on a named
  core-matrix coordinate subclass) plus two bounded boundary results. It changes no status,
  priority or completion label; G and both edges stay OPEN.

## Source reading

digest + targeted reads. Digest current at dispatch. Read in full: appH L3132-3197 (the whole
G ledger block 081-090, the Row length / Edge datum / Missing step / Vacuum term paragraphs);
ch17-agenda L475-495; proposals/090-g-interaction-induced-simplex-profiles/review-r2.md
(Scope and ranked relaxations); reports/graph/frontier.yaml L547-587 (chain-2 edge block);
reports/sme-scout-20261118-2350.md (R1-R3); templates
proposals/089-g-profile-pushforward-weight/hygiene_089_r3.py and
proposals/090-g-interaction-induced-simplex-profiles/smoke_compile_090_r2.py. Live
re-verification of all anchors and counts on the current tree by hygiene_091.py and
simulate_apply_091.py. No full scan: the insert adds a new conditional ledger paragraph and
changes no definition, assumption, scope statement or status passage.
## Research and reasoning

1. Setup. The gaussian state model of the Row length paragraph (momenta \(\Pi^a\) independent
   hermitian, entry variance \(f(l)\) on spin-\(l\) matrix elements) is a supplied input state
   (appH L3147-3149). Restrict to the subclass where the variance is constant on the block
   entries. Then \(A=\Theta\Pi\bar\Theta\), the \(M\times(N-M)\) edge block of the Edge datum
   paragraph, has independent identically distributed complex gaussian entries; write
   \(G=AA^{\dagger}\), \(D=\min(M,N-M)\) nonzero eigenvalues.
2. Eigenvalue change of variables (the Jacobian origin). Pass from the \(M(N-M)\) real
   coordinates of \(A\) to the eigenvalues of \(G\) and the fibre. On the fibre chart
   \(Z=U\operatorname{diag}(y)U^{H}\) the Jacobian of the Hermitian eigenvalue-eigenvector map
   is the Vandermonde squared: exact at \(D=2\) via the explicit chart
   \(U=\begin{pmatrix}\cos\theta&\sin\theta e^{i\phi}\\-\sin\theta e^{-i\phi}&\cos\theta\end{pmatrix}\),
   \(\det J=\tfrac12(y_1-y_2)^2\lvert\sin2\theta\rvert\), verified numerically-exactly at six
   rational points to \(10^{-30}\) (s2c; the sympy trigsimp failure is a simplifier limitation,
   recorded); at \(D=3\) by finite-difference \(\det J\), coincidence slope 1.990-1.998 per
   pair (5 trials) and 6.000 at triple collision (3 trials) (s2e). The general-\(D\) formula
   is the standard complex Wishart Jacobian (textbook: Muirhead; not independently verified) -
   the package is self-contained at \(D\le3\). The exponent two is therefore a property of
   the complex Hermitian structure of the core matrices, not of any weight.
3. Trace conditioning and the 090 family. The joint density of \(\lambda\) (gaussian block
   weight) times the Jacobian is \(\propto\prod_i\lambda_i^{a-1}\prod_{i<j}
   (\lambda_i-\lambda_j)^2 e^{-\tau}\) with \(a=\lvert N-2M\rvert+1\) (Wishart exponent
   \(\lvert N-2M\rvert\) plus the delta from \(\tau\) integration); the substitution
   \(p_i=\lambda_i/\tau\) separates \(\tau\) (density \(\propto\tau^{2a+1}e^{-\tau}\) at
   \(D=2\); exact \(\tau^7/210\) inner integral at \(a=3\), s3c; \(\Gamma(8)\) CDF leading
   term \(t^8/40320\), s3c) from the profile density \(\propto\prod p_i^{a-1}
   \prod(p_i-p_j)^2\): the separation ratio joint\(\cdot\lvert\det J\rvert\) divided by
   \(\tau^{2a+1}e^{-\tau}u^2(1-u^2)^{a-1}\) is the constant \(2^{1-2a}\) (s2; this is where
   the quarantined dead-pass script s1 failed - it asserted constant 1). The profile law is
   **exactly** the \((a,\beta)=(\lvert N-2M\rvert+1,2)\) member of the 090 fixed-trace beta
   family, free of the block variance, as 090's member is.
4. Pair statistics as discriminators (exact, \(D=2\)). Separation density
   \(f(u)\propto u^2(1-u^2)^{a-1}\), mode \(u^{*}=1/\sqrt a\) (interior iff \(a>1\));
   \(\mathbb E u=2\Gamma(a+\tfrac32)/(\sqrt\pi\,\Gamma(a+2))\), \(\sqrt a\,\mathbb E u\to
   2/\sqrt\pi\); \(\operatorname{Var}(p_1)=3/(8a+12)\) against the flat \(\beta=0\) comparator
   \(1/(4(2a+1))\) (exact, s2f) - at \(a=1\): \(3/20\) vs \(1/12\);
   \(\mathbb P(u<\varepsilon)=\varepsilon^3\) vs \(\varepsilon\) (s2b_v2). These are the
   signatures 089 showed no postulated symmetric fibre-average can generate, and here they
   are computed.
5. Kinematic universality (prefactor vs exponent). Because the exponent is a Jacobian, a
   non-constant variance profile on the block entries deforms only the prefactor: MC at
   \(D=2\) with column variances (1,4,9,16) keeps the \(u\)-CDF exponent 3.09 (density 2.09,
   within fit noise of 3), against 2.986 for the iid block (s3_v3); the exact integrated
   fibre with a two-value profile reproduces the 089 slot-pushforward density
   \(1/(g_1g_2(x/g_1+(1-x)/g_2)^2)\) pointwise (8 points, s2d_v2), i.e. the prefactor
   deformation is real and computable while the exponent survives. The **closed family form**
   is claimed only in the constant-variance subclass.
6. Rank-one boundary (081-idealisation consistency). In the rank-one edge-datum class the
   slot vector is a gaussian column contraction whose coefficients use only off-diagonal
   entries of \(\Pi\) (the two cut sides carry the row and column vectors), hence independent
   complex gaussian: the normalised squared entries are **exactly** flat Dirichlet at
   \(D=2\), with \(D=3\) moments matching \((1/3,1/6,1/12)\) to MC precision (s3_v3 (3)).
   So the slot-power profile of the moment map carries no repulsion in that class - the core
   reproduces 089's flat case there - and the repulsive weight found here lives on the
   Gram-spectrum coordinate. The identification of the moment-map profile coordinate with
   Gram-spectrum data is not supplied by the repository (consistent with 086's note that the
   moment map carries no weight on profile space).
7. What is NOT done: the core-action matrix integral is not evaluated (all computations are
   on the supplied gaussian state class plus change-of-variables identities); no state is
   fixed; selection stays inside the orbit equivalence relation (every law obtained is
   relabelling-invariant, so 090's orbit-rigidity alternative applies verbatim); the Missing
   step items are unchanged; RTN/Hewitt-Savage are not cited as if they derived anything.
8. Comparison with the original target. The target asked for a derived non-product slot law /
   pair-repulsion factor from the core, or a bounded obstruction. Delivered: the pair-
   repulsion factor is derived from core-matrix coordinates on the named constant-variance
   subclass (exact \(D=2\), standard+\(D=3\) numerics above), closing the "postulation
   forbidden" gap for the factor itself on that subclass; and a bounded flatness result at
   the rank-one slot-power level whose hypothesis class is stated. The edge is not closed:
   carrying the weight from the Gram-spectrum coordinate into the moment-map profile requires
   the coordinate identification, an unresolved state-side input, and the entropy-density and
   stationarity link of 090 is untouched.

Literature checked vs not. Independently verified (arXiv abs page): Kumar-Sambasivam-Anand,
arXiv:1701.07402 (fixed-trace complex Wishart-Laguerre ensemble is standard; smallest-
eigenvalue marginals; does not contain the fixed-trace Jacobian derivation used here).
Not independently verified: Muirhead, Aspects of Multivariate Statistical Theory (standard
Wishart Jacobian); Forrester, Log-gases and Random Matrices. The scout-supplied id
arXiv:1301.6213 was checked and is an unrelated paper - discarded. Manuscript prior art: no
Wishart/Wigner/Joint-eigenvalue mechanism exists in the manuscript; the single "Vandermonde"
mention (appH L1612, Problem E slice-bridge band) is a different context and the new
paragraph's header distinguishes it. No bibliography edit is requested; the insert carries no
citations.

## Claim classification

- Gaussian block entries in the constant-variance subclass: conditional result of the supplied
  gaussian state model (input state, appH L3147-3149).
- \(\det J=\tfrac12(y_1-y_2)^2\lvert\sin2\theta\rvert\) at \(D=2\): established derivation
  (exact numerics at six points, s2c).
- \(D=3\) coincidence exponents 2/6: numerical verification (s2e), not a proof.
- General-\(D\) Wishart Jacobian \(\prod(\lambda_i-\lambda_j)^2\): established textbook
  identity; record not independently verified; the package derivation covers \(D\le3\).
- \(\tau\)-separation, exponents \(a=\lvert N-2M\rvert+1\), \(\beta=2\), ratio constant
  \(2^{1-2a}\), \(\tau^7/210\) and \(\Gamma(8)\) checks: established derivation + exact
  symbolic checks (s2, s3c).
- Exact pair statistics (mode, \(\mathbb E u\), variances, \(\varepsilon^3\) tail): established
  (s2b_v2, s2f).
- Kinematic exponent two / prefactor-only deformation: established mechanism (Jacobian
  factor independent of weight) + numerical MC confirmation (s2d_v2, s3_v3); the closed
  family form outside the constant-variance subclass: unresolved.
- Rank-one slot law exactly flat Dirichlet: established at \(D=2\); numerical at \(D=3\).
- Gram-spectrum coordinate = moment-map profile coordinate: unresolved (not supplied).
- Everything about Problem G's completion: unchanged, OPEN.
## Proposed changes

One file: `chapters/appH-microscopic-proofs.tex`. Purely additive; no existing sentence is
replaced; no equation is touched; no other passage becomes stale.

Anchor. The 090 paragraph ends with the unique line-final text
`...and it closes nothing in Problem~G.` and is followed by a blank line and the line-initial
`\emph{Vacuum term.}`. Compound PIN (live count verified 1):
`closes nothing in Problem~G.\r\n\r\n\emph{Vacuum term.}`; the `\emph{Vacuum term.}` side is
verified at line start. Splice: after `closes nothing in Problem~G.\r\n\r\n` insert the single
line of `insert-r1.tex` plus one CRLF. Both boundary texts stay.

Insert file: `insert-r1.tex` (3773 B, sha8 3e471d12, single CRLF-terminated line, ASCII-only).
Text (verbatim):

```latex
\emph{Eigenvalue reduction of the edge Gram and the Jacobian origin of the beta factor.} Let \(\Pi\) be a momentum matrix of the gaussian state class of the Row length paragraph, in the subclass of constant variance on the block entries, and let \(A=\Theta\Pi\bar\Theta\) be the \(M\times(N-M)\) edge block of the Edge datum paragraph. Then the entries of \(A\) are independent identically distributed complex gaussians, and the Gram matrix \(G=AA^{\dagger}\), whose nonzero spectrum has size \(D=\min(M,N-M)\), carries under the change of variables to its ordered eigenvalues \(\lambda_{1}>\dots>\lambda_{D}>0\) and fibre the Jacobian \(\prod_{i<j}(\lambda_{i}-\lambda_{j})^{2}\): the squared Vandermonde factor of the fixed-trace beta deformation of the preceding paragraph is, on this coordinate, a change-of-variables Jacobian, and its exponent two is fixed by the complex Hermitian structure of the core matrices rather than posed. At \(D=2\) the chart computation is exact, the eigenvalue-eigenvector Jacobian of a Hermitian \(2\times2\) matrix being \(\det J=\tfrac{1}{2}(y_{1}-y_{2})^{2}\lvert\sin 2\theta\rvert\); at \(D=3\) the coincidence slopes of \(\det J\) are \(2\) per pair and \(6\) at triple collision, to within \(0.01\) numerically. Conditioning on the block trace \(\tau=\operatorname{Tr}G=\lVert A\rVert_{F}^{2}\) is a fixed-invariant fibre: the scale separation of the preceding paragraph holds with the exponents \(a=\lvert N-2M\rvert+1\) and \(\beta=2\) computed rather than posed, and the normalised eigenvalue profile \(p_{i}=\lambda_{i}/\tau\) carries exactly the \(a=\lvert N-2M\rvert+1\), \(\beta=2\) member of the family of the preceding paragraph, free of the block variance as there. Two exact pair statistics at \(D=2\) quantify the repulsion: with \(u=\lvert p_{1}-p_{2}\rvert\) the separation density is \(f(u)\propto u^{2}(1-u^{2})^{a-1}\), the variance is \(\operatorname{Var}(p_{1})=3/(8a+12)\) against \(1/(4(2a+1))\) at \(\beta=0\) for the same \(a\), and at \(a=1\) the coincidence probability is \(\mathbb{P}(u<\varepsilon)=\varepsilon^{3}\) against \(\varepsilon\) for the flat member (exact identities). The exponent two is kinematic: it belongs to the change of variables, not to the gaussian weight, so a non-constant variance profile on the block entries deforms the prefactor of the eigenvalue density and leaves the repulsion exponent two, confirmed numerically by Monte Carlo under heterogeneous column variances; the closed family form is stated in the constant-variance subclass, where the block law is exactly the gaussian one. Two boundaries are recorded. In the rank-one edge-datum class of the Row length paragraph the slot vector is a gaussian column contraction with independent identically distributed complex entries, and its normalised squared entries are exactly flat on the simplex at \(D=2\), with the flat Dirichlet moments confirmed numerically at \(D=3\): the slot-power profile of the moment map therefore carries no repulsion in that class, and the repulsive weight lives on the Gram-spectrum coordinate \(p_{i}=\lambda_{i}/\operatorname{Tr}G\), whose identification with the profile coordinate of the moment map is not supplied by the repository. And every member obtained here is relabelling-invariant, so the orbit-rigidity alternative of the preceding paragraph applies verbatim to the computed member: whole orbits, never single profiles. These statements are change-of-variables and exact-statistics statements for the named constant-variance edge-block subclass and the rank-one slot class of the gaussian state model; the matrix integral of the core action is not evaluated, no state is fixed, the missing steps of the Missing step paragraph are unchanged, and they close nothing in Problem~G.
```

Integrator notes: the phrases "the preceding paragraph" bind to the 090 paragraph; if any
earlier integration moves 090, re-check adjacency before splicing. Header text verified
absent from appH (count 0), so no header collision. Close idiom surface form: plural noun
"they close nothing in Problem~G." Expected POST (from simulate_apply_091.py rehearsal):
size 760,461; `close nothing in Problem~G.` 16 to 17; `closes nothing in Problem~G.` stays 1;
`\emph{Vacuum term.}` stays 2; new header 1; CRLF 3846; POST sha256
784cb0a8351d7bf51d62315b9fca9718df419aef133ebd2f68921e6be82f35a1 (valid only if the tree is
still at PRE sha 068ce3f2...).

## Verification scripts

Manifest `manifest.md` carries the full inventory with sizes and sha8. Reproduction pack
(`python -I` from repo root):

- `python -I proposals/091-g-core-induced-pair-correlation/hygiene_091.py` - expect final
  line `HYGIENE 091: PASS` (24 OKs: insert bytes/sha8/CRLF/ascii, banned-word screen incl.
  "derived", emph==1, no dollars/brackets/refs, paren balance 35/35, close-idiom 1, appH
  live counts 1/16/2, header absent).
- `python -I .../smoke_compile_091.py` - expect `SMOKE 091: PASS` (POS rc0; NEG rc1 with
  undefined control sequence). Scratch dir in-folder, deleted on exit.
- `python -I .../simulate_apply_091.py` - expect `SIMULATE 091: PASS`; prints PRE sha, PIN
  count 1, POST 760461 and POST counts (read-only).
- `python -I .../s2_exact_d2.py` - expect separation-ratio constant True, ratio 2/4**a.
- `python -I .../s2b_exact_d2_stats_v2.py` - expect mode 1/sqrt(a); E[u] limit 2/sqrt(pi);
  eps**3 tail True; 3/20 vs 1/12.
- `python -I .../s2c_chart_check.py` - expect 6x True (detJ identity to 1e-30).
- `python -I .../s2d_numeric_id_v2.py` - expect 8x True and 8x True (Var identity; 089
  integrated density identity); `S2D-V2 DONE`.
- `python -I .../s2e_d3_jacobian_num.py` - expect slopes 1.99-1.998 and triple 6.0.
- `python -I .../s2f_dirichlet_var.py` - expect `== 1/(4(2a+1)): True`.
- `python -I .../s3_mc_checks_v3.py` - expect CDF exponents 2.986 and 3.092; E[u^2] deciles
  0.332-0.334; rank-one moments 0.3340/0.1672/0.0836; `S3-V3 DONE`.
- `python -I .../s3b_tau_exponent.py` - expect flat deciles; the 5.23 tau-CDF fit is the
  recorded unresolvable-window artifact (s3b_tau_exponent_v2.out).
- `python -I .../s3c_tau_exponent_exact.py` - expect 1/210 True, tau**7/210 True, leading
  term True; `S3C DONE`.

Quarantined dead-pass WIP `s1_jacobian_v4.py/.out` is registered in the manifest, is not
relied upon, and its check-(2) assertion (ratio 1; true constant \(2^{1-2a}\)) is wrong -
do not re-run as evidence.

## Decisions Taken

- Route (A) over (B): (A) produced a derived factor, so the bounded-obstruction branch was
  not needed; the flatness result is reported as a boundary, not as route (B).
- Closed-form family claims restricted to the constant-variance subclass; prefactor
  deformation for profile laws kept numerical/exact-only-where-computed. Rejected: claiming
  the family for general \(f(l)\) (unsupported).
- Close idiom "they close nothing in Problem~G." (plural noun form matching 081-089 usage);
  keeps the verb form count at 1. Rejected: third-person singular (would alter the PIN
  semantics for future items).
- Kept the s3b MC artifact and answered it with the exact s3c rather than deleting - honest
  record of what MC can and cannot resolve for Gamma(8).
- Discarded scout-supplied arXiv id 1301.6213 (verified unrelated); cite Muirhead/Forrester
  as standard-but-unverified, arXiv:1701.07402 as the verified anchor. No bib change needed
  (insert carries no citations).
- Header name chosen unique in appH (verified 0 occurrences) to avoid collision with any
  concurrent chain.
- Dead-pass WIP quarantined rather than edited; all its central identities independently
  re-derived (s2c, s2b_v2, s2, s2e).

## Milestone assessment

Routine. No MILESTONE.md trigger is claimed: no critical-path step is closed, no dependency
made optional. The package is a consequential sub-lemma (the beta factor's Jacobian origin on
a named subclass) that improves two OPEN edges without closing them; the gatekeeper rules.

## Status-label recommendation

Derived from ch17 (L475-495) and Appendix H, the current critical-path set is A, B, C, D1,
E, F, G-derived, N (re-read 2026-11-19; unchanged). Affected labels: none - all unchanged.
G stays OPEN/CRITICAL PATH; edges G.moments-interaction-nonconvex and
G.moments-nonproduct-measures stay OPEN; G.moments-fibre-named stays bounded with re-entry
only via a relaxation an accepting review names (this package may be weighed as candidate
evidence of the kind of relaxation 089/090 anticipated, but that is a ledger decision, not
made here).

## Author decision needed

None. (The Gram-spectrum-vs-profile-coordinate identification is a research gap, not a
label/scope decision; supplying it as a postulate would be a core input and would then have
to be labelled as such in a future package - flagged for visibility, not recommended.)
## Remaining open step

Exactly what would still be needed, in dependency order:

1. Coordinate transport: a derivation (or a clearly labelled supplied input) identifying the
   profile coordinate of the moment map with the Gram-spectrum data
   \(p_i=\lambda_i/\operatorname{Tr}G\), or a mechanism that carries the Jacobian weight from
   the Gram layer into slot powers beyond the rank-one class (where flat Dirichlet is an
   exact obstruction, hypothesis class: rank-one edge datum + off-diagonal gaussian
   contraction).
2. Beyond the constant-variance subclass: the eigenvalue-density prefactor under the named
   variance-profile law is computed only in the integrated \(D=2\) fibre case (s2d_v2); the
   closed family form there is unresolved.
3. The 090 chain unchanged: entropy density and stationarity relation from the matrix theory,
   \(\Lambda_{\mathrm{eff}}\) from them (ch17 L488), remain the completion criterion for G.
4. Selection/orbit rigidity: untouched; every law here is relabelling-invariant, so the
   profile-vs-orbit dichotomy of 090 applies to the computed member as well.
5. Core action: the matrix integral of the core action is still not evaluated; all results
   here are change-of-variables and exact-statistics statements on the supplied gaussian
   state class.

## Special instructions for the gatekeeper

- Scope limits that must be honoured in review: the derivation is for the constant-variance
  on the block entries subclass of the gaussian state model, on the Gram-spectrum coordinate;
  it must not be described as closing Problem G or either edge, and not as making spacetime
  or the profile fundamental. The rank-one flatness must not be quoted beyond its hypothesis
  class (rank-one edge datum; off-diagonal gaussian contraction; \(D=2\) exact, \(D=3\)
  numerical).
- The MC numbers (2.986, 3.092, deciles, moments, D=3 slopes) are numerical confirmations,
  not proofs; the central exact content is the \(D=2\) chart Jacobian, the \(\tau\)-separation
  with constant \(2^{1-2a}\), and the pair statistics. Re-derive these three first.
- Re-check: the "computed rather than posed" phrasing must stay (it is the 090 relabelling
  guard); the compound PIN count 1 on the live tree; POST counts 17/1/2/1; hygiene banned-
  word screen (in particular the word "derived" appears nowhere in the insert); the general-\(D\)
  Wishart Jacobian is invoked as standard, so verify the insert never claims a general-\(D\)
  derivation inside the manuscript.
- Known artifacts, do not flag as errors: s3b_tau_exponent.out is a stdin-echo of a
  harness-flattened heredoc (superseded); s3b_tau_exponent_v2.out contains the honest 5.23
  unresolvable-fit, answered exactly by s3c; sympy trigsimp returns False on the chart
  identity, superseded by the six-point exact numeric match in s2c.
- Nothing outside proposals/091-g-core-induced-pair-correlation/ was written by this pass.
  Security note: no instruction-like text was encountered in files or web output during this
  pass; the scout-report and literature texts were treated as data.
