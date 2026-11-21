#!/usr/bin/env python3
"""054-055 r3: build the r3 inserts from the r2 inserts by the r3 replacements, and check anchors.

Run (from the repository root):
    python -I proposals/local-gpu/054-055-r2/build_r3.py [--apply-to DIR]

Reads (read-only): the r2 files E1-E4 *.r2.tex in this folder and chapters/appH-microscopic-proofs.tex.
Writes only into this folder: E1_053_sentence.r3.tex (the full replacement of anchor A1),
E2_insert_054_055.r3.tex, E3_056_adjusted.r3.tex, E4_057_adjusted.r3.tex (all CRLF).
With --apply-to DIR (outside the repository) it writes DIR/appH-microscopic-proofs.tex with E1-E4 applied.
Every replacement asserts that its old string occurs exactly once."""
import hashlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
CUR = os.path.join(ROOT, 'chapters', 'appH-microscopic-proofs.tex')

def sha(b):
    return hashlib.sha256(b).hexdigest()

def rd(name):
    return open(os.path.join(HERE, name), 'rb').read().decode('utf-8').replace('\r\n', '\n').rstrip('\n')

def sub1(text, old, new, tag):
    n = text.count(old)
    assert n == 1, '%s: old string occurs %d times' % (tag, n)
    print('  applied %s' % tag)
    return text.replace(old, new)

STATUS = 'Problem~E remains open and PROGRAMME-CONDITIONAL.'
E1s, E2, E3, E4 = (rd('E1_053_sentence.r2.tex'), rd('E2_insert_054_055.r2.tex'),
                   rd('E3_056_adjusted.r2.tex'), rd('E4_057_adjusted.r2.tex'))

# ---------------- E1 (review (d)) ----------------
A1_OLD = ('so that the domination above fails for them. It does not exclude a real-time reading '
          'obtained by continuation.')
A1_NEW = ('so that the domination above fails for them. ' + E1s +
          ' The result above does not exclude a real-time reading obtained by continuation.')

# ---------------- E2 (review (a), (b), (f); option (i) conversion) ----------------
print('E2:')
E2 = sub1(E2,
    r'For \(r^0\ne0\) the one-dimensional branch integral \(\int_{\mathbb R}\mathrm e^{-Qa^2}\,2\cos(\gamma_{\mathrm c}|a|)\,\mathrm da=2\sqrt{\pi/Q}\,\mathrm e^{-\gamma_{\mathrm c}^2/(4Q)}\), \(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i/8}r^0/2\) frozen at its value on the Hermitian contour, gives in that frozen-coefficient model (with \(g_{\mathrm{YM}}=1\)) pointwise modulus growth \(\mathrm e^{{(r^0)}^2\cos(3\pi u/4-\pi/4)/(16\epsilon)}\) for the soft temporal mode at \(\gamma=0\), saturating as \(\epsilon\to0^+\) at fixed \(\gamma<0\) to a constant of order \(\mathrm e^{{(r^0)}^2\sin(3\pi u/4-\pi/4)/(8|\gamma|)}\),',
    r'For \(r^0\ne0\) write the soft temporal mode as \(\tilde A_0=a\sigma^3/2\), on which the regulator and the mass give \(\mathrm e^{-Qa^2}\) with \(Q=\tfrac12\mathrm e^{-3\pi\mathrm iu/4}(\epsilon-\mathrm i\gamma/(2g_{\mathrm{YM}}^2))\). The one-dimensional branch integral \(\int_{\mathbb R}\mathrm e^{-Qa^2}\,2\cos(\gamma_{\mathrm c}|a|)\,\mathrm da=2\sqrt{\pi/Q}\,\mathrm e^{-\gamma_{\mathrm c}^2/(4Q)}\), with \(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i/8}r^0/2\) frozen at its value on the Hermitian contour, gives in that frozen-coefficient model pointwise modulus growth \(\mathrm e^{{(r^0)}^2\cos(3\pi u/4-\pi/4)/(8\epsilon)}\) for the soft temporal mode at \(\gamma=0\), saturating as \(\epsilon\to0^+\) at fixed \(\gamma<0\) to a constant of order \(\mathrm e^{g_{\mathrm{YM}}^2{(r^0)}^2\sin(3\pi u/4-\pi/4)/(4|\gamma|)}\),',
    '(a) Q defined, frozen exponents in Definition (A)')
