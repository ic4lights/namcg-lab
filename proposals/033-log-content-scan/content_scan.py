"""Exact content scan of the A-side (fixed-state, contact-completed) and T-side log coefficients on the families of 026/029/031.
Reads data.json (collect.py).  All arithmetic exact.  24 pi units for the A side (Sigma-density), a_2 density (no sqrt G) for the T side.
Symbols: Ns, nD.  Ntot = Ns+2-4nD, b = 1-nD/2.
A-side pieces (all derived from the per-component formulas of 029/031, NOT from the closed forms tested at the end):
  boson, scalar-type component with endomorphism E (positive sign, O=-nabla^2-E):  (R/6-E) - Q/30,  Q = Rii-2Rj = Rsig-3W         [eq (70)]
  Dirac field (4 comps, weight -1), Z_n weights (x,y,z)=(-1/2,1,1/2):  D = -[ x(4R/6-trEf) - y(4/30)Q + z tau ]                    [029; 031 dirac_anomaly_check]
  Dirac periodic (x,y,z)=(1,1,0)
  uniform E_delta contact (cross term, kappa'=-1/240):  C_E = -(1/240)[60 R sum(w trI) - 360 sum(w tr E_pos)]
  Omega_delta contact:  C_Om = sum w tr(J Omega) ; vector: tau_v (=tau) ; Dirac: -(1/2) tau per field (J -> gamma^12/2)
"""
import json, sys
import sympy as sp
Ns, nD = sp.symbols('Ns nD')
R_ = sp.Rational
recs = json.load(open('data.json'))
def g(r, k): return sp.Rational(sp.sympify(r[k]))
Ntot = Ns + 2 - 4*nD; b = 1 - nD/2

def pieces(r):
    R, Rii, Rj, e, tau, Xp = [g(r, k) for k in ('R', 'Rii', 'Rijij', 'e', 'tau', 'Xp')]
    trEv = -g(r, 'trEv_G'); trEf = -g(r, 'trEf_G')           # positive-sign traces
    W = Rj - Rii + R/3; Rs = R - 2*Rii + Rj; Q = Rii - 2*Rj
    tauV = g(r, 'trJOm_v')
    a1bos = (Ns - 2)*(R/6 - e) + (4*R/6 - trEv)
    a1D = -(4*R/6 - trEf)                                      # one Dirac field, weight included
    a1tot = a1bos + nD*a1D
    # periodic
    Sper = a1tot - (Ntot/30)*Q
    # Dirac fixed state
    D = -(R_(-1, 2)*(4*R/6 - trEf) - (4*R_(1, 30))*Q + R_(1, 2)*tau)
    Dper = -((4*R/6 - trEf) - (4*R_(1, 30))*Q)
    fs = a1bos - ((Ns + 2)/30)*Q + nD*D
    # contacts
    CE_b = -R_(1, 240)*(60*R*(Ns + 2) - 360*((Ns - 2)*e + trEv))
    CE_D = -R_(1, 240)*(60*R*(-4) - 360*(-trEf))
    COm_b = tauV
    COm_D = -tau/2
    comp = fs + CE_b + COm_b
    comp_all = Sper + CE_b + nD*CE_D + COm_b + nD*COm_D
    return dict(R=R, Rii=Rii, Rj=Rj, e=e, tau=tau, tauV=tauV, Xp=Xp, W=W, Rs=Rs, Q=Q, trEv=trEv, trEf=trEf, a1bos=a1bos, a1D=a1D, a1tot=a1tot, Sper=Sper, D=D, Dper=Dper,
                fs=fs, CE_b=CE_b, CE_D=CE_D, COm_b=COm_b, COm_D=COm_D, comp=comp, comp_all=comp_all)

