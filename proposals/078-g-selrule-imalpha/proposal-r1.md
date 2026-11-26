# Proposal 078-g-selrule-imalpha, round 1

## Result

For the coincident-copy block-cut edge charge of the integrated 077 paragraph, at fixed q
and arbitrary N, the q=2 double-pair criterion is extended exactly to general q inside the
norm-equalized class, and the Im-mismatch branch is closed with a bounded transversality
negation:

1. (exact, all q) det(lambda I_2q - T) = det(lambda^2 I_q + 4 lambda H - 4 K) with
   H = Im(U^dag R), K = R^dag(1 - UU^dag)R >= 0, T the 2q x 2q pencil of 077. The reduced
   spectrum depends on the edge block only through (H,K); Re C0 is invisible at every q,
   symbolically even when it enters C0 and Z0 = R^dag R jointly.
2. (exact, all q, conditional on exact norm equalization K = n I_q, n > 0) the 2q nonzero
   eigenvalues are exactly the union over the eigenvalues h_f of H of the Row length pairs
   -2h_f +/- 2(h_f^2+n)^{1/2}. This is the reduction 077 left unestablished for q>2, now
   established conditionally, with no commutativity hypothesis on H.
3. (exact, equalized class) a double eigenvalue occurs iff two h_f coincide (then the
   multiset is tiled by the repeated row pair - at q=2 this reproduces the 077 double-pair
   iff with the norm condition absorbed by equalization); Im-mismatch gives a simple
   spectrum with the explicit quantitative gap lower bound of the insert; the double-pair
   locus has real codimension exactly three in the q^2+1 parameters (H,n) (eigenvalue
   coincidence in Hermitian matrices; linear onset verified in the three traceless
   directions); the only forced pairing is the fixed-point-free involution
   lambda -> -4n/lambda, which swaps each pair's members and never identifies them;
   forced multiplicity survives only at the excluded boundary K = 0 (rank loss).
   Hence Exit A (a forced-pairing mechanism: Kramers/J^2 = -1 antiunitary, symplectic,
   moment-map) is NEGATED in this class, and Exit B (bounded codimension/transversality
   negation) HOLDS.
4. (q=2, general per-row K) the double-eigenvalue locus is the zero set of the quartic
   discriminant, one real polynomial in the 8 real parameters of (H,K) - codimension one
   along the diagonal directions - and it is strictly larger than the double-pair (tiling)
   locus: the exact rational rows (Im alpha, ||w_perp||^2) = (3,7), (5,11) give quartic
   (lambda-2)^2(lambda+14)(lambda+22): a double root with BOTH Im and norm mismatch that
   is not a double pair; a 10^{-3} shift of the second norm splits it linearly.

Nothing is closed in Problem G: no selection rule, no criterion for general K or general
states, no two-sided reading of the +/- pairs.

## Target and status

- Target: frontier edge G.selrule-imalpha (frontier.yaml L147-157), the avenue (1) of
  077 review-r2: test the Im-alpha mismatch at EXACT-spectra level, norm-equalized rows,
  and general q beyond the exact q=2 case. Boundaries kept: fixed q (does not scale with
  N); 077-bounded and 072-076 classes not re-attempted; the rank-deficient U2 caveat
  (077 review-r2 finding 1) is carried by using no U2 claim in the insert (U2 appears in
  the scripts only as a labelled diagnostic on rank-full data, where the nonzero-spectrum
  guard is asserted).
- Problem G, live-verified from appH L3025-3029 (targeted read this session):
  Status OPEN; Priority CRITICAL PATH; Completion PROGRAMME-CONDITIONAL. Original target:
  the entropy-density/selection functional derived from the matrix theory (items (i)-(iii)
  and the selection rule of the stacked/copy-invariant block). Dependencies: unchanged.
  This contribution: conditional general-q evidence inside the equalized subclass +
  bounded negation for the mismatch branch; DERIVED only in the narrow exact sense of
  items 1,2,4 as structure theorems for the pencil; the programme-level criterion stays
  PROGRAMME-CONDITIONAL. Nothing closes.

## Source reading

