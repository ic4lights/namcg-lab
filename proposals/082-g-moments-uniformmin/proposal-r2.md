# Proposal 082-g-moments-uniformmin, round 2

## Result

The uniform-minimiser inequality that the 081 integration (appH L3177)
deliberately excluded as sample-verified-only is now established as a theorem
for the exact profile class of the 081 moment map: for every block-row profile
\(g=(g_1,\dots,g_D)\) with \(g_i\ge0\), total weight \(W=\sum_i g_i>0\), fixed
slot count \(D\), and every integer \(p\ge1\), the obstruction factor
\(\rho_p(g)=p!\,h_p(g)/W^p\) (with \(h_p\) the complete homogeneous symmetric
polynomial) satisfies \(\rho_p(g)\ge\prod_{k=1}^{p-1}(1+k/D)\), with equality
for \(p\ge2\) if and only if all slots are equal (\(p=1\): equality always;
\(D=1\): both sides \(=p!\)). The proof is self-contained (pairwise
mean-preserving smoothing on the simplex plus an exact pair identity for
\((x-y)(\partial_x h_p-\partial_y h_p)\)) and needs no majorisation machinery.
The insert records the lemma, the sharp two-slot closed form of the defect, and
its exact scope. This is a lemma (established), not a no-go or counterexample.
It closes nothing in Problem G: the missing steps (i)-(iv), the derived state
fixing \(W\) and \(g\), and the entropy-density/stationarity requirement of
ch17 L482-495 are untouched. Round 2 changes no mathematical claim: it applies
the gatekeeper's F1 one-character display correction
\(D^{-p}\prod_{k=0}^{p-1}(D+k)\) to the shipped insert by asserted byte
surgery and regenerates all downstream byte pins.

## Target and status

- Edge `G.moments-uniformmin`, chain 2, RANK 1 in `reports/graph/frontier.yaml`,
  based_on INTEGRATION 12; named by the 081 gatekeeper review as ranked avenue
  (3), verbatim: 'proof of the uniform-minimiser inequality as a lemma'
  (sample-verified only, correctly excluded from the integrated insert).
- Problem G ledger label and Status paragraph (appH L3025-3027 region,
  re-verified by targeted read of the 081 paragraph block L3177-3181) are
  unchanged by this package: G remains open and PROGRAMME-CONDITIONAL; the ch17
  completion wording read at L474-495 ('mechanism CLOSED CONDITIONALLY,
  derivation OPEN'; G is DERIVED only when the entropy density and stationarity
  relation are derived from the matrix theory) is unaffected.
- What this package establishes: the named sub-lemma. Classification of the
  package itself: DERIVED as a pure-mathematics sub-lemma about the profile
  functional; PROGRAMME-CONDITIONAL for the programme, because \(W\) and \(g\)
  remain inputs (081 review Input audit) and the lemma turns none of them into
  outputs.

## Source reading

digest + targeted reads. `scratch/digest.md`: compact, DIGEST CURRENT at 384dfc1,
dirty-chapters yes (expected: uncommitted 081 is the current live tree state);
working-tree appH 729,152 B / sha256
5d52b67252b152751709dd2f7d22ccdd29e77df131d60fd43432d7583463a303 / CRLF 3,828
re-verified this round by the read-only `simulate_apply_082_r2.py` PRE block
(`PRE OK`, no drift). Round 2 read in full: this folder's `review-r1.md`
(findings F1-F5, Corrected snippet, Final integration instructions),
`proposal-r1.md`, `manifest.md`, and `simulate_apply_082.py` (basis of the r2
regenerate). `insert-r1.tex` is read by `make_insert_r2.py` in binary and
never retyped. Round 1's reads stand as recorded in r1 (frontier.yaml
`G.moments-uniformmin` and `G.edge-moments` rows, 081 proposal/review passages,
appH L3177-3181 and the Problem G ledger, ch17 L474-495); round 2 introduces no
new mathematical claim and needs no new manuscript reading beyond the anchor
coordinates, which the gatekeeper's own PRE measurement re-confirmed (081
header L3177, G-side Vacuum L3179).

