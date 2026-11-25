# Proposal 126-d1-lorentz, round 1 (RESUMED)

Resume note: the prior invocation of this chain completed all investigation, the
verification scripts (A, B, C, all green, runs identical) and compile certificate v2,
then died of context overflow before writing this document. This round (resume1)
re-verified every pinned artifact by hash, re-ran all three scripts from disk bytes
(byte-identical outputs), reproduced the payload and spliced file from the generator
(byte-identical), cross-checked payload claims against the scripts and the manuscript,
and surfaced one sign-convention defect in the certified payload (finding F1 below).
F1 was repaired as payload v2 with a one-clause 86-byte edit and recompiled
externally (certificate v3). No new mathematics was introduced in this round beyond
verification of numbers already asserted (the +/-4 Killing values, checked exactly by
`check_payload_killing_126.resume.py`).

## Result

(1) Obstruction (conditional theorem, hypotheses H1-H5 stated below): take the two
relations of the first-order equivariant class (appH L1617-L1621) over
\(\mathcal A=\mathbb C\) at finite matrix size \(N\), with the \(\mathcal S_{cd}\)
anti-Hermitian (unitary fibre action, boosts included) and \(\eta\) Lorentzian.
The adjoint action of the \(\mathcal S\)-sector is a homomorphic image of
\(\mathfrak{so}(3,1)\) by anti-Hermitian endomorphisms, hence has
negative-semidefinite Killing form; \(\mathfrak{so}(3,1)\) is simple with indefinite
Killing form, so the image is \(0\); the first relation then forces
\(\mathbb D_a=0\) (label map of rank 4), and the \(\mathcal S\)-sector itself
vanishes since \(\mathfrak{so}(3,1)\) is perfect. Hence the only finite-\(N\)
realization of the class data with anti-Hermitian \(\mathcal S\) is trivial: a
nontrivial unitary realization requires \(N=\infty\), and every finite-\(N\)
Lorentzian datum of the class has non-anti-Hermitian (mixed \(*\)) \(\mathcal S\).
The compact fibres used elsewhere in the section (the 059 toy's \(U(1)\), the
reflection paragraph's compact fibres) are not obstructed, because compact algebras
do have negative-semidefinite Killing form.

(2) With the \(*\)-structure relaxed, two exact finite-\(N\) realizations of the two
relations with Lorentzian \(\eta\) are given: the flat \(5\times5\) real affine
\(\mathfrak{iso}(3,1)\) model (\(\mathsf T=\mathsf R=\mathsf F=0\); exact label
Lorentz matrix from \(\mathrm e^{\mathcal S}\mathbb D_a\mathrm e^{-\mathcal S}\);
kinetic/ghost operator vanishes on \(\operatorname{span}\{\mathbb I,\mathcal S,
\mathbb D\}\); centralizer \(\mathbb C\mathbb I\) plus the square-zero
\(\operatorname{span}\{\mathbb D_a\}\)) and the curved \(4\times4\) complex spinor
model on \(\operatorname{Cl}_{3,1}=\mathrm M_4(\mathbb C)\) (\(\mathbb D_a=\gamma_a\),
\(\mathcal S_{cd}=\tfrac14[\gamma_c,\gamma_d]\), sign forced \(s=+1\) twice;
\(\mathsf R_{ab}{}^{cd}=4(\delta\delta-\delta\delta)\), \(\mathsf R_{ab}{}^{ae}=12\delta\),
\(\mathrm{Ric}=-12\eta\) under the manuscript identification at L1628; kinetic
eigenvalues \(3,2,4,1\) on the bivector/pseudoscalar/axial/vector-bilinear sectors
besides \(0\) on scalars; 16 bilinears close with rational constants).

(3) These are consistency and obstruction results at the algebraic level. They derive
no \(\mathrm{SO}(3,1)\) from the matrix algebra or the condensate, construct neither
the locked frame nor its non-degeneracy, and close nothing: Problem D1 remains OPEN,
CRITICAL PATH, PROGRAMME-CONDITIONAL. What they fix is the shape of the remaining
route: at finite \(N\) the D1 fibre data cannot be unitary (mixed \(*\) required), or
the fibre must live at \(N=\infty\), or the carrier must be outside the class-relation
form (composite/bilocal carrier, Problem D1's avenue 2 consumed by 122; the
representation is the relaxed hypothesis, as stated at appH L1614 "The hypothesis
relaxed below is the representation").

(4) Finding F1 (verification, surfaced): the certified payload v1 attributed to "the
class ghost operator" the eigenvalues \(12,8,16,4\); the manuscript defines the
background-gauge ghost operator as \([\hat X^a,[\hat X_a,\cdot\,]]\) (appH L1624) and
\(\hat X_a=\mathrm i\mathbb D_a\) (L1617), so the class ghost is
\(-[\mathbb D^a,[\mathbb D_a,\cdot\,]]\) and its eigenvalues in the spinor model are
\(-12,-8,-16,-4\); the verified eigenvalues \(12,8,16,4\) belong to
\([\mathbb D^a,[\mathbb D_a,\cdot\,]]=4L\), where script C checks
\(L=\tfrac14\eta^{ab}[\mathbb D_a,[\mathbb D_b,\cdot\,]]\) with sector eigenvalues
\((3,2,4,1)\) and kernel the scalars. Payload v2 states the operator as
\([\mathbb D^a,[\mathbb D_a,\cdot\,]]\), "the class ghost operator up to the sign of
\(\hat X_a=\mathrm i\mathbb D_a\)". v1 bytes are preserved and both certificates kept
(see Proposed changes and manifest).

## Target and status

- Problem D1 (frontier edge D1.lorentz), 059-r3 avenue 1 "finite-N Lorentzian-fibre
  class test" (six avenues recorded in the 059 review r3 L31, per this chain's journal
  T0). Manuscript ledger: `chapters/appH-microscopic-proofs.tex`, section "Problem D:
  local Lorentz" (L765-766), "Status: OPEN. Priority: CRITICAL PATH. Completion:
  PROGRAMME-CONDITIONAL" (L769-770), reduced-scope note "D2 ... D remains OPEN and the
  matrix-derived criterion is unmet" (L770-772). Missing step (L795-802): "Derive
  \(\mathrm{SO}(3,1)\) from the matrix algebra alone, or state that Presentation~A is
  not ontologically prior ... The locked frame and its non-degeneracy must also be
  derived rather than assumed (Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg})."
