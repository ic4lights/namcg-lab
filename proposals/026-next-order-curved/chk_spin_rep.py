import sympy as sp
import lib
from common import gammas
gam = gammas()
I = sp.I
sig = [sp.Matrix([[0,1],[1,0]]), sp.Matrix([[0,-I],[I,0]]), sp.Matrix([[1,0],[0,-1]])]
tau = [-I*s for s in sig]
eta = lib.eta3(); etab = lib.etabar()
ok = True
for blk, lab, ee in ((0, 'upper', None), (1, 'lower', None)):
    pass
res = {}
for lab, sl in (('upper', (slice(0,2), slice(0,2))), ('lower', (slice(2,4), slice(2,4)))):
    for name, E in (('eta', eta), ('etabar', etab)):
        for sgn in (1, -1):
            good = True
            for m in range(4):
                for n in range(4):
                    g = (gam[m]*gam[n]-gam[n]*gam[m])/2
                    blkm = g[sl[0], sl[1]]
                    pred = sum((sgn*E[k][m, n]*tau[k] for k in range(3)), sp.zeros(2, 2))
                    if sp.simplify(blkm - pred) != sp.zeros(2, 2):
                        good = False; break
                if not good: break
            if good: print(lab, 'gamma^{mn} =', sgn, '*', name, '^k_{mn} tau_k')
