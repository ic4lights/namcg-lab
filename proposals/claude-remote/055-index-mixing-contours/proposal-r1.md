# Proposal 055-index-mixing-contours, round 1

## Result

Avenue 2 of review 054-r2 (contours that mix the indices) is settled for every linear contour
A_mu = sum_nu Lambda_{mu nu} X_nu, Lambda in GL(10,C), X traceless Hermitian. The class contains the
per-index family R_u and all complex Lorentz images of it. Definition (A), gamma = 0, eps -> 0 first at
fixed N.

1. **Normal form and two classes (exact; algebra at any N).** Write h = Lambda^T eta Lambda. The contour gives
   Re iS_b <= -c S_E(X) for some c > 0 exactly when
   (P) Im[h(a,a)h(b,b) - h(a,b)^2] > 0 for all independent real a, b. This is the equivalence at N = 2. At
   N >= 3 the inequality implies (P) through an su(2) block.
   For n = 10 >= 3, (P) holds iff h = T^T diag(d_mu) T with T real and, up to h -> -h, the phases of d have
   pairwise sums in (0, pi). So the set splits as C = C_0 ∪ (-C_0). The Hermitian contour h = eta lies in the
   closure of C_0 and not in the closure of -C_0. No path of invertible h inside the closure of C joins the
   two.
2. **Bounded no-go (exact; any N).** Suppose h is in C_0 and the Fourier mode Tr e^{i k^mu A_mu} is bounded on
   the contour, which is the case exactly when q = Lambda^T k is real. Then k.k = q^T h^{-1} q lies in the open
   sector -pi < arg(k.k) < pi/2, i.e. |arg t| < 3 pi/4 with t = e^{i pi/4} k.k. The R_u already fill this
   sector. So no index mixing, complex boost or linear change of variables enlarges the 054 sector. Real causal
   momenta (k != 0, k.k <= 0) are exactly the real momenta that this class cannot reach.
3. **Values (proved at N = 2).** For h in C_0 and q real, the contour integral is
   V(h,q) = F_E(e^{i pi/4} q^T h^{-1} q), a value of the 054 continuation of the Euclidean characteristic
   function. On -C_0 it is F_E(-e^{i pi/4} q^T h^{-1} q).
4. **New positive result (proved at N = 2).** For every real spacelike k, in any direction (boosted
   included), the pointwise limit lim_{eps->0} <Tr e^{i k^mu A_mu}>_eps exists and equals
   F_E(e^{i pi/4} k.k). That is the value on the ray arg t = pi/4. The limit is Lorentz invariant although the
   regulator breaks boosts, and the same holds for any positive definite regulator matrix M. 054 gave real
   spacelike axis momenta only in smeared form; the pointwise statement and boosted directions are new.

**What this means for avenue 1.** The one place a non-Euclidean light-cone datum could enter this observable
class is now pinned: real timelike and null momenta. No linear contour reaches them. They require non-linear
contours (for example thimbles) or a direct analysis of the oscillatory integral. The light cone found here is
that of the eta put into S_b. **No signature is derived.** Problem E stays OPEN, CRITICAL PATH,
PROGRAMME-CONDITIONAL.

## Target and status

- **Problem E** (appH `sec:status-E`, L1482-1531, read in full).
  - Ledger label: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion:
    PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or
    matrix-derived Lorentzian signature."
  - Status paragraph: "Remains Assumption~\ref{ass:lorentzian}."
- **Chapter 17** (ch17 L394-399): "OPEN; CRITICAL PATH for the matrix-derived label." The criterion (L718-719)
  reads "Problem~E: Lorentzian signature is derived rather than retained (Assumption~\ref{ass:lorentzian})."
  The two sources agree, and there is no discrepancy.
- **Original target:** derive Lorentzian signature rather than retain ass:lorentzian (ch04 L321-328).
- **Current critical-path set** (ch17 criterion and appH): A, B, C, D1, E, F, G-derived, N. Unchanged.
- **Dependencies used:**
  - 053 block (appH L1495-1510): Definition (A), the contours R_u, the N = 2 identity Pf M = c_P (det G)^4,
    the Cauchy-Binet bound, and the flat-direction bound at k = 0.
  - 054 block (L1512-1527): F_E and its holomorphy on |arg t| < 3 pi/4, used in (iv).
- **Classification:** PROGRAMME-CONDITIONAL sharpening. A bounded no-go for one observable/contour class, plus a
  pointwise sub-lemma. No label change.

### Why this target

Of the ranked avenues in review 054-r2:

- **Avenue 1** (edge behaviour of F_E at arg t = -3 pi/4 and the pointwise real-timelike limit) asks first
  whether the edge is an artefact of the per-index contours. A contour class that crossed the edge would
  decide avenue 1 at once: real timelike k would become an interior point with a convergent representation.
  So avenue 2 is the necessary first step of avenue 1.
- **Avenue 2** (index-mixing contours) proved tractable in full generality for linear contours, by an exact
  reduction to diagonal phases.

The package settles avenue 2 for linear contours. It also returns a positive pointwise result, and it reduces
avenue 1 to a precisely stated residue: non-linear contours or direct oscillatory analysis at real causal k.
Avenue 3 (N -> infinity first), avenue 4 (OS positivity) and scout R2 stay queued. They are less tractable at
this point and would not change the conclusion of this class.

## Source reading

**Digest + targeted reads. Not a full scan.**

