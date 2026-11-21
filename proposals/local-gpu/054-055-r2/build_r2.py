#!/usr/bin/env python3
"""054-055 r2: build the corrected inserts from the gpu-integrated text and check anchors.

Run (from the repository root):
    python -I proposals/local-gpu/054-055-r2/build_r2.py [--apply-to DIR]

Reads (read-only):
  scratch/integrator-backup/gpu-import-full/chapters/appH-microscopic-proofs.tex  (gpu text of 053-057)
  chapters/appH-microscopic-proofs.tex                                          (current tree)
If the scratch backup is missing, the frozen copy gpu_source_053_057.txt in this folder is used.
Writes only into this folder:
  gpu_source_053_057.txt        the five gpu source lines (053 closer, 054, 055, 056, 057), LF
  E1_053_sentence.r2.tex        the sentence added to the 053 closing paragraph (CRLF)
  E2_insert_054_055.r2.tex      the corrected 054+055 paragraph (CRLF)
  E3_056_adjusted.r2.tex        056 text with its closer adjusted (CRLF; for integration with 056)
  E4_057_adjusted.r2.tex        057 text with its last two sentences adjusted (CRLF; idem)
With --apply-to DIR (DIR outside the repository) it writes DIR/appH-microscopic-proofs.tex with
E1 + E2 + E3 + E4 applied, for a build check.
Every replacement asserts that its old string occurs exactly once."""
import hashlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
GPU = os.path.join(ROOT, 'scratch', 'integrator-backup', 'gpu-import-full', 'chapters', 'appH-microscopic-proofs.tex')
CUR = os.path.join(ROOT, 'chapters', 'appH-microscopic-proofs.tex')
SRC = os.path.join(HERE, 'gpu_source_053_057.txt')

def sha(b):
    return hashlib.sha256(b).hexdigest()

def sub1(text, old, new, tag):
    n = text.count(old)
    assert n == 1, '%s: old string occurs %d times' % (tag, n)
    return text.replace(old, new)

# ---------------- gpu source paragraphs ----------------
if os.path.exists(GPU):
    L = open(GPU, 'rb').read().decode('utf-8').replace('\r\n', '\n').split('\n')
    src = {'053': L[1607], '054': L[1609], '055': L[1611], '056': L[1613], '057': L[1616]}
    assert src['054'].startswith('\\emph{Exponential observables')
    assert src['055'].startswith('\\emph{The slice at \\(k\\ne0\\)')
    assert src['056'].startswith('\\paragraph{Slice bridge band')
    assert src['057'].startswith('\\paragraph{The \\(\\gamma\\to0^{-}\\) link')
    open(SRC, 'wb').write(('\n'.join(src[k] for k in ('053', '054', '055', '056', '057')) + '\n').encode('utf-8'))
else:
    parts = open(SRC, 'rb').read().decode('utf-8').split('\n')
    src = dict(zip(('053', '054', '055', '056', '057'), parts[:5]))
print('gpu source lines: ' + ', '.join('%s %d B' % (k, len(src[k].encode())) for k in sorted(src)))

STATUS = 'Problem~E remains open and PROGRAMME-CONDITIONAL.'

# ---------------- E1: sentence for the 053 closing paragraph ----------------
E1_OLD_053 = ('so that the domination above fails for them. It does not exclude a real-time reading '
              'obtained by continuation.')
E1_SENT = ('The paragraph on exponential observables at \\(N=2\\) below sharpens this at \\(N=2\\), \\(\\gamma=0\\), '
           'regulator (A) and the contours \\(\\mathcal R_u\\): the right-hand side diverges in modulus for every '
           'nonzero real \\(k\\) and every \\(k\\) off one slice, the identity is unresolved on that slice at '
           '\\(k\\ne0\\), and the failure is absent at fixed \\(\\gamma<0\\).')
E1_NEW_053 = ('so that the domination above fails for them. ' + E1_SENT +
              ' It does not exclude a real-time reading obtained by continuation.')

