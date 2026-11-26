# Proposal 089-g-profile-pushforward-weight, round 1

## Result
The R-A fibre-integration (pushforward) template, frontier avenue (1), is EXECUTED EXACTLY at finite D
on the only configuration-space measures the record names — the coupled proper-complex-Gaussian slot law
E w_i w_j* = s^2 g_i delta_ij (integrated 084, appH L3183) and the Haar frame measure (085/087/088). Two
exact outcomes. (S) Slot side: the pushforward of the slot law under the normalization (fibre) map
p(w) = (|w_1|^2,...,|w_D|^2)/sum|w_j|^2 onto the profile simplex is exactly
f(p) = (D-1)! / ( G * (sum_i p_i/g_i)^D ), G = prod g_i — independent of s^2 and of W by scale
cancellation. This weight is S_D-equivariant (f_{sigma g}(sigma p) = f_g(p)), it DETERMINES the input
profile g (up to the W-fixed scale), it is log-convex on the simplex, has no interior stationary profile
unless g is uniform, and its unique maximum sits at the vertex of the largest slot variance (for a unique largest g_i). So the
induced "profile weight" is the input profile in measure form: its relabelling asymmetry is re-imported
label data (rule-3 boundary), and read as a selector it selects the single-slot profile — the maximal
081/082 obstruction — not the uniformity locus. (F) Frame side: the Haar measure pushes forward under
u -> (|u_1|^2,...,|u_D|^2) to the FLAT exchangeable weight (Dirichlet(1,...,1)) — the fully degenerate
symmetric case of the integrated 088 Lemma-4 dichotomy (every profile a minimiser); zero profile content;
on the unordered simplex quotient the weight stays flat, so the R-C orbit-branch reading buys nothing.
The joint fibre integral factorizes (slot and frame are independent product measures in the named class).
Class-bounded extension: for the whole class of PRODUCT slot laws whose squared magnitudes are
independent with law fixed by s^2 x slot variance, the same equivariance + exchangeable-at-uniform
properties hold. Localization: in the record g is a PARAMETER of the slot measure, not a coordinate of
the integrated configuration; the only natural coordinate-output p carries the input equivariantly and
with O(1) noise (no large-parameter concentration inside the named class). No core weight is postulated;
nothing in Problem G is closed.

## Target and status
Problem G, appH L3026-3029: Status OPEN, Priority CRITICAL PATH, Completion PROGRAMME-CONDITIONAL
(unchanged; no labels touched). Edge G.moments-derivedprofile (frontier L487-520, rank 1,
attempted-open post-19). Original target: a weight on profile space PRODUCED BY THE CORE,
non-degenerate along the kernel directions (088 audit sentence, L3189). Dependencies: missing steps
(i)-(iv) untouched. DERIVED: the exact pushforward package inside the named measures. PROGRAMME-CONDITIONAL: everything else.

## Source reading
digest + targeted reads. NOTE: `make_digest.py --check` printed DIGEST STALE (head f5b0b9b -> cd6669f);
per dispatch the digest was NOT regenerated. The digest's appH hash ecb67a25a288 matches the live file
byte-for-byte (re-hashed: 748,814 B / ecb67a25a288...6749 / CRLF 3,840 / bareLF 0), and git status shows
chapters/ and bib/ clean, so the staleness is head-movement only; every passage cited below was read IN FULL.
Reads: frontier.yaml L480-563 (chain-2 G.moments-derivedprofile block); appH L3020-3095, L3119-3121
(Missing step head), L3140-3193 (state-and-coarse-graining L3149, 081-088 block, Vacuum term L3191,
closer L3193); scout 20261118-1954 IN FULL; scout 20261118-1644 skimmed (headers + routes R1-R4);
ledger tail (INTEGRATION-19 entry).

## Research and reasoning
(derivation written after scripts; see Verification)

## Claim classification
(written after scripts; see Verification)

## Proposed changes
(written after scripts)

