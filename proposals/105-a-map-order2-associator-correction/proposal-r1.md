# Proposal 105-a-map-order2-associator-correction, round 1

Date 2026-11-20. Branch local/gpu. Problem A, order-Theta^2 associator of the naive
variable-coefficient truncation as a Hochschild coboundary.

## Result

On the exact polynomial model (test polynomials of total degree <= 2, coefficient 1-jet
pointwise model, bidifferentials of order <= 2 per slot), the order-Theta^2 associator A2 of
the naive truncation f *_1 g = fg + (i/2)Theta^{ab}(x) d_a f d_b g satisfies a sharp
dichotomy: A2 = delta(B2) for a bidifferential B2 with arbitrary pointwise coefficients at a
fixed 1-jet (Theta(0), dTheta(0)) IF AND ONLY IF the Schouten bracket [Theta,Theta](0) = 0
(C3/C5/C7: for generic 1-jets A2 is not a coboundary, and the obstruction functionals span
exactly the Schouten 3-form space; along the 21-parameter closure family the system is
solvable at every closed jet). The slot-antisymmetric part of A2 equals
+1 * [Theta,Theta]^{abc} d_a f d_b g d_c h with kappa = +1 exactly (C1b), CONFIRMING the
coefficient in the integrated 058 paragraph. For constant Theta the Moyal graph
B2 = -1/8 Theta^{ab}Theta^{cd} d_a d_c f d_b d_d g satisfies A2 = delta(B2) identically
(C8 symbolic, C9 numeric). Closure alone does not make the naive truncation associative:
closed jets with Theta(0) != 0 have nonzero A2 (244/544 rows, C7). Bounded no-go (C6): no
jet-universal B2 exists in the enumerated five-structure natural class
{P1, M, div1, U1, U2}; the completed Kontsevich natural class was NOT tested and the
natural-universal question stays OPEN. This package derives NO critical-path step: Problem A
remains OPEN; nothing here derives Assumption ass:dictionary or the half-sided inclusion.

## Target and status

Problem A (chapters/appH-microscopic-proofs.tex, sec:status-A, lines 13-20, read this round):
"Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label.
Completion: PROGRAMME-CONDITIONAL. The general matrix-to-modular map remains unproved. A
scope-limited Presentation-B model may retain Assumption~\ref{ass:dictionary} and claims no
derivation from the matrix model." Dependencies: the matrix-to-modular map target; the
continuum/star-product presentation feeds the derivation chain of the dictionary assumption.
Verdict: this package is a PROGRAMME-CONDITIONAL consistency/sharpness result around the
star-product truncation; DERIVED = nothing on the critical path. No status label is changed.

## Source reading

digest + targeted reads. Digest status: current (scratch/digest.md, tree b9b4260315c2).
Live chapters/appH-microscopic-proofs.tex: 805839 B, sha256/16 21163962e4f7f514, 3870 CRLF.
The dispatch quoted sha prefix e37ca538 is stale; live/digest value used (discrepancy
flagged). Targeted reads this round: full sec:status-A block incl. the integrated 058
paragraph and the "Missing step." paragraph; macro inventory (counts: \Theta 333,
\partial 323, \delta 275, \tfrac 643, \star 8, \le 61, \neq 80, \equiv 5, \paragraph 140);
Problem A ledger lines 15-20. No unreadable files. Full scan not triggered (no
definition/assumption/scope/status edit).

## Research and reasoning

1. s1 audit (s1_naive_associator.py kept unmodified as provenance). Its claim (a) used a
   component-ratio probe, invalid because A2 is not slot-antisymmetric, and its
   "antisymmetric-tensor identity PASS" was vacuous (skipped loop). Its claim (b) examples
   both had Theta(0) = 0, and A2 depends only on the 1-jet (C1a), so A2 was identically
   zero - vacuous. Its claim (c), the constant-Theta Moyal order-2 check, is genuine and is
   reproduced independently here (C8/C9). The correct probe - slot-antisymmetrization -
   gives kappa = +1 exactly (C1b): the integrated 058 kappa sentence needs no correction.
2. Model. Normal-ordered jets MON(e) = x^e/e!, 15-jet basis, 544 test triples (all slot
   orders >= 1, total <= 4), 196 B2 coefficient unknowns; Hochschild coboundary
   delta C(f,g,h) = f C(g,h) - C(fg,h) + C(f,gh) - C(f,g) h gives the 544x196 matrix M2r,
   rank 160 at generic jets, dim ker M2r^T = 384. Schouten bracket per the 058 convention
   [Theta,Theta]^{pqr} = Theta^{pd} d_d Theta^{qr} + cyc. All central ranks/exactness over
   QQ; numeric cross-checks seeds 105, 1051, 20261120.
3. Sign convention derived, not assumed: with f*g = fg + hbar c1 + hbar^2 c2, the hbar^2
   term of (f*g)*h - f*(g*h) is A2 - delta(c2); the correction equation is A2 = delta(c2)
   (hand check (x0, x0, x1^2/2): A2 = +1/4 Theta_01^2 = delta c2 with c2 = -1/8 P1).
   Earlier draft scripts used the opposite sign; corrected and re-verified (C8/C9).
