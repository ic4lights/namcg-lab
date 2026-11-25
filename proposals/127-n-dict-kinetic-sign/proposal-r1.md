# Proposal 127-n-dict-kinetic-sign, round 1  [STRUCTURAL - author only]

## Result / negative result (what is established; no overclaiming)

**Negative result (derivation-quality), hypothesis class stated.** Let
\(\Theta^{\mu\nu}\) be real, antisymmetric and non-degenerate (the reality
forced by hermitian \(\hat X^\mu\) in \eqref{eq:NC}) and let \(g^{(0)}_{\mu\nu}\)
be non-degenerate Lorentzian (Assumption ass:lorentzian). Consider the quadratic
transfer class: transfers through the dictionary image \eqref{eq:dictionary} of any
quadratic \(\eta\)- or \(g^{(0)}\)-contracted commutator term of \eqref{eq:Smatrix},
all indices saturated by \(g^{(0)}\) or its inverse, dagger or non-dagger, with no
inserted background tensors (in particular no \(C\)-tensor insertions), retaining only
the two-derivative \(p^2\) coefficient. Then, established:

1. **(Tensor type.**) Every member of the class yields a kinetic tensor equal, up to a
   constant factor, an overall sign, and index placement, to
   \(K^{\mu\nu}=\Theta^{\alpha\mu}g^{(0)}_{\alpha\beta}\Theta^{\beta\nu}\) of
   Definition def:matrix-coords-ext (plain and dagger contractions give the two overall
   signs; checked symbolically for generic \(\Theta\), checks S5a-S5c).
2. **(K is a competing Lorentzian tensor, never a failed metric.**) \(K\) is congruent
   to \(g^{(0)}_{\mu\nu}\) (Sylvester), hence Lorentzian of the same signature for
   every non-degenerate \(\Theta\) (S1b, S1f).
3. **(Non-matching, new proof of the recorded obstruction, plus its extension.**)
   \(K = \lambda\, g^{(0)-1}\) has no solution over real non-degenerate data: with
   \(A=\Theta\eta\) one has \(A^2=-K\eta\) and \(\det A=-\mathrm{pf}(\Theta)^2\),
   while \(K=\lambda\eta\) forces \(A^2=-\lambda I\), hence
   \(\lambda^2=\det A=-\mathrm{pf}^2\), impossible for real non-degenerate data
   (S1a-S1d); this reproves the recorded conjugate-coordinate non-proportionality in one
   line for the identity embedding. Adding a background trace insertion \(s\,g^{(0)-1}\)
   changes the matching equation only by that multiple and creates no new real solution
   (S3a-S3b). Over the complex numbers the matching equation is solved exactly by the
   (anti-)self-dual class \(q=\pm i\,p\) in the aligned normal form - the unique
   escape, contradicting the hermiticity of \eqref{eq:NC} (S1g-S1h).
4. **(Sign/positivity no-go - the new step.**) The energy of a scalar kinetic term of
   \(K\)-type is bounded below exactly for time directions inside the cone of \(K\)
   (standard plane-wave criterion, checks S4a-S4c). Hence positivity for the full
   \(g^{(0)}\)-time cone would force the cone inclusion \(C_{g^{(0)}}\subseteq C_K\),
   and by maximality of Lorentzian cones equality and proportionality, excluded by 3.
   For \(g^{(0)}=\eta\) the statement is strict and exact: with
   \(E_i=\Theta_{0i}\), \(b_i=\tfrac12\epsilon_{ijk}\Theta^{jk}\),
   \((K^{-1})_{00}=|b|^2/\mathrm{pf}(\Theta)^2>0\) identically in the six components
   of \(\Theta\) (S2a-S2c, S2g): the \(g^{(0)}\)-time direction is strictly
   \(K\)-spacelike for every real non-degenerate \(\Theta\), and the energy is
   unbounded below for every normalization and both overall signs. Purely spatial
   \(\Theta\) is the recorded degenerate case (S2f).
