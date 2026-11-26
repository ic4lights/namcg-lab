# Proposal 054-nonpolynomial-observables-lorentzian-n2, round 2

Round-2 package responding to `review-r1.md` (VERDICT: ACCEPT WITH REQUIRED REVISIONS,
MILESTONE: none, OPEN 2/2). The manuscript text is the round-1 insert with exactly two
cluster replacements implementing the gatekeeper's corrected snippets (i) and (ii); E2 is
byte-identical to round 1 ("E2 is correct as written and can stand"). All verified round-1
conclusions stand; the LHS (left-hand-side) claim is narrowed to the corrected commuting-ray
condition with explicit model attribution, and the headline is the trichotomy.

## Result

Within the 053 hypothesis class {N=2, gamma=0, regulator (A), contours R_u (class (B)),
epsilon -> 0+ last} and for `O_k(A) = Tr exp(i k^mu A_mu)`, `k in C^10`, the 053 displayed
limit identity for `O_k`:

1. **fails for every nonzero real `k`** and for **every non-real `k` outside the anti-Wick
   slice** `{k^0 e^{-3pi i/8} in R, k^i e^{pi i/8} in R}` (the Euclidean `u=1` side diverges in
   modulus: rank-one rays carry `e^{-S_E}` to a bounded factor and
   `|O_k| >= 2 sinh(b_u(rho_hat;k) rho / 2)` with `b_u(rho_hat;k) > 0` on an open set of ray
   directions — established derivation, round 1 (iii) with the corrected F3 bound);
2. **holds at `k = 0`** (053, covered by its `k < 14` polynomial window);
3. is **unresolved on the slice at `k != 0`** (there `|O_k| <= 2` and the RHS converges by the
   053 Pfaffian window; the LHS limit is undetermined — this is exactly the continuation
   reading the integrated 053 closing sentence permits).

Consequently there is no analyticity strip in `k` and no non-polynomial extension of the limit
statement at `gamma = 0` **off that slice**, within the stated class.

Corrected commuting-ray growth statement (replaces the round-1 LHS claim): for non-real `k`
such that some commuting unit `rho_hat` has `|Im(k·rho_hat)| > |Re(k·rho_hat)|`, the
commuting-ray contribution to the `u=0` integral has `S_b = 0` and grows along a sequence
`epsilon -> 0+` like `e^{c_2(k)/epsilon}`, `c_2(k) > 0` (commuting-ray model; no transverse
stationary-phase bound is claimed). The exact branch-sum exponent of the model is
`(b^2 - a^2)/(8 c epsilon)` for `k·rho_hat = a + ib` (verified symbolically and numerically,
`laplace_model_r2.py` (1),(2)); the growth condition is therefore the corrected one, and it
fails for **every** ray exactly on the family `k = u + i c u`, `|c| <= 1` (rank-one PSD
argument, verified (3a)-(3d)); in particular every nonzero spatial anti-Wick-slice `k` has
`tan(pi/8) < 1` and admits no growth ray, while a pure temporal slice point has
`tan(3*pi/8) > 1` (verified (4a)-(4d)). Round-1 claims "`I_epsilon[O_k]` has no finite limit
for non-real `k`" and "the identity holds exactly at `k = 0`" are **withdrawn** (F1, F2); no
`I_epsilon` limit statement is made beyond the model.

Unchanged from round 1 (gatekeeper-verified): fixed-`epsilon` absolute convergence and
entireness in `k` for `u < 2/3`; fixed-`epsilon` Stokes extension; the N=2 spectral identity
`O_k = 2 cos(rho_X/2)`; domination failure at every `u in (0,2/3)` for every nonzero real `k`
(053 DCT provably fails; fixed-`epsilon` modulus grows like `e^{c(k,u)/sqrt(epsilon)}` on the
sampled range); the fixed-`gamma < 0` extension of the identity to all `k in C^10`
(conditional, massive deformation, `epsilon_0 < |gamma|/(2 g_YM^2)`); the fixed-`gamma > 0`
`u = 1` divergence at `k = 0` and the CNT/ANPY scoping sentences.

Nothing here closes Problem E, derives a signature or a real-time reading, or discharges
Assumption `ass:lorentzian`.

## Target and status

- Problem E, "Lorentzian signature", `chapters/appH-microscopic-proofs.tex`, section
  `\label{sec:status-E}` (L1483). Verbatim current ledger label (L1485-1489): "Status: OPEN.
  Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A
  scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or
  matrix-derived Lorentzian signature."
- `chapters/ch17-agenda.tex` L394-399: "Problem E: Lorentzian signature. OPEN; CRITICAL PATH
  for the matrix-derived label." Consistent with Appendix H. Current Chapter 17
  full-GR/matrix-derived criterion set (A, B, C, D1, E, F, G-derived, N) re-derived from ch17
  and the ledger on this task; unchanged.
