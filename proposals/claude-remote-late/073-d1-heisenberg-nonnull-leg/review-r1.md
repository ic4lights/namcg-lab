VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/1

Gatekeeper r1 review, remote/claude, 2026-11-22. Saved by the orchestrator. The gatekeeper's checks are in gk_op_r1.py and gk_cut_r1.py.

## Source reading
Digest plus targeted reads: appH L715-764, L1513-1533, L1609-1661; ch03 eq:Smatrix; ch17 D; adversary F3. A full scan under 3(c) is still owed (Edit 2).

## Verified
- All scripts were re-run in full and reproduce their outputs. make_insert is byte-identical. apply_and_build: pre c8c07938, post 69ab958a, 418 pp, clean.
- Independent operator-level check with the literal L1519 fields and omega = -w, at tilted, untilted and 072-limit points: residual {0}. Negative control with tau != 0 at s != 0 fails, as it should.
- Checked by hand:
  - basis reduction and the 072 limit;
  - the constraint, which forces 3 vartheta^2 >= 5 chi^2 and hence R^2 > 0 on tilted members with c != 0;
  - leg operator L^2 = 0, nilpotent; the tensor leg form is nonzero;
  - the Q identity, which holds on the whole ansatz (W_[xyz] = 0);
  - the root-formula algebra and its 072 limit.
- Q2: NOT a PRIOR-CLAIM-ERROR. The 072 text says only that the tensor form is nonzero, which stays true. Edit 2 is accurate.
- Placement is OK. The closer carries the emergent-metric non-identification.
- Q8: the mu^2 term is not in eq:Smatrix. Adopting it would be STRUCTURAL (fundamentality agent). It may be studied as a scoped hypothesis class. C_munulambda != 0 is a within-core relaxation and is ranked first.
- Q9: worth integrating. It settles the 072 rank-1 avenue and redirects further work away from more constant-connection Heisenberg families.

## Findings
- F1 MAJOR: the gap-decision argument is convention-laden and incomplete (non-real Lambda not covered; the root formula is numerical). Fix with S1.
- F2 minor: the multiplicities are verified only at s=0, l<=5. Fix with S2.
- F3 minor, proposal text only: the S7(e) column-cut counts are wrong. Correct values: T1 has 109 roots (108 + 1 unassigned); T2 has 115 (108+1 assigned, 6 unassigned). Either add an N-dependence test or state that the cut is not valid at s != 0.
- F4 minor: "positive for |vartheta|>|chi|" -> "positive for \(c\neq0\) and \(|\vartheta|>|\chi|\)".
- F5 minor: "so" presents O1 as derived. Fix with S3.
- F6 minor: define \(\delta_0^a=(1,0,0,0)\). Optionally rename the tilt to (sin phi, cos phi), because c collides with an index and with the class label, and Lambda collides with the gauge parameter.

## Snippets
S1: replace from "This term is not a mass:" through "on this family at this order." with:
"This term does not give a gap. It is the term \(-\Lambda^2k_\parallel^2\) of the square \((q_\parallel+\Lambda k_\parallel)^2\), fixed by the coefficient \(\Lambda\) of the first-order term \(2\Lambda(q_0-cp)\), and it vanishes with \(s\). Given the displayed equation, as \(p\to0\) the roots of a class tend to \(q_0=-\Lambda(1\mp c)\), which are not real when \(\Lambda\) is not real; for real \(\Lambda\neq0\), as at \(\chi=0\), these two limits have the same sign, unlike the pair \(\pm m\) of a mass, and for each \(l\) one of the two roots vanishes at the unique \(p>0\) with \(p^2+(2c\Lambda+\kappa l)p=s^2\Lambda^2\) (by hand from the displayed equation). So no gauge-invariant gap or mass appears for the Lorentz or torsion modes on this family at this order."
Keep "No norm is used, so no statement on stability is made."

S2: after "and half of these at \(l=\pm1\)" insert "(at \(s=0\) and \(l\le5\); at \(s=\tfrac35\) only the presence of the predicted roots with \(l\le3\) is checked)".

S3: replace "At \(s\neq0\) the null leg has a component along \(E_1\), on which the Landau sectors act by oscillators, and \(k_\parallel^2=-s^2\), so the characteristic equation contains" with "At \(s\neq0\) the null leg has a component along \(E_1\), on which the Landau sectors act by oscillators, \(k_\parallel^2=-s^2\), and the characteristic equation found above contains".

## Scope
- Exact: the family; Q identity; L^2 = 0; operator-level validity; U1 divisors.
- Numerical: the Lambda fit, the multiplicities, the tilted roots.
- Bounded no-gap result. No label change; D, F, N OPEN.
- Avenues:
  1. C != 0 (within core)
  2. one loop on the tilted family
  3. pairing/Krein
  4. non-constant connections / other algebras
  5. mu^2 (structural if adopted)
  6. nonlinear
  7. analytic root formula (O1)

## Disposition
r2: S1-S3, F4, F6, plus the F3 proposal fix and new hashes. Then the full scan, then the final verdict.
