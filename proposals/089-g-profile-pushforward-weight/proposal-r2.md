# Proposal 089-g-profile-pushforward-weight, round 2

Round 1 verdict: ACCEPT WITH REQUIRED REVISIONS (review-r1.md, 19425 B / sha8 c52d2e82). The mathematics is ACCEPTED; round 2 applies only the gatekeeper wording fixes F1/F2 verbatim plus folder fixes F4/F5. No new derivations, no changed claims, no label touched.

## Findings disposition
- F1 (major, required): DONE. The wider-product-class sentence is replaced by the gatekeeper Corrected-snippet replacement, adopted verbatim (review-r1.md, Corrected snippet). This is changed span 3: old 410 B at insert-body offset 2862 -> new 461 B. Machine-confirmed: the new span bytes occur as a substring of review-r1.md.
- F2 (minor, required): DONE. Span 1 (offset 2027): "and has its unique minimum at the vertex of the largest slot variance:" (70 B) -> gatekeeper replacement (152 B). Span 2 (offset 2175): "this weight selects the single-slot profile" (43 B) -> "read as a selector this weight favours the single-slot profile" (62 B). Both verbatim-in-review, machine-confirmed (build_insert_089_r2.py).
- F3 (minor, optional): NOT actioned. Gatekeeper: the dichotomy clause is "defensible as-is"; smallest-text rule.
- F4 (minor): DONE in notes-research.md (new 4732 B / sha8 e6f4ff9a): stale 3824 / aa5db164 / 752640 / 7ede2bc7... replaced by the live r1 numbers 3823 / 602e63d9 / 752639 / 2da0e0764e92...be654bb (full sha copied from the shipped simulate_apply_089.out), plus a one-clause note that r2 supersedes with the insert-r2 contract.
- F5 (minor): ANSWERED: the three r1 placeholder sections point to r1 ## Claims (the claim list) and notes-research.md (derivations, anchor detail); no separate refill, since round 2 adds no claims.

## Decisions Taken
- New-file policy: hygiene_089.py REWRITES insert-r1.tex from insert-body.txt on every run (gatekeeper Hygiene note), so no r1 script or insert file was edited. All r2 artifacts are NEW files: insert-body-r2.txt, insert-r2.tex, build_insert_089_r2.py, hygiene_089_r2.py + .out, simulate_apply_089_r2.py + .out, proposal-r2.md, manifest_r2.md. The only r1-era file modified is notes-research.md (F4). hygiene_089_r2.py asserts insert-r1.tex sha8 602e63d9 unchanged at exit; all r1 bytes verified frozen.
- Dead-pass quarantine: F4 removes the stale 3824 / 7ede2bc7 numbers from the notes.

## Claim set (UNCHANGED from r1; rule-6 classifications as in the review Manuscript contract)
1. Pushforward density (D-1)!/(G (sum p_i/g_i)^D) of the named exponential slot law, independent of s^2 and W: established identity (gatekeeper re-derived independently).
2. S_D-equivariance and uniform-input exchangeability: established.
3. Identifiability of g up to the W-fixed scale WITHIN the exponential family: established; beyond the exponential family: ARGUED, NOT PROVED, now explicitly marked in the fixed sentence (F1).
4. Convexity of Phi, no interior stationary profile unless g uniform, vertex minimum: established; uniqueness only when the largest g_i is unique, tied variances leave the spanning face minimal: established and now stated (F2a).
5. Haar frame pushforward = flat Dirichlet(1,...,1); flat unordered quotient; joint factorization: established.
6. Bounded negative: inside the named measures and named fibre maps the route yields no weight beyond re-imported profile data or flatness: established within the stated hypotheses.
7. Vertex-as-selector reading: interpretation, hedged ("read as a selector ... favours") per F2b.

## Byte contract (NEW; r1 POST contract 752639 / 2da0e076... IS DEAD - length changed)
PRE (live appH, asserted): 748814 / ecb67a25...df6749 / CRLF 3840 / bareLF 0. PIN: unique 356-byte 088 tail at 711637 (count 1); gap to \emph{Vacuum term.} exactly CRLFCRLF. insert-r2.tex: 3975 B / sha8 bba6adc4 (full sha in manifest_r2.md). POST (simulate_apply_089_r2.out, rc 0, read-only): size 752791; sha256 e5355e61f99f9b1e5dee0f17c727c478cf22cd0d1fad28fcf175128bfe10f1c8; CRLF 3842; bareLF 0; close-idiom 16; new-header 1; Vacuum-term 2. Integrator: use ONLY these r2 numbers; re-verify the PRE hash live before splicing.

## Status discipline and remaining open step
No closure or status/label text in the insert (hygiene_089_r2.out: banned-set 0 hits, HYGIENE PASS). G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; the closer leaves missing steps (i)-(iv) unchanged. Remaining open step (as r1): a core-PRODUCED profile weight non-degenerate along the kernel directions; the named-measures fibre route stays closed-negative (review, Scope).
