import sympy as sp

# S4: 084 joint channel re-checked, plus the frame-averaged coupled Tr Q^4 excess.
# Q = -2i(|u><w| - |w><u|), a = Im<u|w>, r = |w|^2 - |<u|w>|^2,
# Tr Q^4 = 256a^4 + 256a^2 r + 32r^2 (eigenvalues -2a +- 2 sqrt(a^2+r)).
# Slots w_i independent proper CN, E[w_i w_j*] = s^2 g_i delta_ij, unit frame u
# (frame phases drop out of Gamma and mu; test with real positive frames).
# a = sum_i c_i y_i with c_i = u_i/sqrt2 and w_i = (x_i + i y_i)/sqrt2,
# x_i,y_i iid N(0, s^2 g_i).  r = sum_i (x_i^2+y_i^2)/2 - sum_ij c_i c_j (x_i x_j + y_i y_j).

s = sp.symbols('s', positive=True)
a, r = sp.symbols('a r', real=True)
y2 = a**2 + r
tr4 = sp.expand((-2*a + 2*sp.sqrt(y2))**4 + (-2*a - 2*sp.sqrt(y2))**4)
print("(1) TrQ4 eigenvalue form == 256a^4+256a^2r+32r^2:",
      sp.simplify(tr4 - (256*a**4 + 256*a**2*r + 32*r**2)) == 0)
tr2 = sp.expand((-2*a + 2*sp.sqrt(y2))**2 + (-2*a - 2*sp.sqrt(y2))**2)
print("(1b) TrQ2 eigenvalue form == 16a^2+8r:", sp.simplify(tr2 - (16*a**2 + 8*r)) == 0)

def run(Dn):
    gv = list(sp.symbols('g0:%d' % Dn, positive=True))
    uv = list(sp.symbols('u0:%d' % Dn, positive=True))
    cov = lambda m, n: s**2*gv[m % Dn] if m == n else sp.sympify(0)
    E2 = lambda p, q: cov(p, q)
    E4 = lambda p, q, rr, t: cov(p, q)*cov(rr, t) + cov(p, rr)*cov(q, t) + cov(p, t)*cov(q, rr)
    Y = lambda i: i
    X = lambda i: Dn + i
    c = [uv[i]/sp.sqrt(2) for i in range(Dn)]
    aT = [(c[i], Y(i)) for i in range(Dn)]
    rT = [(sp.Rational(1, 2), X(i), X(i)) for i in range(Dn)] + \
         [(sp.Rational(1, 2), Y(i), Y(i)) for i in range(Dn)]
    for i in range(Dn):
        for j in range(Dn):
            rT.append((-c[i]*c[j], X(i), X(j)))
            rT.append((-c[i]*c[j], Y(i), Y(j)))
    Ea2 = sum(cf1*cf2*E2(v1, v2) for cf1, v1 in aT for cf2, v2 in aT)
    Er = sum(cf*E2(v1, v2) for cf, v1, v2 in rT)
    Ea2r = sum(cfa1*cfa2*cfr*E4(va1, va2, vr1, vr2)
               for cfa1, va1 in aT for cfa2, va2 in aT for cfr, vr1, vr2 in rT)
    Ea4 = sum(c1*c2*c3*c4*E4(v1, v2, v3, v4)
              for c1, v1 in aT for c2, v2 in aT for c3, v3 in aT for c4, v4 in aT)
    W = sum(gv)
    mu = sum(gv[i]*uv[i]**2 for i in range(Dn))
    Gam = sum(uv[i]**2*(gv[i]-mu)**2 for i in range(Dn))
    covar2r = Ea2r - Ea2*Er
    print("  D=%d: E[a^2] == s^2 mu/2: %s" % (Dn, sp.simplify(Ea2 - s**2*mu/2) == 0))
    # exact identity check by random rational substitution (symbolic expand too large)
    import random as _rd
    rngsub = _rd.Random(7)
    ok1 = ok2 = True
    for _ in range(5):
        ks = [rngsub.randrange(1,10) for _ in range(Dn)]
        Sk = sum(ks)
        vals = {gv[i]: sp.Rational(rngsub.randrange(1,10), rngsub.randrange(1,10)) for i in range(Dn)}
        vals.update({uv[i]: sp.sqrt(sp.Rational(ks[i], Sk)) for i in range(Dn)})  # unit frame
        vals[s] = sp.Rational(rngsub.randrange(1,10), rngsub.randrange(1,10))
        if sp.nsimplify(sp.together((covar2r - s**4*Gam/2).subs(vals))) != 0: ok1 = False
        if sp.together((256*covar2r - 128*s**4*Gam).subs(vals)) != 0: ok2 = False
    print("  D=%d: Cov(a^2,r) == (s^4/2)Gamma (exact rational substitution): %s" % (Dn, ok1))
    excess = covar2r*256
    print("  D=%d: 256 Cov == 128 s^4 Gamma (exact rational substitution): %s" % (Dn, ok2))
    trq2 = sp.simplify(16*Ea2 + 8*Er)
    print("  D=%d: <TrQ2> = 16Ea2+8Er == 8 s^2 W: %s" % (Dn, sp.simplify(trq2 - 8*s**2*W) == 0))
    Deff = W**2/sum(gi**2 for gi in gv)
    exU = sp.simplify(excess.subs({uv[i]: 1/sp.sqrt(Dn) for i in range(Dn)}))
    tgt = 128*s**4*(W**2/Dn)*(1/Deff - sp.Rational(1, Dn))
    print("  D=%d: uniform-frame excess == 128 s^4 (W^2/D)(1/Deff-1/D): %s"
          % (Dn, sp.simplify(exU - tgt) == 0))