digest + targeted reads. scratch/digest.md head (30 lines) per dispatch; digest reported
dirty-chapters: yes, so all relied-on passages were read live and the live hashes pinned:
appH 713,071 B / 3f7e48564a9d... / CRLF 3820 (verified by simulate_apply_078.py PRE
asserts, exit 0); bib 37,463 B / 4d6d7b2a668f.... Read in full: appH L3140-3173 (Row
length paragraph, 076 paragraph L3167, 077 paragraph L3169, anchor L3171, block closer
L3173) and appH L3020-3035 (Problem G ledger entry); proposals/077-g-selrule-copyinv/
review-r2.md (full); 077 proposal-r2.md (grep + targeted); frontier.yaml G.selrule-imalpha
row + chain-2 notes; reports/sme-scout-20261117-1309.md (a)-item-2 and edge-1 table;
reports/ledger.md L1090-1103. Unreadable files: none. Discrepancy: none found; the
digest's dirty flag reflects other chapters, not appH.

## Research and reasoning

Conventions: metric irrelevant (finite-dimensional); T := the pencil of 077 = -2i M,
M = [[C0^dag, Z0], [-I_q, -C0]]; lambda = -2it maps the 077 t-polynomial
t^2 + 4(Im alpha)t - 4||w_perp||^2 (Row length paragraph) to
lambda^2 + 4(lambda)(Im alpha)... explicitly, roots t of the row polynomial give
lambda = -2it = -2 Im alpha +/- 2((Im alpha)^2 + ||w_perp||^2)^{1/2}, matching the Row
length pair formula exactly (convention cross-check done in s2b/s3 against the physical
Hermitian charge Q~, not just the pencil).

Proof of 1. tI_2q - M = [[tI - C0^dag, -Z0], [I_q, tI + C0]]. The block determinant rule
det[[A,B],[C,D]] = det(AD - CB) applies because C = I_q commutes with everything:
det(tI - M) = det((tI - C0^dag)(tI + C0) + Z0) = det(t^2 I + t(C0 - C0^dag) + Z0 - C0^dag C0)
= det(t^2 I + 2i H t + K) with K = Z0 - C0^dag C0 = R^dag(1 - UU^dag)R >= 0. Substituting
t = i lambda/2 and multiplying by 4^q gives the monic identity
det(lambda I_2q - T) = det(lambda^2 I_q + 4 lambda H - 4 K), exact for all q. Re C0 drops
out of (H, K): H = Im C0, K = R^dag P R with P = 1 - UU^dag; the symbolic q=2 check (s3(A))
verifies invariance under arbitrary Hermitian A added to C0 with Z0 = K + C0^dag C0 held
fixed, i.e. including the coupled Z0 dependence. Numerics s1(q<=6) and s3(A,B) confirm.

Proof of 2. K = n I_q: H unitarily diagonalizable, so det(lambda^2 I + 4 lambda H - 4n I)
= prod_f (lambda^2 + 4 h_f lambda - 4n), roots -2h_f +/- 2(h_f^2 + n)^{1/2}. No
commutativity needed because K is scalar. Each quadratic has two distinct real roots
(discriminant 16(h^2+n) > 0), one strictly positive (lambda+ = 2(sqrt(h^2+n) - h)) and one
strictly negative (lambda- = -2(sqrt(h^2+n) + h)); lambda+ is a strictly decreasing
bijection R -> (0, infinity) (dlambda-/dh = -2 + 2h/sqrt(h^2+n) < 0 since |h| < sqrt(h^2+n)),
likewise lambda- onto (-infinity, 0). Therefore multiset coincidences occur exactly when
h_f = h_g (same branch), never across branches (opposite signs).

Proof of 3. Double eigenvalue iff h_f = h_g by the above. Gap bound: on |h| <= M both
branch maps are bi-Lipschitz with constant c(M,n) = 2(1 - M/sqrt(M^2+n)) > 0, giving
same-branch separation >= c min| h_f - h_g |; cross-branch gap =
2(sqrt(h_f^2+n) - h_f) + 2(sqrt(h_g^2+n) + h_g) >= 4n/(sqrt(M^2+n) + M) since
sqrt(h^2+n) - h = n/(sqrt(h^2+n) + h) >= n/(sqrt(M^2+n)+M) and symmetrically. Involution:
lambda+ lambda- = -4n, so lambda -> -4n/lambda preserves the multiset (equivalently the
char poly is invariant since it is even after conjugating h -> ... ; verified numerically
to 2.7e-13); fixed points over R would need lambda^2 = -4n < 0: none; the AM-GM bound
|lambda + 4n/lambda| >= 4 sqrt(n) is sharp (attained at h = 0) and is a separation, not a
coincidence. Codimension: the locus {two h_f equal} in Herm(q) has top stratum
multiplicities (2,1,...,1) of real dimension (q-1) + [q^2 - (4 + q - 2)] = q^2 - 3, so
codim 3 in (H,n) as well (n adds one dimension to both). Near h I_q: H = h I + eps V with
V traceless Hermitian; double eigenvalue iff V does, i.e. iff V = 0: three independent
real conditions - the (G) numerics show linear onset in three independent traceless
directions, so the locus is nowhere dense and crossed transversally. Exit A adjudication:
any mechanism forcing multiplicity two independent of h-coincidence would have to act on
the dense set of simple spectra constructed above - impossible; the only universal
structure is the fixed-point-free involution (which forces the count 2q parity but not
multiplicity). Kramers-type doubling would require an anti-linear symmetry squaring to -1
commuting with T and acting on eigenspaces; T's data here are the generic 2q real
parameters (H,K) with no such symmetry in the class (s2b(D)/s3(F): 300/300 and 400/400
simple spectra on generic data - a forced doubling would give the opposite). This is the
standard Hermitian fact (no stable level crossings below 3 parameters), used as an
analogue, not as a citation-dependent step; the proof above is self-contained.