E2 = sub1(E2,
    r'with this contour-dependent coefficient in \(\gamma_{\mathrm c}\) the soft-mode growth exponent at \(\gamma=0\) is \({(r^0)}^2/(16\sqrt2\,\epsilon)\) and the fixed-\(\gamma\) saturation exponent is \(-g_{\mathrm{YM}}^2{(r^0)}^2/(8\sqrt2|\gamma|)\)',
    r'with \(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i(1-u)/8}r^0/2\) the soft-mode growth exponent at \(\gamma=0\) is \({(r^0)}^2/(8\sqrt2\,\epsilon)\) and the fixed-\(\gamma\) saturation exponent is \(-g_{\mathrm{YM}}^2{(r^0)}^2/(4\sqrt2|\gamma|)\)',
    '(b) contour exponents in Definition (A)')
E2 = sub1(E2,
    r'grows without bound as \(\epsilon\to0\) (numerical, for a large-radius \(\cosh\) proxy of \(|O_k|\) in a reduced chart, on the sampled range \(\epsilon\in[0.01,1]\); the rank-one corner estimate of the paragraph on the slice bridge band, applied along a ray with \(b_u(\hat\rho;k)\ne0\), gives growth at least like \(\mathrm e^{c/\epsilon}\) up to polynomial factors)',
    r'grows without bound as \(\epsilon\to0\): the rank-one corner estimate of the paragraph on the slice bridge band, applied along a ray with \(b_u(\hat\rho;k)\ne0\), gives growth at least like \(\mathrm e^{c/\epsilon}\) up to polynomial factors (a large-radius \(\cosh\) proxy of \(|O_k|\) in a reduced chart increases on the sampled range \(\epsilon\in[0.02,2]\) of Definition~(A) with \(g_{\mathrm{YM}}^2=1/2\), numerical)',
    '(f) derived clause first, proxy range converted (option (i))')
E2 = sub1(E2,
    r'In the reduced \(N=2\) integral (regulator (A), contours \(\mathcal R_u\), \(\epsilon\to0^+\) last) with the factorized surrogate',
    r'In the reduced \(N=2\) integral (Definition~(A) with \(g_{\mathrm{YM}}^2=1/2\), the normalisation of every value of \(\epsilon\) and \(\gamma\) below, contours \(\mathcal R_u\), \(\epsilon\to0^+\) last) with the factorized surrogate',
    '(i) normalisation of the reduced model stated')
E2 = sub1(E2, r'evaluated at \(u=0\) for \(\epsilon\ge0.1\) only', r'evaluated at \(u=0\) for \(\epsilon\ge0.2\) only',
          '(i) exact-insertion threshold 0.1 -> 0.2')
E2 = sub1(E2, r'along the ladder down to \(\epsilon=3\cdot10^{-3}\)', r'along the ladder down to \(\epsilon=6\cdot10^{-3}\)',
          '(i) ladder end 3e-3 -> 6e-3')
E2 = sub1(E2, r'against the pointwise corner value \(0.044/\epsilon\) at \(r^0=1\))',
          r'against the corner value \({(r^0)}^2/(8\sqrt2\,\epsilon)\approx0.088/\epsilon\) at \(r^0=1\) of the one-dimensional branch model)',
          '(i) corner value 0.044 -> 0.088, identified')

# ---------------- E3 (review (e)) ----------------
print('E3:')
E3 = sub1(E3, r'so the \(k<14\) Pfaffian window applies with the \(k=0\) majorant',
          r'so the bound along the flat directions applies with polynomial degree \(0\)', '(e1) degree wording')
E3 = sub1(E3, r'by dominated convergence within the window', r'by dominated convergence under that bound', '(e2) window wording')

# ---------------- E4 (review (g)) ----------------
print('E4:')
E4 = sub1(E4, r'with \(\beta(\epsilon,\gamma)\ge|\gamma|\sin(3\pi u/4)/(2g_{\mathrm{YM}}^2)\), and the ray region contributes at least',
          r'with \(\beta(\epsilon,\gamma)\to|\gamma|\sin(3\pi u/4)/(2g_{\mathrm{YM}}^2)\) as \(\epsilon\to0^+\), and in that limit the ray region contributes at least',
          '(g) beta limit')

