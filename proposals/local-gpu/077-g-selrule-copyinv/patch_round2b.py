"""077 round-2b patches: s5 symbolic Qs construction, s2b eigvals, s6 threshold.

All replacements asserted unique; backups appended to the existing .round1.bak
chain by writing new .bak2 copies. Run: python -I
proposals/077-g-selrule-copyinv/patch_round2b.py
"""
import shutil
import os

D = os.path.dirname(os.path.abspath(__file__))


def patch(fname, pairs):
    path = os.path.join(D, fname)
    src = open(path, encoding="utf-8").read()
    bak = path + ".bak2"
    done = True
    for old, new in pairs:
        if new in src and old not in src:
            continue
        done = False
        n = src.count(old)
        assert n == 1, (fname, n, old[:60])
        src = src.replace(old, new, 1)
    if done:
        print("already patched:", fname)
        return
    if not os.path.exists(bak):
        shutil.copyfile(path, bak)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(src)
    print("patched:", fname)


# ---- s5: symbolic Qs must be built as the exact product -2i(U R^+ - R U^+)
s5_pairs = [
    (
        "        n = q * Nsym\n"
        "        Qs = sp.zeros(n, n)\n"
        "        for a in range(q):\n"
        "            for b in range(q):\n"
        "                # block(a,b) = -2i(|u)(z_b| - |z_b)(u|), u = e_0 (FULL z_b)\n"
        "                blk = sp.zeros(Nsym, Nsym)\n"
        "                for i in range(Nsym):\n"
        "                    for j in range(Nsym):\n"
        "                        ui = 1 if i == 0 else 0\n"
        "                        uj = 1 if j == 0 else 0\n"
        "                        blk[i, j] = -2 * sp.I * (ui * sp.conjugate(zc[b][j])\n"
        "                                                 - zc[b][i] * uj)\n"
        "                Qs[a * Nsym:(a + 1) * Nsym, b * Nsym:(b + 1) * Nsym] = blk",
        "        n = q * Nsym\n"
        "        U = sp.zeros(n, q)\n"
        "        Rm = sp.zeros(n, q)\n"
        "        for a in range(q):\n"
        "            U[a * Nsym, a] = 1                        # u = e_0 per copy\n"
        "            for i in range(Nsym):\n"
        "                for cb in range(q):\n"
        "                    Rm[a * Nsym + i, cb] = zc[cb][i]  # R_{xy} = z_y\n"
        "        Qs = -2 * sp.I * (U * Rm.adjoint() - Rm * U.adjoint())",
    ),
    (
        "(v) Lemma 2's two-copy classification solved the t^1 condition for beta2,",
        "(vi) the symbolic Q~ was built blockwise as -2i(|u)(z_col| - |z_col)(u|),\n"
        "      which is NOT of the form -2i(U R^+ - R U^+) (the product puts the\n"
        "      TRANSPOSED block on the ket side); the ROUND-2 object was\n"
        "      non-Hermitian (debug_conventions.py Part 2: max|Q-Q^H| = 5.29 at one\n"
        "      random z), so the Lemma 1(a) failure was the CHECK, not the lemma.\n"
        "      Q~ is now built as the exact product -2i(U R^+ - R U^+) with\n"
        "      block-equal R columns (numerically the spectrum identity holds to\n"
        "      4.4e-15: debug_conventions.py Part 2).\n"
        "(vii) the numpy U used np.kron(I_q, e_0-as-1d-row), which numpy pads to a\n"
        "      (q, qN) matrix; now e_0 as a column (qN, q).\n"
        "(v) Lemma 2's two-copy classification solved the t^1 condition for beta2,",
    ),
]

