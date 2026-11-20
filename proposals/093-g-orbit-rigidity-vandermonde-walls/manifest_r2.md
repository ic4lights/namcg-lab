# Manifest r2 093-g-orbit-rigidity-vandermonde-walls

Registry of all live round-2 package files; manifest_r2.md itself not hashed.
Round-2 deliverables: proposal-r2.md, simulate_apply_093_r3.py/.out, manifest_r2.md.
Unchanged live r1 files: insert-r1.tex (accepted unchanged), s1_wall_jacobian_v8.py/.out,
s2_integrability_v7.py/.out, hygiene_093.py/.out, review-r1.md, proposal-r1.md (r1 text,
with the Expected-POST paragraph superseded).

| file | bytes | sha256 | note |
|---|---|---|---|
| hygiene_093.out | 1335 | 8ed476edd67c1baed6a7032a7fdb51145af5e1665e2488f2980c7302663582c1 |  |
| hygiene_093.py | 2086 | d11f4c8d2e5cb90578711fb12cdc403f1ccc979070979f9818ea41f6a23f9b01 |  |
| insert-r1.tex | 4044 | 2f7a5320d295c8415c2a17621fa847e7e8758e423b68b9b97eca3dd0ea17b7f1 |  |
| manifest.md | 1991 | f16e041fd5e66df3a98584b4c208735e116193d6aac557427fcdefd272475f80 |  |
| proposal-r1.md | 18513 | 4dd1761155628af696f3f5a1cc8a26620a6d37f9dc39b0e317939bf67759387a | retained; its Expected-POST paragraph (769118 / 9dba1723 / CRLF3849) is SUPERSEDED by review-r1 finding 1 and proposal-r2.md Finding 1 (769120 / 5f62af10 / CRLF 3850) |
| proposal-r2.md | 5093 | dc51243b5f8feb15c49f8b655e25e9c187e291f3c19bd17b48d96eb29dacac6c | LIVE r2 |
| review-r1.md | 16194 | 66c3922cf6fd8dd7cfc298a6214a02e0aba64cf64d732065d06e85e655914de8 |  |
| s1_wall_jacobian_v8.out | 1719 | 14f37dcf27dffcb458987ca015448ba898acb725c04d091f19c9521ef2bbd45a |  |
| s1_wall_jacobian_v8.py | 8250 | df142fcb0b5f130dd8cc7943bc0b2cb3f7d88caf0f8d0ed1c574b4c2dd19aa27 |  |
| s2_integrability_v7.out | 1631 | a5c0adf3288a539303869f367e79d428a2b842317a405b575d4ad82223f21dfe |  |
| s2_integrability_v7.py | 5637 | 3422db6e5f4752974229d706a40df1e3179fb760a197aa9a5fa266579f4d9251 |  |
| simulate_apply_093.out | 522 | 73a54674cb6f957e6aff9ebccbaf4e5d31b60dcbdf85186257a8970c60a63358 | SUPERSEDED-retained (round-1 POST 769118/9dba1723 contract; superseded) |
| simulate_apply_093.py | 2423 | db8513cab1fd169163839e2b193c158dd0d0d85eeacad6c1412627c89cba5925 | SUPERSEDED-retained (round-1 splice without blank-line separator CRLF; contract superseded by r3) |
| simulate_apply_093_r3.out | 595 | 6cc7df7d9197117fd7247b0da18460889b60918db6419babb76e4da430eae58a | LIVE r2 |
| simulate_apply_093_r3.py | 3537 | 534e385bed10ac3399a8175fc767c8a35db89eaf301ffcb15aa237efe9be8ecd | LIVE r2 |

Deleted this round: simulate_apply_093_r2.py/.out (first corrected draft; failed only on
its own blank-line check-line slice, never on the contract; superseded before first PASS by
simulate_apply_093_r3.py, per the no-edit-WIP rule).

Final run statuses: simulate_apply_093_r3.py PASS (rc 0, no write performed; POST 769120 /
5f62af10bbcfc0507c852e127bbad53a6829fce572c97e69f7a9b0e1e0e0d4e3 / CRLF 3850 / bareLF 0 /
noun 19 / verb 1 / Vacuum-term 2 / header 1). s1, s2, hygiene PASS (gatekeeper byte-identical
re-runs recorded in review-r1.md). No files outside this folder touched.
