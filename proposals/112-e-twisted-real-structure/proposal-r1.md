# Proposal 112-e-twisted-real-structure, round 1

RECORD package: no manuscript-bound LaTeX text (see "Manuscript landing note").
Source reading: digest (CURRENT, head 23266972cd07; dirty-chapters: yes, the two
expected uncommitted integrations, ordinals 40-41) + targeted reads of the Problem
E entry windows L1657-1700, L1700-1752, L1757-1759, L1774-1831, L1905-1909,
ch17 L394-399 and L717-724, ch04 L322-328, frontier.yaml L1466-1512,
sme-scout-20261121 L30-68, plus live arXiv fetches of the two literature anchors.

## Claim

Target. Problem E (signature), appH `sec:status-E` (L1657-1909). Ledger wording,
quoted verbatim (whitespace-normalized) from L1661-1664: "Status: OPEN. Priority:
CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A
scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or
matrix-derived Lorentzian signature." Chapter 17 states the criterion (L721-722):
"Problem~E: Lorentzian signature is derived rather than retained (Assumption~
\ref{ass:lorentzian})", and (L394-399) that Euclidean positivity and a formal Wick
rotation do not select it. Dependencies: E is not gated on A, B, C, D1, F, G, N;
E gates the matrix-derived label itself (ch17 L721). No status, priority or
completion label is changed or proposed for change by this package.

Dispatch authority. `reports/graph/frontier.yaml` L1470-1472 records E as
"blocked_by: author-direction pause" with the 060-review unblock list (thimble/
intersection control, signed-Pfaffian N>=3, large-N singlet positivity);
`reports/ledger.md`:1436 records the E twisted-real-structure edge as "offered,
not dispatched"; `reports/sme-scout-20261121-faster-routes.md` (L61, L66) ranks
"E via Nieuviarts-style twisted real-structure selection" as the top E route.
This package is that edge, dispatched by the orchestrator on 2026-11-22 under the
author's standing autonomous-mode directive. It attacks the real-structure side
of E, complementary to the 060 list's contour side; it does not replace it.

Central result (one sentence). The signature-emergence mechanism of Nieuviarts
(arXiv 2502.18105; proceedings arXiv 2512.15450, both verified live this pass)
uses no measure- or state-positivity and so is NOT obstructed by the recorded
N=2 reflection-positivity failure (appH L1696-1752) - but its signature content
is the choice of an involutive reflection r (equivalently a self-adjoint unitary
K with rho = Ad K), which its own Section 5 states is not derived from the
algebraic constraints, and this package derives that no realization of such a
twist on the N=2 NAMCG data can supply the missing selection: conjugation-type
twists preserve the Clifford form carried by the supplied fermions (E4),
real-index automorphisms never move a positive form to eta (Sylvester, E5),
and the complex-index orbit that does reach eta is invisible to the contour
integral, whose admissible class has both the Riemannian and the Lorentzian
real slices on its boundary (E6, restating the established appH L1823(i)). The
real-structure selection available on the N=2 data is therefore exhausted by
the recorded Majorana-Weyl dichotomy t in {1,5,9} (appH L1829) intersected with
the contour class {0,1,9,10} (L1823) giving t in {1,9} with invisible overall
sign (L1831): the transplant (option (c) of the mission brief) yields a bounded
no-go for the twist class plus a narrowing - the missing datum of E is a
real-slice (contour or vacuum) selection, not an algebraic twist.

Not claimed. No closure or partial closure of E; no derivation of a signature,
background, frame, real-time response or fermion content; Assumption
`ass:lorentzian` (ch04 L322-328) is not discharged. The result is bounded to
its hypothesis class (see "Result classification" E7) and does not reach H/I/J.
## Inputs

Manuscript (labels verified present; passages read in full at the given lines):
- appH L1658 `sec:status-E`; L1661-1664 ledger label (quoted above); L1670-1695
  regulated Lorentzian integral, definitions (A)-(C), contours R_u, the proved
  statement that within its class the regulated integral "carries ... no datum
  beyond the Euclidean model" (L1685); L1907-1908 Status: "Remains
  Assumption~\ref{ass:lorentzian}."
