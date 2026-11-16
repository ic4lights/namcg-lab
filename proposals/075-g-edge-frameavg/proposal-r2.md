# Proposal 075-g-edge-frameavg, round 2

Revision round in response to `review-r1.md` (verdict ACCEPT WITH REQUIRED
REVISIONS | MILESTONE none | FLAGS none | PROGRESS first | OPEN 0/1). The
gatekeeper verified the package's mathematics in full and independently and
required exactly one wording correction to the insert. This round applies that
correction, regenerates the length-sensitive byte contract against the live
tree, and changes nothing else. No computation was redone: all research
scripts and outputs are byte-unchanged from round 1 and were re-verified by
the gatekeeper in review-r1 (reproduction pack r1-r8 byte-identical to the
gatekeeper-reviewed 073/074 shipped files; every `.out` byte-reproducible).

## Result

Unchanged from round 1 (proposal-r1.md, "Result" and "Research and reasoning"
sections, whose cited numbers all appear verbatim in the byte-unchanged shipped
`.out` files): within the (H1)-(H4) class extended by cap frames, the fixed
frame vacuum-term excess extends to the cap-frame (rank-M spectral projector)
average; the frame dependence factors exactly through two edge-length fractions
entering additively through a profile strictly increasing and strictly concave
in the fraction; on the mean-preserving family (E_n rho = 1, tr B = 3) the
sphere mean is at most the round-frame value 0.523248144 = log(27/16) with
equality iff B is proportional to the identity, and at least the strictly
positive most-contracted-frame value; stacked rows scale by depth; finite-N
residuals are frame-uniform on the tested range; nothing in Problem G is
closed. The only change in r2 is that the insert's upper-bound clause now makes
the mean-preserving condition explicit in the sentence itself (finding 1).

## Target and status

Unchanged from round 1. Problem G: Status OPEN, Priority CRITICAL PATH,
Completion PROGRAMME-CONDITIONAL (labels quoted, not touched). Frontier edge
G.edge-frameavg: bounded conditional computation of the cap-frame average of
the excess; DERIVED not claimed; no label change proposed.

## Finding-by-finding disposition

| # | severity | disposition |
|---|---|---|
| 1 | MAJOR (blocking) | FIXED. In `insert-r1.tex` the clause "to the sphere mean of the defect function, which by concavity is bounded above by the round-frame value \(0.523248144\), attained only when the edge data are of the round frame, and bounded below by" is replaced, verbatim per the review's "Corrected snippet", by "to the sphere mean of the defect function, which, when the sphere mean of the edge-length fraction equals its round-frame value, is by concavity bounded above by the round-frame value \(0.523248144\), attained only when the edge data are of the round frame, and bounded below by". The replacement is unique in the insert (asserted count 1 on the old bytes, 0 of the new clause before writing). This is exactly the condition the proposal body already imposes (E_n rho = 1, equivalently tr B = 3); the counterexample B = 2I (sphere mean 0.678355 > 0.523248144) is now excluded by the sentence itself. The lower-bound clause keeps no proviso (strict monotonicity alone, as the review confirms). No other text in the insert changed. |
| 2 | minor (proposal record) | ADDRESSED by this note: the concavity used for the Jensen upper bound is concavity in the edge-length fraction rho (verified symbolically: R_u > 0, R_uu < 0 and d^2[R(1/2,1,sqrt(rho)/2)]/d rho^2 < 0 on the frame orbit), not concavity in z = cos(theta); the round-1 z-route justification (increasing concave of concave in z) is not true for gamma < 1 and is withdrawn as a justification. The corrected insert sentence routes the bound through rho-concavity plus the stated mean-preserving condition E_n rho = 1; no manuscript text beyond finding 1 changes. |
| 3 | minor (optional wording) | NO CHANGE. The review confirms the closing parenthetical "(numerical, via the exact closed form, N up to 3200)" already scopes the residual sentence correctly and no change is required; the optional "consistent with" substitution is declined to keep the r2 diff to the single required clause (smaller text = smaller re-verification surface; the numerical status is unambiguous as reviewed). |
| 4 | minor (favourable) | NO CHANGE. The review confirms the s^2(n) formula is an exact theorem of the class while the insert claims only roundoff-verified re-establishment; the modest wording stays. |
| 5 | none | Nothing to do; noted for the record (anchor unique, manifest 38/38 at r1, outputs byte-reproducible, byte contract independently reproduced, status lines intact). |

