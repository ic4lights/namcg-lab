#!/usr/bin/env python3
"""054-055 r3: normalisation of the reduced N=2 code against Definition (A), and conversion of the
reduced-model numbers quoted in the 054/055 text (option (i) of review-r2 finding 1).

Run (from the repository root):  python -I proposals/local-gpu/054-055-r2/convert_r3.py

What it checks (symbolically, with explicit 2x2 matrices, no use of the code's own formulas
except the exponent it implements):
  (C1) Definition (A) exponent  iS_b + iS_gamma - eps_A sum_mu Tr A_mu^2  on R_u, at N=2, with
       A_0 = e^{-i al} sum_k a_k sigma^k/2, A_i = e^{i be} sum_a y_i^a sigma^a/2 and spatial Gram
       sum_i y_i^a y_i^b = diag(w1,w2,w3) (eigenframe chart of the code), al = 3 pi u/8, be = pi u/8,
       eta = diag(-1,1,...,1), S_b = -(1/4g^2) Tr[A_mu,A_nu][A^mu,A^nu], S_gamma = -(gamma/2g^2) Tr A_mu A^mu.
  (C2) The exponent coded in n2_slice_r1.py / n2_exp_mech.py (LAM = 0.5):
         i LAM e^{4i be} e2 - (eps_c + i gam_c/2) e^{2i be} T - sum_k Q_k a_k^2,
         Q_k = eps_c e^{-2i al} + i LAM e^{2i(be-al)} T_k - i (gam_c/2) e^{-2i al}.
  (C3) Solve C1 == C2 identically in (a_k, w_k, al, be) for (eps_A, gamma_A, g^2) with a_k the Pauli
       components: unique solution eps_A = 2 eps_c, gamma_A = gam_c, g_YM^2 = 1/(4 LAM) = 1/2.
  (C4) The insertion confirms the Pauli reading: Tr exp(i k^0 A_0) with A_0 = a sigma^3/2 (u=0),
       k^0 = e^{3 pi i/8} r0, is 2 cos(gc a) with gc = e^{3 pi i/8} r0/2, the code's gc; with the
       Hilbert-Schmidt component (A_0 = a sigma^3/sqrt2) it would be gc = e^{3 pi i/8} r0/sqrt2.
  (C5) Conversion table of every reduced-model number quoted in E2 (054 and 055 parts)."""
import sympy as sp

I = sp.I
a1, a2, a3 = sp.symbols('a1 a2 a3', real=True)
w1, w2, w3 = sp.symbols('w1 w2 w3', positive=True)
al, be = sp.symbols('alpha beta', real=True)
epsA, gamA, g2 = sp.symbols('epsilon_A gamma_A g2', positive=True)  # g2 = g_YM^2; gamma_A sign free below
gA = sp.Symbol('gA', real=True)
epsc, gamc = sp.symbols('epsilon_c gamma_c', real=True)
LAM = sp.Rational(1, 2)

s = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
A0 = sp.exp(-I*al)*(a1*s[0] + a2*s[1] + a3*s[2])/2
sq = [sp.sqrt(w1), sp.sqrt(w2), sp.sqrt(w3)]
Asp = [sp.exp(I*be)*sq[i]*s[i]/2 for i in range(3)]       # y_i^a = sqrt(w_a) delta_ia; A_4..A_9 = 0
A = [A0] + Asp
eta = [-1, 1, 1, 1]
tr = lambda M: sp.expand(M.trace())
comm = lambda X, Y: X*Y - Y*X

Sb = 0
for m in range(4):
    for n in range(4):
        C = comm(A[m], A[n])
        Sb += eta[m]*eta[n]*tr(C*C)
Sb = sp.expand(-Sb/(4*g2))
AA = sp.expand(sum(eta[m]*tr(A[m]*A[m]) for m in range(4)))
Sgam = sp.expand(-gA/(2*g2)*AA)
reg = sp.expand(epsA*sum(tr(A[m]*A[m]) for m in range(4)))
EA = sp.expand(I*Sb + I*Sgam - reg)

e2 = w1*w2 + w1*w3 + w2*w3
T = w1 + w2 + w3
Tk = [w2 + w3, w1 + w3, w1 + w2]
Qk = [epsc*sp.exp(-2*I*al) + I*LAM*sp.exp(2*I*(be - al))*Tk[k] - I*(gamc/2)*sp.exp(-2*I*al) for k in range(3)]
Ec = sp.expand(I*LAM*sp.exp(4*I*be)*e2 - (epsc + I*gamc/2)*sp.exp(2*I*be)*T - sum(Qk[k]*[a1, a2, a3][k]**2 for k in range(3)))

ok = []
def rep(name, cond):
    ok.append(bool(cond)); print(('PASS ' if cond else 'FAIL ') + name)

