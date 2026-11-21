# Proposal 079-g-frameavg-residual, round 1

## Result

Within the dominant-representation hypotheses of the integrated Problem G block of
`chapters/appH-microscopic-proofs.tex` (the frame-average paragraph L3165, the
stacked-rows paragraph L3163 it extends, and the row-perturbation paragraph behind
them), the following is proved with explicit constants:

**Theorem (frame-free residual bound).** Let M = M1 + M2, depths q1, q2, rows
(l1^{q1}, l2^{q2}) with l1 >= l2 >= 0, and let Δ_q(M1,M2,q1,q2,l1,l2) be the log of the
exact stacked multiplicative defect (content factors times hook ratios, the L3163
functional), and T_q = q1·I(M,M1,l1) + q2·I(M,M2,l2) its continuum target, where
I(A,B,ℓ) = (A+ℓ)log(A+ℓ) − A log A − (B+ℓ)log(B+ℓ) + B log B. Under the guards
M1 − q1 ≥ 1, M2 − q2 ≥ 1, M − q1 − q2 + 1 ≥ 1,

|Δ_q − T_q| ≤ B_q := Σ_{f=1,2} Σ_{r=1}^{q_f} |log(A_{f,r}/B_{f,r})|
              + l1 Σ_{r=1}^{q1} [(r−1)/(M−r+1) + (r−1)/(M1−r+1)]
              + l2 Σ_{r=1}^{q2} [(q1+r−1)/(M−q1−r+1) + (r−1)/(M2−r+1)]
              + q1 q2 log(l1 + q1 + q2),

with A_{1,r} = M−r+1, B_{1,r} = M1−r+1, A_{2,r} = M−q1−r+1, B_{2,r} = M2−r+1.

