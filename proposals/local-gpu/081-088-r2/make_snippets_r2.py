"""Write the CRLF snippets insert_r2.tex and closing_r2.tex of 081-088 r2 (UTF-8, no BOM).
Run: python -I proposals/local-gpu/081-088-r2/make_snippets_r2.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent

P1 = (r"\emph{Moments of the edge charge in the Gaussian rank-one class.} With \(a=\operatorname{Im}\alpha\) and \(r=|w_\perp|^{2}\) as in the Row length paragraph, the nonzero eigenvalues of the charge of a single cap are the roots of \(\lambda^{2}+4a\lambda-4r=0\), so that, pointwise, \(\operatorname{Tr}Q^{m}=(-1)^{m}2^{m+1}\sum_{k\le m/2}\binom{m}{2k}\sum_{j=0}^{k}\binom{k}{j}a^{m-2k+2j}r^{k-j}\) for every \(m\ge1\); for the two band-separated caps of one axis, and for the direct sum of the two-component paragraph with momenta without entries between the summands, the moment sequences add (exact). "
      r"Reversing the sign of the momenta sends \(Q\) to \(-Q\), so the odd moments average to zero in every state invariant under that reversal, and at \(a=0\) the even moments are \(2\ell^{2p}\), with \(\ell=2r^{1/2}\) the row length. "
      r"If \(r=s^{2}\sum_{i}g_{i}E_{i}\) with independent unit exponentials \(E_{i}\), a profile \(g=(g_{1},\dots,g_{D})\) of \(D\) slots and \(W=\sum_{i}g_{i}\), then \(\langle\ell^{2}\rangle=4s^{2}W\) and, at \(a=0\), the averaged \(2p\)-th moment is its single-row value \(2(4s^{2}W)^{p}\) times \(\rho_{p}(g)=p!\,h_{p}(g)/W^{p}=\sum_{\lambda\vdash p}(p!/z_{\lambda})\prod_{k\ge1}(s_{k}/W^{k})^{m_{k}}\), with \(h_{p}\) the complete homogeneous symmetric polynomial, \(s_{k}=\sum_{i}g_{i}^{k}\) and \(m_{k}\) the multiplicity of the part \(k\) in \(\lambda\); hence \(\rho_{2}-1=1/D_{\mathrm{eff}}\) with \(D_{\mathrm{eff}}=W^{2}/s_{2}\), \(\rho_{p}-1\ge\binom{p}{2}/D_{\mathrm{eff}}\), \(\rho_{p}\le p!\) with equality for \(p\ge2\) only when one slot carries all the weight, and \(\rho_{p}\ge\prod_{k=1}^{p-1}(1+k/D)\) with equality for \(p\ge2\) only at the uniform profile (exact). "
      r"In the Gaussian state of the Row length paragraph, as in every Gaussian state of the momenta invariant under conjugation by \(e^{\mathrm i\theta\,n\cdot J}\), the entries of the boundary row \(w\) in the eigenbasis of \(n\cdot J\) are independent circular complex Gaussians, since distinct entries carry distinct charges under that rotation; so \(a\) is independent of \(r\), \(r\) has the form above with \(s^{2}g_{i}\) the variances of the entries other than the one at \(u\), and \(\langle\operatorname{Tr}Q^{2}\rangle\) is \(8s^{2}\) times the full sum over the boundary row inside the block (exact). "
      r"These variances vanish for entries more than \(l_c\) places from \(v\) in that eigenbasis, so at most \(l_c-1\) slots carry \(r\) and \(\rho_{2}-1\ge1/(l_c-1)\) for every \(N\) and \(M\) (exact); \(D_{\mathrm{eff}}=29.5\) at \(N=400\), \(M=N/2\), \(l_c=40\) and \(f=\nu l/2\) (numerical). "
      r"The reading of the rows from the edge data in the transplanted selection rule therefore matches the averaged charge moments exactly at the second moment, and beyond it only as \(D_{\mathrm{eff}}\to\infty\), which in this state requires \(l_c\to\infty\).")

P2 = (r"\emph{Coupled slots and laws of the edge vector.} For a Gaussian state without that invariance, write the boundary row in a basis of \(D\) slots in which \(\mathbb{E}\,w_{i}w_{j}^{*}=s^{2}g_{i}\delta_{ij}\), assume the slots circular, and set \(q_{i}=|u_{i}|^{2}\), \(W=\sum_{i}g_{i}\), \(\mu=\sum_{i}q_{i}g_{i}\) and \(\Gamma=\sum_{i}q_{i}(g_{i}-\mu)^{2}\). "
      r"Then \(\mathbb{E}\,a^{2}=s^{2}\mu/2\), \(\mathbb{E}\,ar=0\), \(\mathbb{E}\,a^{2}r-\mathbb{E}\,a^{2}\,\mathbb{E}\,r=s^{4}\Gamma/2\) and \(|(\mathbf 1-uu^{\dagger})Gu|^{2}=\Gamma\), with \(G=\operatorname{diag}(g)\), so \(a\) and \(r\) are independent if and only if \(\Gamma=0\), that is, if and only if \(g\) is constant on the support of \(u\), which holds in the preceding paragraph, where \(u\) is one slot; \(\langle\operatorname{Tr}Q^{2}\rangle=8s^{2}W\) for every \(u\), and \(\langle\operatorname{Tr}Q^{4}\rangle\) exceeds its value for independent \(a\) and \(r\) with the same marginals by \(128s^{4}\Gamma\) (exact). "
      r"For a law \(\pi\) of \(u\) independent of \(g\), \(\mathbb{E}_{\pi}\Gamma=g^{T}\Sigma_{\pi}g\) with \(\Sigma_{\pi}=\mathbb{E}_{\pi}(\operatorname{diag}(q)-qq^{T})\) positive semidefinite and annihilating the constant profiles. "
      r"On the hyperplane \(\sum_{i}g_{i}=W\) the zero set, the minimiser set and the stationary set of \(\mathbb{E}_{\pi}\Gamma\) are the profiles constant on the components of the graph in which \(i\) and \(j\) are joined when \(\pi(q_{i}q_{j}>0)>0\); this is the uniform profile alone exactly when the graph is connected, as for the Haar law, for which \(\Sigma_{\pi}\) is \(1/(D+1)\) times the orthogonal projector onto the profiles of mean zero; and \(\mathbb{E}_{\pi}\Gamma\ge\lambda^{+}W^{2}(D_{\mathrm{eff}}^{-1}-D^{-1})\), with \(D_{\mathrm{eff}}=W^{2}/\sum_{i}g_{i}^{2}\) and \(\lambda^{+}\) the least eigenvalue of \(\Sigma_{\pi}\) on profiles of mean zero (exact). "
      r"The stationary set is unchanged under reparametrisations with nowhere-vanishing derivative and becomes that of the union of the graphs under positive combinations of laws, so no functional built in this way from averaged decoupling data selects a value of the profile within a component; a profile is fixed only by the state, which the State and coarse-graining paragraph leaves as a supplied input. "
      r"These two paragraphs fix no state, \(s\), \(g\) or edge vector.")

OLD_CLAUSE = r"and for Gaussian states with the stated variances or the stated momentum data."
NEW_CLAUSE = r"and for Gaussian states with the stated variances, the stated momentum data or the stated slot laws, with the stated laws of the edge vector."


def main():
    ins = (P1 + '\r\n\r\n' + P2 + '\r\n\r\n').encode('utf-8')
    (HERE / 'insert_r2.tex').write_bytes(ins)
    (HERE / 'clause_r2.txt').write_bytes((OLD_CLAUSE + '\r\n' + NEW_CLAUSE + '\r\n').encode('utf-8'))
    apph = (HERE.parents[2] / 'chapters' / 'appH-microscopic-proofs.tex').read_bytes()
    lines = apph.split(bytes([13, 10]))
    idx = [i for i, l in enumerate(lines) if l.startswith(b'These statements are for a compact factor with positive contraction; for a single projector')]
    assert len(idx) == 1
    old = lines[idx[0]]
    assert old.count(OLD_CLAUSE.encode()) == 1
    (HERE / 'closing_r2.tex').write_bytes(old.replace(OLD_CLAUSE.encode(), NEW_CLAUSE.encode()) + bytes([13, 10]))
    print('insert_r2.tex', len(ins), 'B; clause_r2.txt and closing_r2.tex written')


if __name__ == '__main__':
    main()
