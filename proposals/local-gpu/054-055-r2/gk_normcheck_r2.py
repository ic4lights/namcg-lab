# Gatekeeper check: soft temporal mode of Definition (A) at N=2, manuscript normalisation.
import sympy as sp, mpmath as mp
u,eps,r0,g,G,a=sp.symbols('u epsilon r0 g Gamma a',positive=True)
pi=sp.pi
# A_0 = e^{-3 pi i u/8} At0, At0 = a sigma^3/2 (A = sum A^a sigma^a/2); Tr At0^2 = a^2/2
# exponent: -eps Tr A0^2 + i*gamma/(2g^2) Tr A0^2 (from iS_gamma, eta^{00}=-1)
def Qtrue(gam): return sp.exp(-3*pi*sp.I*u/4)*(eps - sp.I*gam/(2*g**2))/2
def expo(phi,Q): # O=2cos(coef a/2), gamma_c = coef/2, coef = e^{i phi} r0
    gc=sp.exp(sp.I*phi)*r0/2; return -gc**2/(4*Q)
re=lambda e: sp.simplify(sp.re(sp.expand_complex(e)))
fro,con=3*pi/8,3*pi*(1-u)/8
print('frozen g=0   :',sp.simplify(re(expo(fro,Qtrue(0)))-r0**2*sp.cos(3*pi*u/4-pi/4)/(8*eps)))
Qm=sp.exp(-3*pi*sp.I*u/4)*(sp.I*G/(2*g**2))/2
print('frozen gam<0 :',sp.simplify(re(expo(fro,Qm))-g**2*r0**2*sp.sin(3*pi*u/4-pi/4)/(4*G)))
print('contour g=0  :',sp.simplify(re(expo(con,Qtrue(0)))-r0**2/(8*sp.sqrt(2)*eps)))
print('contour gam<0:',sp.simplify(re(expo(con,Qm))+g**2*r0**2/(4*sp.sqrt(2)*G)))
# direct numeric check of the 1D integral, u=0, eps=0.7, r0=1.3
e_,R=0.7,1.3
coef=mp.e**(1j*3*mp.pi/8)*R
f=lambda x: mp.e**(-e_*x**2/2)*2*mp.cos(coef*x/2)
num=mp.quad(f,[-mp.inf,0,mp.inf])
print('numeric |I| =',abs(num),' predicted', abs(2*mp.sqrt(2*mp.pi/e_))*mp.e**(R**2/(8*mp.sqrt(2)*e_)),
      ' stated-model', abs(2*mp.sqrt(2*mp.pi/e_))*mp.e**(R**2/(16*mp.sqrt(2)*e_)))
# rank-one HS normalisation At0 = rho H, Tr H^2=1: eigenvalues +-rho/sqrt2
f2=lambda x: mp.e**(-e_*x**2)*2*mp.cos(coef*x/mp.sqrt(2))
print('HS-normalised |I| =',abs(mp.quad(f2,[-mp.inf,0,mp.inf])), ' exp factor', mp.e**(R**2/(8*mp.sqrt(2)*e_)))
print('Re Q>0 check u in (0,2/3) at gamma<0:', all(float(sp.re(Qtrue(-sp.Rational(1,5)).subs({u:t,eps:sp.Rational(1,100),g:1})))>0 for t in [sp.Rational(i,30) for i in range(1,20)]))
