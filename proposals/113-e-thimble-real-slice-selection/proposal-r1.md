# Proposal 113-e-thimble-real-slice-selection, round 1

RECORD package: no manuscript-bound text is drafted, no build, no status,
priority or completion change. Per the 112 review-r1 disposition ("Next
target for the loop: g3 avenue 2 (thimble-side)"), this package attacks the
strongest contour-side route ranked by 112: whether Lefschetz-thimble /
nonlinear-contour data of the N=2 IKKT matrix model can select the real
slice, i.e. confront premise (P1) of the recorded dichotomy at appH L1831
outside linear regulator-class contours.

## Result

Inside the named class K (stated in (T5)): N=2, massless, unregularized
holomorphic action $S_{\mathrm b}[h_0]$ with fixed complex symmetric
$h_0$, contour data taken to be the critical set, downward-flow and
Stokes/intersection data of $H=\operatorname{Re}(\mathrm i S_{\mathrm b}[h_0])$,
no mass, no state, finite $N$ — thimble data cannot select the Lorentzian
real slice. Concretely: (i) the critical set of $S_{\mathrm b}$ at $N=2$ is
computed exactly: it is the locus $(\operatorname{tr}\mathcal G)X=\mathcal GX$,
contains a 12-complex-dimensional commuting cone and a null branch, is a
cone (scaling), hence contains no isolated critical point, and
$S_{\mathrm b}\equiv0$ on all of it (Euler identity), so the standard
thimble decomposition has no discrete intersection data to carry (T2);
(ii) the flow/sign data is congruence-covariant: the map $X\mapsto XL^{\mathrm T}$
identifies the critical and $H$-level-set data of $h_0$ with that of
$(L^{\mathrm T})^{-1}h_0L^{-1}$ (T3), and with the 112-E5 witness
$\Lambda_w=\operatorname{diag}(i,\hat 1_9)$, $\Lambda_w^{\mathrm T}\eta\Lambda_w=\mathbb 1$,
the Riemannian and Lorentzian actions carry the same thimble data up to a
bijection: no statistic natural under it separates the slices (T5b);
(iii) $H\equiv0$ on the Hermitian slice and, along temporal phase rays,
$H(\varphi)=\tfrac{k}{4}C\sin 2\varphi$ with $C=\operatorname{(tr}\mathcal G_s)(t\!\cdot\!t)-t^{\mathrm T}\mathcal G_s t\ge0$
independent of the slice choice: the damping direction is fixed by the
product of the exponent orientation and $h_0$ alone (T4); (iv) the input
finding: the thimble construction takes as input the contraction $h_0$
inside $S_{\mathrm b}$, a conjugation (real form) for the flow, and an
exponent orientation — the signature datum sits in the inputs of the very
object whose thimbles were hoped to derive it. Within K this is a bounded
no-go consistent with, and filling, the recorded gap "This is no statement
about non-linear contours" (appH L1831). E stays OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL; the escapes named by the bound are mass (recorded
as supplied, L1818), $N\ge3$ Pfaffian-weighted flow, states/vacuum, large
$N$, and the finite-$\epsilon$ regulated thimble decomposition.

## Claim

Problem E, contour side. The target of E is stated in ch17 L721-722:
"Problem~E: Lorentzian signature is derived rather than
retained (Assumption~\ref{ass:lorentzian})." and ch17 L698:
"DERIVED means no remaining assumed premise in the claimed chain".
The current E ledger (appH L1661-1664, live tree, quoted verbatim):
"Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label.
Completion: PROGRAMME-CONDITIONAL. A scope retaining
Assumption~\ref{ass:lorentzian} gives up the claim of emergent or
matrix-derived Lorentzian signature."; the E status passage (appH
L1907-1908): "Remains Assumption~\ref{ass:lorentzian}."

Claim. (C1) Derived identities at $N=2$ (established, verified
numerically to $10^{-14}$): the exact critical-set equation of the
bosonic action, (T2); vanishing of $S_{\mathrm b}$ on the critical set,
(T2b); congruence covariance of critical and $H$-level data, (T3); the
slice-phase damping law $H(\varphi)=(k/4)C\sin2\varphi$, $C\ge0$, (T4).
(C2) Bounded no-go with input finding (conditional on class K, (T5)):
no datum of the thimble construction of
$\operatorname{Re}(\mathrm i S_{\mathrm b}[h_0])$ at massless $N=2$
selects the Lorentzian real slice over the Riemannian one; the
signature enters the construction as the input $h_0$ plus the flow
conjugation and exponent orientation. This is the thimble-side
counterpart of 112-E6/E7 and consumes the recorded allowance "This is
no statement about non-linear contours" (appH L1831) with a bounded
negative statement inside K plus the positive lemmas (C1). It derives
nothing toward closing E: it constrains the contour-side route and
records where the needed datum would have to enter (non-equivariance
under $\Lambda_w$).

