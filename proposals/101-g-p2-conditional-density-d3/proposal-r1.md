# Proposal 101-g-p2-conditional-density-d3, round 1

## Result

For the uniform (Haar) fibre law of the D=3 diagonal-moment problem, the exact conditional
density of the diagonal $d=(d_1,d_2,d_3)$ of $U\Lambda U^\dagger$ given the spectrum
$\Lambda=\mathrm{diag}(\lambda_1,\lambda_2,\lambda_3)$, $\lambda_1>\lambda_2>\lambda_3$,
$\sum_i\lambda_i=1$, is derived (as a signed sum of hinge functions over $S_3$, the type-A$_2$
Kostant/Duistermaat--Heckman shape) and integrated **exactly in rationals** at two explicit
spectra: $Z=3/200$ at $\lambda=(0.6,0.3,0.1)$ and $Z=117/4000$ at $\lambda=(0.7,0.25,0.05)$,
both equal to $\tfrac12\prod_{i<j}(\lambda_i-\lambda_j)$; $\mathbb{E}\,d_i=1/3$ and
$\mathbb{E}\,P_2=(1+\sum_i\lambda_i^2)/4$ hold exactly at both. Pushing forward by
$P_2=\sum_i d_i^2$ gives the exact one-dimensional density $f_{P_2}$ via the coarea formula
over the ellipse $P_2-1/3=3a^2+b^2$; at $\lambda=(0.6,0.3,0.1)$ it is the constant
$40\pi/(3\sqrt3)$ on $[1/3,67/200]$, smooth on $(67/200,17/50)$ and $(17/50,23/50)$, and zero
beyond $23/50=\sum_i\lambda_i^2$. The exact curve matches a 3-million-sample Haar histogram at
$|z|\le1.83$ (25 bins), the 2-D density matches at correlation $0.9967$ (3M) and $0.9902$
(800k, second spectrum), and the Laplace transform of the density equals the
Harish--Chandra/Itzykson--Zuber determinant to relative $1.65\cdot10^{-16}$. This sharpens the
G.moments fibre-side bookkeeping; it closes nothing in Problem G. $D>3$ and the exact
profile-tilted conditional density remain unresolved.

## Target and status

- Problem: G (HBEV), `chapters/appH-microscopic-proofs.tex`, `\section{Problem G: HBEV}`,
  `\label{sec:status-G}`. Live ledger text (read 2026-11-19): "Status: OPEN. Priority:
  CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and
  G-external support at most a scope-limited model; G remains OPEN and neither satisfies the
  matrix-derived criterion."
- Original target of Problem G: derivation of the infrared entropy density and stationarity
  from the matrix theory (mechanism CLOSED CONDITIONALLY under a stated boundary entropy; the
  derivation itself OPEN). Unchanged by this package.
- This package's target: the exact conditional density of the diagonal moment $P_2$ under the
  profile/fibre law at D=3 (uniform fibre law), by hand from the 096 patch-Jacobian fibre
  picture, with validity domain and independent numeric validation. Dependency: none of the
  unresolved critical-path inputs (A--N) is assumed; it uses only Haar geometry on the fibre.
- Classification: this is a derived conditional law *for the uniform fibre model* (a
  consistency/sharpening package for the fibre side). It does not supply a state-side profile
  weight and is PROGRAMME-CONDITIONAL with respect to Problem G; nothing is closed.

## Source reading

digest + targeted reads. Targeted reads: Problem G ledger opening (live file lines 3022--3040),
the anchor seam in the G.moments ledger block, `reports/ledger.md` Problem G entries, prior
proposals 096/098/099/100 fibre-marginal results referenced by number only where their scripts
were re-checked. No chapters/ file was modified. Digest status: assumed current per orchestrator
run state; not re-run by this agent (read-only role).

## Research and reasoning

