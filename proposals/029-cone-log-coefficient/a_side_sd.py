"""A-side log density on the SD example, Sigma={x1=x2=0}. Uses geom.py (copied from 026) for sector data.
S = (1/24pi)*{ sum over scalar-type comps [n R/6 - trE] weighted + Dirac pieces } - Q/(90pi)-type geometry; see proposal."""
import sympy as sp, sys
import jetlib as jl
from jetlib import Jet
from common import *
import geom, sd_family, lib
use_gaussian(3)
gm = gam_mn_domain()
gam = gammas()
X = sd_family.X
b1 = -(X[0]*X[2] + X[1]*X[3]); b2 = X[0]*X[3] - X[1]*X[2]; b3 = 1 + X[2]**2 - X[3]**2
bsol=[b1,b2,b3]; eta=lib.eta3()
def C(z):
    z=z.c0() if hasattr(z,'c0') else z
    return sp.nsimplify(sp.sympify(QQ_I.to_sympy(z)))
def run(x0, bsol=bsol, eta=eta):
    wj = sd_family.omega_jets(bsol, eta, x0)
    Th = theta_from_omega(wj)
    Ginv, G, rho = geom.metric_data(Th)
    Gam = geom.christoffel(G, Ginv)
    Rm, Ric, Rs = geom.riemann(Gam, G, Ginv)
    g0=[[C(G[i][j]) for j in range(4)] for i in range(4)]
    gi=[[C(Ginv[i][j]) for j in range(4)] for i in range(4)]
    R=C(Rs)
    # orthonormal-frame normal-plane curvature (G diagonal conformally flat: g=rho*delta)
    r=g0[0][0]
    Ricl=[[C(Ric[i][j]) for j in range(4)] for i in range(4)]
    Rii=(Ricl[0][0]+Ricl[1][1])/r
    Rl=lambda a,b,c,d: sum(g0[a][p]*C(Rm[(p,b,c,d)]) for p in range(4))
    Rijij=sum(Rl(i,j,i,j) for i in range(2) for j in range(2))/r**2
    out={}
    A,B=geom.scalar_AB(Th,G,Ginv,rho); om,EV,Om=geom.vassilevich(A,B,G,Ginv,Gam,1); e=-C(EV[0][0])
    A,B=geom.vector_AB(Th,G,Ginv,rho); om,EV,Om=geom.vassilevich(A,B,G,Ginv,Gam,4)
    trEv=-sum(C(EV[i][i]) for i in range(4))
    A,B=geom.dirac_AB(Th,G,Ginv,rho,gm); om,EVd,Omd=geom.vassilevich(A,B,G,Ginv,Gam,4)
    trEf=-sum(C(EVd[i][i]) for i in range(4))
    # T = tr(gamma^{12} Omega^G_{12}),  Omega^G_{12} = Omega^chart_{12} * G^{11}
    g12=gam[0]*gam[1]
    Om12=sp.Matrix(4,4,lambda i,j: C(Omd[0][1][i][j]))
    Tt=sp.simplify((g12*Om12).trace()*gi[0][0])
    Xp=-(trEv-4*e)          # X' = -tr(b.b)_vector
    return dict(R=R,Rii=Rii,Rijij=Rijij,e=e,trEv=trEv,trEf=trEf,T=Tt,Xp=Xp,Rsig=R-2*Rii+Rijij)
if __name__=='__main__':
    pts=[(0,0,sp.Rational(1,3),sp.Rational(1,5)),(0,0,sp.Rational(1,2),sp.Rational(-1,3)),(0,0,sp.Rational(2,3),sp.Rational(1,7))]
    for x0 in pts:
        d=run(x0)
        W=0
        S=(sp.Rational(7,3)*d['R']-12*d['e']+sp.Rational(3,2)*d['Xp']-d['T']-d['Rijij']-d['Rsig']+2*W)  # times 1/24pi
        # general (not assuming e=R/6): scalar-type + Dirac
        S2=(8*d['R']/6-(8*d['e']+(d['trEv']-4*d['e']))+d['R']-d['trEf']-d['T']-d['Rijij']-d['Rsig'])
        print('x0',x0); print('  ',{k:str(v) for k,v in d.items()})
        print('  e-R/6 =',sp.simplify(d['e']-d['R']/6),' Weyl check Rijij-(Rii-R/3)=',sp.simplify(d['Rijij']-(d['Rii']-d['R']/3)))
        print('  24pi*S =',sp.simplify(S),' direct:',sp.simplify(S2),'  Xp, T:',d['Xp'],d['T'], ' 1.5Xp-T =',sp.simplify(sp.Rational(3,2)*d['Xp']-d['T']))