# ---- s2b: T is non-Hermitian; eigvalsh read the wrong triangle (round-1 z0
#      failure dev 5.12e+02). Also record the verified copy convention.
s2b_pairs = [
    (
        "def stats_from_eigs(ev, q):",
        "def eigsT(Tm):\n"
        "    # T is generally NOT Hermitian (it is -2i S (NM) S, S = diag(I,-I), a\n"
        "    # product whose factors carry Q~'s nonzero spectrum); eigvalsh would\n"
        "    # read only one triangle - use eigvals and bound the imaginary part.\n"
        "    ev = np.linalg.eigvals(Tm)\n"
        "    assert np.abs(ev.imag).max() < 1e-8 * max(1.0, np.abs(ev).max())\n"
        "    return np.sort(ev.real)\n\n\n"
        "def stats_from_eigs(ev, q):",
    ),
    (
        "    e1 = np.sort(np.linalg.eigvalsh(Ql))\n"
        "    e2 = np.sort(np.linalg.eigvalsh(Tmat_from_z(z, u, q_)))",
        "    e1 = np.sort(np.linalg.eigvalsh(Ql))\n"
        "    e2 = eigsT(Tmat_from_z(z, u, q_))",
    ),
    (
        "    def Dz():\n"
        "        zz = sample_z(u, Vm, q_, M, sig)\n"
        "        ev = np.linalg.eigvalsh(Tmat_from_z(zz, u, q_))",
        "    def Dz():\n"
        "        zz = sample_z(u, Vm, q_, M, sig)\n"
        "        ev = eigsT(Tmat_from_z(zz, u, q_))",
    ),
    (
        "        for _ in range(10):\n"
        "            zz = sample_z(u, Vm, q, M, sig)\n"
        "            ev = np.linalg.eigvalsh(Tmat_from_z(zz, u, q))",
        "        for _ in range(10):\n"
        "            zz = sample_z(u, Vm, q, M, sig)\n"
        "            ev = eigsT(Tmat_from_z(zz, u, q))",
    ),
    (
        "    for _ in range(8):\n"
        "        zz = sample_z(u, Vm, q, M, sig)\n"
        "        ev = np.linalg.eigvalsh(Tmat_from_z(zz, u, q))",
        "    for _ in range(8):\n"
        "        zz = sample_z(u, Vm, q, M, sig)\n"
        "        ev = eigsT(Tmat_from_z(zz, u, q))",
    ),
    (
        "Run: python -I proposals/077-g-selrule-copyinv/s2b_qwindow.py [--full]",
        "ROUND 2: (z0) failed in round 1 (dev 5.12e+02) because eigvalsh was applied\n"
        "to the non-Hermitian T; now eigvals with an imaginary-part bound. The z ->\n"
        "R copy-block convention R_{xy} = w_{xy} (= z[(x,y)]) used by Tmat_from_z is\n"
        "verified by the matrix identity max|Q~ - (-2i(U R^+ - R U^+))| = 7.9e-14\n"
        "(debug_conventions.py Part 1).\n"
        "Run: python -I proposals/077-g-selrule-copyinv/s2b_qwindow.py [--full]",
    ),
]

# ---- s6: (c) threshold encoded a wrong qualitative claim (O(1) violation);
#      the data show a subleading M^(-1/2) violation, far above tiling level.
s6_pairs = [
    (
        "  (c) DIRECT: block-diagonal 2-copy charges with matched-scale row data and\n"
        "      iid Im alpha: the exact mult-2 D statistic is O(1) at every N\n"
        "      (Im-alpha mismatch kills EXACT tiling: no state family inside the\n"
        "      tested class achieves exact tiling by norms alone), while the\n"
        "      leading-order signature U_2 - 1 = O(1/N) decays with slope ~ -1: the\n"
        "      Im-alpha column of the exact criterion is invisible at leading order.",
        "  (c) DIRECT: block-diagonal 2-copy charges with iid (matched-scale) row\n"
        "      data: the exact mult-2 D statistic NEVER approaches the exact-tiling\n"
        "      level (D_exact >= 0.05 at every N tested, >= 4e7 times the tiling\n"
        "      threshold 1e-12: no tested product family achieves exact tiling by\n"
        "      norms alone) but decays as M^(-1/2) with the |alpha|/|w| slope\n"
        "      (CORRECTED ROUND 2: round 1 asserted an O(1) level with threshold\n"
        "      > 0.3; measured D_exact 0.1317 -> 0.0536, slope -0.43): the Im-alpha\n"
        "      column kills EXACT tiling but is subleading, invisible at leading\n"
        "      order; the leading-order signature U_2 - 1 = O(1/N), slope ~ -1.",
    ),
    (
        "Run: python -I proposals/077-g-selrule-copyinv/s6_imalpha.py",
        "ROUND 2: the (c) assert min(rows_c1) > 0.3 encoded the wrong qualitative\n"
        "claim; corrected to non-tiling level (> 0.01) plus M^(-1/2) decay slope.\n"
        "Run: python -I proposals/077-g-selrule-copyinv/s6_imalpha.py",
    ),
    (
        "sC2 = slope(Ns, rows_c2)\n"
        "ok = (-0.8 < sA < -0.25) and (-0.8 < sB < -0.25) \\\n"
        "     and min(rows_c1) > 0.3 and (-1.6 < sC2 < -0.5)\n"
        "print('slopes: |alpha|/|w| %.3f ; rel-dev %.3f ; U_2-1 %.3f ; min D_exact %.3f'\n"
        "      % (sA, sB, sC2, min(rows_c1)))",
        "sC2 = slope(Ns, rows_c2)\n"
        "sC1 = slope(Ns, rows_c1)\n"
        "ok = (-0.8 < sA < -0.25) and (-0.8 < sB < -0.25) \\\n"
        "     and min(rows_c1) > 0.01 and (-0.8 < sC1 < -0.25) and (-1.6 < sC2 < -0.5)\n"
        "print('slopes: |alpha|/|w| %.3f ; rel-dev %.3f ; D_exact %.3f ; U_2-1 %.3f ; '\n"
        "      'min D_exact %.3f' % (sA, sB, sC1, sC2, min(rows_c1)))",
    ),
]

patch("s5_gram_and_q2_exact.py", s5_pairs)
patch("s2b_qwindow.py", s2b_pairs)
patch("s6_imalpha.py", s6_pairs)
print("PATCH2b DONE")