**Ansatz (conditional).** For Haar $U\in\mathrm U(3)$ the conditional density of $(d_1,d_2)$
is claimed to be $\widehat\rho(d)=Z(\lambda)^{-1}\sum_{w\in S_3}\varepsilon(w)\,
k(\lambda_{w(1)}-d_1,\lambda_{w(2)}-d_2)$ with $k(g_1,g_2)=\min(g_1,g_1+g_2)$ when
$g_1>0,g_1+g_2>0$, else $0$. This is the type-A$_2$ Kostant/Duistermaat--Heckman density
summed over the Weyl group; the literature proof was NOT independently verified, so the package
does not rely on it: every structural property (support = permutahedron
$\{\lambda_3\le d_i\le\lambda_1\}$, piecewise linearity, kink lines $d_i=\lambda_a$) is checked
here by brute force on the 9-line wall arrangement (exact101b.py: 512 sign patterns, wall-line
membership of all kinks), and all normalizations/moments are recomputed from scratch from the
piecewise formula (exact103/103b). The formula is also verified pointwise against 3M-sample and
800k-sample Haar Monte Carlo (sym101, mc101d).

**Exact integration.** The wall arrangement of the three lines $d_i=\lambda_a$ cuts the
permutahedron (hexagon, area $37/200$ at spectrum 1) into 7 cells with signed densities
affine on each cell (barycentric values from the vertices). Integrals use the exact barycentric
monomial rule $\int_T L_0^aL_1^bL_2^c\,dA=2A\,a!b!c!/(2+a+b+c)!$ on a fan triangulation
(exact103.py; a midpoint-rule attempt failed for affine-times-quadratic integrands and was
discarded -- see exact102 lineage). This gives $Z$, $\mathbb E d_i$, $\mathbb E P_2$ as exact
Fractions (Result section above). $\mathbb E P_2=(1+\sum\lambda^2)/4$ agrees with the
integrated 098-type second-moment identity at both spectra; the same marginal is also cross-checked against the integrated 096 marginal by Monte Carlo (mc101b.py: max z = 1.43 over the d1 marginal bins).
**Pushforward to $P_2$ (established derivation).** With $u_i=d_i-1/3$ and eigen-coordinates
$a=(u_1+u_2)/\sqrt2$, $b=(u_1-u_2)/\sqrt2$, one has with $\sum_i u_i=0$ on the trace plane and
$P_2-1/3=3a^2+b^2=:Q$ (verified symbolically). Level sets are ellipses; the coarea formula gives
$f_{P_2}(P_2)=\int dl/|\nabla Q|=\,(2\sqrt3)^{-1}\int_0^{2\pi}\widehat\rho(\tfrac13+u(\theta))\,d\theta$
with $u_1(\theta)=(s\cos\theta/\sqrt3+s\sin\theta)/\sqrt2$,
$u_2(\theta)=(s\cos\theta/\sqrt3-s\sin\theta)/\sqrt2$, $s^2=P_2-1/3$; The Jacobian identity $dl/|\nabla Q|=d\theta/(2\sqrt3)$ is checked symbolically in jac101b.py: on the level curve $a(\theta)=c\cos\theta/\sqrt3$, $b(\theta)=c\sin\theta$ the plane speed is $c\sqrt{\cos^2\theta+\sin^2\theta/3}$ and $|\nabla Q|=2c\sqrt{3\cos^2\theta+\sin^2\theta}$, ratio exactly $\sqrt3/6=1/(2\sqrt3)$; also $3a^2+b^2=\sum_i u_i^2$ on the trace plane (sympy, assert-guarded). The ellipse is inscribed in the central triangle $\{(0.3,0.3),(0.3,0.4),(0.4,0.3)\}$
(area $1/200$, $\widehat\rho\equiv1/5$ there) until its maximal coordinate excursion
$\sqrt{2Q/3}$ reaches the triangle edges, i.e. up to $Q=1/600$, $P_2=67/200$ (Cauchy--Schwarz
max on the ellipse: derived); hence the exact plateau $f=2\pi\cdot(1/5)/(2\sqrt3)\cdot
\rho\text{-normalization}=40\pi/(3\sqrt3)\approx24.184$ on $[1/3,67/200]$ (endpoint value in
num104b.out matches $24.183992$). Breakpoints: $Q=1/150$ ($P_2=17/50$, ellipse through the
central-triangle vertices) and $P_2=23/50=\sum\lambda_i^2$ (hexagon vertices, ellipse through
support corners), verified numerically (exact101b.out breakpoints $1/150$, $19/150$). Near the
endpoint $f\sim C(23/50-P_2)^2$ (bin-centre bias of raw histograms against the point value
explains an earlier apparent excess; resolved by comparing to bin-averaged exact densities,
which is the num104b comparison at $|z|\le1.83$).

