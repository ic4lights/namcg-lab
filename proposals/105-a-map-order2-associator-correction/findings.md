# Findings - proposal 105, Problem A order-Theta^2 associator as a Hochschild coboundary

Date 2026-11-20. Branch local/gpu. Live chapters/appH-microscopic-proofs.tex: 805839 B,
sha256/16 21163962e4f7..., 3870 CRLF (matches scratch/digest.md, tree b9b4260315c2; the
dispatch's quoted sha prefix e37ca538 is stale - live/digest used).

## 0. Question and provenance

The s1 script (s1_naive_associator.py, kept unmodified as provenance) made three failed
header claims about the naive order-Theta truncation
f *_1 g = fg + (i/2)Theta^{ab}(x) d_a f d_b g and its order-Theta^2 associator
A2(f,g,h) = B1(B1(f,g),h) - B1(f,B1(g,h)). This package (a) audits s1's claims, (b) settles
the decisive question - is A2 a Hochschild coboundary delta(B2) of an explicit bidifferential
in Theta, dTheta under Schouten closure - on the polynomial 2-jet model, symbolically, and
(c) records a bounded non-existence for a jet-universal natural ansatz. All results come from
s1b_order2_coboundary.py (reproduce: python -I
proposals/105-a-map-order2-associator-correction/s1b_order2_coboundary.py, ~72 s, exit 0).

## 1. s1 audit

- s1 claim (a) (associator/Schouten mismatch): the probe was wrong. s1 tested
  component-ratio equality, meaningless because A2 is not slot-antisymmetric; its "full
  antisymmetric-tensor identity PASS" was vacuous (loop skipped when the ratio was None).
  The correct probe - slot-antisymmetrization of the trilinear symbol - gives (C1b)
  antisym(A2) = +1 * [Theta,Theta]^{abc} d_a f d_b g d_c h EXACTLY (symbolic, generic
  jets). This CONFIRMS the coefficient in the integrated 058 paragraph (appH: the
  antisymmetrized order-Theta^2 associator equals [Theta,Theta]^{abc} d_a f d_b g d_c h).
  No correction to that sentence is needed.
- s1 claim (b) (closed Theta examples showing irreducibility): both examples had
  Theta(0)=0, and A2 depends only on the 1-jet (Theta(0), dTheta(0)) (C1a), so A2 was
  identically zero in both: vacuous. Corrected examples: C7.
- s1 claim (c) (Moyal constant-Theta order-2 check): genuine; consistent with C8/C9 below.

## 2. Model and hypothesis class (exact)

Test functions: polynomials of total degree <= 2 on R^4 in normal-ordered monomials
MON(e) = x^e/e! on the 15-jet basis. Bilinear operators of order <= 2 per slot with
coefficients that are polynomials in the coefficient 1-jet symbols TA = Theta(0) (6 comps),
TB = dTheta(0) (24 comps, antisymmetric pair), TQ = d^2Theta(0). A2 is represented by its
table on jet triples, rows = triples with all orders >= 1 and total order <= 4 (544 rows,
DER3); B2 coefficients are the 196 values B2(MON_P,MON_Q)|_0 on nonzero jet pairs (BAS2r).
Hochschild coboundary delta C(f,g,h) = f C(g,h) - C(fg,h) + C(f,gh) - C(f,g) h: the
544x196 matrix M2r (rank 160 over generic jets; dim ker M2r^T = 384). Schouten bracket per
the 058 convention [Theta,Theta]^{pqr} = Theta^{pd} d_d Theta^{qr} + cyc. Central
computations are exact over QQ; numeric cross-checks use seeds 105, 1051, 20261120.

Associativity sign convention (derived, not assumed): with f*g = fg + hbar c1 + hbar^2 c2,
the hbar^2 term of (f*g)*h - f*(g*h) is A2 - delta c2, so the correction requires A2 =
delta c2 (hand-checked on (f,g,h) = (x0, x0, x1^2/2): A2 = +1/4 Theta_01^2 = delta c2 with
c2 = -1/8 P1). Earlier drafts used A2 = -delta B2; corrected here.

## 3. Claims (script labels; all PASS, see .out)

- C1a ESTABLISHED (symbolic): A2 depends on Theta only through the 1-jet and vanishes when
  any argument is constant.
- C1b ESTABLISHED: slot-antisymmetrization of A2 equals +1 x [Theta,Theta]^{abc} d_a f d_b
  g d_c h, kappa = +1 exactly, symbolic generic jets. Confirms the 058 kappa sentence.
- C2 ESTABLISHED (exact rational rank): generic jets, A2 not in im delta (160 -> 161).
- C3 ESTABLISHED (exact linear algebra over QQ with rational jets): the obstruction
  (witness) functionals span EXACTLY the Schouten 3-form space (dim 4). Consequence: at a
  fixed 1-jet, a wild (arbitrary pointwise coefficients) B2 exists iff [Theta,Theta](0) = 0.
- C4 ESTABLISHED: delta_hoch A2 = 0 identically in TB (A2 is always a 2-cocycle; 80
  generating quadruples).
- C5 ESTABLISHED (exact symbolic rank): parametric closure solvability - over the
  21-dimensional family of closed 1-jets at generic Theta(0) = TA1, every z-monomial column
  of A2(z) lies in im M2r (rank stays 160), i.e. delta b = A2 is solvable at every closed
  jet of the family.
- C6 BOUNDED NO-GO, class stated: at four closed test points (two generic Theta(0) x two
  closed TB directions) rank(image of enumerated ansatz class) = 3, augmented = 4: no
  jet-universal B2 in the class {P1, M, div1, U1, U2} solves A2 = delta B2. The enumerated
  class is NOT the full Kontsevich natural class - it omits (dTheta)(dTheta), Theta d^3
  Theta and (d^2Theta)(d^2Theta) contractions; Theta d^2Theta with the undifferentiated
  pair contracted vanishes identically (antisym x sym, verified). Natural-universal
  correction question stays OPEN.
- C7 ESTABLISHED: nonclosed jets: membership False; Schouten-closed jet with Theta(0) != 0:
  A2 nonzero in 244 of 544 rows yet membership True; s1 ex1/ex2 have Theta(0) = 0 hence
  A2 identically 0 (verified).
- C8 ESTABLISHED (exact): constant Theta: delta(B2M) - A2 = 0 identically as polynomials in
  TA, all 544 rows, with B2M = -1/8 Theta^{ab} Theta^{cd} d_a d_c f d_b d_d g (single Moyal
  graph).
- C9 ESTABLISHED as numeric cross-check of C8: exact operator form, 3 random quadratic
  triples, seed 20261120.

## 4. The dichotomy (main result)

At a fixed coefficient 1-jet (Theta(0), dTheta(0)): A2 = delta B2 for a bidifferential
operator of order <= 2 per slot with arbitrary coefficients at that point IF AND ONLY IF
Schouten [Theta,Theta](0) = 0. Without closure it is never a coboundary (C2/C7); with
closure the exact linear system is solvable at every closed jet (C3, C5, C7), and for
constant Theta the universal solution is the Moyal graph -1/8 P1 (C8). Closure alone does
NOT make the naive truncation associative: closed jets with Theta(0) != 0 have nonzero A2
(244 rows, C7) - the defect is removable by adding a correction operator, not by closure.
This SHARPENS (does not contradict) the integrated 058 sentence that Schouten-closure alone
does not remove the full order-Theta^2 associator of the naive truncation: true if read as
"closure alone does not make the naive truncation associative"; misleading if read as
"the associator is not coboundary-removable under closure" (it is, pointwise). Recorded for
the gatekeeper as a possible M3 prior-claim clarification; no appH edit is made in this
proposal.

## 5. No-go fork discipline (C6)

Hypotheses of the C6 bounded non-existence: (i) B2 restricted to the five enumerated
structures P1, M, div1, U1, U2 (products Theta*Theta and Theta*dTheta with <=2 contractions,
orders <=2 per slot); (ii) coefficients of B2 universal (constant) in the jets; (iii) fixed
Theta(0), closed TB direction; (iv) pointwise table model. Avenues, ranked derivation-first:
1. Widen the natural class with (dTheta)(dTheta), Theta d^3 Theta, (d^2Theta)(d^2Theta)
   contractions and retest universality - could yield POSITIVE derivation-grade data (a
   jet-universal natural B2 matching Kontsevich formality U2 existence). Not yet computed.
2. Jet-universal WILD solution: one constant 196-vector b solving delta b = A2 at every
   closed jet simultaneously - positive-aimed, cheap; not yet run.
3. Literature cross-check of the explicit Kontsevich U2 / DeWilde-Lecomte hbar^2
   star-product formula: attempted this session - web search returned empty; the fetched
   arXiv record (math/0101039) was unrelated; the explicit hbar^2 formula is NOT
   independently verified and was NOT used in this package.
4. (Bottom, data-free) sharpening statistics of the same five-column ansatz.

## 6. Tool and provenance notes

- sympy 1.14.0: instance call M.hstack(N) silently returns N (base dropped), at least for
  mismatched row counts; ALL horizontal concatenations here use sp.Matrix.hstack(...).
- s1 files kept unmodified; all .out files committed next to their scripts.

## 7. Unresolved (unchanged by this package)

Orders Theta^3 and higher (associativity-destruction tower beyond order 2 untouched);
operator-norm and convergence estimates for the corrected product; selection of any B2 by
the matrix theory; the natural-universal question of section 5. Problem A remains OPEN;
nothing here derives Assumption ass:dictionary or the half-sided inclusion.
