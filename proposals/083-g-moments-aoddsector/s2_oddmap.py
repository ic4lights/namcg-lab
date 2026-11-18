# s2_oddmap.py (083) Exact averaged map. Hypothesis class: a independent of r;
# h_n = h_n(s^2 g) complete homogeneous symmetric polynomial (h_0=1); A_n = E[a^n].
# Map: <Tr Q^m> = (-1)^m 2^(m+1) sum_k C(m,2k) sum_{j=0}^k C(k,j) A_{m-2k+2j} (k-j)! h_{k-j}.
# Run: python -I proposals/083-g-moments-aoddsector/s2_oddmap.py   (from repo root)
import sympy as sp
from sympy import factorial, binomial, expand, sqrt, pi, exp, oo, Function, Symbol
from itertools import product
from s1 import trQ_sym  # placeholder guard, replaced below
EOF_MARKER_UNUSED = 0
