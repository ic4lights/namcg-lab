import numpy as np
from core import *
rng=np.random.default_rng(5)
klow=np.array([1.,0,0,1.])
def nullq(shift):
    v=rng.normal(size=3); n=np.array([np.linalg.norm(v),*v]); return n-shift*klow
def partial(c,w,q,n,Lmax=4):
    A=M_of_q(c,w,q); P=M_of_q(c,w,q+n); Mi=M_of_q(c,w,q-n)
    B=(P-Mi)/2; C=(P+Mi)/2-A      # M(q+t n)=A+tB+t^2C
    out=[]
    for L in range(1,Lmax+1):
        big=np.zeros((40*L,40*L),dtype=complex)
        for i in range(L):
            big[40*i:40*i+40,40*i:40*i+40]=A
            if i+1<L: big[40*i:40*i+40,40*(i+1):40*(i+1)+40]=B
            if i+2<L: big[40*i:40*i+40,40*(i+2):40*(i+2)+40]=C
        out.append(40*L-rank(big,1e-7)-10*L)
    return out   # cumulative sum_i min(m_i,L)
n=np.array([1.,.3,-.2,.5])
print('flat',partial(*flat(),nullq(0),n))
for j in (-2,-1,0,1,2): print('null g2 shift',j,partial(*null_rotation_g2(),nullq(j),n))
q=nullq(0); q[2]=0; q[0]=np.linalg.norm(q[[1,3]])
print('heis q2=0',partial(*heisenberg(),q,np.array([1.,.3,0,.5])))
print('heis q2=0, q along E_1 only',partial(*heisenberg(),np.array([1.,1,0,0]),np.array([1.,.3,0,.5])))
print('null g1 q0=q3',partial(*null_rotation_g1(),np.array([1.3,0,0,1.3]),np.array([1.,0,0,.4])))
print('null g1 q0=-q3',partial(*null_rotation_g1(),np.array([1.3,0,0,-1.3]),np.array([1.,0,0,.4])))