- `make_digest.py --check` printed DIGEST CURRENT, with dirty-chapters yes. That was the 054 integration, then
  uncommitted; the author has since committed it (HEAD f5222e1). The working appH is 540605 bytes, sha256 e67297cd...34d7, CRLF 3220, bare LF 0, which is the
  stated baseline. `git status --short` shows only this proposal folder (untracked), and `git diff --stat HEAD -- chapters bib` is empty, so the working appH equals HEAD's.
- Read in full:
  - appH L1482-1531: the Problem E section, the 053 and 054 blocks, the Status paragraph;
  - ch17 L388-401 and L712-724;
  - ch04 L316-334 (ass:lorentzian);
  - ch03 L138-150 (eq:Smatrix);
  - proposals/054-.../review-r2.md, the head of proposal-r2.md, and apply_check.py/.txt;
  - the 053 and 054 entries of reports/ledger.md;
  - MILESTONE.md.
- Searched: `\mathcal C` in appH. It is used locally in Problem D (commutant labels), so the insert uses
  `\mathfrak C`, which occurs nowhere in chapters/.
- No definition, assumption, scope or status passage is changed, so no full scan is due (CLAUDE.md 3(c)). The
  integration ordinal would be 53. Unreadable files: none.

## Research and reasoning

Conventions:
- eta = diag(-1,1,...,1), in the manuscript's order. Units 1/(4 g_YM^2) = 1 in the scripts only.
- At N = 2, A_mu = sum_a A_mu^a sigma^a/2. X is the real 10x3 matrix of the X_nu^a, with columns x^a in R^10.
- h(a,b) = a^T h b, a complex bilinear form.

### Step 0. The action on a linear contour (N = 2)

[A_mu, A_nu] = i (x_mu x x_nu).sigma/2 (colour cross product). With (u x v).(w x z) = (u.w)(v.z) - (u.z)(v.w):

    S_b = -(1/4g^2) Tr[A_mu,A_nu][A^mu,A^nu] = (1/8g^2)[(tr G)^2 - tr G^2] = sigma_2(G)/(4g^2),
    G_ab = eta^{mu nu} A_mu^a A_nu^b.

On A = Lambda X one has G = X^T h X, so

    sigma_2(G) = sum_{a<b} [h(x^a,x^a)h(x^b,x^b) - h(x^a,x^b)^2] = sum_{a<b} (Lambda^2 h)(x^a ∧ x^b, x^a ∧ x^b).

For h = delta this gives S_E = sigma_2(X^T X)/(4g^2), the manuscript's S_E. The Pfaffian is
c_P (det G)^4 (053, valid for all complex A).

**Equivalence with (P).**
- If (P) holds, compactness of the unit decomposable bivectors gives Im(Lambda^2 h)(omega,omega) >= c|omega|^2.
  With sigma_2(X^T X) = sum_{a<b} |x^a ∧ x^b|^2 this yields Re iS_b = -Im sigma_2(G)/4g^2 <= -c S_E.
- Conversely, take X with only two colour columns a, b. The inequality then gives (P).
- Cauchy-Binet gives |det(X^T h X)| <= C_h det(X^T X).

So for any bounded O the integrand is dominated by C (det X^TX)^4 e^{-c S_E}. This is integrable by 053's N = 2
bound at k = 0.

**N >= 3.** Embed X in a 2x2 block. S_b and S_E restrict to their su(2) forms, so Re iS_b <= -c S_E at N >= 3
implies (P). Hence C^(N) is contained in C.

### Step 1. Normal form (Lemma 1; exact, n = 10 >= 3)

(a) **No real isotropic vector.** Suppose h(a,a) = 0 with a real and nonzero. The hyperplane
{b : (Re h a).b = 0} has dimension 9 >= 2, so it contains some b not in Ra. For that b, h(a,b) = i (Im h a).b
is purely imaginary, and det_h(a,b) = -h(a,b)^2 is real, which contradicts (P).

(b) **Argument lift.**
- The map a ↦ h(a,a) sends S^9 continuously to C*. Since S^9 is simply connected, it lifts to a continuous
  argument alpha.
- h(-a,-a) = h(a,a), so alpha(-a) - alpha(a) = 2 pi m is constant. Applying this twice gives m = 0, so alpha is
  even.
- On a 2-plane with orthonormal basis (a', b'), the curve phi ↦ h(cos phi a' + sin phi b'), phi in [0, pi], is
  the ellipse m + A cos 2 phi + B sin 2 phi, traced once. It avoids 0 by (a). Its winding number about 0 is
  (alpha(-a') - alpha(a'))/2 pi = 0.
- A possibly degenerate ellipse that does not pass through 0 and has winding number 0 has 0 outside its convex
  hull. It therefore lies in an open half-plane through 0, and along it alpha varies by less than pi.
- Take the plane through a maximiser and a minimiser of alpha on S^9; if they are dependent, the range is 0.
  This gives max alpha - min alpha < pi.
- With theta the midpoint, Re(e^{-i theta} h(a,a)) > 0 for every real a != 0. So P = Re(e^{-i theta} h) is
  positive definite.

This is a Finsler/Brickman-type statement. The proof here is self-contained and no citation is needed.

(c) **Diagonalisation.** Write P = W^T W and W^{-T} Q W^{-1} = O^T diag(lambda) O, with
Q = Im(e^{-i theta} h). Then h = T^T diag(d) T, with T = O W and d_mu = e^{i theta}(1 + i lambda_mu).

(d) **The condition on d.** With a' = T a and b' = T b,

    det_h(a,b) = sum_{mu<nu} d_mu d_nu (a'_mu b'_nu - a'_nu b'_mu)^2.

