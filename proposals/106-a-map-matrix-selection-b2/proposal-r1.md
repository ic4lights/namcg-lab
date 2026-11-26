# Proposal 106, round 1 — matrix-side selection of the order-Θ² correction B₂ (Problem A, edge A.map)

Date 2026-11-21. Branch local/gpu. Researcher package; nothing integrated; no status,
priority or completion label touched (rule 2).

Live anchor record at package time: `chapters/appH-microscopic-proofs.tex` = **807971 B,
sha256/16 53c1c478ae1a79ff, 3872 CRLF** — the POST state of integrated item 35
(gatekeeper review `proposals/105-a-map-order2-associator-correction/review-r2-final.md`).
The package is anchored on the integrated order-Θ² coboundary-dichotomy paragraph in
sec:status-A (the 105 payload), specifically on its closing scoping sentence "what
remains open here is not the existence of a general natural correction but its selection
by the matrix theory". Digest basis: `scratch/digest.md` DIGEST CURRENT for this tree
(head b9b4260, dirty-chapters: yes — the uncommitted integration); reads were
"digest + targeted reads" (protocol 4): appH Problem A entry in full, ch17 Problem A
passage, ch03 L140-229 and L330-510, 105 proposal/findings/review-r2-final/s1b in full.

## 1. Claim (one sentence)

On the diffeomorphism-pullback class of the manuscript's own semiclassical coordinate
construction, the matrix theory SELECTS a concrete order-Θ² correction B₂ explicitly
(below: the pulled-back Moyal second term), it satisfies the 105 coboundary equation
A₂ = δB₂ exactly on the 544-row model, it lies outside the 105 bounded five-structure
class, and the selection is provably NOT a function of the bivector 1-jet — the residual
selection problem reduces to choosing the semiclassical chart (embedding 2-jet), i.e. to
the condensate/class-selection sub-step, not to any 1-jet formula.

## 2. Exact setting (what the manuscript supplies)

(H1) Semiclassical configuration, `chapters/ch03-matrix-action.tex` def:matrix-coords-ext
(L172-205): background Hermitian X̂ with [X̂^I, X̂^J] = iΘ^{IJ}, Θ CONSTANT and
nondegenerate; a D=4 configuration is a local diffeomorphism y ↦ x(y) from leaf
coordinates with nondegenerate Poisson bivector θ^{αβ}(y) obeying the manuscript
identity  Θ^{IJ} = θ^{αβ}(y) ∂_αx^I ∂_βx^J;  Tr → ∫d⁴y ρ, ρ = 1/|Pf θ|.
(H2) Constant-Θ Weyl map, rem:ch3-trace-quadratic (L448 ff.): Ŵ(f) = ∫ d⁴k/(2π)⁴
f̃(k)e^{ik·X̄}. (H3) Product = operator product; per rem:ch3-moyal-check (L371-446) this
is the constant-Θ Moyal product, exact.

Fix d=4 and rename the leaf coordinates to x (the 105 framework variable; manuscript y ↔
script x). Let φ = x(·): leaf → target. For leaf test functions F,G define F̃ = F∘φ⁻¹ on
the target and the induced leaf product
    F ⋆_y G := ((F̃ ⋆_Θ G̃) ∘ φ).
M = dy/dx|₀ = (∂x/∂y)⁻¹|₀; the manuscript identity is equivalent to
θ^{ab}(0) = Θ^{IJ}M^a_I M^b_J (verified symbolically, P1). Second jet of the inverse
map: N^a_{IJ} = ∂²y^a/∂x^I∂x^J|₀ = −M^a_P B^P_{bc} M^b_I M^c_J with B^I_{ab} =
∂²x^I/∂y^a∂y^b|₀ (Taylor inversion; used as defined).

Taylor model used by the checker: x^I = A^I_a y^a + ½B^I_ab y^a y^b with A the FIXED
rational matrix [[1,1,0,0],[0,1,1,0],[0,0,1,1],[0,0,0,1]] and B, Θ rational or symbolic;
A⁻¹ is always rational, which avoids generic 4×4 symbolic inversion.

## 3. The selection and its properties

