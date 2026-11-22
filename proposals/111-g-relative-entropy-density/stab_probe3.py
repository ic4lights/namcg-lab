import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as cm
def raw(G):
    n=G.shape[0]//2; O=cm.omega(n)
    wG,U=np.linalg.eigh(0.5*(G+G.T))
    sq=U@np.diag(np.sqrt(wG))@U.T; isq=U@np.diag(1/np.sqrt(wG))@U.T
    Kh=-1j*(sq@O@sq); hw,HV=np.linalg.eigh(Kh)
    Kf=HV@np.diag(np.sign(hw)*cm.hvec(np.abs(hw)))@HV.conj().T
    return -1j*((isq@Kf@sq)@O)
for mu in [0.05,0.1,0.2,0.3]:
    row=[]
    for N in [8,12,16,20]:
        L=2*N+15; sites=np.arange(6,6+N)
        C,Pi=cm.restrict(L,mu,sites); G0=cm.G_block(C,Pi)
        A=raw(G0)
        r=np.max(np.abs(A.imag))/(1+np.max(np.abs(A.real)))
        row.append("N=%d r=%.1e" % (N,r))
    print("mu=%.2f "%mu + " ".join(row))
