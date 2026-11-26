# Core-aspect register (working artifact, 127; live bytes 2026-11-25)

Derived from live sources (appH sha1 123108d4a947, 4144 lines; ch17 23bd98d96532;
ch03/ch04/ch09 read as listed in proposal-r1.md Source reading). Scope: aspects the
127 package touches or consumes; NOT a full-manuscript register (that is the 3(c)
scan's product). Columns: locus | states | dependents (label-ref file counts from
live grep) | effect of package | emergence class.

1. ass:dictionary (ch03-matrix-action.tex L345-363; 7 using files)
   [X_mu,Phi] <-> i Theta D Phi + "quadratic commutator term of eq:Smatrix is
   required to generate the kinetic term of eq:Smicro, including its sign in
   (-,+,+,+); matching condition, not an established result."
   Dependents: Problem A; appH N input list (L4025); ch05 conversion discussion;
   review-124 avenue (1). Effect: sign clause proved unsatisfiable as transfer on
   real data; recorded as datum (P1 sentence). Emergence-preserving.
2. def:matrix-coords-ext (ch03 L172-205; incl. K = theta g theta at L192 and the
   recorded non-identification at L199-204 citing app:status). Dependents: ch03;
   appH L1735 (120 lift), appH F theorems L2711-2744. Effect: extended (K always
   Lorentzian; g0-time strictly K-spacelike, flat frame). Nothing breaks.
3. Conjugate-coordinate theorems (appH L2711-2744): G = K^-1 not proportional to g,
   pointwise, any real Lorentzian leaf metric, D >= 4; K != c eta^-1. Consumed,
   not changed. Supplies covariant non-matching for P1/P2 wording.
4. 120 lift paragraph (appH L1735): recorded shift-symmetric lift is K-type;
   "K = c g admits no real solution with Theta != 0"; purely spatial Theta makes K
   degenerate (no time-derivative term). Generalized to the full class tensor type.
5. 124 realization paragraph (appH L4025): Presentation-B MQM class realizes the
   N sublemma hypotheses; pins three inputs, first = ass:dictionary kinetic-sign
   content. Untouched; its first input gains proved datum status (new adjacent
   paragraph P2).
6. eq:NC hermiticity (ch03 L120-140): Theta real. Consumed. Complex self-dual
   escape excluded by it (escape listed only). Emergence-critical.
7. ass:lorentzian (ch04 L300-334; 7 using files) + ass:nondeg (ch04; 6 files):
   g0 Lorentzian nondegenerate background. Consumed; preserved by derivation.
8. eq:Smicro (ch03 L220-228; 6 files) and its sign note (L233-237): target kinetic
   convention. Kept verbatim; never re-identified with the K-cone (escape (b)
   reported with cost, not proposed).
9. eq:g-from-e / def:composite-metric (ch04 L140-199; 4 files): emergent metric.
   Untouched. Hard invariant (spacetime emergent) preserved: package adds no
   fundamental structure; both payload sentences state non-identities.
10. thm:ostro + ass:EFT-a2 (ch09 L93-151): ghost veto used at second-derivative
    order only; package's unboundedness claim is two-derivative, consistent.

Stale/undocumented flags from this pass: (a) frontier edge N.dict-kinetic-sign
wording ("nothing pins down the kinetic-sign direction") should become
RESOLVED-NEGATIVE with pointer to the new appH paragraph upon integration
(reports/ writer's edit, not chapters/); (b) review-124's "unique transfer step"
superseded in substance (proposals/ artifact; no manuscript change); (c) no other
passage asserts the transfer sign is derivable or fixed (grep "kinetic-sign":
single appH hit L4025; grep "including its sign": single ch03 hit L360).