Proof of 4. q=2 general K: char poly = lambda^4 + ... real coefficients (isospectrality of
T with Hermitian Q~ forces all roots real; the quartic coefficients are real because
det(lambda I - T) = det(lambda^2 I + 4 lambda H - 4K) with H,K Hermitian:
conjugate-symmetric coefficients... verified: leading monic, and roots real since T is
similar to the Hermitian Q~ on its range). Double root iff discriminant = 0, one real
polynomial in the 8 real parameters; not identically zero (sample value 212336640);
factorization identity disc(f1 f2) = disc(f1) disc(f2) res(f1,f2)^2 symbolic, with
disc(f_i) = 16(h_i^2 + n_i) > 0 for n_i > 0: double roots come only from cross-resultant
zeros, a genuine codim-1 hypersurface (in the diagonal class: the resultant in 4
parameters is not identically zero and changes sign across the example, so codim exactly
1 there). Example (3,7),(5,11): -2*3+2 sqrt(9+7) = 2 = -2*5+2 sqrt(25+11); the charge
spectrum is exactly {-22,-14,2,2}; this is a double ROOT but not a double PAIR (not tiled
by one pair), consistent with the 077 iff (whose two conditions are both violated).
Perturbation n2 -> 11+1e-3 splits the double root at first order (gap 1.667e-04), so the
locus is crossed transversally: mismatched double eigenvalues exist only as codim-1
tunings, never on an open set of mismatched data - the transversality negation for the
per-row class.

Literature (context only, NOT used as derivations; recorded from
reports/sme-scout-20261117-1309.md edge-1 table, which reports DOI-level verification by
the scout; I did NOT independently re-fetch these records this session - not independently
verified): Tisseur & Higham, SIAM J. Matrix Anal. Appl. 22 (2001), DOI
10.1137/S0895479800371451 (quadratic-eigenvalue linearization: motivation for the pencil
reduction - my identity L1 is self-contained); Al-Ammari, Tisseur, Linear Algebra Appl.
453 (2012), DOI 10.1016/j.laa.2012.03.020 (generic simplicity of quadratic pencils:
analogue for item 3 - not imported); Tisseur & Zaballa, SIAM J. Matrix Anal. Appl. 34
(2013), DOI 10.1137/120867640 (perturbing matrix pencils to simple spectrum: analogue);
Ryu, Schnyder, Furusaki, Ludwig, New J. Phys. 12 (2010) 065010, DOI
10.1088/1367-2630/12/6/065010 (Kramers/AII pairing: the Exit-A mechanism class checked
and found absent here); Keller, "Multiple eigenvalues", arXiv:0711.3948 (2007) (venue not
independently verified by scout either); Xia, IEOT 48 (2004), DOI 10.1007/s00020-002-1191-y
(background); Frenkel 2311.10131 section 3.2 (fixed-q constraint; the necessity direction
for stacking remains absent, consistent with 076). No bib entry is needed: the insert has
no citation.

Comparison with original target: the edge asked for exactly items 1-4; all delivered.
The 077 sentence "no such reduction is established for q>2" is sharpened: it IS
established for all q under exact norm equalization (items 1-2), and unestablished but
transversally forbidden outside it (items 3-4). Problem G's missing steps (selection rule
derivation, criterion outside the tested classes, two-sided +/- reading, state input) are
untouched.

## Claim classification

- det identity + Re invisibility incl. coupled Z0: established (proof + symbolic q=2,3;
  numerics q<=6).