## Insert (r2, corrected; single ASCII line + terminal CRLF)

File `insert-r1.tex` (filename kept per the review's disposition instruction;
the integrated text is what matters, not the version label of the shipping
file). New size 3,255 B (+80 vs r1), sha256
`6801fc391a0435bc4e4ff405be30eeabc99e5b1373ebedb9e0c2efc43c2b53c5`, single
line + terminal CRLF, bareLF 0. Hygiene re-asserted on the new bytes: zero
`$`, `\ref`, `\eqref`, `\label`, `\cite`, `[`, `]`; no status vocabulary
(status/priority/completion/open/derived/programme/critical); no trailing
whitespace; `\emph{Vacuum term.` count 0; header `\emph{Frame average of the
fixed-frame excess at the saddle.}` count 1. Verbatim (single line):

```latex
\emph{Frame average of the fixed-frame excess at the saddle.} Under the same hypotheses as the three preceding paragraphs, and within them, the fixed-frame excess extends to the average over cap frames: deforming a factor by a real matrix, with Gram matrix \(B\), the squared edge length of a cap with axis \(n\) is one quarter of \(M(N-M)\) times the trace of \(B\) restricted to the plane orthogonal to \(n\), a general-axis case of the edge-datum identity above, re-established here by direct block computation at small sizes to within roundoff, so the saddle rows and the continuum defect depend on the frame only through the two edge-length fractions, which enter the defect additively through a per-factor profile that is strictly increasing and strictly concave in the fraction. Averaging the two cap axes independently and uniformly over the sphere, the frame-averaged defect per \(N\) converges, with per-frame finite-\(N\) residuals bounded independently of the frame (at most \(7.7\) for the two-row defect and \(59.8\) at depth three, \(N\) up to \(3200\), against the uniform residual bound of the second preceding paragraph), to the sphere mean of the defect function, which, when the sphere mean of the edge-length fraction equals its round-frame value, is by concavity bounded above by the round-frame value \(0.523248144\), attained only when the edge data are of the round frame, and bounded below by the strictly positive value at the most contracted frame, attained at the axis of the largest eigenvalue of \(B\): for the mean-preserving axisymmetric family of axial parameter \(\gamma\), the averaged limit is \(0.522655,0.519217,0.511350\) and the frame minimum is \(0.479485,0.396700,0.268892\) at \(\gamma\) equal to \(1.4,2,2.6\), so that the average and the minimum of the defect over cap frames remain extensive and strictly positive at every tested non-degenerate deformation, the lower bound tending to zero only as the transverse edge data of a factor degenerate, while the round-frame value is an upper bound rather than the value of the average (numerical, via the exact closed form, \(N\) up to \(3200\)). The stacked-row excess obeys the same average, with limit equal to the depth times the averaged profile and residuals of the same order (numerical, depths up to \(3\), \(N\) up to \(3200\), reproducing the integrated isotropic values at the round frame); the corner-mode fraction of the selection data stays \(O(1/N)\) uniformly over the frames tested (between \(0.9423\) and \(2.4484\) for axial parameters up to \(2.6\)), the saddle rank ratio stays between \(0.7858\) and \(0.9023\), and the large-perturbation breakdown boundary of the second preceding paragraph is untouched by the frame average, which acts on the diagrams at fixed saddle data. These statements are for cap frames of the product testbed within the dominant-representation class of the three preceding paragraphs with the saddle parameter held fixed, rows in two stacks of equal length and depths held fixed; they are not the full frame average or the minimisation over frames of the leading reference, they leave the selection of the diagram, the monotonicity statement and the items (i)-(iii) unchanged, and they close nothing in Problem~G.
```