5. **(Dependency resolution.**) The frontier edge N.dict-kinetic-sign ("the manuscript
   records nothing that pins down the kinetic-sign direction of ass:dictionary") resolves
   as follows: the sign direction cannot be pinned by the transfer route at all on core
   data - it is a datum, free in both directions as a sign within the class. The
   Presentation-B matrix-quantum-mechanics realization of the Problem N sublemma
   hypotheses (appH, paragraph "Realization of the spectral-positivity hypotheses...")
   needs no transfer and is untouched by this no-go; the no-go bars only the
   Presentation-A supply route, i.e. the sign clause of Assumption ass:dictionary as a
   derivable matching condition.

Not established and not claimed: any closure of Problem N, Problem A, or
Assumption ass:dictionary; a derivation of the datum in any direction; curved-
background versions of the strict-spacelike statement beyond the flat adapted frame
(the covariant content actually used is item 4's first sentence, which needs only the
recorded non-proportionality); exhaustion of contraction classes beyond the named
transfer class. No status label is changed by this package.

## Target and status (problem(s), current Appendix H status/priority, original
## target, dependencies)

- **Target:** the missing step recorded in the live appH Problem N entry as the
  input "the kinetic-sign content of Assumption~\ref{ass:dictionary} that
  Presentation~A reproduces the convention of Equation~\eqref{eq:Smicro}" (appH
  L4025, live sha1 123108d4a947...), i.e. the edge the frontier records as
  N.dict-kinetic-sign (reports/graph/frontier.yaml L1430-1542, sha1
  256c37c88162..., routing flag STRUCTURAL to this agent). Connected: the sign
  clause of Assumption ass:dictionary (ch03 L358-361, Problem A), Problem N
  (critical path for the matrix-derived label, PROGRAMME-CONDITIONAL per the live
  ch17 L497-516 and the N ledger entry), and Problem A.
- **Current status (live bytes, unchanged by this package):** Problem N: OPEN,
  critical priority, completion not achieved; Assumption ass:dictionary: OPEN
  matching condition; Problem A: OPEN. This package changes none of these; it
  determines that the named input is not derivable within the quadratic transfer
  class and records its datum status.
- **Dependencies:** the package consumes only core-stated data: \eqref{eq:NC},
  \eqref{eq:Smatrix}, \eqref{eq:Smicro}, Definition def:matrix-coords-ext,
  Assumptions ass:lorentzian and ass:nondeg, and the recorded conjugate-coordinate
  non-proportionality theorems (appH Problem F section, L2711-2744) and the
  recorded lift-tensor observation (appH, 120-commutator-lift-bridge paragraph,
  L1735). It unblocks nothing by construction; it converts a named open input into
  a proved datum-status (an honest negation of the transfer reading of that input).
- **Original target after this package:** the target "derive the kinetic-sign
  direction of the dictionary transfer from Presentation A" is proved
  unattainable within the named class (negation, this package). The residual
  target is one of the ranked escapes listed below or the acceptance of the datum.

## Source reading (what was read in full vs skimmed; digest status)

- Digest scratch/digest.md sha1 c7fe588c... read first; digest freshness caveat
  noted (permanently-dirty tree), live bytes re-hashed for every file relied on.
- READ IN FULL (live bytes): appH L3872-4144 (complete Problem N ledger entry:
  sublemma L3987-4023, the matrix-quantum-mechanics realization paragraph L4025,
  completion-class paragraph L4027-4055, deferral L4058-4072, 121 paragraph
  L4074-4132); ch17 L497-516, L650-676, L693-740; ch03 L120-364 (\eqref{eq:NC},
  \eqref{eq:Smatrix}, Definition def:matrix-coords-ext incl. the
  \(K^{\mu\nu}\) display L192 and the explicit non-identification paragraph
  L199-204, \eqref{eq:Smicro} and sign note, Assumption ass:frame-lock,
  \eqref{eq:Phi-transform}, Section sec:ch3-relate, Assumption ass:dictionary
  L345-363); ch04 L140-199 (def:composite-metric, \eqref{eq:g-from-e},
  ass:nondeg) and L300-334 (ass:lorentzian); ch05 L55-99; ch09 L40-167
  (thm:ostro, ass:EFT-a2 and compositeness paragraph, UV lists); ch01 L170-212;
  appA L55-159; appH L1725-1745 (120 lift paragraph) and L2700-2750 (conjugate-
  coordinate theorems) re-read in full for this package; MILESTONE.md triggers.
- READ IN FULL: proposals/124-n-mqm-pos/review-r2.md (ACCEPT; avenue ranking that
  names the ass:dictionary kinetic-sign step as the unique transfer step) and
  review-r1.md L25-40; frontier.yaml L1430-1542 (N gap and edge rows verbatim);
  121 proposal-r2 Result section.
