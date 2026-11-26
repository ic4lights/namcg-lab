# 095 Gram<->moment non-bridge verification (deterministic, exact sympy + seeded MC)
# Run: python -I proposals/095-g-gram-moment-identification/gram_moment_nonbridge_095.py
import sympy as sp

ok = []
def chk(name, cond):
    ok.append((name, bool(cond)))
    print(name, '=', 'PASS' if cond else 'FAIL')

# ---------- S1: exact Schur-Horn fibre of the 2x2 Gram spectrum map ----------
a, l1, l2, phi = sp.symbols('a lambda1 lambda2 phi', real=True)
tau = l1 + l2   # trace = sum of eigenvalues on the spectrum fibre
b = tau - a
r2 = a*b - l1*l2                      # |G12|^2 forced by trace+det
G = sp.Matrix([[a, sp.sqrt(r2)*sp.exp(sp.I*phi)], [sp.sqrt(r2)*sp.exp(-sp.I*phi), b]])
tr = sp.simplify(G.trace()); dt = sp.simplify(G.det())
x = sp.symbols('x')
chk('S1.trace_equals_tau', tr == tau)
chk('S1.det_equals_l1l2', dt == l1*l2)
# trace and det fix the charpoly of a 2x2 matrix, hence the multiset of eigenvalues;
# numeric instantiation anchors this exactly:
Gnum = G.subs({l1: 3, l2: 1, a: sp.Rational(5,2), phi: sp.pi/7})
cp = sp.factor(sp.expand(Gnum.charpoly(x).as_expr()))
chk('S1.numeric_fibre_spectrum_3_1', cp == (x-3)*(x-1))
chk('S1.numeric_offdiag_nonzero', sp.Abs(Gnum[0,1]) > 0)
# PSD-on-fibre iff a in [l2,l1]: r2 >= 0  <=>  (a-l1)(a-l2) <= 0
chk('S1.psd_iff_interval', sp.expand(r2 + (a-l1)*(a-l2)) == 0)

# ---------- S2: rho2hat range on the fibre ----------
rho = sp.simplify((a**2 + b**2)/tau**2)          # sum (Gii/tau)^2 (shift-free part)
rho_at_mid = rho.subs(a, tau/2)
rho_at_l1  = rho.subs(a, l1)
rho_at_l2  = rho.subs(a, l2)
width = sp.simplify(rho_at_l1 - rho_at_mid)
chk('S2.min_is_one_half', sp.simplify(rho_at_mid - sp.Rational(1,2)) == 0)
chk('S2.max_symmetric', sp.simplify(rho_at_l1 - rho_at_l2) == 0)
chk('S2.max_value', sp.simplify(rho_at_l1 - (l1**2+l2**2)/tau**2) == 0)
chk('S2.width_formula', sp.simplify(width - (l1-l2)**2/(2*tau**2)) == 0)
# monotone decreasing on (l2, tau/2): d/da rho = (4a-2tau)/tau^2 < 0 for a < tau/2
chk('S2.monotone_below_mid', sp.simplify(sp.diff(rho, a).subs(a, tau/4) + 1/tau) == 0)
# degenerate spectrum l1=l2=tau/2 forces a=tau/2 (single-point fibre)
deg = sp.solve(sp.Eq(sp.expand(r2.subs(l2, l1)), 0), a)   # degenerate spectrum l2=l1
chk('S2.degenerate_fibre_point', deg == [l1])   # fibre collapses to a = l1 = tau/2
# rank-one fibre l2=0: rho takes 1 at a=l1 (vertex) and 1/2 at a=l1/2 (barycenter)
chk('S2.rankone_range', sp.simplify(rho.subs({l2: 0, a: l1}) - 1) == 0 and sp.simplify(rho.subs({l2: 0, a: l1/2}) - sp.Rational(1,2)) == 0)

