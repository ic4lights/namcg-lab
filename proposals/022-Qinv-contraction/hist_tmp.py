import sys
from quantum_compact_hessian import *
from collections import Counter
for N in [1,2,3]:
    for nm,pp in [("P4c",[(a,4) for a in range(4)]),("P5c",[(A,5) for A in range(5)])]:
        r=run(nm,pp,N)
        c=Counter(np.round(r['ev'],4))
        print(nm,N,sorted(c.items()))
