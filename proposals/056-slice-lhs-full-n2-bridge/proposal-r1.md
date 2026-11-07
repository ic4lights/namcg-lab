# Proposal 056-slice-lhs-full-n2-bridge, round 1

## Result
Package: "The two-regulator Stokes bridge to the anti-Wick-slice insertion at full N=2: exact Stokes
band, convergent damped family, and a bounded obstruction to modulus-based linking."
(1) Established: for slice data (k^0 e^{-3pi i/8}, k^i e^{pi i/8} real) the insertion satisfies
|O_k| <= 2 on the final contour R_1 (the contraction k^mu A_mu(1) = r^mu Atilde_mu is Hermitian;
rho_X^2 = sum_a (r^mu Atilde^a_mu)^2 >= 0, verified matrix-side vs contraction-side, bridge_r1.py SEC 2),
so the established k<14 window majorant applies verbatim with the k=0 majorant 2|Pf|e^{-c S_E}.
(2) Established: inserting the auxiliary delta factor with delta = lambda*eps, the total quadratic
damping along the slide R_theta, theta in [u,1], is, per unit eps in the temporal direction,
c_0(theta) = cos(3 pi theta/4) + lambda cos(3 pi (2theta-1)/8), and per unit eps in the spatial
direction c_1(theta) = cos(pi theta/4) + lambda cos(pi (2theta-1)/8) > 0 for all lambda >= 0, theta.
The ratio -cos(3 pi theta/4)/cos(3 pi (2theta-1)/8) is strictly increasing on [0,1] (its derivative is
exactly (3 pi/4) sin(3 pi/8) cos(3 pi(2theta-1)/8)^{-2} > 0, verified symbolically to simplify to 0)
with supremum at theta=1 equal to lambda_* = sqrt(2+sqrt2) = 1.8477590650225735. Hence uniform strict
Stokes damping on the whole slide holds iff delta > lambda_* eps (link_r1.py SEC A).
(3) Established (conditional on the chain legs of the 053 displayed limit identity): for every fixed
lambda > lambda_* the delta-damped family at u=1 converges to the RHS of the displayed identity by
dominated convergence with the window majorant (the O(eps) anti-damping e^{+|cos(3pi/4)|eps rho^2} at
u=1 is dominated quartically by e^{-S_E} uniformly in eps, link_r1.py SEC D).
(4) Bounded obstruction (core of the package): no modulus (absolute-value) two-regulator bridge can
establish the displayed identity for the UNDAMPED slice insertion at r^0 != 0 at N=2. Any linking bound
|I_eps - J_{eps,delta}| <= delta * M_u(eps) requires delta*M_u(eps) -> 0, but the rank-one corner chart
(Atilde_0 = rho H, Tr H^2 = 1, transverse scale c_1 sqrt(eps) so all quartic and Pfaffian pieces are
O(1)) gives |O_k| >= e^{b_u rho/2}/(2 sqrt2), b_u = sin(3 pi(1-u)/8)|r^0| > 0 for u < 1, against
regulator damping eps cos(3 pi u/4) rho^2, so M_u(eps) >= e^{c_0(u)/eps}/poly with
c_0(u) = sin^2(3 pi(1-u)/8)(r^0)^2 / (16 cos(3 pi u/4)) > 0 for u < 2/3 (c_0(0.3) = 0.0443 at r^0=1);
for u >= 2/3 the regulator is non-damping in the temporal direction and M_u(eps) = infinity outright.
The required linking band delta <= poly*exp(-c_0(u)/eps) is incompatible with the Stokes band
delta >= lambda_* eps (empty for eps <= 0.015 at u=0.3, link_r1.py SEC C). On the flat Minkowski
contour the same failure occurs: |O_k| <= e^{c(k) rho} there (it is bounded ONLY at u=1), so the
delta-removal error on the flat side grows like e^{c(k)^2/(4 eps)} and no rate delta(eps) removes the
delta factor in modulus. The exact 1D branch model makes the failure explicit: |I| ~ e^{sqrt2/(32 eps)}/
sqrt(eps) while |J|/|I| -> 0, so |I - J|/|I| -> 1 (link_r1.py SEC B). This also covers the fixed
gamma<0 mass bridge at u=0 (mass real part vanishes at u=0; 055) and every contour slide inside the
R_u family. It does NOT refute the identity: it bounds the strategy class "modulus-controlled
two-regulator/contour bridging" for regulator (A), gamma=0, slice k with r^0 != 0, N=2.

