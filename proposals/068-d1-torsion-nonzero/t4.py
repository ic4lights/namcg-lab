import numpy as np
from core import *
rng=np.random.default_rng(5)
k=np.array([-1.,0,0,1.])   # k^a ; lower k_a=(1,0,0,1)
klow=ETA@k
def nullq(shift):
    # random q with (q + shift*klow)^2 = 0 : q = n - shift*klow, n null
    v=rng.normal(size=3); n=np.array([np.linalg.norm(v),*v])
    return n-shift*klow
print('flat: dim ker at null q minus 10 =',40-rank(M_of_q(*flat(),nullq(0)))-10)
c,w=null_rotation_g2()
for j in (-2,-1,0,1,2):
    q=nullq(j); M=M_of_q(c,w,q)
    print('null g2, (q%+dk)^2=0: extra kernel'%j,40-rank(M)-10)
# chain test: is there v1 with M v1 + dM/dt v0 = 0 ?  count Jordan heads: solve [M, dM; 0, M]
def chain(c,w,q,n,eps=1e-6):
    M=M_of_q(c,w,q); dM=(M_of_q(c,w,q+eps*n)-M_of_q(c,w,q-eps*n))/(2*eps)
    big=np.block([[M,dM],[np.zeros_like(M),M]])
    # kernel of big = {(v1,v0): M v0=0, M v1 + dM v0=0}; gauge: v0 gauge(q), v1 = d gauge
    return 80-rank(big,1e-6)
n=rng.normal(size=4)
print('flat: dim of length-<=2 chain space',chain(*flat(),nullq(0),n),'(gauge contributes 20; heads+solutions extra)')
for j in (-2,-1,0,1,2):
    print('null g2 shift',j,chain(c,w,nullq(j),n))
c,w=heisenberg()
q=nullq(0); q[2]=0; q[0]=np.linalg.norm(q[[1,3]])
print('heis q2=0 null: extra kernel',40-rank(M_of_q(c,w,q))-10,'chain',chain(c,w,q,np.array([1.,.3,0,.2])))
c,w=null_rotation_g1()
for (q0,q3,lab) in [(1.3,1.3,'q0=q3'),(1.3,-1.3,'q0=-q3'),(1.3,-1.3-2,'a'),(1.3,-1.3+2,'b'),(1.3,-1.3-1,'c'),(1.3,-1.3+1,'d')]:
    q=np.array([q0,0,0,q3]); print('null g1',lab,'extra kernel',40-rank(M_of_q(c,w,q))-10)
