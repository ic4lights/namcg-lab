# Proposal 060-rp-n2-invariant-failure, round 1

## Result

For the Lorentzian IKKT definitions recorded in the Problem E section of Appendix H, the
Euclidean measure that the finite-N limit identity produces **fails reflection positivity
on the gauge-invariant polynomial algebra**: at N=2, with the p=4 content (weight
c_P (det G~)^4 e^{-S_E}) or with a mass, and bosonically with a mass at every finite N,
there are manifestly gauge-invariant, theta-odd polynomials — Tr A~_0 A~_i and
Tr([A~_0,A~_i]A~_j), i != j — whose reflected pairing is strictly negative, exactly
-|f|^2-weighted integrals. Moreover every unital *-subalgebra on which the reflected
form is nonnegative is contained in the theta-even invariant algebra, and the same
negative sign passes through the R_1 continuation of the mixed bilinear. This is a
proved, bounded no-go on the Euclidean reconstruction side: it refutes at the finite-N
model level the positivity premise that the D-section relaxation (i) ("Singlets") takes
from field theory, and it bounds what any Osterwalder–Schrader-type reconstruction from
these measures can contain. It does not discharge ass:lorentzian and closes nothing:
Problem E remains open and PROGRAMME-CONDITIONAL.

## Target and status

