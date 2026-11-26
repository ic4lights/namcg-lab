import os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common073 import *
def solve_be(chi, th, al, ga):
    A=-2; B=-2*th; Cc=th**2-al**2-ga**2+2*chi*(al+ga)
    return (-B-np.sqrt(B*B-4*A*Cc))/(2*A)
ga2=0.1; al2=-0.3-ga2
pts=[('T1',(1.0,0.6,0.0,1.0,0.5,-1/3,-2**-0.5,0.0,2**-0.5)),('T2',(1.0,0.6,0.3,0.8,0.4,-0.5,al2,solve_be(0.3,0.8,al2,ga2),ga2))]
p=0.45
for name,par in pts[int(sys.argv[1]):int(sys.argv[1])+1]:
    kap,s,chi,th,zeta,x,al,be,ga=par; c=np.sqrt(1-s*s)
    C,W,k,n=family(*par); tau=chi+al+ga; Ls,_=lambdas(chi,th,tau)
    for N,Lc in [(16,6),(20,6),(16,5)]:
        cols=[i*N+nn for i in range(40) for nn in range(Lc+1)]
        Mf=lambda q0: K.M_op(C,W,modes(p,q0,N,kap))[:,cols]
        r=K.rank(Mf(0.37+0.11j)); rt=Tl.char_roots(Mf,r)
        un=[]; cc=[0]*6
        for z in rt:
            best=min(((abs(((z+La)**2-(p+c*La)**2)/(kap*p)-round((((z+La)**2-(p+c*La)**2)/(kap*p)).real)),j) for j,La in enumerate(Ls)))
            lval=[((z+La)**2-(p+c*La)**2)/(kap*p) for La in Ls]
            ok=[j for j in range(6) if abs(lval[j]-round(lval[j].real))<5e-3 and int(round(lval[j].real))%2]
            if ok: cc[ok[0]]+=1
            else: un.append((z,best))
        print(name,'N=%d Lc=%d rank %d roots %d per class %s unassigned:'%(N,Lc,r,len(rt),cc),
              ['%.5f%+.5fi (best |dl| %.2g cls %d)'%(z.real,z.imag,b[0],b[1]) for z,b in un],flush=True)
