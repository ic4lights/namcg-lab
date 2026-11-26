#!/usr/bin/env python3
"""simulate_apply_080_r2: byte contract for inserting insert-r2.tex into appH, read-only.
PRE pins (live tree, 2026-11-17): size 720144, sha256 a10eca51...028012f, CRLF 3824, bare LF 0,
anchor line-start unique at line 3175, r2 header absent from appH AND from every
chapters/**/*.tex. POST = computed from the live tree (never written). No write is done."""
import glob, hashlib, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
APP = os.path.join(ROOT, 'chapters', 'appH-microscopic-proofs.tex')
INS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'insert-r2.tex')
ANCHOR = b'\\emph{Vacuum term.} The abstract of~\\cite{Steinacker2023'
HEADER = b'\\emph{Mixed-multiplicity spectra of block-equalized coincident copies.}'
pre = open(APP, 'rb').read()
ins = open(INS, 'rb').read()
assert len(ins) == 5395, ('insert-r2 size', len(ins))
assert hashlib.sha256(ins).hexdigest() == 'a74841c2916dc1ed438ec3d46b30129cea688ff0d2f9a41906cf7f34750487ee'
sha = hashlib.sha256(pre).hexdigest()
crlf = pre.count(b'\r\n'); bare = pre.count(b'\n') - crlf
assert len(pre) == 720144, ('PRE size', len(pre))
assert sha == 'a10eca5184d853b8baa0ffac185c67265e6414672e93025dad05a4e08028012f', ('PRE sha', sha)
assert crlf == 3824 and bare == 0, ('PRE CRLF/bareLF', crlf, bare)
lines = pre.split(b'\r\n')
hits = [i for i, L in enumerate(lines) if L.startswith(ANCHOR)]
assert len(hits) == 1 and hits[0] == 3174, ('anchor', hits)
assert pre.count(HEADER) == 0, 'header already present in appH'
chap_total = 0
for f in glob.glob(os.path.join(ROOT, 'chapters', '**', '*.tex'), recursive=True):
    chap_total += open(f, 'rb').read().count(HEADER)
assert chap_total == 0, ('header collision in chapters tree', chap_total)
o = sum(len(L) + 2 for L in lines[:3174])
post = pre[:o] + ins + b'\r\n' + pre[o:]
psha = hashlib.sha256(post).hexdigest()
pcrlf = post.count(b'\r\n'); pbare = post.count(b'\n') - pcrlf
plines = post.split(b'\r\n')
phits = [i for i, L in enumerate(plines) if L.startswith(ANCHOR)]
phead = [i for i, L in enumerate(plines) if L.startswith(HEADER)]
print('PRE  size=%d sha=%s CRLF=%d bareLF=%d anchorLine=%d headerCount=%d chaptersHeaderTotal=%d'
      % (len(pre), sha, crlf, bare, 3175, pre.count(HEADER), chap_total))
print('POST size=%d sha=%s CRLF=%d bareLF=%d anchorLine=%d headerLine=%d headerCount=%d'
      % (len(post), psha, pcrlf, pbare, phits[0] + 1, phead[0] + 1, post.count(HEADER)))
assert post.count(HEADER) == 1 and len(phead) == 1
assert pcrlf == 3826 and pbare == 0 and phits[0] + 1 == 3177 and phead[0] + 1 == 3175
assert len(post) == len(pre) + len(ins) + 2
assert hashlib.sha256(open(APP, 'rb').read()).hexdigest() == sha, 'appH was written!'
print('OK: no write performed; appH unchanged after simulation')
