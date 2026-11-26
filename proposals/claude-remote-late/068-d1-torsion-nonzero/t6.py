import numpy as np, scipy.linalg as sl
from core import *
from t1 import common
c,w=second_algebra()
for q0,n in [(np.array([0.545,-0.183,0,0]),np.array([2.5,0.541,0,0])),(np.array([0.2,0.7,0,0]),np.array([1.,0.,0,0]))]:
    cr=common(c,w,q0,n)
    for t in sorted(set(np.round(cr,5)),key=lambda z:(z.real,z.imag)):
        q=q0+t*n; q2=-q[0]**2+q[1]**2
        print('t',t,'mult',int((np.abs(cr-t)<1e-4).sum()),'q^2',np.round(q2,5),'q0',np.round(q[0],5),'q1',np.round(q[1],5),' q^2/(i q0)',np.round(q2/(1j*q[0]),5) if abs(q[0])>1e-9 else None)
from t5 import partial