So (P) is equivalent to Im(d_mu d_nu) > 0 for all mu != nu: necessity from a' = e_mu, b' = e_nu; sufficiency
because some term is nonzero.

(e) **One k for all pairs.**
- Take the arguments beta_mu in (theta - pi/2, theta + pi/2). Then each pair sum lies in
  (2 theta - pi, 2 theta + pi) and in one of the intervals (2k pi, (2k+1) pi).
- Suppose two pairs that share an index used different k. Then two of the beta would differ by more than pi,
  which is impossible.
- Two disjoint pairs are linked by a third pair that shares an index with each.
- So k is common to all pairs. Shifting by k pi gives h = (-1)^k T^T diag(|d| e^{i beta'}) T, with beta' in
  K_0 = {0 < beta_mu + beta_nu < pi for mu != nu}.
- Hence C = C_0 ∪ (-C_0).

### Step 2. The two classes (Lemma 2; exact)

**Eigenvalue counts.**
- For beta in K_0, at most one beta_mu lies outside (0, pi). Two non-positive ones would sum to <= 0. One
  >= pi forces all the others below 0.
- Likewise at most one beta_mu lies outside (-pi/2, pi/2).
- By Sylvester's law of inertia, on C_0 both Re h = T^T diag(|d| cos beta') T and Im h have at least 9
  positive eigenvalues. On -C_0 they have at least 9 negative ones.

**Disjoint closures on invertible h.**
- On the closures the inequalities become non-strict. A common limit point therefore has Re h and Im h each
  with at least 8 zero eigenvalues.
- The two kernels meet in dimension at least 6. A real a in that intersection has h a = 0, so h is singular.
- But h = Lambda^T eta Lambda is invertible. So the closures of C_0 and -C_0 contain no common invertible h.
- A connected path of invertible h in the closure of C therefore stays in the closure of one class.

**Position of the Hermitian contour.**
- R_u has h = diag(e^{i(pi - 3 pi u/4)}, e^{i pi u/4} x 9). Its pair sums are pi - pi u/2 and pi u/2, so R_u lies
  in C_0 exactly for 0 < u < 2 (lemma_checks E).
- So eta = h(R_0) is in the closure of C_0.
- eta is not in the closure of -C_0: there Re h would have at least 9 non-positive eigenvalues, while Re eta has
  one negative eigenvalue.

### Step 3. Momenta reached (exact; any N)

**When the mode is bounded.** Tr e^{i k.A} = 2 cos(sqrt(v.v)/2), with v = q^T X in C^3 and q = Lambda^T k.
- If q is real, the trace is bounded by 2.
- If Im q != 0, choose X with a single colour column s a and a ⊥ Re q, Im q . a = 1. Then v.v = -s^2 and the
  trace grows like cosh(s/2). (If Im q is parallel to Re q, then (q.a)^2 is non-real for generic a.)
- So the mode is bounded exactly when q is real.

**The value of k.k.** k.k = k^T eta k = q^T h^{-1} q = sum_mu q'_mu^2 / d_mu, with q' = T^{-T} q real.
- On C_0 this is a positive combination of the directions e^{-i beta'_mu}, which lie within pi/2 of -theta',
  where theta' = (beta'_max + beta'_min)/2 is in (0, pi/2).
- beta'_max - beta'_min < pi, using a third index.
- So arg(k.k) is in (-theta' - pi/2, -theta' + pi/2), a subset of (-pi, pi/2), and k.k != 0.
- The R_u give arg(k.k) = -pi + 3 pi u/4 for k along A_0, and -pi u/4 along A_j. They fill the sector.

### Step 4. Values at N = 2 (Theorem; proved at N = 2)

Define W(h,q) = ∫ dX (det X^T h X)^4 e^{i sigma_2(X^T h X)/4g^2} Tr e^{i q.X}.

**Properties of W.**
- W is holomorphic in h on C, by locally uniform domination (Step 0).
- W is even in h, since sigma_2 and (det)^4 are even.
- The substitution X = T Y gives W(h,q) = |det T|^3 W(T^T h T, T^T q) for real invertible T.

**W(.,0) on C_0.** Let f(d) = W(diag d, 0) on D_0 = {phases in K_0}, which is contractible.
- f satisfies f(diag(s^2 d)) = prod |s_mu|^{-3} f(d).
- Then g = f prod d_mu^{3/2} is holomorphic and invariant under positive real scalings of each d_mu. So
  d_mu ∂_mu g = 0 and g is constant.
- g ≠ 0, from its value at the Euclidean point e^{i pi/4} I, which is the Euclidean partition function times a
  phase.
- Hence W(h,0) ≠ 0 on C_0.

**The function U.**
- V(T^T D T, q) = V(D, T^{-T} q), and rescaling X_mu by s_mu = 1/q'_mu gives V(D, q') = U(w), with
  w_mu = q'_mu^2/d_mu.
- U is holomorphic on Ω = {w : the args of 1/w_mu can be chosen in K_0}. Ω is connected, being the image of
  R_+^10 x K_0.
- On w = e^{-i pi/4} x with x in R_+^10, rescaling gives the Euclidean contour with q = sqrt(x). SO(10)
  invariance then gives U = F_E(sum x).

**Identity theorem.**
- e^{-i pi/4} R_+^10 is open in the maximal totally real subspace e^{-i pi/4} R^10.
- U(w) - F_E(e^{i pi/4} sum w) is holomorphic on Ω. Here sum w lies in the sector of Step 3, where F_E is
  holomorphic by 054 (iv). The difference vanishes on that subset, so it vanishes on Ω.
- Zero components of q' follow by continuity in q (dominated convergence).

**Result.** V = F_E(e^{i pi/4} q^T h^{-1} q) on C_0. On -C_0, evenness gives F_E(-e^{i pi/4} q^T h^{-1} q).

### Step 5. Pointwise limits (proved at N = 2)

**Hypotheses on the path.** Lambda(tau) is continuous, with:
- Lambda(0) real;
- h(tau) in the closure of C, so that Re iS_b <= 0;
- Re Lambda^T Lambda > 0, so the regulator has positive real part;
- h(1) in C_0 and Lambda(1)^T k real.

**Argument.**
- At fixed eps the integrand is bounded on the swept region by poly e^{C|X| - eps c|X|^2}. Stokes' theorem
  moves I_eps from the Hermitian contour to Lambda(1), as for R_u.
- On Lambda(1) the regulator has modulus <= 1 and the integrand is dominated as in Step 0. Dominated
  convergence gives lim I_eps[O] = W(h(1), q) up to the constant det Lambda^3, and likewise for O = 1.
- The ratio is V(h(1), q) = F_E(e^{i pi/4} k.k).

**Construction for real spacelike k.**
- Take L in O(9,1) real with L^T k = kappa e_1.
- Phases: beta(tau) = (pi - 3 pi u tau/4, -pi u tau/8, pi u tau/4 x 8).
- D_half = diag(e^{i(beta_0 - pi)/2}, e^{i beta_i/2}).
- r is real in the (1,2) plane with r_1^2 e^{-i beta_1} + r_2^2 e^{-i beta_2} = 1. Explicitly
  r_2^2 = 1/(4 cos^2 a - 1) and r_1^2 = 2 cos a r_2^2, with a = pi u tau/8.
- S(tau) is complex Lorentz (S eta S^T = eta), with row 1 equal to s = D_half^{-1} r; s^T eta s = 1. The other
  rows come from eta-bilinear Gram-Schmidt.
- Lambda = L S D_half.

**Checks on the construction.**
- h = D_half S^T eta S D_half = diag(e^{i beta}), and Lambda^T k = kappa D_half s = kappa r is real.
- Pair sums at tau = 1 are pi - 7 pi u/8, pi - pi u/2, pi u/8 and pi u/2. So h(1) is in C_0 for 0 < u < 8/7,
  and h(tau) is in the closure of C_0 along the path.
- At tau = 0, Lambda(0) = L S_0 is real.
- As u -> 0 the path tends uniformly to L S_0, so Re Lambda^T Lambda -> S_0^T L^T L S_0 > 0. Hence some small u
  works.
- With a general positive definite M the same argument applies, with M in place of L^T L.
- path_check.txt: 40 random k with rapidities up to 2. All of conditions (a)-(d) hold. The admissible u
  decreases with rapidity, down to about 5e-4 at rapidity 2.

**Result.** For every real spacelike k, lim <Tr e^{ik.A}>_eps = F_E(e^{i pi/4} k.k). For a real spacelike axis
k = kappa delta_j, 054 gave F_E(e^{i pi/4} kappa^2) in smeared form only; the pointwise statement is new.

### Step 6. What remains on the gap (fork analysis)

The obstruction "real causal k not reached" depends on four hypotheses.

1. **Linearity of the contour.**
   - Relaxation: non-linear contours (Lefschetz thimbles of the oscillatory integrand, or contours adapted to
     the flat directions).
   - Status: OPEN. This is now the main residual of avenue 1.
2. **The closure-of-C path class.**
   - Relaxation: paths with Re iS_b <= 0 that leave the closure of C. Lemma 2 does not cover them.
   - Status: OPEN. They could only connect to -C_0, where the values are F_E(-e^{i pi/4} k.k); for real
     timelike k that would be F_E(e^{i pi/4}|k.k|).
3. **Order of limits (eps -> 0 first at fixed N).**
   - Relaxation: N -> infinity first (avenue 3).
   - Status: OPEN.
4. **Strict domination at the end contour.**
   - Relaxation: direct analysis of the conditionally convergent Lorentzian x_0 Fresnel integral at real
     timelike k.
   - Finding of this round: after exact x_0 integration, real timelike kappa produces the factor
     exp(i kappa^2 g^2 n^T M(x_s)^{-1} n / 4), with M = tr G_s - G_s. That factor is a pure phase on the
     Hermitian contour, and it grows like exp(c/m) under any rotation of the spatial matrices. So no
     contour-rotation argument exists at real timelike kappa. The existence of the limit there hinges on
     oscillation at the flat directions m -> 0.
   - Status: not completed. This is a heuristic power count (the leading flat region behaves like
     ∫ dL L^{-1} e^{i kappa^2 L/mu}), not a proof.

**Ranked open avenues:**
1. Non-linear (thimble) contours at real causal k, at N = 2.
2. Direct oscillatory analysis of the real-timelike limit at N = 2, in the reduced variables
   (gamma_a, x_0) of Step 6.4.
3. Paths leaving the closure of C.
4. N -> infinity first.
5. OS positivity (054 avenue 4).
6. Scout R2.

### Literature

No new citations. Lemma 1 is proved in full above. Related classical results (Finsler 1937; Calabi 1964;
Brickman 1961, on definite combinations and the convexity of the joint numerical range for n >= 3) are known.
They are not cited in the insert and not independently verified here.

## Claim classification

| Claim | Class |
|---|---|
| S_b = sigma_2(X^T h X)/4g^2 on linear contours; Re iS_b <= -c S_E iff (P) (N = 2); C^(N) ⊂ C | established |
| Lemma 1 (normal form, C = C_0 ∪ -C_0) | established (proof above; numerical check lemma_checks A, B) |
| Lemma 2 (classes, eta adjacent only to C_0, no common invertible limit) | established |
| Sector of k.k for bounded modes on C_0, at every N | established |
| R_u in C_0 iff 0 < u < 2 | established |
| V = F_E(e^{i pi/4} q^T h^{-1} q) on C_0 at N = 2 | established at N = 2 (uses 053's N = 2 bound and 054 (iv)); MC check |
| Pointwise eps -> 0 limit for real spacelike k at N = 2 | established at N = 2 (construction checked numerically) |
| (iv), (v) at N >= 3 | unresolved (would need the 053 extension to general h) |
| Real timelike/null k: existence and value of the limit; continuation of F_E across the edge | unresolved |
| Non-linear contours; paths leaving the closure of C | unresolved |
| Heuristic power count of Step 6.4 | conjecture/mechanism (not in the insert) |
| Any signature derivation | not claimed |

## Proposed changes

### chapters/appH-microscopic-proofs.tex

**Placement.**
- Insert the new paragraph `appH_insert.tex` immediately before the unique anchor at L1529:

      \paragraph{Status.}
      Remains Assumption~\ref{ass:lorentzian}.

- The insert is followed by one blank line. This places it after the 054 paragraph "Fourier observables of the
  regulated integral (conditional for N >= 3)", which ends "... and Problem~E keeps its ledger label."
- Nothing is replaced or removed.

**Anchor and insert data.**
- Anchor: 61 bytes, sha256 a7c774127bc7...26cc, count 1.
- Insert, LF form (proposal file): 9324 bytes, sha256 ca32f19296b2645a12936ce2732b1c9d092277badcfac16ca53c3710538de5b1.
- Insert, CRLF form: 9345 bytes, sha256 3b14cca7803034f3e295d297d560d1cb9becdaeab734127f79228a7f5948a945.
- Resulting appH: 549952 bytes, sha256 008db280ef2bebae769670a5b8ea498ab1cd6ae9539253b878e615beef83f1c5.
  It has CRLF 3242 and bare LF 0.
- These are produced by `apply_check.py` (report mode, baseline 540605 / e67297cd...34d7).

**Insert form.** ASCII, LF only, no trailing whitespace.
- Its only reference is `\ref{ass:lorentzian}` (defined once, ch04 L322).
- It has no labels and no citations, and no process language.
- `\mathfrak C` is new and local; `\mathcal G`, `\mathcal R_u`, `S_E`, `F_E` and "Definition (A)" are from the
  two preceding paragraphs.

**Stale passages elsewhere.**
- The 054 paragraph's caveat "about momenta off the coordinate axes, which combine matrices with different
  phases on R_u" stays correct as a statement about that paragraph. The new paragraph treats those momenta for
  linear contours and leaves the causal ones open, so no edit is needed.
- The 053 caveat on non-polynomial observables is likewise unchanged.
- No other file is affected.

The full LaTeX block is in `appH_insert.tex`. It is reproduced here:

```latex
\paragraph{Linear contours that mix the indices, and real spacelike momenta (proved at \(N=2\)).}
Keep Definition~(A), \(\gamma=0\) and the notation of the two preceding paragraphs, and take the contours \(A_\mu=\sum_\nu\Lambda_{\mu\nu}X_\nu\) with \(\Lambda\in\mathrm{GL}(10,\mathbb C)\) and \(X_\nu\) traceless Hermitian. They contain the \(\mathcal R_u\) and their images under complex Lorentz transformations. Put \(h=\Lambda^{\mathrm T}\eta\Lambda\) and write \(h(a,b)=a^{\mathrm T}hb\). At \(N=2\), with \(X_\nu=\sum_aX_\nu^a\sigma^a/2\) and \(x^a=(X_\nu^a)_\nu\in\mathbb R^{10}\), the matrix \(\mathcal G\) of the preceding paragraphs is \(\mathcal G_{ab}=h(x^a,x^b)\), and \(S_{\mathrm b}=\tfrac1{4g_{\mathrm{YM}}^2}\sum_{a<b}[h(x^a,x^a)h(x^b,x^b)-h(x^a,x^b)^2]\), which for \(h=\delta\) is \(S_{\mathrm E}\). Hence \(\operatorname{Re}\mathrm iS_{\mathrm b}\le-c\,S_{\mathrm E}(X)\) holds on the contour for some \(c>0\) exactly when \(h\) lies in the set \(\mathfrak C\) defined by
\[
\operatorname{Im}\bigl[h(a,a)h(b,b)-h(a,b)^2\bigr]>0\quad\text{for all linearly independent real }a,b,
\]
and then, by the Cauchy--Binet formula, the integrand at \(\epsilon=0\) times a bounded \(O\) is dominated as in the bound along the flat directions. For \(N\ge3\) the same inequality, applied to \(X\) in an \(\mathfrak{su}(2)\) block, implies \(h\in\mathfrak C\).

(i) \emph{Normal form.} Let \(h\in\mathfrak C\). Then \(h(a,a)\neq0\) for real \(a\neq0\), since otherwise a real \(b\notin\mathbb Ra\) with \(\operatorname{Re}h(a,b)=0\) exists, and for it the bracket is \(-h(a,b)^2\), which is real. As the unit sphere of \(\mathbb R^{10}\) is simply connected, \(\arg h(a,a)\) has a continuous branch on it, which is even. On the unit circle of each real 2-plane the values \(h(a,a)\) form an ellipse that avoids \(0\) and around which this branch winds zero times, so the ellipse lies in an open half-plane and the branch varies by less than \(\pi\) on the circle. The plane through a maximum and a minimum then shows that it varies by less than \(\pi\) on the sphere. So \(\operatorname{Re}(\mathrm e^{-\mathrm i\theta}h)\) is positive definite for some \(\theta\), and a simultaneous real diagonalisation gives \(h=T^{\mathrm T}\operatorname{diag}(d_\mu)T\) with \(T\) real and invertible. The condition defining \(\mathfrak C\) becomes \(\operatorname{Im}(d_\mu d_\nu)>0\) for \(\mu\neq\nu\), and with the arguments \(\beta_\mu\) of the \(d_\mu\) taken in \((\theta-\pi/2,\theta+\pi/2)\), all sums \(\beta_\mu+\beta_\nu\) lie in one interval \((2k\pi,(2k+1)\pi)\). So \(\mathfrak C=\mathfrak C_0\cup(-\mathfrak C_0)\), where \(\mathfrak C_0\) consists of the \(T^{\mathrm T}\operatorname{diag}(d_\mu)T\) whose arguments can be chosen with \(0<\beta_\mu+\beta_\nu<\pi\) for \(\mu\neq\nu\).

(ii) \emph{The class adjacent to the Hermitian contour.} On \(\mathfrak C_0\) at most one \(\beta_\mu\) lies outside \((-\pi/2,\pi/2)\) and at most one outside \((0,\pi)\). So \(\operatorname{Re}h\) and \(\operatorname{Im}h\) each have at least nine positive eigenvalues there, and at least nine negative ones on \(-\mathfrak C_0\). At a common limit point both would have kernels of dimension at least eight, so \(h\) would be singular. Since \(h=\Lambda^{\mathrm T}\eta\Lambda\) is invertible, a path of these contours whose \(h\) stays in the closure of \(\mathfrak C\) cannot pass from \(\mathfrak C_0\) to \(-\mathfrak C_0\). The Hermitian contour, \(h=\eta\), is the limit as \(u\to0\) of the \(\mathcal R_u\), which lie in \(\mathfrak C_0\) for \(0<u<2\). It is not a limit of points of \(-\mathfrak C_0\), since there \(\operatorname{Re}h\) has at least nine negative eigenvalues.

(iii) \emph{Momenta reached.} For \(k\in\mathbb C^{10}\), the observable \(\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\) is bounded on the contour exactly when \(q=\Lambda^{\mathrm T}k\) is real, and then \(k^\mu k_\mu=q^{\mathrm T}h^{-1}q=\sum_\mu(T^{-\mathrm T}q)_\mu^2/d_\mu\). For \(h\in\mathfrak C_0\) the directions \(\mathrm e^{-\mathrm i\beta_\mu}\) lie in an open half-plane, so \(k^\mu k_\mu\) lies in the sector \(-\pi<\arg(k^\mu k_\mu)<\pi/2\). This is the sector \(|\arg t|<3\pi/4\) for \(t=\mathrm e^{\mathrm i\pi/4}k^\mu k_\mu\), and the \(\mathcal R_u\) already reach every point of it. No contour of this class with \(h\in\mathfrak C_0\) therefore makes the Fourier mode bounded for \(k^\mu k_\mu\) outside the sector, in particular for real \(k\neq0\) with \(k^\mu k_\mu\le0\). By the inclusion above, this holds for every \(N\).

(iv) \emph{Values at \(N=2\).} For \(h\in\mathfrak C\) and real \(q\), let \(W(h,q)\) be the integral over real \(X\) of \((\det\mathcal G)^4\mathrm e^{\mathrm iS_{\mathrm b}}\operatorname{Tr}\mathrm e^{\mathrm iq^\nu X_\nu}\), and let \(V(h,q)=W(h,q)/W(h,0)\). Then \(W\) is holomorphic in \(h\), is even in \(h\), and satisfies \(W(h,q)=|\det T|^3W(T^{\mathrm T}hT,T^{\mathrm T}q)\) for real invertible \(T\). On \(\mathfrak C_0\) this gives \(W(T^{\mathrm T}\operatorname{diag}(d_\mu)T,0)=c\,|\det T|^{-3}\prod_\mu d_\mu^{-3/2}\) for a continuous branch, with \(c\neq0\), and \(V(T^{\mathrm T}\operatorname{diag}(d_\mu)T,q)=U(w)\) with \(w_\mu=(T^{-\mathrm T}q)_\mu^2/d_\mu\), where \(U\) is holomorphic on the connected set of \(w\) for which the arguments of the \(1/w_\mu\) can be chosen with pairwise sums in \((0,\pi)\); zero components of \(q\) follow by continuity. For \(w=\mathrm e^{-\mathrm i\pi/4}x\) with \(x\in(0,\infty)^{10}\) the contour is, after a real rescaling of the \(X_\nu\), the Euclidean one with \(q_\mu=\sqrt{x_\mu}\), and \(\mathrm{SO}(10)\) invariance gives \(U(w)=F_{\mathrm E}(\sum_\mu x_\mu)\). That set of \(w\) is open in a maximal totally real subspace, \(\sum_\mu w_\mu\) lies in the sector of (iii), and \(F_{\mathrm E}\) is holomorphic on \(|\arg t|<3\pi/4\) by the preceding paragraph, so the identity theorem gives
\[
V(h,q)=F_{\mathrm E}\bigl(\mathrm e^{\mathrm i\pi/4}q^{\mathrm T}h^{-1}q\bigr)\quad(h\in\mathfrak C_0),\qquad V(h,q)=F_{\mathrm E}\bigl(-\mathrm e^{\mathrm i\pi/4}q^{\mathrm T}h^{-1}q\bigr)\quad(h\in-\mathfrak C_0).
\]

(v) \emph{Pointwise limits at \(N=2\).} Let \(\Lambda(\tau)\), \(0\le\tau\le1\), be continuous, with \(\Lambda(0)\) real, \(h(\tau)\) in the closure of \(\mathfrak C\), \(\operatorname{Re}\Lambda(\tau)^{\mathrm T}\Lambda(\tau)\) positive definite, \(h(1)\in\mathfrak C_0\) and \(\Lambda(1)^{\mathrm T}k\) real. Stokes' theorem at fixed \(\epsilon\), as for the \(\mathcal R_u\), and dominated convergence on the last contour then give \(\lim_{\epsilon\to0^+}\langle\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\rangle_\epsilon=F_{\mathrm E}(\mathrm e^{\mathrm i\pi/4}k^\mu k_\mu)\). For real \(k\) with \(k^\mu k_\mu=\kappa^2>0\) such a path exists. Take a real Lorentz transformation \(L\) with \(L^{\mathrm T}k=(0,\kappa,0,\dots,0)\), phases \(\beta(\tau)=(\pi-3\pi u\tau/4,\,-\pi u\tau/8,\,\pi u\tau/4,\dots,\pi u\tau/4)\), which give \(h(\tau)\) in the closure of \(\mathfrak C_0\) and \(h(1)\in\mathfrak C_0\) for \(0<u<8/7\), and \(\Lambda(\tau)=LS(\tau)\operatorname{diag}(\mathrm e^{\mathrm i(\beta_0-\pi)/2},\mathrm e^{\mathrm i\beta_1/2},\dots,\mathrm e^{\mathrm i\beta_9/2})\). Here \(r\) is real in the \((1,2)\)-plane with \(r_1^2\mathrm e^{-\mathrm i\beta_1}+r_2^2\mathrm e^{-\mathrm i\beta_2}=1\), and \(S(\tau)\) is a complex Lorentz transformation, obtained by Gram--Schmidt for the bilinear form \(\eta\), whose row \(\mu=1\) has the entries \(r_\nu\) divided by the \(\nu\)-th diagonal entry; the condition on \(r\) gives this row \(\eta\)-norm \(1\). Then \(h(\tau)=\operatorname{diag}(\mathrm e^{\mathrm i\beta_\mu(\tau)})\) and \(\Lambda(\tau)^{\mathrm T}k=\kappa r\). As \(u\to0\) the path tends uniformly to a real matrix, so \(\operatorname{Re}\Lambda^{\mathrm T}\Lambda\) stays positive definite for small \(u\). Hence for every real spacelike \(k\), in any direction, the pointwise limit exists and equals \(F_{\mathrm E}(\mathrm e^{\mathrm i\pi/4}k^\mu k_\mu)\), a value on the ray \(\arg t=\pi/4\) inside the sector. It depends only on \(k^\mu k_\mu\), although the regulator breaks the boosts, and the same holds with any positive definite \(M\) in place of the regulator.

For linear contours, this order of limits and \(\gamma=0\), the contour integrals with bounded Fourier modes are therefore at \(N=2\) values of \(F_{\mathrm E}\) at \(\mathrm e^{\mathrm i\pi/4}k^\mu k_\mu\) inside the sector, they are the pointwise limits of the regulated integral wherever a path as in (v) exists, which includes every real spacelike \(k\), and the real momenta that no contour with \(h\in\mathfrak C_0\) reaches are exactly the nonzero causal ones, \(k^\mu k_\mu\le0\). This is no statement about non-linear contours, about whether \(F_{\mathrm E}\) continues beyond \(\arg t=-3\pi/4\), about the pointwise limit at real timelike or null \(k\), about paths along which \(\operatorname{Re}\mathrm iS_{\mathrm b}\le0\) but \(h\) leaves the closure of \(\mathfrak C\), about (iv) and (v) for \(N\ge3\), about \(N\to\infty\) taken first, or about \(\gamma\neq0\) and Definitions~(B) and~(C). The light cone found here is the one of \(\eta\) in \(S_{\mathrm b}\), so no signature is derived, Assumption~\ref{ass:lorentzian} is not discharged, and Problem~E keeps its ledger label.
```

## Verification scripts

All are in `proposals/055-index-mixing-contours/`, with outputs in `.txt`.

**`lemma_checks.py` → `lemma_checks.txt`** (about 10 min).
- A: 30 normal-form samples, each checked in both classes:
  - (P) by direct minimisation;
  - the midpoint of the θ-arc in (0, pi/2) for C_0 and in (pi, 3 pi/2) for -C_0;
  - the arguments of q^T h^{-1} q for 4000 random real q in each sample lie in the predicted sector.
- B: 200 general complex symmetric h near e^{i pi/4} I and near eta.
  - (P) is decided by minimisation and, independently, by Lemma 1's normal form.
  - The two decisions agree in 200 of 200; (P) holds in 53, all in C_0, and all with cone args in the sector.
- C: adversarial penalty search. In all 8 starts the optimiser left (P), so the search yielded no admissible
  counter-candidate. It is uninformative and is reported as such.
- D: an n = 2 example where (P) holds but q^T h^{-1} q = -1.20 + 1.41 i. This shows that n >= 3 is used.
- E: R_u lies in C_0 exactly for 0 < u < 2.
- F: 400 perturbations of R_u near eta that satisfy (P). All are in C_0, and Re h has exactly one negative
  eigenvalue.

**`path_check.py` → `path_check.txt`.** The Step 5 construction for 40 random real spacelike k, with
rapidities 0 to 2. On 401 τ points:
- h(τ) = diag(e^{i beta(τ)}) to 1e-12;
- min eig Re Λ^TΛ > 0;
- |Im q|/|q| < 1e-16;
- q^T h^{-1} q = k.k to 1e-13;
- Λ(0) real.

**`mc_check.py` → `mc_check.txt`.** Importance-sampled Monte Carlo at N = 2.
- Setup:
  - 8e5 samples;
  - the Gram eigenvalues are sampled by Metropolis, and the Stiefel frames are Haar.
- Checks:
  - Each contour has distinct per-index phases and a generic real q, and is compared with a single-axis
    contour with the same z = q^T h^{-1} q.
  - Agreement is within 0.1-0.8 sigma, for example 1.7783 - 0.0271i against 1.7787 - 0.0272i.
  - A control at the same |q|^2 with averaged phases differs by 7-30 sigma, so the test discriminates.
  - An O^T D O row and a Euclidean row are included.
- This is a check, not a proof.

**`apply_check.py` → `apply_check.txt`.** Baseline, anchor uniqueness, insert form and the hashes above. Given a
path outside the repository, it writes the would-be appH there.

**Scratch build** (outside the repository, `<scratchpad>/build055`).
- The patched appH was produced by apply_check.
- The scratch copy could not be deleted afterwards: the `rm -rf` of the scratchpad directory was denied, and it was left in place, not worked around.
- Two pdflatex passes: exit 0, 361 pages (baseline after 054: 359), 0 undefined references or citations, 0 multiply defined labels.

## Decisions Taken

1. **Target: avenue 2 rather than avenue 1 directly.** A contour class crossing the edge would have decided
   avenue 1. Avenue 2 is therefore the first step of avenue 1, and it was tractable in full generality for
   linear contours.
   - Rejected: a numerical attack on the edge via R_u with u -> 0. The damping vanishes there (|J| <=
     2 sin(4 arg kappa/3)^{-27/2}), and the result would be inconclusive.
2. **Class of paths: the closure of C.** This is the class in which Lemma 2 is proved. Paths with
   Re iS_b <= 0 outside the closure are stated as not covered.
3. **Notation: `\mathfrak C`, not `\mathcal C`.** This avoids a clash with Problem D's local `\mathcal C`.
4. **The positive spacelike result goes into the same paragraph.** It shares the derivation (Steps 4-5).
5. **The heuristic flat-direction power count stays out of the insert.** It is not a proof.

## Milestone assessment

**M2: a new bounded no-go.** It rules out the route "enlarge the analyticity sector or reach real causal
momenta by index-mixing or complex-Lorentz linear contours". The manuscript kept that route open (054 caveat on
off-axis momenta; review-r2 avenue 2).

- It also contains a positive sub-lemma: the pointwise real-spacelike limit, Lorentz invariant.
- It is not M1 or a BREAKTHROUGH: no step of a signature derivation is made, and eta is an input.
- It is not M3: no merged claim is found wrong.
- It is not M4 or M5.

## Status-label recommendation

- **Current critical-path set** (ch17 criterion and appH): A, B, C, D1, E, F, G-derived, N.
- **Affected label:** Problem E only. It stays OPEN; CRITICAL PATH for the matrix-derived label;
  PROGRAMME-CONDITIONAL.
- No change is proposed.

## Author decision needed

None.

For the author's information: the result sharpens the 053 ledger note (a), "what 'Lorentzian signature
derived' means when eta sits in the action". In this class the integral's light cone is exactly the light cone
of the eta put into S_b.

## Remaining open step

To close Problem E, Lorentzian signature must be derived from the matrix theory rather than retained. Within
this line, the next steps on the gap are:
- (a) the regulated integral at real timelike and null k at N = 2, via non-linear contours or a direct
  oscillatory analysis;
- (b) whether F_E continues across arg t = -3 pi/4;
- (c) paths leaving the closure of C;
- (d) N >= 3 for (iv) and (v), which needs 053's flat-direction bound for general h;
- (e) N -> infinity first;
- (f) gamma != 0 and Definitions (B) and (C).

Even a full answer to (a) would concern an eta that is put in by hand. A signature derivation needs a mechanism
selecting eta, for example from a Euclidean or signature-agnostic model, which this line does not supply.

## Special instructions for the gatekeeper

**Re-derive:**
- Step 0: sigma_2 as a sum over colour pairs, and the equivalence with (P).
- Lemma 1:
  - (a), which needs n >= 3; D shows that n = 2 fails;
  - (b), the even lift and the winding-zero ellipse;
  - (e), the common k.
- Lemma 2: the inertia counts and the kernel intersection of dimension >= 6.
- Step 3: the sector.
- Step 4: the scaling argument for W(.,0), and the identity theorem on e^{-i pi/4} R_+^10.
- Step 5: the construction, in particular s^T eta s = 1, h = diag(e^{i beta}) and Lambda(0) real.

**Must not be asserted:**
- any signature derivation;
- statements about real timelike or null k;
- continuation of F_E across the edge;
- non-linear contours;
- (iv)/(v) at N >= 3.

**Check:** the paragraph's caveat list matches the claim classification. The heading "(proved at N = 2)" covers
(iv) and (v); (i)-(iii) are exact at the level of h, with (iii) stated for every N.
