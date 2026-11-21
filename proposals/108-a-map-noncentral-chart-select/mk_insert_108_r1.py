# mk_insert_108_r1.py -- writes insert-r1.tex (one paragraph line, CRLF-terminated)
# into this proposal folder only. Writes nothing else.
import io, hashlib

PARA = (
    r"\paragraph{Scalarity dichotomy and noncentral condensate selection of the leaf bivector.} "
    r"Let \hat X^I be self-adjoint coordinate operators generating a unital operator algebra, and call "
    r"\(\Theta^{IJ}_\omega:=-\mathrm i\,\omega([\hat X^I,\hat X^J])\), indexed by normalized states \(\omega\), "
    r"the state-induced bivector. This datum is independent of the state if and only if every commutator "
    r"\([\hat X^I,\hat X^J]\) is scalar; in finite dimension the trace forces such a scalar to vanish, so the "
    r"centrality mechanism of the constant-\(\Theta\) chart-blindness is exactly the scalar case of the dichotomy, "
    r"and every finite-\(N\) matrix regularization with noncommuting coordinates realizes the complement: the "
    r"commutator is traceless, hence non-scalar, and the state-induced bivector has nontrivial spread over states "
    r"(block-local states in a direct sum of \(N=5\) and \(N=8\) 't Hooft blocks give distinct bivector values). "
    r"In the Lie-type class \([\hat X^I,\hat X^J]=\mathrm i\,c^{IJ}{}_K\hat X^K\), possibly with scalar terms, the "
    r"bivector of a state with one-point functions \(x^K=\omega(\hat X^K)\) equals \(c^{IJ}{}_Kx^K\), a derived "
    r"leaf-dependent bivector field: for the spin-\(j\) fuzzy sphere \(\hat X^i=\ell\hat J^i\) with "
    r"\([\hat X^1,\hat X^2]=\mathrm i\ell\hat X^3\), the bivector \(\Theta^{12}_\omega=\ell\,\omega(\hat X^3)\) "
    r"takes values spanning \([-\ell^2 j,\ell^2 j]\) over pure states, its coherent-state fluctuation has relative "
    r"width exactly \(1/\sqrt j\) about the mean bivector, and the exact Casimir identity "
    r"\(\hat X\cdot\hat X=\ell^2 j(j+1)\mathbb 1\) fixes the leaf radius, the bivector field being the "
    r"Kirillov--Kostant--Souriau field of that orbit. Where the derived bivector field is nondegenerate on the "
    r"leaf, the set of chart 1-jets carrying it to the constant ambient bivector is a single orbit of the "
    r"symplectic group (dimension \(10\) at leaf dimension \(4\)): the bivector field supplies the gauge-invariant "
    r"content of the semiclassical-chart 1-jet, with the bivector-automorphism group (\(\mathfrak{so}(3)\), "
    r"dimension \(3\), for the fuzzy sphere) as the residual gauge. Where it is degenerate (rank \(2\) at the "
    r"poles of the fuzzy sphere, and at every point of any four-coordinate embedding), rank invariance under frame "
    r"change blocks this supply, and characteristic-direction data beyond the bivector are required. These are "
    r"exact linear-algebraic and \(\mathfrak{su}(2)\)-representation identities with explicit finite-dimensional "
    r"matrix computations; they do not compute the order-\(\Theta^2\) correction selected in the Lie-type class, "
    r"they do not determine whether a derived bivector germ fixes the embedding 2-jet within the "
    r"\(20\)-dimensional fiber of embedding 2-jets at fixed bivector 1-jet, they do not cover generic "
    r"non-Lie-type condensates, and this paragraph does not close Problem~A."
)

body = PARA + "\r\n"
data = body.encode("utf-8")
with io.open("insert-r1.tex", "wb") as f:
    f.write(data)
print("insert-r1.tex bytes=%d sha256/16=%s CRLF=%d" % (
    len(data), hashlib.sha256(data).hexdigest()[:16], data.count(b"\r\n")))
