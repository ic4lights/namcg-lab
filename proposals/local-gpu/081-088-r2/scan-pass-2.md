SCAN-PASS 2/4: CLEAN (gatekeeper, 2026-11-19)

Scope: appH L1751-3463 read in full (live sha 779bfcac...), with Problem G L2886-2967 read in small chunks.

No conflicts with:
- the edge block, L2928 and L2934;
- the State paragraph, L2924;
- Bearing, L2926;
- Row length after S3, L2922;
- toric 067, L2940-2965. Its W at L2959 is defined explicitly as the full row sum, and its normalisation is a unit choice.
- Problems H, I, J and N, and the closing section.

Other checks:
- S2 clause occurs once.
- All S1 internal references resolve.
- No duplicate labels or new titles.

Advisory, no action: symbol reuse (mu, s_k, q_i, G, W) is defined locally each time. Renaming would change the hashes.

Findings: none.