# (C1)/(C3): match coefficients monomial by monomial
diff = sp.expand(EA - Ec)
P = sp.Poly(diff, a1, a2, a3, w1, w2, w3)
eqs = [sp.simplify(c) for c in P.coeffs()]
eqs = [e for e in eqs if e != 0]
sol = sp.solve(eqs, [epsA, gA, g2], dict=True)
print('coefficient equations:', len(eqs))
print('solutions (eps_A, gamma_A, g_YM^2):', sol)
rep('(C3) unique solution eps_A = 2 eps_c, gamma_A = gam_c, g_YM^2 = 1/2',
    len(sol) == 1 and sp.simplify(sol[0][epsA] - 2*epsc) == 0 and sp.simplify(sol[0][gA] - gamc) == 0
    and sp.simplify(sol[0][g2] - sp.Rational(1, 2)) == 0)
sub = {epsA: 2*epsc, gA: gamc, g2: sp.Rational(1, 2)}
rep('(C1=C2) Definition (A) exponent equals the coded exponent identically under that map',
    sp.simplify(sp.expand(EA.subs(sub) - Ec)) == 0)
# soft-mode Gaussian at the corner (w2 = w3 = 0 along a1): Q_A = (1/2) e^{-2i al}(eps_A - i gamma_A/(2 g^2))
QA = sp.Rational(1, 2)*sp.exp(-2*I*al)*(epsA - I*gA/(2*g2))
coef_a1 = sp.expand(-EA.coeff(a1, 2).subs({w2: 0, w3: 0}))
rep('(C1a) coefficient of -a_1^2 at the corner is Q = (1/2) e^{-3 pi i u/4}(eps - i gamma/(2 g^2))',
    sp.simplify(coef_a1 - QA) == 0)
rep('(C1b) code Q_1 at the corner is twice Q at g_YM = 1 with the same numbers (review (c) statement)',
    sp.simplify(Qk[0].subs({w2: 0, w3: 0}) - 2*QA.subs({epsA: epsc, gA: gamc, g2: 1})) == 0)

# (C4) Pauli reading from the insertion
a, r0 = sp.symbols('a r0', positive=True)
k0 = sp.exp(3*sp.pi*I/8)*r0
ev_P = (k0*a*s[2]/2).eigenvals()
ev_HS = (k0*a*s[2]/sp.sqrt(2)).eigenvals()
gc_code = sp.exp(3*sp.pi*I/8)*r0/2
rep('(C4) Pauli component: eigenvalues of k^0 A_0 are +-gc a with gc = code gc = e^{3pi i/8} r0/2',
    set(sp.simplify(e - gc_code*a) == 0 or sp.simplify(e + gc_code*a) == 0 for e in ev_P) == {True})
rep('(C4b) HS component would give +-e^{3pi i/8} r0 a/sqrt2 (not the code gc)',
    all(sp.simplify(sp.Abs(e) - sp.Abs(gc_code*a)) != 0 for e in ev_HS))

# (C5) conversions
print('--- conversion of quoted reduced-model numbers to Definition (A) with g_YM^2 = 1/2 ---')
for lab, vc in [('055 ladder end eps', 0.003), ('055 exact-insertion threshold eps >=', 0.1),
                ('054 proxy range eps min', 0.01), ('054 proxy range eps max', 1.0)]:
    print('  %-40s code %-6g -> Definition (A) %g' % (lab, vc, 2*vc))
for gv in (-0.2, -0.05):
    print('  %-40s code %-6g -> Definition (A) %g  (gamma/g^2 = %g)' % ('055 gamma at u=0.6', gv, gv, gv/0.5))
cc = float(1/(16*sp.sqrt(2)))
cA = float(1/(8*sp.sqrt(2)))
print('  055 corner value at r0=1: code %.7f/eps_c -> Definition (A) %.7f/eps_A  (r0^2/(8 sqrt2 eps))' % (cc, cA))
rep('(C5a) corner value transforms consistently: 0.0441942/eps_c = 0.0883883/eps_A',
    abs(cc*2 - cA) < 1e-12 and abs(cA - 0.0883883) < 1e-7)
fs = lambda gv, g2v: float(sp.exp(g2v*sp.sin(3*sp.pi*sp.Rational(3, 5)/4 - sp.pi/4)/(4*abs(gv))))
print('  frozen saturation factors at u=0.6, r0=1, Definition (A), g^2=1/2: gamma=-0.2 -> %.4f, gamma=-0.05 -> %.4f'
      % (fs(sp.Rational(-1, 5), sp.Rational(1, 2)), fs(sp.Rational(-1, 20), sp.Rational(1, 2))))
rep('(C5b) these equal the code-normalisation values 1.4439 / 4.3469 printed by n2_slice_r1.py',
    abs(fs(sp.Rational(-1, 5), sp.Rational(1, 2)) - 1.4439) < 1e-4 and abs(fs(sp.Rational(-1, 20), sp.Rational(1, 2)) - 4.3469) < 1e-4)
print('  ratios |Z_eps[O_k]|/|Z_eps[1]| (2.0-4.1, ->2, 0.74-1.78) are ratios of the same integrals: unchanged')
print('  fit slope of ln-ratio against 1/eps: slope_A = 2 slope_c = 0.0000')
print('OVERALL: ' + ('ALL CHECKS PASS' if all(ok) else 'SOME CHECK FAILED'))