- BY POINTER (not read in full): bodies of proposals/124 proposal-r1/r2 (their
  content was summarized in the reviews read in full); 067 proposal/manifest;
  remainder of frontier.yaml and digest; all other chapters skimmed via digest
  and label grep only. **Digest + targeted reads; no full scan was performed and
  none is claimed** (3(c) scan is the gatekeeper's, triggered by this package).

## Core-aspect register delta (aspects examined/changed; file:line; dependents)

Register lives at proposals/127-n-dict-kinetic-sign/core-aspect-register.md (built
this task from live bytes). Aspects this package touches or relies on:

| aspect | locus | states | used by | breaks without/with it | class |
|---|---|---|---|---|---|
| ass:dictionary sign clause | ch03 L358-361 | transfer of the quadratic commutator term must generate the eq:Smicro kinetic term including its sign | A; N input chain (appH L4025); review-124 avenue (1) | package records it unsatisfiable as transfer on real data; datum either way | candidate-for-redaction -> datum-record (proposed) |
| def:matrix-coords-ext K display | ch03 L192 | K = theta-theta-eta contraction | ch03 L199-204 non-identification; appH L1735 lift; appH F-section theorems | package extends: K always Lorentzian, g0-spacelike time; nothing breaks | emergence-preserving |
| conjugate-coordinate theorems | appH L2711-2744 | G = K^-1 nowhere proportional to g, any real Lorentzian leaf metric, D >= 4 | Problem F selection discussion; ch03 L199-204 | package consumes, does not change; supplies the covariant non-matching | emergence-preserving |
| 120 lift paragraph | appH L1735 | recorded shift-symmetric lift has K-type kinetic tensor; K = c g no real solution; spatial Theta degenerate K | D1 bridge; this package | package generalizes the tensor-type claim to all class members | emergence-preserving |
| 124 realization paragraph | appH L4025 | Presentation-B MQM class realizes N sublemma hypotheses; lists ass:dictionary kinetic-sign as first pinned input | N | untouched by the no-go (needs no transfer); its input list gains datum status | emergence-preserving |
| eq:NC hermiticity (Theta real) | ch03 L120-140 | [X,X] = i Theta with hermitian X => Theta real | all of ch03-ch05 | complex-Theta escape (S1h) contradicts it: listed as escape with cost | emergence-critical (not proposed to change) |
| ass:lorentzian | ch04 L300-334 | g0 Lorentzian background | E; N; this package | consumed, unchanged; the K-cone of the package is an alternative emergent cone, never a fundamental metric | emergence-critical (preserved by derivation) |

No other definition, assumption or scope statement is modified. The register file
lists all examined aspects with dependents as read from live label grep.

## Research and reasoning (the derivation or obstruction chain)

**Setup.** Dictionary image \([\hat X_\mu,\Phi]\longleftrightarrow i\Theta_{\mu\nu}D^\nu\Phi\)
(\eqref{eq:dictionary}); a quadratic commutator term of the class has all Lorentz
indices saturated by \(\eta\) or \(g^{(0)}\) (the only background tensors the class
admits); at quadratic order in \(\Phi\) each factor is replaced by its dictionary
image, so the kinetic tensor is built from two copies of \(\Theta\) and two copies of
the background or its inverse, with all orderings that make a \((2,0)\) or \((0,2)\)
tensor. Up to transposition (\(\Theta\) antisymmetric) and the overall sign from the
dagger, the only possibilities are \(K^{\mu\nu}=\Theta^{\alpha\mu}g^{(0)}_{\alpha\beta}
\Theta^{\beta\nu}\) and its index-lowered variants: the two explicit contractions
(non-dagger and dagger) are computed symbolically and give exactly \(+\eta K\eta\) and
\(-\eta K\eta\) (checks S5a-S5c), which raise to \(\pm K\).

**Step 1 (congruence).**** \(K=\Theta^{T}g^{(0)}\Theta\) is a congruence of
\(g^{(0)}\); by Sylvester's law \(K\) is non-degenerate Lorentzian of the same
signature for every non-degenerate real \(\Theta\). Symbolic support: S1b
(\(\det K=\det(g^{(0)})\det\Theta^{2}\)), S1f (canonical form
\(\mathrm{diag}(p^2,-p^2,q^2,q^2)\)).

**Step 2 (non-matching, new one-line proof and extension).** Suppose
\(K=\lambda\,g^{(0)-1}\). Work at the identity embedding \(g^{(0)}=\eta\) (the
general leaf case is the recorded theorem, appH L2711-2744). With \(A=\Theta\eta\):
\(A^2=\Theta\eta\Theta\eta=-K\eta\) (from \(\Theta^T=-\Theta\); identity
checked as S1c), and \(\det A=\det\Theta\,\det\eta=-\mathrm{pf}(\Theta)^2\)
(S1a, S1d). If \(K=\lambda\eta\) then \(A^2=-\lambda I\), so the minimal
polynomial of \(A\) divides \(t^2+\lambda\), the characteristic polynomial is
\((t^2+\lambda)^2\) and \(\det A=\lambda^2\ge 0\). Hence
\(\lambda^2=-\mathrm{pf}^2\): real forces \(\mathrm{pf}=0\), i.e. degenerate
\(\Theta\), and then \(\lambda=0=K\) forces \(\Theta=0\). Over
\(\mathbb C\) the aligned normal form gives \(q=\pm i\,p\), equivalently
(anti-)self-duality, and these do solve \(K\propto\eta\) (S1h witness), which is
why the escape list starts there. Trace-insertion extensions
\(K+s\,g^{(0)-1}=c\,g^{(0)-1}\) are again proportionality (S3a: the residual
conditions are exactly the off-diagonal and \(K_{00}+K_{ii}\) conditions of S1).

**Step 3 (sign/positivity).** For a scalar kinetic term with non-degenerate
Lorentzian tensor \(G^{\mu\nu}\), the Hamiltonian along a time direction \(t\)
is bounded below iff \(t\) lies in the closed cone of \(G\) with the matching
orientation (standard two-branch plane-wave argument; the two checks S4a/S4b/S4c
confirm the criterion distinguishes exactly the proportionally-positive case). The
full \(g^{(0)}\)-positivity the sign clause demands is therefore equivalent to
\(C_{g^{(0)}}\subseteq C_K\) up to orientation; Lorentzian cones are maximal among
proper cones of quadratic forms (inclusion of null-cone inclusions forces
proportionality of the forms), so \(C_{g^{(0)}}\subseteq C_K\) gives
\(K\propto g^{(0)-1}\), excluded by Step 2 for every class member and every
normalization, both signs included.

**Step 4 (strict flat-frame lemma).** At \(g^{(0)}=\eta\), in the background frame
of \eqref{eq:Smicro}, the failure is strict and identity-level. With
\(E_i=\Theta_{0i}\) and \(b_i=\tfrac12\epsilon_{ijk}\Theta^{jk}\), for generic
six-component \(\Theta\): \(\det\Theta=\mathrm{pf}^2\) with
\(\mathrm{pf}=E^ib_i\) (S1a); the spatial block of \(K\) has determinant
\(-|b|^2\mathrm{pf}^2\) (S2a, from
\(K_{\mathrm{sp}}=|b|^2 I-EE^{T}-bb^{T}\) and the determinant lemma); and
\((K^{-1})_{00}=\det K_{\mathrm{sp}}/\det K=|b|^2/\mathrm{pf}^2>0\) whenever
\(\mathrm{pf}\ne 0\) (S2b-S2c, S2g; the strict inequality uses
\(\mathrm{pf}=E\cdot b\ne 0\Rightarrow b\ne 0\)). So \(\partial_0\) is
strictly \(K\)-spacelike for every real non-degenerate \(\Theta\): the recorded
dichotomy (generic: wrong cone; purely spatial: degenerate, no time derivative -
appH L1735, S2f) is exhaustive, and in neither branch does the transfer carry the
eq:Smicro sign.

**Step 5 (dependency resolution).** The appH N entry (L4025) pins the sublemma
hypotheses' open content to three inputs, the first being this kinetic-sign content.
The Presentation-B MQM realization derives the sublemma hypotheses inside its named
class from \eqref{eq:Smicro} alone; it never consumes the transfer. Hence the no-go
does not weaken any realized N step; it retires the transfer reading of the input and
relabels it: the input is a stated convention/datum of the dictionary, and any future
derivation of it must come from one of the escapes, not from the current core data.

Literature: not used; the positivity criterion and cone maximality are standard
textbook facts, quoted as such, no external citation needed or invented.

## Claim classification

- **Established identity/derivation** (all with symbolic checks in
  verify_dict_sign_127.py, generic six-component \(\Theta\), not sampling, except
  where noted): the transfer-class tensor type for the two explicit contractions
  (S5a-S5c); \(\det\Theta=\mathrm{pf}^2\); \(\det K=\det(g^{(0)})\det\Theta^2\);
  \(A^2=-K\eta\); \(\det A=-\mathrm{pf}^2\); canonical form of \(K\);
  non-existence of real solutions of \(K=\lambda\eta\) for non-degenerate
  \(\Theta\) (general \(A\)-argument; the aligned-normal-form solution set is
  exact via linear algebra in \(p^2,q^2\), and Lorentz classification of real
  two-forms is input as a standard fact); complex solution set
  \(q=\pm ip\) in the aligned form (S1g-S1h); the trace-insertion reduction
  (S3a); \(\det K_{\mathrm{sp}}=-|b|^2\mathrm{pf}^2\) and
  \((K^{-1})_{00}=|b|^2/\mathrm{pf}^2>0\) (exact identities; sampling S2d only
  illustrates); degenerate spatial case (S2f, matches recorded text).
- **Conditional result:** Step 3's boundedness criterion is a standard field-theory
  lemma, established conditional on its hypotheses (second-order scalar,
  non-degenerate Lorentzian \(G\), WKB/legal-class assumption on states); the
  covariant non-matching for curved \(g^{(0)}\) is conditional on the recorded
  leafwise theorem (appH L2711-2744), which is cited, not reproved here.
- **Exhaustion input (declared, not proved):** the enumeration of transfer-class
  members is by index placement (two \(\Theta\)'s, background metrics saturating
  all indices); the two computed contractions are the two index orientations with
  and without the dagger; no other \((2,0)/(0,2)\) saturation exists inside the
  declared class. This is an honest class definition, verified for its two
  elements, not a proved classification theorem of an unrestricted operator basis.
- **Phenomenological input:** none introduced.
- **Conjecture/mechanism:** none used.
- **Unresolved after this package (unchanged from before):** everything Problem N
  and Problem A actually ask; the datum itself in either direction; all escapes.

## Structural impact and compatibility ledger

Commitments the proposed record-payloads must preserve (enumerated from the live
manuscript, not from memory):

1. **The metric is emergent (hard invariant).** Preserved by derivation: the package
   adds no metric at any level; \(K\) is an emergent-derived tensor of the
   condensate phase, and the payloads state its non-identity with \(g^{(0)}\),
   reinforcing rather than relaxing emergence. No option in this package
   fundamentalizes spacetime; the excluded escapes are reported, not adopted.
2. **ass:lorentzian / \eqref{eq:g-from-e} chain (ch04).** Preserved unchanged: the
   payload never identifies \(K\) with any metric of the book; escape (b)
   (re-identifying the \(K\)-cone with the eq:Smicro kinetic structure) is listed
   with its cost (it would overturn \eqref{eq:g-from-e} and the recorded Problem D
   and F consumption chain) and is NOT proposed.
3. **ch17 full-GR / matrix-derived criterion (A, B, C, D1, E, F, G-derived, N).**
   Preserved: no criterion item is asserted complete; N's input list is relabeled
   (datum), never discharged; the payload sentences end in "not closure" register
   and the appH paragraph repeats the 124 paragraph's own non-closure formulae.
4. **thm:ostro / ass:EFT-a2 reading of ch09.** Preserved: the package uses no
   higher-derivative claim; the unboundedness statement concerns the two-derivative
   kinetic term only.
5. **eq:NC hermiticity (\(\Theta\) real).** Preserved: the package consumes it;
   the complex escape is excluded, listed only.
6. **Low-energy Lorentzian GR recovery passages (ch17/ch18).** Not touched: no
   passage relies on the transfer sign being derived rather than stipulated.

New obligations created by the payload: none beyond the record itself (no new
label is referenced that is not already defined: ass:dictionary, ass:lorentzian,
def:matrix-coords-ext, eq:NC, eq:Smatrix, eq:Smicro, eq:dictionary, eq:g-from-e,
app:status - all grepped unique in live bytes; verify_anchors_127.py).

Downstream stale-passage scan (from live greps, full-scan deferred to gatekeeper
per 3(c)): ch03 L199-204 (consistent; payload sentence sits in ass:dictionary and
cites app:status, already cited there); appH L1735 (consistent - generalized);
appH L2711-2744 (consistent - consumed); appH L4025 (consistent - its input gains
datum status via the new adjacent paragraph); review-124's avenue-(1) description
("unique transfer step") is superseded in substance by this package - it lives in
proposals/, needs no manuscript change; frontier edge N.dict-kinetic-sign moves
from OPEN to RESOLVED-NEGATIVE in the next frontier refresh (frontier is a
reports/ artifact, single-writer, not edited by this agent); ledger: one line to
be appended by the integrator/orchestrator on integration (not by this agent).

## Proposed changes (exact anchors, fenced latex blocks; what is kept; retirement list)

Two minimal insertions; nothing is deleted, no status label is touched, no
citation is added. Both payloads are ASCII; CRLF handling is the integrator's job;
anchors are unique in live bytes (verify_anchors_127.py, A1-A4).

**P1 - ch03-matrix-action.tex, Assumption ass:dictionary.** Anchor (unique, A1):
the sentence ending "...this is a matching condition, not an established result."
Insert immediately after that sentence, same paragraph:

```latex
Within the quadratic transfer class the requirement sharpens to a no-go: for real non-degenerate \(\Theta^{\mu\nu}\), every \(\eta\)- or \(g^{(0)}\)-contracted quadratic commutator transfer yields a kinetic tensor equal, up to a constant factor, an overall sign, and index placement, to \(K^{\mu\nu}=\Theta^{\alpha\mu}g^{(0)}_{\alpha\beta}\Theta^{\beta\nu}\) of Definition~\ref{def:matrix-coords-ext}, which is congruent to \(g^{(0)}_{\mu\nu}\) (hence Lorentzian) and nowhere proportional to \(g^{(0)\mu\nu}\); the energy of a kinetic term of this type is bounded below only for time directions within the cone of \(K\), so no normalization makes the transfer positive for the full \(g^{(0)}\)-time cone, and on these data the sign of the kinetic term is an independent datum of the dictionary rather than an open consequence of the transfer (Appendix~\ref{app:status}).
```

Kept verbatim: the whole preceding assumption including the matching-condition
sentence and the sentence keeping \(\LUV\) the cutoff. Retired: nothing (the clause remains; the
inserted sentence records its status). The alternative redaction (deleting
"including its sign in the signature \((-,+,+,+)\)" outright) is listed as option
(B) under the author decision and is NOT the recommended payload, because the
sign content survives as a datum that the sentence records.

**P2 - chapters/appH-microscopic-proofs.tex, Problem N section.** Anchor (unique,
A3): the paragraph head "\paragraph{The named completion class and the remainder
bound.}" (L4027). Insert the following paragraph immediately before it (after the
blank line that follows the matrix-quantum-mechanics paragraph of L4025):

