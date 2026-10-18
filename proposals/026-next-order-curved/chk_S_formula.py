"""S = tr_V[(b.b)^2] - n_D tr_D[(beta.beta)^2]  with b_s = G_{st} B^t (so(4) valued), beta = spinor lift.
Check (a) generic n_D: S = 4(tr a + tr b)^2 + 16 tr(c c^T) - 2 n_D [ (tr a)^2 + (tr b)^2 ],
       (b) n_D = 2: S = 8 tr(a) tr(b) + 16 tr(c c^T)  >= 0, with a = G^{st} l_s l_t, b = G^{st} r_s r_t, c = G^{st} l_s r_t,
       l^k_s = (1/4) eta^k_{mn} b_{s,mn}, r^k_s = (1/4) etabar^k_{mn} b_{s,mn}  (b_s,mn lowered with G)."""
import numpy as np, sympy as sp
import lib
from common import gammas
rng = np.random.default_rng(1)
eta = [np.array(e.tolist(), dtype=float) for e in lib.eta3()]
etab = [np.array(e.tolist(), dtype=float) for e in lib.etabar()]
gam = [np.array(g.evalf().tolist(), dtype=complex) for g in gammas()]
gmn = [[0.5*(gam[m]@gam[n]-gam[n]@gam[m]) for n in range(4)] for m in range(4)]
worst = 0
for trial in range(5):
    Bup = rng.normal(size=(4, 4, 4)); Bup = Bup - Bup.transpose(0, 2, 1)       # B^t_{mn}
    Mg = rng.normal(size=(4, 4)); Gm = Mg@Mg.T + np.eye(4)                      # G_{st}
    Gi = np.linalg.inv(Gm)                                                      # G^{st}
    b = np.einsum('st,tmn->smn', Gm, Bup)                                       # b_{s,mn}
    bb = sum(Gi[s, t]*b[s]@b[t] for s in range(4) for t in range(4))
    trV = np.trace(bb@bb)
    beta = [0.25*sum(b[s, m, n]*gmn[m][n] for m in range(4) for n in range(4)) for s in range(4)]
    bbD = sum(Gi[s, t]*beta[s]@beta[t] for s in range(4) for t in range(4))
    trD = np.trace(bbD@bbD).real
    l = np.array([[0.25*np.sum(eta[k]*b[s]) for k in range(3)] for s in range(4)])
    r = np.array([[0.25*np.sum(etab[k]*b[s]) for k in range(3)] for s in range(4)])
    a_ = l.T@Gi@l; b_ = r.T@Gi@r; c_ = l.T@Gi@r
    for nD in (0, 1, 2, 3, 4):
        S = trV.real - nD*trD
        pred = 4*(np.trace(a_)+np.trace(b_))**2 + 16*np.trace(c_@c_.T) - 2*nD*(np.trace(a_)**2 + np.trace(b_)**2)
        worst = max(worst, abs(S-pred)/(1+abs(S)))
    S2 = trV.real - 2*trD
    print('trial', trial, ' S(nD=2) =', S2, ' 8 tr a tr b + 16 tr(c c^T) =', 8*np.trace(a_)*np.trace(b_) + 16*np.trace(c_@c_.T))
print('max relative deviation over all nD:', worst)
