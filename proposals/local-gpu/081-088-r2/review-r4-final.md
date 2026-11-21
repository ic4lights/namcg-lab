VERDICT: ACCEPT | MILESTONE: none | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 0/0

Gatekeeper decision, remote/claude, 2026-11-19. This is the final disposition of review-r3.md.
- Finding 1 was closed by r4. It was confirmed byte for byte in scan-pass-1.
- Finding 4 (the full scan) was closed by scan-pass-1..4: appH L1-1750, appH L1751-3463, ch01-ch09, and ch10-ch18 + appA-G, appI-L. All four passes are clean.

Flags:
- PRIOR-CLAIM-ERRORs corrected by this package:
  - The gpu 081/085/087 "fuzzy variance proxy" (D_eff=1488) did not describe the Row length state. It is dropped, so 086 is moot.
  - The W definition in the integrated Row length paragraph is corrected.

Accepted text. apply_build_r4.py implements exactly this, on live appH sha 779bfcac...:
- S1: insert_r3.tex (sha 8dfc3ac0...), placed after the Coincident copies item and before "\emph{Vacuum term.} The abstract".
- S2: clause_r2.txt, the closing-clause extension.
- S3: rowlen_r4.txt, the Row length W definition.

Expected post: appH 682,047 B, sha fc0884aa.... No bib change.

No label change. Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