```latex
\paragraph{Kinetic-sign content of Assumption~\ref{ass:dictionary}: a no-go for quadratic transfers on real data (not closure).}
Let \(\Theta^{\mu\nu}\) be real, antisymmetric and non-degenerate and let \(g^{(0)}_{\mu\nu}\) be a non-degenerate background of Lorentzian signature (Assumption~\ref{ass:lorentzian}). (i)~Tensor type: every transfer through the dictionary image \eqref{eq:dictionary} of a quadratic \(\eta\)- or \(g^{(0)}\)-contracted commutator term of Equation~\eqref{eq:Smatrix} whose indices are saturated only by \(g^{(0)}\) and its inverse, dagger or non-dagger and with no inserted background tensors, yields a kinetic tensor equal, up to a constant factor, an overall sign, and index placement, to \(K^{\mu\nu}=\Theta^{\alpha\mu}g^{(0)}_{\alpha\beta}\Theta^{\beta\nu}\) (plain and dagger contractions give the two overall signs; identities checked symbolically for generic \(\Theta\)). (ii)~Non-matching: \(K\) is congruent to \(g^{(0)}_{\mu\nu}\), hence Lorentzian of the same signature, and by the conjugate-coordinate theorems recorded above it is nowhere proportional to \(g^{(0)\mu\nu}\); a background trace insertion shifts the matching equation only by a multiple of \(g^{(0)\mu\nu}\) and creates no real solution; over the complex numbers the equation for \(g^{(0)}=\eta\) is solved exactly by the (anti-)self-dual class, which contradicts the hermiticity of \(\hat X^\mu\) in Equation~\eqref{eq:NC}. (iii)~Sign: the energy of a scalar kinetic term with tensor \(K\) is bounded below exactly for time directions inside the cone of \(K\); the cones of \(K\) and \(g^{(0)}_{\mu\nu}\) are distinct, so no normalization of the transfer is positive for the full \(g^{(0)}\)-time cone; for \(g^{(0)}=\eta\) the failure is strict, \((K^{-1})_{00}=|b|^2/\mathrm{pf}(\Theta)^2>0\) with \(E_i=\Theta_{0i}\), \(b_i=\tfrac12\epsilon_{ijk}\Theta^{jk}\) and \(\mathrm{pf}(\Theta)=E^ib_i\) (checked symbolically for generic \(\Theta\)), so the \(g^{(0)}\)-time direction is strictly spacelike for \(K\) for every real non-degenerate \(\Theta\), and purely spatial \(\Theta\) is the recorded degenerate case. Consequences: the kinetic-sign input of the sublemma hypotheses recorded above is not derivable within this transfer class on real data and is a datum, free in sign for every class member; none of this derives the datum, Problems~A and~N remain open, the Presentation-B realization above consumes no transfer and is unaffected, and no status label changes. Escapes outside the class, with costs: complex self-dual \(\Theta\) (contradicts Equation~\eqref{eq:NC} and the hermiticity of Definition~\ref{def:matrix-coords-ext}); taking the cone of \(K\) as the kinetic structure of Equation~\eqref{eq:Smicro} (overturns Equation~\eqref{eq:g-from-e} and the recorded Problem-D and Problem-F consumption); transfers with inserted background tensors (outside the quadratic class, none fixed in the book); a bare background insertion of the \(g^{(0)\mu\nu}\)-kinetic term (a re-datuming whose sign content is a stated constant).
```