# ---------------- E2: 054 ----------------
t = src['054']
t = sub1(t, '\\emph{Exponential observables \\(\\operatorname{Tr}\\mathrm e^{\\mathrm ik^\\mu A_\\mu}\\) at \\(N=2\\).} ',
         '\\paragraph{Exponential observables \\(\\operatorname{Tr}\\mathrm e^{\\mathrm ik^\\mu A_\\mu}\\) at \\(N=2\\) '
         '(bounded obstruction, partly numerical).}\n'
         'Keep Definition~(A), the contours \\(\\mathcal R_u\\) and the displayed limit identity of the paragraph on '
         'the regulated Lorentzian integral at finite \\(N\\). ', 'E2.0 heading')
t = sub1(t, '\\(\\rho_X^2=k^\\mu k^\\nu\\mathcal G_{\\mu\\nu}\\)',
         '\\(\\rho_X^2=\\sum_{a=1}^{3}(k^\\mu A^a_\\mu)^2\\)', 'E2.5 rho_X')
t = sub1(t, 'where \\(|O_k|\\le2\\) and that side converges by the \\(k<14\\) Pfaffian window.',
         'where \\(|O_k|\\le2\\) and that side converges by the bound along the flat directions with polynomial '
         'degree \\(0\\).', 'E2.6 window')
t = sub1(t, ', numerically like \\(\\mathrm e^{c(k,u)/\\sqrt\\epsilon}\\) on the sampled range.',
         ' (numerical, for a large-radius \\(\\cosh\\) proxy of \\(|O_k|\\) in a reduced chart, on the sampled range '
         '\\(\\epsilon\\in[0.01,1]\\); the rank-one corner estimate of the paragraph on the slice bridge band, applied '
         'along a ray with \\(b_u(\\hat\\rho;k)\\ne0\\), gives growth at least like \\(\\mathrm e^{c/\\epsilon}\\) up to '
         'polynomial factors).', 'E2.3 numerics')
t = sub1(t, 'there is no analyticity strip and no non-polynomial extension of the limit statement at \\(\\gamma=0\\) '
            'off that slice, within the hypothesis class',
         'the displayed identity has no analyticity strip in \\(k\\) and no non-polynomial extension at '
         '\\(\\gamma=0\\) off that slice, within the hypothesis class', 'E2.1a strip')
t = sub1(t, 'contours \\(\\mathcal R_u\\), \\(\\epsilon\\to0^+\\) last. The obstruction',
         'contours \\(\\mathcal R_u\\), \\(\\epsilon\\to0^+\\) last. This concerns the right-hand side of the displayed '
         'identity and the modulus route, not the existence of the limit: by (v) of the paragraph on linear contours '
         'that mix the indices, at \\(N=2\\) the limit of \\(\\langle O_k\\rangle_\\epsilon\\) exists and equals '
         '\\(F_{\\mathrm E}(\\mathrm e^{\\mathrm i\\pi/4}k^\\mu k_\\mu)\\) for every real spacelike \\(k\\) and for every '
         '\\(k\\) with \\(\\Lambda^{\\mathrm T}k\\) real on \\(\\mathcal R_{u\'}\\), \\(0<u\'<2/3\\), although for some of '
         'these \\(k\\) the commuting-ray contribution grows. The obstruction', 'E2.1b limit sentence')
t = sub1(t, 'extends to \\(O_k\\) for every \\(k\\in\\mathbb C^{10}\\) (numerical).',
         'extends to \\(O_k\\) for every \\(k\\in\\mathbb C^{10}\\) (derived in the paragraph on the '
         '\\(\\gamma\\to0^-\\) link below).', 'E2.4 derived')
t = sub1(t, ' Assumption~\\ref{ass:lorentzian} is not discharged. ' + STATUS,
         ' Assumption~\\ref{ass:lorentzian} is not discharged.', 'E2.7 054 closer')
e054 = t