## Research and reasoning

### Audit of the dead-pass partial (lineage, superseded)

`s1_uniform_min_certificate.py` (3,200 B, sha8 4d3a10f7): parses but has no
`if __name__` tail (running it does nothing); its docstring claims section (E),
which the code never implements. Run by import: section (A) coefficient checks
pass up to the first (B) comparison, which fails `closedform` at D=3, p=2. Two
code defects, not a mathematics failure: (i) it compares the quotient `P` to
`(x-y)**2 * sum(...)` (wrong scale - it should compare `P` to the bare sum, or
`(x-y)**2 * P` to `(x-y)**2 * sum`); (ii) the `a`-sum runs to `m-1` without the
`a <= p-1-m` cap, and its `hp(Z, k)` returns 1 for `k = -1` (negative order is
never zeroed). My own generating-function derivation (below) gives the claimed
closed form, so the identity in the dead-pass docstring is correct; v2 fixes the
two defects and regenerates everything from my own run. Per the workflow
instruction the partial is left as lineage and the complete corrected script is
the new file `s1_uniform_min_certificate_v2.py`.

### Lemma and proof

Hypothesis class (named in full): profiles \(g=(g_1,\dots,g_D)\), \(g_i\ge0\),
\(W=\sum g_i\in(0,\infty)\), slot count \(D\ge1\) fixed and equal to the length
of the profile tuple as used in the 081 moment map \(\langle\mathrm{Tr}\,Q^{2p}\rangle=2(4s^2W)^p\rho_p(g)\); order \(p\ge1\) an integer.

Step 1 (homogeneity). \(h_p\) is homogeneous of degree \(p\), so
\(\rho_p(\mu g)=\rho_p(g)\): minimise over the compact simplex
\(K=\{\mu\ge0:\sum\mu_i=W\}\) on which \(h_p\) is continuous; a minimiser
\(\mu^*\) exists.

Step 2 (exact pair identity). Let \(V=\{x,y\}\sqcup Z\). From the generating
function \(H(t)=\sum_p h_p t^p=\prod_{v\in V}(1-vt)^{-1}\),
\(\partial_x h_p=\sum_{m=0}^{p-1}(m+1)x^m h^{(x)}_{p-1-m}\), where
\(h^{(x)}\) omits \(x\) (certificate (C), exact for p=2..6, D=3), and
\(h^{(x)}_q=\sum_{a=0}^{q} y^a h_{q-a}(Z)\). Hence
\((\partial_x-\partial_y)h_p=\sum_m (m+1)\sum_a h_{p-1-m-a}(Z)(x^m y^a-x^a y^m)\).
The summand is antisymmetric under \((m,a)\mapsto(a,m)\); pairing the two, the
common factor \(x^{\min}y^{\min}(x-y)G_{|m-a|}\) (with
\(G_r=\sum_{t=0}^{r-1}x^{r-1-t}y^t\), all coefficients 1) is multiplied by
\((m+1)-(a+1)=m-a\). Thus, for all \(p\ge1\) and all \(Z\),
\[
(x-y)(\partial_x h_p-\partial_y h_p)=(x-y)^2\sum_{m=1}^{p-1}\ \sum_{a=0}^{\min(m-1,\,p-1-m)}(m-a)\,h_{p-1-m-a}(Z)\,x^{a}y^{a}\,G_{m-a}(x,y).
\]
The range condition is \(1\le m\le p-1\), \(0\le a\le m-1\), \(m+a\le p-1\)
(the dead-pass cap bug; \(h_{p-1-m-a}(Z)\) then has nonnegative order).
Certificate (B) checks the identity exactly as polynomials (p=2..6, D=3,4),
certificate (A) checks the quotient's nonnegative coefficient scan there.

