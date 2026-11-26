# Proposal 090-g-interaction-induced-simplex-profiles, round 2

Round-2 note. Single mechanical quantifier fix per review-r1 (ACCEPT WITH REQUIRED REVISIONS,
16,138 B / sha8 29ed2d57). No new mathematics; all r1 files frozen and hash-checked by the r2
scripts. Canonical new artifact: `insert-r2.tex`, 3,894 B, sha8 2f868a49 (r1: 3,735 B / 3a6a69c4;
delta +159 bytes = F1 +114, F2 +12, F3 +33).

## Result

insert-r2.tex states the concavity/existence sentence with the correct quantifiers on the beta=0
corners and keeps every other claim, number and closer byte-identical to r1. Classification is
unchanged from r1 (PROVED layer inside a named input family; matrix-origin of the beta factor NOT
established; Problem G and `G.moments-interaction-nonconvex` remain OPEN).

## Findings addressed, point by point

- F1 (major): OLD "strictly concave for \(a\ge 1\), so for \(a>1\) it has exactly one stationary
  profile there" replaced by the review's clause, extracted from review-r1.md bytes with
  html.unescape only (never retyped): "strictly concave whenever \(a>1\) or \(\beta>0\); for
  \(a>1\) and \(\beta>0\) it has exactly one stationary profile there, while for \(\beta=0\) its
  unique stationary point on the simplex is the barycenter". Both false corners (log-weight
  identically 0 at a=1,beta=0; barycenter outside the open chamber at beta=0,a>1) are now excluded
  by the wording. Verified: new clause count 1, old string count 0 in r2.
- F2 (minor): "at any deformation strength" now reads "at any deformation strength
  \(\beta>0\)" (new string count 1; the containment of the old phrase inside the new one is
  bookkept explicitly by the fix script, since a literal 1->0 count is impossible for this
  replacement).
- F3 (minor, optional - taken): D=2 sentence now reads "... is
  \(u=\sqrt{\beta/(\beta+2(a-1))}\) (at \(\beta=0\), the barycenter) with log-weight curvature
  ..." (parenthetical extracted from the review; anchored on "with log-weight curvature" to keep
  the closed-form math span untouched; new clause count 1).
- F4 (minor, no action): no text change; the r1 scoping of "residuals below 10^{-28}" to the cited
  beta=1 profiles stands as the review confirms (1.1e-29 / 1.58e-29 recomputed by the gatekeeper).

## Verification (r2, all shipped with .out)

- fix_insert_090_r2.py: byte surgery from frozen insert-r1.tex (pre-assert 3,735/3a6a69c4);
  per-step counts 1->0 (except F2 containment, documented), new clauses 1 each; ASCII; no control
  bytes; terminal CRLF; \( \) balance 58/58; prints size/sha8 and delta arithmetic.
  History note: interim v1 had a wrong F1 end-marker and v5/v6/v7 had F3 anchoring errors caught
  by the asserts (a v7 run left a transient broken insert-r2.tex which the passing v8 run
  overwrote; the shipped file is the v8 output, hash-verified downstream). The canonical script is
  the v8 content.
- hygiene_090_r2.py: PASS on insert-r2 (banned map empty, macros 0, brackets 0, single CRLF line,
  closer 1, header 1 in insert / 0 in PRE appH); also asserts frozen r1 3,735/3a6a69c4.
- smoke_compile_090_r2.py: SMOKE GATE OK - POS insert-r2 rc=0 (article+amsmath,amssymb, in-folder
  scratch_latex), NEG (\lvert to \lvertz, in memory) rc=1 with Undefined control sequence; frozen
  r1 hash-checked.
- simulate_apply_090_r2.py: PRE live appH re-verified 752,790 B / sha 4b521316...2068d6 / CRLF
  3,842 / PIN count 1; read-only; outside-window identity True; NEW POST 756,686 B
  (= 752,790 + 3,894 + 2, matching the review's "insert size + 2" rule), sha256
  068ce3f21139911ee7beccd6086b85a4ad18b19df683918ee4beb67b2963df38, CRLF 3,844, lone-LF 0;
  layout L3191 089 / L3193 new / L3195 Vacuum.

## Integrator note

Integrate `insert-r2.tex` (not r1) per review-r1 "Final integration instructions"; re-derive PRE
live immediately before splicing (working tree is dirty); POST to verify against the numbers above.

## Milestone assessment

Routine (same as r1; the review concurs: no M1-M5 trigger).

## Status-label recommendation

Unchanged: none. Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

Unchanged from r1: derive the interaction (pair-repulsion or relabelling-asymmetric non-convex)
factor from the core matrix theory or a derived non-product slot law; the edge's DERIVED-density
requirement is untouched.

## Special instructions for the gatekeeper

Verify r2 differs from r1 only inside the three edited regions (character-level difflib opcodes merge to exactly 3 regions after gap-merge at 30 B: byte offsets 1336-1524, 1820-1946, 2281-2440 of r1; the file tail, including the closer, is byte-equal), the
extracted clauses match review-r1.md's unescaped text, and the new POST numbers reproduce.