**Pullback selection.** ⋆_y is exactly associative (conjugate of ⋆_Θ). Its order-Θ term
is (i/2)Θ^{IJ}M^a_IM^b_J ∂_aF∂_bG = (i/2)θ^{ab}(0)∂_aF∂_bG — exactly the 105 naive
truncation with Θ(x) := θ(y) (coefficient check P1). The order-Θ² term of the exact
product is therefore, necessarily, a solution B₂ of A₂ = δB₂ at the induced jet, and it
is the explicit bidifferential
    B₂^PB(F,G) = −(1/8)Θ^{IJ}Θ^{KL}
        (M^a_I M^b_K ∂_a∂_bF + N^a_{IK} ∂_aF)(M^c_J M^d_L ∂_c∂_dG + N^d_{JL} ∂_dG),
the pullback of the single Moyal graph. Only the EMBEDDING 2-JET (A,B) enters B₂^PB(0);
the coefficient 3-jet and above do not (∂² of F∘φ⁻¹ needs φ⁻¹ only through 2-jets),
while A₂ needs the induced θ 1-jet (θ(0),∂θ(0)) = (ΘMM, Θ(NAM + MNᵗA)-type terms).

**Verified statements** (script `s2_matrix_selection.py`, exit 0, 101.8 s, all exact
over ℚ/symbolic; framework identical to 105 s1b: 15-jet MON basis, 544 all-derivative
rows DER3, 196 columns BAS2r, integer coboundary matrix M2r with rank 160,
dim ker M2r = 36, dim ker M2r^T = 384 — reproduced exactly; A2 table rebuilt with the
full 2-jet coefficient function THS and 105's C1a parity re-checked):

- P1 PASS: manuscript identity Θ^{IJ} = θ^{ab}∂_ax^I∂_bx^J holds identically in the
  embedding 2-jet B; (2,2) channel of B₂^PB equals −(1/8)θ^{αγ}θ^{βδ}F_{,αβ}G_{,γδ} so
  the first-order term is the naive B₁(θ).
- P2 PASS: [θ,θ](0) = 0 IDENTICALLY in (B,Θ) at generic rational A: every induced leaf
  1-jet is Schouten-closed (pushforward of a constant bivector is Poisson). The matrix
  class lands on the coboundary-solvable side of the 105 dichotomy automatically.
- P3 PASS: at B = 0 the B₂^PB table equals the 105 C8 Moyal table −(1/8)·P1 entrywise
  on all 196 columns (integration-35 text match).
- P4 PASS: at 3 rational embedding points (seeds 1061-3, Θ and θ(0) both nondegenerate,
  A fixed, B ≠ 0): all 544 rows of M2r·b₂vec − A₂(θ-jet) vanish exactly; wild
  membership True. (General point: the equality is forced by exact associativity of
  ⋆_y — A₂ = δc₂ is the order-2 associativity identity — verified symbolically at 3
  points, not proved symbolically for all jets.)
- P5 PASS: at each of the 3 points the evaluated five-structure class
  {P1, M, div1, U1, U2} (105 NKINDS; D2 vanishes) has rank 5 and adding b₂vec gives
  rank 6: **B₂^PB lies outside the 105 bounded class** — it contains the (∂θ)(∂θ) and
  θ(∂θ) channels that class omits (the channel tensors C21/C12/C11 of the formula).
  So matrix selection genuinely escapes the C6 obstruction; C6 is not invalidated,
  its class is just smaller than what the matrix side produces.
- P6 PASS: at fixed (A, Θ), the linear map B ↦ ∂θ(0) has rank 20 (= 24 minus the 4
  linearized-closure directions, cf. P2) and kernel dimension 20. An exact rational
  kernel vector δB changes 7 of 196 entries of the B₂^PB table while leaving
  θ(0) AND ∂θ(0) unchanged; the difference table lies in ker M2r (M2r·Δ = 0). Hence:
  **two matrix backgrounds with identical naive data (identical coefficient 1-jet)
  select different corrections, differing by a wild (coboundary-kernel) element.**
  Selection is NOT 1-jet-local.
- P7 PASS: the span of the 20 kernel-direction changes has dimension 20 ≤ 36: within a
  fixed closed 1-jet the matrix-selected solutions form a 20-dimensional affine family
  inside the 36-dimensional pointwise solution freedom; the remaining
  36−20 = 16-dimensional freedom at that jet is not touched by any embedding 2-jet.
- P8 PASS: invariance under a rational Sp(Θ) target-frame change S (Θ' = SΘSᵗ,
  A' = SA, B' = SB): θ-jet and selected table agree exactly (selection is
  target-symplectic-frame invariant).

## 4. Rule-6 classification

- Setting (H1)-(H3): manuscript content, cited by file:line above; NOT re-derived here.
- "⋆_y exactly associative; order-1 term = naive B₁(θ); order-2 term = B₂^PB":
  ESTABLISHED identity/derivation (chain-rule algebra; P1/P3 symbolic; the pullback
  argument is standard conjugation).
- δB₂^PB = A₂ at induced jets: ESTABLISHED for the 3 checked rational points (all 544
  rows exact) and CONDITIONAL-BY-ARGUMENT for the whole class (associativity of ⋆_y
  forces it at every jet; a general symbolic proof for arbitrary rational jets was not
  run — 3 generic points + structural argument).
- P2 closedness: ESTABLISHED (symbolic identity in (B,Θ)).
- P5 outside-class, P6 non-1-jet-locality, P7 freedom dimension, P8 frame invariance:
  ESTABLISHED at the stated test data (exact linear algebra).
- "The residual selection problem reduces to choosing the semiclassical chart":
  this is an ANALYSIS STATEMENT (unresolved step honestly located), not a derivation of
  that selection.
- No new numerical constants and no citations were introduced; Kontsevich formality is
  NOT used (selection here is intrinsic to the matrix construction, not a literature
  formula). Nothing in this package needs "not independently verified" marking — there
  are no external literature claims.

## 5. Hypothesis class covered / NOT covered (scope honesty)

Covered: backgrounds that are semiclassical diffeomorphism configurations of
def:matrix-coords-ext with D=4 (A invertible), constant Θ, Weyl operator product
(H1)-(H3); order-2 truncation of the exactly-associative pullback product, on the
polynomial 2-jet model with order ≤ 2 per slot.
NOT covered: D>4 submanifold embeddings (θ induced from a degenerate ambient pullback;
closure there is the submanifold-Poisson question, untouched); non-Abelian
[X̂,X̂]; backgrounds with ∂Θ≠0 not arising from an embedding; orders Θ³ and higher
(the pullback product is exact to all orders but only the order-2 table is tabulated
here); operator-norm/convergence; the semiclassical limit itself; selection of the
chart/condensate.
Status: **Problem A remains OPEN.** This package supplies a derivation-grade selection
input WITHIN (H1)-(H3) and precisely locates the residual gap (chart selection, and the
16-dim kernel component invisible to embedding 2-jets); it does not close A, does not
derive Assumption ass:dictionary, and does not make spacetime fundamental — the matrix
model remains primitive and x(y), θ(y) remain derived semiclassical data (emergence
preserved).

## 6. Relation to 105 (integrated) and to the scouting report

The integrated paragraph ends "…its selection by the matrix theory". This package is
the first edge on that word: it shows (i) the matrix side DOES select (explicit formula,
matrix-verified δB₂^PB = A₂), (ii) the selected object is outside the bounded
five-structure class (so 105's C6 no-go neither blocks nor is evaded by scope — a
different, matrix-native object wins), and (iii) the selection cannot be encoded as any
function of the coefficient 1-jet alone (P6), which retires the "closed 1-jet ⇒
1-jet-universal selected formula" search programme and redirects effort to chart/
condensate selection. The scout report `reports/sme-scout-20261120-1952.md` predates
integration 35 (it still lists the dichotomy paragraph as unintegrated); relied upon
only as noted. `reports/sme-scout-20261120-1952.md` predates integration 35 (it
lists the dichotomy paragraph as not yet integrated); on its routes: Route 4 (explicit
Kontsevich/Cattaneo-Felder correction terms) is now SUPERSEDED on this class — the
pullback formula replaces any literature formula on (H1)-(H3); Route 10 (twist for
non-Poisson Θ) is irrelevant inside the class (P2: automatically Poisson) and remains
the handle for ∂Θ-not-from-embedding backgrounds; Route 5 (Steinacker-type algebraic
states as selection analogues) is the natural next pointer for CHART selection (the
remaining step); scout no-go #1 (associativity ⇒ Poisson) is confirmed and sharpened
(P2: the matrix class automatically satisfies it).

## 7. Smallest-accurate integration anchor candidate (proposed, nothing integrated)

One new paragraph in `chapters/appH-microscopic-proofs.tex` sec:status-A, inserted in
the SAME position convention as item 35: immediately after the integrated
order-Θ²-dichotomy paragraph (ending "…does not close Problem~A.") and before
"\paragraph{Missing step.}", payload = `insert-r1.tex` (1950 B, sha256/16
e10d4960e7777f54, one CRLF line). Live PIN
`b"does not close Problem~A.\r\n\r\n\paragraph{Missing step.}"` count 1
(hygiene_106.py PASS). Simulated POST (`simulate_apply_106.py`, scratch/sim only):
**809923 B / sha256/16 0c322018295cec67 / 3874 CRLF — valid only for the current live
bytes**; the integrator must re-verify the anchor and live sha against the working tree
(the anchor moves if any other chain integrates into sec:status-A first). No label,
ref, cite, or status word introduced (hygiene-checked); macros all pre-existing in
appH: \Theta \delta \le \paragraph \partial \tfrac \theta. Alternative anchor considered
and rejected: appending to the 105 paragraph (would exceed the smallest-text rule and
re-open accepted 105 text).

## 8. Gatekeeper instructions

Reproduce from repo root: `python -I proposals/106-a-map-matrix-selection-b2/s2_matrix_selection.py`
(~102 s, exit 0) and diff against `s2_matrix_selection.out`;
`python -I .../hygiene_106.py`, `python -I .../simulate_apply_106.py` (both exit 0);
`python -I .../manifest_106.py` for the file table. Framework parity vs 105 is
asserted INSIDE the script (rank 160, ker 36/384, C1a). Re-derivation pointers: the
P6 witness is a kernel vector of the Jacobian Mb printed by the script; membership uses
the same exact rank test as 105. MUST-NOT-assert list for any verdict text: closure of
Problem A; derivation of ass:dictionary or the half-sided inclusion; that the selection
is 1-jet-local or universal; that spacetime is non-emergent or that the semiclassical
chart is fundamental; any applicability beyond (H1)-(H3); any D>4, non-Abelian or Θ³+
content. The package is one edge of A.map; it does not change any status/priority/
completion classification.

## 9. Findings appendix (folded in per harness policy: no standalone findings file)

Folder inventory is given by `manifest_106.py` (run it; it lists every file with size and
sha256/8, including itself and the regenerated .out, so no hash is self-referential).
Reproduce all claims: `python -I proposals/106-a-map-matrix-selection-b2/s2_matrix_selection.py`
(~102 s, exit 0; log `s2_matrix_selection.out`). Hygiene evidence: `hygiene_106.out`
(insert-r1.tex 1950 B / sha256/16 e10d4960e7777f54; macros \Theta \delta \le \paragraph
\partial \tfrac \theta; PIN count 1 on live appH 807971 / sha256/8 53c1c478 / 3872
CRLF; HYGIENE PASS). Splice evidence: `simulate_apply_106.out` (PIN occurrences 1;
simulated POST 809923 B / sha256/16 0c322018295cec67 / 3874 CRLF written to
scratch/sim/appH_after_106.tex only; live appH hash unchanged after the run).
Rule-8 redirect content: (i) matrix-side selection is nonempty and explicit on the
pullback class (B₂^PB); (ii) any 1-jet-universal selected formula is provably
impossible (P6 witness); (iii) the open problem localizes to semiclassical chart/
condensate selection; (iv) 16 of the 36 wild-solution dims at a fixed closed jet are
invisible even to embedding 2-jets, so higher embedding data or dynamics are the
candidates to finish. Problem A remains OPEN; no status/priority/completion label was
added, removed or changed anywhere by this package.
