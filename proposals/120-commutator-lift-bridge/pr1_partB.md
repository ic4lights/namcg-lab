## Central claim and rule-6 tiering

The payload insert-commutator-lift-r1.tex (pin <<PAYPIN>>, 8 lines, one clause block per
line) makes five claims. Tier legend: established identity/derivation (E); established
under stated inputs/branch hypothesis (E-in); conditional result (C); input/datum (I);
conjecture/mechanism (J); unresolved missing step (U). Verification anchors are chk ids
in verify_r120.py; each is a PASS line in out-r120.txt (line references in the mapping
below).

(a) Exact all-orders star identity (bridge). Under the inputs of the next section,
[Xhat^mu, Phi]_star = i Theta^{mu nu} (d_nu Phi - i[A_nu, Phi]_star) holds for every
matrix-valued Weyl symbol Phi, exactly and to all orders in Theta, for the commutator-type
(Phi-shift-symmetric) lift Xhat^mu = x^mu I + Theta^{mu rho} A_rho with the adjoint
connection on Phi; hence eq:dictionary is an identity at dictionary order for the adjoint
reading, with the even star-corrections beyond dictionary order controlled. Tier: E-in
(established derivation under the stated inputs: adjoint connection, embedding ansatz,
symbol-calculus correspondence; the ansatz items are inputs, not consequences of
eq:Smatrix). Anchors: T2a-T2j (generic symbolic Theta, n=2,3,4, A const/linear/quadratic,
Phi const/linear/quadratic-mixed, Hermitian A), T2k (monomial-class sweep at numeric
Theta with generic coefficients), T2l (Theta = 0 boundary: both sides vanish separately),
T2m (degenerate rank-2 Theta), T2n (Phi Hermitian-structured and general).

(b) Printed left action exactly incompatible. For the printed D_mu Phi = d_mu Phi -
i A_mu Phi of eq:Dmu-Phi, the A-linear mismatch of the identity is -Theta^{mu nu} Phi
*_star A_nu, a right-action product that no commutator produces (witness: nonzero for
generic data), and the central u(1) part of A is invisible to commutators while it is not
invisible in the printed left action; so no commutator-type lift reproduces eq:Smicro with
the connection as printed. The adjoint reading is a representation choice recorded as
datum D-120d (with quartic gauge coupling of Tr([A,Phi][A,Phi]^dagger)-type, which the
check pack sees as nonzero off vacuum). Tier: established identity/obstruction (E).
Anchors: T3a (mismatch identity, 4 symbol classes x 4 mu), T3a2 (constant-Phi witness
equals the right-action product exactly), T3a3 (teeth: mismatch nonzero for generic data),
T3b (u(1) invisibility witness), T8 (lift nonzero on linear Phi: quartic gauge-matter
coupling present in the class).

(c) Gaussian content bound to K-type. The shift-symmetric lift
-(kappa/2) int d^4x g^{mu nu} Tr([Xhat_mu, Phi]_star [Xhat_nu, Phi]_star), with
normalization kappa a datum (order Theta^{-2} against eq:Smicro, D-120a), has kinetic
tensor exactly proportional to K^{mu nu} of def:matrix-coords-ext (this pack: K = Theta g
Theta with the pack convention, opposite-sign under the transposed convention, T4b); for
real nonzero Theta, K = c g admits no real solution (sum-of-squares certificate T4c1/T4c2;
canonical block data T4d; numeric teeth T4e: K00 g22 - K22 g00 = -13 at (t01,t23)=(2,3)),
so the class never produces a g-type kinetic term, in agreement with the manuscript's own
non-proportionality record under ass:emergent-op; for purely spatial Theta, K is
degenerate with K^{0 mu} = 0 (T4g): Phi carries no time-derivative term. Tier: bound
established for the class (E-in). Anchors: T4a, T4b, T4c1, T4c2, T4d, T4e, T4g, T5d.

