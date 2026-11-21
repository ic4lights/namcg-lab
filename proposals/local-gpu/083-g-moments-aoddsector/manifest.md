# manifest 083-g-moments-aoddsector, round 2 (2026-11-18)

Round 2 is metadata-only (review-r1 findings F1-F5): citation author initials and DOI in proposal-r1.md, one chi2-parameterization clarifying clause, manifest regeneration. No mathematics, no manuscript text, no scripts, no insert changed.
insert-r1.tex (2176 B / 55e96f6f) and EVERY script and .out are byte-frozen and sha-verified unchanged from round 1 (re-hash below matches the round-1 register).

Round-1 -> round-2 supersessions:
- proposal-r1.md: 21743 B / faf5f4ec (pre) -> 23064 B / 2a6e484a (post); corrected in place, review-r1 F1/F2/F3/F4 + appended 'Round 2 corrections' section; no new proposal-r2.md (round-2 instruction).
- manifest.md: 2753 B / 0a0c3330 (superseded, F5 'handback table' reference removed) -> the present file (its own sha8 is reported in the round-2 handback).
- s3b_noncentral_r.py comment L64 label 'chi2_2(c)/2' intentionally NOT edited (file frozen); the standard-parameterization clarification (chi2_2(2c)/2, c = lam/2) lives in proposal-r1.md only.

Live PRE pins: appH 731183 B, sha256 956070afcd26fc1c8ffd040ca2d8bb8340467de79117bd0a10d782b6dd062c52, CRLF 3830, bareLF 0.
Expected POST after apply: 733361 B, sha256 c35bfed009668845a5ff313e0a35b3f48374cbc843ed85e9d4fedb2a936cedfd, CRLF 3832, bareLF 0. Anchor = full unique 082 tail (count 1); the short suffix 'do not fix the state that sets' occurs 3x and must never be used as a pin; splice = insert bytes + one CRLF before the next line-start Vacuum-term header after the pin end.

| file | bytes | sha8 |
|---|---|---|
| insert-r1.tex | 2176 | 55e96f6f |
| proposal-r1.md | 23064 | 2a6e484a |
| review-r1.md | 12815 | 740e4072 |
| s1_allm_spectral.out | 697 | 2d851491 |
| s1_allm_spectral.py | 1592 | 5ef5277b |
| s2_oddmap.py | 555 | 7353fe43 |
| s2b_oddmap.out | 994 | 71554d9b |
| s2b_oddmap.py | 3595 | 8ac9510b |
| s2c_oddmap.out | 1283 | 724246e5 |
| s2c_oddmap.py | 4276 | 086f2fc0 |
| s2d_oddmap.out | 1386 | b0590321 |
| s2d_oddmap.py | 4199 | 3abcbc8c |
| s3_noncentral_r.out | 1092 | 8c42a35f |
| s3_noncentral_r.py | 5021 | ad834519 |
| s3b_noncentral_r.out | 1006 | 7d24a23b |
| s3b_noncentral_r.py | 5017 | 5d056168 |
| simulate_apply_083.out | 139 | 1bd9e6be |
| simulate_apply_083.py | 1882 | c25af000 |

Status notes:
- LIVE scripts: s1_allm_spectral.py (S1 OK), s2d_oddmap.py (S2d OK), s3b_noncentral_r.py (S3b OK), simulate_apply_083.py (read-only, 'no write performed').
- DEAD (do not use as evidence): s2_oddmap.py (dead stub, never executed, no .out); s2b_oddmap.py/.out (superseded: sqrt(r) inside Poly, missing positivity, variable mismatch); s2c_oddmap.py/.out (superseded: factorial double-count in map_m); s3_noncentral_r.py/.out (superseded by s3b for speed; its Parts 3-4 used a chi-square-2 scale convention, hence FAIL there; Parts 1,2,5 passed).
- insert-r1.tex hygiene: one line + terminal CRLF, zero dollar/square-bracket/cite/ref/label/eqref tokens, one emph, zero banned substrings, header unique across chapters/.
- Citation verification (round 2, all fetched live 2026-11-18): arXiv:0912.0577v2 abstract page (Satoshi Kuriki, Yasuhide Numata; AISM 62 (2010) 645-672); api.crossref.org/works/10.1007/s10463-010-0279-4 (Kuriki/Numata, graph-moments title, vol 62 pp 645-672, 2010); arXiv:2505.08149v4 abstract page (Jia Xu, Yong Yao).