4. Dichotomy: C2/C7 (nonclosed: no solution), C3 (witness span = Schouten 3-forms, dim 4,
   exact over QQ), C5 (parametric solvability along the closure family, symbolic rank stays
   160), C7 (closed jet with Theta(0) != 0: A2 nonzero in 244/544 rows yet removable).
   delta(A2) = 0 identically (C4, 80 generating quadruples) - A2 is always a 2-cocycle.
5. Relation to the integrated 058 paragraph. The sentence "Schouten-closure alone does not
   remove the full order-Theta^2 associator of the naive truncation" remains TRUE under the
   reading "closure alone does not make the naive truncation associative" (confirmed, C7),
   but is misleading under a reading "the associator is not coboundary-removable under
   closure" (it is, pointwise and along the closure family). Recorded as a possible M3
   prior-claim clarification for the gatekeeper; NO appH edit of that paragraph is made here.
6. Literature: an attempt to cross-check the explicit Kontsevich U_2 / DeWilde-Lecomte
   hbar^2 star-product formula was made (web search empty; fetched arXiv record
   math/0101039 unrelated). The explicit formula is NOT independently verified and was NOT
   used anywhere in this package. No new citations are proposed.

## Claim classification

- C1a  established (exact symbolic): A2 factors through the 1-jet; vanishes on constant args.
- C1b  established: kappa = +1 exactly vs the 058 Schouten convention.
- C2   established (exact rational rank): generic jets, A2 not in im delta (160 -> 161).
- C3   established: obstruction functionals span exactly the Schouten 3-forms (dim 4);
       pointwise wild-B2 existence iff Schouten-closed.
- C4   established: delta(A2) = 0 identically.
- C5   established (symbolic parametric rank): solvable at every closed jet of the family.
- C6   conditional/bounded no-go, class explicit: five-structure natural ansatz only; NOT
       the full Kontsevich natural class (omits (dTheta)^2, Theta d^3 Theta, (d^2Theta)^2;
       the Theta d^2Theta contraction vanishing is verified). Natural-universal existence:
       unresolved.
- C7   established: nonclosed membership False; closed nontrivial example membership True;
       s1 examples A2 identically 0.
- C8   established (exact, constant Theta): delta(B2M) - A2 = 0 identically in TA, 544 rows.
- C9   established (numeric cross-check of C8, seed 20261120).
- Sign convention A2 = delta(c2): established (expansion + hand check).
- 058 sentence clarification (section 5, item 5): analysis of an integrated claim; the
  clarification itself is a reading, offered, not integrated.
- Kontsevich U_2 literature formula: not independently verified; not used.

## Proposed changes

File: chapters/appH-microscopic-proofs.tex, sec:status-A, ONE paragraph inserted.

Anchor (PIN, verified count 1 in the live bytes, programmatic build shown in
simulate_apply_105.py): the end of the 058 paragraph

    they do not derive Assumption~\ref{ass:dictionary}.

followed by a blank CRLF line and then

    \paragraph{Missing step.}

The new paragraph goes between them, after the 058 paragraph and before
"\paragraph{Missing step.}". All existing sentences and equations are KEPT; no other passage
is touched. The single inserted line is proposals/105-a-map-order2-associator-correction/
insert-r1.tex (1849 B, one CRLF-terminated ASCII line, sha256/8 7c6fd752):

```latex
\paragraph{Order-\(\Theta^2\) coboundary dichotomy.} For the naive truncation \(f\star_1 g=fg+\tfrac{i}{2}\Theta^{ab}(x)\,\partial_af\,\partial_bg\), the order-\(\Theta^2\) associator \(A_2(f,g,h)=B_1(B_1(f,g),h)-B_1(f,B_1(g,h))\) depends on \(\Theta\) only through its 1-jet at the origin, vanishes when any argument is constant, satisfies \(\delta A_2\equiv0\), and its slot-antisymmetric part equals exactly \([\Theta,\Theta]^{abc}\,\partial_af\,\partial_bg\,\partial_ch\). At a fixed 1-jet, the equation \(A_2=\delta B_2\) admits a bidifferential \(B_2\) of order \(\le2\) per slot with arbitrary pointwise coefficients if and only if \([\Theta,\Theta](0)=0\): for generic 1-jets no such \(B_2\) exists and the obstruction functionals span exactly the Schouten 3-forms, while along the closure family the system is solvable at every closed jet. For constant \(\Theta\), the correction \(B_2(f,g)=-\tfrac{1}{8}\Theta^{ab}\Theta^{cd}\,\partial_a\partial_c f\,\partial_b\partial_d g\) satisfies \(A_2=\delta B_2\) identically. Closure alone does not make the naive truncation associative: at closed jets with \(\Theta(0)\neq0\) the associator is still nonzero, and removability requires adding a correction operator. In the five-structure natural ansatz built from contractions of the products \(\Theta\Theta\) and \(\Theta\partial\Theta\) of order \(\le2\) per slot, no jet-universal \(B_2\) solves \(A_2=\delta B_2\) at closed jets, so the natural-universal question remains open. These are exact algebraic facts for polynomial test functions of degree \(\le2\) at the 1-jet level; they do not address orders \(\Theta^3\) and higher, operator-norm estimates, or convergence, do not select a correction from the matrix theory, and this paragraph does not derive the dictionary assumption or the half-sided inclusion and does not close Problem~A.
```