Splice hygiene: each payload block, when spliced with its anchor, adds only the
block bytes; both blocks end before an existing blank line; no new labels are
defined; the only cross-references are grepped-existing labels listed above; no
build run was performed by this agent per dispatch (no compile certificate is
shipped; the gatekeeper must require one from the integrator per the payload
compile-certificate rule).

## Verification scripts (paths and what each checked)

- `proposals/127-n-dict-kinetic-sign/verify_dict_sign_127.py` (run:
  `python -I verify_dict_sign_127.py` from the folder): 30 checks, all PASS.
  S0 sanity (antisymmetry, symmetry of K, control fires); S1 congruence/determinant
  identities, one-line non-proportionality chain, exact aligned-form solution sets
  (real: none; complex: q = +/- i p), 200-point sampling control; S2 exact
  spacelike-lemma identities incl. (K^-1)_00 = |b|^2/pf^2, canonical instance,
  degenerate-case controls, 100-point sampling; S3 trace-insertion reduction to
  proportionality with positive control; S4 positivity-cone criterion with
  proportional positive and negative controls; S5 plain/dagger contraction signs,
  non-K control. Every guard has an injected positive control proving it fires;
  symbolic claims are generic-Theta identities (sampling appears only as controls).
  Capture: `capture-verify-r1.txt`.
