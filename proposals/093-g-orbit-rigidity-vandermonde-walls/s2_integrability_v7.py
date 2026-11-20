# s2_integrability_v7.py  -- proposal 093, round 1 (authoritative version)
# Run from repo root:  python -I proposals/093-g-orbit-rigidity-vandermonde-walls/s2_integrability_v7.py
# Exact beta-integral claims for the inverse-Jacobian moment of the |V| singularity
# in the named fixed-trace Dirichlet-beta family on the D=2 Gram coordinate u in (0,1).
import sympy as sp

a, u, eps, beta, v, t = sp.symbols("a u eps beta v t", positive=True)
sq2 = sp.sqrt(2)

def ex(expr, tgt, tol=1e-12):
    if sp.simplify(sp.gammasimp(expr - tgt)) == 0:
        return True
    try:
        return abs(float(sp.N(expr - tgt))) < tol
    except Exception:
        return False

def gammom(m, aa, bb):
    # int_0^1 u^m u^bb (1-u^2)^(aa-1) du = 1/2 B((m+bb+1)/2, aa), written via Gamma
    x = (m + bb + 1) / 2
    return sp.Rational(1, 2) * sp.gamma(x) * sp.gamma(aa) / sp.gamma(aa + x)

print("== PART E: D=2 exact inverse-Jacobian moments, (a, beta) family ==")
E1 = sp.simplify(gammom(-1, a, 2) / gammom(0, a, 2))
closed1 = (2 * a + 1) * sp.gamma(a + sp.Rational(1, 2)) / (a * sp.sqrt(sp.pi) * sp.gamma(a))
chain = E1 - sp.gamma(a + sp.Rational(3, 2)) / (a * sp.gamma(sp.Rational(3, 2)) * sp.gamma(a))
ok_chain = sp.simplify(sp.gammasimp(chain)) == 0 or max(
    abs(float(chain.subs(a, sp.Rational(q, 4)))) for q in range(4, 41)) < 1e-12
rec = 2 * sp.gamma(a + sp.Rational(3, 2)) - (2 * a + 1) * sp.gamma(a + sp.Rational(1, 2))
ok_rec = sp.simplify(rec) == 0 or max(
    abs(float(rec.subs(a, sp.Rational(q, 4)))) for q in range(4, 41)) < 1e-12
okE1 = ok_chain and ok_rec
sweep = all(abs(float(E1.subs(a, aa)) - float(closed1.subs(a, aa))) < 1e-9 for aa in (1, 2, 3, 5, 7))
print("E[u^-1](beta=2) = (2a+1)Gamma(a+1/2)/(a sqrt(pi) Gamma(a)) : chain %s, recursion %s, sweep %s"
      % (ok_chain, ok_rec, sweep))
print("value at a=1 (repo member |N-2M|+1) equals 3/2 : %s" % ex(closed1.subs(a, 1), sp.Rational(3, 2)))
Ehalf = sp.simplify(gammom(-sp.Rational(1, 2), a, 2) / gammom(0, a, 2))
okE2 = ex(Ehalf.subs(a, 1), sp.Rational(6, 5)) and ex(Ehalf.subs(a, 2), sp.Rational(4, 3))
print("E[u^-1/2](beta=2) at a=1 equals 6/5 and at a=2 equals 4/3 : %s" % okE2)
print("PART E RESULT:", "PASS" if (okE1 and sweep and okE2) else "FAIL")

print("== PART E2: beta=0 members: exact logarithmic divergence ==")
Ia1 = sp.integrate(1 / u, (u, eps, 1))
okE3 = ex(sp.limit(Ia1 / sp.log(1 / eps), eps, 0), 1)
print("a=1: int_eps^1 u^-1 du = log(1/eps), log-coefficient 1 : %s" % okE3)
Ia2 = sp.integrate((1 - u ** 2) / u, (u, eps, 1))
okE4 = ex(Ia2, sp.log(1 / eps) - (1 - eps ** 2) / 2)
Z2 = gammom(0, 2, 0)  # 1/2 B(1/2, 2)
okE5 = ex(Z2, sp.Rational(2, 3))
okE6 = ex(sp.limit(Ia2 / Z2 / sp.log(1 / eps), eps, 0), sp.Rational(3, 2))
print("a=2: int_eps^1 (1-u^2)/u du = log(1/eps)-(1-eps^2)/2 : %s ; Z(2)=2/3 : %s ; normalized coefficient 3/2 = C(2) : %s"
      % (okE4, okE5, okE6))