**Laplace transform (established numerically).** $\int e^{s\cdot d}\widehat\rho\,dd/Z =
\det(e^{a_i\lambda_j})_{1\le i,j\le3}/(2\,\Delta(a)\Delta(\lambda))$ at $a=(s_1,s_2,0)$ checked
at 5 points to max relative $1.65\cdot10^{-16}$, including the normalization ($Z$ from
quadrature vs $3/200$, rel $2.3\cdot10^{-16}$) (hciz101.py, mpmath 50-digit). This is the $2=(3-1)!$-normalized
Itzykson--Zuber/Harish--Chandra integral; as with the density ansatz, the general literature
proof is not imported as a proof here -- the identity is verified to machine precision for the
two displayed spectra, and the insert says so.

**Validity domain.** Strictly ordered distinct $\lambda$; trace normalized to 1; the uniform
fibre law only. Degenerate limits ($\lambda_i\to\lambda_j$) and the $D\to\infty$ scaling of the
arrangement cell count are NOT analyzed here. $Z(\lambda)=\Delta(\lambda)/2$ is verified at two
spectra (an observed pattern, not a derived general-$\lambda$ theorem in this package).

**Profile class.** Under bounded profile-class reweightings of the fibre law only a
bounded-Radon--Nikodym comparison of conditional densities is available (the tilt is bounded on
the fibre for bounded profile weights); the exact tilted density was NOT computed. The general
$D>3$ conditional density is unresolved even for the uniform fibre law.

**Failed/superseded routes (recorded so the gatekeeper can skip them).** mid-point-rule moments
(wrong for affine x quadratic), first MC draft with $d=1-\sum_i|U_{ui}|^2\cdot(\dots)$ identity
bug, duplicate-bin-edge nan histograms, first-principles angle parametrization of the fibre
(abandoned as intractable), endpoint-fit drafts. All lineage files are marked in manifest.md.

## Claim classification

- Kostant-sum shape of $\widehat\rho$: **conditional** (identified with the established
  DH/Kostant A$_2$ density; literature proof not independently verified); treated in this
  package as an ansatz verified by exact checks below.
- Support = permutahedron, piecewise linearity, kink-line bookkeeping: **established** for the
  two displayed spectra by exhaustive arrangement check (exact101b.py).
- $Z=3/200$, $Z=117/4000$, $\mathbb E d_i=1/3$, $\mathbb E P_2=(1+\sum\lambda^2)/4$ at both
  spectra, plateau value $40\pi/(3\sqrt3)$, breakpoints $17/50$, $23/50$, coarea Jacobian
  $d\theta/(2\sqrt3)$: **established derivations** (exact rational or symbolic, scripts
  re-runnable).
- $Z(\lambda)=\Delta(\lambda)/2$ for general $\lambda$: **unresolved pattern** (verified at two
  spectra only).
- HCIZ determinant identity at the displayed spectra: **established to $1.65\cdot10^{-16}$
  numerically** (not an independent proof of the general formula).
- MC agreements (corr 0.9967 / 0.9902, $|z|\le1.83$, marginal $z=1.43$): **established
  numerical checks** (fixed seeds).
- Profile-class tilt: **conjecture/mechanism statement** limited to the bounded-RN comparison;
  exact tilted density **unresolved**. General D: **unresolved**.
- Input: none beyond the fibre-law definition; $(1+\sum\lambda^2)/4$ is derived here, not
  imported.
## Proposed changes

Single file: `chapters/appH-microscopic-proofs.tex`. One insertion, no deletions, no edits to
existing sentences or equations.