(d) Frame blindness, unique quartic W1, non-transfer. Writing Phi = phi0 I + Phi-tilde,
star-commutators with phi0(x) I collapse to i Theta^{mu nu} d_mu phi0-type terms (T5a
exact identity, T5b shift-invariance of the bracket), so the frame mode enters only
derivatively: no quadratic term and no X-dependent potential exists at any order in the
class (T5c: full star lift invariant under Phi -> Phi + s I exactly, via the exact bracket-congruence implementation of repair R3; T5d: frame lift is
exactly -(kappa/2) K^{bd} d_b phi0 d_d phi0 Tr(I); T5e: A = 0 constant Phi has zero
bracket and zero lift, so no mass term; T5f: at Phi = v I the bracket and lift vanish for
any A, so the gauge-quartic coupling vanishes on the vacuum and no gauge-boson mass
arises from the condensate). At the level X = Phi^dagger Phi: no nonzero quadratic
conjugation-invariant is shift-invariant (T6f, exact nullspace on the 6-dimensional
conjugation-invariant quadratic family), and at quartic order the X-free shift-invariant
sector is one-dimensional, spanned by W1 = Tr([Phi, Phi^dagger])^2, checked at matrix
sizes n = 2, 3 over the conjugation-invariant families (T6g/T6g2 uniqueness at n=2 with
the direction pinned to alpha*W1 exactly; T6i n=3 teeth: the four standard quartic
conjugation-invariants are all shift-variant); with C = [Phi, Phi^dagger] Hermitian,
W1 = Tr(C^dagger C) >= 0 with equality exactly for normal Phi (T6a algebraic identity,
T6b/T6c numeric teeth), hence W1 vanishes on all of v.U(n) (T6d: v.U(2) and v times
rational orthogonal 4x4) and locks nothing on eq:vacuum-manifold. W1 is not a function of
X: left multiplication by a fixed unitary preserves X and moves W1 from 0 to
(p1^2 - p2^2)^2 on diagonal Phi with distinct entries (T7a exact witness, T7b numeric
values W1 = 0 vs 9 at p = (2,1) with the degenerate boundary p1 = p2 giving 0, T7c
channel obstruction for any U with U^dagger U = I), so the induced W(X)-channel data of
the commutator class is (0, 0) for every group choice, the fixed-ray system of the 119
paragraph is vacuous on this branch, and the 119 channel data (A_G, B_G) do not transfer
to it. Tier: E-in under the branch hypothesis (class = commutator-type shift-symmetric
words, tested invariant families at n = 2, 3). The retention of the vanishing of the
W(X) sector to loops is a kinematic-symmetry argument NOT computed here (C); the loop
coefficient of W1 is not evaluated (I).

(e) True missing datum. What is missing for the selection of eq:V is not the ratio
r = c2/c3 and not the group: within this class it is a shift-BREAKING sector supplying
W(X), and every such sector carries its own instance of the 119 underdetermination. Tier:
U (missing datum located, not supplied; D-120c).

## What this does not do

- It closes nothing. The payload's last sentence states that the paragraph closes none of
  Problem D, Problem D1, or Problem A, and all three remain OPEN with the priorities the
  manuscript already records. No status, priority or completion label is proposed for any
  problem by this package.
- It does not derive eq:V, the vacuum selection, the frame-locking or eating mechanism, or
  any matrix-model state or dynamics; no Theta value is derived (D-120b); no claim is made
  that the adjoint reading is the one nature realizes (D-120d records the representation
  choice as a datum).
- It refines, and does not contradict, the integrated 119 paragraph: 119 records the
  selection of eq:V as a constrained but underdetermined datum in the Tr X^2, (Tr X)^2
  counterterm channels; 120 shows that the commutator class contributes exactly (0, 0) to
  that channel pair, so the datum cannot come from this class - the same gap, with a
  sharper location.
- Spacetime stays emergent: Theta is an input 2-form datum on the matrix coordinates and
  no fundamental metric or background spacetime is introduced anywhere in the payload or
  this proposal.

## Inputs and ansatze (assumptions, all recorded, none derived here)

1. Constant real antisymmetric Theta^{mu nu} (background specification = datum D-120b).
2. Weyl/Moyal symbol calculus as the semiclassical description of matrix commutators
   (star products computed exactly through the orders used; polynomial symbols of degree
   <= 2 per operand with the bilinear operator truncating the Moyal series at p = 2).
3. Embedding ansatz Xhat^mu = x^mu I + Theta^{mu rho} A_rho (Poisson-dressing
   identification: an input on the matrix coordinates, not a consequence of eq:Smatrix).
4. Connection on Phi read in the adjoint (commutator) sense; A_mu Hermitian matrix
   symbols (representation choice = datum D-120d).
5. kappa, the normalization of the quadratic lift, a datum of order Theta^{-2} against
   eq:Smicro (D-120a).
