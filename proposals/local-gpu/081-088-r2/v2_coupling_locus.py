"""081-088 r2, v2: induced coupling of a=Im alpha and r=|w_perp|^2, and the frame-law locus.

Slots w_i independent circular complex Gaussians, E w_i w_j^* = s^2 g_i delta_ij; unit u; q_i=|u_i|^2.
By circular invariance the phases of u are absorbed into w, so u_i = sqrt(q_i) WLOG.
Checks (exact unless stated; D=3 symbolic in sqrt(q_i), sqrt(g_i), s, then sum q = 1):
 A  E a^2 = s^2 mu/2,  E a r = 0,  E r = s^2 (W - mu),  E a^2 r - E a^2 E r = s^4 Gamma/2;
 B  <Tr Q^2> = 8 s^2 W;  <Tr Q^4> - (256 E a^4 + 256 E a^2 E r + 32 E r^2) = 128 s^4 Gamma;
 C  |(1-uu^+)G u|^2 = Gamma (so the covariance of w_perp with alpha vanishes iff Gamma = 0);
    Tr B = W - mu, Tr B^2 = s_2 - 2 sum q g^2 + mu^2 for B = G^(1/2)(1-uu^+)G^(1/2), hence the
    spectrum of B equals g with one support slot removed only if Gamma = 0; at Gamma = 0 it does (numeric);
 D  Gamma = g^T (diag q - q q^T) g; PSD; annihilates constants;
 E  Haar (q ~ Dirichlet(1,..,1)): Sigma = (1 - J/D)/(D+1), exact moments + MC;
 F  kernel of Sigma_pi = profiles constant on components of the coincidence graph (random finite frame
    laws, 300 cases), stationary set on {sum g = W} = kernel, lower bound lam+ W^2 (1/D_eff - 1/D),
    union-graph kernel for positive combinations, reparametrisation phi(Q) with phi' > 0.
Run: python -I proposals/local-gpu/081-088-r2/v2_coupling_locus.py   Last line: PASS v2
"""
import itertools

import numpy as np
import sympy as sp

ok = True
D = 3
b = sp.symbols('b1:4', positive=True)      # sqrt(q_i)
c = sp.symbols('c1:4', positive=True)      # sqrt(g_i)
s = sp.symbols('s', positive=True)
X = sp.symbols('x1:4', real=True)
Y = sp.symbols('y1:4', real=True)
w = [s*c[i]*(X[i] + sp.I*Y[i])/sp.sqrt(2) for i in range(D)]
alpha = sum(b[i]*w[i] for i in range(D))
a_ = sp.expand(sp.im(sp.expand(alpha)))
absw2 = sum(s**2*c[i]**2*(X[i]**2 + Y[i]**2)/2 for i in range(D))
alpha_re = sp.expand(sp.re(sp.expand(alpha)))
r_ = sp.expand(absw2 - alpha_re**2 - a_**2)
gvars = list(X) + list(Y)


def E(poly):
    poly = sp.Poly(sp.expand(poly), *gvars)
    tot = 0
    for mon, coef in poly.terms():
        f = 1
        for e in mon:
            f *= 0 if e % 2 else sp.factorial2(e - 1)
        tot += coef*f
    return sp.expand(tot)


q = [bi**2 for bi in b]; g = [ci**2 for ci in c]
mu = sum(q[i]*g[i] for i in range(D)); Wg = sum(g)
Gam = sum(q[i]*(g[i] - mu)**2 for i in range(D))
sub = {b[2]: sp.sqrt(1 - b[0]**2 - b[1]**2)}


def z(expr):
    return sp.simplify(sp.expand(expr).subs(sub)) == 0


Ea2, Er, Ear = E(a_**2), E(r_), E(a_*r_)
Ea2r, Ea4, Er2 = E(a_**2*r_), E(a_**4), E(r_**2)
chkA = [z(Ea2 - s**2*mu/2), z(Ear), z(Er - s**2*(Wg - mu)), z(Ea2r - Ea2*Er - s**4*Gam/2)]
print('A E a^2, E a r, E r, coupling:', chkA); ok &= all(chkA)
trQ2 = 16*a_**2 + 8*r_
trQ4 = 256*a_**4 + 256*a_**2*r_ + 32*r_**2
chkB = [z(E(trQ2) - 8*s**2*Wg), z(E(trQ4) - (256*Ea4 + 256*Ea2*Er + 32*Er2) - 128*s**4*Gam)]
print('B <TrQ^2>=8s^2W, TrQ^4 excess 128 s^4 Gamma:', chkB); ok &= all(chkB)
lamQ = sp.symbols('lamQ')
chk_pow = sp.simplify(((-2*sp.Symbol('A') + 2*sp.sqrt(sp.Symbol('A')**2 + sp.Symbol('R')))**4 +
                       (-2*sp.Symbol('A') - 2*sp.sqrt(sp.Symbol('A')**2 + sp.Symbol('R')))**4) -
                      (256*sp.Symbol('A')**4 + 256*sp.Symbol('A')**2*sp.Symbol('R') + 32*sp.Symbol('R')**2)) == 0
print('B power sum p4 = 256a^4+256a^2r+32r^2:', chk_pow); ok &= chk_pow

