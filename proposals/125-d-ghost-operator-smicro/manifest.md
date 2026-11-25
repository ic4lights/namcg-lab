# manifest 125-d-ghost-operator-smicro (generated 2026-11-25 02:10)

sha1 | size | file
---|---|---
7103f8fcf565ee1b155612c78b26d51b4f598f22 | 828 | dbg_c2.py
fbd240e9171ba6c77c92eaff9f7c9fda8f10f7f8 | 855 | dbg_c2b.py
84bd489674585a8d4a384ae6514efd628bcf4fc0 | 10013 | ghost_linearization_125.py
84bd489674585a8d4a384ae6514efd628bcf4fc0 | 10013 | ghost_linearization_125.py.dead-bytes
c33c65b9a04107a07992c172b5323534cc50a046 | 20335 | ghost_linearization_125b.py
43a7b1ebbaa17c22e7e2f170c0c4d81285976498 | 15524 | ghost_linearization_125c.py
6025cef618cdcf43e7c8e28d9c04d0c73b67cf7a | 14369 | ghost_linearization_125c.py.prefix-addl-bug
ee1ce1d7d853006065ebcb4080ac3df4da753c79 | 11521 | journal.md
f003482705cf8da5c6b4475453bad46c86752e23 | 290 | kill125b.ps1
1535d63d3ba4a1f3a0dd571cb5315ad177a46bc0 | 1351 | out-125b.txt
0037b05c8c9d5984f70da806274fe9b0ad0fe50c | 929 | out-125c-9of10.txt
f2d857769c1bf1b191160582d53106ce407df9a0 | 246 | out-125c-bugtrace.txt
fbd08fca260270f2a55e0252155152b6405505c3 | 1243 | out-125c.txt
bb00c19a5dd87ce701b0e71f84e9b96130327d90 | 380 | out-dbg-d1.txt
0f43ec2d59ddf60b6fae1cd8b9fd85e78045159f | 44 | out-dbg-d5.txt
4dbe7fcf7894dfd418fd0d751cc7711ddf51a6ac | 177 | out-dbg-d5b.txt
a90eadc7e0929183297653b297c081ba225b77e2 | 89 | out-dbg-d5c.txt
4e6f6fad71d33eb4897626611cfb34fd8d2ceec2 | 993 | out-ghost-linearization-part1.txt
44cc570ac9324c15e37a928fdc4b6321bdb64f22 | 1246 | out-gk125c-run.txt
eb3565d130b67171e6b7103805a45c5773b94bcd | 29218 | proposal-r1.md

Supersession chain (all bytes retained):
- ghost_linearization_125.py == .py.dead-bytes (predecessor artifact, sha-equal pin).
- ghost_linearization_125c.py.prefix-addl-bug = pre-fix D battery (concat addl).
- out-125c-bugtrace.txt = D1 FAIL firing of the concat-addl bug (residual [0,+f] = +Ric xi).
- out-125c-9of10.txt = run of script sha de74bc75 (elementwise addl, combined-16 D5:
  9/10, D5 FAIL is a simplify artifact; superseded by per-component D5, journal resume6).
- out-125c.txt = FINAL certificate (script 43a7b1eb): 13/13 PASS, EXIT=0 (journal resume8:
  foreign stale-wrapper line stripped byte-exactly; content untouched).
- out-125b.txt: C0-C3 certificate; ends EXIT=124 (wrapper timeout, by design of the re-run
  pack); its script contains the pre-fix addl in a code path the run never reached and a
  latent tan-import gap that fires at C4 (never reached).
- payload: NONE shipped (proposal-r1.md, Proposed changes).