- `proposals/127-n-dict-kinetic-sign/verify_anchors_127.py`: 7 checks, all PASS:
  uniqueness of both payload anchors and of the two sentences quoted from them,
  absent-string control, multiplicity control (Problem~N > 1), CRLF presence in
  both target files. Capture: `capture-anchors-r1.txt`.
- `core-aspect-register.md`: register artifact (live label grep + full reads).
- `payload-P1.txt`, `payload-P2.txt`: byte-exact payload blocks extracted from the
  fenced blocks above (each appears verbatim in this file exactly once): P1 one
  source line, 871 bytes; P2 two source lines, 3043 bytes; both ASCII, no CR,
  spliced as ONE new source line (P1) or TWO new source lines (P2) inserted after
  the anchor line, so POST = PRE + 1 (resp. + 2) lines and the inserted region
  grows by exactly the payload bytes after the integrator's CRLF conversion.
- Symbolic output is a check of the stated identities, not a proof of the prose
  lemmas; the hand proofs (Sylvester congruence, A-argument, determinant lemma,
  cone maximality) are in the Research section and are what the checks illustrate.

## Decisions Taken (routine choices only)

- Transfer class declared as: two dictionary factors, all indices saturated by
  g^(0) or inverse, dagger/non-dagger, no inserted background tensors, p^2 part
  only. Chosen because it is exactly what the dictionary clause consumes and what
  the recorded 120 lift uses; C-insertions and four-factor transfers are declared
  outside and listed as escapes.