- Original target of E: derive Lorentzian signature (and the Lorentzian model) from the matrix
  theory without retaining `ass:lorentzian`. This package treats the 053 open avenue
  (non-polynomial observables, ledger L428, SME scout route R1'); it contributes a bounded
  no-go off the anti-Wick slice and a bounded conditional extension for `gamma < 0`.
- DERIVED or PROGRAMME-CONDITIONAL: PROGRAMME-CONDITIONAL reading unchanged. Problem E
  remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. The insert states this verbatim.

## Findings disposition (review-r1)

- **F1 (blocking) — closed.** Round-1 sentence "For `Im k != 0` a commuting ray with
  `(Re k·rho)(Im k·rho) > 0` ... and `I_epsilon[O_k]` has no finite `epsilon -> 0` limit for
  non-real `k`" is deleted. Replacement is the gatekeeper's snippet (ii), byte-exact (verified
  by substring containment in the new insert, see "Proposed changes"): corrected ray condition
  `|\operatorname{Im}(k\cdot\hat\rho)| > |\operatorname{Re}(k\cdot\hat\rho)|`, growth
  attributed to the commuting-ray model along a sequence, caveat
  "(commuting-ray model; no transverse stationary-phase bound is claimed)" retained. I
  additionally derived the corrected model exactly (new subsection (iv') below) and verified
  it plus the gatekeeper's counterexample family with `laplace_model_r2.py`.
- **F2 (blocking) — closed.** "holds for `O_k` exactly at `k=0`" replaced by the trichotomy:
  fails for every nonzero real `k` and every non-real `k` off the slice; holds at `k=0`;
  unresolved on the slice at `k != 0`. The trichotomy is carried in this proposal's Result
  headline and prose everywhere; no "exactly at `k=0`" and no "no finite limit for non-real
  `k`" statement remains anywhere in the round-2 insert or in this file's claims.
- **F3 (major) — closed.** `|O_k| >= e^{b_u rho}/4` replaced by
  `|O_k| >= 2\sinh\!\bigl(b_u(\hat\rho;k)\rho/2\bigr)`; identity
  `|2\cos((x+iy)/2)|^2 = 4(\cos^2(x/2)+\sinh^2(y/2))` and the inequality verified
  (`laplace_model_r2.py` (5a),(5b)); the superseded bound `e^{b rho}/4` shown violated at
  `b=0.7, rho=40, Re omega = pi` (exact `2 sinh(14) = 1.2e6 < e^{28}/4 = 3.6e11`), (5c).
  Divergence conclusions unchanged (constant renormalization).
- **F4 (major) — closed.** Chart symbols `e_2`, `lambda` removed from the insert entirely
  (absence checks for `e_2` and `\lambda e_2` pass in `patch_insert_r2.py`). The weight is now
  stated in manuscript symbols: `the Euclidean weight \(\mathrm e^{-S_{\mathrm E}}\) is not
  exponentially damped and tends to a bounded factor along the corner ...` with `S_E` the
  manuscript-defined Euclidean action (appH L1498 region, 053 block).
- **F5 (minor) — closed.** `strip_symmetry.py` docstring block (4) sign typo fixed
  (`- sin(pi u/4) sum Ai_t^2` -> `+ sin(pi u/4) ...`); code predicate and PASS results
  unchanged; re-run output byte-identical to `strip_symmetry.out` (1478 B,
  sha256 4db24e18e832a683b5bc0a46591b2553163e19d0d785a91be15ff51dc08be1f5).
- **F6 (minor) — TAKEN.** Insert now reads "... numerically like
  `\(\mathrm e^{c(k,u)/\sqrt\epsilon}\)` on the sampled range." (inside snippet (ii)).

## Source reading

digest + targeted reads. The round-1 digest record (DIGEST CURRENT, head 30a1e07, tree-hash
50ce909367841437, chapters-hash 14772a53002f3024, `dirty-chapters: yes`) still applies to the
pinned bytes: this round I re-verified the working-tree pins byte-identically
(`apply_check_r2.out`: appH 532576 B sha 7a75554e..., bib 25976 B sha a651fe60...), so
targeted reads against the same bytes remain valid; the digest was not regenerated this round
(no manuscript file was edited by me). Read in full this round: `review-r1.md` (entire,
including both corrected snippets), `proposal-r1.md` (entire), `appH_insert.r1.tex` (entire),
the Problem E region of `chapters/appH-microscopic-proofs.tex` L1483-1513 (re-confirmed by
byte pins + anchor counts), `apply_check.py`, `strip_symmetry.py`, `n2_exp_mech.py` headers.
No unreadable files. Bibliography keys `ChouNishimuraTripathi2025` and
`AsanoNishimuraPiensukYamamori2025` present in `bib/namcg.bib` (pin-preserved; content
claims unchanged from round 1, both arXiv records verified in earlier rounds).

## Research and reasoning

Notation as in round 1 (`R_u`: `A_0 = e^{-3pi i u/8} Ã_0`, `A_i = e^{pi i u/8} Ã_i`;
`S_b = -(1/4g^2) Tr[A_mu,A_nu][A^mu,A^nu]`; `I_epsilon[O] = int dA O Pf M e^{i S_b - eps Sum Tr A_mu^2}`;
definition (A), contour class (B), `S_E` the Euclidean action as defined in the 053 block).

**(i)-(iii),(v)-(viii) unchanged from round 1** and gatekeeper-verified in review-r1
("the real-k half of the no-go, the gamma<0/gamma>0 fork, the anti-Wick-slice RHS convergence
statement, the k=0 case, and all byte/anchor/hash mechanics are independently verified and
sound"). With the F3 correction, (iii)'s ray lower bound reads
`|O_k| >= 2 sinh(b_u(rho_hat;k) rho/2) >= (1/2) e^{b_u rho/2}` on the ray (since
`|2 cos(omega/2)|^2 = 4(cos^2(Re omega/2) + sinh^2(Im omega/2))` and `|Im omega| = b_u rho`
on rank-one rays with `Tr H^2 = 1`); divergence of the RHS is unchanged for every nonzero real
`k` and every `k` off the slice, since `e^{b rho/2}` still beats every polynomial in the strip
power count.

**(iv') Corrected commuting-ray model (replaces round-1 (iv); derivation + verification).**
At `u = 0` (Hermitian `A`), take a commuting ray `A_mu = rho_mu H`, `Tr H^2 = 1` (unit ray
direction `rho_hat`, radius `rho`); all commutators vanish so `S_b = 0` exactly, the regulator
is `e^{-c epsilon rho^2/2}` (`c = 1` with `Tr H^2 = 1` normalization; the model keeps a general
`c > 0`), and with `k·rho_hat = kappa = a + ib` (`a = Re(k·rho_hat)`, `b = Im(k·rho_hat)`),
`O_k = 2 cos(kappa rho/2) = e^{i kappa rho/2} + e^{-i kappa rho/2}`. Completing the square,
`± i kappa rho/2 - c epsilon rho^2/2 = -(c epsilon/2)(rho ∓ i kappa/(2 c epsilon))^2
- kappa^2/(8 c epsilon)`, and the branch integrals are exactly

    int_R e^{± i kappa rho/2 - c epsilon rho^2/2} d rho = sqrt(2 pi/(c epsilon)) e^{-kappa^2/(8 c epsilon)},

equal for the two branches (the substitution `rho -> -rho` maps one branch onto the other;
no `kappa -> -kappa` damping is dropped). Hence the branch sum equals
`2 sqrt(2 pi/(c epsilon)) e^{-kappa^2/(8 c epsilon)}` and its modulus is
`2 sqrt(2 pi/(c epsilon)) e^{(b^2 - a^2)/(8 c epsilon)}`, since
`-kappa^2 = -(a^2 - b^2) - 2 i a b`. With polynomial transverse/radial weights `rho^q` the
statement holds up to powers of `epsilon`. Therefore:

- the model grows as `epsilon -> 0+` **iff `b^2 > a^2`**, i.e.
  `|Im(k·rho_hat)| > |Re(k·rho_hat)|` (the two branches can cancel in phase at isolated
  `epsilon`, so the claim is along a sequence; qualifier retained);
- the round-1 condition `(Re k·rho)(Im k·rho) > 0` is **wrong**: it neither implies nor is
  implied by `b^2 > a^2`; e.g. `k = u + i c u` with `0 < |c| < 1` satisfies it on every ray
  while `b^2 - a^2 = (c^2 - 1)(u·rho_hat)^2 < 0` gives decay;
- failure of the growth condition **for every ray**: `exists unit rho_hat with
  (v·rho_hat)^2 > (u·rho_hat)^2` fails for all `rho_hat` iff `vv^T - uu^T <= 0`
  (Rayleigh quotient; `k = u + iv`), which for a difference of two rank-one PSD matrices holds
  iff `v = c u` with `|c| <= 1` (including `v = 0`); on that family the top eigenvalue is
  `(c^2-1)||u||^2 <= 0` and equals 0 exactly on the 9-dimensional orthogonal complement of
  `u`, so there is no strict growth ray. Verified: 500 generic (u,v) in R^10 draws all admit
  growth rays; 500 draws `v = c u, |c| <= 1` all give `lambda_max <= 0`; 500 draws `|c| > 1`
  all give `lambda_max > 0` (`laplace_model_r2.py` (3a)-(3d));
- anti-Wick slice at `u = 0`: slice points are `k^0 = r^0 e^{+3 pi i/8}`,
  `k^i = r^i e^{-pi i/8}`; pure temporal slice points have `v = tan(3 pi/8) u` with
  `tan(3 pi/8) ≈ 2.414 > 1` (growth rays exist), pure spatial ones have
  `|c| = tan(pi/8) ≈ 0.414 < 1` (no growth ray) — matching the gatekeeper's
  `lhs_model.py` observation; generic mixed slice points have `v` not parallel to `u` and
  `lambda_max > 0` (`laplace_model_r2.py` (4a)-(4d)).

The growth statement is a statement of the **commuting-ray model** (the ray is a locus of the
full integral, but a lower bound along a locus does not control the full oscillatory integral
without transverse stationary-phase bounds, which are not supplied). No statement about
`lim I_epsilon[O_k]` is made for any non-real `k`; the manuscript sentence is confined to the
commuting-ray contribution.

**Why the trichotomy is the sharp statement within the class.** For real `k != 0` and
non-real `k` off the slice the RHS divergence (iii) alone kills the identity as a finite
equality, independent of LHS behaviour (gatekeeper: "this half is airtight"). For `k = 0`
053 proves it. For slice `k != 0`: RHS converges (`|O_k| <= 2`, `k < 14` window) and the LHS
limit is undetermined (the ray mechanism for spatial slice points points to model decay;
transverse control is unavailable) — so the membership is genuinely unresolved and the insert
says so.

**Comparison with the original target.** Unchanged from round 1: E's target is untouched; the
no-go is about the observable class in an already-conditional finite-N regulated integral; the
obstruction is located at the massless flat direction; the mass sign is the switch. The slice
(`k != 0` unresolved) is now visibly the only window where a positive (continuation-reading)
outcome could live within this class.

## Claim classification

- (i) fixed-epsilon absolute convergence, entire-in-`k`, fixed-epsilon Stokes for `O_k`,
  `u < 2/3`: **established derivation** (053 estimates extended; gatekeeper-verified).
- (ii) N=2 `Tr e^{iX} = 2 cos(rho_X/2)`, `rho_X^2 = k^mu k^nu G_{mu nu}`, modulus identity:
  **established identity** (sympy `strip_symmetry.py` 1a-1e).
- (iii') ray bound `|O_k| >= 2 sinh(b_u rho/2)` and RHS divergence for every nonzero real `k`
  and every `k` off the slice: **established derivation** (corrected F3; strip power count as
  in round 1, sketch-level at subleading powers — flagged, unchanged) **with numerics as
  corroboration**; RHS convergence on the slice: **conditional** on the 053 `k < 14` window.
- (iv') corrected commuting-ray model: **established within the model** (exact one-dimensional
  Gaussian computation, sympy + mpmath `laplace_model_r2.py` (1),(2); corrected growth
  criterion and failure family established (3),(4)). Its bearing on the full `I_epsilon` is
  **unresolved** (no transverse control; stated as a model claim in the insert).
- (v) domination failure for real `k != 0` at every `u in (0,2/3)`: **established**;
  `e^{c/sqrt(epsilon)}`-type growth of the fixed-epsilon modulus: **numerical**, now scoped
  "on the sampled range" (F6); existence of the real-`k` LHS improper limit: **unresolved**
  (not claimed).
- (vi) gamma<0 extension to all `k in C^10`: **conditional derivation** (chain as in round 1;
  mass-sign identity **established** sympy 4a-4d). (vii) gamma>0 `u=1` divergence at `k=0`
  and CNT definitional scoping: **established within the stated class**. Classicalization
  framing: **input** (cited paper, abstract re-quoted by the gatekeeper).
- Headline trichotomy: **established within the hypothesis class** {N=2; gamma=0; regulator
  (A); contours `R_u`; epsilon->0+ last; `O = Tr e^{ik·A}`} for the two "fails" arms and the
  `k=0` arm; **"unresolved on the slice at `k != 0`" is the honest statement of the open arm**.

## Proposed changes

Two edits, both in `chapters/appH-microscopic-proofs.tex`, Problem E section (after the 053
block, before its Status paragraph). No other file changes; no bib additions (both cite keys
already in `bib/namcg.bib`); no new `\label`s; the only `\ref` used is `ass:lorentzian`
(defined exactly once, checked 1x by `apply_check.py`).

### E1 — pure insert (new paragraph, no text removed)

Anchor (unchanged from round 1; occurrence count 1 re-verified this round in
`apply_check_r2.out`): the CRLFCRLF before `\paragraph{Status.}` + CRLF +
`Remains Assumption~\ref{ass:lorentzian}.` (the bare Status anchor also occurs exactly once).
The paragraph of `appH_insert.tex` is inserted as its own paragraph between that blank line and
the Status paragraph; everything before and after stays byte-identical.

Round-2 insert (LF form, 4572 B, sha256
`69b83c6701983b006e23919fc5d933b5d676af719c84182e516fe7d2970cc50c`;
CRLF form, 4573 B, sha256
`27beeabaed68f7b34a933dc9873761b51ec30c0496254993169dbc294fbb7a81`):

```latex
\emph{Exponential observables \(\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\) at \(N=2\).} Let \(O_k(A)=\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\) with \(k\in\mathbb C^{10}\), at \(\gamma=0\), regulator (A), contours \(\mathcal R_u\) and \(\epsilon\to0^+\) last. For each fixed \(\epsilon>0\) and \(u<2/3\) the integral converges absolutely and is entire in \(k\), because on \(\mathcal R_u\) the growth of \(O_k\) is at most \(\mathrm e^{c(u,k)\|\tilde A\|}\) against a Gaussian regulator, and the fixed-\(\epsilon\) Stokes identity extends to it. At \(N=2\) the matrix \(k^\mu A_\mu\) has eigenvalues \(\pm\rho_X/2\) with \(\rho_X^2=k^\mu k^\nu\mathcal G_{\mu\nu}\), so \(O_k=2\cos(\rho_X/2)\) is branch-independent, and \(|2\cos(\omega/2)|^2=4(\cos^2(\operatorname{Re}\omega/2)+\sinh^2(\operatorname{Im}\omega/2))\). Along rank-one rays \(\tilde A_\mu=\rho_\mu H\), \(\operatorname{Tr}H^2=1\), the Euclidean weight \(\mathrm e^{-S_{\mathrm E}}\) is not exponentially damped and tends to a bounded factor along the corner (\(S_{\mathrm E}\) vanishes on the exact rank-one rays), the Pfaffian vanishes on the ray and is polynomial in the coordinates nearby, and the remaining factors are polynomial (numerical, in a reduced chart), while \(|O_k|\ge 2\sinh\!\bigl(b_u(\hat\rho;k)\rho/2\bigr)\) with \(b_u(\hat\rho;k)=|\operatorname{Im}(k^0\mathrm e^{-3\pi\mathrm iu/8}\hat\rho_0+k^i\mathrm e^{\pi\mathrm iu/8}\hat\rho_i)|\). At every \(u\in(0,1]\) the functional \(\hat\rho\mapsto\operatorname{Im}(k^0\mathrm e^{-3\pi\mathrm iu/8}\hat\rho_0+k^i\mathrm e^{\pi\mathrm iu/8}\hat\rho_i)\) is nonzero for every nonzero real \(k\) (at \(u=1\) its coefficients are \(-\sin(3\pi/8)k^0\) and \(\sin(\pi/8)\vec k\)), so the Euclidean side of the displayed limit identity diverges in modulus for every nonzero real \(k\); more generally it diverges for every \(k\) outside the slice on which \(k^0\mathrm e^{-3\pi\mathrm i/8}\) and all \(k^i\mathrm e^{\pi\mathrm i/8}\) are real, where \(|O_k|\le2\) and that side converges by the \(k<14\) Pfaffian window. For \(\operatorname{Im}k\ne0\) such that some commuting unit \(\hat\rho\) has \(|\operatorname{Im}(k\cdot\hat\rho)|>|\operatorname{Re}(k\cdot\hat\rho)|\), the commuting-ray contribution to the \(u=0\) integral has \(S_{\mathrm b}=0\) and grows along a sequence \(\epsilon\to0^+\) like \(\mathrm e^{c_2(k)/\epsilon}\) with \(c_2(k)>0\) (commuting-ray model; no transverse stationary-phase bound is claimed), and for real \(k\ne0\) the integrand at \(u=0\) carries \(|O_k|\le2\) pointwise, but no fixed-\(u\) domination in \(\epsilon\) is available at any \(u\in(0,2/3)\): the fixed-\(\epsilon\) modulus on \(\mathcal R_u\) grows without bound as \(\epsilon\to0\), numerically like \(\mathrm e^{c(k,u)/\sqrt\epsilon}\) on the sampled range. Hence within the class stated the displayed limit identity fails for every nonzero real \(k\) and for every non-real \(k\) outside the slice on which \(k^0\mathrm e^{-3\pi\mathrm i/8}\) and all \(k^i\mathrm e^{\pi\mathrm i/8}\) are real, holds at \(k=0\), and is unresolved on that slice at \(k\ne0\): there is no analyticity strip and no non-polynomial extension of the limit statement at \(\gamma=0\) off that slice, within the hypothesis class \(N=2\), regulator (A), contours \(\mathcal R_u\), \(\epsilon\to0^+\) last. The obstruction is the massless flat direction, and at fixed \(\gamma<0\) it is absent: the mass contributes on \(\mathcal R_u\) the real exponent \((\gamma/2g_{\mathrm{YM}}^2)[\sin(3\pi u/4)\operatorname{Tr}\tilde A_0^2+\sin(\pi u/4)\sum_{i=1}^{9}\operatorname{Tr}\tilde A_i^2]\), a Gaussian damping on every component that dominates \(\mathrm e^{c(k)\|\tilde A\|}\) uniformly for \(\epsilon\le\epsilon_0<|\gamma|/(2g_{\mathrm{YM}}^2)\), and the displayed limit identity then extends to \(O_k\) for every \(k\in\mathbb C^{10}\) (numerical). At fixed \(\gamma>0\) the \(u=1\) integral diverges in modulus even at \(k=0\) (numerical), so the contour family and the thimbles of~\cite{ChouNishimuraTripathi2025} act on different contour integrals and produce no competing value; the classicalization of~\cite{AsanoNishimuraPiensukYamamori2025} is tied there to a Lorentz-breaking infrared cutoff and bears neither on this paragraph nor on the statements above. Everything in this paragraph is for the hypothesis class stated in it, does not address \(N\to\infty\) taken first, and derives no signature, real-time response, background or continuation; Assumption~\ref{ass:lorentzian} is not discharged. Problem~E remains open and PROGRAMME-CONDITIONAL.
```

The round-2 insert is the round-1 insert with exactly two cluster replacements
(`patch_insert_r2.py`, idempotent; re-run output `patch_insert_r2.out`):

- **OLD_A -> NEW_A** (666 B -> 604 B), the F3+F4 cluster. OLD_A (round-1 text, deleted):
  "Along rank-one rays \(\tilde A_\mu=\rho_\mu H\), \(\operatorname{Tr}H^2=1\), the Euclidean
  weight at \(u=1\) is not exponentially damped and the Pfaffian vanishes on the ray and is
  polynomial in the coordinates nearby, so convergence is governed by powers of the reduced
  variables and the radius: in reduced coordinates the weight is polynomial times
  \(\mathrm e^{-\lambda e_2/2}\) with \(e_2\) bounded along the corner and no other damping
  along it (numerical, reduced coordinates), while \(|O_k|\ge\mathrm e^{b_u(\hat\rho;k)\rho}/4\)
  with \(b_u(\hat\rho;k)=|\operatorname{Im}(k^0\mathrm e^{-3\pi\mathrm iu/8}\hat\rho_0
  +k^i\mathrm e^{\pi\mathrm iu/8}\hat\rho_i)|\)."
  NEW_A = the gatekeeper's corrected snippet (i), except that its pronoun
  "(it vanishes on the exact rank-one rays)" is written
  "(\(S_{\mathrm E}\) vanishes on the exact rank-one rays)" — an explicit-subject clarification
  with identical content (the "it" could read as the weight rather than the action; the weight
  does not vanish). Snippet (i) with exactly this deviation is a byte-exact substring of the
  new insert (checked).
- **OLD_B -> NEW_B** (991 B -> 1261 B), the F1+F2+F6 cluster. OLD_B (round-1 text, deleted):
  "For \(\operatorname{Im}k\ne0\) a commuting ray with
  \((\operatorname{Re}k\cdot\rho)(\operatorname{Im}k\cdot\rho)>0\) has \(S_{\mathrm b}=0\) and
  \(|O_k|\) of order \(\mathrm e^{b\rho}\) with \(b>0\), so the regulated Laplace integral at
  \(u=0\) grows like \(\mathrm e^{c_2(k)/\epsilon}\) along a sequence \(\epsilon\to0^+\), and
  \(I_\epsilon[O_k]\) has no finite \(\epsilon\to0\) limit for non-real \(k\). For real
  \(k\ne0\) the integrand at \(u=0\) carries \(|O_k|\le2\) pointwise, but no fixed-\(u\)
  domination in \(\epsilon\) is available at any \(u\in(0,2/3)\): the fixed-\(\epsilon\)
  modulus on \(\mathcal R_u\) grows without bound as \(\epsilon\to0\), numerically like
  \(\mathrm e^{c(k,u)/\sqrt\epsilon}\). Hence the displayed limit identity holds for \(O_k\)
  exactly at \(k=0\): there is no analyticity strip and no non-polynomial extension of the
  limit statement at \(\gamma=0\), within the hypothesis class \(N=2\), regulator (A),
  contours \(\mathcal R_u\), \(\epsilon\to0^+\) last."
  NEW_B = the gatekeeper's corrected snippet (ii), **byte-exact** (verified substring
  containment of the review's snippet-(ii) line in the new insert; includes the F6 wording "on
  the sampled range").

All bytes outside these two clusters are identical between the round-1 and round-2 inserts
(difflib check; size arithmetic: 4364 LF − 666 + 604 − 991 + 1261 = 4572 LF; CRLF insert 4573
with one line break).

**Archive record (round-1 insert):** `appH_insert.r1.tex`, on-disk CRLF 4365 B, sha256
`b453177e4c649d1c98cb12d11be3f17a4ca78e06d9bc73e6ee89318a3721a284`; LF-normalized 4364 B,
sha256 `52d390c623772453b68f8cf620ae1c727206e21ebf6cbf56fbfb1ac7c8833fcb` — identical to the
round-1 insert recorded in `proposal-r1.md` / `apply_check_r1.out`.

### E2 — unchanged from round 1 (bytes fixed, per "E2 ... can stand")

OLD (exact bytes, occurrence count 1 re-verified; 175 B, sha256
`1ee39123b022a93f7750a9d6cd858a4d9a95a6a2b4ec4cc76310567eef1d181b`):

```latex
or about non-polynomial observables such as \(\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\), which grow on \(\mathcal R_u\), so that the domination above fails for them.
```

NEW = OLD byte-identical + appended sentence (346 B, sha256
`0d51660a0f6cfd15618ca2486171007a9b5830f5b`-prefix `0d51660a0f6cfd8825c292181d7aa9616d9e315618ca2486171007a9b5830f5b`):

```latex
or about non-polynomial observables such as \(\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\), which grow on \(\mathcal R_u\), so that the domination above fails for them. The next paragraph sharpens this at \(N=2\) and \(\gamma=0\): the failure occurs for every nonzero \(k\) in the contour class (B), and it is absent at fixed \(\gamma<0\).
```

(E2 remains accurate for **domination** failure — review-r1 "Scope of what is established"
(d): domination failure at each fixed `u in (0,2/3)` for every nonzero `k`; the slice
degeneracy of the growth functional occurs only at `u = 1`, outside `(0,2/3)`.)

### Stale passages elsewhere

None. The 053 closing exclusion sentence stays true and pointed-to (E2). Chapter 17 needs no
change. The Definition-(C) γ>0 sentence (L1508) stays consistent. The superseded round-1
headline and LHS claims live only in `proposals/` (this package's r1 files), never in the
manuscript, so no manuscript staleness is introduced by the correction.

### Expected applied outputs (pin table)

| file | before | after (CRLF-applied) |
|---|---|---|
| chapters/appH-microscopic-proofs.tex | 532576 B, sha256 `7a75554ef8cb7efe0e4c5cd3c53d6a9c4ffd2a9149e6ff29c7e8e067bb7f6aaa` | **537324 B, sha256 `943816e923a844521faf56fc88774cd0827eca501f69bb7b12dc9f4af18e8571`**, CRLF 3206, bare-LF 0 (= 532576 + 171 + (4573 + 4)) |
| bib/namcg.bib | 25976 B, sha256 `a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b` | unchanged (pin preserved; re-checked True after application) |

The 537324 B / `943816e9...` row was **realized byte-exactly** in the out-of-repo build copy
(`apply_copy_r2.out`).

## Verification scripts

All in this folder, re-runnable with `python -I <script>` (numpy/scipy/sympy/mpmath):

1. `patch_insert_r2.py` (6036 B, sha `02a1b058b093eed3...`) -> `patch_insert_r2.out`: rebuilds
   the round-2 insert from the archived round-1 insert by the two cluster replacements
   (idempotent; re-run reproduced sha `69b83c67...`), asserts absence of `e_2`,
   `\lambda e_2`, "exactly at \(k=0\)", "no finite \(\epsilon\to0\) limit for non-real", and
   presence of the corrected inequality, `2\sinh\!\bigl(b_u...`, `\mathrm e^{-S_{\mathrm E}}`,
   the trichotomy clause, "on the sampled range", the corrected ray condition and the model
   caveat. (`fix63.py`, `fix64.py` were one-shot byte-repair helpers for the patch script; not
   needed for re-verification.)
2. `laplace_model_r2.py` (7945 B, sha `9f255ed24a446737...`) -> `laplace_model_r2.out`
   (OVERALL: ALL CHECKS PASS): (1a) sympy real-`kappa` Gaussian
   `= sqrt(2pi/(c eps)) e^{-kappa^2/(8 c eps)}`; (1b) mpmath quadrature matches at 4 complex
   `kappa = a+ib` samples, both branch signs, max rel err `5.6e-16`; (2) branch sum
   `= 2 sqrt(2pi/(c eps)) e^{(b^2-a^2)/(8c eps)}` (max rel err `4.2e-15`) with monotone
   `eps -> 0` growth iff `b^2 > a^2` for four `(a,b)` cases; (3a)-(3d) failure-set criterion
   `lambda_max(vv^T - uu^T) <= 0` ⟺ no growth ray; generic (u,v) admit growth; family
   `v = c u, |c| <= 1` never does (`lambda_max = 0` on the orthogonal 9-space — the growth
   test is strict positivity); `|c| > 1` always does; (4a)-(4d) slice tangents
   `tan(pi/8) < 1 < tan(3pi/8)`, pure-temporal slice point has growth rays, pure-spatial does
   not, generic mixed slice points do; (5a),(5b) `2 sinh(|y|/2) <= |2 cos((x+iy)/2)|` and the
   modulus identity on a 20000-point grid (relative tolerance); (5c) the superseded
   `e^{b rho}/4` bound violated at `b=0.7, rho=40, x=pi`.
   (Initial run of this script failed three checks due to check-level bugs, not math: a strict
   `< 0` instead of "not > 0" growth criterion at `lambda_max = 0` boundaries, absolute
   tolerances on 1e13-scale values, and dps-30 quadrature cancellation; the fixes are visible
   in the file and all checks then pass. Documented here for transparency.)
3. `strip_symmetry.py` (8701 B after the F5 docstring sign fix, sha `08bc8f61172d7c56...`) ->
   `strip_symmetry.out` re-run **byte-identical** (1478 B, sha `4db24e18...` — same as round
   1; the fix touched only the docstring line "- sin(pi u/4) sum Ai_t^2" -> "+ ...", the code
   predicate was already all-plus).
4. `n2_exp_mech.py` (unchanged) -> `n2_exp_mech.out` re-run **byte-identical** (2085 B, sha
   `b19a134f...` — same as round 1).
5. `apply_check.py` (unchanged) -> `apply_check_r2.out` (report mode): appH pin True
   (532576/`7a75554e...`), bib pin True (25976/`a651fe60...`), E2 OLD count 1, E1 anchor count
   1, insert LF 4572 `69b83c67...` / CRLF 4573 `27beeaba...`, E2 OLD 175 `1ee39123...` /
   NEW 346 `0d51660a...`, both cite keys in bib, `ass:lorentzian` defined 1x, **no labels
   introduced**. `--copy` mode log in `apply_copy_r2.out`: applied to the build copy, applied
   appH 537324 B `943816e9...`, CRLF-only, bib pin re-checked True.
6. `build_check_r2.out`: out-of-repo build `C:/Users/redgi/tmp/p054r2_build_r1` (253 tracked
   files minus proposals/, reports/, scratch/, .claude/), `pdflatex -> bibtex -> pdflatex x3`
   all exit 0: **359 pages**, 2661526 B; final pass: 0 "rerun to get cross-references",
   0 undefined refs/citations, 0 multiply-defined labels, 0 bibtex warnings/errors (a
   "Label(s) may have changed" flag at the third pass cleared on the fourth; the table in
   `build_check_r2.out` records the final pass). NOTE: the copy could not be deleted from
   this session (the sandbox denies recursive deletes: `Bash(rm -rf:*)`); it sits outside the
   repository at `C:/Users/redgi/tmp/p054r2_build_r1` and should be removed by the author or
   orchestrator. Nothing in the repository was touched by the build.

## Decisions Taken

- **F6 taken** ("on the sampled range"): strictly more precise than the round-1 wording, costs
  nothing, and is inside the gatekeeper's own snippet (ii). Rejected: leaving the round-1
  wording (the review's "not required" leaves it optional; precision favours the derivation).
- **S_E pronoun clarification in NEW_A**: the gatekeeper's "(it vanishes ...)" is written
  "(\(S_{\mathrm E}\) vanishes on the exact rank-one rays)". Content identical; the explicit
  subject removes the antecedent ambiguity (the weight `e^{-S_E}` does not vanish; `S_E`
  does). Rejected: verbatim "it" (ambiguity risk in manuscript prose).
- **No transverse stationary-phase bound added** (the alternative F1 fix): not derivable to
  gatekeeper standard within this package; the narrowed model attribution (the gatekeeper's
  own required action) is chosen. Rejected: keeping any `I_epsilon` non-existence claim.
- **E2 kept byte-identical to round 1**: review-r1 confirms it is accurate for domination
  failure (the sense in which it reads); changing it would perturb verified pins.
- **Added `laplace_model_r2.py` with the counterexample/failure-set analysis** rather than
  only spot-checking the corrected claim: the rank-one-PSD characterization
  (`lambda_max <= 0 ⟺ v = c u, |c| <= 1`) makes the corrected condition's exact reach visible,
  including the slice tangents the gatekeeper flagged as decisive.
- **Round-1 decisions carried over unchanged** (no `b^2/(32 epsilon)` constant; "along a
  sequence" qualifier; `ca`-proxy restricted to `eps = gam = 0`; single-paragraph insert with
  one closing status sentence; no SO(10) argument).

## Milestone assessment

Routine. No MILESTONE.md trigger (M1-M5): Problem E stays OPEN/CRITICAL PATH/
PROGRAMME-CONDITIONAL; no critical-path step closes; the package remains a bounded no-go in a
named hypothesis class (now sharper: the anti-Wick slice at `k != 0` is the only unresolved
window inside the class) plus a bounded conditional extension for the massive deformation.
Gatekeeper's round-1 disposition ("no milestone trigger fires") is unchanged by the
corrections.

## Status-label recommendation

Critical-path set re-derived from ch17 and `reports/ledger.md` this round: A, B, C, D1, E, F,
G-derived, N (unchanged). Affected labels: **none**. Problem E remains OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL (the insert states this verbatim). No LABEL-CHANGE-PROPOSED note.

## Author decision needed

None.

## Remaining open step

To close the original target E: nothing here contributes a signature derivation;
`ass:lorentzian` stands. Ranked avenues (round-1 ranking retained; hypothesis each relaxes):

1. **Real-`k` LHS limit, rigorous Abel/Fresnel treatment** (relaxes: presentation/truncation
   of the LHS side). `lim I_epsilon[O_k]` at real `k != 0` is neither shown to exist nor to
   diverge; the exact remaining computation is an improper-limit (stationary-phase/Fresnel)
   analysis on the flat rays. It cannot restore the identity (RHS divergent) but decides
   whether the Lorentzian side carries a finite non-Euclidean value for `Tr e^{ik·A}` —
   directly relevant to the IR two-point programme, since the `k`-expansion of this observable
   generates all polynomial moments. (review-r1's relaxation list ranks first the *non-real
   slice-k* variant of the same computation — transverse stationary-phase control plus
   `u`-uniform domination for `k` on the spatial anti-Wick slice, where the RHS converges and
   the ray model points to decay; this is the corrected package's sharpest positive-outcome
   window and the two items share the required transverse analysis.)
2. **CNT gamma<0 plot reconciliation and gamma>0 thimble mechanism at N=2 with fermions**
   (relaxes: contour class (B) -> thimble class). Comparison requires a shared invariant; none
   exists at gamma>0; the gamma<0 gap (053 L1508) untouched.
3. **Uniform-in-`N` and `N -> infinity`-first statements** (relaxes: `N = 2` and epsilon-last):
   flat commuting rays exist at every N; the Pfaffian-vanishing order needs the N>=3 analogue
   of `Pf = c_P (det G)^4`; the `2 cos` mechanism is N=2-specific (gatekeeper: the general-N
   carrier would be `max |Im eigenvalue(k·A)|`).
4. **Real-time/continuation reading** (relaxes: presentation of the observable sector): the
   053 exclusion sentence "It does not exclude a real-time reading obtained by continuation"
   stays; the corrected trichotomy localizes precisely where such a reading could live
   (slice `k != 0`).
5. **`N >= 3` independent Pfaffian bound** (053's flagged reading-dependency, unchanged).
6. **Alternative presentations relaxing regulator (A)** (e.g. fibre-bounded cone windows of
   Problem F's class damping the flat direction): the obstruction is hypothesis-local at the
   flat direction; not explored — no evidence within (A) that they would change the gamma=0
   divergence, which is also on the Euclidean (RHS) side.
   (review-r1 adds: gamma -> 0- uniformity of the gamma<0 chain, `epsilon_0 -> 0`
   degeneration, as the sharp bridge to the gamma=0 obstruction.)

## Special instructions for the gatekeeper

- **Text identity**: the round-2 insert must be exactly the archived round-1 insert with the
  two cluster replacements OLD_A->NEW_A, OLD_B->NEW_B (byte counts 666->604, 991->1261); NEW_B
  must contain the review-r1 snippet-(ii) line byte-exactly (it does, checked); NEW_A must
  match snippet (i) with exactly the documented `(\(S_{\mathrm E}\) vanishes ...)` deviation
  (checked). Absence checks (`e_2`, `\lambda e_2`, "exactly at \(k=0\)", "no finite
  \(\epsilon\to0\) limit for non-real") are in `patch_insert_r2.py`.
- **Must re-derive** (independent of my scripts): the exact branch Gaussian with the
  `-kappa^2/(8 c epsilon)` exponent and the equal-branch statement (`rho -> -rho`); the
  modulus exponent `(b^2-a^2)/(8c epsilon)`; `|O_k| >= 2 sinh(b_u rho/2)` from
  `|2cos((x+iy)/2)|^2 = 4(cos^2(x/2)+sinh^2(y/2))`; the failure-set criterion
  (`exists unit rho_hat: (v·rho_hat)^2 > (u·rho_hat)^2` fails for all rays ⟺ `vv^T - uu^T <= 0`
  ⟺ `v = c u, |c| <= 1`; note the growth test is strict positivity of `lambda_max`, since on
  the orthogonal complement the Rayleigh quotient is 0, not negative); `tan(pi/8) < 1 <
  tan(3 pi/8)` and the slice-point values `|c| = tan(pi/8)` (spatial), `tan(3 pi/8)`
  (temporal).
- **Must NOT be asserted**: any non-existence or divergence of `lim I_epsilon[O_k]` for
  non-real `k` (or of the slice-`k != 0` membership either way); that commuting-ray growth
  controls the full integral (no transverse bound is claimed); that the identity fails on the
  slice; any rate off the epsilon-sequence; anything about `N -> infinity` taken first,
  signature, real-time response, backgrounds or continuation. The no-go is only for the stated
  hypothesis class; for thimble classes the question is open.
- E2 bytes are unchanged from round 1 (pins `1ee39123...` OLD x1, `0d51660a...` NEW); the
  E2 sentence's "the failure" refers to domination failure (review-r1 established (d)); if
  the integrator prefers, no E2 change is required.
- Build: applied appH 537324 B `943816e9...` realized in the build copy; 359 pages, 0
  undefined/multiply/citations, 0 bibtex issues, no rerun flag on the final pass. The build
  copy `C:/Users/redgi/tmp/p054r2_build_r1` still exists (deletion blocked by sandbox
  `rm -rf` deny) — it is outside the repository and must be removed outside this session.
- Pins are against the working tree (532576 B appH), not HEAD; `dirty-chapters: yes` is the
  expected 052+053 integration state.
