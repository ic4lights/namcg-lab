# Manifest 092-g-profile-coordinate-transport, round 1

Insert: `insert-r1.tex`, 4,544 B, sha8 a39bcb33 (body in `insert-body.txt`, 4,542 B / sha8
3d424f0b, body + terminal CRLF = insert).

Integration contract (handback):

- PRE appH (re-measured live by `hygiene_092.py` and `simulate_apply_092.py`, both OK):
  760,528 B / sha256 46dbfb3f14d444b7e7046883e00e4c58d19847ab4b9ca37bd47a3f97e691811d /
  CRLF 3,846 / bareLF 0 / noun idiom 17 / verb idiom 1 / Vacuum-term 2.
- Splice PIN (count 1 live): 091 tail sentence `the matrix integral of the core action is not
  evaluated, no state is fixed, the missing steps of the Missing step paragraph are unchanged,
  and they close nothing in Problem~G.` + CRLFCRLF + line-start `\emph{Vacuum term.}`.
- Splice operation: insert bytes + one extra CRLF immediately before the G-side
  `\emph{Vacuum term.}` line (same convention as integrations 20-22; PRE + insert + 2 bytes).
- POST (computed by `simulate_apply_092.py`, asserted there):
  sha256 b1b62410229383c112d3a50e7c47f0beccdb3835001858d01628b31736b3fd0e / 765,074 B /
  CRLF 3,848 / bareLF 0 / noun idiom 18 / verb idiom 1 / Vacuum-term 2 / new header
  `Transport of the profile coordinate` count 1. Outside the splice window the POST bytes are
  asserted identical to PRE.
- Header uniqueness swept across all `chapters/*.tex`: 0 hits pre-splice.
- Placement: G block, after L3195 (091 paragraph) and before the G-side Vacuum term line
  (L3197); sec:status-H stays at the section boundary below; no other passage touched.

File table (size B / sha8):

    file                        | size  | sha8
    ----------------------------+-------+---------
    hygiene_092.out             |  2033 | 9e5791da
    hygiene_092.py              |  4240 | cf47f499
    insert-body.txt             |  4542 | 3d424f0b
    insert-r1.tex               |  4544 | a39bcb33
    s1b_transport_group.out     |  1134 | e0a57dec
    s1b_transport_group.py      |  4578 | a6dd2d40
    s2_moment_map.out           |  1328 | 2d87dad7
    s2_moment_map.py            |  6381 | b5660f1e
    s3_mc_transport.out         |   592 | 38530a3b
    s3_mc_transport.py          |  4115 | e943c5f2
    s4_mean_map_d2.out          |   875 | 689310fa
    s4_mean_map_d2.py           |  3358 | dbabcad1
    simulate_apply_092.out      |   622 | bf014bb2
    simulate_apply_092.py       |  2752 | c8f2c13a
    smoke_compile_092.out       |   107 | 801401c0
    smoke_compile_092.py        |  1614 | fc21075b

Notes:
- The superseded first `s1_transport_group.py` (general-D symbolic determinants hung) was
  replaced by `s1b_transport_group.py` before submission and deleted; the shipped `.out` files
  all byte-match their script stdout (s1b re-run and byte-compared).
- `proposal-r1.md` written after this table's script rows were fixed; sizes of scripts and
  outputs stable since last runs.
- All scripts read-only outside this folder; `simulate_apply_092.py` performs no write.
