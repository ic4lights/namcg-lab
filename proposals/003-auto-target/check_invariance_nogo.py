"""Check 3 (proposal 003): a quadratic form on symmetric h_{mu nu} whose matrix depends on the
momentum p only through p^2 (as forced by scaffold-Lorentz invariance when the components of h are
scaffold scalars) is invariant under delta h = p (x) xi + xi (x) p for all xi only if it vanishes.

Let B be the (symmetric) 10x10 matrix of the form at a fixed value c = p^2.  Invariance of
Q(h) = h^T B h under h -> h + delta h for all h means B delta h = 0.  Since B is the same for every p
with p^2 = c, impose B s(p, xi) = 0 for a spanning set of such p and all basis xi, and solve for B.
Also: the linearized Einstein-Hilbert (massless Fierz-Pauli) form is invariant but direction dependent,
so it is not of the required form.
"""
import itertools
import sympy as sp

idx = [(i, j) for i in range(4) for j in range(i, 4)]          # 10 independent components
def vec_from_sym(S):
    return sp.Matrix([S[i, j] for (i, j) in idx])

Bsyms = sp.symbols('b0:55')
B = sp.zeros(10)
it = iter(Bsyms)
for a in range(10):
    for b in range(a, 10):
        B[a, b] = B[b, a] = next(it)

def solve_for(pset, label):
    eqs = []
    for p in pset:
        for c in range(4):
            xi = sp.zeros(4, 1); xi[c] = 1
            S = p*xi.T + xi*p.T
            eqs += list(B*vec_from_sym(S))
    sol = sp.solve(eqs, Bsyms, dict=True)
    Bsol = B.subs(sol[0]) if sol else None
    print(f'{label}: number of equations {len(eqs)}; solution forces B = 0:', Bsol == sp.zeros(10))

E = [sp.Matrix([1 if k == i else 0 for k in range(4)]) for i in range(4)]
a = sp.Integer(1)
ch, sh = sp.cosh(a), sp.sinh(a)
# Euclidean, p^2 = 1 (components of p with lower indices; spanning set on the unit sphere)
solve_for(E, 'Euclidean |p|^2=1')
# Lorentzian eta = diag(-1,1,1,1); p^2 = eta^{mu nu} p_mu p_nu
solve_for([E[1], E[2], E[3], sp.Matrix([sh, ch, 0, 0])], 'Lorentzian p^2=+1')
solve_for([E[0], sp.Matrix([ch, sh, 0, 0]), sp.Matrix([ch, 0, sh, 0]), sp.Matrix([ch, 0, 0, sh])], 'Lorentzian p^2=-1')
solve_for([sp.Matrix([1, 1, 0, 0]), sp.Matrix([1, -1, 0, 0]), sp.Matrix([1, 0, 1, 0]), sp.Matrix([1, 0, 0, 1])], 'Lorentzian p^2=0')

# Linearized EH / massless FP form, Euclidean, indices with delta: ratios (1,-2,2,-1) as in Appendix H
p = sp.Matrix(sp.symbols('p0:4', real=True))
H = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'h{min(i,j)}{max(i,j)}'))
def QFP(pv, Hm):
    p2 = (pv.T*pv)[0]
    tr = Hm.trace()
    t1 = p2*sum(Hm[i, j]**2 for i in range(4) for j in range(4))
    ph = Hm*pv
    t2 = (ph.T*ph)[0]
    t3 = tr*(pv.T*Hm*pv)[0]
    t4 = p2*tr**2
    return sp.expand(t1 - 2*t2 + 2*t3 - t4)
xi = sp.Matrix(sp.symbols('xi0:4', real=True))
dH = p*xi.T + xi*p.T
print('Q_FP gauge invariant under h -> h + p xi + xi p:', sp.expand(QFP(p, H + dH) - QFP(p, H)) == 0)
Hm = sp.zeros(4); Hm[0, 1] = Hm[1, 0] = 1
print('Q_FP at p=(1,0,0,0) and p=(0,0,1,0) for h_01 = 1 (equal p^2):',
      QFP(sp.Matrix([1, 0, 0, 0]), Hm), QFP(sp.Matrix([0, 0, 1, 0]), Hm), '-> direction dependent')

# Trace-constrained block (Theorem mT, eq:FP-gauge): traceless T with
# delta T = p xi + xi p - (1/2) eta (p.xi), eta the tangent metric.  A form on the 9 traceless
# components with p-dependence only through p^2 that is invariant for all xi must vanish.
def traceless_check(eta, pset, label):
    # basis of eta-traceless symmetric tensors: coordinates = the 10 components minus one constraint;
    # parametrise S by its 10 components and impose B-invariance on the projected variations, with B
    # acting on the quotient by adding the trace direction as a free (unconstrained) gauge direction.
    etainv = eta.inv()
    eqs = []
    for p in pset:
        for c in range(4):
            xi = sp.zeros(4, 1); xi[c] = 1
            pu = etainv*p                       # p with raised index for p.xi
            pdotxi = (p.T*etainv*xi)[0]
            S = p*xi.T + xi*p.T - sp.Rational(1, 2)*eta*pdotxi
            # S must be eta-traceless
            assert sp.simplify((etainv*S).trace()) == 0
            eqs += list(Bt*vec_from_sym(S))
    # restrict B to act on traceless tensors: add the condition that B annihilates nothing else; we
    # parametrise traceless tensors by projecting with P(S) = S - (1/4) eta tr(eta^-1 S)
    sol = sp.solve(eqs + list(Bt*vec_from_sym(eta)), Btsyms, dict=True)
    # B restricted to the traceless subspace:
    basis = []
    for (i, j) in idx:
        S = sp.zeros(4); S[i, j] = S[j, i] = 1
        S = S - sp.Rational(1, 4)*eta*(etainv*S).trace()
        basis.append(vec_from_sym(S))
    Bsol = Bt.subs(sol[0])
    restricted = sp.Matrix([[ (u.T*Bsol*w)[0] for w in basis] for u in basis]).applyfunc(sp.simplify)
    print(f'{label}: invariant form restricted to traceless block vanishes:', restricted == sp.zeros(10))

Btsyms = sp.symbols('c0:55')
Bt = sp.zeros(10)
it2 = iter(Btsyms)
for a_ in range(10):
    for b_ in range(a_, 10):
        Bt[a_, b_] = Bt[b_, a_] = next(it2)
eta = sp.diag(-1, 1, 1, 1)
traceless_check(sp.eye(4), E, 'traceless (delta), |p|^2=1')
traceless_check(eta, [E[1], E[2], E[3], sp.Matrix([sh, ch, 0, 0])], 'traceless (eta), p^2=+1')
traceless_check(eta, [E[0], sp.Matrix([ch, sh, 0, 0]), sp.Matrix([ch, 0, sh, 0]), sp.Matrix([ch, 0, 0, sh])], 'traceless (eta), p^2=-1')

# Feynman-de Donder: Q_FP + 2 (p^mu h_{mu nu} - p_nu h/2)^2 = p^2 (h.h - h^2/2), direction blind
ph = H*p
gf = ph - p*H.trace()/2
Q_dD = sp.expand(QFP(p, H) + 2*(gf.T*gf)[0])
p2 = (p.T*p)[0]
target = sp.expand(p2*(sum(H[i, j]**2 for i in range(4) for j in range(4)) - H.trace()**2/2))
print('Q_FP + de Donder gauge-fixing term == p^2 (h.h - h^2/2):', sp.expand(Q_dD - target) == 0)
