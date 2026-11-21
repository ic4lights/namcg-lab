# Proposal 083-g-moments-aoddsector, round 1

## Result

The Gaussian-averaged odd-sector charge moments of the rank-one edge block are
computed exactly, to all orders, inside the named Gaussian state class of the
charge-to-edge moment paragraph (appH "Charge-to-edge moment identification in
the Gaussian rank-one class."), with the leading-order convention of that
paragraph relaxed to a Gaussian Im(alpha) of mean a-bar and variance V,
independent of the slot radii, and with the exponential slots optionally
displaced by nonnegative shifts c_i. Four statements:

1. Master averaged map (all orders). For every integer m >= 1,
   <Tr Q^m> = (-1)^m 2^(m+1) sum_{k<=m/2} C(m,2k) sum_{j=0}^k C(k,j)
   A_{m-2k+2j} H_{k-j}, where A_n = E[(Im alpha)^n] are noncentred normal
   moments and H_n = <r^n> is any slot-law moment sequence. Verified
   symbolically against the exact all-order trace polynomial of the block for
   m = 1..9 (s2d), the trace polynomial itself verified for m = 1..14 against
   direct 2x2 matrix powers (s1).
2. Centred exact vanishing. If a-bar = 0 then every odd averaged moment
   vanishes identically, for every variance V and every slot law (central or
   shifted) independent of Im(alpha). So the pointwise odd-sector vanishing in
   the moment paragraph is a symmetry statement about the model, not a
   consequence of neglecting Im(alpha); no odd-moment truncation is needed at
   any order.
3. Noncentred odd sector. For odd m = 2p+1 the averaged moment is an odd
   polynomial in a-bar with leading term <Tr Q> = -4 a-bar (exact); the closed
   forms for p = 0,1,2 are printed by s2d Part F. The odd sector is governed
   by the state-level mean shift, not by the slot noncentrality: the slot
   shifts c_i never by themselves produce odd charge moments while slots stay
   independent of Im(alpha) (s3b Part 5).
4. Noncentred slot law. For shifted exponential slots the moment kernel of
   H_n = <r^n> is prod_i (1 - s^2 g_i t)^(-1) exp(c_i s^2 g_i t /
   (1 - s^2 g_i t)); H_n equals n! h_n(s^2 g) at c = 0 and obeys the exact
   set-partition (Bell) identity with cumulants kappa_k =
   (k-1)! s^(2k) sum_i g_i^k (1 + k c_i) (s3b, Parts 1-2, plus two independent
   probabilistic cross-checks at D = 1, Parts 3-4). This is the rank-one
   specialization of the real-graph presentation calculus of Kuriki-Numata
   (see References below), whose published bookkeeping was NOT pasted: the
   NAMCG combinatorics were rebuilt from first principles and the kernel
   re-derived from the slot MGF.
At a-bar = 0, V = 0 the even half of the master map reduces exactly to the
integrated 081 map 2^(2p+1) p! h_p(s^2 g) = 2 (4 s^2 W)^p rho_p(g) (s2d
Part E), and the map needs no p <= N fallback: it closes for all p.

## Target and status

Frontier edge `G.moments-aodd-sector` (reports/graph/frontier.yaml, chain 2,
rank 1, state untried at last digest): extend the 081 edge-charge moment map
to the non-centred class with a != 0, via noncentral-Wishart-type moment
combinatorics, keeping W, g, s as inputs.

Current manuscript status, re-read from source this round (digest + targeted
reads): appH Problem G, Ledger label: "Status: OPEN. Priority: CRITICAL PATH.
Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and
G-external support at most a scope-limited model; G remains OPEN and neither
satisfies the matrix-derived criterion." Status paragraph: "The mechanism is
CLOSED CONDITIONALLY under the stated boundary entropy; derivation of the
infrared entropy density and stationarity from the matrix theory is OPEN."
Missing step (i)-(iv) quoted verbatim at appH L3119-3130 (dictionary
derivation of the boundary-cut identification; interacting condensate sector;
stationarity derivation; mass-dimension-one conversion). Ch17 completion
criterion for G (ch17-agenda L474-495 area): only the matrix-derived entropy
density plus stationarity counts as closed; this package asserts nothing
about either.

This package: DERIVED (exact, all orders) inside the named Gaussian state
class with a named mean-shift and slot-shift extension; PROGRAMME-CONDITIONAL
with respect to Problem G, whose missing steps (i)-(iv) it leaves untouched.
It closes nothing; W, g, s, a-bar, V, c_i remain inputs (the state that sets
W and g is still unfixed). No status, priority or completion label is changed
by any text in this package.

## Source reading

digest + targeted reads. Digest status: compact digest supplied by the
orchestrator. Read in full: chapters/appH-microscopic-proofs.tex Problem G
section (L3022-3130 region), the charge-to-edge moment paragraph and the
uniform-minimiser paragraph (byte window 688600-694366, which revealed that
the short tail string "do not fix the state that sets" now occurs 3 times in
appH - at 670528, 692129 and 694204 - so the round-1 anchor uses the FULL
082 tail, unique at count 1, byte index 694052); chapters/ch17-agenda.tex G
criterion passage; reports/graph/frontier.yaml G.moments-aodd-sector entry;
proposals/081-g-edge-moments/proposal-r1.md (model definition), its
review-r1.md (odd/even trace polynomials, ranked avenue 2);
proposals/082-g-moments-uniformmin/review-r2.md (hygiene list, byte contract).
No unreadable files. Live appH pins re-verified this round: size 731183,
sha256 956070afcd26fc1c8ffd040ca2d8bb8340467de79117bd0a10d782b6dd062c52,
CRLF 3830, bare LF 0.

## Research and reasoning

### Lemma 1 (all-order spectral trace polynomial) - established identity

For the rank-one block Q(a,t) = [[-4a, -2 i t], [2 i t, 0]], r = t^2,

  Tr Q^m = (-1)^m 2^(m+1) sum_{k=0}^{floor(m/2)} C(m,2k) a^(m-2k) (a^2 + r)^k.

Proof sketch: the eigenvalues are -2a +- 2 sqrt(a^2 + r), so Tr Q^m =
(-2a + 2d)^m + (-2a - 2d)^m with d = sqrt(a^2 + r); the +- expansion cancels
odd powers of d and the surviving terms are 2 * C(m,2k) (-2a)^(m-2k) (2d)^(2k)
= (-1)^m 2^(m+1) C(m,2k) a^(m-2k) (a^2+r)^k. Script s1 verifies this against
direct matrix powers m = 1..14, and separately verifies the even/odd
corollaries (even: Tr Q^2p = 2^(2p+1) sum_k C(2p,2k) a^(2p-2k)(a^2+r)^k;
odd: Tr Q^(2p+1) = -2^(2p+2) sum_k C(2p+1,2k) a^(2p+1-2k)(a^2+r)^k). Note
Tr Q = -4a and Tr Q^3 = -64a^3 - 48 a r (matches 081 review-r1).

### Master averaged map - conditional on the named model

Model (081, extended): a = Im alpha is Gaussian with mean a-bar, variance V;
a is independent of r; r = s^2 sum_i g_i chi_i, where chi_i is a shifted
exponential slot (chi_i ~ Exp(1) + c_i at the level of H generating function;
see kernel below; at the rank-one level the slot law is fully specified by
its moment kernel). Taking the expectation of Lemma 1's expansion,
(a^2+r)^k = sum_j C(k,j) a^(2j) r^(k-j), and a |_ r independent, gives

  <Tr Q^m> = (-1)^m 2^(m+1) sum_k C(m,2k) sum_j C(k,j) A_{m-2k+2j} H_{k-j},

A_n = E[a^n], H_n = <r^n>. s2d Part A verifies this against the directly
expanded trace polynomial read coefficient-by-coefficient through the linear
functional A_n H_m -> A(n) H(m), m = 1..9; Part D verifies it against fully
explicit double Gaussian-exponential integrals (rational data
a-bar = 1/3, V = 2/7, v = 5/11) for p = 1,2,3; values
<Tr Q^3> = -58064/2079, <Tr Q^5> = -1098414976/1440747,
<Tr Q^7> = -3992152240640/142633953.

### Centred vanishing theorem - established inside the model

A_n for centred Gaussian is 0 for odd n. In the master map every odd-m term
carries A with index m - 2k + 2j of the same parity as m, so all odd-m terms
involve odd A and vanish. Hence <Tr Q^(2p+1)> = 0 identically for every V and
every r-law independent of a. This strengthens the 081 pointwise statement
(which held only at a = 0 under the neglecting convention): with any variance
present, centring alone kills the whole odd sector. The vanishing is the
symmetry a -> -a of the centred state combined with Tr Q^m(a, r) being odd in
a for odd m. With a-bar != 0 the odd moments are odd polynomials in a-bar
(s2d Part F) with leading term <Tr Q> = -4 a-bar.

### Noncentred slot kernel and graph-presentation combinatorics

For shifted slots the moment kernel is
M(t) = prod_i (1 - s^2 g_i t)^(-1) exp(c_i s^2 g_i t / (1 - s^2 g_i t)),
i.e. H_n = n! [t^n] M(t) (coefficient extraction; s3b Part 1: at c = 0 this
reproduces H_n = n! h_n(s^2 g) for n = 1..6, the 081 Exp-slot law). The
cumulants are kappa_k = (k-1)! s^(2k) sum_i g_i^k (1 + k c_i), and moments
are the sum over set partitions of products of cumulants (Bell identity),
s3b Part 2 verified n = 1..5 against both the kernel and independent
differentiation of log M. Two independent probabilistic cross-checks of the
D = 1 kernel: Bessel-density integrals of the 2-df noncentral chi-square and
Poisson-gamma mixture sums (s3b Parts 3-4, 25 dps). This is exactly the
structure of Kuriki-Numata graph presentations of noncentral Wishart moments
(real symmetric case: undirected graphs; here rank one, the directed/complex
branch is not used); the published calculus was used only as a pointer for
the class of objects - the NAMCG kernel and bookkeeping were rebuilt here.
Structural conclusion (s3b Part 5): with a independent of r, noncentral slot
shifts c_i enter H_n only, and the centred odd-sector vanishing survives the
shifts; the odd sector is sensitive to state-level Im alpha shift only.

### Comparison with the original target

Original target (frontier edge): derive <Tr Q^(2p+1)> as exact combinatorial
objects in (a-profile, g, s) for the non-centred class. Achieved: the full
double-sum closed form (all m, both parities), the centred vanishing theorem,
the a-bar-oddness, the shift kernel, and the exact 081 reduction. No fallback
to finite p needed. What was NOT done and not claimed: any derivation of the
state, of W, g, s, of a-bar, V or c_i from the matrix theory; nothing about
the selection rule; missing steps (i)-(iv) untouched.

### Literature checked

- Kuriki, S. and Numata, Y., "Graph presentations for moments of noncentral
  Wishart distributions and their applications", Ann. Inst. Statist. Math.
  62 (2010) 645-672; arXiv:0912.0577v2. Verified against the arXiv record
  (fetched this session): real (symmetric) Wishart moments indexed by
  undirected graphs, complex by directed graphs; our rank-one kernel is the
  specialization, and our Bell/set-partition identity is the cumulant form of
  the same bookkeeping. The scout's paraphrase "shifted Gaussian quadratic
  forms" is not the abstract's wording; treat as description, not citation.
- Xu, J. and Yao, Y., arXiv:2505.08149v4 (verified record): cautionary note
  that majorization-order arguments fail for CHS-type statements at p >= 8;
  our package uses no majorization step, so the caution does not bind. Both
  references appear in this proposal only, not in the manuscript insert
  (the insert names Kuriki and Numata in text without \cite).

Not independently verified: none beyond the above note on the scout
paraphrase; no other external claims are used.

## Claim classification

- Lemma 1 trace polynomial (all m): established identity (s1, m=1..14;
  closed-form proof sketched).
- Master averaged map: established algebra given the named model
  (independence of a and r); conditional on the model (s2d A, D).
- Centred vanishing theorem: established inside the model, all orders and
  any variance (s2d C; symmetry argument).
- Odd-in-a-bar and <Tr Q> = -4 a-bar: established inside the model
  (s2d F, s3b 5).
- Noncentred slot kernel, cumulants, Bell identity, c=0 reduction:
  established inside the named slot model (s3b 1-2), plus two independent
  probabilistic cross-checks (s3b 3-4).
- 081 exact reduction at a-bar = V = 0: established (s2d E).
- Probabilistic meaning of the shifts (Y ~ chi2_2(c)/2 per slot, Poisson-
  gamma mixture): established as a property of the kernel; the identification
  c_i = |m_i|^2 or any matrix-theoretic reading of c_i: NOT claimed, input. Under the standard noncentral-chi2 parameterization (MGF (1-2t)^(-d/2) exp(lam t/(1-2t))) the kernel law is chi2_2(2c)/2 with c = lam/2; the kernel, Bessel-density and Poisson-gamma representations used here are mutually consistent (review-r1 finding 4).
- a-bar, V, c_i, W, g, s: phenomenological inputs of the named class; none
  is derived here.
- Nothing in this package is a DERIVED statement about the state, the
  selection rule, or Problem G's missing steps (i)-(iv).

## Proposed changes

Single file, chapters/appH-microscopic-proofs.tex. Insert ONE new single-line
paragraph between the uniform-minimiser paragraph and \emph{Vacuum term.} in
the Problem G ledger. All existing text is kept byte-for-byte; nothing is
replaced or removed.

Anchor (TAIL-PIN, no offsets used by the apply script): the unique full tail
of the uniform-minimiser paragraph,

  they do not by themselves recover the effective-dimension lower bound of
  the moment map, say nothing about whether true block-row profiles
  concentrate, do not fix the state that sets \(W\) and \(g\), leave the
  missing steps (i)-(iv) of the Missing step paragraph unchanged, and they
  close nothing in Problem~G.

occurs exactly once in appH (verified this round; the shorter suffix
"do not fix the state that sets" occurs 3 times and must NOT be used as the
pin). The splice point is the next occurrence of "\emph{Vacuum term.}" after
the pin end, with the verified gap CRLF CRLF. Splice = insert bytes + one
CRLF, before that header. No \ref, \label, \cite is added; no labels
referenced.

Insert text (verbatim file bytes of insert-r1.tex, one line + terminal CRLF):

```latex
\emph{Odd-sector map of the non-centred Gaussian rank-one edge charge.} Within the Gaussian state model of the second paragraph above, relaxing its leading-order convention to a Gaussian \(\operatorname{Im}\alpha\) of mean \(\bar a\) and variance \(V\) independent of the slot radii, and optionally displacing the exponential slots by shifts \(c_i\ge0\), all averaged charge moments close exactly at every order: for every integer \(m\ge1\), \(\langle\operatorname{Tr}Q^{m}\rangle=(-1)^{m}2^{m+1}\sum_{k\le m/2}\binom{m}{2k}\sum_{j=0}^{k}\binom{k}{j}A_{m-2k+2j}H_{k-j}\), where \(A_n=\mathbb{E}\bigl((\operatorname{Im}\alpha)^{n}\bigr)\) are non-centred normal moments and \(H_n=\langle r^{n}\rangle\), verified symbolically against the exact trace polynomials and against direct double integrals at rational data. For odd \(m=2p+1\) this is an odd polynomial in \(\bar a\) with leading term \(\langle\operatorname{Tr}Q\rangle=-4\bar a\), so in the centred model every odd averaged moment vanishes identically for every variance and every slot law independent of \(\operatorname{Im}\alpha\): the odd-sector vanishing asserted in the second paragraph above is a symmetry statement, not a consequence of neglecting \(\operatorname{Im}\alpha\). The slot shifts enter only through the moment kernel \(\prod_i(1-s^{2}g_i t)^{-1}\exp\bigl(c_i s^{2}g_i t/(1-s^{2}g_i t)\bigr)\) for \(H_n=n!\) times the coefficient of \(t^{n}\), equivalently \(H_n=\sum_{\pi}\prod_{B\in\pi}\kappa_{|B|}\) over set partitions of \(\{1,\dots,n\}\) with cumulants \(\kappa_k=(k-1)!\,s^{2k}\sum_i g_i^{k}(1+k c_i)\), the real-graph presentation calculus of Kuriki and Numata specialised to this rank-one law; the shifts never by themselves generate odd charge moments while the slots stay independent of \(\operatorname{Im}\alpha\), and at \(\bar a=0\), \(V=0\) the even half of the map reproduces the closed moment map of the second paragraph above exactly. The mean, the variance and the slot shifts are inputs of the named state class, they do not fix the state that sets \(W\) and \(g\), leave the missing steps (i)-(iv) of the Missing step paragraph unchanged, and they close nothing in Problem~G.
```

Hygiene of the insert (checked by script this round): zero `$`, `[`, `]`,
`\cite`, `\ref`, `\label`, `\eqref`; exactly one `\emph{...}`; no banned
substrings (status, priority, completion, open, critical, programme,
derived, case-insensitive); header occurs 0 times elsewhere under
chapters/; no control bytes below 0x20 except the terminal CRLF; UTF-8
without BOM; single logical line.

Stale passages elsewhere: none. The package does not contradict any existing
text; the second paragraph above's "all odd charge moments vanish,
pointwise" (at the neglecting convention) stays correct and the insert only
generalises it.

## Verification scripts and reproduction pack

All commands from the repository root; interpreter
`python` (CPython 3.11), flag `-I`. Outputs are deterministic; captured
`.out` files accompany each script.

1. `python -I proposals/083-g-moments-aoddsector/s1_allm_spectral.py`
   Expected invariants: `S1 invariant: fail count = 0`, `S1 OK`;
   `p=1 odd trace: -64*a**3 - 48*a*r`; 14 `m=.. identity=True`,
   7 even-corollary True, 5 odd-corollary True.
2. `python -I proposals/083-g-moments-aoddsector/s2d_oddmap.py`
   Expected: invariants 1-6 fail count 0, `S2d OK`; explicit double-integral
   values -58064/2079, -1098414976/1440747, -3992152240640/142633953;
   closed p=0 leading -4*a0.
3. `python -I proposals/083-g-moments-aoddsector/s3b_noncentral_r.py`
   Expected: invariants 1-5 fail count 0, `S3b OK`; D=1 cross-check values
   0.42, 0.3384, 0.397008 for both Bessel and Poisson-gamma.
4. `python -I proposals/083-g-moments-aoddsector/simulate_apply_083.py`
   READ-ONLY. Expected: `PRE OK size 731183 sha8 956070af`,
   `POST size 733361 sha8 c35bfed0 CRLF 3832 bareLF 0` (full POST sha256
   c35bfed009668845a5ff313e0a35b3f48374cbc843ed85e9d4fedb2a936cedfd),
   `close-idiom count PRE 10 POST 11`, `no write performed`.

Dead/superseded scripts (kept for provenance, do not run as evidence):
s2_oddmap.py (dead stub, never run), s2b_oddmap.py (+ .out, superseded:
sqrt(r) inside Poly, missing positivity, variable mismatch),
s2c_oddmap.py (+ .out, superseded: factorial double-count in map_m),
s3_noncentral_r.py (+ .out, superseded: 100 s/sympy series and a
chi-square-2 scale convention error in Parts 3-4; invariants 1,2,5 of that
file passed). s3b replaces s3 with the same invariant list.

## Decisions Taken

- Model class: Gaussian a independent of r, mean/variance free, Exp slots
  with shifts - chosen as the minimal non-centred extension of the exact
  081 class so the 081 map is the exact c=0, a-bar=V=0 reduction (rejected:
  coupled a-r models, which lose the closed form; rejected: full
  noncentral-Wishart rank > 1, not the rank-one object of the model).
- Independence of a and r kept as a NAMED hypothesis, stated in the insert
  ("independent of the slot radii", "while the slots stay independent of
  Im(alpha)"); the vanishing theorem and the kernel statement are valid only
  under it. Rejected: silently importing Kuriki-Numata bookkeeping without
  re-deriving (the scout warned the coupling differs; we rebuilt it).
- Odd-moment map stated for all m at once (no odd-only formula): same proof,
  less clutter, and it makes the 081 even reduction checkable on the spot.
- Insert refers positionally ("the second paragraph above") matching the
  local manuscript convention; descriptive fallback avoided since the
  headers are long.
- Kuriki-Numata named in the insert without \cite (insert hygiene forbids
  \cite); full record given here for the gatekeeper; if the integrator wants
  a citation, bib entry: `@article{kuriki2010graph, author=Kuriki, S. and
  Numata, Y., title=Graph presentations for moments of noncentral Wishart
  distributions and their applications, journal=Ann. Inst. Statist. Math.,
  volume=62, pages=645-672, year=2010, doi=10.1007/s10463-010-0279-4,
  arXiv=0912.0577}` - VERIFY DOI at integration time; the arXiv record was
  verified this session.
- Anchor: full 082 tail pin (unique); the short tail pin from the earlier
  round is ambiguous (3 occurrences) - flagged here because 082's review
  recorded a shorter pin.

## Milestone assessment

Routine. No MILESTONE.md trigger: this is a within-class combinatorial
completion of the 081 map (edge G.moments-aodd-sector), not a critical-path
step of Problem G derived from the matrix theory.

## Status-label recommendation

Re-derived critical-path set from ch17 + appH this round: A, B, C, D1, E, F,
G-derived, N (G itself: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL).
Affected labels: none. This package proposes no label change.

## Author decision needed

none.

## Remaining open step

For Problem G (unchanged): missing steps (i)-(iv) of the Missing step
paragraph - the boundary-cut identification, the interacting condensate
sector, the stationarity derivation, and the mass-dimension-one conversion.
For the edge itself (optional, not required by the insert): (a) relaxing
independence between Im(alpha) and the slot radii (coupled class: the master
map survives verbatim if A_n and H_n are replaced by mixed moments
E[a^(m-2k+2j) r^(k-j)], so the next computation is those mixed moments under
a named coupling); (b) whether any matrix-theoretic object selects a-bar, V
or the c_i (currently pure inputs).

## Special instructions for the gatekeeper

- Do not let the word "map closes" be read as closing anything in Problem G;
  the insert asserts inputs and closes nothing, and the status passage keeps
  all labels.
- Re-run the four reproduction commands; the .out files are captured and the
  invariant lines must match.
- Re-pin at apply time: the live appH may have moved since this round;
  simulate_apply_083.py re-asserts PRE size/sha and pin uniqueness, and it
  must print "no write performed".
- The short pin "do not fix the state that sets" has 3 occurrences (670528,
  692129, 694204) - only the full 082 tail is unique; do not shorten.
- Math to re-derive if doubted: Lemma 1 (two lines), the centred vanishing
  (parity of A-index), the kernel log-derivative and cumulants, and the
  Bell identity. The Poisson-gamma cross-check uses K ~ Poisson(c), NOT
  Poisson(c/2); the scale convention of the kernel is (1 - s^2 g t)^{-1},
  i.e. chi2_2(c)/2 per slot, not chi2_2(c).
- Security: the proposal folder was scanned for injected-instruction
  patterns; report in the final handback.


## Round 2 corrections
- F1: 'Kuriki, F. and Numata, T.' -> 'Kuriki, S. and Numata, Y.'; bib 'author=Kuriki and Numata' -> 'author=Kuriki, S. and Numata, Y.' (arXiv:0912.0577v2 abstract, fetched 2026-11-18: Satoshi Kuriki, Yasuhide Numata).
- F2: doi=10.1007/s10463-009-0242-4 -> doi=10.1007/s10463-010-0279-4 (api.crossref.org names Kuriki/Numata, 'Graph presentations for moments of noncentral Wishart distributions and their applications', Ann. Inst. Statist. Math. 62, 645-672, 2010).
- F3: 'Xu, Z. and Yao, Q.' -> 'Xu, J. and Yao, Y.' (arXiv:2505.08149v4 abstract, fetched 2026-11-18: Jia Xu, Yong Yao).
- F4: chi2 parameterization clause appended to the shift-meaning bullet (standard chi2: kernel law = chi2_2(2c)/2, c = lam/2; kernel/Bessel/Poisson-gamma mutually consistent). s3b_noncentral_r.py left byte-frozen per round-2 instruction.
- F5: manifest.md regenerated without the 'handback table' reference; old manifest 2753 B / sha8 0a0c3330 superseded.
Round 2 changes no mathematical claim; insert-r1.tex remains the sole integrable artifact.