- scalar-K spectrum formula, all q, simple spectra, gap bound, involution, codim-3 locus:
  established (elementary proofs above; conditional on the stated equalization hypothesis
  for the formula itself).
- q=2 general-K: disc identity, positivity of row discriminants, exact example,
  codim-1-along-diagonal-directions: established (symbolic rational arithmetic).
- "no mechanism internal to the class forces multiplicity two": established relative to
  the explicitly described class (simple spectra dense + only forced structure the
  fixed-point-free involution); not a statement about mechanisms outside the class.
- Hermitian-crossing codim-3 as a general fact: established (standard; self-contained
  proof given for the needed direction).
- Everything about states, ensembles, ensembles' typicality, the selection rule, N->inf:
  NOT claimed here (077 owns those, unchanged).

## Proposed changes

One file: chapters/appH-microscopic-proofs.tex. Site: immediately BEFORE the unique
line-start anchor `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}` (currently
L3171), i.e. after the blank line following the 077 paragraph (L3169); the new paragraph
is blank-line separated on both sides. KEPT: everything; no sentence removed or replaced;
no existing equation touched. The insert adds exactly one paragraph (the paragraph block
of the 072-077 problem-G block, before the closer L3173 which stays).

Anchor first sentence (verified unique by search): `\emph{Vacuum term.} The abstract
of~\cite{Steinacker2023} states that the vacuum energy there does not act as a cosmological
constant` - occurs exactly once (simulate_apply_078.py: 1 occurrence of the line-start
long form, 2 of the short `\emph{Vacuum term.}` as before). No \ref/\eqref/\cite/\label
added; no new labels; no duplicate labels introduced (insert defines none).

The paragraph body (fenced latex; file insert-r1.tex, single content line, terminal CRLF,
3,910 B content, sha256 e7697412c4de...):

```latex
\emph{Exact spectrum structure of norm-equalized coincident copies at general copy number.} Denote by \(T\) the \(2q\times2q\) pencil of the paragraph above, set \(H=\operatorname{Im}C_0=(C_0-C_0^\dagger)/(2\mathrm i)\) and \(K=Z_0-C_0^\dagger C_0=R^\dagger(\mathbf 1_{qN}-UU^\dagger)R\), positive semidefinite. For every \(q\) the characteristic polynomial of the pencil is exactly \(\det(\lambda\mathbf 1_{2q}-T)=\det(\lambda^{2}\mathbf 1_q+4\lambda H-4K)\), so the nonzero spectrum of \(\widetilde Q\) depends on the edge block only through \((H,K)\) and \(\operatorname{Re}C_0\) is invisible at every copy number, not only at \(q=2\) (exact; symbolic at \(q=2\) and \(q=3\), and at \(q=2\) with \(\operatorname{Re}C_0\) entering \(C_0\) and \(Z_0\) jointly; numerical to \(10^{-14}\) through \(q=6\)). Under exact norm equalization, \(K=n\,\mathbf 1_q\) with n>0, which in the block-diagonal per-copy reading is equality of all \(\|w_\perp\|^{2}\) with vanishing cross terms, the \(2q\) nonzero eigenvalues are exactly \(-2h_f\pm2(h_f^{2}+n)^{1/2}\), with \(h_{1},\dots,h_{q}\) the eigenvalues of \(H\), for every \(q\) and with no commutativity hypothesis on \(H\): the Row length pair formula, lifted from \(q=2\) to general \(q\) conditionally on exact equalization, the reduction the paragraph above left unestablished for \(q>2\) (exact; the \(\widetilde Q\)-spectra agree with the pairs to \(2\times10^{-14}\) through \(q=6\)). Within the equalized class a double eigenvalue occurs if and only if two imaginary parts coincide, \(h_f=h_g\), and the multiset is then tiled by the repeated Row length pair of the common value; imaginary-part mismatch leaves the \(2q\) eigenvalues pairwise distinct, with spacing at least \(\min\bigl(2(1-M(n+M^{2})^{-1/2})\min_{f\ne g}|h_f-h_g|,\;4n((n+M^{2})^{1/2}+M)^{-1}\bigr)\) for \(|h_f|\le M\), the gap turning on linearly in the mismatch with log-log slope between \(0.987\) and \(1\) over three decades, and the double-pair locus is the eigenvalue-coincidence set of the Hermitian matrix \(H\), of real codimension three in the \(q^{2}+1\) real parameters \((H,n)\): the only structure forced at mismatch is the fixed-point-free involution \(\lambda\mapsto-4n/\lambda\), which swaps the two members of each Row length pair without ever identifying them, and multiplicity two is forced nowhere except at the excluded boundary \(K=0\), where the pencil loses rank. Beyond exact equalization the quartic at \(q=2\) has a double root exactly where its discriminant vanishes - one real polynomial condition in the eight real parameters of \((H,K)\), and in the diagonal directions tested below it cuts a hypersurface of codimension exactly one - and this double-root locus is strictly larger than the double-pair locus of the paragraph above: the mismatched rows \((\operatorname{Im}\alpha,\|w_\perp\|^{2})=(3,7)\) and \((5,11)\) share the root \(\lambda=2\) with quartic exactly \((\lambda-2)^{2}(\lambda+14)(\lambda+22)\), a double root that is not a double pair, splitting linearly, minimum gap \(1.67\times10^{-4}\) at the shift \(10^{-3}\) of the second norm (exact in rational arithmetic for the factorization, numerical for the split; \(400/400\) random general \((H,K)\) samples have simple spectrum). These are exact-spectrum structure statements for the rank-one edge-datum family of coincident copies at fixed \(q\) and arbitrary \(N\), inside the transplanted rule with its single-dominant-diagram hypothesis at leading semiclassical order and its diagonal-cut convention, valid in the exactly equalized class and, for the last display, in the general \(q=2\) class; they are statements about pencil spectra, not about any state or ensemble, they leave the two-sided reading of the \(\pm\) pairs, the selection rule itself and the general-\(q\) criterion of the paragraph above untouched outside the equalized class, and they close nothing in Problem~G.
```

