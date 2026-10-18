import sympy as sp
e,a=sp.symbols('e a',positive=True)
den=1-sp.exp(-2*e)
# regular scalar component, flux a in (0,1), field B, eps=sB; Delta = Tr(a)-Tr(0) at fixed cutoff
Dreg=(a-1)*sp.exp(-e)/den+(sp.exp(-e*(1+2*a))-sp.exp(-3*e))/den**2
s=sp.series(Dreg,e,0,2).removeO()
c0=sp.simplify(s.coeff(e,0)); c1=sp.simplify(s.coeff(e,1))
B3=a**3-sp.Rational(3,2)*a**2+a/2
print('C1(a) =',sp.factor(c0),' expected (a^2-a)/2:',sp.simplify(c0-(a**2-a)/2)==0)
print('T1/B =',sp.factor(c1),' expected -B3(a)/3:',sp.simplify(c1+B3/3)==0)
# flagged component (sigma*a>0, a>0): critical channel joins LLL tower
flag=(sp.exp(-e)-sp.exp(-e*(1+2*a)))/den
f=sp.series(flag,e,0,2).removeO()
print('flag a>0: const',sp.simplify(f.coeff(e,0)),' lin',sp.simplify(f.coeff(e,1)),' expected a, -a^2')
# a<0 written with b=|a|: regular tower for ell=m+b: use a->-b, Delta for a in (-1,0) by shifting a'=1-b
b=sp.symbols('b',positive=True)
Dneg=Dreg.subs(a,1-b)  # flux 1-b equivalent to -b up to relabelling m
flagneg=(sp.exp(-e*(1-2*b))-sp.exp(-e))/den
s2=sp.series(Dneg,e,0,2).removeO(); f2=sp.series(flagneg,e,0,2).removeO()
print('reg a=-b: C1',sp.factor(s2.coeff(e,0)),' lin',sp.factor(s2.coeff(e,1)))
print('flag a<0: const',sp.simplify(f2.coeff(e,0)),' lin',sp.simplify(f2.coeff(e,1)),' expected b, +b^2')
# sums over fermionic twists
n=sp.symbols('n',positive=True)
def S2(N): return sum(sp.Rational(k,N)**2 for k in [sp.Rational(2*j-(N-1),2) for j in range(N)])
print([ (N,S2(N),sp.Rational(N*N-1,12*N)) for N in (1,2,3,4,5)])
print('dS2/dn at 1 =',sp.diff((n**2-1)/(12*n),n).subs(n,1))
# net omega coefficient: sum_k sum_sigma sigma*[g_reg + flag*(-a|a|)] : g_reg cancels; flag terms
tot=lambda N: sum( -(+1)*ak*abs(ak) *(1 if ak>0 else 0) + (-1)*(-ak*abs(ak))*(1 if ak<0 else 0) for ak in [sp.Rational(2*j-(N-1),2)/N for j in range(N)])
print('sum_k sigma*flag*(-a|a|):',[(N,tot(N),-S2(N)/2*2/2) for N in (2,3,4,5)])
