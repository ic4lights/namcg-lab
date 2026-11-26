#!/usr/bin/env python3
"""Apply review-r1 F1, F2, F3 verbatim to appH_insert.tex.  Checks the r1 hash first, and that each old string
occurs exactly once before (and zero times after) and each new string zero times before and exactly once after.
Backslashes are built from chr(92)."""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, 'appH_insert.tex')
R1_SHA = 'ac95c6691538edc112fbe03006481b729a4c79ae6a75dbcd1e2666b2e43e9680'
B = chr(92)
def L(s):
    return s.replace('@', B)
EDITS = [
 ("F1",
  L(r"The induced tensor of Definition~@ref{def:matrix-coords-ext} is its pull-back by a configuration, and for @(h_0@) of signature @((9,1)@) the restriction to a four-dimensional tangent space is positive definite, Lorentzian or degenerate according to the configuration, so the signature of the composite metric is a property of the background and is not derived here."),
  L(r"With @(h_0@) in place of @(@eta_{IJ}@), the induced tensor of Definition~@ref{def:matrix-coords-ext} is its pull-back by a configuration, and for @(h_0@) of signature @((9,1)@) it is positive definite, Lorentzian or degenerate according to the configuration. Neither its signature nor that of the composite metric is derived here.")),
 ("F2",
  L(r"Two differences matter. @(@mathfrak C@) is invariant under @(h@mapsto-h@), whence the two classes and the values @(t=9,10@), whereas the allowable domain contains no negative definite metric."),
  L(r"Three differences matter. @(@mathfrak C@) contains no real form, so the positive definite forms also lie only on its boundary, whereas the Riemannian metrics lie inside the allowable domain; the Euclidean contours of the matrix weight are @(h=@mathrm e^{@mathrm i@pi/4}T^{@mathrm T}T@). @(@mathfrak C@) is invariant under @(h@mapsto-h@), whence the two classes and the values @(t=9,10@), whereas the allowable domain contains no negative definite metric.")),
 ("F3",
  L(r"@(hv=-cMv@) on the span of the @(@Lambda^{-1}e_j@)."),
  L(r"@(hv=-cMv@) on the span of the @(@Lambda^{-1}e_j@), @(e_j@) the basis vectors of the negative entries.")),
]
b = open(P, 'rb').read()
h = hashlib.sha256(b).hexdigest()
print("r1 insert:", len(b), "bytes sha256", h, " matches r1:", h == R1_SHA)
if h != R1_SHA:
    sys.exit("r1 hash differs; stop")
s = b.decode('ascii')
for name, old, new in EDITS:
    print(name, "before: old", s.count(old), "new", s.count(new))
    assert s.count(old) == 1 and s.count(new) == 0
    s = s.replace(old, new)
    print(name, "after:  old", s.count(old), "new", s.count(new))
    assert s.count(old) == 0 and s.count(new) == 1
out = s.encode('ascii')
open(P, 'wb').write(out)
print("r2 insert:", len(out), "bytes sha256", hashlib.sha256(out).hexdigest())