## Target and status
Problem E (Lorentzian signature, Assumption ass:lorentzian), Appendix H: status "Remains
Assumption~\ref{ass:lorentzian}", CRITICAL PATH, PROGRAMME-CONDITIONAL in the full-GR scope
(ch17-agenda). Original target: derive the Lorentzian-signature limit identity of appH L1502-1505 for
the physically relevant (non-polynomial) slice insertions at N=2, i.e. close the 054 trichotomy case
"unresolved on that slice at k != 0". Dependencies: 053 displayed identity (polynomial k<14), 054
trichotomy, 055 slice modulus facts. DERIVED-ness: nothing closes; the package narrows the open step.

## Source reading
digest + targeted reads. Pins re-verified this round: chapters/appH-microscopic-proofs.tex 540349 B,
sha256 5766105967f830ae8817cc50636d881315ddaa62070e5dfd875727b675fc4cce, CRLF 3209, bare-LF 0;
bib/namcg.bib 25976 B sha a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b. Read:
appH Problem E block (L1490-1519), ch17-agenda L375-414/L695-739, reports/ledger.md (055 entry),
proposals/055-*/review-r2.md (ACCEPT, ranked avenues), proposals/055-*/proposal-r2.md and its scripts,
reports/sme-scout-20261106-2023.md.

## Research and reasoning
Notation follows 053/055: A_0(theta) = e^{-3 pi i theta/8} Atilde_0, A_i(theta) = e^{pi i theta/8}
Atilde_i; regulator (A) contributes Re(-eps sum A_mu A_mu) = -eps[cos(3 pi theta/4) Atilde_0^2 +
cos(pi theta/4) sum Atilde_i^2]; auxiliary delta factor exp(-delta[e^{3 pi i/8} Tr A_0^2 +
e^{-pi i/8} sum Tr A_i^2]) with, on R_theta, Re e^{3 pi i/8} A_0(theta)^2 = cos(3 pi(2theta-1)/8) and
Re e^{-pi i/8} A_i(theta)^2 = cos(pi(2theta-1)/8) (both re-derived symbolically; note this CONFIRMS
the 053 sentence that the delta exponent has negative real part on the contours - an earlier suspicion
of a phase error in 053 was my own slip and is withdrawn).
(2a) Stokes band. c_0(theta;lambda) < 0 iff lambda > ratio(theta); derivative identity above gives
sup at theta=1: lambda_* = -cos(3pi/4)/cos(3pi/8) = sqrt(2+sqrt2) (closed form confirmed by
nsimplify; numeric min c_0 at lambda_* -/+ 1e-9 flips sign at +/-3.8e-10, link_r1.py SEC A).
(2b) Positive family. At u=1, delta = lambda eps with lambda > lambda_*: net quadratic coefficient
cos(3pi/4) + lambda cos(3pi/8) (sign flips exactly at lambda_*); e^{-S_E} quartic domination gives the
uniform L^1 majorant e^{-S_E/2 + C(eps_0)} * 2|Pf| * poly, inside the k<14 window (k=2 effective),
hence J_{eps,lambda eps}^{(1)} -> RHS.
(2c) Corner lower bound. On R_u, u < 2/3, the chart Atilde_0 = rho H with |Atilde_i| ~ c_1 sqrt(eps)
keeps quartic S_E pieces O(1); slice k: rho_X = e^{3 pi i(1-u)/8} r^0 rho + O(c_1 sqrt(eps));
|2cos(z/2)| >= e^{|Im z|/2}/(2 sqrt2) for |Im z| >= 2 gives |O_k| >= e^{b_u rho/2}/(2 sqrt2) on that
chart; maximizing b_u rho/2 - eps cos(3 pi u/4) rho^2 gives the e^{c_0(u)/eps} lower bound. For
u >= 2/3 the Atilde_0 quadratic is anti-damping: M_u(eps) = infinity.
(2d) Flat side. On the original flat contour e^{iS_b} has modulus 1 and |O_k| ~ e^{c(k) rho}; the
delta-linking error bound grows as e^{c(k)^2/(4eps)}; DCT in delta with the eps-regulator majorant
holds only at FIXED eps (finite bound), but with delta = lambda eps simultaneously -> 0 the product
lambda eps * e^{c^2/(4eps)} diverges. Hence both modulus removals of the delta factor fail.
Literature: no external import used; no citations added. Nothing cited unverified.

