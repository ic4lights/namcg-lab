# Manifest — proposals/100-g-mi-tau-conditioning-d2 (round 1)

Byte sizes and sha256-8 as of 2026-11-19. A `__pycache__/` directory is present (import
byproduct; removal was blocked by the guard hook; safe to delete, no content).

## MI pipeline lineage (numpy, route A + route B)
- `mi_tau_100.py` 3286 e625c1b5 / `mi_tau_100.out` 572 eca80752 — predecessor v1 (p-channel style base).
- `mi_tau_100b.py` 3687 ebb99863, `mi_tau_100r.py` 5810 6ef2c9c0, `mi_tau_100n.py` 3669 dd041927
  (+ `mi_tau_100n.out` 0) — failed predecessor tau attempts; `err100.txt` 1526 9f91b80d,
  `err100p.txt` 408 950b2959 — their tracebacks (tool-echo deaths of the two predecessor contexts).
- `mi_tau_100p.py` 3689 76bc4e35 (+ `.out` 0) — surviving base. Real defects (re-derived): h() branch
  algebra wrong in BOTH branches; lnNu had spurious `/Wv`; Elnq row shape bug. Its KL line is correct.
- `fix_100.py` 2393 4e3fb14e — PRE-COMPACTION fix; itself WRONG (claimed f(tau|u) power 2M-1);
  kept as lineage only, superseded.
- `fix2_100.py` 2949 666615e4 — byte authority mi_tau_100q.py **v2** (`mi_tau_100q.py` 3644 dc9ef719;
  v1 sha 59b773a1 was overwritten in place). `mi_tau_100q.out` 1473 66ad0060: A/B agree 5-8e-14,
  refine drift <=1e-13, I(p2;x) reproduces integrated 099 to <=3e-8, sigma/swap identical, cv=0 (route A).

## Independent mpmath path (route A', dps 30, no numpy/scipy)
- `rederive_100.py` 2702 4fe545bd — v2 by `fix4_100.py` 2237 d05cac9d (v1 nan bug: 1-exp cancellation
  at tanh-sinh nodes for w ~ 1e-18..1e-6; fixed via mp.expm1 log-space). `rederive_100.out` 502 0b824e9d.

## MC corroboration
- `mc100.py` 3852 a42240dd, `mc100r.py` 4238 29d944bc (+out), `mc100b.py` 4074 94df4f9c (+out) —
  predecessor attempts; mc100r.py dead (array/scalar Zf ValueError, np.math on numpy 2).
- `mc100s.py` 3841 7d9dc8a5 — clean rewrite; v1->v6 by `fix3..fix8_100.py` (unpack convention, Zf
  endpoints, density weights, u-node count, gamma vs lgamma). `mc100s.out` 758 e67c83de: ALL |z|<=1.8,
  refs -0.223877/-0.419234 match pipeline Eh.

## Closed-form anchors (sympy)
- `verify_anchors.py` 2904 7044f974, `verify_anchors.out` 271 100ccc30 — checks A-G incl. f(tau|u)
  power 2M-2 and h(r) formula/series. END "PASS verify_anchors".

## Insert artifact pack
- `gen_insert_100.py` 3905 62b3bcc5 — SOLE byte authority for `insert-r1.tex` 1989 511ddc60
  (two in-place edits during authoring: dropped `[...]` exponent notation; closing tail reworded to
  "and close nothing in Problem~G." to avoid the old-seam pattern — both in sha history above).
- `hygiene_100.py` 3190 6c8781d9 — v2 by `fix9_100.py` 1371 5fed6173 (predecessor v1 post.adjacency
  counted a single-CRLF pattern impossible under the contract's double-CRLF seam; unsatisfiable bug).
  `hygiene_100.out` 668 f35fce16 — SUMMARY ALL PASS.
- `simulate_apply_100.py` 1493 c4005f89 (READ-ONLY), `simulate_apply_100.out` 511 5d4a3558 — ends
  "no write performed"; POST bytes 795607, crlf 3864, bareLF 0,
  POST sha256 3f1b030cf81dff1b39a0fc96be87331d92ca2ed5c33bc592bb794b66670e3202, idiom 26,
  verb 1, vacuum 2, hdr 1, adjacency 1, oldseam 0.

## Manuscript state relied on (NOT modified by this proposal)
- `chapters/appH-microscopic-proofs.tex` PRE: 793616 B, sha 7cd6e208..., crlf 3862, bareLF 0; pin 162 B
  at 756633 count 1; compound count 1; cut 756799 at `\emph{Vacuum term.}` (line 3213; 099 paragraph L3211).