C = lambda aa: sp.simplify(2 * sp.gamma(aa + sp.Rational(1, 2)) / (sp.sqrt(sp.pi) * sp.gamma(aa)))
okE7 = all(ex(C(aa), 1 / gammom(0, aa, 0)) for aa in (1, 2, 3, 4))
print("general beta=0 coefficient C(a) = 2Gamma(a+1/2)/(sqrt(pi)Gamma(a)) = 1/Z(a,0) for a=1..4 : %s" % okE7)
print("PART E2 RESULT:", "PASS" if (okE3 and okE4 and okE5 and okE6 and okE7) else "FAIL")

print("== PART F: D=3 wall and triple-point exponents of the beta-family weight ==")
vv = sp.Rational(3, 4)
p1, p2, p3 = vv / 2 + u / 2, vv / 2 - u / 2, 1 - vv
w3 = (p1 - p2) ** beta * (p1 - p3) ** beta * (p2 - p3) ** beta
rwall = sp.simplify(sp.limit(w3 / u ** beta, u, 0, "+"))
okF1 = ex(rwall, (3 * vv / 2 - 1) ** (2 * beta)) and rwall != 0
print("D=3 wall (v=3/4): weight/u^beta -> (3v/2-1)^(2beta) = (1/8)^(2beta) nonzero : %s" % okF1)
okF2 = ex(sp.integrate(u ** (beta - 1), (u, 0, sp.Rational(1, 4))), 4 ** (-beta) / beta)
print("D=3 wall: int_0 u^(beta-1)du = 4^(-beta)/beta, finite iff beta>0 : %s" % okF2)
tp = [sp.Rational(1, 3) + t / sq2, sp.Rational(1, 3), sp.Rational(1, 3) - t / sq2]
wt = (tp[0] - tp[1]) ** beta * (tp[1] - tp[2]) ** beta * (tp[0] - tp[2]) ** beta
rt = sp.simplify(sp.limit(wt / t ** (3 * beta), t, 0, "+"))
okF3 = ex(rt, 2 ** (-beta / 2))
print("D=3 triple: weight/t^(3beta) -> 2^(-beta/2) nonzero, exponent = C(3,2)beta : %s" % okF3)
okF4 = True
for m in (2, 3, 4):
    # simplex-local radial exponent of |V|^-1 * weight * area element at an m-fold
    # coincidence: C(m,2)(beta-1) from factors and |V|^-1, +(m-2) from t^(m-2) dt
    e = sp.binomial(m, 2) * (beta - 1) + (m - 2)
    okF4 = okF4 and sp.simplify((e + 1) - (sp.binomial(m, 2) * (beta - 1 + sp.Rational(2, m)))) == 0
    print("m=%d: integrand exponent e; e+1 = C(m,2)(beta-(1-2/m)); e>-1 <=> beta > 1-2/m = %s"
          % (m, 1 - sp.Rational(2, m)))
print("D=3 triple: radial integrand exponent 3beta-2, integrable iff beta>1/3 : %s"
      % bool(okF4 and sp.simplify((sp.binomial(3,2)*(beta-1)+1) - (3*beta-2)) == 0))
print("PART F RESULT:", "PASS" if (okF1 and okF2 and okF3 and okF4) else "FAIL")

print("== PART G: consistency with the accepted 091 numerals (a=1, beta=2 member) ==")
okG1 = ex(sp.integrate(3 * u ** 2, (u, 0, eps)), eps ** 3)
print("P(u<eps) at (a=1,beta=2): int_0^eps 3u^2 du = eps^3 : %s" % okG1)
okG2 = ex(gammom(0, 1, 2), sp.Rational(1, 3))
print("normalization int_0^1 u^2 du = 1/3 (density 3u^2) : %s" % okG2)
okG3 = ex(E1.subs(a, 1), sp.Rational(3, 2))
print("E|p1-p2|^-1 = E[u^-1] at (a=1,beta=2) = 3/2 : %s" % okG3)
print("PART G RESULT:", "PASS" if (okG1 and okG2 and okG3) else "FAIL")

allok = okE1 and sweep and okE2 and okE3 and okE4 and okE5 and okE6 and okE7 and okF1 and okF2 and okF3 and okF4 and okG1 and okG2 and okG3
print("S2 OVERALL:", "PASS" if allok else "FAIL")