## Claim classification
- |O_k| <= 2 at R_1 for slice k; rho_X^2 = sum (r.Atilde)^2: established identity (script-verified).
- Stokes band delta > sqrt(2+sqrt2) eps, monotone-ratio lemma: established derivation.
- Damped family (fixed lambda > lambda_*) converges to RHS at u=1: conditional result (relies on the
  established 053 chain legs for the damped family and the k<14 window at L1500).
- M_u(eps) >= e^{c_0(u)/eps}/poly for u < 2/3; M_u = infinity for u >= 2/3; flat-side growth
  e^{c(k)^2/(4eps)}: established derivation (chart-level; constants script-reproduced).
- Exact 1D model I, J closed forms: established (model).
- "No modulus two-regulator bridge exists for slice k, r^0 != 0": bounded no-go, exact hypothesis
  class: regulator (A), gamma=0, N=2, contour family R_u, linking by absolute-value estimates.
- Whether an oscillation-based (non-modulus) link exists: unresolved step. The identity itself on the
  slice at k != 0: unresolved (as in 054).

## Proposed changes
File: chapters/appH-microscopic-proofs.tex. Anchor (unique; verified once in the current file): the
block "\r\n\r\n\r\n\r\n\paragraph{Status.}\r\nRemains Assumption~\ref{ass:lorentzian}." (the only other
"Remains Assumption" occurrence carries \ref{ass:EFT-a2}). Insert one \paragraph immediately BEFORE
that anchor block, after the 055 paragraph: replace the first occurrence of the anchor with
"\r\n\r\n" + T_CRLF + anchor, where T is the single line below plus a trailing newline. Nothing is
removed; all 053/054/055 paragraphs and the Status block stay byte-identical. No \ref or \cite added
(no new labels; duplicate-label check not needed). CRLF counts after apply: 3209 + (LF count in T = 1)
+ 4 (the "\r\n\r\n" separator contributes 2 CRLF; total inserted CRLF = 6... integrator: expected
applied size 540349 + 4 + (len(line)+2), bare-LF 0. T (ASCII, one line):

```latex
\paragraph{Slice bridge band and modulus obstruction.} For slice data, i.e.\ $k^\mu$ with
$k^0 e^{-3\pi i/8}$ and $k^i e^{\pi i/8}$ real, the insertion is bounded on the final contour,
$|O_k|\le 2$, since $k^\mu A_\mu$ there is Hermitian and $\rho_X^2=\sum_a(k\cdot\widetilde A^a)^2\ge
0$, so the $k<14$ window majorant applies with the $k=0$ majorant. With the auxiliary factor at
$\delta=\lambda\varepsilon$, the quadratic damping along $R_\theta$, $\theta\in[u,1]$, is strictly
positive on the whole slide if and only if $\delta>\lambda_*\varepsilon$,
$\lambda_*=\sqrt{2+\sqrt2}$: the spatial coefficient stays positive for all $\delta\ge0$ and the
temporal ratio $-\cos(3\pi\theta/4)/\cos(3\pi(2\theta-1)/8)$ is strictly increasing with supremum
$\lambda_*$ at $\theta=1$. For each fixed $\lambda>\lambda_*$ the damped family at $u=1$ converges to
the right-hand side by dominated convergence within the window. Removing the auxiliary factor from
either undamped side in modulus fails: on the rank-one corner $\widetilde A_0=\rho H$ with transverse
scale $O(\sqrt\varepsilon)$, $|O_k|\ge e^{b_u\rho/2}/(2\sqrt2)$, $b_u=\sin(3\pi(1-u)/8)|r^0|>0$ for
$u<1$, against regulator damping $\varepsilon\cos(3\pi u/4)\rho^2$, so the modulus integral obeys
$M_u(\varepsilon)\ge e^{c_0(u)/\varepsilon}/\mathrm{poly}$, $c_0(u)=\sin^2(3\pi(1-u)/8)(r^0)^2/
(16\cos(3\pi u/4))>0$ for $u<2/3$, and diverges for $u\ge 2/3$; on the flat contour $|O_k|$ grows like
$e^{c(k)\rho}$ and the corresponding bound grows like $e^{c(k)^2/(4\varepsilon)}$. The linking band
$\delta\le\mathrm{poly}\cdot e^{-c_0(u)/\varepsilon}$ is therefore incompatible with the Stokes band
$\delta\ge\lambda_*\varepsilon$, and no rate $\delta(\varepsilon)$, no fixed negative mass at $u=0$,
and no slide within the family $R_u$ bridges the undamped slice insertion by modulus estimates at
$N=2$. The displayed limit identity remains unresolved on the anti-Wick slice at $k\ne0$ beyond such
bridges; closing it requires non-modulus (oscillation-based) estimates or an independent mechanism.
Problem~E remains open and PROGRAMME-CONDITIONAL.
```
(On disk: LF in the proposal file; integrator normalizes to CRLF. Verify pins unchanged elsewhere.)
Stale passages: none; 054's "unresolved on that slice at k != 0" stays accurate.

## Verification scripts
proposals/056-slice-lhs-full-n2-bridge/bridge_r1.py + bridge_r1.out (SEC 1 contour real parts incl.
delta-factor phases; SEC 2 slice rho_X^2 matrix-vs-contraction identity, real >= 0 asserted, off-slice
contrast; SEC 3 ray lower bound and 2cosh envelope; SEC 4 055 branch closed form vs 60-term series,
growth/saturation constants reproduce the merged text; SEC 5 damped/undamped ratios).
proposals/056-slice-lhs-full-n2-bridge/link_r1.py + link_r1.out (SEC A exact lambda_* monotone-ratio
identity; SEC B exact 1D model |1-J/I| -> 1; SEC C c_0(u) table and band-incompatibility table;
SEC D u=1 net damping flip at lambda_* and quartic-domination constant).
NOT RUN this round (run-interrupted): apply_check.py and the out-of-repo build at
C:/Users/redgi/tmp/056_apply_r1. Procedure pinned above (anchor count 1; expected applied size
540349 + 6 + len(line); then pdflatex, bibtex namcg-book7, pdflatex, pdflatex; never build in-repo).

## Decisions Taken
- Chose the two-regulator-bridge analysis (055 avenue 1/3 hybrid) as the single package over the
  gamma->0^- mass route (already covered by the same obstruction at u=0: mass Re part vanishes) and
  over a pure r^0=0 sub-window (an earlier hope that the window majorant closes u<1 at r^0=0 is false:
  |O_k| still grows like e^{c rho} off R_1 even for purely spatial k; withdrawn).
- Withdrew the flagging of a 053 delta-factor phase error (my phase slip; 053's sentence is correct).
- Reported the linking failure as a bounded no-go with its exact hypothesis class rather than claiming
  a u=1 closure of the displayed identity: the u=1 damped convergence is proven, but the flat-side
  delta-removal in modulus fails (e^{c(k)^2/(4eps)}), so nothing closes.

## Milestone assessment
Routine. No milestone trigger: nothing on the critical path is closed; a bounded obstruction and
positive lemmas are recorded.

## Status-label recommendation
Critical-path set re-derived from ch17-agenda + Appendix H: A, B, C, D1, E, F, G-derived, N.
No label changes proposed; Problem E stays "Remains Assumption~\ref{ass:lorentzian}", open,
PROGRAMME-CONDITIONAL.

## Author decision needed
None.

## Remaining open step
To close the slice case of the displayed identity at N=2: an oscillation-based estimate controlling
I_eps[O_k] - (delta-damped family) without absolute values (cancellation in e^{iS_b} along the flat
contour and along R_u, u<2/3), or a mechanism outside regulator (A) moduli bridging (other regulator,
fermion-contact sector, different presentation). The transverse-domination question at fixed u
(055 avenue 1) remains open for non-modulus norms; this package shows it cannot be done in modulus.

## Special instructions for the gatekeeper
Re-derive: (i) Re e^{3pi i/8}A_0(theta)^2 = cos(3pi(2theta-1)/8) and the monotone-ratio derivative
identity; (ii) c_0 lower bound at u=0.3 (b_u = sin(0.7*3pi/8) r^0 = 0.7337 r^0; K = cos(0.3*3pi/4) =
0.5878; c_0 = 0.04432 r^0 2); (iii) band emptiness at eps=0.01: lambda_* eps = 0.01848 > e^{-4.432} =
0.01189; (iv) the u=1 sign flip at lambda_*. Must NOT be asserted: any closure of the slice identity;
that the no-go extends beyond modulus-based bridging; anything about u >= 2/3 beyond M_u = infinity.
Re-run both scripts with python -I. bridge_r1.py SEC 4 series-vs-closed-form at u=0, eps=0.002 has
reldev ~ 1e-3 (slow convergence of the 80-term series; closed form is exact) - flag if the
gatekeeper wants a cleaner series check. The 055 review m1 (4-CRLF before Status) is why the anchor is
the 4-CRLF block; confirm count 1 before applying.
