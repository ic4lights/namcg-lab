# Proposal 065-b-ward-measure-insertion-sublemma, round 1

Target: attack-plan node **B.ward** (Problem B, replica Ward identity / entanglement stationarity).
Intended integration ordinal: 63.

## Result

Two things are established and one bounded obstruction is reported precisely.

1. **Exact insertion identity with the measure Jacobian.** For the replica functional built from the
   matrix data of Equation~(eq:Smatrix) at finite $N$, writing the integrand as $j_\varepsilon e^{-S_{E,\varepsilon}}$,
   \[
     \partial_\varepsilon\ln Z_n=-\langle\mathcal I_n\rangle_n+\langle\partial_\varepsilon\ln j_\varepsilon\rangle_n,
     \qquad \mathcal I_n=\partial_\varepsilon S_{E,n},
   \]
   holds exactly (differentiation under the integral sign; verified symbolically, residual 0). This converts
   the disclaimed item at appH L477, "the measure of the matrix integral", into a precise term: for the flat
   Lebesgue matrix measure of eq:Smatrix the Jacobian term vanishes identically; for any non-flat measure
   (Moyal corrections, field redefinitions) it is the *entire* measure contribution and it is not computed
   anywhere in the book.

2. **Null directions of the insertion identity.** Schwinger–Dyson (loop) equations
   $\langle\mathcal V(S_{E,n})\rangle_n=\langle\operatorname{Div}\mathcal V\rangle_n$ give zero expectation to
   equation-of-motion insertions and reduce insertions to contact terms. Divergence-free (unimodular)
   change-of-variables directions are **null**: $Z_n(\varepsilon)$ is $\varepsilon$-independent and
   $\langle\mathcal I_n\rangle_n=0$ for every $n$. The compensating rotation acts as $X^a\mapsto e^{tB}X^a$
   with $B$ antisymmetric in $\eta$ (so $B\in\mathfrak{so}(1,3)$, $\operatorname{tr}B=0$), hence the Jacobian
   over the $N^2$ matrix entries is $(\det e^{tB})^{N^2}=e^{tN^2\operatorname{tr}B}=1$; adjoint flows
   $X\mapsto e^{t\Lambda}Xe^{-t\Lambda}$ have $\operatorname{tr}\operatorname{ad}_\Lambda=0$. **Consequence:** the
   coefficient $-4\kappa_X$ required in the paragraph "Matrix gauge realisation" can never be produced by the
   insertion identity along a compensating rotation or an adjoint flow. This sharpens (does not replace) the
   recorded conclusion at appH L462 that the coefficient is a property of the modular Hamiltonian of the state
   at $\Sigma$, or of a local symmetry, and not of the induced density.

