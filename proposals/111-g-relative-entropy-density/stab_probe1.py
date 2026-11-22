import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as cm
np.set_printoptions(precision=3, suppress=True)
def rawA(G):
    n = G.shape[0]//2; O = cm.omega(n)
    wG,U = np.linalg.eigh(0.5*(G+G.T))
    sq = U@np.diag(np.sqrt(wG))@U.T; isq = U@np.diag(1/np.sqrt(wG))@U.T
    Kh = -1j*(sq@O@sq); hw,HV = np.linalg.eigh(Kh)
    Kf = HV@np.diag(np.sign(hw)*cm.hvec(np.abs(hw)))@HV.conj().T
    return -1j*((isq@Kf@sq)@O)
for (L,mu,N) in [(31,0.05,8),(41,0.01,12),(41,0.01,6),(41,0.01,10)]:
    sites = np.arange(6,6+N)
    C,Pi = cm.restrict(L,mu,sites); G0 = cm.G_block(C,Pi)
    A = rawA(G0)
    mi = np.max(np.abs(A.imag)); mr = np.max(np.abs(A.real))
    print("L=%d mu=%.2f N=%d maxIm=%.3e maxRe=%.3e ratio=%.3e" % (L,mu,N,mi,mr,mi/(1+mr)))