This fenced line is byte-equal to the line in `insert-r1.tex` (asserted
programmatically when this file was written: placeholder replaced by the exact
file bytes minus the terminal CRLF).

## Byte contract (r2; live-verified 2026-11-16)

Live PRE pins re-verified before applying the fix; they match the pins recorded
in review-r1:
- appH PRE: 700,825 B / sha256
  50f12c8131819f513ff37d5149529ba616063578b04510891a6b7f1d43b8f25e / CRLF 3814
  / bareLF 0.
- bib PRE: 37,463 B / sha256
  4d6d7b2a668fdaa64663e624b3f296d833c3bbcaa06a74ec5012a7f494ce0de6 / CRLF 1239
  / bareLF 0 (unchanged; no bib modification proposed).

Anchor checks pass live (short `\emph{Vacuum term.}` x2, long form x1,
line-start long form x1; new header x0).

POST (from the fresh `simulate_apply` run on the corrected insert,
`simulate_apply.out`, reproduced byte-identically by a second run
`simulate_apply.repro.out`, cmp-clean, stderr empty, exit 0):
- appH POST: 704,082 B / sha256
  58eb0c7fa4a360d4c9f2fc400c5112555d8b7480fe0873ae9b35a07f57c6e5e0 / CRLF 3816
  / bareLF 0 (delta +3,257 B = 3,255 insert + 2 CRLF; +2 CRLF).
- bib POST: unchanged, byte-identical to PRE.

Integration instruction unchanged (review-r1, "Recommended disposition"):
insert the single line + one blank CRLF line immediately before the unique
line-start paragraph `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}`
inside the Problem G block; the integrator must re-verify the anchor and the PRE
pins against the live tree at integration time (they matched when r2 was
written); no other byte changes; then `python scripts/build_check.py` and
`python scripts/make_digest.py`.

## Verification scripts and reproduction pack

Unchanged from r1 (see proposal-r1.md, "Verification scripts"): s1, s2, s3,
r1-r8 and all their `.out`/`.repro.out` files are byte-unchanged; the expected
invariant outputs r1..r8 are exactly those the gatekeeper already verified
against byte-identical copies of the 073/074 shipped files and fresh runs in
review-r1 ("Checks performed"). The only regenerated artefacts are
`insert-r1.tex`, `simulate_apply.out`, `simulate_apply.repro.out` (new byte
contract). Reproduction for r2:

- `python -I proposals/075-g-edge-frameavg/simulate_apply.py > ...out 2>...err`
  from the repository root: expected exit 0, empty stderr, and the lines
  "appH pre  bytes 700825", "appH post bytes 704082 sha256 58eb0c7fa4a3...",
  "delta appH: bytes +3257 CRLF +2 bareLF +0" (the file uses CRLF endings, as
  all shipped `.out` files do; cmp the fresh run against the shipped
  `simulate_apply.out`).
- Invariants of the corrected insert (mechanical): `insert-r1.tex` is 3,255 B,
  sha256 6801fc391a0435bc4e4ff405be30eeabc99e5b1373ebedb9e0c2efc43c2b53c5, one
  CRLF (terminal); it contains the corrected clause "which, when the sphere
  mean of the edge-length fraction equals its round-frame value, is by
  concavity bounded above" exactly once and the old clause "which by concavity
  is bounded above" zero times.

Mathematical invariants behind the corrected sentence, as verified by the
gatekeeper in review-r1 (not redone here): strict concavity of the profile in
rho (symbolic); E_sphere rho = tr B/3 (symbolic), so E_n rho = 1 iff tr B = 3;
Jensen E[P(rho)] <= P(1) with equality iff rho = 1 a.e. iff B proportional to
I; strict monotonicity gives the lower bound at the largest-eigenvalue axis,
strictly positive for non-degenerate B.

## Source reading

