"""Orientation sign vs sign(y4*y0), and conical growth of |r|/|p| near Sigma (sheet y0<0 as realised by the orbit)."""
import numpy as np
from scipy.optimize import minimize
from check_flux_classification import *
rng=np.random.default_rng(3)
tab={}
for t in range(150):
    z=rand_z_pos(rng,rng.uniform(0.5,4)); M0=Mfun(z); S=structure(M0)
    Q,y,y4=Qmat(M0); Qhi=np.linalg.inv(sqrtm_sym(Q)); om=Qhi@S[:,:,0]@Qhi
    Op,Om=hodge_split(om); sg=+1 if amp(Op)>amp(Om) else -1
    tab.setdefault((int(np.sign(y[0])),int(np.sign(y4))),set()).add(sg)
print("orientation sign (+1=SD) by (sign y0, sign y4) [centre basis vector 0]:",tab)
n=2.0; ell=n/2
def point_from_y(yv):
    def o(p):
        zz=p[:4]+1j*p[4:]; q=np.real(zz.conj()@H@zz)
        if q<1e-6: return 1e6
        zz=zz*np.sqrt(n/q); return np.sum((Mfun(zz)[:5,5]-yv)**2)
    best=None
    for t in range(12):
        r=minimize(o,rng.normal(size=8),method='Nelder-Mead',options={'xatol':1e-13,'fatol':1e-28,'maxiter':80000})
        if best is None or r.fun<best.fun: best=r
    zz=best.x[:4]+1j*best.x[4:]; zz=zz*np.sqrt(n/np.real(zz.conj()@H@zz)); return Mfun(zz),best.fun
for d in (0.2,0.1,0.05):
    y4=ell*(1+d); y0=-np.sqrt(ell**2+y4**2)
    M0,res=point_from_y(np.array([y0,0,0,0,y4])); S=structure(M0)
    vals=[]
    for ph in np.linspace(0,np.pi,91):
        F=S[:,:,0]*np.cos(ph)+S[:,:,1]*np.sin(ph); f1,f2,_,p,r=flux_ratio(F); vals.append(r/p)
    cf_par=abs(ell-y4)/(ell+y4)
    ell_,ax,pe,_=closed_form_ratios(M0)
    print("y4=l(1+%.2f) res=%.1e |r|/|p| in [%.5f,%.5f]; from closed form f2/f1 in [%.5f,%.5f] -> |r|/|p|=(1-x)/(1+x) in [%.5f,%.5f]"%(d,res,min(vals),max(vals),min(ax,pe),max(ax,pe),(1-max(ax,pe))/(1+max(ax,pe)),(1-min(ax,pe))/(1+min(ax,pe))))
