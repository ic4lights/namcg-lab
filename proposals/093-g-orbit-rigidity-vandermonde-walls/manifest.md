# Manifest 093-g-orbit-rigidity-vandermonde-walls, round 1

Generated after all deliverables; manifest.md itself is not hashed. All sha256 are full-file.

| file | bytes | sha256 |
|---|---|---|
| hygiene_093.out | 1335 | 8ed476edd67c1baed6a7032a7fdb51145af5e1665e2488f2980c7302663582c1 |
| hygiene_093.py | 2086 | d11f4c8d2e5cb90578711fb12cdc403f1ccc979070979f9818ea41f6a23f9b01 |
| insert-r1.tex | 4044 | 2f7a5320d295c8415c2a17621fa847e7e8758e423b68b9b97eca3dd0ea17b7f1 |
| proposal-r1.md | 18513 | 4dd1761155628af696f3f5a1cc8a26620a6d37f9dc39b0e317939bf67759387a |
| s1_wall_jacobian_v8.out | 1719 | 14f37dcf27dffcb458987ca015448ba898acb725c04d091f19c9521ef2bbd45a |
| s1_wall_jacobian_v8.py | 8250 | df142fcb0b5f130dd8cc7943bc0b2cb3f7d88caf0f8d0ed1c574b4c2dd19aa27 |
| s2_integrability_v7.out | 1631 | a5c0adf3288a539303869f367e79d428a2b842317a405b575d4ad82223f21dfe |
| s2_integrability_v7.py | 5637 | 3422db6e5f4752974229d706a40df1e3179fb760a197aa9a5fa266579f4d9251 |
| simulate_apply_093.out | 522 | 73a54674cb6f957e6aff9ebccbaf4e5d31b60dcbdf85186257a8970c60a63358 |
| simulate_apply_093.py | 2423 | db8513cab1fd169163839e2b193c158dd0d0d85eeacad6c1412627c89cba5925 |

Supersession register: s1_wall_jacobian v1-v7 superseded and removed (v8 authoritative);
s2_integrability v1-v4 removed (v5 removed: off-by-one in m-fold exponent identity, caught by
its own run); v5-v6 removed: v6 PART E gamma-identity check failed on symbolic simplification
and was replaced in v7 by the chain+recursion check (symbolic-or-1e-12-numeric, branch printed);
v7 authoritative. hygiene_093.py, simulate_apply_093.py, insert-r1.tex unchanged after first
run. All four scripts final run status: PASS (s1, s2, hygiene, simulate).

Key decision summary: prod_k! Jacobian constant over D! guess; dropped false W^2-Lipschitz
pair claim for exact quadratic identity; m-fold threshold beta>1-2/m via e+1 identity; insert
citation-free, ref-free, one line + terminal CRLF. No files outside this folder touched.
