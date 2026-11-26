"""070 s2: quadratic forms of rho R[g_rho] and rho^2 X on plane-wave modes about constant Theta-bar (Euclidean).
omega = wbar + eps dA, A_nu = u_nu cos(phi), phi = p.x.  delta rho = 0 at first order iff Thetabar^{mu nu} p_mu u_nu = 0.
g_rho = G/rho, G = omega omega^T (G^{-1} = Theta^T Theta), rho = Pf omega, X = sum (d_rho Theta^{mu nu})^2.
Claim checked: phi-average at order eps^2 of rho R[g_rho] equals -(1/4) that of rho^2 X on modes with delta rho = 0,
so that c rho R[g_rho] + k rho^2 X has the tensor coefficient c - 4k (c_T = N_tot/6 - 4 kappa_X).
Re-run: python proposals/070-b-content-class/s2_mode_ratio.py
"""
import random, sympy as sp
random.seed(702)
eps, ph = sp.symbols('epsilon phi')
def rnd(): return sp.Rational(random.randint(-3, 3), random.randint(1, 2))
def tr2(e):
    e = sp.expand(e)
    return sum(e.coeff(eps, k)*eps**k for k in range(3))
def mtr(M): return M.applyfunc(tr2)
def avg(e): return sp.simplify(sp.integrate(sp.expand(e), (ph, 0, 2*sp.pi))/(2*sp.pi))

def run(constrain):
    while True:
        wb = sp.zeros(4, 4)
        for i in range(4):
            for j in range(i+1, 4):
                wb[i, j] = rnd(); wb[j, i] = -wb[i, j]
        if wb.det() != 0: break
    Tb = wb.inv()
    while True:
        p = sp.Matrix([rnd() for _ in range(4)]); u = sp.Matrix([rnd() for _ in range(4)])
        if constrain:
            # solve Thetabar^{mu nu} p_mu u_nu = 0 for u_3
            v = (Tb.T*p)            # sum_mu Tb[mu,nu] p_mu
            if v[3] == 0: continue
            u[3] = -sum(v[i]*u[i] for i in range(3))/v[3]
        F = p*u.T - u*p.T
        if F.norm() != 0 and (not constrain or sum(Tb[m, n]*p[m]*u[n] for m in range(4) for n in range(4)) == 0): break
    dw = -sp.sin(ph)*F                       # (dA)_{mu nu} = d_mu A_nu - d_nu A_mu
    w = wb + eps*dw
    T = mtr(Tb - eps*Tb*dw*Tb + eps**2*Tb*dw*Tb*dw*Tb)
    pf = sp.expand(w[0, 1]*w[2, 3] - w[0, 2]*w[1, 3] + w[0, 3]*w[1, 2])
    sgn = sp.sign(pf.subs(eps, 0)); rho = sgn*pf
    r0, r1, r2 = [rho.coeff(eps, k) for k in range(3)]
    rinv = tr2(1/r0 - eps*r1/r0**2 + eps**2*(r1**2/r0**3 - r2/r0**2))
    G = mtr(w*w.T)
    g = mtr(G*rinv); gi = mtr((T.T*T)*rho)
    d = lambda e, m: p[m]*sp.diff(e, ph)
    Gam = [[[tr2(sum(gi[a, l]*(d(g[l, c], b) + d(g[l, b], c) - d(g[b, c], l)) for l in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
    R = 0
    for m in range(4):
        for n in range(4):
            ric = sum(d(Gam[a][m][n], a) - d(Gam[a][m][a], n) for a in range(4))
            ric += sum(Gam[a][a][b]*Gam[b][m][n] - Gam[a][n][b]*Gam[b][m][a] for a in range(4) for b in range(4))
            R += gi[m, n]*ric
    rhoR = tr2(rho*tr2(R))
    X = tr2(sum(d(T[m, n], r)**2 for m in range(4) for n in range(4) for r in range(4)))
    rho2X = tr2(rho**2*X)
    aR, aX = avg(rhoR.coeff(eps, 2)), avg(rho2X.coeff(eps, 2))
    return r1, avg(rhoR.coeff(eps, 1)), aR, aX
ok = True
for t in range(4):
    r1, a1, aR, aX = run(True)
    print(f"delta rho = 0 mode {t}: first-order delta rho = {sp.simplify(r1)}, <rho R>_2 = {aR}, <rho^2 X>_2 = {aX}, ratio = {sp.simplify(aR/aX)}")
    ok &= (sp.simplify(r1) == 0 and aX != 0 and sp.simplify(aR/aX + sp.Rational(1, 4)) == 0)
for t in range(2):
    r1, a1, aR, aX = run(False)
    print(f"generic mode {t} (delta rho != 0): <rho R>_2 = {aR}, <rho^2 X>_2 = {aX}, ratio = {sp.simplify(aR/aX)}")
print("S2 PASS: ratio -1/4 on every delta rho = 0 mode" if ok else "S2 FAIL")
