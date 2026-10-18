import mpmath as mp
mp.mp.dps=30
# (1) heat-trace constant of one Bessel channel (Friedrichs, regular J_nu), measure r dr:
#     Tr_nu(t) = (1/2) int_0^X e^{-x} I_nu(x) dx  with x=r^2/(2t); finite-part constant = -nu/2.
def const(nu,Xs=(4000,16000,64000)):
    f=lambda x: mp.besseli(nu,x)*mp.e**(-x)
    vals=[]
    for X in Xs:
        I=mp.quad(f,mp.linspace(0,X,60))
        vals.append(I/2-mp.sqrt(2*X/mp.pi)/2)
    # remove the X^{-1/2} tail by Richardson on the sequence X -> 4X
    r=[(2*vals[i+1]-vals[i]) for i in range(len(vals)-1)]
    return vals,r
for nu in (mp.mpf(0),mp.mpf('0.25'),mp.mpf('0.5'),mp.mpf('0.75')):
    v,r=const(nu)
    print("nu=%s  finite-part constants (X-sequence) %s  Richardson %s   expected -nu/2=%s"%(nu,[mp.nstr(x,8) for x in v],[mp.nstr(x,8) for x in r],mp.nstr(-nu/2,6)))
# (2) singular-rho cone: scalar operator is unitarily -Box + E_s, Bessel index nu_k = sqrt(k^2+lam^2)/n, lam=(n-1)/2 (appendix H, replica-cone paragraph).
#     constant C(n) = -1/2 sum_k nu_k (zeta-regularised); O(lam^2) = O((n-1)^2) terms drop out of (1-n d_n)(.)|_{n=1}.
n=mp.mpf(1)
def C_first_order(n,branch):
    # k != 0:  sum |k|/n = 2 zeta(-1)/n ; k = 0: friedrichs nu0=|n-1|/(2n) ; less singular: -nu0
    nu0=abs(n-1)/(2*n)
    s0 = nu0 if branch=='F' else -nu0
    return -(2*mp.zeta(-1)/n + s0)/2
def S_coef(branch,n0):
    g=lambda m: C_first_order(m,branch)-m*C_first_order(mp.mpf(1),branch)
    h=lambda m: g(m)-m*mp.diff(g,m)
    return h(n0)
for br in ('F','LS'):
    for n0 in (mp.mpf('0.999999'),mp.mpf('1.000001')):
        print("branch",br,"n=",n0," entropy coefficient per component (units of the scalar value 1/6 -> compare):",mp.nstr(S_coef(br,n0),10))
print("contact formula 1/6-Q, Q=1/4:",mp.mpf(1)/6-mp.mpf(1)/4,"   other branch 1/6+1/4:",mp.mpf(1)/6+mp.mpf(1)/4)
# (3) O(lam^2) term: sum_{k>=1}(sqrt(k^2+lam^2)-k) diverges like (lam^2/2) ln K  -> tip-scale dependent, second order in (n-1)
lam=mp.mpf('0.1')
for K in (10**3,10**4,10**5):
    s=mp.nsum(lambda k: mp.sqrt(k*k+lam**2)-k,[1,K])
    print("K=%d  partial sum / (lam^2/2) - ln K = %s"%(K,mp.nstr(s/(lam**2/2)-mp.log(K),8)))
# (4) unitary equivalence O = -Box + grad f . grad  ~  -Box + E_s,  E_s = -1/2 Box f + 1/4 |grad f|^2  (f = ln rho), flat check
import sympy as sp
x,y=sp.symbols('x y')
f=sp.Function('f')(x,y); u=sp.Function('u')(x,y)
lap=lambda g: sp.diff(g,x,2)+sp.diff(g,y,2)
gr=lambda g,h: sp.diff(g,x)*sp.diff(h,x)+sp.diff(g,y)*sp.diff(h,y)
psi=sp.exp(f/2)*u
Opsi=-lap(psi)+gr(f,psi)
target=sp.exp(f/2)*(-lap(u)+(-lap(f)/2+gr(f,f)/4)*u)
print("check O(e^{f/2}u) = e^{f/2}(-Box u + E_s u):",sp.simplify(Opsi-target)==0)