6. Matrix size and reality data of Phi (n = 2, 3, 4 with Hermitian and general Phi both
   tested); shift-preserving regularization at the cutoff of eq:LUV-def; quadratic and
   quartic order for the class invariants.

## Research and reasoning (derivations live in the record; this file points, does not re-derive)

Stage-1 record: scratch/120/notes.md, sections S0-S8 plus appendix; preliminary
disposition at L43, final S8 DISPOSITION at L178-191 ("STAGE 2 WARRANTED... Tier:
established derivation UNDER the stated ansatz... nothing closes"). Stage-1 scripts
s2b (bridge identity), s2c (lift, kinetic tensor, frame), s3a (quadratic/quartic shift
invariants), s3b (frame blindness and W1 non-transfer); this folder carries their re-run
captures, byte-identical to the stage-1 pins recorded in reports/ledger.md
(CHAIN-120-S2-DEATH-RESUME): out-s2b-bridge-r1.txt 9c14be97058a/828 (SUMMARY pass=3
fail=0), out-s2c-lift-r1.txt b27a498ec4b2/1645 (pass=7 fail=0), out-s3a-quartic-r1.txt
1b01e527846c/1362 (pass=18 fail=0), out-s3b-frame-r1.txt 0bc923bb8d5e/451 (pass=5 fail=0).

Stage-2 verification pack (independent code path, same mathematics, fresh machinery):
verify_r120.py, pin <<VERPIN>>; canonical capture out-r120.txt <<R120PIN>>/<<R120SIZE>>,
ending <<TOTAL>> + "ALL CHECKS DONE 120". Clause-to-check mapping with capture line
numbers (grep-stable):

| clause | chk ids | out-r120.txt lines |
|---|---|---|
| payload integrity | P1-P8 | <<LINES-P>> |
| (a) bridge identity | T2a-T2n | <<LINES-T2>> |
| (b) left-action obstruction | T3a, T3a2, T3a3, T3b, T8 | <<LINES-T3>> |
| (c) K-type bound | T4a, T4b, T4c1, T4c2, T4d, T4e, T4g | <<LINES-T4>> |
| (d) frame blindness | T5a-T5f, T5c-teeth | <<LINES-T5>> |
| (d) W1 sector | T6a-T6i (incl. T6g2) | <<LINES-T6>> |
| (d) non-transfer | T7a, T7b, T7c | <<LINES-T7>> |

Literature: the payload carries no citations (P4 checks absence of \cite); the Weyl-Groenewold
star-truncation computation is recomputed in this pack rather than cited, so no external
record required independent verification for this package.

## Verification scripts (reproduction pack; all paths in this folder)

- `python -I -B verify_r120.py` -> per-check "PASS ..." lines, then "<<TOTAL>>" and
  "ALL CHECKS DONE 120"; expected invariants: P1 matches payload pin, all chk lines
  PASS, zero FAIL. Capture: out-r120.txt.
- `python -I -B patch_r2_simplify.py` -> "PATCH R2 VERIFIED (idempotent) ... new pin ..."
  and "CONTROL OK 120R2"; re-derives the whole check-side repair chain (R1 T5c rewrite +
  R2 simplify_sym) from verify_r120-preR1.py (54ec6b20233b/34530) and re-checks pins, a
  byte-exact re-derivation of the current verify_r120.py, 4 string controls and
  py_compile. Capture: out-patchR2.txt (the intermediate R1 step also has its own script
  patch_r1_t5c.py and capture out-patchR1.txt).
- `python -I -B repair_chain120.py` -> "CHAIN OK 120": rebuilds the whole check-side repair
  chain (R1+R2+R3) from verify_r120-preR1.py in a temp dir, byte-compares to the current
  verify_r120.py, and audits that all pre-repair chk claim strings occur verbatim in it.
  Capture: out-chain120.txt.
- `python -I -B gen_payload_120.py` -> "GEN OK 120", payload 343226e27ebf/5138, POST
  853982 (= 848842 + 5138 + 2) sha1 d5e2e67c0a63ad3b0bce6034f2985ea94b9f3274, 12 positive
  controls fired. Captures out-gen120-a.txt == out-gen120-b.txt (twice byte-identical).
- `python -I -B cert-r120p.py` -> "CERT PASS" (baseline appH 9e0b198af2c3/848842, anchor
  1 @ 295299, two pdflatex passes rc=0, 0 '!' lines, 0 undefined/multiply-defined).
- `python -I -B check_labels120.py` -> "LABELS OK 120" (all 11 referenced labels defined
  exactly once). Capture: out-labels120.txt.

## Verify-pack repair log (S2-final)

Full log: verify_repair_log.txt. Summary: R0 observability (buffered stdout made two runs
look dead at 0 bytes; killed, raw captures kept as out-r120-fail1.txt, out-r120-fail2.txt);
R1 the chunk-assembled T5c expanded and simplified a quartic form in 44 generic symbols
(replaced by an exactly-equivalent unexpanded comparison plus a non-vacuity tooth; bytes
preserved as verify_r120-preR1.py 54ec6b20233b/34530; step capture out-patchR1.txt); R2
after R1 the stall recurred at the same gap (40+ min, raw capture out-r120-fail3.txt) and
was localized to simplify_sym's per-coefficient sp.simplify heuristic, removed as
unnecessary (coefficients are pre-expanded; bytes preserved as verify_r120-preR2.py
610a2c6c7a32/36376); R3, after a third stall (raw capture out-r120-fail4.txt),
probe_t5c.py timed the residual cost (out-probe-t5c.txt: each generic-symbolic
lift_from_B call ~50 min on 21100-entry star lists, mats_eq 1 s) and T5c was re-proved
by exact bracket congruence plus 6 deterministic integer-draw lift evaluations (claim
string verbatim; bytes preserved as verify_r120-preR3.py b71430a6ebf3/36449).
repair_chain120.py re-derives preR1 -> R1 -> R2 -> R3 byte-exactly, verifies every
pre-repair chk claim string still occurs verbatim, and prints "CHAIN OK 120"
(out-chain120.txt). Final verify pin <<VERPIN>>. All repairs are check-side cost/
observability fixes: no chk deleted, narrowed or renamed; no payload edit at any point.

## Decisions Taken

- This is the third attempt at chain-120 stage 2; the two prior deaths (API
  prompt-too-long) are pinned in reports/ledger.md at CHAIN-120-S2-DEATH-RESUME and
  CHAIN-120-S2B-DEATH. This run enforced bounded reads (tails and <= 150-line windows)
  and immediate persistence of every artifact.
- Payload, generator and certificate were treated as fixed inputs (their pins and PASS
  captures predate this round); nothing under insert-commutator-lift-r1.tex,
  gen_payload_120.py, cert-r120p.py changed.
- When verify_r120.py produced 0-byte captures twice (once as a pre-dispatch orphan at
  30+ min, once at 8 min), I diagnosed rather than accepted "hang": unbuffered re-run
  localized the stall to T5c; the fix rewrites the check implementation only (exact
  same claim, same inputs, added control), per the rule that check-side defects may be
  repaired but claims may not be weakened. Chose the structural-lift proof over numeric
  sampling because numeric sampling would have weakened the "exactly" in the claim.
- When the R1 rewrite did not clear the stall (40+ min at the same gap; capture kept as
  out-r120-fail3.txt), I localized the remaining cost to simplify_sym's per-coefficient
  sp.simplify and removed that heuristic call (R2): coefficients there are pre-expanded,
  so Add/Mul canonicality plus the existing equality tests preserve every claim. Rejected
  alternatives: numeric sampling of the coefficient matrices (would weaken the "exactly"
  in the T5c claim), per-check timeouts or file splits (fragment the single-TOTAL
  convention), and running the 30-min expand job as-is (no evidence it terminates).
- When the post-R2 run still stalled (~38 min, out-r120-fail4.txt), I instrumented the
  region with probe_t5c.py instead of guessing again: the two generic-symbolic lift
  evaluations cost ~50 min each while the bracket comparison costs 1 s. Since lift_from_B
  is a deterministic program in the four bracket polynomials, I re-proved T5c by exact
  bracket equality plus substitutivity, adding 6 deterministic integer-draw lift
  evaluations as a same-program cross-check (R3). Rejected: keeping the intractable
  expansion (blocks the whole pack for ~2 h per run), random-draw-only or
  sampling-only verification (would weaken "exactly"), and deleting T5c.
- Proposal register mirrors the payload clause structure clause-by-clause so the
  gatekeeper can align payload line, proposal clause, and chk ids one-to-one.
- Rejected alternatives: splitting verify_r120.py into per-clause scripts (loses the
  single TOTAL line the chain convention records); deleting T5c (weakens the class
  claim); re-running the 30-min expand job on a faster loop (no evidence it terminates).

## Author-datum list (recorded in text, not decided here)

- D-120a: kappa normalization of the quadratic lift (order Theta^{-2} against eq:Smicro).
- D-120b: Theta background specification (constant real antisymmetric datum on the matrix
  coordinates; no derivation claimed).
- D-120c: the shift-breaking W(X) sector supplying the selection datum (the located
  missing datum; carries its own 119 underdetermination).
- D-120d: adjoint-vs-left-action representation choice for the connection on Phi
  (eq:Dmu-Phi prints the left action; the class requires the adjoint).

## Milestone assessment

Routine probe-record package: no MILESTONE.md trigger is claimed. The package relocates
and sharpens the D1 selection datum (positive derivation-grade output for the named
missing step "what constrains eq:V") and records the exact class in which the dictionary
bridge is a derived identity; it closes no critical-path problem.

## Status-label recommendation

Unchanged for every problem. Derived from the live sources as recorded in "Target and
status" above: A OPEN/CRITICAL PATH; D OPEN/CRITICAL PATH/PROGRAMME-CONDITIONAL; D1 and
the rest of the Chapter 17 full-GR criterion set as the ledger snapshot lists them. This
package proposes no label change.

## Author decision needed

None. D-120a-d are inputs recorded by the text; none changes a label, the Chapter 17
scope, the critical-path set, or a core assumption, and spacetime stays emergent.

## Remaining open step

For the D1 selection datum: a concrete shift-breaking sector supplying a nonzero W(X)
(D-120c), with its own analysis against the 119 underdetermination. For the bridge
clause: dropping the embedding ansatz to a consequence of eq:Smatrix, or replacing it by
a lift derived in the matrix model, remains open; deriving Theta (D-120b) and the
representation choice (D-120d) remain open; loop-level retention of W(X) = 0 and the loop
coefficient of W1 are not computed. None of these is closed by this package.

## Special instructions for the gatekeeper

- The payload is fixed at <<PAYPIN>>; check the proposal clauses against the payload
  line by line (payload has exactly 8 lines; clause map in "Central claim").
- Re-run the reproduction pack; the canonical verify command is `python -I -B
  verify_r120.py` and the run ends <<TOTAL>> / "ALL CHECKS DONE 120". Raw failed
  iterations out-r120-fail1.txt (0 B, killed), out-r120-fail2.txt (stall at T5c, killed)
  are kept unedited.
- Repairs R0-R3 touched check code only: run repair_chain120.py (temp-dir rebuild of
  preR1 -> R1 -> R2 -> R3, byte-comparison to the current verify_r120.py, chk claim-string
  census; "CHAIN OK 120"), and confirm against verify_r120-preR1.py (54ec6b20233b/34530)
  that every pre-repair chk id still occurs with identical claim text, that the T5c claim
  string equals the old one, that the simplify_sym change is only the removal of the
  per-coefficient sp.simplify cleanup call, and that the T5c replacement block proves
  L(Phi + s I) = L(Phi) by exact bracket equality (mats_eq) plus 6 deterministic
  integer-draw evaluations of both lifts with identical substitutions per draw - an
  exact route substituting for the intractable full generic-symbolic expansion timed by
  probe_t5c.py; no chk name deleted, narrowed or renamed.
- Anchor facts for integration if ACCEPT: anchor "\section{Problem E: signature}" in
  chapters/appH-microscopic-proofs.tex, count 1 at byte 295299; POST 853982
  d5e2e67c0a63ad3b0bce6034f2985ea94b9f3274 (= baseline 848842 + payload 5138 + 2,
  blank-line join). It must not be asserted that any problem closes, and no
  frame-locking, mass, or W(X)-channel claim may be attributed beyond the branch
  hypothesis stated in the payload's "Hypotheses and limits" line.

## Triage r1 (49/53) - 2026-11-23, R4
- T6f: check-side vacuous pass (right-nullspace + all-entries shift map); truth: quadratic shift-invariant subspace = 3-dim traceless-part span, Tr X direction shift-variant; re-scoped (probe-r4-heavy2.txt).
- T6g: check-side bugs (transpose, shift map, W1 word) PLUS genuine payload defect: quartic shift-invariant sector of the n=2 family is 4-dim (W1 direction + 3 traceless-part invariants), not 1-dim spanned by W1 (probe-r4-heavy2.txt).
- T6h: check-side wrong word identity; true identity W1 = 2Tr(P Pd P Pd) - 2Tr(P^2 Pd^2) = Tr(C^dag C), verified symbolically and numerically (probe-r4-fast.txt P0/P2).
- T7c: check-side missing unitarity normalization (U^dag U = (|al|^2+|be|^2)I); true statement (U2 Phi)^dag(U2 Phi) = norm Phi^dag Phi verified exactly with real-parameter U(2) plus non-normalized teeth (probe-r4-fast.txt P1; p1 run True).
## Payload r2 scope fix (supersession, 2026-11-23)
- Paragraph-5 scope fix per R4 findings (T6f/T6g genuine payload defect). Minimal corrected wording
(A) 'no shift-invariant term is a function of \(X\) at quadratic order, \(X\) itself being
shift-variant' replaces 'no quadratic shift-invariant term exists'; (B) the quartic claim becomes
'at quartic order the shift-invariant sector of the checked conjugation-invariant family is
four-dimensional, spanned by \(W_1=\operatorname{Tr}([\Phi,\Phi^\dagger])^2\) and three
invariants of the traceless part \(\widetilde\Phi=\Phi-(\operatorname{Tr}\Phi/2)\,\mathbb I\)
(checked at matrix size \(2\))'; (C) 'so this quartic locks nothing'. The verifier MARK string for
W1 is preserved; paragraph 6 (W(X)-channel) untouched (uses only T7). Diff: payload line 5 only
(9-line file, 1 changed line); generator source line 31 only; fix script fix_para5.py.
- Pins: payload 343226e27ebf/5138 -> a5aa77dc90a3/5287 (old archived byte-identical as
insert-commutator-lift-r1-superseded-r1.tex); gen_payload_120.py 3eab305230b3/10229 ->
67cee1fbc771/10378 (archived gen_payload_120-superseded-r1.py). Gen run twice: outputs identical
(out-gen120-c.txt == out-gen120-d.txt). POST 853982 -> 854131 (= 848842 + 5287 + 2),
POST_SHA1 f5a761c55396faf78bb5f6d74693c5193bafbea0 (from gen).
- R5 (constant-only re-pins, fix_r5.py; rationale appended to verify_repair_log.txt '## R5'): new
payload exceeds the P8 chain-119 ceiling 5191, so verify_r120.py 4d751ac4afb8/39745 ->
dac3381f5dc8/39762 (P1 payload pin re-pinned; P8 ceiling 5191 -> 5340, chain-119 +53 margin kept;
pre-R5 copy verify_r120-preR5.py) and cert-r120p.py 1bf4a61b1597/4781 -> c633cbdc2288/4781
(PAY_SHA1_12/PAY_SIZE/POST/POST_SHA1; pre-R5 copy cert-r120p-preR5.py). Note: R5 necessarily also
covered the P1 and cert payload pins, which pinned the superseded bytes; constants only, no logic
edits, no tier-word changes.
- assemble_pr1.py tweaked (now 4eb619312b8c) to read the capture from %CAP120% or the newest
existing of out-r120-rerun3.txt / out-r120-rerun2.txt. This proposal-r1.md was assembled from the
rerun2 (old-payload, green) capture: TOTAL/R120PIN/LINES-* therefore cite rerun2 until refreshed.
Re-run assemble_pr1.py after out-r120-rerun3.txt is green to refresh them on the new payload.
Background chain bv8szddan: cert-r120p.py -> out-cert-r120p-r2.txt, then verify_r120.py ->
out-r120-rerun3.txt.
- Refresh (2026-11-23, same dispatch): background chain bv8szddan exited 0. out-r120-rerun3.txt 0950831e672d/4610 = TOTAL 53/53 PASS + ALL CHECKS DONE 120 with zero FAIL lines on the NEW payload a5aa77dc90a3/5287; out-cert-r120p-r2.txt 53787eb3cf34/418 = CERT PASS. proposal-r1.md re-assembled from the rerun3 capture (CAP120 unset, fallback picks rerun3): TOTAL/R120PIN/LINES-* now cite rerun3; the preceding bullet's rerun2-capture note is superseded by this line.