run(2)
run(3)

# (3) full-channel Monte Carlo, D=4: random profile, Haar frames, slots (s=1).
import numpy as np
rng = np.random.default_rng(20261118)
Dn = 4
M = 400000
gg = rng.random(Dn); Wv = gg.sum()
Deff = Wv*Wv/(gg*gg).sum()
Gam_target_avg = (Dn*(gg*gg).sum() - Wv*Wv)/(Dn*(Dn+1))
z = (rng.standard_normal((M, Dn)) + 1j*rng.standard_normal((M, Dn)))/np.sqrt(2)
u = z/np.linalg.norm(z, axis=1, keepdims=True)
w = (rng.standard_normal((M, Dn)) + 1j*rng.standard_normal((M, Dn)))/np.sqrt(2)*np.sqrt(gg)
al = np.abs(np.einsum('mi,mi->m', u.conj(), w))**2
aa = np.imag(np.einsum('mi,mi->m', u.conj(), w))
rr = np.sum(np.abs(w)**2, axis=1) - al
cov_hat = np.mean(aa**2*rr) - np.mean(aa**2)*np.mean(rr)
esc = np.std(aa**2*rr, ddof=1)/np.sqrt(M)
# pooled over frames the covariance carries the frame-level term
# Cov_u(E[a2|u], E[r|u]) = -Var_u(mu)/2 (marginals E[a2|u]=mu/2, E[r|u]=W-mu):
wq = np.abs(u)**2
mu_m = wq @ gg
Gam_m = (wq*(gg[None, :] - mu_m[:, None])**2).sum(axis=1)
target_cov = 0.5*Gam_target_avg - 0.5*np.var(mu_m)
print("  MC D=4: pooled Cov(a2,r) = %.6g +- %.2g ; E_u[Gamma/2] - Var_u(mu)/2 = %.6g ; |z|=%.2f"
      % (cov_hat, esc, target_cov, abs(cov_hat-target_cov)/esc))
trq4 = 256*aa**4 + 256*aa**2*rr + 32*rr**2
trq2 = 8*aa**2 + 8*(aa**2+ (rr + al)*0)  # placeholder replaced below
trq2 = np.abs(2*(-2*aa + 2*np.sqrt(aa**2+rr)))**0  # unused
# per-sample TrQ2 from eigenvalues: 8a^2+8(a^2+r)? = 16a^2+8r
trq2 = 16*aa**2 + 8*rr
e2, es2 = trq2.mean(), trq2.std(ddof=1)/np.sqrt(M)
print("  MC D=4: <TrQ2> = %.5f +- %.2g ; 8 s^2 W = %.5f ; |z|=%.2f"
      % (e2, es2, 8*Wv, abs(e2-8*Wv)/es2))
print("S4 DONE")