- appH L1696-1752 reflection-positivity paragraph: theta = diag(-1,1,...,1);
  normalized pairing <f,f>_theta = (int |f_+|^2 w - int |f_-|^2 w)/int w; every
  theta-odd invariant polynomial (Tr A0 Ai; Tr([A0,Ai]Aj)) has strictly negative
  reflected value; the recorded measures "do not satisfy the reflection
  positivity of \cite{OsterwalderSchrader1973,OsterwalderSchrader1975} on the
  invariant polynomial algebra" at N=2 with p=4 content, and bosonically with a
  mass at every finite N; exclusions kept verbatim in mind: signed Pfaffian
  N>=3, large-N singlet algebra, other involutions, non-polynomial test
  algebras, thimbles, the slice bridge (L1744-1747).
- appH L1774-1794 linear contours: h = Lambda^T eta Lambda, class
  C = C_0 ∪ (-C_0); at N=2 S_b is determined by h alone (L1775 formula).
- appH L1796-1807 regulator rigidity: damped absolutely-convergent linear
  contours lie in C_0 (algebraic at every N, proved at N=2); -C_0 contours
  compute observables at imaginary momenta (L1805); "the inertia ... is that of
  the eta put into S_b, which the regulator carries over to every admissible
  contour but does not select" (L1807).
- appH L1820-1831 other-signature contractions: real invertible boundary points
  of C_0 are exactly the forms with t in {0,1,9,10} negative eigenvalues, and
  all occur, "T^T T is the limit of e^{i theta} T^T T in C_0 ... and eta is the
  limit of the R_u" (L1823(i)); rigidity of 2<=t<=8 (L1825(ii)); Majorana-Weyl
  exists in signature (s,t), s+t=10, iff s-t = 0 mod 8, i.e. t in {1,5,9}
  (L1829(iv), citing VanProeyen1999); dichotomy "(P1) ... (P2) ... Then t in
  {0,1,9,10} ∩ {1,5,9} = {1,9} ... S_b does not see the sign ... both premises
  are imposed, and Assumption~\ref{ass:lorentzian} is not discharged" (L1831);
  the induced tensor of `def:matrix-coords-ext` (ch03 L173) is the pull-back of
  h0 by a configuration.
- ch04 L322-328 `ass:lorentzian`: "The locked vacuum is Lorentzian:
  \eta_{AB}=\mathrm{diag}(-1,+1,+1,+1). Dynamical emergence of this signature
  from a Euclidean matrix model is not proved in the source notes and is not
  pretended here."
- eq:Smatrix (ch03 L143) is bosonic (relied on as stated at appH L1831).

Literature (both anchors verified live on arXiv abs pages this pass; mechanism
extracted from the arXiv HTML of 2502.18105, full text, both halves):
- G. Nieuviarts, "Emergence of Lorentz symmetry from an almost-commutative
  twisted spectral triple", arXiv:2502.18105 [math-ph] (no journal reference
  shown on the abs page).
- G. Nieuviarts, "Emergence of Time from a Twisted Spectral Triple in
  Almost-Commutative Geometry", arXiv:2512.15450 [math-ph], v1 17 Dec 2025,
  v2 11 May 2026 - the recorded follow-up exists; it is a proceedings write-up
  of the same mechanism (used for existence only; all mechanism quotes below
  from 2502.18105).
Mechanism, as extracted (quotes verbatim from the HTML): rho ∈ Aut(A) with
rho(a†) = (rho^{-1}(a))† (2.1), rho(J) = eps J (2.4), rho^2 = id, implemented
by a unitary K with rho(·) = K(·)K†; the "fundamental twist" (Def. 2.3)
requires K = K†; twisted commutator [D,a]_rho = Da - rho(a)D (2.2); twisted
first-order condition [[D,a]_rho, b°]_{rho°} = 0 (2.5); the K-product is
"Hermitian and indefinite if and only if K = K†" (2.16-2.17); at the Clifford
level rho(e_a) = e_a† = ±e_a on the metric ± sectors (3.35) and K is a product
of gammas over the negative directions (3.68); the signature-change morphism is
g(·,·) →_Phi^K g(·, r·) with r the "spacelike reflection" (4.15), acting "in
the same manner as a Wick rotation"; Section 5 derives O = O†, JO = eps OJ,
Gamma O = eps' O Gamma (Prop. 5.1) and sets O = K = K† (5.7), but "the
algebraic constraints ... do not pin down how many eigenvalues of K are ±1";
the KO-dimension choice is "motivated by physical considerations"; "the
spacelike reflection r - and hence the choice of K - remains an additional
input"; no Osterwalder-Schrader or measure/state positivity appears anywhere.
## Derivation