# ---------- S3: explicit rational counterexamples (same spectrum, different rho2hat) ----------
# pair 1: G = diag(3,1) ; G' = [[2,1],[1,2]]  (both spectrum {3,1})
G1 = sp.diag(3, 1)
G2 = sp.Matrix([[2, 1], [1, 2]])
e1 = sorted([str(e) for e in G1.eigenvals()]); e2 = sorted([str(e) for e in G2.eigenvals()])
r_1 = sum((G1[i,i]/4)**2 for i in range(2)); r_2v = sum((G2[i,i]/4)**2 for i in range(2))
chk('S3.same_spectrum_3_1', e1 == ['1','3'] and e2 == ['1','3'])
chk('S3.rho_values_5_8_and_1_2', r_1 == sp.Rational(5,8) and r_2v == sp.Rational(1,2))
chk('S3.values_distinct', r_1 != r_2v)
# PSD check that G2 = G12 phase realisation with a=tau/2: |G12|^2 = 1
chk('S3.G2_psd', all(c >= 0 for c in G2.eigenvals()))
# rank-one pair: w=(1,0) vs w'=(1/sqrt2,1/sqrt2) as 2x1 configurations; Gram spectra {1,0}
w1 = sp.Matrix([1, 0]); w2 = sp.Matrix([1, sp.sqrt(sp.Rational(1,2))])*sp.sqrt(1)
w2 = sp.Matrix([sp.sqrt(sp.Rational(1,2)), sp.sqrt(sp.Rational(1,2))])
g1 = w1*w1.adjoint(); g2 = w2*w2.adjoint()
s1 = [sp.simplify(e) for e in g1.eigenvals()]; s2 = [sp.simplify(e) for e in g2.eigenvals()]
rr1 = sum((g1[i,i]/1)**2 for i in range(2)); rr2 = sum((g2[i,i]/1)**2 for i in range(2))
chk('S3.rankone_spectra_equal_atom', sorted([str(e) for e in s1]) == sorted([str(e) for e in s2]) and set([str(e) for e in s1]) == {'1','0'})
chk('S3.rankone_rho_1_and_1_2', rr1 == 1 and rr2 == sp.Rational(1,2))

# ---------- S4: moment-coordinate identity rho2 = 1 + s2/W^2 at D=2 (092 convention) ----------
g1s, g2s = sp.symbols('g1 g2', positive=True)
W = g1s + g2s
h2 = g1s**2 + g1s*g2s + g2s**2                      # complete homogeneous h_2
rho2_092 = sp.simplify(2*h2/W**2)                    # rho_2 = 2 h_2 / W^2
s2p = (g1s**2 + g2s**2)/W**2                         # s_2/W^2
chk('S4.rho2_eq_1_plus_s2', sp.simplify(rho2_092 - (1 + s2p)) == 0)
# wall value 3/2 at g1=g2, single-slot value 2 at g2=0
chk('S4.wall_3_2', sp.simplify(rho2_092.subs(g2s, g1s) - sp.Rational(3,2)) == 0)
chk('S4.single_2', sp.simplify(rho2_092.subs(g2s, 0) - 2) == 0)
# rho2 evaluated at diagonal profile d_i=Gii/tau equals 1 + sum d_i^2  (= 1 + rho2hat - 1 shift)
d1 = sp.symbols('d1', nonnegative=True); d2 = 1 - d1
chk('S4.diagonal_realisation', sp.simplify(rho2_092.subs({g1s: d1, g2s: d2}) - (1 + d1**2 + d2**2)) == 0)

# ---------- S5: measure-level non-degeneracy, seeded Monte Carlo ----------
import numpy as np
rng = np.random.default_rng(20261119)
A = rng.standard_normal((200000, 2, 2)) + 1j*rng.standard_normal((200000, 2, 2))
GG = A @ A.conj().swapaxes(-1,-2)
trc = np.einsum('nii->n', GG).real
ev = np.linalg.eigvalsh(GG)                          # ascending
p1 = ev[:,1]/trc                                     # larger normalised eigenvalue
rho2hat = (np.abs(GG[:,0,0])**2 + np.abs(GG[:,1,1])**2)/trc**2
band = (p1 > 0.79) & (p1 < 0.81)                     # near-degenerate 4:1 target spectrum band
sel = rho2hat[band]
theo_lo, theo_hi = 0.5, (4**2 + 1**2)/5**2           # spectrum (4,1)/5: [1/2, 17/25]
print('S5.band_count', int(band.sum()))
print('S5.rho_min_max', float(sel.min()), float(sel.max()))
print('S5.theory_range', theo_lo, theo_hi)
chk('S5.fiber_nondegenerate_MC', sel.min() > theo_lo - 0.02 and sel.max() < theo_hi + 0.02
    and (sel.max() - sel.min()) > 0.10)

bad = [n for n, c in ok if not c]
print('SUMMARY', 'ALL PASS' if not bad else 'FAILURES: ' + ', '.join(bad))