- Identity embedding g^(0) = eta used for the strict flat-frame lemma (S2); the
  covariant payload statements use only congruence, the recorded general
  non-proportionality theorem, and the cone criterion.
- The appH record paragraph is placed before the completion-class paragraph so it
  sits adjacent to the 124 paragraph whose input list it refines.
- Payload wording avoids "no-go" inside the assumption environment itself (the
  sentence says "sharpens to a no-go", one sentence, scoped to the class).

## Milestone assessment

Trigger 2 (new no-go ruling out a class of routes the manuscript currently keeps
open - the transfer reading of the ass:dictionary sign clause / frontier edge
N.dict-kinetic-sign) AND trigger 5 (structural change proposed to a core
assumption clause; author decision among alternatives required). M5-class stop
applies: the loop should stop for the author on this package's verdict, since the
decision (which of options A-E) gates whether the manuscript text changes.

## Status-label recommendation (expected: none; report only)

None. Problem N, Problem A and Assumption ass:dictionary stay exactly as the live
bytes record them. If the author integrates the payloads, no ledger status word
changes; the frontier edge N.dict-kinetic-sign is a frontier artifact whose
refresh (OPEN -> RESOLVED-NEGATIVE, pointer to the new appH paragraph) belongs to
the single reports/ writer, not to any agent editing chapters/.

