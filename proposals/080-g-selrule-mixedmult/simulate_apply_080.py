#!/usr/bin/env python3
"""simulate_apply_080: byte contract for inserting insert-r1.tex into appH, read-only.
PRE pins (live tree, 2026-11-17): size 720144, sha256 a10eca51...028012f, CRLF 3824, bare LF 0,
anchor line-start unique at line 3175, my header absent. POST = computed stats. No write is done.
"""
import hashlib, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
APP = os.path.join(ROOT, 'chapters', 'appH-microscopic-proofs.tex')
INS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'insert-r1.tex')
ANCHOR = b'\\emph{Vacuum term.} The abstract of~\\cite{Steinacker2023'
HEADER = b'\\emph{Mixed-multiplicity spectra of block-equalized coincident copies.}'
pre = open(APP, 'rb').read()
ins = open(INS, 'rb').read()
sha = hashlib.sha256(pre).hexdigest()
crlf = pre.count(b'\r\n'); bare = pre.count(b'\n') - crlf
assert len(pre) == 720144, ('PRE size', len(pre))
assert sha == 'a10eca5184d853b8baa0ffac185c67265e6414672e93025dad05a4e08028012f', ('PRE sha', sha)
assert crlf == 3824 and bare == 0, ('PRE CRLF/bareLF', crlf, bare)
lines = pre.split(b'\r\n')
hits = [i for i, L in enumerate(lines) if L.startswith(ANCHOR)]
assert len(hits) == 1 and hits[0] == 3174, ('anchor', hits)
assert pre.count(HEADER) == 0, 'header already present'
o = sum(len(L) + 2 for L in lines[:3174])
post = pre[:o] + ins + b'\r\n' + pre[o:]
psha = hashlib.sha256(post).hexdigest()
pcrlf = post.count(b'\r\n'); pbare = post.count(b'\n') - pcrlf
plines = post.split(b'\r\n')
phits = [i for i, L in enumerate(plines) if L.startswith(ANCHOR)]
phead = [i for i, L in enumerate(plines) if L.startswith(HEADER)]
print('PRE  size=%d sha=%s CRLF=%d bareLF=%d anchorLine=%d headerCount=%d'
      % (len(pre), sha[:16], crlf, bare, 3175, pre.count(HEADER)))
print('POST size=%d sha=%s CRLF=%d bareLF=%d anchorLine=%d headerLine=%d headerCount=%d'
      % (len(post), psha[:16], pcrlf, pbare, phits[0]+1, phead[0]+1, post.count(HEADER)))
assert post.count(HEADER) == 1 and len(phead) == 1
assert pcrlf == 3826 and pbare == 0 and phits[0] + 1 == 3177
assert len(post) == len(pre) + len(ins) + 2
assert hashlib.sha256(open(APP, 'rb').read()).hexdigest() == sha, 'appH was written!'
print('OK: no write performed; appH unchanged after simulation')