- Chapter 17 criterion (L696-701): "DERIVED means no remaining assumed premise in the
  claimed chain, so a chain that still uses Assumption~... \ref{ass:frame-lock},
  \ref{ass:nondeg} ... does not qualify." D1 item (L715-720): "an \(\mathrm{SO}(3,1)\)
  gauge symmetry is derived from the matrix algebra and condensate, with the
  \(\omega,A_\mu,B\) and ghost operators specified ... The locked frame and its
  non-degeneracy on the claimed domain are derived, not assumed".
- Classification of this package: PROGRAMME-CONDITIONAL evidence for D1 (an
  obstruction within a named hypothesis class plus conditional algebraic data under
  named relaxations). DERIVED: nothing. D1 stays OPEN; no status/priority/completion
  label is touched by this proposal.
- Dependencies: none of the derivation's inputs are gated on another critical-path
  problem's missing step (the argument is representation-theoretic); the result
  constrains the D1 search space and is compatible with all integrated D1 closers
  (059, 115-120, 122). Chapter 17 order passage (L650-669) puts D1 first among
  D1, C, F, N, B, G; this package does not gate or ungate any of them.

## Source reading

digest + targeted reads. Digest status at chain start (journal T0): dirty-chapters,
`make_digest --check` vacuous on this permanently-dirty tree, live pins authoritative.
Read in full: the Problem D/D1 ledger (appH L765-808); the first-order equivariant
class paragraphs (appH L1616-1636), flat point (L1638-1675), one-loop/reflected
paragraphs (L1677-1702), D1 closers L1704-1740 (059 toy L1704-1705, composite
mechanism L1707-1708, 115 L1710-1711, 116 L1713, 117 L1715, 122 L1717, 118 L1720,
119 L1722-1731, 120 L1733-1740); ch17 L694-723 (criterion and D1 item); the Problem E
paragraph containing L1931 (existing standard-lemma statement); all definition,
assumption and label passages used (eq:Smatrix, ass:frame-lock ch03 L265, ass:nondeg
ch04 L171 - each verified unique). Git state re-checked: live appH pin
`76d862968c31d78fffc665f72aaf60d40c90367a`, 875,106 B, 4,142 lines, UNCOMMITTED
(unchanged this resume; not restored). Not a full scan: this proposal inserts one
conditional ledger paragraph and changes no definition, assumption, scope statement
or status passage, so CLAUDE.md source-reading rules 3(a)-(d) do not require one.
## Research and reasoning

### A. Avenue choice and non-duplication

Avenue 1 of the 059-r3 list ("finite-N Lorentzian-fibre class test", journal T0) is
not consumed by any integrated paragraph. Checked against the live closers:

- 059 toy (L1704-1705): "The toy is compact in base and fibre, Abelian in fibre,
  torsion-free and two-dimensional: it retains neither \(\mathrm{SO}(3,1)\) nor the
  noncompact fibre nor the \((7,3)\) kinetic signature nor the selection of the class
  by the matrix equation". Compact Euclidean base and Abelian fibre: no
  \(\mathrm{SO}(3,1)\) fibre at finite \(N\), and its ghost spectrum is the
  Euclidean-contraction \(\sum_i\operatorname{ad}_{X_i}^2/\hbar_{\mathrm{eff}}^2\), a
  different operator from the Lorentzian class ghost.
- 115 (L1710-1711) defect threshold of the displayed potential; 116 (L1713)
  pointwise-bound realization, "pointwise singular-value bounds do not control the
  smallest singular value of a two-point kernel"; 117 (L1715) Gibbs probe measure;
  118 (L1720) Presentation-A selection constraints; 119 (L1722-1731) one-loop and
  scheme-level underdetermination; 120 (L1733-1740) commutator lift and \(K\)-type
  bound: none addresses finite-\(N\) matrix realizations of the class relations or a
  Lorentzian fibre representation.
- 122 (L1717): the bilocal reduction, avenue 2, is consumed there and records "the
  computation of \(w\) for the specific carrier of Problem~D1 remains open".