Macros used: \Theta, \delta, \equiv, \le, \neq, \paragraph, \partial, \star, \tfrac - all
confirmed to occur in appH (hygiene_105.out). No \label/\ref/\eqref/\cite, no hard-coded
chapter numbers, braces balanced (9/9), one scoped status sentence.

Expected POST after byte surgery (from simulate_apply_105.out): size 807690,
sha256/16 f54e215622bc4116, CRLF 3872.

Stale passages elsewhere: none edited. The 058 sentence discussed above is left untouched;
if the gatekeeper accepts the clarification as an M3 prior-claim correction, that is a
separate future package.

## Verification scripts

All in proposals/105-a-map-order2-associator-correction/ (run from repo root with -I):

1. s1b_order2_coboundary.py (+ .out): the central verification. Reproduction:
   `python -I proposals/105-a-map-order2-associator-correction/s1b_order2_coboundary.py`
   (~72 s). Expected invariants: "rank = 160 (196 cols, 544 rows)"; generic-jet augmented
   rank 161; "witness dim" 4; closure Schouten map rank 4, nullspace dim 20 at both test
   jets; C5 rank 160 -> 160; C6 rank(C) = 3, rank(aug) = 4 at all four closed points;
   "nonclosed membership=False"; closed example "A2 nonzero rows=244, membership=True";
   "kappa ... = 1"; all of C1a,C1b,C2,C3,C4,C5,C6,C7,C8,C9 PASS; exit 0.
2. s1_naive_associator.py (+ .out): original provenance run, UNMODIFIED; kept for audit.
3. hygiene_105.py (+ .out): insert-line hygiene vs live appH. Expected "HYGIENE: PASS",
   macro list as above, "appH size 805839 sha256/8 21163962 CRLF 3870 PIN count 1", exit 0.
4. simulate_apply_105.py (+ .out): byte-surgery simulation pinned to live appH bytes;
   writes only to scratch\sim\appH_after_105.tex. Expected: BEFORE 805839 / 21163962e4f7f514
   / 3870; AFTER(simulated) 807690 / f54e215622bc4116 / 3872; "live appH untouched:
   sha256/16 21163962e4f7f514"; exit 0.
5. mk_artifacts.py: regenerates findings.md and insert-r1.tex byte-identically (asserts).
6. manifest_105.py (+ manifest.md): folder file sizes and sha256/8 + live appH line.

## Decisions Taken

- C6 reworked from a "failed claim" into a PASS of an explicitly bounded non-existence, and
  the completed-class retest was deferred as ranked avenue 1, per the derivation-first
  directive (positive-aimed avenues listed in findings.md section 5; C6's expected outcome
  was the same no-go in the same class).
- Sign convention A2 = delta(c2) derived from the associativity expansion (plus hand check)
  instead of trusted from earlier drafts; C8/C9 re-verified under the corrected sign.
- C9 decoupled from C6 semantics to a pure constant-Theta Moyal cross-check of C8.
- Fixed two bugs in my own verification scripts found by running them (inverted stray-CR
  check in hygiene_105.py; dropped app-suffix in the simulate splice). Manuscript untouched.
- Rejected: editing the 058 sentence (offered as clarification only); rejected: any wording
  suggesting closure of Problem A or the dichotomy removes the missing step.

## Milestone assessment

Routine. No milestone trigger claimed. Flag for the gatekeeper: possible M3 prior-claim
clarification on the integrated 058 sentence (see Research, item 5).

## Status-label recommendation

Current critical path re-derived from ch17-agenda/appH ledger: A, B, C, D1, E, F, G-derived,
N. Affected labels: NONE. Problem A stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed

none

## Remaining open step

To move Problem A toward its original target one would still need: (i) orders Theta^3 and
higher - whether a corrected product can be made associative to all orders (jet-universal
B2 in the completed Kontsevich natural class, and the wild jet-universal solvability test);
(ii) operator-norm/convergence estimates for any corrected product; (iii) selection of the
correction (which B2) by the matrix theory itself - the genuinely missing input; (iv) the
full matrix-to-modular map. The pointwise dichotomy here does not touch (i)-(iv).

## Special instructions for the gatekeeper

- Re-run scripts 1, 3, 4 before re-deriving; reproduce the sign convention independently
  (the sign is the one point where an earlier draft was wrong).
- MUST NOT be asserted: closure of Problem A; derivation of Assumption ass:dictionary or
  the half-sided inclusion; that C6 covers the full Kontsevich natural class; that the
  literature U_2 formula was verified (it was not, and was not used).
- C6 is bounded to the five enumerated structures with universal jet-independent
  coefficients; the .out shows rank 3 vs 4.
- Anchor re-verification is mandatory at integration time (PIN built programmatically in
  simulate_apply_105.py; live appH 805839 B / 21163962e4f7f514 / 3870 CRLF at this round).
