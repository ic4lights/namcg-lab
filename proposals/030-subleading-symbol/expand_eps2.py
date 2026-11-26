"""030 script 3: expand the symbols r0, r1, r2 of nlo_symbol.py to second order in eps in the ORIGINAL momentum variables
o_a = omega_a (omega'_a = o_a - eps zeta alpha_a S), zeta, with Ui0 = 1/(eta o o - z); then average over the phase phi (S,C -> trigonometric means).
Output: dict  order -> {n: polynomial in (o, zeta, al, ka)} such that  <r_k>_phi |_{eps^2} = sum_n Ui0^n P_{k,n}(o, zeta; alpha, kappa).
Ui^n -> Ui0^n [1 - n Ui0 delta + n(n+1)/2 Ui0^2 delta^2],  delta = eps d1 + eps^2 d2, d1 = -2 S zeta (o.alpha), d2 = S^2 zeta^2 (alpha.alpha) (truncated at eps^2)."""
import sympy as sp, pickle, time

def phase_mean(expr, S, C):
    P = sp.Poly(sp.expand(expr), S, C)
    out = 0
    for (a, b), cf in P.terms():
        if a % 2 or b % 2:
            continue
        m = sp.gamma(sp.Rational(a + 1, 2)) * sp.gamma(sp.Rational(b + 1, 2)) / (sp.pi * sp.gamma(sp.Rational(a + b, 2) + 1))
        out += cf * sp.nsimplify(sp.simplify(m))
    return sp.expand(out)

def expand(pk='nlo_symbol_eta4.pkl', eta=(-1, 1, 1, 1), order=2):
    d = pickle.load(open(pk, 'rb'))
    w, al, ka, zeta, S, C, eps, Ui = d['w'], d['al'], d['ka'], d['zeta'], d['S'], d['C'], d['eps'], d['Ui']
    n = len(w)
    o = sp.symbols('o1:%d' % (n + 1)); Ui0 = sp.Symbol('Ui0')
    sub = {w[a]: o[a] - eps * zeta * al[a] * S for a in range(n)}
    oa = sum(eta[a] * o[a] * al[a] for a in range(n)); aa = sum(eta[a] * al[a] ** 2 for a in range(n))
    d1 = -2 * S * zeta * oa; d2 = S ** 2 * zeta ** 2 * aa
    res = {}
    for name in ['r0', 'r1', 'r2']:
        t0 = time.time()
        Pn = sp.Poly(d[name], Ui)
        acc = {k: {} for k in range(order + 1)}
        for (m,), cf in Pn.terms():
            cs = sp.expand(cf.subs(sub, simultaneous=True))
            Pe = sp.Poly(cs, eps)
            ce = {k: Pe.coeff_monomial(eps ** k) for k in range(order + 1)}
            # (1 + x)^(-m) truncated: coefficient of eps^j in Ui^m expansion factor
            f = {0: 1, 1: -m * Ui0 * d1, 2: -m * Ui0 * d2 + sp.Rational(m * (m + 1), 2) * Ui0 ** 2 * d1 ** 2}
            for k in range(order + 1):
                tot = 0
                for j in range(k + 1):
                    tot += ce[k - j] * f[j]
                tot = sp.expand(tot * Ui0 ** m)
                if tot != 0:
                    acc[k][m] = acc[k].get(m, 0)
                    # collect into powers of Ui0 later
                    acc[k][m] += tot
        res[name] = {}
        for k in range(order + 1):
            tot = sp.expand(sum(acc[k].values()))
            tot = phase_mean(tot, S, C)
            Pu = sp.Poly(tot, Ui0)
            res[name][k] = {mm[0]: sp.expand(c) for mm, c in Pu.terms()}
        print(name, "done in %.1fs" % (time.time() - t0), flush=True)
    return dict(res=res, o=o, al=al, ka=ka, zeta=zeta, eta=eta)

if __name__ == "__main__":
    E = expand()
    for name in ['r0', 'r1', 'r2']:
        for k in range(3):
            terms = E['res'][name][k]
            print(name, "eps^%d" % k, ": powers of Ui0:", sorted(terms.keys()), " nterms:", {n: len(sp.Add.make_args(c)) for n, c in terms.items()})
    pickle.dump(E, open('eps2_eta4.pkl', 'wb'))
    print("r0 eps^2 coefficient (phase-averaged):", E['res']['r0'][2])
    print("r1 eps^0,1,2 coefficients:", {k: E['res']['r1'][k] for k in (0, 1, 2)})
