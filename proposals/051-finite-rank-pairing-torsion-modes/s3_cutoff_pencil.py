"""051 s3: the action's pairing on cut-off first-order probes.  Part A exact (sympy), part B floating point, part C exact.

Setting: flat class, fixed translation momentum k (lower index, null), transverse polarisation, so that the matrix index
contraction gives eps.eps = 1 and the problem is the scalar one below.  For a probe with kernel
   O = e^{ik.y} g(P) Psi,  Psi = int dt psi(t) R(t),  R(t) = right translation by Lam_t = exp(t lam)
the adjoint operator acts by multiplication by Q2(p,t) = (k + (1 - Lam_t) p).(k + (1 - Lam_t) p), and the pairing of the action
is <O1,O2> = (IR volumes) x int d^4p int dt g1 g2 psi1 psi2.  The volumes are common factors and are dropped.
One-parameter subgroup: the integral over the five other fibre directions is a further smearing, not treated here.

Weights: g^2 = w(p), Gaussian N(0, P^2 delta_ab) in one chosen frame (no Lorentz invariance is possible for a positive weight);
psi1 = phi, psi2 = sqrt(2) eps phi', phi^2 = exp(-t^2/eps^2)/(eps sqrt(pi)), so int psi1^2 = int psi2^2 = 1 and int psi1 psi2 = 0.
Probes: O1 = (c.P) g Psi[psi1] / norm, O2 = g Psi[psi2]; c = v, where d/dt Q2 at t = 0 equals v.p.
These are cut-offs of the P-label mode and of the fibre part R of the first-order class.

 A  exact 2 x 2 Hermitian matrix H_ij = <Oi, Q2 Oj>, eigenvalues, their leading behaviour.
 B  independent Monte Carlo of the same integrals (seeded), and the spectral measure of each probe: a positive measure whose
    support and width are printed.
 C  W_ab = int w p_a p_b is positive definite for every positive weight, so it is never proportional to eta;
    a Lorentz transformation of the weight changes it by a congruence.  Exact on a sample.
"""
import numpy as np
import sympy as sp

d = 4
eta = sp.diag(-1, 1, 1, 1)
eps, P = sp.symbols('epsilon P', positive=True)
tt = sp.Symbol('t', real=True)
ps = sp.symbols('p0:4', real=True)
pv = sp.Matrix(ps)


def case(name, Lam, k):
    print('---', name, ' k =', list(k))
    assert (k.T * eta * k)[0] == 0
    vec = k + (sp.eye(d) - Lam) * pv
    Q2 = sp.expand((vec.T * eta * vec)[0])
    # d/dt Q2 at t = 0: v.p
    dQ2 = sp.diff(Q2, tt)
    dQ20 = sp.expand(dQ2.subs(tt, 0))
    v = sp.Matrix([sp.diff(dQ20, x) for x in ps])
    assert sp.expand(dQ20 - (v.T * pv)[0]) == 0
    print('dQ2/dt at 0 = v.p with v =', list(v), '; |v|^2 =', (v.T * v)[0])
    assert (v.T * v)[0] != 0

    def Ep(expr):
        """Gaussian moments N(0,P^2) of a polynomial in p, degree up to 6."""
        expr = sp.Poly(sp.expand(expr), *ps)
        out = sp.S.Zero
        for mon, co in expr.terms():
            f = co
            for m_ in mon:
                if m_ % 2:
                    f = 0
                    break
                f = f * sp.factorial2(m_ - 1) * P ** m_ if m_ > 0 else f
            out += f
        return out

    cp = (v.T * pv)[0]
    a = Ep(cp ** 2)
    # expectations in t of the coefficient functions of Q2, exact through the characteristic function
    def moment_exp(s):
        return sp.exp(s ** 2 * eps ** 2 / 4)

    def Eg(f, weight):
        """exact: E over N(0, eps^2/2) of weight(t) f(t), with f a polynomial in exp(+-t) or exp(+-i t) rewritten as exponentials."""
        f_exp = sp.expand(f.rewrite(sp.exp))
        total = sp.S.Zero
        for term in sp.Add.make_args(f_exp):
            co, rest = term.as_independent(tt)
            if rest == 1:
                s = sp.S.Zero
            else:
                s = sp.simplify(sp.log(rest).expand(force=True).coeff(tt) if rest.func == sp.exp else sp.diff(sp.log(rest), tt))
            base = moment_exp(s)
            if weight == 'one':
                total += co * base
            elif weight == 't2':     # E[t^2 e^{s t}] = (eps^2/2 + s^2 eps^4/4) e^{s^2 eps^2/4}
                total += co * (eps ** 2 / 2 + s ** 2 * eps ** 4 / 4) * base
            elif weight == 'deriv':  # E[d/dt e^{s t}] = s e^{s^2 eps^2/4}
                total += co * s * base
        return sp.simplify(total)

    Qp = sp.Poly(Q2, *ps)
    def contract(pw, weight):
        out = sp.S.Zero
        for mon, co in Qp.terms():
            mono = sp.prod([ps[i] ** mon[i] for i in range(d)])
            out += Ep(pw * mono) * Eg(sp.sympify(co), weight)
        return sp.simplify(out)

    H11 = contract(cp ** 2, 'one') / a
    H22 = contract(sp.S.One, 't2') * 2 / eps ** 2
    H12 = -eps / sp.sqrt(2) * contract(cp, 'deriv') / sp.sqrt(a)
    H = sp.Matrix([[H11, H12], [H12, H22]])
    print('H11 series:', sp.series(H11, eps, 0, 3))
    print('H22 series:', sp.series(H22, eps, 0, 3))
    print('H12 series:', sp.series(H12, eps, 0, 3))
    predicted = -sp.sqrt(2) * eps * P * sp.sqrt((v.T * v)[0]) / 2
    print('predicted leading H12 = -(eps/sqrt 2) P |v|:', predicted, '; ratio to exact at eps -> 0:',
          sp.limit(H12 / predicted, eps, 0))
    assert sp.limit(H12 / predicted, eps, 0) == 1
    for e_ in (sp.Rational(1, 10), sp.Rational(1, 100), sp.Rational(1, 1000)):
        Hn = H.subs({eps: e_, P: sp.Integer(1)}).evalf(30)
        tr, det = Hn[0, 0] + Hn[1, 1], Hn[0, 0] * Hn[1, 1] - Hn[0, 1] ** 2
        disc = sp.sqrt(tr ** 2 - 4 * det)
        print('  P=1 eps=%s  H12=%.6e  eigenvalues %.6e, %.6e  (real: symmetric matrix on a positive Gram; both residues positive)'
              % (e_, Hn[0, 1], (tr + disc) / 2, (tr - disc) / 2))
    # the unnormalised first-order basis, the one in which a Jordan block is read: O2raw = O2 / (sqrt(2) eps)
    # psi = phi' stays a fixed distribution direction: <O1,Q2 O2raw> stays finite while <O2raw,O2raw> = 1/(2 eps^2) diverges.
    print('  in the basis O1, O2raw = O2/(sqrt2 eps):  <O1,Q2 O2raw> -> %s, <O2raw,O2raw> = 1/(2 eps^2)' % sp.limit(H12 / (sp.sqrt(2) * eps), eps, 0))
    return Q2, v


