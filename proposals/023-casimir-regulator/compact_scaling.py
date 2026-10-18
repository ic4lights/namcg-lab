"""023 script 11: scaling of the negative-mode count of the compact four-matrix gauge-fixed operator inside the window a<=A."""
import numpy as np
from compact_exact import formula_spectrum
prev=None
for A in [8,16,32,48]:
    fs=formula_spectrum(A); tot=sum(w for _,w,_,_ in fs); neg=sum(w for l,w,_,_ in fs if l<-1e-9)
    s="A=%d total=%d negative=%d frac=%.3e"%(A,tot,neg,neg/tot)
    if prev: s+="  local exponents: neg ~ A^%.2f, total ~ A^%.2f"%(np.log(neg/prev[1])/np.log(A/prev[0]),np.log(tot/prev[2])/np.log(A/prev[0]))
    print(s); prev=(A,neg,tot)