- **Anchor.** The unique occurrence of the byte sequence
  `close nothing in Problem~G.` + CRLF + CRLF + `\emph{Vacuum term.}` (verified count 1 in the
  live file; the other 25 occurrences of the idiom `close nothing in Problem~G.` do not precede
  `\emph{Vacuum term.}` at this seam). Boundary: the paragraph ending "...and they close
  nothing in Problem~G." and the paragraph beginning `\emph{Vacuum term.}` both stay verbatim;
  the insert becomes a new paragraph between them, separated by a blank line on both sides.
- **Splice rule (exact, as simulated in simulate_apply_101c.py):** at byte position
  `pos = find(anchor) + len("close nothing in Problem~G.\r\n\r\n")`, insert the 2686 bytes of
  `insert-r1.tex` followed by one additional CRLF.
- **PRE contract (live, verified 2026-11-19):** appH 795,607 B, sha256 `3f1b030cf81d...`,
  CRLF 3864, bare LF 0, idiom count 26, `\emph{Vacuum term.}` count 2.
- **POST contract (measured by simulation):** 798,295 B, sha256
  `000dbd83671676c8d7f6f324b09c1ffde6ca9e8bc2c3ec4f3002820b2ceb814b`, CRLF 3866, bare LF 0,
  idiom count 27, `\emph{Vacuum term.}` count 2, bytes outside the splice interval unchanged.
- **The inserted paragraph** is `insert-r1.tex` (2686 B, sha256
  `6bf81c473c453198884f33b93da6d9a22da9c24401d3dd486cc7d0965d2f411b`), a single line, ASCII,
  no `\ref`/`\cite`, no square brackets, no status/priority words, closing with the established
  idiom "...identify no state-side profile weight and close nothing in Problem~G." It states the
  formula, the two exact spectra, the moments, the coarea pushforward with plateau and
  breakpoints, the HCIZ identity with its explicit "not independently verified" caveat, and the
  honest D>3 / profile-class limitations.
- **Stale passages elsewhere:** none identified. The existing G.moments ledger text makes no
  claim contradicted by this package.

## Verification scripts

All in this folder; run with `python -I <script>` from the folder. Reproduction pack (expected
invariants; scripts are deterministic -- fixed seeds, exact arithmetic):

| command | expected invariant output |
|---|---|
| `python -I gen_insert_101.py` | `insert-r1.tex bytes: 2686 sha256: 6bf81c47...411b` |
| `python -I hygiene_101.py` | `ALL PASS` |
| `python -I simulate_apply_101c.py` | 10 x PASS, `POST sha256: 000dbd83...814b`, `no write performed` |
| `python -I exact103.py` | `Z = 3/200`, `E[d1] = 1/3`, `E[sum d^2] = 73/200` |
| `python -I exact103b.py` | `Z = 117/4000`, `E[d1] = 1/3`, `E[sum d^2] = 311/800` |
| `python -I exact101b.py` | 7 cells, `rho(centroid) = 1/5`, breakpoints `1/150`, `19/150` |
| `python -I hciz101.py` | `max rel HCIZ mismatch = 1.65e-16`, `Z(quad) ... rel 2.3e-16` |
| `python -I jac101b.py` | `speed/|grad Q| = sqrt(3)/6 ... diff 0`, `JACOBIAN CHECK PASS` |
| `python -I num104b.py` | `max |z| = 1.83` (seed 101202611, N=3M, bin-averaged exact f) |
| `python -I mc101d.py` | `shape corr: 0.9902`, `trapz ... 1.00000`, `E[P2] = 0.388732` |
| `python -I mc101b.py` | `max z = 1.43` |
| `python -I sym101.py` | `shape corr on MC support (mode0): 0.9967` |

`manifest.md` (regenerate with `python -I gen_manifest_101.py`) lists every file with bytes and
full sha256 and marks the BROKEN/SUPERSEDED lineage (exact101/102, num101-104, mc101a/c,
fit101*, sym102/103, simulate_apply_101/101b, jac101.py: jac101.py records the wrong
3-component-gradient check and must fail its assert; jac101b.py is the corrected check). The
`simulate_apply_101b.out` FAIL line is a checker slicing bug (2-byte slice for a 4-byte
pattern), documented; the splice itself is correct in `_101c`.
## Decisions Taken

