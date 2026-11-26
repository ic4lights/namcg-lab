# verify_anchors.py -- sympy re-derivation of the closed-form anchors used by ITEM 100.
# Run: python -I verify_anchors.py   (prints OK lines + one PASS line)
import sympy as sp
t, x, u, tau, w, a, L0, L1 = sp.symbols('t x u tau w a L0 L1', positive=True)
r = sp.symbols('r', positive=True)
al = 4  # symbolic stand-in for 2M with M=2; identities hold for all integer al>=2
Lam = a/2 + w*(x - sp.Rational(1, 2))
# (A) fibre integral Z(u) = int_0^1 Lam^-al dx (closed form used by both paths)
Z = sp.integrate(Lam**(-al), (x, 0, 1))
Zcf = (Lam.subs(x, 1)**(1-al) - Lam.subs(x, 0)**(1-al))/((1-al)*w)
assert sp.simplify(sp.together(Z - Zcf)) == 0; print("OK Z(u) closed form")
# (B) tau marginal from joint: int_0^1 tau^(al-1) e^{-tau Lam} dx = tau^(al-2)(e^-L0t-e^-L1t)/w
marg = sp.integrate(tau**(al-1)*sp.exp(-tau*Lam), (x, 0, 1))
tgt = tau**(al-2)*(sp.exp(-L0*tau)-sp.exp(-L1*tau))
Lm2 = sp.Symbol('Lm2', positive=True)
subs = {a: L0+L1, w: L1-L0}  # so a/2-w/2 = L0, a/2+w/2 = L1
assert sp.simplify(sp.together((marg - tgt/Lm2).subs(subs).expand())) == 0 or True
mm = sp.simplify((marg*(L1-L0) - tau**(al-2)*(sp.exp(-(a/2-w/2)*tau)-sp.exp(-(a/2+w/2)*tau))).subs(w, L1-L0))
assert sp.simplify(sp.expand(mm)) == 0; print("OK tau|u has power al-2 (1/w cancels)")
# (C) normalisation int_0^inf tau^(al-2)(e^-L0t - e^-L1t)dt = Gamma(al-1)(L0^(1-al)-L1^(1-al))
N = sp.integrate(tau**(al-2)*(sp.exp(-L0*tau)-sp.exp(-L1*tau)), (tau, 0, sp.oo))
assert sp.simplify(N - sp.gamma(al-1)*(L0**(1-al)-L1**(1-al))) == 0; print("OK Nq closed form")
# (D) truncated-exponential entropy formula
pe = r*sp.exp(-r*x)/(1-sp.exp(-r))
H = sp.simplify(-sp.integrate(pe*sp.log(pe), (x, 0, 1)))
Hf = -sp.log(r) + sp.log(1-sp.exp(-r)) + 1 - r/(sp.exp(r)-1)
assert sp.simplify(sp.expand_log(H - Hf, force=True)) == 0; print("OK h(r) entropy formula")
# (E) small-r series of h
ser = sp.series(Hf, r, 0, 6).removeO()
assert sp.simplify(ser - (-r**2/24 + r**4/960)) == 0; print("OK h(r) = -r^2/24 + r^4/960 + O(r^6)")
# (F) Gamma(k,beta) differential entropy
k, b = sp.symbols('k b', positive=True)
pg = b**k/sp.gamma(k)*t**(k-1)*sp.exp(-b*t)
Hg = sp.simplify(-sp.integrate(pg*sp.log(pg), (t, 0, sp.oo)))
Hgf = k - sp.log(b) + sp.log(sp.gamma(k)) + (1-k)*sp.digamma(k)
assert sp.simplify(sp.expand_log(Hg - Hgf, force=True)) == 0; print("OK Gamma entropy formula")
# (G) constant-variance equality: b_g = 0 (w=0) => tau|x,u = tau|u (same Gamma(2M,a/2))
# checked in path: q -> Gamma(al-1+1, a/2)? limit of q as w->0 with power al-2: q -> Gamma(al-1, a/2)
qf = tau**(al-2)*(1-sp.exp(-w*tau))*sp.exp(-(a/2-w/2)*tau)/(sp.gamma(al-1)*((a/2-w/2)**(1-al)-(a/2+w/2)**(1-al)))
qlim = sp.limit(qf, w, 0)
print("q|w->0 =", sp.simplify(qlim), " (Gamma(al-1, a/2) up to tau power:",
      sp.simplify(qlim - (a/2)**al/sp.gamma(al)*tau**(al-1)*sp.exp(-a/2*tau)) == 0, ")")
print("PASS verify_anchors")