# C
u = sp.Matrix(b); G = sp.diag(*g); Gh = sp.diag(*c)
P = sp.eye(D) - u*u.T
vC = P*G*u
chkC1 = z((vC.T*vC)[0] - Gam)
B = Gh*P*Gh
chkC2 = z(B.trace() - (Wg - mu)) and z((B*B).trace() - (sum(gi**2 for gi in g) - 2*sum(q[i]*g[i]**2 for i in range(D)) + mu**2))
print('C |(1-uu)Gu|^2 = Gamma:', chkC1, '| Tr B, Tr B^2:', chkC2); ok &= chkC1 and chkC2
rng = np.random.default_rng(882)
gg = np.array([2.0, 2.0, 2.0, 0.7, 1.3]); uu = np.zeros(5, complex); uu[:3] = rng.normal(size=3) + 1j*rng.normal(size=3)
uu /= np.linalg.norm(uu)
Bn = np.diag(np.sqrt(gg)) @ (np.eye(5) - np.outer(uu, uu.conj())) @ np.diag(np.sqrt(gg))
ev = np.sort(np.linalg.eigvalsh(Bn)); target = np.sort(np.array([0.0, 2.0, 2.0, 0.7, 1.3]))
chkC3 = np.max(np.abs(ev - target)) < 1e-12
print('C at Gamma=0 spectrum = g minus one support slot (+0):', chkC3, np.max(np.abs(ev - target))); ok &= chkC3

# D
qs = sp.symbols('q1:4', nonnegative=True); gs = sp.symbols('g1:4')
qv = sp.Matrix(qs); gv = sp.Matrix(gs)
Sig = sp.diag(*qs) - qv*qv.T
mus = sum(qs[i]*gs[i] for i in range(3))
chkD = sp.simplify(((gv.T*Sig*gv)[0] - (sum(qs[i]*(gs[i] - mus)**2 for i in range(3)))).subs(qs[2], 1 - qs[0] - qs[1])) == 0
chkD2 = sp.simplify((Sig*sp.ones(3, 1)).subs(qs[2], 1 - qs[0] - qs[1])) == sp.zeros(3, 1)
print('D Gamma = g^T Sigma g, Sigma 1 = 0:', chkD, chkD2); ok &= chkD and chkD2

# E Haar
for Dh in (3, 5, 8):
    Eqq = sp.Matrix(Dh, Dh, lambda i, j: sp.Rational(2, Dh*(Dh + 1)) if i == j else sp.Rational(1, Dh*(Dh + 1)))
    SigH = sp.diag(*[sp.Rational(1, Dh)]*Dh) - Eqq
    chk = SigH == (sp.eye(Dh) - sp.ones(Dh, Dh)/Dh)/(Dh + 1)
    z_ = rng.normal(size=(200000, Dh)) + 1j*rng.normal(size=(200000, Dh))
    qq = np.abs(z_)**2; qq /= qq.sum(1, keepdims=True)
    SigMC = np.diag(qq.mean(0)) - (qq[:, :, None]*qq[:, None, :]).mean(0)
    err = np.max(np.abs(SigMC - np.array(SigH, dtype=float)))
    print('E Haar D=%d exact Sigma=(1-J/D)/(D+1): %s, MC max err %.1e' % (Dh, chk, err)); ok &= chk and err < 2e-3


# F
def comps(Dn, edges):
    par = list(range(Dn))

    def f(i):
        while par[i] != i:
            i = par[i]
        return i
    for i, j in edges:
        par[f(i)] = f(j)
    return len({f(i) for i in range(Dn)})


bad = 0
for trial in range(300):
    Dn = int(rng.integers(3, 8)); K = int(rng.integers(1, 4))
    Sg = np.zeros((Dn, Dn)); edges = []
    laws = []
    for k in range(K):
        supp = rng.choice(Dn, size=int(rng.integers(1, Dn)), replace=False)
        Sk = np.zeros((Dn, Dn))
        for _ in range(4):
            qv_ = np.zeros(Dn); qv_[supp] = rng.random(len(supp)) + 0.1; qv_ /= qv_.sum()
            Sk += (np.diag(qv_) - np.outer(qv_, qv_))/4
        laws.append(Sk); Sg += Sk*(k + 1)
        edges += list(itertools.combinations(supp, 2))
    ev = np.linalg.eigvalsh(Sg)
    nker = int(np.sum(ev < 1e-10))
    if nker != comps(Dn, edges):
        bad += 1
    gg = rng.random(Dn) + 0.2; Wv = gg.sum()
    P0 = np.eye(Dn) - np.ones((Dn, Dn))/Dn
    evm = np.linalg.eigvalsh(P0 @ Sg @ P0)
    lamplus = np.sort(evm)[1] if Dn > 1 else 0.0
    lam_restricted = np.min(np.linalg.eigvalsh(np.linalg.qr(np.c_[np.ones(Dn), np.eye(Dn)[:, :Dn - 1]])[0][:, 1:].T @ Sg @ np.linalg.qr(np.c_[np.ones(Dn), np.eye(Dn)[:, :Dn - 1]])[0][:, 1:]))
    deff = Wv**2/np.sum(gg**2)
    if gg @ Sg @ gg < lam_restricted*Wv**2*(1/deff - 1/Dn) - 1e-12:
        bad += 1
    # stationarity on the hyperplane: solve 2 Sigma g = lambda 1 with sum g = W
    Mx = np.block([[2*Sg, -np.ones((Dn, 1))], [np.ones((1, Dn)), np.zeros((1, 1))]])
    sol = np.linalg.lstsq(Mx, np.r_[np.zeros(Dn), Wv], rcond=None)[0]
    if abs(sol[-1]) > 1e-9 or np.linalg.norm(Sg @ sol[:-1]) > 1e-9:
        bad += 1
print('F kernel = components, lower bound, stationarity lambda=0: failures', bad); ok &= bad == 0
print('PASS v2' if ok else 'FAIL v2')