Step 3 (strict sign). Every summand is \(\ge0\) on \(x,y,Z\ge0\). The
\((m,a)=(p-1,0)\) summand exists for \(p\ge2\) and equals
\((p-1)\,h_0(Z)\,G_{p-1}(x,y)=(p-1)\sum_{t=0}^{p-2}x^{p-2-t}y^t=(p-1)h_{p-2}(x,y)\),
which is \(>0\) whenever \(x+y>0\) (for \(p=2\) it is the constant 1). Hence the
pair Schur product \((x-y)(\partial_x h_p-\partial_y h_p)\) vanishes on
\(x\ne y\), \(x,y\ge0\) never; it is the classical Schur-Ostrowski pair
condition, but the argument below is self-contained.

Step 4 (smoothing and equality). If \(\mu^*\) is a minimiser with
\(\mu^*_i\ne\mu^*_j\), set \(\varphi(\tau)=h_p\) with the pair replaced by
\(x(\tau)=\tfrac{x+y}{2}+(x-y)(\tfrac12-\tau)\), \(y(\tau)=\tfrac{x+y}{2}-(x-y)(\tfrac12-\tau)\).
Then \(\varphi'(\tau)=-(x-y)^2\,Q(x(\tau),y(\tau),Z)\) with \(Q>0\) along the
whole path (the pair sum \(x+y\) is preserved and \(>0\)), so
\(\varphi(1)<\varphi(0)\): strict decrease under mean-preserving smoothing of
any unequal pair, contradicting minimality. So \(\mu^*\) has all slots equal,
\(\mu^*=u=(W/D,\dots,W/D)\), and for any \(g\ne u\) smoothing one unequal pair
gives \(\rho_p(g)>\rho_p(u)\). Equality iff uniform (p\ge2); for \(p=1\), \(h_1=\sum\mu_i=W\) gives \(\rho_1=1\) identically.

Step 5 (uniform value). On the uniform profile
\(h_p(u)=\binom{D+p-1}{p}(W/D)^p\) (complete homogeneous polynomial of
\(D\) equal arguments), so \(\rho_p(u)=p!\binom{D+p-1}{p}D^{-p}=D^{-p}\prod_{k=0}^{p-1}(D+k)
=\prod_{k=1}^{p-1}(1+k/D)\). Certificate (D) checks this exactly for
p=0..6, D=1,2,3,7,120; certificate (G) checks
\(\prod_{k=1}^{p-1}(1+k/D)\ge1+\binom{p}{2}/D\) (the slot-count shadow of the
integrated \(D_{\mathrm{eff}}\) lower bound, \(D_{\mathrm{eff}}\le D\)) exactly
for D=1..120, p=2..8.

Step 6 (two-slot defect, closed form). For \(D=2\),
\(h_p(t,1-t)=(t^{p+1}-(1-t)^{p+1})/(2t-1)\). With \(s=2t-1\):
\((1+s)^{p+1}-(1-s)^{p+1}=2\sum_{j\,\mathrm{odd}}\binom{p+1}{j}s^{j}\), so
\(h_p=2^{-p}\sum_{r=0}^{\lfloor p/2\rfloor}\binom{p+1}{2r+1}s^{2r}\) and
\(h_p(1/2,1/2)=(p+1)/2^{p}\); the defect is
\(h_p(t,1-t)-h_p(1/2,1/2)=2^{-p}\sum_{r\ge1}\binom{p+1}{2r+1}(2t-1)^{2r}\)
with strictly positive coefficients. (Coefficient \(2^{-p}\), not
\(2^{1-p}\): the first v2 run failed (E) at p=2 and the hand check
\(h_2(t,1-t)=((2t-1)^2+3)/4\) fixed it; the dead pass's (E) was never executed
so its coefficient was untested.) Certificate (E) checks the closed form and
coefficient positivity exactly for p=2..8.

### Relation to integrated 081 content (exact, checked)

The lemma bounds \(\rho_p\) from below by a function of the slot count \(D\);
the integrated paragraph's obstruction is the separate lower bound
\(\rho_p-1\ge\binom{p}{2}/D_{\mathrm{eff}}\) with
\(D_{\mathrm{eff}}=W^2/\sum g_i^2\le D\). Neither recovers the other at fixed
profile (exact rational witnesses, p=3):
- \(g=(1/2,1/2,0,0,0)\), \(D=5\): \(\rho_3=3=\prod_{k=1}^{2}(1+k/2)\) exactly,
  \(D_{\mathrm{eff}}=2\), \(D_{\mathrm{eff}}\)-bound \(=1+3/2=5/2=2.5\), while the
  lemma alone would give only \(\prod_{k=1}^{2}(1+k/5)=42/25=1.68<2.5\) - the
  lemma does not by itself imply the \(D_{\mathrm{eff}}\) bound.
- uniform \(D=5\): lemma \(42/25=1.68\) strictly exceeds the
  \(D_{\mathrm{eff}}\)-bound \(1+3/5=8/5=1.6\) - the lemma is strictly stronger
  there.
The 081 superseded-draft counterexample \(g=(9/10,1/10)\), p=3 (081 ledger note:
\(123/25>3003/625\) refuted the superseded draft s3's false upper bound): its
\(\rho_3=6h_3=6\cdot(2t^2-2t+1)|_{t=0.9}=6\cdot0.82=123/25=4.92\) satisfies
this lemma with margin (\(\ge\prod_{k=1}^{2}(1+k/2)=3\)). No integrated passage
is stale: the 081 paragraph never states the minimiser inequality.

Literature. The pair condition is the classical Schur-Ostrowski criterion; its
statement was verified against the Wikipedia article 'Schur-convex function'
(accessed 2026-11-18; the Marshall-Olkin-Arnold textbook attribution there is
'not independently verified'). Nothing is imported: the proof above is
self-contained (compactness + smoothing), the manuscript insert cites nothing,
and no bib entry is proposed.

## Claim classification

- Lemma \(\rho_p(g)\ge\prod_{k=1}^{p-1}(1+k/D)\) with the stated equality case:
  established (full derivation above; certificates (A)-(E) machine-check the
  exact identities on which the steps rely for the checked finite ranges; the
  derivation itself is general in p, D).
- Pair identity and its closed form (Step 2): established derivation; exact
  polynomial certificates (A),(B) at p=2..6, D=3,4 and (C) at p=2..6, D=3.
- Uniform value (Step 5): established; exact certificate (D).
- Two-slot closed form (Step 6): established derivation; exact certificate (E)
  at p=2..8.
- Random-profile in-class two-direction checks (F) and product-shadow bound
  (G): sampled/consistency confirmations; the theorem does not depend on them.
- Non-implication statements between the slot-count bound and the
  \(D_{\mathrm{eff}}\) bound: established by the exact rational witnesses.
- \(W\) and \(g\) as physical inputs: unchanged INPUT status (081 review Input
  audit). The lemma does not promote them to outputs.
- Problem G status: unchanged OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL
  (manuscript text; no label touched here).

## Proposed changes

One file: `chapters/appH-microscopic-proofs.tex`, one new paragraph (the
the fenced block below, shipped as `insert-r2.tex` (the
F1-corrected body; `insert-r1.tex` retained as lineage only,
SUPERSEDED FOR INTEGRATION), single content line, CRLF,
UTF-8 no BOM).

Anchor contract (tail-pinned; the line-start `\emph{Vacuum term.}` occurs twice
- L3006 in Problem F and the G-side one - so position is defined relative to
the unique 081 header): the insert lands blank-CRLF-separated immediately before
the unique line-start `\emph{Vacuum term.}` occurrence that follows the unique
line start `\emph{Charge-to-edge moment identification in the Gaussian
rank-one class.}` (currently appH L3179, preceded by the 081 paragraph L3177
and a blank line). All of L3177, L3179 and the block closer L3181 are kept
verbatim; nothing is removed or reworded; no other file changes; no bib entry;
no stale passages elsewhere (the integrated 081 paragraph never mentions the
minimiser inequality, so nothing needs narrowing).

```latex
\emph{Uniform minimiser of the obstruction factor over profiles.} For a block-row profile \(g=(g_{1},\dots,g_{D})\) of \(D\) slots with \(g_{i}\ge0\) and total weight \(W=\sum_{i}g_{i}>0\), the obstruction factor \(\rho_{p}(g)=p!\,h_{p}(g)/W^{p}\), with \(h_{p}\) the complete homogeneous symmetric polynomial, obeys for every integer \(p\ge1\) the sharp profile bound \(\rho_{p}(g)\ge\prod_{k=1}^{p-1}(1+k/D)\), with equality for \(p\ge2\) if and only if all slots are equal. The argument is elementary and pair-local: by homogeneity it suffices to minimise over the compact simplex \(g\ge0\), \(\sum g=W\); for two slots \(x,y\) with remaining slots \(Z\) the exact pair identity \((x-y)(\partial_{x}h_{p}-\partial_{y}h_{p})=(x-y)^{2}\sum_{m=1}^{p-1}\sum_{a=0}^{\min(m-1,p-1-m)}(m-a)\,h_{p-1-m-a}(Z)\,x^{a}y^{a}\sum_{t=0}^{m-a-1}x^{m-a-1-t}y^{t}\) holds, every summand of its right-hand side is nonnegative for \(x,y\ge0\), and the \(m=p-1\), \(a=0\) summand alone is \((p-1)\sum_{t=0}^{p-2}x^{p-2-t}y^{t}\), strictly positive whenever \(x+y>0\); hence, for \(p\ge2\), replacing an unequal pair of slots by their mean, at preserved total weight, strictly decreases \(h_{p}\), so a minimiser has all slots equal, and \(p!\,h_{p}(1/D,\dots,1/D)=D^{-p}\prod_{k=0}^{p-1}(D+k)\) gives the stated minimum. For \(D=2\) the defect has the closed form \(h_{p}(t,1-t)-h_{p}(1/2,1/2)=2^{-p}\sum_{r=1}^{\lfloor p/2\rfloor}\binom{p+1}{2r+1}(2t-1)^{2r}\) with strictly positive coefficients, so at fixed slot count the obstruction is smallest at the uniform profile and largest at single-row profiles, where it equals \(p!\); these statements are properties of the profile functional \(g\mapsto\rho_{p}(g)\) at fixed slot count: they do not by themselves recover the effective-dimension lower bound of the moment map, say nothing about whether true block-row profiles concentrate, do not fix the state that sets \(W\) and \(g\), leave the missing steps (i)-(iv) of the Missing step paragraph unchanged, and they close nothing in Problem~G.
```

## Verification scripts and reproduction pack (round 2 pins)

All commands run from the repository root, deterministic, exact rational or
symbolic arithmetic only; every script performs no write except where stated.

1. `proposals/082-g-moments-uniformmin/make_insert_r2.py` (lineage generator,
   already run in round 2; the only script that writes, and only to
   `insert-r2.tex` - do not re-run it in verification, verify the artifact via
   read-only items 2 and 4). It asserted against the frozen `insert-r1.tex`
   (2,029 B, sha256 `edec101f...0690`): exactly one occurrence of the pre-F1
   `(D+k)` product display starting at `k=1` (review-r1, Corrected snippet),
   and wrote `insert-r2.tex` size-unchanged at 2,029 B, Hamming distance 1
   from r1 (single byte `0x31`->`0x30` at offset 1260), no body control bytes,
   terminal CRLF, never retyping the body. The on-disk artifact is
   `9342a7be34ea588defdaf6efd465c6617f5e4d1bebe4f45e00c8f9218f37414e`; this
   pin is independently re-asserted, read-only, by the INS pin of item 2.
2. `python -I proposals/082-g-moments-uniformmin/simulate_apply_082_r2.py`
   Invariants: three printed lines; first begins `PRE OK size 729152
   sha8 5d52b672`; second begins `POST computed size 731183 sha8 956070af
   CRLF 3830 bareLF 0; insert lands line 3179`; final line exactly `no write
   performed`; exit 0. Observed in `simulate_apply_082_r2.out`. Regeneration
   lineage: the r1 simulate output (`POST computed size 731183 sha8 192b8f9a`)
   became stale when the F1 character fix changed the insert bytes (size and
   CRLF count unchanged, hash changed); the VOID pin `731180 / 6414cbbe`
   remains VOID. On PRE drift (any of size 729152 / sha256
   5d52b67252b152751709dd2f7d22ccdd29e77df131d60fd43432d7583463a303 / CRLF
   3828 / bareLF 0 / header-collide 0 / 081-pin 1 / vacuum 2) the simulator
   aborts by assertion - STOP and report (no drift in either round). Its
   BANNED scan uses the seven-word standard including `derived` (F4): 0 hits.
   Lineage: derived from the frozen r1 script by `gen_simulate_r2.py`; the
   read-only `verify_gen_lineage_r2.py` re-proves in memory that that
   single-occurrence-anchor substitution maps the shipped r1 script to the
   shipped r2 script byte-for-byte (prints `LINEAGE OK equal`, both 3,412 B /
   sha8 `861dfd2d`), so the generator itself need not be run.
3. `python -I proposals/082-g-moments-uniformmin/post_pin_full_r2.py`
   Same anchor contract as item 2, in memory; prints the FULL POST sha256 for
   the record: `POST FULL size 731183 sha256
   956070afcd26fc1c8ffd040ca2d8bb8340467de79117bd0a10d782b6dd062c52 sha8
   956070af; insert lands line 3179` then `no write performed`; observed in
   `post_pin_full_r2.out`. These, not `192b8f9a...`, are the round-2
   integration POST pins.
4. `python -I proposals/082-g-moments-uniformmin/check_r2_consistency.py`
   Read-only: extracts the fenced insert body from `proposal-r2.md`,
   byte-compares it to `insert-r2.tex` minus terminal CRLF, and counts display
   forms over the whole proposal (pre-F1 `k=1`-started `(D+k)` form must have
   zero hits; corrected `k=0` form at least one). Invariant (observed in
   `check_r2_consistency.out`): `PASS body sha8 2d69d745 insert sha8 2d69d745
   size 2027; old-hits 0 new-hits N` with N >= 1 (the sha8 pair is of the
   2,027 B body; the 2,029 B file sha8 `9342a7be` includes the terminal CRLF).

## Round 2 corrections (gatekeeper review-r1.md findings F1-F5)

F1 (blocking, false display formula in the insert). Applied exactly the
gatekeeper's one-character fix `k=1` -> `k=0`, i.e.
`p!\,h_{p}(1/D,\dots,1/D)=D^{-p}\prod_{k=0}^{p-1}(D+k)`, by byte surgery
(`make_insert_r2.py`): read `insert-r1.tex` in binary, asserted size 2,029 and
sha256 `edec101f...0690`, asserted the old substring occurs exactly once,
wrote `insert-r2.tex` of the same size with Hamming distance 1 (single byte
`1`->`0` at offset 1260), no body control bytes, terminal CRLF. The body was
never retyped. Math check: `D^{-p}\prod_{k=0}^{p-1}(D+k) = p!\binom{D+p-1}{p}
D^{-p} = \prod_{k=0}^{p-1}(1+k/D) = \prod_{k=1}^{p-1}(1+k/D)` (the k=0 factor
is 1), so the corrected display equals the stated minimum; spot values p=1
(both sides 1) and D=2, p=2 (3/2). New insert sha256
`9342a7be34ea588defdaf6efd465c6617f5e4d1bebe4f45e00c8f9218f37414e`; INS and
POST pins regenerated (items 1-3 above); the fence body in §Proposed changes
is `insert-r2.tex` itself (consistency pinned by item 4).

F2 (major, stale simulate invariant in the reproduction pack). §Verification
item 2 now quotes the regenerated r2 invariant (`POST computed size 731183
sha8 956070af CRLF 3830`) and records the regeneration lineage: the r1 simulate
output (731183 / 192b8f9a) became stale when the F1 fix changed the insert
bytes; the VOID 731180 / 6414cbbe remains VOID.

F3 (major, non-re-auditable manifest byte-exactness claim). The manifest
"Repair lineage" section no longer claims byte-exact reverse collapse. It now
records only what is checkable: the escape sites in the repaired body are the
unique backslashes at offsets 1404 (`\rfloor}`), 1412 (`\binom`), 1682
(`g\mapsto\rho_{p}(g)`), whose documented 1-byte collapses land at the r1
manifest void coordinates 1404/1411/1680; void artifact 2,026 B, sha8
`ee51a36c`; and it states explicitly that the VOID bytes are not on disk, that
no shipped evidence reproduces `ee51a36c` byte-exactly, and that the
gatekeeper's independent reconstruction (same size 2,026 B, sha8 `121b4c8e`,
125 single-site replacement variants x 3 tail conventions, none matching)
confirms the coordinates and size but not the bytes.

F4 (minor, BANNED list short one word). `simulate_apply_082_r2.py` uses the
seven-word standard `['status','priority','completion','open','critical',
'programme','derived']`; it was derived from the frozen r1 script by
`gen_simulate_r2.py` (asserted single-occurrence anchors; exactly the BANNED
change and the INS re-pin to `insert-r2.tex` 2,029 B / `9342a7be...`, plus the
run-command filename in the docstring). Control-byte guard and read-only
design kept. The r2 run asserts all seven words against the actual insert-r2
line: 0 hits.

F5 (minor note, no action required). Noted and accepted: the dead-lineage
audit claims are all true as the gatekeeper independently confirmed;
`s1_uniform_min_certificate_v2.py` is unchanged this round (byte-reproduced by
the gatekeeper's own `python -I` re-run) and was deliberately not re-executed.

## Decisions Taken

1. Superseded the partial s1 with `s1_uniform_min_certificate_v2.py` instead of
   the in-place Edit that killed the prior pass; partial kept as lineage.
2. Corrected the (E) coefficient to \(2^{-p}\) (hand check p=2; first-run
   failure), replacing the untested claim; the insert carries the corrected
   coefficient.
3. Proof route: self-contained compactness + pairwise smoothing, not the
   Schur-Ostrowski/majorisation theorem from the literature (avoids importing
   an unverified theorem-number citation; the literature note is background
   only). Rejected: citing Hardy-Littlewood-Polya / Marshall-Olkin-Arnold
   without independent verification.
4. Anchor: tail-pinned G-side landing after the 081 paragraph (the only legal
   contract given the double `\emph{Vacuum term.}`); closing idiom taken
   verbatim from the nine existing integrated uses.
5. Stated the lemma for \(p\ge1\) with equality condition tied to \(p\ge2\),
   and inserted an explicit non-recoverability clause for the
   \(D_{\mathrm{eff}}\) bound (honest scoping; rule 6; prevents reading the
   lemma as strengthening the integrated obstruction).
6. No bib entry; no status/label text in the insert.

7. Round 2 (F1): applied the corrected display by asserted byte surgery on the
   frozen `insert-r1.tex` (`make_insert_r2.py` -> `insert-r2.tex`, size 2,029 B,
   Hamming distance 1), never retyping the body; re-pinned INS (item 2) and
   POST (item 3) downstream. Rejected: retyping the 2,029 B insert (character
   error risk - exactly the F1 failure mode) and in-place edits of the frozen
   r1 artifacts (the repair lineage required them kept byte-frozen).
8. Round 2 (F4): regenerated the simulate as a NEW file
   `simulate_apply_082_r2.py` via `gen_simulate_r2.py` with two content changes
   (seven-word BANNED list; INS pin -> `insert-r2.tex`), keeping the
   control-byte guard and read-only design; the r1 simulate script and its POST
   pin 192b8f9a are retained as lineage only. Added `post_pin_full_r2.py` (a
   separate read-only recorder, same anchor contract) because the simulate
   prints sha8 only and the manifest needs the full POST sha256.

## Milestone assessment

Routine. A gatekeeper-named gap (081 review avenue (3)) is closed as a lemma,
but no MILESTONE.md trigger fires: Problem G's missing steps (i)-(iv) and the
ch17 L488-495 derivation requirement are untouched, and nothing on the
critical path is completed.

## Status-label recommendation

Derived from the current agenda (ch17 L474-495, re-read this round) and the
ledger (last entry INTEGRATION 12, accepted=12): critical-path set A, B, C, D1,
E, F, G-derived, N unchanged. Affected labels: none. Problem G stays open and
PROGRAMME-CONDITIONAL; `G.moments-uniformmin` is discharged at the in-class
level (report-layer/frontier fact, not manuscript text). No label edit is
proposed or made.

## Author decision needed

None.

## Remaining open step

What this does NOT close (all still open, per the 081 review and ch17): the
derived profile/state data fixing \(W\) and \(g\) (`G.moments-derivedprofile`);
the non-centred/coupled a-sector (`G.moments-aodd-sector`); finite-V
corrections (`G.moments-finiteV`); the two-sided selection-rule reading
(`G.selrule-twosided`); G missing steps (i)-(iv); entropy density and boundary
stationarity as matrix-derived outputs (the ch17 G DERIVED criterion). Inside
the lemma nothing is left unproven for its stated class; extending it beyond
fixed slot count is vacuous (infimum over D of the bound tends to 1), so the
slot-count-fixed form is the right statement.

## Special instructions for the gatekeeper

- Re-derive Step 2 (pair identity) independently or re-run certificate (A)+(B);
  then verify Step 3's strict term and Step 4's sign
  \(\varphi'(\tau)=-(x-y)^2Q\le0\) (the minus sign: increasing \(\tau\) moves
  \(x(\tau)\) toward the mean).
- The (E) coefficient is \(2^{-p}\); the classic trap is \(2^{1-p}\) (caught in
  this pass); spot-check p=2 by hand.
- Assert the non-implication witnesses exactly (42/25 vs 5/2 and vs 8/5).
- The insert must be read ONLY as the fixed-slot-count profile bound; it is not
  a \(D_{\mathrm{eff}}\) improvement and asserts nothing about state derivation.
- PRE pins drift => STOP (read-only contract; the repo copy of appH must be
  untouched; `simulate_apply_082.py` performs no write).
- Do not merge the superseded `s1_uniform_min_certificate.py` into any evidence
  chain.
- Scope limit: one paragraph insertion; no bib; no other files.

- Round 2 re-pin: integrate ONLY `insert-r2.tex` (2,029 B, sha256
  9342a7be34ea588defdaf6efd465c6617f5e4d1bebe4f45e00c8f9218f37414e);
  `insert-r1.tex` (edec101f...), the VOID insert (2,026 B, ee51a36c), both old
  POST pins (731,180/6414cbbe VOID and 731,183/192b8f9a stale lineage) and the
  superseded `simulate_apply_082.py` must not be integrated. The integrated
  display must read `D^{-p}\prod_{k=0}^{p-1}(D+k)`; verify by reproduction-pack
  item 4 or the p=2, D=2 spot check (3/2).
