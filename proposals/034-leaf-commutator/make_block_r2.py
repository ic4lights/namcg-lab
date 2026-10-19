b = open('block-r1.tex', encoding='ascii', newline='').read().replace('\r\n', '\n')
def sub(old, new):
    global b
    assert b.count(old) == 1, old
    b = b.replace(old, new)
sub('correction of the preceding Landau model).}', 'supersession of the preceding Landau model).}')
sub('this is the commutator that the Jacobi identity forbids at the nilpotent order.', 'this commutator is inconsistent with the Jacobi identity at the nilpotent order with frozen coefficients.')
sub("(complex, \(1.5\%\) off in the real part). In four", "(complex, \(1.5\%\) off in the real part). The two-dimensional test validates the prescription for a central \(K\); the identification of the leaf field \(Y\) with the seam insertion \(P\) is conditional on the nilpotent order and the frozen first jet. In four")
sub("A finite, covariant, sign-definite Einstein--Hilbert coefficient does not emerge in this class.", "In the sampled per-centre-variable forms the tetrad part of the finite remainder is neither proportional to the form \(A\) nor sign-definite; the sign and covariance of the full finite remainder (tetrad, charge and cross parts) and of its window average over the centre variable were not tested, so no finite, covariant, sign-definite Einstein--Hilbert coefficient is obtained here.")
sub("the window average over the centre variable, the spectral", "the window average over the centre variable, the sign and covariance of the full finite remainder, the spectral")
open('block-r2.tex', 'w', encoding='ascii', newline='').write(b)
d = open('block-r2.tex','rb').read()
print('bytes', len(d), 'TAB', d.count(b'\t'), 'nonASCII', sum(c>127 for c in d), 'CR', d.count(b'\r'))