- The orbit-geometry nonexistence paragraph at L1614 is a Poisson-limit statement
  about \(\mathrm{SO}(4,1)\)-equivariant bases ("The hypothesis relaxed below is the
  representation"); it is not a finite-dimensional representation statement.
- Disclosure (material to novelty): appH L1931 (Problem E section) already states the
  standard lemma, applied there to the five-index algebra of the conjugate-coordinate
  class: "A representation of a non-compact simple Lie algebra by Hermitian
  \(N\times N\) matrices is trivial, since its image would be a compact Lie algebra
  isomorphic to it, with negative definite Killing form, whereas the Killing form of
  a non-compact simple Lie algebra is indefinite" and "the Lorentzian member exists
  only for \(N\to\infty\)". The group-theoretic lemma is therefore standard and is
  NOT claimed as new. What is new in this package is: (i) its application to the D1
  first-order equivariant class relations, where the adjoint-action formulation
  converts "the representation is trivial" into "the class DATA is trivial":
  \(\operatorname{ad}\mathcal S=0\) plus the first relation plus the rank-4 label map
  forces \(\mathbb D_a=0\); (ii) the two explicit finite-\(N\) models under the
  relaxed \(*\)-structure; (iii) the compact-fibre non-obstruction note. The payload
  paragraph cites none of this history (no \cite) and claims only the D1-class
  statement.

### B. The obstruction theorem

Setting (appH L1616-1621): \(\mathcal A\) commutative, \(\mathbb D_a,\mathcal S_{cd}\in
\mathrm{Der}(\mathcal A)\)-valued data with the two class relations, \(\mathcal S_{cd}\)
anti-Hermitian derivations forming a free and proper unitary \(\mathrm{SO}(3,1)\)
action (L1617), \(\eta=\operatorname{diag}(-1,1,1,1)\). Specializing to a finite
matrix representation over \(\mathcal A=\mathbb C\) means: matrices
\(\mathbb D_a,\mathcal S_{cd}\in\mathrm M_N(\mathbb C)\), \(N<\infty\), satisfying the
relations as matrix identities. Hypotheses of the obstruction, one by one:

- H1 (finite dimension): the representation space has \(N<\infty\). Used in: the
  Killing-form comparison (the trace pairing on a finite-dimensional image is a
  sum of non-positive terms) and in script A6's rank computation.
- H2 (unitary fibre action at the algebra level): all \(\mathcal S_{cd}\), boosts
  included, are anti-Hermitian: \(\mathcal S_{cd}^\dagger=-\mathcal S_{cd}\). This is
  what "anti-Hermitian derivations forming a free and proper unitary action of
  \(\mathrm{SO}(3,1)\)" (L1617) means after exponentiation on a finite-dimensional
  Hilbert space. Used in: negative semidefiniteness of the Killing form of the image.
- H3 (exact class relations / homomorphic adjoint action): the first relation
  \([\mathcal S_{cd},\mathbb D_a]=\eta_{ad}\mathbb D_c-\eta_{ac}\mathbb D_d\) holds
  exactly as a matrix identity (L1619), and the \(\mathcal S\)-sector closes under
  commutators as a homomorphic image of \(\mathfrak{so}(3,1)\) (the Lie-algebra part
  of "forming ... an action of \(\mathrm{SO}(3,1)\)"). The adjoint action
  \(\operatorname{ad}\mathcal S\) is then a homomorphic image of \(\mathfrak{so}(3,1)\)
  in anti-Hermitian endomorphisms of \(\mathrm M_N\) (script A0b checks the
  \(\eta\)-antisymmetry convention of the six generators and A1 their closure).
  Note the formulation avoids the central-extension ambiguity of a literal
  \(\mathcal S\mapsto\) matrices homomorphism claim (journal T4): only the adjoint
  action needs to be a homomorphic image.
- H4 (nondegenerate Lorentzian \(\eta\)): the label map
  \(G\mapsto(\eta_{ad}G_c-\eta_{ac}G_d)_{(cd,a)}\) built from the right-hand side of
  relation 1 has rank 4 for each fixed \(d\) (script A6: rank 4 for each of four
  values of \(d\)); this is an invertibility statement on \(\eta\).
- H5 (commutative coefficient algebra specialized to \(\mathbb C\)): over
  \(\mathcal A=\mathbb C\) the derivations are matrices. For a genuinely nontrivial
  finite-\(N\) commutative \(\mathcal A\ne\mathbb C\) the same argument applies
  entrywise under any evaluation character; a NONcommutative coefficient algebra at
  finite \(N\) falls outside the class definition (L1616 requires \(\mathcal A\)
  commutative) and is a separate relaxation.

Chain (each step annotated by its scripted check where one exists):

1. The adjoint action \(\rho(X)=\operatorname{ad}_{\mathcal S_X}\) is a
  homomorphic image of \(\mathfrak{so}(3,1)\) by anti-Hermitian endomorphisms of
  \(\mathrm M_N\) (H2, H3; the endomorphism of a Hermitian basis element is again
  anti-Hermitian under the Hilbert-Schmidt pairing).
2. For anti-Hermitian \(A\), \(\operatorname{tr}(\operatorname{ad}_A\,\operatorname{ad}_A)
  =-\|\operatorname{ad}_A\|_{\mathrm{HS}}^2\le 0\), so the image \(V=\rho(\mathfrak{so}(3,1))\)
  has negative-semidefinite Killing form (script A4 verifies the identity on 8 random
  seeds, and its CONTROL-FIRED line shows a generic non-anti-Hermitian matrix
  violating it).
3. \(\mathfrak{so}(3,1)\) is simple with indefinite Killing form:
  \(\operatorname{tr}(\operatorname{ad}_{K_1}^2)=+4\) (boosts) and
  \(\operatorname{tr}(\operatorname{ad}_{J_{12}}^2)=-4\) (rotations); the Killing form
  is nondegenerate with signature \((3,3)\) and \(B=2\,\mathrm{tr}(XY)\) exactly
  (scripts A2, A2b, A3, A3a, A3b; the resume helper
  `check_payload_killing_126.resume.py` re-verified the \(\pm4\) and the identity
  \(B=2\,\mathrm{tr}(XY)\) exactly; simplicity itself is the standard fact, not
  machine-checked).
4. A homomorphic image of a simple Lie algebra is \(0\) or an isomorphic copy; an
  isomorphic copy inherits the indefinite Killing form, contradicting step 2; hence
  \(\rho=0\), i.e. \(\operatorname{ad}_{\mathcal S_{cd}}=0\) on the module
  (\(\mathcal S_{cd}\) central on the full matrix algebra).
5. Relation 1 with \(\operatorname{ad}\mathcal S=0\) reads
  \(\eta_{ad}\mathbb D_c-\eta_{ac}\mathbb D_d=0\) for all \(a\) and all pairs
  \((c,d)\); the rank-4 label map (H4; script A6) forces \(\mathbb D_a=0\) for all
  \(a\).
6. With all \(\operatorname{ad}\mathcal S=0\), \([\mathcal S_X,\mathcal S_Y]=
  \mathcal S_{[X,Y]}\) gives \(\mathcal S_{[X,Y]}=0\), and perfection
  \([\mathfrak{so}(3,1),\mathfrak{so}(3,1)]=\mathfrak{so}(3,1)\) (script A5: derived
  algebra of dimension 6 = full) gives \(\mathcal S=0\). The second class relation is
  then vacuous. Conclusion: the only finite-\(N\) realization of the two relations
  with anti-Hermitian \(\mathcal S\) is trivial (the zero class datum).

Script A's CONTROL-FIRED checks confirm the argument discriminates: the \(\mathfrak{so}(4)\)
control (A7) has negative-definite Killing form (six eigenvalues \(-4\)), exactly the
case step 2 does NOT exclude - the compact-fibre non-obstruction note.

Script-vs-theorem gaps (check \(\ne\) proof; the gatekeeper should weigh these):
the scripts verify the ingredients (identity of step 2, closure and generator
normalization, Killing signature and nondegeneracy, perfection, label-map rank) and
the controls, but the following remain pen-and-paper standard facts used as lemmas:
simplicity of \(\mathfrak{so}(3,1)\); "homomorphic image of simple is 0 or a copy"
(ideal argument); the identification of the class's "free and proper unitary action"
with H2-H3 at the algebra level (interpretive step tying the payload to L1617); and
step 1's assertion that \(\operatorname{ad}_{\mathcal S}\) restricted to the
relevant module consists of anti-Hermitian endomorphisms (immediate from H2 on the
full matrix algebra with the Hilbert-Schmidt pairing).

### C. Flat \(5\times5\) realization (relaxed \(*\): mixed, non-unitary)

Real \(5\times5\), indices \(\mu,\nu=0..4\), \(V=\operatorname{span}_{\mathbb R}\{\mathbb D_a\}\)
the translation sector, \(\eta=\operatorname{diag}(-1,1,1,1)\) on \(0..3\):
\(\mathbb D_a=E_{a4}\) and
\((\mathcal S_{cd})^\mu{}_\nu=\delta^\mu_c\eta_{d\nu}-\delta^\mu_d\eta_{c\nu}\)
(\(\mu,\nu=0..3\), translation row zero). Then, exactly (script B):

- The two relations hold with \(\mathsf T=\mathsf R=\mathsf F=0\): relation 1 is the
  defining \((\mathrm{vector},\wedge^2)\) action (B-R1: 48/48 pairs) and
  \([\mathbb D_a,\mathbb D_b]=0\) (B-R1). \(\mathcal S\) is \(\eta\)-antisymmetric
  (B-R2), closes in the 6-dim span (B-R3a) with no leakage to the translation row
  (B-R3b), and reproduces the \(\mathfrak{so}(3,1)\) brackets with the class
  normalization (B-R3c).
- The inner automorphism is exact, not infinitesimal:
  \(e^{\mathcal S_{12}}\mathbb D_a e^{-\mathcal S_{12}}\) and
  \(e^{\mathcal S_{01}}\mathbb D_a e^{-\mathcal S_{01}}\) give the rotation and boost
  label matrices exactly at \(t=1\) (B-R4a, B-R4b).
- The kinetic operator \(\tfrac14\eta^{ab}[\mathbb D_a,[\mathbb D_b,G]]\) vanishes on
  all eleven generators \(\mathbb I,\mathcal S_{cd},\mathbb D_a\) (B-R5): a flat
  finite model has no propagation; any residual kinetic term must live on the
  coefficient algebra.
- The centralizer of \(\{\operatorname{ad}\mathbb D_a\}\) on
  \(\operatorname{span}\{\mathbb I,\mathcal S,\mathbb D\}\) is
  \(\mathbb C\,\mathbb I\oplus\operatorname{span}\{\mathbb D_a\}\) (B-R6); all products
  \(\mathbb D_a\mathbb D_b=0\) (B-R6c), so the nil part is square-zero with point
  spectrum: over \(\mathcal A=\mathbb C\) there is no base manifold inside the fibre
  algebra at \(N=5\). (This corrects the T2-plan note "commutant \(=\operatorname{span}\{1\}\)":
  the \(E_{a4}\) are central for the adjoint action of the \(D\)'s among themselves.)
- The \(*\)-structure is forced mixed: \(\mathcal S_{12}\) anti-Hermitian,
  \(\mathcal S_{01}\) Hermitian - consistent with the obstruction (a unitary choice
  would be trivial).

### D. Curved \(4\times4\) spinor realization (relaxed \(*\): mixed)

Complex \(4\times4\), \(\mathbb D_a=\gamma_a\) a Dirac representation with
\(\{\gamma_a,\gamma_b\}=2\eta_{ab}\) (\(\gamma_0\) anti-Hermitian, \(\gamma_i\)
Hermitian - mixed \(*\) again forced), \(\mathcal S_{cd}=\tfrac{s}{4}[\gamma_c,\gamma_d]\).
Clifford relations exact (C-C0a, 16 checks); \(\mathcal S\) realizes
\(\mathfrak{so}(3,1)\) on the spinor sector with the sign \(s=+1\) FORCED by the
class relation itself: 0/48 violations for \(s=+1\), 24 for \(s=-1\) (C-C1, plus the
contraction-consistency forcing C-C3b). Data (all exact symbolic, script C):

- \(\mathsf T=0\), \(\mathsf F=0\), \(\mathsf R_{ab}{}^{cd}=4(\delta^c_a\delta^d_b-
  \delta^c_b\delta^d_a)\) nonzero constant curvature (C-C2, C-C2b): the second
  relation \([\mathbb D_a,\mathbb D_b]=\tfrac12\mathsf R_{ab}{}^{cd}\mathcal S_{cd}\)
  holds exactly (\([\gamma_a,\gamma_b]=\tfrac12\cdot4(\cdots)\cdot\tfrac14[\gamma,\gamma]\)
  counted correctly in C-C2, 12 checks).
- \(\mathsf R_{ab}{}^{ae}=12\,\delta_b^e\) and the direct contracted double
  commutator \([\mathbb D^a,[\mathbb D_a,\mathbb D_b]]=12\,\mathbb D_b\) (C-C3a), with
  the manuscript contraction identity \(\mathsf R_{ab}{}^{ae}=-\mathrm{Ric}_b{}^e\)
  at \(\mathsf T=0\) (appH L1626-1630) giving \(\mathrm{Ric}_{ab}=-12\,\eta_{ab}\)
  (C-C3: this is the maximally symmetric Einstein value for this normalization;
  controls: replacing \(\eta\) by \(\delta\) fails 36 checks, a flat \(\gamma\) set
  gives \(0\ne12\,\mathbb D_b\)).
- The 16 Dirac bilinears \(\{1,\gamma_a,\mathcal S_{cd},\gamma_a\gamma_5,\gamma_5\}\)
  are a basis of \(\mathrm M_4(\mathbb C)\) (C-C4b rank 16) and close under
  \([\mathcal S,\cdot\,]\) and \([\mathbb D,\cdot\,]\) with rational structure
  constants (C-C4c), so \(\operatorname{End}(\mathbb C^4)\) is a class module;
  \(\gamma_5^2=-I\) (C-C4a, Lorentzian).
- Kinetic \(L=\tfrac14\eta^{ab}[\mathbb D_a,[\mathbb D_b,\cdot\,]]\) on the 16-dim
  module: \(L(1)=0\) (kernel the scalars), \(L(\gamma_a)=3\gamma_a\),
  \(L(\mathcal S_{cd})=2\mathcal S_{cd}\), \(L(\gamma_5)=4\gamma_5\),
  \(L(\gamma_a\gamma_5)=1\cdot\gamma_a\gamma_5\) (C-C5a-C5g; the eigenvalue set
  \(\{0,3,2,4,1\}\) is pairwise distinct - control fired; the Euclidean-contraction
  control fails, confirming the Lorentzian signature is doing the work).
- Ghost-operator sign (finding F1): the manuscript ghost operator is
  \([\hat X^a,[\hat X_a,\cdot\,]]\) (L1624) and \(\hat X_a=\mathrm i\mathbb D_a\)
  (L1617), so the class ghost is \(-[\mathbb D^a,[\mathbb D_a,\cdot\,]]=-4L\) with
  eigenvalues \(-12,-8,-16,-4\); the operator \([\mathbb D^a,[\mathbb D_a,\cdot\,]]=4L\)
  has kernel the scalars and eigenvalues \(12,8,16,4\), which is what payload v2
  states (with "up to the sign of \(\hat X_a=\mathrm i\mathbb D_a\)").
- Status of the model: tier CONDITIONAL ALGEBRAIC DATA - an exact finite-\(N\)
  realization of the two class relations with Lorentzian \(\eta\) and constant
  curvature, NOT a vacuum of the model dynamics, NOT a derivation of the frame or of
  \(\mathrm{SO}(3,1)\), and NOT a D1 closure. Its role: the class relations are
  consistent at finite \(N\) once \(*\) is mixed, and the obstruction's H2 is exactly
  the hypothesis that fails.

### E. Literature

No external result is imported. The standard lemma (noncompact-simple +
finite-dimensional unitary forces triviality) is stated in the manuscript itself at
L1931; nothing was fetched from the web this round (previous chain round recorded no
external citation as needed; the payload carries no \cite). Comparison with original
target: the frontier edge asked for a finite-\(N\) Lorentzian-fibre class TEST; the
package delivers the test with a bounded no-go inside H1-H5 and two exact
realizations outside H2, rather than a realization inside the hypothesis class.
## Claim classification

| # | claim | tier |
|---|-------|------|
| 1 | For anti-Hermitian \(A\), \(\operatorname{tr}(\operatorname{ad}_A\operatorname{ad}_A)=-\|\operatorname{ad}_A\|_{\rm HS}^2\le0\); finite-dimensional unitary (anti-Hermitian) representations of noncompact simple \(\mathfrak{so}(3,1)\) are trivial | established identity / standard lemma (already stated in the manuscript at appH L1931 for the five-index algebra); ingredients scripted (A2-A5) and re-run identical on resume |
| 2 | Obstruction: under H1-H5 the only finite-\(N\) realization of the two D1 class relations with anti-Hermitian \(\mathcal S\) is trivial (\(\operatorname{ad}\mathcal S=0\), \(\mathbb D=0\), \(\mathcal S=0\)) | conditional theorem (derivation pen-and-paper; every scripted ingredient green; gaps listed in Research B) |
| 3 | A nontrivial unitary realization of the class requires \(N=\infty\); the manuscript class construction (L1617-L1622, \(\hat X_a=\mathrm i\,u_a\) on \(L^2(\mathbb R^4\times\mathrm{SO}(3,1))\), boosts anti-Hermitian on that Hilbert space) lives exactly there | conditional corollary of 1-2; the infinite-dimensional construction itself is the manuscript's conditional object, not re-derived here |
| 4 | Compact fibres (059 toy's \(U(1)\), reflected \(\mathrm{SO}(4)\) paragraph) are not obstructed | established (compact algebras have negative-semidefinite Killing form; A7 control exhibits \(\mathfrak{so}(4)\)'s negative-definite form) |
| 5 | Flat \(5\times5\) identities: relations with \(\mathsf T=\mathsf R=\mathsf F=0\); exact exponential label Lorentz matrices; kinetic vanishing on \(\operatorname{span}\{\mathbb I,\mathcal S,\mathbb D\}\); centralizer \(\mathbb C\mathbb I\oplus\operatorname{span}\{\mathbb D_a\}\); \(\mathbb D_a\mathbb D_b=0\) | established exact computation (script B, ALL-PASS, 2 controls, resume re-run byte-identical) |
| 6 | "No base manifold in the fibre algebra at \(N=5\)" (flat model) | interpretive reading of established fact 5 (square-zero nil centralizer over \(\mathbb C\) has point spectrum) |
| 7 | Spinor \(4\times4\) identities: relations with \(\mathsf T=\mathsf F=0\), \(\mathsf R=4(\delta\delta-\delta\delta)\); \(\mathsf R_{ab}{}^{ae}=12\delta\); \(s=+1\) forced twice; 16 bilinears close rationally; kinetic eigenvalues \(0,3,2,4,1\), kernel scalars | established exact computation (script C, ALL-PASS, 4 controls, resume re-run byte-identical) |
| 8 | \(\mathrm{Ric}_{ab}=-12\eta_{ab}\) for the spinor model | conditional algebraic data under the manuscript's own identification \(\mathsf R_{ab}{}^{ae}=-\mathrm{Ric}_b{}^e\) at \(\mathsf T=0\) (appH L1626-1630); an \(\mathrm M_4(\mathbb C)\) matrix-model object, not a metric of emergent spacetime and not a vacuum of any dynamics |
| 9 | Class ghost \([\hat X^a,[\hat X_a,\cdot\,]]=-\![\mathbb D^a,[\mathbb D_a,\cdot\,]]\) has eigenvalues \(-12,-8,-16,-4\); the unsigned operator \(4L\) has \(12,8,16,4\) | established computation under the manuscript conventions L1617/L1624 (the basis of finding F1 and the v2 wording) |
| 10 | Tier of both models overall | CONDITIONAL ALGEBRAIC DATA under named relaxations (mixed \(*\)); explicitly NOT D1 closures, NOT derivations of \(\mathrm{SO}(3,1)\), frame lock or non-degeneracy; the inserted paragraph closes nothing |
| 11 | \(\mathfrak{so}(3,1)\) simplicity; "image of simple is 0 or a copy" | established standard facts used as lemmas, not machine-checked (listed as script-vs-theorem gaps) |

## Proposed changes

### File `chapters/appH-microscopic-proofs.tex` (the only file changed)

One new paragraph, inserted after the last D1 closer and before `\section{Problem E}`.

- Anchor (occurs exactly once in the live pin `76d862968c31d78fffc665f72aaf60d40c90367a`;
  asserted by the generator at splice time): the ending of L1740
  `de the class rather than supplied: this paragraph closes none of Problem~D, Problem~D1, or Problem~A.`
  followed by CRLFCRLF. Verified boundary after the anchor: blank line, then
  `\section{Problem E: signature}` (L1742).
- Kept: every existing byte, including the full 120 closer paragraph
  ("Within this class the bridge becomes a derived identity ... closes none of
  Problem~D, Problem~D1, or Problem~A.") and the Problem E section opening.
- Inserted text = `payload-126-v2.txt` verbatim (4,447 B, sha1 `b9ebeba71fe933b1048dbcd2a0ec4f46d89c54dd`),
  a single conditional ledger paragraph ending in one scoped status sentence ("... closes
  none of Problem~D, Problem~D1, or Problem~A" in substance; see bytes). It uses only
  pre-existing references `eq:Smatrix`, `ass:frame-lock`, `ass:nondeg` (each verified to
  exist and be used once by the payload; no `\label`, no `\cite`, no duplicate labels).

````latex
\emph{Finite matrix size: a unitarity obstruction and two exact algebraic realizations.} Take the two relations of the class over with \(\mathcal A=\mathbb C\) at finite matrix size \(N\), keeping the \(*\)-structure on \(\mathcal S_{cd}\) (anti-Hermiticity). For anti-Hermitian \(A\) one has \(\operatorname{tr}(\operatorname{ad}_A\operatorname{ad}_A)=-\lVert\operatorname{ad}_A\rVert_{\mathrm{HS}}^2\le0\), so every matrix Lie algebra of anti-Hermitian matrices has negative-semidefinite Killing form; \(\mathfrak{so}(3,1)\) is simple with indefinite Killing form (in the vector representation \(\operatorname{tr}(\operatorname{ad}_{J_{12}}\operatorname{ad}_{J_{12}})=-4\) and \(\operatorname{tr}(\operatorname{ad}_{K_1}\operatorname{ad}_{K_1})=+4\)). The adjoint action of the \(\mathcal S\)-sector of the class is a homomorphic image of \(\mathfrak{so}(3,1)\) formed by anti-Hermitian endomorphisms of the matrix space; a homomorphic image of a simple Lie algebra is either \(0\) or an isomorphic copy, and the latter would make the Killing form both negative-semidefinite and indefinite: the adjoint action of the \(\mathcal S\)-sector therefore vanishes identically, and the first relation then forces \(\mathbb D_a=0\) (its label map has rank \(4\)). Hence the only finite-\(N\) realization of the two relations with anti-Hermitian \(\mathcal S\) is trivial, a unitary realization requires \(N=\infty\), and non-unitary \(\mathcal S\) is unavoidable in any finite-\(N\) Lorentzian data of the class; this is why the compact fibres used elsewhere in this section are not obstructed. With the \(*\)-structure relaxed, two exact realizations show that the relations are consistent at finite \(N\) with the Lorentzian \(\eta\) contraction. (i) \(5\times5\) real matrices, \(\mathbb D_a=E_{a4}\) and \(\mathcal S_{cd}\) the standard affine lift of the vector representation, \((\mathcal S_{cd})^{\mu}{}_{\nu}=\delta^{\mu}_{c}\eta_{d\nu}-\delta^{\mu}_{d}\eta_{c\nu}\): both relations hold exactly with \(\mathsf T=\mathsf R=\mathsf F=0\); the inner automorphism \(\mathrm e^{\mathcal S}\mathbb D_a\mathrm e^{-\mathcal S}\) reproduces the label Lorentz matrix exactly (rotation and boost generators, at \(t=1\), exact exponentials), the finite-\(N\) form of the identity of the class that local rotations are matrix gauge transformations; the ghost operator \([\hat X^a,[\hat X_a,\cdot\,]]\) vanishes on \(\operatorname{span}\{\mathbb I,\mathcal S,\mathbb D\}\); and the centralizer of the adjoint action of the \(\mathbb D_a\) on that span is \(\mathbb C\mathbb I\) plus the nilpotent \(\operatorname{span}\{\mathbb D_a\}\) (all products zero), whose spectrum is a point: at \(N=5\) no base manifold sits inside the fibre algebra. (ii) \(4\times4\) complex matrices, \(\mathbb D_a=\gamma_a\) the Lorentzian Clifford generators (\(\gamma_0\) anti-Hermitian, \(\gamma_i\) Hermitian) and \(\mathcal S_{cd}=\tfrac14[\gamma_c,\gamma_d]\): both relations hold exactly with \(\mathsf T=\mathsf F=0\) and \(\mathsf R_{ab}{}^{cd}=4(\delta_a^c\delta_b^d-\delta_b^c\delta_a^d)\), and the contracted matrix identity holds exactly, \([\mathbb D^a,[\mathbb D_a,\mathbb D_b]]=\mathsf R_{ab}{}^{ae}\mathbb D_e=12\,\mathbb D_b\), i.e. \(\mathrm{Ric}_b{}^e=-12\,\delta_b{}^e\) under the identity \(\mathsf R_{ab}{}^{ae}=-\mathrm{Ric}_b{}^e\) of the matrix equation; the sign of \(\mathcal S_{cd}\) is forced, by the first relation (48 exact checks) and independently by this contraction. The operator \([\mathbb D^a,[\mathbb D_a,\cdot\,]]\) on \(\operatorname{End}(\mathbb C^4)\), the class ghost operator up to the sign of \(\hat X_a=\mathrm i\mathbb D_a\) at \(N=4\), has kernel the scalars and eigenvalues \(12,8,16,4\) on the vector, bivector, pseudoscalar and axial sectors of the \(16\) Dirac bilinears, which close under both adjoint actions with rational constants; its mixed \(*\)-structure is forced by the obstruction above. Hypotheses: the two relations at face value with constant coefficients, finite \(N\), no state, no dynamics, no reference to Equation~\eqref{eq:Smatrix}, no matter content, no selection; these are consistency and obstruction results at the algebraic level, they derive no \(\mathrm{SO}(3,1)\) from the matrix algebra or the condensate, and they construct neither the locked frame nor its non-degeneracy (Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg}): this paragraph closes none of Problem~D, Problem~D1, or Problem~A.
````

- Splice recipe and byte accounting (generator `make_payload_126.v2.py`, reproducing
  deterministically): `spliced = base.replace(ANCHOR, ANCHOR + PAYLOAD + b"\r\n")`, so
  the payload is inserted after the anchor's blank line and a join CRLF is appended
  after it. Against the pinned baseline (PRE = 875,106 B): payload 4,447 B;
  certified POST = 879,555 B = PRE + 4,447 + 2, sha1 `13341a8b6fb7f99ff7a005a5ad4ad1d0cf3d5f93`
  (`appH-spliced-126-v2.tex`, compile certificate v3, `out-cert-126-v3.txt`). The
  canonical alternative `replace(anchor, payload+anchor)` would give 879,553 B; the
  +2 join-CRLF accounting follows the splice-POST memory note and matches both
  certificates.
- Lineage (finding F1): payload v1 (4,361 B, sha1 `7e6ed4cd6c83...`, compile
  certificate v2 `out-cert-126.txt`, spliced `7534c424b969...`/879,469 B) is superseded
  ONLY in the ghost-operator clause; its bytes are preserved untouched on disk
  (`payload-126.txt`, `appH-spliced-126.tex`, generators `make_payload_126.v1.py` =
  pinned `make_payload_126.py` and `make_payload_126.v2.py`). The v1-v2 difflib diff is
  three opcodes in one clause: delete "ghost ", insert the
  \([\mathbb D^a,[\mathbb D_a,\cdot\,]]\) operator form, insert " up to the sign of
  \(\hat X_a=\mathrm i\mathbb D_a\)"; all other bytes identical.
- Stale passages elsewhere: none identified. The paragraph adds obstruction data and
  closes nothing, matching the existing closer language at L1717/L1720/L1731/L1740; the
  D ledger missing-step text (L795-808) and the ch17 D1 item remain accurate as
  written. No other file needs changes; no bib entry is added.
## Verification scripts (reproduction pack)

All scripts live in this folder; run with `python -I` from the folder (no package
deps beyond sympy/numpy; sympy 1.14). Expected invariant outputs are quoted from the
shipped captures, which the resume re-runs reproduced byte-identically.

| script | checks | expected output | capture |
|--------|--------|-----------------|---------|
| `verify_126_A_nogo.py` | obstruction ingredients: generator eta-antisymmetry, closure, Killing nondegenerate/indefinite, \(\operatorname{tr}(\operatorname{ad}^2)=\mp4\) rotation/boost, \(B=2\mathrm{tr}(XY)\), anti-Hermitian identity + control, perfection, label-map rank 4, \(\mathfrak{so}(4)\) control | `SUMMARY_A: ALL-PASS`, 2 `CONTROL-FIRED` | `out-A-run4.resume.txt` (= run2/run3 byte-identical) |
| `verify_126_B_flat5.py` | flat \(5\times5\): R1 48/48, R2, R3a/b/c, R4a/b exact exponentials, R5 kinetic vanishing, R6 centralizer, R6c square-zero + Euclidean control | `SUMMARY_B: ALL-PASS`, 2 `CONTROL-FIRED` | `out-B-run4.resume.txt` (= run2/run3) |
| `verify_126_C_spinor.py` | spinor \(4\times4\): C0 Clifford + mixed \(*\), C1 sign forcing (0/48), C2 curvature + \(\mathsf T=\mathsf F=0\), C2b nonzero, C3a direct 12 D, C3b forcing, C4a-c bilinear closure, C5a-g kinetic eigenvalues + distinctness/Euclidean controls | `SUMMARY_C: ALL-PASS`, 4 `CONTROL-FIRED` | `out-C-run3.resume.txt` (sha1 `8a58011ca975...` = run1/run2) |
| `check_payload_killing_126.resume.py` | payload's \(\pm4\) Killing numbers and \(B=2\mathrm{tr}(XY)\) exactly | `KILLING-CHECK: PASS J12=-4: True K1=+4: True B=2tr(XY): True` | `out-killing-check.resume.txt` |
| `make_payload_126.v2.py <repo-root>` | regenerates payload v2 + spliced v2 from live appH bytes; asserts pin `76d862968c31`, anchor count 1, F1-clause anchors count 1 each, ASCII, single CRLF terminator | `PAYLOAD-BYTES 4447`, `PRE 875106 POST 879555 DELTA 4449`, `SPLICED-SHA1 13341a8b6fb7...`, `MAKE-OK` | `out-payload-v2.txt` |
| `build_v2_generator_126.resume.py` | rebuilds `make_payload_126.v2.py` from the preserved v1 generator bytes (auditable lineage; its F1 asserts fired during development, demonstrating the join guard is non-vacuous) | `V2-GEN-WRITTEN 7417 e996ca20baad...` | recorded in journal R2 |

Do NOT run `make_payload_126.py` (v1 pinned generator) or
`proposals/123-f-coeff-locked-block/verify_ghost_op_123.py` (frozen). v1 lineage is
verified by hash, not re-execution (re-execution would rewrite `payload-126.txt` /
`appH-spliced-126.tex` in this folder; it is deterministic and would reproduce the
same bytes, but is unnecessary).

Compile certificates (external temp trees, kept, outside the repo; the repo was never
built): v2 cert `out-cert-126.txt` covers `appH-spliced-126.tex`
(`7534c424b969...`/879,469, payload v1) in
`C:/Users/redgi/AppData/Local/Temp/build126_cert_v2_31476`; v3 cert
`out-cert-126-v3.txt` covers `appH-spliced-126-v2.tex`
(`13341a8b6fb7...`/879,555, payload v2) in
`C:/Users/redgi/AppData/Local/Temp/build126_cert_v3_41207`: 2 passes exit 0, 0
lines matching `^! `, 0 undefined references, 196 undefined citations (= baseline,
bibtex not run, payload adds no `\cite`), and in compiled text 'unitarity
obstruction' x1, 'class ghost operator up to the sign' x1, superseded v1 clause
'The ghost operator on' x0.

sympy pitfalls found (journal T3; relevant to re-derivation): (i) `Matrix.D` is the
Dirac conjugate in sympy 1.14 - use `.H` for adjoint; (ii)
`sp.Matrix(sp.BlockMatrix(...))` stays a `MatrixExpr` - build blocks with
`row_join`/`col_join`; (iii) \(\sigma_2=\begin{pmatrix}0&-i\\ i&0\end{pmatrix}\) (the
real antisymmetric version breaks Clifford); (iv) `Matrix([Matrix rows])` nests -
flatten with `list(...)`.

## Decisions Taken

- F1 disposition (routine choice, decided per autonomous mode): repair rather than
  ship-and-note. Integrating a clause that misattributes eigenvalues under the
  manuscript's own definitions would import a false claim (rules 6-7); leaving it
  with a footnote would ask the gatekeeper to ACCEPT known-wrong text. Chosen:
  one-clause v2 (86-byte minimal edit keeping v1's numbers and structure) + fresh
  compile certificate, with all v1 bytes preserved and both certificates disclosed.
  Rejected: (a) ship v1 unchanged plus finding (puts a false sentence in the
  manuscript); (b) rewrite the whole ghost discussion (violates minimal-insertion);
  (c) silent in-place edit of certified bytes (breaks lineage; avoided by v2 files).
- Wording "the class ghost operator up to the sign of
  \(\hat X_a=\mathrm i\mathbb D_a\)" chosen over "minus the class ghost operator" to
  keep the sentence declarative about the verified operator and its spectrum.
- Anchor and join unchanged from v1 (certificate says the splice compiles; no reason
  to move).
- Superseded T2-plan note "commutant \(=\operatorname{span}\{1\}\)" corrected to
  "\(\mathbb C\mathbb I\oplus\operatorname{span}\{\mathbb D_a\}\)" (journal T3 line
  stands; the proposal text uses the corrected statement).
- L1931 disclosed as prior in-manuscript statement of the standard lemma rather than
  omitting it; the package's novelty claim narrowed accordingly (Research A).
- Dispatch said "if the generator re-run reproduces the certified bytes, leave the
  payload untouched"; followed literally for v1 (untouched), with the v2 change made
  only as the documented F1 disposition under the dispatch's payload-change provision
  (new temp tree, temp dirs kept, no repo build).

## Milestone assessment

Routine. No milestone trigger: no critical-path step is derived, no missing link is
closed; the package records a bounded obstruction plus conditional algebraic data and
one verification finding. No milestone digest warranted.

## Status-label recommendation

Re-derived from the current sources: CRITICAL PATH / OPEN at the full-GR scope: A, B,
C, D1, E, F, G-derived, N (ch17 L694-723; appH ledgers). Affected labels: none.
Problem D / D1 stay OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; this proposal changes
no label anywhere. The obstruction is evidence within D1's evidence list only if the
gatekeeper accepts the paragraph; even then D1's original target (derivation of
\(\mathrm{SO}(3,1)\), frame lock, non-degeneracy) stays untouched.

## Author decision needed

None. (No core change, no scope change, spacetime stays emergent: all objects are
matrix-model algebraic data; no fundamental metric is introduced anywhere.)

## Remaining open step

To close D1's original target one still needs: (1) a derivation of
\(\mathrm{SO}(3,1)\) as a gauge symmetry from the matrix algebra and condensate
(whatever the fibre's \(N\)), with \(\omega,A_\mu,B\) and the ghost operator
specified; (2) derivation of the locked frame (ass:frame-lock) and its non-degeneracy
(ass:nondeg) rather than assumption; (3) the class-selection step (which datum picks
the class) still open per L1731/L1740. What this package settles about the search
space, inside its hypothesis class H1-H5 (finite-dimensional, unitary \(\mathcal S\),
exact class relations, nondegenerate \(\eta\), \(\mathcal A=\mathbb C\)): the unitary
finite-\(N\) realizeroute does not exist. Avenues it does NOT exclude, ranked
positive-derivation-first: (i) finite-\(N\) with dynamically-derived mixed \(*\)
(the spinor model is consistent algebraic data there; a derivation selecting the
\(*\) from the matrix-model dynamics is the named missing sub-step this finding
routes to); (ii) composite/bilocal carriers outside the class-relation form (122's
open \(w\) computation); (iii) the genuinely infinite-\(N\) unitary class plus the
selection/frame derivations on it; (iv) relaxations of H3's exact first-relation form
(higher-order completions) or of H5 (noncommutative coefficient algebras, which
leave the class definition). The no-go closes nothing beyond H1-H5 and does not
address the compact-fibre constructions.

## Special instructions for the gatekeeper

1. Re-run A, B, C with `python -I` (commands in the table); expect ALL-PASS and the
   control counts (2/2/4). Byte-identical to captures is expected modulo nothing (the
   scripts are deterministic). Do not run the frozen 123 script or the v1 generator.
2. F1 must be weighed, not waved: verify appH L1617 (\(\hat X_a=\mathrm i\mathbb D_a\))
   and L1624 (ghost operator \([\hat X^a,[\hat X_a,\cdot\,]]\)) against script C's
   definition of \(L\) and its eigenvalues, then decide whether v2's "up to the sign"
   clause is accurate. v1 remains on disk if you prefer to adjudicate on the original
   bytes; the diff is three difflib opcodes in one clause.
3. The payload must not be read as D1 progress toward closure: it derives no
   \(\mathrm{SO}(3,1)\), no frame lock, no non-degeneracy, and asserts only that the
   finite-\(N\) unitary route is obstructed within H1-H5 plus the two explicit relaxed
   models. Check the payload wording against scripts A/B/C clause by clause; the
   scripts are checks, not proofs, and the theorem's pen-and-paper lemmas (simplicity,
   image-of-simple, class-text -> H2/H3 reading) are listed in Research B.
4. Anchor re-verification is mandatory at integration time: the tree is dirty; the
   anchor string and the live pin `76d862968c31...` were unique at splice time, and
   the byte POSTs (879,555 for v2) are valid only against that baseline. If appH has
   moved, re-anchor on the same unique sentence and recompute.
5. The 196 undefined-citations figure is the temp-build baseline (bibtex not run);
   compare against `out-cert-126.txt`, not zero.
6. No bib additions; no label additions (payload adds none); check no duplicate label
   was introduced by the splice (certificate: 0 undefined/multiply references in the
   spliced build).