r2 is a wording revision with no new claims: r1 source reading stands (digest +
targeted reads; appH never read whole; the anchor region L3022-3170 read in
full then). This round: review-r1.md, proposal-r1.md, insert-r1.tex,
simulate_apply.py/.out, manifest.md read in full; live PRE pins and anchor
counts re-verified by the regenerated simulate_apply run (digest not relied
on). No chapters/ or bib/ file was read or written beyond the read-only pin
hashes.

## Claim classification

Unchanged from r1 except that the upper-bound clause in the integrated text is
now explicitly conditioned on the mean-preserving normalization (E_n rho = 1,
equivalently tr B = 3), matching the already-established conditional
classification (Jensen bound on the mean-preserving family: established within
the class; its unconditional version was FALSE per the review's B = 2I
counterexample and is not claimed anywhere in r2).

## Decisions Taken

1. Kept the filename `insert-r1.tex` for the corrected insert rather than
   creating `insert-r2.tex`. Reason: the review's disposition says "apply the
   corrected sentence (snippet below) to insert-r1.tex" and the integrator and
   simulate_apply.py both reference this path; the proposal text (this file)
   carries the round versioning. Rejected: a second insert file (two candidate
   inserts in one folder is an integration hazard).
2. Declined the optional "against" -> "consistent with" wording change
   (finding 3). Reason: the review itself rules no change required; minimizing
   the r2 diff to the single mandatory clause reduces re-verification surface.
   Rejected: bundling an optional wording tweak into the required revision.
3. Applied the gatekeeper clause verbatim, character-for-character, including
   the comma structure ("which, when ... value, is by concavity bounded
   above"). Reason: it is the reviewed string; any paraphrase would void the
   review's clause-level verification.

## Milestone assessment

Routine (unchanged from r1): no milestone trigger applies; conditional testbed
evidence inside the integrated 065 block; no critical-path step derived.

## Status-label recommendation

Unchanged: re-derived from ch17 (L474-497 region) and the Appendix H ledger
lines, the current critical-path set at the full-GR scope is A, B, C, D1, E, F,
G-derived, N (H, I, J optional). Problem G remains OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL. Affected labels: none.

## Author decision needed

None.

## Remaining open step

Unchanged from r1 (proposal-r1.md, "Remaining open step"): beyond cap frames
(conjugacy-class projector average; joint frame-diagram minimisation) and, for
Problem G itself, the missing steps (i)-(iv), two-sided diagrams, minimised
block entropy; selection-rule transplant (H2) still supplied. The review's
ranked avenues (proved frame-uniform residual bound; full conjugacy-class
average with the 2408.05274 saddle template; uniform-in-gamma positive lower
bound; 065 selection-rule transplant) stand as the queue.

## Special instructions for the gatekeeper

- The only mathematical content change is the explicit mean-preserving
  proviso on the upper-bound clause; everything else in the insert is
  byte-identical to what review-r1 verified. Please verify (a) the corrected
  clause is character-identical to your "Corrected snippet" (modulo the
  surrounding unchanged text), (b) the new insert size/sha and the new POST
  contract 704,082 B / 58eb0c7fa4a3... / CRLF 3816 / bareLF 0 against the live
  tree at review time (PRE pins must match at that moment; if the tree has
  moved, re-run simulate_apply.py, which asserts the pins), (c) that no other
  line of any shipped script/out changed (they should be at their r1 hashes;
  manifest.md is updated only for insert-r1.tex, simulate_apply.out,
  simulate_apply.repro.out plus the new proposal-r2.md / review-r1.md
  entries), (d) the hygiene profile on the new bytes.
- Must NOT be asserted (unchanged): that the full frame average or the
  FlissFrenkelHartnollSoni2025 minimisation was computed; that anything in
  Problem G or items (i)-(iii) is closed; uniform-in-all-deformations
  positivity of the lower bound; and now explicitly, the upper bound must not
  be quoted without the mean-preserving condition that is in the sentence.
- This round introduced no new mathematics; no re-derivation beyond the byte
  contract is needed to verify r2.