**Corollary (frame-uniformity).** B_q depends on the rows only through l_f and on the
ranks; it contains no other frame datum. The stacked fixed-frame defect of the
frame-average paragraph depends on the frame only through the saddle row lengths
(the paragraph's exact closed form, s²(n) = ¼ M(N−M)(tr B − nᵀB n)), and row lengths
of valid diagrams never exceed the total rank, so l_f ≤ N. Hence for every frame,
|Δ_q − T_q| ≤ q1 q2 log(N + q1 + q2) + C(M1/M2, q1, q2), and the residual per N tends
to 0 uniformly over frames. This upgrades the frame-average paragraph's clause that the
residual bound was "verified numerically on frames with N up to 3200" (shipped: at most
7.7 two-row, 59.8 at depth three) to a theorem with explicit constants in the stated
class, and establishes the uniform-in-N residual bound of the row-perturbation
paragraph and its stacked extension (previously numerical, of order q log(l1+1)).

Machine-checked (s1, s2): Lemma R in exact integer arithmetic (210 checks); hook
telescoping in exact rational arithmetic (77 checks); the multiplicative defect
identity against the Weyl hook-content dimension ratio in exact rational arithmetic
(70 guarded small-case checks); the chain inequality |Δ_q − T_q| ≤ B_q on 1560 small
cases (worst residual/bound 0.6652); the two-row closed form against the integrated
selection-independence paragraph's displayed expression (0 failures); a 150-frame scan
at N ∈ {400,1600,3200} (worst residuals 5.167/6.411/7.102 two-row and 37.552/48.669/
54.874 at depth three, always below the frame-free bounds 6.539–9.006 and 56.491–
80.211; at the shipped round frame N=3200, bounds 8.772 and 77.037 vs shipped 7.7 and
59.8); the bound takes literally one value over all frames at fixed rows (scan 2).

**What is not claimed.** Nothing is closed (rule 3). The problem's live missing step —
"derivation of the infrared entropy density and stationarity from the matrix theory is
OPEN" (appH L3036-3040) — is untouched, as are diagram selection, the monotonicity
statement, the minimisation over frames, and two-sided diagrams. The bound constants
are not optimised. The scan quantities are defect functionals of the class, not the
entropy itself. This is proof-level within-class evidence: PROGRAMME-CONDITIONAL
contribution, not a DERIVED closure.

## Target and status

- Problem G (HBEV), appH ledger (live, L3025-3029): "Status: OPEN. Priority: CRITICAL
  PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and
  G-external support at most a scope-limited model; G remains OPEN and neither
  satisfies the matrix-derived criterion." Status paragraph (L3036-3040): mechanism
  CLOSED CONDITIONALLY under the stated boundary entropy; infrared entropy density and
  stationarity from the matrix theory OPEN.
- Frontier row `G.frameavg-residual` (`reports/graph/frontier.yaml` L224-245): missing
  input = "the PROOF of frame-uniformity of the residual bound - 075 establishes the
  frame-uniform residual bound NUMERICALLY only"; prior art 075 ACCEPT; ranked first in
  `proposals/075-g-edge-frameavg/review-r2.md` ("proved frame-uniform residual bound").
- Ch17 criterion: read ch17-agenda.tex L474-495 (Problem G criterion; completion
  levels). This package advances the G-derived sub-line within the integrated
  edge-data block; it closes nothing.

## Source reading

digest + targeted reads. `scratch/digest.md`: DIGEST CURRENT (head d8b29f8fb1c7, appH
be3dbddd9156). Read in full: appH L3010-3048 (G ledger + Status + bounded-obstruction
paragraph head) and L3130-3179 (the integrated G paragraph block 072-078 + Vacuum
anchor); ch17-agenda.tex L474-495; frontier.yaml L224-245;
proposals/075-g-edge-frameavg/review-r2.md; reports/ledger.md L1090-1107;
reports/sme-scout-20261117-1309.md. No unreadable files. No full scan (no definition,
assumption, scope or status passage is changed; the insert is a new conditional
evidence paragraph).

## Research and reasoning

**1. Exact stacked defect.** For the two-stack diagram λ = (l1^{q1}, l2^{q2}) of U(M),
M = M1 + M2, the ratio dim_{U(M)}(λ) / [dim_{U(M1)}(l1^{q1}) dim_{U(M2)}(l2^{q2})]
equals, exactly, the product of: content factors Π_{r=1}^{q1} Π_{c=1}^{l1}
(M+c−r)/(M1+c−r) on stack 1; Π_{r=1}^{q2} Π_{c=1}^{l2} (M−q1+c−r)/(M2+c−r) on stack 2;
and hook ratios Π_{r=1}^{q1} Π_{c=1}^{l2} (l1−c+q1−r+1)/(l1−c+q1+q2−r+1) on the first
l2 columns of stack 1's rows. This is the functional displayed in the integrated
stacked-rows paragraph (L3163). *Established identity*: derived from the Weyl
hook-content formula dim(λ) = Π_{boxes} (M+c−r)/h(r,c) with h(r,c) =
(l_r − c) + (l'_c − r) + 1 — content factors cancel as written and hooks cancel except
on the overlap block, where l'_c jumps from q1+q2 to q1 for c ≤ l2. s1 re-verifies the
full identity as exact Fraction equality against a from-scratch hook-content dimension
on a guarded small grid (M1,M2 ∈ {2,3,5}, q ∈ {1,2,3}, all valid (l1,l2)); 70 checks,
0 failures. The guard (small cases only) is conservative: the symbolic cancellation is
general, but only small cases are machine-verified, and the insert text says so.

**2. Continuum target.** For each stack, sum over the row of the content-factor logs.
With S(A,B,ℓ) = Σ_{c=1}^{ℓ} log((A+c)/(B+c)) and I(A,B,ℓ) = ∫_0^ℓ log((A+y)/(B+y))dy
(closed form above), the target is T_q = Σ_f q_f I(M,M_f,l_f). Substituting M =
N m_tot, M_f = N m_f, l_f = N u_f: the N log N terms cancel identically in
I(N m_tot, N m_f, N u) (coefficient m_tot − m_tot − (m_f+u)+... = 0), giving
I = N[(m_tot+u)log(m_tot+u) − m_tot log m_tot − (m_f+u)log(m_f+u) + m_f log m_f] =
N[G(m_tot,u) − G(m_f,u)], G(m,u) = (m+u)log(m+u) − m log m (the −u log u term of the
integrated form cancels in the difference). So T_q is exactly the continuum stacked-rows
functional of the integrated paragraph; no asymptotic step is hidden. *Established
identity.*

**3. Lemma R (bracketing).** f(y) = log((A+y)/(B+y)) is monotone (decreasing iff A>B,
since f' = 1/(A+y) − 1/(B+y)). For A>B, ∫_1^{ℓ+1} f ≤ Σ_{c=1}^{ℓ} f(c) ≤ ∫_0^ℓ f gives
|I − S| ≤ f(0) − f(ℓ) ≤ f(0) = log(A/B); the case A<B follows from antisymmetry of I
and S under swap. General A,B ≥ 1: |I−S| ≤ |log(A/B)|. *Established derivation*;
additionally checked EXACTLY (no floats) by integer exponentiation of both sides of
exp(I−S) ∈ [min(A/B,B/A), max(A/B,B/A)] on 210 tuples.

**4. Shift bound.** ∂_A I = log((A+ℓ)/A) = log(1+ℓ/A), decreasing in A, 0 ≤ ∂_A I ≤
ℓ/A; ∂_B I = −log(1+ℓ/B), |∂_B I| ≤ ℓ/B. Along the rectangle from (A,B) to
(A−a, B−b): |I(A−a,B−b,ℓ) − I(A,B,ℓ)| ≤ a·ℓ/(A−a) + b·ℓ/(B−b) (sup of each partial on
the shifted interval). Apply with (A,B) = (M,M1), a = b = r−1 (stack 1 row r) and
(A,B) = (M,M2), a = q1+r−1, b = r−1 (stack 2 row r); guards keep A−a ≥ 1, B−b ≥ 1.
*Established derivation.* (Earlier draft had heuristic shift terms; replaced — see
manifest lineage note 2.)

**5. Lemma H (hook telescoping).** ∏_{x=0}^{ℓ−1}(x+a)/(x+a+q2) = ∏_{i=0}^{q2−1}
(a+i)/(ℓ+a+i) (exact telescoping of consecutive factors). Applied with x0 = l1−l2
re-indexed, a = l1−l2+q1−r+1 ≥ 1: the stack-1 hook block product for row r telescopes,
and its total log-magnitude is ≤ q2 log(ℓ+a+q2−1) = q2 log(l1+q1+q2−r) ≤ q2
log(l1+q1+q2); summing r = 1..q1 gives q1 q2 log(l1+q1+q2). *Established derivation*;
s1 checks both the draft form (a = 2q−r+1) and the general (a,q2) form as exact
Fractions on 77 tuples, and the bound numerically on the same tuples.

**6. Chain theorem.** Decompose per row-sum: |Δ_q − T_q| ≤ Σ_r |S(A_{f,r},B_{f,r},l_f)
− I(M,M_f,l_f)| + hook term, and each summand ≤ |log(A_{f,r}/B_{f,r})| (Lemma R,
A_{f,r}B_{f,r} ≥ 1 by the guards) + shift term (item 4). Triangle inequality gives the
theorem. *Established derivation* (guards: M−r+1 ≥ M−q1+1 ≥ q2+2 ≥ 3 > 0 etc.;
denominators M−q1−r+1 ≥ M−q1−q2+1 ≥ 1, M1−r+1 ≥ M1−q1+1 ≥ 2, M2−r+1 ≥ 2). s1 checks
the full chain on 1560 guarded small tuples against the exact product functional
(floats only in the log accumulation; margins O(1), worst ratio 0.6652).

**7. Frame-uniformity corollary.** The frame-average paragraph's exact closed form
shows the saddle defect depends on the frame B only through the row lengths l_f(B)
(via s_f(n) = ½√(M_f(N−M_f)(tr B − nᵀBn)) and the saddle rule l_f = t·s_f, t the
saddle parameter of the class). B_q(M1,M2,q,l1,l2) involves no other frame datum, and
rows of valid diagrams satisfy l_f ≤ N (class hypothesis, as in 072/073/075).
Substituting l_f ≤ N: B_q ≤ q1q2 log(N+q1+q2) + C(M1/M2, q1, q2) uniformly;
B_q/N → 0 uniformly over frames. *Conditional result* (conditional exactly on the
class hypotheses; the uniformity statement itself is derived within the class).
The scan then confirms at scale: scan 1 (150 frames: identity + 149 random
tr-B=3 PD Grams, rng.seed(79)), scan 2 (bound at fixed rows: one distinct value over
all frames), scan 3 (saddle-parameter sweep t ∈ {0.25,0.5,1,2}, residual and bound
grow together, bound always dominates).

**8. Relation to shipped text.** L3165 clause "verified numerically ... at most 7.7
... 59.8" (numerical) is now a theorem-with-constants in the class; the scan at the
shipped round frame reproduces the residual scale (7.102, 54.874) and the bound
dominates (8.772, 77.037). 072/073's uniform-in-N residual bound, stated there with a
numerical constant of order q log(l1+1), acquires explicit constants.

**9. Literature.** The sme-scout report (`reports/sme-scout-20261117-1309.md`, Edge-2)
routes Meckes-Meckes / Guntuboyina-Leeb-type concentration statements to this problem.
They were weighed and NOT used: the defect here is an exact product functional, so an
elementary exact route (Riemann bracketing + telescoping) gives an explicit-constant
theorem without concentration theory. No external result is imported. Classification
of those routes: *not used, not independently verified*.

## Claim classification

| claim | class |
|---|---|
| multiplicative defect identity (content × hooks), small guarded cases vs Weyl dimensions | established identity (machine-exact); general symbolic cancellation argued, not machine-checked beyond the guard |
| Lemma R | established derivation + exact-integer verification |
| shift bound (mean value on I) | established derivation |
| Lemma H telescoping + hook log-bound | established derivation + exact-Fraction verification |
| chain theorem \|Δ_q − T_q\| ≤ B_q | established derivation; verified on 1560 small cases |
| I = N[G(m_tot,u)−G(m_f,u)] identification | established identity |
| frame-uniformity corollary | conditional result (on the class hypotheses: saddle rows, rows ≤ N, defect frame-dependence through rows only) |
| residual/N → 0 uniformly in frames, class | conditional result (consequence of corollary) |
| 150-frame scan, t-sweep, bound-frame-independence at fixed rows | numerical verification (seeded, reproducible) |
| bound constants optimal / extension beyond class / any entropy or selection statement | unresolved — not claimed |

## Proposed changes

One file, one passage: `chapters/appH-microscopic-proofs.tex`. Insert the single
paragraph `insert-r1.tex`, blank-separated, immediately before the unique line-start
anchor

    \emph{Vacuum term.} The abstract of~\cite{Steinacker2023

(verified unique at 1-based L3173, immediately after the integrated block's last
paragraph at L3171 and before L3173; the block's closing structure is unchanged).
All existing text is kept; nothing is replaced. No `\ref`/`\label`/`\cite` is added, so
no label verification is needed. Stale passages elsewhere: the 075 clause "verified
numerically ... with N up to 3200" remains accurate (it was numerical then); the new
paragraph records the upgrade in its own scope. No other file changes.

The insert is one content line + terminal CRLF, 3,157 B, sha256
709f64f3149d73f656f9ac6fa7eccf2a227394a7311cb246933abcc25f065a11, ASCII, zero-cite
(no $, [, ], \cite, \ref, \label, \eqref), exactly one `\emph{}`, one scoped closing
status sentence ("... they close nothing in Problem~G."). Full text is in
`insert-r1.tex`.

## Verification scripts

All in this folder; run from repo root. Reproduction pack (invariants, exact):

1. `python -I proposals/079-g-frameavg-residual/s1_exact_lemma.py` → final line
   `PASS s1`, with exactly: `Lemma R: 210 exact integer checks, 0 failures`;
   `Lemma H: 77 exact Fraction checks, 0 failures`;
   `multiplicative defect identity: 70 exact Fraction checks, 0 failures`;
   `chain cross-check: 1560 cases, 0 failures, worst |residual|/bound = 0.6652`;
   `two-row closed-form match: 0 failures`.
2. `python -I proposals/079-g-frameavg-residual/s2_frame_uniform_check.py` → final
   line `PASS s2`, with `N=3200 q=(1,1) ... worst residual= 7.102 bound in
   [8.609, 9.006]`, `N=3200 q=(3,3) ... 54.874 ... [74.830, 80.211]`,
   `distinct depth-3 bound values over 150 frames: 1 (expected 1)`, and the check line
   `rows=(1131,1131) two-row bound=8.772 (vs shipped 7.7) depth-3 bound=77.037 (vs
   shipped 59.8) this-scan two-row residual=7.102`. Determinism: rng.seed(79) printed.
3. `python -I proposals/079-g-frameavg-residual/simulate_apply_079.py` → final line
   `PASS simulate_apply`, `PRE bytes 716985 sha256 be3dbddd...b2e`,
   `POST bytes 720144 sha256 a10eca51...12f`, `anchor line POST (1-based): 3175
   (PRE 3173)`, `no write performed on chapters/appH-microscopic-proofs.tex`.

Scripts: s1 = exact lemmas + chain; s2 = frame scan + shipped-number cross-check;
simulate_apply = in-memory byte contract + insert hygiene. Saved `.out` files in this
folder; hashes in `manifest.md`.

## Decisions Taken

- **Elementary exact route over SME concentration routes** (Meckes-Meckes /
  Guntuboyina-Leeb): the defect is an exact product functional, so explicit-constant
  bracketing/telescoping beats importing concentration theory that would need new
  verified hypotheses. Rejected alternative: measure-concentration proof of
  uniformity — would add unverified external inputs (rule 7 risk) and constants would
  be non-explicit.
- **Adopted + repaired the dead draft** of s1 (M1 = M−3 asymmetric grid kept; WIP
  lines deleted; check strengthened to the stacked functional). No `.out` existed at
  repair time — lineage in manifest.md.
- **Replaced the heuristic shift terms with the mean-value-correct terms** after a
  documentation-vs-code audit found the former unprovable for general depths (e.g.
  q1 large, r=1 stack-2 term); regenerated all `.out`s and the two quoted insert
  numbers (10.9→8.8, 79.2→77.0) before any freeze. Disclosed in manifest.md lineage 2.
- **Referenced the three source paragraphs descriptively** ("frame-average",
  "stacked-rows", "row-perturbation") instead of relative counts, which are wrong
  post-076/077/078 insertions; verified the headers are unique in the block.
- **Kept the identity check conservatively guarded** (small valid-diagram cases only)
  rather than asserting the general case from the check; text says "small cases".
- **Declared scan quantities as defect functionals, not entropies** (rule 6), to
  avoid any inference from the scan to physical entropy.

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step is closed; G's missing step
(infrared entropy density + stationarity from the matrix theory) is untouched. This is
a within-class proof-level sub-lemma closing the 075 review's first-ranked missing
input (the PROOF of frame-uniformity) at the defect-functional level.

## Status-label recommendation

Re-derived from the live agenda (ch17 L474-495) and ledger: current critical-path set
at the full-GR / matrix-derived scope: A, B, C, D1, E, F, G-derived, N. Affected
labels: **none** — Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; the
frontier input is satisfied but that is not a manuscript label.

## Author decision needed

none

## Remaining open step

To reach the original Problem G target: (1) derivation of the infrared entropy density
and stationarity from the matrix theory (appH L3036-3040); (2) selection of the
dominant diagram from the moment problem; (3) the monotonicity statement and the
minimisation over frames as a derived two-sided bound; (4) extension to two-sided
diagrams and to the full conjugacy-class average with the 2408.05274 saddle template;
(5) uniform-in-γ positive lower bound; (6) 065 selection-rule transplant. Within the
defect-functional line itself: optimise the constants of B_q and drop the guard
M−q1−q2+1 ≥ 1 by refined hook bookkeeping if needed for larger depths (not needed for
fixed depths as N → ∞).

## Special instructions for the gatekeeper

- Scope limits: do not read the theorem as an entropy, selection, or frame-minimisation
  statement; it is about the defect functional of the three named paragraphs.
- Re-derive Lemma R, the shift bound, the Lemma H telescoping, and the I ↔ N[G−G]
  identification yourself (short proofs above; s1 is exact-arithmetic support, not the
  proof).
- Check the identity-guard wording ("small cases") is preserved in the insert, and
  that the insert's "row lengths of valid diagrams never exceed the total rank" is
  read as the class hypothesis inherited from 072/073/075, not as a new claim.
- Re-check the shipped-number clause: insert quotes 7.7/59.8 (L3165) and scan numbers
  7.1/54.9 vs 8.8/77.0 — verify against `s2_frame_uniform_check.out`, not from memory.
- The 075 paragraph's numerical sentence stays; the insert adds, not replaces.
- Confirm anchor uniqueness line-start L3173 and byte contract against the live tree at
  integration time (078 chain's integrations could have moved it since this run;
  `simulate_apply.out` reflects the tree at this run: 716,985 B PRE).