Setting. N = 2, IKKT content with input symmetric form h0 on the index space
V = R^10 (h0 = eta in the manuscript), traceless Hermitian A_mu, colour-adjoint
index a = 1,2,3; fermion operator M(A) = Gamma^mu ⊗ ad(A_mu) on a supplied
spinor space S carrying {Gamma^mu, Gamma^nu} = 2 h0^{mu nu} (this pairing of
Clifford form with contraction is premise (P2), appH L1831); observable algebra
= invariant polynomials, Weyl-generated by Gram entries and epsilon
contractions at N=2 (appH L1726-1728). The proved identity Pf M = c_P (det G)^4,
G_ab = h^{mu nu}... G_ab = eta^{mu nu} A^a_mu A^b_nu (appH L1675), exhibits the
fermion weight at N=2 as a function of the fermion Clifford form alone.

(E1) Where signature lives in the N=2 data. Exactly three objects carry it,
each already recorded: the input form h0 in S_b; the Clifford pair (S, Gamma)
over h0, i.e. the supplied content (P2), since eq:Smatrix is bosonic; and the
choice of contour class C_0 vs -C_0 (the real slice / sign of the imaginary
part, appH L1796-1807). The strongest existing statement is the dichotomy:
under (P1) contour representability and (P2), t in {1,9}, overall sign
invisible because S_b is even in h0 (L1831). Nothing in the manuscript derives
any of the three. (Tier: established restatement of appH.)