# ---------------- E2: 055 ----------------
t = src['055']
t = sub1(t, 'the Cauchy-Binet identity \\(\\rho_X^2=\\sum_{a=1}^{3}{(k^\\mu A^a_\\mu)}^2\\) is exact at \\(N=2\\)',
         'the identity \\(\\rho_X^2=\\sum_{a=1}^{3}{(k^\\mu A^a_\\mu)}^2=-4\\det(k^\\mu A_\\mu)\\) is exact at \\(N=2\\)',
         'E2.8 identity name')
t = sub1(t, '\\(\\gamma_{\\mathrm c}=\\mathrm e^{3\\pi\\mathrm i/8}r^0/2\\), gives pointwise modulus growth',
         '\\(\\gamma_{\\mathrm c}=\\mathrm e^{3\\pi\\mathrm i/8}r^0/2\\) frozen at its value on the Hermitian contour, '
         'gives in that frozen-coefficient model (with \\(g_{\\mathrm{YM}}=1\\)) pointwise modulus growth',
         'E2.9 frozen label')
t = sub1(t, 'which diverges as \\(\\gamma\\to0^-\\) when \\(3\\pi u/4-\\pi/4>0\\) and decays when it is negative. ',
         'which diverges as \\(\\gamma\\to0^-\\) when \\(3\\pi u/4-\\pi/4>0\\) and decays when it is negative. '
         'In the one-dimensional branch model the coefficient of \\(\\tilde A_0\\) in \\(k^\\mu A_\\mu\\) on '
         '\\(\\mathcal R_u\\) at pure temporal slice momentum is \\(\\mathrm e^{3\\pi\\mathrm i(1-u)/8}r^0\\), not its '
         'value at \\(u=0\\); with this contour-dependent coefficient in \\(\\gamma_{\\mathrm c}\\) the soft-mode growth '
         'exponent at \\(\\gamma=0\\) is \\({(r^0)}^2/(16\\sqrt2\\,\\epsilon)\\) and the fixed-\\(\\gamma\\) saturation '
         'exponent is \\(-g_{\\mathrm{YM}}^2{(r^0)}^2/(8\\sqrt2|\\gamma|)\\), both independent of \\(u\\), so the '
         'saturation factor above and its growth as \\(\\gamma\\to0^-\\) for \\(3\\pi u/4-\\pi/4>0\\) are properties of '
         'the frozen-coefficient model, not of the contour family; with the contour-dependent coefficient the '
         'exponential factor of the signed one-dimensional integral tends at fixed \\(\\gamma<0\\) to a constant below '
         'one for every \\(u\\in(0,2/3)\\). ',
         'E2.10 correction from 057')
t = sub1(t, 'In the reduced \\(N=2\\) integral (regulator (A), contours \\(\\mathcal R_u\\), \\(\\epsilon\\to0^+\\) last) '
            'with this insertion at pure temporal slice momenta,',
         'In the reduced \\(N=2\\) integral (regulator (A), contours \\(\\mathcal R_u\\), \\(\\epsilon\\to0^+\\) last) '
         'with the factorized surrogate of this insertion along the soft temporal mode, coefficient frozen as above '
         '(it coincides with the contour-dependent one at \\(u=0\\)), at pure temporal slice momenta (the exact '
         'insertion, evaluated at \\(u=0\\) for \\(\\epsilon\\ge0.1\\) only, gives ratios between \\(2.0\\) and '
         '\\(4.1\\)),', 'E2.11 surrogate label')
t = sub1(t, 'nor the pointwise saturation factor materialises',
         'nor the pointwise saturation factor of the frozen-coefficient model materialises', 'E2.12 saturation label')
t = sub1(t, 'and the pure-spatial half of the slice is now ray-free; ' + STATUS,
         'and the pure-spatial half of the slice has no commuting ray with growth.', 'E2.13 ray-free + closer')
e055 = t

E2 = e054 + '\n\n' + e055

