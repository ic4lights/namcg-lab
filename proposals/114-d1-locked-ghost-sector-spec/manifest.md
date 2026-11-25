# manifest 114-d1-locked-ghost-sector-spec (round 2, re-pinned)

sha1 / bytes / name; r2 byte-revision state (review-r1.md findings 1,2,3 applied; 4 not).
Cert rerun on pinned insert: spliced bytes: 828027 rc: 0 exclam-lines: 0
Output written: True -> CERT OK. appH sha1 60a8eb47bb32184d60d0165483a635f9a331c2b3;
anchor grep -c = 1. See r2-report.md for diffs and byte-scan proofs.

d0cc7251ca8ba06fd742282b93d4dc823e88c3e3     1866  cert-r114p.py
a813eb9cf97f7f6c7ad57ca12f4595e75c53ef33     3647  insert-d1-locked-ghosts.tex
d512e4ab88989b6531633e39e417f683bfcc74a0    29389  proposal-r1.md
59556cf805cdc111e386e0e561fcbfc2b417dd6b     5723  r2-report.md
163c0d62f22d8e279a210734ff0db315bf2fd058    13565  review-r1.md
6b8832bd1dc199c17c24fedda8e6d3fced8a4d92      822  run-r114.txt
595212189dfb57c56f8be5a22b321178c6c3b3b9     6585  verify_ghost_fp_114.py

Reproduction:
  python -I -B verify_ghost_fp_114.py   -> ends 'ALL CHECKS DONE'
  python -I -B cert-r114p.py               -> ends 'CERT OK' (828027-spliced)
