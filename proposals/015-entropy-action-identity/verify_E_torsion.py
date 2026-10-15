"""
Torsion form of the scalar-sector endomorphism (proposal 015).

In the Poisson-limit class (omega = Theta^{-1} closed, e^A_mu = eta^{AB} omega_{mu B}, G_{mu nu} = eta_{AB} e^A_mu e^B_nu,
rho = |Pf omega|), the scalar-sector endomorphism
        E_s = -(1/2) box_G ln rho + (1/4) G^{mu nu} d_mu ln rho d_nu ln rho
is tested against
        E_s  =  (1/4) R_G + (1/16) T_{lam mu nu} T^{lam mu nu} + (1/8) T_{lam mu nu} T^{mu lam nu},
        T^A_{mu nu} = d_mu e^A_nu - d_nu e^A_mu,  T_{lam mu nu} = eta_{AB} e^A_lam T^B_{mu nu}.
This is the Weitzenboeck form  R_G = -(1/4 T^2 + 1/2 T T' - V^2) - 2 nabla V,  V_mu = G^{lam nu} T_{lam mu nu} = d_mu ln rho,
combined with E_s = -(1/2) nabla V + (1/4) V^2.  Test: random closed omega (omega = omegabar + dA, A polynomial of degree 2,3),
2-jets at the origin, both signatures.  The residual must vanish to rounding.
"""
import itertools
import numpy as np
import sympy as sp

x = sp.symbols('x0:4')
rng = np.random.default_rng(2026)


def random_A():
    A = []
    for nu in range(4):
        expr = 0
        for deg in (2, 3):
            for mono in itertools.combinations_with_replacement(range(4), deg):
                if rng.random() < 0.5:
                    expr += sp.Rational(int(rng.integers(-3, 4)), 4) * sp.Mul(*[x[i] for i in mono])
        A.append(expr)
    return A


def jets(P):
    """value, gradient, hessian of a sympy polynomial at the origin"""
    o = {xi: 0 for xi in x}
    v = float(P.subs(o))
    g = np.array([float(sp.diff(P, x[i]).subs(o)) for i in range(4)])
    h = np.array([[float(sp.diff(P, x[i], x[j]).subs(o)) for j in range(4)] for i in range(4)])
    return v, g, h


def run(eta_diag):
    eta = np.diag(eta_diag)
    etai = np.linalg.inv(eta)
    A = random_A()
    base = rng.normal(size=(4, 4))
    base = base - base.T
    omega = sp.Matrix(4, 4, lambda m, n: sp.Rational(int(round(base[m, n] * 4)), 4)
                      + sp.diff(A[n], x[m]) - sp.diff(A[m], x[n]))
    etaS = sp.diag(*[sp.Rational(int(v)) for v in eta_diag])
    G = (omega * etaS.inv() * omega.T).applyfunc(sp.expand)
    e = (etaS.inv() * omega.T).applyfunc(sp.expand)            # e[A, mu] = eta^{AB} omega[mu, B]
    pf = omega[0, 1] * omega[2, 3] - omega[0, 2] * omega[1, 3] + omega[0, 3] * omega[1, 2]
    rho_sign = 1 if float(pf.subs({xi: 0 for xi in x})) > 0 else -1
    rho = sp.expand(rho_sign * pf)
    # jets
    G0 = np.zeros((4, 4)); dG = np.zeros((4, 4, 4)); ddG = np.zeros((4, 4, 4, 4))
    e0 = np.zeros((4, 4)); de = np.zeros((4, 4, 4))
    for m in range(4):
        for n in range(4):
            v, g, h = jets(G[m, n]); G0[m, n] = v; dG[:, m, n] = g; ddG[:, :, m, n] = h
            v, g, h = jets(e[m, n]); e0[m, n] = v; de[:, m, n] = g
    r0, dr, ddr = jets(rho)
    Gi = np.linalg.inv(G0)
    # Christoffel and its derivative at 0
    # Gam^l_{mn} = 1/2 G^{ls}(d_m G_{sn} + d_n G_{sm} - d_s G_{mn})
    t1 = np.einsum('msn->smn', dG)       # d_m G_{sn}  -> index (s,m,n)
    t2 = np.einsum('nsm->smn', dG)       # d_n G_{sm}
    t3 = dG                              # d_s G_{mn}  -> index (s,m,n)
    Gam = 0.5 * np.einsum('ls,smn->lmn', Gi, t1 + t2 - t3)
    dGi = -np.einsum('la,rab,bs->rls', Gi, dG, Gi)               # d_r G^{ls}
    dt = (np.einsum('rmsn->rsmn', ddG) + np.einsum('rnsm->rsmn', ddG) - np.einsum('rsmn->rsmn', ddG))
    dGam = 0.5 * (np.einsum('rls,smn->rlmn', dGi, t1 + t2 - t3) + np.einsum('ls,rsmn->rlmn', Gi, dt))
    # R = G^{sn}( d_r Gam^r_{ns} - d_n Gam^r_{rs} + Gam^r_{rl} Gam^l_{ns} - Gam^r_{nl} Gam^l_{rs} )
    Ric = (np.einsum('rrns->ns', dGam) - np.einsum('nrrs->ns', dGam)
           + np.einsum('rrl,lns->ns', Gam, Gam) - np.einsum('rnl,lrs->ns', Gam, Gam))
    R = np.einsum('ns,ns->', Gi, Ric)
    # E_s
    dlnr = dr / r0
    ddlnr = ddr / r0 - np.outer(dr, dr) / r0 ** 2
    box = np.einsum('mn,mn->', Gi, ddlnr - np.einsum('lmn,l->mn', Gam, dlnr))
    E = -0.5 * box + 0.25 * np.einsum('mn,m,n->', Gi, dlnr, dlnr)
    # torsion
    Tab = np.einsum('mAn->Amn', de) - np.einsum('nAm->Amn', de)       # T^A_{mn} = d_m e^A_n - d_n e^A_m  (de[r,A,mu] = d_r e^A_mu)
    Tl = np.einsum('AB,Al,Bmn->lmn', eta, e0, Tab)
    Tup = np.einsum('lmn,la,mb,nc->abc', Tl, Gi, Gi, Gi)
    T2 = np.einsum('lmn,lmn->', Tl, Tup)
    TT = np.einsum('lmn,mln->', Tl, Tup)
    V = np.einsum('ln,lmn->m', Gi, Tl)
    rhs = 0.25 * R + T2 / 16 + TT / 8
    print(f"  eta={eta_diag}:  E_s = {E:.10f}   R/4 + T^2/16 + TT'/8 = {rhs:.10f}   |diff| = {abs(E - rhs):.1e};"
          f"  V - d ln rho = {np.abs(V - dlnr).max():.1e}")
    return E, R, T2, TT


print("Torsion form of E_s:")
for ed in ([1, 1, 1, 1], [-1, 1, 1, 1]):
    for _ in range(2):
        run(ed)
