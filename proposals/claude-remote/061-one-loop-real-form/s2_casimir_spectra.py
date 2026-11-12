"""s2: one-loop spectra of the compact member by representation theory, all n.

Operators (alpha=1, gamma=3), verified against explicit matrices in s1 for n=1,2:
  4-block vector   K_A   = C5 - C4tot            (C4tot: so(4) Casimir of End (x) vector)
  transverse (x6)  K_perp= C5 - C4ad - 3
  ghost            K_gh  = C5 - C4ad
  Weyl spinor      K_psi = C5 - C4tot + 3/2       (each so(4) chirality; 16 = 4x(2,1)+4x(1,2))
on End(V_n) minus the identity, V_n = Sym^n(C^4) = so(5) irrep (n/2,n/2).
End(V_n) is decomposed with Racah-Speiser, branched to so(4) with Gelfand-Tsetlin.
Output per n: N, mode counts, zero modes and negative modes of each operator, and the
one-loop modulus exponent Gamma_E' = 1/2 sum' log|K_A| + 6/2 sum' log|K_perp|
 - 1/4*4 sum' log K_psi(both chiralities) - sum' log K_gh (primes: zero modes omitted).
"""
from fractions import Fraction as Fr
from collections import Counter
import itertools, math, sys

def so5_dim(m1,m2):
    return int((2*m1+3)*(2*m2+1)*(m1+m2+2)*(m1-m2+1)/6)

def so5_C(m1,m2): return m1*(m1+3)+m2*(m2+1)

def weights_Vn(n):
    sp=[(Fr(1,2),Fr(1,2)),(Fr(1,2),Fr(-1,2)),(Fr(-1,2),Fr(1,2)),(Fr(-1,2),Fr(-1,2))]
    c=Counter()
    for comb in itertools.combinations_with_replacement(range(4),n):
        w=(sum(sp[i][0] for i in comb),sum(sp[i][1] for i in comb)); c[w]+=1
    return c

def dominant(nu):
    a,b=nu; sgn=1
    if a<0: a=-a; sgn=-sgn
    if b<0: b=-b; sgn=-sgn
    if a<b: a,b=b,a; sgn=-sgn
    if a==b or b==0: return None,0
    return (a,b),sgn

def end_decomp(n):
    lam=(Fr(n,2),Fr(n,2)); rho=(Fr(3,2),Fr(1,2))
    out=Counter()
    for mu,mult in weights_Vn(n).items():
        nu=(lam[0]+mu[0]+rho[0],lam[1]+mu[1]+rho[1])
        d,s=dominant(nu)
        if d is None: continue
        out[(d[0]-rho[0],d[1]-rho[1])]+=s*mult
    out={k:v for k,v in out.items() if v!=0}
    assert all(v>0 for v in out.values())
    return out

def branch(m1,m2):
    res=[]
    k1=m2
    while k1<=m1:
        k2=-m2
        while k2<=m2:
            res.append((k1,k2)); k2+=1
        k1+=1
    return res

def jlr(k1,k2): return (Fr(k1+k2,2),Fr(k1-k2,2))
def c4(jL,jR): return 2*jL*(jL+1)+2*jR*(jR+1)
def tens(j,s):  # su(2): j (x) s
    out=[]; t=abs(j-s)
    while t<=j+s: out.append(t); t+=1
    return out

def spectra(n):
    dec=end_decomp(n)
    N=so5_dim(Fr(n,2),Fr(n,2))
    assert sum(so5_dim(*k)*v for k,v in dec.items())==N*N
    A=Counter(); P=Counter(); G=Counter(); FL=Counter(); FR=Counter()
    for (m1,m2),mult in dec.items():
        if (m1,m2)==(0,0): mult-=1          # remove identity (traceless)
        if mult==0: continue
        C5=so5_C(m1,m2)
        for (k1,k2) in branch(m1,m2):
            jL,jR=jlr(k1,k2); Cad=c4(jL,jR); d=(2*jL+1)*(2*jR+1)
            G[C5-Cad]+=mult*d
            P[C5-Cad-3]+=mult*d
            for tL in tens(jL,Fr(1,2)):
                for tR in tens(jR,Fr(1,2)):
                    A[C5-c4(tL,tR)]+=mult*(2*tL+1)*(2*tR+1)
                FL[C5-c4(tL,jR)+Fr(3,2)]+=mult*(2*tL+1)*(2*jR+1)
            for tR in tens(jR,Fr(1,2)):
                FR[C5-c4(jL,tR)+Fr(3,2)]+=mult*(2*jL+1)*(2*tR+1)
    return N,dec,A,P,G,FL,FR

def stats(c):
    tot=sum(c.values()); z=c.get(0,0); neg=sum(v for k,v in c.items() if k<0)
    lg=sum(v*math.log(abs(float(k))) for k,v in c.items() if k!=0)
    return int(tot),int(z),int(neg),lg

if __name__=="__main__":
    ns=[int(a) for a in sys.argv[1:]] or list(range(1,13))
    print("n  N  | modes(N^2-1) | zeros: K_A K_perp K_gh K_psiL K_psiR | negs: K_A K_perp | Gamma_E'(zero modes omitted) | z16 | zB'=zA+6(zperp-4) | z16/4-zB'/2")
    for n in ns:
        N,dec,A,P,G,FL,FR=spectra(n)
        a=stats(A); p=stats(P); g=stats(G); fl=stats(FL); fr=stats(FR)
        GE=0.5*a[3]+3*p[3]-0.25*4*(fl[3]+fr[3])-g[3]
        zpsi=fl[1]+fr[1]
        z16=4*zpsi; zB=a[1]+6*(p[1]-4)
        print(f"{n:2d} {N:5d} | {N*N-1:7d} | {a[1]:4d} {p[1]:4d} {g[1]:3d} {fl[1]:6d} {fr[1]:6d} | {a[2]:6d} {p[2]:5d} | {GE: .6e} | {z16:7d} | {zB:5d} | {z16/4-zB/2:9.1f}")