# ---------------- E3 / E4: closers of 056 and 057 ----------------
e056 = sub1(src['056'], ' or an independent mechanism. ' + STATUS, ' or an independent mechanism.', 'E3 056 closer')
OLD057 = src['057'][src['057'].index('In the one-dimensional branch model'):]
assert OLD057.endswith('not of the contour family. ' + STATUS)
NEW057 = ('The statements of this paragraph and of the two preceding ones hold in the hypothesis classes stated '
          'there, at \\(N=2\\) with \\(\\epsilon\\to0^+\\) taken last, and derive no signature, real-time response, '
          'background or continuation; Assumption~\\ref{ass:lorentzian} is not discharged, and ' + STATUS)
e057 = sub1(src['057'], OLD057, NEW057, 'E4 057 tail')

# ---------------- checks on the inserted text ----------------
block = E2 + '\n\n' + e056 + '\n\n' + e057
for bad in ('the researcher', 'proposal', 'as proposed', 'now ray-free', 'Cauchy-Binet', 'k^\\mu k^\\nu\\mathcal G'):
    assert bad not in block and bad not in E1_SENT, 'forbidden string: ' + bad
print('status closers in 054-057 block: %d (expected 1, at the end of 057)' % block.count(STATUS))
assert block.count(STATUS) == 1 and block.rstrip().endswith(STATUS)
print('\\ref uses in block: %s' % sorted(set(x.split('}')[0] for x in block.split('\\ref{')[1:])))
print('\\cite uses in block: %s' % sorted(set(x.split('}')[0] for x in block.split('\\cite{')[1:])))
assert '\\label' not in block
print('non-ASCII characters in block: %d' % sum(ord(c) > 127 for c in block))

def crlf(s):
    return (s.replace('\r\n', '\n').rstrip('\n') + '\n').replace('\n', '\r\n').encode('utf-8')

out = {'E1_053_sentence.r2.tex': E1_SENT, 'E2_insert_054_055.r2.tex': E2,
       'E3_056_adjusted.r2.tex': e056, 'E4_057_adjusted.r2.tex': e057}
for name, s in out.items():
    b = crlf(s)
    open(os.path.join(HERE, name), 'wb').write(b)
    print('%-26s %6d B  CRLF %3d  bare-LF %d  sha256 %s' % (name, len(b), b.count(b'\r\n'),
          b.count(b'\n') - b.count(b'\r\n'), sha(b)[:16]))

# ---------------- anchors in the current tree ----------------
cur = open(CUR, 'rb').read()
print('current appH: %d B  CRLF %d  bare-LF %d  sha256 %s' % (len(cur), cur.count(b'\r\n'),
      cur.count(b'\n') - cur.count(b'\r\n'), sha(cur)[:16]))
A1 = E1_OLD_053.encode()
A2 = b'Problem~E stays open with Assumption~\\ref{ass:lorentzian} retained.\r\n\r\n\\paragraph{Status.}\r\nRemains Assumption~\\ref{ass:lorentzian}.\r\n'
print('anchor A1 (053 closer, E1) count: %d' % cur.count(A1))
print('anchor A2 (end of Problem E ledger before Status, E2-E4) count: %d' % cur.count(A2))
assert cur.count(A1) == 1 and cur.count(A2) == 1
assert b'Exponential observables' not in cur and b'Slice bridge band' not in cur, 'inserts already present'

if '--apply-to' in sys.argv:
    d = sys.argv[sys.argv.index('--apply-to') + 1]
    assert not os.path.abspath(d).startswith(ROOT), 'apply target must be outside the repository'
    new = cur.replace(A1, E1_NEW_053.encode())
    head = b'Problem~E stays open with Assumption~\\ref{ass:lorentzian} retained.\r\n\r\n'
    tail = b'\\paragraph{Status.}\r\nRemains Assumption~\\ref{ass:lorentzian}.\r\n'
    ins = crlf(E2) + b'\r\n' + crlf(e056) + b'\r\n' + crlf(e057) + b'\r\n'
    new = new.replace(A2, head + ins + tail)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'appH-microscopic-proofs.tex'), 'wb').write(new)
    print('applied copy: %d B  CRLF %d  bare-LF %d  sha256 %s' % (len(new), new.count(b'\r\n'),
          new.count(b'\n') - new.count(b'\r\n'), sha(new)[:16]))
print('BUILD_R2 OK')