(E2) What Nieuviarts derives and what it inputs (verified quotes, Inputs).
Derived: the compatibility conditions on K (self-adjointness, intertwining of
J and Gamma). Input: the reflection r, i.e. the ±1 splitting of the vector
generators that rho implements ("rho(e_a) = g_a e_a", 3.35; r is "an additional
input", Sec. 5). Hence the mechanism relocates the signature datum from the
metric to the chosen twist; it does not produce the datum. It never uses
positivity of a measure or state: the K-product is indefinite by construction
("indefinite if and only if K = K†"). (Tier: verified literature statement.)

(E3) Transplant dictionary. Matching (E1) and (E2) on the NAMCG side: the
Nieuviarts derived-compatibility half has an exact analogue in the recorded
Majorana-Weyl existence dichotomy t in {1,5,9} (appH L1829) - a real-algebraic
consistency condition that prunes the set of signatures but does not fix it;
the Nieuviarts input half (choice of r) has as its NAMCG analogue the choice
of real slice / contour class and the invisible 1-vs-9 sign. Both mechanisms
derive a reality condition and retain a signature choice; the match is exact
and neither side closes E. (Tier: mechanism - my construction.)

(E4) Conjugation-twist lemma. A twist realized on the spinor space as
Gamma(v) -> K Gamma(v) K^{-1}, K in GL(S), preserves the Clifford form:
{KGamma(v)K^-1, KGamma(w)K^-1} = K{Gamma(v),Gamma(w)}K^-1 = 2 h0(v,w) id
(two-line algebra; symbolic check run 7, defects identically zero for general
complex 2x2 K on the Cl(1,1) toy). So no conjugation-type twist of the fermion
operator M(A) can change h0: it preserves the very datum E must derive.
Changing the signature of h0 requires a different Clifford representation
class, which conjugation cannot produce: for t = 0 the volume element has
omega^2 = (-1)^{45+t}|det h0| = -1 (runs 1-5), so no chirality operator exists
and the supplied 16-component Majorana-Weyl content cannot be realized on
Riemannian data at all - the recorded VanProeyen rule, reproduced from the
real-structure side. (Tier: established derivation + standard Cl-table input,
same source appH cites.)

(E5) Automorphism orbits of the N=2 data. The automorphisms of the data
(polynomial configurations with the given Clifford/contraction coupling) act
on configurations as index GL(10) maps A -> Lambda A and colour GL(2) adjoint
maps; colour acts through SO(3,C) on the Killing-orthogonal colour indices and
fixes every Gram contraction, so signature selection can only live on the
index factor. Over the reals, h0 -> Lambda^T h0 Lambda preserves signature
(Sylvester; run 8), so no real-data twist carries a positive form to eta.
Over the complexes it reaches: Lambda = diag(i,1,...,1) satisfies
Lambda^T eta Lambda = 1 and Lambda^T 1 Lambda = eta (run 6), i.e. eta and the
Riemannian form are real forms of one complex congruence class - Wick rotation
as complex orthogonality. (Tier: established.)

(E6) Class blindness of the contour integral. Established (appH L1823(i)): the
real invertible boundary points of the regulator class C_0 are exactly the
forms with t in {0,1,9,10}, and both the Riemannian point T^T T (t=0) and eta
(t=1) occur as boundary limits within C_0 ("T^T T is the limit of
e^{i theta} T^T T in C_0 ... and eta is the limit of the R_u"). Established
(appH L1685): within its class the regulated integral "carries ... no datum
beyond the Euclidean model". Deduction: every quantity the class-C contour
integral can supply is class-level data, and both real slices lie on the
boundary of one class, so no choice within C separates Riemannian from
Lorentzian real slices. The move that does separate them is a complex
congruence (E5, run 6) - a choice of real form inside one complex class,
i.e. Nieuviarts' r seen from the contour side. Hence the sub-lemma sought in
`reports/sme-scout-20261121-faster-routes.md` (L66: a theorem that the
twist/contour choice "is selected by the action's positivity structure") is
false in the named class C: the class is blind, and no positivity structure
internal to it can select. Separation needs data from outside C (thimble
intersection data) or a state (vacuum). (Tier: conditional - deductive
consequence of the two quoted established statements.)

(E7) Confrontation with the recorded RP no-go, and the bounded statement.
The OS reflection-positivity route dies on the invariant polynomial algebra
at N=2 (appH L1696-1752: theta-odd invariants strictly negative). The twist
route is NOT obstructed by that no-go: it asks no positivity at all - the
indefinite K-product is the target signature input as data, not a derived
property (2.16-2.17). The two failures are complementary: RP fails at the
measure; the twist fails at the input r. Bounded no-go. Within the class of
(i) N=2 IKKT data with invariant-polynomial observables (Weyl generators),
(ii) the supplied IKKT Majorana-Weyl fermion content (P2), (iii) linear
contours in regulator class C, (iv) twists realized as automorphisms of the
index/colour data or as spinor-operator conjugations, E's signature
selection is unobtainable: (E4) kills spinor-conjugation moves (they
preserve h0), (E5) kills real data moves (Sylvester), (E6) kills
contour-class moves (class blindness); the only orbit representative that
reaches eta (complex Lambda) supplies no datum to the class-C integral.
Excluded by the bound: thimbles/nonlinear contours (E6 is stated for C);
signed-Pfaffian N>=3 and large-N singlet algebra (the appH class and
integrability statements are N=2); vacuum/state selection (a state, not an
integral datum); the L1744-1747 exclusions carry over verbatim; loop terms.
(Tier: bounded no-go, conditional on E4-E6 and the quoted appH statements.
The "not blocked by RP" clause is an established observation: a proof of
absence of a premise.)

(E8) Net real-structure constraint on the N=2 data. Weyl requires t odd
(runs 1-5); Majorana-Weyl gives t in {1,5,9} (L1829); the contour-class
boundary gives t in {0,1,9,10} (L1823(i)); intersection t in {1,9} with the
overall sign invisible to S_b (L1831). E4-E6 add that no further reduction
is possible inside the twist class. The maximal output of real-structure
selection on the N=2 data is the recorded dichotomy; E's missing step is a
real-slice (contour or vacuum) selection, not an algebraic twist. E remains
OPEN and PROGRAMME-CONDITIONAL. (Tier: conditional; the dichotomy itself is
the recorded appH statement, the maximality clause is conditional on E4-E6.)

Recorded script output (e_twist_checks.py, `python -I`, 2026-11-22):
```
run 1: t=0 omega^2=-1 Weyl=N MW=N
run 2: t=1 omega^2=+1 Weyl=Y MW=Y
run 3: t=3 omega^2=+1 Weyl=Y MW=N
run 4: t=5 omega^2=+1 Weyl=Y MW=Y
run 5: t=9 omega^2=+1 Weyl=Y MW=Y
run 6: L^T eta L == 1: True; L^T 1 L == eta: True
run 7: conjugation Clifford defects all zero: True
run 8: T^T T signs all positive: True
MW set (t, 0..10) = {1,5,9} check True; MW cap contour = [1, 9] check True
```

## Result classification (rule 6)

- E1: established identity/restatement (appH ledger, contour and dichotomy
  passages, line anchors above).
- E2: established-as-literature; the two selection quotes verified verbatim
  from the arXiv 2502.18105 HTML this pass; the paper's own theorems not
  re-derived (not needed - the package uses only the absence of a positivity
  premise and the self-declared input status of r).
- E3: mechanism/conjecture (my dictionary; content = E2 + recorded appH
  statements; no new theorem).
- E4: established derivation (two-line conjugation identity; run 7 checks the
  general 2x2 case symbolically) plus standard Clifford-classification table
  inputs (omega^2 formula; MW rule), cited-table input from the same source
  family as appH's VanProeyen1999.
- E5: established (Sylvester law of inertia; explicit complex-orthogonal
  witness, run 6; colour automorphisms fixing Gram contractions is standard
  first Fundamental Theorem content, used only to confine where a selection
  could live).
- E6: conditional - deductive consequence of the two quoted established appH
  statements (L1823(i), L1685); relative to the regulator class C as
  recorded there.
- E7: bounded no-go (conditional, class stated in the item; bound list
  explicit).
- E8: conditional (recorded dichotomy + the maximality clause conditional
  on E4-E6).
No claim in this package is a phenomenological input or a fit; no number in
it is new (every t-set and rule is appH's, reproduced mechanically).

## What this does NOT do

- It does not close or partially close E, and proposes no status, priority
  or completion-label change: E remains exactly as quoted (OPEN, CRITICAL
  PATH for the matrix-derived label, PROGRAMME-CONDITIONAL). If any label
  change ever became warranted, report to author separately.
- It derives no Lorentzian signature, background, frame, real-time response
  or fermion content, and does not discharge `ass:lorentzian` (ch04
  L322-328); the ch04 locked-vacuum Lorentzianity IS that assumption and
  nothing here feeds it.
- It does not compute the composite metric of a derived vacuum (route 1 in
  Dependencies): no derived locked vacuum exists, so its induced tensor
  (`def:matrix-coords-ext`, ch03 L173) has no signature to compute yet.
- It does not touch thimbles/nonlinear contours, N>=3 signed-Pfaffian, or
  the large-N singlet algebra: E6-E7 are stated within class C at N=2, so
  the frontier 060 unblock list (frontier.yaml L1473-1478 region) and the
  appH L1744-1747 exclusions remain open and are untouched by this no-go.
- It says nothing about H, I or J, and feeds no other Appendix H problem.
- It does not claim the Nieuviarts mechanism is wrong or inapplicable in its
  own setting: his output is an almost-commutative triple over a base
  manifold whose NAMCG analogue at N=2 is absent (no continuous coordinate
  algebra for his rho to act on); E2-E6 locate the same selection gap on
  both sides, which is a finding about E, not a defect in the paper.
- It does not claim the complex orbit of E5 is physically irrelevant in
  general - only that it supplies no datum to a class-C contour integral.

## Dependencies and gaps (named, with fix routes)

- g1 = (P1): contour representability of the correlation observables on the
  damped linear class is imposed, not derived (appH L1831 "both premises are
  imposed"). Fix route: the 060 unblock list's contour item (frontier.yaml
  L1466-1512, read this pass: thimble/intersection control, signed-Pfaffian
  N>=3, large-N singlet positivity). E6 constrains its payoff: no
  within-class-C resolution can separate the real slices, so a (P1) route
  must exit C or add a state.
- g2 = sign invisibility: even (P1)+(P2) yields only t in {1,9}; t=1 vs t=9
  is invisible to S_b (evenness, L1831). Fix routes: the vacuum selection of
  g3, or a fermion datum beyond Pf M at N=2 - e.g. a signed Pfaffian at
  N>=3 (an explicitly excluded class, appH L1744-1747).
- g3 = real-slice selection: the narrowing produced by E6-E7 identifies this
  as THE missing datum of E. Ranked open avenues (derivation-first per the
  author directive of 2026-11-20):
  1. Signature of the composite metric from a derived locked vacuum
     (`def:matrix-coords-ext`, ch03 L173): compute the signature of the
     induced tensor from a derived - not assumed - vacuum. Gated upstream on
     D/D1 (no derived locked vacuum yet). The computation must be
     signature-neutral: the ch04 locked-vacuum Lorentzianity IS
     `ass:lorentzian`, so no Lorentzian input may enter it. E4-E6 transfer:
     no data automorphism, conjugation, or contour-class move supplies the
     split - the vacuum must break the blindness dynamically (energetics).
  2. Thimble/nonlinear contours beyond C against (P1): E6 is stated only for
     C, so intersection-theoretic selection data is not yet excluded; this
     is the 060 list's contour item and remains the strongest contour-side
     route.
  3. N>=3 signed Pfaffian / large-N singlet algebra: the appH class and
     integrability statements are N=2 statements; E4 (conjugations preserve
     the Clifford form) and E5 (Sylvester) are structurally N-independent and
     constrain such routes without negating them.
- Upstream transfer: if g3 is attacked at the D/D1 vacuum problem, this
  package says the mechanism cannot be structural (automorphism/conjugation/
  contour class); it must be dynamical selection of a real slice by the
  derived vacuum or by contour data outside C.

## Manuscript landing note

Future passage only; no text drafted (item-111 convention; RECORD package).
If a manuscript note is ever authorized, the natural location is the
Problem E ledger section of `chapters/appH-microscopic-proofs.tex`, as a new
labelled paragraph after the reflection-positivity paragraph (which ends at
the recorded L1752 status sentence, before the linear-contours subsection
heading near L1774 - integrator re-verifies anchors against the current
tree), stating: the twist route bypasses the recorded RP no-go (it uses no
positivity), selection within the E7 hypothesis class is blocked, the
missing datum is a real-slice (contour-or-vacuum) selection, E remains open
and PROGRAMME-CONDITIONAL. A BibTeX entry for arXiv:2502.18105 (full record
drafted only at integration; no journal reference seen on the abs page)
would accompany it. Stale passages: none - the package contradicts no
existing text (E is recorded open; the dichotomy is quoted as recorded; the
sme-scout sub-lemma lives in a scout report, not manuscript text, and its
negative answer holds only in class C).

## Verification scripts

- `C:\Users\redgi\Projects\namcg-lab@gpu\proposals\112-e-twisted-real-structure\e_twist_checks.py`
  - 8 runs plus a summary, one printed line each. Re-run:
    `python -I "C:\Users\redgi\Projects\namcg-lab@gpu\proposals\112-e-twisted-real-structure\e_twist_checks.py"`
    (needs numpy, sympy). Expected invariant output: the block recorded under
    (E8), ending `MW set (t, 0..10) = {1,5,9} check True; MW cap contour =
    [1, 9] check True`. Checks: runs 1-5 chirality existence
    (omega^2 = (-1)^(45+t)) and the recorded MW rule (10-2t) = 0 mod 8 per t;
    run 6 the E5 complex-orthogonal witness Lambda = diag(i,1,x9); run 7 the
    E4 conjugation lemma for GENERAL 2x2 symbolic S (all three Clifford
    defects simplify to zero); run 8 Sylvester numerically for a random real
    T. Tool output is a check, not a proof; the reasoning is (E4)-(E6).
- `C:\Users\redgi\Projects\namcg-lab@gpu\proposals\112-e-twisted-real-structure\assemble_parts.py`
  - byte-assembly of part files into this record; no mathematical content.
- No .tex was written, no build was run, nothing outside this folder was
  touched.

## Decisions Taken

- D1: transplant at the structural level (involution/reflection and its
  realizers on the actual N=2 data), not by packaging NAMCG as an
  almost-commutative spectral triple. Reason: the triple packaging needs
  base-manifold data (continuous coordinates, fixed Hilbert-space
  representation) that NAMCG denies at N=2, and would risk re-importing a
  fundamental background - excluded by the emergence directive. The
  structural level is where the selection gap (E2) is visible and where
  E4-E6 are provable. Rejected: spectral-triple packaging.
- D2: headline = bounded no-go (mission option (c)) + narrowing, not dressed
  as a conditional result (b): no recorded step of E's route receives a new
  derived input from the twist. E4-E6 are kept as positive derived lemmas
  and the open avenues are ranked positive-first per the 2026-11-20
  directive; the no-go is bounded, not a stop.
- D3: E4 classified established (identity is two lines; run 7 covers the
  general 2x2 case), with the Clifford-table facts (omega^2 formula, MW
  rule) flagged as cited-table inputs rather than re-derived from
  real-structure cohomology.
- D4: rejected twisting the composite metric now (r-like reflection applied
  to the induced tensor of `def:matrix-coords-ext`): there is no derived D1
  vacuum to twist and any Lorentzian input to such a move is
  `ass:lorentzian` in disguise.
- D5: rejected importing Nieuviarts' KO-dimension-6 choice ("motivated by
  physical considerations", his words) as a NAMCG premise: it is admitted
  phenomenological input there; using it here would be a fit, not a
  derivation. Used only as evidence (E2) that his side has the same gap.
- D6: proceeded despite frontier.yaml L1470-1472 `blocked_by:
  author-direction pause`, on the orchestrator dispatch of 2026-11-22 plus
  the top-ranked E route in sme-scout-20261121 and ledger.md:1436 ("offered,
  not dispatched") under the standing author autonomous-mode directive; the
  package attacks the real-structure complement of the 060 contour-side
  unblock list and consumes no contour-side premise.

## Milestone assessment

Routine: no MILESTONE.md trigger applies. No critical-path step is derived;
E remains OPEN / PROGRAMME-CONDITIONAL exactly as recorded. The package's
value is a bounded no-go plus a narrowing of E's missing datum, with three
ranked open routes. The gatekeeper decides.

## Status-label recommendation

Current critical-path list re-derived from ch17 L717-724 and the appH ledger
(digest CURRENT at 23266972cd07): A, B, C, D1, E, F, G-derived, N - unchanged
from the dispatch brief; no discrepancy found. Affected labels: none. E's
labels (appH L1661-1664) stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL;
this package proposes no change anywhere.

## Author decision needed

None. (The frontier pause on E is a dispatch question resolved in D6; no
label, scope or core change is implicated. Spacetime remains emergent
throughout: no route proposed here assumes a fundamental metric.)

## Remaining open step

To close E's original target (Lorentzian signature derived rather than
retained, ch17 L721-722) one needs a derived selection of the real slice
that is outside the union of the E7 hypothesis class - concretely at least
one of: (i) a signature-neutral computation of the induced tensor of
`def:matrix-coords-ext` from a derived locked vacuum (requires D/D1), whose
mechanism breaks the E6 blindness dynamically; (ii) a thimble/nonlinear
contour construction in which a real slice is selected by
intersection-theoretic data, together with (P1) for it; (iii) a fermion sign
datum (e.g. the signed Pfaffian at N>=3) that breaks the t=1 vs t=9
invisibility of g2, plus an argument promoting the choice to the dynamics.
Until then E remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL, and
`ass:lorentzian` stands.

## Special instructions for the gatekeeper

- Scope: RECORD package; there is no manuscript-bound text to integrate and
  no build to run. Digest was CURRENT (head 23266972cd07) with the two
  expected uncommitted integrations; targeted reads only - a full scan is
  not triggered (no definition/assumption/scope/status passage is changed).
- Re-check: (a) the E4 conjugation identity and run 7 (general 2x2 symbolic
  S); (b) the E5 witness run 6 and the Sylvester use; (c) E6 strictly
  against appH L1823(i) and L1685 as quoted in Inputs (the argument is
  "class-level data cannot separate two boundary points of one class" - it
  is NOT a transitivity claim under a single contour change, which would be
  wrong because the epsilon-zero integrand depends on the pair of forms
  (Lambda^T h0 Lambda, Lambda^T eta Lambda) and one Lambda cannot
  Euclideanize both sectors); (d) the two load-bearing Nieuviarts quotes in
  Inputs (eigenvalue splitting not pinned down; r "remains an additional
  input") against arXiv:2502.18105; (e) re-derive the intersection t in
  {1,9}.
- Must NOT be asserted from this package: that E is closed or partially
  closed; that the no-go reaches beyond the E7 class (in particular it does
  not close thimble, N>=3, large-N singlet, or vacuum routes); that
  reflection positivity holds anywhere or that the twist route restores any
  positivity; that the twist route derives a signature; that the Nieuviarts
  mechanism fails on its own ground.