# boost in the (0,2) plane on lower indices
ch, sh = sp.cosh(tt), sp.sinh(tt)
Lb = sp.Matrix([[ch, 0, sh, 0], [0, 1, 0, 0], [sh, 0, ch, 0], [0, 0, 0, 1]])
Q2b, vb = case('boost(0,2)', Lb, sp.Matrix([-1, 1, 0, 0]))
# rotation in the (1,2) plane, on the covering line (the periodic images are exponentially small at small eps)
c_, s_ = sp.cos(tt), sp.sin(tt)
Lr = sp.Matrix([[1, 0, 0, 0], [0, c_, -s_, 0], [0, s_, c_, 0], [0, 0, 0, 1]])
Q2r, vr = case('rotation(1,2)', Lr, sp.Matrix([-1, 1, 0, 0]))

# B: independent Monte Carlo for the boost case at eps = 0.05, P = 1, and the spectral measure
rng = np.random.default_rng(51)
N = 4000000
e_ = 0.05
p = rng.normal(0, 1, size=(N, 4))
tv = rng.normal(0, e_ / np.sqrt(2), size=N)      # phi^2
chv, shv = np.cosh(tv), np.sinh(tv)
pp = np.stack([chv * p[:, 0] + shv * p[:, 2], p[:, 1], shv * p[:, 0] + chv * p[:, 2], p[:, 3]], axis=1)
kv = np.array([-1.0, 1, 0, 0])
vecv = kv + p - pp
etan = np.array([-1.0, 1, 1, 1])
Qm = (vecv ** 2 * etan).sum(axis=1)
vn = np.array([float(x) for x in vb])
cpn = p @ vn
a_ = (cpn ** 2).mean()
w2 = 2 * tv ** 2 / e_ ** 2                        # psi2^2 / phi^2
w12 = -np.sqrt(2) * tv / e_                       # psi1 psi2 / phi^2
print('--- Monte Carlo, boost, eps = %.2f, P = 1, N = %d' % (e_, N))
print('  <O2,O2> = %.4f (exact 1), <O1,O2> = %.2e (exact 0)' % (w2.mean(), (cpn * w12).mean() / np.sqrt(a_)))
H11m = (cpn ** 2 * Qm).mean() / a_
H22m = (w2 * Qm).mean()
H12m = (cpn * w12 * Qm).mean() / np.sqrt(a_)
print('  H11 = %.5f, H22 = %.5f, H12 = %.5f' % (H11m, H22m, H12m))
print('  eigenvalues', [round(float(x), 5) for x in np.linalg.eigvalsh(np.array([[H11m, H12m], [H12m, H22m]]))])
for lab, wt in (('O1', cpn ** 2 / a_), ('O2', w2)):
    order = np.argsort(Qm)
    cw = np.cumsum(wt[order]) / wt.sum()
    q05, q50, q95 = (Qm[order][np.searchsorted(cw, x)] for x in (0.05, 0.5, 0.95))
    print('  spectral measure of %s: positive weights by construction; quantiles 5%%, 50%%, 95%% of Q2 = %.4f, %.4f, %.4f' % (lab, q05, q50, q95))

# C
Wm = np.diag([1.0, 1, 1, 1])
L = np.array([[np.cosh(1.3), np.sinh(1.3), 0, 0], [np.sinh(1.3), np.cosh(1.3), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
Wb = L @ Wm @ L.T
print('--- W: at a boost of rapidity 1.3 the Gaussian frame weight has W_00 = %.4f, W_11 = %.4f, W_01 = %.4f, eigenvalues %s' %
      (Wb[0, 0], Wb[1, 1], Wb[0, 1], np.round(np.linalg.eigvalsh(Wb), 4)))
assert (np.linalg.eigvalsh(Wb) > 0).all() and Wb[0, 0] > 0
print('W_00 > 0 for every positive weight, while eta_00 = -1 and eta_11 = +1, so W = c eta has no solution (W_00 = -c, W_11 = c).')
print('ALL ASSERTIONS PASSED')