Stale passages elsewhere: none require change. The 077 paragraph's "no such reduction is
established for \(q>2\)" remains TRUE as stated (it concerns the 077 class, not the
equalized subclass) and is explicitly referenced, not edited. No bib changes.

Hypothesis class of the negation (quoted for the gatekeeper): fixed q >= 2 (not scaling
with N); 077 factorization block data U = 1_q (x) u with u a unit vector, R any qN x q,
N >= q+1 fixed; (for items 2-3) EXACT norm equalization R^dag(1_q (x) 1_N - UU^dag)R =
n I_q, n > 0 (equivalently, block-diagonal per-copy: all ||w_perp,f||^2 equal, cross
terms zero); Re(U^dag R) arbitrary; u arbitrary. Negated statement: no mechanism internal
to this class forces a double eigenvalue at Im(U^dag R) mismatch, except at the excluded
boundary K = 0 (rank loss). Beyond the equalization, at q=2 and general K: double roots
live exactly on the codim-1 discriminant locus; simple spectra are dense (400/400 random).

## Verification scripts

All in this folder; run with `python -I <name> > <name>.out 2>&1` from the folder (the
simulator from the repo root). None reads chapters/ except the simulator (read-only,
asserts pins). Reproduction pack (exact commands + expected invariants):

- `python -I s1_structure_general_q.py` -> ends `ALL S1 ASSERTS PASS`; invariants: sign
  dict all 1.0; identity max rel dev <= 8e-15; invisibility dev <= 5e-15; sympy True,True.
- `python -I s2b_imalpha_exact_fixed.py` -> ends `ALL S2B ASSERTS PASS`; invariants:
  slope == 1/sqrt(a1^2+n) (symbolic); D(d=0)=0; resultant sub-checks d**2, -4*N1*d**2;
  row disc negative; (C) dev <= 5e-15, D slopes in [0.98,1.02]; 300/300 simple.
- `python -I s3_scalarK_general_q.py` -> ends `ALL S3 ASSERTS PASS`; invariants:
  (A) both symbolic True; (B) worst union 1.776e-14, worst Re-dev 1.066e-14;
  (C) >=130/150 trials pass with bound asserted; gap slopes [0.9999,0.9987,0.987];
  (D) involution dev <= 3e-13, FP margin <= 0 (i.e. >= 4 sqrt(n) holds);
  (E) disc identity True, example factorization (lam-2)**2(lam+14)(lam+22), generic disc
  212336640, spectrum [-22,-14,2,2] to 1e-9, split gap in (1e-5,1e-1);
  (F) 400/400; (G) slopes within 0.01 of 1.
- `python -I proposals/078-g-selrule-imalpha/simulate_apply_078.py` (repo root) ->
  `ALL ASSERTS PASS`, exit 0; PRE pins 713,071 B / 3f7e48564a9d / CRLF 3,820 / bareLF 0;
  POST appH 716,985 B / be3dbddd9156... / CRLF 3,822 / body line 3171 / anchor 3173.

