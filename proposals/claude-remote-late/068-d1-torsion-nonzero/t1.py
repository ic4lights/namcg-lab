import numpy as np, scipy.linalg as sl
from core import *
rng=np.random.default_rng(3)
def roots(c,w,q0,n,seed):
    r=np.random.default_rng(seed)
    Pr=r.normal(size=(30,40)); Vc=r.normal(size=(40,30))
    M0=M_of_q(c,w,q0); Mp=M_of_q(c,w,q0+n); Mm=M_of_q(c,w,q0-n)
    A=M0; B=(Mp-Mm)/2; C=(Mp+Mm)/2-M0
    A,B,C=[Pr@X@Vc for X in (A,B,C)]
    Z=np.zeros((30,30)); I=np.eye(30)
    L=np.block([[Z,I],[-A,-B]]); R=np.block([[I,Z],[Z,C]])
    ev=sl.eig(L,R,right=False)
    return ev[np.isfinite(ev)]
def common(c,w,q0,n):
    a=roots(c,w,q0,n,1); b=roots(c,w,q0,n,2)
    out=[x for x in a if np.abs(b-x).min()<1e-4*(1+abs(x))]
    return np.array(sorted(out,key=lambda z:(round(z.real,3),round(z.imag,3))))
if __name__=="__main__":
  for name,bg in [('flat',flat()),('null g2',null_rotation_g2()),('heis',heisenberg()),('second',second_algebra()),('null g1',null_rotation_g1())]:
      c,w=bg
      dirs=[m for m in range(4) if np.abs(c[:,:,m]).max()==0]
      q0=np.zeros(4); n=np.zeros(4)
      for m in dirs: q0[m]=rng.normal(); n[m]=rng.normal()
      n[0]=2.5  # timelike direction: t plays the role of a frequency
      cr=common(c,w,q0,n)
      print(name,'q0',q0.round(3),'n',n.round(3),'count',len(cr))
      print(np.round(cr,4))
