# mk_insert_107.py -- writes proposals/107-a-map-chart-condensate-selection/insert-r1.tex
# as EXACTLY one ASCII line terminated by CRLF (byte control via script, not the editor).
import hashlib
import sys

LINE = (r"\paragraph{Chart-blindness of the constant-\(\Theta\) symbol map and the reach of"
        r" matrix selection at order \(\Theta^2\).} Within the constant-\(\Theta\) Abelian class"
        r" the Weyl symbol map and its finite-\(N\) Weyl-ordered realization carry no"
        r" semiclassical-chart datum: the map's own datum is the constant bivector plus an"
        r" ordering convention, and the ordering is a gauge. Concretely, the Weyl-ordered mode"
        r" product of the finite-\(N\) torus pair differs from the left-ordered mode product by"
        r" the coboundary of the quadratic mode phase \(e^{i\Theta m n/2}\), its commutator"
        r" coefficient is the exact \(-2i\sin(\Theta\sigma/2)\) in the symplectic pairing"
        r" \(\sigma\), equal to the constant-\(\Theta\) Moyal bracket and differing from the"
        r" Poisson bracket first at order \(\Theta^3\), and its structure constants depend on the"
        r" mode labels and \(\Theta\) only. Since the commutator is central, every state of the"
        r" fixed Heisenberg algebra has the same constant effective bivector, so states and"
        r" condensates of the fixed algebra induce no leaf dependence. Combining with the pullback"
        r" selection: at a fixed closed bivector 1-jet the solutions of the coboundary equation"
        r" reachable from the model product form exactly the image of the embedding 2-jet, an"
        r" affine 20-dimensional subspace of the 36-dimensional kernel freedom, and the remaining"
        r" 16 kernel directions are invisible to every order-\(\Theta^2\) datum of the class."
        r" Hence within the stated class no matrix-side object -- symbol map, ordering convention,"
        r" trace pairing, state, or condensate -- resolves the semiclassical-chart selection;"
        r" chart-resolving data must come from outside the class, namely from noncentral"
        r" commutator (condensate) backgrounds or the Presentation-B vacuum correspondence. These"
        r" are exact algebraic facts for polynomial test data of degree \(\le 2\) at order"
        r" \(\Theta^2\) within the class stated here; they do not cover noncentral commutator"
        r" backgrounds, \(D>4\) submanifold embeddings, non-Abelian configurations, or orders"
        r" \(\Theta^3\) and higher, do not derive the dictionary assumption, and this paragraph"
        r" does not close Problem~A.")

out = LINE.encode("ascii") + b"\r\n"
assert b"\n" not in LINE.encode("ascii")
p = r"proposals\107-a-map-chart-condensate-selection\insert-r1.tex"
open(p, "wb").write(out)
print("wrote %s : %d bytes, sha256/16 %s, CRLF-terminated single line: %s"
      % (p, len(out), hashlib.sha256(out).hexdigest()[:16],
         out.endswith(b"\r\n") and out.count(b"\r\n") == 1))
sys.exit(0)
