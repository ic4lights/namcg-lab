# Manifest for proposals/097-g-nonbridge-hetero-variance (round 2)

Integration artifact: insert-r2.tex only. insert-r1.tex must never be integrated.

- `gen_insert_097.py` | 7032 B | sha256 c325ac8c89e732b43bda1495ab8b51919f473019e69f0e79f1ded78422a485d6 | generator r1 | kept (historical provenance of insert-r1.tex)
- `gen_insert_097_r2.py` | 2338 B | sha256 4cd6998d70b5f201670c2536edc24bf6563d2fc7dfde8032f3dc323239072324 | byte surgery r1->r2 + diff proof | live
- `gen_manifest_097_r2.py` | 2353 B | sha256 b2d015df0d9e85bc482857c551e7d13e1cc35d33eab143be7a3ddf0ec1eb305d | manifest r2 generator | live
- `gen_scripts_097_r2.py` | 1333 B | sha256 035c74ccf75438daed84ecd8458cdb7ffe53d973710a93166f60c480fca02c15 | derives r2 check scripts from r1 bytes | live
- `hygiene_097.out` | 493 B | sha256 299ee8a2e44acc8066bd008087f7d32139467d141608f377d0ed4b647e8a5531 | hygiene r1 output | kept as record
- `hygiene_097.py` | 2693 B | sha256 4e14c61f3298fb3660aac81f9759bc6a6e00cbe0edd7747026c774f6b25accd7 | hygiene r1 | kept (source of r2 derivative)
- `hygiene_097_r2.out` | 573 B | sha256 9e80647bd30b1f651ed91a8918f82a3c3f862503b1d8c41ebedee61f6fbe0a34 | hygiene r2 output | live
- `hygiene_097_r2.py` | 2934 B | sha256 eb45243200335235369811b4d821b4184a768c912614234a7f3a8542ca01514b | hygiene r2 (24 checks) | live
- `insert-r1.tex` | 5373 B | sha256 e3cc6a01b73b826661d91ee92961356d6d1b3b7c390c045b8cb5c9e05e03a761 | insert round 1 | SUPERSEDED, never integrate
- `insert-r2.tex` | 5420 B | sha256 312fdcb188610089bf33d89bd438efe94dc6ad4533f33591fe28d39345514b59 | SOLE INTEGRATION ARTIFACT | live
- `manifest.md` | 1590 B | sha256 7e01b9b69f8a2fc19d7fac30ff04a1f88da5a6c020e992fdd6c53d5705fb91bc | manifest r1 | SUPERSEDED by manifest_r2.md
- `proposal-r1.md` | 25513 B | sha256 e05e8811706f450eb2af6ac638204a6c7df06b80ee7f5bf0e12a2dcc508adbbf | proposal round 1 | SUPERSEDED by proposal-r2.md (kept as record)
- `proposal-r2.md` | 10479 B | sha256 c98023e66db5da9614210f2cdfa44e5d4216db64a43b9a3d77cd1fe8e75799a8 | proposal round 2 (this package) | live
- `review-r1.md` | 15893 B | sha256 12e3a9f2fa9b9a1071a0f4ae197f666f1bf5ceee4e6b0d113764e8535a11ad71 | gatekeeper review round 1 | live input record
- `simulate_apply_097.out` | 134 B | sha256 269fa7affa5ab3289447cee383a9ab8ac23de7cc84beee54fecbbf6d47dbf3f4 | splice sim r1 output | kept as record (superseded POST)
- `simulate_apply_097.py` | 2566 B | sha256 1cf54de4ebea9ee6d07eac90a52f102ae80f4dfe63b9b85bbbd96a2ca6e271e5 | splice sim r1 | kept (source of r2 derivative)
- `simulate_apply_097_r2.out` | 134 B | sha256 734528c9d1fc0f24c8f1237fb071847d370a7cd6a79b29debf7f11609320adc6 | splice sim r2 output | live
- `simulate_apply_097_r2.py` | 2566 B | sha256 55773dec8918648cda65a201e312d44e107023a9af1506c9284f433e3fe5cffb | splice sim r2 (assert-only, no writes) | live
- `verify_097.out` | 506 B | sha256 fc6e409952bbdca3cdb5076724212fb55754f731816ae3097c960c0f3d50870b | verify r1 output | live, re-run r2 byte-identical (cmp SAME)
- `verify_097.py` | 6811 B | sha256 0e74cbeb57a78f3cf491fade5c6703d1c962a117dd4be6c73a6f366d3afa8dde | math verification (21 checks) | live, UNCHANGED since r1