## Inputs

All manuscript statements relied on, quoted from the live tree
(appH = chapters/appH-microscopic-proofs.tex; digests were CURRENT,
head 23266972cd, appH live sha1 60a8eb47bb...c2b3):

- appH L1673 (defs (A) and contour; Stokes slide; damping formula):
  "\(I_\epsilon[O]\) equals the same integral on \(\mathcal R_u\) for
  every \(u<2/3\) (exact)" and
  "\(\operatorname{Re}\mathrm iS_{\mathrm b}=-\sin(\pi u/2)\,S_{\mathrm E}(\tilde A)\)".
  Used: (T4) consistency at $u=0$ (no damping on the Hermitian slice)
  and (T5g).
- appH L1685: "therefore carries at finite \(N\), conditionally for
  \(N\ge3\), no datum beyond the Euclidean model". Used: (T5g) context.
- appH L1687: "act on different contour integrals and produce no
  competing value". Used: (T5d) scope — the \(\gamma>0\) CNT thimble
  family is quoted, not used as evidence.
- appH L1775 (N=2 reduction): \(\mathcal G_{ab}=h(x^a,x^b)\),
  \(S_{\mathrm b}=\tfrac1{4g_{\mathrm{YM}}^2}\sum_{a<b}[h(x^a,x^a)h(x^b,x^b)-h(x^a,x^b)^2]\).
  Used: setup; equals \((8g_{\mathrm{YM}}^2)^{-1}E(\mathcal G)\),
  \(E(\mathcal G)=(\operatorname{tr}\mathcal G)^2-\operatorname{tr}\mathcal G^2\)
  since \(E=2\sum_{a<b}[\cdots]\).
- appH L1783(ii): "Since \(h=\Lambda^{\mathrm T}\eta\Lambda\) is
  invertible, a path of these contours whose \(h\) stays in the closure
  of \(\mathfrak C\) cannot pass from \(\mathfrak C_0\) to
  \(-\mathfrak C_0\)." Used: (T5g) the flow-side damping side is the
  \(\mathfrak C_0\) side; no crossing.
- appH L1807 (regulator class fixing): "which the regulator carries
  over to every admissible contour but does not select, so
  Assumption~\ref{ass:lorentzian} is not discharged" [full sentence:
  "The inertia found in (i) is that of the \(\eta\) put into
  \(S_{\mathrm b}\), ..."]. Used: (T5a) input inventory: the
  manuscript's own "put into" statement, extended to flow data.
- appH L1821: "is even in \(h_0\), the values \(t\) and \(10-t\) give
  the same integrand, with \(\mathfrak C_0\) and \(-\mathfrak C_0\)
  [interchanged]". Used: (T5b) the \(t\)-symmetry of the data.
- appH L1823(i): "the real invertible forms in the closure of
  \(\mathfrak C\) are those with \(t\in\{0,1,9,10\}\), and all of
  these occur". Used: (T5g): both \(\eta\) (\(t=1\)) and
  \(T^{\mathrm T}T\) (\(t=0\)) are boundary points of one class.
- appH L1827(c): "paths ending on damped contours exist: the
  \(\mathcal R_u\) for \(h_0=\eta\), and
  \(A=\mathrm e^{\pi\mathrm i\tau/8}X\) for \(h_0=\mathbb 1\)". Used:
  (T5b): both candidate slices admit damped contours, so existence of
  damping cannot separate them.
- appH L1831 (dichotomy and exclusions): "(P1) is a condition on the
  representation of the integral within linear contours, and (P2) is
  supplied content, since Equation~\eqref{eq:Smatrix} is bosonic.
  This is no statement about non-linear contours, about linear maps
  that also mix the colour components, ... The signature selected
  under (P1) and (P2) is that of a contraction of matrix indices,
  both premises are imposed, and Assumption~\ref{ass:lorentzian} is
  not discharged." Used: the gap this package fills, with its own
  exclusions kept (colour-mixing maps, fixed \(\gamma>0\), \(N\to\infty\)
  first, Definitions (B),(C)).
