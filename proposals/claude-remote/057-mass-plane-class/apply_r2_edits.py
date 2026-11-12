#!/usr/bin/env python3
"""Apply review-r1 replacements R1, R2 (two parts), R3 verbatim to appH_insert.tex.
Checks the r1 insert hash, saves the r1 bytes as appH_insert.r1.tex (refuses to overwrite a different file),
and checks that each old string occurs exactly once before and each new string exactly once after."""
import hashlib, os
HERE = os.path.dirname(os.path.abspath(__file__))
INS = os.path.join(HERE, 'appH_insert.tex')
R1F = os.path.join(HERE, 'appH_insert.r1.tex')
R1_SHA = 'f7fbbade4567d6843f13fe50f06ccb457cc78ac230863e1505b0bdb8f074af82'
R1_LEN = 7714
BS = chr(92)


def L(s):
    return s.replace('@', BS)


reps = [
    ('R1',
     L('For @(@gamma@le0@) the lower class is empty, and the inertia argument there applies instead.'),
     L('For @(@gamma@le0@), where @(-@pi/2@le@varphi@le0@), the interval @((-@pi,2@varphi-@pi]@) is empty, and the inertia argument of (i) of the preceding paragraph applies instead.')),
    ('R2a',
     L('At @(N=2@) this integrand of @(I[1]@) on the contour @(@Lambda_@infty@) is not absolutely integrable.'),
     L('At @(N=2@) this integrand of @(I[1]@) on the contour @(@Lambda_@infty@), with any real @(@gamma@) in the mass term, is not absolutely integrable.')),
    ('R2b',
     L('So for fixed @(@gamma>0@), and for @(@gamma/@epsilon@to@infty@), no linear contour reached from the Hermitian contour in this way, fixed or convergent as @(@epsilon@to0@), carries the dominated convergence used above for @(@gamma@le0@), in line with the closing of the admissible @(u@) on @(@mathcal R_u@) like @(@epsilon/@gamma@).'),
     L('So for fixed @(@gamma>0@), and for @(@gamma/@epsilon@to@infty@) with @(@gamma@) converging to a finite limit, no linear contour reached from the Hermitian contour in this way, fixed or convergent as @(@epsilon@to0@), carries the dominated convergence used above for @(@gamma@le0@), since a dominating function would also dominate the integrand at @(@epsilon=0@) on @(@Lambda_@infty@) with that limit of @(@gamma@); this is in line with the closing of the admissible @(u@) on @(@mathcal R_u@) like @(@epsilon/@gamma@).')),
    ('R3',
     L('The two classes are fixed by the @(@eta@) in @(S_{@mathrm b}@) and by the regulator, so no signature is selected and Assumption~@ref{ass:lorentzian} is still required.'),
     L('The two classes are fixed by the @(@eta@) in @(S_{@mathrm b}@) and by the regulator, so they select no signature, and the positive mass does not discharge Assumption~@ref{ass:lorentzian}.')),
]

b = open(INS, 'rb').read()
sha = hashlib.sha256(b).hexdigest()
if sha != R1_SHA:
    if os.path.exists(R1F) and hashlib.sha256(open(R1F, 'rb').read()).hexdigest() == R1_SHA:
        print('insert is not r1 (already edited?); r1 copy present. sha', sha)
        raise SystemExit(1)
    raise SystemExit('insert hash differs from r1; stop')
assert len(b) == R1_LEN
if os.path.exists(R1F):
    assert open(R1F, 'rb').read() == b, 'r1 copy exists and differs'
else:
    open(R1F, 'wb').write(b)
print('r1 saved:', R1F, len(b), sha)
s = b.decode('utf-8')
for tag, old, new in reps:
    co, cn = s.count(old), s.count(new)
    print(tag, 'old count before', co, 'new count before', cn)
    assert co == 1 and cn == 0
    s = s.replace(old, new)
for tag, old, new in reps:
    co, cn = s.count(old), s.count(new)
    print(tag, 'old count after', co, 'new count after', cn)
    assert co == 0 and cn == 1
out = s.encode('utf-8')
open(INS, 'wb').write(out)
print('r2 insert:', len(out), hashlib.sha256(out).hexdigest(), 'CR present:', b'\r' in out)