- **Ansatz + exact-verification route** for the conditional density, rather than a
  first-principles angular/sector parametrization of the fibre (rejected: intractable at 6x6
  Jacobians without new input; the Kostant-sum shape is checkable exactly and every
  normalizing consequence is recomputed here from the formula).
- **Two explicit spectra verified exactly** ((0.6,0.3,0.1) and (0.7,0.25,0.05)) instead of a
  general-symbolic run, to support "at both spectra" claims while keeping the general-lambda
  statement honest; the insert therefore states Z=Delta(lambda)/2 only as the two-spectrum fact
  plus display, not a general theorem.
- **Bin-averaged exact density vs raw MC bins** (num104b) after identifying that raw bin-centre
  comparison against a convex endpoint is biased (earlier |z|=5.5 artifact); the corrected
  comparison gives |z|<=1.83.
- **Splice after the double CRLF with one added CRLF** (simulate_apply_101c), so the new
  paragraph is blank-line separated from BOTH neighbours; the earlier one-sided splice
  (simulate_apply_101) is kept as documented failure lineage.
- **General-D and tilted-density statements left explicitly unresolved**; no profile weight is
  asserted anywhere in the insert. General lambda Z=Delta(lambda)/2 stated as verified pattern.
- Stale print labels in exact103b.py fixed (values unchanged); num104b.out, exact103b.out,
  mc101b.out, sym101.out regenerated from the current scripts so every shipped .out matches its
  script.

## Milestone assessment

Routine. No milestone trigger applies: this is a fibre-side exactness/consistency package that
sharpens G.moments bookkeeping (Problem G stays OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL).

## Status-label recommendation

Critical-path list re-derived from the live ledger: A, B, C, D1, E, F, G-derived, N remain as
recorded in Chapter 17 / Appendix H; Problem G ledger unchanged. All labels: **unchanged** by
this package.

## Author decision needed

none

## Remaining open step

To close Problem G one still needs the infrared entropy density and stationarity derived from
the matrix theory (unchanged original target). Within this package's scope the remaining steps
are: (i) a proof (or derivation) of $Z(\lambda)=\Delta(\lambda)/2$ for general strictly ordered
$\lambda$; (ii) the exact tilted conditional density under bounded profile weights (beyond the
bounded-Radon--Nikodym comparison); (iii) the $D>3$ conditional density of $P_2$ for the
uniform fibre law; (iv) a derivation (not just a machine-precision identity) of the
DH/Kostant density formula at A$_2$ from the fibre Jacobian of 096.

## Special instructions for the gatekeeper

- Do NOT accept any assertion that DH/Kostant/IZ literature proves the ansatz: the insert says
  "whose proof in the literature we have not independently verified"; the package's strength is
  the exact checks. If you can verify arXiv/DOI records for DH or Kostant convexity or IZ
  yourself, record it, but the insert text must not change to import them as proofs.
- Do not read "close nothing in Problem~G" as anything but non-closure; assert no status change.
- Re-run the full reproduction table; the MC scripts are seed-fixed so numbers must match
  exactly (1.83, 0.9902, 0.9967, 1.43) up to float formatting.
- Verify the splice yourself: read `chapters/appH-microscopic-proofs.tex` bytes, apply
  `pre[:pos] + ins + b"\r\n" + pre[pos:]` with the anchor rule above, and check sha256
  `000dbd83671676c8d7f6f324b09c1ffde6ca9e8bc2c3ec4f3002820b2ceb814b`. Never write chapters/.
- `jac101.py` failing is expected (lineage of the 3-component-gradient error); `jac101b.py` is
  the shipped check.
- Scope limit for the review: the general-lambda formula is an ansatz-with-exact-checks; any
  wording upgrade beyond the insert's current text is out of scope for this round.
