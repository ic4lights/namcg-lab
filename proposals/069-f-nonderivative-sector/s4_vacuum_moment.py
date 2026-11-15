"""s4: fibre average of the vacuum term (alpha.v)^2 on helicity +-2 at level one.
alpha = n^i c_i, v = n^j s_j, c_i = D_ij s_j, G_ij = s_i.s_j = m^2(q0^2 delta - k k) + l^2(k^2 delta - k k), k along 3.
Claim: <(alpha.v)^2> = (2/15) a^2 tr D^2 = (2/15) a (c.c),  a = m^2 q0^2 + l^2 k^2,  c.c = tr(D G D^T) = a tr D^2."""
import sympy as sp
m, l, q0, k, d1, d2 = sp.symbols("m ell q0 k d1 d2", real=True)
th, ph = sp.symbols("theta phi", real=True)
n = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
kv = sp.Matrix([0, 0, k])
G = m**2 * (q0**2 * sp.eye(3) - kv * kv.T) + l**2 * (k**2 * sp.eye(3) - kv * kv.T)
# G is fixed by the merged identity tr G delta + 2 G = 5 m^2[delta(q0^2 - k^2/5) - (2/5) k k] + l^2 k^2 (4 delta - 2 qhat qhat)
lhs = G.trace() * sp.eye(3) + 2 * G
rhs = 5 * m**2 * (sp.eye(3) * (q0**2 - k**2 / 5) - sp.Rational(2, 5) * kv * kv.T) + l**2 * k**2 * (4 * sp.eye(3) - 2 * kv * kv.T / k**2)
print("merged identity for G:", sp.simplify(lhs - rhs) == sp.zeros(3, 3))
D = sp.Matrix([[d1, d2, 0], [d2, -d1, 0], [0, 0, 0]])     # helicity +-2
av = (n.T * D * G * n)[0]                                   # alpha.v = n^i n^j (D G)_ij
avg = sp.integrate(sp.integrate(av**2 * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi)) / (4 * sp.pi)
a = m**2 * q0**2 + l**2 * k**2
cc = (D * G * D.T).trace()
print("c.c - a tr D^2 =", sp.simplify(cc - a * (D * D).trace()))
print("<(alpha.v)^2> - (2/15) a c.c =", sp.simplify(avg - sp.Rational(2, 15) * a * cc))