- Target: attack-plan node **E.sig**, obligation E.1 ("derive (-,+,+,+) of the locked
  vacuum; drop ass:lorentzian", src ch04:322). E.sig gates goals gr.spin2 and gr.einstein
  in `reports/graph/attack-plan.yaml` (state: open-critical, priority critical-path).
- Appendix H (appH-microscopic-proofs.tex, current file, 3269 lines, hash c39e90f5b343):
  Problem E, label `sec:status-E` (L1537): L1540 "Status: OPEN. Priority: CRITICAL PATH
  for the matrix-derived label." L1541 "Completion: PROGRAMME-CONDITIONAL. A scope
  retaining ...". E section L1536–1579 contains the three definitions (A)/(B)/(C), the
  contour Stokes band u<2/3, the N=2 Pfaffian identity Pf M = c_P (det G)^4, the finite-N
  limit identity with phase e^{7 pi i (N^2-1)/4}, the Austing–Wheater k<14 window, the
  (C)-at-N=2 reduction, the exponential-observable trichotomy, and the slice-bridge /
  gamma→0^- modulus no-gos. It records no reflection-positivity statement.
- ch17-agenda.tex L395: "OPEN; CRITICAL PATH for the matrix-derived label."; completion
  criterion item L718–719: "Problem~E: Lorentzian signature is derived rather than
  retained (Assumption~\ref{ass:lorentzian})."
- Dependencies: D-section relaxation paragraph (L1526, item (i) Singlets) is the
  Euclidean-reconstruction route this package constrains; thm:mT (ch07) and the locked
  frame (ch04 ass:lorentzian, L321–328) sit behind E.sig.
- Classification of this package: DERIVED sub-lemma + bounded no-go **within the recorded
  class** (Euclidean finite-N measures, polynomial invariant test algebra, the signature
  involution theta). DERIVED or PROGRAMME-CONDITIONAL: nothing changes; E stays
  PROGRAMME-CONDITIONAL and open; no label is touched.

## Source reading

digest + targeted reads. `python scripts/make_digest.py --check` printed DIGEST CURRENT at
task start; dirty-chapters: no; appH hash matches (c39e90f5b343). Read in full: appH
Problem E section L1536–1599 (twice; incl. the L1554 convention
A_mu = sum_a A^a_mu sigma^a/2, G_ab = eta^{mu nu} A^a_mu A^b_nu), appH D-section
"Reflected form" and "Bearing ... relaxations" L1510–1534 (incl. items (i)–(iv) and the
L1528 closer), ch17 L370–414 and the criterion passage L714–722, ch04 L305–339
(ass:lorentzian), ch03 L188–201 (eq:Smatrix context), ch07 L270–299 (thm:mT premise 2),
`reports/sme-scout-20261108-1715.md` in full, `reports/vector/vector-mining-skel-ADE-20261108-1647.md`
(CC-E1 entry), `reports/ledger.md` E-chain entries (053/055/056/057),
`proposals/059-d1-lorentz-local-frame/proposal-r3.md` (apply-rule precedent),
`bib/namcg.bib` grep-verified entries (below). Full scan not due (no definition/assumption/
scope/status change; digest current; dirty-chapters: no).

## Research and reasoning

**Setup.** On R_1 the finite-N limit identity (appH L1556–1560) expresses the regulated
Lorentzian integral as an integral over Hermitian Euclidean matrices A~_mu with weight
Pf M(-i A~_0, A~_i) e^{-S_E}, S_E = (1/4 g^2) sum ||[A~_mu,A~_nu]||^2 (Hilbert–Schmidt).
At N=2, appH L1554: Pf M = c_P (det G)^4 with G_ab = eta^{mu nu}A^a_mu A^b_nu for all
complex A; substituting A = (-i A~_0, A~_i) gives G_ab = sum_mu A~^a_mu A~^b_mu =:
G~_ab (positive semidefinite, 3x3), so the right-hand-side weight is
c_P (det G~)^4 e^{-S_E}: a constant times a nonnegative function. Integrability with the
extra factor (1+||A~||)^k for k<14 is recorded as proved directly at N=2 (L1554, L1560);
the partition function nonvanishing is proved at N=2 (L1560). e^{-S_E} alone is not
integrable (flat directions), so the bosonic case is taken with a mass.

**Involution.** theta = diag(-1,+1,...,+1): A~_0 → -A~_0, A~_i → A~_i. This is the same
signature reflection used in the D-section "Reflected form" paragraph.

**Lemma 1 (weight invariance).** Each commutator [A~_mu,A~_nu] picks up a factor -1
exactly when it carries exactly one time index, and the HS norm is unchanged, so S_E is
theta-invariant at every N. The Lebesgue measure is invariant. G~_ab = sum_mu
A~^a_mu A~^b_mu is invariant (the mu=0 term A~^a_0 A~^b_0 is invariant). A mass
e^{-(1/2) sum M_{mu nu} Tr A~_mu A~_nu} is theta-invariant iff M is block diagonal
(M_{0i}=0); positive definite block-diagonal masses are used. (This block-diagonal
restriction is a correction I caught while writing: a general positive-definite M with
M_{0i} != 0 is NOT theta-invariant; the manuscript's limit-identity regulator allows
general M, but the RP statement needs the block-diagonal subclass. The MC script uses a
diagonal mass.) Constants (c_P, phases) cancel in normalized ratios.

**Lemma 2 (even/odd split).** For complex f, f_± = (f ± f^theta)/2. Then
f^theta f̄ = (f_+ - f_-)(f̄_+ + f̄_-) = |f_+|^2 - |f_-|^2 + C, C = f_+ f̄_- - f_- f̄_+.
C is purely imaginary and theta-odd: C^theta = -C. Since w := |rho| (the real weight)
and dA~ are theta-invariant, int C w dA~ = int C^theta w dA~ = -int C w dA~, so the cross
term integrates to 0. Hence
  <f,f>_theta := (int f^theta f̄ rho dA~)/(int rho dA~) = (int |f_+|^2 w - int |f_-|^2 w)/(int w).

**Lemma 3 (strict negativity for theta-odd invariants).** If f^theta = -f and f is not
zero a.e.: <f,f>_theta = -int |f|^2 w / int w < 0 strictly, since w >= 0 and w > 0 on a
nonempty open set (for the Pfaffian weight: {det G~ > 0} is open and nonempty — take
A~_mu = delta_{mu,a} sigma^a/2 — and e^{-S_E} > 0; with a mass w > 0 everywhere), and
|f|^2 is a nonzero continuous function positive off a measure-zero algebraic set.
Denominator: nonzero at N=2 (recorded), strictly positive with a mass.

**Probes survive the gauge quotient.** The gauge group is constant U(N) conjugation. By
cyclicity, Tr A~_0 A~_i is invariant, and with A_mu = sum_a A^a_mu sigma^a/2 (the
manuscript convention, appH L1554):
  Tr A~_0 A~_1 = (1/2) sum_a A~^a_0 A~^a_1  (theta-odd, nonzero),
  Tr([A~_0,A~_1]A~_2) = (i/2) eps^{abc} A~^a_0 A~^b_1 A~^c_2  (theta-odd, nonzero for i != j;
  vanishes identically for i=j by cyclicity, hence the i != j restriction).
Both are invariant polynomials; sympy check (7) verifies Tr(U X U^dag) = s Tr X for the
quaternionic U with U U^dag = s I, so the SU(2)-normalized conjugation fixes them.
Descriptively (not used in the proof): by Weyl's first fundamental theorem for SO(3)
these, with the Gram entries sum_a A~^a_mu A~^a_nu, generate the invariant polynomial
algebra of adjoint tuples at N=2.

**Conclusion (bounded no-go).** The OS reflected form (OsterwalderSchrader1973,
OsterwalderSchrader1975) is not nonnegative on the invariant polynomial algebra for:
(i) the N=2 p=4 Euclidean measure (with or without block-diagonal positive mass);
(ii) the bosonic measure with such a mass at every finite N (probes nonzero at every
N; S_E invariance holds at every N). The reflected values are exactly negative:
<-probe> = -int probe^2 w/int w, with the two-point mixed bilinear giving the mixed
two-point function channel.

**Even-subalgebra bound.** If a unital *-subalgebra A has <f,f>_theta >= 0 for all
f in A, then A contains no nonzero theta-odd element (it would have strictly negative
square), so A lies in the theta-even invariant algebra. Any reflection-based
reconstruction from these measures can therefore only use theta-even invariants: no
observable mixing time and space under the signature reflection is admissible.

**Continuation sign.** Tr A_0 A_1 on R_1: in the Pfaffian variables (-i A~_0, A~_i):
-(i/2) sum_a A~^a_0 A~^a_1; on the observable contour (e^{-3 pi i/8}A~_0,
e^{pi i/8}A~_1): (e^{-pi i/4}/2) sum_a A~^a_0 A~^a_1 (sympy check 6). Both are theta-odd
up to a unit-modulus constant phase, reflected value -|phase|^2 * (1/4) int (sum A~^a_0
A~^a_1)^2 w < 0: the negative sign survives the continuation to the Lorentzian side of
the mixed two-point function.

**Relation to recorded material (no duplication, no conflict).**
- D "Reflected form" (L1514–1524): tree-level negative reflected signs on translation-label
  probes of fluctuations about a background. New here: all-orders measure-level failure on
  the base invariant polynomial algebra, with exact values, no background.
- D relaxation (i) (L1526): its premise ("singlet correlators ... satisfy the positivity,
  which is taken from field theory and not checked here") is refuted at the finite-N model
  level on the invariant algebra; the large-N 4d reduced-gauge-theory statement remains
  untested. The package does not conflict with lattice gauge theory OS positivity: there
  the test algebra is generated on one side of a reflection plane and theta maps it to a
  different algebra; here theta is an automorphism of the whole polynomial algebra, which
  is why nonzero odd invariants are fatal.
- CNT (definition C at N=2, appH L1562): concerns equality of expectations for gamma<=0,
  not positivity; no conflict. The CNT gamma<0 data tension (L1562) is untouched.
- Exponential-observable trichotomy (L1564–1568): different question (growth on contours
  of non-polynomial observables); my test algebra is polynomial; the exponential case is
  explicitly not treated here.
- Negative-norm reading of the time components (FurutaHanadaKawaiKimura2007, cited 8x in
  appH): consistent — the bilinear probe is a Gram-mixed singlet.
- Scout hazard H2 respected: no Nishimura-ensemble / CLM / CDT citation is used or implied
  as a signature derivation.

**Comparison with the original target.** E.1 asks to derive (-,+,+,+) and drop
ass:lorentzian. This package derives neither; it closes no route silently: it proves that
the Euclidean-reconstruction route (the route relaxation (i) offers) cannot work on any
test algebra containing the mixed bilinear singlet, at finite N. Combined with the
recorded contour-side no-gos (slice bridge band; gamma→0^- modulus obstruction), both
currently named routes from E's own section are now bounded from one side each. The
remaining honest routes are listed under "Remaining avenues".

## Claim classification

1. Lemma 1 weight invariance — established derivation (within the stated weight class;
   integrability inputs are recorded results at appH L1554/1560, proved at N=2, and the
   k<14-window reading for N>=3 is conditional exactly as appH says).
2. Lemma 2 split identity — established identity (cross-term cancellation proof above).
3. Lemma 3 strict negativity — established derivation given Lemmas 1–2 and w > 0 on an
   open set (checked).
4. Probe identities and nonvanishing — established identities (sympy-checked).
5. RP failure on the invariant algebra (N=2 p=4; bosonic + mass at any N) — conditional
   result on the recorded finite-N Euclidean measures; the N=2 measure facts are recorded
   as proved in appH, the N>=3 bosonic case needs only S_E-invariance + mass integrability
   (established).
6. Even-subalgebra bound — established derivation.
7. Continuation sign — established identity + the conditional R_1 reading of appH.
8. Bearing on relaxation (i) — conditional/bounded (refutes the premise at finite-N model
   level; large-N 4d field-theory positivity: unresolved, explicitly not treated).
9. Weyl-generator description of the invariant algebra — established theorem invoked
   descriptively; the proof only needs the two explicit invariant probes.
10. Nothing here is an input, fit, or conjecture; no number in the package appears without
    derivation or script.

## Proposed changes

Two pure insertions into `chapters/appH-microscopic-proofs.tex` (current: 555396 B, 3269
CRLF, sha256 c39e90f5b3431f8197b8b759e83c95564456cf6191549c7838dd0517a473ca26 = digest
c39e90f5b343). No other file changes. No bib change. No new label. No status/priority/
completion text is altered; both insertions sit above the unchanged Status lines.

### Change 1 — Problem E section, immediately before `\paragraph{Status.}`

Anchor A_E (raw bytes, occurs exactly once, at offset 269380):
`PROGRAMME-CONDITIONAL.\r\n\r\n\r\n\r\n\r\n\paragraph{Status.}\r\nRemains Assumption~\ref{ass:lorentzian}.`
(The tail is unique: the only other `Remains Assumption~\ref{...}` in the file is for
`ass:EFT-a2` at 554979.) Insertion point: 269406, i.e. immediately after the prefix
`PROGRAMME-CONDITIONAL.\r\n\r\n` inside the anchor; inserted bytes = insert-E.tex
converted to CRLF. The preceding paragraph (the gamma→0^- link paragraph ending
"Problem~E remains open and PROGRAMME-CONDITIONAL.") and the `\paragraph{Status.}` /
"Remains Assumption~\ref{ass:lorentzian}." lines are kept verbatim. This placement
follows the E-chain precedent (053/055/056/057: inserts immediately before the Problem E
Status paragraph).

Block file `insert-E.tex` (LF, trailing LF included): 4781 B, CR count 0,
sha256(LF) = 0e7ca8330cfd90ec5cd2bb0c07367178ef764a9ea10252600a4f64331acac548;
CRLF form 4843 B, CR = 62, sha256(CRLF) =
c2e633c65fa557a7d89874796b8cba83946f18cb5a43b8f58612d8172680dc74.

The LaTeX (identical to insert-E.tex):

```latex
\paragraph{Reflection positivity of the Euclidean measure at \(N=2\): failure on the
invariant algebra and the even-subalgebra bound (conditional; bounded no-go).}
Fix the reflection \(\theta=\mathrm{diag}(-1,1,\dots,1)\), acting on the Euclidean
variables of \(\mathcal R_1\) by \(\tilde A_0\mapsto-\tilde A_0\),
\(\tilde A_i\mapsto\tilde A_i\), and consider the normalized reflected pairing
\(\langle f,f\rangle_\theta=\int f^\theta\bar f\,\rho\,\mathrm d\tilde A\big/
\int\rho\,\mathrm d\tilde A\) on polynomial observables, with
\(f^\theta(\tilde A)=f(\theta\tilde A)\) and \(\rho\) one of the Euclidean weights on
the right-hand side of the displayed limit identity: \(\rho=c_{\mathrm P}
(\det\tilde{\mathcal G})^4\mathrm e^{-S_{\mathrm E}}\) at \(N=2\) with the content
above (integrable by the paragraph on the bound along the flat directions), the
Pfaffian reading there following from \(\operatorname{Pf}\mathcal M=c_{\mathrm P}
(\det\mathcal G)^4\) with \(\mathcal G_{ab}=\eta^{\mu\nu}A^a_\mu A^b_\nu\) at
\(A=(-\mathrm i\tilde A_0,\tilde A_i)\), or \(\rho=\mathrm e^{-S_{\mathrm E}}\mathrm
e^{-\frac12\sum_{\mu,\nu}M_{\mu\nu}\operatorname{Tr}\tilde A_\mu\tilde A_\nu}\) for
any positive definite block-diagonal \(M\) with \(M_{0i}=0\) at any \(N\); constant
factors cancel in the ratio, and the denominator is nonzero for the Pfaffian weight
at \(N=2\) and strictly positive with a mass. Each commutator in \(S_{\mathrm E}\)
changes sign exactly when it carries one time index, so \(S_{\mathrm E}\), the
Lebesgue measure, every such mass factor and the Gram
\(\tilde{\mathcal G}_{ab}=\sum_\mu\tilde A^a_\mu\tilde A^b_\mu\) are
\(\theta\)-invariant, and with \(f_\pm=(f\pm f^\theta)/2\) one has
\(\langle f,f\rangle_\theta=(\int|f_+|^2w-\int|f_-|^2w)/\int w\) with \(w\ge0\) the
real weight. Hence every \(\theta\)-odd polynomial not vanishing almost everywhere
has strictly negative reflected value \(-\int|f|^2w/\int w\), and such polynomials
are gauge invariant: \(\operatorname{Tr}\tilde A_0\tilde A_i=
\frac12\sum_a\tilde A^a_0\tilde A^a_i\), and, with
\(A_\mu=\sum_aA^a_\mu\sigma^a/2\), \(\operatorname{Tr}([\tilde A_0,\tilde A_i]
\tilde A_j)=\frac{\mathrm i}2\epsilon^{abc}\tilde A^a_0\tilde A^b_i\tilde A^c_j\) for
\(i\ne j\); both are nonzero and \(\theta\)-odd and invariant by cyclicity of the
trace (with the Gram entries they are the generators of the invariant polynomial
algebra of adjoint tuples at \(N=2\), Weyl's first fundamental theorem for
\(\mathrm{SO}(3)\) with the \(\epsilon\)-contractions). Therefore the measures of
this weight class, with \(p=4\) content at \(N=2\) and with or without a mass, and
bosonically with a mass at every finite \(N\), do not satisfy the reflection
positivity of~\cite{OsterwalderSchrader1973,OsterwalderSchrader1975} on the
invariant polynomial algebra: the failure sits on manifestly gauge-invariant
bilinear and cubic singlets, not only on the translation labels of
Section~\ref{sec:status-D}. Any unital \(*\)-subalgebra on which
\(\langle\cdot,\cdot\rangle_\theta\) is nonnegative contains no nonzero
\(\theta\)-odd element, since such an element would have negative square, so every
reflection-positive test algebra for these measures lies in the \(\theta\)-even
invariant algebra, and every invariant mixing time and space under \(\theta\) is
excluded from any reconstruction from these measures. On the continuation side
\(\operatorname{Tr}A_0A_i\) restricted to \(\mathcal R_1\) is
\(-\frac{\mathrm i}2\sum_a\tilde A^a_0\tilde A^a_i\) in the Pfaffian variables
\((-\mathrm i\tilde A_0,\tilde A_i)\) and \(\frac{\mathrm e^{-\pi\mathrm
i/4}}2\sum_a\tilde A^a_0\tilde A^a_i\) on the observable contour, still
\(\theta\)-odd up to a constant phase of unit modulus with strictly negative
reflected value: the negative sign passes to the Euclidean-side continuation of the
mixed two-point function. These statements are for the Euclidean weights above and
polynomial test functions at the stated \(N\) (for the regulated Lorentzian measure
the weight is not nonnegative, so the even-odd identity gives no sign); they do not
treat the signed fermionic Pfaffian at \(N\ge3\), which is not a nonnegative weight
and where the determinant identity is unavailable, the large-\(N\) singlet algebra
of relaxation (i) of Section~\ref{sec:status-D}, other involutions, non-polynomial
test algebras, the thimble contour integrals of~\cite{ChouNishimuraTripathi2025}, or
the slice bridge left open above. The bearing is to bound the reconstruction route
of that relaxation at the finite-\(N\) Euclidean level, complementing the
contour-side no-go, and to derive nothing: no signature, no background and no frame
is obtained, Assumption~\ref{ass:lorentzian} is not discharged. Problem~E remains
open and PROGRAMME-CONDITIONAL.
```

### Change 2 — D-section relaxations paragraph, inside item (i), after its final sentence

Anchor A_D (occurs exactly once, offsets 235533–235613):
`and the diagonal elements, so Assumption~\ref{ass:lorentzian} is not discharged.`
Insertion at offset 235613 (before the following ` (ii) \emph{Constraint.}`). All
existing text of items (i)–(iv) and the L1528 closer are kept verbatim.

Block file `insert-D.tex` (LF): 468 B with trailing LF, CR 0, sha256(LF, as stored) =
7b9cadaee6e22ee8e121e6de61b1a830755ab5dc1d06c870719b9b24a6baf205. The applied form is
the same text with the trailing newline stripped: 467 B, CR 0, sha256 =
73c35e54f36c94a9de1cc6c0135837cf58e078b2c07b7edc951e774b630f612e. The applied sentence
(begins with a leading space, appended in-line):

```latex
 The positivity taken from field theory already fails on the finite-\(N\) invariant algebra of the Euclidean model: the paragraph ``Reflection positivity of the Euclidean measure at \(N=2\)\dots{}'' of Section~\ref{sec:status-E} exhibits \(\theta\)-odd invariant polynomials with strictly negative reflected pairing, at \(N=2\) with the content above and bosonically at every finite \(N\) with a positive mass; the large-\(N\) field-theory statement remains untested.
```

### Post-apply predictions (from simulate_apply.py on the current bytes)

After both insertions: 560706 B (delta +5310), 3331 CRLF lines, bare LF count 0,
sha256 = 4f15b0719ac3d8dc588b20b289fcef91fbe91775168e169438b9251c83506be6.
If the integrator applies only Change 1: 555396 + 4843 = 560239 B.

### Stale passages elsewhere

None. No passage in any other file contradicts or is contradicted by the insertions; the
ch17 E passage (L395–399) and the criterion remain accurate as stated. No replacement
text anywhere.

### Bibliography

Zero new entries. Keys cited in the insertions, all already present in `bib/namcg.bib`
and verified by me earlier against primary records:
- OsterwalderSchrader1973: OSTERWALDER, Schrader, Comm. Math. Phys. 31 (1973) 83–112,
  doi 10.1007/BF01645738 (record verified).
- OsterwalderSchrader1975: Comm. Math. Phys. 42 (1975) 281–305, doi 10.1007/BF01608978
  (record verified).
- ChouNishimuraTripathi2025: PRL 134, 211601, doi 10.1103/PhysRevLett.134.211601,
  arXiv 2501.17798 (record verified).
Existing keys used via \ref only: sec:status-D (label at L645), sec:status-E (L1537),
ass:lorentzian, eq:Smatrix — all confirmed present; no new label introduced (checked: 0
`\label` in both blocks); no duplicate `\ref` risk.

## Verification scripts

All in this folder; run with `python -I <script>` (outputs saved next to each).

1. `rp_identities_n2.py` + `rp_identities_n2.out` — sympy, manuscript convention
   A_mu = sum_a A^a_mu sigma^a/2: (1) Tr A~_0 A~_1 = (1/2) sum_a A~^a_0 A~^a_1; (2)
   Tr([A~_0,A~_1]A~_2) = (i/2) eps^{abc}A~^a_0 A~^b_1 A~^c_2; (3) both probes theta-odd;
   (4) S_E theta-invariant (truncated model mu=0,1,2, covers all term types); (5) Gram
   G~_ab and det G~ theta-invariant; (6) R_1 continuation phase e^{-pi i/4} for the
   bilinear; (7) SU(2)-type covariance Tr(U X U^dag) = s Tr X; (8) Gaussian toy:
   normalized reflected pairing of f = y0 y1 equals -1/4, and of g = 1 + y0 y1 equals
   +3/4 (identity check of the split formula). ALL_CHECKS_PASS: True.
2. `rp_mc_n2.py` + `rp_mc_n2.out` — seeded Metropolis on the 9-variable N=2 truncated
   model (mu = 0,1,2), diagonal positive mass m^2 = 1: both weights p=0 and
   p=4 = (det G~)^4; measured reflected pairings of both probes: p=0: -1.07859,
   -0.34388; p=4: -0.98501, -12.71516; cross-check <f1> ~ 0 (theta-symmetric measure);
   second seed reproduces. Signs strict negative at both weights and both probes.
3. `simulate_apply.py` + `simulate_apply.out` — byte-level simulation of the two
   insertions on the current appH bytes (read-only; no file modified): anchor counts
   (A_E: 1 at 269380; A_D: 1 at 235533), insertion offsets (269406; 235613), block
   sizes/hashes in LF and CRLF forms, CR counts 0, predicted post-state
   560706 B / 3331 CRLF / 0 bare LF / sha256 4f15b071..., and key-existence guards.

## Decisions Taken

1. **Avenue choice (RESEARCHER-DECISION from mandate ranking).** Chosen: avenue 2
   (reflection positivity for the N=2 singlet/invariant sector) as a SHARP FAILURE with
   named quotient-surviving probes, plus the even-subalgebra bound and the continuation
   sign. Reason: it is fully derivable at finite N within one package, it directly
   attacks the positivity premise that D-relaxation (i) imports from field theory (the
   only manuscript-sanctioned Euclidean reconstruction route), and it is the only avenue
   whose deliverable is a theorem rather than a conditional estimate. Rejected: avenue 1
   (thimble/intersection control of the anti-Wick slice) — the vector-mining report CC-E1
   confirms it is untouched, but a defensible intersection-counting result for the D-class
   backgrounds is larger than this package's evidence boundary and its payoff is a band
   refinement, not a premise test; avenue 3 (Liao 2609.40183 radical/semisimple saddle
   constraints) — algebraic classification is literature-import heavy, and scout H3 marks
   it as constrained but not closing anything; avenue 4 (CNT gamma<0 tension) — a data
   reconciliation with no bearing on signature unless it changes the (C)-equivalence
   scope, which I could not test; recorded as later work with hazard H4 respected.
2. **Zero new references.** No new bib entries. A claimed Fukuma–Koike–Tanizaki thimble
   "review" I checked first (arXiv 2509.13200) is a robotics paper (StageACT) — the
   claimed review does not exist under that id; author/title searches on export.arxiv.org
   found no such review. Per the "unverifiable ids must not appear" rule it is excluded
   entirely. Handrack–Salmhofer 2026 (arXiv 2608.10685, verified record) was considered
   and NOT cited: not needed for any claim here.
3. **No new label.** The E paragraph is referenced from the D append by its printed
   heading rather than a \label, matching current manuscript practice (no paragraph
   labels exist in appH); avoids any duplicate-label risk. `par:rp-E-n2` confirmed absent
   and is left unused.
4. **Block-diagonal positive masses** replace "any positive definite M" in the RP weight
   class, because M_{0i} != 0 masses are not theta-invariant; the limit identity itself
   (general M) is untouched. MC uses a diagonal mass, consistent.
5. **Bosonic p=0 case carries a mass** (e^{-S_E} alone is non-integrable on the flat
   directions); stated explicitly in the block.
6. **Anchor strategy**: E-insertion placed by the unique long anchor including
   `Remains Assumption~\ref{ass:lorentzian}.` (distinguishes it from the identical-shaped
   `ass:EFT-a2` Status at 554979); `\paragraph{Status.}` alone occurs 6x and was not used.

## Milestone assessment

Routine. Bounded no-go / premise refutation at the recorded finite-N class, comparable to
the 056/057 E-chain items: no MILESTONE.md trigger (no critical-path step derived, no
missing link closed for the programme).

## Status-label recommendation

Re-derived from the current ledger snapshot (ch17 criterion L714–722 + appH status lines
L16/124/483/648/1540/1585/2770/3134): critical-path set {A, B, C, D1, E, F, G-derived, N}.
Labels affected by this package: **none**. Problem E stays OPEN, CRITICAL PATH for the
matrix-derived label, PROGRAMME-CONDITIONAL. No recommendation to change anything.

## Author decision needed

None. (Nothing here changes the core, the scope, or a critical-path dependency; spacetime
remains emergent throughout — the package is a positivity no-go for a class of measures,
not a geometric input.)

## Remaining open step

E.1 still requires deriving (-,+,+,+) of the locked vacuum and dropping ass:lorentzian.
What remains open after this package:
- whether any Lorentzian definition (A)/(B)/(C) carries a positivity structure that
  survives at all (the Lorentzian weights are oscillatory; the Euclidean-side pairing is
  now known non-positive on mixed singlets);
- the signed fermionic Pfaffian at N>=3: is there any involution under which a signed
  measure's reflected form is controlled, or an exact sign/equivariance statement for
  Pf M under theta-type maps;
- the large-N singlet algebra: positivity of 4d reduced-gauge-theory singlet correlators
  (relaxation (i)'s untested premise) — untouched and still the only open
  reconstruction-side hypothesis;
- other involutions / reflection planes in the reduced model; non-polynomial test
  algebras;
- the recorded contour-side obstructions (slice bridge band, gamma→0^- modulus) and the
  untouched thimble/intersection route (vector-mining CC-E1).

## Ranked remaining avenues (for follow-up packages)

1. Thimble / intersection-number control of the anti-Wick-slice bridge (avenue 1; CC-E1
   "untouched"): replace the exponential linking bound by an intersection-counting
   statement on the D-class backgrounds; would attack the recorded slice-bridge band.
2. Signed-Pfaffian analysis at N>=3 (theta-equivariance or sign structure of Pf M on real
   Euclidean A): decides whether this package's no-go extends to the full IKKT measure.
3. Large-N singlet positivity (relaxation (i)): lattice-regularized reduced gauge theory
   evidence; hazard H2 (must not be cited as a signature derivation).
4. Liao 2609.40183 radical/semisimple saddle constraints applied to the D-class
   backgrounds (avenue 3; scout H3).
5. CNT gamma<0 data tension at appH L1562 (avenue 4; preserve the "not resolved here"
   sentence, hazard H4).

## Special instructions for the gatekeeper

- Re-derive Lemma 2 including the cross-term cancellation (C purely imaginary and
  theta-odd forces int C w = 0) — the manuscript sentence states the identity without the
  cross term; the md proof is the full version.
- Re-derive the strictness of -int|f|^2w/int w: needs w > 0 on a nonempty open set
  (Pfaffian weight: det G~ > 0 open set, e.g. A~_mu = delta_{mu,a} sigma^a/2) and
  integrability of the p=4 weight at k=0 (recorded proved at N=2, appH L1554/1560).
- The blocks must not be read as closing E, discharging ass:lorentzian, or resolving
  relaxation (i) at large N; the D-append says explicitly the field-theory statement
  remains untested. Verify both closers are present and are the last sentences of their
  blocks.
- Verify anchors/offsets/hashes by re-running `python -I simulate_apply.py` (must print
  SIMULATION_OK and the sha above on the current appH); note the D applied form strips
  the trailing newline (467 B block).
- No new bib entries; verify the three cited keys exist in bib/namcg.bib.
- Do not import lattice-gauge RP as contradicting this: the difference (theta as an
  automorphism of the test algebra vs reflection-plane algebras) is part of the package.
- Hazard H2: no Nishimura-ensemble/CLM/CDT material is cited or implied.
