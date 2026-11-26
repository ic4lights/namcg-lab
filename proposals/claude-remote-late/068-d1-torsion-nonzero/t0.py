import numpy as np
from core import *
rng=np.random.default_rng(1)
for name,bg in [('flat',flat()),('null g1',null_rotation_g1()),('null g2',null_rotation_g2()),('heis',heisenberg()),('second',second_algebra())]:
    c,w=bg
    r1,r2,T,R=background_residual(c,w)
    dirs=[m for m in range(4) if np.abs(c[:,:,m]).max()==0]
    q=np.zeros(4); 
    for m in dirs: q[m]=rng.normal()
    M=M_of_q(c,w,q); G=gauge_vectors(c,w,chars(q))
    print(name,'res',r1,r2,'dirs',dirs,'rank M',rank(M),'gauge rank',rank(G),'|M G|',np.abs(M@G).max())
# Heisenberg oscillator
c,w=heisenberg(); N=12
E=heisenberg_modes(0.7,0.3,N)
comm=E[3]@E[1]-E[1]@E[3]-E[2]
print('rep defect below top level',np.abs(comm[:N-1,:N-1]).max())
M=M_op(c,w,E); G=gauge_vectors(c,w,E)
# keep columns of G with gauge-parameter level <= N-4, rows of M*G everywhere
MG=M@G
lev=np.repeat(np.arange(N),10)
print('|M G| on low levels',np.abs(MG[:,lev<=N-5]).max(),' all',np.abs(MG).max())