## Decisions Taken

1. Fix convention for the s2 crash: new file s2b (byte-frozen defect artifacts retained
   with lineage) rather than in-patch editing s2 - preserves the audit trail the
   gatekeeper can re-check. Rejected: silent overwrite (loses the defect evidence the
   dispatch requires).
2. During development I additionally found and fixed two latent defects of the never-run
   s2 sections: the invalid `eigvalsh(-2j*M)` on a non-Hermitian matrix (replaced by
   eigvalsh of the genuinely Hermitian Q~ = -2i(UR^dag-RU^dag) with rank guards), and the
   wrong U2 epsilon assert (U2 varies linearly in the mismatch). All recorded in the
   s2b header and manifest.
3. Exit direction: combined package - positive exact theorems (1,2,4) + the bounded
   negation (3) - rather than choosing one exit, because both share the same derivation
   (L1-L2) and the gatekeeper can verify one coherent chain; the negation would be
   unprovable without items 2-3 and the theorems would not answer the edge's "mismatch"
   question without item 3.
4. U2 is kept out of the insert entirely (script diagnostic only), to avoid re-exposing
   the rank-deficient caveat of 077 review-r2 finding 1; the D/tiling reading carries the
   insert's "double pair" language, which matches the 077 paragraph's usage.
5. Codimension statement corrected mid-research from an earlier "codim 1" note to codim 3
   (equalized class) / codim 1 (general-K q=2 quartic locus) after checking the
   Hermitian-coincidence stratum dimension; the insert states the corrected facts with
   the numerics (G) backing the transversal crossing.
6. "double root" vs 077 "double pair" distinguished explicitly in the insert (the (3,7),
   (5,11) example is a double root, not a double pair) to prevent a spurious
   contradiction with the integrated q=2 iff.

## Milestone assessment

Routine. No critical-path step is closed; no milestone trigger applies. The package
sharpens the G ledger evidence (a general-q conditional reduction + a bounded mismatch
negation) without any label change.

## Status-label recommendation

Current critical-path list re-derived from ch17 (full-GR scope: A,B,C,D1,E,F,G-derived,N)
and appH ledger: Problem G remains Status OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL
(L3025-3029). Affected labels: none. No change proposed.

## Author decision needed

None.

## Remaining open step

To close the original Problem G targets: the selection rule must be derived from the
matrix theory (not transplanted); the stacked/copy-invariant criterion must be extended
beyond exact equalization (general K) at fixed q>2 (at q=2 the double-root discriminant
locus is now known, its diagrammatic reading is not); the two-sided reading of the +/-
pairs is still untreated; the state input and the (i)-(iii) items of the ledger are
untouched. For the edge itself, the residual open step: none inside the equalized class
(items 2-3 answer the avenue), while the general-K general-q (q>2) double-eigenvalue
locus (quintic-and-up discriminants) and the diagrammatic reading of the mismatched
double-root hypersurface remain open.

## Special instructions for the gatekeeper

- Re-derive items 1-4 from scratch; the block-determinant step in item 1 requires the
  commuting-block condition (C = I_q) - check it is used, not assumed away.
- The insert must NOT be read as closing, or partially closing, Problem G, and the
  equalized hypothesis K = n I_q must not be read as derived from any state: it is the
  exact form of the 077 norm-equality condition in block language.
- Check the insert against the hygiene contract in simulate_apply_078.py (ASCII, one
  content line, no brackets/dollars/refs, forbidden-word scan, exactly one \emph,
  required closer sentence) and that the numbers quoted (1e-14, 2e-14, 0.987, 3,7)/(5,11),
  (lam-2)^2(lam+14)(lam+22), 1.67e-4, 400/400) appear in the .out files of s1/s2b/s3 -
  they are upper bounds or exact outputs there.
- Verify no contradiction with the integrated 077 "double pair iff both match": the
  example is a double root with multiset {2,2,-14,-22}, tiled by no one-copy pair; the
  077 iff is about tilings (D = 0), and inside the equalized class a double eigenvalue
  IS a tiling, as stated.
- The literature list is context only; no manuscript claim depends on it; no bib entry
  is requested.
- Re-run all four commands in the reproduction pack before re-deriving; if the live
  appH hash has moved past 3f7e48564a9d..., re-anchor by the quoted line and redo the
  PRE pins (the site itself is anchor-based, not line-number-based).
