# manifest - proposals/099-g-mi-p-d-d2 (round 2, 2026-11-19; r1 section kept as lineage)

sha8 = first 8 hex of sha256. Live = use as-is for r2 integration. Lineage = r1 evidence, not-to-integrate.
Generated = script output, reproducible by rerunning the named script from repo root with `python -I`.

## Round 2 (CURRENT CONTRACT)

| file | bytes | sha8 | role | status |
|---|---|---|---|---|
| proposal-r2.md | 9806 | 32088493 | round-2 delta proposal (notation fix + new contract) | live |
| insert-r2.tex | 1656 | aa19ac66 | MANUSCRIPT INSERT (paragraph + CRLF), bare-u eliminated | live (sole integration bytes) |
| gen_insert_099_r2.py | 3863 | 4d403dbe | SOLE byte authority for insert-r2.tex; asserts bare_u=0 | live |
| hygiene_099_r2.py | 3778 | 9e3ad9a0 | live-appH contract + anchors + ins.nobareu (read-only) | live |
| hygiene_099_r2.out | 791 | ebd106a2 | 19 PASS, SUMMARY ALL PASS | generated |
| simulate_apply_099_r2.py | 1880 | 781e67cf | read-only POST simulation | live |
| simulate_apply_099_r2.out | 581 | ec32a4b5 | **AUTHORITATIVE r2 POST CONTRACT**: POST 793616 B, sha256 7cd6e2084c065f69045e82216439bcb5feee71468b4b84fb7caaae71b9305885, CRLF 3862, bareLF 0, idiom 25, verb 1, vac 2, hdr 1, adj 1/1, old-seam 0 | generated |
| review-r1.md | 11746 | 0f14dbb8 | gatekeeper round-1 review (ACCEPT WITH REQUIRED REVISIONS) | evidence |

## Round 1 (LINEAGE - math accepted by review-r1; bytes not-to-integrate)

| file | bytes | sha8 | role | status |
|---|---|---|---|---|
| proposal-r1.md | 20523 | 160c62d3 | round-1 proposal | lineage (Coordinates sentence superseded by r2 wording) |
| insert-r1.tex | 1556 | 0cdf7c9b | round-1 insert (bare `u`, 093 collision) | SUPERSEDED not-to-integrate |
| gen_insert_099.py | 3484 | 4942389f | r1 byte authority | superseded by gen_insert_099_r2.py |
| hygiene_099b.py / .out | 3704/730 | d15d8d7c/43fde117 | r1 hygiene (insert pins r1 bytes) | superseded by hygiene_099_r2 pair |
| simulate_apply_099.py / .out | 1661/564 | 2b698428/bfdeebb0 | r1 POST simulation | superseded; **r1 POST 793516 B / sha fae8dcd2... is VOID** (described insert-r1.tex only) |
| rederive_099.py / .out | 3135/636 | 85948a2f/b319d8a0 | exact re-derivation (numerics UNCHANGED in r2) | live (math evidence, rerunnable) |
| ksg_099.py / .out | 2139/383 | 0d0edcea/ee231739 | bin-free MI arbiter | live (math evidence) |
| mc_099.py / .out | 1263/233 | a49944b8/0e450ba6 | Wishart-sampling checks | live (math evidence) |
| cellcheck_099.py / .out | 1582/406 | 0911b67b/5c8c943d | joint-exponent MC test | live (math evidence) |
| verify_099.py / .out / .err | 11336/3898/193 | 4b53fd4c/7ec7660e/46348026 | predecessor verification | evidence: S1-S3,S5 sound; S4 It values REJECTED; double SUMMARY genuine; .err benign |
| hygiene_099.py / .out | 4661/1421 | 33206f6a/963d9be3 | predecessor hygiene (stale tail pin) | SUPERSEDED; retained |

## Correction and notation record

- Hetero I(p;P2) 0.2863661/0.4958970 (predecessor, WRONG) -> 0.267988/0.475266;
  confirmed to <=4e-7 by gatekeeper's independent exact mpmath path (review-r1).
- Round 2: all bare `u` tokens eliminated (review-r1 blocking finding, 093 collision
  at appH L3199): snippet adopted verbatim + disclosed renaming \((\tau,u,x)\)->
  \((\tau,p_{2},x)\) (u=p2). Numbers, claims, scope unchanged.

## Handover

To integrate: run gen_insert_099_r2.py (byte authority), hygiene_099_r2.py, then
splice insert-r2.tex at byte cut 755141 (after live 098 paragraph, before
line-initial \emph{Vacuum term.}); verify against simulate_apply_099_r2.out.
Re-verify anchors against the live tree at integration time. No bib, labels, ch17
or status changes.
