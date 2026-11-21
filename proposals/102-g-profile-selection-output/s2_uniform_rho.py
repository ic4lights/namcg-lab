# s2_uniform_rho.py - exact sympy check for proposal 102.
# For the uniform profile g_i = 1/D (W = 1) the obstruction factor of the moment map,
# rho_p = p! h_p(g)/W^p, is checked against the two closed forms recorded in the G block:
#   (a) the sharp fixed-D minimum prod_{k=1}^{p-1} (1 + k/D)  [Uniform minimiser paragraph],
#   (b) the partition form sum_{lambda |- p} (p!/z_lambda) prod_k (s_k/W^k)^{m_k}
#       with s_k the power sums  [Charge-to-edge moment identification paragraph].
# Also checks D_eff = (sum g)^2/sum g^2 = D at uniform.
import sympy as sp

def h_complete(p, D):
    # complete homogeneous symmetric polynomial h_p at g_i = 1/D via the
    # generating function sum_p h_p t^p = prod_i (1 - g_i t)^{-1}
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
        minf = sp.product(1 + sp.Rational(k, D), (k, 1, p - 1)) if p > 1 else sp.Integer(1)
        minf = sp.nsimplify(sp.simplify(minf))
        # partition form
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
                sk = sum(gi ** k for gi in g)          # = D^(1-k)
                mono *= (sk / W ** k) ** mk
            part_sum += sp.factorial(p) / z * mono
        a = sp.simplify(rho - minf) == 0
        b = sp.simplify(sp.expand(rho - part_sum)) == 0
        print("D=%d p=%d: rho_p=%s  floor=%s  partition match: %s  floor match: %s"
              % (D, p, rho, minf, b, a))
        ok = ok and a and b
print("ALL EXACT CHECKS PASS" if ok else "CHECK FAILURE")
