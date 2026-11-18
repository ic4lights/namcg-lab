# Manifest, proposal 084-g-moments-coupledmixed, round 1

Generated 2026-11-18 after the final green re-run of all scripts (every script reproduces its
saved .out byte-for-byte, `python -I` from repo root).

## Folder contents (bytes, sha256 first 8)

    insert-r1.tex                2332  0a7396c4   single content line + terminal CRLF, UTF-8 no BOM
    proposal-r1.md              28463  cac06857   13 sections, 350 lines
    s1_coupled_map.py            2004  eab81c9b   mixed map + flip, m=1..9 (sympy)
    s1_coupled_map.out            615  24146d9a
    s2_induced_joint.py          3135  696b021a   exact rational Isserlis, 3 datasets (sympy)
    s2_induced_joint.out          476  1608792a
    s3_monte_carlo.py            2139  72fea1f7   MC D=6 N=6e5 seed 20261118 (numpy)
    s3_monte_carlo.out            735  1f271d0d
    s4_uniform_frame.py          1793  f2f7a215   Gamma = (W^2/D)(1/D_eff-1/D) exact rational
    s4_uniform_frame.out          513  731c031e
    simulate_apply_084.py        2016  3c4607bf   READ-ONLY splice simulation, writes nothing
    simulate_apply_084.out        172  cef814f1

## Dead work-in-progress register

First drafts of s2 (garbled Isserlis line), s3 (broken z-helper, broadcast bug) and s4 (float vs
rational identity) were superseded IN PLACE by rewrite or python byte-surgery; no orphan draft
files exist in this folder. The hashes above are the final, verified ones.

## Byte-contract lineage (appH-microscopic-proofs.tex), from the saved .out of each proposal

    081-g-edge-moments          POST 729152 / 5d52b672
    082-g-moments-uniformmin    PRE  729152 / 5d52b672  ->  POST 731183 / 956070af
    083-g-moments-aodd-sector   PRE  731183 / 956070af  ->  POST 733361 / c35bfed0  (CRLF 3832)
    084-g-moments-coupledmixed  PRE  733361 / c35bfed0  (live, re-verified this round)
                                expected POST 735695 / a13240a7  (CRLF 3834, bareLF 0)
                                close-idiom "close nothing in Problem~G." 11 -> 12

Splice rule: insert-r1.tex + one CRLF inserted immediately before the line-start
`\emph{Vacuum term.}` of Problem G (the G-side occurrence, pinned via the unique 083-tail
sentence; the Problem F occurrence near L3006 is not the anchor).

## Live PRE pins verified this round (read-only)

appH size 733361, sha c35bfed009668845a5ff313e0a35b3f48374cbc843ed85e9d4fedb2a936cedfd,
CRLF 3832, bareLF 0; 083-tail pin count 1; gap after tail == CRLFCRLF.