## Author decision needed

**The structural decision (never taken by this agent): how the ass:dictionary
sign clause should stand after the transfer reading is proved unsatisfiable on
core data.** Options:

- (A) Integrate both payloads P1+P2 as written: clause kept, datum status and
  no-go recorded in ch03 and appH. **Recommended**: smallest text that keeps the
  manuscript honest; every downstream use stays valid; the recorded non-
  proportionality theorems already commit the book to this reading, so the
  payload only makes explicit what ch03 L199-204 and the F-section already state.
- (B) Integrate P2 only (appH ledger record; ch03 assumption untouched).
  Acceptable minimum if the author prefers assumption text frozen.
- (C) Redact "including its sign in the signature (-,+,+,+)" from the clause and
  add P2. Honest but strictly larger change to an assumption environment; the
  datum would then live only in appH.
- (D) No manuscript change; record the no-go in frontier/ledger notes only.
  Not recommended: it leaves the manuscript implying the sign is still an open
  matching outcome while appH theorems already exclude that outcome on core data.
- (E) Reject the package and keep the clause as an open matching condition. This
  is a live choice for the author but conflicts with the recorded theorems, and
  the gatekeeper should test that reading.

Recommendation: (A).

## Remaining open step (what the original target still requires)

Under the old core (unchanged): Problem N still requires control of the effective
expansion / absence of an Ostrogradsky ghost for p < LUV beyond the named
truncation class; Problem A still requires the dictionary itself; both stay OPEN.
For the retired target specifically: deriving the kinetic-sign direction (or the
dictionary equivalence it was meant to serve) requires one of the four escapes
listed (each with stated costs) or a new core input; none is derivable from the
current core, which is exactly what this package establishes.

## Special instructions for the gatekeeper (3(c) full scan required)

- **Rule 3(c) is triggered: a full scan of every current chapters/**/*.tex file is
  mandatory for the verdict on this package** (an assumption clause is amended by
  P1 and a new ledger paragraph is added by P2). Report must state the scan was
  done on current bytes.
- Re-derive, at minimum: the A-argument (Step 2), the determinant-lemma identity
  det K_sp = -|b|^2 pf^2 and (K^-1)_00 = |b|^2/pf^2 (S2a-S2c), the two-contraction
  sign table (S5), and the cone-criterion claim (Step 3), each in full, plus re-run
  both scripts with python -I and compare captures.
- Check the payload labels exist and are unique in the live tree; check no label is
  defined by the payloads; check the hard invariant (nothing proposed makes
  spacetime or the K-cone fundamental - the excluded escapes are reported, not
  offered); check rule 3 (no closure by scope: the package negates a sub-target and
  relabels an input as datum; N and A remain open and so is the dictionary itself);
  check the hypothesis class is stated tightly (C-insertions, four-factor and
  higher-transfer members are out of scope and named).
- Must NOT be asserted in any downstream summary: closure of N, A or ass:dictionary;
  that the datum has been derived; that curved-background strict-spacelike
  statements beyond the flat adapted frame are proved here; that the two-contraction
  enumeration covers classes outside the declared transfer class; that any review
  of this package verified the full manuscript (only the 3(c) scan does).
- Integrator note: compile certificate (spliced-file pdflatex) required before
  ACCEPT-of-integration per the payload-compile rule; this agent ran no build.