# ---------------- checks on the inserted text ----------------
block = E2 + '\n\n' + E3 + '\n\n' + E4
for bad in ('the researcher', 'proposal', 'as proposed', 'now ray-free', 'Cauchy-Binet', 'k^\\mu k^\\nu\\mathcal G',
            '16\\sqrt2', '8\\sqrt2|\\gamma|', '/(16\\epsilon)', '0.044/', 'k<14', 'within the window',
            '\\epsilon\\in[0.01,1]', '3\\cdot10^{-3}', '\\beta(\\epsilon,\\gamma)\\ge'):
    assert bad not in block and bad not in A1_NEW, 'forbidden or stale string: ' + bad
assert 'g_{\mathrm{YM}}=1' not in E2
print('status closers in 054-057 block: %d (expected 1, at the end of 057)' % block.count(STATUS))
assert block.count(STATUS) == 1 and block.rstrip().endswith(STATUS)
print('\\ref uses: %s' % sorted(set(x.split('}')[0] for x in (block + A1_NEW).split('\\ref{')[1:])))
print('\\cite uses: %s' % sorted(set(x.split('}')[0] for x in block.split('\\cite{')[1:])))
assert '\\label' not in block
print('non-ASCII characters: %d' % sum(ord(c) > 127 for c in block + A1_NEW))

def crlf(s):
    return (s.replace('\r\n', '\n').rstrip('\n') + '\n').replace('\n', '\r\n').encode('utf-8')

out = {'E1_053_sentence.r3.tex': A1_NEW, 'E2_insert_054_055.r3.tex': E2,
       'E3_056_adjusted.r3.tex': E3, 'E4_057_adjusted.r3.tex': E4}
for name, s in out.items():
    b = crlf(s)
    open(os.path.join(HERE, name), 'wb').write(b)
    print('%-26s %6d B  CRLF %3d  bare-LF %d  sha256 %s' % (name, len(b), b.count(b'\r\n'),
          b.count(b'\n') - b.count(b'\r\n'), sha(b)[:16]))

# ---------------- anchors in the current tree ----------------
cur = open(CUR, 'rb').read()
print('current appH: %d B  CRLF %d  bare-LF %d  sha256 %s' % (len(cur), cur.count(b'\r\n'),
      cur.count(b'\n') - cur.count(b'\r\n'), sha(cur)[:16]))
A1 = A1_OLD.encode()
A2 = b'Problem~E stays open with Assumption~\\ref{ass:lorentzian} retained.\r\n\r\n\\paragraph{Status.}\r\nRemains Assumption~\\ref{ass:lorentzian}.\r\n'
print('anchor A1 (053 closer, E1) count: %d' % cur.count(A1))
print('anchor A2 (end of Problem E ledger before Status, E2-E4) count: %d' % cur.count(A2))
assert cur.count(A1) == 1 and cur.count(A2) == 1
assert b'Exponential observables' not in cur and b'Slice bridge band' not in cur, 'inserts already present'

if '--apply-to' in sys.argv:
    d = sys.argv[sys.argv.index('--apply-to') + 1]
    assert not os.path.abspath(d).lower().startswith(ROOT.lower()), 'apply target must be outside the repository'
    new = cur.replace(A1, A1_NEW.encode())
    head = b'Problem~E stays open with Assumption~\\ref{ass:lorentzian} retained.\r\n\r\n'
    tail = b'\\paragraph{Status.}\r\nRemains Assumption~\\ref{ass:lorentzian}.\r\n'
    ins = crlf(E2) + b'\r\n' + crlf(E3) + b'\r\n' + crlf(E4) + b'\r\n'
    new = new.replace(A2, head + ins + tail)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'appH-microscopic-proofs.tex'), 'wb').write(new)
    print('applied copy: %d B  CRLF %d  bare-LF %d  sha256 %s' % (len(new), new.count(b'\r\n'),
          new.count(b'\n') - new.count(b'\r\n'), sha(new)[:16]))
print('BUILD_R3 OK')
