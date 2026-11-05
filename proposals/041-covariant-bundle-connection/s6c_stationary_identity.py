"""s6c: stationary-set identity from the J = dJ = 0 samples of s6b (pickle): singular-value analysis of the 6 columns
[R, V2, box, th2, vth, t2V2]  ->  one-dimensional null space  <=>  |U|^2 = th2 - 2 vth + t2V2 is a combination of R, V2, box on the stationary set.
Also the exact fit of a_1 (V and M) with the null direction removed."""
import pickle
import numpy as np
d = pickle.load(open('s6b_samples.pkl', 'rb'))
names = ['R', 'V2', 'box', 'th2', 'vth', 't2V2']
for etad, (rows, yV, yM) in d.items():
    sv = np.linalg.svd(rows, compute_uv=False)
    print(f'eta={etad}: {len(yV)} samples; singular values of the invariant matrix: ' + ' '.join(f'{x:.3e}' for x in sv))
    u, s, vt = np.linalg.svd(rows)
    n = vt[-1]; n = n/n[np.argmax(np.abs(n))] 
    # normalise so that the t2V2 coefficient is 1
    n = vt[-1]/vt[-1][5]
    print('   null vector (t2V2 coefficient = 1): ' + ', '.join(f'{nm}={c:+.6f}' for nm, c in zip(names, n)))
    # relation  th2 - 2 vth + t2V2 = |U|^2 ;  check  s|U|^2 = -R/2 + V2 - 3/2 box
    sgn = 1.0 if etad[0] > 0 else -1.0
    U2 = rows[:, 3] - 2*rows[:, 4] + rows[:, 5]
    rhs = -rows[:, 0]/2 + rows[:, 1] - 1.5*rows[:, 2]
    print(f'   max | s|U|^2 - (-R/2 + V2 - 3/2 box) | = {np.max(np.abs(sgn*U2 - rhs)):.2e}   (max |rhs| = {np.max(np.abs(rhs)):.2f})')
    # a1 prediction from covariant formula
    pred = -rows[:, 0]/3 + rows[:, 2] - rows[:, 1] + 6*sgn*U2
    print(f'   max | a1(V) - [-R/3 + box - V2 + 6 s|U|^2] | = {np.max(np.abs(yV - pred)):.2e};  max|a1(M) - same| = {np.max(np.abs(yM - pred)):.2e}')
    pred2 = -10*rows[:, 0]/3 + 5*rows[:, 1] - 8*rows[:, 2]
    print(f'   max | a1(V) - [-10R/3 + 5 V2 - 8 box] | = {np.max(np.abs(yV - pred2)):.2e}')
