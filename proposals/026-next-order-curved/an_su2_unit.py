import pickle, sympy as sp
res = pickle.load(open('su2_a2_unit.pkl', 'rb'))
h1, h2, h3 = sp.symbols('h1 h2 h3')
print('keys', list(res.keys()))
print('Pf omega(0) =', res['Pf_omega'], ' J =', res['J'])
# on-shell relations (r0=h0=1): ODE 2h^2 r h'' + 10 h^2 h' + 4 h r h'^2 + r^2 h'^3 = 0 and its r-derivative
r, hh = sp.symbols('r hh')
hf = sp.Function('hf')(r)
F = 2*hf**2*r*sp.diff(hf, r, 2) + 10*hf**2*sp.diff(hf, r) + 4*hf*r*sp.diff(hf, r)**2 + r**2*sp.diff(hf, r)**3
dF = sp.diff(F, r)
sub = {hf: 1, sp.diff(hf, r): h1, sp.diff(hf, r, 2): h2, sp.diff(hf, r, 3): h3}
dF0 = dF.subs(sub[sp.diff(hf, r, 3)] if False else {}, simultaneous=True)
dFs = dF.subs({sp.diff(hf, r, 3): h3}).subs({sp.diff(hf, r, 2): h2}).subs({sp.diff(hf, r): h1}).subs({hf: 1}).subs({r: 1})
Fs = F.subs({sp.diff(hf, r, 2): h2}).subs({sp.diff(hf, r): h1}).subs({hf: 1}).subs({r: 1})
h2s = sp.solve(Fs, h2)[0]
h3s = sp.solve(dFs.subs(h2, h2s), h3)[0]
u = sp.symbols('u')
h2s_u = sp.simplify(h2s.subs(h1, u)); h3s_u = sp.simplify(h3s.subs(h1, u))
print('h2(u) =', sp.factor(h2s_u), '   h3(u) =', sp.factor(h3s_u))
def onshell(e):
    return sp.factor(sp.simplify(sp.sympify(e).subs({h2: h2s, h3: h3s}).subs(h1, u)))
out = {}
rho = res['rho']
sqrtG = rho**2
print('rho =', sp.factor(rho.subs(h1, u)))
a1 = {k: res[k][0] for k in ('scalar', 'vector', 'weyl_upper', 'weyl_lower')}
a2 = {k: res[k][1] for k in ('scalar', 'vector', 'weyl_upper', 'weyl_lower')}
Ns, nD = 6, 2
tot1 = sqrtG*((Ns-2)*a1['scalar'] + a1['vector'] - nD*sp.Rational(1, 2)*(a1['weyl_upper'] + a1['weyl_lower']))
tot2 = sqrtG*((Ns-2)*a2['scalar'] + a2['vector'] - nD*sp.Rational(1, 2)*(a2['weyl_upper'] + a2['weyl_lower']))
print('sqrtG a1_total on shell:', onshell(tot1))
print('sqrtG a2_total on shell:', onshell(tot2))
for k in a2:
    print(k, 'sqrtG a2 on shell =', onshell(sqrtG*a2[k]))
print('R_G on shell =', onshell(res['R']), '  Weyl^2-type (riem2-2ric2+R2/3) =', onshell(res['riem2'] - 2*res['ric2'] + res['R']**2/3))
pickle.dump(dict(tot2=onshell(tot2), tot1=onshell(tot1)), open('su2_tot_unit.pkl', 'wb'))
