"""S6 (numerical check of the by-hand statements on the roots
   q0 = -i gamma +- ((p + i gamma)^2 + kappa p l)^(1/2),  gamma = c chi / 2,  c in {-1, 1, 3}).
 - no root is real for p > 0 when chi != 0 (min |Im q0| on a grid in p > 0, levels l = -1 .. 9);
 - l >= 1: max |Im q0| < |c chi|, approaching |c chi| for large p;
 - l = -1: max |Im q0| = |gamma| + sigma, sigma = kappa/4 + (kappa^2/16 + gamma^2)^(1/2), at p = sigma;
 - the overall largest |Im q0| is 3|chi|/2 + sigma_3, and both signs of Im q0 occur.
Run: python -I -B s6_growth.py"""
import numpy as np

ps = np.concatenate([np.linspace(1e-4, 5, 200001), np.linspace(5, 400, 40001)])
for kap, chi in [(1.0, 0.5), (1.0, -0.5), (1.3, 0.8), (2.0, -0.25)]:
    allmax = 0.0; signs = set(); minim = np.inf
    for c in (-1, 1, 3):
        g = c * chi / 2
        sig = kap / 4 + np.sqrt(kap ** 2 / 16 + g ** 2)
        line = []
        for l in (-1, 1, 3, 9):
            s = np.sqrt((ps + 1j * g) ** 2 + kap * ps * l)
            im = np.stack([(-1j * g + s).imag, (-1j * g - s).imag])
            a = np.abs(im).max(axis=0)
            minim = min(minim, np.abs(im).min())
            signs |= set(np.sign(im[np.abs(im) > 1e-9]).astype(int).tolist())
            allmax = max(allmax, a.max())
            if l == -1:
                line.append('l=-1: max %.6f at p=%.4f (closed form %.6f at p=%.4f)' % (a.max(), ps[a.argmax()], abs(g) + sig, sig))
            else:
                line.append('l=%d: max %.6f (< |c chi| = %.6f: %s)' % (l, a.max(), abs(c * chi), a.max() < abs(c * chi)))
        print('kappa=%.2f chi=%+.2f c=%+d: ' % (kap, chi, c) + '; '.join(line))
    s3 = kap / 4 + np.sqrt(kap ** 2 / 16 + 9 * chi ** 2 / 4)
    print('   overall max |Im q0| %.6f, closed form 3|chi|/2 + sigma_3 = %.6f ; min |Im q0| over the grid %.2e ; signs of Im q0 %s'
          % (allmax, 1.5 * abs(chi) + s3, minim, sorted(signs)))
