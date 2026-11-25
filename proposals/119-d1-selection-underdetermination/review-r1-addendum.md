# Review 119 round 1 — gatekeeper addendum (same session, appended after verdict)

Final determinism check complete. Background job (third independent `verify_r119.py` rerun): the 6-byte difference earlier flagged is the gatekeeper's own appended `rc2=0` status line; the verifier output proper (first 6476 bytes) is byte-identical to the pinned `out-r119.txt` (`009de59d50ac`), exit code 0, ending `TOTAL 62/62 PASS` / `ALL CHECKS DONE 119`. Three independent reruns (out1, outF, out2) plus the package's own run, all byte-identical — the reproduction-pack determinism claim stands, unchanged. No finding in the issued review changes; the earlier `RERUN-OUT2-DIFFERS` string was an artifact of the appended rc line, not a verifier divergence.

Final verdict stands as issued:

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2

Recap of the three required revisions (full text in review-r1.md):
- F-1 MINOR: `insert-overdetermination-r1.tex` fixed-ray clause — endpoint `w = w* = 64+16\sqrt{42}` admits a marginal double ray `r* = \sqrt{42}/14`; use `\ge` with equality case and `0\le w<w*`.
- F-2 MAJOR: same payload, beta clause — printed system is the `u(4)` instance (`+4w` channel, `A_G=4`); the `B_G=1/16 for su(4)` parenthetical pairs incompatible group data (su(4) has `A_G=7/2`). Minimal fix: label system `u(4)`, drop the parenthetical; alternative parameterization with `(A_G,B_G)=(4,0)/(7/2,1/16)` and rays condition `((A_G/4)w-v_4-64)^2\ge 10752+112B_Gw` (identity independently verified).
- F-3 MAJOR: payload shift clause and `proposal-r1.md` reasoning item 1 — shift invariance is false for the eq:Smicro lift (`D_\mu\Phi=\partial_\mu\Phi-iA_\mu\Phi`, left action on the I index, `chapters/ch03-matrix-action.tex` L215-216/L221) and for the eq:dictionary bridge; scope the clause to commutator-type lifts.

Integrator guidance unchanged: after revision re-pin from the live baseline, splice `replace(anchor, payload+CRLF+anchor, 1)`, rerun generator (twice byte-identical), fresh cert in a clean temp tree, `verify_r119.py`, `scripts/build_check.py`, `scripts/make_digest.py`; do not commit; label-touched: no.