## Verification scripts
Re-run from repo root: python -I proposals/089-g-profile-pushforward-weight/<script>; live this round all five rc 0, empty stderr, stdout byte-equal to shipped .out. Invariants (live): s1 norm D=2,3,4=1, vertex argmax=argmax g (D=3: 1/3, 8/3, 9), uniform const (D-1)!=2, interior critical forces uniform g; s2 Dirichlet moments 2(D-1)!/(D+2)! vs MC, factorization; s3 equivariance MC, shape-dependence 0.19976 vs 0.18394; hygiene PASS (insert 3,823 B / 602e63d9); simulate read-only PRE 748,814 / ecb67a25...6749, POST 752,639 / 2da0e076...54bb, CRLF 3,842, bareLF 0 (full shas in the .out files).

## Decisions Taken
(1) notes/proposal split (full derivation vs summary + claims; shared markers). (2) Convexity fix this pass: notes said log-concave - wrong. log f = const - D log L, L = sum p_i/g_i linear positive; -log L convex, so f is log-convex, maximum at a vertex (largest g_i), no interior stationary profile unless g uniform; s1 live D=3 vertex densities 1/3, 8/3, 9 give argmax = argmax g. Proposal 'unique minimum ... largest slot variance' fixed to unique maximum. (3) Dispatch 'truncates at it is log-' stale: file complete, already log-convex; only extremum reversed. (4) Prior dead-pass insert corrections stand (notes Decisions (full)).

## Milestone assessment
Routine; no MILESTONE.md trigger applies.

## Status-label recommendation
Unchanged: G OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed
none.

## Remaining open step
A core-PRODUCED profile weight, non-degenerate along kernel directions; requires a dynamical core measure beyond the named slot and frame measures; missing steps (i)-(iv) untouched.

## Special instructions for the gatekeeper
Re-derive the f normalization and the vertex-maximum/log-convexity fact (s1); re-verify insert anchors against the live chapters/ file (POST 752,639 B / 2da0e076...); no bib, labels or refs are added.

## Claims
(fibre map p_i = |w_i|^2/sum_j|w_j|^2; named slot law E w_i w_j^* = s^2 g_i delta_ij; G = prod g_i.)
- Exact pushforward density f(p) = (D-1)!/(G (sum p_i/g_i)^D): established identity conditional on the named slot law; independent of s^2 and W.
- S_D-equivariance f_{sigma g}(sigma p) = f_g(p) and exchangeability at uniform g: established (exact; s3 MC).
- f determines g up to the W-fixed scale: established in the named class (log f recovers linear L; s3 exact D=2).
- f log-convex on the simplex; no interior stationary profile unless g uniform; maximum at the vertex of the largest g_i: established identity.
- Haar frame pushforward = flat Dirichlet(1,...,1), flat on the unordered quotient; joint fibre integral factorizes: established (s2 MC).
- Product-slot-class extension (equivariance, exchangeability at uniform): conditional (quantile identifiability not proved); closed form exponential-specific (s3): conjecture/mechanism beyond exponential case.
- Weight as re-imported label data / single-slot selector: interpretive consequence of the vertex maximum: conjecture/mechanism.

## Relation to integrated passages
Anchors by paragraph position only (exact byte positions in notes-research.md): the insert lands after the 088 rigidity paragraph closer "...and they close nothing in Problem~G." and before Vacuum term. The flat frame pushforward is the fully degenerate symmetric case of the integrated 088 Lemma-4 dichotomy; no produced weight is added, and the integrated 085/087 passages and their claims are untouched.

## What is not claimed
No core-produced profile weight (g stays a parameter of the named slot measure); no closure or narrowing of Problem G; missing steps (i)-(iv) untouched; no sharpening outside the named-measure class; no change to spacetime emergence, definitions, scope or status labels; the flat Dirichlet result is not a selection mechanism.

## Round-2 lead
Test whether a core-dynamical fibre weighting beyond the named product class (e.g. frame fluctuations coupled to the slots) yields a non-flat profile law without g as an inserted parameter.
