VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2

Gatekeeper r1 review, remote/claude, 2026-11-22. Saved here by the orchestrator. The gatekeeper's independent Q code is gk_gkQ_r1.py.

Source reading: digest + targeted reads (appH L715-760, L1505-1649; ch17 D1; adversary F3). Full scan owed: 3(c), because Edit 2 changes a scope passage.

## Verified
- Q = Q|_{w=0} - chi k^a F_ab, re-derived by hand: the last two w-terms cancel for N, N' and B.
- Ground-mode eigenvalue, checked with independent Q code: zeta and x drop out, and the roots follow the formula.
- Root formula and growth bounds, re-derived by hand (l>=1, l=-1, no real root at p>0; chi=0 reduces to kappa/2, matching 068).
- s3 exactness logic (J conservation, Cauchy-Binet). The exact parts and the numerical parts are identified.
- Gauge kernel = gauge directions (numerical).
- All scripts are identical on re-run, including s3 (full, about 7 min).
- apply_and_build: pre b98a3a34, post ae6c95cd; 416 pp, clean.
- Edit 2 is accurate. The survey statement is marked numerical. Placement OK.
- Derivation-first: it redirects D1 (null leg => no gap structurally; points to non-null-leg connections). Consequential enough to integrate. No trimming required beyond the optional F8.

## Findings
- F1 MAJOR: the root display has no exact/numerical qualifier. Fix: S1.
- F2 MAJOR: the "no gap" sentence hides the p->0 imaginary root q0 = -i c chi, a rate. "No sign of a mass" is ambiguous. Fix: S2, S3.
- F3-F7 minor: "maximal minors" -> "minors of the generic rank"; the l<=5 claim rests on the observed pattern; entries are rationally reconstructed; zeta,x is a single sample; "rate" -> |Im q0|.
- F8 optional: the closing sentence duplicates 071's closer.

## Snippets
S1. Insert after the display, before "For \(l\ge3\)":
"This is exact in the blocks described below and numerical, at sampled points, for \(l\le9\) otherwise; higher levels are not checked."
In the same paragraph:
- "of the maximal minors" -> "of the minors of the generic rank"
- "which contain all factors with \(l\le5\)," -> "which on the observed pattern of levels contain all factors with \(l\le5\),"
- "(exact in rational arithmetic)" -> "(exact in rational arithmetic after rational reconstruction of the double-precision entries)"
- "At \(\chi=0\) this gives the levels \(q_0^2=p^2+\kappa p\,l\) of the paragraph on left-invariant backgrounds with torsion for every \(\zeta,x\) (numerical)." -> "At \(\chi=0\) and a sampled \((\zeta,x)\neq(0,0)\) the levels \(q_0^2=p^2+\kappa p\,l\) of the paragraph on left-invariant backgrounds with torsion are recovered (numerical)."

S2. Replace "No gauge-invariant gap or mass therefore appears for the Lorentz or torsion modes at this order, although the background carries the scale \(\kappa\) and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4\chi^2\kappa^2\neq0\), and no sign of a mass arises." with:
"No term independent of the momentum enters, so no gauge-invariant gap or mass appears for the Lorentz or torsion modes at this order, although the background carries the scale \(\kappa\) and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4\chi^2\kappa^2\neq0\); \(\chi\) enters the roots only as a rate, since as \(p\to0\) they tend to \(q_0=0\) and to the imaginary \(q_0=-\mathrm ic\chi\)."

S3.
- "with supremum \(|c\chi|\) as \(p\to\infty\);" -> "with supremum \(|c\chi|\), approached as \(p\to0\) and as \(p\to\infty\);"
- "its largest rate rises from" -> "its largest \(|\operatorname{Im}q_0|\) rises from"
- "Over all modes the largest rate is" -> "Over all modes the largest \(|\operatorname{Im}q_0|\) is"

F8 (optional) closer: "Nothing here shows that the matrix integral selects this class or these backgrounds, so the assumptions listed in the preceding paragraph are not discharged; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL."

## Scope
- Exact: the Q identity; the ground mode; the growth bounds given the root formula; no real root at p>0; the J-block roots at zeta=x=0.
- Bounded no-gap result on the null-leg constant-connection class (tree level, linear order, no norm).
- No label change. D, F and N stay OPEN.

Avenues, ranked:
1. Non-null-leg connections (s4).
2. A pairing or Krein form.
3. One loop.
4. Nonlinear.
5. Non-constant connections.
6. Other null-leg families (last).

## Disposition
r2 with S1-S3 (plus F8 optional), then the full scan, then plain ACCEPT.