bad = 0
print('=== identity checks at every point (exact) ===')
for r in recs:
    P = pieces(r)
    chk = {}
    # 1) 029 assembly at (6,2): s24 = 8R/6-(4e+trEv)+R-trEf-tau-Rj-Rsig+2W
    s24 = R_(8, 6)*P['R'] - (4*P['e'] + P['trEv']) + P['R'] - P['trEf'] - P['tau'] - P['Rj'] - P['Rs'] + 2*P['W']
    chk['fs(6,2) - 029 assembly'] = sp.simplify(P['fs'].subs({Ns: 6, nD: 2}) - s24)
    # 2) Dirac lemma: D - Dper = C_E,D + C_Om,D
    chk['Dirac lemma D-Dper-(C_E,D+C_Om,D)'] = sp.simplify(P['D'] - P['Dper'] - P['CE_D'] - P['COm_D'])
    # 3) tr_V(J Omega^v) = tau
    chk['tauV - tau'] = sp.simplify(P['tauV'] - P['tau'])
    # 4) completed = periodic + all contacts
    chk['comp - comp_all'] = sp.simplify(P['comp'] - P['comp_all'])
    # 5) closed forms
    comp_cf = -P['a1tot']/2 + b*P['tau'] - (Ntot/30)*P['Q']
    chk['comp - closed form'] = sp.simplify(P['comp'] - comp_cf)
    fs_cf = P['Sper'] - R_(3, 2)*(nD*P['a1D']) - nD*P['tau']/2
    chk['fs - closed form'] = sp.simplify(P['fs'] - fs_cf)
    # 6) E-contact = -(3/2) a1
    chk['C_E,all + (3/2) a1tot'] = sp.simplify(P['CE_b'] + nD*P['CE_D'] + R_(3, 2)*P['a1tot'])
    # 7) fs - comp = (3/2)a1bos - tau (n_D independent)
    chk['(fs-comp) - ((3/2)a1bos - tau)'] = sp.simplify(P['fs'] - P['comp'] - (R_(3, 2)*P['a1bos'] - P['tau']))
    # 8) a1 from heat-kernel parts
    if True:
        a1s, a1v, a1d = g(r, 'scalar_a1'), g(r, 'vector_a1'), g(r, 'dirac_a1')
        a1_hk = (Ns - 2)*a1s + a1v - nD*a1d
        chk['a1tot (sector formula) - a1 (heat kernel)'] = sp.simplify(P['a1tot'] - a1_hk)
    for k, v in chk.items():
        if v != 0: bad += 1
    print(r['family'][:28].ljust(28), r['pt'][:24].ljust(24), 'all zero' if all(v == 0 for v in chk.values()) else {k: v for k, v in chk.items() if v != 0})
print('nonzero checks:', bad)

print('\n=== closed forms (symbolic in Ns,nD), 24 pi units ===')
print('Ntot =', sp.expand(Ntot), ' b =', b)
print('A_comp  = -(1/2) a1tot + b tau - (Ntot/30)(Rsig-3W);  A_fs = A_comp + (3/2) a1_bos - tau ; S_per = a1tot - (Ntot/30)(Rsig-3W)')
print('A_fs - S_per = -(3/2) nD a1_D - nD tau/2 (Dirac contacts only);  A_comp - S_per = -(3/2) a1tot + b tau')

print('\n=== rotation-invariant SD family (e=R/6, W=0, tau=R_Sigma+3g/4, Xp=3g/2) ===')
for r in recs:
    if r['family'] not in ('SD example (029)', 'SD rot-invariant'): continue
    P = pieces(r); gg = g(r, 'g')
    a = sp.simplify(P['comp'] - (b - Ntot/30)*P['Rs'])
    f = sp.simplify(P['fs'] - ((b - Ntot/30 - 1)*P['Rs'] + R_(3, 2)*gg))
    p = sp.simplify(P['Sper'] - (b*(P['Xp']) - Ntot/30*P['Rs']))
    print(r['pt'][:24].ljust(24), 'A_comp-(b-Ntot/30)R_S =', a, '| A_fs-((b-Ntot/30-1)R_S+3g/2) =', f, '| S_per-(b X\'-(Ntot/30)R_S) =', p)
print('=> on this family A_comp = (b - Ntot/30) R_Sigma for every content, independent of g;  b - Ntot/30 = (28 - Ns - 11 nD)/30')
print('   zero set of A_comp coefficient: Ns + 11 nD = 28 ->', sp.solve(sp.Eq(b - Ntot/30, 0), Ns))

print('\n=== T side: weighted a_2 = (Ns-2) s + v - nD d ; decomposition ===')
for r in recs:
    s, v, d = g(r, 'scalar_a2'), g(r, 'vector_a2'), g(r, 'dirac_a2')
    vp, dp = v - 4*s, d - 4*s
    T = (Ns - 2)*s + v - nD*d
    Tdec = Ntot*s + (vp - nD*dp)
    ok1 = sp.simplify(T - Tdec) == 0
    chiral = (dp == vp/2)
    tag = r['family'][:28].ljust(28) + ' ' + r['pt'][:22].ljust(22)
    print(tag, 'T - [Ntot s + (v\'-nD d\')] =0:', ok1, '| d\' = v\'/2:', chiral, '| s =', sp.nsimplify(s), "v' =", sp.nsimplify(vp), "d' =", sp.nsimplify(dp))
print('On chiral points T = Ntot s + b v\' with s, v\' != 0: vanishes iff Ntot = 0 and b = 0, i.e. (Ns,nD)=(6,2).')
sc = [(g(r, 'scalar_a2'), g(r, 'vector_a2') - 4*g(r, 'scalar_a2')) for r in recs if (g(r, 'dirac_a2') - 4*g(r, 'scalar_a2')) == (g(r, 'vector_a2') - 4*g(r, 'scalar_a2'))/2]
print('number of points with d\' = v\'/2 exactly:', len(sc))
