# s2_uniform_rho_r2.py - fixed rerun of s2_uniform_rho.py (proposal 102).
# Defect in the original: the loop variable k of the partition-monomial loop
# (line 44 of s2_uniform_rho.py) rebound the name k to an integer, so at p=2
# sp.product(1 + k/D, (k, 1, p-1)) received limits (1, 1, 1) with variable 1
# (ValueError: Invalid limits given). Fix: dedicated dummy symbol kk.
# Purpose unchanged: exact sympy check that for the uniform profile g_i = 1/D
# the obstruction factor rho_p = p! h_p(g)/W^p equals (a) the sharp fixed-D
# minimum prod_{k=1}^{p-1}(1+k/D) [appH L3179] and (b) the partition form
# sum_{lambda|-p} (p!/z_lambda) prod_k (s_k/W^k)^{m_k} [appH L3177],
# and D_eff = D at uniform.
import sympy as sp

def h_complete(p, D):
    t = sp.symbols("t")
    ser = sp.series((1 - t / D) ** (-D), t, 0, p + 1).removeO()
    return sp.simplify(ser.coeff(t, p))

ok = True
for D in range(2, 6):
    g = [sp.Rational(1, D)] * D
    W = sum(g)
    Deff = sp.Rational(1) / sum(gi * gi for gi in g)
    assert sp.simplify(Deff - D) == 0
    for p in range(1, 7):
        hp = h_complete(p, D)
        rho = sp.factor(sp.simplify(sp.factorial(p) * hp / W ** p))
        kk = sp.symbols("kk", integer=True, positive=True)
        minf = sp.nsimplify(sp.simplify(sp.product(1 + kk / D, (kk, 1, p - 1))))
        partitions = []
        def gen(n, mx, cur):
            if n == 0:
                partitions.append(dict(cur))
                return
            for part in range(min(n, mx), 0, -1):
                cur[part] = cur.get(part, 0) + 1
                gen(n - part, part, cur)
                cur[part] -= 1
                if cur[part] == 0:
                    del cur[part]
        gen(p, p, {})
        part_sum = sp.Integer(0)
        for lam in partitions:
            z = sp.Integer(1)
            for k, mk in lam.items():
                z *= sp.Integer(k) ** mk * sp.factorial(mk)
            mono = sp.Integer(1)
            for k, mk in lam.items():
                sk = sum(gi ** k for gi in g)
                mono *= (sk / W ** k) ** mk
            part_sum += sp.factorial(p) / z * mono
        a = sp.simplify(rho - minf) == 0
        b = sp.simplify(sp.expand(rho - part_sum)) == 0
        print("D=%d p=%d: rho_p=%s  floor=%s  partition match: %s  floor match: %s"
              % (D, p, rho, minf, b, a))
        ok = ok and a and b
print("ALL EXACT CHECKS PASS" if ok else "CHECK FAILURE")