- appH L1744-1747: the RP-paragraph exclusion list containing "the
  thimble contour integrals of~\cite{ChouNishimuraTripathi2025}":
  these are not used; the package's statements are at \(\gamma=0\)
  about the massless flow of the chosen action.
- ch03 L143 eq:Smatrix (bosonic action with the \(\eta\)-contraction)
  and ch03 L173 def:matrix-coords-ext: context only; eq:Smatrix is the
  locus of the input finding (T5a): the defining action already
  carries \(h_0=\eta\).
- ch04 L322-328 ass:lorentzian ("The locked vacuum is Lorentzian:
  \(\eta_{AB}=\mathrm{diag}(-1,+1,+1,+1)\). Dynamical emergence of
  this signature from a Euclidean matrix model is not proved in the
  source notes and is not pretended here."): its name only is used;
  the package neither discharges nor modifies it.
- 112 proposal-r1 E5 (gatekeeper-VERIFIED, review-r1): the complex
  congruence witness \(\Lambda=\operatorname{diag}(i,1\times9)\) with
  \(\Lambda^{\mathrm T}\eta\Lambda=\mathbb 1\) and
  \(\Lambda^{\mathrm T}\mathbb 1\Lambda=\eta\). Used: (T3), (T5b).

## Derivation

Setup (S0). \(N=2\): traceless \(2\times2\) fields
\(A_\mu=\sum_a x^a_\mu\sigma^a\) with Pauli basis \(\sigma^a\), colour
vectors \(x^a\in\mathbb C^{10}\), \(a=1,2,3\): the complexified
configuration space is \(X\in\mathbb C^{3\times10}\) (30 complex
dimensions). For a fixed nondegenerate complex symmetric
\(h_0\in\mathbb C^{10\times10}\):
\(\mathcal G=Xh_0X^{\mathrm T}\) (symmetric \(3\times3\)),
\(E(\mathcal G)=(\operatorname{tr}\mathcal G)^2-\operatorname{tr}\mathcal G^2\),
and \(S_{\mathrm b}[h_0](X)=(k/8)E(\mathcal G)\) where the constant \(k\ne0\)
depends only on the Pauli normalization. The flow function is
\(H=\operatorname{Re}(\mathrm i S_{\mathrm b}[h_0])\) for the integrand
\(e^{\mathrm i S_{\mathrm b}}\) (appH L1671 convention; flipping the
exponent orientation flips \(H\)).

(T1) Reduction constant (established). Direct evaluation of the
commutator contraction \(-\tfrac14 h^{ma}h^{nb}\operatorname{Tr}[C_{mn}C_{ab}]\),
\(C_{mn}=[A_m,A_n]\), on random \(X\) for
\(h_0\in\{\eta,\mathbb 1,L^{\mathrm T}\eta L\}\) gives a constant of
proportionality to \((k/8)E\) independent of \(X\):
\(k(\eta)=16\) in the Pauli convention (r1, rel. err. \(<10^{-14}\)).
This matches the manuscript form at L1775 (see Inputs) with
\(k=16/g_{\mathrm{YM}}^2\); only \(k\ne0\) enters every subsequent
statement, so the convention is immaterial.

(T2) Critical set (established derivation + verification r2, r5).
\(E\) is a polynomial of the symmetric matrix \(\mathcal G\) with
\(\partial E/\partial\mathcal G_{ab}=2(\operatorname{tr}\mathcal G)\delta_{ab}-2\mathcal G_{ab}\);
polarizing \(\mathrm d\mathcal G_{ab}=h_0(\mathrm dx^a,x^b)+h_0(x^a,\mathrm dx^b)\) and
using symmetry,
\[
\mathrm d S_{\mathrm b} \;=\; \tfrac{k}{2}\sum_a h_0\!\bigl(\mathrm dx^a,\;V_a\bigr),
\qquad V_a=(\operatorname{tr}\mathcal G)\,x^a-\textstyle\sum_b \mathcal G_{ab}\,x^b ,
\]
so, \(h_0\) nondegenerate, the critical locus is exactly
\(\{X:(\operatorname{tr}\mathcal G)X=\mathcal GX\}\) (equivalence, not
merely inclusion; the factor \(\tfrac k2\) is irrelevant to the zero
set). Consequences:
(a) Cone structure: \(V(\lambda X)=\lambda^3V(X)\) (quartic \(S_{\mathrm b}\)),
so the critical locus is a complex cone; any nonzero critical point lies
on a \(\mathbb C^\times\)-line of critical points.
(b) Two explicit positive-dimensional families: the commuting cone
\(\{X=wz^{\mathrm T}\}\) (complex dim. \(3+10-1=12\)): there
\(\mathcal G=(z^{\mathrm T}h_0z)\,ww^{\mathrm T}\) has rank \(\le1\), so
\(\mathcal GX=(\operatorname{tr}\mathcal G)X\); and the null branch
\(\{\operatorname{tr}\mathcal G=0,\ \mathcal GX=0\}\), sample
\(X=(x,-\mathrm ix,0)\) at \(h_0=\mathbb 1\) (dim. \(\ge10\)). Generic
rank-2 \(X\) is not critical (r2: residual \(=1.00\) and \(50.6\) vs.
\(<10^{-13}\) on the families). Hence the critical locus is nowhere
isolated, including at \(X=0\) (a limit of the cone).
(c) Euler identity: \(\tfrac12\sum_a h_0(x^a,V_a)=4S_{\mathrm b}\)
(r5, residual \(0.0\) exactly), so \(S_{\mathrm b}\equiv0\) on the
whole critical locus (r2: \(|S_{\mathrm{crit}}|<10^{-13}\)).
(d) Thimble consequence: the Lefschetz decomposition
\(\Gamma=\sum_\sigma\langle\Gamma,J_\sigma\rangle J_\sigma\) requires
isolated critical points \(\sigma\) and carries the weights
\(e^{\mathrm i S(\sigma)}\); at massless \(N=2\) the critical set is a
positive-dimensional cone and all weights equal \(1\): the construction
supplies no discrete selection datum. Isolation returns only with an
added scale (mass: \(\delta S+\gamma A=0\) forces commuting
\(A=0\) only after the mass deformation - the supplied \(\gamma\) case,
appH L1812-1818; or the finite-\(\epsilon\) regulator, see (T5e)).

(T3) Congruence covariance (established derivation + r3). For any
\(L\in\mathrm{GL}(10,\mathbb C)\), with the bijection
\(\Phi_L:X\mapsto XL^{\mathrm T}\) of the complexified space,
\(\mathcal G[(L^{\mathrm T})^{-1}h_0L^{-1}](\Phi_LX)=
XL^{\mathrm T}(L^{\mathrm T})^{-1}h_0L^{-1}LX^{\mathrm T}=\mathcal G[h_0](X)\),
hence \(S_{\mathrm b}[(L^{\mathrm T})^{-1}h_0L^{-1}]\circ\Phi_L
=S_{\mathrm b}[h_0]\): \(\Phi_L\) carries critical loci, \(H\)-level
sets and thimble (Stokes) data of \(h_0\) bijectively onto those of
\((L^{\mathrm T})^{-1}h_0L^{-1}\) (r3: criticality of the cone point
and non-criticality of the random point both preserved; the \(H\)-value
identity is the displayed equality). The flow \emph{lines} themselves
depend additionally on a choice of real metric and conjugation used to
define "downward", which is a separate input (T5a) and is not
\(\Phi_L\)-natural for general \(L\).

(T4) Slice and phase-ray sign table (established derivation + r4),
\(h_0=\eta\). Write \(X=(t,x)\) with temporal colour vector \(t\in\mathbb C^3\)
and spatial part \(x\) (9 columns), and restrict first to
\(t,x\) real (Hermitian-slice data):
(i) \(H\equiv0\) on the Hermitian slice: there \(S_{\mathrm b}\) is
real, so \(\operatorname{Re}(\mathrm iS_{\mathrm b})=0\) (r4:
\(|H_0|<10^{-16}\); consistent with appH L1673 at \(u=0\):
\(\operatorname{Re}\mathrm iS_{\mathrm b}=-\sin(\pi u/2)S_{\mathrm E}\)).
(ii) Temporal phase ray \(X(\varphi)=(e^{\mathrm i\varphi}t,x)\): a direct expansion gives: with
\(\mathcal G(\varphi)=\mathcal G_s-\mathrm e^{2\mathrm i\varphi}tt^{\mathrm T}\) (\(\eta_{00}=-1\)) and \(tt^{\mathrm T}\) rank 1, the
\(e^{\pm4\mathrm i\varphi}\) coefficients \(\sigma^2-\sigma^2\) cancel and
\[
H(\varphi)\;=\;\tfrac{k}{4}\,C\,\sin 2\varphi,\qquad
C=\bigl(\operatorname{tr}\mathcal G_s\bigr)(t\!\cdot\!t)-t^{\mathrm T}\mathcal G_s t,
\qquad \mathcal G_s=xx^{\mathrm T}\ (\text{PSD }3\times3).
\]
By Cauchy-Schwarz for the PSD Gram matrix,
\(t^{\mathrm T}\mathcal G_st\le(\operatorname{tr}\mathcal G_s)(t\!\cdot\!t)=C\)
with equality iff the spatial colour span is rank \(\le1\) and \(t\) is
aligned with its top eigenvector (the rank-one corner of appH L1687).
So \(C\ge0\) always, and along every such ray
\(H<0\) exactly for \(\varphi\in(-\pi/2,0)\cup(\pi,3\pi/2)\): the
damping direction (clockwise in the temporal phase) is uniform, set by
the exponent orientation times \(\eta_{00}\), with no dependence on the
data \(X\) (r4: \(C=21.8928\), \(H(\varphi{=}0.6)\) matched to
\(10^{-14}\), clockwise \(H=-86.3<0\)). The sign of damping therefore
carries no slice datum: it is the same on either side for every
configuration, and degenerates only at the recorded rank-one corner.

(T5) Assembly: bounded no-go and input finding inside class K.
Class K: \(N=2\); massless (\(\gamma=0\)); one fixed nondegenerate
complex symmetric \(h_0\) in the action \(S_{\mathrm b}[h_0]\); contour
data = critical set, downward-flow manifolds and Stokes/intersection
data of \(H=\operatorname{Re}(s\,\mathrm i S_{\mathrm b}[h_0])\) for a
fixed exponent orientation \(s=\pm1\) and a fixed conjugation
(real form) of \(\mathbb C^{3\times10}\); finite \(\epsilon\) regulator
used only as in the recorded class-fixing paragraph (appH L1796-1807),
not flowed. Selection means: a datum of this construction that
distinguishes the Lorentzian model \((h_0=\eta)\) from the Riemannian
one \((h_0=\mathbb 1)\) in the sense of ch17 L721-722.
(a) Input inventory (established, definitional): the construction is a
function of the inputs \((h_0,s,\text{conjugation})\). The manuscript
already states the \(h_0\)-input for the linear theory, appH L1807:
"The inertia found in (i) is that of the \(\eta\) put into
\(S_{\mathrm b}\), which the regulator carries over to every admissible
contour but does not select"; the flow inherits the same input, and
the exponent orientation and conjugation are two further choices not
fixed by the matrix data (appH L1671 notes the two possible exponent
signs). So a thimble "selection" of the slice from data of this form
would be a function of the slice choice already made in the inputs.
(b) Cross-slice equivariance (established via (T3) + 112-E5): with
\(\Lambda_w=\operatorname{diag}(i,\hat 1_9)\) and
\(L=\Lambda_w^{-1}\), so that
\(L^{\mathrm T}L=\Lambda_w^{-\mathrm T}\Lambda_w^{-1}=\eta\)
(equivalently \((L^{\mathrm T})^{-1}\eta L^{-1}=\mathbb 1\), from
the 112-E5 witness \(\Lambda_w^{\mathrm T}\eta\,\Lambda_w=\mathbb 1\)),
\(\Phi_L\) of (T3) is a bijection carrying the critical locus, \(H\)-level sets and thimble
complement data of the Lorentzian action onto those of the Riemannian
one; by (T4) the damping half-spaces correspond too. Any selection
statistic natural under this bijection takes the same value on the two
models. Since the two models are the two candidates of the recorded
boundary set (appH L1823(i), \(t\in\{0,1,9,10\}\); evenness in \(h_0\),
L1821; both admit damped contours, L1827(c)), no statistic of the
construction built equivariantly from \((h_0,s,\text{conjugation})\)
separates them. This is the thimble-side image of 112-E5/E6: the
separating move is the complex congruence itself.
(c) Same-action blindness (conditional on recorded Stokes facts):
within one action, the recorded Stokes slide
(appH L1673, "\(I_\epsilon[O]\) equals the same integral on
\(\mathcal R_u\) for every \(u<2/3\) (exact)") and the
\(\mathfrak C_0/\!-\mathfrak C_0\) non-joinability (L1783(ii)) say the
admissible contours of \(h_0=\eta\) are homologous on the class and
their integrals coincide; a thimble decomposition re-expresses exactly
these integrals (\(\Gamma=\sum\langle\Gamma,J_\sigma\rangle J_\sigma\)
is homological), so thimble data cannot carry a datum the integrals do
not have, and at finite \(N\) the recorded conclusion is "no datum
beyond the Euclidean model" (L1685). (d) Non-isolation ((T2)): at
\(\gamma=0\) the decomposition has no isolated critical points; the
recorded \(\gamma>0\) thimble family acts "on different contour
integrals and produce[s] no competing value" (L1687).
(e) Scope (named escapes, not covered): the finite-\(\epsilon\)
regulated flow (\(\operatorname{Re}(\mathrm iS_{\mathrm b}-\epsilon Q)\)
does generically isolate critical points; the quadratic regulator form
\(Q\) is \(\delta\)-type and is \emph{not} \(\Lambda_w\)-equivariant:
under \(\Phi\) it maps to the \(\eta\)-type form, i.e. \(\Phi\) sends
\((\eta,Q_\delta)\mapsto(\mathbb 1,Q_\eta)\), the Wick-partner model,
not the Riemannian model with its own regulator; the linear version of
this question is the recorded no-selection of L1796-1807; the
non-linear thimble version at fixed \(\epsilon\) is an open
sub-computation whose \(\epsilon\to0\) limit is controlled by L1673
and L1685); mass terms (recorded supplied deformation, L1812-1818);
colour-mixing linear maps and Definitions (B),(C) (L1831 exclusions);
\(N\ge3\) flow weighted by \(\operatorname{Re}\ln\mathrm{Pf}\,\mathcal M\)
(cf. Transfer below); states/vacuum; \(N\to\infty\) taken first.
Transfer (conditional, to g3.3): if at \(N\ge3\) the Pfaffian weight is
invariant under index rotations \(\Phi\) (the \(N=2\) identity
appH L1675 is an \(\mathrm{SO}(10,\mathbb C)\times\mathrm{SO}(3,\mathbb C)\)
invariance statement; the \(N\ge3\) analogue is not re-derived here and
is flagged), then (b) still applies to the Pfaffian-weighted flow and
the signed-Pfaffian route must break real-form symmetry elsewhere to
feed selection.

## Result classification

- (T1): established identity (verified numerically, rel. err.
  \(\le10^{-14}\), and matching the recorded L1775 form).
- (T2): established derivation (calculus of \(E(\mathcal G)\); cone
  and branch computations; Euler identity checked exactly) with
  numerical verification r2, r5.
- (T3): established derivation (one-line congruence algebra), r3.
- (T4): established derivation (phase-ray expansion; Cauchy-Schwarz
  for PSD Gram matrices), r4; the sign table is a theorem of the
  phase-ray family, not of the full nonlinear flow.
- (T5a): established inventory of definitions (appH L1671, L1807,
  eq:Smatrix).
- (T5b): conditional result, conditional on (T3) + 112-E5 (accepted);
  the quantifier is "every selection statistic natural under the
  bijection", not "no conceivable construction" - see Dependencies.
- (T5c): conditional on the recorded appH L1673/L1685/L1783(ii)
  Stokes facts plus the standard homological invariance of thimble
  intersection data.
- (T5d): established at \(\gamma=0\), unregularized; the \(\gamma>0\)
  sentence is a quotation of appH L1687, not a derivation.
- (T5e): unresolved steps named (finite-\(\epsilon\) thimbles,
  \(N\ge3\) Pfaffian-weighted flow, vacuum, large \(N\)).
- Transfer to g3.3: conjecture-level conditionality as flagged; the
  \(N\ge3\) Pfaffian invariance under index congruences was not
  verified here.

## What this does NOT do

- It does not derive E. E remains OPEN / CRITICAL PATH /
  PROGRAMME-CONDITIONAL (appH L1661-1664, quoted);
  Assumption~\ref{ass:lorentzian} (ch04 L322) is neither discharged
  nor altered, and the E status line "Remains
  Assumption~\ref{ass:lorentzian}." (appH L1907-1908) stands.
- It does not close or discharge (P1): the no-go says thimble data of
  class K cannot replace (P1), not that (P1) is false; (P2), the mass
  paragraph (L1812-1818), and the dichotomy t\(\in\{1,9\}\) are
  untouched.
- It does not reach: the vacuum/state route (g3.1), \(N\ge3\) with
  genuinely non-equivariant weight, the large-\(N\)-first limit,
  colour-mixing linear maps, Definitions (B)/(C), or the fixed
  \(\gamma>0\) CNT thimble integrals (appH L1744-1747, L1687) -
  those are named escapes, quoted not analyzed.
- It makes no claim about Problems H, I, J, and no label, priority or
  completion change is proposed anywhere.
- k=16 is a Pauli-convention constant; it is not a physical
  prediction and is never used numerically.

## Dependencies and gaps

Dependencies of the package: appH L1661-1664, L1671-1673, L1675,
L1685-1687, L1744-1747, L1775, L1783(ii), L1796-1807, L1812-1831,
L1907-1908; ch17 L698, L721-722; ch04 L322 (name only);
eq:Smatrix (ch03 L143); 112-E5 witness (accepted, 112 review-r1).
No dependency on any unmerged proposal other than 112.

Gaps (explicit):
1. Full classification of the critical locus at \(\operatorname{rank}X=2\)
   is not done; only explicit positive-dimensional families plus the
   exact defining equation are claimed (enough for non-isolation).
2. (T5b) quantifies over selection statistics natural under
   \(\Phi_{\Lambda_w^{-1}}\); a universal "no construction whatsoever"
   is not provable and is not claimed - the bound is class K plus
   naturality, and its value is that any escape must break
   \(\Lambda_w\)-equivariance, which is a test any proposed selection
   mechanism must pass.
3. The finite-\(\epsilon\) regulated thimble decomposition at \(N=2\)
   is not computed (named sub-computation, (T5e)): expected outcome
   constrained by L1673/L1685 (contour values are already equal) and
   L1796-1807 (linear analogue: no selection).
4. The \(N\ge3\) Pfaffian invariance needed for the g3.3 transfer is
   not verified here (flagged, transfer is conditional).

## Manuscript landing note

No text is drafted. If a future Problem-E note is authorized, a
suitable future passage (near the E ledger section of
appH-microscopic-proofs.tex, beside the (P1)+(P2) paragraph) would
state, with the class K qualifier inline: that at massless \(N=2\) the
critical set of \(S_{\mathrm b}\) is the cone
\((\operatorname{tr}\mathcal G)X=\mathcal GX\) carrying
\(S_{\mathrm b}\equiv0\), so the Lefschetz decomposition has no
isolated critical points and no discrete selection datum; that the
thimble data of the Lorentzian and Riemannian actions are congruent
under \(\Lambda_w=\operatorname{diag}(i,\hat 1_9)\); that the damping
direction of \(\operatorname{Re}\mathrm iS_{\mathrm b}\) is fixed by
the input \(h_0\) and the exponent orientation, not by the
configuration; and that consequently the non-linear-contour route at
\(\gamma=0\) supplies no slice selection, the remaining contour-side
openings being the finite-\(\epsilon\) regulated thimble problem,
\(N\ge3\), states and large \(N\); one scoped status sentence, E
unchanged (OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL). Any such
sentence must carry the class-(K) qualifier inline (112 review-r1
finding 3 applies verbatim) and must not assert that (P1) is
discharged.

## Verification scripts

Folder: proposals/113-e-thimble-real-slice-selection/
- t13_thimble_checks.py - re-run:
  `cd proposals/113-e-thimble-real-slice-selection && python -I t13_thimble_checks.py`
  (python3 + numpy; rng seeded 113; deterministic).
  Expected invariant output (recorded final block):
```
BEGIN 113 thimble checks
r1: PASS k(eta)=16-1.06735e-15j errs=['7.5e-16', '1.5e-15', '8.7e-15']
r2: PASS critres cone=2.3e-14 null=2.9e-15 rank2=1.00 rand=50.64 S_crit=1.4e-14
r3: PASS crit cone both=6.2e-13 rand both nonzero
r4: PASS C=21.8928 H(0.6)err=1.5e-14 H0=0.0e+00 Hcw=-86.2970
r5: PASS |4S-sum x dS|=0.0e+00
END 113 thimble checks
```
  r1 = (T1); r2 = (T2) equation on cone/null branch vs non-critical
  rank-2/generic plus \(S_{\mathrm{crit}}=0\); r3 = (T3); r4 = (T4);
  r5 = Euler identity in (T2c). Symbolic output is a check, not a
  proof; the proofs are the displayed derivations.
- Runs used: 2 of 12. Run 1 r4 FAILed: harness bug only - the spatial
  slice extraction read 8 of 9 columns; fixed, run 2 all PASS.
- A superseded draft (t13_thimble_checks_part2.py) was deleted before
  submission; patch helpers were deleted. Nothing outside this folder
  was written.

## Decisions Taken

- Locus: attacked at \(N=2\), massless, \(\gamma=0\) - the locus where
  the manuscript's exact reduction (L1675, L1775) holds, so all
  statements are exact model identities, not toy substitutions
  (derivation-first directive). Rejected: starting at \(N\ge3\) or
  with the mass term, where the action itself is no longer the
  derived object.
- Flow function \(H=\operatorname{Re}(\mathrm iS_{\mathrm b})\) with
  the appH L1671 exponent convention; the opposite orientation flips
  \(H\) and is treated as the input \(s\) of (T5a).
- Method: exact algebraic invariants (critical equation, cone
  structure, Euler identity, congruence covariance, phase-ray law)
  verified numerically, instead of integrating flow lines (unreliable
  within the run budget and adding no selection-relevant datum:
  selection data is homological, (T5c)).
- Kept the regulator outside the flowed function, matching the
  recorded treatment (L1796-1807), and named the finite-\(\epsilon\)
  thimble problem as a gap instead of glossing it ((T5e)).
- Routine wording, notation, and record-placement choices are mine
  per the author directive; no label/scope/core choice arises, hence
  no Author-decision item.

## Milestone assessment

Routine. Bounded narrowing of a contour-side route plus positive
sub-lemmas at \(N=2\); no critical-path step derived, no missing link
closed, no merged claim falsified. (Same reasoning the 112 review-r1
applied to 112: the appH consequence lives next to the already
recorded L1685/L1807/L1831 statements; this package is their
thimble-side completion inside class K.)

## Status-label recommendation

Derived from ch17 L694-731 + appH: current critical-path list at the
full-GR scope is A, B, C, D1, E, F, G-derived, N; none touched. For E:
unchanged - OPEN / CRITICAL PATH for the matrix-derived label /
PROGRAMME-CONDITIONAL. No label change proposed.

## Author decision needed

None.

## Remaining open step

To close E one still needs a real-slice selection outside class K.
Ranked escapes, derivation-first:
1. Upstream gate: the vacuum/state route (g3.1, Problem D/D1-gated).
   Transfer from this package: any such route must produce a
   composite/vacuum datum that breaks
   \(\Phi_{\Lambda_w^{-1}}\)-equivariance - a concrete falsifiable
   test for D1-type candidate order parameters.
2. Finite-\(\epsilon\) regulated thimble decomposition at \(N=2\)
   (isolated critical points via the quadratic regulator; decide
   whether its \(\epsilon\to0\) thimble data can carry anything
   beyond the recorded L1685 blind value).
3. \(N\ge3\) signed-Pfaffian-weighted flow (g3.3 x g3.2), conditional
   on the transfer flag in (T5e).
4. Large-\(N\)-first (non-uniformity explicitly noted at appH L1685).

## Special instructions for the gatekeeper

Scope limits: every claim is inside class K as defined in (T5); the
no-go must not be quoted beyond it, and must not be read as
discharging (P1), as reaching the vacuum/N\(\ge3\)/large-\(N\)/
\(\gamma>0\) routes, or as making (P1) optional. Please re-check:
(i) the differential \(\mathrm dS_{\mathrm b}=(k/2)\sum h_0(\mathrm dx^a,V_a)\)
(only the zero set matters; factor \(\tfrac k2\) convention-dependent);
(ii) the direction of the (T3) bijection: \(\Phi_L:X\mapsto XL^{\mathrm T}\)
carries data of \(h_0\) to data of \((L^{\mathrm T})^{-1}h_0L^{-1}\),
with \(L=\Lambda_w^{-1}\) giving \(\eta\mapsto\mathbb 1\);
(iii) the (T4) sign: with \(\eta_{00}=-1\) the temporal part enters
\(\mathcal G\) as \(-e^{2\mathrm i\varphi}tt^{\mathrm T}\), producing
\(+\,(k/4)C\sin2\varphi\), and \(C\ge0\) by PSD Cauchy-Schwarz (r4
checks the sign directly); (iv) the quoted appH lines (1673, 1685,
1687, 1775, 1783, 1807, 1821, 1823, 1827, 1831, 1907) against the
live tree, and 112-E5 in proposals/112 (accepted); (v) the script
reproduction block above (re-run command in Verification scripts;
expected: the five PASS lines verbatim). Nothing about H/I/J; no
label; RECORD-only, no build required.

END PROPOSAL 113 r1