3. **Bounded no-go: the loop equations do not imply $\delta S_D=0$, even at Gaussian order.** For the
   Gaussian conical-contact family $A_n=A_1+(\tfrac1n-n)P+\varepsilon B$ ($P$ supported at the branch locus;
   the $n$-dependence $c(n)=1/n-n$ is the same as the flat-cone coefficient of the paragraph "Replica cone
   coefficient", where $\tfrac1{12}(\tfrac1n-n)=\tfrac1{12}c(n)$, $c(1)=0$, $c'(1)=-2$), one derives exactly
   \[
     \partial_\varepsilon S_D=\operatorname{Tr}(G_1BG_1P)-\tfrac12\operatorname{Tr}(G_1B),\qquad G_1=A_1^{-1},
   \]
   (hand derivation below; symbolically verified, residual 0). This is nonzero for a generic block
   deformation (e.g. $B=bE_{11}$ gives $b(2-a_1)/(2a_1^2)$) and vanishes only on the codimension-one
   hyperplane $2\operatorname{Tr}(G_1BG_1P)=\operatorname{Tr}(G_1B)$. In this class, $\delta S_D=0$ is a
   *linear condition on the deformation* (a linearised block equation plus a contact term at the tip), not a
   consequence of any Schwinger–Dyson identity. **Nothing is closed.** Problem B remains OPEN,
   CRITICAL PATH, PROGRAMME-CONDITIONAL, exactly as recorded.

Additionally (R4) the nearest published statements are recorded with verified records, and the Arata et al.
prior-claim difference is analysed: their first-law extra term is the Noether charge of a genuine **local**
symmetry $\delta u^a=f\,a^a$ of a reduced gauge-fixed action; in NAMCG the compensating rotation is rigid
isotropy, not a local rotation of the matrix index (appH L469), and this is the *mirror obstruction*, not an
application of their mechanism.

## Target and status

- **Problem** (appH, `\section{Problem B: replica Ward identity}`, label `sec:status-B` region): current
  ledger wording, appH L123–126 verbatim: "Status: OPEN. Priority: CRITICAL PATH.
  Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity
  condition for the tensor block is not derived."
- **Missing step** (appH L146–155 verbatim): "Derive from the microscopic dynamics the
  entanglement-stationarity condition \(\delta S_D=0\) for the allowed fixed-volume variations, and
  establish the area contribution and its relation to the \emph{emergent} metric without presupposing
  that metric or the fluctuation split of Chapter~5. For variations of the auxiliary scaffold, the replica
  insertion computes a response to \(g^{(0)}_{\mu\nu}\); relating it to the emergent metric still requires a
  specified map between them. Problem~B therefore remains open, although the fixed-algebra first-law
  identity is established."
- **ch17 closure criterion** (L134–137): "Closure requires fixed-volume variations of the tensor
  (non-conformal) block from the microscopic action, a specified map \(g^{(0)}\mapsto g\), and no use of an
  already-existing metric. A conformal-only derivation is a sub-case and leaves B OPEN."
- **Dependency** (ch17 L671–673): "A derivation of B or F that still invokes Assumption~\ref{ass:dictionary}
  is DERIVED only after Problem~A is." Problem A is OPEN (appH L16, L109).
- **Classification of this proposal:** PROGRAMME-CONDITIONAL sub-lemma plus a bounded obstruction. It does
  not DERIVE B. It occupies exactly the item disclaimed at appH L477 ("the measure of the matrix
  integral") and the loop-equation route into it, and reports what that route can and cannot supply.
- **Dependencies of the proposal's own claims:** eq:Smatrix (ch03 L143), the replica-insertion paragraph
  (appH L179 ff.), the "Matrix gauge realisation" paragraph (appH L462–471), the "Replica cone coefficient"
  paragraph (appH L225–231), `ass:EE` (ch06 L71).

## Source reading

digest + targeted reads. `python scripts/make_digest.py --check` reported DIGEST CURRENT at task start.
Read in full: the Problem B section of `chapters/appH-microscopic-proofs.tex` (L120–478, including L146–155,
L179–186, L225–231, L462–481); the Problem B closure passage and dependency passage of
`chapters/ch17-agenda.tex` (L120–140, L665–680); `chapters/ch06-entanglement-equilibrium.tex` L55–99
(ass:EE); the `bib/namcg.bib` entries used as style templates (LewkowiczMaldacena2013 at L548 ff., Chen2022
at L621–629) and the full key list; the certified pre-states (appH 582,706 B / sha256
dd0bea7780757e51d9677d38130d0425dc38cd54538d85f14f26f23f97bdcf4a / CRLF 3435 / bare LF 0; bib 28,038 B /
sha256 c71780a9d968f47076613cf9d2c9a3fc3370f2b24e015178d569b28fc28757aa / CRLF 931 / 88 entries) — both
re-verified byte-exact by `simulate_apply.py` (it asserts them and passes). Unreadable files: none. Scout
reports `reports/sme-scout-20261109-*.md` were consulted for leads only; every imported claim is verified
below. Prior proposals 062 (C no-go style precedent) and 063/064 folders were read to avoid repeating routes.

## Research and reasoning

### R1. Insertion identity with measure Jacobian (established derivation)

Let $Z_n(\varepsilon)=\int d\mu_0(X)\,j_\varepsilon(X)\,e^{-S_{E,n}(\varepsilon;X)}$ where $d\mu_0$ is the flat
Lebesgue matrix measure of eq:Smatrix and $j_\varepsilon$ the ratio of the actual measure to $d\mu_0$.
Then
$\partial_\varepsilon\ln Z_n=\big\langle-\partial_\varepsilon S_{E,n}+\partial_\varepsilon\ln j_\varepsilon\big\rangle_n$.
The appH paragraph at L179 ("hold fixed the regulated geometry, branch locus, conical-locus data, and
integration measure") is the case $j_\varepsilon\equiv1$. The disclaimed item at L477 is the case
$j_\varepsilon\neq1$; this proposal makes its only possible entry point into the insertion identity explicit
and notes it is computed nowhere in the book. Verification: Check 1 of `derive_ward_r1.py` (one-dimensional
convergent Gaussian with an $\varepsilon$-dependent measure factor; residual 0, `derive_ward_r1.out`).

### R2. Schwinger–Dyson / loop kernel (established; general proof + exact check)

For compactly supported vector fields $\mathcal V$ on the matrix entries,
$0=\int \mathcal V(e^{-S_{E,n}})=\langle\mathcal V(S_{E,n})\rangle_n-\langle\operatorname{Div}\mathcal V\rangle_n$
by integration by parts with boundary decay — this is the loop-equation kernel
(`EynardOrantin2009`, J. Phys. A 42 293001 (2009), method reference). EOM insertions
($\mathcal V=\partial_k$) have zero expectation and mixed insertions give contacts
$\langle(\partial_kS)x_i\rangle=\delta_{ki}$. Because the general proof is elementary, the script verifies
it on explicit rational data (2×2 Gaussian, $A=[[2,\tfrac12],[\tfrac12,3]]$, $J=(1,-1)$; exact rationals;
all three checks pass, Check 2 of `derive_ward_r1.out`). The general-symbolic-integration version of the
same check was computationally intractable (nested sympy `integrate` with general symbols hung; see
Decisions) — the explicit-data check plus the parts argument above is the honest pairing.

### R3. Null directions and the $-4\kappa_X$ localisation (conditional on the stated lift; exact algebra)

If the $\varepsilon$-dependence is generated by a change of variables with flow $\mathcal V$, then
$\partial_\varepsilon S_{E,n}=\mathcal V(S_{E,n})-\partial_\varepsilon\ln j_\varepsilon$ up to the Jacobian, so
divergence-free directions are null: $\langle\mathcal I_n\rangle_n=-\langle\partial_\varepsilon\ln j_\varepsilon\rangle_n=0$.
Exact algebra (Check 3 of the script): a general $\eta$-antisymmetric generator ($\eta=\operatorname{diag}(-1,1,1,1)$,
$B^a{}_b$ with $B^T\eta+\eta B=0$, six free parameters) has $\operatorname{tr}B=0$; hence on the $N^2$ matrix
entries the Jacobian is $(\det e^{tB})^{N^2}=e^{tN^2\operatorname{tr}B}=1$. A concrete rotation+boost sample
gives $\det(e^B)-1=4.6\times10^{-41}$ (deterministic mpmath 80-term series, dps 40, permutation determinant).
Adjoint flows: $\operatorname{ad}_\Lambda=I\otimes\Lambda-\Lambda^{T}\otimes I$ on $2\times2$ matrices has
$\operatorname{tr}\operatorname{ad}_\Lambda=4\operatorname{tr}\Lambda-4\operatorname{tr}\Lambda=0$ (symbolic, general
$\Lambda$); numeric sample $\det(e^{\operatorname{ad}})-1=9.6\times10^{-34}$.
The identification "the compensating rotation is realised at matrix level as the rigid rotation
$X^a\mapsto e^{tB}X^a$" is the natural lift of the Poisson-limit statement at appH L469
($\{\varepsilon,X^a\}=B^a{}_bX^b$, a rigid linear rotation: "not a local rotation of the matrix index", L469);
this conditional identification is stated as such in the insert. Consequence: along compensating-rotation and
adjoint directions the insertion identity produces nothing, so the required $-4\kappa_X$ of the "Matrix gauge
realisation" paragraph cannot originate from $\langle\mathcal I_n\rangle_n$ along those directions. The
manuscript's own conclusion at L462 ("a property of the modular Hamiltonian of the state at $\Sigma$, or of a
local symmetry ... and not of the induced density") is thereby *sharpened*, not replaced.

### R4. Gaussian conical-contact no-go (established computation)

Family: $S_{E,n}=\tfrac12 x^TA_nx$ (matrix index suppressed; the same computation applies entrywise with the
$N^2$-fold degeneracy cancelling from $S_D$), $A_n=A_1+c(n)P+\varepsilon B$, $c(n)=1/n-n$, $P$ rank-one at the
branch locus. The $n$-structure matches the manuscript's flat-cone coefficient of the "Replica cone
coefficient" paragraph (L225–231): $\tfrac1{12}(1/n-n)=\tfrac1{12}c(n)$, and $c(1)=0$, $c'(1)=-2$
(Check 4(e)). With $\ln Z_n=-\tfrac12\ln\det A_n$ and the replica normalisation
$S_D=(\partial_n(-\ln Z_n))|_{n=1}+$ (constant subtraction $=-\ln Z_1$ term):
- $\langle\mathcal I_n\rangle_n=\tfrac12\operatorname{tr}(BA_n^{-1})$ (Check 4(a): identity residual 0);
- $\partial_\varepsilon S_D=\partial_n\langle\mathcal I_n\rangle_n\big|_{n=1}-\langle\mathcal I_1\rangle_1
  =-\tfrac12\operatorname{tr}\!\big(BG_1c'(1)PG_1\big)-\tfrac12\operatorname{tr}(G_1B)
  =\operatorname{Tr}(G_1BG_1P)-\tfrac12\operatorname{Tr}(G_1B)$
  (Check 4(b): exact closed form, residual 0);
- $B=bE_{11}$: value $b(2-a_1)/(2a_1^2)\neq0$ generically (Check 4(c));
- stationarity $\partial_\varepsilon S_D=0$ solves to the codimension-one linear condition
  $b_{11}=a_1^2(-a_2b_{33}-a_3b_{22})/(a_2a_3(a_1-2))$, and $B=E_{12}+E_{21}$ lies in the kernel (Check 4(d)).

Conclusion (the honest outcome, reported as a bounded obstruction, same class as the 062 no-go): **in this
hypothesis class the loop equations do not imply $\delta S_D=0$; stationarity is an extra linear condition —
a linearised block equation plus a tip contact — and the conical contact contributes to $\partial_n$ of the
insertion, not a Ward identity.**

### R5. Hypothesis class of the obstruction and the no-go fork (ranked avenues)

The obstruction depends on, exactly: (H1) Gaussian quadratic block form; (H2) the conical contact encoded as
an $n$-dependent *action* insertion $c(n)P$ under the fixed-geometry, fixed-measure prescription of L179;
(H3) $\varepsilon$-deformation linear in a single matrix $B$; (H4) flat Lebesgue matrix measure; (H5) finite
$N$ with no factorisation; (H6) bosonic single sector. Within the package two relaxations were explored:
(H4) via R1/R3 (result: null directions, not stationarity), and (H1)+(H2) via R4 (result: the bounded no-go).
Avenues still open, ranked by proximity to the critical path:

1. **Measure Jacobian for the actual (Moyal/Chen-type) measure** — R1 gives its exact entry
   $\langle\partial_\varepsilon\ln j_\varepsilon\rangle_n$; never computed in the book; the most direct
   occupant of L477's disclaimed item.
2. **Large-$N$ factorisation + locality** (Problem A / `ass:map` territory): factorisation would turn
   $\partial_n\langle\mathcal I_n\rangle$ into products of one-point blocks; this is where a Ward identity of
   the block could live, but A is OPEN and no factorisation is derived.
3. **Interacting block** (non-Gaussian $S_E$): insertions become connected correlators; the verified
   `AlloucheDou2026` abstract shows interaction corrections on fuzzy spaces are bulk-extensive and do not
   obey a pure area law — evidence that interactions alone do not restore area structure, not a no-go for
   the block. Uncomputed for the NAMCG block.
4. **State-side route**: appH L462 already locates $-4\kappa_X$ in the modular Hamiltonian of the state; the
   action-insertion route explored here structurally cannot reach it (R3).
5. **Local symmetry route** ($\delta u^a=fa^a$ analogue on matrix data): belongs to Problem D; R4/R3 show no
   rigid/adjoint matrix symmetry carries $-4\kappa_X$.
6. **Deformations that change geometry / branch locus / measure** (the L179 "must add" clause): outside the
   fixed prescription; uncomputed.
7. **Fermionic/Berezin measure sectors** (appH fermion paragraphs): uncomputed.

### R6. R4 literature and the Arata prior-claim difference analysis

Verified records (arXiv export API, abstracts in `citecheck_arxiv.out`; Eynard–Orantin via Crossref,
`citecheck_eo.json`):
- `TsuchiyaYamashiro2022` (2201.06871, JHEP 04 (2022) 086): target-space entanglement of eigenvalue
  subregions in the bubbling-geometry matrix model, qualitative area agreement.
- `KawamotoKuroki2021` (2107.08907, JHEP 12 (2021) 101): momentum-space entanglement on fuzzy spheres.
- `AlloucheDou2026` (2609.10027): $\lambda\phi^4$ corrections to entanglement on fuzzy spaces; interaction
  correction bulk-extensive, no pure area law (abstract checked verbatim).
- `ChoudhuryLaurenzano2024` (2407.13336, PRD 110 126018): entanglement of the black 0-brane with its
  Hawking radiation in BFSS.
- `Craps2026` (2602.02683, "Area terms and entanglement entropy in the $c=1$ string theory"; authors Craps,
  Gerbershagen, Pavlov, Vilar López): a dilaton-dependent area-like term is expected in the generalised
  entropy of bulk subregions but the leg-pole (nonlocal) transformation cannot account for it; non-singlet
  sectors suggested. Closest published instance of "an area-like term the microscopic mechanism does not
  supply".
- `EynardOrantin2009` (J. Phys. A 42 293001, DOI 10.1088/1751-8113/42/29/293001; method reference for the
  loop equations / topological recursion; DOI record verified via Crossref; the arXiv record was not
  independently fetched, so the bib entry carries **no eprint**).
- `JacobsonVisser2019` (1812.01596, SciPost 7 079) and `Svesko2019` (1810.12236, PRD 99 086006): causal-diamond
  first law / entanglement equilibrium — they presuppose an existing metric and geometric (conformal Killing)
  modular flow; inputs a derivation of `ass:EE` from eq:Smatrix must not use.
- `JensenSorceSperanza2023` (2306.01837, JHEP 12 (2023) 020): type-II-algebra realisation of a version of
  entanglement equilibrium; the abstract itself states the construction "relies on the existence of
  well-motivated but conjectural states whose modular flow is geometric at an instant in time".
- `ArataLiberatiNeri2026` (2603.28851): covariant phase space for Einstein–aether; stationary-black-hole
  first law carries an "irreducible entropic AEther contribution" (horizon-charge heat term).
- `ArataIsmailLiberati2026` (2606.27437): the extra first-law term for misaligned universal horizons is the
  Noether charge of a "previously unidentified symmetry of the reduced action, generated by infinitesimal
  transformations of the form $\delta u^a=f a^a$" ($f$ elliptic-constrained), of the reduced, elliptic
  gauge-fixed action (abstract checked verbatim).

**Arata difference (prior-claim analysis).** Could the NAMCG $-4\kappa_X$ / $r$-family edge term be the same
mechanism? No — mirror obstruction. Their mechanism needs (a) a genuine *local* symmetry of the (reduced,
gauge-fixed) action with parameter obeying a constraint, and (b) a charge from the covariant phase space.
NAMCG: the compensating rotation is an isotropy of the background and rigid on the matrix index
("not a local rotation of the matrix index", appH L469); R3 shows rigid index rotations are *null*
insertion directions, so no such charge can arise from the insertion identity; the $r$-family densities
$L_r$ agree with $L_0$ only on the stated background class (L462), the term $Y(\phi,\mathcal L_\xi X)=Y(\phi,\delta_\varepsilon X)$
does not drop out and $r$ is not selected (L471). The existence of an analogous local symmetry on matrix
data is exactly what Problem D would have to supply. The insert states this; nothing is imported.
Chen2022 (already in bib, JHEP 04 (2022) 076, doi 10.1007/JHEP04(2022)076) was re-checked against arXiv
2202.00680 and remains consistent; it is not re-cited by the insert.

Citation hygiene respected: the insert cites none of Lewkowicz–Maldacena, Donnelly–Wall, Solodukhin (so the
known ID traps 1307.2892 / 1512.00013 do not arise), cites no Chae2023 or Bulanikov–Sukhbaeva, and does not
cite 2608.29688 (read-before-cite rule: it was not read, so it is not cited). `Makeenko–Migdal` was **not**
independently verified and is therefore not cited (the loop-equation method reference used is
EynardOrantin2009, DOI-verified).

### Comparison with the original target

Original target: derive $\delta S_D=0$ for fixed-volume tensor-block variations from the microscopic
dynamics. This proposal does **not** deliver it. It (i) makes the disclaimed measure item precise (R1),
(ii) proves the loop-equation route cannot supply the edge coefficient along the symmetry directions the
manuscript actually uses (R3), and (iii) proves by exact computation that within the Gaussian conical-contact
class stationarity is an extra linear condition, not an SD consequence (R4). Per the task specification this
bounded obstruction ("the loop equations do NOT localise to the block functional under the stated hypothesis
class") is the honest P1 outcome.

## Claim classification

- R1 insertion identity: **established** (elementary differentiation under the integral; script residual 0).
- R2 SD kernel (general): **established** (integration by parts, boundary decay); the script check is an
  **established** instance on explicit rational data.
- R3 algebra ($\operatorname{tr}B=0$, $\operatorname{tr}\operatorname{ad}_\Lambda=0$, Jacobian $=1$):
  **established** (symbolic + deterministic numeric with error bounds in output).
- R3 identification "compensating rotation $\Rightarrow X\mapsto e^{tB}X$ at matrix level":
  **conditional** on the natural lift of the Poisson-limit statement appH L469; flagged in the insert.
- R3 conclusion "$-4\kappa_X$ not producible along those directions": **conditional result** on R3 + the
  stated lift; consistent with and sharpening appH L462.
- R4 family $A_n=A_1+(1/n-n)P+\varepsilon B$: **model (phenomenological encoding)** — same $n$-structure as
  the manuscript's flat-cone coefficient (established match, Check 4(e)), but the NAMCG block's contact
  encoding is not shown to be of this form; flagged.
- R4 closed form, non-vanishing, hyperplane: **established derivation** (exact, symbolically verified).
- R5 ranked avenues: **unresolved steps** (1,2,3,4,5,6,7 all uncomputed in the package).
- R6 literature statements: **established** as descriptions of the cited papers (abstracts verified);
  their status for NAMCG is **input / not imported**.

## Proposed changes

### File 1: `chapters/appH-microscopic-proofs.tex` — one insertion, nothing else

- **Anchor (verified once, at line start):** `\section{Problem C: conformal mode and Cassini}`
  (occurrences: 1; appH L479). This is the end of the Problem B section, immediately after the paragraph
  that contains the disclaimed item at L477.
- **Operation:** insert the block below **immediately before** that anchor line. No sentence is deleted or
  modified. All existing text, including the L477 disclaimer ("the measure of the matrix integral" item,
  which remains accurate: the Moyal/Chen-type Jacobian term is still computed nowhere) and the L462
  conclusion, is kept. No status/priority/completion text is touched (verified: the 4000-byte window from
  the `\section{Problem B` header is byte-identical pre/post).
- The insert is LF-only in the proposal folder; the integrator splices with CRLF conversion. It contains no
  `\label`, uses only `\eqref{eq:Smatrix}` (label verified unique, ch03 L143), `\ref{ass:EE}` (ch06 L71),
  and cites only keys added in File 2. Paragraph titles ("Schwinger--Dyson insertion, measure Jacobians and
  null directions of the replica functional", "Nearest published statements and the reduced-action charge
  mechanism") were grepped: no collisions with any existing `\paragraph` title.

Insert (LF form, 6,668 bytes, sha256 `46a385840371e54af11590a143faf5cac3df58eb84b490c995a96381bfa051d3`):

```latex
\paragraph{Schwinger--Dyson insertion, measure Jacobians and null directions of the replica functional (conditional; not closure).}
Let \(Z_n(\varepsilon)\) be the replica functional of the paragraph on the replica insertion identity, built from the matrix data of Equation~\eqref{eq:Smatrix} at finite \(N\) and Presentation~A: \(\varepsilon\) deforms a datum of the block or of the induced density and the insertion is \(\mathcal I_n=\partial_\varepsilon S_{E,n}\). Writing the integrand as \(j_\varepsilon\,e^{-S_{E,\varepsilon}}\), with \(j_\varepsilon\) the ratio of the integration measure to the reference matrix measure, differentiation under the integral sign gives, at finite \(N\), the exact identity
\[
  \partial_\varepsilon\ln Z_n=-\langle\mathcal I_n\rangle_n+\langle\partial_\varepsilon\ln j_\varepsilon\rangle_n\,,
\]
and the Schwinger--Dyson (loop) equations of the matrix integral~\cite{EynardOrantin2009}, \(\langle\mathcal V(S_{E,n})\rangle_n=\langle\operatorname{Div}\mathcal V\rangle_n\) for compactly supported vector fields \(\mathcal V\) on the matrix entries, give zero expectation to every equation-of-motion insertion and reduce insertions to contact terms. For the flat Lebesgue matrix measure of Equation~\eqref{eq:Smatrix} the Jacobian term vanishes identically; for Moyal corrections, field redefinitions and the measure of the matrix integral disclaimed in the preceding paragraph it must be retained, and it is not computed anywhere in this book.

Two consequences bound what the loop equations can supply for Problem~B. (i)~Unimodular deformations are null directions: if the \(\varepsilon\)-dependence is generated by a divergence-free field redefinition, then every \(Z_n(\varepsilon)\) is \(\varepsilon\)-independent and \(\langle\mathcal I_n\rangle_n=-\langle\partial_\varepsilon\ln j_\varepsilon\rangle_n=0\) for every \(n\). The compensating rotation acts as \(X^a\mapsto e^{tB}X^a\) with \(B^a{}_b=\partial_b\xi^a\) antisymmetric in \(\eta\), hence \(\operatorname{tr}B=0\) and \((\det e^{tB})^{N^2}=1\) over the \(N^2\) matrix entries, and the adjoint flows \(X\mapsto e^{t\Lambda}Xe^{-t\Lambda}\) have \(\operatorname{tr}\operatorname{ad}_\Lambda=0\) (exact checks). The coefficient \(-4\kappa_X\) required in the paragraph on the matrix gauge realisation cannot therefore be produced by the insertion identity along a compensating rotation or an adjoint flow, which sharpens the recorded conclusion that this coefficient is a property of the modular Hamiltonian of the state at \(\Sigma\), or of a local symmetry under which the compensating rotation would be a gauge transformation, and not of the induced density. (ii)~The loop equations do not imply stationarity even at Gaussian order: for the conical-contact family \(A_n=A_1+(\tfrac1n-n)P+\varepsilon B\) of the block quadratic form, with \(P\) supported at the branch locus (the same \(n\)-dependence as the flat-cone coefficient of the paragraph on the replica cone coefficient), the identity above gives exactly
\[
  \partial_\varepsilon S_D=\operatorname{Tr}(G_1BG_1P)-\tfrac12\operatorname{Tr}(G_1B),\qquad G_1=A_1^{-1},
\]
which is nonzero for a generic block deformation \(B\) and vanishes only on the codimension-one hyperplane \(2\operatorname{Tr}(G_1BG_1P)=\operatorname{Tr}(G_1B)\). In this class \(\delta S_D=0\) is a linear condition on the deformation, a linearised block equation together with a contact term at the tip, and not a consequence of any Schwinger--Dyson identity. These statements are for finite \(N\), the Gaussian conical-contact class, the flat matrix measure of Equation~\eqref{eq:Smatrix}, Presentation~A and the fixed-geometry, fixed-measure replica prescription of the paragraph on the replica insertion identity, into which the conical-locus contribution enters through \(S_{E,n}\); they do not give the locality or large-\(N\) factorisation that would turn contact identities into a Ward identity of the block, do not establish fixed-volume stationarity of the tensor block, and do not select the edge term.

\paragraph{Nearest published statements and the reduced-action charge mechanism (conditional; not closure).}
The nearest published analogues compute entanglement of matrix degrees of freedom rather than the response of a block to fixed-volume deformations: target-space entanglement of eigenvalue subregions with qualitative area agreement in the bubbling-geometry matrix model~\cite{TsuchiyaYamashiro2022}; momentum-space entanglement on fuzzy spheres~\cite{KawamotoKuroki2021}; perturbative interaction corrections to entanglement on fuzzy spaces, which are bulk-extensive and do not obey a pure area law~\cite{AlloucheDou2026}; the entanglement of the black 0-brane with its Hawking radiation in the BFSS model~\cite{ChoudhuryLaurenzano2024}; and the \(c=1\) string, where a dilaton-dependent area-like term is expected in the generalised entropy of bulk subregions but no singlet-sector mechanism accounts for it~\cite{Craps2026}. None of these treats fixed-volume variations of a non-conformal block, and none supplies the missing step of Problem~B. On the continuum side, the first law and equilibrium statements for causal diamonds~\cite{JacobsonVisser2019,Svesko2019} and the type-II-algebra realisation of a variant of the entanglement equilibrium hypothesis~\cite{JensenSorceSperanza2023} presuppose an existing metric or a geometric modular flow, an input that a derivation of Assumption~\ref{ass:EE} from Equation~\eqref{eq:Smatrix} must not use. For the edge-term bookkeeping, the published mechanism nearest to the \(r\)-family argument is the charge mechanism of Einstein--aether thermodynamics: the first law of stationary black holes carries an irreducible entropic aether contribution~\cite{ArataLiberatiNeri2026}, and the additional first-law term of misaligned universal horizons is the Noether charge of a genuine local symmetry \(\delta u^a=f\,a^a\) of the reduced, elliptic gauge-fixed action~\cite{ArataIsmailLiberati2026}. The NAMCG situation is the mirror obstruction, not an application of this mechanism: the compensating rotation is an isotropy of the background and not a local rotation of the matrix index, the densities \(L_r\) agree with \(L_0\) only on the stated background class, the term \(Y(\phi,\mathcal L_\xi X)\) does not drop out of the charge, and no local symmetry of the matrix data carries the coefficient \(-4\kappa_X\); the existence of such a symmetry belongs to Problem~D. These identifications record what the published mechanisms do and do not supply for Problem~B; no result is imported into the matrix theory. Problems~B and~D remain open and PROGRAMME-CONDITIONAL.
```

### File 2: `bib/namcg.bib` — append only

Append the 11 verified entries in `bib_additions.bib` (3,631 B, sha256
`d9f83e00b3e5f5be8c6da25b3005701abdf45a647b84556f1e1b8202ba8e3b95`, reproduced verbatim in that file; keys:
ChoudhuryLaurenzano2024, TsuchiyaYamashiro2022, KawamotoKuroki2021, AlloucheDou2026, Craps2026,
EynardOrantin2009, JacobsonVisser2019, Svesko2019, JensenSorceSperanza2023, ArataLiberatiNeri2026,
ArataIsmailLiberati2026). No key collides with the current 88-entry bib (verified; and no collision among
the new keys). EynardOrantin2009 deliberately has **no eprint** (arXiv record not independently fetched;
Crossref/DOI verified).

### Predicted post-states (asserted by `simulate_apply.py`, reproducible)

- `chapters/appH-microscopic-proofs.tex`: **589,389 B, CRLF 3450, bare LF 0, sha256
  `46ba16b9398ec63c1f70f8cabb046803968f635dc9aa029ee827b55fe1ebf26b`**.
- `bib/namcg.bib`: **31,789 B, CRLF 1050, bare LF 0, sha256
  `9e9dfa0617f90b9dae1dd3c94eabd584a22db3cd18c138719e91d7b46b9b6429`, 99 entries**.

### Stale passages elsewhere

None found. ch17 L134–137 (B closure) and L671–673 (A-dependency) are unaffected: the insert claims no
closure and no dictionary bypass. appH L477 and L462 remain accurate. No other file changes.
(ch17, ch03, ch05, ch06: no edits.)

## Verification scripts

All in this folder, run with `python -I`, deterministic (fixed dps, fixed series lengths, permutation
determinant, exact rationals; no timestamps or absolute paths in outputs):

- `derive_ward_r1.py` (9,609 B, sha256 `041a0e47f06dc56d8a1e3815665a4fe1bab0a5fb2b57fb5d1054a13c8b484fda`)
  / `derive_ward_r1.out` (2,400 B, sha256
  `6655d85b1b49d3877c9bb0a4b38eabc23e68723b01fbe2799f73d153117d3268`): Check 1 insertion+Jacobian identity
  (residual 0); Check 2 SD kernel on explicit rational Gaussian (EOM insertions 0, contacts $\delta_{ki}$,
  traceless-field insertion 0); Check 3 unimodularity (general $\mathfrak{so}(1,3)$ generator $\operatorname{tr}B=0$,
  $\eta$-antisymmetry residual, $(\det e^{tB})^{N^2}=1$, concrete $\det(e^B)-1=4.6\cdot10^{-41}$; general
  $\operatorname{tr}\operatorname{ad}_\Lambda=0$, sample $9.6\cdot10^{-34}$); Check 4 conical Gaussian family
  (a)–(e) as above. Summary: ALL PASS.
- `simulate_apply.py` (3,625 B, sha256 `6f9e685ea6a0d1534a2b72bb8613134ecb44cf0ab28cc0329b7b8c9cf92ea0f4`)
  / `simulate_apply.out` (1,204 B, sha256 `0381bb749500f6b35877bbebd0c8219b479e7d52d729f41c14694956cea802ba`):
  asserts certified pre-states; anchor uniqueness and line-start; insert CR-free, label-free,
  newline-terminated; byte-exact splice; Status-B window unchanged; bib key-collision checks; predicted
  post-states above. Read-only (in-memory simulation; verified twice, outputs byte-identical).
- `citecheck_arxiv.xml` (22,562 B, sha256 `9239f5f90f73bda7f0869ad9096fae30a2cf6c661f951b1e241afd1b66ae1ee6`)
  and `citecheck_arxiv.out` (13,505 B, sha256
  `fa556a905142cd27d54875f0296d2d4f7d4cbf2a7a6aa079173773ffb204461b`): raw arXiv API responses (title/author/
  journal-ref/DOI/abstract) for the 10 arXiv-bearing records, formatted.
- `citecheck_eo.json` (18,438 B, sha256 `29c11b76c2436112dc53ff620d103669e0ccfaaae8b5662109056ca8ea9df8d8`):
  Crossref record for Eynard–Orantin 2009 (DOI, journal, volume, pages).

## Decisions Taken

- **Single splice at the end of Problem B** (before the Problem C section header) for both paragraphs,
  instead of splitting P1 near L179/L477 and P2 elsewhere: both address the same target B.ward, the anchor
  is unique, and one status block per contiguous insertion is preserved. Rejected: interleaving into the
  L179 paragraph (would edit existing prose; task prefers minimal insertion).
- **P1 outcome reported as a bounded obstruction, not dressed as a sub-lemma of stationarity.** Task
  directive; the manuscript wording says "not a consequence of any Schwinger--Dyson identity" and scopes
  every statement to the named hypothesis class.
- **General SD kernel proved by parts in prose; script check on explicit rationals.** General-symbolic
  sympy integration was computationally intractable (nested general-symbolic integrals hung; two attempts
  killed). Explicit rational data + the elementary parts argument is the honest pairing; disclosed to the
  gatekeeper.
- **EynardOrantin2009 as method reference only, DOI-only bib entry.** Its arXiv record was not fetched;
  no eprint is added. Makeenko–Migdal not verified, not cited.
- **`Craps2026` key and author escaping** (`Vilar L{\'o}pez, Alejandro`) follow the first-author/year
  convention of the bib; record verified.
- **Wording "fixed-geometry, fixed-measure replica prescription of the paragraph on the replica insertion
  identity"** replaces my earlier coinage "fixed-state replica prescription" to mirror appH L179's actual
  list (geometry, branch locus, conical-locus data, integration measure), avoiding a term the manuscript
  does not define.
- **"only on the stated background class"** (not "stationary class") for $L_r=L_0$, matching appH L462's
  "equal to \(L_0\) on the class"; final wording check re-ran the simulator (insert 6,668 B; new appH post
  hash 46ba16b9…).
- **No eprints added to LM / Donnelly–Wall / Solodukhin** (hazard: bib carries none; none are cited).

## Milestone assessment

Routine. No MILESTONE.md trigger: B stays OPEN (no closure, no new critical-path completion, no definition
or assumption changed). The result is a bounded obstruction + sub-lemmas occupying L477's disclaimed item;
the no-go is scoped and forked (ranked open avenues in R5), per the author's "no-go is a fork" directive.

## Status-label recommendation

Re-derived from ch17 and the current ledger: critical path = A, B, C, D1, E, F, G-derived, N.
**All labels unchanged.** Problem B: OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. Problem A: OPEN (B's
dependency per ch17 L671–673 unchanged). Problem D: unchanged. Proposed label changes: none.

## Author decision needed

None.

## Remaining open step

To close the original B target (fixed-volume $\delta S_D=0$ for the tensor block from the microscopic
action, with the specified $g^{(0)}\mapsto g$ map and no pre-existing metric) all of the following remain:

1. Compute the measure Jacobian $\langle\partial_\varepsilon\ln j_\varepsilon\rangle_n$ for the actual
   (Moyal/Chen-type, non-flat) matrix measure — the disclaimed item, still computed nowhere.
2. Derive locality/factorisation (Problem A / `ass:map`) that would promote contact identities to Ward
   identities of the block (finite $N$ identities alone provably do not, in the Gaussian conical class).
3. Show the actual block's contact encoding is (or is not) of the conical family, and evaluate
   $\partial_\varepsilon S_D$ for the NAMCG block beyond the Gaussian model.
4. Supply the edge coefficient: either a property of the modular Hamiltonian of the state (state-side
   route; action insertions provably fail along rigid/adjoint directions) or a genuine local symmetry of
   the matrix data carrying $-4\kappa_X$ (Problem D).
5. The $g^{(0)}\mapsto g$ map (L151–154) and the selection of $r$ / removal of
   $Y(\phi,\mathcal L_\xi X)$ (L471).

## Special instructions for the gatekeeper

- Re-run `python -I derive_ward_r1.py` and `python -I simulate_apply.py`; outputs must match the `.out`
  files byte-for-byte.
- Re-derive Checks 1–4 independently: the closed form
  $\partial_\varepsilon S_D=\partial_n\langle\mathcal I_n\rangle_n|_1-\langle\mathcal I_1\rangle_1
  =\operatorname{Tr}(G_1BG_1P)-\tfrac12\operatorname{Tr}(G_1B)$ (note the second term comes from the replica
  normalisation $\partial_\varepsilon\ln Z_1=-\langle\mathcal I_1\rangle_1$, not from the $c(n)P$ contact).
- The insert must NOT be read as closing B, deriving $\delta S_D=0$, selecting the edge term, or supplying
  the $g^{(0)}\mapsto g$ map; it is scoped to the named hypothesis class and says so in one closing sentence
  per paragraph.
- The claim that $-4\kappa_X$ cannot arise along compensating/adjoint directions is conditional on the
  stated lift of the compensating rotation to $X\mapsto e^{tB}X$; check the conditional wording in the
  insert is adequate ("acts as ... antisymmetric in \(\eta\)" — appH L469 is the source of the rigid
  rotation statement).
- Verify the 11 bib records against `citecheck_arxiv.out`/`.xml` and `citecheck_eo.json`; EynardOrantin2009
  is DOI-only by design.
- Hazard list respected by construction: no Seiberg/Ho–Kawai–Steinacker closure-by-scope (neither cited in
  the insert); ch17 L134–137 untouched; no thermodynamic upgrade of L473–475 analogy language (the insert
  adds no thermodynamic claim); citation-ID traps avoided (no LM / Donnelly–Wall / Solodukhin cites or
  eprints); Chae2023, Bulanikov–Sukhbaeva not cited; 2608.29688 not cited; no status/priority/completion
  edit (byte-window check); no invented numbers (every numeric in the insert is either from the manuscript
  or from the scripts).
- Makeenko–Migdal: not independently verified, deliberately not cited — do not request its addition.
