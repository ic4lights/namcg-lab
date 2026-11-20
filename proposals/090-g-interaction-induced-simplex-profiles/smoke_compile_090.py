import hashlib, os, subprocess, re
# Standalone smoke compile of insert-r1.tex (positive) and a deliberately broken variant
# (negative control: first \lvert byte-surgered to \lvertz). Scratch subdir INSIDE the proposal
# folder; run from the repository root.
P = 'proposals/090-g-interaction-induced-simplex-profiles/'
D = P + 'scratch_latex'
os.makedirs(D, exist_ok=True)
B = bytes([92])
def m(s): return B + s.encode()
PRE = (m('documentclass{article}') + b'\n' + m('usepackage{amsmath,amssymb}') + b'\n' + m('begin{document}') + b'\n')
POST = m('end{document}') + b'\n'
for W in (PRE, POST):
    assert not [c for c in W if c < 32 and c not in (10, 13)], 'ctrl byte wrapper'
ins = open(P + 'insert-r1.tex', 'rb').read()
assert len(ins) == 3735 and hashlib.sha256(ins).hexdigest()[:8] == '3a6a69c4'
neg = ins.replace(B + b'lvert', B + b'lvertz', 1)
assert len(neg) == len(ins) + 1 and neg != ins
def comp(name, buf0):
    t = name + '.tex'
    buf = PRE + buf0 + POST
    assert not [c for c in buf if c < 32 and c not in (10, 13)], 'ctrl byte buffer'
    open(os.path.join(D, t), 'wb').write(buf)
    p = os.path.join(D, name + '.log')
    if os.path.exists(p): os.remove(p)
    r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', t], cwd=D, capture_output=True)
    log = open(p, 'rb').read() if os.path.exists(p) else b''
    return r.returncode, bool(re.search(rb'(?m)^! ', log)), log
rc, err, log = comp('smoke090', ins)
p1 = rc == 0 and not err and b'undefined control' not in log.lower()
rc2, err2, log2 = comp('smoke090neg', neg)
p2 = rc2 != 0 and err2 and b'undefined control sequence' in log2.lower()
print('GATE insert-r1: rc=%d PASS=%s' % (rc, p1))
print('NEG-CONTROL lvert->lvertz: rc=%d EXPECTED-FAIL=%s' % (rc2, p2))
print('SMOKE GATE', 'OK' if (p1 and p2) else 'PROBLEM')
